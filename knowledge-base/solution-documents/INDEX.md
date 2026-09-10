# Index — solution-documents

Functional specification — how features are meant to behave, acceptance criteria, availability by role. The baseline for "what does pass mean".

**Read this index before opening anything in this folder.** Only open a source document when the row below tells you it is the one you need.

| Document | Covers | Notes |
|---|---|---|
| `sca-solution-document-v3.pdf` | SCA storefront, features 1–46 + appendix A-1…A-44 | Current baseline. **The appendix reuses core feature numbers with an `A-` prefix** — cite "Feature #29" vs "Appendix A-29", never "section 29" |
| `erp-customization-spec-v2.pdf` | Custom records, Suitelets, user event and scheduled scripts | Includes the acceptance criteria for the approval workflow |
| `integration-spec-crm-sync.docx` | Customer/contact sync to the CRM, field mapping, error handling | Field mapping table is the part QA needs; the sequence diagrams are background |
| `<filename>` | `<what it covers>` | `<version, status, known gaps, what supersedes it>` |

## Watch for

**Numbering collisions.** If your specification has both a core section list and a lettered appendix, they will eventually reuse numbers. Record the collisions here so nobody tests the wrong feature:

| Number | Core feature | Appendix (`A-` prefix) |
|---|---|---|
| 29 | Wishlist to quote (RFQ) | A-29 — News content type |
| 30 | Transaction history | A-30 — Projects content type |

## Known gaps

Record what is **not** documented. A named gap saves the agent from inventing an answer.

- Error-handling behaviour for the CRM sync when the remote system returns 5xx — not specified; confirm with the integration owner.
- Mobile breakpoints for the storefront — design files only, no written criteria.
