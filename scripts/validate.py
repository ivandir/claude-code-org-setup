#!/usr/bin/env python3
"""Validate the templates in this repo. No third-party dependencies.

Checks:
  1. Every settings preset is valid JSON with permissions.allow/ask/deny lists,
     disables bypass mode, and has no bare "Bash" in `ask` (it would shadow allow rules).
  2. Every skill has SKILL.md with `name` (matching its folder) and `description` front matter.
  3. No file contains an obvious credential pattern.
  4. Relative Markdown links resolve.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def check_settings() -> int:
    files = sorted((ROOT / "templates" / "settings").glob("settings.*.json"))
    if not files:
        err("no settings presets found in templates/settings")
    for f in files:
        rel = f.relative_to(ROOT)
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            err(f"{rel}: invalid JSON ({e})")
            continue
        perms = data.get("permissions")
        if not isinstance(perms, dict):
            err(f"{rel}: missing 'permissions' object")
            continue
        for key in ("allow", "ask", "deny"):
            if not isinstance(perms.get(key), list):
                err(f"{rel}: permissions.{key} must be a list")
        if perms.get("disableBypassPermissionsMode") != "disable":
            err(f"{rel}: must set permissions.disableBypassPermissionsMode to 'disable'")
        if "Bash" in perms.get("ask", []):
            err(f"{rel}: bare 'Bash' in ask shadows every Bash allow rule")
        overlap = set(perms.get("allow", [])) & set(perms.get("deny", []))
        if overlap:
            err(f"{rel}: rules both allowed and denied: {sorted(overlap)}")
    return len(files)


FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def check_skills() -> int:
    dirs = sorted(p for p in (ROOT / ".claude" / "skills").iterdir() if p.is_dir())
    for d in dirs:
        skill = d / "SKILL.md"
        rel = skill.relative_to(ROOT)
        if not skill.exists():
            err(f"{d.relative_to(ROOT)}: missing SKILL.md")
            continue
        m = FRONT_MATTER.match(skill.read_text(encoding="utf-8"))
        if not m:
            err(f"{rel}: missing YAML front matter")
            continue
        fields = dict(
            line.split(":", 1) for line in m.group(1).splitlines() if ":" in line
        )
        fields = {k.strip(): v.strip() for k, v in fields.items()}
        if fields.get("name") != d.name:
            err(f"{rel}: front matter name {fields.get('name')!r} != folder {d.name!r}")
        if not fields.get("description"):
            err(f"{rel}: missing description")
    return len(dirs)


SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}"),
    re.compile(r"sk-[A-Za-z0-9]{32,}"),
]


def tracked_files():
    for p in ROOT.rglob("*"):
        if p.is_file() and ".git" not in p.parts and p.suffix in {".md", ".json", ".py", ".yml", ".yaml"}:
            yield p


def check_secrets() -> None:
    for p in tracked_files():
        text = p.read_text(encoding="utf-8", errors="ignore")
        for pat in SECRET_PATTERNS:
            if pat.search(text):
                err(f"{p.relative_to(ROOT)}: matches credential pattern {pat.pattern!r}")


LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")


def check_links() -> None:
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts:
            continue
        in_fence = False
        for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
            if in_fence:
                continue
            for target in LINK.findall(line):
                if re.match(r"[a-z]+:", target) or target.startswith("mailto:"):
                    continue
                if not (p.parent / target).resolve().exists():
                    err(f"{p.relative_to(ROOT)}:{n}: broken link {target}")


def main() -> int:
    n_settings = check_settings()
    n_skills = check_skills()
    check_secrets()
    check_links()
    if errors:
        print("Validation failed:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {n_settings} settings presets, {n_skills} skills, no broken links or credential patterns.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
