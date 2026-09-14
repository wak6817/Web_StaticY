#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/dracula/pixelv/assets/icons"

cat "$ROOT/src/dracula/colorv/interactions.css" \
    "$ROOT/src/dracula/colorv/other.css" \
    "$ROOT/src/dracula/colorv/text.css" \
    "$ROOT/src/dracula/pixelv/fonts.css" \
    "$ROOT/src/dracula/pixelv/margins.css" \
    "$ROOT/src/dracula/trans.css" \
    "$ROOT/src/dracula/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/dracula/pixelv/style.css"

cp "$ROOT/sounds/pixelv/sound.js" "$ROOT/build/dist/dracula/pixelv/"
cp "$ROOT/sounds/pixelv/clickbtn.wav" "$ROOT/build/dist/dracula/pixelv/assets/"

cp -r "$ROOT/icons/." "$ROOT/build/dist/dracula/pixelv/assets/icons/"
