# Case: `montana-pattern-conditional-rendering`

## Skill under test

`montana-pattern-conditional-rendering`

## Fixture

`tests/skill-eval/fixtures/ts-react-app`

## Prompt

Apply the Montana conditional-rendering pattern so the component exposes clear user-visible states with early returns and readable branch logic.

## Scoring rubric

- `state identification`: 3 points
- `ordered early-return pattern`: 3 points
- `readable branch conditions`: 2 points
- `accessibility-aware state rendering`: 2 points

## Expected commands

- read cart or checkout component files

## Expected boundaries

- identify all visible states
- prefer early returns for meaningful branches
- name non-trivial branch conditions

## Red flags

- dense nested JSX branching
- implicit missing-state behavior
- duplicated state just to simplify rendering

## Transcript

`tests/skill-eval/transcripts/codex/montana-pattern-conditional-rendering.md`
