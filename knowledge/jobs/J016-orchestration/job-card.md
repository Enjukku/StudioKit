---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (orchestration redesign)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J016 — Redesign the studio's orchestration

| Field | Value |
| --- | --- |
| Job id | J016-orchestration (J006 stays reserved for the animator) |
| Size | L (the rules every agent follows, the lead's skill, 6+ saved job workflows, role files; two research papers and 14 Riot transcripts as evidence) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | **closed 2026-10-21 (J016-D9).** Kit 0.6.1. G1 J016-D4, G2 J016-D5, G3 J016-D9 after the internal audit (57 blocking found, fixed, rechecked) and owner decisions J016-D6..D8. The first real cutscene job is the pilot. Map page: https://claude.ai/artifact/XAJRbSA5W887CBu5AtXcAa |

## Goal (owner's words, 2026-10-21)
"I am the CEO and design lead. I give my decisions and what the game needs to the orchestrator (the lead)."
"The right leads agree on a job's idea and look before the crafts start."
"The crafts cooperate, because no one can do their part alone (sound needs the VFX timing, the modeler must build what the rigger and animator need)."
"Work goes back up through reviews before it reaches me, and I decide at a few clear gates."
"Every agent follows its workflow book: what great work looks like, numbered steps, reference images first for visual work, style books, its Roblox docs rows and best practices, and a self-review."
"Quality matters more than token cost in agent messages; cheaper models for mechanical work."
"Use it as strong evidence, but not as gospel; check claims that matter, especially what Claude Code can and cannot do today."

## Steps (owner's order)
| # | Step | Owner gate |
| --- | --- | --- |
| 1 | Design from the research papers and the current kit (plus the Riot transcripts) | — |
| 2 | Read the owner's `my-flow-sketch.md`, compare, judge each difference by evidence | — |
| 3 | Map + design + comparison + trade-offs to the owner | **G1: owner approves the design** |
| 4 | Rewrite `rules/company.md`, `rules/messages.md`, the `orchestration` skill | — |
| 5 | One saved workflow per job type; cutscene first | **G2: owner sees the finished cutscene workflow** |
| 6 | Role files where an agent's place in the chain changed | — |
| 7 | Gate `python tools/verify.py`; commit on PASS; no push | — |
| 8 | Plain-words report; the owner runs the quality audit and pilot | **G3: owner audit + pilot** |

## Evidence
| Key | Source |
| --- | --- |
| P1 | `C:\Users\Firew\Downloads\Studio_Orchestration_Research_2026.txt` (owner paper, 689 lines, cutoff 2026-10-21) |
| P2 | `C:\Users\Firew\Downloads\AI_Roblox_Studio_Orchestration_Research.txt` (owner paper, 673 lines, checked 2026-10-21) |
| R* | 14 Riot transcripts in `C:\Users\Firew\Downloads\` (extracts: `riot-extracts.md` in this folder) |
| CC | Claude Code docs check against code.claude.com/docs (2026-10-21) + a live messaging probe on the installed 2.1.296 (`capability-check.md`) |
| KC | Spot-check of 7 design-driving paper claims against their primary sources (`capability-check.md`) |

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Step 1-3 | ~1.5 M tokens (6 Opus transcript readers, 1 docs checker, 1 claim checker, 2 Haiku probes, lead) | reported at G1 |
| Steps 4-7 | ~2-3 M tokens (lead writes rules and skill; workflows; role edits; gate) | steps 1-8 about 5.3 M in total |
| G3 (audit, rehearsal, fixes, rechecks, probes) | not estimated | about 7.9 M |

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 design | 2026-10-21 | "I approve the flow and context design, with all recommendations on the page. Start step 4." (J016-D4; map page version 2) |
| G2 cutscene workflow | 2026-10-21 | "I approve the cutscene workflow's shape. Build the other six job workflows the same way, then continue with steps 6 and 7." (J016-D5; map page version 3) |
| G3 audit + close | 2026-10-21 | "Close J016. File it into the vault and leave the real test for the first cutscene job." (J016-D9; internal audit in `pilot-plan.md` §4) |

## Filing at close (rules/knowledge.md §7, adapted for a kit job)
| Record | Filed to | Why there |
| --- | --- | --- |
| Owner decisions D1-D9 | this folder's `decisions.md` | kit process decisions; `knowledge/design/decisions.md` is the empty game ledger every new game copies |
| Lead decisions LD1-LD16 | this folder's `decisions.md` | the lead's calls inside the approved design |
| Capability record C01-C24, K1-K7 | `knowledge/reference/studio/claude-code-capabilities.md` | the living record `/improve` updates after every Claude Code update |
| Rejected approaches | `knowledge/reference/studio/orchestration-research-2026-10.md` "Tried and rejected in J016" | kit evidence; the game's tried-and-failed file is a starter |
| Metrics | this folder's `evidence.md` | per job |
| Lessons | `knowledge/inbox/2026-10-21-J016-orchestrator.md`, `2026-10-21-J016-T01-feature-builder.md`, `2026-10-21-J016-G3-orchestrator.md` | the weekly `/improve` pass |
| Precedents, vocabulary, taste log, systems, catalogs | none | no game artifact, no taste correction; the new names live in `rules/company.md`, `rules/messages.md` and `.agents/workflows/jobs/README.md` |

## Open follow-ups (not blocking)
- The workflows still say "Studio writer" where the rules say "Studio driver" (behaviour is right).
- The UI-screen workflow takes code file owners from the direction sheet, not the architect's contract header.
- `eval_context --compare` matches cases by task text.
- In the kit repo the J016 audit reviews rank high in the lead's packets (game repos do not carry kit job folders).
- The first real cutscene job: run it on `/job-cutscene` and file its result as the J016 pilot.

**Retrospective:** more iteration would come from one real job; the internal audit found what paper review alone could not (tool lists, packet leaks, workflow seams).
