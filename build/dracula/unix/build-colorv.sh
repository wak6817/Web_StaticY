#!/bin/sh

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

mkdir -p "$ROOT/build/dist/dracula/colorv"

cat "$ROOT/src/dracula/colorv/interactions.css" \
    "$ROOT/src/dracula/colorv/other.css" \
    "$ROOT/src/dracula/colorv/text.css" \
    "$ROOT/src/dracula/trans.css" \
    "$ROOT/src/dracula/api.css" \
    "$ROOT/src/templates.css" \
    > "$ROOT/build/dist/dracula/colorv/style.css"
