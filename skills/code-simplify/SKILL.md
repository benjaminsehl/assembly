---
name: code-simplify
description: Use when simplifying working code for clarity and maintainability while preserving exact behavior.
---

# Code Simplify

## Purpose

Reduce code complexity without changing behavior. Simplification is only successful when tests and behavior still hold.

## References

- `references/workflows/engineering-delivery.md`: simplification mode and behavior-preservation rules.
- `references/testing-patterns.md`: characterization and regression testing.

## Workflow

1. State that the `code-simplify` workflow is active and identify the target files or recent diff.
2. Read the target code, its callers, tests, and project conventions.
3. Identify high-value simplifications: clearer names, guard clauses, smaller functions, removed duplication, or deleted dead code.
4. Preserve behavior exactly. Characterize behavior before changing risky code.
5. Apply simplifications in small steps, verifying after each meaningful step.
6. Review the final diff for accidental behavior changes or readability regressions.
7. Revert or abandon any simplification that cannot be verified.

## Verification

- Behavior is covered by existing or newly added tests where practical.
- Targeted checks pass after each meaningful simplification.
- Final diff is smaller or clearer for a concrete reason.
- Any unverified behavior is disclosed.

## Stop Conditions

- Behavior is not understood and cannot be characterized safely.
- The simplification requires architectural redesign outside the requested scope.
- The target includes unrelated user changes that would be risky to edit.
