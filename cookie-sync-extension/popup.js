// popup.js

const $ = id => document.getElementById(id);

function showToast(msg) {
  const t = $("toast");
  t.textContent = msg;
  t.className = "show";
  setTimeout(() => t.className = "", 2600);
}

function timeAgo(iso) {
  if (!iso) return "Never";
  const diff = Math.floor((Date.now() - new Date(iso)) / 1000);
  if (diff < 60)  return `${diff}s ago`;
  if (diff < 3600) return `${Math.floor(diff/60)}m ago`;
  if (diff < 86400) return `${Math.floor(diff/3600)}h ago`;
  return new Date(iso).toLocaleDateString();
}

async function loadState() {
  // Load stored settings
  const settings = await chrome.storage.sync.get(["owner", "repo", "ghPat", "autoSync"]);
  if (settings.ghPat)   $("gh-pat").value = settings.ghPat;
  if (settings.repo)    $("gh-repo").value = settings.repo;
  if (settings.autoSync) $("auto-sync-toggle").checked = true;

  // Load local state (cookie, sync status)
  const local = await chrome.storage.local.get(["leetcodeCookie","cookieDetectedAt","synced","syncedAt"]);

  const cookieEl = $("cookie-status");
  const syncEl   = $("sync-status");
  const detEl    = $("detected-at");

  if (local.leetcodeCookie) {
    cookieEl.textContent = "✓ Detected";
    cookieEl.className = "status-value detected";
    $("btn-auto-sync").disabled = false;
    $("btn-copy-cmd").disabled  = false;
  } else {
    cookieEl.textContent = "Not detected";
    cookieEl.className = "status-value none";
    $("btn-auto-sync").disabled = true;
    $("btn-copy-cmd").disabled  = true;
  }

  if (local.synced && local.syncedAt) {
    syncEl.textContent = `✓ ${timeAgo(local.syncedAt)}`;
    syncEl.className = "status-value synced";
  } else if (local.leetcodeCookie) {
    syncEl.textContent = "Pending";
    syncEl.className = "status-value pending";
  }

  if (local.cookieDetectedAt) {
    detEl.textContent = timeAgo(local.cookieDetectedAt);
  }
}

// ── Auto-Update GitHub Secret ──────────────────────────────────
$("btn-auto-sync").addEventListener("click", async () => {
  const { leetcodeCookie } = await chrome.storage.local.get("leetcodeCookie");
  const settings = await chrome.storage.sync.get(["repo", "ghPat"]);

  if (!settings.ghPat || !settings.repo) {
    showToast("⚠️ Enter GitHub PAT and repo name first!");
    return;
  }
  if (!leetcodeCookie) {
    showToast("⚠️ No cookie detected. Log in to LeetCode first.");
    return;
  }

  const [owner, repo] = settings.repo.split("/");
  $("btn-auto-sync").textContent = "⏳ Updating…";
  $("btn-auto-sync").disabled = true;

  chrome.runtime.sendMessage(
    { type: "MANUAL_SYNC", owner, repo, ghPat: settings.ghPat, cookie: leetcodeCookie },
    (res) => {
      if (res && res.success) {
        showToast("✅ GitHub secret updated!");
        $("btn-auto-sync").textContent = "✅ Updated!";
        setTimeout(() => {
          $("btn-auto-sync").textContent = "⚡ Auto-Update GitHub Secret";
          $("btn-auto-sync").disabled = false;
          loadState();
        }, 2000);
      } else {
        showToast(`❌ Failed: ${res?.error || "unknown"}`);
        $("btn-auto-sync").textContent = "⚡ Auto-Update GitHub Secret";
        $("btn-auto-sync").disabled = false;
      }
    }
  );
});

// ── Copy gh Command ────────────────────────────────────────────
$("btn-copy-cmd").addEventListener("click", async () => {
  const { leetcodeCookie } = await chrome.storage.local.get("leetcodeCookie");
  const { repo } = await chrome.storage.sync.get("repo");

  if (!leetcodeCookie) {
    showToast("⚠️ No cookie detected. Log in to LeetCode first.");
    return;
  }

  const repoArg = repo ? `--repo ${repo}` : "--repo Bhargava-Ram-Thunga/my_leetcode_journey";
  const cmd = `gh secret set LEETCODE_COOKIE ${repoArg} --body '${leetcodeCookie}'`;

  try {
    await navigator.clipboard.writeText(cmd);
    showToast("📋 Copied! Paste in terminal to update the secret.");
  } catch {
    // Fallback: open a text area
    const el = document.createElement("textarea");
    el.value = cmd;
    document.body.appendChild(el);
    el.select();
    document.execCommand("copy");
    document.body.removeChild(el);
    showToast("📋 Copied! Paste in terminal.");
  }
});

// ── Trigger Sync Workflow ──────────────────────────────────────
$("btn-trigger").addEventListener("click", async () => {
  const settings = await chrome.storage.sync.get(["repo", "ghPat"]);
  if (!settings.ghPat || !settings.repo) {
    showToast("⚠️ Enter GitHub PAT and repo name first!");
    return;
  }

  const [owner, repo] = settings.repo.split("/");
  $("btn-trigger").textContent = "⏳ Triggering…";
  $("btn-trigger").disabled = true;

  chrome.runtime.sendMessage(
    { type: "TRIGGER_WORKFLOW", owner, repo, ghPat: settings.ghPat },
    (res) => {
      if (res && res.success) {
        showToast("🚀 Workflow triggered! Check GitHub Actions.");
        $("btn-trigger").textContent = "✅ Triggered!";
        setTimeout(() => {
          $("btn-trigger").textContent = "🔄 Trigger Sync Now";
          $("btn-trigger").disabled = false;
        }, 3000);
      } else {
        showToast(`❌ Failed: ${res?.error || "unknown"}`);
        $("btn-trigger").textContent = "🔄 Trigger Sync Now";
        $("btn-trigger").disabled = false;
      }
    }
  );
});

// ── Save Settings ──────────────────────────────────────────────
$("save-btn").addEventListener("click", async () => {
  const repoVal = $("gh-repo").value.trim();
  const patVal  = $("gh-pat").value.trim();
  const auto    = $("auto-sync-toggle").checked;

  let owner = "", repo = "";
  if (repoVal.includes("/")) {
    [owner, repo] = repoVal.split("/");
  }

  await chrome.storage.sync.set({ owner, repo: repoVal, ghPat: patVal, autoSync: auto });
  showToast("✅ Settings saved!");
});

// Init
loadState();
