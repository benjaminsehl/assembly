# Implementation Plan: Codex Agent Skills Plugin

## Overview

Build the plugin in careful layers: first lock the command contract, then add validation, then add the seven entry skills, then vendor or adapt the underlying skills, then run smoke tests in a throwaway project. The command layer is load-bearing, so every phase should leave us with a reviewable artifact and a clear verification checkpoint.

## Architecture Decisions

- The seven command-like workflows are Codex skills, not slash commands. Codex plugin manifests expose `skills`, and the local spec does not define a `.codex/commands` equivalent.
- Entry skills stay thin. They orchestrate and route, while detailed workflows live in deeper skills.
- The plugin should be self-contained. Depending on `/Users/sai/.agents/skills` would make it fragile across machines and Codex sessions.
- Validation is part of the product. A broken skill graph is a product bug, not a documentation typo.
- `ship` needs a Codex-specific adaptation because Claude's command assumes automatic parallel subagents, while Codex should only spawn subagents when explicitly authorized.

## Phase 1: Contract and Scaffold

### Task 1: Finalize Plugin Manifest

Description: Make `.codex-plugin/plugin.json` valid and intentional for a private local developer-tools plugin.

Acceptance criteria:

- [ ] Manifest parses as JSON.
- [ ] `skills` points to `./skills/`.
- [ ] No placeholder paths reference missing hooks, MCP servers, apps, screenshots, or icons.

Verification:

- [ ] `python3 -m json.tool .codex-plugin/plugin.json >/dev/null`

Files likely touched:

- `.codex-plugin/plugin.json`

Estimated scope: XS

### Task 2: Lock the Seven Entry-Skill Contract

Description: Create `docs/COMMAND_CONTRACT.md` defining each entry skill's trigger, inputs, required outputs, underlying skills, and refusal or stop conditions.

Acceptance criteria:

- [ ] All seven entry skills have explicit responsibilities.
- [ ] Each entry skill has success evidence.
- [ ] The contract names what the entry skill must not do.

Verification:

- [ ] Manual review against `docs/SPEC.md`.

Files likely touched:

- `docs/COMMAND_CONTRACT.md`

Estimated scope: S

### Checkpoint: Foundation

- [ ] Spec reviewed.
- [ ] Plan reviewed.
- [ ] Manifest valid.
- [ ] Command contract approved.

## Phase 2: Validation Harness

### Task 3: Add Plugin Shape Validator

Description: Add a script that verifies the plugin manifest, required directories, and skill file anatomy.

Acceptance criteria:

- [ ] Fails when `plugin.json` is invalid.
- [ ] Fails when a required entry skill is missing.
- [ ] Fails when a `SKILL.md` lacks required frontmatter.

Verification:

- [ ] `python3 scripts/validate_plugin.py`

Files likely touched:

- `scripts/validate_plugin.py`
- `tasks/todo.md`

Estimated scope: M

### Task 4: Add Skill Graph Validator

Description: Add a validator for the seven-entry mapping and underlying skill references.

Acceptance criteria:

- [ ] Fails if an entry skill omits a required underlying skill.
- [ ] Fails if an entry skill references a missing skill directory.
- [ ] Flags entry skills that exceed a conservative size limit.

Verification:

- [ ] `python3 scripts/validate_skill_graph.py`

Files likely touched:

- `scripts/validate_skill_graph.py`
- `docs/COMMAND_CONTRACT.md`

Estimated scope: M

### Checkpoint: Guardrails

- [ ] Manifest validation passes.
- [ ] Skill graph validation passes against placeholder fixtures or intentionally reports missing skills before implementation.
- [ ] We know validation will catch drift before skills become operational.

## Phase 3: Entry Skills

### Task 5: Implement `spec` and `plan`

Description: Add the first two entry skills for defining and planning work.

Acceptance criteria:

- [ ] `skills/spec/SKILL.md` routes to definition skills and saves a spec.
- [ ] `skills/plan/SKILL.md` routes to planning and task breakdown.
- [ ] Both include clear human-review gates.

Verification:

- [ ] `python3 scripts/validate_plugin.py`
- [ ] `python3 scripts/validate_skill_graph.py`
- [ ] Manual smoke prompt in a throwaway folder.

Files likely touched:

- `skills/spec/SKILL.md`
- `skills/plan/SKILL.md`
- `tasks/todo.md`

Estimated scope: M

### Task 6: Implement `build` and `test`

Description: Add implementation and verification entry skills.

Acceptance criteria:

- [ ] `build` chooses one pending task and requires test/build evidence.
- [ ] `test` supports feature TDD and bug Prove-It workflows.
- [ ] Browser verification is called out for UI/runtime work.

Verification:

- [ ] Validators pass.
- [ ] Manual smoke prompt against a tiny fixture project.

Files likely touched:

- `skills/build/SKILL.md`
- `skills/test/SKILL.md`
- `tasks/todo.md`

Estimated scope: M

### Task 7: Implement `review`, `code-simplify`, and `ship`

Description: Add quality, simplification, and launch decision entry skills.

Acceptance criteria:

- [ ] `review` leads with file/line findings when code is available.
- [ ] `code-simplify` preserves behavior and verifies after each meaningful simplification.
- [ ] `ship` produces GO/NO-GO with blockers, risks, and rollback plan.
- [ ] `ship` is Codex-safe about subagents and parallelization.

Verification:

- [ ] Validators pass.
- [ ] Manual smoke prompt against a non-trivial diff.

Files likely touched:

- `skills/review/SKILL.md`
- `skills/code-simplify/SKILL.md`
- `skills/ship/SKILL.md`
- `tasks/todo.md`

Estimated scope: M

### Checkpoint: Entry Surface

- [ ] All seven entry skills exist.
- [ ] All seven entry skills pass graph validation.
- [ ] Entry skills remain thin.

## Phase 4: Underlying Skill Library

### Task 8: Vendor or Adapt Required Skills

Description: Bring in the deeper skill library needed by the seven entry points.

Acceptance criteria:

- [ ] Required underlying skill directories exist.
- [ ] Source attribution is preserved.
- [ ] Any local Codex-specific changes are documented.

Verification:

- [ ] Validators pass.
- [ ] Diff review confirms no accidental truncation.

Files likely touched:

- `skills/*/SKILL.md`
- `references/*`
- `docs/SOURCE_NOTES.md`

Estimated scope: L; split if needed

### Task 9: Add Reference Checklists and Persona Adaptation

Description: Add the supporting checklists and decide how reviewer personas should be represented in Codex.

Acceptance criteria:

- [ ] Security, performance, accessibility, and testing references are available.
- [ ] Persona behavior needed by `ship` is available as skills or documented subagent prompts.
- [ ] Codex subagent limitations are represented accurately.

Verification:

- [ ] Validators pass.
- [ ] Manual `ship` dry run includes all required audit dimensions.

Files likely touched:

- `references/*`
- `skills/*`
- `docs/COMMAND_CONTRACT.md`

Estimated scope: M

### Checkpoint: Self-Contained Plugin

- [ ] The plugin no longer depends on global `/Users/sai/.agents/skills`.
- [ ] All entry-skill references resolve locally.
- [ ] Validation passes from the plugin root.

## Phase 5: Smoke Testing and Installation

### Task 10: Create Throwaway Smoke Fixtures

Description: Add tiny fixture scenarios for each entry skill so we can test behavior without risking real projects.

Acceptance criteria:

- [ ] Fixture instructions exist for spec, plan, build, test, review, simplify, and ship.
- [ ] Smoke tests document expected evidence.

Verification:

- [ ] Manual smoke run checklist completed.

Files likely touched:

- `docs/SMOKE_TESTS.md`
- `fixtures/*`

Estimated scope: M

### Task 11: Decide Local Installation Path

Description: Decide whether to add this plugin to `~/.agents/plugins/marketplace.json` or keep it as a manually referenced local plugin.

Acceptance criteria:

- [ ] Installation path is documented.
- [ ] No marketplace entry is added without explicit approval.

Verification:

- [ ] Manual install or discovery check.

Files likely touched:

- `docs/INSTALL.md`
- Maybe `~/.agents/plugins/marketplace.json` only with explicit approval

Estimated scope: S

### Final Checkpoint

- [ ] Validators pass.
- [ ] Smoke checklist passes.
- [ ] The seven entry skills are ready for real project use.
- [ ] Remaining open questions are documented.

## Risks and Mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Entry skills become bloated duplicates | High | Enforce size limit and graph validator |
| Codex invocation differs from Claude slash commands | High | Make entry skill names simple and document prompt examples |
| `ship` assumes unauthorized subagent fan-out | High | Codex-specific `ship` contract with explicit authorization rules |
| Upstream content drifts | Medium | Record source commit and add source notes |
| Validation gives false confidence | Medium | Pair scripts with manual smoke tests |
| Plugin depends on this machine's global skills | High | Vendor/adapt required skills into plugin |

## Open Questions

- Do we want this as a private plugin only, or eventually publishable?
- Should the first build copy from local installed skills or clone the upstream repo at a pinned commit?
- Should the seven entry skills use short names only (`spec`) or namespaced aliases as well (`agent-spec`) to avoid conflicts?

