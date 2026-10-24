---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J026 (research-anthropic.md, research-loading.md, measured-agents.md)
supersedes: []
---
> Author: orchestrator (side session) · claude-opus-5-5 · default · 2026-10-24. Nothing in the kit is edited. Nothing is committed. The owner picks the fixes.

# J026: context structure against Anthropic's advice, and what to fix

Owner words: "they're not fully grasping their role, and then they're not properly looking at the Roblox documentation ... I want you to look at more like Anthropic employees, saying what context should look like." And: "I'm wondering if it would be better to use Obsidian".

## 1. The answer in five lines

1. The kit's context design mostly matches Anthropic's advice on paper. The failures are in how the rules reach the agent at run time.
2. **The brief decides docs use.** When the lead's brief names the docs pages, agents opened the docs in 40 of 41 engine runs (98 %). When the brief is silent, they opened them in 60 of 143 runs (42 %). Briefs named the docs in only 15 % of runs.
3. **The docs rule is buried.** It is one bullet at `AGENTS.md:22`, in a block the agent gets as a user-turn reminder. 19 of 25 role files never mention the docs. The start hook gives a line number (`docs-map.md L17`), not the pages. Agents opened `docs-map.md` in 3 of 285 runs.
4. **Roles run without their books.** In Reverse (current kit) the lead ran each craft as a side session that reads the role file. 5 of 9 sessions loaded none of the books the brief named. Example: the review session loaded none of `code-review`, `networking-security`, `data-saving`.
5. **Obsidian:** the vault already opens in Obsidian as it is. It helps you read and browse. It changes nothing for the agents.

Evidence: `measured-agents.md` (transcripts, probe), `research-anthropic.md` (Anthropic posts and staff), `research-loading.md` (Claude Code docs on what a subagent loads).

## 2. The kit against each Anthropic recommendation

Labels: OFFICIAL = Anthropic docs or engineering post. STAFF = an Anthropic employee. Row ids point into `research-anthropic.md` (A) and `research-loading.md` (L).

| # | Anthropic says | Label, id | Kit | Verdict |
| --- | --- | --- | --- | --- |
| 1 | Give the smallest set of high-signal tokens. A long CLAUDE.md makes Claude ignore real rules. The Claude Code team cut its own system prompt by about 80 % for the newest models. | OFFICIAL A1.1, A1.3, A1.15 · STAFF A1.9-1.11 | Always-loaded text is under 200 lines, 4,454 tokens, gate-checked (`rules/knowledge.md:25`). But every craft agent also loads lead-only process (`AGENTS.md` §1, gates), and the role file tells it to read more rules (`templates/role.md:19`). Agents read `rules/company.md` in 2 of 285 runs. | **Gap** |
| 2 | Emphasise only the rule that gets skipped. Restate a rule that must reach a subagent in the delegation prompt. | OFFICIAL A1.5 · L §2 | The docs rule is one bullet among 9 (`AGENTS.md:22`). It is not in 19 of 25 role files. The brief rule exists (`orchestration` `SKILL.md:99`) but 15 % of briefs met it. | **Gap** (measured) |
| 3 | Name the source in the prompt. Tell the agent to fetch it. | OFFICIAL A3.1, A3.2 | Same brief rule as row 2. Measured effect: 98 % vs 42 %. | **Gap** (measured) |
| 4 | A brief needs an objective, an output format, the tools and sources, and boundaries. Vague briefs gave duplicate work. | OFFICIAL A4.1, A4.2 | `rules/messages.md` §2 has intent, spec, `refs`, `skills`, `packet`. Docs ride inside `refs`. | **Matches** on paper; sources often missing in practice |
| 5 | Hybrid context: some data up front, the rest fetched just in time by path. | OFFICIAL A2.1, A2.2 · STAFF A2.7 | Packet up front (about 8K tokens), docs mirror on lookup (`rules/knowledge.md:27-31`). The packet ran in 26 of 285 runs, 0 of 12 Reverse sessions. | **Matches** in design; the up-front half seldom runs |
| 6 | Skills: description, then SKILL.md, then reference files one level deep; table of contents in long files. | OFFICIAL A2.3-2.6 | SKILL.md ≤ 500 lines, "Read this file when" tables, descriptions ≤ 400 characters (`rules/knowledge.md:28`). | **Matches** |
| 7 | Watch real runs. If agents never open a file, the link is weak or the file is not needed. | OFFICIAL A3.4 | Retrieval eval exists (`rules/knowledge.md:117`). Nothing checks transcripts for docs or reference reads. Skill references opened in 26 of 285 runs. | **Gap** (J026 scripts are the first check) |
| 8 | Advisory text is not a guarantee. Use hooks for what must happen. | OFFICIAL A3.6 | Start hook gives a line number and prints nothing in a game without `knowledge/jobs/active.md` (`tools/hooks/subagent_context.py:52`). The hand-back check is not enabled and skips tool hand-backs, which is how 284 of 285 hand-backs arrive (`tools/hooks/handback_check.py:8`). 207 of 284 hand-backs had no `docs_read`. | **Gap** |
| 9 | Use subagents for isolated, specialised work with their own prompt and tools. Anthropic's example role prompt is short. | OFFICIAL A5.1, A5.2 · L §1 | Kit subagents get the role as system prompt and books preloaded (probe, `measured-agents.md` M3). Reverse side sessions lose the role's model, tools and books (M2). | **Conflict** in practice |
| 10 | For a heavy corpus, a docs-lookup helper searches in its own context and returns only the answer. | STAFF A2.8 | `explore` scout and `researcher` for wide searches (`AGENTS.md:22`). | **Matches** |
| 11 | Results go to files; the lead gets references. Fresh context per task; state in files. | OFFICIAL A4.6, A6.1-6.5 | `rules/knowledge.md` §4; J022 session per stage. | **Matches** |
| 12 | Test instructions on each model you run. | OFFICIAL A1.8 | J017 per-model prompt changes. | **Matches** |
| 13 | A long role file helps role grasp. | none found (A5.4) | Role bodies 669-4,749 tokens plus 0-20,559 tokens of preloaded books. | No evidence either way. No change proposed. |

## 3. Fixes, smallest first

Base cost: a kit-role spawn starts with 5,123-29,635 tokens of kit text (`measured-agents.md` M3). None of these fixes adds an agent run, so the J024 cut (72 % fewer runs) stays.

| Rank | Fix | Files | Agent runs added | Tokens | Fixes rows |
| --- | --- | --- | --- | --- | --- |
| F1 | **Hook gives the docs pages, not a line number.** The SubagentStart hook prints the role's docs-map row (sections and key pages) and runs also when no job is active. | `tools/hooks/subagent_context.py` | 0 | +150-250 per kit-role spawn | 2, 8 |
| F2 | **One docs line at the top of each role file.** Example: "Before you design or build with an engine system, open its page in the docs mirror (your sections: `effects/`, ...). List each page in `docs_read`." `tools/sync_harness.py` writes it from the docs-map row, so one source stays true. | 25 role files via `sync_harness.py`; `templates/role.md` | 0 | +60-120 per spawn | 2 |
| F3 | **Every engine brief carries a `docs:` key, filled by a tool.** A short packet mode prints the 3-8 mirror pages for the task and role. The lead pastes them. The brief lint (`rules/messages.md` §9 list) flags engine work without `docs:`. | `tools/context_packet.py`, `rules/messages.md` §2, `orchestration` §10 | 0 | about 1-2K in the lead's context per brief; about 200 in the brief | 2, 3, 4, 5 |
| F4 | **Real hand-back check.** `handback_check.py` reads the hand-back tool call from the transcript. It sends an engine role back once when `docs_read` is missing. You enable it in settings (agents never edit settings). | `tools/hooks/handback_check.py`; your settings | 0 (one extra turn only when the field is missing) | small | 7, 8 |
| F5 | **Craft work runs with its book.** Prefer kit subagents for one-stage craft work. When a side session is needed, it starts with a generated role command (role body plus "load these books first"), not a role line at 41-64 % of the brief. | `sync_harness.py` (one command per role), `orchestration` §6 | 0 | the role body, once per session | 9 |
| F6 | **Cut what crafts never read.** Move lead-only process out of `AGENTS.md` into `orchestration` and `rules/company.md`. Drop "read `AGENTS.md`" from role files (it is already loaded). Keep the safety, docs and gate lines. | `AGENTS.md`, `templates/role.md`, role files | 0 | saves about 1-2K per spawn (estimate, not measured) | 1 |

Not proposed now: a docs-lookup subagent for every engine question (STAFF A2.8). It adds one run per lookup, against J024. The kit's `explore` and `researcher` already cover wide searches.

Possible variant of F3 (needs a probe first): if the SubagentStart hook can read the brief text, the hook can add the task's docs pages by itself. Then F3 does not depend on the lead. `research-loading.md` §4 says the docs do not state the full hook input.

**Recommendation: F1 + F2 + F3 now. F4 after one week if `docs_read` is still missing. F5 together with the routing fix from the sibling session.** F3 has the measured effect (98 % vs 42 %). F1 and F2 move the rule to where the agent reads first, at almost no cost.

Weakest part: F3 still depends on the lead. The same rule exists today (`SKILL.md:99`) and was met in 15 % of briefs. The tool and the lint make it easier and visible, not certain. F4 and the F3 variant are the deterministic backups.

Alternative: F6 first (cut the always-loaded text). Anthropic supports it (rows 1-2), but no source gives a size limit, and we have no measurement that our size causes the misses. The measured cause is the brief.

F5 overlaps the sibling session's routing proposal (side-session note `routing-failure-proposal.md`, its side finding). Pick one owner for it.

**Check after one game week:** run `scripts/pass3.py` and `scripts/claims2.py` on the new game's transcripts. Target: docs opened in engine runs ≥ 85 %, `docs_read` in ≥ 90 % of hand-backs, every named book loaded in role sessions. No rise in the lead's median context (`tools/usage_report.py`).

## 4. Obsidian

**What it is.** Obsidian is an editor and viewer for a folder of Markdown files. It does not change the files into another format.

**Does the vault open as it is?** Yes. Open the `knowledge/` folder as the vault.
- Kit links use paths from `knowledge/`, for example `[[reference/ui/05a-research-rules]]`. Obsidian resolves them the same way. The gate (`tools/kb_index.py`) checks dead links with the same rule.
- Frontmatter shows as Obsidian "Properties".
- The Obsidian installer is already in your Downloads folder (`Obsidian-1.12.7.exe`).

**What it adds for you:** a graph view, a backlinks pane, fast search, and plugins (for example Dataview, which lists notes by frontmatter fields such as `status` or `roles`). It is a good way to read and browse the studio's memory.

**What it adds for the agents: nothing.** Agents read files with Read, Grep and Glob, and with the context packet. They never see Obsidian. Only 24 of 796 notes (outside the docs mirror) use `[[links]]`. Agents follow backtick paths and `file:line`. The measured failure is where the instructions sit and what the brief names, not the file format. Anthropic's own Claude Code moved from pre-indexed retrieval to plain grep (STAFF A2.7).

**If you use it, set three things:**
1. Add `knowledge/.obsidian/` to `.gitignore`. Obsidian writes its settings there.
2. Exclude `external/` in Obsidian's "Excluded files". The docs mirror (900 Markdown and 1,209 YAML files) otherwise fills the graph and search.
3. Set "New link format" to "Absolute path in vault", so links you add match the kit format.

Risk: if you edit notes in Obsidian, keep the frontmatter keys and the author line. The gate reports a broken note.

## 5. Decision for the owner

Which fixes do you approve? Default if you do not answer: none. Nothing changes until you pick.
- **A (recommended):** F1 + F2 + F3 now, F4 after one week, F5 with the routing fix.
- **B:** F1 + F2 only (no lead change).
- **C:** A plus F6 (cut always-loaded text), with a before/after measurement.

## 6. Usage

3 agent runs (2 Sonnet researchers, 1 Sonnet probe): 84,851 + 95,625 + 71,546 = 252,022 subagent tokens. No estimate was set before the job.
