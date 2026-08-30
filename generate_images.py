from pathlib import Path

from openai import OpenAI
from playwright.sync_api import Playwright, sync_playwright

SOURCE_DIR = Path.home() / "LeetCodes/Leetcode/finished"
IMAGE_DIR = SOURCE_DIR / "images"
CAPTION_DIR = SOURCE_DIR / "captions"
RAYSO_URL = "https://ray.so/"
MODEL = "qwen_3_4b-safetensors"

THEMES = [
    "Bitmap",
    "Noir",
    "Ice",
    "Sand",
    "Forest",
    "Mono",
    "Breeze",
    "Candy",
    "Crimson",
    "Falcon",
    "Meadow",
    "Midnight",
    "Raindrop",
    "Sunset",
]


def generate_caption(file):
    code = file.read_text(encoding="utf-8")
    language = "Python" if file.suffix.lower() == ".py" else "JavaScript"

    system_prompt = """
You write short LinkedIn posts for a software engineering student who solves LeetCode problems regularly.

Write like a real person documenting daily progress. Keep it pragmatic, professional, concise, and natural, with a subtle dry sense of humor when appropriate.

Use only a few sentences. Mention the problem, briefly explain the actual approach used in the provided code, and mention time/space complexity naturally when useful.

Do not use emojis, headings, bullet points, motivational clichés, exaggerated claims, or generic explanations. Do not say "Today I learned", "I'm excited to share", or mention AI.

End with 2 or 3 relevant hashtags.

Write only the final LinkedIn post.
"""

    prompt = f"""
Write a LinkedIn post for this LeetCode solution.

Problem:
{file.stem}

Language:
{language}

My actual solution:

{code}

Describe the approach actually used in my code, not a generic solution.
"""

    response = OpenAI(
        base_url="http://localhost:1234/v1", api_key="lm-studio"
    ).chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=0.75,
        max_tokens=200,
    )

    return response.choices[0].message.content.strip()


def generate_image(page, file, theme, output):
    page.goto(RAYSO_URL, wait_until="domcontentloaded", timeout=60000)
    page.get_by_role("radio", name="64").click()
    page.get_by_role("switch").nth(2).click()
    page.get_by_role("combobox").filter(has_text="").click()
    page.get_by_role("option", name=theme).click()
    page.locator("textarea").fill(file.read_text(encoding="utf-8"))

    with page.expect_download(timeout=60000) as download_info:
        page.get_by_role("button", name="Export as PNG").click()

    download_info.value.save_as(output)


def generate_missing_images(files):
    missing = [
        (index, file)
        for index, file in enumerate(files)
        if not (IMAGE_DIR / f"{file.stem}.png").exists()
    ]

    if not missing:
        return

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        for index, file in missing:
            output = IMAGE_DIR / f"{file.stem}.png"
            theme = THEMES[index % len(THEMES)]

            try:
                print(f"Generating image: {file.name} [{theme}]")
                generate_image(page, file, theme, output)
                print(f"Saved: {output.name}")
            except Exception as error:
                print(f"Image failed: {file.name} - {error}")

        context.close()
        browser.close()


def generate_missing_captions(files):
    for file in files:
        output = CAPTION_DIR / f"{file.stem}.txt"

        if output.exists():
            print(f"Caption already exists: {file.name}")
            continue

        try:
            print(f"Generating caption: {file.name}")
            caption = generate_caption(file)
            output.write_text(caption, encoding="utf-8")
            print(f"Saved: {output.name}")
        except Exception as error:
            print(f"Caption failed: {file.name} - {error}")


def main():
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    CAPTION_DIR.mkdir(parents=True, exist_ok=True)

    files = sorted(
        file
        for file in SOURCE_DIR.iterdir()
        if file.is_file() and file.suffix.lower() in {".py", ".js"}
    )

    if not files:
        print("No .py or .js files found.")
        return

    generate_missing_images(files)
    generate_missing_captions(files)


if __name__ == "__main__":
    main()
