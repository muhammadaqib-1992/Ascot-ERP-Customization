---
name: qa-test-writing
description: "Writes test cases for this QA project in the team's standard format. Use whenever the user asks to 'write test cases', 'create TCs', 'add tests for feature X', 'cover this requirement', 'cover this acceptance criterion', or names a feature and wants it turned into testable steps. Sources acceptance criteria, role availability and configuration options from the knowledge base — never invents an expected result that isn't grounded in a document, and labels anything inferred as inferred. ALWAYS posts drafted test cases in chat for review first; never writes them into the tracker or a spreadsheet without the user confirming. Once approved, saves them to test-cases/ as a date-stamped file so the team keeps a record. Do NOT use for running an existing test case (that is qa-test-execution), for filing a defect (qa-bug-reporting), or for role/permission coverage specifically (qa-permission-testing)."
---

# QA Test Writing

Turns a documented requirement into atomic, executable test cases. Output goes to chat for review first. Once approved, the cases are saved to `test-cases/` as a date-stamped file — the team's record of what was written and when. This skill never writes to a tracker or spreadsheet on its own.

**Only load `references/test-case-format.md` when you are about to produce the table** — it holds the column definitions and worked examples.

## Ground rules

1. **Chat first, always.** Post cases as a table for review. They are a draft until the user says otherwise. Once approved they are saved to `test-cases/` (Step 4); they go to a tracker or spreadsheet only if the user asks.
2. **Ground every expected result in a document.** Pull the acceptance criteria, role availability and configuration options from the knowledge base before writing anything (`qa-context-lookup` handles the retrieval). If a scenario is an obvious edge case the docs don't cover, you may add it — but label it **Inferred** in Comments so a reviewer can challenge it.
3. **One scenario per case.** "Verify layout and responsiveness and role access" is three test cases wearing a trenchcoat. Split them.
4. **An expected result must be checkable.** "Works correctly" cannot fail. "Total shows 55, matching the sum of online locations" can.

## Step 1 — Locate the requirement

Identify the feature and pull its section: the acceptance criteria list, which roles it applies to, and any configuration toggles. If the requirement has upstream dependencies (another module, an unresolved decision), pull those too — they change what "expected" means.

If a needed document is missing or the criteria are ambiguous, **stop and say so**. Test cases built on a guessed expectation are worse than no test cases: they produce confident false failures.

## Step 2 — Derive cases from the criteria

Walk the acceptance criteria one line at a time. For each, ask whether it is one scenario or several. Typical decomposition:

- **Layout / structure** — does the element render with the right parts?
- **Data accuracy** — does what's displayed match the system of record?
- **Configuration behaviour** — toggle on *and* off; both states are a case.
- **Role-based visibility** — one case per applicable role, not one case listing roles.
- **Responsiveness / cross-environment** — where relevant.
- **Negative and edge cases** — empty states, invalid input, permission denied, feature disabled. Usually the highest-value cases and usually absent from the acceptance criteria; mark them Inferred.

## Step 3 — Present

Produce the table in the format from `references/test-case-format.md`, grouped under the requirement heading.

Then flag, in a line or two: anything marked Inferred, any open dependency affecting expected results, and any ambiguity in the source document that ought to be resolved before these are executed. This short note is often more valuable than the cases themselves — it's where the specification's real gaps show up.

## Step 4 — Save the approved cases

When the user approves the cases — "looks good", "approved", "save them" — write them to:

```
test-cases/YYYY-MM-DD_<ShortCode>_<short-slug>.md
```

Use **today's date** (the day they were approved), the feature's short code, and a few words describing the batch — e.g. `test-cases/2026-09-12_PDP_inventory-block.md`. The date prefix is what makes the folder sort into a timeline, so never omit it.

Start the file with this header, then the table exactly as approved:

```markdown
# <Requirement heading>

- **Created:** YYYY-MM-DD
- **Author:** <who wrote/approved them>
- **Source:** <document + section, or ticket id>
- **Status:** Approved
- **Cases:** TC_<Code>_001 – TC_<Code>_00N
```

Put the Inferred / open-dependency notes from Step 3 under a `## Notes` heading at the end.

**Revising an existing batch:** don't silently overwrite. For a small correction, edit in place and add `- **Updated:** YYYY-MM-DD — <what changed>` under the header. A new test cycle for the same feature gets a new dated file, and the old one's status becomes `Superseded by <new file>` — otherwise someone executes the stale version.

If the user wants a draft kept before approval, save it the same way with `Status: Draft`. Say where the file was saved in your reply. See `test-cases/README.md` for the full convention.

## Step 5 — Handoff

The cases are now ready to be pasted into the team's tracker by the user, executed via `qa-test-execution`, or revised. **Wait for the user.** Do not proceed to execution or file anything automatically.
