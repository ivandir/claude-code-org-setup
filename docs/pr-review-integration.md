# PR review integration

AI-assisted code changes where the risk sits. It is syntactically clean and passes tests far more often than it is *right for your system*, so review has to shift from "does it compile and look tidy" to "is it correct, secure, and does the author understand it".

## Principles

1. **The author owns the change.** "Claude suggested it" is never an answer to a design question.
2. **Disclose, don't police.** Marking a PR as AI-assisted tells the reviewer where to look. It is not a confession, and it should never lower the review bar.
3. **The same bar for all code.** AI-assisted or not, a PR is accepted on correctness, security and clarity.
4. **Keep diffs small.** AI makes large diffs easy to produce and hard to review. Split them.

## The PR template

Copy [`.github/pull_request_template.md`](../.github/pull_request_template.md). It adds an **AI assistance** section asking:

- Was AI used? (None / assisted / mostly generated)
- What did you verify yourself?
- Anything you are unsure about?

## Reviewer checklist for AI-assisted changes

- [ ] Does the change match the **stated intent** — and is the intent stated?
- [ ] Is the logic *right*, not just plausible? Trace one non-trivial path by hand.
- [ ] Does it follow **existing architecture and patterns**, or invent a parallel one?
- [ ] Are **security implications** considered (input validation, authz, secrets, PII in logs)?
- [ ] Do the **tests** assert behavior and cover failure paths, or just mirror the implementation?
- [ ] Are there **unneeded changes** — reformatting, renamed things, extra abstractions?
- [ ] Ask the author: *"Do you understand why this works?"* for anything non-obvious.

## Using Claude for the first pass

The [`review-pr`](../.claude/skills/review-pr/SKILL.md) skill produces a structured first-pass review (blocking issues, suggestions, questions, test gaps). Use it to **prepare**, not to replace the human reviewer — and verify any claim before repeating it in a comment.

## What not to automate

- **PR descriptions.** In our rollout, generated descriptions were generic and missed the *why*; PRs using them were flagged more often for lacking context. Let AI draft a summary of *what* changed if you like, but write the reasoning and trade-offs yourself.
- **Approval.** A human approves.

## Handling the over-reliance pattern

If you see correct-looking but architecturally naive or insecure code repeatedly from one author:

1. Ask the "do you understand why this works?" question in review.
2. Pair on the next task so they can see calibrated use.
3. Fix it with culture and coaching. Don't respond with more tooling restrictions.
