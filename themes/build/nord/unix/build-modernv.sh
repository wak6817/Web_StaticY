#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/nord/modernv/assets/icons"

cat "$ROOT/src/nord/colorv/interactions.css" \
    "$ROOT/src/nord/colorv/other.css" \
    "$ROOT/src/nord/colorv/text.css" \
    "$ROOT/src/nord/modernv/fonts.css" \
    "$ROOT/src/nord/modernv/margins.css" \
    "$ROOT/src/nord/trans.css" \
    "$ROOT/src/nord/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/nord/modernv/style.css"

cp "$ROOT/sounds/modernv/sound.js" "$ROOT/build/dist/nord/modernv/"
cp "$ROOT/sounds/modernv/clickbtn.wav" "$ROOT/build/dist/nord/modernv/assets/"

cp -r "$ROOT/icons/." "$ROOT/build/dist/nord/modernv/assets/icons/"
