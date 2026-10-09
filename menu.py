def main_menu(progress):


    print(
f"""
==========================================
            AutoGAO v1.2
==========================================

Current Job

Category:
{progress["category_name"]}

Completed : {len(progress["completed_urls"])}
Remaining : {len(progress["all_urls"]) - len(progress["completed_urls"])}

------------------------------------------

1. Continue Current Job

2. Start New Job

3. Exit
"""
    )

    return input("Choice: ").strip()

def processing_summary(
    category_name,
    remaining,
    processing,
    remaining_after
):

    print(
f"""
==========================================
        Starting AutoGAO v1.2
==========================================

Category:
{category_name}

Remaining Products:
{remaining}

Processing This Run:
{processing}

Remaining Afterwards:
{remaining_after}

------------------------------------------

Please make sure:

✓ Gemini is fully loaded
✓ Excel workbook is loaded
✓ Cell A of the next empty row is selected

------------------------------------------

Press ENTER to begin...
"""
    )

    input()

def product_error_menu(error):

    print(
f"""
==========================================
Error while processing product.

{error}

==========================================

1. Retry this product

2. Skip this product

3. Exit
"""
    )

    return input("\nChoice: ").strip()

def ask_product_amount():

    while True:

        try:

            amount = int(
                input("How many products would you like to process? ")
            )

            if amount <= 0:
                print("Please enter a number greater than 0.\n")
                continue

            return amount

        except ValueError:

            print("Please enter a valid number.\n")

