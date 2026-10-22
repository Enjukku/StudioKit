---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer film-director · claude-opus-5-5 · high · 2026-10-22

# Review: film-director books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/film-director.md (body) + .agents/skills/film-direction/ (SKILL.md, references/ incl. new beats-and-timing.md, worked-examples.md) + .agents/skills/film-craft/ (SKILL.md, references/; evals/ not part of the work), working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer film-director (opus, high)
looked_at_first: [
  all 14 book files read in full (role body, both SKILL.md, 7 + 6 references), then git diff df13ff4 and git show df13ff4 of the role file and both SKILL.md (removed lines walked one by one),
  knowledge/reference/craft/riot/universal-principles.md (master, UP-01..UP-20, statements, cinematic lines and general checks),
  knowledge/reference/craft/riot/matrix.md (film-direc column: 76 findings, script-extracted) and principle / apply / check of all 76 in the topic files,
  stage2-brief-v2.md (V1-V11), tool-modes.md, job-card.md (fixed list, J018-D2..D4),
  tools/art/look_check.py (value / silhouette / thumb / palette --help and the value_stats and compare_subjects source, lines 555-597, 799-831), tools/film/shotlist.py (check / log-diff / blender / diff / luau --help),
  partner books read-only: animation-design (SKILL.md, references/game-timing.md), animation-craft SKILL.md, sound-design (SKILL.md S-133, references/review.md R-43, R-54, cue-card.md), vfx-design (SKILL.md flash safety, references/camera-and-screen.md), platform-policy/references/rules.md §A, game-design systems-economy.md §no near-miss,
  roblox-creator-docs: GuiService.yaml (ReducedMotionEnabled), enums/FieldOfViewMode.yaml,
  film-craft/evals/briefs.md (E1, E2 used for the C7 read),
  my own tool runs on synthetic samples (scratchpad fdrev-*: in-scene frame with a thin lit hero and a mid-grey lamp, a dark frame with a small white-hot lamp, letterboxed frame, hero mask, anchor A-pose vs same figure running vs a wider figure in A-pose, a 5 x 45-frame shot list and a sparse playback log)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C8 V3, C3",
     where: ".agents/skills/film-craft/references/review.md:100 (B-06 rank), :112 (B-18 'brightest named region moves'), :125-126 via R-09; film-direction/SKILL.md:129 (§7 #3 check); film-craft/references/blender-previs.md:73 (Measures)",
     expected: "The B-06 / B-18 rank answers 'is the subject the brightest named region, and does no stray lamp, sky patch or white prop out-shine it?' on the real inputs: a shaded key frame or a Roblox capture with a figure, lamps and sky, where each named region is a --box (compare-subjects takes boxes only, and on captures boxes are all there is)",
     observed: "The lines read the tool's rank_by_median. look_check.py compare_subjects (source :574-597) takes the median of every pixel in each box. A figure fills well under half of its bounding box, so its median is the background's; a small light inside a looser box also reports the background. The rank is then wrong in both directions, with verdict 'measured' and no error. The book gives no box rule (tight box, or which statistic to read); the maker's V3 run used hand-tight boxes, so the trap did not show",
     evidence: "my runs: (a) thin lit hero (luminance 0.80) in its 81x141 bbox + a mid-grey lamp (0.40): rank_by_median = [lamp, hero] (hero p50 0.030, p95 0.798): false FAIL. (b) small white-hot lamp (0.997) in a 56x56 box + a mid hero block (0.27): rank_by_median = [hero, lamp] (lamp p50 0.021, p95 0.997): false PASS, the exact stray-light case B-06 exists to catch. Ranking by each region's p95 from the same JSON gives the right order in both runs. The same hero measured with --mask gives subject p50 0.798, subject/ring 11.1 (right)",
     smallest_fix: "In review.md B-06 and B-18 (and the measures bullet of blender-previs.md §7): 'rank the named regions by each region's p95 from the --compare-subjects JSON, not by rank_by_median; draw each box tight around its region (a box that is mostly background reports the background's median); the subject's subject/ring ratio comes from the --mask run where a mask exists.' On Roblox captures say where the box comes from (for example the subject's screen box from Camera:WorldToViewportPoint of its bounding-box corners through the MCP, or a hand-drawn tight box, recorded). Add a proposals row for look_check.py: --compare-subjects with per-subject masks and a selectable rank statistic"}
  - {id: F2, class: blocking, check: "C8 V3, C3, C2",
     where: ".agents/skills/film-craft/references/review.md:106 (B-12 'silhouette --compare against each character's approved anchor render'); film-direction/SKILL.md:137 (§7 #11 check, same command)",
     expected: "A check that the cutscene cast is the in-game cast (same model, proportions, identity anchors) and gives a wrong-cast answer only for a wrong cast",
     observed: "silhouette --compare aligns two masks by bbox height and reports IoU, so it measures pose and view as much as identity. A cutscene key frame shows the character in an acting pose at a shot camera; the anchor render is a sheet pose at the anchor camera. The same character scores low and a different character in the anchor's pose scores high. The maker did not run B-12 (coverage table d has no B-12 row)",
     evidence: "my runs: anchor A-pose black-fill vs the same figure running: IoU 0.342; vs a different, wider figure in the A-pose: IoU 0.893. Both 'measured', no error",
     smallest_fix: "B-12 and §7 #11: replace the compare with (1) a doc check that each cast member is the approved in-game rig and model (asset or file id equal to the anchor record), and (2) where a silhouette compare is wanted, render the cutscene rig in the anchor's pose at the anchor's camera and compare that pair; keep palette --roles. B-14's still-vs-clip compare stays, with 'both black-fills from the still's camera' written in"}
  - {id: R1, class: recommendation, check: "C8 V10",
     where: ".agents/skills/film-direction/references/beats-and-timing.md:33 (last sentence of the sync rule); knowledge/jobs/J018-riot-craft/proposals/film-director.md:27",
     expected: "The hand-off text agrees with the partner books as they are now",
     observed: "'The sound-designer's book governs the sound side until its window is aligned with this one (J018 proposal); a measured offset outside this window is reported as MEASURED, not FAIL' and the proposals row ('today −35 to +100 ms') are stale: the wave-2 sound-design rebuild already states the same window (sound-design/SKILL.md:111 S-133 '0 ... up to about 40 ms ... never more than one frame before'; references/review.md:84 R-43 'pass only from −16.7 ms to +40 ms'; cue-card.md:33). The clause also puts a job id into the body and makes R-04 softer than the partner's review line",
     evidence: "grep of sound-design for '40 ms' (S-133, R-43, R-54, cue-card row 22); the −35/+100 window now survives only in sound-design/evidence/",
     smallest_fix: "Delete the last sentence of beats-and-timing.md:33 once the sound-designer rebuild passes its review (or today, with a note to the lead); withdraw proposals row 27"}
  - {id: R2, class: recommendation, check: "C5, C7",
     where: ".agents/skills/film-craft/SKILL.md:43 (step 12) and :91 (self-check 'Review'); role file :39 (step 8); film-craft/references/review.md:7-13 (§1 four passes)",
     expected: "The capture review keeps its four passes (continuity, emotional readability per shot, sound-picture, interaction) or says which §6 lines replace each",
     observed: "Old step 8 and the old self-check named 'four passes'; the new step 12 and self-check name the §6 lines, the §2 table and the defect table only. §1 is still in review.md but nothing sends the agent there. The per-shot 'intended read vs what the capture gives' on the final captures is now covered only by numbers (R-09 re-runs B-06/B-07) and the §2 table. The unchanged eval E1-6 grades 'four passes and the pass/fail table'",
     evidence: "git show df13ff4:.agents/skills/film-craft/SKILL.md step 8 and self-check line 7; film-craft/evals/briefs.md:14 (E1-6)",
     smallest_fix: "Step 12: add 'the §1 four passes, run as the §6 lines (continuity B-02/P-08, readability: each shot's first-second read on its R-09 capture, sound-picture R-04, interaction R-02/R-05/R-07)'; the self-check line reads 'four passes, §6 lines and the §2 table'"}
  - {id: R3, class: recommendation, check: C5,
     where: ".agents/roles/film-director.md:54-66 (partner table)",
     expected: "Every partner the old role could ask is kept",
     observed: "The old line listed 'modeler for props and set pieces (a new cast without a usable rig is a character job first)'; the new table has no modeler row (the cast clause survives at :69). A cutscene prop or set piece (the gate that bursts, the boss's club) has no named ask",
     evidence: "git show df13ff4:.agents/roles/film-director.md:42",
     smallest_fix: "Add a row: modeler | hero props and set pieces at true scale, with their identity anchors and named parts for the moments that move them | at readiness"}
  - {id: R4, class: recommendation, check: C5,
     where: "film-direction/SKILL.md:54 (D-02), :58 (D-06), :68 (D-15), :77 (D-25); coverage table c row for D-01..D-29 ('detail kept in the references')",
     expected: "Each tightened D-row keeps its old content in the row or in a reference, as the coverage says",
     observed: "Four old clauses are in neither place: D-02 '\"No cuts\" does not mean freedom'; D-06 'if both read equally, choose by style and cost, not by \"motion is better\"; a move hurts when it hides acting, loses a landmark or fights a subtitle' (shot-language §4 keeps only 'the static alternative'); D-15 '\"brighter\" is not an instruction'; D-25 'progression never hangs on a visual cue'",
     evidence: "git show df13ff4:.agents/skills/film-direction/SKILL.md:48, :52, :61, :71; grep of the current books for each phrase: no hit",
     smallest_fix: "Add the D-06 sentence to shot-language.md §4 (after 'the static alternative'), the D-02 clause to game-cinematics.md §1, the D-15 clause to acting-light-sound.md §2 value-plan bullets, and the D-25 clause to game-cinematics.md §2 (the essential-objective bullet); correct the coverage row"}
  - {id: R5, class: recommendation, check: "C8 V6",
     where: "sync window numbers: beats-and-timing.md:33, film-direction/SKILL.md:91 (D-39), roblox-assembly.md:35, review.md:120 (R-04), role file :46; flash cap: SKILL.md:93, :104, :146, game-cinematics.md:29, review.md:126, role file :47; confirmed outcome stated in about 9 places",
     expected: "One rule, one place; other places point to it",
     observed: "The sync window (0 to about +40 ms, never more than one frame early) is written out with its numbers in 5 files; the 3-per-second flash cap in 4 files (6 lines); vfx-design owns the flash rule (design 2, never above 3, no saturated red flashes) and the film lines carry only part of it",
     evidence: "grep counts over the 14 book files",
     smallest_fix: "Keep the numbers in beats-and-timing.md §4 (sync) and in vfx-design (flashes); D-39, roblox-assembly §3, R-04 and the role file say 'the sync rule (beats-and-timing §4)'; D-41, §5, game-cinematics §2 and R-10 say 'the vfx-design flash rule'"}
  - {id: R6, class: recommendation, check: "C3, C8 V1",
     where: ".agents/skills/film-craft/references/review.md:126 (R-10 flash count)",
     expected: "A line the agent can run with its inputs inside the image budget",
     observed: "'flashes per second counted on a frame strip at a known rate ... (manual count)' with input 'img 4 + num'. A known-rate strip exists only for the Blender animatic (Studio MCP captures are single stills); a manual count over 30 frames per second of footage is far outside img 4",
     evidence: "review.md:126 vs §7 budget :133; studio-mcp gives stills; the maker's own proposal row 22 (flash_count tool)",
     smallest_fix: "R-10: 'on the animatic rendered at the shot-list rate: per-frame mean luminance by a short script (a measure, labelled not verified (measured offline)), count large jumps per rolling second; on Roblox: not verified without a device recording'"}
  - {id: R7, class: recommendation, check: "C7, C8 V1",
     where: ".agents/skills/film-craft/references/review.md:133 (§7 maxima); film-craft/SKILL.md:32, :34",
     expected: "The light-check rule (J005-D8: images only where a number fails, plus a few key cases) and the brief's own cap decide when they are lower",
     observed: "The §7 maxima add up to roughly 25-30 images for a 5-shot sequence with all endings (3 option sheets, 4 strips, 3 black-fills, 2 stills, a board sheet, 5 key captures, 2 per ending, 4 access). The eval brief E1 caps the job at 8 images. Nothing says the brief's cap wins or what to drop first",
     evidence: "film-craft/evals/briefs.md:6 ('Max 8 images'); memory and J005-D8 wording",
     smallest_fix: "One line in §7: 'the brief's image cap wins; cut in this order: light-variant strip (numbers only), option sheets to one combined sheet, black-fills to the reveal frame, ending captures to finish + skip'"}
  - {id: R8, class: recommendation, check: C6,
     where: "film-direction/references/game-cinematics.md:67; film-craft/SKILL.md:68 (C-20 evidence 'J018 tool runs'); shot-list-format.md:38 ('in J018'); beats-and-timing.md:33 ('J018 proposal')",
     expected: "Book bodies in the agent's own voice without job citations; a studio method not filed as a first-game lesson",
     observed: "The new 'Pitch the moment as the experience' row sits in §5 'First game's lessons' with certainty 'studio method (J018)'; three more body lines cite J018",
     evidence: "the lines above",
     smallest_fix: "Move the pitch row to game-cinematics §2 or the D-29 owner line (no job id); C-20 evidence 'O'; shot-list-format:38 'found by running them on sample files'"}
  - {id: R9, class: recommendation, check: "C8 V3",
     where: ".agents/skills/film-craft/references/roblox-assembly.md:35; handoff-briefs.md:20 (engineering row); beats-and-timing.md:32",
     expected: "The log engineering writes matches the ids log-diff reads",
     observed: "The books name cuts 'shot:<id>' (the Blender marker form) and ask for a log of shot starts, but log-diff matches bare shot ids ('A'); a log written with 'shot:A' lists every shot as 'planned, not logged' and 'logged, not planned'",
     evidence: "my run: log with shot:A, shot:B: 'planned, not logged: A, B, C, D, E ...; logged, not planned: shot:A, shot:B'",
     smallest_fix: "roblox-assembly §3: 'log ids are the shot ids as in the file (A, B, ...) and the cue ids as in cues[].id; animation markers by the animator's names'"}
  - {id: R10, class: recommendation, check: "C1, C2, C3",
     where: "review.md R lines (sell list), :112 (B-18 'during a build motion converges'), film-direction/SKILL.md:141 (§7 #15)",
     expected: "CD-02's check (each sell-list item pointed to in the result); CF-10's check with an input a stills-only agent has; UP-15's 'do not be precious' part",
     observed: "The sell list is checked only at the options pick (P-04), never on the captured key frames; B-18's convergence clause names no frames (a single value-strip image cannot show motion); §7 #15 has cheap stages and frozen gates but not 'let go of your own idea when a better one appears, and never reopen a closed door without a new decision'",
     evidence: "CD-02 check (character-design.md); CF-10 check 'frame sequence: tracked particles move toward the focus'; UP-15 principle",
     smallest_fix: "R-13 or R-09: '+ each sell-list item is pointed to in a captured key frame'; B-18: 'convergence: 2-3 frames of the build, or the actor and emitter paths from the Blender data'; §7 #15: '+ a better option replaces mine without a fight; a closed door reopens only by a new owner decision'"}
keep: [
  the stage order options -> shot list with picture plan -> blocking strip -> value pass (light variants, grayscale strip, then colour) -> boards on the blocking stills -> timed animatic -> briefs -> animator blocking check -> Roblox (film-craft §3),
  the per-stage self-review lines with named inputs and image budgets (review.md §6-7) and the 'say what each input can prove' rule,
  beats-and-timing.md: the tell/build/beat/peak/result grammar with failure modes, rhythm and one climax, the marker contract and sync rule, confirmed outcomes,
  shot-language.md §5 read-order table and 'find the missing contrast', and §7 stills from a cinematic,
  acting-light-sound.md performance sheet, adjectives as pose changes, pushed moments on a believable base, the value plan per beat table,
  the partner 'ask for, and when' table in the role file and the handoff-briefs rows (consistent with the animator's game-timing table and check-in),
  the honest 'what the commands do not judge' notes in shot-list-format.md §2 and the trap notes in blender-previs.md §7,
  the five worked Roblox examples, the §7 core principles table (each row: rule, own example, check with input),
  the proposals file (tool rows, template rows, G3 recipe and workflow rows with reasons)
  ]
verdict: fix-first
</spec>
```

## Result per check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass | 76 of 76 tagged findings have a row (script against matrix.md); every landed-in location opened; rule and check carried in all 76; 1 rejection (SD-29, the sound-designer's craft) and 2 partials (GD-25, WT-05) soundly reasoned. 0 rows failed. Rows whose check runs through the B-06/B-18 rank (LC-12, CF-11, CF-13, VH-06, VC-04) inherit F1. Small gaps: R10 |
| C2 core principles | pass with F2 | `film-direction` §7 (the skill loaded first) states all 20 UPs for the craft, each with its own example and a check with its input; no contradiction with the master. The §7 #3 and #11 checks inherit F1 and F2; UP-15's "do not be precious" part missing (R10) |
| C3 self-review | fail | Every checkable finding has a line in `review.md` §6 with its input; two lines give wrong answers on their real input (F1, F2); R-10 input not runnable as written (R6) |
| C4 kit rules and engine | pass | No conflict with AGENTS.md, rules/, J018-D2..D4; engine claims checked (`GuiService.ReducedMotionEnabled`, `FieldOfViewMode.Vertical`); every tool mode named exists (`--help` and source) |
| C5 nothing valuable lost | pass with recommendations | Diff walked; the D-rows' detail moved to the references as claimed except four clauses (R4); the modeler ask dropped (R3); four review passes no longer named in the steps (R2) |
| C6 fixed rules | pass | Only the film books, the coverage and proposals files changed; role frontmatter (lines 1-10) byte-identical to df13ff4; SKILL.md 146 and 94 lines; descriptions 379 and 388 characters; no section renumbered (new §7 in film-direction, §7 in shot-language and blender-previs, §6-7 in review.md appended; steps inside §3 reordered, which the owner allowed); J018 phrase in every changed file's header and the role comment; no Riot names, library ids or transcript lines in bodies; no tips section; evals unchanged; LF endings. Minor: J018 cited in four body lines (R8) |
| C7 better work | better, with two measuring traps | See the judgment below |
| C8 brief v2 | fail on V3 | V1 pass (R6, R7 small); V2 pass; V3 fail (F1, F2; R9); V4 pass (paid random reveal follows game-design and platform-policy); V5 pass; V6 recommendation (R5); V7 pass (steps, rules and self-check before 18 KB in both skills; §7 at 19.5 KB with the re-read note in §1); V8 pass (performance sheet, value plan, picture plan, partner asks); V9 pass; V10 pass with one stale clause (R1); V11 pass (the animator's still row adopted) |

## Better work (C7)
Read as the agent at the start of eval E2 ("the boss entrance feels flat") and E1 (the flooded observatory reveal). The old books had a strong runtime and continuity spine and almost no picture craft: five composition bullets, no value plan, no timing grammar, no options stage, and a review that watched clips the agent cannot watch. The new books make the agent write a premise, hook and sell list; try 2-3 greybox options at equal finish; plan a first-second read, read order and value key per shot; block and value-check on proxies before any board; time each key beat as tell, build, beat, peak, result on one marker list; brief each partner with what it needs and when; and check its own work stage by stage with named inputs. On E2 the agent now names metronomic cuts, even lighting and effects-before-layout as well as the old defects, and proposes contrast and timing fixes. The weak spots: two measuring lines give wrong answers with no error (F1: rank by box median; F2: silhouette IoU against an anchor); a stale sync clause (R1); the four review passes dropped from the steps while the unchanged eval still grades them (R2); a few old clauses lost (R3, R4); repeated numbers that will drift (R5); and an image budget well above the "few key cases" rule with no rule for a brief's lower cap (R7). Fix F1 and F2 and the agent clearly makes better cinematics than with the old books.
