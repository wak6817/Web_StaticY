#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/cmacchiato/modernv/assets/icons"

cat "$ROOT/src/cmacchiato/colorv/interactions.css" \
    "$ROOT/src/cmacchiato/colorv/other.css" \
    "$ROOT/src/cmacchiato/colorv/text.css" \
    "$ROOT/src/cmacchiato/modernv/fonts.css" \
    "$ROOT/src/cmacchiato/modernv/margins.css" \
    "$ROOT/src/cmacchiato/trans.css" \
    "$ROOT/src/cmacchiato/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/cmacchiato/modernv/style.css" # make sure it exists empty

cp "$ROOT/sounds/modernv/sound.js" "$ROOT/build/dist/cmacchiato/modernv/"
cp "$ROOT/sounds/modernv/clickbtn.wav" "$ROOT/build/dist/cmacchiato/modernv/assets/"

cp -r "$ROOT/icons/." "$ROOT/build/dist/cmacchiato/modernv/assets/icons/"
