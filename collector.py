from playwright.sync_api import sync_playwright

playwright = None
context = None
page = None

PRODUCT_SELECTOR = "a.wd-product-img-link"
LOAD_MORE_SELECTOR = "a.wd-products-load-more"

def start_collection():
    global playwright, context, page

    playwright = sync_playwright().start()

    context = playwright.chromium.launch_persistent_context(
        user_data_dir="chrome_profile",
        channel="chrome",
        headless=False
        )
    page = context.new_page()
 
def collect_product_urls(category_url):

    page.goto(
        category_url,
        wait_until="domcontentloaded",
        timeout=120000
    )

    category_name = (
        page.locator("h1.entry-title.title")
        .inner_text()
        .strip()
    )

    print("Category opened.\n")

    # Click "Load More" until it disappears
    while True:

        load_more = page.locator(LOAD_MORE_SELECTOR)

        if load_more.count() == 0:
            print("✅ All products loaded.\n")
            break

        before = page.locator(PRODUCT_SELECTOR).count()

        print(f"Products loaded: {before}")

        load_more.scroll_into_view_if_needed()
        load_more.click()

        page.wait_for_function(
            f"""
            () => document.querySelectorAll(
                '{PRODUCT_SELECTOR}'
            ).length > {before}
            """,
            timeout=120000
        )

    # Collect URLs
    links = page.locator(PRODUCT_SELECTOR)

    urls = set()

    for i in range(links.count()):

        href = links.nth(i).get_attribute("href")

        if href:
            urls.add(href)

    urls = sorted(urls)

    print(f"Collected {len(urls)} products.")

    return category_name, urls


def close_collection():

    global context
    global playwright

    context.close()
    playwright.stop()

