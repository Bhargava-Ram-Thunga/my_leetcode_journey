// seal.js — BLAKE2b for crypto_box_seal nonce derivation
// Exposes: globalThis.computeSealNonce(ephPk, recipientPk) → Uint8Array(24)
//
// NaCl crypto_box_seal nonce = BLAKE2b(eph_pk || recipient_pk)[:24]
// BLAKE2b is not in Web Crypto API — this is a pure JS implementation (RFC 7693)
//
// Only supports input ≤ 128 bytes (sufficient: our input is always 64 bytes)

'use strict';

(function () {
  // ── BLAKE2b initialization vectors (same as SHA-512, LE uint32 pairs [lo, hi]) ──
  const IV = new Uint32Array([
    0xF3BCC908, 0x6A09E667,  // 0x6A09E667F3BCC908
    0x84CAA73B, 0xBB67AE85,  // 0xBB67AE8584CAA73B
    0xFE94F82B, 0x3C6EF372,  // 0x3C6EF372FE94F82B
    0x5F1D36F1, 0xA54FF53A,  // 0xA54FF53A5F1D36F1
    0xADE682D1, 0x510E527F,  // 0x510E527FADE682D1
    0x2B3E6C1F, 0x9B05688C,  // 0x9B05688C2B3E6C1F
    0xFB41BD6B, 0x1F83D9AB,  // 0x1F83D9ABFB41BD6B
    0x137E2179, 0x5BE0CD19,  // 0x5BE0CD19137E2179
  ]);

  // ── BLAKE2b message schedule (σ) ──────────────────────────────────────────────
  const SIGMA = new Uint8Array([
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,
    14,10, 4, 8, 9,15,13, 6, 1,12, 0, 2,11, 7, 5, 3,
    11, 8,12, 0, 5, 2,15,13,10,14, 3, 6, 7, 1, 9, 4,
     7, 9, 3, 1,13,12,11,14, 2, 6, 5,10, 4, 0,15, 8,
     9, 0, 5, 7, 2, 4,10,15,14, 1,11,12, 6, 8, 3,13,
     2,12, 6,10, 0,11, 8, 3, 4,13, 7, 5,15,14, 1, 9,
    12, 5, 1,15,14,13, 4,10, 0, 7, 6, 3, 9, 2, 8,11,
    13,11, 7,14,12, 1, 3, 9, 5, 0,15, 4, 8, 6, 2,10,
     6,15,14, 9,11, 3, 0, 8,12, 2,13, 7, 1, 4,10, 5,
    10, 2, 8, 4, 7, 6, 1, 5,15,11, 9,14, 3,12,13, 0,
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,
    14,10, 4, 8, 9,15,13, 6, 1,12, 0, 2,11, 7, 5, 3,
  ]);

  // ── blake2b(input, outlen) ────────────────────────────────────────────────────
  // 64-bit state stored as Uint32Array pairs: arr[i*2]=lo, arr[i*2+1]=hi
  function blake2b(input, outlen) {
    // Initialise h from IV, XOR parameter block word 0
    // Parameter block byte layout: [outlen, keylen=0, fanout=1, maxdepth=1, ...]
    // As uint32 LE: outlen | (0<<8) | (1<<16) | (1<<24)
    const h = new Uint32Array(16);
    for (let i = 0; i < 16; i++) h[i] = IV[i];
    h[0] = (IV[0] ^ outlen ^ (1 << 16) ^ (1 << 24)) >>> 0;

    // Pad input into a 128-byte block
    const block = new Uint8Array(128);
    block.set(input.subarray(0, Math.min(input.length, 128)));

    // Load message as 16 LE 64-bit words (32 uint32s)
    const m = new Uint32Array(32);
    for (let i = 0; i < 32; i++) {
      m[i] = (block[i*4] | (block[i*4+1] << 8) |
              (block[i*4+2] << 16) | (block[i*4+3] << 24)) >>> 0;
    }

    // Working variables v[0..15] = 16 × 64-bit words = 32 uint32s
    const v = new Uint32Array(32);
    for (let i = 0; i < 16; i++) v[i]    = h[i];   // v[0..7]  = h
    for (let i = 0; i < 16; i++) v[16+i] = IV[i];  // v[8..15] = IV

    // v[12] ^= byte counter (lo 32 bits; our input always fits in 32 bits)
    v[24] = (v[24] ^ (input.length >>> 0)) >>> 0;
    // v[14] ^= 0xFFFF...FFFF (last-block finalization flag)
    v[28] = (v[28] ^ 0xFFFFFFFF) >>> 0;
    v[29] = (v[29] ^ 0xFFFFFFFF) >>> 0;

    // 64-bit add: v[a] += [blo, bhi]
    function add64(a, blo, bhi) {
      const old = v[a * 2];
      v[a * 2]     = (old + blo) >>> 0;
      v[a * 2 + 1] = (v[a * 2 + 1] + bhi + (v[a * 2] < old ? 1 : 0)) >>> 0;
    }

    // BLAKE2b G mixing function (RFC 7693 §3.1)
    function G(a, b, c, d, xi, yi) {
      // v[a] += v[b] + m[xi]
      add64(a, v[b*2], v[b*2+1]);
      add64(a, m[xi*2], m[xi*2+1]);
      // v[d] = ROT64(v[d] ^ v[a], 32)  →  swap lo/hi
      v[d*2] ^= v[a*2]; v[d*2+1] ^= v[a*2+1];
      { const t = v[d*2]; v[d*2] = v[d*2+1]; v[d*2+1] = t; }

      // v[c] += v[d]
      add64(c, v[d*2], v[d*2+1]);
      // v[b] = ROT64(v[b] ^ v[c], 24)
      v[b*2] ^= v[c*2]; v[b*2+1] ^= v[c*2+1];
      { const lo = v[b*2], hi = v[b*2+1];
        v[b*2]   = ((lo >>> 24) | (hi << 8)) >>> 0;
        v[b*2+1] = ((hi >>> 24) | (lo << 8)) >>> 0; }

      // v[a] += v[b] + m[yi]
      add64(a, v[b*2], v[b*2+1]);
      add64(a, m[yi*2], m[yi*2+1]);
      // v[d] = ROT64(v[d] ^ v[a], 16)
      v[d*2] ^= v[a*2]; v[d*2+1] ^= v[a*2+1];
      { const lo = v[d*2], hi = v[d*2+1];
        v[d*2]   = ((lo >>> 16) | (hi << 16)) >>> 0;
        v[d*2+1] = ((hi >>> 16) | (lo << 16)) >>> 0; }

      // v[c] += v[d]
      add64(c, v[d*2], v[d*2+1]);
      // v[b] = ROT64(v[b] ^ v[c], 63)  →  rotate left by 1
      v[b*2] ^= v[c*2]; v[b*2+1] ^= v[c*2+1];
      { const lo = v[b*2], hi = v[b*2+1];
        v[b*2]   = ((lo << 1) | (hi >>> 31)) >>> 0;
        v[b*2+1] = ((hi << 1) | (lo >>> 31)) >>> 0; }
    }

    // 12 rounds of mixing
    for (let r = 0; r < 12; r++) {
      const s = r * 16;
      G(0, 4,  8, 12, SIGMA[s],    SIGMA[s+ 1]);
      G(1, 5,  9, 13, SIGMA[s+ 2], SIGMA[s+ 3]);
      G(2, 6, 10, 14, SIGMA[s+ 4], SIGMA[s+ 5]);
      G(3, 7, 11, 15, SIGMA[s+ 6], SIGMA[s+ 7]);
      G(0, 5, 10, 15, SIGMA[s+ 8], SIGMA[s+ 9]);
      G(1, 6, 11, 12, SIGMA[s+10], SIGMA[s+11]);
      G(2, 7,  8, 13, SIGMA[s+12], SIGMA[s+13]);
      G(3, 4,  9, 14, SIGMA[s+14], SIGMA[s+15]);
    }

    // Finalize: h[i] ^= v[i] ^ v[i+16]
    for (let i = 0; i < 16; i++) h[i] = (h[i] ^ v[i] ^ v[i + 16]) >>> 0;

    // Extract outlen bytes (little-endian from h)
    const out = new Uint8Array(outlen);
    for (let i = 0; i < outlen; i++) {
      out[i] = (h[Math.floor(i / 4)] >>> ((i % 4) * 8)) & 0xff;
    }
    return out;
  }

  // ── Public API ───────────────────────────────────────────────────────────────
  // computeSealNonce(ephPk: Uint8Array(32), recipientPk: Uint8Array(32)) → Uint8Array(24)
  // = BLAKE2b(eph_pk || recipient_pk, outlen=24)
  // This is exactly the nonce used by libsodium's crypto_box_seal.
  globalThis.computeSealNonce = function (ephPk, recipientPk) {
    const input = new Uint8Array(64);
    input.set(ephPk, 0);
    input.set(recipientPk, 32);
    return blake2b(input, 24);
  };
})();
