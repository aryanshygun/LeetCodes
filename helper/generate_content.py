import hashlib
from pathlib import Path

from playwright.sync_api import sync_playwright

from captions import create_post
from images import THEMES, generate_images


BASE_DIR = Path(__file__).resolve().parent.parent

CONTENT_DIR = BASE_DIR / "content"

FINISHED_DIR = CONTENT_DIR / "codes" / "finished"

MEDIUM_DIR = FINISHED_DIR / "medium"
HARD_DIR = FINISHED_DIR / "hard"

IMAGES_DIR = CONTENT_DIR / "images"
POSTS_FILE = CONTENT_DIR / "posts.json"
PROMPT_FILE = BASE_DIR / "helper" / "prompt.txt"


def get_theme(name):
    index = int(
        hashlib.md5(name.encode("utf-8")).hexdigest(),
        16,
    ) % len(THEMES)

    return THEMES[index]


def get_files():
    files = []

    for directory in (MEDIUM_DIR, HARD_DIR):
        if not directory.exists():
            continue

        files.extend(
            file
            for file in directory.iterdir()
            if file.is_file() and file.suffix.lower() in {".py", ".js"}
        )

    return sorted(files)


def generate_content():
    IMAGES_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    files = get_files()

    if not files:
        print("No medium or hard solutions found.")
        return

    image_jobs = [
        (file, get_theme(file.stem))
        for file in files
        if not (IMAGES_DIR / f"{file.stem}.png").exists()
    ]

    print("=== IMAGE PHASE ===")

    if image_jobs:
        with sync_playwright() as playwright:
            generate_images(
                playwright=playwright,
                files=image_jobs,
                images_dir=IMAGES_DIR,
            )
    else:
        print("All images already exist.")

    print("\n=== CAPTION PHASE ===")

    for file in files:
        print(f"\nProcessing: {file.stem}")

        create_post(
            file=file,
            base_dir=BASE_DIR,
            images_dir=IMAGES_DIR,
            posts_file=POSTS_FILE,
            prompt_file=PROMPT_FILE,
        )

    print("\nDone.")


if __name__ == "__main__":
    generate_content()
