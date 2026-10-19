#!/usr/bin/env python3
"""Optional: render extra emoji icons to transparent 256x256 PNGs.

The skill already ships its icons in assets/icons/. Use this script only to add
an icon that is not bundled. Requires Pillow and a CBDT color emoji font such as
Noto Color Emoji (on Windows/macOS, download NotoColorEmoji.ttf and pass --font).

Usage:
  python render_emoji.py --font /path/NotoColorEmoji.ttf --out ../assets/icons tent=🏕️ bus=🚌
"""
import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont

DEFAULT_FONTS = [
    "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf",
    "/usr/share/fonts/noto/NotoColorEmoji.ttf",
    os.path.expanduser("~/Library/Fonts/NotoColorEmoji.ttf"),
    os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", "NotoColorEmoji.ttf"),
]
STRIKE = 109  # the only valid bitmap strike size for Noto Color Emoji (CBDT)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("icons", nargs="+", help="name=emoji pairs, e.g. bus=🚌")
    ap.add_argument("--font", default=os.environ.get("EMOJI_FONT"), help="path to NotoColorEmoji.ttf")
    ap.add_argument("--out", default="assets/icons", help="output folder (default: assets/icons)")
    args = ap.parse_args()

    font_path = args.font or next((f for f in DEFAULT_FONTS if os.path.exists(f)), None)
    if not font_path or not os.path.exists(font_path):
        sys.exit("Noto Color Emoji font not found. Pass --font /path/to/NotoColorEmoji.ttf")
    font = ImageFont.truetype(font_path, STRIKE)
    os.makedirs(args.out, exist_ok=True)

    for pair in args.icons:
        name, _, ch = pair.partition("=")
        if not name or not ch:
            sys.exit(f"Bad argument {pair!r}; expected name=emoji")
        img = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
        ImageDraw.Draw(img).text((80, 80), ch, font=font, embedded_color=True, anchor="mm")
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
        size = max(img.size)
        canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        canvas.paste(img, ((size - img.width) // 2, (size - img.height) // 2))
        canvas = canvas.resize((256, 256), Image.LANCZOS)
        path = os.path.join(args.out, f"{name}.png")
        canvas.save(path)
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
