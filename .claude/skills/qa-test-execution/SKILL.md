---
name: qa-test-execution
description: "Executes QA test cases end-to-end. Sources the case from test-cases/, chat, qa-test-writing, a ticket, or raw steps the user gives directly (write them down first, then execute). Always drives the browser via Playwright MCP; runs qa-test-data-prep (backend/NetSuite MCP) alongside it for test data, falling back to asking the user or a Playwright UI lookup if that MCP isn't connected. Produces a pass/fail report plus a test-data record in a dated reports/ folder (failure evidence to bug-evidence/). Use for 'execute TC_', 'run this test case', 'test this on staging', 'go through <ticket id>', 'verify this works'. Not for ad-hoc browsing, writing cases (qa-test-writing), or permission coverage (qa-permission-testing). Never auto-files a defect — on failure it offers qa-bug-reporting and waits."
---

# QA Test Execution

Runs a test case the way a QA engineer would: confirm what "pass" means, drive the real application, verify against the system of record, and report actual versus expected. This skill executes and reports — it does not file defects.

**Only load `references/report-format.md` when you are about to write the report.**

## Ground rules

1. **Never store or write down credentials** — not in this file, not in scripts, not in the report, not in chat beyond the turn the user gives them. Read them from `.claude/qa-test-env.md`; if a value is a `<PLACEHOLDER>`, ask for that run only.
2. **Always drive the browser through the Playwright MCP.** It's the browser-automation connector for this project (`claude mcp add playwright -- npx -y @playwright/mcp@latest` per `README.md`). Don't fall back to computer-use or another browser tool for a test execution run unless the user explicitly asks for a different one.
3. **The UI is not the source of truth.** Most test cases compare what the application *shows* against what the backend actually *holds*. Check both. "It looked right" is not a pass for a data-accuracy case.
4. **Never auto-file a defect.** A failure gets reported clearly, with an offer to hand off to `qa-bug-reporting`. Filing happens only if the user says so after reading the report.
5. **Confirm your tooling is live before starting.** If the Playwright MCP isn't reachable, stop and say so rather than failing silently halfway through a run.
6. **Report what happened, not what should have happened.** If you skipped a step, say so. If you substituted test data, say so. A report that hides its own gaps is worse than no report, because someone will act on it.

## Step 1 — Establish the test case

The test case arrives one of two ways:

- **A written test case** — from `test-cases/` (the user names a file or a TC id you look up there), pasted in chat, from `qa-test-writing`, or a tracker ticket. Normalise into: id, pre-condition, numbered steps, expected result per step.
- **A raw instruction set** — the user describes what to test in plain language instead of pointing at a written case. **Write the steps down first**, in the same shape (id, pre-condition, numbered steps, expected result per step), post them in chat, and get a quick confirmation before executing. Treat this written-down version as the test case for the rest of the run — it's what the report and test-data record are checked against.

If the expected result is vague ("works correctly"), resolve that **before** running anything — an unfalsifiable case wastes the whole run.

## Step 2 — Gather test data and satisfy the pre-condition

Before touching the browser, verify the pre-condition is actually true, and gather whatever backend records the run needs (a user with a given role, an item in a given status, an unrelated account's data for an exclusion check).

**Coordinate two connections for this:**
- **Backend/NetSuite MCP**, via the `qa-test-data-prep` agent — dispatch it (in the background, so its query output doesn't crowd the main thread) to find and verify the records this run needs. It's read-only and never touches the browser, so it runs alongside Playwright without conflict.
- **Playwright MCP**, in the main thread — once the data comes back, this is what actually drives the application.

**If the backend/NetSuite MCP isn't connected** (the agent reports it unreachable), don't stall the run — do one of:
1. **Ask the user directly** for the specific record/value the step needs, or
2. **Extract it via Playwright** instead — a UI lookup (open the record, read the field) stands in for the backend query. Say plainly in the report that this came from a UI read, not a direct backend check, since that's weaker evidence for a data-accuracy assertion.

If the pre-condition state is wrong, **ask before changing it.** Setting up test data by mutating records is a legitimate step, but silently altering the system of record invalidates whatever else is running against it.

**Save what you gathered** — see Step 6b. The data a run used is part of its record, the same way the report is.

## Step 3 — Log in as the right role

Confirm which environment and which role the case requires, then authenticate through the Playwright MCP. Capture the landed state before proceeding — it is the first piece of evidence, and it catches "the run was against the wrong environment" before you waste twenty steps.

## Step 4 — Execute

One step at a time:

- Perform the action.
- Capture the actual result — screenshot or page state.
- Where the expected result is a backend comparison, pull the backend value and **state both numbers explicitly** in the report. "Matched" is a conclusion; "UI 55, backend 55" is evidence.
- Compare against expected immediately, not in a batch at the end.
- If a step blocks progress, mark it and everything downstream **Blocked**, capture evidence, and stop.

## Step 5 — Handle a failure

A failure on one step doesn't automatically end the run: if later steps are independent, continue and report both. If they depend on the failed step, stop and mark the rest Blocked.

Capture evidence at the moment of failure — screenshot, console error, exact field values. Reconstructing it afterwards is unreliable and the detail that mattered is usually gone.

Save it straight into a draft evidence folder, so it's ready if a defect is raised:

```
bug-evidence/DRAFT_YYYY-MM-DD_<TC-id>/
├── 01_<what-it-shows>.png
├── console.txt        # console errors, if any
└── backend.txt        # the backend values you compared against
```

With Playwright, pass that path as the screenshot filename rather than saving elsewhere and moving it. Follow `bug-evidence/README.md` — above all, no credentials, no session-token URLs, no HAR files. Passed steps need no image files; the report's Actual column is enough.

## Step 6 — Report, save test data, and hand off

Each run gets one dated folder, not a loose file — this is where both the report and the test data it used live together:

```
reports/YYYY-MM-DD_<TC-id>_<env>/
├── report.md       # the execution report
└── test-data.md    # the records this run used, and where each came from
```

e.g. `reports/2026-09-12_TC_PDP_002_sandbox/`. One folder per test case per run: a re-run gets a new dated folder, never an overwrite, because a history of fails-then-passes is itself evidence.

### 6a — `report.md`

Write it per `references/report-format.md`, post it in chat, and save it into the run folder. Reference any failure evidence by its `bug-evidence/` path in the Evidence section, and say where the report was saved.

### 6b — `test-data.md`

Carry over the table `qa-test-data-prep` returned (or what you gathered via the Playwright/user-asked fallback from Step 2), so the next person re-running this case knows exactly what it ran against without re-deriving it:

```markdown
## Test Data — TC_XXX_00X, YYYY-MM-DD

| Need | Record type | Internal ID | Identifier | Source | Notes |
|---|---|---|---|---|---|
| ... | ... | ... | ... | qa-test-data-prep / Playwright UI lookup / user-supplied | ... |
```

If nothing needed backend data for this run, save the file anyway with one line saying so — an empty run with no file looks like a skipped step, not a deliberate "none needed."

Saving to `reports/` is part of the run. Posting the report anywhere else — the tracker, a shared sheet — still needs the user's go-ahead.

If the result is **Failed**, mention that you can draft a defect via `qa-bug-reporting` — then wait. Never chain straight into filing.
