#!/bin/sh

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
SOURCE_DIR="$PROJECT_ROOT/src/themes"
OUTPUT_DIR="$PROJECT_ROOT/dist/themes"

if [ ! -d "$SOURCE_DIR" ]; then
  printf '%s\n' "Theme source directory not found: $SOURCE_DIR" >&2
  exit 1
fi

rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

theme_count=0

for theme_dir in "$SOURCE_DIR"/*; do
  [ -d "$theme_dir" ] || continue

  theme_name=$(basename "$theme_dir")
  for required_file in trans.css api.css modernv/fonts.css modernv/margins.css \
    pixelv/fonts.css pixelv/margins.css colorv/interactions.css \
    colorv/other.css colorv/text.css; do
    if [ ! -f "$theme_dir/$required_file" ]; then
      printf '%s\n' "Missing $required_file in theme: $theme_name" >&2
      exit 1
    fi
  done

  mkdir -p "$OUTPUT_DIR/$theme_name"
  cp -R "$theme_dir"/. "$OUTPUT_DIR/$theme_name/"
  theme_count=$((theme_count + 1))
done

if [ "$theme_count" -eq 0 ]; then
  printf '%s\n' "No themes found in: $SOURCE_DIR" >&2
  exit 1
fi

printf 'Built %s theme(s) in %s\n' "$theme_count" "$OUTPUT_DIR"
