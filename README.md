# AutoGAO

Automates the GAOTek product content creation workflow using Python, Playwright, and BeautifulSoup.

## Features

- Scrapes product information from GAOTek product pages
- Automatically builds prompts for Gemini
- Waits for AI generation to finish
- Parses structured AI output
- Automatically writes results into Excel Online
- Configurable whitelist for product sections
- Supports different product page layouts

## Technologies

- Python
- Playwright
- BeautifulSoup
- Requests
- Pyperclip

## Project Structure

main.py
gemini.py
excel.py
prompt_builder.py
parser/
requirements.txt

## Setup

1. Clone the repository

2. Install requirements

pip install -r requirements.txt

3. Install Playwright

playwright install

4. Create a settings.txt file

EXCEL_URL=YOUR_SHAREPOINT_EXCEL_LINK

5. Run

python main.py

## Notes

settings.txt is intentionally excluded from Git to protect private URLs.

chrome_profile is also excluded because it contains browser session data.

## Future Improvements

- Automatic product queue
- Resume after interruption
- Duplicate detection
- Better error recovery
- GUI version

## License

MIT