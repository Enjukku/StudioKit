# Execution profile: Codex

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20; revised by orchestrator-fixer W1 · claude-opus-5-5 · high · 2026-10-21 (J016 G3); revised by J024 writer · claude-opus-5-5 · default · 2026-10-24 (J024 design)

Read `AGENTS.md` and `rules/company.md` first. The main chat is the lead (orchestrator).

| Concern | Rule |
| --- | --- |
| Models | Per tier from `kit.json` (lead, craft, research, mechanical). Project instructions do not hot-switch a running chat's model. Pick the model when starting a chat and request it for every worker. |
| Roles | Canonical in `.agents/roles/`. `python tools/sync_harness.py` generates `.codex/agents/*.toml`. Never edit generated files. Run `--check` in the gate. |
| Skills | Canonical in `.agents/skills/*/SKILL.md`. Load the matching skill for the task. |
| Delegation | Use the Codex collaboration tools (spawn, send message, follow up, list, wait, interrupt). Give model, effort and a complete bounded brief on every spawn. |
| Capacity | Parallel workers per stage: max 5 (`rules/company.md` §9), within the live tool limit. Queue independent tasks and reuse workers as slots free up. Limits and gates come from `rules/company.md` (sections 2 and 9). |
| Effort | Low for locating and mechanical notes. Medium for bounded build and research. High for architecture, integration and risky code. |
| Workspace | Shared checkout with disjoint write scopes by default. Use a worktree when isolation helps. Only the lead edits shared registries. Never revert another chat's changes. |
| Context | Run `python tools/context_packet.py packet "<task>" --role <role> --job <job-id>` first and read the cited sections. |
| Workflows | `.agents/workflows/*.md` are instruction files to read on request, not registered commands. `.agents/workflows/jobs/*.js` are Claude Code job workflows; in Codex run the same stages by hand from the `orchestration` skill's `references/job-types.md` (its stage map says which recipe rows belong to `direction`, `build` and `repair`; there is no proof stage, J024). Sideways work between workers goes through exchange files in a fixed order (`rules/company.md` §5). |
| Hooks | None. The lead checks every hand-back itself (STATUS first line, `coverage`, `built_on`, `docs_read`) and puts the job id and packet line in every brief. |
| Verification | Gate first (`python tools/verify.py`). Then Studio MCP for runtime and visual work. Label every check. |
| Reviews | Every job whose candidate includes code gets a reviewer worker with the `code-review` skill (`rules/company.md` §7); economy, purchase, persistence and remote changes at high effort. Check evidence before integrating. |
| Branches | New branches use `codex/` unless the owner names another. |
| Records | Decisions, lesson drafts and system notes per `AGENTS.md` section 5. Commit trailers use the real role, model id and effort. |
