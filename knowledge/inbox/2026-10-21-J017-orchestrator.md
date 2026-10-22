---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J017 close
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J017 lessons (agent start-up context, prompting per model)

| # | type | cause | layer | what happened | evidence link | proposed change |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | win | win | role files (`tools:` lines) | Tool definitions, not rules or skills, were most of an agent's start-up: a role with no `tools:` line loaded every connected server (70-76 k base). Naming only the servers a role uses saved 22-33 k per agent; nothing broke | `knowledge/jobs/J017-context-and-prompting/startup-cost.md` | Every new role gets a `tools:` line with only its servers; `/build-agent` checks it |
| 2 | win | win | measurement method | The agent's total tokens depend on how many steps it took (a control read 44.8 k total vs 29.8 k start-up); the first request's prompt size from the agent journal is the same for every run of a role (spread under 1.5 k) | `startup-cost.md` "After"; capability C27 | Measure start-up from the journal's first request, with two unchanged roles as controls |
| 3 | failure | tool failure | Claude Code journals | A background agent's `output_file` was empty after it finished; the journal was in the session's `subagents/` folder, and workflow agents in `subagents/workflows/<run>/` | capability C27 | Read journals from `subagents/` with a script; never open them whole |
| 4 | owner-correction | win | J017 decisions | The owner kept the second Blender server and the full Figma connector | "I think the reason why there's two on my PC is because I have two accounts, and I think I needed to connect both of them, maybe." · "those seem like they're potentially useful, just leave it." · "I approve J017 at G3 as measured. Close it and file it into the vault." | Do not propose removing these again unless start-up cost becomes a problem |
