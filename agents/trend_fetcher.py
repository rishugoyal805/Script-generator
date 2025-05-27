# import requests
# from bs4 import BeautifulSoup

# def fetch_trending_data(theme):
#     query = theme.replace(" ", "+")
#     url = f"https://www.google.com/search?q={query}&tbm=nws"
#     headers = {'User-Agent': 'Mozilla/5.0'}
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, "html.parser")
#     headlines = [h.get_text() for h in soup.select("h3")][:5]
#     return "\n".join(headlines)
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_trending_data(theme):
    api_key = os.getenv("SERPER_API_KEY")
    url = "https://google.serper.dev/news"

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "q": theme
    }

    response = requests.post(url, headers=headers, json=data)
    news_items = response.json().get("news", [])[:6]  # Get top 6 trends

    if not news_items:
        return [], ""

    all_trends = [item["title"] for item in news_items]
    concatenated_trends = "\n".join(all_trends)

    return all_trends, concatenated_trends
