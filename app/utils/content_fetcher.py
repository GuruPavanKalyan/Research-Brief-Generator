# app/utils/content_fetcher.py

from newspaper import Article

def fetch_url_text(url: str) -> str:
    article = Article(url)
    article.download()
    article.parse()
    return article.text
