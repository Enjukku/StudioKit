---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer level-design · claude-opus-5-5 · high · 2026-10-22

# Review: level-design books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/skills/level-design/ (SKILL.md; references/review-artifact.md; new references/plan-and-blockout.md and references/worked-examples.md; no evals/, no role file: shared skill), working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer level-design (opus, high)
looked_at_first: [
  the four book files read in full; git show df13ff4 of the old SKILL.md and review-artifact.md, and git diff df13ff4 -- .agents/skills/level-design/,
  knowledge/reference/craft/riot/universal-principles.md (UP-01..UP-20, every space/level line and applies list),
  matrix.md level-design column (96 IDs, script-extracted; all 96 have a coverage row) and the principle/apply/check/roblox_fit of all 96 (script-extracted from the topic files, read in full),
  tools: tool-modes.md; look_check.py value/silhouette/thumb --help; scene_audit.py load_probe (:92),
  V3 runs by me (scratchpad/ldrev/): the §6.2 route-table script extracted verbatim from the book on a 4-node route JSON with via points, a 12-stud climb and ledges on both margin boundaries; M1 value --compare-subjects on a 1280x720 in-scene first view (sky, ground, HUD bar, light goal tower, two competitors) and a dark-goal variant; thumb --size 844x390 with no box; silhouette --compare on 512x512 flat-key towers and a dome with and without a cast shadow on the key and with a lighting gradient on the key; the §6.7 markup one-liner extracted verbatim,
  roblox-creator-docs: StarterPlayer.yaml:243-252 (JumpHeight 7.2, visible only when CharacterUseJumpPower is false), :272-284 (JumpPower 50), :329-339 (CharacterUseJumpPower defaults to true), :358-364 (WalkSpeed 16); Workspace.yaml:458-467 (Gravity 196.2); Humanoid.yaml:640-660; greybox-your-environment.md:77 (5 studs); Lighting.yaml:389-397 (GlobalShadows); BasePart.yaml:653-659 (CastShadow),
  partner books: game-design/references/spaces.md (full), game-design/references/review.md §7 (flat-key capture definition :59), environment-design SKILL.md §1, §3 step 1, references/review.md §7 (RD5, RD9, RD12, VB5, VB13, FL1, FL7, FL11, AM1), place-reading.md PR-38, environment-craft/references/measure-captures.md §0-§1 (M1, M5, M8, M9, M10), environment-craft/references/handoffs.md:89, studio-mcp tools.md:18 and SKILL.md C-08, preproduction/references/handoffs.md:23,
  .agents/workflows/jobs/job-stage.js:243-251, :386-396, :480-500, :589-593 (read only),
  game-concept/evals/briefs.md §5 (level review eval, read as the agent would)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C8 V12 + V3; C3 (the landmark-uniqueness check passes falsely in the common Studio case)",
     where: "review-artifact.md:76 (§6.1 'Flat-key landmark captures'), :101-104 (§6.4 recipe and its false readings); used by :45 (C4), :135 (LD13), plan-and-blockout.md:52 (grey read pass 'Landmarks'), SKILL.md:86 (§7 #5 check)",
     expected: "V12: the silhouette recipe is run on the exact input form the book prescribes (a Studio capture of a landmark in front of a key Part at the game camera, under the place's light) and its silent false readings are listed; the capture setup removes what the key cannot separate",
     observed: "The capture is 'each landmark alone in front of a flat key backdrop Part, same game-camera angle and distance'. Studio's default lighting casts the landmark's shadow onto that Part (or onto the ground in front of it). A shadow is not key colour, so look_check counts it as part of the outline with no error. Because the sun is fixed in the world while the camera is set the same way relative to each landmark, two landmarks get differently placed shadows, which lowers their IoU. The known-limits list names only key-colour keying and frame-edge contact; the coverage run (table d) used drawn flat images, not a capture under scene light, and the capture is not marked 'probe first'. A false pass is never looked at: the eye check in §5 and §6 is only for failing or borderline numbers",
     evidence: "My run, look_check.py silhouette A --compare B, 512x512 magenta key: the same tower with its cast shadow to the right vs to the left IoU 0.778 (below the 0.8 limit: 'different silhouettes', a false pass); the same tower with vs without the shadow 0.603; bbox_px widened from 91 to 126 px; no error, verdict 'measured'. A 25 % light falloff on the key gave invalid-mask (that case errors loudly). Lighting.GlobalShadows (Lighting.yaml:389-397) and BasePart.CastShadow (BasePart.yaml:653-659) exist to switch shadows off",
     smallest_fix: "In §6.1 and §6.4: the flat-key capture is taken with shadows off (Lighting.GlobalShadows false, restored after the capture; probe first) and with the key filling the whole frame border, including the ground under the landmark (point to the flat-key capture defined in game-design/references/review.md §7 instead of restating it). Add to §6.4's 'wrong number with no error': 'a cast shadow on the key joins the outline (review run: the same tower, shadow right vs left, 0.78)'. Compare bbox_px with the landmark on the still for every pair, not only in the key-colour case. Add a proposal row for game-design review.md §7 (the same shadow rule in its flat-key definition)"}
  - {id: F2, class: blocking, check: "C5 (an old rule was narrowed, not kept)",
     where: "SKILL.md:42 (L-02), review-artifact.md:45 (C4), :72 (§6.1 'One decision view per fork ... facing the approach direction'), plan-and-blockout.md:51 ('Forks ... in the direction of the intended move'); coverage/level-design.md:181 (L-02 'sharpened') and :202",
     expected: "The old books required landmarks and cues to be readable from every real approach direction: df13ff4 SKILL.md:33 (L-02 'distinguishable from the real approach directions and camera') and df13ff4 review-artifact.md:37 (check 4 'cues distinguishable from the real approach directions and camera')",
     observed: "The new L-02, C4, the capture set and the grey read pass check each fork from one direction (the intended move). Return trips, which L-08 makes part of the loop, and the second approach to each fork are no longer checked; the flat-key silhouette comparison uses one camera angle per landmark. The coverage table calls the change 'sharpened' and does not list the loss",
     evidence: "job-stage.js:246 asks the studio operator for 'a player-eye capture from each decision point in both directions' and :591 asks the design review for 'landmark read at every decision point in both directions', so the workflow still expects what the book dropped; SKILL.md:48 (L-08 return trips)",
     smallest_fix: "Add 'from each direction players approach it (both ways at each fork, return trips included)' to L-02 and C4; §6.1: 'one decision view per fork per approach direction'; plan-and-blockout §4 Forks row: 'from each approach direction'; correct the coverage row"}
  - {id: F3, class: blocking, check: "C1 + C3 + V11 (coverage rows that claim a check the books do not carry)",
     where: "review-artifact.md:45 (C4), :135 (LD13), :129 (LD8), :55 (C14); coverage/level-design.md:114 (WL-23), :43 (GD-13), :226 (environment-designer proposal 'adopted ... C4 ... (silhouette, symbol)')",
     expected: "WL-23's check (an identity symbol per zone or team visible from its entry at the game camera, large enough for a phone) and GD-13's check (the same attack always has the same tell, compared on captures) each have a review or self-review line, as the coverage table states",
     observed: "WL-23: the identity symbol is only a standard (L-02, SKILL.md:42). C4 checks landmark height, forks and silhouette, not the symbol; LD13 does not name it. The coverage row points at C4's 'silhouette comparison', which is a different finding (CF-14 / WL-23 conflated). The environment designer's adopted proposal row asked for exactly this check. GD-13: the rule is in §3 (:34 'the same attack gives the same tell'), but the coverage row's check location C14 is failure cost and retry, and LD8 (encounters) does not list the tell",
     evidence: "C4 text :45; LD8 text :129; LD13 text :135; library WL-23 check 'List per zone: at least one identity prop visible from its entry at the game camera'; GD-13 check 'the same attack always has the same tell (compare captures)'",
     smallest_fix: "C4: add 'each zone or team identity symbol shows from its entry at the game camera on a phone viewport (1 entry capture per zone)'. LD8: add 'the same attack gives the same tell (two uses compared on the partner's captures)'. Correct the two coverage rows"}
  - {id: R1, class: recommendation, check: "V5 (worked example arithmetic)",
     where: "worked-examples.md:16; plan-and-blockout.md:76",
     expected: "The pacing numbers in the example agree with the segments listed, and 'gap between peaks' has one definition",
     observed: "Segments rest 6, build 9, peak 4, rest 7, build 12, peak 6, rest 5, climax 10: the gaps between peaks are 19 s and 5 s (end to start) or 23 s and 11 s (start to start), not '16 s and 23 s'. The pacing map totals 59 s, but the spiral is computed at 81 s and timed at 94 s in the next bullet. An agent copies the example's method",
     evidence: "cumulative times 0-6, 6-15, 15-19 (peak), 19-26, 26-38, 38-44 (peak), 44-49, 49-59 (climax)",
     smallest_fix: "Correct the gaps (for example '19 s and 5 s'), make the segment sum match the route time or say the map covers only part of the spiral, and define a gap in plan-and-blockout §6 as the end of one peak to the start of the next"}
  - {id: R2, class: recommendation, check: "V1 (image budget against the inputs the checks name)",
     where: "SKILL.md:29 (budget: first view, each fork, busiest moment, top-down, one per hazard); review-artifact.md:52 (C11 '1 scale shot per area'), :50 (C9 'captures along the route'), :47 (C5 'walk captures per beat'), :28 (§2 approach, decision and after-commit view at each key node), :60 (C19 key views at both settings), :76 (flat-key per landmark)",
     expected: "The budget line names every image the checks ask for, or says which captures are measured only and looked at only when their number fails",
     observed: "The checks ask for about three to four times as many images as the budget names. LD18 asks for 'images used against the budget', so the agent either breaks the budget or leaves checks Unproven with no rule for choosing",
     evidence: "count for a 6-node stage with 3 forks, 4 landmarks, 5 areas and 4 teaching beats: about 40-50 captures against about 10 named in the budget",
     smallest_fix: "In §3, split the captures into 'looked at' (the current list) and 'measured only' (flat-key, scale shots, both settings, route captures for C9: looked at only when a number fails or is borderline), and name the per-check image count in §6.1"}
  - {id: R3, class: recommendation, check: "C8 V3 (a screening aid's known limits)",
     where: "review-artifact.md:97 (§6.3 pass rule), plan-and-blockout.md:50, :47",
     expected: "The known false readings of the focus ranking include a dark goal against a light sky or wall",
     observed: "The pass rule is 'ranks first by median or has the widest spread'. A dark landmark silhouetted against a bright sky has the strongest contrast in the frame but ranks last and has no spread, so it fails. The eye check catches it, but the agent's fix note would then say 'brighten the landmark'",
     evidence: "My run, dark goal variant: goal p50 0.017, spread 0.0, ratio_to_ring 6.07 (the highest of the three subjects), rank_by_median [crates, stall, goal]",
     smallest_fix: "Add to §6.3's false readings: 'a dark goal silhouetted against a light sky or wall fails by rank; read ratio_to_ring and brighter_than_ring'"}
  - {id: R4, class: recommendation, check: "V11 (an adopted proposal narrowed) + C7",
     where: "review-artifact.md:58 (C17 'team and competitive maps; else n/a')",
     expected: "Game-designer proposal row 21 and spaces.md §4 apply 'every height change is intentional' and 'collision as simple as the visible shape' to every map (for a third-person phone game: 'no surprise height hides a threat from the camera')",
     observed: "Both lines sit inside C17, which is n/a outside team and competitive maps, so most Roblox maps (simulators, obbies, PvE, hubs) never check them. Stuck spots are still caught in the walk test (LD11)",
     evidence: "spaces.md:25-27; proposals/game-designer.md:21",
     smallest_fix: "Move the intentional-height and simple-collision clauses into C10 or C3 (all maps); keep spawn-to-contact, neutral parity and cover counters in C17"}
  - {id: R5, class: recommendation, check: "V10 + proposals (stale partner references)",
     where: "game-design/references/spaces.md:1 ('route graph, 14 checks, walk-throughs'); .agents/workflows/jobs/job-stage.js:591 ('the level-design 14 checks')",
     expected: "A proposal row for each file that still names the old 14-check review (both files are outside this maker's books)",
     observed: "proposals/level-design.md has no row for either; a reviewer that the workflow briefs with 'the 14 checks' stops at C14 and skips C15-C19",
     evidence: "grep for '14 checks' in .agents/",
     smallest_fix: "Add two proposal rows: spaces.md:1 → 'the fixed checks (C1-C19)' (for the game-designer book owner) and job-stage.js:591 → the same (workflow, G3)"}
  - {id: R6, class: recommendation, check: "V10 (hand-off to the environment designer)",
     where: "plan-and-blockout.md:44 (the blockout brief)",
     expected: "The brief carries what the environment designer's intake expects from the game designer: the material-to-rule table, the orientation conventions and the intentional-height list (environment-design SKILL.md:34; environment-craft/references/handoffs.md:89; environment-design/references/review.md FL11)",
     observed: "The brief lists per-node geometry, the job card, route table, teaching sheet and pacing map, but not these three, which C18, C2 and FL11 check",
     evidence: "environment-design SKILL.md:34 intake list",
     smallest_fix: "Add 'the material-to-rule table, the orientation conventions and the intentional-height list (spaces.md §3, §4, §6)' to the brief"}
  - {id: R7, class: recommendation, check: "V6 (one rule, one place)",
     where: "SKILL.md:49 (L-09 last sentence), :56 (L-16), :58 (L-18), parts of :42 (L-02) and :43 (L-03)",
     expected: "Rules the game designer owns live in game-design/references/spaces.md and the level book points to them, as it already does for L-17 and the walk limits",
     observed: "The dead-boundary risk-and-reward, items 30-50 % hidden, one treatment per interactive type, one material per rule and the identity symbol are restated from spaces.md §5-§7. They agree today; they will drift",
     evidence: "spaces.md:32, :45-47, :39",
     smallest_fix: "Keep the level-specific part of each row and replace the restated sentence with '(spaces.md §n)'"}
  - {id: R8, class: recommendation, check: "V2 + V12 (named tool on the wrong input form)",
     where: "plan-and-blockout.md:24 ('route JSON drawn by the markup recipe in review-artifact.md §6.7')",
     expected: "A drawing method that takes the options pass's real input (route JSON in studs, no capture yet)",
     observed: "The §6.7 one-liner needs a base image and a marks JSON in image pixels ('arrows', 'circles'); route JSON has studs and no such keys, and the options pass has no capture. It fails with an error (not a silent number)",
     evidence: "§6.7 recipe text :114; my run of the verbatim one-liner wrote the PNG only with a base image and pixel marks",
     smallest_fix: "'Python + Pillow on a blank canvas, x/z in studs to pixels at one fixed scale for all three options'"}
  - {id: R9, class: recommendation, check: "C1 (CD-26) + C2 consistency",
     where: "SKILL.md:92 (§7 #10 check 'names a story fact and the mood (C12)'); review-artifact.md:53 (C12)",
     expected: "C12 checks what §7 #10 says it checks: the mood against the job card's personality words (CD-26's check)",
     observed: "C12 checks the theme and one story fact; no mood or personality",
     evidence: "C12 text :53; plan-and-blockout.md:17 (personality in 3-5 words)",
     smallest_fix: "C12: add 'and the mood, compared with the job card's personality words'"}
  - {id: R10, class: recommendation, check: "C1 (GD-25 half landed)",
     where: "plan-and-blockout.md:12 (job card 'Conflict sentence')",
     expected: "GD-25's check: the conflict sentence and the objective's story reason exist before blockout",
     observed: "The job card has the conflict sentence only; the story reason is in spaces.md §2 and not pointed to",
     evidence: "spaces.md:13",
     smallest_fix: "Conflict row: 'one sentence per mode and the objective's reason in the world's story (spaces.md §2)'"}
  - {id: R11, class: recommendation, check: "C4 (Studio step not marked)",
     where: "review-artifact.md:73 (§6.1 'Top-down')",
     expected: "Like the other Studio steps that have no tested probe, the top-down capture is marked 'probe first'",
     observed: "screen_capture with a camera position is a real mode (studio-mcp tools.md:18), but a straight-down look-at and the camera restore (C-08) are untested; the maker's own proposal row asks studio-mcp for this probe",
     evidence: "proposals/level-design.md:21",
     smallest_fix: "Add 'probe first; restore the edit camera (studio-mcp P-05)' to the row"}
keep: [
  the level job card with measured movement metrics, smallest gameplay object, stop criteria and pass budget (plan-and-blockout §1),
  the layout options pass: three hooks, warm-up labelled, one atypical, pick with reasons, diagrams only (§2),
  the jump correction: the default character uses JumpPower 50 (about 6.4 studs, inference), 7.2 only when CharacterUseJumpPower is false, measured on a ladder; verified against the mirror. The old 7.2 would have passed 6.4-7.2-stud ledges as climbable,
  the route JSON and route-table recipe: my verbatim run matched hand checks, ledge margins correct at both boundaries (5.4 ok / 5.5 CHECK; 7.4 ok / 7.3 CHECK), false readings listed, played walk is the truth,
  the teaching sheet (inference and the action that shows it) and the pacing map with frequency and difficulty as separate dials,
  19 fixed checks each with an input, Unproven when the input is missing, every check re-rated every round, no totals,
  the screening-aid rule (failing or borderline numbers checked on the still; a passing number never overrules a capture),
  worked example 1: the problem behind the arrow note, cause before fix, contrast before detail,
  the core principles table: all 20 principles stated for levels, UP-09 and UP-19 marked 'in part' with reasons, no contradiction with the master,
  the proposals file (WL-29 library fix with doc lines, studio-mcp probes, route-graph template, route_times tool, look_check key warning, hand-off fields)
  ]
verdict: fix-first
</spec>
```

## Result per check
| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | fail (2 of 96 rows) | All 96 tagged IDs have a row; 18 rejections have sound reasons (owners verified in the environment books, for example PR-38, E-12, E-19, FL4, VB1, VB7). Failed: WL-23, GD-13 (F3). Half-landed, recommendation: CD-26 (R9), GD-25 (R10). The 17 untagged rows I spot-checked land as stated |
| C2 core principles | pass | §7 has all 20 principles with a level example and a check with its input; nothing contradicts the master; UP-09 and UP-19 are marked 'in part' with a reason. The pointer in #10 overstates C12 (R9) |
| C3 self-review | fail | LD1-LD18 and C1-C19 run on our tools and named captures. Missing lines: identity symbol, same tell (F3). The landmark-uniqueness check passes falsely in the common Studio case (F1) |
| C4 kit rules and engine | pass | Engine claims verified in the mirror (WalkSpeed 16, JumpPower 50, UseJumpPower true, Gravity 196.2, greybox 5 studs). Tool modes are real (look_check value/silhouette/thumb flags, scene_audit.load_probe, screen_capture camera position, character_navigation, inspect_instance). Proposals only, no stage edits, PROPOSAL labels, rights rule kept. Top-down not marked 'probe first' (R11) |
| C5 nothing valuable lost | fail | Every old row is kept, moved or sharpened, and the 7.2-stud jump is correctly replaced. Exception: landmarks and cues from every real approach direction (F2). Old check 3's 'optional alternatives found' is weaker but is covered by node field 10 and the missed-clue walk-through |
| C6 fixed rules | pass | Only the four book files plus coverage and proposals changed for this role; SKILL.md 103 lines; description 394 characters; sections 1-6 and §1-§5 not renumbered (checks keep their numbers as C1-C14); J018 phrase in all four headers; no Riot names, library IDs or transcript lines in the bodies (the J018 evidence tag follows the kit's convention); no tips section; LF endings; no evals/ |
| C7 better work | yes, clearly | See below |
| C8 brief v2/v3 | fail | V12/V3: F1 (silhouette recipe never run on its real input form). V1: R2. V2: R8. V6: R7. V7: steps, rules and self-check end at about 15.3 KB, §1 tells the agent to re-read §7 after a compaction. V8: findings became sheets (job card, option sheet, route table, teaching sheet, pacing map), a brief (blockout brief) and review checklists on named captures. V10: R5, R6. V11: adopted with reasons; one row narrowed (R4). V13: the 9-line route script is borderline 'a few lines'; a tested tool is proposed (accept) |

## C7: will the agent make better work?
I read the books as the game designer would for eval brief 5 ('our lobby, top-down and part coordinates; new players don't find the shop'). The old books gave a job card, 14 bare checks and 'measure walk times', with no method, no inputs and a wrong jump number. The new books lead to a better review. The agent writes the job card. It builds the route JSON and gets edge times and OVER flags from a tested script. Worked example 1 makes it look for the problem behind the 'add an arrow' note: the cue is off-camera on the approach, not too small. It rates C2 as Unproven until a first-view capture arrives instead of guessing, and it ranks fixes with contrast before detail. For a new stage, the options pass, teaching sheet, pacing map and blockout brief give the environment designer and the progression designer real inputs that did not exist before.

Weak spots:
- The landmark-uniqueness measure gives false passes in the common Studio case (F1). Landmarks are checked from one direction only (F2).
- Two claimed checks are missing (F3).
- The image budget does not match the captures the checks ask for, so the agent has no rule for which checks to leave Unproven (R2).
- About a third of the L-rows restate spaces.md (R7). The book stack (18 L-rows, 19 checks, 18 self-review lines, 20 principles) is long, but each layer has a different job, and the scope line in §7 (review-only runs LD15-LD18) keeps a review job small.
