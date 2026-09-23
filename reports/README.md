# Reports

Execution and permission-test reports, one date-stamped record per test case per run. Tracked in git — this is the team's record of **what actually happened** on each run.

`qa-test-execution` and `qa-permission-testing` save here automatically at the end of a run.

## Naming

`qa-test-execution` saves a **folder per run** (it also records the test data used):

```
reports/YYYY-MM-DD_<TC-id>_<env>/
├── report.md       # the execution report
└── test-data.md    # the backend records this run used, and where each came from
```

`qa-permission-testing` saves a single dated **file** per run (no separate backend data to carry, since it's checking access, not data values):

```
reports/YYYY-MM-DD_<TC-id-or-PERM-check>_<env>.md
```

| Part | Meaning | Example |
|---|---|---|
| `YYYY-MM-DD` | Date of the run | `2026-09-12` |
| `<TC-id>` | The test case executed | `TC_PDP_002` |
| `<env>` | Environment it ran against | `sandbox` |

→ `reports/2026-09-12_TC_PDP_002_sandbox/` (test execution) or `reports/2026-09-12_PERM_L2-invoices_sandbox.md` (permission test).

## One run, one record

A re-run gets a **new dated folder or file** — never overwrite an earlier report. A test that failed on the 10th and passed on the 12th is a history worth keeping: it shows when a fix landed and proves it was re-verified.

## Rules

- **Plain markdown only.** Safe to read, diff, and paste into a tracker.
- **Never put credentials in a report** — not a username paired with a password, not a session URL carrying a token.
- **Screenshots and logs go in `bug-evidence/`, not here.** Reference them from the report's Evidence section by path, e.g. `bug-evidence/DRAFT_2026-09-12_TC_PDP_002/01_total-65.png`.
- **State the environment.** A pass against the wrong environment is a false pass.

See `sample_execution_report.md` for the shape, and `.claude/skills/qa-test-execution/references/report-format.md` for the field-by-field definition.

## Related folders

| Folder | Holds |
|---|---|
| `test-cases/` | What *should* happen — approved test cases |
| `reports/` | What *did* happen — execution results |
| `bug-evidence/` | Proof of what went wrong — per-defect evidence |
