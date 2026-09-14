# Index — technical-design

Technical design (TDD) — the implementation spec for the same features the solution documents describe functionally. Reach for it when a defect might be a **configuration** root cause rather than a functional gap, or when a defect report needs a script or field identifier.

**Read this index before opening anything in this folder.** Only open a source document when a row below says it is the one you need.

| Document | Covers | Notes |
|---|---|---|
| `Ascot Capital - Consice TDD for QA.docx` | Concise TDD written for QA. **Pricing engine:** request validation and parsing, data loading (CPS, customer pricing, item pricing matrix, product pricing fallback, item markup configuration), best-price calculation and the **price-source precedence hierarchy**. **Price export:** on-demand Suitelet export, scheduled queue→map/reduce→scheduled-script batch export, legacy matrix→delta→Excel pipeline. **Configuration:** customer and agent batch enrolment, File Cabinet folders (SB2 defaults), scheduled-script deployment pools, monthly batch parameter, PLM status defaults, item catalog scope, Suitelet access. Errors are logged to an error-message field on a queue custom record. 129 sections. | [Drive](https://drive.google.com/file/d/1lD6fOYP7bij2f93Sx1WlFKfwJ6dOLyUB/view) · modified 2026-09-14 · ~22,640 words, 321 tables · **auto-summary from section headings — needs review** |

## What QA usually needs from here

- **Configuration navigation path** — where a toggle actually lives, so "is it enabled?" can be answered rather than assumed.
- **Script / deployment identifiers** — a defect citing the script id gets triaged faster than one describing only the symptom.
- **Custom field and record identifiers** — needed to query the backend and verify what the UI displays.
- **Data flow** — which records are read and written, so you know what to check after an action.
- **Prerequisites** — a feature that silently depends on a custom field fails confusingly where that field is missing.

## Cross-referencing rule

Cross-reference the solution document and the TDD **by feature number, not by title** — titles drift apart between the two while numbers stay stable.

## Known gaps

- The summary above was generated from **section headings only**. Open the relevant section before citing a script id, field id or config path in a defect.
- 94 further headings are not itemised here.
- Whether this TDD's numbering matches the solution document's is **unverified** — check before cross-referencing by number.
