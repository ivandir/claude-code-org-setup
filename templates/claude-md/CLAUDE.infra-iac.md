# CLAUDE.md — Infrastructure as code

## Project overview

TODO(team): Tooling (CDK / Terraform / CloudFormation), accounts and regions managed, and the blast radius of a bad apply.

- **Environments:** TODO(team) — dev / staging / prod and how they're separated
- **State / deploy:** TODO(team) — where state lives and who/what applies it

## Commands

```bash
# TODO(team): synth / plan / diff commands — the READ-ONLY ones
cdk diff        # or: terraform plan
```

## Conventions

- Always produce a plan/diff and show it before proposing an apply. **Never apply or deploy on your own.**
- Least privilege: no `*` actions or `*` resources in IAM unless explicitly justified in a comment.
- Everything is tagged (`owner`, `env`, `cost-center`). Stateful resources set an explicit removal/retention policy.
- No hard-coded account IDs, regions, or secrets — use context/variables and the secrets manager.
- Prefer existing shared modules/constructs over new bespoke resources.

## Do not do without explicit approval

- Run `apply`, `deploy`, or `destroy` against any environment
- Change anything that causes resource **replacement** (call out replacements explicitly in the diff summary)
- Modify networking, IAM boundaries, or encryption settings
- Touch state files or backends

## Review focus

When reviewing a diff: list resources that will be created / changed / **replaced / destroyed**, and flag anything publicly exposed.
