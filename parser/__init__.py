from parser.page import get_page
from parser.product import (
    get_product_name,
    get_short_description
)
from parser.content import get_content


def scrape_product(url):

    soup = get_page(url)

    return {
        "product_name": get_product_name(soup),
        "short_description": get_short_description(soup),
        "content": get_content(soup)
    }