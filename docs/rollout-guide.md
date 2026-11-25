# Rollout guide

A phased plan for adopting Claude Code across 10–100+ engineers. The configuration (CLAUDE.md, permissions, skills) is roughly 30% of what decides whether a rollout works. The other 70% is expectations, modeling, and review culture — so this guide covers both.

## Why team adoption is different

Alone, *you* are the context. On a team, three problems appear:

- **Coordination** — without standards you get N different `CLAUDE.md` files, N permission setups, and N opinions on when AI output needs review. The variation is also risk: permissive settings from a side project can leak into a shared production repo.
- **Consistency** — output quality tracks instruction quality. Two PRs that both say "AI-assisted" can reflect wildly different verification. The bar must be set at team level.
- **Trust** — some engineers over-trust and commit code they haven't read; others under-trust and don't use the tool. Calibration is a management problem, not a configuration one.

## Phases

### Phase 0 — Prepare (week 0, ~2–3 days of leadership time)

- [ ] Choose a pilot team (5–10 engineers, mixed seniority, at least two enthusiasts and one skeptic).
- [ ] Write the **project `CLAUDE.md`** for the pilot repo with 2–3 senior engineers. Budget a full day. Use [`templates/claude-md/CLAUDE.annotated.md`](../templates/claude-md/CLAUDE.annotated.md).
- [ ] Choose permission presets ([`permission-tiers.md`](permission-tiers.md)) and commit `.claude/settings.json`.
- [ ] Decide where session logs go ([audit trail](permission-tiers.md#audit-trail)).
- [ ] Add the [PR template](../.github/pull_request_template.md) and agree the [review norms](pr-review-integration.md).
- [ ] Get security/legal sign-off on data handling if you work with regulated data.

### Phase 1 — Pilot (weeks 1–2)

- [ ] Run the [onboarding checklist](onboarding-checklist.md) with each pilot engineer.
- [ ] Run one 45-minute kickoff: what Claude Code is good and bad at, the permission model, the "you own what you ship" rule.
- [ ] Seed three high-ROI use cases (below) so people succeed on day one.
- [ ] Hold a 20-minute retro at the end of week 2. Update `CLAUDE.md` with every recurring mistake.

### Phase 2 — Expand (weeks 3–8)

- [ ] Roll out to the next teams, one repo at a time. Each repo gets its own `CLAUDE.md` — never copy one blindly.
- [ ] Start the shared skill library ([`skill-conventions.md`](skill-conventions.md)). Promote a skill only after two people use it successfully.
- [ ] Nominate one **champion per team** to triage `CLAUDE.md` / skill change requests.
- [ ] Review session-log samples for permission friction and fix the presets.

### Phase 3 — Operate (ongoing)

- [ ] Review each `CLAUDE.md` quarterly: delete rules the model now follows by default; add recurring review findings.
- [ ] Track adoption and outcomes (below). Share wins and failures openly.
- [ ] Revisit permission tiers when you add new deployment paths.

## High-ROI use cases to seed first

1. **Writing tests for existing code.** Lowest activation energy, easy to review. In our rollout this moved active-module coverage by ~18 points over four months.
2. **Explaining unfamiliar code.** Cut "orientation time" in legacy areas from half a day to under an hour.
3. **Drafting infrastructure-as-code.** Saved a few hours per change for engineers whose main skill is application code.

The pattern: the best uses are tedious, well-defined, high-volume tasks. Be skeptical of "generate the implementation from this spec" and "auto-write PR descriptions" — both looked promising and underdelivered (the first needs more revision than writing it yourself; the second produces generic descriptions that miss the *why*).

## Cultural dynamics

Expect a **bimodal** adoption curve, not a smooth S: roughly 30% adopt in two weeks, 40% over weeks 3–8 as social proof builds, and 30% skeptical or unconvinced.

- **Experienced skeptics** have seen CASE tools and low-code hype. Don't evangelize — demonstrate. Pair on a task in *their* area and let them judge the output.
- **Quality-minded skeptics** ask "if Claude writes it, can I maintain it?" The answer: Claude Code is a pair programmer, not a replacement for understanding. If you can't explain the code in the PR, it doesn't go in the PR.
- **Over-reliers** commit output without reading it; you'll see it in review as correct-looking but architecturally naive code. Fix it with review culture (ask "do you understand why this works?"), not with more tooling.

## Measuring it

Pick a few signals and watch trends, not absolutes (you can't cleanly isolate the effect):

- Weekly active users per team
- Test coverage on actively-changed modules
- PR cycle time and change-failure rate (DORA)
- Developer sentiment (a two-question pulse every month)

Treat any number as a conversation starter, not a performance metric for individuals.

## Anti-patterns

- Pushing one global `~/.claude/CLAUDE.md` to everyone's machine.
- Copying one repo's `CLAUDE.md` into another without editing.
- Using `--dangerously-skip-permissions` in shared codebases (disabled in every preset here).
- Measuring individuals by AI usage.
- A `CLAUDE.md` nobody owns.
