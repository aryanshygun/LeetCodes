
# LeetCode → LinkedIn

A small automation pipeline for turning LeetCode solutions into LinkedIn posts.

The project takes completed LeetCode solutions, generates code images using [Ray.so](https://ray.so/), creates concise captions using a local LLM through LM Studio, stores everything in a single `posts.json` file, and publishes one unposted solution to LinkedIn automatically.

The goal is simple: keep solving LeetCode and let the repetitive publishing work happen automatically.

---

## How It Works

```text
LeetCode Solution
       │
       ▼
content/codes/finished/
       │
       ├── medium/
       └── hard/
       │
       ▼
   Image Generator
     (Ray.so)
       │
       ▼
 content/images/
       │
       ▼
 Caption Generator
   (LM Studio)
       │
       ▼
 content/posts.json
       │
       ▼
 GitHub Actions
       │
       ▼
   LinkedIn Post
```

Only **Medium** and **Hard** solutions are published. Easy solutions and attempted solutions remain outside the publishing pipeline.

---

## Features

- Automatically finds completed Medium and Hard LeetCode solutions.
- Generates code images using Ray.so.
- Assigns a consistent Ray.so theme to each problem.
- Generates LinkedIn captions using a locally running LLM.
- Uses the actual implementation when describing the solution.
- Stores captions, images, difficulty, and posting state in `posts.json`.
- Skips solutions that already have generated images.
- Skips solutions that have already been posted.
- Retries image and caption generation when something fails.
- Publishes only **one post per GitHub Actions run**.
- Automatically records when a post was published.
- Runs the LinkedIn publisher on a daily schedule.

---

## Project Structure

```text
LeetCodes/
│
├── content/
│   ├── posts.json
│   │
│   ├── images/
│   │   └── *.png
│   │
│   └── codes/
│       └── finished/
│           ├── easy/
│           ├── medium/
│           └── hard/
│
├── helper/
│   ├── captions.py
│   ├── images.py
│   ├── generate_content.py
│   ├── linkedin.py
│   └── prompt.txt
│
├── .github/
│   └── workflows/
│       └── linkedin.yml
│
└── main.py
```

### `content/codes/finished/`

Contains completed solutions.

The directory determines the difficulty:

```text
medium/ → Medium
hard/   → Hard
```

`easy/` and `attempted/` are intentionally ignored by the content generator.

### `content/images/`

Contains the Ray.so-generated PNG images corresponding to each solution.

### `content/posts.json`

Acts as the central database for generated posts and their publishing state.

Each entry contains information similar to:

```json
{
    "title": "LeetCode 150. Evaluate Reverse Polish Notation",
    "difficulty": "Medium",
    "posted": false,
    "posted_at": null,
    "caption": "LeetCode 150. Evaluate Reverse Polish Notation\n\nDifficulty: Medium\n\n...",
    "code": "content/codes/finished/medium/150. Evaluate Reverse Polish Notation.py",
    "image": "content/images/150. Evaluate Reverse Polish Notation.png"
}
```

After successful publication:

```json
{
    "posted": true,
    "posted_at": "2026-09-03T18:00:00+00:00"
}
```

---

## Content Generation

The local generator is started with:

```bash
python helper/genereate_content.py
```

It performs two main phases.

### 1. Image Generation

The generator searches:

```text
content/codes/finished/medium/
content/codes/finished/hard/
```

For each solution without an existing image, it opens Ray.so using Playwright, enters the problem title and source code, selects a theme, and exports the result as a PNG.

Existing images are skipped.

### 2. Caption Generation

The solution is then sent to a locally running LLM through LM Studio.

The model receives:

- Problem name
- Programming language
- Actual source code
- Writing instructions from `helper/prompt.txt`

The generated caption is stored in `content/posts.json`.

The difficulty is determined from the solution's directory rather than being guessed by the model.

---

## Local LLM

Caption generation uses the OpenAI-compatible API provided by LM Studio.

Current model:

```text
qwen_3_4b-safetensors
```

The application connects to:

```text
http://localhost:1234/v1
```

Make sure LM Studio is running and its local server is enabled before generating captions.

The model can be changed in:

```text
helper/captions.py
```

```python
MODEL = "qwen_3_4b-safetensors"
```

---

## Image Generation

Images are generated with Playwright and Ray.so.

The project does not require Node.js or the Ray.so npm package.

The image generator uses a predefined collection of Ray.so themes and assigns a theme deterministically based on the problem name. This means running the generator again will produce the same theme for a given problem.

---

## LinkedIn Publishing

`main.py` handles publishing.

It reads:

```text
content/posts.json
```

and searches for the first entry where:

```json
"posted": false
```

It then:

1. Checks that the image exists.
2. Checks that the caption is not empty.
3. Uploads the image.
4. Publishes the post to LinkedIn.
5. Marks the entry as posted.
6. Records `posted_at`.
7. Saves `posts.json`.

Only after LinkedIn successfully returns a post ID is the entry marked as posted.

This prevents failed publishing attempts from consuming a post.

---

## GitHub Actions

The LinkedIn publisher runs through:

```text
.github/workflows/linkedin.yml
```

The workflow is scheduled for **21:00 Asia/Tehran** every day and can also be triggered manually.

The workflow:

```text
Checkout repository
        ↓
Install Python
        ↓
Install requests
        ↓
Run main.py
        ↓
Publish one unposted post
        ↓
Update content/posts.json
        ↓
Commit changes
        ↓
Push changes back to GitHub
```

The GitHub Action does **not** generate captions or images.

Those steps require the local environment and LM Studio, so the intended workflow is:

```text
Local machine
    ↓
Generate images + captions
    ↓
Commit/push repository
    ↓
GitHub Actions
    ↓
Publish one post per day
```

---

## GitHub Secrets

The LinkedIn workflow expects the following repository secret:

```text
LINKEDIN_ACCESS_TOKEN
```

The token is provided to the workflow through:

```yaml
env:
  LINKEDIN_ACCESS_TOKEN: ${{ secrets.LINKEDIN_ACCESS_TOKEN }}
```

Never commit the access token directly to the repository.

---

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install openai playwright requests
```

Install the Playwright browser:

```bash
playwright install chromium
```

---

## Generating Content

Make sure LM Studio is running with its local server enabled.

Then:

```bash
python helper/genereate_content.py
```

The generator will process all eligible solutions that have not already been generated.

---

## Publishing Manually

To run the LinkedIn publisher locally:

```bash
python main.py
```

The required LinkedIn access token must be available in the environment:

```bash
export LINKEDIN_ACCESS_TOKEN="your-token"
```

On successful publication, `content/posts.json` is updated automatically.

---

## Design Decisions

### `posts.json` as the source of truth

Instead of maintaining separate files for captions, posting state, and metadata, the project keeps them together in `content/posts.json`.

This makes each post self-contained:

```text
Problem
├── Title
├── Difficulty
├── Caption
├── Code path
├── Image path
└── Posting state
```

### Difficulty comes from the filesystem

The difficulty is determined from:

```text
content/codes/finished/<difficulty>/
```

rather than asking the LLM to determine it.

This avoids unnecessary model inference and guarantees that the stored difficulty matches the folder containing the solution.

### One post per workflow run

`main.py` intentionally stops after successfully publishing one solution.

This prevents a single GitHub Actions run from accidentally publishing the entire backlog.

### Generate once, publish later

Content generation and publishing are separate processes.

This allows the local machine to handle the heavier tasks:

- Browser automation
- Ray.so
- Local LLM inference

while GitHub Actions only handles the lightweight publishing process.

---

## Current Workflow

The intended daily workflow is:

```text
1. Solve LeetCode
        ↓
2. Save solution in medium/ or hard/
        ↓
3. Run local content generator
        ↓
4. Ray.so generates image
        ↓
5. LM Studio generates caption
        ↓
6. posts.json is updated
        ↓
7. Push repository to GitHub
        ↓
8. GitHub Actions runs at 21:00
        ↓
9. One post is published
        ↓
10. posts.json records the publication
```

The result is a simple separation of responsibilities:

**Local machine → create content**

**GitHub Actions → publish content**
