# Codex adapter kit

This directory is the Codex-facing adapter kit for the canonical Montana skills source.

## Purpose

Use the core skills in `package/skills/` as source material, then map them into the Codex distribution surface you verify for your users.

## Source of truth

- Canonical source: `package/skills/*/SKILL.md`
- Machine-readable index: `package/MANIFEST.json`
- Category model: `package/CATEGORIES.md`

## Included templates

- `PROMPT_TEMPLATE.md`
- `SKILL_WRAPPER_TEMPLATE.md`
- `MANIFEST.json`

## Verification status

- Adapter kit included
- Native Codex runtime integration not yet verified in a real Codex environment
