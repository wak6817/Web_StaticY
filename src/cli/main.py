import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog="nbdmt",
            description="No bullshit Developer Multi tool",
        )

        subparsers = parser.add_subparsers(dest="command")

        subparsers.add_parser("ienv")
        subparsers.add_parser("bthemes")
        subparsers.add_parser("ctemp")

        args = parser.parse_args()

        if args.command == "ienv":
            subprocess.run(
                ["sh", SCRIPTS / "env-init.sh"],
                check=True,
            )

        elif args.command == "bthemes":
            subprocess.run(
                ["sh", SCRIPTS / "build-themes.sh"],
                check=True,
            )

        elif args.command == "ctemp":
            temp = ROOT / "tests" / "temp"

            if temp.exists():
                import shutil
                shutil.rmtree(temp)


if __name__ == "__main__":
    Main()