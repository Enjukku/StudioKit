---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer environment-designer · claude-opus-5-5 · high · 2026-10-22

# Review: environment-designer books, round 4 (J018 stage 3, focused round)

```text
<spec>
artifact: .agents/roles/environment-designer.md (body) + .agents/skills/environment-design/ + .agents/skills/environment-craft/ (evals/ not reviewed), working tree after repair round 3, 2026-10-22 (book files last written 06:35-06:37; role file not touched since 05:34)
reviewer: J018 reviewer environment-designer (opus, high)
looked_at_first: [
  my round-3 review (B1, R1-R3),
  measure-captures.md in full (M3 cell, M4 cell, M12 row, §3 script and its grey and flat-fill bullets), studio-light-air.md §9 and :68, review.md VB4-VB6 and VB11-VB12, light-and-air.md VB-a and VB-f, environment-design SKILL.md P7/P11/P12, environment-craft SKILL.md step 7 and C-09, terrain-and-water.md:11; grep over all env books for M12, zoo, palette role, as rendered, neutral light,
  tools/art/look_check.py contrast and palette (--sample pairs, fg_sample = per-channel sRGB median; --roles format), srgb_to_linear / linear_to_srgb,
  roblox-creator-docs Terrain.yaml:1027-1035 (SetMaterialColor, capability Environment), :683-690 (GetMaterialColor),
  V3 runs (scratch: scratchpad/env4/): pipe.py = M12 with its two one-liners cut out of the M12 row by regex and run as written on 8 synthetic 1280 x 720 zoo captures (4 plain role reference blocks; material blocks with a +-12 % value texture: 2 exact on-palette, 2 on-palette near the limit at authored 12.0 and 12.1, 2 off-palette near the limit at 17.0 and 17.3, 1 blue at 30.4). Lights: my round-3 multipliers x1.05, x1.25, warm sun, warm dusk, x0.6; the maker's model A neutral sun, a dim neutral, a bright neutral. study.py / cal.py: the same comparison at colour level for 4 roles x 8 Lab directions x authored 12-19 under 15 lights, and a model A neutral calibrated so a mid grey renders as authored. wb.py: the §3 script cut out by awk, `grey` from the grey block's lit face and from its shadow face, beige floor 0 / 50 / 100 % in shadow, 4 lights
  ]   # the maker's "Repair round 3" coverage note was seen at the start (one grep of the coverage file) before the books were read in full; every number below is from my own runs
findings:
  - {id: R1, class: recommendation, check: "C8 V3 (M12 near the limit; the neutral-light capture is the safety net but is not defined)",
     where: "measure-captures.md:27 (M12: 'A material passes when it passes on every zoo capture'; wrong-number cell 'the neutral-light capture catches them'); review.md:101 (VB11 '... on the capture of each look and on the neutral-light capture'); studio-light-air.md §9 ('once under a neutral light')",
     expected: "The measure gives the right verdict, or the cell names where it does not. The capture that has to catch the dim and night false passes has defined settings",
     observed: "B1 is fixed: with roles as rendered, exact on-palette blocks read 0.1-1.5 and the blue fails under every light. But the distance between two rendered colours still moves by up to about 5 near the limit, through clipping, exposure and any tone curve. Two effects follow. (a) The rule 'passes only when it passes on every capture' turns a bright or clipped look into a false fail for a right material, and VB11 then sends the agent to recolour it. (b) 'A neutral light' has no settings (sun colour, brightness, exposure, post effects). Under a dim, bright or tone-mapped neutral light, off-palette materials a little past the limit pass. So the claim 'the neutral-light capture catches them' holds for the maker's olive (17.3 -> 16.1), but not in general",
     evidence: "pipe.py, M12 as written, limit 15. Material at authored 12.0 (wood, darker): x1.05 12.7; x1.25 15.8 (false fail); warm sun 15.9 (false fail); bright neutral 16.6 (false fail). Authored 12.1 (terracotta +a): model A neutral sun 14.2; bright neutral 16.1 (false fail). Authored 17.0 (stone, lighter): x1.05 17.2; model A neutral sun 13.5, dim neutral 13.2, bright neutral 12.5 (all false passes on a neutral capture). Authored 17.3 (moss -b): dim neutral 14.9 (false pass). study.py, colour level: false fails at authored 12.0-13.6 under x1.25, warm sun (x1.30,1.22,1.05) and bright or hot neutrals. False passes at authored 17-19 in the lighter direction under the maker's model A neutral sun (13.6-14.4). cal.py: the model A neutral with grey calibrated to render as authored still gives 13.9-14.6 for authored 17.0-17.1 (lighter), and 15.5 for authored 13.6 (terracotta +a). The tool runs without error in every case",
     smallest_fix: "M12 cell: add 'near the limit (about 4 either side: 11-19 at 15) the distance moves with exposure, clipping and tone curve (J018 rev4: authored 12.0 read 15.8-16.6 under a bright or warm sun; authored 17.0 read 12.5-13.5 under neutral lights): record such a material as near-limit, and settle it on the authored values (CIEDE2000 from the part's Color to the role hex, exact for a plain Color) or by the art director on the zoo image'. Base the palette verdict on the neutral capture, and record each look's numbers. A material over the limit only under one look is a look note for the art director, not a recolour. Define the neutral capture in §9: white sun, no ColorCorrection or Bloom, and exposure set so that the grey block's lit face samples within about 2 of its authored hex (`contrast --sample`)"}
  - {id: R2, class: recommendation, check: "C8 V3 (new M3 `grey` key: which face of the grey block)",
     where: "measure-captures.md:33 (spec key `grey`: 'the hex of a mid-grey reference block as rendered under the same light'), :62 (`grey` bullet); review.md VB5, VB6",
     expected: "The sample that white-balances the frame is taken from the face lit by the look's main light, as the M12 role samples are (lit faces)",
     observed: "The key names the block but not the face. Under a coloured look the sun and the ambient have different colours. A grey sampled on the shadow face, or a grey block that stands in shade in the view, white-balances to the ambient. Sunlit surfaces then read more chromatic than the raw number: a false fail of the neutral limit. This is the error the key exists to remove",
     evidence: "wb.py, §3 script as written, beige floor #9A8F80, player-band mean chroma (neutral limit 20), raw / grey from the lit face / grey from the shadow face. Floor fully in sun: warm sun 13.5 / 8.2 / 20.2; warm dusk 17.4 / 7.2 / 25.8; deep sunset 23.2 / 7.5 / 31.4. Floor half in shadow: dusk 12.0 / 8.0 / 15.7; sunset 16.1 / 10.4 / 18.1. With the lit face, every case stays under 20 (max 13.4: a sunset floor fully in shadow). The maker's runs had no shadow and so did not show this",
     smallest_fix: "Spec key `grey`: 'sampled on the grey block's face lit by the look's main light (sun, moon or the zone's key light), never on a shadow face or a block in shade'. Same words in the §9 zoo bullet ('`grey` from the grey block')"}
keep: [
  "M12 with the roles as rendered from plain reference blocks in the same capture: the systematic stage-light error of round 3 is gone (exact on-palette 0.1-1.5 under all 8 lights; blue 23.0-36.2 fails everywhere)",
  "the reference blocks in the zoo (palette roles, reserved hues, mid grey) and the reserved hue as rendered from its reference block on the zoo",
  "the M3 `grey` white balance on chroma only, with mean_a / mean_b and the reserved share left raw (lit-face sample: right on every case I ran)",
  "VB12 and the flat-fill boxes from a key view with Atmosphere and fog off (round-3 R1)",
  "VB-a pointing to the bible's separation-targets row (round-3 R2)",
  "C-09, terrain-and-water and studio-light-air §6/:68: terrain material colours through Terrain:SetMaterialColor (round-3 R3; Terrain.yaml:1027-1035, :683)",
  "everything in my round-3 keep list (not touched this round)"
  ]
verdict: pass (ready for the next review)
</spec>
```

## Round 3 findings: status

| Round 3 id | Status | Evidence this round |
| --- | --- | --- |
| B1 M12 compared rendered lit faces with authored role hexes | fixed in every place named | M12 step 1 (role reference blocks, `contrast --sample` → `roles-rendered.json`), steps 2-3 on it; wrong-number cell names the stage-light trap; VB11; P11; studio-light-air §9 zoo bullet; craft SKILL step 7; VB-f. My runs of the commands as written: on-palette 0.2-1.5 under my round-3 lights x1.05, x1.25, warm sun, warm dusk and x0.6, where round 3 gave 2.0-20.8. The blue fails under every light. Residual error near the limit and an undefined neutral capture: R1 |
| R1 flat wall in haze passed VB12 | fixed | `flat` boxes from a key view with Atmosphere and fog off (M3 cell, §3 spec, flat-fill bullet, VB12). The maker's "near third still passes at 20 %" agrees with my round-3 numbers |
| R2 separation targets copied | fixed | VB-a points to art-bible §7; "1.5:1" no longer in the environment books |
| R3 MaterialColors routed to Properties | fixed | C-09, terrain-and-water:11, studio-light-air:68; doc lines checked (Terrain.yaml:1027 SetMaterialColor, capability Environment; :683 GetMaterialColor) |

## Fixed-list checks

| Check | Result |
| --- | --- |
| Only this role's books and its two job files changed this round | pass. Files newer than my round-3 review in this role: measure-captures, studio-light-air, terrain-and-water, both SKILL.md, light-and-air, review.md, coverage, proposals. The other new files belong to other roles (rigger, sound, VFX, art director) |
| Frontmatter unchanged | pass. The role file was not touched this round. Its frontmatter is unchanged against df13ff4. Both skill descriptions are unchanged |
| SKILL.md at most 500 lines; descriptions at most 400 characters | pass: 113 and 84 lines; 393 and 390 characters |
| No renumbering | pass: every heading in the changed files is the same as at df13ff4, or appended (review.md §3 retitled, not renumbered) |
| No citations or Riot names in bodies | pass: no library IDs (grep over the prefixes); "Riot" only in author or header lines |
| No new conflict | none found. The new `grey` key leaves the old output unchanged when it is not set. M4 and VB5/VB6 point to it |

## Will an agent make better work with these books?

Yes. The palette-role line now measures the material, not the light. In eval brief 3 (warm dusk hub, dark cave), the materials that are right now pass, so the agent no longer recolours them against the mood. The two remaining gaps are small, and the fixes are text only:
- A material within about 4 of the limit can get the wrong verdict from lighting effects alone (R1).
- The grey sample needs the lit face named (R2).
