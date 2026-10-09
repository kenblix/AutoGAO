from gemini import (
    start_gemini,
    close_gemini
)

from excel import (
    start_excel
)

context = None

def start_processing():

    global context

    if context is not None:

        print("\nReusing existing browser session.\n")
        return context

    print("\nLaunching Gemini...")

    context = start_gemini()

    print("\nLaunching Excel...")

    start_excel(context)

    return context


def close_processing():

    global context

    if context is None:
        return

    close_gemini()

    context = None