# Knowledge rules — the context system

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20; revised in J016 (owner approval J016-D4, 2026-10-21): five layers with writers, role- and job-aware routing, withheld context, revision-pinned hand-offs, filing jobs into the vault, cause-based learning. Kit file: universal. Evidence: `knowledge/reference/studio/context-research-2026-10.md`; `knowledge/jobs/J016-orchestration/design-context.md` (E1-E28) and `capability-check.md` (C17-C21).

Results depend on context. These rules keep context **correct, small and findable** for every agent, keep it **moving** between agents without loss, and make it **grow** with every job.

## 1. One source of truth, five layers
Everything the studio knows is plain markdown or data files **in this repository**. A conversation is never a source of truth; a transcript is not a memory system.

| Layer | Holds | Writer (one per file) | Read by |
| --- | --- | --- | --- |
| L0 Always | `AGENTS.md` + harness profile (+ `CLAUDE.md` imports), ≤ 200 lines | lead, owner-approved | every agent, automatically |
| L1 Kit books | `rules/`, `.agents/skills/`, `.agents/roles/`, job recipes in `.agents/workflows/jobs/`, `templates/` | lead via `/improve` or `/build-agent`, owner-approved | by role and skill |
| L2 Game vault | `knowledge/design/` (game profile, decisions, open questions, tried-and-failed, taste log, art bible, precedents, vocabulary), `knowledge/systems/`, asset catalogs, `knowledge/overlays/`, `knowledge/lessons/` | owner's words via the lead (decisions, taste); art-director (art bible); doc-keeper at job close (precedents, vocabulary, systems, catalogs); `/integrate` (overlays); `/improve` (lessons) | packet + brief `refs` |
| L3 Job folder | `knowledge/jobs/<job-id>/`: job card, direction sheet, contract, decisions, dependency map, `crew.md`, `exchange/`, `reviews/`, `evidence.md`, `ledger.md` | lead (card, crew, ledger, decisions); job lead (direction, contract, dependency map); makers (own outputs); reviewers (own review files) | the job's crew; filed into L2 at close |
| L4 Agent memory | `.claude/agent-memory/<role>/`: **craft** lessons only (how to do the job better) | that role; `/improve` merges | that role (first 200 lines / 25 KB of MEMORY.md) |

- A fact lives in one layer; others link to it. Game facts never go into agent memory.
- Parallel instances of one role share its memory folder: write dated topic files and keep MEMORY.md an index.
- Universal lessons rise from L2 to L1 only through `/improve` and `/kit-sync`, owner-approved.

## 2. Load by cost
| Layer | Loaded | Size rule |
| --- | --- | --- |
| Always | every session and subagent (Explore and Plan skip it) | ≤ 200 lines total, human- or lead-written |
| Index | when a task starts | one routing level: `knowledge/index.md` → area index → note |
| Packet | start of every task | `python tools/context_packet.py packet "<task>" --role <role> --job <job-id>`, ~8K tokens |
| Skills | preloaded by the role file, or when the craft is needed | SKILL.md ≤ 500 lines; its steps and rules in the first 5,000 tokens (that is what survives compaction); detail in references; **description ≤ 400 characters, "Use when" first** (the skill list has a budget and drops the least-used descriptions) |
| Path rules | `.claude/rules/*.md` with `paths:` load when matching files are touched | only area-specific rules |
| Agent memory | when that role starts | first 200 lines / 25 KB |
| Reference | on lookup | agent-ready cards for big docs; raw mirror for exact lookup. Roblox mirror: the packet's docs section, then grep; refresh with `python tools/sync_roblox_docs.py`, then update `knowledge/reference/roblox/whats-new.md` |

## 3. Routing: how every agent reaches its context
**Load order** (the same for every agent and task):
1. L0 loads by itself.
2. The role file and its preloaded `skills:` load by themselves; "Read first" names the rest of its book, opened through each skill's "Read this file when" table.
3. **The brief** (`rules/messages.md` §2): `owner_words`, intent, `refs` with take/avoid notes, `inputs@rev`, every rule, checks. The briefer decides what is needed.
4. **The packet for this role and job.** `--role` adds the role's skills, overlays and Roblox docs-map rows and ranks notes tagged with the role (optional frontmatter `roles: [<role>, ...]`) higher; `--job` lists the job's canonical files with their revisions and ranks notes in that folder higher. The packet seeds; the brief decides.
5. Open only what the packet and the brief cite. Nothing fits, or a Roblox system is new to you → the `explore` scout or the `researcher` (`AGENTS.md` §0).
6. The role's own memory loads by itself.

A `SubagentStart` hook (`tools/hooks/subagent_context.py`, enabled by the owner in settings) adds the active job pointer for kit roles at start and on resume; the job list is `knowledge/jobs/active.md`, kept current by the lead.

**Context withheld on purpose:**
| Step | Not given | Why |
| --- | --- | --- |
| Direction proposals | other leads' proposals | independent first ideas (messages from others flipped 11.1 % of correct answers) |
| Any review | the maker's hand-back before the reviewer's own first look | judge the artifact, not the story |
| Creative review | the agent instance that made the work | correlated errors |
| Every craft step | the whole job history and other crafts' working files | more shared context raised completion but lowered robustness to wrong context |
| Evaluations | held-out keys (`hidden-*`, never opened or listed by content) | honest scores |
| Every game | other games' facts (`scope: game`) | no leaks between games |

## 4. Passing context between agents
- **Files carry content; messages carry pointers and news** (`rules/messages.md`). Every input is named with its revision; every hand-back names `built_on`; a contract change names its consumers and marks old outputs stale.
- **The owner's words travel verbatim**: job card first, then `owner_words` in briefs that touch taste.
- **No chain of summaries** is ever the source of truth: each receiver re-reads the files at the named revision.
- **Across time:** a long chat that is compacted, a resumed agent and the next workflow stage read state from the job folder, never from memory. A `SessionStart` hook with the `compact` matcher (`tools/hooks/compact_context.py`, owner-enabled) gives the lead its job state back after compaction; then re-load the `orchestration` skill.

## 5. Notes
Every note is **one topic** and starts with typed frontmatter, then the author line:
```yaml
---
type: decision | lesson | failed | system | job | reference | log | index | profile | overlay
scope: universal | game
status: draft | active | superseded
updated: 2026-10-20          # absolute dates only
source: J07 | session 2026-10-20 | url
supersedes: []               # paths of notes this one replaces
roles: [film-director]       # optional: roles that need this note (ranks it higher in their packet)
---
> Author: <role> · <model id> · <effort> · <date>
```
- **scope: universal** = true for any Roblox game made with the kit; candidate for `/kit-sync`. **scope: game** = this game only. Never mix scopes in one note.
- **Superseded, not deleted.** Set `status: superseded` and link the replacement; the packet skips superseded notes.
- **Revisions:** contracts, direction sheets and other files that others build on carry `revision:` in their frontmatter (or a `> Revision: n` line) and a change table.
- **Links:** `[[folder/name]]` for related notes. A link never replaces putting the fact in the note that needs it.
- **Dense for AI readers:** tables, fixed keys, `file:line`, numbers with units and sources.

## 6. Where things go
| Kind | Path | Type |
| --- | --- | --- |
| Owner decisions (closed doors, each with a revisit trigger) | `knowledge/design/decisions.md` | decision |
| Open questions | `knowledge/design/open-questions.md` | — |
| Rejected approaches, each with a retry condition | `knowledge/design/tried-and-failed.md` | failed |
| What the game is | `knowledge/design/game-profile.md` + design notes | profile |
| Owner corrections, word for word | `knowledge/design/taste-log.md` | profile |
| Accepted examples per craft ("this is our game") | `knowledge/design/precedents.md` | reference |
| One name per thing: states, events, cues, assets | `knowledge/design/vocabulary.md` | reference |
| Finished systems | `knowledge/systems/<system>.md` (contract card first) | system |
| Jobs; the list of open jobs | `knowledge/jobs/<job-id>/`; `knowledge/jobs/active.md` | job; index |
| Lesson drafts | `knowledge/inbox/YYYY-MM-DD-<job>-<agent>.md` | lesson (draft) |
| Accepted lessons | `knowledge/lessons/<area>/<slug>.md` | lesson (active) |
| Game overlays for kit skills and roles | `knowledge/overlays/<name>.md` (made by `/integrate`) | overlay |
| Session logs | `knowledge/logs/YYYY-MM-DD-<topic>.md` (≤ 40 lines) | log |
| Research and references | `knowledge/reference/<area>/` | reference |
| Generated maps and indexes | `knowledge/generated/` (tool-owned, never hand-edited) | index |

The design files ship as empty starters in `knowledge/design/`; every game fills its own.

## 7. Filing a job into the vault (every job close)
The lead gives a doc-keeper the list and checks the result (`orchestration` skill §9): decisions with revisit triggers · accepted artifacts into precedents · new names into vocabulary · finished systems · rejected options with retry conditions · owner corrections into the taste log · new reusable assets into their catalog · job metrics into `evidence.md`. Then `/integrate` turns new decisions, taste and precedents into "for this game" overlays. A new agent joins the project by reading what earlier jobs filed.

## 8. The learning loop
1. **Capture (every job, cheap):** at a gate answer or job end, each agent writes a lesson draft (`knowledge/inbox/README.md`): what worked, what failed, **the owner's corrections word for word**, and two typed fields: `cause` (context missed · context missing · brief gap · interface conflict · craft error · tool failure · review broke correct work · defect found by the owner after internal review · owner taste change · win) and `layer` (the file or skill step that should change). The job's `evidence.md` keeps each defect with its cause and the job metrics.
2. **Consolidate (weekly `/improve`):** group by cause; send each to its layer (the routing table in `.agents/workflows/improve.md` step 2); merge duplicates; supersede; prune. **Promote** a lesson into a skill step, rule, recipe, precedent or overlay only when it happened twice or the owner stated or confirmed it; every promotion links its evidence; the owner reviews the change summary.
3. **Test:** retrieval cases (`knowledge/evals/retrieval.jsonl`) get a new case for every "context missed"; a defect the owner found after internal review becomes a seeded fault for reviewer evals; skill evals and the monthly agent scorecard run before and after; a change that makes them worse is reverted and gets a `tried-and-failed` row.
4. **Share:** universal lessons go to the kit with `/kit-sync`, owner-approved.
5. **After every Claude Code update:** re-run the capability probes (agent messaging, a one-stage workflow, resume) and update the capability record; behaviour changed between 2.1.296 and 2.1.306.

## 9. Retrieval and context health
- `python tools/kb_index.py` regenerates area indexes and runs the lint (frontmatter, dead links, superseded without replacement, notes over 300 lines, duplicate titles, unknown `roles:` names). Part of the gate.
- `python tools/eval_context.py` scores the packet on `knowledge/evals/retrieval.jsonl` (task → files the work really needed). Run it before and after any change to retrieval; keep a change only if the score holds.
- The gate checks always-loaded size ≤ 200 lines, SKILL.md ≤ 500 lines and skill descriptions ≤ 400 characters (`python tools/verify.py`). After description changes, `/doctor` (run by the owner) shows the skill-list cost.
