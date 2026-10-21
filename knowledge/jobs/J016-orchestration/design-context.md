---
type: job
scope: universal
status: draft
updated: 2026-10-21
source: J016 (owner request J016-D2; P1, P2, Riot transcripts, kit context research, live probes)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J016 — Context design (PROPOSAL until G1)

The owner's four questions (J016-D2): (1) how every agent reaches its correct context, (2) how context passes between agents, (3) how the vault grows so agents become part of the project over time, (4) how wins and failures are recorded so every part of context keeps improving. Keys as in `design.md`; `M-nn` = `knowledge/reference/studio/agent-messaging-research-2026-10.md`; `CX` = `knowledge/reference/studio/context-research-2026-10.md`.

## 0. The answer in five lines
1. **Five layers, one owner each:** kit books · game vault · job folder · agent memory · conversation. Only the first four are memory; a conversation never is (P1:463; P2:453).
2. **Routing:** every agent gets context in a fixed order: always-loaded rules → its role and preloaded skills → the brief → a context packet built for its **role and job** → only the cited notes. Some context is withheld on purpose (independent proposals, fresh reviewers) (CX: 2607.24882; P1:159; K1).
3. **Passing:** files carry content, messages carry pointers and awareness, every input names its revision, and the owner's words travel verbatim (P1:171, P1:286-300, P1:361; M-23).
4. **Vault growth:** every job is "filed" at close: decisions, accepted examples (precedents), names, systems, rejected options, owner corrections, new reusable assets. `/integrate` turns them into per-skill "for this game" overlays (R11 precedents; R07:602-606 shared library; kit `/integrate`).
5. **Learning:** each failure gets a cause and goes to the layer that caused it; each repeated win becomes a recipe step, a precedent or a book example; every change is tested and kept only if the numbers hold (P1:262, P1:436, P1:446; kit `/improve`).

## 1. What the evidence says about context
| # | Finding | Source | Consequence |
| --- | --- | --- | --- |
| E1 | Agents' own searches missed every needed file in 27-35 % of samples; a retrieved seed packet raised file F1 with less exploration | CX (arXiv 2607.24882) | Keep the packet at the start of every task; measure it |
| E2 | One routing level (index → note) is enough; a second level hurt | CX (arXiv 2607.17598) | No index of indexes |
| E3 | Context files did not fix weak craft; failures were skill | CX (arXiv 2607.27250) | Craft lives in books and checks, not in long notes |
| E4 | Our own docs routing: packet docs section 16/30, plus a Haiku scout 29/30 | kit lesson J010 | Packet first, scout when it finds nothing (AGENTS.md §0) |
| E5 | Fuller shared context raised completion 74.6 → 86.9 % but isolation robustness fell 97.1 → 72.4 % and tokens rose 37 %; "making information available and keeping it applicable are separate" | P1:159, P1:584 (CoMemBench) | Give each agent what its step needs, not the whole job history |
| E6 | Memory alone 17 → 36.5 %; memory plus a typed exchange protocol 62.5 % | P1:155 (MASBench) | Structure the exchange (agree / conflict / missing), not only the storage |
| E7 | Upstream messages turned 11.1 % of correct answers wrong; 94 % of harmful flips copied the upstream answer | K1 | Independent first work; reviewers see the artifact before the maker's story |
| E8 | A brief without its rules: success 76.5 % → 0 %; shortened messages lose rules first; limits do not travel down a chain by themselves | M-22, M-20, M-26 | Restate every rule in every brief; never compress briefs |
| E9 | Agents that passed only files spread no injected instruction (0 % vs 95 % with free chat) | M-23 | Content in files; messages point to them |
| E10 | A valid-looking message can silently miss content; 80 % of incomplete runs reported completion | M-09, M-31 | `coverage` lists every item; the receiver re-reads files |
| E11 | A transcript is not a memory system; a confident predecessor is not evidence | P1:463; P2:453 | No chains of summaries as the source of truth |
| E12 | The artifact is the source of truth; handoffs carry revisions, conventions, evidence, limits, next consumer; staleness is tracked | P1:286-300; P2:255-272 | Revision-pinned inputs and outputs |
| E13 | Full books exist, but each turn loads only what the step needs; lessons go into the step they fix | P1:258-262; P2:280-293 | Books split into SKILL.md + references; lessons edit steps, not a warning pile |
| E14 | Memory helps most when context is short or the task is hard; no single memory form wins | CX (EvoMemBench) | Mixed forms: ledger rows, precedents, lessons, overlays, agent memory |
| E15 | Scheduled, reviewed consolidation of memory ("dreaming") surfaces recurring mistakes and converged workflows | CX (Managed Agents, 2026-05-19) | `/improve` stays the weekly consolidation, owner-reviewed |
| E16 | Archive the accepted artifact, versions, decision log, evidence ledger, usage, defect history and owner outcome; update the book step | P1:436, P1:446 | A "file the job" step at every close |
| E17 | Agents with the same book and framing make correlated errors; role names are not independent expertise | P2:546 | Fresh contexts and separate first judgments for reviews |
| E18 | Riot keeps a style across many artists with shared rules plus **roster precedents** (named past designs) | R11:89-90, R11:108-109, R11:285-286, R11:310 | A precedent register per game |
| E19 | Riot's shared effect and sound libraries are reused first; the sound team calls sharing its "secret sauce" | R06:41-44; R07:113-118, R07:602-606 | Asset catalogs in the vault, searched before making new |
| E20 | Closed doors stay closed; a pipeline needs hand-off channels, version history, who-edits-what and naming rules | R00:840-858; R00:2499-2641 | Decision log with revisit triggers; one writer per file; naming rules |
| E21 | Calibrate "good" against top-tier reference before judging your own work | R00:4431-4447 | Books carry accepted examples, not only rules |
| E22 | Maps are reopened months later after player feedback; retrospectives list what more iteration would fix | R09:974-996, R09:1116-1142 | Decisions carry revisit triggers; jobs end with a short retrospective |
| E23 | Keep the owner's original words beside the interpreted brief | P1:361 | `owner_words` travel verbatim |
| E24 | Messaging behaviour changed between Claude Code 2.1.296 and 2.1.306 | C03 | Re-run the capability probes after every update |
| E25 | The skill list has a budget of 1 % of the context window; on overflow Claude Code drops descriptions, least-used skills first. **In this lead session, 24 of the kit's 48 skills showed only their names** (e.g. `reference-images`, `rig-pipeline`, `vfx-craft`, `preproduction`). Kit skill descriptions total 41,019 characters; role descriptions 20,158 | D skills ("drops descriptions starting with the skills you invoke least"); measured 2026-10-21 | Routing by skill description is already failing for the lead. Short descriptions, "use when" first; roles preload their skills; the packet routes, not the listing |
| E26 | A `SubagentStart` hook can inject text into a subagent "at the start of its conversation, before its first prompt", also on resume; its matcher is the role's `name`. A `SessionStart` hook with the `compact` matcher re-adds context after compaction | D hooks (v2.1.306) | Deterministic routing: every role gets its job pointer and overlay without relying on the briefer; the lead gets its job state back after compaction |
| E27 | After compaction each invoked skill keeps at most 5,000 tokens, 25,000 in total, oldest dropped first; CLAUDE.md and unscoped rules are re-read from disk | D context-window (v2.1.306) | The first 5,000 tokens of every SKILL.md hold its steps and rules; long chats re-load the skill they need |
| E28 | Agent memory folders are keyed by role name, so parallel instances of one role share one folder; no write-conflict handling is documented | D sub-agents | Agents append dated topic files; `/improve` merges MEMORY.md |

## 2. Five layers, each with one owner
| Layer | Holds | Writer (one per file) | Life | Read by |
| --- | --- | --- | --- | --- |
| L0 Always | `AGENTS.md` + harness profile (≤ 200 lines) | lead, owner-approved | kit | every agent, automatically (C05) |
| L1 Kit books | rules, skills (design + craft), roles, job recipes (workflows), templates | lead through `/improve` and `/build-agent`, owner-approved | kit, all games | by role and skill |
| L2 Game vault | game profile · decisions (closed doors, revisit triggers) · open questions · tried-and-failed · **taste log** (owner corrections word for word) · art bible · **precedents** (accepted examples per craft) · **vocabulary** (state names, event, cue and asset ids) · systems notes · **asset catalogs** (models, VFX textures, sounds, kit pieces) · overlays per skill · docs-map rows | owner's words via the lead (decisions, taste); art-director (bible); doc-keeper at job close (precedents, vocabulary, systems, catalogs); `/integrate` (overlays); `/improve` (lessons) | the game's life | packet + brief `refs` |
| L3 Job folder | job card with the owner's words · direction sheet · contract (revision) · decision log · dependency map · `crew.md` (role → agent id) · `exchange/` · `reviews/` · evidence ledger (checks, defects with causes, metrics) · ticket ledger | lead (card, crew, ledger, decisions); job lead (direction, contract, dependency map); makers (own outputs); reviewers (own review files) | the job; filed into L2 at close | the job's crew |
| L4 Agent memory | **craft** lessons of one role (how to do the job better) | that agent; `/improve` merges and prunes | across games | that role, first 200 lines (C06) |
| L5 Conversation | working thoughts | — | one session | never a source of truth (E11) |

Rules: a fact lives in one layer only; others link to it (kit `rules/knowledge.md` §1). Game facts never go into agent memory (kit role files already say so). Universal lessons rise from L2 to L1 only through `/improve` and `/kit-sync`, owner-approved.

## 3. Question 1: how each agent reaches its correct context
**Load order** (the same for every agent, every task):
1. L0 rules load by themselves (C05).
2. The role file and its preloaded skills load by themselves (role frontmatter `skills:`, C06). The role file's "Read first" names the rest of its book, opened through each skill's "Read this file when" table (E13).
3. **The brief** (`rules/messages.md` format): the owner's words, intent, `refs` with take/avoid notes, `inputs` with revisions, every rule, checks. The briefer decides what is needed; nobody else's conversation is assumed (C05; E8).
4. **The context packet for this role and job:** `python tools/context_packet.py packet "<task>" --role <role> --job <job-id>` (two new flags). It adds the job's canonical files at their current revision, the role's overlay, the role's docs-map rows and top docs pages, matching decisions, tried-and-failed rows, precedents and lessons tagged with that role (optional new frontmatter key `roles:`). The packet seeds; the brief decides (E1, E4).
5. Open only what the packet and the brief cite. Nothing fits, or a Roblox system is new to the agent → the `explore` scout or the `researcher` (AGENTS.md §0; E4).
6. The agent's own memory loads by itself (first 200 lines) (C06).

**Context that is withheld on purpose** (E5, E7, E17):
| Step | Not given | Why |
| --- | --- | --- |
| Direction proposals (D1) | the other leads' proposals | independent first ideas; 11.1 % of correct answers flipped by upstream messages |
| Any review | the maker's hand-back narrative before the reviewer's own first pass | the reviewer judges the artifact, not the story |
| Review of creative work | the maker's own agent instance | correlated errors; a fresh context |
| Every craft step | the whole job history and other crafts' working files | completion rose with more context, but robustness to wrong context fell |
| Evaluations | held-out test keys (`hidden-*`) | kit lesson J003 |
| Every game | other games' facts (`scope: game`) | kit `rules/knowledge.md` §3 |

**How we know routing works:** `tools/eval_context.py` gains cases per role (task → the files the work really needed), from real misses (§6). A routing change is kept only if the score holds (kit `rules/knowledge.md` §6).

### 3b. Claude Code mechanisms that carry context (checked on 2.1.306)
| Mechanism | Use | Who sets it up |
| --- | --- | --- |
| Role frontmatter `skills:` (full skill text at start) | the role's own books always arrive | kit role files (exists) |
| **`SubagentStart` hook, matched per role** (E26) | injects a short job pointer into every subagent at start and on resume: active job id, its canonical files at current revisions, the role's overlay and docs-map rows, the withheld-context rule for that step | kit ships the script (`tools/hooks/`); **you enable it in settings** (agents never edit settings) |
| **`SessionStart` hook, `compact` matcher** (E26) | gives the lead its job state back after compaction: open jobs, gate states, open tickets, next step | same: script in the kit, you enable it |
| Compaction limits (E27) | every SKILL.md keeps its steps and rules in its first 5,000 tokens; the lead re-loads `orchestration` after compaction | kit skill rule + gate check |
| Skill list budget (E25) | descriptions ≤ 400 characters, "use when" first; the lead routes crafts through roles and the packet, not the skill list; check the result with `/doctor` | kit; lint check in `kb_index.py` |
| Path-scoped rules `.claude/rules/*.md` with `paths:` | area rules load only when matching files are touched (exists) | kit |
| Agent memory (E28) | craft lessons as dated topic files; MEMORY.md is an index; `/improve` merges | role files + `/improve` |

## 4. Question 2: how context passes between agents
| Direction | Carrier | What it must hold | Evidence |
| --- | --- | --- | --- |
| Owner → lead | job card | your words verbatim, then the interpreted brief | E23 |
| Lead → job lead → craft (down) | brief, one message | `owner_words` (when taste is involved), intent, `refs`, **`inputs: [path@rev]`**, **`protected`** (what already passed), **`consumers`** (who reads my output), every rule, checks, return | E8, E12; P2:255-272 |
| Craft ↔ craft (sideways) | exchange note file + direct message by id for awareness | agree / conflict / missing evidence, the contract revision, the decision or test needed | E6, E9; P2:151; C03 |
| Craft → asker (up) | hand-back | `STATUS`, `coverage`, evidence per check, **`built_on: [path@rev]`**, decisions made, limits | E10, E12 |
| Reviewer → maker | review file | artifact@rev, location or frame, expected vs observed, class (blocking / recommendation / new request), evidence, smallest fix | P1:226-228 |
| Contract change | new contract revision + message to each consumer | what moved, which consumers must acknowledge and recheck; older outputs marked stale, not deleted | P1:298; P2:158 |
| Across time (compaction, restarts, next stage) | the job folder | stage results and statuses written to files, so a resumed lead or the next workflow stage reads state, not memory | P1:268; E11 |
| Lead → owner | gate packet | the real artifact first, the decision, what changed since the last approval, what was checked and how | P1:359-361 |

Never: a chain of summaries as the source of truth (E11); pasted content instead of paths (M-23); a claim built on without re-reading the file (kit `rules/messages.md` §5).

## 5. Question 3: how the vault grows with the project
**At every job close, the lead "files" the job** (a Haiku or Sonnet doc-keeper writes from the lead's list; the lead checks):
| From the job | Into the vault | Why |
| --- | --- | --- |
| owner decisions | `decisions.md` rows with the owner's words and a **revisit trigger** | closed doors stay closed until the trigger fires (E20, E22) |
| accepted artifacts (a model, an effect, a cue, a shot, a screen, a place) | `precedents.md`: what it is, why it was accepted, the owner's words, path and revision | agents learn "what our game looks, sounds and moves like" from real examples (E18, E21) |
| new names (states, events, cues, assets) | `vocabulary.md` | one name per thing across crafts (kit `preproduction` readiness: shared state vocabulary) |
| finished systems | `systems/<system>.md` with a contract card | kit rule (AGENTS.md §5) |
| rejected options | `tried-and-failed.md` with a retry condition | no repeated failures |
| owner corrections | `taste-log.md`, word for word | the most valuable taste data |
| new reusable assets | the catalog of its kind (models, sounds, VFX textures, kit pieces) | reuse before making new (E19) |
| what more iteration would fix | the job's retrospective lines in the lesson draft | E22 |

**Then `/integrate`** (exists) turns new decisions, taste and precedents into short "for this game" overlays per skill and role. Over time each agent's working context for this game = kit book + overlay + precedents + vocabulary + its lessons, all surfaced by the packet for its role. That is how a new agent instance "joins" the project: it reads what earlier jobs filed, not what earlier chats said.

## 6. Question 4: how wins and failures make every part of context better
**Capture (every job, cheap):**
1. Lesson drafts (exist), now with two typed fields: `cause` and `layer` (below).
2. **Evidence ledger** per job: each check with its evidence and revision; each defect with its cause class: context missed (existed, not read) · context missing · brief gap · interface conflict · craft error · tool failure · review-induced regression · owner taste change (P1:446).
3. **Wins:** what passed first time and which step or method made it pass; owner praise word for word.
4. **Job metrics at close:** first-pass acceptance, repair rounds by cause, defects you found after internal approval, stale or lost handoffs, unsupported "done" claims, usage vs estimate, your decisions and minutes (P1:446; P2:408-418).

**Consolidate (weekly `/improve`, exists), route each cause to its layer:**
| Cause | Fix the layer | Proof the fix works |
| --- | --- | --- |
| context missed | packet ranking or a `roles:` tag; add the case to `retrieval.jsonl` | retrieval score holds or rises |
| context missing | a vault row (decision, vocabulary, precedent, catalog) | the next packet for that task shows it |
| brief gap | brief template or the recipe stage's brief | the next brief passes `rules/messages.md` §6 checks |
| interface conflict | contract template or recipe stage | fewer conflicts in the next exchange round |
| craft error | the step of that role's book that would have caught it (E13) + an eval brief | skill evals; monthly agent scorecard |
| defect found by you after internal review | a seeded fault for reviewer evals + a check in the reviewer's book | the reviewer catches the seeded fault (P2:420) |
| review broke correct work | protected-list rule; reviewer book | collateral regressions fall |
| tool failure | tool fix; `capability-check.md` | the probe passes |
| owner taste change | taste log → overlay or art bible | your next gate needs fewer changes |
| a win that repeats twice | recipe step, precedent, or a book example | first-pass acceptance holds |

Promotion rule (kit, kept): a lesson becomes a rule or skill line only when it happened twice or you stated or confirmed it; every promotion links its evidence; changes to rules, skills, roles or hooks go to your digest (kit `rules/knowledge.md` §5).
**Keep only what works:** retrieval score, skill evals, monthly agent scorecard and job metrics are compared before and after; a change that makes them worse is reverted and gets a `tried-and-failed` row (kit `/improve` step 6b).
**After every Claude Code update:** re-run the capability probes (messaging, a one-stage workflow, resume) and update `capability-check.md` (E24).

## 7. What would change in the kit (after your approval)
| File | Change |
| --- | --- |
| `rules/knowledge.md` | the five layers with writers; load order; withheld context; filing at close; cause classes; probes after updates |
| `rules/messages.md` | `owner_words`, `inputs@rev`, `protected`, `consumers`, `built_on`; exchange note and review finding formats; crew ids |
| `tools/context_packet.py` (+ tests), `tools/kb_index.py`, `tools/eval_context.py` | `--role`, `--job`; optional `roles:` frontmatter key; per-role eval cases (an engineering ticket inside this job) |
| `templates/jobs/` | `direction-sheet.md`, `crew.md`, `evidence.md` (checks, defects, metrics), `exchange-note.md`, contract header with revision and consumers; inbox draft fields `cause`, `layer` |
| `templates/design/` (new) | `precedents.md`, `vocabulary.md`, `taste-log.md` |
| `.agents/workflows/improve.md` | cause routing table, wins promotion, seeded faults, job metrics, probes after updates |
| orchestration skill | "file the job" step at close; packet with `--role --job` in every brief |
| `tools/hooks/subagent_context.py`, `tools/hooks/compact_context.py` (new, with tests) | the two hook scripts (E26); **settings entries are proposals you apply** |
| all 48 kit skill descriptions | shortened to ≤ 400 characters, "use when" first (E25); `kb_index.py` warns above the limit; SKILL.md first 5,000 tokens hold steps and rules (E27) |

## 8. Unknowns
- No study measures our own notes' effect on output quality (CX gap). The evidence ledger and metrics start that measurement.
- The best amount of shared context per step is unmeasured for Opus 5.5 (E5 used an older model). Start narrow; widen when the "context missed" count is high.
- Precedents can over-anchor style (all new work copies old work). The art bible's "allowed variation" section stays the counterweight (kit `art-direction`).
