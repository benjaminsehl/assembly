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
# defense in depth, not a sandbox: it matches a flat command string, so it cannot
# see actions hidden behind shell aliases, script wrappers (`npm run deploy`,
# `make ship`), or a protected branch that is the current checkout. It biases
# toward a one-keystroke confirmation and fails closed (asks) if it cannot
# evaluate. It cannot see money, credential, or external-messaging actions that
# are not shell commands — those stay governed by the protocol and tool-level
# permission prompts.
#
# All reason strings below are interpolated into JSON by raw substitution, so they
# MUST stay free of double quotes, backslashes, and newlines.

set -euo pipefail

payload="$(cat)"

# A safety control must fail closed: if we cannot run our matcher, ask.
if ! command -v grep >/dev/null 2>&1; then
  printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Assembly ask-first guard could not evaluate this command (grep unavailable). Confirm manually."}}'
  exit 0
fi

# Extract the Bash command. Prefer jq, then python3. Only when neither parser is
# present do we scan the raw payload (coarse, but safe-failing toward "ask").
cmd=""
have_parser=0
if command -v jq >/dev/null 2>&1; then
  have_parser=1
  cmd="$(printf '%s' "$payload" | jq -r '.tool_input.command // empty' 2>/dev/null || true)"
elif command -v python3 >/dev/null 2>&1; then
  have_parser=1
  cmd="$(printf '%s' "$payload" | python3 -c 'import json,sys
try:
    print(json.load(sys.stdin).get("tool_input", {}).get("command", ""))
except Exception:
    pass' 2>/dev/null || true)"
fi
[ "$have_parser" -eq 1 ] || cmd="$payload"

# A parser that returned nothing means there is no command to guard.
[ -n "$cmd" ] || exit 0

# has PATTERN -> true when the command matches the extended regex (case-insensitive).
has() { printf '%s' "$cmd" | grep -Eiq -e "$1"; }

# `git` may carry global options before the subcommand (e.g. `git -C <path> push`,
# `git -c push.default=current push`). Allow them so the subcommand matchers still
# fire — `git -C` is the canonical way an agent operates on a repo without `cd`.
GIT='git( +(-c +[^ ]+|-C +[^ ]+|--git-dir(=[^ ]+| +[^ ]+)|--work-tree(=[^ ]+| +[^ ]+)|--namespace(=[^ ]+| +[^ ]+)|-p|--paginate|--no-pager|--bare))*'

# Force flags / refspecs: --force, --force-with-lease, short clusters containing f
# (-f, -fu, -uf), --mirror (can delete every remote branch), and +refspec.
FORCE='(--force( |$)|--force-with-lease|--mirror| -[a-z]*f[a-z]*( |$)| \+[A-Za-z])'
# A "main"/"master" target as a bare arg, a :refspec dest, or a +refspec dest.
MAIN='( |:|\+)(refs/heads/)?(main|master)( |$)'

reason=""
# --- Pull requests, releases ---------------------------------------------------
if   has 'gh +pr +merge';                                  then reason="merging a pull request"
elif has 'gh +api( |$)' && has 'pulls/[0-9]+/merge';       then reason="merging a pull request via gh api"
elif has 'gh +pr +ready';                                  then reason="marking a pull request ready for review"
elif has 'gh +pr +create' && ! has '(--draft|-d)( |$)';    then reason="creating a non-draft pull request"
elif has 'gh +release +create';                            then reason="publishing a GitHub release"
# --- git push family -----------------------------------------------------------
elif has "${GIT} +push" && has "$FORCE";                   then reason="force-pushing or mirroring"
elif has "${GIT} +push" && has '(--delete| :)';            then reason="deleting a remote branch"
elif has "${GIT} +push" && has "$MAIN";                    then reason="pushing directly to main/master"
# --- branch & history destruction ----------------------------------------------
elif has "${GIT} +branch +(-[a-z]*[dD]( |$)|--delete)";    then reason="deleting a branch"
elif has "${GIT} +reset" && has '--hard';                  then reason="a hard reset (discards uncommitted work)"
elif has "${GIT} +clean" && has '(--force|-[a-z]*f[a-z]*( |$))'; then reason="git clean (deletes untracked files)"
elif has "${GIT} +checkout +(-- +)?\.( |$)";               then reason="discarding working-tree changes (git checkout .)"
elif has "${GIT} +restore" && has ' \.( |$)' && ! has '\-\-staged'; then reason="discarding working-tree changes (git restore .)"
# --- deploy / publish ----------------------------------------------------------
elif has '(^| )(wrangler|netlify) +(pages +)?(deploy|publish)'; then reason="deploying"
elif has '(^| )wrangler +versions +deploy';                then reason="deploying"
elif has '(^| )vercel\b' && has '(--prod|--prebuilt)';     then reason="a production deploy"
elif has '(^| )(npm|pnpm|yarn|bun) +publish';              then reason="publishing a package"
# --- infrastructure / catastrophic ---------------------------------------------
elif has 'terraform +(apply|destroy)';                     then reason="a terraform apply/destroy"
elif has 'kubectl +delete';                                then reason="deleting Kubernetes resources"
elif has '(^| )aws +s3 +rm' && has '--recursive';          then reason="a recursive S3 delete"
elif has '(^| )dd +' || has '(^| )mkfs';                   then reason="a raw disk write (dd/mkfs)"
# --- recursive force delete ----------------------------------------------------
elif has '(^| )rm ' \
     && has '(-[a-z]*r[a-z]*( |$)|--recursive)' \
     && has '(-[a-z]*f[a-z]*( |$)|--force)';                then reason="a recursive force delete (rm -rf)"
fi

[ -n "$reason" ] || exit 0

msg="Assembly ask-first floor: this command looks like ${reason}. Per the Assembly SPEC, confirm before merging PRs, deploying, force-pushing, deleting branches or refs, publishing, or destructive operations. Approve to proceed, or revise the command."

printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"%s"}}\n' "$msg"
exit 0
