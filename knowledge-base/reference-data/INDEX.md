# Index — reference-data

Structured lookup data — permission matrices, configuration exports, test-data catalogues.

**Read this index before opening anything in this folder.** For files queried often, run the owning skill's script rather than reading the file by hand.

| File | Covers | How to read it |
|---|---|---|
| `permissions-matrix.example.csv` | Roles x features, with scope qualifiers | **Run** `.claude/skills/qa-permission-testing/scripts/lookup_permission.py` — do not read the file into context |
| `custom-fields-export.csv` | Custom field ids, types, applied record types | Grep for the field id when a defect needs it cited |
| `test-data-catalogue.md` | Known-good records per scenario: customers, items, orders | Saves re-discovering which record has the state a test needs |
| `<filename>` | `<what it covers>` | `<script, or read directly>` |

## Rule of thumb

If a file here gets queried more than a couple of times, it should have a **script** in the owning skill rather than being parsed ad hoc each run. A script's source never enters the context window — only its output does — and tested code beats code regenerated from scratch on every run.

`permissions-matrix.example.csv` is the worked example: see `.claude/skills/qa-permission-testing/`.

## Keeping this current

Exports go stale silently. Record the export date next to each file, and re-export before a release cycle rather than trusting last quarter's copy.
