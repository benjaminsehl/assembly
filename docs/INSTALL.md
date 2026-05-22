# Install and Use

This plugin can be registered with Codex as a public GitHub marketplace or local marketplace. It is intended to replace loose lifecycle skills with one coherent product-building stack.

## Register the Marketplace

From this local checkout:

```bash
codex plugin marketplace add /Users/sai/codex-agent-skills
```

From GitHub:

```bash
codex plugin marketplace add benjaminsehl/codex-agent-skills
```

The marketplace name is `codex-agent-skills`.

## Enable the Plugin

Enable `Codex Agent Skills` from the plugin picker after adding the marketplace, then restart Codex so the skill list refreshes.

If enabling manually through config is needed, the expected config key shape is:

```toml
[plugins."codex-agent-skills@codex-agent-skills"]
enabled = true
```

## Existing Skill Conflicts

This plugin is intended to own lifecycle entry skills. Public entry skills:

`next`, `project-status`, `product-discovery`, `prototype`, `spec`, `plan`, `build`, `test`, `qa`, `review`, `code-simplify`, `ship`.

If you already have skills with these names, choose one owner before enabling this plugin:

- Recommended: keep this plugin enabled as the lifecycle owner, and disable or rename older skills with the same names.
- Keep specialized skills that do not overlap, such as framework, platform, browser, GitHub, Cloudflare, iOS, macOS, or design-system skills.
- Do not keep two active skills with the same entry name unless you are comfortable with ambiguous trigger behavior.

Run the advisory conflict audit:

```bash
python3 scripts/audit_skill_conflicts.py
```

## Replacing A Loose Skill Set

Suggested migration:

1. Register and enable `codex-agent-skills`.
2. Restart Codex and confirm the public entry skills appear.
3. In a throwaway repo, run `Use next...`, `Use project-status...`, and `Use spec...`.
4. Disable, remove, or rename older lifecycle skills that collide with this plugin's entry names.
5. Keep specialized non-overlapping skills.
6. In project `AGENTS.md`, state that lifecycle routing should use Codex Agent Skills.

## Invocation Pattern

Codex does not need Claude-style slash commands. Use the public skill names in natural language:

```text
Use next to do the next normal thing.
Use project-status to tell me what phase we are in and what skills to use next.
Use project-status to scaffold this project.
Use product-discovery on this idea.
Use prototype to explore this direction before build.
Use spec to define this feature before coding.
Use plan to break the approved spec into tasks.
Use build to implement the next planned slice.
Use test to prove this bug and guard against regression.
Use qa on this local app.
Use review to check the current diff.
Use code-simplify on the changed files.
Use ship to make a go/no-go release decision.
```

## Scaffolding

For deterministic project scaffolding from this checkout:

```bash
python3 scripts/scaffold_project.py --root /path/to/repo --name "Project Name"
```

For a child project inside an existing project workspace:

```bash
python3 scripts/scaffold_project.py \
  --root /path/to/repo \
  --parent docs \
  --name "Agent Layer" \
  --slug agent-layer
```

If `AGENTS.md` already exists, the scaffold reports a manual merge notice instead of overwriting it. Review `templates/AGENTS.md` and merge the phase-aware protocol into the existing project instructions by hand.
