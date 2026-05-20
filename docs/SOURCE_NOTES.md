# Source Notes

## Upstream Source

This plugin adapts the lifecycle-command pattern from Addy Osmani's `agent-skills` repository:

- Repository: https://github.com/addyosmani/agent-skills
- Pinned upstream commit inspected for this build: `f17c6e88c904dc747381c374312c2d58e10647ae`
- Upstream license: MIT, copied to `docs/UPSTREAM_LICENSE_agent-skills_MIT.txt`

## Vendored Content

The 23 underlying workflow skills were copied from the locally installed `/Users/sai/.agents/skills` versions that correspond to the Addy-style skill pack already available in this Codex environment.

The following support material was copied from upstream commit `f17c6e88c904dc747381c374312c2d58e10647ae`:

- `agents/`
- `references/`

## Codex-Specific Adaptation

Codex does not expose the same `.claude/commands/*.md` command primitive through the local plugin manifest. This plugin therefore implements the seven lifecycle commands as thin Codex entry skills:

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

