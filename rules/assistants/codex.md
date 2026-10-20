# Execution profile: Codex

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20

Read `AGENTS.md` and `rules/company.md` first. The main chat is the lead (orchestrator).

| Concern | Rule |
| --- | --- |
| Models | Per tier from `kit.json` (lead, craft, mechanical). Project instructions do not hot-switch a running chat's model. Pick the model when starting a chat and request it for every worker. |
| Roles | Canonical in `.agents/roles/`. `python tools/sync_harness.py` generates `.codex/agents/*.toml`. Never edit generated files. Run `--check` in the gate. |
| Skills | Canonical in `.agents/skills/*/SKILL.md`. Load the matching skill for the task. |
| Delegation | Use the Codex collaboration tools (spawn, send message, follow up, list, wait, interrupt). Give model, effort and a complete bounded brief on every spawn. |
| Capacity | Use the live tool limit. Queue independent tasks and reuse workers as slots free up. Limits and gates come from `rules/company.md` (section 6). |
| Effort | Low for locating and mechanical notes. Medium for bounded build and research. High for architecture, integration and risky code. |
| Workspace | Shared checkout with disjoint write scopes by default. Use a worktree when isolation helps. Only the lead edits shared registries. Never revert another chat's changes. |
| Context | Run `python tools/context_packet.py packet "<task>"` first and read the cited sections. |
| Workflows | `.agents/workflows/*.md` are instruction files to read on request, not registered commands. |
| Verification | Gate first (`powershell -File tools/verify.ps1`). Then Studio MCP for runtime and visual work. Label every check. |
| Reviews | Send risky economy, purchase, persistence and remote changes to a reviewer. Check evidence before integrating. |
| Branches | New branches use `codex/` unless the owner names another. |
| Records | Decisions, lesson drafts and system notes per `AGENTS.md` section 5. Commit trailers use the real role, model id and effort. |
