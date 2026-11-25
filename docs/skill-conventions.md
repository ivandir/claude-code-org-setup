# Skill conventions

Skills are reusable workflows that tell Claude Code how to accomplish a specific task in a specific way — shared runbooks you invoke conversationally. Skills without conventions become tribal knowledge within months.

## Layout

```
.claude/skills/
└── <skill-name>/
    └── SKILL.md
```

`SKILL.md` starts with YAML front matter:

```markdown
---
name: review-pr
description: Structured PR review covering correctness, security and API compatibility. Use when asked to review a PR or diff.
---
```

- `name` **must match the folder name** (enforced by `scripts/validate.py`).
- `description` is what Claude uses to decide when to load the skill — say what it does *and* when to use it.

## Naming

- **kebab-case**, named for **what the skill does**, not the technology: `write-tests`, not `pytest-helper`.
- **Version breaking changes in the name:** `review-pr-v2`. Keep the old one until nobody uses it, then delete it.
- Prefer verbs: `review-`, `write-`, `draft-`, `scaffold-`.

## Document inputs and outputs

Every skill body should state:

1. **Inputs** — what the skill needs and what to ask for if it's missing.
2. **Output** — what it produces and where.
3. **Procedure** — numbered steps.
4. **Rules** — hard constraints (what it must never do).

## The four categories that cover ~80% of the value

| Category | Starter skills in this repo |
| --- | --- |
| Code generation | `scaffold-endpoint`, `write-tests` |
| Review | `review-pr` |
| Documentation | `write-adr` |
| Incident response | `draft-postmortem` |

Add skills for repeated, well-defined work. Don't add a skill for something you'd do once.

## Versioning and distribution

| Scope | How | Trade-off |
| --- | --- | --- |
| One repo | Commit to `<repo>/.claude/skills/` | Versioned with the code; everyone gets updates on pull |
| Org-wide | Git submodule into `~/.claude/skills/` | Operationally simple; engineers must remember to update |
| Org-wide, pinned | Publish as an internal package | Adds a dependency; enables CI-enforced version pinning |

## Promotion process

1. Someone writes a skill in their own repo.
2. After **two** people use it successfully, propose it to the shared library via PR.
3. The team champion reviews: clear trigger, documented I/O, no repo-specific assumptions (or marked `TODO(team)`).
4. Review the whole library quarterly; delete skills nobody uses.

## Safety rules for skills

- A skill must never contain secrets, tokens or internal-only URLs.
- A skill must not widen permissions — it works within the engineer's `settings.json`.
- Skills that can modify shared state (deploys, migrations) must say so explicitly and require confirmation.
