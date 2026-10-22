---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer environment-designer · claude-opus-5-5 · high · 2026-10-22

# Review: environment-designer books, rebuild round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/environment-designer.md (body) + .agents/skills/environment-design/ (SKILL.md, references/) + .agents/skills/environment-craft/ (SKILL.md, references/; evals/ not reviewed), working tree on top of df13ff4 after repair round 1, 2026-10-22
reviewer: J018 reviewer environment-designer (opus, high)
looked_at_first: [
  role file body, both SKILL.md files, review.md, measure-captures.md, light-and-air.md, worked-examples.md, read-plan.md read in full; handoffs.md §2-§3 and §7, studio-light-air.md §1 and §7-§9, place-reading.md PR-10/13/15/20/27/32/36-38/44-51, ambience.md §2-§5, ambience-in-place.md step 6, audit-and-capture.md camera list; every removed line of git diff df13ff4 over both skills; section headings old vs new in every changed file,
  knowledge/reference/craft/riot/universal-principles.md (UP-01..UP-20; UP-12 and UP-20 text re-read), matrix.md environment column (195 IDs, script), the library check line of LC-05, LC-09, LC-18, MD-10 and of the 14 rows that name a repaired review line,
  my own review of round 1 (every F and R finding re-checked below),
  tools: look_check.py --help (value, contrast, thumb, palette) and srgb_to_lab/srgb_to_linear/ciede2000/hex_to_rgb source (:122-191); scene_audit.py probe/audit --help; the M8 one-liner on tools/tests/fixtures/env/probe_stage.json,
  V3 runs (scratch: scratchpad/env2/): the M3 script cut out of measure-captures.md §3 by awk and run as written on synthetic 1280 x 720 in-scene frames (sky, HUD bar, wall, ground under a light gradient, landmark, dark and light avatars): clean; red patch on the wall; the same patch dimmed; team-blue sky; orange above head height; a value-gradient wall; a 2 px checker wall; a one-hue brick wall (bricks +-15 % value, darker mortar); the same bricks with a small hue shift per brick. Also M6 with --min-ratio, M5 steps 1-3, M2, M10 mirror, M1 --compare-subjects,
  roblox-creator-docs: GlobalSettings.yaml:12, RenderSettings.yaml:66-84, :106-125, :256-261,
  partner books: art-review/references/art-bible.md §7, look-check.md:54, self-review.md RD6; modeling-craft/references/handoffs.md:44; proposals/*.md rows that name the environment books,
  environment-craft/evals/briefs.md briefs 1-3 (read as the agent would)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: B1, class: blocking, check: "C1 (LC-09) + C3 + C8 V3: the flat-fill line passes the library's named mistake",
     where: "review.md:102 (VB12 'hue_spread or value_spread is above the flat limits'); measure-captures.md:59 ('A surface is flat when both are under the flat limits'); SKILL.md:103 (P12 check); light-and-air.md:49 (VB-e rule 'small hue and value shifts')",
     expected: "VB-e, LC-09 and UP-12 ask for small shifts in hue and value; LC-09's named mistake is a monochrome material ('people don't tend to shift their color wheel'), and its roblox_fit says built-in materials are uniform per part, so variation comes from per-part Color, MaterialVariant or a ColorMap. A surface with value texture in one hue fails",
     observed: "VB12 passes a surface when either spread is above its limit. A one-hue wall whose only variation is value (a built-in material's texture under one part Color, or value-only patches) passes on value_spread alone, so the line does not catch the monochrome case it exists for. The maker's own run shows it: 'value-only stone patches 2.6 / 0.114' passes VB12 as written",
     evidence: "V3 run, M3 script as written: one-hue brick wall (bricks +-15 % value, darker mortar) hue_spread 2.686, value_spread 0.2896: VB12 pass. Same bricks with a small hue shift per brick: hue_spread 22.177. Truly flat wall: 2.708 / 0.0075 (fails, right). The hue measure alone separates monochrome from hue-shifted, and the maker's faint-tint run (11.0) still passes a hue limit of 8",
     smallest_fix: "VB12 and measure-captures.md §3: a surface passes when hue_spread is above its flat limit; value_spread above its limit with hue_spread under it is 'monochrome' and fails (record both numbers). P12 can keep its wording. Re-read worked example 3 (silt stains and damp patches are hue shifts, so it still passes)"}
  - {id: R1, class: recommendation, check: "C2 + C7 (core-principle checks name a measure no line runs)",
     where: "SKILL.md:98 (P7 'Reserved-hue cluster share'), SKILL.md:102 (P11 'palette clusters against the bible roles (VB11, FL8)'); coverage row LC-05",
     expected: "After repair round 1 environment colour is measured with the M3 pixel-share script, and §7 lines say what runs",
     observed: "P7 still says 'cluster share'. P11 promises palette clusters against the bible's palette roles, but VB11 measures band and reserved hues only, and FL8 is a capture pair. LC-05's check ('no cluster far from every role swatch') lands only as VB12's image judgement 'stays in one colour family'. An agent reading §7 first may run `palette` on a whole capture, which §0 of measure-captures says gives whole-frame numbers",
     evidence: "palette --help has --box, --exclude-box and --roles, so a boxed run is a real mode",
     smallest_fix: "P7: 'reserved-hue pixel share in environment boxes (VB4, M3)'. P11: either add to VB11 'palette <cap> --box <env boxes> --exclude-box <gameplay> --roles <bible palette>: no cluster far from every role (art director's distance)', or reword P11 to the lines that run"}
  - {id: R2, class: recommendation, check: "C8 V6 + V11 (one copy of the starting values)",
     where: "light-and-air.md:45 (VB-a band values 15-85 %, 8-92 %, luminance 0.020-0.69); measure-captures.md:8 (unit table), :32 (max_de 10); proposals/art-director.md:38",
     expected: "art-review/references/art-bible.md §7 now says it holds 'the kit's only copy of the starting values: other books point here' (bands and the CIEDE2000 10 distance); the art director's row 38 asks the environment books to point there. V11: the row adopted or declined in the coverage file",
     observed: "VB-a and M3 keep their own copies (the numbers agree today). The coverage V11 table does not answer row 38 (the art-director proposals file was written about 2 minutes before the coverage file, so the maker probably did not see it)",
     evidence: "art-bible.md §7 'Value bands' and 'Reserved colours' rows; coverage §d V11 table",
     smallest_fix: "VB-a: 'starting bands: art-review/references/art-bible.md §7 (PROPOSAL)'; keep the separation targets here (the bible has no row for them yet; the maker's own proposal asks for one). M3 max_de: point to the same row. Add a V11 line for art-director row 38"}
  - {id: R3, class: recommendation, check: "C3 (a line with no number to compare)",
     where: "review.md:96 (VB6 'Saturated colour (share_chroma_above) is a small share')",
     expected: "Each numeric line has a starting value marked PROPOSAL (measure-captures.md §0: MEASURED against a starting value)",
     observed: "VB6 reads share_chroma_above but gives no starting share and no way to tell 'on focal elements' from the number; it can only be MEASURED with nothing to compare",
     evidence: "my orange-above run: env share_chroma_above 0.098, player band 0.0; the line cannot say if 0.098 is small",
     smallest_fix: "Give a starting share marked PROPOSAL (or the art bible's palette-role accent share), measured in the environment boxes with focal elements boxed apart"}
keep: [
  "the rule above all: the place is the backdrop; route, objective, hazards, characters and pickups read first, on a phone, in the busiest moment",
  "the read plan sheet before any image, with a worked example per field; the option round with a reasoned pick and recorded rejections; the ranked work list agreed with the game designer",
  "the grey value and light-direction pass on the greybox by the numbers, now written once (LA-15 what, craft §3 step 4 how) with pointers elsewhere",
  "the separation targets (character 1.5:1, marker 3:1, PROPOSAL) and the stated meaning of the symmetric ratio, matching art-review look-check.md:54 and self-review RD6",
  "the M3 colour script: box-only pixel share, the 'as rendered' second swatch, mean chroma by band, temperature by lit/shadow box, and a flat measure that ignores light gradients; every trap in its 'wrong number' cell was reproduced",
  "review.md §7 with 51 lines, each with its input, the fix-job scope, and the three restored old checks (camera clearance FL7, haze VB7, repetition along the camera path FL3)",
  "M5 with both letterbox offsets, M8 through scene_audit.load_probe, M9 settled on EnableFRM false + EditQualityLevel",
  "partner asks with timing (handoffs §7), the modeler brief now with the greybox origin and a ground capture, the film-director row adopted",
  "platform-policy routing for blood, violence, alcohol, adult venues and brands",
  "the 16 rejections, each with a sound owner-based reason"
  ]
verdict: fix-first
</spec>
```

## Round 1 findings: status

| Round 1 id | Status | Evidence this round |
| --- | --- | --- |
| F1 separation lines could not fail | fixed | VB-a targets (light-and-air.md:45); §0 states the ratio (measure-captures.md:9); RD3, VB2, VB7, VB9, VB13, FL1, P1, worked example 2, studio-light-air §9 use them. My M6 run: dark-blue avatar on the brown ground 1.256, `--min-ratio 1.5` gives verdict fail |
| F2 reserved hue measured on sky and HUD | fixed | M3 is box-only. Run: team-blue sky, environment boxes 0.0; red patch 0.00096 in env boxes, 0.0 clean; dimmed patch 0.0 with the authored swatch, as the trap cell says |
| F3 flat-fill check never fired | fixed as asked; new gap B1 | Flat wall 2.708 / 0.0075 (flat); hue patches 62.0. The OR rule passes a one-hue textured wall (B1) |
| F4 three old checks lost their line | fixed | FL7 (review.md:112), VB7 (:97), FL3 (:108) |
| R1 UI-06 text | fixed | light-and-air.md:47 |
| R2 VB5 false fail on a neutral place | fixed | neutral limit `PROPOSAL` 20 (review.md:95) |
| R3 grey pass in five places | fixed | ED step 5, C-15, studio-light-air §1 step 2, VB8 and PS2 point to LA-15 / craft §3 steps 3-4 |
| R4 no scope for fix jobs | fixed | review.md:73; role step 2; ED §6 |
| R5 modeler brief | fixed | handoffs.md §3 `fixed` has the greybox origin and the ground capture (matches modeling-craft handoffs.md:44) |
| R6 M8 input, M5 offset, M11 one-liner | fixed | M8 one-liner ran on the fixture through `load_probe`; M5 and M10 add both offsets; M11 reads `mean_b` / `mean_chroma` from M3 |
| R7 "Riot" in evidence cells | fixed | grep over the books: only the required header phrase |
| R8 wave-2 rows | answered | coverage §d V11; one later art-director row (38) open: R2 |

## C1-C8 results

| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | fail (1 of 207) | All 195 tagged IDs have a row, plus 12 untagged; IDs scripted against matrix.md. Every review-line id a row names exists in §7 (51 lines). Re-opened: the 9 rows that failed in round 1, the 27 rows that name a repaired line (library check vs the line), and 22 sampled rows; 16 rejections re-read, all sound. Failed: LC-09 (B1). LC-05 is carried as an image judgement only (R1) |
| C2 core principles | pass (R1) | `environment-design/SKILL.md` §7, P1-P20, one per UP, master unchanged since round 1; repaired checks in P1, P12, P20 agree with the master (UP-20: about 3:1 markers, at most 3 flashes a second). P7 and P11 name a measure no line runs (R1) |
| C3 self-review | fail (B1) | Every other line runs with Studio MCP captures, the M-recipes, scene_audit, partner check-ins and reference images; VB6 has no starting value (R3) |
| C4 kit rules and engine | pass | M9 doc lines checked (GlobalSettings.yaml:12; RenderSettings.yaml:66-84, :106-125, :256-261). Tool modes used exist (value, thumb, contrast --sample, scene_audit probe/audit). The M3 script lives in the stage folder (write scope allows scripts) with a tool proposal to fold it into look_check. No conflict with AGENTS.md, rules or J018-D2 found |
| C5 nothing valuable lost | pass | Every removed line of the diff walked: old review §4 topics all have §7 lines or ambience.md §5 rows; old E-rows, steps, LA rows and hand-off keys kept or sharpened ("their keys in the map are theirs" kept, ambience-in-place step 6) |
| C6 fixed rules | pass | Only the env books changed (`git diff df13ff4 --stat`: 15 files) plus 3 new references; tools/, templates/, rules/, .agents/workflows unchanged; evals untouched. Role frontmatter lines 1-10 identical to df13ff4. SKILL.md 113 and 84 lines; descriptions 393 and 390 characters. Headings: sections only appended. J018 phrase in every changed header and the role comment. No library IDs (scripted grep for every library prefix), no "Riot" beyond the header phrase, no tips section. LF endings |
| C7 better work | yes, clearly | see below |
| C8 brief v2 | fail on V3 (B1) | V1 pass (inputs and image budgets per line, option and grey-pass budgets). V2 pass. V3: the M3 script, M1, M2, M5, M6, M8, M10 re-run as written and right, except the VB12 pass rule (B1). V4 pass. V6 one leftover copy (R2). V7 pass (§6 ends at 16.8 KB, §7 at 17.7 KB with a re-read line). V8 pass. V9 pass. V10 pass (separation targets match art-review; modeler ask met; film-director row adopted). V11: one later art-director row open (R2) |

## Will an agent make better work with these books?

Yes, clearly, and more so than in round 1. I read eval brief 1 (swamp edge, falls, cave mouth, ridge) and brief 2 (players miss the cave) as the agent would.

With the old books the agent had a good order and good standards, but its review was one sentence of topics with no measure. With these books the agent:
- writes the read plan first;
- runs one option round and records its pick;
- picks the sun in grey by the numbers;
- keeps the backdrop in its band with reserved hues out of decoration;
- checks the smallest pickup on every floor at phone size;
- answers 51 lines with named inputs, and can now get real failures: a dark avatar on dark ground fails at 1.5:1, and a decoration in the team colour shows up even under a blue sky.

For brief 2 it now has a fix-job scope: the lines the change touches, plus five guard lines. It no longer has to choose between 51 lines and none.

Weak spots that remain:
- The flat-fill line passes a wall that has value texture in one hue only (B1). In Roblox that is the common case: one Color with a built-in material.
- P7 and P11 promise cluster measures that no line runs (R1).
- The starting bands are a second copy of the art bible's (R2).
- VB6 has no number to compare with (R3).

All four are text fixes of one or two lines.
