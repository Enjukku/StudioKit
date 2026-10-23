---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018-riot-craft
supersedes: []
---
> Author: doc-keeper · claude-sonnet-5-5 · high · 2026-10-22 (facts from the lead)

# Evidence: J018-riot-craft

## 1. Checks (per candidate revision)
A failed check stays visible until a passing run on a repaired revision supersedes it. Missing evidence is "not verified", never a pass.

| Candidate @rev | Check | Result | Evidence (file, log line, capture) | Label (gate / MCP / owner / not verified) | By | Date |
| --- | --- | --- | --- | --- | --- | --- |
| 7876e3d | gate (sync_harness --check + verify.py) | no result recorded in the commit message; the owner accepted the rebuilt agents at this revision (J018-D6) | `git log -1 7876e3d` | not verified (later gate PASS at 44eb038 and the J019 commits) | lead | 2026-10-22 |
| 44eb038 (J019 P6, last J018 G3 decision applied before close) | gate | PASS, 855 tests | commit message | gate-verified | lead | 2026-10-22 |
| per-role (17 roles + reference-images, orchestration, level-design) | reviewer pass or lead close after final repair | see `g3-packet.md` per-role Coverage lines and `reviews/` | `g3-packet.md`, `reviews/` | not owner-verified (owner accepted at G3) | lead | 2026-10-22 |

## 2. Protected list (must stay passed)
| Since @rev | What | Check that proves it |
| --- | --- | --- |
| none (kit books; no game tests) | | |

## 3. Defects
Cause (the list in `rules/knowledge.md` §8, word for word): context missed · context missing · brief gap · interface conflict · craft error · tool failure · review broke correct work · defect found by the owner after internal review · owner taste change.

| ID | Found @rev | By | Class (blocking / recommendation / new request) | Cause | Owner of the fix | Fixed @rev | Rechecked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hand-written measuring code in books (flash counter, loudness compare, rig caps) | in review rounds | adversarial reviewers, 3-4 rounds each for six roles | blocking | craft error (layer: build-agent maker brief + missing tool modes) | G3-P1/P8 in J019: measures moved to tested tools (`tools/vfx/flash_count.py`, `tools/audio/cue_check.py`, rig_audit modes, look_check modes) | J019 (G3-P1, G3-P8) | evidence: `stage2-brief-v2.md` v3 addendum, `g3-packet.md` line 228 |

## 4. Metrics at close
| Metric | Value |
| --- | --- |
| First-pass acceptance (gates passed with no change request) | G1 passed with no change request (J018-D5). G3 accepted the rebuilt agents (J018-D6) and changed proposal decisions P7, P9, P10, P11 and two details (J018-D7, J018-D8). 1 of 2 owner gates without a change request. |
| Repair rounds, by cause | Wave 1: modeler 2 repairs + lead round 3 (wf_defb0d44-38e). Wave 2: 6 roles fix-first with one measuring-recipe finding each, focused round 3-4 (wf_2fe45f27-9e5), and a final repair for vfx-designer, character-rigger, sound-designer (wf_974de974-390). Wave 3: reviewer and level-design one text-only blocker each, final repair (wf_dff63473-240). Main cause: hand-written measuring code (craft error at the maker-brief layer). Details: `crew.md`. |
| Defects the owner found after internal review | 0. The owner changed one decision on taste/process: roughs at the highest image quality, not medium (J018-D7, J009-D20). |
| Stale or lost hand-offs | 0 found |
| "Done" claims without evidence | none found; measures that could not be made exact were labelled screening aids |
| Usage: estimate vs actual (tokens) | Estimate 11.8 M (10-15 M, no limit by J018-D4). Actual 45.99 M in subagents for J018 (`job-card.md` Budget table). Why: 20 rebuild targets not 17, Opus high for every maker and reviewer, review loops on measuring code. J019 (applying G3) is not counted here: see the J019 card. |
| Owner decisions asked | 8 (J018-D1..D8; D1 superseded by D2; D3 withdrew D2 point 5) |
| Coverage | Per role in `g3-packet.md` (example: modeler 230 tagged, 221 landed, 9 rejected) |
| Retrospective | What worked: one library (443 findings, UP-01..UP-20) and one master principles file read by every role; equal-finish options and cheap passes now in every recipe. Too big: 20 targets at Opus high in three waves; review loops on measures that belonged in tools. What more iteration would fix: run the first real game job of each type through the new recipes and file what breaks (owner: real games are the test bed, J018-D3); the follow-ups listed in the J019 card. |
| Manual step repeated 3+ times (tool proposal, PROPOSAL) | Rebuilding the per-group row lists from the `g3-proposals.md` appendix by hand (done for P4 and six P6 groups). A `g3-proposals` filter by group would remove it. |
