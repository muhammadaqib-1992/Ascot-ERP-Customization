# Call / Meeting Index

**Purpose:** don't open raw transcripts to answer a question — scan this index first. Each entry summarises one call. Open the underlying recording or transcript **only** when you need exact wording, a quote, or a detail finer than what is captured here.

> The entries below are examples showing the shape and the level of detail that makes an index useful. Replace them with your own.

---

## Quick lookup — topic to calls

Maintain this so a topic question resolves to a short list of dates instead of a scan.

| Topic / feature | Discussed in |
|---|---|
| Pricing engine / contract pricing | 2026-03-16, 2026-05-13 |
| Role permissions matrix | 2026-02-10, 2026-05-20 |
| CRM customer/contact sync | 2026-01-14, 2026-04-07 |
| Approval workflow customization | 2026-02-24 |
| Storefront quote-to-order (RFQ) | 2026-04-21, 2026-05-06 |

---

## Calls

### 2026-05-20 — `2026-05-20_permissions-review.vtt`
**Topics:** Permissions matrix scope review; quote-to-order emails; debit memo scope.
**Decisions:** Matrix corrected — quotes, sales orders, invoices and credit memos are visible **own + parent** (whole company), while RFQs stay **own only** because they are not yet real transactions. RFQ submission sends two emails: one to the submitter, one to a per-subsidiary internal address.
**Open items:** Multi-IP restriction per customer requested; the field is currently single-value. Owner: integration lead.
**Participants:** QA lead, PM, solution architect, client stakeholder.

### 2026-04-07 — `2026-04-07_integration-checkpoint.vtt`
**Topics:** CRM sync error handling; retry policy; field mapping gaps.
**Decisions:** Failed syncs retry three times with backoff, then write to the error log custom record rather than blocking the transaction. Mapping for the tax-exemption field deferred to phase 2.
**Open items:** Who monitors the error log in production — unassigned.
**Participants:** Integration developer, QA lead, PM.

### 2026-03-16 — `2026-03-16_pricing-engine.vtt`
**Topics:** Where contract pricing is owned; storefront vs ERP.
**Decisions:** The storefront holds **no** pricing data of its own — price is always sourced live from the ERP pricing engine. Fallback when the service is unavailable is a configured default price, **not** the platform's native catalogue price.
**Open items:** Confirm quantity-tier breakpoints are honoured on the committed order, not just in the storefront display.
**Participants:** Solution architect, QA lead, client stakeholder.

---

## Excluded / misfiled

List anything in this folder that is **not** part of this project, so nobody wastes a read on it.

| File | Why excluded |
|---|---|
| `2026-02-02_other-client.vtt` | Different client — uploaded to the wrong folder |
| `2026-03-16_pricing-engine (1).vtt` | Duplicate recording of the same call |

---

## Keeping this current

The index is only trustworthy if it is written when the call happens. A useful habit: add the entry before the recording is filed. An index that lags reality is worse than none, because the agent will trust it.

**Decisions recorded here often supersede the written specification** — teams rarely go back and update documents after changing their minds. The 2026-03-16 entry above is a typical case: if the solution document still describes a native-pricing fallback, the document is stale and the call is right. When the two disagree, that conflict is itself the finding; surface it rather than picking a side.
