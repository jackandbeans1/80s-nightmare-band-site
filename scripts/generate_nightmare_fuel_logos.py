"""Generate standalone Nightmare Fuel SVG variants from the core logo artwork."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw
from fontTools.pens.basePen import BasePen
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
VIEWBOX_HEIGHT = 410
LOCKUP_CENTER_X = VIEWBOX_X + (VIEWBOX_WIDTH / 2)


class FlattenPen(BasePen):
    """Approximate SVG curves as polygons for lower-letter reconstruction."""

    def __init__(self, steps: int = 18) -> None:
        super().__init__(None)
        self.steps = steps
        self.contours: list[list[tuple[float, float]]] = []
        self.current: list[tuple[float, float]] = []

    def _moveTo(self, point: tuple[float, float]) -> None:
        if self.current:
            self.contours.append(self.current)
        self.current = [point]

    def _lineTo(self, point: tuple[float, float]) -> None:
        self.current.append(point)

    def _curveToOne(
        self,
        control_1: tuple[float, float],
        control_2: tuple[float, float],
        point: tuple[float, float],
    ) -> None:
        start = self._getCurrentPoint()
        for index in range(1, self.steps + 1):
            t = index / self.steps
            inverse = 1 - t
            self.current.append(
                (
                    inverse**3 * start[0]
                    + 3 * inverse**2 * t * control_1[0]
                    + 3 * inverse * t**2 * control_2[0]
                    + t**3 * point[0],
                    inverse**3 * start[1]
                    + 3 * inverse**2 * t * control_1[1]
                    + 3 * inverse * t**2 * control_2[1]
                    + t**3 * point[1],
                )
            )

    def _qCurveToOne(
        self, control: tuple[float, float], point: tuple[float, float]
    ) -> None:
        start = self._getCurrentPoint()
        for index in range(1, self.steps + 1):
            t = index / self.steps
            inverse = 1 - t
            self.current.append(
                (
                    inverse**2 * start[0] + 2 * inverse * t * control[0] + t**2 * point[0],
                    inverse**2 * start[1] + 2 * inverse * t * control[1] + t**2 * point[1],
                )
            )

    def _closePath(self) -> None:
        if self.current:
            self.contours.append(self.current)
            self.current = []

    def _endPath(self) -> None:
        self._closePath()


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


def reconstruct_lower_letters(
    nightmare: str, cutoff_y: int = 285, baseline_y: int = 402
) -> tuple[str, str]:
    """Extrude the surviving lower contours of I through R to a shared baseline."""

    pen = FlattenPen()
    parse_path(nightmare, pen)
    pen._endPath()

    mask = Image.new("1", (1477, 435), 0)
    draw = ImageDraw.Draw(mask)
    for contour in pen.contours:
        draw.polygon(contour, fill=1)

    pixels = mask.load()
    bottoms: dict[int, int] = {}
    for x in range(205, 1276):
        for y in range(baseline_y, cutoff_y - 1, -1):
            if pixels[x, y]:
                bottoms[x] = y
                break

    runs: list[list[int]] = []
    for x in sorted(bottoms):
        if not runs or x > runs[-1][-1] + 1:
            runs.append([x])
        else:
            runs[-1].append(x)

    fill_parts: list[str] = []
    outline_parts: list[str] = []
    baseline_pattern = (0, 2, -1, 3, 1, -2, 2)
    for run_index, run in enumerate(runs):
        if len(run) < 5:
            continue

        sampled_x = run[::4]
        if sampled_x[-1] != run[-1]:
            sampled_x.append(run[-1])

        top_points: list[tuple[int, int]] = []
        for x in sampled_x:
            window = [bottoms[value] for value in range(max(run[0], x - 2), min(run[-1], x + 2) + 1)]
            top_points.append((x, max(cutoff_y, max(window) - 10)))

        bottom_x = sampled_x[::4]
        if bottom_x[-1] != sampled_x[-1]:
            bottom_x.append(sampled_x[-1])
        bottom_points = [
            (x, baseline_y + baseline_pattern[(run_index + index) % len(baseline_pattern)])
            for index, x in enumerate(bottom_x)
        ]

        fill_points = top_points + list(reversed(bottom_points))
        fill_parts.append(
            "M"
            + "L".join(f"{x} {y}" for x, y in fill_points)
            + "Z"
        )
        outline_points = [top_points[0], bottom_points[0], *bottom_points[1:], top_points[-1]]
        outline_parts.append("M" + "L".join(f"{x} {y}" for x, y in outline_points))

    return "".join(fill_parts), "".join(outline_parts)


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


def reconstructed_nightmare_layers(
    nightmare: str,
    extension_fill: str,
    extension_outline: str,
    fill: str,
    contour: str,
) -> str:
    return "".join(
        (
            f'<path data-layer="nightmare-contour" fill="{contour}" stroke="{contour}" '
            f'stroke-width="20" stroke-linejoin="round" paint-order="stroke fill" d="{nightmare}"/>',
            f'<path data-layer="nightmare-shadow" fill="#000000" stroke="#000000" '
            f'stroke-width="12" stroke-linejoin="round" paint-order="stroke fill" d="{nightmare}"/>',
            f'<path data-layer="nightmare-reconstruction" fill="{fill}" d="{extension_fill}"/>',
            f'<path data-layer="nightmare" fill="{fill}" d="{nightmare}"/>',
            f'<path data-layer="nightmare-reconstruction-contour" fill="none" stroke="{contour}" '
            f'stroke-width="20" stroke-linecap="round" stroke-linejoin="round" d="{extension_outline}"/>',
            f'<path data-layer="nightmare-reconstruction-shadow" fill="none" stroke="#000000" '
            f'stroke-width="12" stroke-linecap="round" stroke-linejoin="round" d="{extension_outline}"/>',
        )
    )


def render_svg(
    variant: Variant,
    nightmare: str,
    extension_fill: str,
    extension_outline: str,
    fuel: str,
) -> str:
    nightmare_layers = reconstructed_nightmare_layers(
        nightmare, extension_fill, extension_outline, variant.nightmare, variant.contour
    )
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
    extension_fill, extension_outline = reconstruct_lower_letters(nightmare)
    # Match the 99.5-unit height of the original ON / STREET supporting type.
    fuel = text_path(args.font, "FUEL", target_height=99.5, center_y=350)

    for variant in VARIANTS:
        output = OUTPUT_DIR / variant.filename
        output.write_text(
            render_svg(variant, nightmare, extension_fill, extension_outline, fuel),
            encoding="utf-8",
            newline="\n",
        )
        print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
