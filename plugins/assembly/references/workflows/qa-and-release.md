# QA And Release Workflow

## Contents

- Live QA
- Health check
- Ship
- PR readiness
- Post-release learning

Use this reference from `qa` and `ship`.

## Live QA

- Identify the app, URL, build, feature, or user flow under test.
- Define user paths, personas, risks, and evidence to collect.
- Test like a user, not just like a developer.
- Record bugs with repro steps, expected behavior, actual behavior, severity, and evidence.
- When fixing, retest the exact repro and recommend regression coverage.

## Health Check

Use only for broad periodic readiness, not ordinary changed-code review.

Check:

- Tests and CI health.
- Performance and accessibility readiness.
- Security and dependency risk.
- Documentation and decision trail.
- Maintainability and architectural drift.

Output blockers, important fixes, quick wins, and one next action.

## Ship

- Gather diff, tests, builds, CI, deployment path, feature flags, migrations, docs, and rollback path.
- Decide `GO` or `NO-GO`.
- Separate blockers from accepted risks and nice-to-have fixes.
- Name rollback triggers and rollback procedure.
- For GitHub-backed work, confirm PR state, CI/check status, review status, and whether the PR is draft or ready.
- Do not use subagents unless the user explicitly authorized parallel agent work.

## PR Readiness

Use this before marking a draft PR ready for review.

- Confirm the branch is pushed and the PR exists.
- Confirm targeted and broad verification has passed or clearly document accepted gaps.
- Run `review` against the final diff or PR.
- Run `code-simplify` on the changed files when simplification risk is reasonable.
- Fix important findings and rerun relevant checks.
- Update the PR body with final summary, verification, risk, and follow-up.
- Confirm the PR body explains why the work matters, the principles behind the change, and how the agent approached it.
- Ask before marking ready. Run `gh pr ready` only after the self-review and simplification pass are complete and the user explicitly authorizes the ready-for-review transition.
- Keep the PR draft if unresolved blockers, failing checks, missing verification, or user-requested hold remain.

## Post-Release Learning

- Grade against proposal outcomes, principles, and what good looks like.
- Capture what shipped, what users learned, what broke, and what changed.
- Record follow-up work in project docs.
- Propose memory updates only when the user explicitly asks for memory changes.
