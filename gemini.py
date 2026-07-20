from playwright.sync_api import sync_playwright

# Global objects
playwright = None
context = None
page = None

AUTO_SEND = True # Set to True to automatically send prompts after auto-pasting


def start_gemini():
    
    # Starts Chrome and opens Gemini.
    
    global playwright, context, page

    playwright = sync_playwright().start()

    context = playwright.chromium.launch_persistent_context(
        user_data_dir="chrome_profile",
        headless=False
    )

    # Reuse existing tab if one already exists
    if context.pages:
        page = context.pages[0]
    else:
        page = context.new_page()

    if "gemini.google.com" not in page.url:
        page.goto("https://gemini.google.com")

    print("Gemini Opening...")

    page.wait_for_selector('div[role="textbox"]', timeout=300000)

    print("✅ Gemini ready!\n")
    
    return context


def paste_prompt():
    """
    Pastes the clipboard contents into Gemini.
    """

    global page

    textbox = page.locator('div[role="textbox"]')

    page.bring_to_front()
    textbox.click()

    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    page.keyboard.press("Control+V")

    print("✅ Prompt pasted.")

def send_prompt():
    """
    Clicks Gemini's Send button.
    """

    global page

    send_button = page.locator(
        'button[aria-label="Send message"]'
    )

    # send_button.wait_for(state="visible")

    send_button.click()

    print("✅ Prompt sent.")

def wait_for_generation_to_start():
    
    # Waits until Gemini starts generating.

    global page

    print("Waiting for generation to start...")

    stop_button = page.locator(
        'button[aria-label="Stop response"]'
    )

    stop_button.wait_for(
        state="visible",
        timeout=300000
    )

    print("Generation started.")

def wait_for_response():
    
    # Waits until Gemini finishes generating.

    global page

    print("Waiting for Gemini response...")

    stop_button = page.locator(
        'button[aria-label="Stop response"]'
    )

    stop_button.wait_for(
        state="hidden",
        timeout=300000
    )

    print("✅ Gemini finished.")

def read_response():
    """
    Returns the HTML of Gemini's latest response.
    """

    global page

    response = page.locator(
        "structured-content-container"
    ).last

    response.wait_for(state="visible")

    return response.inner_html()
