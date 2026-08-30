import json
from pathlib import Path

from linkedin import post


BASE_DIR = Path(__file__).resolve().parent

CAPTIONS_DIR = BASE_DIR / "captions"
IMAGES_DIR = BASE_DIR / "images"
POSTED_FILE = BASE_DIR / "posted.json"


def load_posted():
    if not POSTED_FILE.exists():
        return set()

    try:
        data = json.loads(
            POSTED_FILE.read_text(encoding="utf-8")
        )
    except (json.JSONDecodeError, OSError):
        return set()

    return set(data.get("posted", []))


def save_posted(posted):
    POSTED_FILE.write_text(
        json.dumps(
            {"posted": sorted(posted)},
            indent=2,
        ),
        encoding="utf-8",
    )


def main():
    posted = load_posted()

    caption_files = sorted(
        CAPTIONS_DIR.glob("*.txt"),
        key=lambda file: file.name,
    )

    for caption_file in caption_files:
        name = caption_file.stem

        if name in posted:
            continue

        image_file = IMAGES_DIR / f"{name}.png"

        if not image_file.exists():
            print(f"Missing image for: {name}")
            continue

        caption = caption_file.read_text(
            encoding="utf-8"
        ).strip()

        if not caption:
            print(f"Empty caption for: {name}")
            continue

        print(f"Posting: {name}")

        post_id = post(
            caption=caption,
            image_path=image_file,
            alt_text=f"LeetCode solution: {name}",
        )

        posted.add(name)
        save_posted(posted)

        print(f"Successfully posted: {name}")
        print(f"Post ID: {post_id}")

        return

    print("No unposted solutions found.")


if __name__ == "__main__":
    main()