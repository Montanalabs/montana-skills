#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="${1:-0.1.0}"
OUT_DIR="$ROOT_DIR/releases"
STAGE_DIR="$OUT_DIR/montana-skills-v$VERSION"
ZIP_PATH="$OUT_DIR/montana-skills-v$VERSION.zip"

rm -rf "$STAGE_DIR"
mkdir -p "$STAGE_DIR"

cp "$ROOT_DIR/README.md" "$STAGE_DIR/"
cp "$ROOT_DIR/CATEGORIES.md" "$STAGE_DIR/"
cp "$ROOT_DIR/SUPPORT_MATRIX.md" "$STAGE_DIR/"
cp "$ROOT_DIR/MANIFEST.json" "$STAGE_DIR/"
cp "$ROOT_DIR/LICENSE" "$STAGE_DIR/"
cp "$ROOT_DIR/CHANGELOG.md" "$STAGE_DIR/"
cp -R "$ROOT_DIR/maintainers" "$STAGE_DIR/"
cp -R "$ROOT_DIR/adapters" "$STAGE_DIR/"
cp -R "$ROOT_DIR/templates" "$STAGE_DIR/"
cp -R "$ROOT_DIR/scripts" "$STAGE_DIR/"
cp -R "$ROOT_DIR/skills" "$STAGE_DIR/"

mkdir -p "$OUT_DIR"
rm -f "$ZIP_PATH"
(
  cd "$OUT_DIR"
  zip -qr "$(basename "$ZIP_PATH")" "$(basename "$STAGE_DIR")"
)

echo "Built $ZIP_PATH"
