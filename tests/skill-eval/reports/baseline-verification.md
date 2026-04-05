# Baseline Verification

These checks confirm that the fixtures contain real issues for skill-driven testing.

## Verified failing fixtures

- `go-api`
  - Command: `GOCACHE=/tmp/go-build-cache go test ./internal/service`
  - Result: fails because whitespace-only names are not rejected before save

- `python-service`
  - Command: `python3 -c "from src.customer_service import normalize_customer_name; assert normalize_customer_name('  Ada   Lovelace  ') == 'Ada Lovelace'"`
  - Result: fails because internal whitespace is not normalized

- `rust-cli`
  - Command: `cargo test`
  - Result: fails because `parse_port("0")` currently returns success

## Environment limitations seen during verification

- `python3 -m pytest -q` failed because `pytest` is not installed in this environment.
- `go test` needed `GOCACHE=/tmp/go-build-cache` because the default Go cache path was not writable in the sandbox.

## Not yet executed

- `ts-react-app`
  - The fixture is ready for intake, TypeScript, React, and frontend-architecture scenario testing.
  - Full scripted verification was not run here because the workspace does not include installed frontend toolchain dependencies for the fixture.

- `js-node-service`
  - The fixture is ready for JavaScript workflow testing.
  - No additional runtime verification was needed because the issue is a direct code-path quality problem.

- `release-sample`
  - This fixture is document-driven and intended for release-note quality evaluation rather than runtime execution.
