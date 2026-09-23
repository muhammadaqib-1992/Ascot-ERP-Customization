# Execution Report Format

Reference for `qa-test-execution`. **Only load this when you are about to write a report.**

Match your team's tracker columns so a report can be pasted straight in without reformatting.

## Template

```markdown
## Test Execution Report

**Test Case ID:** TC_XXX_00X — <title>
**Requirement:** <full requirement heading from the source document>
**Module / Feature:** <...> / <...>
**Source:** <test-cases/ file | pasted in chat | ticket id | written by qa-test-writing | steps given directly and written down this run>
**Environment:** <env name and URL>
**Role under test:** <role>
**Executed:** <date> via Playwright MCP [+ backend/NetSuite MCP via qa-test-data-prep, or the stated fallback — see test-data.md]

### Steps

| # | Action | Expected | Actual | Status |
|---|---|---|---|---|
| 1 | ... | ... | ... | Passed / Failed / Blocked / N/A |

### Result
**Passed / Failed / Blocked / Deferred** — <one line: what decided it>

### Defect ID
<blank unless a defect was drafted and confirmed in this same conversation>

### Comments
<data substitutions, deferred reasons, open dependencies, anything ambiguous,
 anything you skipped and why>

### Evidence
<screenshots taken, one line each>

### Test Data
<see the sibling `test-data.md` in this run's folder for the full record>
```

## Writing the Actual column

This is the column that gets read when someone disputes the result, so it carries the evidence. Values, not verdicts:

| Weak | Strong |
|---|---|
| "Didn't match" | "Page shows 65; backend shows 55 — the offline location was included" |
| "Error appeared" | "Banner: 'Unable to load pricing (503)'; console shows a failed call to the pricing endpoint" |
| "Worked" | "Total updated to 55 without a page reload, matching the sum of online locations" |
| "Sync failed" | "Sync returned 500 after 3 retries; error-log record created with the payload; source order left in Pending" |
| "Approval didn't trigger" | "Order saved at 12,000 with status Pending Fulfilment; expected Pending Approval; approver field empty" |

## Verifying different kinds of work

The same report shape, but "actual" comes from a different place.

| Type | Where the truth lives | Common false pass |
|---|---|---|
| **Storefront / UI** | What the browser renders, cross-checked against the backend record | The page shows a cached value that no longer matches the record |
| **Customization** (scripts, workflows) | The **record state** after the action — status, field values, records created | The screen shows a success toast while the script silently failed downstream |
| **Integration** | **Both systems**, plus the log | Source system looks fine; the remote never received it, or received it with a field missing |

For integration cases especially: a report asserting only the source side has verified half the test. State what you saw on the far side, or say that you couldn't check it.

## Status vocabulary

| Status | Use when |
|---|---|
| **Passed** | Actual matched expected, and you verified it rather than assuming it |
| **Failed** | Actual contradicted expected. This is a finding, not a problem with the run |
| **Blocked** | Could not execute — a prior step failed, the environment was down, data was missing |
| **Deferred** | Deliberately not run this cycle. Say why |
| **N/A** | The case doesn't apply to this configuration or role |

## Honesty rules

These exist because a report is acted on by people who weren't watching the run:

- **Never mark Passed on a step you didn't actually verify.** If you inferred it from a later screen, say so.
- **Report partial runs as partial.** A report covering 4 of 9 steps says so at the top.
- **State the environment.** A pass on the wrong environment is a false pass, and a surprisingly common one — sandboxes get refreshed and URLs get reused.
- **If you changed data to satisfy the pre-condition, record what you changed.** The next person running against that record needs to know.
- **Asynchronous results need a stated wait.** "No record after 5 minutes" is a result; checking once immediately and calling it failed is not.
