#!/usr/bin/env python3

import subprocess
import sys


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


def build(script: str) -> None:
    subprocess.run(["sh", script], check=False)


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
