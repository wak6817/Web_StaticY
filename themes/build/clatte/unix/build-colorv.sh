#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/clatte/colorv"

cat "$ROOT/src/clatte/colorv/interactions.css" \
    "$ROOT/src/clatte/colorv/other.css" \
    "$ROOT/src/clatte/colorv/text.css" \
    "$ROOT/src/clatte/trans.css" \
    "$ROOT/src/clatte/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/clatte/colorv/style.css" # make sure it exists empty
