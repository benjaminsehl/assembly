# QA And Release Workflow

## Contents

- Live QA
- Health check
- Ship
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
- Do not use subagents unless the user explicitly authorized parallel agent work.

## Post-Release Learning

- Grade against proposal outcomes, principles, and what good looks like.
- Capture what shipped, what users learned, what broke, and what changed.
- Record follow-up work in project docs.
- Propose memory updates only when the user explicitly asks for memory changes.
