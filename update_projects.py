import requests

username = "ZimEthane"
url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=4"
res = requests.get(url)
repos = res.json()

table_header = "| Projet | Description | Langage |\n|---------|--------------|----------|"
rows = []
for r in repos:
    lang = r["language"] if r["language"] else "—"
    emoji = "📁"
    if lang.lower() == "php": emoji = "💻"
    elif lang.lower() == "java": emoji = "☕"
    elif lang.lower() in ["shell", "bash"]: emoji = "🐚⚙️"
    row = f"| [{r['name']}]({r['html_url']}) | {r['description'] or '—'} | {emoji} {lang} |"
    rows.append(row)

table_content = table_header + "\n" + "\n".join(rows)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start_tag = "<!-- PROJETS_RECENTS:START -->"
end_tag = "<!-- PROJETS_RECENTS:END -->"

before = content.split(start_tag)[0]
after = content.split(end_tag)[-1]

new_content = before + start_tag + "\n" + table_content + "\n" + end_tag + after

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
