#!/bin/sh

# Use printf for input

set -eu

printf '%s' "What is your username? "
if ! read -r answer; then
  printf '%s\n' "Could not read username" >&2
  exit 1
fi

USERNAME=$answer
YEAR=$(date +%Y)

PROJECT_DIR=$(pwd -P)

DESTINATION_ICON_DIR="$PROJECT_DIR/assets/icons"
DESTINATION_SOUND_DIR="$PROJECT_DIR/assets/sounds"

SOURCE_ICON_DIR=""
SOURCE_SOUND_DIR=""
SEARCH_DIR="$PROJECT_DIR"

while [ "$SEARCH_DIR" != "/" ]; do
  if [ -d "$SEARCH_DIR/assets/icons" ]; then
    SOURCE_ICON_DIR="$SEARCH_DIR/assets/icons"
    break
  fi
  SEARCH_DIR=$(dirname -- "$SEARCH_DIR")
done

printf '%s' "Are you running this script in the project directory? (y/n) "
if ! read -r answer; then
  printf '%s\n' "Could not read confirmation" >&2
    exit 1
fi

if [ "$answer" = "y" ] || [ "$answer" = "Y" ]; then
  echo "Continue"

  cat > README.md <<'EOF'
# THIS README.MD IS GENERATED

This project is a small starting point for building a static website with HTML, CSS, and TypeScript.

## Project structure

- `page/` contains the website files that visitors open in a browser.
- `page/index.html` is the homepage.
- `page/style.css` contains the page styles.
- `page/script.ts` is where interactive TypeScript code can be added.
- `src/` contains source files shared by the project.
- `assets/` stores fonts, icons, and other static resources.
- `scripts/` stores helper shell scripts.
- `dist/` is the destination for a published copy of the project.

## Start editing

Open `page/index.html` and add the structure of your page. For example:

```html
<main>
    <h1>Hello, web!</h1>
    <p>This is my first generated page.</p>
</main>
```

Add the appearance in `page/style.css`:

```css
body {
    max-width: 60rem;
    margin: 0 auto;
    padding: 2rem;
    font-family: sans-serif;
}
```

## Preview the website

From the project directory, start a local web server:

```sh
python -m http.server --directory page
```

Open `http://localhost:8000` in a browser. Stop the server with `Ctrl+C`.

## Add TypeScript

TypeScript source belongs in `page/script.ts`. Browsers do not run TypeScript directly, so compile it to JavaScript before using it in a page. The generated project installs TypeScript with npm; add a `tsconfig.json` and a build command when the project needs a repeatable TypeScript workflow.

Keep the generated source files in `page/` and copy the finished website to `dist/` only when you are ready to publish it.

## Copy files to `dist/`

The helper script is `scripts/run.sh`. Make it executable once, then run it from the project directory:

```sh
chmod +x scripts/run.sh
./scripts/run.sh
```

Review the contents of `dist/` after copying. Do not publish source files or local configuration accidentally.

## Version control

Initialize Git if this is a new project:

```sh
git init
git add .
git commit -m "Start generated website"
```

The generated `.gitignore` excludes macOS `.DS_Store` files. Add other machine-specific files if your editor or operating system creates them.

## Next steps

Try adding navigation, a second HTML page, responsive styles, and a small TypeScript interaction. Keep the site accessible by using semantic HTML, descriptive link text, keyboard-friendly controls, and readable color contrast.
EOF

  echo "Generated README.md"

  cat > LICENSE <<EOF
MIT License

Copyright (c) $YEAR $USERNAME

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

  echo "Generated LICENSE"

  cat > .gitignore <<EOF
.DS_Store
EOF

  echo "Generated .gitignore"

  mkdir -p src
  echo "Generated src/"

  mkdir -p assets/fonts assets/icons assets/sounds
  echo "Generated assets/"

  if [ -n "$SOURCE_ICON_DIR" ] && [ -d "$SOURCE_ICON_DIR" ]; then
    SOURCE_ICON_PATH=$(cd -- "$SOURCE_ICON_DIR" && pwd -P)
    DESTINATION_ICON_PATH=$(cd -- "$DESTINATION_ICON_DIR" && pwd -P)

    if [ "$SOURCE_ICON_PATH" = "$DESTINATION_ICON_PATH" ]; then
      echo "Icons already exist in the project directory"
    else
      cp -R "$SOURCE_ICON_PATH"/. "$DESTINATION_ICON_PATH"/
      echo "Copied icons"
    fi
  else
    echo "Warning: source icons were not found; continuing without copying icons"
  fi

  if [ -n "$SOURCE_SOUND_DIR" ] && [ -d "$SOURCE_SOUND_DIR" ]; then
    SOURCE_SOUND_PATH=$(cd -- "$SOURCE_SOUND_DIR" && pwd -P)
    DESTINATION_SOUND_PATH=$(cd -- "$DESTINATION_SOUND_DIR" && pwd -P)

    if [ "$SOURCE_SOUND_PATH" = "$DESTINATION_SOUND_PATH" ]; then
      echo "Sounds already exist in the project directory"
    else
      cp -R "$SOURCE_SOUND_PATH"/. "$DESTINATION_SOUND_PATH"/
      echo "Copied sounds"
    fi
  else
    echo "Warning: source sounds were not found; continuing without copying sounds"
  fi

  mkdir -p scripts
  echo "Generated scripts/"

  cat > scripts/inspector.py <<'EOF' #TODO: Find a better way to do this
from pathlib import Path
from collections import Counter
import subprocess

files = list(Path(".").rglob("*"))
line_count = 0

file_count = sum(file.is_file() for file in files)
directory_count = sum(file.is_dir() for file in files)

print(f"Files\t{file_count}")
print(f"Folders\t{directory_count}")

for file in files:
    if file.is_file():
        try:
            line_count += len(file.read_text().splitlines())
        except (UnicodeDecodeError, PermissionError):
            pass

print(f"Lines\t{line_count}")

try:
    branch = subprocess.check_output(
        ["git", "branch", "--show-current"],
        text=True
    ).strip()

    print("\nGit:")
    print(f"  Branch\n{branch}")

except subprocess.CalledProcessError:
    print("\nGit: Not a repository")

print("\nFiles:")
for file in files:
    print(f"  {file}")

extensions = Counter(
    file.suffix
    for file in files
    if file.is_file() and file.suffix
)

print("\nFile types:")
for extension, count in extensions.most_common():
    print(f" {extension}\t{count}")
EOF

  cat > scripts/run.sh <<'EOF'
#!/bin/sh
set -eu
cp -R src assets scripts page dist/
EOF

  echo "Generated scripts/run.sh"

  mkdir -p page
  touch page/index.html page/style.css page/script.ts
  echo "Generated page/"

  mkdir -p dist
  echo "Generated dist/"

  if command -v npm >/dev/null 2>&1; then
    npm init -y
    npm install --save-dev typescript

    echo "Installed TypeScript using npm"
  else
    echo "Warning: npm was not found."
    echo "Go to your Web_StaticY installation and run the scripts/download/<os-pkg>.sh script"
  fi

  python3 -m venv .venv
  python3 -m pip install --upgrade pip
  echo "Generated and updated Python environment"

  git init
  echo "Initialized Git"

  printf "\nThis could take a few seconds!\n"
else
  printf '%s\n' "Abort"
fi
