# Python type hinting guidelines (Montana defaults)

## Defaults
- Type public functions/methods and non-trivial internals.
- Prefer `Sequence`/`Mapping`/`Iterable` over concrete types for params when appropriate.
- Prefer `Optional[T]` only when `None` is a valid value.
- Avoid `Any`; use `unknown`-like patterns via `object` + runtime checks, or `Protocol`/generics.

