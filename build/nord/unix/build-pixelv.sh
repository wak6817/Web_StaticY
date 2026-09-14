#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/nord/pixelv/assets/icons"

cat "$ROOT/src/nord/colorv/interactions.css" \
    "$ROOT/src/nord/colorv/other.css" \
    "$ROOT/src/nord/colorv/text.css" \
    "$ROOT/src/nord/pixelv/fonts.css" \
    "$ROOT/src/nord/pixelv/margins.css" \
    "$ROOT/src/nord/trans.css" \
    "$ROOT/src/nord/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/nord/pixelv/style.css"

cp "$ROOT/sounds/pixelv/sound.js" "$ROOT/build/dist/nord/pixelv/"
cp "$ROOT/sounds/pixelv/clickbtn.wav" "$ROOT/build/dist/nord/pixelv/assets/"

cp -r "$ROOT/icons/." "$ROOT/build/dist/nord/pixelv/assets/icons/"
