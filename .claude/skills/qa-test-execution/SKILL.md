---
name: qa-test-execution
description: "Executes QA test cases end-to-end against the running application. Sources the test case (pasted in chat, written moments earlier by qa-test-writing, or from a tracker ticket), drives the browser via the browser-automation MCP, cross-checks backend data via the data MCP when a step requires it, and produces a formatted pass/fail execution report. Use whenever the user says 'execute TC_', 'run this test case', 'test this on staging', 'go through <ticket id>', 'verify this works', or asks for validation of application behaviour against a written test case. Do NOT use for ad-hoc browsing with no defined test case, for writing new test cases (qa-test-writing), or for role/permission coverage (qa-permission-testing). Never files a defect automatically — on a failure it offers to hand off to qa-bug-reporting and waits for explicit confirmation."
---

# QA Test Execution

Runs a test case the way a QA engineer would: confirm what "pass" means, drive the real application, verify against the system of record, and report actual versus expected. This skill executes and reports — it does not file defects.

**Only load `references/report-format.md` when you are about to write the report.**

## Ground rules

1. **Never store or write down credentials** — not in this file, not in scripts, not in the report, not in chat beyond the turn the user gives them. Read them from `.claude/qa-test-env.md`; if a value is a `<PLACEHOLDER>`, ask for that run only.
2. **The UI is not the source of truth.** Most test cases compare what the application *shows* against what the backend actually *holds*. Check both. "It looked right" is not a pass for a data-accuracy case.
3. **Never auto-file a defect.** A failure gets reported clearly, with an offer to hand off to `qa-bug-reporting`. Filing happens only if the user says so after reading the report.
4. **Confirm your tooling is live before starting.** If the browser MCP isn't reachable, stop and say so rather than failing silently halfway through a run.
5. **Report what happened, not what should have happened.** If you skipped a step, say so. If you substituted test data, say so. A report that hides its own gaps is worse than no report, because someone will act on it.

## Step 1 — Establish the test case

Source it from chat, from `qa-test-writing`, or from a tracker ticket. Normalise into: id, pre-condition, numbered steps, expected result per step.

If the expected result is vague ("works correctly"), resolve that **before** running anything — an unfalsifiable case wastes the whole run.

## Step 2 — Satisfy the pre-condition

Before touching the browser, verify the pre-condition is actually true. If it references backend state (a record's status, a quantity, a configuration toggle, a role assignment), check it via the data MCP rather than assuming.

If the state is wrong, **ask before changing it.** Setting up test data by mutating records is a legitimate step, but silently altering the system of record invalidates whatever else is running against it.

## Step 3 — Log in as the right role

Confirm which environment and which role the case requires, then authenticate. Capture the landed state before proceeding — it is the first piece of evidence, and it catches "the run was against the wrong environment" before you waste twenty steps.

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

## Step 6 — Report and hand off

Write the report per `references/report-format.md` and post it in chat. Ask before saving it anywhere else.

If the result is **Failed**, mention that you can draft a defect via `qa-bug-reporting` — then wait. Never chain straight into filing.
