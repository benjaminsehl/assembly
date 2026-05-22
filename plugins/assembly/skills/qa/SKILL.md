---
name: qa
description: Use after implementation to test the product like a user, find bugs with repro steps, verify fixes, and recommend regression coverage.
---

# QA

## Purpose

Use the product like a real user after implementation. Find product bugs, not just code issues, and turn them into reproducible fixes or clear reports.

## References

- `references/qa-checklist.md`: user-flow and scenario coverage.
- `references/testing-patterns.md`: regression coverage recommendations.
- `references/workflows/qa-and-release.md`: live QA mode and reporting shape.

## Workflow

1. State that `qa` is active and identify the app, URL, build, or feature under test.
2. Define user paths, personas, risks, and evidence to collect.
3. For browser apps, use available browser tooling to interact with the product.
4. Record every bug with repro steps, expected behavior, actual behavior, severity, and evidence.
5. If asked to fix issues, isolate root cause and add regression coverage for meaningful bugs.
6. Check the QA references for scenario coverage.
7. End with pass/fail status, bugs found, fixes made or recommended, and remaining risk.

## Verification

- Tested flows are listed.
- Bugs include reproducible steps and severity.
- Fixes are re-tested.
- Regression coverage is added or recommended for each meaningful bug.

## Stop Conditions

- No runnable app, URL, build instructions, or target feature is available.
- Authentication or private data blocks testing and cannot be safely provided.
- The user asked for report-only QA and fixing would change code.
