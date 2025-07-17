import random
STYLES = [
    "digital painting",
    "photorealistic",
    "vector art",
    "retro comic style",
    "surreal collage",
    "watercolor",
    "low‑poly 3D render"
]
def pick_style():
    return random.choice(STYLES)
