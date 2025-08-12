#!/usr/bin/env python3
import os, re, sys, datetime, requests

OWNER = os.getenv("GH_OWNER", "").strip()
TOKEN = os.getenv("GITHUB_TOKEN", "").strip()

HEAD_REPOS = "<!--START_SECTION:repos-->"
TAIL_REPOS = "<!--END_SECTION:repos-->"
HEAD_ACT = "<!--START_SECTION:activity-->"
TAIL_ACT = "<!--END_SECTION:activity-->"

if not OWNER or not TOKEN:
    print("Missing GH_OWNER or GITHUB_TOKEN", file=sys.stderr)
    sys.exit(1)

S = requests.Session()
S.headers.update({
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
})

def fetch_repos(owner, limit=6):
    url = f"https://api.github.com/users/{owner}/repos"
    r = S.get(url, params={"per_page": 100, "sort": "updated", "direction": "desc"}, timeout=30)
    r.raise_for_status()
    repos = [x for x in r.json() if not x.get("fork")]
    return repos[:limit]

def render_repos(repos):
    lines = []
    for repo in repos:
        name = repo["name"]
        url = repo["html_url"]
        desc = repo["description"] or ""
        stars = repo["stargazers_count"]
        updated = repo["updated_at"].replace("T"," ").replace("Z"," UTC")
        lines.append(f"- [{name}]({url}) — ⭐ {stars} — _updated: {updated}_\n  \n  {desc}")
    if not lines:
        lines = ["_No public repositories found._"]
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    return f"\n{os.linesep.join(lines)}\n\n_Last update: {ts}_\n"

def fetch_activity(owner, limit=10):
    url = f"https://api.github.com/users/{owner}/events/public"
    r = S.get(url, params={"per_page": limit}, timeout=30)
    r.raise_for_status()
    return r.json()

def render_activity(events):
    pretty = []
    for ev in events:
        et = ev["type"]
        repo = ev["repo"]["name"]
        when = ev["created_at"].replace("T"," ").replace("Z"," UTC")
        if et == "PushEvent":
            commits = [c["message"].splitlines()[0] for c in ev["payload"].get("commits", [])]
            msg = commits[0] if commits else "push"
            pretty.append(f"- ⬆️ Push to **{repo}** — _{when}_ — “{msg}”")
        elif et == "CreateEvent":
            ref = ev["payload"].get("ref_type", "repo")
            pretty.append(f"- 🆕 Created {ref} in **{repo}** — _{when}_")
        elif et == "IssuesEvent":
            action = ev["payload"].get("action", "issues")
            pretty.append(f"- 🐛 Issue {action} in **{repo}** — _{when}_")
        elif et == "PullRequestEvent":
            action = ev["payload"].get("action", "PR")
            pretty.append(f"- 🔀 PR {action} in **{repo}** — _{when}_")
        elif et == "WatchEvent":
            pretty.append(f"- ⭐ Starred **{repo}** — _{when}_")
        else:
            pretty.append(f"- 📌 {et} in **{repo}** — _{when}_")
    if not pretty:
        pretty = ["_No recent public activity._"]
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    return f"\n{os.linesep.join(pretty)}\n\n_Last update: {ts}_\n"

def replace_block(text, head, tail, new_block):
    pat = re.compile(rf"({re.escape(head)})(.*)({re.escape(tail)})", re.DOTALL)
    if pat.search(text):
        return pat.sub(rf"\1\n{new_block}\3", text)
    # si faltan marcadores, lo añadimos al final
    return text + f"\n\n{head}\n{new_block}{tail}\n"

def main():
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()

    repos = fetch_repos(OWNER, 6)
    activity = fetch_activity(OWNER, 10)

    new_repos = render_repos(repos)
    new_act = render_activity(activity)

    out = replace_block(readme, HEAD_REPOS, TAIL_REPOS, new_repos)
    out = replace_block(out, HEAD_ACT, TAIL_ACT, new_act)

    if out != readme:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(out)
        print("README updated.")
    else:
        print("No changes.")

if __name__ == "__main__":
    main()
