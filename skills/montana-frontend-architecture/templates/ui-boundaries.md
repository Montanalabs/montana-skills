# Frontend UI boundary rules

- Shared UI components should not import feature-specific code.
- Feature modules may depend on shared UI primitives and shared utilities.
- Network code should not live directly inside presentational components.
- Keep one clear public entrypoint per feature where practical.

