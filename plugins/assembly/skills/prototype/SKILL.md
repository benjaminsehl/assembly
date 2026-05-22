---
name: prototype
description: Use when a project needs a throwaway tangible artifact before build; explores UI direction, state models, workflows, feasibility, or product feel.
---

# Prototype

## Purpose

Answer a risky product, UX, technical, or business question with the smallest tangible artifact that lets the user feel or inspect the direction before production build work.

## References

- `references/design-quality-checklist.md`: UI quality and AI-slop checks.
- `references/business-model-checklist.md`: pricing, offer, or demand-test prototypes.
- `references/workflows/product-strategy.md`: prototype and design-plan modes.
- `references/project-phases.md`: prototype phase evidence and exit gate.

## Workflow

1. State that `prototype` is active and write the exact question the prototype must answer.
2. Narrow the prototype to one learning goal.
3. Choose the branch:
   - Product or UI feel: build a small interactive UI or several sharply different variants.
   - Logic, state, or workflow: build a minimal runnable model that exposes state after each action.
   - Business or pricing: create a testable offer, landing copy, pricing strawman, or validation script.
4. Keep prototype code obviously temporary, close to the relevant app surface or under the project `prototypes/` folder.
5. Provide one command or URL to run it.
6. Avoid persistence unless persistence is the question; use scratch data when needed.
7. Capture the verdict in the project prototype phase file, an ADR, or a short project note.
8. Recommend delete, absorb into build, or continue prototyping.

## Verification

- The artifact directly answers the prototype question.
- The user can run or inspect it with one clear command, URL, or file path.
- Relevant state, variants, or trade-offs are visible.
- The final verdict is captured somewhere durable before production build work depends on it.

## Stop Conditions

- The prototype question is not clear enough to choose an artifact.
- The requested artifact is production work rather than throwaway learning.
- The prototype would require private data, irreversible side effects, or live integrations without approval.
