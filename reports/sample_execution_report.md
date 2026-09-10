# Sample Execution Report

> **A format example, not a real run.** It exists so the shape is obvious before your first
> execution. Delete it once you have real reports.

---

## Test Execution Report

**Test Case ID:** TC_PDP_002 — Verify displayed quantity matches the ERP
**Requirement:** 14 — Inventory Availability on the Product Page
**Module / Feature:** Storefront / Inventory block — data accuracy
**Source:** written by qa-test-writing, this conversation
**Environment:** Sandbox — `https://staging.example.test`
**Role under test:** Anonymous
**Executed:** 2026-09-09 via browser MCP + backend MCP

### Steps

| # | Action | Expected | Actual | Status |
|---|---|---|---|---|
| 1 | Query per-location availability for item SKU-10237 in the backend | Baseline captured | Warehouse A (online) 40, Warehouse B (**offline**) 10, Warehouse C (online) 15 | Passed |
| 2 | Open the product page for SKU-10237 | Page loads with the inventory block visible | Page loaded; inventory block rendered below the price | Passed |
| 3 | Compare the displayed total against online locations only | Total shows 55 (40 + 15; offline excluded) | Total shows **65** — Warehouse B included in the sum | **Failed** |
| 4 | Confirm the per-location breakdown | Offline locations not listed | Warehouse B listed with 10 units | **Failed** |

### Result
**Failed** — offline locations are included in both the total and the breakdown, contradicting acceptance criterion 3.

### Defect ID
*(blank — draft offered to the user, not yet filed)*

### Comments
Reproduced on two items with offline stock (SKU-10237, SKU-10412), so this is not specific to one record. Sandbox only; not retested elsewhere. The acceptance criterion is unambiguous, so this is a genuine defect rather than a specification gap. The location's online/offline flag was read from the backend, not inferred from the storefront.

### Evidence
- Backend query result showing per-location availability with the online/offline flag
- Product page screenshot showing total 65 and the Warehouse B row
- Side-by-side of expected 55 vs. displayed 65

---

### What makes this report usable

- **Actual carries values, not verdicts.** "Total shows 65, expected 55" can be argued with; "didn't match" cannot be acted on.
- **Step 1 captured the baseline before touching the UI.** Without it there is nothing to compare against, and the run only proves that *a* number appeared.
- **Environment and role are stated.** A pass on the wrong environment is a false pass, and sandbox refreshes make that easy to do.
- **Comments record the limits of the run** — what was and wasn't retested, and whether the criterion was clear enough to call it a defect at all.
- **No defect was filed automatically.** That waits for the user.

### The same shape for other work

A **customization** case asserts the record state, not the screen: *"Order saved at 12,000 with status Pending Fulfilment; expected Pending Approval; approver field empty; user event script execution log shows no entry for this record."*

An **integration** case asserts both sides plus the log: *"Customer created in the source system at 14:02; no matching record in the CRM after 15 minutes; error-log custom record shows three retries then a 500; source transaction was correctly left unblocked."*

In both cases the failure is invisible on the screen the user was looking at, which is exactly why the report has to say where you actually looked.
