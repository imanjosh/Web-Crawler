import requests
from bs4 import BeautifulSoup


def crawl(url, max_depth=2, current_depth=0, visited=None):
    print(url)
    if visited is None:
        visited = set()

    try:
        response = requests.get(url)
    except Exception:
        return

    if response.status_code != 200:
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    visited.add(url)

    if current_depth < max_depth:
        for link in links:
            href = link.get('href')
            if href and 'http' in href and href not in visited:
                crawl(href, max_depth, current_depth + 1, visited)


crawl('https://www.reddit.com')
