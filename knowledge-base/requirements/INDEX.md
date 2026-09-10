# Index — requirements

Business requirements upstream of the solution documents. Use for scope questions — "was this ever asked for?", "is this in scope?".

**Read this index before opening anything in this folder.** Only open a source document when the row below tells you it is the one you need.

| Document | Covers | Notes |
|---|---|---|
| `brd-erp-implementation-v4.pdf` | ERP modules, customizations, approval workflows | Superseded by the solution documents wherever they disagree |
| `brd-storefront-v2.pdf` | B2B storefront scope, user roles, access levels | Origin of the role model the permissions matrix encodes |
| `change-requests/` | CRs raised after the BRD was signed | Each CR should say which feature it amends |
| `<filename>` | `<what it covers>` | `<version, status>` |

## Why this folder matters to QA

A defect and a change request look identical from the outside: the system does something other than what you expected. The difference is whether the behaviour was ever agreed. Before filing, check whether the requirement exists here at all — filing a CR as a defect wastes a triage cycle and erodes trust in the queue.

## Known gaps

- `<requirement area>` — discussed but never written up; confirm with `<owner>`.
