# Reports

Execution and permission-test reports land here.

`.gitignore` excludes `reports/*.md` by default, keeping only this file and the sample. Reports are run artefacts — they go stale immediately and they accumulate fast. If your team does want them in version control (useful for an audit trail across releases), remove that ignore rule deliberately rather than by accident.

## Rules

- **Plain markdown only.** Safe to read, safe to diff, safe to paste into a tracker.
- **Never put credentials in a report** — not a username paired with a password, not a session URL carrying a token. Reports get shared and attached to tickets.
- **Screenshots stay out of the repo.** Reference them by caption; attach the images to the ticket instead. Binary files in git history are permanent and large.
- **Name reports so they sort usefully**, e.g. `2026-09-09_TC_PDP_002_sandbox.md`.

See `sample_execution_report.md` for the shape, and `.claude/skills/qa-test-execution/references/report-format.md` for the field-by-field definition.
