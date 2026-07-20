import pyperclip


def build_prompt(product):

    with open("prompt_template.txt", "r", encoding="utf-8") as file:
        template = file.read()

    template = template.replace(
        "{product_name}",
        product["product_name"]
    )

    template = template.replace(
        "{short_description}",
        product["short_description"]
    )

    template = template.replace(
        "{content}",
        product["content"]
    )

    pyperclip.copy(template)
    # print(template)

    print("\n✅ Prompt copied to clipboard.")

    return template