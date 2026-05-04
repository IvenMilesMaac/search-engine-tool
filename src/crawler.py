import requests
import time
from bs4 import BeautifulSoup

def crawl(base_url, delay=6):
    """
    Crawl all the pages of a website and returns their text content.
    
    Args:
        base_url (str): The base URL of the website to crawl.
        delay (int): The delay in seconds between each request.

    Returns:
        dict: A dictionary mapping page URLs to their text content.
    """
    
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