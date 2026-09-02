import json
from datetime import datetime, timezone
from pathlib import Path

from helper.linkedin import post

BASE_DIR = Path(__file__).resolve().parent

CONTENT_DIR = BASE_DIR / "content"
POSTS_FILE = CONTENT_DIR / "posts.json"


def load_posts():
    if not POSTS_FILE.exists():
        return {}

    try:
        return json.loads(POSTS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_posts(posts):
    POSTS_FILE.write_text(
        json.dumps(
            posts,
            indent=4,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def main():
    posts = load_posts()

    for name, data in posts.items():
        if data.get("posted", False):
            continue

        image_path = BASE_DIR / data["image"]

        if not image_path.exists():
            print(f"Missing image for: {name}")
            continue

        caption = data.get("caption", "").strip()

        if not caption:
            print(f"Empty caption for: {name}")
            continue

        print(f"Posting: {name}")
        print(f"Difficulty: {data.get('difficulty', 'Unknown')}")

        post_id = post(
            caption=caption,
            image_path=image_path,
            alt_text=f"LeetCode solution: {data['title']}",
        )

        data["posted"] = True
        data["posted_at"] = datetime.now(timezone.utc).isoformat()

        save_posts(posts)

        print(f"Successfully posted: {name}")
        print(f"Post ID: {post_id}")

        return

    print("No unposted solutions found.")


if __name__ == "__main__":
    main()
