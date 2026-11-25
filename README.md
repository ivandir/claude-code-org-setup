# claude-code-org-setup

A template repository for rolling out [Claude Code](https://docs.claude.com/en/docs/claude-code) across an engineering organization — from 10 engineers to 100+.

Most teams figure out `CLAUDE.md`, permissions and skills from scratch, one engineer at a time, and end up with 25 different configurations and no shared quality bar. This repo is the starting point I wish existed: annotated templates, tiered permission presets, a starter skill library, and a rollout guide covering the part that configuration can't fix — the team.

> Companion to the essay [How I Set Up Claude Code for a Team of 25](https://ivandir.com/blog/claude-code-team-case-study.html).

## What's inside

| Path | What it is |
| --- | --- |
| [`templates/claude-md/`](templates/claude-md) | An **annotated** project `CLAUDE.md` (every section explained), four service-type variants (API, frontend, infrastructure, data pipeline), and a personal global example |
| [`templates/AGENTS.md`](templates/AGENTS.md) | Conventions for tool-agnostic agent instructions, kept in sync with `CLAUDE.md` |
| [`templates/settings/`](templates/settings) | Three permission presets — `junior`, `senior`, `lead` — as drop-in `.claude/settings.json` files |
| [`.claude/skills/`](.claude/skills) | A starter skill library: `review-pr`, `write-adr`, `draft-postmortem`, `write-tests`, `scaffold-endpoint` |
| [`.github/pull_request_template.md`](.github/pull_request_template.md) | PR template with an AI-assistance section |
| [`docs/rollout-guide.md`](docs/rollout-guide.md) | Phased rollout plan for 10–100+ engineers, including the cultural dynamics |
| [`docs/onboarding-checklist.md`](docs/onboarding-checklist.md) | Per-engineer checklist for week one |
| [`docs/permission-tiers.md`](docs/permission-tiers.md) | The three-tier permission model and why each preset looks the way it does |
| [`docs/skill-conventions.md`](docs/skill-conventions.md) | Naming, versioning and distribution of team skills |
| [`docs/pr-review-integration.md`](docs/pr-review-integration.md) | How to review AI-assisted code without slowing down |

## Quick start (under 30 minutes)

1. **Fork or use this repo as a template.** Replace `Acme` / `your-org` placeholders (search for `TODO(team)`).
2. **Write your project `CLAUDE.md`.** Copy [`templates/claude-md/CLAUDE.annotated.md`](templates/claude-md/CLAUDE.annotated.md) into your service repo as `CLAUDE.md`, delete the annotations, and fill it in with 2–3 senior engineers. Start from the service-type variant closest to your codebase.
3. **Pick a permission preset.** Copy one of [`templates/settings/`](templates/settings) to `.claude/settings.json` in your service repo. Default new hires to `junior`, most engineers to `senior`.
4. **Add the skills you want.** Copy any folder from [`.claude/skills/`](.claude/skills) into your repo's `.claude/skills/` (or into `~/.claude/skills/` to apply across repos).
5. **Add the PR template** from [`.github/pull_request_template.md`](.github/pull_request_template.md).
6. **Run the onboarding checklist** with your first cohort — see [`docs/onboarding-checklist.md`](docs/onboarding-checklist.md).

Then read the [rollout guide](docs/rollout-guide.md) before widening beyond your first team.

## Design principles

- **The project `CLAUDE.md` is the highest-leverage file.** Spend a day on it, with senior engineers, and review it quarterly.
- **Tier permissions by blast radius, not by seniority alone.** Read-only is free; reversible writes are cheap; anything irreversible asks every time.
- **No bypass flag in shared codebases.** `--dangerously-skip-permissions` is disabled in every preset.
- **Own what you ship.** AI is an accelerator for your work, not a substitute for understanding it.
- **Skills are shared runbooks.** Version them, document inputs and outputs, and keep them in the repo.

## Validating your setup

```bash
python scripts/validate.py
```

Checks that every settings preset is valid JSON with the expected keys, every skill has `name` and `description` front matter that matches its folder, and the templates still contain no unresolved real credentials patterns. CI runs the same script on every push.

## Related

- Enterprise-grade hooks (audit logging, secret detection) — see the security-focused configuration notes in [`docs/permission-tiers.md`](docs/permission-tiers.md#hardening-for-regulated-environments).

## License

[MIT](LICENSE)
