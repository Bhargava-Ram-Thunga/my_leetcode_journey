# LeetCode → GitHub Sync — Chrome Extension

A Chrome extension that **automatically detects your LeetCode login** and syncs your session cookie to GitHub Actions — so your repo stays up to date without you touching anything.

## 🚀 Install (takes 60 seconds)

1. Open Chrome → `chrome://extensions/`
2. Enable **Developer Mode** (top-right toggle)
3. Click **"Load unpacked"** → select this folder (`cookie-sync-extension/`)
4. The extension icon will appear in your toolbar

## ⚙️ First-Time Setup

Click the extension icon and fill in:

| Field | Value |
|---|---|
| **GitHub PAT** | Go to [github.com/settings/tokens](https://github.com/settings/tokens/new) → Generate token with `repo` + `secrets` scopes |
| **Repo** | `Bhargava-Ram-Thunga/my_leetcode_journey` |
| **Auto-sync on login** | Toggle ON for fully automatic updates |

Click **Save Settings**.

## ✨ How It Works

```
You log into leetcode.com
         ↓
Extension detects LEETCODE_SESSION cookie change
         ↓  (automatically)
Option A — Auto-sync ON:   Updates GitHub secret instantly 🔒
Option B — Auto-sync OFF:  Shows notification + badge icon
                           Click "Copy gh Command" → paste in terminal
         ↓
GitHub Actions picks up the new cookie on next run
         ↓
Your new LeetCode solution is committed to the repo ✅
```

## 🔑 Getting Your GitHub PAT

1. Go to https://github.com/settings/tokens/new
2. Set name: `leetcode-sync`
3. Select scopes: ✅ `repo` (for secrets and workflow dispatch)
4. Copy the token → paste in extension settings

## 🍪 Cookie Expiry

LeetCode session cookies expire **every ~2 weeks**. Just log out and back in to LeetCode — the extension auto-detects the new cookie instantly.
