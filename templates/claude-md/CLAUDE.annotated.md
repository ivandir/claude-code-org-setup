# CLAUDE.md — annotated project template

> **How to use this file:** copy it to the root of a service repository as `CLAUDE.md`, fill in each section, then delete every block that starts with `> **Why:**`. Those blocks explain the intent; they should not ship in your real file (they cost context on every session).
>
> Keep the final file under ~150 lines. If it grows past that, move subsystem rules into a local `CLAUDE.md` (see the bottom of this file).

---

## Project overview

TODO(team): One paragraph. What does this service do, who uses it, what does it depend on, where does it run?

- **Purpose:** TODO(team) — e.g. "Processes claims events and exposes the claims API."
- **Runtime / deploy target:** TODO(team) — e.g. "Python 3.12 on ECS Fargate, deployed by GitHub Actions."
- **External dependencies:** TODO(team) — databases, queues, third-party APIs.
- **Data sensitivity:** TODO(team) — e.g. "Handles PII; HIPAA-regulated." or "No customer data."

> **Why:** The model has no idea what the codebase is for. A model that knows it is working in a regulated data service makes different — and better — security decisions than one that doesn't. This is the cheapest context you can give it.

## Commands

```bash
# TODO(team): the exact commands, copy-pasteable
make test        # run unit tests
make lint        # lint + type-check
make run         # run locally
```

> **Why:** Claude will guess commands otherwise, and guess wrong. List the three or four commands used in every change: test, lint, run, build.

## Conventions that differ from defaults

- TODO(team): import order, naming, error-handling pattern, logging format…
- TODO(team): patterns that look wrong to an outsider but are intentional (and why).

> **Why:** Do **not** paste your whole style guide. Only list what Claude gets wrong without instruction. If a linter already enforces it, leave it out — the linter will tell Claude.

## Do not do without explicit approval

- Modify database migrations or run them against any shared environment
- Change public API contracts (request/response shapes, status codes, event schemas)
- Delete files or directories
- Modify CI/CD configuration or deployment files
- Add or upgrade dependencies
- TODO(team): anything else where a mistake is expensive to undo

> **Why:** These are the actions where an automated mistake has amplified consequences. This list is advisory to the model; permissions in `.claude/settings.json` are the **enforced** version. Keep the two consistent.

## Architecture notes

TODO(team): The three things a new engineer needs to know before touching this code — data flow, module boundaries, where state lives.

> **Why:** Without this Claude re-derives the architecture from scratch every session, and sometimes derives it wrongly.

## Testing expectations

- New behavior needs a test. Bug fixes need a regression test.
- TODO(team): framework, fixtures, how to run a single test, what must not be mocked.

> **Why:** Writing tests for existing code was the highest-ROI use of Claude Code in our rollout. Tell it how your tests are structured so the output matches.

## AI-assisted changes

- You own everything you commit. If you cannot explain a change in the PR, it should not be in the PR.
- Say so in the PR description when a change was AI-assisted (see the PR template).
- Prefer small, reviewable diffs. Ask for one change at a time.

> **Why:** Sets the quality bar at the team level instead of leaving it to individual discretion. See `docs/pr-review-integration.md`.

---

## Where each level of CLAUDE.md belongs

| Level | Location | Put here | Don't put here |
| --- | --- | --- | --- |
| Global | `~/.claude/CLAUDE.md` | Personal preferences, machine context, personal security rules | Team standards (don't push this to everyone's machine) |
| Project | `CLAUDE.md` at repo root (committed) | Everything above — shared by all engineers in the repo | Personal style preferences |
| Local | `<subdir>/CLAUDE.md` | Subsystem overrides (`infra/`, `frontend/`) with genuinely different conventions or risk | Workarounds for restrictions in the project file |
