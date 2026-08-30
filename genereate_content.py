import hashlib
from pathlib import Path

from captions import generate_caption
from images import THEMES, generate_image

FINISHED_DIR = Path("finished")
CAPTIONS_DIR = Path("captions")
IMAGES_DIR = Path("images")


def get_theme(name):
    index = int(
        hashlib.md5(name.encode("utf-8")).hexdigest(),
        16,
    ) % len(THEMES)

    return THEMES[index]


def generate_content():
    CAPTIONS_DIR.mkdir(exist_ok=True)
    IMAGES_DIR.mkdir(exist_ok=True)

    for file in sorted(FINISHED_DIR.iterdir()):
        if file.suffix.lower() not in {".py", ".js"}:
            continue

        name = file.stem
        caption_file = CAPTIONS_DIR / f"{name}.txt"
        image_file = IMAGES_DIR / f"{name}.png"

        print(f"\nProcessing: {name}")

        if not caption_file.exists():
            print("Generating caption...")
            caption = generate_caption(file)
            caption_file.write_text(caption, encoding="utf-8")
        else:
            print("Caption exists.")

        if not image_file.exists():
            theme = get_theme(name)
            print(f"Generating image with theme: {theme}")
            generate_image(
                file=file,
                output=image_file,
                theme=theme,
            )
        else:
            print("Image exists.")

    print("\nDone.")


if __name__ == "__main__":
    generate_content()
