from bs4 import BeautifulSoup


def parse_response(html):
    
    # Parses Gemini's HTML response into a dictionary

    soup = BeautifulSoup(html, "html.parser")

    data = {
        "new_product_name": "",
        "new_product_overview": "",
        "new_applications": ""
    }

    heading_map = {
        "New Product Name": "new_product_name",
        "New Product Overview": "new_product_overview",
        "New Applications": "new_applications"
    }

    headings = soup.find_all("h2")

    for heading in headings:

        section_name = heading.get_text(strip=True)

        key = heading_map.get(section_name)

        if key is None:
            continue

        content = []

        node = heading.find_next_sibling()

        while node and node.name != "h2":

            # Paragraph
            if node.name == "p":

                content.append(
                    node.get_text(" ", strip=True)
                )

            # Bullet list
            elif node.name == "ul":

                for li in node.find_all("li", recursive=False):

                    content.append(
                        li.get_text(" ", strip=True)
                    )

            node = node.find_next_sibling()

        if key == "new_applications":

            data[key] = "\n".join(content)

        else:

            data[key] = " ".join(content)

    return data