import os, json, random, uuid, requests
from text_overlay import overlay
from style import pick_style

import openai

KEYWORDS = json.load(open(os.path.join(os.path.dirname(__file__), "config", "keywords.json")))

class AlbumGenerator:
    def __init__(self):
        self.seen_prompts = set()

    def build_prompt(self, genre):
        pool = KEYWORDS[genre]
        n = random.randint(1, min(4, len(pool)))
        kws = random.sample(pool, n)
        style = pick_style()
        prompt = f"{genre} album cover, {', '.join(kws)}, {style}"
        while prompt in self.seen_prompts:
            prompt = self.build_prompt(genre)
        self.seen_prompts.add(prompt)
        return prompt, kws

    def fetch_image(self, prompt, size):
        resp = openai.Images.generate(prompt=prompt, n=1, size=size, model="dall-e-3")
        url = resp.data[0].url
        return requests.get(url).content

    def create_cover(self, genre, size, out_dir, title_mode):
        prompt, kws = self.build_prompt(genre)
        img_bytes = self.fetch_image(prompt, size)
        fname = f"{uuid.uuid4().hex}.png"
        path = os.path.join(out_dir, fname)
        with open(path, "wb") as f:
            f.write(img_bytes)
        if title_mode == "keywords":
            overlay(path, ' '.join(kws).title())
        return path
