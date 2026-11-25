# CLAUDE.md — API service

## Project overview

TODO(team): What this service does, its consumers, and where it runs.

- **Consumers:** TODO(team) — internal services / mobile app / third parties
- **Data sensitivity:** TODO(team)

## Commands

```bash
make test
make lint
make run
```

## Conventions

- Handlers stay thin: validate input, call a service function, map the result. Business logic lives in `services/`, not in route handlers.
- Errors use the shared error type and map to documented status codes. Never return raw exception text to clients.
- Every endpoint is covered by an integration test that hits the real router (no mocking the framework).
- Log structured JSON; never log request bodies, tokens, or PII.

## API contract rules

- The OpenAPI spec is the source of truth. Change the spec first, then the code.
- Additive changes only on existing versions: new optional fields are fine; removing, renaming, or changing the type of a field is a breaking change and needs a new version.
- Do not change status codes or error shapes without approval.

## Do not do without explicit approval

- Change public API contracts or the OpenAPI spec in a breaking way
- Modify or run database migrations
- Delete files, change CI/CD, add dependencies

## Testing

- Unit tests for services, integration tests for endpoints, contract tests for consumers.
- Run a single test: `TODO(team)`
