#!/usr/bin/env python3
"""Generate the extension's minimal back-arrow icons."""

from pathlib import Path

from PIL import Image, ImageDraw

SIZES = (16, 32, 48, 128)
SCALE = 8
ORANGE = "#ff4500"
WHITE = "#ffffff"


def generate_icon(size: int, destination: Path) -> None:
    canvas_size = size * SCALE
    image = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    inset = round(canvas_size * 0.04)
    radius = round(canvas_size * 0.22)
    draw.rounded_rectangle(
        (inset, inset, canvas_size - inset, canvas_size - inset),
        radius=radius,
        fill=ORANGE,
    )

    def point(x: float, y: float) -> tuple[int, int]:
        return round(canvas_size * x), round(canvas_size * y)

    width = max(SCALE, round(canvas_size * 0.115))
    line = [point(0.75, 0.5), point(0.25, 0.5)]
    arrow = [point(0.42, 0.32), point(0.25, 0.5), point(0.42, 0.68)]
    draw.line(line, fill=WHITE, width=width)
    draw.line(arrow, fill=WHITE, width=width, joint="curve")

    cap_radius = width // 2
    for x, y in (line[0], arrow[0], arrow[-1]):
        draw.ellipse(
            (x - cap_radius, y - cap_radius, x + cap_radius, y + cap_radius),
            fill=WHITE,
        )

    image.resize((size, size), Image.Resampling.LANCZOS).save(destination)


def main() -> None:
    icons_dir = Path(__file__).resolve().parent.parent / "icons"
    icons_dir.mkdir(exist_ok=True)
    for size in SIZES:
        generate_icon(size, icons_dir / f"icon-{size}.png")


if __name__ == "__main__":
    main()
