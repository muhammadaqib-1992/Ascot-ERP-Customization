# ISM / Sales Order — existing excluded item not flagged when order reopened in Edit Mode

- **Tracker:** [NACG-1010](https://folio3.atlassian.net/browse/NACG-1010)
- **Found:** 2026-09-23
- **Environment:** SB1 — https://628731-sb1.app.netsuite.com
- **Role:** Administrator
- **Linked test case:** none (ad hoc live validation, not from a written TC)

## Files
| File | Shows |
|---|---|
| 01_exclusion-rule-14-item-1000002-quebec.png | Sales Order Exclusion Rule list — rule #14: Item 1000002, State = Quebec, Valid From 9/1/2026, Valid To 9/30/2099 (active). |
| 02_so1523-saved-with-excluded-item.png | Sales Order SO1523 (id 57345), customer AVALED CORP (ship-to Quebec), saved successfully with item 1000002 on the line — "Transaction successfully Saved", Total 34.49. |
| 03_ism-edit-mode-no-flag.png | SO1523 reopened in Edit Mode, ISM opened from the Items subtab — "Added Items — Edit Mode" label confirms genuine edit-mode load; item 1000002 line shows no warning/flag, styled identically to a compliant line. |
| 04_control-fresh-order-correctly-excludes-item.png | Control/scope check: a brand-new, never-saved Sales Order for the same customer (SO1524) — searching "1000002" in ISM's Create Mode correctly returns 0 results. Shows the exclusion filter itself works on fresh searches; the gap is specifically about re-validating a line already present on a saved order. |

## Draft

**Title:** ISM / Sales Order — existing excluded item not flagged or blocked when order reopened in Edit Mode

**Environment:** SB1 — https://628731-sb1.app.netsuite.com
**Role:** Administrator

**Steps to Reproduce**
1. Confirm an active Sales Order Exclusion Rule exists (used: rule #14 — Item 1000002, State Quebec, Valid 9/1/2026–9/30/2099).
2. Open Sales Order **SO1523** (internal id 57345) — customer CUS104013-A AVALED CORP, ship-to state Quebec — which already has item 1000002 on its item line (see evidence 02).
3. Click **Edit** on the saved order.
4. On the Items subtab, observe the existing item 1000002 line.
5. Click the **ISM** button to open the Item Selector in Edit Mode (confirmed by the "Edit Mode" label next to "Added Items").
6. Observe the loaded line for item 1000002.
7. Attempt to Save the order.

**Actual Result**
The existing item 1000002 line — which matches an active exclusion rule for this order's ship-to state — shows **no warning, flag, or highlighting** anywhere: not on the native Sales Order sublist, and not when the same line loads into ISM's Edit Mode. The order can be saved/re-saved with the excluded item present, with no validation error.

For scope/control: a fresh, never-saved order for the same customer correctly excludes item 1000002 from ISM's Create Mode search results (evidence 04) — so the exclusion filter itself works on new searches. The gap is specifically that an **already-present line matching an active exclusion rule is never re-validated or flagged** when the order is reopened.

**Expected Result**
The Solution Document (REQ 9.2, "Order Behaviour if Ship To State/Province Changes") defines a restricted-item flagging and block-on-save mechanism for saved orders:
> "Restricted item lines will be clearly identified... **Critical Business Rule: A Sales Order cannot be saved or processed if it contains any restricted item lines**... System will display a validation error if save is attempted with restricted items present."

That section frames the trigger as a ship-to province *change*, not a plain reopen — so it's not 100% certain this rule is meant to apply on every edit-mode load. **This should be confirmed with the Solution Architect/BA:** should ISM/the native sublist re-validate exclusion for all existing lines on every edit-mode load (not just after a province change)? Either way, an order that currently, verifiably contains a Quebec-excluded item, with zero indication of the problem, is a gap against the spirit of the exclusion feature at minimum.

**Evidence**
`01_exclusion-rule-14-item-1000002-quebec.png`, `02_so1523-saved-with-excluded-item.png`, `03_ism-edit-mode-no-flag.png`, `04_control-fresh-order-correctly-excludes-item.png` — see Files section above.

**Priority:** High — per the priority guide, this is close to an access/compliance-control failure (a regulatory item-exclusion control silently not catching an existing violation), though not marked Critical since the *initial* exclusion check does work correctly on fresh searches (evidence 04) — this is a narrower re-validation gap, not a total control failure.
**Labels:** customization, REQ_9.2
**Linked test case:** none

## Open question for the team
Does the Solution Document intend exclusion re-validation to run on *every* edit-mode load of an order, or only as a reaction to a ship-to province change? The current build does neither for a plain reopen — confirming the intended scope will determine whether this is a full miss or a partial one.
