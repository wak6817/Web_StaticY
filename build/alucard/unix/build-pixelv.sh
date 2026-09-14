#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/alucard/pixelv/assets/icons"

cat "$ROOT/src/alucard/colorv/interactions.css" \
    "$ROOT/src/alucard/colorv/other.css" \
    "$ROOT/src/alucard/colorv/text.css" \
    "$ROOT/src/alucard/pixelv/fonts.css" \
    "$ROOT/src/alucard/pixelv/margins.css" \
    "$ROOT/src/alucard/trans.css" \
    "$ROOT/src/alucard/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/alucard/pixelv/style.css" # make sure it exists empty

cp "$ROOT/sounds/pixelv/sound.js" "$ROOT/build/dist/alucard/pixelv/"
cp "$ROOT/sounds/pixelv/clickbtn.wav" "$ROOT/build/dist/alucard/pixelv/assets/"

cp -r "$ROOT/icons/." "$ROOT/build/dist/alucard/pixelv/assets/icons/"
