# Onboarding checklist (per engineer)

Run this in the engineer's first week with Claude Code. Budget about 90 minutes in total.

## Before the session

- [ ] Engineer has Claude Code installed and can authenticate.
- [ ] Their repo has a project `CLAUDE.md` and `.claude/settings.json` (pick a [preset](permission-tiers.md)).
- [ ] They know which tier they are on and why.

## Session (45–60 minutes, pair with a champion)

- [ ] **Mental model:** Claude Code is a pair programmer. You review and own everything it produces.
- [ ] **Permissions:** walk through read-only → reversible writes → approval-required. Trigger an approval prompt on purpose.
- [ ] **CLAUDE.md hierarchy:** show the global, project and local levels and what belongs in each. Have them create their own personal `~/.claude/CLAUDE.md` from [`CLAUDE.global-personal.md`](../templates/claude-md/CLAUDE.global-personal.md).
- [ ] **First task together:** write tests for an existing function using the `write-tests` skill.
- [ ] **Second task:** ask Claude to explain a module they haven't touched.
- [ ] **Review norms:** read the [PR review integration](pr-review-integration.md) page, and show the AI-assistance section of the PR template.
- [ ] **Skills:** list the available skills and how to invoke them; show where to propose a new one.
- [ ] **What not to do:** no bypass flag; no pasting secrets or customer data; no committing output you can't explain.

## First week (self-directed)

- [ ] Use Claude Code for at least three real tasks.
- [ ] Open one PR that is AI-assisted and fill in the PR template honestly.
- [ ] Add one line to the project `CLAUDE.md` (via PR) for something Claude got wrong.

## Check-in (end of week 1, 15 minutes)

- [ ] What worked? What was frustrating?
- [ ] Any permission prompts that felt pointless or too loose? (Feed back into the presets.)
- [ ] Any skill ideas?
