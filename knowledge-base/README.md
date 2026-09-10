# Knowledge Base

Every project document the QA agent is allowed to reason from. Drop files into the right folder, then **write the index** — the index is what makes this affordable.

## The rule that makes this work

> **Never open a raw source document to answer a question an index could answer.**

A 200-page solution document or a 90-minute call transcript will happily consume most of a context window. Each folder therefore carries an index summarising what is inside; the agent reads the index, and opens a source file **only when the index points at a specific one**. `qa-context-lookup` enforces this order automatically.

If you add documents but skip the index, you have made the knowledge base *worse* — the agent now has more to wade through and no map.

## Routing map

Keep this table current. It is the first thing the agent consults.

| Topic / keyword | Folder | Index |
|---|---|---|
| Feature behaviour, acceptance criteria, functional spec | `solution-documents/` | `solution-documents/INDEX.md` |
| Implementation detail, config paths, field/script identifiers, data flow | `technical-design/` | `technical-design/INDEX.md` |
| Business requirements, scope, BRD | `requirements/` | `requirements/INDEX.md` |
| Contractual scope, deliverables, SOW | `contracts/` | `contracts/INDEX.md` |
| Decisions, rationale, "was this discussed", timeline, open items | `call-recordings/` | `call-recordings/INDEX.md` |
| Permission matrices, config exports, lookup tables, test data | `reference-data/` | `reference-data/INDEX.md` |

## Folders

| Folder | What goes in it |
|---|---|
| **`solution-documents/`** | Functional specification — how features are meant to behave, acceptance criteria, availability by user role. The baseline for "what does pass mean". |
| **`technical-design/`** | TDD / technical design — implementation spec for the same features: components and versions, configuration paths, field and script identifiers, prerequisites, data flow. Reach for this when a defect might be a configuration root cause rather than a functional gap. |
| **`requirements/`** | BRD and requirement sources upstream of the solution document. Useful for "was this ever in scope". |
| **`contracts/`** | SOW and contractual scope. Rarely needed for test execution — keep it here so scope questions have an answer. |
| **`call-recordings/`** | Meeting transcripts plus `INDEX.md`. **The index is mandatory here** — raw transcripts are the single most expensive thing in the repo to read. |
| **`reference-data/`** | Structured lookup data: permission matrices, configuration exports, test-data catalogues. If a file here is queried often, give the querying skill a script rather than parsing it by hand each run (see `ARCHITECTURE.md`). |

## Cross-document rule

Most application behaviour traces back to a decision recorded somewhere else. Before concluding a defect is UI-only, check whether an upstream document or a call decision explains it. Where two sources conflict — a call decision versus a written spec — **flag the conflict rather than silently choosing one**. Written documents are frequently not updated after a decision changes.

## A note on large binaries

PDFs, spreadsheets and recordings are fine here, but remember they stay in git history forever once committed. If a document is large, sensitive, or changes often, consider linking to it from the relevant `INDEX.md` instead of committing the file itself.
