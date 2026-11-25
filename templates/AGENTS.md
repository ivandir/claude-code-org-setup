# AGENTS.md — conventions

`AGENTS.md` is the tool-agnostic counterpart to `CLAUDE.md`: a plain-Markdown instruction file that other coding agents (and humans) read. If your org uses more than one AI tool, keep them from drifting.

## Recommended approach: one source of truth

Make `AGENTS.md` the canonical file and have `CLAUDE.md` import it, then add Claude-specific notes below the import:

```markdown
<!-- CLAUDE.md -->
@AGENTS.md

## Claude Code specifics
- Use the skills in `.claude/skills/` for review, ADRs, and post-mortems.
```

If you only use Claude Code, skip `AGENTS.md` entirely — an unused file is a file that rots.

## What belongs in AGENTS.md

| Section | Content |
| --- | --- |
| Overview | What the repo is and its risk profile |
| Commands | Build, test, lint, run |
| Conventions | Only what differs from defaults |
| Boundaries | What the agent must not do without approval |
| Testing | How tests are structured and run |

This is the same content as the annotated `CLAUDE.md` in [`claude-md/CLAUDE.annotated.md`](claude-md/CLAUDE.annotated.md) — copy it from there.

## What does not belong

- Tool-specific permission config (that lives in `.claude/settings.json`)
- Personal preferences (that lives in `~/.claude/CLAUDE.md`)
- Secrets, tokens, or internal URLs you wouldn't paste into a ticket

## Rules of the road

1. **Never fork the content.** If two files describe the same rules differently, one is wrong.
2. **Review changes like code.** A one-line edit to `AGENTS.md` can change the behavior of every agent run in the repo — it needs a PR and a reviewer.
3. **Review quarterly.** Delete rules the model now follows by default, and add the mistakes you keep seeing in review.
