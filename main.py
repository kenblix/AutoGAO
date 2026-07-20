from parser import scrape_product
from prompt_builder import build_prompt

from gemini import (
    AUTO_SEND,
    start_gemini,
    paste_prompt,
    send_prompt,
    wait_for_generation_to_start,
    wait_for_response,
    read_response
)
from parser.gemini_response import parse_response

from excel import (
    start_excel,
    write_product
)

    #Startup

context = start_gemini()

start_excel(context)

print(
"""
==========================================
            AutoGAO Ready
==========================================

Please make sure:

✓ Gemini is fully loaded
✓ Excel workbook is loaded
✓ Cell A of the next empty row is selected

Press ENTER to begin...
"""
)
input()


                    # Main Loop

while True:

    url = input("\nProduct URL (or type exit): ").strip()

    if url.lower() == "exit":
        print("Goodbye!")
        break


                    # Retry loop

    while True:
        
        try:

            product = scrape_product(url)
            # print(product)

            build_prompt(product)

            paste_prompt()

            if AUTO_SEND:
                send_prompt()

            wait_for_generation_to_start()

            wait_for_response()

            html = read_response()
            # print(html)

            response = parse_response(html)
            # print(response)

            write_product(url, response)

            print("✅ Product completed.\n")

            break

        except Exception as e:

            print("\n==========================================")
            print("Error while processing product.\n")
            print(e)
            print("==========================================\n")

            choice = input(
                "1. Retry this product\n"
                "2. Skip this product\n"
                "3. Exit\n\n"
                "Choice: "
            ).strip()

            if choice == "1":

                print("\nRetrying...\n")

                continue

            elif choice == "2":

                print("\nSkipping product.\n")

                break

            elif choice == "3":

                print("Goodbye!")

                raise SystemExit

            else:

                print("\nInvalid choice. Retrying product.\n")