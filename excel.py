from playwright.sync_api import Page
import pyperclip

def load_settings():
    settings = {}
    
    with open("settings.txt", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or "=" not in line:
                continue

            key, value = line.split("=", 1)
            settings[key.strip()] = value.strip()

    return settings


SETTINGS = load_settings()

EXCEL_URL = SETTINGS["EXCEL_URL"]

excel_page = None
excel_frame = None


def start_excel(context):

    # Opens Excel Online once.

    global excel_page
    global excel_frame

    excel_page = context.new_page()
    excel_page.goto(EXCEL_URL)

    print("Excel Opening...")

    excel_page.wait_for_load_state("domcontentloaded")

    for frame in excel_page.frames:

        # print(frame.url)

        if "officeapps.live.com" in frame.url:

            excel_frame = frame

            break

    # print("\nWorkbook frame found:\n", excel_frame.url)
    

def type_value(value):

    # Types text into the currently selected cell.

    global excel_page
    global excel_frame

    lines = str(value).split("\n")

    for i, line in enumerate(lines):

        grid = excel_frame.locator("#gridKeyboardContentEditable_textElement")
        grid.type(line)

        if i < len(lines) - 1:

            # First line break
            excel_page.keyboard.press("Alt+Enter")

            # Blank line
            excel_page.keyboard.press("Alt+Enter")

def next_cell():

    # Moves one column to the right.

    global excel_page

    excel_page.keyboard.press("Tab")


def next_row():

    # Returns to column A and moves to next row.

    global excel_page

    excel_page.keyboard.press("Home")

    excel_page.keyboard.press("ArrowDown")


def write_product(url, response):
    
    # Writes one product into Excel.

    values = [

        url,

        response["new_product_name"],

        response["new_product_overview"],

        response["new_applications"]

    ]

    print("Switching to Excel...")

    excel_page.bring_to_front()
    excel_page.wait_for_timeout(300)

    # excel_page.keyboard.press("Escape")
    # excel_page.wait_for_timeout(50)

    # excel_page.keyboard.press("F2")
    # excel_page.wait_for_timeout(100)

    print("Writing row...")

    for index, value in enumerate(values):
    
        type_value(value)
        excel_page.wait_for_timeout(50)
        
        if index < len(values) - 1:

            next_cell()

    next_row()
