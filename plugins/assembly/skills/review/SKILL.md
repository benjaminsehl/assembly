---
name: review
description: Use when reviewing a diff, branch, commit, or pull request for correctness, readability, architecture, security, and performance.
---

# Review

## Purpose

Review current changes with a bug-first posture. Findings come before summaries, and concrete issues include file and line references. Fan out to specialist reviewers in parallel by default; surface findings without auto-applying fixes.

## References

- `references/workflows/engineering-delivery.md`: review mode and findings format.
- `references/security-checklist.md`: security review triggers and checks.
- `references/performance-checklist.md`: performance review triggers and checks.
- `references/accessibility-checklist.md`: UI accessibility review triggers and checks.

## Workflow

1. State that the `review` workflow is active and identify the scope: working tree, staged diff, commits, or PR.
2. Inspect the diff and relevant surrounding code before judging; for GitHub PRs, use the GitHub MCP tools to read PR metadata, checks, and review context.
3. Fan out specialist reviewers in parallel by default:
   - Correctness reviewer: bugs, edge cases, off-by-one, null handling, error paths.
   - Architecture reviewer: design fit, layering, premature abstraction, missing abstraction.
   - Security reviewer: input handling, auth, secrets, dependencies, network, external integrations.
   - Performance reviewer: hot paths, rendering, queries, loops, bundles, concurrency.
   - Test reviewer: coverage gaps, brittle tests, missing characterization for legacy paths.
4. Skip a specialist when the diff demonstrably does not touch its surface (e.g., no UI → skip accessibility). Name what was skipped and why.
5. Merge findings, ordered by severity.
6. Surface findings only. Do not auto-apply fixes. The founder picks which findings to address; `code-simplify` runs separately when invoked.
7. Include open questions, test gaps, and residual risk after findings.

## Verification

- Specialist fan-out is named; skipped specialists are justified.
- Findings include file and line references when code is accessible.
- Severity is clear: Critical, Important, Suggestion, or Nit.
- Missing tests and unrun checks are called out.
- For PR review, PR state and check status are named when available.
- If no issues are found, remaining risk is still stated.
- No fixes are silently applied — the founder decides.

## Stop Conditions

- No diff, commit, PR, or review scope is accessible.
- Reviewing would require printing secrets or sensitive data.
- The requested review surface is too broad for the available context.
