# Source Notes

## Upstream Source

This plugin adapts the lifecycle-command pattern from Addy Osmani's `agent-skills` repository:

- Repository: https://github.com/addyosmani/agent-skills
- Pinned upstream commit inspected for this build: `f17c6e88c904dc747381c374312c2d58e10647ae`
- Upstream license: MIT, copied to `docs/UPSTREAM_LICENSE_agent-skills_MIT.txt`

It also takes methodology inspiration from Garry Tan's GStack:

- Repository: https://github.com/garrytan/gstack
- Public docs inspected: `README.md` and `docs/skills.md`
- No GStack code is vendored in this pass; the product/company layer is an original Codex-native adaptation of the sprint and specialist-role ideas.

## Vendored Content

The 23 underlying workflow skills were copied from the locally installed `/Users/sai/.agents/skills` versions that correspond to the Addy-style skill pack already available in this Codex environment.

The following support material was copied from upstream commit `f17c6e88c904dc747381c374312c2d58e10647ae`:

- `agents/`
- `references/`

## Codex-Specific Adaptation

Codex does not expose the same `.claude/commands/*.md` command primitive through the local plugin manifest. This plugin therefore implements command-like workflows as thin Codex entry skills. The original engineering spine is:

- `spec`
- `plan`
- `build`
- `test`
- `review`
- `code-simplify`
- `ship`

The underlying skills remain separate so the entry surface stays small and the detailed workflows load only when needed.

## Local Additions

The following files are original to this Codex adaptation:

- `.codex-plugin/plugin.json`
- `.agents/plugins/marketplace.json`
- `skills/spec/SKILL.md`
- `skills/plan/SKILL.md`
- `skills/build/SKILL.md`
- `skills/test/SKILL.md`
- `skills/review/SKILL.md`
- `skills/code-simplify/SKILL.md`
- `skills/ship/SKILL.md`
- `scripts/validate_plugin.py`
- `scripts/validate_skill_graph.py`
- `docs/SPEC.md`
- `docs/PLAN.md`
- `docs/COMMAND_CONTRACT.md`
- `docs/INSTALL.md`
- `docs/SMOKE_TESTS.md`
- `skills/product-discovery/SKILL.md`
- `skills/founder-review/SKILL.md`
- `skills/business-model-review/SKILL.md`
- `skills/design-plan-review/SKILL.md`
- `skills/qa/SKILL.md`
- `skills/health-check/SKILL.md`
- `skills/retro/SKILL.md`
- `skills/learn/SKILL.md`
- `skills/founder-product-critique/SKILL.md`
- `skills/business-model-evaluation/SKILL.md`
- `skills/live-qa-methodology/SKILL.md`

## Public License

This repository is public and uses the MIT license. Upstream MIT attribution for vendored Addy-style material is preserved separately.
