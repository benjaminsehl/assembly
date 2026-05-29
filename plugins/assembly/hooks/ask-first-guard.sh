#!/usr/bin/env bash
#
# Assembly ask-first guard (Claude Code only).
#
# A PreToolUse hook on the Bash tool. When a command looks like one of the
# Assembly "ask-first floor" actions, it returns permissionDecision "ask" so the
# human confirms even under bypassPermissions. Otherwise it stays silent (exit 0)
# and the normal permission flow proceeds.
#
# This is the runtime counterpart to the prose floor in docs/SPEC.md. It is
# deliberately conservative and biased toward a one-keystroke confirmation; it is
# defense in depth, not a substitute for judgment. It cannot see money,
# credential, or external-messaging actions that are not shell commands — those
# stay governed by the protocol and tool-level permission prompts.

set -euo pipefail

payload="$(cat)"

# Extract the Bash command. Prefer jq, then python3, else fall back to scanning
# the raw payload so a missing dependency never blocks a tool call.
cmd=""
if command -v jq >/dev/null 2>&1; then
  cmd="$(printf '%s' "$payload" | jq -r '.tool_input.command // empty' 2>/dev/null || true)"
elif command -v python3 >/dev/null 2>&1; then
  cmd="$(printf '%s' "$payload" | python3 -c 'import json,sys
try:
    print(json.load(sys.stdin).get("tool_input", {}).get("command", ""))
except Exception:
    pass' 2>/dev/null || true)"
fi
[ -n "$cmd" ] || cmd="$payload"

# has PATTERN -> true when the command matches the extended regex (case-insensitive).
has() { printf '%s' "$cmd" | grep -Eiq -e "$1"; }

reason=""
if   has 'gh +pr +merge';                                       then reason="merging a pull request"
elif has 'gh +pr +ready';                                       then reason="marking a pull request ready for review"
elif has 'gh +pr +create' && ! has '\-\-draft';                 then reason="creating a non-draft pull request"
elif has 'gh +release +create';                                 then reason="publishing a GitHub release"
elif has 'git +push' && has '(\-\-force|\-\-force-with-lease| \-f( |$))'; then reason="force-pushing"
elif has 'git +push' && has '(\-\-delete| :)';                  then reason="deleting a remote branch"
elif has 'git +push' && has ' (main|master)( |$)';              then reason="pushing directly to main/master"
elif has 'git +branch +-(d|D)\b';                               then reason="deleting a branch"
elif has 'git +reset +\-\-hard';                                then reason="a hard reset (discards uncommitted work)"
elif has 'git +clean +\-[a-z]*f';                               then reason="git clean (deletes untracked files)"
elif has '(wrangler|netlify) +(deploy|publish)';                then reason="deploying"
elif has 'vercel' && has '(\-\-prod|\-\-prebuilt)';             then reason="a production deploy"
elif has '(npm|pnpm|yarn|bun) +publish';                        then reason="publishing a package"
elif has 'rm +\-[a-z]*r[a-z]*f|rm +\-[a-z]*f[a-z]*r';           then reason="a recursive force delete (rm -rf)"
fi

[ -n "$reason" ] || exit 0

msg="Assembly ask-first floor: this command looks like ${reason}. Per the Assembly SPEC, confirm before merging PRs, deploying, force-pushing, deleting branches or refs, publishing, or destructive operations. Approve to proceed, or revise the command."

printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"%s"}}\n' "$msg"
exit 0
