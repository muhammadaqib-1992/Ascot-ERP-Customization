# Bug Evidence

One folder per defect, holding everything that proves it: screenshots, recordings, console output, the backend values it was compared against, and the draft itself. Tracked in git — this is the permanent record for each defect.

`qa-test-execution` saves failure evidence here at the moment a step fails. `qa-bug-reporting` saves the draft alongside it, and renames the folder once the defect is filed.

## Folder naming

| Stage | Folder name | Example |
|---|---|---|
| Before filing | `DRAFT_YYYY-MM-DD_<short-slug>` | `DRAFT_2026-09-12_rfq-price-not-refreshed` |
| After filing | `<TRACKER-ID>_<short-slug>` | `PROJ-633_rfq-price-not-refreshed` |

The date is the day the failure was found. When the defect is created in the tracker, the folder is renamed to lead with the ticket id — so you can always go from a ticket to its evidence and back.

## What goes inside

```
PROJ-633_rfq-price-not-refreshed/
├── evidence.md               # the defect draft + a captioned list of every file here
├── 01_edit-item-popup.png    # numbered in the order they tell the story
├── 02_item-record-price.png
├── recording.mp4             # screen recording, if there is one
├── console.txt               # browser console errors
└── backend.txt               # the backend/query values the UI was compared against
```

Number screenshots `01_`, `02_`… with a few words on what each shows. A developer reading the folder cold should be able to follow the failure in order.

## `evidence.md` template

```markdown
# <Defect title>

- **Tracker:** <TRACKER-ID and link, or "not filed yet">
- **Found:** YYYY-MM-DD
- **Environment:** <env + URL>
- **Role:** <role it reproduces under>
- **Linked test case:** <TC id + path in test-cases/, if it came from a run>

## Files
| File | Shows |
|---|---|
| 01_edit-item-popup.png | Edit Item popup showing 88.85 at qty 1880 |
| 02_item-record-price.png | Item record showing 411.30 (CPS) |

## Draft
<the defect draft exactly as posted in chat>

## Fix verification
<added when re-tested: date, build/release, result, fix-verified_YYYY-MM-DD.png>
```

## Rules

These exist because this folder is shared and its contents stay in git history permanently.

- **No credentials, ever.** Not in a screenshot, not in a log, not in a pasted URL. Crop or blur login fields.
- **No session URLs.** Links carrying tokens or session ids in the query string are credentials in disguise — strip the query string before saving.
- **No HAR files.** Network captures carry session cookies and authorisation headers. They are git-ignored and blocked by the commit hook. If network detail matters, copy the relevant request/response into `evidence.md` by hand, with auth headers removed.
- **Crop customer data the defect doesn't need.** If a screenshot shows a real customer's pricing or contact details and the defect doesn't depend on them, crop them out.
- **Mind the size.** GitHub rejects files over 100 MB and warns above 50 MB. Trim recordings to the relevant seconds, or compress them. If large recordings are routine for your team, move this folder to Git LFS.

## Attaching to the tracker

The agent cannot attach files to tickets. When a defect is filed, attach the files from its folder through the tracker UI — the agent will tell you the exact path. A defect whose evidence never got attached is a defect that gets bounced back.
