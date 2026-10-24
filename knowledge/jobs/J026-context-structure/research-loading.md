---
type: reference
scope: universal
status: active
updated: 2026-10-24
source: "J026 research"
supersedes: []
---

> Author: researcher · claude-sonnet-5-5 · medium · 2026-10-24

# What a custom subagent receives at start (Claude Code docs, read 2026-10-24)

Facts only; no comparison with the kit. Labels: OFFICIAL-DOC (page says it) or INFERENCE (mine). Installed version 2.1.309; newest changelog entry seen 2.1.310.
Pages: SUB = https://code.claude.com/docs/en/sub-agents; MEM = .../memory; HOOKS = .../hooks; SKILL = .../skills; CTX = .../context-window; SDK = .../agent-sdk/subagents; LOG = .../changelog.
Local: `claude --help` / `claude agents --help` NOT run (the researcher role has no shell). Hook script read: `tools/hooks/subagent_context.py`.

## 1. Known items from `knowledge/reference/studio/prompting-guide-2026-10.md` §4 (lines 168-232)

| Guide item (line) | Verdict | Today's fact | Source |
| --- | --- | --- | --- |
| Fresh isolated window, no history/invoked skills/read files (174) | CONFIRMED | "starts with a fresh, isolated context window" | SUB, "What loads at startup" |
| System prompt = body + environment details, not CC prompt (175) | CONFIRMED | "the agent's own prompt plus environment details that Claude Code appends" | SUB, same |
| Task message is part of context (176) | CONFIRMED | "the delegation prompt Claude writes" | SUB, same |
| CLAUDE.md: every level + AGENTS.md as project instructions (177) | CONFIRMED, with detail | Hierarchy "including `~/.claude/CLAUDE.md`, project rules, `CLAUDE.local.md`, managed policy files, and any `AGENTS.md`". AGENTS.md is read directly only when no CLAUDE.md exists above the working dir; otherwise via the import | SUB; MEM "AGENTS.md" table |
| Explore/Plan skip CLAUDE.md; `omitClaudeMd: true` loads only managed policy (177) | CONFIRMED, added | Managed-settings definitions get none. Subdirectory CLAUDE.md and matching path-scoped rules "still load" when the subagent works with files there. `omitClaudeMd` needs v2.1.271+ | SUB; SDK AgentDefinition |
| Git status snapshot; Explore/Plan skip (178) | CONFIRMED | Snapshot at subagent start; off when `includeGitInstructions` is off | SUB |
| `skills:` injects full content; unlisted skills invocable via Skill tool (179) | CONFIRMED, added | At most first 32 distinct names; skills with `disable-model-invocation: true` cannot be preloaded; missing skill skipped with a debug-log warning | SUB, "Preload skills into subagents" |
| Sibling roster only with SendMessage (180) | CONFIRMED | Roster is a system reminder, a snapshot at start | SUB |
| Auto memory not loaded; `memory:` field gives first 200 lines/25 KB (181) | CONFIRMED, added | Memory text sits in the subagent's system prompt; with auto memory off the field has no effect | SUB, "Enable persistent memory" |
| Output style not applied (182) | CONFIRMED | "doesn't shape its responses, except in a fork" | SUB |
| Tools inherit when omitted (183) | CONFIRMED | Omit `tools` = every tool available to subagents | SDK table |
| Context window sized by own model (184) | CONFIRMED | | SUB |
| Skill descriptions listed at start (195) | NOT FOUND for subagents | Page says this for a regular session only; subagent case not stated | SKILL, "Control who invokes a skill" |
| Path-scoped rules load on matching file read (198) | CONFIRMED for main; subagent by INFERENCE | See Q4 | MEM; SUB |
| Imports load at launch, depth 4 (199) | CONFIRMED | "maximum depth of four hops" | MEM "Import additional files" |
| CLAUDE.md is a user message after the system prompt (206) | CONFIRMED (main session) | "delivered as a user message after the system prompt" | MEM, troubleshooting |
| "No guarantee of strict compliance" (206) | CONFIRMED | same sentence | MEM |
| Reads from CC-COST cited in guide (212) | not re-read | Out of scope here | n/a |

## 2. Answers to questions 1-7

| # | Answer | Label | Source | Quote |
| --- | --- | --- | --- | --- |
| 1a | Pieces a non-fork subagent starts with: system prompt, task message, CLAUDE.md files, git status, preloaded skills, sibling roster. The page lists them in that sequence but gives no ordering of positions in the window. | OFFICIAL-DOC | SUB, "What loads at startup" | "A non-fork subagent's initial context contains" |
| 1b | System prompt = role body plus environment details; a `memory:` agent also gets memory instructions and MEMORY.md head inside the system prompt. | OFFICIAL-DOC | SUB, "Write subagent files"; "Enable persistent memory" | "The body becomes the system prompt" |
| 1c | CLAUDE.md content is a user message after the system prompt, stated for the main session. For subagents the page lists CLAUDE.md as part of initial context but does not say user or system. Likely the same mechanism. | OFFICIAL-DOC (main), INFERENCE (subagent) | MEM, troubleshooting | "delivered as a user message after the system prompt" |
| 1d | Hook `additionalContext` goes "at the start of the conversation, before the first prompt"; position relative to CLAUDE.md and skills is not stated. | OFFICIAL-DOC | HOOKS, "Add context for Claude" | "before the first prompt" |
| 1e | Preloaded skills, git status, roster: placement (system vs user turn) not stated. Roster is "a system reminder". Claude Code adds the roster "to the subagent's first turn". | OFFICIAL-DOC | SUB; SDK "What subagents inherit" | "first turn automatically" |
| 2a | `@` imports are expanded when CLAUDE.md loads ("expanded and loaded into context alongside the CLAUDE.md"), and inside AGENTS.md too. The subagent page never mentions imports; subagents get "every level of the CLAUDE.md hierarchy", so expanded imports reach them by inference. | OFFICIAL-DOC (expansion), INFERENCE (subagent) | MEM "Import additional files"; "AGENTS.md" | "subagents that start without project instructions start without these files too" |
| 2b | AGENTS.md is not delivered twice when CLAUDE.md imports it. | OFFICIAL-DOC | MEM, "Remove an earlier AGENTS.md workaround"; table row 3 | "never makes Claude read `AGENTS.md` twice" |
| 3a | A subagent can invoke non-preloaded project, user and plugin skills through the Skill tool, unless `Skill` is omitted from `tools` or listed in `disallowedTools`. | OFFICIAL-DOC | SUB, "Preload skills into subagents" | "can still discover and invoke project, user, and plugin skills" |
| 3b | Whether a subagent sees the skill description listing: not stated. | NOT FOUND | SUB, SKILL | n/a |
| 3c | Preloaded skill = "full content of any skill"; invoking a skill puts the "rendered `SKILL.md`" in as one message. `references/` files are not loaded with it; they are read on demand when SKILL.md points to them. The preload section does not mention supporting files. | OFFICIAL-DOC (SKILL.md), INFERENCE (references) | SKILL, "Skill content lifecycle", "Add supporting files"; SUB | "rendered `SKILL.md` content enters the conversation as a single message" |
| 4a | Project rules without `paths:` load at launch "with the same priority as `.claude/CLAUDE.md`"; the subagent CLAUDE.md hierarchy includes "project rules". | OFFICIAL-DOC | MEM "Set up rules"; SUB | "loaded at launch" |
| 4b | Path-scoped rules firing in an ordinary custom subagent: not stated outright. The page says Explore, Plan and `omitClaudeMd` subagents "still load" subdirectory CLAUDE.md and matching path-scoped rules when working with files there. That implies other subagents get them too. | INFERENCE | SUB, "What loads at startup" | "still load when the subagent works with files there" |
| 4c | Path-scoped rules load into message history when the trigger file is read; each has its own per-file size cap, past which only the start is delivered. | OFFICIAL-DOC | CTX; MEM, "Claude ignores the end of my subdirectory CLAUDE.md" | "load into message history" |
| 5a | Shape: `{"hookSpecificOutput":{"hookEventName":"SubagentStart","additionalContext":"..."}}`. Context only, no blocking. | OFFICIAL-DOC | HOOKS, decision control table | "No blocking or decision control" |
| 5b | Wrapper: a system reminder inserted into the conversation; any `<system-reminder>` text inside is escaped. Several hooks: all values delivered. | OFFICIAL-DOC | HOOKS, "Add context for Claude" | "wraps the string in a system reminder" |
| 5c | Cap 10,000 characters; over it the text goes to a file and the model sees the path plus a 2,000-character preview, and is not told to read it. | OFFICIAL-DOC | HOOKS | "capped at 10,000 characters" |
| 5d | Doc advice: write factual statements, not imperatives; out-of-band command phrasing "can trigger" injection defenses. Injected text is saved in the transcript and replayed on resume. | OFFICIAL-DOC | HOOKS | "Write factual statements" (paraphrase) |
| 5e | Matcher is the agent type name (custom names allowed). Event input carries `agent_id` and `agent_type`. Full SubagentStart input schema: not read (page cut off). | OFFICIAL-DOC | HOOKS; SUB | "Agent type name" |
| 5f | What the kit hook injects (facts): only when `agent_type` is a kit role and `knowledge/jobs/active.md` has open jobs, else nothing. Text: role overlays, docs-map row line numbers, precedent line numbers, vocabulary path, withheld-context line, "several jobs open" line, per active job the job file list and the `python tools/context_packet.py packet ... --job` command. Hard cap `CONTEXT_CAP = 2000` characters (`text[:2000]`), far under 10,000. | local file | `tools/hooks/subagent_context.py:32-88` | n/a |
| 6a | Length and adherence: "Longer files consume more context and reduce adherence"; target under 200 lines per CLAUDE.md; contradicting instructions "may pick one arbitrarily". Imports "don't reduce its context cost". | OFFICIAL-DOC | MEM, "Write effective instructions" | "reduce adherence" |
| 6b | Subagent-specific advice: the main conversation keeps full CLAUDE.md, so "most rules don't need to reach the subagent"; a rule that must reach it should be restated in the delegation prompt. Position effects (start vs end of a file): not stated for subagents. | OFFICIAL-DOC | SUB, "What loads at startup" | "restate it in the prompt you give Claude" |
| 6c | `omitClaudeMd`: boolean frontmatter, v2.1.271+; ignored when the agent is the main-session agent. For taking "everything they need from the delegation prompt". | OFFICIAL-DOC | SUB, frontmatter table | "Ignored when the agent runs as the main session agent" |
| 6d | `initialPrompt`: auto-submitted first user turn only when the agent is the main session agent; "Ignored when the agent is invoked as a subagent" (SDK table). | OFFICIAL-DOC | SUB; SDK AgentDefinition | "Ignored when the agent is invoked as a subagent" |
| 6e | System prompt options for a custom subagent: the markdown body (or `prompt` field) is the whole system prompt; no append option is documented for subagents. `--append-system-prompt` is a launch flag for the main session. | OFFICIAL-DOC | SUB "Write subagent files"; MEM troubleshooting | "Subagents receive only this system prompt" |
| 7 | Changelog 2.1.306 to 2.1.310: nothing on CLAUDE.md, AGENTS.md, rules, memory, `omitClaudeMd` or SubagentStart. Subagent/skill entries: 2.1.307 forks told which launch is their own, subagent fallback-model naming fix; 2.1.309 `--add-dir` skill name clash fix. Earlier gates that matter: AGENTS.md direct read 2.1.277 (reliable 2.1.281), `omitClaudeMd` 2.1.271, skill-description rebuild after compaction 2.1.304, rules `project` exclusion fix 2.1.211. Only the first 100,000 of 1.1 million changelog characters were read. | OFFICIAL-DOC | LOG; MEM; CTX | "Improved fork subagents launched together" |

## 3. Order of a subagent's start context

The docs give no position order. This list follows the SUB bullet sequence; the type column is what the docs support.

1. Role body (markdown body) plus appended environment details (working directory, platform): system-prompt. Documented.
2. For `memory:` agents: memory instructions and first 200 lines/25 KB of MEMORY.md: system-prompt. Documented ("The subagent's system prompt includes...").
3. CLAUDE.md hierarchy with expanded `@` imports (user, project, local, managed; project rules without `paths:`; AGENTS.md via the import): user-turn (documented for the main session; INFERENCE for subagents). Position relative to the task message: unknown.
4. Git status snapshot: unknown (SUB lists it, no placement).
5. Preloaded skills (`skills:` full SKILL.md each): unknown.
6. SubagentStart hook `additionalContext`: system-reminder-wrapped, "before the first prompt" (documented), so it sits ahead of the delegation prompt; its position against items 3-5 is unknown.
7. Sibling roster (only with `SendMessage` in tools): system reminder on the first turn. Documented.
8. Delegation prompt from the parent: user-turn (the first user message is the Agent tool's `prompt`, per SDK "the only content you pass from parent to subagent is the Agent tool's prompt string").
9. Later, on demand: path-scoped rules and subdirectory CLAUDE.md when a matching file is read; skills the subagent invokes through the Skill tool.

## 4. Not found

- Exact order and system/user placement of CLAUDE.md, git status and preloaded skills in a subagent.
- Whether a subagent sees the skill description listing at start.
- A subagent-specific sentence on `@` imports or on path-scoped rules firing in an ordinary custom subagent (both inferred).
- Whether a preloaded skill loads files under `references/` (docs imply no).
- Full SubagentStart input schema (hooks page fetch cut off at 100,000 of 279,543 characters); the 4,096-character style limits of the guide's §4.2 for subagents.
- Any statement that instruction position or file ordering changes adherence in subagents.
- `claude --help` and `claude agents --help` output: not run (no shell for this role).
- Tail of SUB (last 16,349 characters) and of HOOKS/LOG/SKILL not read.
