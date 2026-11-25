# Permission tiers

Claude Code's permission rules decide which operations run automatically, which ask first, and which are blocked. This repo tunes them by **blast radius** — how bad and how reversible a mistake is — rather than by trust in the engineer alone.

## The three operation tiers

| Tier | Examples | Policy |
| --- | --- | --- |
| **Read-only** | File reads, grep, directory listing, `git log` / `git diff` | Allow automatically |
| **Reversible writes** | Editing source files, creating files, running tests, local commits | Allow (the engineer can undo; review happens in the PR) |
| **Irreversible / high blast radius** | Deleting files, `git push`, database migrations, deploys, installing dependencies | Ask every time — or deny |

Rule evaluation order in Claude Code is **deny → ask → allow**, first match wins. Practical consequence: never put a bare `Bash` in `ask` alongside specific `allow` rules — it would match first and make every allow rule moot. Unlisted commands already prompt by default.

## The three presets

| Preset | File | Intended for | Key differences |
| --- | --- | --- | --- |
| **junior** | [`settings.junior.json`](../templates/settings/settings.junior.json) | New to the codebase or to AI tooling | Edits and writes ask every time; read-only git allowed; `git push`, `curl`, `wget` denied |
| **senior** | [`settings.senior.json`](../templates/settings/settings.senior.json) | Most engineers | Edits/writes, local commits and tests allowed; push, installs, docker and deploys ask |
| **lead** | [`settings.lead.json`](../templates/settings/settings.lead.json) | Tech leads, platform owners | Adds `gh pr` workflows, `cdk diff`/`terraform plan`, fetch/pull; `apply`/`deploy`/`destroy` still ask |

Preset choice is per-engineer-per-repo and is a starting point, not a verdict — move people up as they build calibration, and down for sensitive repos.

All three presets:

- Set `"disableBypassPermissionsMode": "disable"` — there is essentially no legitimate team use for `--dangerously-skip-permissions` in a shared codebase. (For a hard guarantee, set it in managed/enterprise settings so engineers can't override it locally.)
- Deny reading `.env*`, private keys, `~/.aws/**` and `~/.ssh/**`.
- Deny force-push, `rm -rf`, `sudo`.

## Using a preset

```bash
cp templates/settings/settings.senior.json <your-repo>/.claude/settings.json
```

Commit it so everyone in the repo shares the same baseline. Personal overrides belong in `.claude/settings.local.json`, which should be git-ignored; for rules engineers must not be able to loosen, use managed settings.

## Audit trail

Claude Code writes a session log to `~/.claude/logs/` by default. For team deployments, ship these somewhere shared (an S3 bucket, your log platform) so that when something goes wrong you can reconstruct what the model was asked to do, what it did, and what was approved. This isn't surveillance — it's the same audit trail you'd want from any automated system that touches production code.

## Hardening for regulated environments

If you work in fintech, healthtech or another regulated industry, add on top of any preset:

- A **PreToolUse hook** that logs every file write (path, hash, timestamp, user) to an append-only destination.
- A **PreToolUse hook** that blocks writes containing secret patterns (API keys, private key headers, credentials).
- A permission boundary that prevents editing outside the project directory.
- Managed settings so none of the above can be disabled locally.

These are deliberately out of scope for the starter presets because they need to match your compliance regime; treat the list above as a checklist for your security team.

## Keeping CLAUDE.md and settings consistent

The "Do not do without explicit approval" list in `CLAUDE.md` is advisory to the model. The `deny`/`ask` rules in `settings.json` are the **enforced** version. When you change one, change the other.
