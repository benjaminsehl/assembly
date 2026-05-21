---
name: design-plan-review
description: Use before implementing user-facing UI to review UX quality, interaction model, accessibility, taste, and AI-slop risk.
---

# Design Plan Review

## Purpose

Review planned UI before implementation so the product is useful, coherent, and likely to feel good to real users.

## Underlying skills

- `frontend-ui-engineering`
- `founder-product-critique`
- `performance-optimization`

## Workflow

1. State that `design-plan-review` is active and identify the planned UI or user flow.
2. Read the spec, plan, design docs, screenshots, or existing UI conventions.
3. Use `frontend-ui-engineering` to review layout, components, states, responsiveness, accessibility, and interaction patterns.
4. Use `founder-product-critique` to check whether the flow creates a strong product moment.
5. Use `performance-optimization` for likely rendering, bundle, or interaction-latency risks.
6. Check `references/design-quality-checklist.md` for quality dimensions and AI-slop signals.
7. Output a design verdict with must-fix issues, recommended improvements, and the approved build shape.

## Verification

- Core user flow and primary action are clear.
- Empty, loading, error, and success states are covered when relevant.
- Accessibility and responsive behavior are considered.
- Any taste or UX concerns are concrete enough to implement.

## Stop Conditions

- There is no user flow or design artifact to review.
- The design needs user/product clarification before UI decisions.
- The review would require implementation rather than plan feedback.

