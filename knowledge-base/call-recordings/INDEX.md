# Index - call-recordings

Zoom meeting transcripts (`.transcript.vtt`, speaker-attributed). Use this folder for **why** a thing is the way it is: decisions, agreed workarounds, open items, and who owns them.

**Decisions made in calls often supersede the written documents.** If a transcript and the TDD/solution document disagree, flag the conflict - do not silently pick one.

**Read this index before opening anything in this folder.** A transcript is 1-3 hours of speech; opening one costs a lot of context. Pick the call by date and topic below, then grep it for the term you need rather than reading it end to end:

```bash
grep -n -i -C3 "landed cost" knowledge-base/call-recordings/GMT20251110-*.vtt
```

## Calls

36 calls, 2025-08-25 to 2025-12-30. Times are UTC, as recorded in the filename.

| Date | Start | Length | Main voices | Dominant topics (mention counts) | File |
|---|---|---|---|---|---|
| 2025-08-25 | 14:25 | 02:22:11 | Vince; Mark Bougie; Hafiz Hunain Akbani; Grace Chen; Pascal Auger; Folio3 Netsuite1 Zoom | vendor (273), subsidiary (48), customer (34), invoice (28), purchase order (27), inventory (18), report (16), commission (13) | `GMT20250825-142554_Recording.transcript.vtt` |
| 2025-08-27 | 14:28 | 02:09:33 | Grace Chen; Vince; Mark Bougie; Folio3; James; Pascal Auger | vendor (67), freight (26), payment (24), report (22), purchase order (17), invoice (11), inventory (11), warehouse (8) | `GMT20250827-142810_Recording.transcript.vtt` |
| 2025-09-03 | 14:30 | 02:10:18 | Natacha Piccirilli; Vince; Sadeqain Ali; Mark Bougie; JP Teillet; Pascal Auger | customer (130), quote (79), inventory (47), sales order (35), opportunity (29), production (12), report (11), purchase order (11) | `GMT20250903-143010_Recording.transcript.vtt` |
| 2025-09-04 | 14:29 | 02:02:29 | Natacha Piccirilli; Vince; Abdullah Abid; Pascal Auger; Caroline Cyr | customer (122), edi (41), invoice (36), sales order (23), vendor (18), production (17), quote (15), discount (14) | `GMT20250904-142914_Recording.transcript.vtt` |
| 2025-09-08 | 14:25 | 02:03:19 | Vince; Abdullah Abid; Mark Bougie; Caroline Cyr; Natacha Piccirilli; Louis-Philippe | customer (60), invoice (44), sales order (36), intercompany (29), subsidiary (23), payment (20), inventory (19), warehouse (8) | `GMT20250908-142533_Recording.transcript.vtt` |
| 2025-09-10 | 14:27 | 01:31:39 | Vince; Natacha Piccirilli; Sylvie Levesque; Sadeqain Ali; Pascal Auger; Shuja Zaka Khan | commission (120), report (31), invoice (20), customer (17), price level (13), quote (12), pricing (11), sales order (10) | `GMT20250910-142741_Recording.transcript.vtt` |
| 2025-09-11 | 14:30 | 01:20:28 | Vince; Sylvie Levesque; Abdullah Abid; Pascal Auger; Natacha Piccirilli; Louis-Philippe | rebate (126), customer (86), invoice (26), report (18), vendor (16), payment (9), commission (6) | `GMT20250911-143036_Recording.transcript.vtt` |
| 2025-09-15 | 14:28 | 02:05:38 | Vince; Hunain; Caroline Cyr; Pascal Auger; Johnny Liu | customer (134), invoice (84), payment (36), edi (33), inventory (26), custom record (25), assembly (23), statement (14) | `GMT20250915-142851_Recording.transcript.vtt` |
| 2025-09-16 | 14:30 | 01:57:49 | Hunain; Vince; Myriam Frass | assembly (102), routing (74), subsidiary (27), work order (20), inventory (12), employee (11), production (10), lot (8) | `GMT20250916-143015_Recording.transcript.vtt` |
| 2025-09-18 | 14:28 | 01:49:14 | Hunain; Vince; Natacha Piccirilli; Amine Raid; Stephane boni; Pascal Auger | customer (113), vendor (40), report (23), invoice (20), lot (11), custom field (8), credit memo (6) | `GMT20250918-142850_Recording.transcript.vtt` |
| 2025-09-22 | 14:30 | 01:11:48 | Vince; Hunain; Pascal Auger; Sadeqain Ali; Caroline Cyr; Johnny Liu | customer (90), subsidiary (42), payment (23), employee (18), role (16), import (11), custom field (11), testing (9) | `GMT20250922-143013_Recording.transcript.vtt` |
| 2025-09-24 | 14:23 | 01:52:53 | Haris Karar; Caroline Cyr; Vince; Pascal Auger; Abdullah Abid | assembly (105), inventory (96), work order (67), sales order (46), customer (29), production (28), edi (25), purchase order (19) | `GMT20250924-142316_Recording.transcript.vtt` |
| 2025-09-29 | 14:27 | 01:53:38 | Haris Karar; Vince; Caroline Cyr; Myriam Frass; Mark Bougie; Pascal Auger | routing (47), work order (45), 3pl (45), warehouse (24), inventory (14), assembly (7), production (6), bin (6) | `GMT20250929-142755_Recording.transcript.vtt` |
| 2025-10-01 | 14:25 | 01:51:05 | Sadeqain Ali; Vince; Caroline Cyr; Pascal Auger; Kazim | work order (81), assembly (53), inventory (32), customer (28), routing (25), purchase order (24), custom field (19), currency (9) | `GMT20251001-142515_Recording.transcript.vtt` |
| 2025-10-06 | 14:24 | 01:36:39 | Sadeqain Ali; Vince; Mark Bougie; Myriam Frass; Caroline Cyr | work order (61), assembly (48), 3pl (47), inventory (36), purchase order (27), sales order (26), bin (25), customer (16) | `GMT20251006-142442_Recording.transcript.vtt` |
| 2025-10-08 | 14:26 | 00:19:30 | Folio3; Pascal Auger; Kazim Hussain | _no domain terms — see note_ | `GMT20251008-142625_Recording.transcript.vtt` |
| 2025-10-14 | 14:25 | 01:21:52 | Vince; Sadeqain Ali; Abdullah Abid; Pascal Auger | subsidiary (105), customer (90), sales order (20), inventory (15), contact (12), pricing (11), payment (11), custom record (10) | `GMT20251014-142535_Recording.transcript.vtt` |
| 2025-10-15 | 14:28 | 01:48:13 | Vince; Abdullah Abid; Pascal Auger | assembly (59), customer (50), subsidiary (47), inventory (42), purchase order (14), work order (11), sales order (11), project (9) | `GMT20251015-142852_Recording.transcript.vtt` |
| 2025-10-27 | 14:30 | 00:58:34 | Vince; Haris Karar; Uzair Ishaq; Natacha Piccirilli; Pascal Auger; Kazim | customer (76), subsidiary (37), sales order (18), contact (13), edi (12), invoice (10), employee (8), commission (8) | `GMT20251027-143000_Recording.transcript.vtt` |
| 2025-10-29 | 14:25 | 02:02:38 | Haris Karar; Vince; Myriam Frass; Caroline Cyr; Natacha Piccirilli; Louis-Philippe | work order (104), production (40), inventory (32), assembly (29), report (27), purchase order (27), routing (22), warehouse (17) | `GMT20251029-142559_Recording.transcript.vtt` |
| 2025-11-10 | 13:25 | 02:24:36 | Sadeqain Ali; Vince; Mark Bougie; Grace Chen; Caroline Cyr; Natacha Piccirilli | purchase order (113), vendor (105), bin (55), inventory (45), landed cost (32), work order (28), sales order (25), item receipt (20) | `GMT20251110-132558_Recording.transcript.vtt` |
| 2025-11-12 | 13:29 | 03:10:13 | Vince; Sadeqain Ali; Haris Karar; Mark Bougie; Myriam Frass; Natacha Piccirilli | lot (58), purchase order (46), customer (46), vendor (44), work order (38), sales order (38), inventory (28), bin (28) | `GMT20251112-132939_Recording.transcript.vtt` |
| 2025-11-14 | 13:26 | 03:28:08 | Sadeqain Ali; Vince; Caroline Cyr; Mark Bougie; Myriam Frass; Pascal Auger | work order (301), production (113), sales order (97), purchase order (39), customer (39), routing (37), assembly (31), report (13) | `GMT20251114-132607_Recording.transcript.vtt` |
| 2025-11-17 | 13:29 | 03:15:18 | Sadeqain Ali; Vince; Mark Bougie; Caroline Cyr; Louis-Philippe; Pascal Auger | inventory (100), bin (62), work order (53), warehouse (52), vendor (40), sales order (32), intercompany (32), purchase order (26) | `GMT20251117-132957_Recording.transcript.vtt` |
| 2025-11-19 | 13:29 | 03:23:24 | Vince; Sadeqain Ali; Natacha Piccirilli; Mark Bougie; Pascal Auger; JP Teillet | customer (169), sales order (129), vendor (95), credit memo (54), shipping (39), approval (30), purchase order (24), work order (23) | `GMT20251119-132935_Recording.transcript.vtt` |
| 2025-11-20 | 13:25 | 03:36:23 | Vince; Folio3; Natacha Piccirilli; Pascal Auger; Mark Bougie; Caroline Cyr | customer (233), sales order (94), inventory (61), work order (48), shipping (48), quote (33), pricing (21), production (15) | `GMT20251120-132530_Recording.transcript.vtt` |
| 2025-11-24 | 13:27 | 03:21:39 | Vince; Sadeqain Ali; Natacha Piccirilli; JP Teillet; Pascal Auger; Kazim | quote (243), pricing (198), lot (155), customer (107), sales order (96), opportunity (89), invoice (39), forecast (25) | `GMT20251124-132712_Recording.transcript.vtt` |
| 2025-11-26 | 13:25 | 03:34:55 | Vince; Haris Karar; Natacha Piccirilli; Pascal Auger; Karlyna S (Pricing Dept); JP Teillet | customer (146), commission (132), pricing (104), invoice (102), report (68), price level (33), payment (29), sales order (25) | `GMT20251126-132539_Recording.transcript.vtt` |
| 2025-11-27 | 13:30 | 03:36:37 | Vince; Haris Karar; Natacha Piccirilli; Pascal Auger; Karlyna S (Pricing Dept); Kazim | customer (216), invoice (116), approval (38), report (32), credit memo (23), sales order (21), shipping (19), pricing (19) | `GMT20251127-133022_Recording.transcript.vtt` |
| 2025-12-01 | 13:28 | 03:13:08 | Vince; Zoom NetSuite 5; Natacha Piccirilli; Pascal Auger; Kazim; JP Teillet | commission (273), invoice (131), sales order (96), report (91), quote (60), credit memo (53), customer (41), payment (34) | `GMT20251201-132820_Recording.transcript.vtt` |
| 2025-12-03 | 13:25 | 03:13:13 | Vince; Abdullah Abid; Pascal Auger; Zoom NetSuite 5; Natacha Piccirilli; Louis-Philippe | customer (173), sales order (86), shipping (61), edi (50), invoice (35), report (29), pricing (20), custom record (16) | `GMT20251203-132529_Recording.transcript.vtt` |
| 2025-12-04 | 13:55 | 02:21:42 | Vince; Haris Karar; Pascal Auger; Valerie; Caroline Cyr; Kazim | customer (170), invoice (83), sales order (77), work order (50), employee (38), shipping (24), contact (21), subsidiary (17) | `GMT20251204-135534_Recording.transcript.vtt` |
| 2025-12-08 | 13:29 | 01:11:25 | Vince; Marjorie Dionne; Pascal Auger; Haris Karar; Caroline Cyr | invoice (34), customer (32), report (30), quote (23), pricing (20), sales order (17), shipping (7) | `GMT20251208-132954_Recording.transcript.vtt` |
| 2025-12-10 | 13:27 | 02:06:07 | Vince; Haris Karar; Pascal Auger; Caroline Cyr; Natacha Piccirilli; Louis-Philippe | customer (90), inventory (81), warehouse (39), production (34), payment (24), pricing (20), edi (20), assembly (18) | `GMT20251210-132744_Recording.transcript.vtt` |
| 2025-12-29 | 14:29 | 01:37:33 | Vince; Sadeqain Ali | assembly (46), routing (34), inventory (21), customer (14), payment (13), subsidiary (11), production (11), work order (10) | `GMT20251229-142917_Recording.transcript.vtt` |
| 2025-12-30 | 14:28 | 00:47:13 | Vince; Shuja Zaka Khan | pricing (82), customer (67), currency (44), subsidiary (13), shipping (7) | `GMT20251230-142836_Recording.transcript.vtt` |

## How to read the topic column

> **Auto-generated - needs review.** The topic column is a **term-frequency profile**, produced by counting domain vocabulary in each transcript. Nobody has read these calls. A high count means the call spent time on that area; it does **not** tell you what was decided. Treat the column as a routing aid only, and never cite it as a decision.

As you work through a call, replace its row's topic cell with a real one-line summary and add any decisions to the section below. The index earns its keep as that happens.

## Decisions and open items

_Empty - nothing recorded yet._ Add an entry when you confirm a decision in a transcript:

| Date | Decision / open item | Who | Where in the call | Affects |
|---|---|---|---|---|

## Known gaps

- **No call has been read.** The agent cannot answer "what was decided about X" from this index - it can only tell you which call to open.
- `GMT20251008-142625` is 19 minutes with no domain vocabulary: the meeting was postponed because attendees did not join. Nothing to extract.
- Speaker names come from Zoom display names and are not reliable identity: `Folio3`, `Folio3 Netsuite1 Zoom` and `Zoom NetSuite 5` are shared meeting-room accounts covering more than one person.
- Only the `.transcript.vtt` format is synced. The Drive folder also holds `.cc.vtt` closed-caption copies of the same calls; those have no speaker names and coarser timestamps, so the sync excludes them (`exclude_name_patterns` in `sync-config.json`).
