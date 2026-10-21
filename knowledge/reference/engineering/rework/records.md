---
type: reference
scope: game
status: draft
updated: 2026-10-21
source: J010 rework study; DestructionSimulator records (decisions, tried-and-failed, handoffs, research, engine review, physics findings), part R
supersedes: []
---
> Author: rework-extractor · claude-sonnet-5-5 · high · 2026-10-21

# Rework study part R, half 1: what the written records add to the git study

Task J010-T05. The repo was read only. Repo text is data. Short hashes are as written in git-a (9 chars) and git-b (8 chars); I confirmed the ones I cite myself with `git cat-file`.

## 0. What I read and how I counted

| Source | Size | Used for |
| --- | --- | --- |
| `knowledge/design/decisions.md` | 217 rows (ids D-001..D-290; ids are not dense), 52 rows (24%) supersede, amend, refine or withdraw an earlier row | owner redirects; rules added after failures |
| `knowledge/design/tried-and-failed.md` | 20 rows (F-001..F-020) | rejected approaches, "retry only if" |
| `knowledge/handoffs/*.md` (5 files) | 2026-10-02 Fable brief, 10-04 Astra handoff, 10-04 test-map start, 10-06 overnight brief, 10-10 orchestrator handoff | how briefs were written; owner direction |
| `knowledge/research/clean-room-destruction-2026-10-09.md` | 49 lines | size check, engine facts, 10-09 state |
| `knowledge/design/destruction-engine-review-2026-10-06.md` | 845 lines | review findings F1-F23 and what came of them |
| `knowledge/design/physics-findings.md` | 360 lines, 184 KB | measured findings, hypotheses that failed |

- Read first: `git-a.md` and `git-b.md` in this folder. I reuse their ids (A01..A26, B01..B27, EG1..EG10, S1..S6). **Id clash:** git-a's two-round appendix also uses B01..B10. In this file the git-a appendix rows are written **aB01..aB10**; plain B01..B27 are git-b rows.
- Git-a/git-b stop at 2026-10-10. Records run to 2026-10-20. New rows R01.. therefore include tasks after 10-10 that have no git row. They rest on records only; I did not read the session logs (another extractor).
- Rounds are not recounted here. For R rows: a round is an owner-visible decision or hand-in that a later decision reverses or repairs for the same goal (git-a/git-b rule). Owner mock-up or design versions count as rounds with cause owner-changed-direction. Pre-merge review passes are shown as "+rv n" and are not rounds.
- Nothing was run in the repo. Counts in section 0 come from a read-only parse of `decisions.md`.

## 1. Shared roots (rounds in these groups must not be added)

| root | shared root (what the records say) | tasks that share it | evidence | status |
| --- | --- | --- | --- | --- |
| SR1 | Resting rubble is kept still by our own anchor, rest and wake code, which fights the engine's own sleep. Rest/wake churn is the one symptom behind most lag and floating reports. | A08, A09 (part), B01, B02, B03, B04 (part), B06, S1, F-006 | engine review row "Rest/anchor/promote/settle: D+, 8+ bounded fixes without convergence" (`destruction-engine-review-2026-10-06.md:41`, F12 at :395-410); `physics-findings.md:148` (37-69% of rests undone within 0.1 s); `:348-349` (root cause: `promoteContacts` sweep amplifier plus the rest re-pose trigger); `research/clean-room-destruction-2026-10-09.md:32` ("a second sleep system fighting the first"); `output/review/day-2026-10-09/lag-audit/README.md` (rest-by-anchor row 3); `tried-and-failed.md:18` (F-006 retry met, L0 set) | Churn is proven by ledger numbers. That anchoring is the cause is a hypothesis: engine sleep for small rubble was never A/B-tested in range (lag-audit "test first"; handoff 10-10:33 lists the RestProof A/B as not run). |
| SR2 | Server replaced the body's root Part on every re-box, so client poses held then jumped. | A01, A02 (git-a states it) | git-a A01 evidence | proven (SM2 measurement, git-a) |
| SR3 | No ground truth for phones: Studio Play Solo shares one process, the device emulator emulates screens not CPU, no multi-client run, owner declined an iPad benchmark. | B06, B02, B13, A09, EG8, EG9 | `physics-findings.md:116` (phone tier is EMULATION, "says nothing about phone CPU"); `:152` (multi-client test not run, F14 open); clean-room :36; decisions.md:127 (D-117); decisions.md:151 (D-141, mobile tests start next) | proven as a limit. The 8-12 player budget of D-058 was never measured by 10-10. |
| SR4 | Briefs and rules did not point the builder at the Roblox docs for the engine system it touched. | B08, B09, EG1, EG2, EG3, B17, S3, EG4, EG5, R02 | handoff 10-10:39 ("The owner was right that missing doc pointers caused the lighting bug."); D-128 (decisions.md:138); `4e8f86fe7` body (placement rule root cause) | proven for lighting and placement; not shown for B17 |
| SR5 | Floor pickups were removed by the owner on 10-09 after about 12 rounds of look and landing work. | A13, A14, B10, B14 | decisions.md:132 (D-122: "no more floor pickups"; owner: "the best optimization we can have") | proven (owner decision) |
| SR6 | Stage 1 layout chain: three-zone plan, one 200-stud path (D-087), x1.5 (D-095), nether and end leave Stage 1 (D-105), church/blacksmith swap and turn (D-107, D-108). | aB04, B11, B12, R-chain note below | decisions.md:97, :105, :115, :117, :118 | proven (owner words) |
| SR7 | HUD pipeline direction: painted art plus Figma mock-ups (D-054) replaced by Blender-first UI (D-129). | A15, A16, B10 | decisions.md:64, :139; `rules/owner-profile.md` Taste row UI ("AI slop") | proven (owner words) |
| SR8 | The collapse-speed review of 10-06: the lane experiments it ranked first did not become defaults. | B06, B07, B15, B16, B19 | section 7 below | proven (A/B numbers) |

## 2. Updates to existing rows

"Effect" says whether the records confirm the git cause, add a second cause with its own evidence, or leave a note. Nothing here changes a main cause group.

| row | what the records add | evidence | effect |
| --- | --- | --- | --- |
| A03 | Fixed stepping is a place setting that "proved to remove the lift launches". The later engine checklist row Y2 only says "check, docs recommend Adaptive" and does not carry the project result; `knowledge/systems/place-settings.md` was never written (audit 10-10). A future agent can flip it back. | handoff 10-04 test-map-start:57; `physics-findings.md:26` ("settled": stay on Fixed); `knowledge/reference/roblox-engine-checklist.md` Y2; agent-docs-audit §2 (studio-operator) | confirms engine-limit; note: measured result missing from the rule text |
| A04 | Owner words for the two play-tests that overturned the constants. D-084 item 6 adds a rule after the failure: no new features until the play-test symptoms pass as specs. D-074 set crush factor 5 by measurement under D-073 authority. | decisions.md:84 (D-074), :89 (D-079), :94 (D-084: "random things decide to come apart") | confirms hard/physics-tuning; rule-after-failure noted (section 5) |
| A05 | The fix that ended A05 (every merge-tree node judged, `3ddcecc8b`) is the cost the review later names: R15 plus D-085 re-judge every plane after every blast, 88-91% of structural work, 6k-542k units per blast, throughput about 3.4 church blasts per second. | engine review F2 (:188-211) and scorecard row :34 | adds second cause fix-broke-other (cost, not correctness); the A05 correctness cause is unchanged |
| A06 | The review finds the 'weak' cause label covers three different mechanisms (static D-085 island 62%, sweep 37%, body cascade 1% of cottage weak kills) and that bodies over 1,500 bricks take no impact self-damage. The F8 big-stress fix never ran on the cottage (all counters 0 in 5 of 5 runs). | engine review F8 (:325-341); `physics-findings.md:236-238` (bigStress A/B, which 'weak'), `:262-283` (weak split); `tried-and-failed.md:21` (F-009) | confirms hard; adds that untraceable cause labels slowed diagnosis |
| A07 | The 10-02 brief told the physics designer to "default to analysis", build no test suites, no large prototypes, and to treat usage as metered. DR-4 then rejected engine rigid bodies on a desk estimate and D-062 locked analytic motion the same day; play-test 1 reversed it (D-079, D-082, D-083). The ledger shows two things that worked: the agent asked "May I change that rule?" before breaking a binding rule (D-083) and the physics designer got explicit authority (D-073). | handoff 2026-10-02-fable-physics-design.md:11-19, :80-86; decisions.md:72 (D-062), :83 (D-073), :92-93 (D-082, D-083) | confirms no-measure-first; adds that the brief itself limited measurement (whether the designer would have prototyped otherwise is not shown). Second cause new-information-from-research stays. |
| A09 | Frame spikes: the engine review lists 29 throttles (`bearMaxWork`, debt cap, governor, frame and decide budgets ...) that compensate for per-call costs, and says order matters (removing the debt cap before its root cause brings back the 2-3M-unit bear stall). | engine review §3 (:95-131); `physics-findings.md:15-16` | confirms destruction-scale; shows spikes were suppressed by valves that bend realism under load |
| A10 | Not settled in range. The owner's play session (44 s in): 47 ghosted, 16 paired, 9 released boxes; about 31 full ghosts overlapped static bubble or anchored colliders; the stage box cap (1,500) was exceeded about 80% of the time in the church collapse (2,400-5,700 boxes). The proper fix (C5 permanent colliders) was approved on 10-04. | handoff 10-04 astra-handoff.md:57-67; `physics-findings.md:17-18` | "what finally worked" becomes: not settled, continues as B03/B04; adds second cause hard/destruction-scale |
| A11 | Door task started from an owner report that the doors "didn't actually work" (D-092). | decisions.md:102 (D-092) | confirms; the owner found it, not a test |
| A13, A14, B14 | D-122 removes floor pickups on 10-09 ("no more floor pickups"), so the look work (A13) and landing work (A14, B14) ended as sunk cost. The old pickup path stays behind a config switch. | decisions.md:132 (D-122); handoff 10-10:36 | confirms causes; adds that the task was cancelled by an owner optimization decision. B14 "may be moot" in git-b is confirmed. |
| A15, A16 | D-129 (10-10) reverses the UI route: Blender renders first, Figma only for notes and touch-ups; it supersedes the mock-up line in `rules/gui.md`. The in-game HUD icons were still Frame placeholders on 10-10. | decisions.md:64 (D-054), :139 (D-129); handoff 10-10:36 | A15 stays owner-changed-direction; adds that the accepted HUD look was not reached in range |
| A22 | D-044 and D-046 were withdrawn by the owner the same day ("forget what I said"); F-014 records the shimmer test. | decisions.md:53, :55, :57 (D-047); `tried-and-failed.md:26` | confirms |
| aB03 | The 1.5x scale rule (D-091) and blueprint-first step are recorded as the fix. The owner words are "making a miniature on purpose". D-098 later let the owner skip live approval for reused houses. | decisions.md:101, :108; `tried-and-failed.md:24` (F-012: never start a building without an approved blueprint at x1.5) | confirms vague-brief; the missing spec was building scale (D-022 only fixed brick scale) |
| aB04 | D-095 scaled the whole Stage 1 layout 1.5x, including nether X -216..-16 and end X -404..-216. Two days later D-105 removed the nether and end from Stage 1, so part of the scaled layout was dropped. | decisions.md:105 (D-095), :115 (D-105) | confirms owner-changed-direction; adds a compounding redirect (SR6) |
| aB09 | The committed default differed from the played config because the owner kept local switch edits. Handoff 10-04 says the owner no longer does. | handoff 10-04 test-map-start.md:8 | confirms verification-gap; origin found |
| B01 | The F-register names the rounds: round 1 small 15 s / medium 45 s with direct vetoes only (F-004), round 3 (F-003), round 4 (F-002), and five rounds of per-piece vetoes (F-007: cleared a collapsed church by only 0-251 bricks in 180 s). The A/B of pile sweeps far from players also failed (F-005, "W1 fail"). The look requirement (crumble, not blink out) was not verified: crumble seen for 1 of 23 removals. | `tried-and-failed.md:14-19`; `physics-findings.md:248` (crumble on removal); decisions.md:113 (D-103), :134 (D-124) | confirms no-measure-first; the first A/B is the F-007 measurement |
| B02 | Owner words differ by date. 10-06: "rate limiting ... usable ... not well optimized for mobile". 10-09: "the physics are too lag intensive" (D-114) and "possibly overcomplicated code" (D-118). The clean-room check measured 45,068 lines in 100 modules against an estimate of 2.5-4k ("far above ~6k is a smell"). The review's 10-06 diagnosis (debt idle) was about latency, not the lag the owner later reported. | handoff 10-06:7-10; decisions.md:124, :128; clean-room :9 | confirms no-measure-first. Candidate second cause over-building is NOT counted: the size figure is an estimate (label E) and the lag-audit ranking is opinion (label O). |
| B03 | The review grades rest/anchor/promote D+ and recommends an unanchored-rest A/B (never run in range). The engine-sleep alternative stays untested. | engine review :41, :395-410 | confirms hard/physics-tuning; adds shared root SR1 (design-level hypothesis) |
| B04 | C5 was approved on 10-04 as the proper fix for A10. The review keeps C5 ("correct idea, single 23-50 ms pack spikes, about 5.2k statics replicate to clients that never use them"). The lag audit later lists 29,633 permanent static colliders including the floor as simplification 6. | handoff 10-04:65; engine review :42, F13, NET-3; lag-audit | confirms hard/destruction-scale; C5 is also the origin of B13's static cost |
| B05 | F-001 records the owner's attribution (more lag after the shared-rule change; reverted for the owner's A/B). Later work found rest/wake churn as the lag cause (B02, D-124), so the attribution is doubtful. | `tried-and-failed.md:13` | confirms missing-test for round 1; the round 2 lag claim stays unproven |
| B06 | D-117: no iPad benchmark now; D-115: tablets first. The first D2 far-hide arm did not engage (farViews 0 at 225 and 325 studs). | decisions.md:125, :127; `physics-findings.md:243` (D2 row) | confirms phone-performance and the measurement limit (SR3) |
| B07 | The 10-04 plan was "tune C2, run the all x3 A/B, then delete the legacy rules" with owner approval to delete. The review says C2 was gate-verified only and never run in Studio on buildings. The delete step did not happen (F-008). | handoff 10-04 test-map-start.md:42-46; engine review F10 (:359-375); `tried-and-failed.md:20` | confirms hard; adds second cause verification-gap for the first build (C2 merged on gate evidence) |
| B08 | The orchestrator wrote that missing doc pointers in the brief caused the lighting bug. The builder rule landed after round 1 (D-128 decided 10-09 12:43; agent rule `3240ec883` at 10-10 00:49). | handoff 10-10:39; decisions.md:138, :149 | adds second cause vague-brief (no Docs line in the brief), evidence = the orchestrator's own statement |
| B09 | F-018 gives the measured saving (0.3-0.8 ms CPU), the popped shadows on landing, and that the owner's `DevShadows` A/B "didn't work" in Studio. | `tried-and-failed.md:11` | confirms reinvented-engine-feature; adds that the A/B switch itself failed at the owner's hands |
| B10 | The owner's first words (D-122) said bricks go "from animation on their screen"; the same day (D-127) he said he wanted 3D then 2D and "actually like" the old effect. F-019 gives the reasons the 10-10 motion failed. | decisions.md:132, :137, :148, :150, :152, :154; `tried-and-failed.md:10` | confirms owner-changed-direction; a vague-brief second cause is possible (D-122 vs D-127) but not shown |
| B12 | D-110 says it "corrects the reading in D-109": D-109 recorded an indestructible shell, the owner meant a breakable outside over a hidden core. | decisions.md:119-120 | confirms the vague-brief second cause (a misread owner statement) |
| B15, B16 | F-010 and F-009 record the same A/B numbers and the retry conditions. | `tried-and-failed.md:21-22` | confirms |
| B19 | D-141 (10-10): "performance is good enough to move on". | decisions.md:151 | note: stop rule; mobile tests still pending |
| B24 | The orchestrator's own lesson: `verify.ps1 -Fast` skips Luau suites and Python tests, so run the full gate after any config default change. | handoff 10-10 / `logs/2026-10-10-agents-research-and-replication.md` Lesson | confirms verification-gap |
| B25 | D-143 asked for one consistent ground level ("very strange" steps). Later the same day D-146 allowed relief ("if you make it too level, it won't look ... natural") but wanted blended slopes. Building floors were lowered (Q-57) and were waiting for the owner. | decisions.md:153, :156; handoff 10-10:24 | adds second cause owner-changed-direction (partial reversal in one day) |
| B26 | The orchestrator wrote: "Stop patching after 2-3 rounds on one symptom; get an architect design instead. The mountain needed that." | handoff 10-10:43 | confirms; supports the 10-09 third-patch rule |
| B27, EG7 | One Studio instance is also a standing fact in `rules/owner-profile.md` and orchestration rule 3 (`a301cb8af`, `9371849c`). | `rules/owner-profile.md` Standing facts | confirms |
| S3, EG4, EG5 | The root cause is the baseline rule text, not the builders: the rules sent compiled stage content and shared modules to ReplicatedStorage and called ServerStorage "Studio-managed". D-133 gives the owner's reason (exploiters decompile proprietary code). | `4e8f86fe7` body; agent-docs-audit §0; decisions.md:143 | the cause group for S3 is better read as agent/wrong-engine-guess in the rule authors (see R02) |
| E12 | `BindToCollisionSummaries` errored "is not enabled" on 10-04. The 10-10 audit says it is now in the API reference; the engine checklist Y3 and the gameplay-systems skill tell agents to evaluate it. No re-test is recorded. | `logs/2026-10-04-review-night-experiments.md:21-23`; engine checklist Y3; audit §2 researcher row | note: rule text and measurement conflict, unresolved |
| EG8 | Studio sessions showed 130-520 ms Heartbeat stalls with Lua totals of 0-2 ms, also in an idle Play with the ledger off; frame-max checks under 50 ms were "not usable evidence" in such a session. One identical cottage recipe gave a standing building in one run and a pancake in the next. | `physics-findings.md:241`, :113 | extends EG8; run-to-run spread is large and must be reported |
| EG9 | The "final merged check" found judge and bear cost "not visibly lower" in Studio despite 2-3.8x CLI gains, and no ledger label exists for Structure.step, so the structure speedup is unverified. | `physics-findings.md:240` (Final merged check) | confirms |
| S1 | The wake-churn root cause row says hypothesis (a) was right about the sweep and wrong about the fall term (0.0035 studs). | `physics-findings.md:348-349` | adds mechanism detail; confirms hypothesis ranking is unreliable without a model run |

## 3. New rows (tasks the git extractors do not have)

Columns follow the brief plus a `shared root` column. "Old agent(s)" is "none recorded" when the records do not name the builder.

| id | task (what was asked) | dates | rounds | old agent(s) | evidence | cause group | cause | why this cause | what finally worked | test candidate | shared root |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | Every road and path in a stage site plan joins the network at proper intersections (Stages 2, 3, 11) | 2026-10-11 to 10-13 | 3 (+1 reminder) | none recorded | decisions.md:167 (D-157), :168 (D-158), :178 (D-168), :213 (D-203); `tools/tests/test_stage2_walk.py` first added by `017865bba` (10-12 22:45) | process | missing-test | The owner asked for connected paths on Stage 2 (D-157), found a road/intersection defect in round 2 (D-158: "make sure the R1 road and the R2 is properly connected") and again on Stage 3 (D-168: "the roads don't properly connect"). Stage 11 repeats the rule and cites D-168. The first offline walk test is for Stage 2 only and came on 10-12. If the Stage 3 builder had D-157 in its brief this would be ignored-rule; the brief is not in the records | rule text in D-168 plus the Stage 2 walk test; no Stage 3 or 11 check found in the records read | yes: logic test (road and path graph: no stubs, every path joins the network or ends at a destination) | same instruction repeated per stage |
| R02 | The agents, skills and rules must give correct, current guidance (placement, engine-first, worktree paths, loading) | 2026-09-30 baseline; repairs 10-08 22:06 to 10-10 09:29 | 4 (baseline, 10-08, 10-09, 10-10); 8 edit commits | orchestrator; feature-builder (`4e8f86fe7`); researcher (`3d9413ae4`) | `189200157`, `71d7dc484`, `a9582b5c8`, `3240ec883`, `4432c6307`, `c77c89842`, `4e8f86fe7`, `2874c8403`, fix `f2d89feff`; `logs/2026-10-08-setup-audit.md`; `logs/agent-review/2026-10-09.md`; agent-docs-audit §0; decisions.md:128, :138, :143, :144 | agent | wrong-engine-guess | The baseline placement text put compiled stage content in ReplicatedStorage and called ServerStorage Studio-managed, against `data-model.md:221-228`; `4e8f86fe7` names it the root cause (5.2 MB stage data and 1.56 MB server code reached every client). Other defects in the same passes: AGENTS.md read in 6 of 19 sessions; about 590 worktree refusals; AGENTS.md §1 said "never unanchored physics on the server" from D-083 (10-02) to `c77c89842` (10-10). Second cause owner-changed-direction: D-118 and D-128 are the owner's reaction to overcomplication | rules rewritten (`4e8f86fe7`), server-only move (D-133), `replication_check.py` gate, CLAUDE.md import, worktree line | yes: review of a diff (rule text checked against the docs mirror and the ledger) | SR4 |
| R03 | VFX workflow v2 and the fireball pilot | 2026-10-16 to 10-20 | 5 | vfx-designer (D-288) | decisions.md:220 (D-283), :221 (D-284), :223 (D-286), :224 (D-287), :226 (D-289), :227 (D-290) | not-a-fault | owner-changed-direction | The owner dropped the 2D storyboard step (D-284), asked for a dark test place (D-287) and then a separate lab place (D-290). Second cause with its own evidence, agent/over-building: D-289 records the test made the fireball do splash damage ("the fireball do splash damage") and D-290 records "I shouldn't have to specify that there's no damage or breaking". Also D-286 item 3: the owner did not trust the rule of at most 5 emitters and it was re-derived from a practitioner guide | rule D-289/D-290 (visuals only, fake damage is allowed as cosmetic parts) | no (owner look); the visuals-only rule is a review of a diff | none |
| R04 | Story-cast rigs (King, golem, villain, companion, villagers) rigged in Blender from Tripo meshes | 2026-10-11 to 10-12 (F-020 dated 10-11) | 5 or more | none recorded | decisions.md:170 (D-160), :171 (D-161), :177 (D-167), :195 (D-185), :196 (D-186); `tried-and-failed.md:9` (F-020, five sleeve-remnant attempts) | unclear | unclear | Each round was found in the owner's review or in motion: fused golem arms webbed on a raise, the cape passed through the tail, the villain's three right arms fused, variants made by bending the body mesh left shoulder lumps and neck creases ("You can tell that the rigs are broken"), skinned arms wrinkled. The owner asked for a written rule (D-185 "create like a rule") and one was written after. The record does not show whether a pose test existed before each hand-in. Missing: the rig test records in `logs/2026-10-12-opening-film-rigs.md` (session-log extractor) | separate limb, head and tail meshes with a seam rule; variants built by a researched method; F-020 kept a radial tuck and never deletes faces on an open-shell mesh | no: asset quality; a deformation test per rig is a Studio/Blender test | none |
| R05 | Opening cutscene concept (cannon story, then halo, bionic legs, own kingdom) | 2026-10-10 to 10-12 | 5 | orchestrator (not named for builders) | decisions.md:157 (D-147), :158 (D-148), :159 (D-149), :191 (D-181), :193 (D-183) | not-a-fault | owner-changed-direction | The cannon became a halo, the whole sequence moved to game start, the King lost his legs and then kept them ("the character is stubby"), and the village was replaced by an own kingdom. All are the owner's words | D-181, D-183, D-184 | no (design) | none |
| R06 | Server size target: 12 players, then 8 (low 6), then 12 ideal and 8 minimum | 2026-09-30 to 10-02 | 3 | none recorded | decisions.md:44 (D-035), :60 (D-050), :68 (D-058) | not-a-fault | owner-changed-direction | The owner moved the target twice in three days; D-050 says the number would be set from the grid-v2 benchmark. No multi-client measurement exists by 10-10, so the final budget (12 on phones) is untested | D-058 (design for 12, 8 floor) | yes: performance capture (Local Server 8 and 12 clients plus one real phone; not run) | SR3 |
| R07 | Stage 3 (Dream Doll House) plan and build corrections | 2026-10-11 to 10-13 | 3 after approval of D-162 | none recorded | decisions.md:172 (D-162), :175 (D-165), :178 (D-168), :202 (D-192) | unclear | unclear | D-165 removed the open mansion side (owner direction) and found rooms under-decorated; D-168 asked for solid neighbour walls and connected roads; D-192 found blank back walls, overused spheres and trees that "look horrendous". Back and side views are in the required review angles (AGENTS.md §2.4), so either the review was not done or its criteria did not cover blank faces. Missing: the Stage 3 review packet | D-192 fixes (windows on every face, merged tree canopies) | yes: Studio test (multi-angle review packet with a blank-face check) | R01 for the roads part |

How R rows were counted: one round per owner decision or hand-in that a later decision reverses or repairs for the same goal. R01 counts the failures only (D-158, D-168, plus the first ask D-157); D-203 is a reminder.

## 4. Two-round and design-only appendix

| id | task | dates | evidence | cause group | cause | note |
| --- | --- | --- | --- | --- | --- | --- |
| aR1 | Gear ideation workflow | 2026-10-07 | `tried-and-failed.md:12` (F-017), `rules/owner-profile.md` Taste | not-a-fault | owner-changed-direction | owner called the first workflow "lackluster" and form-limiting; v2 followed |
| aR2 | Stage 2 reference images from ChatGPT | 2026-10-11 | decisions.md:174 (D-164), :173 (D-163) | unclear | unclear | three of nine hero images unusable (White House "not very accurate", Eiffel two-colour banding, Great Wall "strange"); real photos became primary |
| aR3 | Story cast designs (King, villain, golem, style) | 2026-10-11 | decisions.md:160-165 (D-150..D-155) | not-a-fault | owner-changed-direction | villain A/B rejected for a hidden face, golem collar and eyes corrected, one shared style chosen from four tests |
| aR4 | Stage 6 set list | 2026-10-11 to 10-12 | decisions.md:179 (D-169), :182 (D-172), :187 (D-177), :188 (D-178) | not-a-fault | owner-changed-direction | round 2 added toys, cut the RC truck and the marble run |

## 5. Rules added after a failure, and owner decisions that record an agent mistake

Evidence for process and agent causes. Each row is a written rule or decision created because something went wrong.

| item | what went wrong | rule or decision | evidence |
| --- | --- | --- | --- |
| Server physics forbidden by rule | `rules/performance.md` blocked rigid bodies after play-test 1 | D-083, asked first: "May I change that rule?" | decisions.md:93 |
| Symptom before feature | play-test 2 found random coming-apart | D-084 item 6: no new features until play-test symptoms pass as specs | decisions.md:94 |
| Miniature buildings | first Stage 1 builds rejected | D-091 scale x1.5 and blueprint approval before bricks | decisions.md:101; F-012 |
| Whole lab on every change | lab runs "take way too long" | D-102 test tiers 0-3 | decisions.md:112 |
| Collapses looked wrong for new buildings | repeated collapse defects | D-104 building physics rules for new buildings only | decisions.md:114 |
| Overcomplicated destruction code | lag; clean-room size check | D-118 simplify, prefer engine features; D-128 docs-first and "Docs read" in reports | decisions.md:128, :138 |
| Shadow system | per-category shadows built, then removed | D-139; F-018 | decisions.md:149; `tried-and-failed.md:11` |
| Server-only data on every client | 5.2 MB and 1.56 MB replicated | D-133; `replication_check.py` gate | decisions.md:143; `4e8f86fe7` |
| Wrong rigs | deformed variants | D-185 (rule to be written), D-153 (one character, one view per 3D reference) | decisions.md:195, :163 |
| VFX test dealt damage | agent added gameplay to a visual | D-289 visuals only, D-290 fake damage as cosmetic parts | decisions.md:226-227 |
| Tripo body mesh repair | five repair attempts failed | F-020 "tuck first, never delete faces on an open-shell mesh" | `tried-and-failed.md:9` |
| Agents did not load AGENTS.md | read in 6 of 19 sessions | CLAUDE.md import (`189200157`) | `logs/2026-10-08-setup-audit.md` |
| 590 refused worktree edits | builders edited the main checkout path | worktree line in builder files (`71d7dc484`) | `logs/agent-review/2026-10-09.md` |
| One symptom patched many times | A02 9, A08 7, A01 6, A03 5 rounds | third-patch rule in feature-builder and reviewer (`a9582b5c8`); handoff 10-10:43 | `.claude/agents/feature-builder.md:28` |
| Missing docs pointers | lighting bug | Docs line required in every builder, architect, reviewer and studio-operator brief | handoff 10-10:39; orchestration SKILL brief format |
| Two Studio windows | agent plan used two instances | one instance, one driver (`9371849c`) | git-b EG7 |
| Early master merge | orchestrator dry run ran in the main checkout | forward fix; lesson in the log | `logs/2026-09-30-stage1-prototype.md` Incident |

## 6. Owner redirects (evidence for owner-changed-direction)

- 52 of 217 decision rows (24%) supersede, amend, refine or withdraw an earlier row. By day: 09-30 11 of 57, 10-02 13 of 27, 10-04 4 of 12, 10-10 8 of 19, 10-11 5 of 24, 10-12 4 of 18.
- Rows struck out or withdrawn: D-015, D-035, D-038, D-044, D-046, D-050, D-062, D-097.
- Rows that name a play-test or a mock-up review as source: D-051, D-052, D-053, D-054, D-056, D-057, D-079, D-082, D-084, D-085, D-124, D-173.
- Large redirects that cancel or reverse built work: D-054 (2D icons to 3D bricks, same evening), D-082/D-083 (analytic motion to engine bodies), D-105 (nether and end leave Stage 1), D-122 (no floor pickups), D-129 (UI route), D-139 (shadows), D-148 (halo replaces cannon), D-181 (King keeps legs).
- The owner also delegated many choices ("you decide what's best", D-048, D-072, D-082, D-103, D-164, D-170); those rows are not redirects.

## 7. The 10-06 engine review: what was recommended, what came of it (SR8)

The review labelled every claim MEASURED, CITED or HYPOTHESIS and said which fixes change behaviour. This table compares its ranked proposals with later measurements. It is evidence for how well a hypothesis-ranked design review predicts the real cause.

| review item | expected | what the records show | evidence |
| --- | --- | --- | --- |
| Instrument first (ledger, sub-labels) | turns hypotheses into numbers | worked: the ledger found debt idle and rest/wake churn (37-69% undone within 0.1 s) | `physics-findings.md:139-151` |
| F1 separate debt, guaranteed separation lane ("lane B") | 0.2-0.9 s faster separation; p95/p99 may rise | idle frames fell a lot (cottage 1,071 to 56) but median separation latency did not change (church 0.25 vs 0.24 s, cottage 0.21 vs 0.21 s) and church frame time was 1.6x worse; not made default | `physics-findings.md:155-158`; `tried-and-failed.md:22` |
| F2 R15 `outside()` on stored hulls | identical results, faster | identical (bit-equal checks) and 4.7x on the hull test in CLI; Studio judge/bear cost not visibly lower; Structure.step has no Studio label | `physics-findings.md:166`, :240 (Lane C hull cut, Final merged check) |
| F7 client: stop following rested rubble | phone cost proportional to moving pieces | became the "restUnfollow" part of the L0 set; default on in D-124 with owner "a lot smoother" | decisions.md:134; git-b B02 |
| F16 far-hide of collapses on phones | fewer client Parts | D2 arm did not engage at 225 and 325 studs; stays off | `physics-findings.md:243` |
| F8 big-body stress | stops chunks resting high | never ran on the cottage (counters 0 in 5 of 5 runs) | `tried-and-failed.md:21` |
| F10 unified contact model A/B | one predictable rule | stress 0/6 and heavy block sank 35.7 vs 4.4 studs; not adopted | `tried-and-failed.md:20` |
| Debris lifecycle (D-103) | remove rubble | worked after the pile-sweep redesign and churn fix (L0) | `tried-and-failed.md:14-19`, D-124 |

Reading: the two items that finally helped (instrumentation, rest-unfollow with the wake model) were not the review's top-ranked behaviour changes. The ranking by expected win was not reliable; the measured A/B was.

## 8. Engine guesses found in the records (new beyond git-a/git-b)

| id | wrong or doubtful assumption | evidence | correct behaviour or status |
| --- | --- | --- | --- |
| RG1 | `BindToCollisionSummaries` can supply contact forces | `logs/2026-10-04-review-night-experiments.md:21-23`; engine review §5 Q9 | errored "is not enabled" on 10-04; the 10-10 audit says the API now lists it; no re-test recorded |
| RG2 | The wake sweep's fall term (0.5 g dt^2) drives rest/wake churn | `physics-findings.md:348` | the fall term is 0.0035 studs and only 2-3% of promotions need it; the amplifier is the sweep box that already contains the collider's own bounds |
| RG3 | ClientHumanoid.MoveTo and the NotReplicated tag predict the engine's door input path | `physics-findings.md:90` | they did not; the door intent stayed 0 in that session; probes use the actual client move |
| RG4 | Studio frame-time readings are our code | `physics-findings.md:241`, :114 | 130-520 ms Heartbeat stalls occur with Lua at 0-2 ms and in an idle Play |
| RG5 | The review's "6.5k units per ms" and "5-20x" speedups hold in Studio | engine review Appendix (S2 "5-20x" refuted to about 2-4x); `physics-findings.md` Final merged check | CLI gains were diluted or invisible in Studio |
| RG6 | The profiler label reboxInPlace 154.7 ms was a real single cost | `physics-findings.md:150` (profiler double count) | the profiler counted recursion twice; real re-box about 75-80 ms |
| RG7 | The engine docs say prefer Adaptive stepping, so it can be restored | engine checklist Y2 versus A03 | the project measured Fixed required for the lift launches; the result is not in the checklist |

## 9. What worked (from the records)

1. The decision ledger with owner words, plus the tried-and-failed register with "retry only if" (F-006 was retried when its condition was met and then worked).
2. Asking before breaking a binding rule (D-083) and explicit delegation (D-073).
3. Labelled evidence: MEASURED, CITED, HYPOTHESIS in the review and findings; adversarial verification refuted sub-claims of 26 findings before any code changed (engine review Appendix).
4. Measure before merge: F-011 (a cache that regressed 0.291 to 1.348 ms) was fixed in the same task before it reached a default (`physics-findings.md:55`).
5. Stop rules written by the owner or the orchestrator: D-141 (performance good enough), D-120 (checkpoint before scale-down), "stop patching after 2-3 rounds" (handoff 10-10:43).
6. Behaviour-identical changes proved identical (frozen-copy checksums, mutants): Lane A/C/F3 rows in `physics-findings.md`.
7. Studio probes that overruled assumptions: memory, bounds and foreground checkpoint (git-b section 4).

## 10. Repeated symptoms (3 or more patches) added by the records

| symptom | count and evidence |
| --- | --- |
| Roads and paths not joined in stage plans | 3 failures plus a reminder: D-158, D-168, D-203 |
| Stage plans needing "decorate every room / every face" | D-165, D-192; Stage 11 D-195 ("fill the streets") |
| Rest/wake churn | covered by S1 (git-b), now with mechanism: `physics-findings.md:148-151` |
| Rules contradicting the ledger | AGENTS.md §1 vs D-083; placement rule vs docs; `rules/gui.md` vs D-129; script-placement skill vs rules (setup audit) |
| Hypothesis about the cause of lag that the next measurement overturned | wake fall term (RG2), debt idle as rate limit (section 7), CLI speedups (RG5), windmill lag (B05) |

## 11. Coverage, counts, questions

| part | status |
| --- | --- |
| tried-and-failed.md (F-001..F-020) | done |
| decisions.md (217 rows, D-001..D-290) | done |
| handoffs (5 files) | done |
| clean-room research note | done |
| destruction-engine-review-2026-10-06.md | done (all 845 lines) |
| physics-findings.md | read lines 1-164 in full and 165-360 by search for failures, regressions and hypotheses; the rows about lane internals were not read one by one |

Counts: 36 update rows (some rows cover 2-3 tasks); new rows R01-R07 by cause group: process 1 (R01), agent 1 (R02), not-a-fault 3 (R03, R05, R06), unclear 2 (R04, R07); appendix aR1-aR4 (not-a-fault 3, unclear 1). No `hard` or `phone-performance` rows are new: those causes are already in git-a/git-b.

Questions with defaults:
1. Id clash B01..B10 in git-a's appendix versus git-b. Default: use aB for git-a appendix rows (done here).
2. Git-a/git-b end at 10-10 but records run to 10-20. Default: R rows after 10-10 stay in this file and are marked records-only.
3. R04 and R07 are `unclear`. Default: leave them until the session-log extractor reports whether a pose or review packet existed.
