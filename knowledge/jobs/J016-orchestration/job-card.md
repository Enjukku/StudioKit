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
| Status | working: steps 1-8 done (G1 J016-D4, G2 J016-D5). G3 part 1 done 2026-10-21: quality audit (57 blocking found, fixed, rechecked), mechanics rehearsal, kit 0.6.1 (gate PASS, 641 tests; committed, not pushed). Owner decisions J016-D6..D8: message tool for the 11 working roles, browser for the image roles, the pilot deferred to the first real cutscene job (`pilot-plan.md`). Map page: https://claude.ai/artifact/XAJRbSA5W887CBu5AtXcAa |

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
| Steps 4-7 | ~2-3 M tokens (lead writes rules and skill; workflows; role edits; gate) | |

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 design | 2026-10-21 | "I approve the flow and context design, with all recommendations on the page. Start step 4." (J016-D4; map page version 2) |
| G2 cutscene workflow | 2026-10-21 | "I approve the cutscene workflow's shape. Build the other six job workflows the same way, then continue with steps 6 and 7." (J016-D5; map page version 3) |
| G3 audit + pilot | | |
