# Album Art Generator

Command‑line utility for bulk‑generating AI album covers that vary in style, comply with genre‑specific keywords, stamp text onto each image, and export at custom dimensions.

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
export OPENAI_API_KEY="sk‑..."
python main.py --genre rock --count 50 --size 1024x1024 --output covers
```
Resulting PNGs land in **covers/**.

## Features
* **1 – 2000** covers in one run.
* Genre‑aware prompt construction driven by `config/keywords.json`.
* Randomised style layer ensures visual diversity.
* Text overlay of selected keywords or custom album title.
* Guarantees no prompt duplication in a single batch.
* Pluggable image backend (OpenAI DALL‑E by default).

## Configuration
Edit `config/keywords.json` to tune per‑genre keyword pools.

## Extending
Implement additional providers by adding a class in `generator.py`
that exposes a `generate(prompt, size)->bytes` method.

## License
MIT. See LICENSE.
