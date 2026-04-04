# Support Matrix

This package has one canonical source: `skills/*/SKILL.md`.

## Publication status

| Target | Status | Notes |
|---|---|---|
| OpenClaw | Supported | Current package shape is directly aligned with OpenClaw skill folders. |
| Claude Code | Adapter kit included | `adapters/claude/` ships a concrete starter kit and manifest; native runtime verification is still pending. |
| Codex | Adapter kit included | `adapters/codex/` ships a concrete starter kit and manifest; native runtime verification is still pending. |

## Contract

- The canonical pack is runtime-neutral.
- Runtime-specific fields should not live in the canonical source unless they are explicitly documented as target-specific extensions.
- `MANIFEST.json` is the machine-readable index for categories, compositions, and recommended stacks.
