---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer environment-designer · claude-opus-5-5 · high · 2026-10-22

# Review: environment-designer books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/environment-designer.md (body) + .agents/skills/environment-design/ (SKILL.md, references/ incl. new read-plan.md, worked-examples.md) + .agents/skills/environment-craft/ (SKILL.md, references/ incl. new measure-captures.md; evals/ not reviewed), working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer environment-designer (opus, high)
looked_at_first: [
  role file body, both SKILL.md files, review.md, read-plan.md, worked-examples.md, place-reading.md, light-and-air.md, ambience.md, diagnosis.md, measure-captures.md, handoffs.md, studio-light-air.md read in full; git diff df13ff4 of every other changed reference (ambience-in-place, audit-and-capture, blender-to-studio, performance, terrain-and-water); old role body, old design SKILL.md, old craft SKILL.md and old review.md read at df13ff4,
  knowledge/reference/craft/riot/universal-principles.md (master, UP-01..UP-20, every space/level line and general check),
  matrix.md environment column (195 IDs, script-extracted) and the principle/apply/check/roblox_fit of all 195 + the 12 untagged findings the maker used (script-extracted from the topic files, read in full),
  tools: tool-modes.md; look_check.py value/palette/thumb --help and source (contrast_ratio :152-155, subject_ring_ratio :570); scene_audit.py probe/audit --help, load_probe :92-117; scene_probe.luau (record format, halfY :141-143),
  V3 runs on synthetic 1280 x 720 in-scene frames (sky, ground, walls, landmark, gate, stall, dark avatar, 30 x 25 px pickup; variants: black patch, red trim, orange above head height, blue sky, blue banner, lit flat wall, varied wall, warm-lit/cool-shadow blocks), scratch: scratchpad/envrev/,
  roblox-creator-docs: StarterPlayer.yaml:243-249, :329-339; greybox-your-environment.md:77; Lighting.yaml:39-50, :129-140, :455-465; ColorCorrectionEffect.yaml:78-84; ParticleEmitter.yaml:78, :962; RenderSettings.yaml:66-84, :106-125, :256-261; GlobalSettings.yaml:9-11; packages.md:3, :14-19; assemble-an-asset-library.md:93; studio/importer.md:234-242; art/blender.md:89,
  partner books: game-design SKILL.md and references/spaces.md; modeling-craft/references/handoffs.md:14, :44; modeling-design/references/kits-and-environment.md:48; platform-policy/references/rules.md:46, :56, :87,
  environment-craft/evals/briefs.md briefs 1-3 (read as the agent would)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C8 V3 + C3 (the core read check cannot fail)",
     where: "review.md:77 (RD3 'ratio above 1'), :91 (VB2), :98 (VB9), :102 (VB13); SKILL.md:92 (P1 check 'ratio above 1'); worked-examples.md:15 ('ratio above 1 in the grey view'); studio-light-air.md:79 (hazard glow 'until a dummy ... separates (M6)'); measure-captures.md:20 (M6)",
     expected: "A separation line fails when a character, dummy or hazard neighbour does not separate from its background, and its 'wrong number with no error' cell names the trap",
     observed: "M6 reads subject_ring_ratio. look_check computes it as the WCAG contrast ratio (max+0.05)/(min+0.05) (look_check.py:152-155, :570): it is 1 or more for every input, and the same for a darker or a lighter subject. So 'ratio above 1' passes every capture where the two medians differ at all, and VB2, VB9, VB13 and the hazard-glow recipe say 'separates' with no number. The line that carries UP-01 (P1, RD3) therefore cannot fail. FL1 is the only separation line with a starting target (3:1)",
     evidence: "V3 run: the pickup that reads by hue only (same value as the floor) gave subject_ring_ratio 1.046 after the M5 recipe: 'above 1' = pass. Dark-blue avatar (40,60,140) on the brown floor gave 1.976 through M6; the tool returns no sign of which side is darker",
     smallest_fix: "Give character and dummy separation one starting value marked PROPOSAL (for example the FL1 3:1, or a lower value that the art director sets), state once in M6 that the ratio is symmetric and 1.0 means no value separation, and use that value in RD3, VB2, VB9, VB13, P1, worked example 2 and studio-light-air §9. Add to M6's 'wrong number' cell: 'any test of above 1 passes'"}
  - {id: F2, class: blocking, check: "C8 V3 + C3 (reserved-colour check measures the sky and HUD)",
     where: "measure-captures.md:17 (M3 command, no --box) and :6 (§0 'A run with no box on a capture gives invalid-mask'); used by review.md:93 (VB4), :95 (VB6), :100 (VB11), :101 (VB12)",
     expected: "M0's own rule: environment measures name environment boxes (ground, walls, props), never the sky, characters, effects or the HUD. The reserved-hue share is measured outside gameplay objects inside those boxes",
     observed: "The M3 command has only --exclude-box. Without --box, palette does not return invalid-mask: it measures the whole frame (params.region 'whole image', mask_source 'none'), so sky, HUD and effects enter the clusters. A sky near a reserved hue becomes the nearest cluster with a large share, and a small decoration in that hue is lost in it. §0's sentence is true for value, not for palette",
     evidence: "V3 run, team blue #1E6EE6 reserved, M3 exactly as written: clean frame with a blue sky: nearest cluster dE2000 0.8, share 0.114 (false fail); the same frame plus a small blue banner on the wall: dE 0.7, share 0.098 (the two frames cannot be told apart). With --box 0,300,1280,720 and the same --exclude-box: clean dE 28.7; banner dE 0.0, share 0.0034 (right). The maker's run used a red reserve on a frame whose sky was not near it, so the trap did not show",
     smallest_fix: "M3: add --box <environment boxes> (the same boxes as M1's band run) and keep --exclude-box for gameplay objects inside them; add to the 'wrong number' cell: 'no --box: the sky and HUD are measured'. Correct §0: 'value and silhouette give invalid-mask with no box; palette measures the whole frame'"}
  - {id: F3, class: blocking, check: "C8 V3 + C3 (flat-fill check never fires)",
     where: "measure-captures.md:17 (M3 'Flat fill: palette <cap> --box <surface>: one cluster = flat'); review.md:101 (VB12); SKILL.md:103 (P12 check 'no flat single-cluster surface'); worked-examples.md:22 (example 3: 'the palette check finds one cluster on the long walls')",
     expected: "A flat single-colour surface in a Studio capture fails VB12 (LC-09, MD-10, UP-12)",
     observed: "palette runs k-means with k clusters (default 8). Any lit surface has a light gradient and render noise, so one flat colour splits into k clusters and 'one cluster' never happens on a real capture. VB12 passes every surface, and worked example 3 shows a result the tool cannot give",
     evidence: "V3 run: one colour (150,120,90) under a 0.8-1.1 light gradient with sigma 1.5 noise, boxed in a 1280 x 720 frame: k_effective 8, eight brown clusters; a wall with real hue and value patches: also 8. A share-weighted spread of the cluster hue angle atan2(b*, a*) separates them: 2.2 degrees (flat) vs 18.9 degrees (varied)",
     smallest_fix: "Replace 'one cluster = flat' with a measure that ignores lightness (for example the share-weighted spread of cluster hue angle and chroma, a one-liner like M4's, with a starting threshold marked PROPOSAL and one run on a lit flat sample), or make VB12 a key-view image line plus a tool proposal row. Rewrite worked example 3's flat-fill sentence to the measure that works"}
  - {id: F4, class: blocking, check: "C5 (old review checks dropped) + C3",
     where: "review.md §7 (:71-135) and §4 (:44-46); old review.md:37 at df13ff4 ('Look: route guidance, focal hierarchy, scale and passage, camera clearance, lighting readability, atmosphere, contact, finish ..., repetition while moving ...'); coverage §c row 'review.md:36-40 §4 checks moved into the §7 lines'",
     expected: "Every old look check lives on as a §7 line (the new §4 says 'Every check is a line of §7')",
     observed: "Three old checks have no §7 line: (1) camera clearance (PR-13: the third-person camera clips a lintel or low ceiling although collision passes; FL7 measures doors against the character only); (2) atmosphere: haze and fog never hide a route, edge, enemy or hazard (LA-10, C-05; P20 says 'fog never hides a hazard', but its check VB13 measures rim and glow only); (3) repetition while moving (PR-20: 'a pan shows a repeating highlight that a still hides'; FL3 uses key-view stills). The standards stayed; the agent's review no longer runs them",
     evidence: "grep -i 'clearance|haze|fog|lintel' on review.md: no hit; the rules are at place-reading.md:37 (PR-13), :49 (PR-20), light-and-air.md:28 (LA-10)",
     smallest_fix: "FL7: add 'the default camera passes every route opening and low ceiling without clipping: one capture through each tight opening'. RD8 or VB7: add 'with Atmosphere on, the route cue, edges and each hazard still read in their decision views (M1 rank with haze on)'. FL3: add 'repeated facades: 3-4 captures along the camera path players use'"}
  - {id: R1, class: recommendation, check: C1,
     where: "coverage/environment-designer.md row UI-06; light-and-air.md:47 (VB-c)",
     expected: "The landed-in text the row quotes is in the file",
     observed: "The row says VB-c carries 'the reserved colours are the same table UI and markers use'. VB-c does not say this (grep 'same table': no hit). The rule of one code for meaning is carried (VB-c, P7), not the shared table with UI and in-world markers",
     evidence: "light-and-air.md:47",
     smallest_fix: "Add to VB-c: 'the same reserved-colour table that UI and gameplay effects use (art bible)', or correct the row"}
  - {id: R2, class: recommendation, check: "C3 / V3 (false fail on a correct place)",
     where: "review.md:94 (VB5); measure-captures.md:18 (M4)",
     expected: "A place that is neutral at every height passes VB5",
     observed: "VB5 passes only when player-band chroma is below the band above head height. In a fully neutral place the two bands differ by noise, so VB5 fails at random",
     evidence: "V3 run, M4 as written: neutral walls: player band 9.10, above head height 8.00 (VB5 fails); orange above head height: 9.10 vs 66.6 (passes, right)",
     smallest_fix: "VB5: 'below the band above head height, or under a neutral limit (starting value marked PROPOSAL)'"}
  - {id: R3, class: recommendation, check: "C8 V6 + C7 (length)",
     where: "environment-design/SKILL.md:38 (step 5), environment-craft/SKILL.md:32 (step 4) and :59 (C-15), light-and-air.md:19 (LA-15), studio-light-air.md:8 (§1 step 2); also role step 3, review.md VB8, PS2",
     expected: "One rule, one place; other places point to it",
     observed: "The grey value and light-direction pass is written out with its parameters (2-3 sun positions, objective lightest, no key position in deep shadow, image budget) in five places. The greybox order (spawns, route, side areas, theme shapes, dummy and known-size object, box collision) is written out in design step 5, craft step 3 and PS2. The texts agree today; the next change must edit every copy",
     evidence: "the lines above",
     smallest_fix: "Keep the full rule in LA-15 (what) and craft §3 step 4 (how); design step 5, C-15 and studio-light-air step 2 name the pass and point there"}
  - {id: R4, class: recommendation, check: "C7 (fix jobs)",
     where: "review.md:71-72 (§7 header 'run before every hand-back'), :45 (§4 're-rates every line'); role 'What you check before handing back'",
     expected: "A small change or fix runs the lines its change touches, not the whole stage checklist",
     observed: "§7 has 51 lines, including option-round, gate and blueprint lines. For eval brief 2 (players miss the cave) the books say both 'retest what the fix touches' (§6) and 'answer every §7 line'. An agent will either run 51 lines for a one-cue fix or skip lines without a rule",
     evidence: "evals/briefs.md brief 2; review.md §6 'Retest what the fix touches'",
     smallest_fix: "One sentence in §7's header: 'For a small change or fix: the lines the change touches by dependency plus RD2, RD3, VB1, FL1 and QV3; the others are n/a (fix job)'"}
  - {id: R5, class: recommendation, check: "C8 V10",
     where: "environment-craft/references/handoffs.md:37 (§3 modeler 'fixed') and :91 (§7 modeler row)",
     expected: "The environment brief gives the modeler what the rebuilt modeler books ask for",
     observed: "modeling-craft/references/handoffs.md:44 asks the environment designer for 'the stage's ground and light (a capture or the art bible values), the snap grid and blockout origin'. The env brief gives the snap grid but not the ground-and-light capture or the blockout origin (blender-to-studio.md §7 uses the origin itself)",
     evidence: "modeling-craft/references/handoffs.md:44; handoffs.md:37",
     smallest_fix: "§3 fixed: add 'a capture of the stage's ground under its chosen light, and the greybox origin'"}
  - {id: R6, class: recommendation, check: "C8 V3 (small)",
     where: "measure-captures.md:22 (M8), :19 (M5), :25 (M11)",
     expected: "Each recipe runs on the real saved output",
     observed: "(a) M8 reads 'the M7 probe JSON', but the saved Studio output is 'SCENE_PROBE k/n' slices; the maker's run used the fixture, which is plain JSON. (b) M5 adds only the x offset; a 4:3 target letterboxes in y (thumb --size 1024x768 on a 16:9 capture: y0 96), so the box then measures the floor with no error. (c) M11 names 'weighted b*' but gives no one-liner, unlike M4",
     evidence: "scene_audit.py:92-117 (load_probe joins slices or reads plain JSON); my thumb run content_box_px {x0 0, y0 96}",
     smallest_fix: "(a) 'load with scene_audit.load_probe'; (b) 'add x0 and y0 of content_box_px'; (c) copy M4's one-liner with lab[2] and lab[1]"}
  - {id: R7, class: recommendation, check: C6,
     where: "place-reading.md:8 (PR-01 'Riot greybox practice'), light-and-air.md:14 (LA-05 'K01-b E (Riot)'), :28 (LA-10 'K02-b E (Riot)')",
     expected: "No 'Riot' in book bodies (fixed list)",
     observed: "Three evidence cells name Riot. They are older J008 tags from the owner's research paper, not J018 text, so I do not block on them",
     evidence: "git show df13ff4 of both files has the same tags",
     smallest_fix: "Keep the paper row ids (K01-d, K01-b, K02-b) and drop the word"}
  - {id: R8, class: recommendation, check: "C8 V11 (for the lead)",
     where: "proposals/art-director.md:30-32, proposals/film-director.md:28, proposals/progression-designer.md:28; proposals/game-designer.md (studio-mcp quality-level row)",
     expected: "Rows that other roles wrote against the environment books are adopted or declined with a reason",
     observed: "These wave-2 rows were written in parallel, so the maker could not answer them (not a V11 failure). The quality-level probe also differs between books: the env books set EditQualityLevel with EnableFRM false (matches RenderSettings.yaml:66-84, :106-125); the game-designer row uses QualityLevel, which applies when EnableFRM is true (RenderSettings.yaml:256-261)",
     evidence: "the files above",
     smallest_fix: "Lead: give these rows to the round-2 maker; settle one quality-level probe in the studio-mcp proposal"}
keep: [
  "the rule above all: the place is the backdrop; route, objective, hazards, characters and pickups read first, on a phone, in the busiest moment (SKILL.md §1, E-15..E-20)",
  "the read plan sheet before any image (personality, 3 story facts, theme cues, key views with ranked reads and critical facts, focal point, smallest gameplay object, band and reserved colours, key light, detail spots, ranked work list, stop criteria and pass budget) with a worked example per field",
  "the option round: research and keyword table, three directions from different sources with one from outside games, warm-up labelled, pick with reasons, rejections recorded, image budget",
  "the grey value and light-direction pass on the greybox, by the numbers, before any art",
  "the environment value band with the grey-value to WCAG-luminance conversion (checked: 15 % = 0.020, 85 % = 0.69, 5 % = 0.004), reserved colours, neutral player band, tamed hazards",
  "review.md §7: every line names its input, PROPOSAL starting values, 'not verified' with the closing input; measure-captures.md with a 'wrong number with no error' column found by real runs (black patch under p5, loose box, landmark in the far band)",
  "collision, cover and sight-line diff against the approved greybox (RD9, M8; the rotation term matches scene_probe.luau halfY)",
  "material zoo under the stage light; one-off Blender pieces held to the modeler's standards by pointer (V6 done right)",
  "M9 written honestly as 'probe first' with a by-hand fallback; RenderSettings citations verified",
  "partner asks with timing (handoffs.md §7), footstep material list and emotion per zone for sound, sight-line distances and off paths for VFX, in-set capture back to the modeler",
  "platform-policy routing for blood, violence, alcohol, adult venues and brands (agrees with rules.md:56, :87)",
  "the 16 rejections, each with a sound owner-based reason",
  "the tool and template proposals with V3 evidence (look_check --dark-below, thumb --crop, probe fields)"
  ]
verdict: fix-first
</spec>
```

## C1-C8 results

| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | fail (9 of 207 rows) | All 195 tagged IDs have a row; the 12 untagged rows were checked too. Every landed-in place was opened and carries the rule. The 16 rejections have sound reasons. Failed rows: UI-06 (quoted text not in the file, R1); LC-01, LC-02 (their check VB4 runs on the whole frame, F2); LC-09, MD-10 (VB12 cannot fail, F3); WL-01, LC-16, LC-18, VC-08 (their separation check cannot fail, F1). The F1-F3 fixes repair all of them |
| C2 core principles | pass | `environment-design/SKILL.md` §7 has P1-P20, one per UP, each stated for stages with its own example and a check with its input. No contradiction with the master. UP-08 and UP-19 are added "in part" with the boundary stated (the master does not list the role; no conflict). P1's check depends on F1, P12's on F3, P20's fog clause on F4. §1 says to re-read §7 after a compaction |
| C3 self-review | fail | F1 (separation lines cannot fail), F2 (reserved hue measured on sky and HUD), F3 (flat fill never found), F4 (camera clearance, haze and repetition-in-motion have no line). The other lines can be run with Studio MCP captures, look_check, scene_audit, the partner check-ins and the reference images |
| C4 kit rules and engine | pass | Engine claims checked in the mirror: CharacterUseJumpPower default true and JumpHeight 7.2 (StarterPlayer.yaml:249, :339), greybox page :77, Lighting Ambient/OutdoorAmbient clamp and ColorShift lines, ColorCorrection Saturation -1, ParticleEmitter Brightness and TimeScale, RenderSettings plugin security, packages and trim-sheet lines, importer options. No invented tool modes. Owner gates, write scope and platform-policy routing agree with AGENTS.md, rules and J018-D2 |
| C5 nothing valuable lost | fail | F4. Every other removed or changed old rule was found kept, moved or sharpened (old E-04..E-12, the old role step 5 and 6 items, old self-check items, old §4 ambience checks, which live on in ambience.md §5 through AM2). E-04's "record the exaggeration in the game profile or blueprint" is now PR-15's "record which relations bend": acceptable |
| C6 fixed rules | pass (R7) | Only the environment books and the two env job files are new or changed by this maker; tools/, templates/, rules/ and .agents/workflows/ unchanged; evals/ unchanged. Role frontmatter byte-identical to df13ff4 (md5 of lines 1-10). SKILL.md files 113 and 84 lines; descriptions 393 and 390 characters. No section renumbered (review.md §3 retitled, §7 appended; light-and-air §4 appended). The J018 phrase is in every changed file's header and the role comment. No library IDs, transcript lines, champions or artists; three old J008 "(Riot)" evidence tags remain (R7). No tips section. LF line endings |
| C7 better work | yes, clearly | see below |
| C8 brief v2 | fail on V3 | V1 pass (every §7 line names its input; image budgets for options, grey pass, look-lab brackets, routine passes and the release candidate). V2 pass (value, palette, thumb, scene_audit probe/audit only). V3 fail: F1, F2, F3 give wrong answers with no error; the maker's other runs reproduce (M1 band, M2 black patch 0.0 vs 0.0044, M4, M5 1.05 loose, M10, M11, M7 FAIL on the fixture's planted defects); small gaps R6. V4 pass (alcohol, adult venues and IP go to platform-policy, rules.md:56, :87). V6 recommendation (R3). V7 pass (§3 at 4.1 KB, §5 at 15.2 KB, §6 at 16.9 KB, §7 starts at 17.8 KB with a re-read line). V8 pass (read plan sheet, partner asks with timing, the §7 checklist on named captures). V10 pass with R5 (route table, hazard sheets, read rank and material-to-rule table match game-design; in-set capture matches the modeler). V11 pass (modeler and game-designer rows adopted or declined with reasons; wave-2 rows R8) |

## Will an agent make better work with these books?

Yes, clearly. I read eval brief 1 (swamp edge, falls, cave mouth, ridge; third-person phone camera) as the agent would.

With the old books the agent would follow a good order (intake, references, blueprint, blockout, slice, build, review) and a good set of standards for routes, scale, terrain, finish and ambience. But its review was one sentence of topics ("route guidance, focal hierarchy, ... cohesion with the art bible") with no measure and no input. Nothing told it what the place must let the player read, how dark or saturated the backdrop may be, or when the light direction is chosen.

With the new books the agent does these things:
- It writes a read plan before the first image: ranked reads per key view, the smallest gameplay object (frog-zone pickups on the boardwalk), story facts and theme cues, a work list ranked with the game designer, and stop criteria.
- It makes three distinct directions, recommends one with a reason, and records why the others lost.
- It chooses the sun on the grey greybox from 2-3 positions by the numbers, so the cave mouth or the falls is the lightest area from the ridge.
- It keeps the backdrop in a value band with no pure black, keeps reserved hues out of the dressing, and keeps the boardwalk band neutral.
- It checks the smallest object on every floor at phone size, and the read plan at the lowest and highest graphics setting.
- It answers each of 51 review lines with a named input, and gives sound and VFX the emotion per zone, the floor materials and the sight lines to keep clear.

Worked example 1 walks almost this exact loop.

Weak spots:
- The line that guards the main read (characters separate from the place) cannot fail as written (F1).
- The reserved-colour check reads the sky and HUD (F2).
- The flat-fill check never fires (F3).
- Camera clearance, haze over hazards and repetition in motion fell out of the review (F4).
- The checklist has no scope for small fixes (R4).
- The grey-pass rule is written out in five places (R3).

All of these are small text fixes. The process and standards around them are sound and much stronger than before.
