#!/usr/bin/env python3

import shutil
import sys
from pathlib import Path


def read_path(prompt: str) -> str:
    return input(prompt).strip()


def main() -> None:
    source = read_path("where should files be imported from? ")
    destination = read_path("where should the imported files go? ")

    if not source or not destination:
        sys.stderr.write("source and destination are required.\n")
        raise SystemExit(1)

    try:
        shutil.move(source, destination)
    except Exception:
        sys.stderr.write("could not move the imported files.\n")
        raise SystemExit(1)

    sys.stdout.write(f"imported files moved to {destination}.\n")


if __name__ == "__main__":
    main()
