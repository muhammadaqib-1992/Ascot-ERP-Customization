# Priority and Label Guide

Reference for `qa-bug-reporting`. **Only load this when you are actually assigning a priority or labels.**

Replace these with your team's real scheme — the value is in having *one* scheme applied consistently, not in this particular one.

## Priority

Priority answers "how soon", not "how annoying". Decide with two questions: **how many users are affected**, and **is there a way around it**.

| Priority | Criteria | Examples |
|---|---|---|
| **Critical** | Blocks a core workflow with no workaround; data loss or corruption; a security or access-control failure | Checkout cannot complete; a user sees another customer's pricing or invoices; a scheduled script fails silently and orders stop syncing |
| **High** | Major feature wrong or unusable, but a workaround exists; incorrect data shown to users | Price displays incorrectly until refresh; approval routes to the wrong approver; sync drops one mapped field |
| **Medium** | Feature works with a defect that degrades it; affects a subset of users or a less common path | Sorting wrong on one column; a validation message is unclear; retry backoff shorter than specified |
| **Low** | Cosmetic, or an edge case unlikely to be hit | Alignment off by a few pixels; typo in a tooltip |

Rules that stop priority inflation:

- **Access-control failures are Critical**, even when they look minor. A role seeing data it shouldn't is not a Medium.
- **Wrong data shown confidently outranks a visible error.** A page that errors is safer than a page quietly showing the wrong number — users act on the wrong number.
- **Silent failures outrank loud ones.** A background script or integration that fails without surfacing anywhere is worse than the same failure with an error on screen, because nobody finds out until reconciliation.
- **"Blocks my testing" is not automatically Critical.** If it blocks a test but not a user, say so in the body and price it on user impact.
- If torn between two levels, pick the lower and **make the case for the higher in the body**. A triage lead can raise it; nobody audits things that were over-prioritised.

## Labels

| Label | Use when |
|---|---|
| `regression` | This used to work. **Say which build or release it last worked in** |
| `data-accuracy` | Displayed value disagrees with the system of record |
| `permissions` | Role-based access behaves differently from the documented matrix |
| `ui` | Visual or layout only, no functional impact |
| `integration` | Failure crosses a system boundary |
| `customization` | Root cause is in custom code — a script, workflow or custom record |
| `config` | Root cause looks like configuration rather than code |
| `needs-info` | Filed to keep a trail, but not reliably reproducible yet |
| `blocked` | Cannot be verified until something else is resolved |

## Detail that saves a triage round-trip

Different failure types get bounced back for different missing information. Include it up front:

| Type | Include |
|---|---|
| **Storefront / UI** | Browser and viewport, the role logged in, whether it reproduces on a hard refresh |
| **Customization** | The script or workflow identifier, the record id it happened on, the execution log entry if you can reach it |
| **Integration** | Both system ids, the payload or its shape, the timestamp, and whether it retried |
| **Permissions** | The role, the documented expectation, **and** whether the live admin configuration matched that expectation when you tested |

That last one matters: an access defect where the live configuration was already wrong is a configuration problem, not a code problem, and it goes to a different person.

## Environment and role

Always record both. A defect reproducing for one role and not another **is** the finding, and it is the first thing a developer will ask. If you only tested one role, say so explicitly rather than leaving the reader to assume you covered them all.

Environments matter more than people expect: sandboxes get refreshed, configuration drifts between them, and "works in one, fails in the other" is itself diagnostic.

## Duplicates

Search the tracker before filing. If something similar exists:

- **Same root cause, same symptom** → comment on the existing defect with your new evidence.
- **Same symptom, plausibly different cause** → file separately and link it, explaining why you think it's distinct.

When unsure, file and link. A linked duplicate costs a triage minute; a missed second bug costs a release.
