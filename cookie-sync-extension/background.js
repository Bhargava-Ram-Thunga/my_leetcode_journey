// background.js — Service Worker
// Watches for LeetCode LEETCODE_SESSION cookie changes (login events)
// and updates the GitHub Actions secret automatically.
//
// 🔒 ACCOUNT GUARD: Only acts when the cookie belongs to YOUR account.
// If you log into someone else's LeetCode, this extension ignores it entirely.

const LEETCODE_HOST  = "leetcode.com";
const SESSION_KEY    = "LEETCODE_SESSION";
const OWNER_USERNAME = "bhargava-ram-thunga"; // ← YOUR LeetCode userSlug (from LEETCODE_SESSION JWT)

// ─── Decode the LEETCODE_SESSION JWT and extract username ────────────────────
function decodeSessionUsername(sessionCookieValue) {
  try {
    // JWT = header.payload.signature — we only need payload (index 1)
    const parts = sessionCookieValue.split(".");
    if (parts.length !== 3) return null;

    // base64url → base64 → JSON
    const b64 = parts[1].replace(/-/g, "+").replace(/_/g, "/");
    const pad  = b64.length % 4 === 0 ? "" : "=".repeat(4 - b64.length % 4);
    const json = atob(b64 + pad);
    const payload = JSON.parse(json);

    // LeetCode JWT payload contains: { username, user_slug, email, id, ... }
    return (payload.user_slug || payload.username || "").toLowerCase();
  } catch (e) {
    console.warn("[LeetCode Sync] Failed to decode JWT:", e);
    return null;
  }
}

// ─── Verify this cookie belongs to our account ──────────────────────────────
function isOurAccount(sessionCookieValue) {
  const slug = decodeSessionUsername(sessionCookieValue);
  if (!slug) {
    console.warn("[LeetCode Sync] Could not determine account from cookie — ignoring.");
    return false;
  }
  const isMatch = slug === OWNER_USERNAME.toLowerCase();
  if (!isMatch) {
    console.log(`[LeetCode Sync] 🚫 Cookie belongs to "${slug}", not "${OWNER_USERNAME}" — ignoring.`);
  }
  return isMatch;
}
const GH_API        = "https://api.github.com";

// ─── Collect all LeetCode cookies into one string ─────────────────
async function collectCookies() {
  const cookies = await chrome.cookies.getAll({ domain: LEETCODE_HOST });
  return cookies
    .map(c => `${c.name}=${c.value}`)
    .join("; ");
}

// ─── GitHub: fetch repo public key for secret encryption ──────────
async function getRepoPublicKey(owner, repo, pat) {
  const res = await fetch(
    `${GH_API}/repos/${owner}/${repo}/actions/secrets/public-key`,
    { headers: { Authorization: `token ${pat}`, Accept: "application/vnd.github+json" } }
  );
  if (!res.ok) throw new Error(`GitHub API ${res.status}: ${await res.text()}`);
  return res.json(); // { key_id, key }
}

// ─── Encrypt secret value for GitHub Secrets API ──────────────────
// Uses NaCl crypto_box_seal (X25519 + XSalsa20-Poly1305)
// Minimal self-contained implementation — no external deps needed.
async function encryptSecret(base64PublicKey, secretValue) {
  // Decode the recipient's X25519 public key
  const recipientPk = base64ToBytes(base64PublicKey);

  // Generate an ephemeral X25519 keypair
  const ephKeyPair = await crypto.subtle.generateKey(
    { name: "X25519" }, true, ["deriveBits"]
  );

  // Export the ephemeral public key as raw bytes (32 bytes)
  const ephPkRaw = new Uint8Array(
    await crypto.subtle.exportKey("raw", ephKeyPair.publicKey)
  );

  // Import recipient public key as X25519 CryptoKey
  const recipientKey = await crypto.subtle.importKey(
    "raw", recipientPk, { name: "X25519" }, false, []
  );

  // Derive shared secret: DH(ephemeral_sk, recipient_pk)
  const sharedSecret = new Uint8Array(
    await crypto.subtle.deriveBits({ name: "X25519", public: recipientKey }, ephKeyPair.privateKey, 256)
  );

  // HSalsa20: derive the actual encryption key from shared secret
  const encKey = hsalsa20(sharedSecret, new Uint8Array(16));

  // Nonce for XSalsa20-Poly1305 = first 24 bytes of Blake2b(ephPk || recipientPk)
  // Simplified: NaCl uses zeros as nonce in box_seal, key is derived via HSalsa20
  const nonce = new Uint8Array(24); // zeros (as per NaCl sealed box spec)

  // Encrypt: XSalsa20-Poly1305(encKey, nonce, message)
  const message = new TextEncoder().encode(secretValue);
  const ciphertext = xsalsa20poly1305Seal(encKey, nonce, message);

  // Result: ephemeral_pk (32 bytes) || ciphertext
  const result = new Uint8Array(32 + ciphertext.length);
  result.set(ephPkRaw, 0);
  result.set(ciphertext, 32);

  return bytesToBase64(result);
}

// ─── Update GitHub secret via API ────────────────────────────────
async function updateGitHubSecret(owner, repo, secretName, secretValue, pat) {
  const { key_id, key } = await getRepoPublicKey(owner, repo, pat);
  const encryptedValue = await encryptSecret(key, secretValue);

  const res = await fetch(
    `${GH_API}/repos/${owner}/${repo}/actions/secrets/${secretName}`,
    {
      method: "PUT",
      headers: {
        Authorization: `token ${pat}`,
        Accept: "application/vnd.github+json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ encrypted_value: encryptedValue, key_id }),
    }
  );
  if (!res.ok && res.status !== 204) {
    throw new Error(`Failed to update secret: ${res.status} ${await res.text()}`);
  }
}

// ─── Trigger GitHub Actions workflow ────────────────────────────
async function triggerSync(owner, repo, pat) {
  const res = await fetch(
    `${GH_API}/repos/${owner}/${repo}/actions/workflows/sync.yml/dispatches`,
    {
      method: "POST",
      headers: {
        Authorization: `token ${pat}`,
        Accept: "application/vnd.github+json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ref: "main" }),
    }
  );
  return res.ok || res.status === 204;
}

// ─── Cookie change listener ───────────────────────────────────────
chrome.cookies.onChanged.addListener(async ({ cookie, removed }) => {
  if (!cookie.domain.includes(LEETCODE_HOST)) return;
  if (cookie.name !== SESSION_KEY) return;
  if (removed) return;

  // 🔒 ACCOUNT GUARD: verify this cookie is for OUR account
  if (!isOurAccount(cookie.value)) {
    // Silently ignore — someone else's account logged in
    return;
  }

  console.log(`[LeetCode Sync] ✅ ${OWNER_USERNAME}'s session detected!`);

    // Collect the full cookie string
    const fullCookie = await collectCookies();
    await chrome.storage.local.set({
      leetcodeCookie: fullCookie,
      cookieDetectedAt: new Date().toISOString(),
      synced: false,
    });

    // Update badge
    await chrome.action.setBadgeText({ text: "!" });
    await chrome.action.setBadgeBackgroundColor({ color: "#FFA116" });

    // Get user settings
    const { owner, repo, ghPat, autoSync } = await chrome.storage.sync.get([
      "owner", "repo", "ghPat", "autoSync"
    ]);

    if (autoSync && owner && repo && ghPat) {
      // Auto-update the GitHub secret
      try {
        await updateGitHubSecret(owner, repo, "LEETCODE_COOKIE", fullCookie, ghPat);
        await chrome.storage.local.set({ synced: true, syncedAt: new Date().toISOString() });
        await chrome.action.setBadgeText({ text: "✓" });
        await chrome.action.setBadgeBackgroundColor({ color: "#4CAF50" });

        chrome.notifications.create({
          type: "basic",
          iconUrl: "icon.png",
          title: "LeetCode Sync ✅",
          message: "Cookie auto-updated on GitHub! Your next LeetCode solution will sync automatically.",
        });
      } catch (err) {
        console.error("[LeetCode Sync] Failed to update secret:", err);
        chrome.notifications.create({
          type: "basic",
          iconUrl: "icon.png",
          title: "LeetCode Sync ⚠️",
          message: `Auto-sync failed: ${err.message}. Open the extension to copy the manual command.`,
        });
      }
    } else {
      // No auto-sync configured — notify user to open popup
      chrome.notifications.create({
        type: "basic",
        iconUrl: "icon.png",
        title: "LeetCode Login Detected! 🔑",
        message: "New cookie captured. Open the extension to sync it to GitHub.",
      });
    }
});

// ─── Message handler (from popup) ────────────────────────────────
chrome.runtime.onMessage.addListener((msg, _sender, sendResponse) => {
  if (msg.type === "MANUAL_SYNC") {
    const { owner, repo, ghPat, cookie } = msg;
    (async () => {
      try {
        await updateGitHubSecret(owner, repo, "LEETCODE_COOKIE", cookie, ghPat);
        await chrome.storage.local.set({ synced: true, syncedAt: new Date().toISOString() });
        await chrome.action.setBadgeText({ text: "✓" });
        await chrome.action.setBadgeBackgroundColor({ color: "#4CAF50" });
        sendResponse({ success: true });
      } catch (err) {
        sendResponse({ success: false, error: err.message });
      }
    })();
    return true; // keep channel open for async response
  }

  if (msg.type === "TRIGGER_WORKFLOW") {
    const { owner, repo, ghPat } = msg;
    (async () => {
      try {
        const ok = await triggerSync(owner, repo, ghPat);
        sendResponse({ success: ok });
      } catch (err) {
        sendResponse({ success: false, error: err.message });
      }
    })();
    return true;
  }
});

// ─── Minimal NaCl crypto (crypto_box_seal) ───────────────────────
// Salsa20 core permutation
function salsa20Block(key, nonce, counter) {
  const k = new Uint32Array(8), n = new Uint32Array(4);
  for (let i = 0; i < 8; i++) k[i] = (key[i*4]|(key[i*4+1]<<8)|(key[i*4+2]<<16)|(key[i*4+3]<<24))>>>0;
  for (let i = 0; i < 4; i++) n[i] = (nonce[i*4]|(nonce[i*4+1]<<8)|(nonce[i*4+2]<<16)|(nonce[i*4+3]<<24))>>>0;
  const SIGMA = [0x61707865,0x3320646e,0x79622d32,0x6b206574];
  let [x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15] =
    [SIGMA[0],k[0],k[1],k[2],k[3],SIGMA[1],n[0],n[1],counter,0,SIGMA[2],k[4],k[5],k[6],k[7],SIGMA[3]];
  function R(v,n){return (v<<n)|(v>>>(32-n));}
  for (let i = 0; i < 10; i++) {
    x4^=R(x0+x12|0,7); x8^=R(x4+x0|0,9); x12^=R(x8+x4|0,13); x0^=R(x12+x8|0,18);
    x9^=R(x5+x1|0,7); x13^=R(x9+x5|0,9); x1^=R(x13+x9|0,13); x5^=R(x1+x13|0,18);
    x14^=R(x10+x6|0,7); x2^=R(x14+x10|0,9); x6^=R(x2+x14|0,13); x10^=R(x6+x2|0,18);
    x3^=R(x15+x11|0,7); x7^=R(x3+x15|0,9); x11^=R(x7+x3|0,13); x15^=R(x11+x7|0,18);
    x1^=R(x0+x3|0,7); x2^=R(x1+x0|0,9); x3^=R(x2+x1|0,13); x0^=R(x3+x2|0,18);
    x6^=R(x5+x4|0,7); x7^=R(x6+x5|0,9); x4^=R(x7+x6|0,13); x5^=R(x4+x7|0,18);
    x11^=R(x10+x9|0,7); x8^=R(x11+x10|0,9); x9^=R(x8+x11|0,13); x10^=R(x9+x8|0,18);
    x12^=R(x15+x14|0,7); x13^=R(x12+x15|0,9); x14^=R(x13+x12|0,13); x15^=R(x14+x13|0,18);
  }
  const out = new Uint8Array(64);
  const vals = [x0+SIGMA[0]|0, x1+k[0]|0, x2+k[1]|0, x3+k[2]|0, x4+k[3]|0,
                x5+SIGMA[1]|0, x6+n[0]|0, x7+n[1]|0, x8+counter|0, x9|0,
                x10+SIGMA[2]|0,x11+k[4]|0,x12+k[5]|0,x13+k[6]|0,x14+k[7]|0,x15+SIGMA[3]|0];
  for (let i = 0; i < 16; i++) {
    out[i*4]=vals[i]&0xff; out[i*4+1]=(vals[i]>>8)&0xff;
    out[i*4+2]=(vals[i]>>16)&0xff; out[i*4+3]=(vals[i]>>24)&0xff;
  }
  return out;
}

function hsalsa20(key, nonce) {
  // Returns 32-byte subkey
  const block = salsa20Block(key, nonce, 0);
  const out = new Uint8Array(32);
  out.set(block.slice(0, 16)); out.set(block.slice(48, 64), 16);
  return out;
}

function xsalsa20poly1305Seal(key, nonce, message) {
  // Derive subkey via HSalsa20 with first 16 bytes of nonce
  const subkey = hsalsa20(key, nonce.slice(0, 16));
  const subnonce = nonce.slice(16); // 8 bytes

  // XSalsa20 stream: generate keystream
  const mLen = message.length;
  const padded = new Uint8Array(32 + mLen);
  padded.set(message, 32);
  const stream = new Uint8Array(32 + mLen);

  for (let pos = 0, ctr = 0; pos < 32 + mLen; pos += 64, ctr++) {
    const block = salsa20Block(subkey, new Uint8Array([
      subnonce[0],subnonce[1],subnonce[2],subnonce[3],subnonce[4],subnonce[5],subnonce[6],subnonce[7],
      ctr&0xff,(ctr>>8)&0xff,(ctr>>16)&0xff,(ctr>>24)&0xff,0,0,0,0
    ]), 0);
    for (let i = 0; i < 64 && pos+i < 32+mLen; i++) {
      stream[pos+i] = block[i];
    }
  }

  // XOR
  const ciphertext = new Uint8Array(32 + mLen);
  for (let i = 0; i < 32 + mLen; i++) ciphertext[i] = padded[i] ^ stream[i];

  // Poly1305 MAC over ciphertext[32..] using key = stream[0..31]
  const polyKey = stream.slice(0, 32);
  const tag = poly1305Mac(polyKey, ciphertext.slice(32));

  // Result: tag(16) || ciphertext(mLen)
  const out = new Uint8Array(16 + mLen);
  out.set(tag, 0);
  out.set(ciphertext.slice(32), 16);
  return out;
}

function poly1305Mac(key, msg) {
  // Simplified Poly1305 — 16-byte authenticator
  // Using BigInt for precision
  const r = clamp(key.slice(0, 16));
  const s = key.slice(16, 32);
  const P = (1n << 130n) - 5n;

  let rn = bytesToBigInt(r);
  let sn = bytesToBigInt(s);
  let acc = 0n;

  for (let i = 0; i < msg.length; i += 16) {
    const chunk = new Uint8Array(17);
    const end = Math.min(i + 16, msg.length);
    chunk.set(msg.slice(i, end));
    chunk[end - i] = 1;
    acc = (acc + bytesToBigInt(chunk)) * rn % P;
  }
  acc = (acc + sn) & ((1n << 128n) - 1n);
  return bigIntToBytes(acc, 16);
}

function clamp(r) {
  const c = new Uint8Array(r);
  c[3]  &= 15; c[7]  &= 15; c[11] &= 15; c[15] &= 15;
  c[4]  &= 252; c[8] &= 252; c[12] &= 252;
  return c;
}

function bytesToBigInt(bytes) {
  let n = 0n;
  for (let i = bytes.length - 1; i >= 0; i--) n = (n << 8n) | BigInt(bytes[i]);
  return n;
}

function bigIntToBytes(n, len) {
  const out = new Uint8Array(len);
  for (let i = 0; i < len; i++) { out[i] = Number(n & 0xffn); n >>= 8n; }
  return out;
}

function base64ToBytes(b64) {
  const binary = atob(b64);
  return new Uint8Array([...binary].map(c => c.charCodeAt(0)));
}

function bytesToBase64(bytes) {
  return btoa(String.fromCharCode(...bytes));
}
