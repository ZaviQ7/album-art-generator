from PIL import Image, ImageDraw, ImageFont

def overlay(path, text):
    im = Image.open(path).convert("RGBA")
    txt_layer = Image.new("RGBA", im.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)
    font_size = max(24, im.height // 15)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except OSError:
        font = ImageFont.load_default()
    w, h = draw.textsize(text, font=font)
    pos = ((im.width - w) // 2, im.height - h - 20)
    draw.text(pos, text, font=font, fill=(255, 255, 255, 255))
    out = Image.alpha_composite(im, txt_layer)
    out.convert("RGB").save(path, "PNG")
