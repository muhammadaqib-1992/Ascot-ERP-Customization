# QA Agentic Workspace

A reusable Claude Code workspace for software QA. Clone it, point it at your project's documents, fill in a few placeholders, and your team shares one agent that researches, writes test cases, executes them, tests permissions, and drafts defects — all in your formats.

Nothing here is tied to a particular product, tracker, or industry. It is a **starting skeleton**, not a finished configuration.

**Read [`ARCHITECTURE.md`](ARCHITECTURE.md) once before extending it.** It explains why each piece lives where it does — mostly so you don't put knowledge in the wrong primitive and wonder why it never loads.

---

## What you get

| | |
|---|---|
| **5 skills** | Research, test-case writing, test execution, permission testing, defect reporting |
| **Knowledge base** | Indexed folders for solution docs, technical design, requirements, contracts, call recordings, reference data |
| **2 working hooks** | Blocks committing credentials; primes each session with environment state |
| **1 custom subagent** | Correctly wired for delegated research (subagents don't inherit skills — this shows how) |
| **Validator** | `scripts/validate_skills.py` checks every skill against the spec limits |

### Built to stay cheap

Everything the agent could load competes with your conversation for the same context window. The design pushes back in four ways:

- **Skills load on demand** — only a one-line description of each sits in context; full instructions load when that skill is actually needed.
- **Indexes before sources** — the agent reads a summary of your documents, and opens a source file only when the index points at one. A 90-minute transcript never enters context to answer a question a two-line index entry covers.
- **Reference files load conditionally** — lookup tables live in `references/` behind an explicit "only load this when…" instruction.
- **Scripts run instead of being read** — a script's source never enters context; only its output costs tokens.

---

## 1. Prerequisites

| You need | For |
|---|---|
| **Claude Code** (desktop app or CLI) | Everything |
| **Node.js 18+** | The browser-automation MCP |
| **Python 3.9+** | The bundled scripts and validator |
| **Git** | Sharing the workspace with your team |
| An issue tracker account | Filing defects |
| Access to your app's test environment | Actually running tests |

## 2. Set it up

**Get the workspace**

```bash
git clone <your-fork-of-this> qa-workspace
```
```bash
cd qa-workspace
```

Open the folder in Claude Code. `CLAUDE.md` and the skills in `.claude/skills/` are picked up automatically — there is nothing to "activate".

**Create your environment file**

```bash
cp .claude/qa-test-env.example.md .claude/qa-test-env.md
```

Fill in your URLs and per-role test logins. This file is git-ignored and must stay that way. Anything you leave as `<PLACEHOLDER>` simply makes the agent ask you in chat when a run needs it, so fill in only what you actually use.

**Turn on the hooks**

```bash
cp .claude/settings.json.example .claude/settings.json
```

That activates two things: a `PreToolUse` hook that refuses to commit your credentials file, and a `SessionStart` hook that tells each session what is configured and what isn't. The example file also carries commented-out `Stop` and `PostToolUse` hooks to adapt.

**Connect your MCP servers**

Three categories matter. Names and endpoints are yours to choose:

| Category | Used for | Notes |
|---|---|---|
| **Browser automation** | Driving the app under test | Local `stdio` server — CLI or `.mcp.json` only, no Connectors-UI path |
| **Issue tracker** | Reading tickets, filing defects | Usually a remote server; can be added through the Connectors UI |
| **Backend / data** | Verifying what the UI shows against the system of record | Often internal — keep the endpoint out of the repo |

```bash
claude mcp add playwright -- npx -y @playwright/mcp@latest
```
```bash
claude mcp list
```

To share config with the team, copy `.mcp.json.example` to `.mcp.json`. Teammates approve it on first run and authenticate remote servers with their own logins.

## 3. Fill in your project

This is the part that decides whether the workspace is useful or generic.

**Replace the placeholders in `CLAUDE.md`.** Application name, environments, tracker key, roles under test, integrations, open decisions. Keep it short — it loads into *every* conversation.

**Load `knowledge-base/`** — and write the indexes. Drop documents into the right folder, then fill in that folder's `INDEX.md`.

> Adding documents without writing the index makes things **worse**: more for the agent to wade through, and no map. The index is the whole mechanism.

`knowledge-base/README.md` has the routing map and explains what belongs where.

**Adapt the skills.** The five in `.claude/skills/` are working defaults. The parts most worth editing:

- `qa-test-writing/references/test-case-format.md` — match your tracker's columns
- `qa-bug-reporting/references/priority-and-labels.md` — match your priority scheme
- `qa-permission-testing` — point the lookup script at your real matrix

**Rename the prefix** if collisions are plausible. Everything is `qa-*`; a personal skill with the same name silently overrides a project one, so `acme-qa-*` is safer in a large org.

**Validate before committing:**

```bash
python scripts/validate_skills.py
```

## 4. Use it

Ask in plain language — the right skill loads on its own:

| You say | What happens |
|---|---|
| *"How is the approval workflow supposed to route orders?"* | Answers from the knowledge base, citing document and section |
| *"Why did we decide the storefront holds no pricing data?"* | Traces it to the call it was decided in, with the date |
| *"Write test cases for the inventory block on the product page"* | Drafts them in your column format, flagging anything inferred |
| *"Write test cases for the CRM customer sync"* | Covers both systems, the field mapping, **and** the failure path |
| *"Execute TC_PDP_002 on the sandbox"* | Drives the app, cross-checks the backend record, reports pass/fail with evidence |
| *"Can Customer Center L2 see another company's invoices?"* | Matrix → live config → actual behaviour, including the negative test |
| *"Draft a bug for this"* | Writes it in your format — **files nothing until you say "create it"** |

Two behaviours are deliberate and worth knowing:

- **Drafts come before writes.** Test cases and defects are posted in chat first. Nothing reaches your tracker without an explicit go-ahead.
- **Gaps are reported, not filled.** If the documents don't answer something, the agent says so rather than producing a confident guess. A guessed expected-result becomes a false defect and costs a developer an afternoon.

## 5. Repo structure

```
qa-workspace/
├── CLAUDE.md                    # Always-on project standards (fill in the placeholders)
├── ARCHITECTURE.md              # Why the workspace is shaped this way — read once
├── README.md                    # This file
├── .gitignore                   # Keeps credentials and run artefacts out of git
├── .mcp.json.example            # Shareable MCP config
├── .claude/
│   ├── qa-test-env.example.md   # Env TEMPLATE (committed, no real secrets)
│   ├── qa-test-env.md           # Your local copy (git-ignored — you create this)
│   ├── settings.json.example    # Hook configuration
│   ├── agents/
│   │   └── qa-researcher.md     # Custom subagent — note its `skills:` frontmatter
│   ├── hooks/
│   │   ├── block-secret-commit.sh   # PreToolUse — refuses to commit credentials
│   │   └── session-start-check.sh   # SessionStart — primes each session
│   └── skills/
│       ├── qa-context-lookup/       # + references/
│       ├── qa-test-writing/         # + references/test-case-format.md
│       ├── qa-test-execution/       # + references/report-format.md
│       ├── qa-permission-testing/   # + references/ + scripts/lookup_permission.py
│       └── qa-bug-reporting/        # + references/priority-and-labels.md
├── knowledge-base/              # Your project documents — each folder has an INDEX.md
│   ├── solution-documents/      #   functional spec, acceptance criteria
│   ├── technical-design/        #   TDD — config paths, identifiers, data flow
│   ├── requirements/            #   BRD and upstream requirements
│   ├── contracts/               #   SOW, contractual scope
│   ├── call-recordings/         #   transcripts + the mandatory INDEX.md
│   └── reference-data/          #   permission matrices, config exports, test data
├── reports/                     # Execution reports land here (git-ignored by default)
└── scripts/
    └── validate_skills.py       # Checks every skill against the spec limits
```

## 6. Things that will bite you

Collected because each one fails *silently* — nothing errors, you just get worse results.

| | |
|---|---|
| **Descriptions over 1,024 characters** | Risk being truncated exactly where the trigger words are. Run the validator. |
| **Subagents don't inherit skills** | They see a skill only if a custom agent names it in `skills:`. Built-in agents can't use skills at all. Keep skill-driven work in the main thread. |
| **Personal skills beat project skills** | A teammate's personal `qa-bug-reporting` silently overrides this repo's. Prefix your names. |
| **`PostCompact` doesn't re-inject context** | Use `SessionStart` with the `compact` matcher. That's the one whose output reaches the conversation. |
| **Auto-accept modes judge danger, not correctness** | Broken code isn't dangerous, so it passes. Pair permissive modes with a `Stop` hook that runs your tests. |
| **A passing report is a claim** | For unattended runs, start from the diff and the actual test output, not the summary. |
| **Documents without indexes** | Strictly worse than no documents. Write the index. |
| **`git rm` doesn't shrink history** | Committed credentials or large binaries stay forever. Prevention (the hook, `.gitignore`) is the only cheap fix. |

## 7. Extending it

Adding a new capability? Pick the right primitive — `ARCHITECTURE.md` has the full reasoning:

- Always true, every conversation → **`CLAUDE.md`**
- A procedure for a kind of task → **a skill**
- Must happen whether or not the model remembers → **a hook**
- Needs its own context window → **a subagent** (and list its skills)
- Talks to an external system → **an MCP server**

The most common mistake is putting a rule in `CLAUDE.md` and treating it as enforcement. Instructions are advice. If it genuinely must not happen, it belongs in a `PreToolUse` hook.
