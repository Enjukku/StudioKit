---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J008-T11
supersedes: []
---
> Author: grader · claude-sonnet-5-5 · high · 2026-10-21

# Grades: hidden test J008-T10 (environment designer, H1-H8)

Inputs: the agent's answers (`hidden-answers.md`) against the keys. H1-H3 against "Cause found", "Fix that worked", "Wrong first guesses" and "Pass test" in `hidden-cases.md` (HC1-HC3). H4-H8 against rows DF01-DF05 in `knowledge/reference/environment/03-pipeline-performance-review.md` section 5.2. The keys are OPINION or first-game evidence; I judged closeness in meaning, not wording. Rule: a case passes when R1 and R3 are pass and no criterion is fail. Partial is not pass.

Criteria: R1 cause matches the key (all parts) · R2 proof before change · R3 fix matches the key's repair · R4 no wrong first guess, nothing invented · R5 says honestly what stays unverified.

## Test-hygiene warning (read before the totals)

The agent cited the key note itself for H4-H8 ("N03 DF01" to "N03 DF05" in every answer). Its own gap table says: "Five of eight cases needed the note, not the skill." So the five DF passes show the agent can find and apply a reference note. They do not show that the skills carry these patterns. H1-H3 are the clean signal: the agent had no key for them. Also, `.agents/skills/environment-design/references/diagnosis.md` was written after the answers (file time 02:00 against 01:59) and quotes HC1-HC3 and DF01-DF05. It is not graded. Any re-test with it in place is contaminated; new held-out cases are needed.

## H1 (HC1): ground jumps round buildings

| crit | grade | quote from the answer | reason |
| --- | --- | --- | --- |
| R1 | partial | "Two height sources that nobody reconciled. The per-column ground heights were written without the building floor heights." | Matches the floor-versus-ground cause and the landform base ("Hill on the wrong datum"). Misses the second cause: decorative relief and noise that added 377 extra steps. Offers whole-cell quantisation instead; the key does not support it (extra, unproven). |
| R2 | partial | "the largest height step between neighbouring columns in the ring versus elsewhere on the map." | It measures per column before any change, and reports `MEASURED`. It has no step to sort steps into designed relief and artifact, which the pass test needs. Steps that cluster at rings are read only as "pad edges". |
| R3 | partial | "a blend ring that eases to the natural ground (width `PROPOSAL`" | Smooth blend, relief kept, floors, doors and routes held as anchors: matches the key. Missing: switching off the artifact steps, and lowering floors where a ring cannot blend (the key lowered six). The agent sends that case to the game designer as a proposal, which is close to the key's open question, but it is not the repair. |
| R4 | pass | "No tolerance is invented: the delta table is reported as `MEASURED`, not pass/fail" | None of the key's wrong guesses (noise setting, flatten, raise buildings, new design). Sink and blend widths are marked `PROPOSAL`. The quantisation idea is a test, not a claim. |
| R5 | pass | "All checks above (planned). Whether fractional `WriteVoxels` occupancy gives the expected smooth surface" | Says nothing was run; names the engine look and the phone as unverified; plans a re-measure. |

Case H1: R1 partial, R3 partial. **FAIL.** Near miss: it found the cause that is easiest to see (floors) and missed the one that needs a per-column split (decorative steps).

## H2 (HC2): grey trim and olive walls

| crit | grade | quote from the answer | reason |
| --- | --- | --- | --- |
| R1 | pass | "The model is right and the picture pipeline is wrong" | Same cause class as the key (preview set-up, not the model). The candidate list is wide (view transform, exposure, tinted light, colour space) and does not name the preview's ambient fill first, which was the real one. Accepted because the first check covers it. |
| R2 | pass | "Calibration card in the same scene and tool: a pure white swatch, a neutral mid-grey swatch" | Matches the pass test (a known white object in the same scene). Adds an engine capture before any colour edit. |
| R3 | pass | "fix the render setup (neutral view transform, neutral light, correct exposure), write it down as the project's render recipe" | Fix the review set-up, record the setting, judge final colour in Studio. No ambient number invented. |
| R4 | pass | "The model's palette values and the art-bible locks." | Palette stays untouched. None of the key's wrong guesses (change palette, polish round, blame concept). The pineapple case is not assumed. |
| R5 | pass | "The cause until the card test runs. How the concept image itself was lit" | Honest about the cause being open and the Studio and phone look being unchecked. |

Case H2: **PASS** (5 of 5).

## H3 (HC3): porch slats and blue lines

| crit | grade | quote from the answer | reason |
| --- | --- | --- | --- |
| R1 | partial | "Porch slats: probably a real defect — the porch roof is separate pieces that do not touch or overlap" | Porch is called real and the outline score is correctly overruled. The cause is wrong in kind: the key is missing vertical riser faces between stepped layers, not loose pieces. Blue lines: "probably sky showing through — a gap between the wall top and the roof underside". The key says false alarm (an authored chimney notch). "Authored detail" is not among the agent's candidates. |
| R2 | partial | "Read the parts: positions and sizes of the porch-roof pieces and the gaps between neighbours" | Data read and re-shoots come before any change; good. But it does not look for missing faces between levels, and for the blue lines it never compares the opening with the blueprint or source (the drawing check is for the porch only). A read of the data would call the notch a defect. |
| R3 | partial | "close the gaps (overlap the slats or use one kit roof piece; seat the roof on the wall top)" | Right layer, one exact note, outline and drawing untouched. But the fix is "overlap or replace", not "add the missing risers, keep footprint and heights". A swapped kit piece may change heights; closing the soffit could remove the authored notch. |
| R4 | pass | "a numeric match score is a floor, not the finish" | Does not trust 0.97, does not lower a threshold, does not rebuild the roof, plans to check the lines before fixing. The lean toward "real" on the blue lines is noted under R1. No numbers invented. |
| R5 | pass | "Which candidate is true until the part data is read and the re-shoots exist." | Names data and capture as not done and the phone as unverified. Does not split data-verified from capture-verified after a fix, but the answer is plan-only, so this fits. |

Case H3: R1 partial, R3 partial. **FAIL.**

## H4 (DF01): flat plaza, "add more lights"

| crit | grade | quote from the answer | reason |
| --- | --- | --- | --- |
| R1 | pass | "No deliberate visual hierarchy, not too little light" | Same as the key; also covers the no-focal-point case. |
| R2 | pass | "A greyscale copy of each shows the value hierarchy." | Compares the focal region with competing surfaces from the player camera; reads the look sheet; luminance is labelled a diagnostic only. |
| R3 | pass | "a bolder large form or a clearer line of sight, not a brighter small prop" | Same as the key. Changes the relationship at the focal region; sends layout changes to the game designer. |
| R4 | pass | "adding lights everywhere is the known failure" | Answers the art director without the wrong guess. All values are `PROPOSAL`. |
| R5 | pass | "The owner's and players' read ("I know where to look") needs them. Phone result. All values." | Honest and specific. |

Case H4: **PASS** (5 of 5; lookup-assisted, see warning).

## H5 (DF02): market street clutter

| crit | grade | quote from the answer | reason |
| --- | --- | --- | --- |
| R1 | pass | "Dressing placed as a quota: every free surface treated as a place to put something" | Same as the key. The bumping cause (props in lanes, oversize collision) is extra, valid. |
| R2 | pass | "Top-down capture with the route graph's lanes and interaction points over it" | Overlays exclusions and asks for a one-line story per cluster before cutting. |
| R3 | pass | "Clear the route lanes, interaction approaches and camera corridors (PR-21)." | Matches: re-apply exclusions, remove low-value clusters, add a story relationship instead of scatter. |
| R4 | pass | "I will not turn collision off on props that stand in the lane" | No invented prop counts or densities. No "more unique meshes". |
| R5 | pass | "Whether players now read meaning (play-test). Feel of the walk. Phone cost." | Honest. |

Case H5: **PASS** (5 of 5; lookup-assisted).

## H6 (DF03): dollhouse stage

| crit | grade | quote from the answer | reason |
| --- | --- | --- | --- |
| R1 | pass | "Wrong scale from an unverified conversion or from assets made without the player reference" | Same as the key. It does not accept "nobody changed the export settings" as proof. |
| R2 | pass | "Measure a door's opening in studs (`GetExtentsSize`) against the scale sheet's player envelope" | Measures first and re-runs the calibration round trip before any resize. |
| R3 | pass | "scale first, because resizing changes contact and repetition" | Source first, then contact, then repetition with a moving camera, then terrain joins from both sides. All four key repairs, in order. |
| R4 | pass | "No invented door size." | Rejects hand-resizing single doors and stacked scale factors. |
| R5 | pass | "The faulty layer until the round trip runs." | Honest; names the owner's feel call. |

Case H6: **PASS** (5 of 5; lookup-assisted).

## H7 (DF04): sound jumps, same sound, waterfall without water

| crit | grade | quote from the answer | reason |
| --- | --- | --- | --- |
| R1 | pass | "no ambience map, or one global loop renamed per zone" | Same as the key. It adds the streaming, parenting, duplicate and state-coordination causes the key lists for sudden changes and picture mismatch. |
| R2 | pass | "Play-mode border walks with a log of the active sources per position" | Checks the map against the audit, inspects each source, counts duplicates on leave and return. |
| R3 | pass | "Write or complete the ambience map: per zone the four jobs filled only where needed" | Per-zone causal layers, blend at the border, briefs to the sound designer and (through the lead) the code role. Sound values left to the sound designer. |
| R4 | pass | "No invented fade times or ranges" | None of the key's wrong guesses (a bad asset). |
| R5 | pass | ""auditory acceptance pending" until someone hears it" | Honest; also flags the undocumented streaming behaviour. |

Case H7: **PASS** (5 of 5; lookup-assisted).

## H8 (DF05): slow on a phone, two bad fixes

| crit | grade | quote from the answer | reason |
| --- | --- | --- | --- |
| R1 | pass | "Unknown until measured. The cost has not been traced to real resources and work" | Same as the key; marker versus expensive system is stated. |
| R2 | pass | "MicroProfiler at the busiest overlap with gameplay on" | Names the device and the target, then traces before any cut. Studio stats are labelled relative only. |
| R3 | pass | "Reduce the **measured** bottleneck, one cost category at a time" | Same as the key; asks the owner what to protect when cuts are needed. |
| R4 | pass | "If a stage passes only with ambience or effects off, it has not passed" | Refuses both bad fixes. No budget invented ("platform caps are not targets"). |
| R5 | pass | "Everything until the trace exists. Other devices. Thermal behaviour over a full session." | Honest. |

Case H8: **PASS** (5 of 5; lookup-assisted).

## Summary

| case | key | R1 | R2 | R3 | R4 | R5 | case pass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1 ground steps | HC1 | partial | partial | partial | pass | pass | FAIL |
| H2 render colour | HC2 | pass | pass | pass | pass | pass | PASS |
| H3 roof slats | HC3 | partial | partial | partial | pass | pass | FAIL |
| H4 flat plaza | DF01 | pass | pass | pass | pass | pass | PASS |
| H5 clutter | DF02 | pass | pass | pass | pass | pass | PASS |
| H6 scale | DF03 | pass | pass | pass | pass | pass | PASS |
| H7 sound | DF04 | pass | pass | pass | pass | pass | PASS |
| H8 cost | DF05 | pass | pass | pass | pass | pass | PASS |

**Total: 6 of 8 cases passed.** First-game failures (H1-H3, no key in hand): 1 of 3. Paper defects (H4-H8, key note cited by the agent): 5 of 5, lookup-assisted. Criteria: 34 of 40 pass, 6 partial, 0 fail.

Strictness note: both failed cases are multi-part causes where the agent found one plausible part and named a single mechanism with a generic repair. The agent's honesty (R4, R5) was clean in all eight: no invented numbers, every unrun check labelled as planned.

## Skill gaps the misses point to

| id | observation | where to look | suggested change |
| --- | --- | --- | --- |
| G1 | H1 R1/R2/R3: nothing in the skills asks the designer to sort measured ground steps into designed relief and artifact, so decorative noise was never a suspect. The agent's own gap row for H1 covers floor-versus-ground only. | `environment-craft/references/terrain-and-water.md` §2-§3; `04-first-game-stages.md` FS-P07 | Add to the ground audit: step per column, split by source (designed relief, noise, outcrop, pad edge); anchors list; neighbour step limit is an owner number; lower a site floor only through the game designer when its ring cannot blend. |
| G2 | H3 R1/R2/R3: no rule for layered or stepped covers (missing vertical riser faces). The agent's own proposed fix ("artifact or defect?" row) does not include "authored detail". It leaned "real" on lines the key calls authored. | `environment-design/references/review.md` §2-§3; `audit-and-capture.md` | Add a three-way test: missing faces between levels, real gap between pieces, render artifact, or authored opening; compare each suspect with the blueprint and source before any fix. Fix keeps footprint and heights; add the missing faces only. Add a low oblique and an under-roof camera. |
| G3 | H2 (pass, weak spot): the cause list is wide and the preview's ambient fill is not first. | `audit-and-capture.md` §3; `blender-to-studio.md` §3 | Put "preview ambient and exposure set-up" first in the calibration-card step; store the render recipe. |
| G4 | Pattern across H1 and H3: the agent proposes one mechanism and one generic repair when the real cause has several parts. | `review.md` §6 cause-first rule | Add: "list every mechanism the data can show; measure each one separately before choosing a repair". |
| G5 | Test hygiene: H4-H8 were answered with the key note in hand; `diagnosis.md` was written after the test from the same keys. | J008 test plan | Do not count H4-H8 as proof of skill coverage. Write fresh held-out cases for the next round and keep `diagnosis.md` out of the test run (or hold out new cases). |
