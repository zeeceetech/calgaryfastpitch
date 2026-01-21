#!/usr/bin/env python3
"""Generate raster favicon PNGs and an ICO from an SVG source.

Usage: python scripts/generate_favicons.py <source-svg> <output-dir>
Produces: favicon-16.png, favicon-32.png, favicon-48.png, favicon.png (32x32), favicon.ico
"""
import sys
from pathlib import Path
from io import BytesIO

try:
    import cairosvg
    from PIL import Image
except Exception as e:
    print("Required packages are missing:", e)
    print("Run: python -m pip install cairosvg pillow")
    sys.exit(2)


def svg_to_png_bytes(svg_path: Path, size: int) -> bytes:
    # Render SVG to PNG bytes at given square size
    png_bytes = cairosvg.svg2png(url=str(svg_path), output_width=size, output_height=size)
    return png_bytes


def main():
    if len(sys.argv) < 3:
        print("Usage: generate_favicons.py <source-svg> <output-dir>")
        sys.exit(1)

    src = Path(sys.argv[1])
    out = Path(sys.argv[2])
    if not src.exists():
        print(f"Source SVG not found: {src}")
        sys.exit(1)
    out.mkdir(parents=True, exist_ok=True)

    sizes = [16, 32, 48]
    png_files = []
    for s in sizes:
        png_data = svg_to_png_bytes(src, s)
        p = out / f"favicon-{s}.png"
        p.write_bytes(png_data)
        png_files.append(p)
        print(f"Wrote {p}")

    # also create a generic favicon.png (32x32)
    favicon32 = out / "favicon.png"
    favicon32.write_bytes(svg_to_png_bytes(src, 32))
    print(f"Wrote {favicon32}")

    # create multi-size ICO from PNGs
    imgs = [Image.open(p).convert("RGBA") for p in png_files]
    ico_path = out / "favicon.ico"
    # Save first image but include sizes for ICO
    imgs[0].save(ico_path, format="ICO", sizes=[(s, s) for s in sizes])
    print(f"Wrote {ico_path}")


if __name__ == '__main__':
    main()
