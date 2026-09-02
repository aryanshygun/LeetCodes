import re

from playwright.sync_api import Page, Playwright

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
    "Verbal",
    "Supabase",
    "Tailwind",
    "OpenAI",
    "Mintlify",
    "Prisma",
    "Clerk",
    "ElevenLabs",
    "Resend",
    "Trigger.dev",
    "Nuxt",
    "Browserbase",
    "Cloudflare",
    "Stripe",
    "Gemini",
    "Firecrawl",
    "AWS",
    "Auth0",
]


def generate_image(page: Page, file, output, theme):
    title = file.stem
    code = file.read_text(encoding="utf-8")

    page.goto(
        RAYSO_URL,
        wait_until="domcontentloaded",
        timeout=60000,
    )

    title_input = page.locator('input[type="text"]')
    textarea = page.locator("textarea")

    title_input.wait_for(
        state="visible",
        timeout=30000,
    )

    textarea.wait_for(
        state="visible",
        timeout=30000,
    )

    title_input.fill(title)
    textarea.fill(code)

    combobox = page.get_by_role("combobox").filter(has_text=re.compile(r"^$"))

    combobox.wait_for(
        state="visible",
        timeout=30000,
    )

    combobox.click()

    option = page.get_by_role(
        "option",
        name=theme,
    )

    option.wait_for(
        state="visible",
        timeout=30000,
    )

    option.click()

    switches = page.get_by_role("switch")
    switch = switches.nth(2)

    if switch.is_visible() and switch.is_enabled():
        switch.click()

    export_button = page.get_by_role(
        "button",
        name="Export as PNG",
    )

    export_button.wait_for(
        state="visible",
        timeout=30000,
    )

    with page.expect_download(timeout=60000) as download_info:
        export_button.click()

    download_info.value.save_as(output)


def generate_images(playwright: Playwright, files, images_dir):
    images_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    browser = playwright.chromium.launch(headless=False)

    try:
        for file, theme in files:
            output = images_dir / f"{file.stem}.png"

            print(f"\nProcessing: {file.stem}")
            print(f"Theme: {theme}")

            if output.exists():
                print("Image exists.")
                continue

            success = False

            for attempt in range(1, 4):
                print(f"Attempt {attempt}/3")

                context = browser.new_context()
                page = context.new_page()

                try:
                    generate_image(
                        page=page,
                        file=file,
                        output=output,
                        theme=theme,
                    )

                    print(f"Saved: {output.name}")
                    success = True

                    context.close()
                    break

                except Exception as error:
                    print(f"Attempt failed: {error}")

                    context.close()

            if not success:
                raise RuntimeError(
                    f"Could not generate image for {file.name} after 3 attempts."
                )

    finally:
        browser.close()
