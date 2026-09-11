#!/usr/bin/env bash
# PreToolUse hook — refuses any command that would commit the local environment file.
#
# Why a hook and not a CLAUDE.md rule: an instruction is advice the model may or may not
# recall under pressure. A PreToolUse hook runs before the tool call and can stop it, so
# the guarantee does not depend on anyone remembering. Credentials in git history are
# effectively permanent, which makes this exactly the kind of rule that must be enforced
# rather than requested.
#
# Wire it up in .claude/settings.json — see settings.json.example.
#
# Contract: read the tool call as JSON on stdin. Exit 0 to allow, exit 2 to block with
# the message on stderr.

set -uo pipefail

PROTECTED_PATTERNS=(
  "qa-test-env.md"
  ".env"
  "credentials.json"
  "secrets.yml"
  ".har"            # network captures carry session cookies and auth headers
)

payload="$(cat)"

# Pull the command out of the tool input. Prefer jq; fall back to grep so the hook still
# works on a machine without it.
if command -v jq >/dev/null 2>&1; then
  command_text="$(printf '%s' "$payload" | jq -r '.tool_input.command // empty' 2>/dev/null)"
else
  command_text="$(printf '%s' "$payload" | grep -o '"command"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | sed 's/.*:[[:space:]]*"//; s/"$//')"
fi

[ -z "${command_text:-}" ] && exit 0

# Only interested in commands that stage or commit.
case "$command_text" in
  *"git add"*|*"git commit"*|*"git stage"*) ;;
  *) exit 0 ;;
esac

for pattern in "${PROTECTED_PATTERNS[@]}"; do
  if printf '%s' "$command_text" | grep -qF -- "$pattern"; then
    cat >&2 <<MSG
BLOCKED: this command references '$pattern', which holds real credentials.

  $command_text

That file is git-ignored on purpose. Credentials committed to git stay in history even
after deletion, so the only safe move is not to commit them at all.

If you genuinely need to commit a template, commit the .example file instead.
MSG
    exit 2
  fi
done

# Catch the blunt instruments too: `git add -A` / `git add .` will sweep in anything that
# is not ignored, which is how these files usually escape.
case "$command_text" in
  *"git add -A"*|*"git add --all"*|*"git add ."*)
    if [ -f ".claude/qa-test-env.md" ] && ! git check-ignore -q ".claude/qa-test-env.md" 2>/dev/null; then
      cat >&2 <<'MSG'
BLOCKED: a bulk `git add` would stage .claude/qa-test-env.md, which is NOT currently
git-ignored and contains credentials.

Add it to .gitignore first, then retry.
MSG
      exit 2
    fi
    ;;
esac

exit 0
