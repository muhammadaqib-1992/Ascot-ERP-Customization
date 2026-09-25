# Item — Minimum Order Quantity still backed by custom field custitem_f3_minumun_order_quantity

- **Tracker:** [NACG-1026](https://folio3.atlassian.net/browse/NACG-1026) — related to [NACG-615](https://folio3.atlassian.net/browse/NACG-615)
- **Found:** 2026-09-25
- **Environment:** SB1 — https://628731-sb1.app.netsuite.com
- **Role:** Administrator
- **Linked test case:** none (verification of NACG-615)

## Files
| File | Shows |
|---|---|
| 01_field-help-shows-custom-field-id.png | Item record (internal id 61763), Sales/Pricing subtab, Field Help popup opened on the "Minimum Order Quantity" field — shows Field ID `custitem_f3_minumun_order_quantity`, Field Value 5, "This is a custom field created for your account." |

## Draft

**Title:** Item — "Minimum Order Quantity" field still driven by custom field custitem_f3_minumun_order_quantity, not the standard field (NACG-615 AC not met)

**Environment:** SB1 — https://628731-sb1.app.netsuite.com
**Role:** Administrator

**Steps to Reproduce**
1. Log in to NetSuite SB1 as Administrator.
2. Open an Item record (reproduced on internal id 61763, an Assembly item).
3. Go to the Sales/Pricing subtab.
4. Locate the "Minimum Order Quantity" field (shows value 5 in this example, with "Enforce Minimum Internally" checked).
5. Open Field Help on that field (right-click or the page's field-help option) to see its underlying Field ID.

**Actual Result**
Field Help reports Field ID `custitem_f3_minumun_order_quantity` — the original Folio3 custom field — still backing the "Minimum Order Quantity" field on the form, with Field Value 5. It reads "This is a custom field created for your account."

**Expected Result**
Per NACG-615 ("Minimum Order Qty Field to be Move to Standard Field"), Acceptance Criteria: "Remove the Custom Field implementation. Use the Standard Minimum Order Field. Field ID: custitem_f3_minumun_order_quantity." That ticket is currently in **Ready for QA** status — meaning it was expected to be done. This screenshot shows the custom field implementation is still in place, so the acceptance criteria has not actually been met.

**Related:** [NACG-615](https://folio3.atlassian.net/browse/NACG-615) — this is a failed verification of that ticket's acceptance criteria, not an independent new requirement. Worth considering whether this should instead be a comment/reopen on NACG-615 rather than a separate ticket — filed separately per explicit instruction, linked both ways.

**Priority:** High — NACG-615 itself was rated Critical; this shows its fix isn't actually in place, which blocks sign-off on that Critical item. Not raised to Critical here since there's no evidence yet of active data corruption from the leftover field, just that the decided-on standard-field migration hasn't happened.
**Labels:** customization
**Linked test case:** none

**Evidence:** `01_field-help-shows-custom-field-id.png` — see Files section above.
