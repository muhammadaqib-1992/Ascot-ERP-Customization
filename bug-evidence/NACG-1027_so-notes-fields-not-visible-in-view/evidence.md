# Sales Order — Notes section fields not available/visible in View mode

- **Tracker:** [NACG-1027](https://folio3.atlassian.net/browse/NACG-1027)
- **Found:** 2026-09-25
- **Environment:** SB1 — https://628731-sb1.app.netsuite.com
- **Role:** Administrator
- **Linked test case:** REQ 17.1.6 (Internal Notes), REQ 17.1.7 (External Notes)

## Files
| File | Shows |
|---|---|
| 01_documented-note-types-reference.png | Reference design note (Basecamp/call) listing the 6 header-level note types: Internal Notes, External Notes, Picking Notes, Carrier Info, Billing Info, Web Instructions — with a SAP comparison showing how the equivalent dropdown-driven notes UI behaves there. |
| 02_so-notes-section-fields-not-visible.png | Sales Order record in SB1, "Notes" section expanded (red box) — shows the field labels (Internal Notes, External Notes, External Notes French, Picking Notes, Customer Notes) with none of them showing an available/visible field to view or enter content. |

## Draft

**Title:** Sales Order — Notes section fields (Internal Notes, External Notes, and related note fields) not available/visible on the record

**Environment:** SB1 — https://628731-sb1.app.netsuite.com
**Role:** Administrator

**Steps to Reproduce**
1. Log in to NetSuite SB1 as Administrator.
2. Open a Sales Order record.
3. Expand the **Notes** section.
4. Observe the fields under it: Internal Notes, External Notes, External Notes French, Picking Notes, Customer Notes.

**Actual Result**
None of the Notes-section fields are available on the record — confirmed live by the reporter. See screenshot 02.

**Expected Result**
Per REQ 17.1.6, Internal Notes should be available as a large text box for internal users to record status/context (never printed on customer-facing documents). Per REQ 17.1.7, External Notes should be available as a large text box whose content prints on the Sales Order Confirmation PDF. The broader Notes design (screenshot 01, from the project's call/Basecamp reference) also names Picking Notes, Carrier Info, Billing Info, and Web Instructions as note types tied to specific downstream documents (WMS picking instructions, Packing Slips, Invoices/Credits/Debits/RMAs, and B2B Portal special instructions respectively) — worth checking whether those are in scope for this same fix or a separate requirement.

**Priority rationale:** High — Internal/External Notes are functional requirements (17.1.6, 17.1.7) with defined downstream behavior (PDF printing, internal-only visibility); if unavailable, the order-communication workflow they support doesn't work at all.
**Labels:** customization, REQ_17.1.6, REQ_17.1.7
**Linked test case:** none

**Evidence:** `01_documented-note-types-reference.png`, `02_so-notes-section-fields-not-visible.png` — see Files section above.
