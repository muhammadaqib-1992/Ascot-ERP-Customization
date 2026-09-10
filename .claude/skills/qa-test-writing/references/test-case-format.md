# Test Case Format

Reference for `qa-test-writing`. **Only load this when you are about to produce or review a test-case table.**

Adapt the columns to match your team's actual tracker or spreadsheet — the point is that a case written by the agent looks identical to one written by a human, so they can live in the same sheet without reformatting.

## Columns

| Column | What goes in it |
|---|---|
| **Requirement** | The section heading, exactly as it appears in the source document — full id + name, so a reader can find it |
| **Test Case ID** | `TC_<ShortCode>_00X` — see the convention below |
| **Module** | Broad area (e.g. `Storefront`, `Checkout`, `My Account`, `Customization`, `Integration`) |
| **Feature** | The specific sub-area within that module |
| **Test Case** | A one-line scenario title — the name, not the steps |
| **Pre-Condition** | Setup that must be true before step 1: configuration state, records that must exist, which role is logged in |
| **Steps** | Numbered, specific, unambiguous actions |
| **Expected** | What should happen. Cite the acceptance criterion it came from where possible |
| **Status** | Blank at authoring time — filled during execution |
| **Defect ID** | Blank — filled only if execution fails and a defect is filed |
| **Comments** | Anything a reviewer needs: `Inferred`, deferred reason, data substitutions, open dependencies |

## Short-code convention

Reuse the existing short code for a feature if one exists; otherwise create a short readable abbreviation and stay consistent across every case for that feature.

| Area | Short code |
|---|---|
| Storefront product page | `PDP` |
| Product listing page | `PLP` |
| Request for quote | `RFQ` |
| Checkout | `CHK` |
| Role permissions | `PERM` |
| Approval workflow (customization) | `APPR` |
| CRM sync (integration) | `SYNC` |

When continuing an existing series, number sequentially from the last known case. If you can't see the current state of the sheet, **ask for the last-used number** rather than guessing and risking a collision.

## Worked examples

Three shapes worth having in mind, because they fail in different ways.

### Storefront / UI

```
### 14 — Inventory Availability on the Product Page

| Test Case ID | Module | Feature | Test Case | Pre-Condition | Steps | Expected | Comments |
|---|---|---|---|---|---|---|---|
| TC_PDP_001 | Storefront | Inventory block — layout | Verify the availability table renders with all columns | Item stocked in 2+ locations; feature enabled | 1. Open the product page for the item. 2. Scroll below the price. | Table shows Location, Available Qty and Incoming Qty columns | |
| TC_PDP_002 | Storefront | Inventory block — data | Verify displayed quantity matches the ERP | Item has known per-location quantities | 1. Note available qty per location in the backend. 2. Open the product page. | Displayed total equals the sum of **online** locations only; offline locations excluded | Criterion 3 |
| TC_PDP_003 | Storefront | Inventory block — zero stock | Verify zero-stock locations are hidden | Item has a location with 0 available; "hide zero stock" = On | 1. Confirm the config. 2. Open the product page. | The zero-stock location is not listed | Inferred — not in criteria |
```

### Customization (script / workflow)

Server-side behaviour needs a record-state assertion, not a screen assertion:

```
### Approval workflow — orders above threshold

| Test Case ID | Module | Feature | Test Case | Pre-Condition | Steps | Expected | Comments |
|---|---|---|---|---|---|---|---|
| TC_APPR_001 | Customization | Approval routing | Order above threshold routes for approval | Threshold configured at 10,000; user lacks approval permission | 1. Create an order totalling 12,000. 2. Save. | Status is set to Pending Approval; the approver field is populated per the routing rule | |
| TC_APPR_002 | Customization | Approval routing | Order below threshold does not route | Same config | 1. Create an order totalling 500. 2. Save. | Status is Pending Fulfilment; no approval record created | Boundary pair with 001 |
| TC_APPR_003 | Customization | Approval routing | Order exactly at threshold | Same config | 1. Create an order totalling exactly 10,000. 2. Save. | Per criterion: "above" is exclusive, so it does **not** route | Boundary — criterion wording ambiguous, confirm |
```

Note TC_APPR_003: boundary conditions are where specifications are most often ambiguous, and flagging that ambiguity is worth more than the test.

### Integration

Integration cases need both sides asserted, plus the failure path — which is where most real defects live:

```
### CRM customer sync

| Test Case ID | Module | Feature | Test Case | Pre-Condition | Steps | Expected | Comments |
|---|---|---|---|---|---|---|---|
| TC_SYNC_001 | Integration | Customer create | New customer propagates to the CRM | Integration enabled; CRM reachable | 1. Create a customer with all mapped fields. 2. Wait for the sync window. | Record exists in the CRM with every mapped field matching, per the mapping table | |
| TC_SYNC_002 | Integration | Field mapping | Unmapped field is not sent | Same | 1. Populate a field absent from the mapping. 2. Trigger the sync. | Sync succeeds; the unmapped value is absent from the CRM payload | |
| TC_SYNC_003 | Integration | Error handling | Remote 5xx is retried, then logged | Ability to simulate a 5xx from the CRM | 1. Force a 5xx. 2. Trigger the sync. | Three retries with backoff, then an error-log record is written; the source transaction is **not** blocked | Per 2026-04-07 call decision |
```

## Anti-patterns

| Don't | Why |
|---|---|
| "Verify the page works correctly" | Cannot fail, so it cannot pass either |
| Bundling three assertions into one case | You lose which one broke |
| "Log in as any user" | Role is usually the variable being tested — name it |
| Expected results written from general reasoning | If it isn't in a document, mark it Inferred or leave it out |
| Steps that assume state from a previous case | Cases get run out of order, in parallel, or alone |
| Testing only the happy path of an integration | The failure path is where the defects are |
| Asserting the UI for server-side logic | A script's job is the record state; the screen is a side effect |
