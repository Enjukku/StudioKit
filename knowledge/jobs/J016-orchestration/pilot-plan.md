---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016 G3; design.md §12 (owner approval J016-D4); P2:402-422; P1:440-450
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J016 G3: audit, rehearsal and pilot

## 1. The three parts
| Part | Question it answers | Who | Status |
| --- | --- | --- | --- |
| Quality audit | Do the written files implement the approved design, without contradictions, gaps or broken references? | 5 independent Opus reviewers, read-only (crew.md J016-A1..A5); the lead verifies each finding, the maker fixes | done: 57 blocking found, fixed by 4 makers, rechecked (§4) |
| Rehearsal | Do the mechanisms the rules rely on work on Claude Code 2.1.306 with the real role files? | lead + real role files on Haiku (mechanics only, not craft quality) | done (§2); one gap needs the owner (R2a) |
| Pilot | Does the new design make a better cutscene than the old process and one strong agent, at what cost? | owner + three runs of one short cutscene | needs the owner's go (§3) |

## 2. Rehearsal results (scratch files: the lead's scratchpad `rehearsal/`)
| # | Mechanism | Result | Evidence | Consequence |
| --- | --- | --- | --- | --- |
| R1 | Two direction leads write first proposals in parallel, independently | PASS | vfx-designer and sound-designer ran at the same time; neither opened the other's file; both hand-backs start with STATUS, list coverage and built_on | — |
| R2a | Sideways direct message by agent id | **FAIL for 14 roles** | sound-designer: "the SendMessage tool is not in my available tools". Its role file allowlist is `Read, Grep, Glob, Write, Edit, Bash, WebFetch, Agent`. 14 of 24 roles have an allowlist without SendMessage (analyst, art-director, doc-keeper, explore, game-designer, live-ops-designer, marketing, progression-designer, researcher, reviewer, sound-designer, studio-operator, trend-scout, vfx-designer); the 10 roles with all tools have it | `rules/company.md` §5 and the role files promise direct messages these roles cannot send. Fix needs the owner (tool lists are agent permissions; the lead's edit was refused as self-modification) |
| R2b | Exchange through files instead | PASS | each designer wrote an exchange note with only the production conflict (rapid pickups: 80 ms sound floor vs 2 flashes per second); the VFX designer answered it | Files work for every role today |
| R3 | Review rejects the work: reviewer opens the artifact first, writes §6 findings, never edits | PASS | art-director opened the proposal before the exchange notes; 2 blocking + 1 recommendation, each with line evidence, a keep list and verdict fix-first; nothing edited. F2 ("3-4 % of screen" is not a size) over-read the acceptance check | A cheap reviewer is fine for format checks but over-reads; it never certifies quality (`orchestration` §11) |
| R4 | Repair by resuming the maker with the finding file and the protected list; selective recheck | PASS | the VFX designer wrote rev2 fixing F1-F3; all 3 protected values unchanged (lead diffed rev1/rev2); the reviewer, resumed, rechecked only F1-F3 and the keep list: verdict ready for the next review. The maker did not dispute the weak F2; it added PROPOSAL sizes instead | Repairs keep correct work when the protected list travels with them |
| R5 | Resume a finished agent, keeping its context | PASS | the VFX designer, resumed by message, recalled its peak time 0.06 s and its non-negotiable from memory, both matching its file (C11 fix in 2.1.304) | Repairs by resume keep the maker's context |
| R6 | Resume an agent after the lead's session was compacted | PASS | a probe agent started before compaction recalled its earlier mid-task message and the step it arrived at | Crew ids in crew.md stay usable after compaction; a resume resends the agent's whole context (105 k tokens for this small probe) |

## 3. Pilot: one short cutscene, three ways (owner's go needed)
| | A: today's process | B: one strong agent | C: the new design |
| --- | --- | --- | --- |
| Who | a lead chat with the game's current rules and old orchestration skill | one Opus agent (film-director role) with the same skills, books and references, no crew | `/job-cutscene` stages with kit 0.6.0: direction → G1 → (proof → G2 if L) → build → G3 |
| Where | its own copy of the place and its own branch | same | same |

Same for all three: the owner's brief (words), the game's art bible and assets, reference images, models (Opus), budget limits. Runs go one after another, so one Studio writer at a time.

**Measures** (both papers): the owner's blind rating of the three final captures (labels X, Y, Z; the key stays sealed until the rating is done), first-pass acceptance at G3, defects the owner finds after internal review, repairs that broke correct work, usage in tokens, wall time, owner minutes spent.

**What the owner picks before the pilot**
1. The game and the cutscene: short (≤ 10 s), with VFX, sound, a character moment and a camera move, so the crafts must cooperate. Candidates: GreatWallSim `B-GYMUNLOCK` (5.3 s, `knowledge/design/cutscenes.md`) or `B-FLOOD` (8 s); note that a GreatWallSim session is building the cutscene runtime on `claude/cutscene-runtime` (work-board.md:33), so the pilot must not touch that branch.
2. Three arms or two: A costs as much as C and measures a process that 0.6.0 replaces; B and C alone still answer "is the crew worth its cost?".
3. The explicit go to run `/job-cutscene` (the Workflow tool runs only when the owner asks).

**Before the first run:** kit 0.6.0 pulled into the game on a pilot branch (`kit-sync`, owner approves); Studio open with the pilot place and its `studio_id`; the owner's decision on the role tool lists (R2a); hooks 1-2 from `tools/hooks/README.md` (optional, recommended).

## 4. Audit results (kit 0.6.0 at 322c8ad → 0.6.1)
| Lane (review files in `reviews/`) | Blocking found | After fixes (recheck at 763a11e) | New from the fixes | Now |
| --- | --- | --- | --- | --- |
| A core rules and playbook | 8 | 7 closed; F08 waits on the owner (tool lists) | 1 blocking + 3 small (lead fixed) | owner decision only |
| B seven workflows | 16 | 15 closed; F11 open in 3 workflows | 1 blocking + 2 small | fixed in repair round 1 (34 tests) |
| C roles and templates | 13 | 13 closed | 1 blocking + 4 small (lead fixed) | closed |
| D context system | 7 | 6 closed; B4 (retrieval drop) open | 2 small | fixed: 16/19 on the original cases, as before J016 (90 tests) |
| E tabletop (3 requests to G3) | 13 | 12 closed; TT-01 narrowed | 3 blocking | fixed (`held_out: true`, split-job owner, image stops) |

Gate after the fixes: PASS, 641 tests. The repair-round fixes were checked by tests and by the lead; a final targeted recheck runs before the commit is reported.

**Usage (G3 so far, as the app reports subagent tokens):** audits 1.53 M · rehearsal and docs check 0.58 M · fixes 2.82 M · rechecks 1.98 M · lead about 0.4 M · total about **7.3 M tokens**. Resuming a large reviewer for a recheck resends its whole context (0.3-0.54 M each).

## 5. Owner decisions before the pilot
1. **Role tool lists (R2a, C22):** add `SendMessage` to the 11 working roles that lack it (analyst, art-director, game-designer, live-ops-designer, marketing, progression-designer, reviewer, sound-designer, studio-operator, trend-scout, vfx-designer). Recommendation: yes. Today they work through exchange notes, which is slower but safe. The docs say the same tool can also message other Claude sessions on this machine.
2. **Browser for image roles:** add the built-in browser tools to art-director, vfx-designer and marketing, so they can make images themselves. Recommendation: not yet. The lead runs image batches between stages with your yes per batch, which keeps your download rule.
3. **The pilot:** the game and cutscene, two or three arms, and the explicit go to run `/job-cutscene` (§3).
