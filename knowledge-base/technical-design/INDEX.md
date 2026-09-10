# Index — technical-design

Technical design (TDD) — the implementation spec for the same features the solution documents describe functionally. Reach for this when a defect might be a **configuration** root cause rather than a functional gap, or when a defect report needs a script or field identifier.

**Read this index before opening anything in this folder.** Only open a source document when the row below tells you it is the one you need.

| Document | Covers | Notes |
|---|---|---|
| `tdd-sca-extensions.gdoc` | Storefront extensions, features 14, 20, 21, 26, 29, 34, 44 | Per feature: extension name/version, config path, configuration JSON, prerequisites, impacted areas, data flow. **Keyed by the same numbers as the solution document** |
| `tdd-customizations.docx` | Custom records, fields, Suitelets, user event / scheduled / map-reduce scripts | Holds the script and deployment identifiers QA cites in defects |
| `tdd-integration-crm.docx` | RESTlet endpoints, authentication, payload shape, retry and error handling | Read before filing anything cross-system — most "integration bugs" are mapping or auth |
| `<filename>` | `<what it covers>` | `<version, status, known gaps>` |

## What QA usually needs from here

- **Configuration navigation path** — where a toggle actually lives, so "is it enabled?" can be answered instead of assumed.
- **Script / deployment identifiers** — a defect that cites the script id gets triaged faster than one that describes the symptom only.
- **Custom field and record identifiers** — needed to query the backend and verify what the UI displays.
- **Data flow** — which records are read and written, so you know what to check after an action.
- **Prerequisites** — a feature that silently depends on a custom field will fail confusingly if that field is missing in the environment you are testing.

## Cross-referencing rule

Cross-reference the solution document and the TDD **by feature number, not by title** — the titles drift apart between the two documents while the numbers stay stable.

## Known gaps

- Features present in the solution document but with no TDD section: list them here. A missing TDD section is not permission to guess a config path — say it isn't documented.
