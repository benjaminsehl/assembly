---
name: review
description: Use when reviewing a diff, branch, commit, or pull request for correctness, readability, architecture, security, and performance.
---

# Review

## Purpose

Review current changes with a bug-first posture. Findings come before summaries, and concrete issues include file and line references.

## References

- `references/workflows/engineering-delivery.md`: review mode and findings format.
- `references/security-checklist.md`: security review triggers and checks.
- `references/performance-checklist.md`: performance review triggers and checks.
- `references/accessibility-checklist.md`: UI accessibility review triggers and checks.

## Workflow

1. State that the `review` workflow is active and identify the scope: working tree, staged diff, commits, or PR.
2. Inspect the diff and relevant surrounding code before judging; for GitHub PRs, use `gh` to read PR metadata, checks, and review context.
3. Review correctness, readability, architecture, tests, and maintainability.
4. Apply the security checklist when the change touches input, auth, data storage, secrets, dependencies, network, or external integrations.
5. Apply the performance checklist when the change touches hot paths, rendering, queries, loops, bundles, concurrency, or resource usage.
6. Report findings first, ordered by severity.
7. Include open questions, test gaps, and residual risk after findings.

## Verification

- Findings include file and line references when code is accessible.
- Severity is clear: Critical, Important, Suggestion, or Nit.
- Missing tests and unrun checks are called out.
- For PR review, PR state and check status are named when available.
- If no issues are found, remaining risk is still stated.

## Stop Conditions

- No diff, commit, PR, or review scope is accessible.
- Reviewing would require printing secrets or sensitive data.
- The requested review surface is too broad for the available context.
