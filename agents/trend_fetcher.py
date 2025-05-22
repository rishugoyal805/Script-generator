import requests
from bs4 import BeautifulSoup

def fetch_trending_data(theme):
    query = theme.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}&tbm=nws"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = [h.get_text() for h in soup.select("h3")][:5]
    return "\n".join(headlines)