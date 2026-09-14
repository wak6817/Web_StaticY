#!/usr/bin/env python3

from pathlib import Path
import sys
import shutil


SCHEMES = {
    "catppuccin": [
        "clatte",
        "cfrappe",
        "cmacchiato",
        "cmocha",
    ],
    "dracula": [
        "dracula",
        "alucard",
    ],
    "other": [
        "nord",
    ],
}

VERSIONS = ["colorv", "modernv", "pixelv"]
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = PROJECT_ROOT / "themes"
OUTPUT_ROOT = PROJECT_ROOT / "build" / "dist"


def build(script: str) -> None:
    script_path = Path(script)
    scheme = script_path.parts[-3]
    version = script_path.stem.removeprefix("build-")
    source = SOURCE_ROOT / "src" / scheme
    output = OUTPUT_ROOT / scheme / version
    output.mkdir(parents=True, exist_ok=True)

    shared = [
        source / "colorv" / "interactions.css",
        source / "colorv" / "other.css",
        source / "colorv" / "text.css",
    ]
    if version == "colorv":
        files = shared + [source / "trans.css", source / "api.css", SOURCE_ROOT / "src" / "templates.css"]
    else:
        files = shared + [
            source / version / "fonts.css",
            source / version / "margins.css",
            source / "trans.css",
            source / "api.css",
            SOURCE_ROOT / "src" / "templates.css",
        ]

    with (output / "style.css").open("w", encoding="utf-8") as destination:
        for file in files:
            destination.write(file.read_text(encoding="utf-8"))

    if version != "colorv":
        shutil.copy2(SOURCE_ROOT / "sounds" / version / "sound.js", output / "sound.js")
        assets = output / "assets"
        assets.mkdir(exist_ok=True)
        shutil.copy2(SOURCE_ROOT / "sounds" / version / "clickbtn.wav", assets / "clickbtn.wav")
        icons = assets / "icons"
        shutil.copytree(SOURCE_ROOT / "icons", icons, dirs_exist_ok=True)


def build_all() -> None:
    for schemes_list in SCHEMES.values():
        for scheme in schemes_list:
            for version in VERSIONS:
                build(f"build/{scheme}/unix/build-{version}.sh")


def build_scheme(scheme: str) -> None:
    print("color version, modern version or pixel art version")
    version = input().strip()

    if version == "*":
        for item in VERSIONS:
            build(f"build/{scheme}/unix/build-{item}.sh")
    elif version == "color version":
        build(f"build/{scheme}/unix/build-colorv.sh")
    elif version == "modern version":
        build(f"build/{scheme}/unix/build-modernv.sh")
    elif version == "pixel art version":
        build(f"build/{scheme}/unix/build-pixelv.sh")
    else:
        print("write color version, modern version or pixel art version")
        build_scheme(scheme)
        return

    print("building file in /build/dist/")


def choose_colorscheme() -> None:
    print("Catppuccin, Dracula, Other, or *")
    choice = input().strip()

    if choice == "*":
        build_all()
        print("building everything in /build/dist/")
        return

    if choice in {"Catppuccin", "catppuccin"}:
        print("Latte, Frappe, Macchiato, Mocha, or *")
        colorscheme = input().strip()

        if colorscheme == "*":
            for scheme in SCHEMES["catppuccin"]:
                build_scheme(scheme)
        elif colorscheme in {"Latte", "latte"}:
            build_scheme("clatte")
        elif colorscheme in {"Frappe", "frappe"}:
            build_scheme("cfrappe")
        elif colorscheme in {"Macchiato", "macchiato"}:
            build_scheme("cmacchiato")
        elif colorscheme in {"Mocha", "mocha"}:
            build_scheme("cmocha")
        else:
            choose_colorscheme()
    elif choice in {"Dracula", "dracula"}:
        print("Dracula, Alucard, or *")
        colorscheme = input().strip()

        if colorscheme == "*":
            for scheme in SCHEMES["dracula"]:
                build_scheme(scheme)
        elif colorscheme in {"Dracula", "dracula"}:
            build_scheme("dracula")
        elif colorscheme in {"Alucard", "alucard"}:
            build_scheme("alucard")
        else:
            choose_colorscheme()
    elif choice in {"Other", "other"}:
        print("Nord or *")
        colorscheme = input().strip()

        if colorscheme in {"*", "Nord", "nord"}:
            build_scheme("nord")
        else:
            choose_colorscheme()
    else:
        print("Please choose Catppuccin, Dracula, Other, or *")
        choose_colorscheme()


if __name__ == "__main__":
    choose_colorscheme()
