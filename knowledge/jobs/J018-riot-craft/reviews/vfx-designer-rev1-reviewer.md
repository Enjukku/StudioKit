---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer vfx-designer · claude-opus-5-5 · high · 2026-10-22

# Review: vfx-designer books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/vfx-designer.md (body) + .agents/skills/vfx-design/ (SKILL.md, references/ incl. new read-card.md, rebuilt review.md) + .agents/skills/vfx-craft/ (SKILL.md, references/ incl. new measure.md); working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer vfx-designer (opus, high)
looked_at_first: [
  role file body (new and df13ff4) and frontmatter diff; vfx-design SKILL.md, read-card.md, review.md read in full; vfx-craft SKILL.md, measure.md read in full; git diff df13ff4 of camera-and-screen, effect-card-and-presets, elements, moment-recipes, scene-and-clutter, plan-and-spec, pro-defaults, techniques; removed lines of both SKILL.md walked one by one,
  knowledge/reference/craft/riot/universal-principles.md (UP-01..UP-20, every 'effect:' line and general check), matrix.md vfx column (214 IDs, script-extracted), library apply/check/roblox_fit lines of 22 findings (CF-03, VR-03/06/07/10/13/16/17/21/26, WT-11/13, VC-06, SS-03/07, LC-21, GD-23, CR-16, SD-22, WL-28, PI-11, VH-05, RH-02),
  tools: tool-modes.md, look_check.py --help for value/silhouette/palette/thumb/contrast and its source (RULE_SCOPE, compare alignment), clip_metrics.py source, vfxlib_catalog.py shortlist --help; V3 runs of my own (below),
  roblox-creator-docs: ParticleEmitter.yaml:962-968 (TimeScale), Model.yaml:716-740 (ScaleTo), effects/highlighting.md:37,
  platform-policy/references/rules.md §A; animation-design/references/game-timing.md §4-§5; sound-design SKILL.md S-133 and review.md R-43/R-54; art-review/references/look-check.md:41; preproduction documents.md §6, §7, §9; reference-images SKILL.md §3; knowledge/reference/vfx/training/README.md (capture method),
  vfx-design/evals/briefs.md briefs 1-3 (read as the agent would)
  ]   # the maker's coverage and proposals files were read after this
v3_runs (scratchpad rev-vfx/, synthetic 1280x720 JPEG frame folders at 30 fps, sky gradient + noisy ground + a character block, named f###_<ms>ms.jpg):
  - mask one-liner, look_check value / silhouette --keep-holes / thumb --size 800x360 / palette --k 4 --roles inline JSON / contrast --sample / silhouette --compare --compare-mask, mirror one-liner, curve one-liner on content/vfx/curves.json, shortlist --help: all run and write the files measure.md names; curve values match measure.md §5 exactly
  - wrong numbers with no error found that the books do not list: F1, F2, F3, F4 below; R3
findings:
  - {id: F1, class: blocking, check: C8 V3 + C3 (the flash-safety and pulse lines),
     where: ".agents/skills/vfx-design/references/review.md:288 (IG-07), :289 (IG-08); .agents/skills/vfx-craft/references/measure.md:11 (busiest-scene folder), :35-41 (wrong-number list), :70-72 (§6)",
     expected: "IG-07 counts large flashes 'Bloom and grade pulses included' and IG-08 measures every pulse rate against 'nothing above 3 Hz'; a count the agent relies on for safety must not come out low or doubled with no error, or the trap must be written next to the command",
     observed: "clip_metrics counts only pixels more than 40 levels from the per-pixel median. (a) A full-screen grade or Bloom pulse of under 40 levels is invisible: no coverage jump, no bright_pct jump, so §6 finds no flash. (b) A lasting zone or countdown pulses for the whole folder, so the median is its middle state: a large swing is counted at both the bright and the dark phase (rate doubled), a small swing is not counted at all. Neither trap is in measure.md §2 or §6, and §6 reads both counts from these rows",
     evidence: "my V3 runs: clipG (whole screen +30 levels for 2 frames, 3 times in 1 s; sky 0.28 -> 0.42 relative luminance, a WCAG flash): peak_coverage 0.0 %, every row 0, flash count 0 / s. clipP2 (ground ring pulsing at 1.5 Hz, 0-160 levels, on screen the whole folder): coverage peaks every 10 rows -> 3.0 Hz (false fail at the cap, and 'urgent' instead of 'safe'). clipP3 (same, 0-60 levels): 0 % in every row, no pulse found. clipP (0-90 levels): 1.5 Hz, right. review.md:18 §A already lists 'blink and pulse rates' as spec (S) values",
     smallest_fix: "IG-08 input 'S, M': 'read each pulse and blink rate from the spec (sequence or tween period, server timer) first; confirm on rows only from a folder where the pulsing layer starts after the still half, counting the bright phase only'. IG-07: '+ every Bloom, ColorCorrection or other post-effect pulse is counted from the spec (S), not only from rows'. measure.md §2 list: add the two traps ('a full-screen change under 40 levels is not seen'; 'a layer on screen the whole folder makes the median its middle state: a pulse reads at double rate or not at all'); §6: point to them"}
  - {id: F2, class: blocking, check: C8 V3 + C2 (the §9 #11 check) + C3,
     where: ".agents/skills/vfx-design/references/review.md:224 (PL-13 'footprint ... equal the base', input S, K); .agents/skills/vfx-craft/references/measure.md:55 ('Variant vs base (PL-13) ... aligned IoU of the two footprints'); .agents/skills/vfx-design/SKILL.md:125 (§9 #11 check 'silhouette --compare, same footprint')",
     expected: "A check named 'same footprint' fails a skin whose effect covers a larger area or sits elsewhere: that is the fairness rule PL-13 guards (a cosmetic never changes the gameplay read)",
     observed: "look_check silhouette --compare crops each mask to its box, scales both to the same box height and centres them before the IoU (look_check.py:499-526, output 'alignment.method'). Size and position are removed by design, so the IoU measures shape only. The books call it the footprint comparison",
     evidence: "my V3 run: base ellipse 120 px wide at x 640 vs variant 240 px wide at x 500 (four times the area, moved): aligned IoU 0.985, scale_b 1.98; no error. The master UP-11 uses --compare for identity anchors (shape), which is right; the VFX books stretch it to footprint",
     smallest_fix: "measure.md:55 cell: 'aligned IoU = same shape only (size and position are normalised away); same footprint = the spec reads the radius from the same data field (S) and the two stills from the same camera have area_frac and bbox_frac within the tolerance'. PL-13 and §9 #11 check: name both parts ('shape: --compare IoU; footprint: same data field + area_frac, bbox_frac')"}
  - {id: F3, class: blocking, check: C8 V3 + C3 (BL-09 fails correct work),
     where: ".agents/skills/vfx-design/references/review.md:237 (BL-09 'the changed-pixel box of every row stays ... outside the information areas'); .agents/skills/vfx-craft/references/measure.md:31 (BL-09 row: 'every row's box ... outside the information areas')",
     expected: "BL-09 fails an effect whose pixels cover an information area and passes one that does not (library VR-07 check: 'mask the information areas and confirm no effect pixels cover them'; IG-02 already says 'no effect pixel')",
     observed: "clip_metrics 'box' is the bounding box of all changed pixels. Any effect that surrounds a character (danger ring, aura, shield, the read card's own ground-slam example, read-card.md:41-45, where the threatened player stands inside the ring) has a box that contains that character, so BL-09 fails although no pixel covers them. The height test on y0 is fine; the cover test is not",
     evidence: "my V3 run clipR (a red ground ring drawn around and behind a character block; information area = the block): row box [0.367, 0.528, 0.617, 0.66] overlaps the block [0.469, 0.417, 0.5, 0.583]; effect-mask pixels inside the block: 0",
     smallest_fix: "BL-09 and measure.md:31: 'box top (y0) below the maximum-height line; the cover test uses the effect mask (§3) of the peak and tail stills against a mask of the information areas drawn on the effects-off frame: 0 overlapping pixels'"}
  - {id: F4, class: blocking, check: C7 (contradiction that makes the work worse) + C8 V3,
     where: ".agents/skills/vfx-design/references/read-card.md:30 (T2 'Near-white: none (a target's brightness flash is allowed)'); .agents/skills/vfx-design/references/review.md:231 (BL-03 'bright_pct > 0 ... none in T1-T2'); against .agents/skills/vfx-design/SKILL.md:55 (Value: 'clipped white only at the single focus on the peak frames (a 1-2 frame flash)'), .agents/skills/vfx-craft/SKILL.md:51 (C-07 'white flash 0.03-0.05 s'), :84 (SP-04 'Impact: flash 0.03-0.05 s'), vfx-craft/references/pro-defaults.md:14 (white flash row, Brightness 'highest'), vfx-design/references/moment-recipes.md:85 (Light hit: 'contact flash')",
     expected: "One rule for the most common effect in the kit (a frequent hit spark, T2): either it may have a tiny contact flash or it may not; the self-review lines agree with the spec lines",
     observed: "A T2 hit built from the craft's impact recipe (SP-04 requires the flash) fails BL-03 and the T2 cap; an agent that passes BL-03 must drop the flash and then fails SP-04. The library supports the small flash (VC-07: white and the highest contrast for small focal spots); SKILL §4 allows it for 1-2 frames at the focus",
     evidence: "my V3 run clipS (small orange spark with a 1-frame white core of 40 px at the contact): bright_pct 0.106 on that row only, 0 elsewhere -> BL-03 'none in T1-T2' FAIL, SP-04 PASS",
     smallest_fix: "read-card.md:30 T2 near-white: 'a 1-frame contact flash, small (about 0.5 % of the screen or less, PROPOSAL), at the contact point only'; BL-03: 'in T1 none; in T2 at most that 1-frame contact flash; in T3 the 1-2 flash frames; in T4 the white-core frames'. Leave SP-04 and C-07 as they are"}
  - {id: F5, class: blocking, check: C4 (tool's documented scope) + C8 V2, V10 (partner book),
     where: ".agents/skills/vfx-craft/references/measure.md:54 (Marker contrast (VS-10): 'contrast --sample ... --rule wcag-nontext'); .agents/skills/vfx-design/references/review.md:255 (VS-10)",
     expected: "A book uses a tool mode inside the scope its help states. look_check contrast help: 'Rules are for UI text/components only, never world art'; art-review/references/look-check.md:41 lists 'a UI rule applied to world props or enemies' as a misuse",
     observed: "VS-10 checks in-world danger edges and pickups with the named UI rule wcag-nontext",
     evidence: "my V3 run of the exact command: output 'scope': 'UI text and UI components only; not a rule for world art, props or characters (AP:559)', verdict 'pass' at 3.0; look_check.py:101, :110 (RULE_SCOPE). The 3:1 number itself is fine (library VC-06 check (DS), PROPOSAL)",
     smallest_fix: "measure.md:54: replace '--rule wcag-nontext' with '--min-ratio 3 --tolerance-source \"VS-10 PROPOSAL (read card)\"'; cell 'ratio and pass at the 3:1 PROPOSAL (not a UI standard)'"}
  - {id: F6, class: blocking, check: C4 (engine claim against the docs mirror),
     where: ".agents/skills/vfx-craft/SKILL.md:71 (C-27 'ParticleEmitter Size does not follow a model's scale: scale the sequences from one factor (probe in Studio before relying on any automatic scaling)')",
     expected: "Engine claims match knowledge/external/roblox-creator-docs",
     observed: "The docs say the opposite for Model:ScaleTo: it resizes all descendants, including 'Visual properties like sizes of particle emitters'. The line comes from the library's VR-17 roblox_fit, which is marked [unverified] there; the book drops the mark and states it as fact",
     evidence: "_api-reference/classes/Model.yaml:716-740 (ScaleTo: 'All \"geometric\" properties of descendant Instances will be scaled ... Visual properties like sizes of particle emitters'); knowledge/reference/craft/riot/vfx-reads-timing.md:251 (VR-17 roblox_fit '[unverified]')",
     smallest_fix: "C-27 last sentence: 'Model:ScaleTo scales emitter sizes with the model (Model.yaml:739); a Part or Attachment resized by hand does not, so keep the one factor in data and scale through ScaleTo or from that factor; probe once before relying on either.' Add a proposals row for the library VR-17 roblox_fit (the lead fixes the library first)"}
  - {id: R1, class: recommendation, check: C1 (one coverage row lands on a keyword),
     where: "knowledge/jobs/J018-riot-craft/coverage/vfx-designer.md:35 (CF-03 -> plan-and-spec.md §B, review.md PL-10)",
     expected: "CF-03 'put detail where the camera distorts least'; check: zoom on the far or foreshortened parts at the game camera and remove small features that merge into lines",
     observed: "§B and PL-10 hold screen-size math (height % at launch and impact), not detail placement. The nearest real carriers are elements.md EL-16 and C-29 / CP-13 (a ground ring gets a vertical or camera-facing border where a low camera flattens it), which the row does not cite",
     evidence: "plan-and-spec.md §B; review.md:221 (PL-10), :272 (CP-13); vfx-craft SKILL.md:73 (C-29); library composition-focus.md CF-03 check",
     smallest_fix: "CP-13 '+ far or foreshortened parts at the game camera: small bits that merge into lines in the phone-size still are removed or enlarged'; coverage row -> C-29, CP-13"}
  - {id: R2, class: recommendation, check: C7 (an input the books depend on has no route),
     where: ".agents/skills/vfx-craft/references/measure.md:10 (Frame folder: 'the studio-operator records it'); every BL, VS, CP line with input M or K",
     expected: "The passes say where the frame folder comes from today, and what the agent does without one",
     observed: "No kit tool records a fixed-camera frame folder: the recorder (record.py, about 27 fps) lives in a session scratchpad (knowledge/reference/vfx/training/README.md:28, :50-53); tools/vfx/ has none; Studio MCP stills are not motion (measure.md:18). The maker filed a proposal (studio-mcp probes row) but the books give no interim route, so the blocking pass, the gates and the check-in may stall or go unmeasured",
     evidence: "ls tools/vfx/ = clip_metrics.py, curve_library.py, emitter_stats.py, vfxlib_catalog.py; README.md:28 'Tools (session scratchpad, to be promoted ...)'",
     smallest_fix: "measure.md §1, one line: 'Until a recorder is in tools/, ask the lead for the capture route at the wiring step; without a frame folder, the M lines are \"not verified\", the S lines and the Studio stills carry the pass, and the hand-back names the missing capture'"}
  - {id: R3, class: recommendation, check: C8 V3 (a silent loss of frames),
     where: ".agents/skills/vfx-craft/references/measure.md:10 ('0 ms on the trigger ... pad before and after'); review.md:229 (BL-01)",
     expected: "The naming rule and the padding rule fit the tool's regex",
     observed: "Frames before the trigger would need negative ms; clip_metrics' FRAME_RE (\\d+) skips them without a message, so the padding before the trigger disappears and the folder may drop under the half-still rule",
     evidence: "my V3 run clipN: 30 frames named f000_-1000ms ... f029_-43ms plus 30 after the trigger: metrics.json frames: 30 (the 30 pre-trigger frames ignored), no error",
     smallest_fix: "measure.md:10: 'pad after the effect; if frames before the trigger are needed, name ms from the folder start and record the trigger ms in the folder name'"}
  - {id: R4, class: recommendation, check: C7 (rules/anti-overengineering.md: build at the size it needs),
     where: ".agents/skills/vfx-design/SKILL.md:20-26 (§2 steps 1-7); .agents/roles/vfx-designer.md:31-41",
     expected: "A small effect or a fix (T1-T2, a retime) has a short route the books name",
     observed: "Every effect gets research, 2-3 options, a key-frame sheet, blocking, check-in, gates, colour, polish and the in-game pass. The read card's pass budget helps, but nothing says which stages a coin pop or a retime may compress, so the agent either over-processes small work or skips stages without a rule",
     evidence: "read-card.md:53-68 (coin card has a stop line but still runs the full §2 order); the role comment (role file :12) names 'medium is a brief-level choice for small effects and fixes' but the books do not",
     smallest_fix: "§2, one line after step 7: 'T1-T2 effects and fixes: options as text only (no sheet unless the brief asks), one bracket round, one capture round; the read card, truth, the gates and the spec lines still run'"}
  - {id: R5, class: recommendation, check: C8 V11 (partner rows not answered),
     where: "knowledge/jobs/J018-riot-craft/coverage/vfx-designer.md:373-376 (only animator and game-designer rows answered)",
     expected: "Each proposal row aimed at the VFX books is adopted (and where) or declined with a reason",
     observed: "Wave-2 rows aimed at vfx-design are not answered: environment-designer.md:37 (ambient specs state the distance to the nearest sight line, off path, ≤3 flashes/s), film-director.md:31 (cutscene effects go on a frame that already passes composition and value), progression-designer.md:25 (reward effects read tier, trigger and rate from the tier table), ui-ux-designer.md:31 (world-to-HUD split on one beat list), art-director.md:30 (bible §7 rows as named inputs). Most are partly covered already (SC-70, CP-12, the partner table)",
     evidence: "grep of proposals/*.md for vfx-design",
     smallest_fix: "Five lines in the coverage file's V11 block (adopt with location, or decline with reason); the progression row is one cell in read-card.md §1 Rate ('Source: feedback stack; reward effects: the progression tier table')"}
  - {id: R6, class: recommendation, check: C7 (evals will grade correct work as wrong),
     where: "knowledge/jobs/J018-riot-craft/proposals/vfx-designer.md evals row; .agents/skills/vfx-design/evals/briefs.md brief 1 check 1.4, brief 3 check 3.3",
     expected: "The evals proposal lists the eval checks the rebuilt books now contradict",
     observed: "Check 1.4 expects trauma shake at importance about 5 (the books: no shake below 8 unless the owner allows); check 3.3 expects odds 'behind a worded Details control' (platform-policy: a pop-up only for long lists, odds update while a modifier is active; moment-recipes §D now says so)",
     evidence: "briefs.md brief 1 1.4, brief 3 3.3; vfx-design SKILL.md:61; platform-policy/references/rules.md §A rows 3-5",
     smallest_fix: "Append to the evals proposal row: 'rewrite 1.4 (shake only when the owner allows) and 3.3 (odds visible before the buy button; worded Details pop-up only for long lists)'"}
  - {id: R7, class: recommendation, check: C8 V6,
     where: ".agents/skills/vfx-design/SKILL.md:47 (toolbox and 'many meshes spawned as particles'); .agents/skills/vfx-craft/references/techniques.md:7, :10; vfx-craft SKILL.md:90 (SP-10)",
     expected: "One rule, one place",
     observed: "The toolbox line and the no-mesh-rain line are written out in the design chooser and again in techniques.md (and SP-10). They agree today",
     evidence: "the three lines quoted",
     smallest_fix: "Keep them in techniques.md; §3 says 'Know the toolbox before writing code (techniques.md intro, T1)'"}
keep: [
  the read card (read-card.md) with its loudness tiers and two worked cards: it turns the brief into checkable fields before any layer,
  review.md §I: self-review lines by pass, each with its input code, the image budget under J005-D8, and the 'fresh read' protocol,
  measure.md: every command tested, with an honest 'wrong numbers with no error' list (median inversion, onset/visible fields, the 40-level threshold, --keep-holes, contrast boxes),
  the build order: blocking with placeholder sprites -> check-in -> grey and black-fill gates -> colour -> polish -> in-game, with 'after the check-in, footprint, peak time and stage starts move only by a recorded decision',
  the 'shake is occasional' contradiction removed from five references, each now pointing to SKILL §4,
  moment-recipes §D split into what the effect owes and what platform-policy owns (V4 done right),
  the ring-curve fix with measured curve values (grow from 38 % = 0.53 at t 0.25) and the fast-in test,
  craft rows C-17 to C-31 (rank by value, coloured additive core with a halo, builds rise, cause-hold-result, solid volumes, piles, one root),
  the partner table in the role file (what to ask whom, and when),
  §9 core principles: all 20, each with its own example and a line-id check
  ]
verdict: fix-first
</spec>
```

## Check results

| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | pass with 1 row failed (R1) | 214 / 214 tagged IDs have a row (script diff against matrix.md, none missing or extra); 184 landed, 30 rejected with sound reasons; every cited location read; CF-03 lands on a keyword |
| C2 core principles | pass, one check wrong | §9 covers UP-01..UP-20 with own example and check; no contradiction with the master; the #11 check uses a scale-free IoU for footprint (F2) |
| C3 self-review | fail | lines exist for every checkable finding and name their input; three lines give wrong verdicts (F1 IG-07/IG-08, F2 PL-13, F3 BL-09) and one contradicts the spec lines (F4) |
| C4 kit rules and engine | fail | C-27 contradicts Model:ScaleTo docs (F6); contrast UI rule on world art against the tool's scope (F5); TimeScale and Highlight 255 claims match the docs; no rule or owner-decision conflict |
| C5 nothing valuable lost | pass | every removed line of both SKILL.md files and the role body is kept, sharpened or moved (old steps inside the new passes, old self-check inside SP-01..SP-13); the old Riot-extracts pointer removed by job rule; 'device mix' now comes from the game profile |
| C6 fixed rules | pass | only the vfx books and the two job files changed (three other references show stat-only status, no content diff, LF); frontmatter byte-identical; SKILL.md 134 and 113 lines; descriptions 377 and 353 chars, unchanged; no section renumbered (§9 appended); J018 phrase in each changed skill header and the role comment; no Riot, games, champions or library IDs in the bodies; no tips section; evals/ unchanged |
| C7 better work | yes, with weak spots | see below |
| C8 brief v2 | fail on V3 (F1-F4), V2/V10 (F5), V11 partial (R5) | V1 inputs and budgets named; V4 paid-random lines agree with platform-policy; V6 mostly pointers (R7); V7 steps and self-check inside about 18 KB, §1 says to re-read §9; V8 sheets, asks and checklists present; V10 sync rule, event ids and freeze frame agree with the animator and sound books |

**C7 judgement (eval brief 1, the heavy rocket hit, read as the agent would).** The old books took the agent from a short restatement straight to a layer plan and one capture. The new books make it write a read card (verb, three reads, a tier with caps, the truth radius from config, information areas, a pass budget). They make it weigh 2-3 options, block the hit with placeholder sprites on the real timing, and prove build, peak, fast-in and tail with clip numbers before any texture. It then checks the grey and black-fill gates, checks the colour against roles, and runs a named in-game pass. Each step catches a known failure mode of the old route: polish on a weak read, a flash off the contact frame, white blowout from stacked additive layers, dust over the information areas, a skin that changes the read. The agent will make clearly better and more honest work. Where it is still weak: three self-review readings give wrong verdicts with no error (F1-F3); the T2 near-white cap fights the impact recipe on the most common effect (F4); the frame folder that most M and K lines need has no route in the kit yet (R2); and small effects have no short route (R4). None needs a rebuild. Each fix is a few lines.
