def load_whitelist():

    with open("whitelist.txt","r", encoding="utf-8") as file:

        return {
            line.strip().lower()
            for line in file
            if line.strip()
        }
    
VALID_HEADINGS = load_whitelist()

def get_content(soup):
    
    #Parses the product documentation using headings defined in whitelist.txt.

    container = soup.find("div", class_="wc-tab-inner")

    if not container:
        return ""

    content_parts = []

    collecting = False

    for tag in container.find_all(
        ["h2", "h3", "p", "ul", "table"]
    ):

        # -------------------------
        # Headings
        # -------------------------

        if tag.name in ["h2", "h3"]:

            heading = tag.get_text(" ", strip=True)

            print(f"FOUND HEADING: '{heading}'")

            if any(
                valid.lower() in heading.lower()
                or heading.lower() in valid.lower()
                for valid in VALID_HEADINGS):

                print("  --> WHITELISTED")
                collecting = True
                content_parts.append(f"\n{heading}")

            else:

                print("  --> NOT WHITELISTED")
                collecting = False

            continue

        # Ignore everything until a valid heading appears

        if not collecting:
            continue

        # -------------------------
        # Paragraphs
        # -------------------------

        if tag.name == "p":

            paragraph = tag.get_text(" ", strip=True)

            # print("PARAGRAPH:", repr(paragraph))
            if paragraph:
                content_parts.append(paragraph)

        # -------------------------
        # Bullet Lists
        # -------------------------

        elif tag.name == "ul":

            for li in tag.find_all("li"):

                bullet = li.get_text(" ", strip=True)

                if bullet:
                    content_parts.append(f"• {bullet}")

        # -------------------------
        # Tables
        # -------------------------

        elif tag.name == "table":

            for row in tag.find_all("tr"):

                cols = row.find_all("td")

                if len(cols) >= 2:

                    key = cols[0].get_text(" ", strip=True)
                    value = cols[1].get_text(" ", strip=True)

                    content_parts.append(f"{key}: {value}")

    return "\n".join(content_parts)