# Test Cases

Every approved batch of test cases lives here, one date-stamped file per batch. This folder is the team's record of **what was written, when, and from which source** — it is tracked in git on purpose.

`qa-test-writing` saves here automatically once you approve a draft in chat.

## Naming

```
YYYY-MM-DD_<ShortCode>_<short-slug>.md
```

| Part | Meaning | Example |
|---|---|---|
| `YYYY-MM-DD` | Date the batch was **approved** | `2026-09-12` |
| `<ShortCode>` | The feature's short code — same one used in the TC ids | `PDP` |
| `<short-slug>` | A few words describing the batch, hyphenated | `inventory-block` |

→ `2026-09-12_PDP_inventory-block.md`

The date prefix is what turns this folder into a timeline — sort by name and you see the order work was done in. Never drop it.

## File layout

```markdown
# 14 — Inventory Availability on the Product Page

- **Created:** 2026-09-12
- **Author:** <name>
- **Source:** Solution Document §14, acceptance criteria 1–5
- **Status:** Approved
- **Cases:** TC_PDP_001 – TC_PDP_008

| Test Case ID | Module | Feature | Test Case | Pre-Condition | Steps | Expected | Comments |
|---|---|---|---|---|---|---|---|
| ... |

## Notes
- TC_PDP_003 is Inferred — not in the acceptance criteria.
- Open dependency: <anything unresolved that affects expected results>
```

Columns follow `.claude/skills/qa-test-writing/references/test-case-format.md`.

## Statuses

| Status | Meaning |
|---|---|
| `Draft` | Saved on request before approval — not yet agreed |
| `Approved` | Reviewed and agreed; ready to execute |
| `Superseded by <file>` | Replaced by a newer batch for the same feature |

## Changing an existing batch

- **Small correction** → edit the file in place and add a line under the header: `- **Updated:** YYYY-MM-DD — <what changed>`.
- **New test cycle for the same feature** → new dated file. Mark the old one `Superseded by <new file>` so nobody executes the stale version.

Execution **results** don't go here — they go in `reports/`. This folder holds what *should* happen; `reports/` holds what *did*.
