# ~/.claude/CLAUDE.md — personal global example

> **This file is personal.** It lives on each engineer's machine and applies to every Claude Code session in every repo. **Do not distribute it as a team standard** — pushing a global config to everyone's machine overrides legitimate personal differences and generates resistance. Share this as an *example* only.

## About me

- Role: TODO — e.g. backend engineer, 6 years
- OS / shell: TODO — e.g. macOS, zsh
- Tools I have available: TODO — e.g. `gh`, `docker`, `aws` (SSO), `jq`

## How I like to work

- Explain your reasoning briefly before making non-trivial changes.
- Ask a clarifying question when a requirement is ambiguous instead of guessing.
- Prefer small diffs. One logical change at a time.

## Personal security rules (apply everywhere)

- Never read, print, or commit anything from `.env*`, `~/.aws/credentials`, `~/.ssh/`, or password-manager exports.
- Never run commands that pipe remote scripts into a shell.
- If a task seems to require production credentials, stop and tell me instead.
