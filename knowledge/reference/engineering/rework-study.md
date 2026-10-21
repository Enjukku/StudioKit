---
type: reference
scope: universal
status: draft
updated: 2026-10-21
source: J010 rework study (DestructionSimulator 2026-09-30..2026-10-20); parts rework/git-a.md, git-b.md, git-c.md, logs.md, records.md, old-agents.md
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Rework study: DestructionSimulator (merged)

Lead's merge of six extractor files in `rework/` (Sonnet 5.5 high; every row there cites commits or file:line). This page counts **engineering tasks only** (art, cast, film-rig and stage-look rows are left out) and counts tasks that share one root once (`rework/records.md` §1 SR1-SR8). Rounds = hand-ins later found wrong for the same goal; pre-merge review passes are not rounds. The main cause is one group; second causes are in the part files. Where git-b (process) and logs (hard) disagreed on the lag task, the lead chose process, because the cause (rest/wake churn) was already in the 10-06 table and five rounds went to costs measured outside Studio (git-b B02, logs L04).

## 1. Totals (engineering tasks with 3+ rounds, root-deduped)

| group | tasks | rounds | share of rounds |
| --- | --- | --- | --- |
| process | 21 | 102 | 64 % |
| hard by nature | 7 | 33 | 21 % |
| agent quality | 6 | 21 | 13 % |
| unclear | 1 | 3 | 2 % |

Not counted as faults: owner changed direction (24 % of all decision rows revise an earlier one, `records.md` §6), e.g. pickups v1-v8 (A13, A15) and later removed by D-122.

## 2. Causes per group

### Process (102 rounds)
| cause | tasks (rounds) | what happened | evidence |
| --- | --- | --- | --- |
| missing test, or test on toy cases instead of the real content and scale | A05 (6), A12 (4), A14+B14 (10), A18+A19 (6), A21 (6), A23 (3), B05 (3), C02 (3), C16+C25+C26 (4) = 9 tasks, 45 | specs used small made-up cases; the real stage, scale or the owner's scene broke them; "nothing falls at load" was fixed 3 times with 3 one-off tools | git-a A05, A14; git-b B05; git-c C16, S1; old-agents GP4 |
| no measurement first (or measured offline, not in the real place) | A01+A02 (9), A07 (4), B01 (6), B02 (6) = 4 tasks, 25 | three smoothing layers built on a guess before the source was measured; debris removal shipped 3 versions before the first Studio A/B; five lag rounds cut costs measured only offline while the real cause (rest/wake churn) showed only in a Studio soak | git-a A01; git-b B01, B02; logs L04 |
| fix broke something else | A08 (7), A10 (5) = 12 | each rest fix and the phasing fix created the next bug | git-a A08, A10 |
| "done" without a real check | A16 (3), B13 (4), C01 (3) = 10; plus 15 commits "Not Studio-verified", fast gate skipping Luau tests | honest labels, but merging went ahead anyway | git-a §5; git-b B13, B24; old-agents GP2 |
| no owner for shared lists | C23 (3), C24 (4) = 7 | decision ids renumbered in 9 commits; one test list edited 4 times in 1.5 h | git-c C23, C24 |
| vague brief | C06 (3) | the lead's own formula was wrong; the reviewer then found a money farm | git-c C06 |
| setup (not counted above) | — | rules file read in 6 of 19 sessions until 10-08; about 590 refused worktree edits | logs §4, §9 |

### Hard by nature (33 rounds)
| cause | tasks (rounds) | evidence |
| --- | --- | --- |
| destruction at real size: costs appear only at full scale | A09 frame spikes (6) with B04/L02 church real physics | git-a A09; git-b B04 |
| physics tuning without engine contact forces | A04 (3), A06+B07+L05 contact model (5, never settled), B03/L01 pyramid rest (5, stochastic) | git-a A06; git-b B03, B07 |
| engine behaviour found by measuring | A03 sky launches (5): Adaptive stepping launched 26 of 144 test pairs, Fixed 0 of 144. Note: the docs already recommended Fixed for destruction | git-a A03; logs A03 update |
| feel judged in play | A20 + A26 blast feel (6) | git-a A20, A26 |
| phones not measurable | B06 phone rubble LOD (3): no real phone, emulator changes the screen only | git-b B06; records SR3 |

### Agent quality (21 rounds)
| cause | tasks (rounds) | evidence |
| --- | --- | --- |
| wrong guess about the engine | A11 doors (3: the engine sleeps a slow door), A17 spawn position read too early (4), A25 own bug blamed on "engine" (4), B08 invented class names "Bloom" (3), R02 rule text sent 5.2 MB stage data and 1.56 MB server code to every client (4) | git-a A11, A17, A25; git-b B08; records R02 |
| rebuilt an engine feature | B09 own shadow system (3; docs say CastShadow is not for performance; saving 0.2-0.8 ms). Second causes elsewhere: A07 own analytic motion instead of engine bodies; SR1 own rest system that fights engine sleep (hypothesis, never A/B-tested) | git-b B09; logs A07; records SR1 |
| over-building (not counted: estimate) | 45,068 lines in 100 modules against a clean-room estimate of 2.5-4k; owner "overcomplicated" (D-118) | logs §4; records B02 |

## 3. What the old agents did well (keep)

| habit | evidence |
| --- | --- |
| failing case first; logic in offline-tested modules | closed bugs in one more round (git-a §3.1; old-agents FB5) |
| independent reviewer before merge | 61 runs, 100 % finished, 3.3 % owner pushback; caught money farms, currency-merge and cooldown defects (logs §4; git-c W1) |
| default-off switch + identity check + Studio A/B | no switched feature shipped as a regression (old-agents HB1) |
| old-vs-new tests with planted bugs for speed-ups | behaviour-identical lanes merged with no rework (git-b §4) |
| measured before/after tables with a pre-set budget | lag p95 23.6 → 0.77 ms (git-b B02) |
| honest verification labels | 15 "Not Studio-verified" bodies, no false "done" claims recorded |
| stop at the third patch, ask the architect | B01, B26 each ended in one design (records B26) |
| ask before breaking a binding rule | D-083 |

Old agent scores (DestructionSimulator scorecard, 30 days to 10-09; activity, not quality): feature-builder 121 runs, 95.9 % finished; reviewer 61, 100 %; quick-builder 13, 92.3 % (on Sonnet); architect 6, 100 %. The scorecard has no rework measure (logs §4).

## 4. Gaps the new agents must close

| gap | from | owner role |
| --- | --- | --- |
| measure first in the real place: baseline, same recipe, 3+ runs, spread | process: no measurement first | performance-engineer, feature-builder |
| tests on the real content, scale and the owner's scene; one shared check per repeated symptom | process: missing test | qa-lead, builders |
| "done" for performance, physics or feel needs Studio evidence, else status `not verified` | process: done without a check | all; reviewer blocks |
| probe engine behaviour the docs do not state (a short Studio test before building on it) | agent: wrong engine guess | builders, architect |
| docs pointer for every engine system in every brief | records SR4 | lead, architect |
| size budget for the simplest version; engine feature named per part | agent: rebuilt engine feature, over-building | architect, reviewer |
| one owner for shared registries | process: no owner | architect (design), lead (assign) |
| route design work to the architect (6 runs vs 121 builder runs) | old-agents GP10 | lead |

## 5. Test candidates (rebuilt as small stand-alone tasks with the same trap)

| past task | trap | role |
| --- | --- | --- |
| A12 weapon cooldown | two interleaved requests both fire across a yield | feature-builder, reviewer |
| A13 / C06 currency merge, stage yield | value not conserved; cross-player merge; farm by floor kill | feature-builder, reviewer |
| B08 lighting presets | invented class names; creating effects in code | quick-builder, reviewer |
| C24 registry list | typed twice instead of derived | quick-builder |
| B09 shadow cost | building a system the engine already has | quick-builder (should stop), reviewer |
| B02 / SR1 rubble lag | own rest system fights engine sleep; measured offline only | performance-engineer |
| B13 stage reset | 24k Parts destroyed in one frame | performance-engineer |
| EG4 / R02 replication | server-only data and collider Parts sent to every client | performance-engineer, reviewer |
| A07 falling pieces | custom motion instead of engine bodies | architect |
| B01 rubble removal | per-piece vetoes instead of a pile sweep + lifetime | architect |
| L03 windmill rules | rules in shared code run for every building | architect, reviewer |
| C16 / C25 / C26 nothing loose at load | one-off tools instead of one shared check | qa-lead |
| A05 / A21 collapse rules | toy cases; no random-update oracle | qa-lead |
| A17, E1, E2, B17, EL4 | spawn position too early; camera offset accumulates; Lua box test vs engine bounds; anchoring to rest | reviewer planted bugs |
