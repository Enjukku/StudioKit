---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J026 step 3 (game transcripts in ~/.claude/projects, read 2026-10-24)
supersedes: []
---
> Author: orchestrator (side session) · claude-opus-5-5 · default · 2026-10-24

# J026 measured: do the agents read their role, books and the Roblox docs?

Transcripts are data. Scripts: `scripts/` (run with `python <script>`; paths inside point at `~/.claude/projects`). "Opened docs" = a tool call or tool result names `roblox-creator-docs` or `_api-reference` (a `cd` or shell variable hides the path, so pass 1 undercounted; pass 3 counts both). Sibling study (routing, not repeated here): side-session note `routing-failure-proposal.md`.

## M1. GreatWallSim subagents (older kit; 2026-10-16 to 2026-10-24; `scripts/pass3.py`, `claims2.py`)

285 subagent runs: 244 kit roles, 29 `general-purpose`, 12 built-in `Explore` (no role file, no preloaded book).

| Measure | Count | Rate |
| --- | --- | --- |
| Opened the Roblox docs mirror | 114 / 285 | 40 % |
| Ran the context packet (`context_packet.py`) | 26 / 285 | 9 % |
| Opened `docs-map.md` | 3 / 285 | 1 % |
| Opened a skill `references/` file | 26 / 285 | 9 % |
| Read `rules/company.md` / `rules/messages.md` (role file "Read first" step 1) | 2 / 5 of 285 | ≤ 2 % |
| Used the Studio MCP `rbx-docs-search` skill | 0 / 285 | 0 % |
| Lead's brief names docs pages or the docs map | 43 / 285 | 15 % |
| Hand-back has a `docs_read` field (284 hand-backs, all via the SubagentHandback tool) | 77 / 284 | 27 % |
| `docs_read` pages with a trace of opening in the same run | 229 / 234 pages (3 hand-backs miss 5 class pages) | 98 % |

**The brief decides docs use.** Kit roles with a brief that touches the engine (Luau, Studio, engine classes): 184.

| Brief | Opened docs |
| --- | --- |
| Names docs pages or the docs map | **40 / 41 (98 %)** |
| Says nothing about docs | **60 / 143 (42 %)** |

Per role (runs: opened docs): reviewer 66: 35 · art-director 51: 5 · feature-builder 36: 30 · animator 16: 13 · game-designer 15: 2 · vfx-designer 12: 3 · architect 10: 7 · sound-designer 9: 2 · film-director 9: 4 · general-purpose 29: 5 · Explore 12: 0. Design and review roles that judge images may not need docs on every run; the counts do not say which runs needed them.

Claims are honest: when a hand-back lists docs, the agent opened them. The failure is missing reads and missing `docs_read`, not false claims.

## M2. Reverse role sessions (current kit; `scripts/rev.py`)

The lead ran each craft as a side session in a worktree, not as a kit subagent. Each brief says "Work as the studio's `<role>` role (read `.claude/agents/<role>.md`; load `<skills>`)".

| Measure | Result |
| --- | --- |
| Sessions | 12 (build-skeleton, core-loop, fidelity, onboarding, perf-200k, review, saves, ui, ui-build, upload, world, quirky-tereshkova) |
| Role line position in the brief | char 1,413-2,944 of 3,266-4,667 (41-64 %), after the context paragraphs |
| Read the role file | 12 / 12 |
| Loaded every skill the brief named (Skill tool or SKILL.md read), of 9 sessions with a parseable list | 2 all (onboarding, world) · 1 part (core-loop: 2 of 4) · **5 none** (build-skeleton, fidelity `game-design`, review `code-review` + `networking-security` + `data-saving` + `performance`, saves, quirky-tereshkova `modeling-*`) |
| Ran the context packet | 0 / 12 |
| Brief names docs | 2 / 12 |
| Opened docs | 9 / 12 (ui 424 calls: 0; fidelity: 0; quirky-tereshkova: 0) |

In a side session the role file arrives as a tool result in the middle of a long context, the role's `model`, `tools` and `skills:` frontmatter do not apply, and the books load only if the agent chooses to load them.

## M3. What a spawned kit role sees at start (probe, StudioKit, 2026-10-24)

Probe: one `feature-builder` subagent (Sonnet, low) listed its own start context without tools. Docs facts: `research-loading.md`.

| # | Item | Seen | Where (probe's account; research-loading §3 for the docs) |
| --- | --- | --- | --- |
| 1 | Role body ("You are the studio's feature builder") | yes | system prompt, first |
| 2 | Role memory index (MEMORY.md) + memory instructions; Studio MCP tool list | yes | system prompt |
| 3 | `CLAUDE.md` → `AGENTS.md` + `rules/assistants/claude.md` | yes | one system-reminder in the user turn; the docs rule is `AGENTS.md:22` of 77 |
| 4 | Git status, user auto-memory index, attribution, user email | yes | system-reminders |
| 5 | The delegation prompt (brief) | yes | user turn |
| 6 | Preloaded skill bodies (`engineering-craft`, `testing`) | yes | user-turn messages |
| 7 | SubagentStart hook text | yes | user turn; its docs line is only "Docs map row: `knowledge/reference/roblox/docs-map.md` L17" |
| 8 | Skill listing (incl. Studio MCP skills `rbx-docs-search`, `rbx-debug`) | yes | Skill tool description |

Kit text at start, per role (`scripts/startsize.py`, characters / 3.8, tool definitions not counted): always-loaded 4,454 tokens; role body 669-4,749; preloaded skills 0-20,559; memory 0-1,067; **total 5,123 (explore) to 29,635 (vfx-designer)**. Probe run total: 71,546 tokens for 1 tool call (tool definitions included).

## M4. Where the docs instruction sits

| Place | Docs instruction | Evidence |
| --- | --- | --- |
| `AGENTS.md` §0 | yes, line 22 of 77, one bullet among 9 in §0 | `AGENTS.md:22` |
| Role files (system prompt, read first) | **19 of 25 never mention the docs**; 6 mention them at line 14-23 | `scripts/startsize.py` column "docs-rule line" |
| Preloaded design books | `art-direction`, `ui-design`, `game-design`, `vfx-design`: 0 mentions; `engineering-craft`: step 2 (`SKILL.md:31`); `environment-design`: line 6 | grep 2026-10-24 |
| SubagentStart hook | a line number into `docs-map.md`, not the pages; prints nothing when the game has no `knowledge/jobs/active.md` (GreatWallSim main: no `knowledge/jobs/`; worktrees: yes) | `tools/hooks/subagent_context.py:52`, `:90`; hand run in GreatWallSim printed nothing |
| Lead's brief | rule exists: `orchestration` `SKILL.md:99` "Every brief names the Roblox docs" | met by 15 % (M1) and 17 % (M2) of briefs |
| Hand-back check | `handback_check.py` is not enabled in settings (game and kit list only SubagentStart and SessionStart), and its docstring skips hand-backs sent through a tool, which is how 284 / 285 hand-backs arrive | `tools/hooks/handback_check.py:8-9`; `.claude/settings.json` |

## Limits

- GreatWallSim ran an older kit; Reverse runs the current kit but has 12 role sessions, a small sample.
- "Engine-touching brief" is a keyword test (Luau, Studio, engine class names), not a judgment of need.
- Hook text never shows in the saved subagent transcripts (0 / 285), so M1 cannot tell whether the hook fired there; the probe shows it reaches the model in StudioKit.
- Token counts are estimates (characters / 3.8), not `/context` readings.
