#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/clatte/modernv/assets/icons"

cat "$ROOT/src/clatte/colorv/interactions.css" \
    "$ROOT/src/clatte/colorv/other.css" \
    "$ROOT/src/clatte/colorv/text.css" \
    "$ROOT/src/clatte/modernv/fonts.css" \
    "$ROOT/src/clatte/modernv/margins.css" \
    "$ROOT/src/clatte/trans.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/clatte/modernv/style.css" # make sure it exists empty

cp "$ROOT/sounds/modernv/sound.js" "$ROOT/build/dist/clatte/modernv/"
cp "$ROOT/sounds/modernv/clickbtn.wav" "$ROOT/build/dist/clatte/modernv/assets/"

cp -r "$ROOT/icons/." "$ROOT/build/dist/clatte/modernv/assets/icons/"
