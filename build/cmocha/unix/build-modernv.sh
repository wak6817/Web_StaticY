#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/cmocha/modernv/assets/icons"

cat "$ROOT/src/cmocha/colorv/interactions.css" \
    "$ROOT/src/cmocha/colorv/other.css" \
    "$ROOT/src/cmocha/colorv/text.css" \
    "$ROOT/src/cmocha/modernv/fonts.css" \
    "$ROOT/src/cmocha/modernv/margins.css" \
    "$ROOT/src/cmocha/trans.css" \
    "$ROOT/src/cmocha/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/cmocha/modernv/style.css" # make sure it exists empty

cp "$ROOT/sounds/modernv/sound.js" "$ROOT/build/dist/cmocha/modernv/"
cp "$ROOT/sounds/modernv/clickbtn.wav" "$ROOT/build/dist/cmocha/modernv/assets/"

cp -r "$ROOT/icons/." "$ROOT/build/dist/cmocha/modernv/assets/icons/"
