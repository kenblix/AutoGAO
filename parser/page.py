import requests
from bs4 import BeautifulSoup


def get_page(url):

    # Downloads the webpage and returns BeautifulSoup.

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers
    )

    response.raise_for_status()

    return BeautifulSoup(
        response.text,
        "html.parser"
    )