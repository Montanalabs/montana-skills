# Publish Checklist

Use this checklist when publishing a Montana Skills Pack release.

## Before tagging

- Confirm `package/CHANGELOG.md` matches the intended release
- Run `bash package/scripts/check-package.sh`
- Build the artifact with `bash package/scripts/build-release.sh <version>`
- Inspect `package/releases/montana-skills-v<version>.zip`
- Confirm `package/SUPPORT_MATRIX.md` reflects the actual runtime support stance
- Confirm `package/MANIFEST.json` matches the released skills and recommended stacks

## GitHub release

- Create tag `v<version>`
- Upload `package/releases/montana-skills-v<version>.zip`
- Paste `package/releases/RELEASE_NOTES_v<version>.md` into the release description

## After publishing

- Verify the uploaded artifact downloads correctly
- Verify the zip contains `skills/`, `templates/`, `adapters/`, `scripts/`, `MANIFEST.json`, and `SUPPORT_MATRIX.md`
- If publishing to ClawHub or another marketplace, use the same released artifact and support stance

