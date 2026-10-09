from parser import scrape_product
from parser.gemini_response import parse_response

from prompt_builder import build_prompt

from collector import (
    start_collection,
    collect_product_urls,
    close_collection
)

from bookkeeper import (
    load_progress,
    save_new_job,
    remaining_urls,
    mark_completed
)

from gemini import (
    AUTO_SEND,  
    paste_prompt,
    send_prompt,
    wait_for_generation_to_start,
    wait_for_response,
    read_response
)

from startup import (
    start_processing,
    close_processing
)

from excel import write_product

from menu import (
    ask_product_amount,
    main_menu,
    processing_summary,
    product_error_menu
)

class StopProcessing(Exception):
    pass


def new_job():

    category_url = input(
        "\nCategory URL: "
    ).strip()

    start_collection()

    try:

        category_name, all_urls = collect_product_urls(category_url)

    finally:

        close_collection()

    save_new_job(
        category_name,
        category_url,
        all_urls
    )

    print(f"\n✅ New job created!")
    print(f"Category : {category_name}")
    print(f"Products : {len(all_urls)}\n")

def continue_job():

    urls = remaining_urls()

    if not urls:

        print("\n This job is already complete.\n")

        return None

    print(f"\nRemaining products: {len(urls)}\n")

    return urls

def prepare_run():

    urls = continue_job()

    if urls is None:
        return None

    amount = ask_product_amount()

    return urls[:amount]


def process_product(url):

    while True:

        try:

            product = scrape_product(url)

            build_prompt(product)

            paste_prompt()

            if AUTO_SEND:
                send_prompt()

            wait_for_generation_to_start()

            wait_for_response()

            html = read_response()

            response = parse_response(html)

            write_product(url, response)

            mark_completed(url)

            print("✅ Product completed.\n")

            return

        except Exception as e:

            choice = product_error_menu(e)

            if choice == "1":

                print("\nRetrying...\n")

                continue

            elif choice == "2":

                print("\nSkipping product.\n")

                return

            elif choice == "3":

                raise StopProcessing

            else:

                print("\nInvalid choice. Retrying product.\n")

def process_products(urls):

    try:

        for number, url in enumerate(urls, start=1):

            print(
                f"\n========== Product {number}/{len(urls)} ==========\n"
            )

            process_product(url)

        print("\n Processing complete!\n")

    except StopProcessing:

        print("\nProcessing stopped by user.\n")

while True:

    progress = load_progress()
    choice = main_menu(progress)

    if choice == "1":

        urls = prepare_run()

    elif choice == "2":

        new_job()

        urls = prepare_run()

    elif choice == "3":

        close_processing()
        print("\nGoodbye!")
        break

    else:

        print("\nInvalid choice.\n")
        continue

    if not urls:

        continue

    start_processing()

    progress = load_progress()

    remaining=len(remaining_urls())

    processing_summary(
        category_name=progress["category_name"],
        remaining=remaining,
        processing=len(urls),
        remaining_after=remaining - len(urls)
    )

    process_products(urls)
