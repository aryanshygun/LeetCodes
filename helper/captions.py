from openai import OpenAI

MODEL = "qwen_3_4b-safetensors"

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


def generate_caption(file):
    code = file.read_text(encoding="utf-8")
    language = "Python" if file.suffix.lower() == ".py" else "JavaScript"

    system_prompt = """
You write short LinkedIn posts for a software engineering student who solves LeetCode problems regularly.

Write like a real person documenting daily progress. Keep it pragmatic, professional, concise, and natural, with a subtle dry sense of humor when appropriate.

Use only a few sentences. Mention the problem, briefly explain the actual approach used in the provided code, and mention time/space complexity naturally when useful.

Do not use emojis, headings, bullet points, motivational clichés, exaggerated claims, or generic explanations.

Do not say "Today I learned", "I'm excited to share", or mention AI.

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

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=0.75,
        max_tokens=200,
    )

    return response.choices[0].message.content.strip()
