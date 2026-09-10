---
name: qa-context-lookup
description: "Research and context-gathering for this QA project. Use BEFORE answering any question about the application under test — how a feature is meant to work, why something was decided, what was agreed in a meeting, project history, or the status of a feature or change request. Searches the knowledge base first via knowledge-base/README.md's routing map, THEN the call-recordings INDEX.md for meeting history — never opens raw transcripts or large documents unless an index points at a specific one. This is the default research step behind every other QA skill: run it automatically, don't wait to be asked to check the docs. Triggers on how, why, what, when, was this discussed, is this in scope, what did we agree. Not for running a test or filing a defect."
allowed-tools: Read, Grep, Glob, Bash
---

# QA Context Lookup

Answers project questions from documented sources, in a cost-controlled order, and cites what it used. This skill is read-only by design: it never writes files, drives a browser, or touches the tracker.

## Why the order matters

The knowledge base contains documents that are individually larger than a comfortable context window. Reading a 200-page specification or a 90-minute transcript to answer a one-line question is the single most expensive mistake available here. Every step below exists to avoid it.

## The lookup order

**1. Route the question.** Open `knowledge-base/README.md` and use its routing map to decide *which folder* the answer lives in. Don't guess — the map exists so you don't have to.

**2. Read that folder's `INDEX.md`.** It says which document covers what, plus known gaps. Frequently the index alone answers the question.

**3. Open a source document only when the index points at one** — and read the specific section, not the whole file.

**4. Check meeting history** via `knowledge-base/call-recordings/INDEX.md` for anything involving *why*, *when*, *who decided*, or *was this discussed*. Open a raw transcript only when the index names a specific call and you need exact wording.

**5. Live system check** — only when documentation is insufficient or you need to verify actual behaviour against spec. Say in your answer that this came from the live system, not the docs.

**6. External sources** — only when the user explicitly asks.

## Conflicts are findings, not noise

Decisions made in meetings routinely supersede written specifications, because teams rarely go back and update documents. When a call decision and a document disagree:

**Surface both, say which is more recent, and flag the conflict.** Do not silently pick the one that seems more authoritative. A stale specification that nobody has noticed is exactly the kind of thing QA should be catching.

## Answering

- **Cite the source** — document and section, or call date. An uncited answer can't be checked, and the person reading it has no way to tell recall from evidence.
- **Say when something is not documented.** "The specification doesn't cover this; confirm with `<owner>`" is a genuinely useful answer. A plausible guess presented as fact is not — it will end up in a test case, then in a defect report, then in an argument with a developer.
- **Flag open decisions as open.** If the answer depends on something still unresolved, state the assumption you are working from.
- **Keep the answer proportional.** A one-line question gets a one-line answer plus its citation.

## When the knowledge base is thin

If the routing map has no row for the topic and no index mentions it, say so plainly and suggest where it should live. Don't pad the answer with general knowledge about how such systems usually work — the user asked about *their* system.
