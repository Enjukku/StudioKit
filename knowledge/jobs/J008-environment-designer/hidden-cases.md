---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J008-T04, DestructionSimulator stage sources (read-only)
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# J008 hidden test cases (held out of the skills)

> Used once on 2026-10-21 (J008-T10 answers, T11 grades: `grades-hidden.md`). After grading, the lessons were folded into `environment-design/references/diagnosis.md`, so these cases no longer test the skills. The next test needs fresh held-out cases (lead note, 2026-10-21).

HELD-OUT TEST SET. Do not load this file into any skill, role file, template, brief or eval prompt. Do not copy its causes or fixes into `04-first-game-stages.md` or any skill. The lead uses it once, after the skills are written, to see whether an agent that has only the skills can diagnose three real first-game failures. If the packet tool indexes `knowledge/jobs/`, exclude this file from it.

Paths: root = `C:\Users\Firew\Downloads\uterd\DestructionSimulator` (read-only). `dec` = knowledge/design/decisions.md (line = ledger row). `log/x` = knowledge/logs/x.md.

How to run a case: give the agent the "Neutral prompt" and the data it names, nothing else. Ask for (1) the most likely cause, (2) the check that proves it, (3) the fix, (4) what it will not change. Score with "Pass test". The "Wrong first guesses" list shows what a weak answer looks like.

## HC1: stage ground that looks wrong next to the buildings (owner rejection)

| Field | Content |
| --- | --- |
| Where | Stage 1, 2026-10-10. |
| Symptom (owner) | The owner walked the stage and said the area round one tower "are like two blocks high or three blocks high"; a large landform "is like sunken into the floor"; a church "has like weird grass that also is higher than the church"; the height change "is common in many spots of our map ... it's very strange" (D-143, dec:153). After the first fix the owner added that the ground need not be level, but the changes must be smooth: "we just have ... blocks or chunks where the level just changes up and down"; "it should just be blended in smoothly ... if you make it too level, it won't look ... natural" (D-146, dec:156). |
| Cause found | Not one bug. (a) Each building site had its own floor height chosen in the plan, independent of the ground round it: 10 of 15 stone sites had grass above or ground below their floor (log/2026-10-10-stage1-ground-level:16; the floors that had to be lowered are listed at :11). (b) Decorative relief added on purpose (per-column noise, rock outcrops, a one-column ridge in front of the landform) made 377 extra steps (:10, :16). (c) A tooling detail: unclaimed columns were computed from the wrong footprint and were corrected (:12); the log does not say how much of the symptom this caused. Together: 1,891 steps of at least one course; 1,084 of more than one course (707 designed relief, 377 artifacts); 993 steps of two courses or more (:16). The cause was only visible after the steps were measured per column and sorted into "designed relief" and "artifact" (:8). |
| Fix that worked | Audit first (step per column, relief against artifact, site rings, landform foot). Then blend: half-course height limit between neighbours; fixed anchors (walkway, site floors and their rings, water, cave cut); lanes and stairs rise in half steps; design artifacts switched off; site floors lowered where their ring could not blend (church 7 to 3, tower 7 to 3, cottage 5 to 3, smithy 7 to 4, house 5 to 4, watchtower 6 to 4) (:9-11). Result: every step is now one course or less; steps over one course 1,084 to 0; steps of two courses or more 993 to 0; stone sites with ground above or below the floor 10 of 15 to 0; landform foot under the ground beside it 2 to 0 (:16). Offline renders before and after; not Studio-verified; one-course steps off the lanes still need a jump, and the floor levels went to the owner as an open question (:19, :23). |
| Neutral prompt | "A walkable outdoor level has buildings, a hill and a lake. In play-test the owner says the ground height jumps up and down in chunks round several buildings, some grass sits higher than a building's floor, and the hill looks sunk into the ground. The owner does not want a flat map. You have the height data per column and the building floor heights. What is wrong, how do you prove it, and what do you change?" |
| Wrong first guesses | A bad noise setting; make the whole map flat; raise the buildings; ask the owner for a new design. |
| Pass test | Measures the height steps per column before changing anything and separates intended relief from unintended steps. Finds that site floors were set independently of the surrounding ground and that decorative noise adds steps. Chooses a smooth blend with fixed anchors, not a flat map (the owner said too level looks unnatural). Re-measures after the change and says what is not verified in the engine. |

## HC2: a colour fault that is in the render, not in the model (build review)

| Field | Content |
| --- | --- |
| Where | Stages 3, 8 and 13, 2026-10-12 and 2026-10-13. Seen three times. |
| Symptom (log) | Offline review renders of finished buildings looked wrong in colour: white trim looked grey and pastel walls looked olive (stage 3); a white marble hall looked grey, and a polish round was started whose notes include "grey not white marble" (stage 8); cream looked khaki and white looked grey (stage 13). |
| Cause found | The offline preview renderer's default ambient light (0.42) was too low for the target look. It darkened shaded faces and shifted pale colours. The model colours were correct. A stage 3 brief says: "render.py default 0.42 turns shaded walls olive" (content/stages/03-dream-house/structures/dh_house_mint/brief.md:51; also dh_mansion_gen/brief.md:52). The stage 8 verdict after the polish round: "white marble was renderer lighting" (log/2026-10-13-stage8-build-wave2:18; the polish had been launched at :31). Stage 13: "Offline renderer shows `cream` as khaki and `white` as grey: judge colour in Studio, not the sheets" (log/2026-10-13-stage13-candy-kingdoms:22); later "colours right (cream/ice read correctly in Studio)" (:48). |
| Fix that worked | Render compare images with ambient 0.72 (stage 3 log/2026-10-12-stage3-dreamhouse-build-and-placement:10; every later shop and house brief names the setting), and judge final colour in the engine with its real lighting. No model colour was changed for this. |
| Not resolved | A sibling note says a pineapple-shaped house "renders brown" where the palette says orange (log/2026-10-13-stage10-bikini-bottom:40). The log does not say whether the same cause applies. Do not assume it. |
| Neutral prompt | "You review a finished building next to its concept image using renders from a preview tool. The concept has white trim and pastel walls. Your render shows grey trim and olive walls. The palette values in the model match the concept. What do you do before editing any colour?" |
| Wrong first guesses | Change the palette values; start a polish round on colour; blame the concept image; ignore it. |
| Pass test | Checks the preview's lighting set-up (or renders a known white reference object in the same scene) before touching model colours. Compares against the engine render with the game's real lighting. Fixes the review set-up, records the setting, and leaves the palette alone unless the engine render also differs. |

## HC3: a roof cover that looks wrong from one angle although every check passed (Studio review)

| Field | Content |
| --- | --- |
| Where | House B, 2026-10-04 to 2026-10-05. |
| Symptom (log) | A building passed the full gate, the outline comparison (against its own saved draft envelope) and the joint probes. Native Studio captures from high, front and eye height then showed the porch roof cover as "separated slats": gaps between thin stacked courses that rise in steps (log/2026-10-05-house-b-integration:11; log/2026-10-05-house-b-porch:6). The same Studio session, reviewing the neighbouring building, raised a false alarm: blue strips under the roof that "intersect solid slate risers"; on inspection the one real opening was the authored chimney notch and "No broad roof/culling defect demonstrated" (log/2026-10-05-two-buildings-studio:8). |
| Cause found | The cover was made of thin horizontal layers that step up three units at a time. The data had all 210 horizontal cover cells and none of the 189 vertical riser cells that join one step to the next (log/2026-10-05-house-b-porch:7). Every earlier check looked at top-down coverage, silhouette or support: the outline score was .976679 front and back and the full gate passed (log/2026-10-04-house-b.md:21,27). None looked at the side faces of the steps from a low or oblique view. |
| Fix that worked | Add the missing riser faces: 36 thin plates forming 3 risers of 21 x 1 x 3, alternating seams, keeping the footprint, heights and the main-wall joint (log/2026-10-05-house-b-porch:8). The original failing data was kept as proof; numbers recomputed (:9, :14). Verified by data. A corrected Studio capture was NOT obtained: the retry stalled and the owner then took over the Studio review (log/2026-10-05-two-buildings-studio:13,16-17; dec:111). Report it as data-verified, Studio not verified. |
| Neutral prompt | "A building passes every automatic check and its outline matches the approved drawing at 0.97. A screenshot from a high three-quarter view shows its porch roof as a row of separate slats with gaps. A second screenshot shows thin blue lines under the main roof. Which of these are real defects, how do you decide, and what do you change?" |
| Wrong first guesses | Trust the 0.97 and call it fine; lower a threshold; rebuild the whole roof; "fix" the blue lines without checking what they are. |
| Pass test | Treats the screenshot as evidence the checks cannot overrule. Inspects the stepped layers from the angle where the gaps show and checks for missing vertical faces between levels. Checks the blue lines against the source (authored notch) before changing anything. Closes the gaps without changing the footprint or heights. Says plainly what is verified by data and what still needs a fresh capture. |
