# news_fetcher.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
news_api_key = os.getenv("NEWSAPI_KEY")

def get_latest_news(topic="sports", language="en", page_size=5, sort_by="publishedAt"):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "language": language,
        "pageSize": page_size,
        "sortBy": sort_by,
        "apiKey": news_api_key
    }
    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    for article in data.get("articles", []):
        articles.append({
            "title": article["title"],
            "url": article["url"],
            "content": article.get("description", "No description")
        })
    return articles
