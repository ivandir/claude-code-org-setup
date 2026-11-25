# CLAUDE.md — Data pipeline

## Project overview

TODO(team): Sources, destinations, schedule, and the downstream consumers that break if output changes.

- **Orchestrator:** TODO(team) — Airflow / Step Functions / dbt / …
- **Data sensitivity:** TODO(team) — PII columns, retention rules

## Commands

```bash
make test
make lint
make dry-run     # TODO(team): run against a sample, never against production data
```

## Conventions

- Transforms are pure functions of their inputs; side effects (writes) happen at the edges only.
- Jobs are idempotent: re-running a partition must produce the same result, not duplicates.
- Schema changes are additive. Renaming or dropping a column needs a migration plan and consumer sign-off.
- Every transform has a test with a small fixture, including empty input and malformed rows.
- Never print or log row-level data in production code paths.

## Do not do without explicit approval

- Run a backfill or any write against production tables
- Change a published schema or partitioning scheme
- Delete data, change retention, or alter access policies
- Modify scheduling or orchestration config

## Testing

- Run a single test: `TODO(team)`
- Use synthetic fixtures. Never copy production rows into the repo.
