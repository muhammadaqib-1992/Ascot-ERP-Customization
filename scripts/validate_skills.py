#!/usr/bin/env python3
"""Validate every skill in .claude/skills against the agent-skills open standard.

    python scripts/validate_skills.py

Checks the constraints that fail silently — an over-length description is not rejected
loudly, it just risks being truncated where its trigger words live, and a name that does
not match its directory can stop the skill being found at all.

Exit code 1 if any ERROR is found, so this can gate a commit.
"""
import os
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

MAX_NAME, MAX_DESC, MAX_LINES = 64, 1024, 500
NAME_RE = re.compile(r"^[a-z0-9-]+$")
SKILLS_DIR = os.path.join(".claude", "skills")


def parse_frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None
    block, fields, key = m.group(1), {}, None
    for line in block.split("\n"):
        fm = re.match(r'^([A-Za-z-]+):\s*(.*)$', line)
        if fm:
            key = fm.group(1)
            fields[key] = fm.group(2).strip()
        elif key and line.strip():
            fields[key] += " " + line.strip()
    for k, v in fields.items():
        if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'":
            fields[k] = v[1:-1]
    return fields


def main():
    if not os.path.isdir(SKILLS_DIR):
        sys.exit(f"No {SKILLS_DIR} directory here. Run this from the workspace root.")

    errors = warnings = 0
    dirs = sorted(d for d in os.listdir(SKILLS_DIR)
                  if os.path.isdir(os.path.join(SKILLS_DIR, d)))
    if not dirs:
        sys.exit(f"No skills found in {SKILLS_DIR}.")

    print(f"Validating {len(dirs)} skill(s)\n")

    for d in dirs:
        path = os.path.join(SKILLS_DIR, d, "SKILL.md")
        issues = []

        if not os.path.isfile(path):
            print(f"  [ERROR] {d}: no SKILL.md")
            errors += 1
            continue

        text = open(path, encoding="utf-8").read()
        fm = parse_frontmatter(text)
        if fm is None:
            print(f"  [ERROR] {d}: no YAML frontmatter (must open with --- on line 1)")
            errors += 1
            continue

        name, desc = fm.get("name", ""), fm.get("description", "")
        lines = text.count("\n") + 1

        if not name:
            issues.append(("ERROR", "missing required field: name"))
        else:
            if name != d:
                issues.append(("ERROR", f"name '{name}' does not match directory '{d}'"))
            if not NAME_RE.match(name):
                issues.append(("ERROR", f"name '{name}' must be lowercase letters, digits and hyphens only"))
            if len(name) > MAX_NAME:
                issues.append(("ERROR", f"name is {len(name)} chars, limit {MAX_NAME}"))

        if not desc:
            issues.append(("ERROR", "missing required field: description"))
        else:
            if len(desc) > MAX_DESC:
                issues.append(("ERROR", f"description is {len(desc)} chars, limit {MAX_DESC} "
                                        f"(over by {len(desc) - MAX_DESC})"))
            elif len(desc) > MAX_DESC * 0.9:
                issues.append(("WARN", f"description is {len(desc)} chars, close to the {MAX_DESC} limit"))
            if len(desc) < 80:
                issues.append(("WARN", "description is very short - it is the matching field, "
                                       "so name the phrases a user would actually type"))
            if not re.search(r"\buse\b|\bwhenever\b|\btrigger", desc, re.I):
                issues.append(("WARN", "description does not say WHEN to use the skill"))

        if lines > MAX_LINES:
            issues.append(("WARN", f"SKILL.md is {lines} lines, over the {MAX_LINES}-line guideline - "
                                   "consider moving reference material into references/"))

        # progressive disclosure: bundled files should be pointed at from SKILL.md
        for sub in ("references", "scripts", "assets"):
            subdir = os.path.join(SKILLS_DIR, d, sub)
            if os.path.isdir(subdir):
                for f in sorted(os.listdir(subdir)):
                    if f not in text:
                        issues.append(("WARN", f"{sub}/{f} is never mentioned in SKILL.md - "
                                               "unreferenced bundled files are dead weight"))
        if os.path.isdir(os.path.join(SKILLS_DIR, d, "reference")):
            issues.append(("WARN", "folder is named 'reference'; the open standard uses 'references'"))

        status = "OK" if not issues else ("FAIL" if any(s == "ERROR" for s, _ in issues) else "WARN")
        print(f"  [{status:4}] {d}  (name {len(name)}, desc {len(desc)}/{MAX_DESC}, {lines} lines)")
        for sev, msg in issues:
            print(f"           {sev}: {msg}")
            if sev == "ERROR":
                errors += 1
            else:
                warnings += 1

    print(f"\n{errors} error(s), {warnings} warning(s)")
    if errors:
        print("Errors must be fixed - they can stop a skill loading or matching correctly.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
