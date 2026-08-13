#!/usr/bin/env python3
"""更新 README 最近活动区 (GitHub Actions 调用)"""
import json, urllib.request, re, os

token = os.environ.get("GITHUB_TOKEN", "")
def api(url):
    req = urllib.request.Request(url)
    req.add_header("Authorization", "token " + token)
    req.add_header("Accept", "application/vnd.github+json")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read())
    except Exception:
        return None

events = api("https://api.github.com/users/Hiloway/events/public?per_page=30") or []
lines = []
seen = set()
for ev in events:
    if ev.get("type") not in ("PushEvent", "CreateEvent", "PullRequestEvent", "IssuesEvent"):
        continue
    repo = ev.get("repo", {}).get("name", "")
    if not repo or repo in seen:
        continue
    seen.add(repo)
    ts = (ev.get("created_at") or "")[:10]
    et = ev["type"]
    if et == "PushEvent":
        n = len(ev.get("payload", {}).get("commits", []))
        lines.append(f"- 🔨 `{ts}` 推送 {n} 个提交到 [{repo}](https://github.com/{repo})")
    elif et == "CreateEvent":
        lines.append(f"- 🎉 `{ts}` 创建了 [{repo}](https://github.com/{repo})")
    elif et == "PullRequestEvent" and ev.get("payload", {}).get("action") == "opened":
        lines.append(f"- 🔀 `{ts}` 在 [{repo}](https://github.com/{repo}) 开启 PR")
    if len(lines) >= 5:
        break

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

block = "\n".join(lines) if lines else "*（暂无公开活动）*"
new_sec = "<!--START_SECTION:activity-->\n" + block + "\n<!--END_SECTION:activity-->"
readme = re.sub(r"<!--START_SECTION:activity-->.*?<!--END_SECTION:activity-->",
                new_sec, readme, flags=re.S)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
print(f"活动区已更新: {len(lines)} 条")
