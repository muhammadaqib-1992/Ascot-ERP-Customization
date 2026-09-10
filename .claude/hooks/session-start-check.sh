#!/usr/bin/env bash
# SessionStart hook — primes a session with the environment facts the agent would
# otherwise have to ask for, and warns about setup that is not finished.
#
# Whatever this prints on stdout is added to the conversation, which makes it the right
# place for the "state of the world" that changes between machines and between days.
#
# Two matchers matter (see settings.json.example):
#   startup  - fresh session only
#   compact  - AFTER compaction. This is how you re-inject context that compaction
#              dropped. PostCompact does NOT get its output back into the conversation;
#              this is the one that does. It is the single most common hook mistake.

set -uo pipefail

ENV_FILE=".claude/qa-test-env.md"
EXAMPLE_FILE=".claude/qa-test-env.example.md"

echo "QA workspace session"
echo ""

# --- environment file ---------------------------------------------------------
if [ ! -f "$ENV_FILE" ]; then
  echo "SETUP INCOMPLETE: $ENV_FILE does not exist."
  echo "  Copy it from $EXAMPLE_FILE and fill in your own values."
  echo "  Until then, ask the user for URLs and logins per run."
else
  placeholders="$(grep -c '<PLACEHOLDER>' "$ENV_FILE" 2>/dev/null || echo 0)"
  if [ "$placeholders" -gt 0 ]; then
    echo "Environment file present, with $placeholders unfilled <PLACEHOLDER> value(s)."
    echo "  Ask the user for those specific values when a run needs them."
  else
    echo "Environment file present and fully populated."
  fi
fi

# --- knowledge base -----------------------------------------------------------
if [ -d "knowledge-base" ]; then
  docs=$(find knowledge-base -type f ! -name "INDEX.md" ! -name "README.md" ! -name ".gitkeep" 2>/dev/null | wc -l | tr -d ' ')
  echo "Knowledge base: $docs source document(s)."
  if [ "$docs" -gt 0 ]; then
    echo "  Read the folder INDEX.md files before opening any source document."
  else
    echo "  Empty. Answer from documents only once they are added; do not fill gaps by guessing."
  fi
fi

# --- reminders that survive compaction ---------------------------------------
echo ""
echo "Standing rules: draft test cases and defects in chat before writing them anywhere;"
echo "never put credentials in reports, screenshots, the tracker, or committed files."

exit 0
