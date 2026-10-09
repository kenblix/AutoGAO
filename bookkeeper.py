import json

PROGRESS_FILE = "progress/current_job.json"

def load_progress():

    with open(PROGRESS_FILE, "r", encoding="utf-8") as file:
        progress = json.load(file)

    return progress

def save_progress(progress):

    with open(PROGRESS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            progress,
            file,
            indent=4
        )

def mark_completed(url):

    progress = load_progress()

    if url in progress["completed_urls"]:
        return

    progress["completed_urls"].append(url)

    save_progress(progress)

    print("✅ Progress updated.")

def save_new_job(category_name, category_url, all_urls):

    progress = {
        "category_name": category_name,
        "category_url": category_url,
        "all_urls": all_urls,
        "completed_urls": []
    }
    
    save_progress(progress)

def remaining_urls():

    progress = load_progress()

    return [
        url
        for url in progress["all_urls"]
        if url not in progress["completed_urls"]
    ]

