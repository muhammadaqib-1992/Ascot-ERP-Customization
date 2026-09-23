---
name: acg-uat-script-writer
description: Write individual UAT (User Acceptance Testing) test cases/scripts for the Ascot Capital Group (ACG) NetSuite implementation, sourced strictly from the project's Solution Document (never the BRD, Decision Logs, or general NetSuite knowledge), one case at a time, in the exact format the ACG team has approved through iterative review. Use this skill whenever the user asks to "create a UAT case/script", "write a test case", asks for cases for a specific BRD requirement number (e.g. "9.3.1", "16.4.1"), asks to cover a flow (Quote, Contract, Inquiry, TBA Order, Customer Pricing, etc.), or gives a raw requirement/solution excerpt and asks for a case to be built from it. Also use this skill when refining an existing case based on user feedback (wrong navigation, wrong expected result, wrong data, wrong numbering) - the skill's iterative-correction pattern applies there too, not just first drafts.
---

# ACG UAT Script Writer

Writes single NetSuite UAT test cases for the ACG project, refined one round of feedback at a time until the user says it's right. This is not a bulk-file-generation skill — cases are shown inline in chat as plain text/markdown so the user can copy-paste directly into their Google Sheet, unless the user explicitly asks for a file.

## Core principle

**One case, one round of iteration at a time.** Show a draft. The user corrects something (a date, a navigation path, a field value, an expected result, the case number). Update just what they flagged and re-show the whole case. Do not move to the next case until the user is satisfied with the current one. Do not batch-produce many cases speculatively — this project's cases get corrected against live NetSuite behavior, and unreviewed batches waste effort.

## Before writing anything: the Solution Document is the only source

**UAT cases in this project are built only from the Solution Document — not the BRD, not Decision Logs, not general NetSuite knowledge, not assumption.** This is a hard rule, not a preference.

1. Search the Solution Document specifically for the requirement number or topic (this is the detailed Google Doc that contains both "BRD Requirements:" and "Solution" text per requirement — the same document used throughout this project, not the shorter/older PDF-style solution summary if both exist. If it's ambiguous which document counts as "the Solution Document," ask the user once, then keep using that same one for the rest of the session).
2. Pull the actual "BRD Requirements" text and "Solution" text from that document verbatim (or close to it) — don't paraphrase from memory, and don't fill gaps from the BRD or Decision Logs even if they'd answer the question. If the Solution Document doesn't cover some part of what's needed for the case, say so plainly as an open item rather than sourcing it elsewhere.
3. The only two exceptions where non-Solution-Document input is used:
   - **The user pastes a requirement/solution excerpt directly in chat** — treat that pasted text as if it came from the Solution Document (it typically is a copy from it), and use it as-is.
   - **A live NetSuite screenshot the user provides** — this is ground truth for what the system actually does, and overrides anything the Solution Document says when the two disagree. Flag the mismatch, don't just quietly override.
4. If two parts of the Solution Document disagree with each other (this project's version has known internal conflicts — e.g. a "no expiry date" statement contradicted elsewhere by a "Validity date; consumed all-or-none" table, or an old "Current" design contradicted by an explicitly-labeled "Updated" design), **do not silently pick one**. This entire document is client-facing — Step Instructions, Notes / Prerequisites, and Expected Results must never carry a `DOC CONFLICT` flag, an "open item," a "confirm with Administrator," or any other internal caveat. Instead, add a separate **Comments** field to the case (see format below) and put the flag there only: say which two statements disagree and where, then proceed using whichever is more authoritative (more detailed, more recent, or explicitly labeled "Updated") while asking the user to confirm.
5. If a browser/MCP tool is available and connected, it's fine to check live NetSuite to confirm exact field labels, subtab names, or navigation paths — but the underlying *behavior/requirement* being tested still has to trace back to the Solution Document, not be invented because it seemed reasonable.
6. If asked to build a case for something not in the Solution Document at all (no matching requirement number, no matching topic), say so directly and ask the user to point to the right requirement or paste the relevant text — don't guess at what the feature probably does.

## The exact case format

Every case has these fields, shown in this order, as separate labeled blocks (not a single paragraph). **This is a client-facing document.** Step Instructions, Notes / Prerequisites, and Expected Results must contain only clean, confident, client-appropriate content — no open items, no "confirm with Administrator," no `DOC CONFLICT` flags, no internal hedging of any kind. All of that goes in the separate **Comments** field instead, which is understood to be internal-only.

```
No.: <case number>

Step Name:
<short, plain-English description of the scenario>

Step Instructions:
<Administrator Role: numbered steps>

Notes / Prerequisites:
<setup needed, data substitution guidance - client-appropriate only>

Expected Results:
<numbered, business-readable outcomes - client-appropriate only>

Comments:
<internal-only: open items, doc conflicts, unconfirmed navigation/field names, anything needing team follow-up>
```

If a case has nothing internal to flag, still show the Comments label with "None" rather than omitting it — that way its absence is a deliberate confirmation, not an accident.

### Case numbering

- A new, independent scenario gets the next whole number: `1.0`, `1.1`, `2.1`, `3.1`...
- The *same* scenario tested via a *different navigation path* gets a `B` suffix on the same number: `1.1 B` is "the same outcome as 1.1, reached a different way" — not a new scenario.
- A scenario that *depends on* an earlier case's data (e.g. testing expiry using the record created in 1.1) still gets its own whole number, but its steps reference the earlier case rather than repeating it (see below).
- Renumber immediately and exactly when the user gives a new number — don't argue for a "better" scheme.

### Step Instructions rules

- Always start with `Administrator Role:` unless the user has specified a different/second role for this case.
- **Every navigation must be the real, exact click path.** Two acceptable forms:
  - A standard NetSuite path: `Lists > Relationships > Customers`, `Transactions > Sales > Enter Sales Orders > New`
  - A custom/Folio3 path confirmed from a screenshot or the doc: `More (...) menu > Folio3 Customizations > Customer Pricing > New Customer Pricing`
  - If the exact path isn't confirmed, say so explicitly in the step ("ask your Administrator to confirm the exact location") rather than inventing a plausible-looking one.
- Item entry on ACG transactions goes through **ISM** (Item Selection Modal), not the native item sublist, on Quotes, Contracts, Inquiries, Sales Orders, TBA Orders, BOM Revisions. State this explicitly and note the ISM button's location ("On the Items subtab, click the 'ISM' button").
- Number every step. Never use comma-separated instructions or run steps together in a paragraph.
- **Merge steps that are really one action.** Don't split "enter field values" and "click Save" into two steps if they happen as one motion — but don't merge genuinely separate actions either (e.g. "open the record" and "click Edit" can often be one step; "save the first record" and "create the second record" cannot).
- If a case builds on a prior case's record, reference it by case number instead of repeating its steps: *"Run Test Case 1.1 (...). Do not repeat the steps here — use the same record created in 1.1 for this test."* Only the delta steps for the new case go in full.
- Put real data inline in the steps themselves (customer names, SKUs, dates, price levels), not as separate placeholders the tester has to cross-reference. If the user hasn't given real data yet, ask for it — don't invent a customer/item/date and present it as final; state clearly what's still needed (e.g. `[CONFIRM - see Comments]`) so it's obvious this isn't done yet, and log the specific thing needed in the Comments field, not in the step itself beyond that short marker.

### Notes / Prerequisites rules

- State what records need to already exist, and what to substitute if they don't — written as clean, confident setup guidance, not as a hedge.
- If a detail is explicitly not the focus of this test (e.g. a background script's internal status field), say so, so the tester doesn't waste time chasing it: *"The Status field on the Trickle Down record is informational only and is not the focus of this test."*
- When a case depends on a prior case, state that dependency here too, not just in the steps.
- **Open items and doc conflicts do not belong here.** If something is unconfirmed, put the client-safe version here (or omit the detail entirely if there isn't a safe way to state it yet) and put the actual flag/explanation in Comments.

### Expected Results rules

- Numbered, one outcome per line.
- **Business-readable, not technical.** Say what the system does in plain terms a non-technical tester would recognize on screen — not script/field-ID language.
- **Never tell the tester when to mark Pass or Fail.** State only what should happen; the tester compares actual vs. expected themselves. (Earlier drafts in this project included "if X happens, mark Fail" — this was explicitly rejected and must not recur.)
- When comparing a before/after state (e.g. expiry management superseding an old pricing record), lay it out as labeled blocks, not prose:
  ```
  Old record:
  - Price Level = A
  - Valid From = ...
  - Valid To = ...

  New record:
  - Price Level = B
  - Valid From = ...
  - Valid To = ...

  1. ...
  2. ...
  ```
- After the record saves, describe **exactly what screen the user lands on** — a view-mode record, a list page, a redirect back to a parent record — based on confirmed behavior, not assumption. This has been wrong more than once in this project (assumed "reopen the record" when the real behavior was "redirected to the list" or "redirected to the parent Customer record") — always ask or verify rather than defaulting to the most generic assumption. If it isn't confirmed yet, don't guess in Expected Results — note the uncertainty in Comments instead and leave Expected Results stating only what is confirmed.
- **No caveats, no hedging, no "confirm with..." language ever appears in Expected Results.** It reads as a finished, confident statement of correct behavior. Anything not yet certain goes in Comments, not here.

### Comments rules (internal-only field)

- This is the one field allowed to be messy, uncertain, or address the internal team rather than the client/tester.
- Use it for: `DOC CONFLICT` flags (name the two conflicting statements and where each appears), open items needing confirmation (exact navigation paths, exact field/form names, exact business role, data values not yet provided), and anything else that would undermine a client-facing document if left in the other fields.
- Keep it factual and specific — say exactly what needs confirming and why, not just "TBD."

### Positive flows by default

Unless the user asks for negative/edge-case coverage, write only the happy path: valid data, successful save, correct propagation/behavior. Don't add validation-failure or error-handling cases unless requested.

## Accessibility requirement: assume zero NetSuite knowledge

Every step must be followable by someone who has never used NetSuite:
- "Log in to NetSuite using an Administrator login" rather than assuming they're already in.
- "In the top search bar, type the name of the item and open its record" rather than "open the item record."
- "Click the 'Edit' button near the top of the page" rather than "edit the item."
- Explain what a field means in plain language the first time it's used in a case, if it's not self-evident from its label.
- Where the exact record/field/button isn't nameable with confidence, write "ask your Administrator to confirm..." rather than presenting a guess as certain — this keeps the case usable by a first-time tester without misleading them.

## Formatting

- Numbered lists for sequential steps and expected results, always.
- Dash bullets (`-`) for unordered groupings within a step (e.g. a list of field values to enter, a list of records in use).
- No comma-separated run-on instructions — this was explicit, repeated feedback.
- Deliver cases as plain text in the chat reply (copyable into a spreadsheet cell), not as a file, unless the user asks for a file. Chat-to-cell paste does not preserve formatting reliably — if the user reports formatting breaking on paste, remind them the fix is copying cell-to-cell from an actual spreadsheet file, and offer to build one, but default back to plain text once that's resolved unless they ask to keep using files.

## When the user gives you a raw requirement excerpt

If the user pastes BRD/Solution text directly (rather than asking you to look it up), treat that pasted text as the authoritative source for that case — don't go search for a conflicting version elsewhere unless something in it seems to require cross-checking (e.g. it references another requirement number by number).

If they also share a flow-diagram link (e.g. a claude.ai artifact link) as supporting reference, try to fetch it, but know that rendered diagram/app links often only return page metadata, not usable content, via a plain fetch. If that happens, say so plainly and proceed from the text source alone, inviting the user to paste the diagram's content directly if it has details the text doesn't.

## Session-start behavior

If project-specific values have already been established earlier in the conversation (a customer ID used across several cases, a standard date range, a standard role name), keep reusing them for consistency unless the user changes them — don't ask again for values already given once, and don't drift to different placeholder data between cases in the same set.
