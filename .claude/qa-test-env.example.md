# QA Test Environment (TEMPLATE)

**This is the committed template. Do NOT put real credentials here.**

Setup, once per teammate:

1. Copy this file to `.claude/qa-test-env.md` (same folder, drop the `.example`).
2. Fill in your own values in that copy.
3. `.claude/qa-test-env.md` is git-ignored — it never gets committed or shared.

The `qa-*` skills read `.claude/qa-test-env.md` at the start of a run. Any field still showing `<PLACEHOLDER>` makes the skill ask you for that value in chat instead of guessing.

---

## Non-secret config (same for everyone)

### Environments

| Environment | URL | Notes |
|---|---|---|
| Development | `<URL>` | |
| Staging / test | `<URL>` | Environment of record for QA |
| Production | `<URL>` | Read-only. Never run destructive tests here |

### Backend / system of record

| Key | Value |
|---|---|
| System | `<e.g. the ERP, the primary database, the admin console>` |
| Account / instance id | `<ID>` — include the sandbox suffix if there is one |
| Admin URL | `<URL>` |
| Integration log location | `<where failed syncs are recorded — a custom record, a log table, a monitoring tool>` |
| Script / deployment ids in scope | `<ids QA needs to cite in defects, or "see technical-design INDEX">` |

### Issue tracker

| Key | Value |
|---|---|
| Tracker | `<e.g. Jira, Linear, Azure DevOps>` |
| Project key | `<KEY>` |
| Site URL | `<URL>` |

### Admin screens worth bookmarking

| Screen | URL |
|---|---|
| Role / permission configuration | `<URL>` |
| Feature flags / configuration | `<URL>` |

---

## Secrets — fill these in your local copy only

### Backend / admin login

| Key | Value |
|---|---|
| Username | `<PLACEHOLDER>` |
| Password | `<PLACEHOLDER>` |
| MFA | `<none | prompt me each run>` |

### Application test accounts, per role

Add a row per role you actually test. The role column is the important one — most access defects only show up when you log in as the specific role.

| Role | Environment | Username | Password |
|---|---|---|---|
| `<Role 1>` | Staging | `<PLACEHOLDER>` | `<PLACEHOLDER>` |
| `<Role 2>` | Staging | `<PLACEHOLDER>` | `<PLACEHOLDER>` |
| `<Admin>` | Staging | `<PLACEHOLDER>` | `<PLACEHOLDER>` |

> Anonymous/guest scenarios need no login.

---

## How the skills use this file

1. At the start of a run, the skill reads this file for URLs, identifiers, and the login matching the role the test requires.
2. A `<PLACEHOLDER>` or a missing row means the skill asks you in chat, for that run only.
3. MFA set to `prompt me each run` makes the skill pause for your code even when the username and password are present.
4. Credentials from this file authenticate the session and nothing else. They are **never** written into reports, screenshots, chat beyond the turn they are used, the tracker, or the project documents.

> **Why this file is git-ignored, and must stay that way:** credentials committed to git remain in history even after the file is deleted. Recovering from that means rotating every password and rewriting history for everyone. The `PreToolUse` hook in `.claude/hooks/block-secret-commit.sh` exists to stop that happening by accident — don't disable it.
