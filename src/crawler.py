import requests
import time
from bs4 import BeautifulSoup

def crawl(base_url, delay=6):
    pages = {}
    page_num = 1

    while True:
        url = f"{base_url}/page/{page_num}/"
        try:
            response = requests.get(url)
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            break
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator=" ", strip=True)

        pages[url] = text
        if not soup.find("li", class_="next"):
            break 

        page_num += 1
        time.sleep(delay)

    return pages