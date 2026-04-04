# Repository boundary rules

- Repositories should hide storage-specific details from callers.
- Domain/use-case layers should not know SQL/ORM/driver details.
- Mapping between persistence models and domain models should be explicit.

