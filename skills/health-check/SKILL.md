---
name: health-check
description: Use for periodic product and engineering readiness audits across tests, performance, accessibility, security, docs, and maintainability.
---

# Health Check

## Purpose

Audit whether a project is healthy enough to keep building on: product clarity, engineering quality, performance, security, docs, and operational readiness.

## Underlying skills

- `code-review-and-quality`
- `performance-optimization`
- `security-and-hardening`
- `documentation-and-adrs`
- `test-driven-development`

## Workflow

1. State that `health-check` is active and define the repo, app, or release surface being audited.
2. Inspect project commands, docs, tests, CI hints, and recent changes.
3. Use `code-review-and-quality` to identify maintainability, architecture, and test-health risks.
4. Use `performance-optimization`, `security-and-hardening`, and `documentation-and-adrs` for specialized checks.
5. Use `test-driven-development` to evaluate test coverage gaps and proof quality.
6. Check the existing performance, security, accessibility, and testing references.
7. Output a scored health report with blockers, important fixes, quick wins, and the next recommended action.

## Verification

- The report names commands or checks inspected or run.
- Findings are grouped by severity.
- Product, engineering, and business-readiness risks are separated.
- The next action is concrete.

## Stop Conditions

- The repo or target surface is not accessible.
- Running checks would require unsafe side effects or credentials.
- The requested scope is too broad to audit honestly in one pass.

