# Claude adapter kit

This directory is the Claude-facing adapter kit for the canonical Montana skills source.

## Purpose

Use the core skills in `package/skills/` as source material, then translate them into the Claude-specific surfaces you support:

- project commands
- personal commands
- specialized agents / subagents

## Suggested mapping

- Language skills -> commands or specialized agents
- Framework and architecture skills -> specialized agents
- Use-case skills -> commands or planning agents

## Source of truth

- Canonical source: `package/skills/*/SKILL.md`
- Machine-readable index: `package/MANIFEST.json`
- Category model: `package/CATEGORIES.md`

## Included templates

- `COMMAND_TEMPLATE.md`
- `AGENT_TEMPLATE.md`
- `MANIFEST.json`

## Verification status

- Adapter kit included
- Native Claude runtime integration not yet verified in a real Claude environment
