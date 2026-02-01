import requests
import time
import pandas as pd

BASE_API = "https://exame.com/wp-json/wp/v2/posts"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

PER_PAGE = 100  
DELAY = 1.5


def get_posts(page):
    params = {
        "page": page,
        "per_page": PER_PAGE
    }

    r = requests.get(BASE_API, headers=HEADERS, params=params, timeout=20)

    if r.status_code == 400:
        return []

    r.raise_for_status()
    return r.json()


def clean_html(text):
    import re
    return re.sub("<.*?>", "", text)


def main(max_pages=10):
    all_posts = []

    for page in range(1, max_pages + 1):
        print(f"Página {page}")

        posts = get_posts(page)

        if not posts:
            break

        for p in posts:
            all_posts.append({
                "id": p["id"],
                "titulo": clean_html(p["title"]["rendered"]),
                "resumo": clean_html(p["excerpt"]["rendered"]),
                "conteudo": clean_html(p["content"]["rendered"]),
                "url": p["link"],
                "data": p["date"]
            })

        time.sleep(DELAY)

    return pd.DataFrame(all_posts)
