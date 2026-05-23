# Engineering Delivery Workflow

## Contents

- Spec
- Plan
- Build
- Test
- Review
- Code simplify
- PR review feedback
- GitHub handoff

Use this reference from `spec`, `plan`, `build`, `test`, `review`, and `code-simplify`.

## Spec

- Define objective, users, constraints, commands, boundaries, success criteria, and open questions.
- Surface assumptions before treating the spec as final.
- Save the spec using the repo convention, usually `SPEC.md` or `docs/SPEC.md`.
- Stop at review before planning unless the user asks to continue.

## Plan

- Start from an approved spec or equivalent requirements.
- Break work into vertical slices with acceptance criteria and verification.
- Name dependencies and checkpoints.
- Save plan and todo files using the repo convention.
- Stop before implementation unless the user asks to continue.

## Build

- Treat an empty or minimal `build` prompt as permission to infer and execute the next unambiguous build-track gate from project evidence.
- Follow the engineering spine when no target is named: repair/spec requirements, plan tasks, implement one slice, test, review, simplify, then prepare GitHub handoff.
- Ask before inventing missing product or design decisions. Keep moving when the missing step is mechanical and recoverable from existing docs.
- Implement one planned slice at a time when a plan exists.
- Write or identify the target test first for behavior changes when practical.
- Make the smallest complete change.
- Keep unrelated cleanup out of scope.
- Run targeted verification and the broadest practical regression check.
- Update task status only after verification passes or skipped checks are explained.
- For material repo changes with a GitHub remote, prepare a PR handoff unless the user says local-only.

## Test

- For bugs, prove the bug with a failing test before fixing when practical.
- For new behavior, write tests that describe the intended outcome.
- Use browser/runtime verification for UI behavior.
- Report targeted and broader check results separately.

## Review

- Inspect the diff plus relevant surrounding code.
- Use `gh` for PR metadata, changed files, checks, and review-thread context when the scope is a GitHub PR.
- Lead with findings ordered by severity.
- Include file and line references for concrete issues.
- Apply security, performance, and accessibility checklists only when their triggers apply.
- If there are no findings, say so and name residual risk.

## Code Simplify

- Preserve behavior exactly.
- Prefer clearer names, guard clauses, smaller functions, removed duplication, and deleted dead code.
- Characterize behavior before changing risky code.
- Verify after each meaningful step.
- Abandon simplifications that cannot be proved safe.

## PR Review Feedback

Use this when the user asks to address GitHub PR comments, requested changes, or unresolved review threads.

- Resolve the PR from local branch context or the provided PR URL/number.
- Fetch thread-aware review state with `gh api graphql` or a helper that preserves review-thread IDs, resolution state, outdated state, file paths, and line anchors.
- Cluster actionable comments by behavior or file; separate fixes from questions, duplicates, stale threads, and non-actionable notes.
- Implement fixes traceably, keeping each change tied to the feedback it addresses.
- If a comment needs explanation rather than code, reply with the reasoning instead of forcing a code change.
- Commit and push fixes to the PR branch when handoff is in scope.
- Reply to review threads and mark them resolved only when the user explicitly asks for that GitHub write action.
- Leave ambiguous or conflicting feedback unresolved and explain the tradeoff.

## GitHub Handoff

Use this for material changes in a git repo with a GitHub remote.

- Inspect branch, remote, status, and whether a PR already exists before committing.
- Keep commits focused and do not include unrelated user changes.
- Prefer a topic branch over committing directly to `main`.
- Use a branch switch pattern that works for both existing and new branches.
- Stage intentionally, commit with a clear message, and push with `git`.
- Use `gh` to open a draft PR when none exists, or `gh pr edit` to update the existing PR for the branch.
- Write a descriptive PR body that explains why the PR exists, the first principles behind the change, how the agent approached it, what changed, verification, risks, and follow-up.
- Leave the PR as draft until verification passes and the agent has run its own `review` and `code-simplify` pass.
- After fixes and final verification, ask before marking a draft PR ready. Run `gh pr ready` only after explicit user authorization.
- If GitHub handoff is blocked by missing auth, no writable remote, branch protection, network failure, or unavailable `gh`, do not loop. Report the blocker, the completed local work, verification status, and the exact next command or credential/access step needed.
- Do not merge, deploy, delete branches, or create non-draft PRs without explicit user direction.

Suggested command flow:

```bash
git status --short --branch
git branch --list <topic-branch>
git switch <topic-branch> || git switch -c <topic-branch>
git add <intentional-files>
git commit -m "<focused message>"
git push -u origin HEAD
gh pr view --json number,url,isDraft,headRefName || gh pr create --draft --title "<title>" --body-file <body-file>
gh pr edit --title "<title>" --body-file <body-file>
gh pr view --json url,state,isDraft,headRefName
```

After verification, self-review, and simplification gates pass:

```bash
# Ask the user first. Run only after explicit authorization:
gh pr ready <pr-number>
```

Draft PR body shape:

- Why this PR exists.
- First principles or product/engineering principles behind the change.
- How the agent approached the work.
- What changed.
- Verification.
- Risks and tradeoffs.
- Follow-up.
