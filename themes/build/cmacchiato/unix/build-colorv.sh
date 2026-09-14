#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/cmacchiato/colorv"

cat "$ROOT/src/cmacchiato/colorv/interactions.css" \
    "$ROOT/src/cmacchiato/colorv/other.css" \
    "$ROOT/src/cmacchiato/colorv/text.css" \
    "$ROOT/src/cmacchiato/trans.css" \
    "$ROOT/src/cmacchiato/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/cmacchiato/colorv/style.css" # make sure it exists empty
