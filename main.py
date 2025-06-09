import requests
from collections import defaultdict

USERNAME = "$GITHUBUSERNAME"

def get_repos():
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&page={page}"
        res = requests.get(url)
        data = res.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return [repo["name"] for repo in repos]

def get_languages(repo):
    url = f"https://api.github.com/repos/{USERNAME}/{repo}/languages"
    res = requests.get(url)
    return res.json()

def aggregate_languages(repos):
    lang_t = defaultdict(int)
    for repo in repos:
        langs = get_languages(repo)
        for lang, bytes_of_code in langs.items():
            lang_t[lang] += bytes_of_code
    return lang_t

def generate_markdown(lang_t):
    total_bytes = sum(lang_t.values())
    lines = ["### Languages Used \n"]
    for lang, count in sorted(lang_t.items(), key=lambda x: x[1], reverse=True):
        percent = 100 * count / total_bytes
        lines.append(f"- {lang}: {percent:.2f}%")
    return "\n".join(lines)

def update_readme(markdown_block):
    stats = f"\n{markdown_block}\n"
    with open("README.md", "w") as f:
        f.write(stats)

repos = get_repos()
lang_stats = aggregate_languages(repos)
md = generate_markdown(lang_stats)
update_readme(md)

