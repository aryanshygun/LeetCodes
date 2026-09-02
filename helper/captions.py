import json
import time

from openai import OpenAI

MODEL = "qwen_3_4b-safetensors"


client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
)


def generate_caption(file, prompt_file):
    code = file.read_text(encoding="utf-8")

    system_prompt = prompt_file.read_text(encoding="utf-8").strip()

    if file.suffix.lower() == ".py":
        language = "Python"
    else:
        language = "JavaScript"

    user_prompt = (
        "Write a LinkedIn post for this LeetCode solution.\n\n"
        "Problem:\n" + file.stem + "\n\n"
        "Language:\n" + language + "\n\n"
        "Actual solution:\n\n"
        "```" + language.lower() + "\n" + code + "\n"
        "```\n\n"
        "Analyze the actual implementation before writing.\n\n"
        "The post should briefly communicate:\n"
        "1. What the problem asks.\n"
        "2. The approach this specific implementation takes.\n"
        "3. One useful implementation detail, tradeoff, or complexity "
        "observation if appropriate.\n\n"
        "Do not describe an optimal solution if the supplied code does "
        "something different.\n\n"
        "Keep the result natural and concise."
    )

    last_error = None

    for attempt in range(1, 4):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
                temperature=0.7,
                max_tokens=500,
                timeout=60,
            )

            content = response.choices[0].message.content

            if content:
                return content.strip()

            raise RuntimeError("LM Studio returned an empty message.content.")

        except Exception as error:
            last_error = error

            print(f"Caption generation failed (attempt {attempt}/3): {error}")

            if attempt < 3:
                print("Retrying in 5 seconds...")
                time.sleep(5)

    raise RuntimeError(
        f"Failed to generate caption for {file.name} after 3 attempts."
    ) from last_error


def load_posts(posts_file):
    if not posts_file.exists():
        return {}

    return json.loads(posts_file.read_text(encoding="utf-8"))


def save_posts(posts, posts_file):
    posts_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    posts_file.write_text(
        json.dumps(
            posts,
            indent=4,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def create_post(
    file,
    base_dir,
    images_dir,
    posts_file,
    prompt_file,
):
    posts = load_posts(posts_file)

    if file.name in posts:
        return posts[file.name]

    problem = file.stem

    number, name = problem.split(
        ".",
        1,
    )

    number = number.strip()
    name = name.strip()

    difficulty = file.parent.name.capitalize()

    title = f"LeetCode {number}. {name}"

    search_name = problem.replace(
        " ",
        "+",
    )

    url = "https://leetcode.com/search/?q=" + search_name

    print(f"Generating caption: {file.name}")
    print(f"Difficulty: {difficulty}")

    generated = generate_caption(
        file=file,
        prompt_file=prompt_file,
    )

    lines = generated.splitlines()

    hashtags = []
    body_lines = []

    for line in lines:
        line = line.strip()

        if line.startswith("#"):
            hashtags.append(line)
        elif line:
            body_lines.append(line)

    body = " ".join(body_lines)

    hashtag_text = " ".join(hashtags[:3])

    caption = title + "\n\n" + "Difficulty: " + difficulty + "\n\n" + body

    if hashtag_text:
        caption += "\n\n" + hashtag_text

    caption += "\n\n" + url

    post = {
        "title": title,
        "difficulty": difficulty,
        "posted": False,
        "posted_at": None,
        "caption": caption,
        "code": str(file.relative_to(base_dir)),
        "image": str((images_dir / f"{file.stem}.png").relative_to(base_dir)),
    }

    posts[file.name] = post

    save_posts(
        posts=posts,
        posts_file=posts_file,
    )

    print(f"Saved post: {file.name}")

    return post
