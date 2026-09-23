---
name: qa-bug-reporting
description: "Drafts and files defects for this QA project in the team's standard format. Use whenever a test fails, a defect is found, or the user wants to log, create, draft, raise or report a bug or ticket. Triggers on phrases like 'create a bug', 'log a defect', 'raise a ticket', 'report this issue', 'this is broken', 'this isn't working as expected', or any time qa-test-execution produces a Failed result and the user asks to write it up. ALWAYS drafts the defect in chat for review first — NEVER creates it in the tracker without explicit user confirmation such as 'create it' or 'go ahead'. Keeps each defect's screenshots, recordings and logs together in bug-evidence/. Do NOT use for writing test cases (qa-test-writing) or running them (qa-test-execution)."
---

# QA Bug Reporting

Turns a failure into a defect report a developer can act on without coming back to ask questions. Drafts in chat first, files only on explicit instruction.

**Tracker for this project:** Jira, project key **NACG**. File defects there unless the user names a different project for a specific ticket.

**Only load `references/priority-and-labels.md` when you are actually assigning a priority or labels** — it holds the full decision tables.

## The golden rule

**Draft first. File only when the user explicitly says so.**

"Create it", "go ahead", "file it" are confirmations. "This is broken" is not — that is a description of a problem, and the correct response is a draft. Filing a defect is visible to the whole team and awkward to undo; a draft costs nothing.

## Step 1 — Gather what a developer will need

Before drafting, make sure you have:

- **What was done** — the exact steps, not a summary of them
- **What happened** — actual behaviour, with real values
- **What should have happened** — and the document or acceptance criterion that says so
- **Where** — environment, URL, role, and any relevant configuration state
- **Evidence** — screenshots, recordings, console errors, backend values, all saved in the defect's `bug-evidence/` folder (see Step 3)
- **When** — build or version if known

If the expected behaviour isn't documented anywhere, say so in the draft rather than asserting it. A defect whose "expected" is really an opinion will be closed as works-as-designed, and the team will trust the next one less.

## Step 2 — Draft

```markdown
**Title:** <Area> — <what is wrong, specifically>

**Environment:** <env, URL, build/version>
**Role:** <role the defect reproduces under>

**Steps to Reproduce**
1. ...
2. ...

**Actual Result**
<what happened, with real values>

**Expected Result**
<what should happen — cite the requirement/criterion it comes from>

**Evidence**
<file paths in bug-evidence/<folder>/, one line each with a caption>

**Priority:** <see references/priority-and-labels.md>
**Labels:** <see references/priority-and-labels.md>
**Linked test case:** <TC id, if it came from a run>
```

### Writing the title

The title is what people scan in a list of two hundred. It should identify the defect without the body.

| Weak | Strong |
|---|---|
| "Pricing bug" | "Product page — price does not refresh when quantity changes" |
| "Login broken" | "Login — valid credentials rejected for role X after password reset" |
| "UI issue" | "Checkout — address form overlaps footer below 768px" |

### Reproduction steps

Write them so someone who has never seen the issue can hit it. Include the starting state, exact identifiers (record ids, SKUs, usernames — never passwords), and the point where behaviour diverges. If reproduction is intermittent, **say so and say how often** — "3 of 5 attempts" is far more useful than silence, which reads as "always".

## Step 3 — Post the draft

Save the evidence and the draft together first:

```
bug-evidence/DRAFT_YYYY-MM-DD_<short-slug>/
├── evidence.md          # the draft, plus a captioned list of every file here
├── 01_<what-it-shows>.png
├── 02_<what-it-shows>.png
├── recording.mp4        # if there is one
├── console.txt
└── backend.txt
```

If the failure came from `qa-test-execution`, a `DRAFT_` folder named after the test case may already exist — reuse it rather than starting a second one. Follow `bug-evidence/README.md`: no credentials, no session-token URLs, no HAR files, and crop out customer data the defect doesn't need.

Then post the draft in chat and stop. Invite corrections — the user usually knows context you don't, like whether this is a known issue or belongs to another team.

## Step 4 — File it (only after confirmation)

On explicit confirmation, create it in the tracker with the drafted content unchanged, then report back the id and link.

Then rename the evidence folder from `DRAFT_YYYY-MM-DD_<slug>` to `<TRACKER-ID>_<slug>` (e.g. `PROJ-633_rfq-price-not-refreshed`) and add the ticket id and link at the top of its `evidence.md`. That folder is now the permanent record for the defect.

**What you cannot do:** attachments. Screenshots and recordings must be attached by the user through the tracker UI. When you file, **give the exact folder path** to attach from — a defect whose evidence never got attached is a defect that gets bounced back.

## Step 5 — Before it is closed

A defect isn't done when the code changes. Confirm, before closing:

- Evidence of the fix is attached to the ticket and saved in its `bug-evidence/` folder (e.g. `fix-verified_YYYY-MM-DD.png`)
- The build or release containing the fix is recorded
- It has been re-verified in the environment where it was found

This checklist is the difference between a defect that stays closed and one that reappears next cycle.
