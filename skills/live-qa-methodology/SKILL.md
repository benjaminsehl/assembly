---
name: live-qa-methodology
description: Use when testing a live app or runnable build like a user, collecting repro steps, evidence, severity, and regression recommendations.
---

# Live QA Methodology

## Workflow

Test the product through realistic user journeys:

1. Identify target users, primary flows, setup state, and test environment.
2. Cover happy paths, empty states, validation failures, navigation, persistence, permissions, and recovery.
3. For each bug, record reproducible steps, expected behavior, actual behavior, severity, environment, and evidence.
4. Re-test fixes in the same flow that found the bug.
5. Recommend regression tests for every meaningful product bug.

Use `references/qa-checklist.md` for coverage prompts when available.

## Output

Return:

- Tested flows.
- Bugs found with severity and repro steps.
- Evidence collected.
- Fix/re-test status.
- Regression recommendations.

## Verification

- Bugs are reproducible.
- Report-only QA does not mutate code.
- Fixing QA includes re-test evidence.

