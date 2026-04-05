# Case: `montana-react`

## Skill under test

`montana-react`

## Fixture

`tests/skill-eval/fixtures/ts-react-app`

## Prompt

Improve the checkout form so the submit button is disabled during save, labels are properly associated, and error text is announced accessibly.

## Scoring rubric

- `accessibility coverage`: 4 points
- `state ownership discipline`: 2 points
- `minimal component-focused change`: 2 points
- `verification behavior`: 2 points

## Expected commands

- inspection of `package.json` and `src/features/checkout/CheckoutForm.tsx`
- repo-check command discovery from the fixture

## Expected boundaries

- should keep state inside the form unless there is a compelling reason otherwise
- should add label association and accessible error handling
- should avoid unnecessary memoization or abstraction

## Red flags

- moving state farther away than needed
- accessibility regressions
- adding complexity without payoff

## Transcript

`tests/skill-eval/transcripts/codex/montana-react.md`
