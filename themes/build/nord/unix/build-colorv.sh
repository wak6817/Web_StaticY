#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/nord/colorv"

cat "$ROOT/src/nord/colorv/interactions.css" \
    "$ROOT/src/nord/colorv/other.css" \
    "$ROOT/src/nord/colorv/text.css" \
    "$ROOT/src/nord/trans.css" \
    "$ROOT/src/nord/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/nord/colorv/style.css"
