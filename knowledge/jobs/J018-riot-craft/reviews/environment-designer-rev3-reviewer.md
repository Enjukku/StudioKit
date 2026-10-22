---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer environment-designer · claude-opus-5-5 · high · 2026-10-22

# Review: environment-designer books, rebuild round 3 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/environment-designer.md (body) + .agents/skills/environment-design/ (SKILL.md, references/) + .agents/skills/environment-craft/ (SKILL.md, references/; evals/ not reviewed), working tree on top of df13ff4 after repair round 2, 2026-10-22 (book files last written 05:55-05:58)
reviewer: J018 reviewer environment-designer (opus, high)
looked_at_first: [
  role file body, both SKILL.md files, review.md, measure-captures.md, light-and-air.md, worked-examples.md, read-plan.md, place-reading.md read in full; handoffs.md §1-§7, studio-light-air.md §1 and §8-§9, ambience.md AB-03..AB-17; section headings old vs new in every changed file; frontmatter lines 1-10 of the role file against df13ff4,
  knowledge/reference/craft/riot/README.md, universal-principles.md UP-07, UP-11, UP-12 (the master for the three changed core-principle checks), light-colour.md LC-05..LC-10, materials-detail.md MD-10, matrix.md environment column (195 IDs, script),
  my round-2 review (B1, R1-R3 re-checked below),
  tools: look_check.py palette/value/thumb/contrast --help; palette_stats, run_palette, srgb_to_lab, hex_to_rgb, ciede2000 source (:122-220, :629-656, :933-963),
  V3 runs (scratch: scratchpad/env3/): the M3 script cut out of measure-captures.md §3 by awk and run as written from the repository root on synthetic 1280 x 720 in-scene frames: flat wall; one-hue bricks (+-15 % value, darker mortar); bricks with +-2 and +-4 degree hue shifts; grey stone with warm and cool patches; a flat wall picking up 5, 10, 20 and 60 % haze toward its far end; VB6 second run (terracotta, loud orange, calm walls with green bunting; vent and avatar excluded). M12 exactly as written (palette --box per lit face --roles --k 7, then the nearest-role one-liner) on a 5-block zoo (4 on-palette, 1 off-palette blue) under neutral light, then the same capture under a bright sun, a warm sun, a warm dusk and a 0.6 dim light,
  roblox-creator-docs: Terrain.yaml:95-109 (MaterialColors), :1027-1051 (SetMaterialColor), MaterialVariant.yaml:80-95,
  partner books: art-review/references/art-bible.md §7 (rows Value bands, Separation targets, Reserved colours, Palette roles), look-check.md K19-K21; art-direction SKILL.md step 9; modeling-craft/references/handoffs.md:14, :44; sound-design references/craft-process.md:18-19, :166; proposals/*.md rows naming the environment books,
  environment-craft/evals/briefs.md briefs 1-3 (read as the agent would)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: B1, class: blocking, check: "C8 V3 + C3 (the new palette-role recipe gives wrong numbers under the stage light, with no error)",
     where: "measure-captures.md:27 (M12 command and its 'wrong number' cell); review.md:101 (VB11 'on the blocks' lit faces no palette cluster lies farther than the palette distance from every palette role ... CIEDE2000 15'); SKILL.md:102 (P11 check); studio-light-air.md §9 zoo bullet ('lit by the stage's own light and time of day')",
     expected: "The zoo is captured under the stage's own light (VB-f, §9), so each block's lit face is compared with the palette roles as they render under that light, as M3 already does for reserved hues (the 'as rendered' second swatch). The recipe's 'wrong number' cell names the stage-light trap",
     observed: "M12 compares rendered lit faces with the art bible's authored role hexes. The distance then grows with the light's level and tint, not with the material's palette. Under ordinary light it sits near the 15 limit, and under dusk, interior or night light on-palette materials fail. The cell names only shadow faces and too-small k. VB11 then tells the agent to fix materials that are right; in eval brief 3 (warm dusk hub, dark cave) that means recolouring materials against the mood the owner asked for, the compensating error LA §3 warns about",
     evidence: "V3, M12 exactly as written, 4 on-palette blocks + 1 off-palette blue: lit faces at 1.05 x role colour: 2.0-2.7 vs blue 36.6 (right). Same capture under a bright neutral sun (x1.25): 13.0-13.6; warm sun (x1.30, 1.22, 1.05): 12.3-15.8 (one false fail); warm dusk (x1.2, 0.9, 0.75): 11.2-15.5 (two false fails); dim interior or night (x0.6): stone 16.5, moss 20.0-20.8 (false fails), the blue 32.7. The maker's run used one light level, so the trap did not show",
     smallest_fix: "M12: build roles.json from the roles as rendered: one reference block per palette role (Color = the role's hex, the stage's plain material) in the zoo row, each sampled with `look_check.py contrast --sample <zoo cap> --fg-box <its lit face> --bg-box <any>` (`fg_sample.hex`), as M3 does for reserved hues; add to the cell: 'the stage light is bright, warm, dim or coloured and the roles are the authored hexes: on-palette faces drift toward or past the limit (J018 review: 15.8 under a warm sun, 20.8 under a dim light)'. studio-light-air §9 zoo bullet: add the role reference blocks and M12 to 'measure each block's box (M1 band, M3 reserved hues)'"}
  - {id: R1, class: recommendation, check: "C3 + C8 V3 (a flat wall in haze passes the flat-fill line)",
     where: "measure-captures.md:18 (M3 'wrong number' cell) and :60 (flat-fill bullet); review.md:102 (VB12)",
     expected: "The 'wrong number' cell names every common case where VB12 passes a flat surface: a light pool and a JPEG are named; Atmosphere is on in every final key view (VB7)",
     observed: "`hue_spread` removes a luminance plane but not a chromaticity gradient. A long wall that recedes from the camera picks up the haze colour toward its far end, so a one-colour wall gains hue spread from distance alone and passes VB12",
     evidence: "V3, M3 as written, flat wall (150,120,90) blending toward haze (170,185,210) along its length: 5 % at the far end 5.6 (flat, right), 10 % 10.0 (passes the 8 limit: false pass), 20 % 18.9, 60 % 48.3. B1 of round 2 is fixed on the same script: flat 3.2 / 0.012 flat; one-hue bricks 3.7 / 0.300 monochrome; +-2 degrees 6.3 monochrome; +-4 degrees 10.5 pass; grey stone with warm and cool patches 20.0 / 0.018 pass",
     smallest_fix: "M3 cell and VB12: 'a surface that recedes into haze reads its haze as variation: box a part at one distance (the near part), or measure the flat-fill boxes on a key view with Atmosphere off'. Or fit and remove a plane from the chromaticity too, as the script already does for log luminance"}
  - {id: R2, class: recommendation, check: "C8 V6 + V11 (second copy of the separation targets)",
     where: "light-and-air.md:45 (VB-a separation targets 1.5:1 and 3:1); coverage §d V11 row for art-director row 38 ('the separation targets stay in VB-a until the bible has a row for them')",
     expected: "One copy of each starting value, other books point to it",
     observed: "art-review/references/art-bible.md §7 now has a 'Separation targets' row with the same starting values (character 1.5:1, marker 3:1), written at 05:57, after this maker's last edit (05:55). The values agree today; the next change must edit two books",
     evidence: "art-bible.md §7 rows 'Value bands' and 'Separation targets'; file times",
     smallest_fix: "VB-a: 'Separation targets: the separation-targets row of `art-review/references/art-bible.md` §7 (PROPOSAL until the game's bible sets them)', keep the two names (character target, marker target) and their meaning here; update the V11 row"}
  - {id: R3, class: recommendation, check: "C4 (engine claim; old text, now leaned on by VB-e)",
     where: "SKILL.md (craft):53 (C-09 'Scripts cannot set terrain ... MaterialColors'); terrain-and-water.md:11 ('All three are NotScriptable: set them in Studio'); studio-light-air.md:68; light-and-air.md:49 (VB-e now asks for terrain patches whose MaterialColors differ in hue)",
     expected: "A colour step a script can do is planned as a script step",
     observed: "The `MaterialColors` property is NotScriptable, but `Terrain:SetMaterialColor(material, Color3)` has security None, so `execute_luau` can set every terrain material colour. The books route this step to the Properties window or to the owner. This text was already in df13ff4 (not a J018 regression), but VB-e now depends on it for hue variation",
     evidence: "Terrain.yaml:95-109 ('cannot be edited by scripts ... To set the color of a material, use Terrain:SetMaterialColor()'), :1027-1051 (security: None)",
     smallest_fix: "C-09 and terrain-and-water.md:11: 'MaterialColors: set through Terrain:SetMaterialColor in execute_luau (one material per call, read back with GetMaterialColor); Decoration and GrassLength stay Properties-window steps'"}
keep: [
  "the rule above all: the place is the backdrop; route, objective, hazards, characters and pickups read first, on a phone, in the busiest moment",
  "the read plan sheet before any image, with a worked example per field; the option round with a reasoned pick and recorded rejections; the ranked work list agreed with the game designer",
  "the grey value and light-direction pass on the greybox by the numbers, written once (LA-15 what, craft §3 step 4 how)",
  "VB12 as repaired: passes on hue spread only, 'monochrome' and 'flat' both fail, both numbers recorded, with the Roblox remedies in VB-e (hue-shifted part Colors, MaterialVariant or SurfaceAppearance ColorMap, terrain patches); my runs agree on every case",
  "VB6 with a number: the stray limit on a second M3 run with the focal elements and eye-path accents excluded (terracotta 0.0, loud orange 0.486 in my run)",
  "band values and the reserved-hue distance by pointer to the art bible §7; the M3 script stops when the spec has no max_de",
  "P7 and P11 now name lines that run",
  "the M3 colour script and its trap cells; M5 with both offsets, M8 through load_probe, M9 settled on EnableFRM false + EditQualityLevel",
  "review.md §7 with 51 lines, each with its input, and the fix-job scope",
  "partner asks with timing (handoffs §7), the modeler brief with the greybox origin and a ground capture, the floor-material list at the kit list for sound",
  "platform-policy routing for blood, violence, alcohol, adult venues and brands",
  "the 16 rejections, each with a sound owner-based reason"
  ]
verdict: fix-first
</spec>
```

## Round 2 findings: status

| Round 2 id | Status | Evidence this round |
| --- | --- | --- |
| B1 flat-fill line passed a one-hue textured wall | fixed | VB12 (review.md:102), measure-captures.md §3 bullet, VB-e, P12. My runs on the script as written: one-hue bricks 3.7 / 0.300 `monochrome`; +-2 degrees 6.3 `monochrome`; +-4 degrees 10.5 pass; flat 3.2 / 0.012 `flat`. Worked example 3 uses hue shifts and boxes above and below the water line. New, smaller gap: haze (R1) |
| R1 P7 and P11 named measures no line ran | fixed; new gap B1 | P7 reads the reserved-hue pixel share (VB4 by M3). P11 now runs through M12 and VB11. M12 runs, but compares rendered faces with authored hexes (B1) |
| R2 second copy of the starting bands | fixed for bands and the reserved distance; separation targets now duplicated (R2) | VB-a, VB1, read-plan band field and the M3 `max_de` point to the bible. The bible gained a separation-targets row after the maker's edit |
| R3 VB6 had no number | fixed | stray limit `PROPOSAL` 0.02 on a second M3 run; my run: terracotta upper wall 0.0, loud orange 0.486, calm walls with green bunting 0.013 |

## C1-C8 results

| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | fail (1 of 207) | All 195 tagged IDs have a row (script against matrix.md), plus 12 untagged and 20 UP rows; every review-line id a row names exists in §7 (51 lines). Re-opened at the landed-in lines this round: the 18 LC rows, MD-09, MD-10, VC-01..VC-09, UI-06, the 6 SI rows, CF-19 and 40 sampled rows (CR, GD, PP, PI, RI, SS, SD, VR, VH, WL): 77 in all. The 16 rejections re-read, all sound. Failed: LC-05 (its check, VB11 by M12, gives wrong numbers under the stage light: B1). LC-09 and MD-10 now pass (R1 is a smaller gap) |
| C2 core principles | pass | `environment-design/SKILL.md` §7, P1-P20, one per UP. The changed checks agree with the master: P7 with UP-07's "share outside gameplay objects near zero"; P11 with UP-11's `palette --roles`; P12 is stricter than UP-12's "one cluster" (one hue fails too) and does not contradict it; the library row for LC-09 is proposed. P11 depends on B1 |
| C3 self-review | fail (B1) | Every other line runs with Studio MCP captures, the M-recipes, scene_audit, partner check-ins and reference images; VB12 haze case (R1) |
| C4 kit rules and engine | pass (R3) | Tool modes used exist (`palette --box --roles --k`, `value`, `thumb`, `contrast --sample`, `scene_audit probe/audit`). MaterialVariant ColorMap checked (MaterialVariant.yaml:80). The MaterialColors claim is old text (R3). No conflict with AGENTS.md, rules or the job card decisions found |
| C5 nothing valuable lost | pass | Changes since round 2 walked: VB-a's band copy became a pointer (values identical in the bible), VB12's rule became stricter, the M3 default `max_de` became a required spec key with the bible's row named. No old rule dropped |
| C6 fixed rules | pass | Only the environment books changed (15 files + 3 new references) plus the two env job files; tools/, templates/, rules/, workflows, evals/ unchanged. Role frontmatter lines 1-10 identical to df13ff4. SKILL.md 113 and 84 lines; descriptions 393 and 390 characters. Headings: sections only appended or retitled (review.md §3). J018 phrase in every changed header and the role comment. No library IDs (scripted grep over all 21 prefixes and UP), no transcript lines, no "Riot" beyond the header phrase, no tips section |
| C7 better work | yes, clearly | see below |
| C8 brief v2 | fail on V3 (B1) | V1 pass (inputs and image budgets per line). V2 pass. V3: M3 (flat fill, VB6) right on every case I ran except the haze case (R1); M12 wrong under the stage light (B1). V4 pass. V6 one duplicate (R2). V7 pass (§3, §5, §6 before §7; re-read line in §1). V8 pass. V10 pass (art-direction's greybox lighting variants, modeler's ground capture and origin, sound's floor list at the kit list all met). V11: answered, one row to update (R2) |

## Will an agent make better work with these books?

Yes, clearly. I read eval brief 1 (swamp edge, falls, cave mouth, ridge) and brief 3 (warm dusk hub, dark cave with one crystal, night sky) as the agent would.

With the old books the agent had a good order and good standards. But its review was one sentence of topics with no measure and no input. With these books the agent:
- writes the read plan first;
- runs one option round and records its pick;
- picks the sun in grey by the numbers;
- keeps the backdrop in its band, with reserved hues out of decoration;
- checks the smallest pickup on every floor at phone size;
- answers 51 lines with named inputs.

Since round 2, two of those lines now catch real faults:
- A one-hue wall made only of value texture (one Color on a built-in material) fails, and VB-e tells the agent how to fix it in Roblox.
- Stray saturation has a number to fail against.

Weak spots that remain:
- The palette-role line (VB11 by M12) measures the stage light as well as the palette (B1). This matters most in brief 3, where the dusk and the dark cave would make right materials fail. The agent would then recolour them against the mood.
- A flat wall in haze passes the flat-fill line (R1).
- The separation targets have a second copy (R2).
- One old engine claim sends a scriptable terrain colour step to the Properties window (R3).

All four are text fixes of one to three lines.
