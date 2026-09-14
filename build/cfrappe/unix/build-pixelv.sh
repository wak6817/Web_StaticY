#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/cfrappe/pixelv/assets/icons"

cat "$ROOT/src/cfrappe/colorv/interactions.css" \
    "$ROOT/src/cfrappe/colorv/other.css" \
    "$ROOT/src/cfrappe/colorv/text.css" \
    "$ROOT/src/cfrappe/pixelv/fonts.css" \
    "$ROOT/src/cfrappe/pixelv/margins.css" \
    "$ROOT/src/cfrappe/trans.css" \
    "$ROOT/src/cfrappe/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/cfrappe/pixelv/style.css" # make sure it exists empty

cp "$ROOT/sounds/pixelv/sound.js" "$ROOT/build/dist/cfrappe/pixelv/"
cp "$ROOT/sounds/pixelv/clickbtn.wav" "$ROOT/build/dist/cfrappe/pixelv/assets/"

cp -r "$ROOT/icons/." "$ROOT/build/dist/cfrappe/pixelv/assets/icons/"
