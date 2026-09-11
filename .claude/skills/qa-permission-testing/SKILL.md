---
name: qa-permission-testing
description: "Tests role-based access control end to end. Permissions are dynamic: access is configured per role in the application's admin settings and users are assigned a role, so this skill always re-checks the live configuration, not just the documented matrix. It looks up expected access (Allowed / Not Allowed / Not Applicable, plus scope such as own only) in the permissions matrix, compares it to what the admin screen actually has set, then logs in as a user holding that role to verify real behaviour. Use whenever the user asks to test or verify permissions, role-based access, RBAC, access levels, user roles, what a role can or cannot see, or references the permissions matrix. Not for general functional testing — use qa-test-execution."
---

# QA Permission Testing

Tests access control across three layers that are supposed to agree and frequently don't:

**Documented matrix** (what was agreed) → **live configuration** (what is actually set) → **application behaviour** (what a user really experiences).

Catching a disagreement between any two of those is the point of this skill.

## Ground rules

1. **This is dynamic, not a fixed checklist.** Permissions are reconfigurable at any time. Never assume the matrix reflects the live configuration — check the admin screen itself, especially when the user says they just changed something. *Whatever is currently granted is what should work.*
2. **The matrix is the acceptance baseline, not optional colour.** When the user hasn't stated an expected result, get it by running the lookup script. Never guess what a role "should" be able to do.
3. **Never store or write down credentials.** Read them from `.claude/qa-test-env.md`; if a value is a `<PLACEHOLDER>`, ask for that run only. Never put them in reports, screenshots, the tracker, or chat beyond the turn they are given.
4. **Access is not binary — check the scope.** "Allowed: own only" means the user sees *their* records. A user who can see the feature but also sees records belonging to someone else is a **failure**, even though the feature "works". Verify the negative half: confirm out-of-scope records are genuinely not reachable.
5. **Never auto-file a defect.** Report the failure and offer `qa-bug-reporting`.

## Step 1 — Look up the expected access

**Run the script — do not read the matrix into context:**

```bash
python scripts/lookup_permission.py --role "User L2" --feature "View pricing"
python scripts/lookup_permission.py --feature "Place order"      # every role at once
python scripts/lookup_permission.py --list-roles
python scripts/lookup_permission.py --matrix <path> --section "My Account"
```

It returns the verdict plus any scope qualifier. Only its output costs context, not the matrix.

**Only load `references/matrix-guide.md` if you need to read the matrix by hand** — the script failed, the matrix has an unusual shape, or you are auditing the script's logic.

## Step 2 — Confirm the live configuration

Open the application's role/permission admin screen and check what is *actually* granted to the role under test right now.

- **Live matches the matrix** → proceed, testing against that expectation.
- **They disagree** → stop and ask which is authoritative for this run. Usually the user has just changed something and wants to confirm it took effect; occasionally the drift *is* the finding. Don't silently pick one.

Confirm you are looking at the right role before reading or changing anything — admin screens commonly default to the first role in a list.

## Step 3 — Get a user holding that role

Access is enforced by the role on the logged-in account, so an admin login proves nothing about what a Level 2 user sees.

Use an existing test account for that role from the environment file. If none exists, check whether one can be created — but **don't create or modify user accounts without the user's explicit go-ahead**.

## Step 4 — Verify in the application

Log in as that user and attempt the specific action. Then check against Step 1's expectation:

| Expected | What "pass" requires |
|---|---|
| **Allowed** (no scope) | Feature reachable and fully usable |
| **Allowed: own only** | Reachable — *and* a record belonging to someone else is genuinely not reachable. Test both halves |
| **Allowed: own + parent / assigned accounts** | Both the in-scope sets are visible *and* an unrelated account's records are not |
| **Not Allowed** | Blocked — by whatever mechanism the app uses: hidden navigation, redirect, error page, disabled control |
| **Not Applicable** | Not a valid scenario for this role. Note and skip; don't force a result |

For anything scoped, the negative test is the one that matters. Confirming a user sees their own data proves very little; confirming they *cannot* reach someone else's is the actual security assertion.

## Step 5 — Report

Use the report shape in `qa-test-execution/references/report-format.md`, plus these fields:

```
**Role:** <role>            **Matrix expected:** <verdict + scope>
**Live config:** <matches matrix | differs — describe>
**Test account:** <identifier, never the password>
```

Always post the report in chat, and save it to `reports/YYYY-MM-DD_PERM_<role>-<feature>_<env>.md` using the date of the run — e.g. `reports/2026-09-12_PERM_L2-invoices_sandbox.md`. A re-test gets a new dated file, never an overwrite. Save failure screenshots to `bug-evidence/DRAFT_YYYY-MM-DD_PERM_<role>-<feature>/` and reference them by path (see `bug-evidence/README.md` — no credentials, session URLs or HAR files).

If the live configuration disagreed with the matrix, **call that out even on a pass** — it means the documented matrix is stale and someone should update it. On a failure, offer `qa-bug-reporting` and wait.
