#!/usr/bin/env python3

import json
import re
from pathlib import Path


COLOR_NAMES = [
    "rosewater", "flamingo", "pink", "mauve", "red", "maroon", "peach",
    "yellow", "green", "teal", "sky", "sapphire", "blue", "lavender",
    "text", "subtext1", "subtext0", "overlay2", "overlay1", "overlay0",
    "surface2", "surface1", "surface0", "base", "mantle", "crust",
]


def read_file(path: Path) -> str | None:
    try:
        return path.read_text()
    except FileNotFoundError:
        return None


def valid_name(name: str | None) -> bool:
    return bool(name and re.fullmatch(r"[\w_-]+", name))


def extract_colors(css: str) -> dict[str, str]:
    colors: dict[str, str] = {}
    for name, value in re.findall(r"--([\w_-]+)\s*:\s*(#[\da-fA-F]+)\s*;", css):
        colors[name] = value
    return colors


def export_theme() -> None:
    print("colorscheme to export: cfrappe, clatte, cmocha, dracula or nord")
    colorscheme = input().strip()

    if colorscheme in {"nord", "dracula"}:
        print("not supported yet")
        return

    if not valid_name(colorscheme):
        print("write cfrappe, clatte, cmocha, dracula or nord")
        return

    destination = input("where should exported.jsonc be saved? ").strip()
    if not destination:
        print("destination is required")
        return

    css = read_file(Path("src") / colorscheme / "trans.css")
    if not css:
        print("colorscheme does not exist")
        return

    colors = extract_colors(css)
    output = {"name": colorscheme, "colors": {}}

    for name in COLOR_NAMES:
        value = colors.get(name)
        if not value:
            print(f"colorscheme is missing --{name}")
            return
        output["colors"][name] = value

    output_path = Path(destination) / "exported.jsonc"
    output_path.write_text(json.dumps(output, indent=2) + "\n")
    print(f"exported to {output_path}")


if __name__ == "__main__":
    export_theme()
