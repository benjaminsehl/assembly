# Decision: Drop The "Hermes" Project Name

Date: 2026-05-28

## Context

Earlier docs introduced "Hermes" as the codename for the post-1.0 orchestrator that would coordinate Assembly-driven agent sessions. The name shows up in the 2026-05-23 ([Codex First, Hermes Next](2026-05-23-codex-first-hermes-next.md)) decision, the post-1.0 roadmap, the orchestrator contract draft, the spec, the north star, and several smaller docs.

The orchestrator concept is still right: a future general-manager layer over Assembly's project trail, phase gates, and GitHub handoff. The name has not earned its place — it carries product-direction implications (mythology, "messenger of the gods") that have not been validated, and it creates a forward-looking branded surface before any of the orchestrator work has been built.

## Decision

Drop the name "Hermes" from forward-looking docs. Refer to the concept as "the post-1.0 orchestrator" (canonical), "post-1.0 orchestration" (action/concept), or "the orchestrator" in context.

The historical decision doc `docs/decisions/2026-05-23-codex-first-hermes-next.md` and the `.agents/log.md` entries that mention Hermes are left untouched as historical record — they describe what was decided and logged at the time.

## Why

- The name has no demonstrated reason to exist yet; the concept does the work.
- A working codename in product docs gets cited by future agents and quietly hardens into a brand commitment before it should.
- Leaving naming open keeps room for a more deliberate naming pass once the orchestrator contract has been spiked.

## Implications

- Forward-looking docs (spec, plans, north star, vision, principles, discovery, research, status, README, decision doc cross-references) say "post-1.0 orchestrator" / "post-1.0 orchestration".
- The two Hermes-named docs are renamed:
  - `docs/plans/2026-05-27-hermes-orchestrator-roadmap.md` -> `docs/plans/2026-05-27-post-1-0-orchestrator-roadmap.md`.
  - `docs/tech-design/hermes-assembly-contract.md` -> `docs/tech-design/post-1-0-orchestrator-contract.md`.
- The 2026-05-23 decision doc and `.agents/log.md` are not edited; they remain accurate historical records.
- Future naming for the orchestrator (if any) should land as a separate decision doc with explicit reasoning.

## Out Of Scope

- Renaming or retiring any other project names in the repo.
- Changing the orchestrator concept itself.
- Backfilling the rename into historical log entries or merged decision docs.
