# Python error style (Montana defaults)

## Defaults
- Raise specific exceptions (`ValueError`, `TypeError`, custom exceptions) instead of `Exception`.
- Messages should be actionable and stable enough for tests where matched.
- Don’t catch broad exceptions unless you re-raise with context or convert to a meaningful domain error.

