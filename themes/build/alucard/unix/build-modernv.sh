#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/alucard/modernv/assets/icons"

cat "$ROOT/src/alucard/colorv/interactions.css" \
    "$ROOT/src/alucard/colorv/other.css" \
    "$ROOT/src/alucard/colorv/text.css" \
    "$ROOT/src/alucard/modernv/fonts.css" \
    "$ROOT/src/alucard/modernv/margins.css" \
    "$ROOT/src/alucard/trans.css" \
    "$ROOT/src/alucard/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/alucard/modernv/style.css" # make sure it exists empty

cp "$ROOT/sounds/modernv/sound.js" "$ROOT/build/dist/alucard/modernv/"
cp "$ROOT/sounds/modernv/clickbtn.wav" "$ROOT/build/dist/alucard/modernv/assets/"

cp -r "$ROOT/icons/." "$ROOT/build/dist/alucard/modernv/assets/icons/"
