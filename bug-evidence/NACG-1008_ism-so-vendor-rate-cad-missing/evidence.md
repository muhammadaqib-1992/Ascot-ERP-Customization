# ISM (Sales Order) — VENDOR RATE (CAD) column missing from Added Items grid

- **Tracker:** [NACG-1008](https://folio3.atlassian.net/browse/NACG-1008)
- **Found:** 2026-09-23
- **Environment:** SB1 — https://628731-sb1.app.netsuite.com
- **Role:** Administrator
- **Linked test case:** none (ad hoc live validation, not from a written TC)

## Files
| File | Shows |
|---|---|
| 01_vendor-rate-to-unit-cost-no-cad-column.png | Added Items grid on Sales Order (SB1, item KIT-STRIPS-AC10-BK), scrolled to the Vendor / Currency / Vendor Rate / Unit Cost $ / Reason / Actions column sequence — no "Vendor Rate (CAD)" column present between Vendor Rate and Unit Cost $. |

## Draft

**Title:** ISM (Sales Order) — VENDOR RATE (CAD) column missing from Added Items grid

**Environment:** SB1 — https://628731-sb1.app.netsuite.com
**Role:** Administrator

**Steps to Reproduce**
1. Log in to NetSuite SB1 as Administrator.
2. Go to Transactions > Sales > Enter Sales Orders > New.
3. Select any Customer (tested with CUS104013-A AVALED CORP) and Subsidiary.
4. Go to the Items subtab.
5. Click the "ISM" button (opens the Item Selection Module in a new window).
6. Search for and select any item (tested with KIT-STRIPS-AC10-BK).
7. Select a Location (e.g. Dorval) in the item detail panel.
8. Click "Add Item" to add it to the Added Items grid.
9. Inspect the full column set of the Added Items grid (scroll right through all columns).

**Actual Result**
The Added Items grid shows a "VENDOR RATE" column but no separate "VENDOR RATE (CAD)" column anywhere in the grid. Confirmed by reading every column header exposed by the grid — immediately after "Vendor Rate," the next column is "Unit Cost $," with nothing for Vendor Rate (CAD) in between or elsewhere in the header set.

**Expected Result**
Per the Solution Document, REQ 9.2 ("On Sales Order record, the following columns will be visible"), both **VENDOR RATE** and **VENDOR RATE (CAD)** are listed as required grid columns. The document further describes Vendor Rate (CAD) as "a new field... added to support functionality" and states it should be used "when creating the Purchase Order" alongside Vendor, Currency, and Vendor Rate (for automated PO creation from third-party/vendor-priced lines).

**Evidence**
`01_vendor-rate-to-unit-cost-no-cad-column.png` — see Files section above.

**Priority:** Medium — a documented field required for the vendor-rate/PO-creation flow is missing, but this affects only third-party/vendor-priced lines (a subset), and PO creation itself wasn't tested to confirm a full block. Could be raised to High if triage confirms this blocks accurate CAD-cost capture for automated PO creation as described in the spec.
**Labels:** customization
**Linked test case:** none
