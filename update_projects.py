import requests

# 🔹 Paramètres
username = "ZimEthane"
repo_count = 4
api_url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page={repo_count}"

# 🔹 Récupération des dépôts
res = requests.get(api_url)
repos = res.json()

# 🔹 Génération du tableau Markdown
table_header = "| Projet | Description | Langage |\n|--------|-------------|---------|"
rows = []

for r in repos:
    lang = r["language"] if r["language"] else "—"

    # Émojis selon langage
    emoji = "📁"
    if lang.lower() == "php": emoji = "💻"
    elif lang.lower() == "java": emoji = "☕"
    elif lang.lower() in ["shell", "bash"]: emoji = "🐚⚙️"
    elif lang.lower() == "javascript": emoji = "🟨 JS"
    elif lang.lower() == "html": emoji = "🌐"
    elif lang.lower() == "c#": emoji = "🎯"

    # Description minimale si vide
    desc = r["description"] or "—"

    # Ligne du tableau
    row = f"| [{r['name']}]({r['html_url']}) | {desc} | {emoji} {lang} |"
    rows.append(row)

table_content = table_header + "\n" + "\n".join(rows)

# 🔹 Insertion dans README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start_tag = "<!-- PROJETS_RECENTS:START -->"
end_tag = "<!-- PROJETS_RECENTS:END -->"

before = content.split(start_tag)[0]
after = content.split(end_tag)[-1]

new_content = before + start_tag + "\n" + table_content + "\n" + end_tag + after

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
