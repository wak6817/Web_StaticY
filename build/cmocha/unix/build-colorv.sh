#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/cmocha/colorv"

cat "$ROOT/src/cmocha/colorv/interactions.css" \
    "$ROOT/src/cmocha/colorv/other.css" \
    "$ROOT/src/cmocha/colorv/text.css" \
    "$ROOT/src/cmocha/trans.css" \
    "$ROOT/src/cmocha/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/cmocha/colorv/style.css" # make sure it exists empty
