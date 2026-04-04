# Publishing Montana Skills Pack

This guide is for maintainers who want to publish the skills pack for public users.

## 1) Versioning

- Use SemVer tags: `v0.1.0`, `v0.2.0`, …
- Update `package/CHANGELOG.md` for each release.
- Add or update `package/releases/RELEASE_NOTES_vX.Y.Z.md` for the GitHub release body.

## 2) GitHub release artifact

Recommended release artifact structure:

```text
montana-skills-vX.Y.Z.zip
  README.md
  CATEGORIES.md
  SUPPORT_MATRIX.md
  MANIFEST.json
  LICENSE
  CHANGELOG.md
  templates/
  adapters/
  scripts/
  skills/
```

Notes:
- Keep skills self-contained.
- Do not ship private/internal instructions or environment-specific paths.
- Ship `CATEGORIES.md`, `MANIFEST.json`, and `templates/` so contributors can extend the pack consistently.

## 3) Claude Code distribution

Treat Claude as an adapter-backed distribution target:

- Do not claim the raw `package/skills/*/SKILL.md` folders are directly installable in Claude unless you have verified the current Claude extension surface.
- Ship `package/adapters/claude/` with the release as the maintained Claude starter kit.
- Publish direct-install Claude support only after testing the real install path and invocation model.

## 4) OpenClaw / ClawHub distribution

OpenClaw is the most direct runtime target for the canonical `skills/` folders.

Document all three end-user flows in the public README:

- install one skill
- install a recommended stack
- install the whole pack

Marketplace references:

- Skills overview: https://docs.openclaw.ai/skills
- ClawHub: https://clawhub.com

## 5) Codex distribution

Treat Codex as an adapter-backed distribution target:

- Do not claim the raw `package/skills/*/SKILL.md` folders are directly installable unless you have verified the current Codex skills/distribution surface for public users.
- Ship `package/adapters/codex/` with the release as the maintained Codex starter kit.

## 6) Quality checklist (before tagging)

- Each skill has correct YAML frontmatter, category/composition guidance, default workflow, and safety rules.
- `package/MANIFEST.json` matches the released skills and stacks.
- `package/SUPPORT_MATRIX.md` matches the published support stance.
- Adapter kits in `package/adapters/` match the published support stance.
- Release scripts in `package/scripts/` work from a clean checkout.
- `package/maintainers/PUBLISH_CHECKLIST.md` reflects the current release flow.
- README runtime support statements are verified and not over-claimed.
- Changelog updated.

