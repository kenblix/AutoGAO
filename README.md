# AutoGAO v1.2

A Python-based workflow automation application for scraping product information, generating AI-powered product content with Google Gemini, writing structured results into Excel, and tracking processing progress, Specifically made for GAOTEK site.

## Features

* **Product collection:** Automatically collects product URLs from category pages, including pages that use a Load More button.
* **Product scraping:** Extracts relevant product information from individual product pages.
* **AI content generation:** Builds structured prompts and processes product content through Google Gemini.
* **Automated Excel entry:** Writes product URLs and generated content into the selected Excel worksheet.
* **Progress tracking:** Records completed products in a local JSON file to support resuming unfinished jobs.
* **Error handling:** Provides retry, skip, and exit options when product processing fails.
* **Batch processing:** Lets the user choose how many products to process in each run.
* **Modular architecture:** Separates browser automation, scraping, response parsing, Excel entry, progress tracking, and menu handling into dedicated modules.

## Workflow

1. Collect product URLs from a selected category.
2. Scrape product information.
3. Build a prompt using the product data and prompt template.
4. Send the prompt to Google Gemini.
5. Wait for the response and parse the generated content.
6. Write the product URL and generated fields into Excel.
7. Mark the product as completed in the progress tracker.
8. Continue to the next product or return to the main menu.

## Project Structure

```text
AutoGAO/
├── parser/
│   ├── __init__.py
│   ├── content.py
│   ├── gemini_response.py
│   ├── page.py
│   └── product.py
├── progress/
│   └── current_job.json       # Local runtime state; not committed
├── .gitignore
├── bookkeeper.py              # Job progress and completion tracking
├── collector.py               # Category and product URL collection
├── excel.py                   # Excel browser interaction and data entry
├── gemini.py                  # Gemini browser interaction and response handling
├── main.py                    # Main application workflow
├── menu.py                    # Menus, prompts, and processing summaries
├── prompt_builder.py          # Prompt construction
├── prompt_template.txt        # Prompt template, if present
├── README.md
├── requirements.txt           # Python dependencies
├── settings.txt               # Local workbook configuration
├── startup.py                 # Browser session startup and shutdown
└── whitelist.txt               # Content parsing configuration
```

## Requirements

* Python
* Google Chrome
* A Google account with access to Gemini
* Access to the Excel workbook used by the workflow
* Python dependencies listed in `requirements.txt`

## Setup

1. Clone or download the repository.

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the Excel workbook link as "EXCEL_URL = {your link}" file labeled as "settings.txt"

4. Ensure that the required workbook is accessible and that the correct worksheet and starting cell are selected.

5. Start the application:

   ```bash
   python main.py
   ```

6. Follow the interactive menu to continue an existing job or start a new category job.

## Progress and Recovery

AutoGAO maintains a local progress file containing the current category, collected product URLs, and completed product URLs.

* Completed products are excluded from the remaining queue.
* Failed products can be retried or skipped.
* Processing can resume from the remaining queue on a subsequent run.

**Important:** Back up `progress/current_job.json` before replacing or resetting a job if you need to preserve your progress.

## Security and Configuration

Browser profiles, local progress data, and temporary files should remain outside version control.

Do not commit browser session data, authentication information, private workbook links, or other sensitive local configuration.

## Limitations

* The browser workflow depends on the current layouts and behavior of the target website, Gemini, and Excel.
* Gemini generation time and response formatting can vary.
* The Excel workbook must be open and positioned correctly before data entry begins.
* This application is designed around the current product-content workflow and may require changes if the underlying websites change.

## Version

**AutoGAO v1.2** — Modular workflow refactor with batch processing, progress tracking, and improved error handling.
