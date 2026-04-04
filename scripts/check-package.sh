#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

for skill in "$ROOT_DIR"/skills/*/SKILL.md; do
  grep -q '^name:' "$skill"
  grep -q '^description:' "$skill"
  grep -q '^metadata:' "$skill"
  grep -q '^## Category' "$skill"
  grep -q '^## Works with' "$skill"
done

test -f "$ROOT_DIR/MANIFEST.json"
test -f "$ROOT_DIR/SUPPORT_MATRIX.md"
test -f "$ROOT_DIR/CATEGORIES.md"
test -f "$ROOT_DIR/maintainers/README.md"
test -f "$ROOT_DIR/maintainers/PUBLISHING.md"
test -f "$ROOT_DIR/maintainers/PUBLISH_CHECKLIST.md"
test -f "$ROOT_DIR/maintainers/SKILLS_PACKAGE.md"
test -f "$ROOT_DIR/templates/SKILL_TEMPLATE.md"
test -f "$ROOT_DIR/templates/SKILL_CHECKLIST.md"
test -f "$ROOT_DIR/templates/STACK_TEMPLATE.md"
test -f "$ROOT_DIR/adapters/openclaw/README.md"
test -f "$ROOT_DIR/adapters/claude/README.md"
test -f "$ROOT_DIR/adapters/claude/COMMAND_TEMPLATE.md"
test -f "$ROOT_DIR/adapters/claude/AGENT_TEMPLATE.md"
test -f "$ROOT_DIR/adapters/claude/MANIFEST.json"
test -f "$ROOT_DIR/adapters/codex/README.md"
test -f "$ROOT_DIR/adapters/codex/PROMPT_TEMPLATE.md"
test -f "$ROOT_DIR/adapters/codex/SKILL_WRAPPER_TEMPLATE.md"
test -f "$ROOT_DIR/adapters/codex/MANIFEST.json"

echo "Package checks passed"
