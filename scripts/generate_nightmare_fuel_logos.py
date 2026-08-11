"""Generate standalone Nightmare Fuel SVG variants from the core logo artwork."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.svgLib.path.parser import parse_path
from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE_LOGO = ROOT / "public" / "assets" / "logo.svg"
OUTPUT_DIR = ROOT / "public" / "assets"
VIEWBOX_X = -20
VIEWBOX_Y = 25
VIEWBOX_WIDTH = 1517
VIEWBOX_HEIGHT = 525
LOCKUP_CENTER_X = VIEWBOX_X + (VIEWBOX_WIDTH / 2)


@dataclass(frozen=True)
class Variant:
    filename: str
    title: str
    nightmare: str
    fuel: str
    contour: str


VARIANTS = (
    Variant(
        "logo-nightmare-fuel.svg",
        "Nightmare Fuel — Slime Signal",
        "#5EFD02",
        "#FFFFFF",
        "#FF2BD6",
    ),
    Variant(
        "logo-nightmare-fuel-aftershock-yellow.svg",
        "Nightmare Fuel — Aftershock Yellow",
        "#00E5FF",
        "#FBEA00",
        "#FF2BD6",
    ),
    Variant(
        "logo-nightmare-fuel-blood-moon.svg",
        "Nightmare Fuel — Blood Moon",
        "#FF334D",
        "#ECEBE4",
        "#FF2BD6",
    ),
    Variant(
        "logo-nightmare-fuel-midnight-signal.svg",
        "Nightmare Fuel — Midnight Signal",
        "#00E5FF",
        "#FFFFFF",
        "#9B5CFF",
    ),
)


def path_bounds(path_data: str) -> tuple[float, float, float, float]:
    pen = BoundsPen(None)
    parse_path(path_data, pen)
    if pen.bounds is None:
        raise ValueError("Path has no drawable bounds")
    return pen.bounds


def nightmare_path_without_article(source: str) -> str:
    tags = re.findall(r"<path\b[^>]*(?:></path>|/>)", source)
    if len(tags) < 3:
        raise ValueError("Core logo does not contain the expected path layers")

    match = re.search(r' d="([^"]+)"', tags[2])
    if not match:
        raise ValueError("Nightmare wordmark path data was not found")

    parts = re.findall(r"M[^M]+", match.group(1))
    kept: list[str] = []
    removed = 0
    for part in parts:
        min_x, min_y, max_x, max_y = path_bounds(part)
        is_article_a = 230 <= min_x <= 270 and max_x <= 310 and max_y <= 105
        is_hairline_artifact = (max_x - min_x) <= 1 or (max_y - min_y) <= 1
        if is_article_a:
            removed += 1
        elif is_hairline_artifact:
            continue
        else:
            kept.append(part)

    if removed != 2:
        raise ValueError(f"Expected to remove two isolated A subpaths, removed {removed}")
    return "".join(kept)


def text_path(font_path: Path, text: str, target_height: float, center_y: float) -> str:
    font = TTFont(font_path)
    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()
    metrics = font["hmtx"].metrics

    glyph_names = [cmap[ord(character)] for character in text]

    bounds_pen = BoundsPen(glyph_set)
    cursor = 0
    for name in glyph_names:
        glyph_set[name].draw(TransformPen(bounds_pen, (1, 0, 0, 1, cursor, 0)))
        cursor += metrics[name][0]
    if bounds_pen.bounds is None:
        raise ValueError(f'Text "{text}" has no drawable bounds')

    min_x, min_y, max_x, max_y = bounds_pen.bounds
    scale = target_height / (max_y - min_y)
    content_width = (max_x - min_x) * scale
    start_x = LOCKUP_CENTER_X - (content_width / 2) - min_x * scale
    baseline = center_y + ((min_y + max_y) * scale / 2)

    paths: list[str] = []
    cursor = 0
    for name in glyph_names:
        svg_pen = SVGPathPen(glyph_set)
        transform = (scale, 0, 0, -scale, start_x + cursor * scale, baseline)
        glyph_set[name].draw(TransformPen(svg_pen, transform))
        paths.append(svg_pen.getCommands())
        cursor += metrics[name][0]
    return "".join(paths)


def layered_paths(path_data: str, fill: str, contour: str, layer_name: str) -> str:
    return "".join(
        (
            f'<path data-layer="{layer_name}-contour" fill="{contour}" stroke="{contour}" '
            f'stroke-width="20" stroke-linejoin="round" paint-order="stroke fill" d="{path_data}"/>',
            f'<path data-layer="{layer_name}-shadow" fill="#000000" stroke="#000000" '
            f'stroke-width="12" stroke-linejoin="round" paint-order="stroke fill" d="{path_data}"/>',
            f'<path data-layer="{layer_name}" fill="{fill}" d="{path_data}"/>',
        )
    )


def render_svg(variant: Variant, nightmare: str, fuel: str) -> str:
    nightmare_layers = layered_paths(nightmare, variant.nightmare, variant.contour, "nightmare")
    fuel_layers = layered_paths(fuel, variant.fuel, variant.contour, "fuel")
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VIEWBOX_X} {VIEWBOX_Y} '
        f'{VIEWBOX_WIDTH} {VIEWBOX_HEIGHT}" width="{VIEWBOX_WIDTH}" height="{VIEWBOX_HEIGHT}" '
        'role="img" aria-label="Nightmare Fuel">'
        f"<title>{variant.title}</title>"
        f'<g data-lockup="nightmare-fuel">{nightmare_layers}{fuel_layers}</g>'
        "</svg>\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--font", required=True, type=Path, help="Path to Anton-Regular.ttf")
    args = parser.parse_args()

    source = SOURCE_LOGO.read_text(encoding="utf-8")
    nightmare = nightmare_path_without_article(source)
    # Match the 99.5-unit height of the original ON / STREET supporting type.
    fuel = text_path(args.font, "FUEL", target_height=99.5, center_y=470)

    for variant in VARIANTS:
        output = OUTPUT_DIR / variant.filename
        output.write_text(render_svg(variant, nightmare, fuel), encoding="utf-8", newline="\n")
        print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
