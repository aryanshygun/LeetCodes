from pathlib import Path

from playwright.sync_api import sync_playwright

RAYSO_URL = "https://ray.so/"

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


def generate_image(file, output, theme):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(RAYSO_URL, wait_until="domcontentloaded", timeout=60000)
        page.get_by_role("radio", name="64").click()
        page.get_by_role("switch").nth(2).click()
        page.get_by_role("combobox").filter(has_text="").click()
        page.get_by_role("option", name=theme).click()
        page.locator("textarea").fill(file.read_text(encoding="utf-8"))

        with page.expect_download(timeout=60000) as download_info:
            page.get_by_role("button", name="Export as PNG").click()

        download_info.value.save_as(output)

        context.close()
        browser.close()
