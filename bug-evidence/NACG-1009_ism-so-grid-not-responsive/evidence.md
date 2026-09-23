# ISM (Sales Order) — Added Items grid does not adapt to viewport width

- **Tracker:** [NACG-1009](https://folio3.atlassian.net/browse/NACG-1009)
- **Found:** 2026-09-23
- **Environment:** SB1 — https://628731-sb1.app.netsuite.com
- **Role:** Administrator
- **Linked test case:** none (ad hoc live validation, not from a written TC)

## Files
| File | Shows |
|---|---|
| 01_added-items-grid-1440x900.png | Added Items grid at 1440x900 (standard desktop) — grid cuts off after ~9 of 27 columns (Quantity through Price On Demand), horizontal scrollbar visible, despite ample unused width available in the window. |
| 02_added-items-grid-768x1024.png | Same grid at 768x1024 (tablet) — still fixed-width, cuts off after Currency; scroll position/column widths behave identically to the desktop view rather than adapting. |

## Draft

**Title:** ISM (Sales Order) — Added Items grid does not adapt to viewport width; always requires horizontal scroll

**Environment:** SB1 — https://628731-sb1.app.netsuite.com
**Role:** Administrator

**Steps to Reproduce**
1. Log in to NetSuite SB1 as Administrator.
2. Go to Transactions > Sales > Enter Sales Orders > New.
3. Select any Customer and Subsidiary, go to the Items subtab, click "ISM".
4. Add any item (tested with KIT-STRIPS-AC10-BK) with a Location selected.
5. With the ISM window's viewport at 1440x900 (standard desktop), observe the Added Items grid.
6. Resize the viewport to 768x1024 (tablet) and observe again.

**Actual Result**
At 1440x900, the Added Items grid table renders at a fixed width and cuts off after roughly 9 of the 27 documented columns (Line Number through Price On Demand), requiring horizontal scrolling to reach Customer Price, Margin %, Discount %, PLM Status, Vendor Rate, Unit Cost $, Reason, and Actions — this despite the surrounding page having ample unused width. At 768x1024 (tablet), the same fixed-width grid persists and cuts off even sooner (after Currency), with no reflow or column-width adjustment for the smaller viewport.

**Expected Result**
No explicit responsive-layout acceptance criterion was found for ISM in the Solution Document — flagging this against general UI expectations for what is the primary, daily-use item-entry screen (used across Sales Orders, Quotes, Contracts, Work Orders, etc. per REQ 9.2), rather than a specific documented requirement. Confirm with the team whether a responsive-behavior spec exists elsewhere before treating "expected" as settled.

**Evidence**
`01_added-items-grid-1440x900.png`, `02_added-items-grid-768x1024.png` — see Files section above.

**Priority:** Medium — the grid is fully functional via horizontal scroll (no data or workflow blocked), but this is the primary item-entry screen for every transaction type ISM supports, so the case for High is that it degrades the core daily workflow for all users rather than an edge case. Picking the lower priority per team convention; triage can raise it.
**Labels:** ui
**Linked test case:** none
