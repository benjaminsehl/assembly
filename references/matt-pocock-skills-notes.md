# Matt Pocock Skills Notes

Source inspiration: https://github.com/mattpocock/skills

Use these ideas as methodology inspiration, not copied runtime behavior.

## Useful Ideas To Adapt

- Small, composable skills should preserve user control instead of owning the whole process.
- Alignment failures are often communication failures; interview or "grill" the plan until terms, branches, and trade-offs are clear.
- When the codebase can answer a question, inspect the code instead of asking the user.
- Shared project language reduces agent verbosity and improves naming.
- Decision records should be rare: use them only for decisions that are hard to reverse, surprising without context, and based on a real trade-off.
- Prototypes should answer a question with throwaway code, one command to run, visible state or variants, and a captured verdict.
- Handoffs should point to existing artifacts instead of duplicating them, redact sensitive details, and include suggested next skills.
- Zoom-out requests should map the relevant modules and callers using project vocabulary.

## Plugin Adaptation

- `prototype` adapts the throwaway-question pattern into the four-phase project lifecycle.
- `project-status` covers much of the "handoff" and "zoom out" need by identifying phase, evidence, missing artifacts, and next skills.
- `new-project` uses the documentation discipline from grill-with-docs but stores it in a project workspace rather than a single `CONTEXT.md`.
- Existing `learn`, `retro`, and `documentation-and-adrs` keep durable lessons and decisions from becoming scattered notes.
