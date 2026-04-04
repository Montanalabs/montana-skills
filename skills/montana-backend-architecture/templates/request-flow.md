# Backend request flow template

```text
transport/handler
  -> validation / auth
  -> use-case / service
  -> repository / external adapter
  -> response mapping
```

