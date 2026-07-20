def get_product_name(soup):
    """
    Extracts the product title.
    """

    title = soup.find(
        "h1",
        class_="product_title entry-title wd-entities-title"
    )

    if title:
        return title.get_text(strip=True)

    return ""


def get_short_description(soup):
    """
    Extracts the short description below the title.
    """

    desc = soup.find(
        "div",
        class_="woocommerce-product-details__short-description"
    )

    if desc:
        return desc.get_text(" ", strip=True)

    return ""