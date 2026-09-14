#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/alucard/colorv"

cat "$ROOT/src/alucard/colorv/interactions.css" \
    "$ROOT/src/alucard/colorv/other.css" \
    "$ROOT/src/alucard/colorv/text.css" \
    "$ROOT/src/alucard/trans.css" \
    "$ROOT/src/alucard/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/alucard/colorv/style.css" # make sure it exists empty
