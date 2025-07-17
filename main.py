import argparse, os
from generator import AlbumGenerator

def cli():
    p = argparse.ArgumentParser()
    p.add_argument("--genre", required=True)
    p.add_argument("--count", type=int, default=1)
    p.add_argument("--size", default="1024x1024")
    p.add_argument("--output", default="output")
    p.add_argument("--title_mode", choices=["keywords", "none"], default="keywords")
    args = p.parse_args()
    os.makedirs(args.output, exist_ok=True)
    gen = AlbumGenerator()
    for _ in range(args.count):
        gen.create_cover(args.genre, args.size, args.output, args.title_mode)

if __name__ == "__main__":
    cli()
