#!/usr/bin/env python3
"""
sync.py — Incremental LeetCode → GitHub sync
=============================================
Designed to run inside GitHub Actions (or locally).
Reads the cookie from the LEETCODE_COOKIE env variable.

Usage:
    LEETCODE_COOKIE="..." python sync.py
    LEETCODE_COOKIE="..." python sync.py --readme-only
    LEETCODE_COOKIE="..." python sync.py --dry-run
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

# ─── Paths ─────────────────────────────────────────────────────
REPO_DIR   = Path(__file__).parent.resolve()
RAW_DIR    = REPO_DIR / ".raw_export"
META_FILE  = REPO_DIR / ".problems_meta.json"
SOL_DIR    = REPO_DIR / "solutions"

USERNAME   = "Bh4gav"
GQL        = "https://leetcode.com/graphql"

DIFF_EMOJI = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
LANG_LABEL = {
    "py":"Python","java":"Java","cpp":"C++","c":"C","cs":"C#",
    "js":"JavaScript","ts":"TypeScript","go":"Go","rs":"Rust",
    "rb":"Ruby","swift":"Swift","kt":"Kotlin","scala":"Scala",
    "php":"PHP","sh":"Bash","dart":"Dart","sql":"SQL","html":"HTML",
}

# ─── Auth ───────────────────────────────────────────────────────
def get_cookie() -> str:
    cookie = os.environ.get("LEETCODE_COOKIE", "").strip()
    if not cookie:
        sys.exit("❌  Set LEETCODE_COOKIE env variable.")
    return cookie

def get_session(cookie: str) -> requests.Session:
    s = requests.Session()
    csrf = next(
        (p.split("=",1)[1] for p in cookie.split(";") if p.strip().startswith("csrftoken=")), ""
    )
    s.headers.update({
        "Content-Type":"application/json","Referer":"https://leetcode.com",
        "x-csrftoken":csrf,"Cookie":cookie,"User-Agent":"Mozilla/5.0",
    })
    return s

# ─── GraphQL ────────────────────────────────────────────────────
def fetch_meta(session: requests.Session, slug: str) -> dict:
    q = """query q($s:String!){question(titleSlug:$s){
        questionFrontendId title difficulty topicTags{name}}}"""
    for _ in range(3):
        try:
            r = session.post(GQL, json={"query":q,"variables":{"s":slug}}, timeout=15)
            if r.status_code == 200:
                data = r.json().get("data",{}).get("question")
                if data: return data
        except Exception as e:
            print(f"    ⚠  retry [{slug}]: {e}")
        time.sleep(1.5)
    return {}

# ─── Parsing ────────────────────────────────────────────────────
def parse_folder(name:str) -> tuple[int,str]:
    m = re.match(r"^(\d+)-(.+)$", name)
    return (int(m.group(1)), m.group(2)) if m else (0, name)

def get_submission_date(pdir:Path) -> str:
    for f in sorted(pdir.iterdir(), reverse=True):
        if f.is_file() and re.match(r"^\d{4}-\d{2}-\d{2}", f.name):
            m = re.match(r"(\d{4}-\d{2}-\d{2})", f.name)
            if m: return m.group(1)
    return "Unknown"

def find_subs(pdir:Path) -> list[Path]:
    return [f for f in pdir.iterdir()
            if f.is_file() and re.match(r"^\d{4}-\d{2}-\d{2}", f.name)]

def html_to_md(html:str) -> str:
    if not html: return ""
    h = html
    h = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", h, flags=re.S)
    h = re.sub(r"<em>(.*?)</em>",   r"*\1*",  h, flags=re.S)
    h = re.sub(r"<code>(.*?)</code>",r"`\1`", h, flags=re.S)
    h = re.sub(r"<pre>(.*?)</pre>",
               lambda m:"\n```\n"+m.group(1).strip()+"\n```\n", h, flags=re.S)
    h = re.sub(r"<p[^>]*>(.*?)</p>",r"\1\n",  h, flags=re.S)
    h = re.sub(r"<li>(.*?)</li>",   r"- \1\n",h, flags=re.S)
    h = re.sub(r"<[^>]+>","",h)
    for e,r in [("&lt;","<"),("&gt;",">"),("&amp;","&"),
                ("&nbsp;"," "),("&#39;","'"),("&quot;",'"')]:
        h = h.replace(e,r)
    return re.sub(r"\n{3,}","\n\n",h).strip()

# ─── Export ─────────────────────────────────────────────────────
def run_export(cookie:str):
    print("📥  Running leetcode-export …")
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [sys.executable, "-m", "leetcode_export",
         "--cookies", cookie,
         "--folder", str(RAW_DIR),
         "--only-accepted",
         "--only-last-submission"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("  stderr:", result.stderr[-300:])
    print("  ✅  Export done")

# ─── Meta ───────────────────────────────────────────────────────
def load_meta() -> dict[str,dict]:
    if not META_FILE.exists(): return {}
    try:
        return {p["folder"]:p for p in json.loads(META_FILE.read_text())}
    except Exception: return {}

def save_meta(meta:dict[str,dict]):
    META_FILE.write_text(json.dumps(sorted(meta.values(), key=lambda x:x["num"]), indent=2))

# ─── Process new problems ────────────────────────────────────────
def process_new(session:requests.Session, existing:dict[str,dict]) -> list[dict]:
    raw_dirs = sorted(
        [p for p in RAW_DIR.iterdir() if p.is_dir() and not p.name.startswith(".")],
        key=lambda p: parse_folder(p.name)[0]
    )
    new = []
    for pdir in raw_dirs:
        num, slug = parse_folder(pdir.name)
        folder = f"{num:04d}_{slug}"
        if folder in existing: continue

        dest = SOL_DIR / folder
        dest.mkdir(parents=True, exist_ok=True)

        langs = []
        for sf in find_subs(pdir):
            ext = sf.suffix.lstrip(".")
            shutil.copy2(sf, dest / f"solution.{ext}")
            langs.append(ext)

        raw_md = next((f for f in pdir.iterdir() if f.is_file() and f.suffix==".md"), None)
        raw_text = raw_md.read_text(errors="replace") if raw_md else ""

        print(f"  🔍  {folder} …", end="", flush=True)
        meta = fetch_meta(session, slug)
        time.sleep(0.35)

        title = meta.get("title") or slug.replace("-"," ").title()
        diff  = meta.get("difficulty") or "Unknown"
        tags  = [t["name"] for t in (meta.get("topicTags") or [])]
        fid   = meta.get("questionFrontendId") or str(num)
        date  = get_submission_date(pdir)

        pm  = f"# {fid}. {title}\n\n"
        pm += f"**Difficulty:** {DIFF_EMOJI.get(diff,'')} {diff}  \n"
        pm += f"**Tags:** {', '.join(tags) or 'N/A'}  \n"
        pm += f"**Solved:** {date}  \n"
        pm += f"**LeetCode:** https://leetcode.com/problems/{slug}/\n\n---\n\n"
        pm += html_to_md(raw_text)
        (dest/"problem.md").write_text(pm)

        p = {"num":num,"fid":fid,"title":title,"slug":slug,
             "difficulty":diff,"tags":tags,"langs":sorted(set(langs)),
             "folder":folder,"solved_on":date}
        new.append(p)
        print(f"  ✅  [{diff}]  {title}  ({date})")
    return new

# ─── README ─────────────────────────────────────────────────────
def bar(n,total,l=22):
    if not total: return "░"*l
    f=round(n/total*l); return "█"*f+"░"*(l-f)

def generate_readme(problems:list[dict]):
    easy   = [p for p in problems if p["difficulty"]=="Easy"]
    medium = [p for p in problems if p["difficulty"]=="Medium"]
    hard   = [p for p in problems if p["difficulty"]=="Hard"]
    total  = len(problems)
    today  = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    lang_counts:dict[str,int]={}
    for p in problems:
        for l in p.get("langs",[]):
            lang_counts[l]=lang_counts.get(l,0)+1

    topic_stats:dict[str,dict]={}
    for p in problems:
        for t in p["tags"]:
            topic_stats.setdefault(t,{"Easy":0,"Medium":0,"Hard":0})
            topic_stats[t][p["difficulty"]]=topic_stats[t].get(p["difficulty"],0)+1

    def solved_key(p):
        d=p.get("solved_on","0000-00-00")
        return d if re.match(r"\d{4}-\d{2}-\d{2}",d) else "0000-00-00"
    recent = sorted(problems, key=solved_key, reverse=True)[:10]

    L=[]

    # Header
    L+=['<div align="center">',""
        ,"# 🚀 My LeetCode Journey",""
        ,f"*{total} problems solved · auto-synced via GitHub Actions*",""
        ,f"[![LeetCode](https://img.shields.io/badge/LeetCode-{USERNAME}-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/{USERNAME}/)"
        ,f"[![Auto-Sync](https://img.shields.io/badge/auto--sync-✓-4CAF50?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/Bhargava-Ram-Thunga/my_leetcode_journey/actions)",""
        ,f"![Solved](https://img.shields.io/badge/Solved-{total}-blueviolet?style=flat-square)"
        ,f"![Easy](https://img.shields.io/badge/Easy-{len(easy)}-brightgreen?style=flat-square)"
        ,f"![Medium](https://img.shields.io/badge/Medium-{len(medium)}-orange?style=flat-square)"
        ,f"![Hard](https://img.shields.io/badge/Hard-{len(hard)}-red?style=flat-square)",""
        ,"</div>","","---",""]

    # Stats card
    L+=['<div align="center">',""
        ,f"[![LeetCode Stats](https://leetcard.jacoblin.cool/{USERNAME}?theme=dark&font=Nunito&ext=heatmap)](https://leetcode.com/{USERNAME}/)",""
        ,"</div>","","---",""]

    # Progress
    L+=["## 📊 Progress","","```"
        ,f"  Easy    {len(easy):>4}  {bar(len(easy),total)}  {len(easy)/total*100:5.1f}%"
        ,f"  Medium  {len(medium):>4}  {bar(len(medium),total)}  {len(medium)/total*100:5.1f}%"
        ,f"  Hard    {len(hard):>4}  {bar(len(hard),total)}  {len(hard)/total*100:5.1f}%"
        ,f"  ────────────────────────────────────────"
        ,f"  Total   {total:>4}  {'█'*22}  100.0%"
        ,"```","","---",""]

    # Languages
    badges=" ".join(
        f"![{LANG_LABEL.get(l,l)}](https://img.shields.io/badge/{LANG_LABEL.get(l,l).replace('+','%2B').replace(' ','-')}-{c}-informational?style=flat-square)"
        for l,c in sorted(lang_counts.items(),key=lambda x:-x[1])
    )
    L+=["## 🛠️ Languages Used","",badges,"","---",""]

    # Recent activity
    L+=["## 🕐 Recent Activity",""
        ,"| Date | # | Title | Difficulty |"
        ,"|:----:|:-:|:------|:----------:|"]
    for p in recent:
        diff=f"{DIFF_EMOJI.get(p['difficulty'],'')} {p['difficulty']}"
        L.append(f"| {p.get('solved_on','—')} | {p['fid']} | [{p['title']}](solutions/{p['folder']}/) | {diff} |")
    L+=["","---",""]

    # Topic breakdown
    L+=["## 🏷️ Topics","","<details>","<summary><b>Browse all topics →</b></summary>",""
        ,"| Topic | Easy | Medium | Hard | Total |"
        ,"|:------|:----:|:------:|:----:|:-----:|"]
    for tag in sorted(topic_stats.keys()):
        c=topic_stats[tag]; tot=sum(c.values())
        L.append(f"| {tag} | {c.get('Easy',0)} | {c.get('Medium',0)} | {c.get('Hard',0)} | **{tot}** |")
    L+=["","</details>","","---",""]

    # All solutions table (collapsible)
    L+=["## 📋 All Solutions","","<details>"
        ,f"<summary><b>View all {total} solutions →</b></summary>",""
        ,"| # | Title | Difficulty | Language | Solved | Topics |"
        ,"|:-:|:------|:----------:|:--------:|:------:|:-------|"]
    for p in problems:
        diff=f"{DIFF_EMOJI.get(p['difficulty'],'')} {p['difficulty']}"
        langs=" · ".join(f"`{LANG_LABEL.get(l,l)}`" for l in p.get("langs",[]))
        tags_str=", ".join(p["tags"][:3])+("…" if len(p["tags"])>3 else "")
        L.append(f"| {p['fid']} | [{p['title']}](solutions/{p['folder']}/) | {diff} | {langs} | {p.get('solved_on','—')} | {tags_str} |")
    L+=["","</details>","","---",""]

    # Footer
    L+=['<div align="center">',""
        ,f"*🤖 Auto-synced every 12h · Last updated: {today}*",""
        ,"</div>",""]

    (REPO_DIR/"README.md").write_text("\n".join(L))
    print("  📝  README.md written")

def generate_progress(problems:list[dict]):
    easy  =[p for p in problems if p["difficulty"]=="Easy"]
    medium=[p for p in problems if p["difficulty"]=="Medium"]
    hard  =[p for p in problems if p["difficulty"]=="Hard"]
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    ts:dict[str,dict]={}
    for p in problems:
        for t in p["tags"]:
            ts.setdefault(t,{"Easy":0,"Medium":0,"Hard":0})
            ts[t][p["difficulty"]]=ts[t].get(p["difficulty"],0)+1

    n=len(problems)
    L=["# 📊 Progress Tracker",f"*Last updated: {today}*",""
       ,"## Overview",""
       ,"| | Count | % |","|:---|------:|--:|"
       ,f"| 🟢 Easy   | **{len(easy)}** | {len(easy)/n*100:.1f}% |"
       ,f"| 🟡 Medium | **{len(medium)}** | {len(medium)/n*100:.1f}% |"
       ,f"| 🔴 Hard   | **{len(hard)}** | {len(hard)/n*100:.1f}% |"
       ,f"| **Total** | **{n}** | 100% |","","## By Topic",""
       ,"| Topic | Easy | Medium | Hard | Total |"
       ,"|:------|:----:|:------:|:----:|:-----:|"]
    for tag in sorted(ts.keys()):
        c=ts[tag]; tot=sum(c.values())
        L.append(f"| {tag} | {c.get('Easy',0)} | {c.get('Medium',0)} | {c.get('Hard',0)} | **{tot}** |")

    (REPO_DIR/"PROGRESS.md").write_text("\n".join(L))
    print("  📊  PROGRESS.md written")

# ─── Git ────────────────────────────────────────────────────────
def git(args:list[str]) -> str:
    r=subprocess.run(["git"]+args,cwd=REPO_DIR,capture_output=True,text=True)
    if r.returncode!=0:
        print(f"  ⚠  git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout.strip()

def commit_and_push(n:int):
    if not git(["status","--porcelain"]):
        print("  ℹ️  Nothing to commit."); return
    git(["add","-A"])
    now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    msg=(f"✅ Add {n} new solution{'s' if n>1 else ''} [{now}]"
         if n>0 else f"📝 Refresh README [{now}]")
    git(["commit","-m",msg])
    git(["push"])
    print(f"  🚀  Pushed: {msg}")

# ─── Main ───────────────────────────────────────────────────────
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--readme-only",action="store_true")
    ap.add_argument("--dry-run",action="store_true")
    args=ap.parse_args()

    print(f"\n{'='*52}")
    print(f"  🚀 LeetCode Sync  —  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*52}\n")

    cookie  = get_cookie()
    existing= load_meta()
    print(f"  📂  Known: {len(existing)} problems")

    new_problems=[]
    if not args.readme_only:
        run_export(cookie)
        session=get_session(cookie)
        new_problems=process_new(session, existing)
        if new_problems:
            print(f"\n  🆕  {len(new_problems)} new problem(s)!")
            for p in new_problems: existing[p["folder"]]=p
            save_meta(existing)
        else:
            print("  ✅  All up to date.")

    all_problems=sorted(existing.values(), key=lambda x:x["num"])
    generate_readme(all_problems)
    generate_progress(all_problems)

    if not args.dry_run:
        commit_and_push(len(new_problems))
    else:
        print("  🔍  Dry run — skipping push")

    print(f"\n✅  Done!  Total: {len(all_problems)} problems\n")

if __name__=="__main__":
    main()
