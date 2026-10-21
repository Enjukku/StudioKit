---
type: job
scope: universal
status: active
updated: 2026-10-20
source: J002-T08
supersedes: []
---
> Author: checker · claude-opus-5-5 · high · 2026-10-20

# J002-T08: independent check of the UI/UX designer books

STATUS: done. Read-only review. No file under review was edited. Paths are relative to the kit root. "src" is the line in the source of truth that the finding is checked against.

## 0. Coverage

| Check | Done | Items checked | Result |
| --- | --- | --- | --- |
| K1 citations | done | 112 cited values, timestamps and ids (TC 27, TS 26, TA 12, TP 18, RP 29); the sample table is in §4 | 3 mismatches (M2, M3, S7) + 2 unsourced details (S9, nit N-12) |
| K2 tags | done | every evidence cell in ui-design §4 (19 rows), review §1, motion §1, shops §3-§5, anime §4 | 1 must-fix (M4), 2 nits |
| K3 Roblox facts | done | 21 engine claims against the docs mirror and ui-basics facts | no wrong facts; 1 overstated pixel rule (S3), 3 caveats missing (S14, S19, N-02) |
| K4 arithmetic | done | screen-contract §5 (8 numbers), the pixel S rule (6 numbers), the text rubric (1 conversion) | 2 must-fix (M1, M8), 1 should-fix (S1) |
| K5 consistency | done | outline, rim, lip, radius, state looks, labels, paths, skill names, F-ids (all 23 cited F-ids exist), "Read this file when" paths (all 24 exist), ui-basics U-ids (12 cited) | 3 must-fix (M5, M6, M7), several should-fix |
| K6 format | done | 6 SKILL.md, 8 reference files, role file, evals | pass: frontmatter, overlay lines, ≤ 100 lines each, descriptions 726-846 chars, role keys valid for `tools/sync_harness.py`. Gate note: N-13 |
| K7 followability | done | read every book as a literal instruction set | covered by M5-M8, S1, S3, S6, S11, S12, S14, S16 |
| K8 copyright / IP | done | all quotes, prompts, style lines | pass: owner quotes and the 2-word tutor quote ("like always") only; originals-only rules present; 1 nit (N-11) |

Counts: **must-fix 8 · should-fix 18 · nit 13**.

## 1. Must-fix

| # | Where | What it says | What the source says | Fix (one line) |
| --- | --- | --- | --- | --- |
| M1 | `ui-design/references/screen-contract.md:55` (K4) | Tablet landscape, short side ~768 pt, factor 0.711, 44 pt needs 62 px, 28 pt needs 39 px | Same file :47 says builders fit with **one outer UIScale** (ui-basics U-02). A 1920 × 1080 canvas fitted to a 4:3 iPad (1024 × 768 pt) is width-bound: min(1024/1920, 768/1080) = **0.533**, so 44 pt needs **83 px** and 28 pt needs **53 px**. iPad Air 1180 × 820 pt: 0.615 → 72 / 46 px. The short-side rule works only for screens 16:9 or wider (the two phone rows are correct: 375/1080 = 0.347 → 127 / 81 px; 360/1080 = 0.333 → 144 px; 70 × 0.347 = 24.3 pt) | Write the factor as `min(width ÷ 1920, height ÷ 1080)`, recompute the tablet row, and say the factor is an upper bound because the top-bar inset (CoreUISafeInsets) lowers the usable height |
| M2 | `ui-style-stud/SKILL.md:40`, `:85`; `screen-contract.md:58`; `evals/briefs.md:34` (check 2.2) (K1) | TS side buttons are 70 × 70 canvas px, ≈ 24 pt, "below Apple's 28 pt minor-control line" | `02a-stud-recipes.md:170-173`: 70 × 70 at TS@40:12, then "Too small: switch to Scale tool and scale whole button up" (TS@41:08-41:32); the outline went 5 → 7, a ×1.4 scale ≈ **98 px**; narrowed later (TS@45:33). 98 × 0.347 ≈ **34 pt**: above the 28 pt line, below 44 pt. (`02b-stud-techniques.md:69`, `:159` repeat "70x70 only" and also need the fix) | Say "starts at 70, scaled up ≈ 1.4× (≈ 98 px, inferred from stroke 5 → 7)"; rewrite the consequence to "≈ 34 pt: passes Apple minor, fails Apple frequent 44 pt"; update eval 2.2 |
| M3 | `ui-style-anime/SKILL.md:24` with rows `:28-:34` (K2) | Header rule: "PROPOSAL unless a TA time is given". Every row carries a TA time, and the rows hold numbers: stroke 2-3 px (TA@9:06), stripes 5-15 % (TA@16:11), overlap ⅓-½ (TA@4:43-8:15), inner glow blur 8-16 / spread 0-2 / 40-60 % (TA@1:30), outer glow blur 12-24 / 40-60 % (TA@19:37), card stroke 3 px and radius 6-10 (TA@21:42), selection 3 px (TA@24:54) | `03-anime-photoshop.md:187`: "Values never stated: every pixel size, hex color, gradient stop, angle, opacity, glow size/spread, stroke width, corner radius ...". Under the book's own rule these invented numbers read as TA's values | Mark each number PROPOSAL inside its cell and keep the TA time only for the technique (or invert the header rule: "all numbers PROPOSAL; TA times cite the technique") |
| M4 | `ui-design/SKILL.md:40` (D-01), `:44` (D-05), `:47` (D-08) (K2) | D-05: "Pick one rubric per project, write it down, never average them", tagged "RA-44..48 V". D-08: per-screen focus map, tagged "RA-53..55 V". D-01: "RA-32, RA-64 V" | `05a-research-rules.md:182` RA-48 = **OPINION**; `:189` RA-55 = **OPINION** (and the per-screen focus-map content is RA-55); `:156` RA-32 = **OPINION**. The skill header `:6` promises "tags kept as the paper gives them"; `05a:13` "A row tagged OPINION ... is never a rule of the platform" | Tag per id: "RA-44..47 V; RA-48 O", "RA-53..54 V; RA-55 O", "RA-32 O; RA-64 V" |
| M5 | `ui-style-cartoon/SKILL.md:58` vs `:61`; `ui-style-stud/SKILL.md:57` vs `:60`; `ui-style-anime/SKILL.md:53` vs `:55`; `ui-figma/SKILL.md:48` (K5, K7) | Hover / gamepad focus = white outline. Selected = white outline. F-15: "Selected = white outline on hover/select" | `ui-design/references/review.md:25-26` check 08 "one clear target", check 09 "selected / owned / equipped ... distinguishable"; `ui-design/SKILL.md:42` D-04 "every state, named apart". In a grid with gamepad focus on item A and item B selected, both show the same white outline: a literal build fails checks 08 and 09 | Give focus and selected two different marks in every book (e.g. focus = outer white ring + scale, selected = fill or corner badge); split F-15 into Focused and Selected |
| M6 | `ui-figma/SKILL.md:61` and F-11 `:44` vs F-03 `:36`, `ui-style-cartoon/SKILL.md:22`, `:27`, `:31`, `:94`; `ui-style-anime/SKILL.md:33`, `:41` (K5) | ui-figma rule: "One outline weight, one radius, one lip depth ... per game". F-03: lip "equal on every control **of a size**". Cartoon: "one radius everywhere" (:22) but "10 px all controls (12-16 for big panels)" (:27); lip "4 px buttons / 6 px cards" (:31); self-check "identical across all controls" (:94). Anime: card radius 6-10, search radius 6 | Two different rules for the same token; the cartoon book breaks its own signature and self-check, and the ui-figma final check fails every cartoon screen | Define radius and lip as a per-size ladder in ui-figma (F-03, F-11, §5) and make the cartoon signature and self-check say "one value per size step" |
| M7 | `ui-style-stud/SKILL.md:28` vs `:77`, `:93`; `evals/briefs.md:37` (K5) | Token: inner stroke 4 px "(3 on tiny, 5 on 70 px side buttons)". Build: "UIStroke (Inner 4)". Self-check: "inner 4 equal on every block". Eval 2.5: "inner 4 consistent" | Source mixes too: shop side button raised to 5 (`02a:180`, TS@45:56), index side button 3 (`02a:184`), plus button 3 (`02a:207`). The book gives the agent two rules | Pick one: "4 everywhere" (and drop the exceptions) or a per-size ladder used in all four lines |
| M8 | `ui-style-pixel/SKILL.md:41` vs `:23-26` (K4, K7) | Press Start 2P "at sizes that are multiples of 8 canvas px" | Same book §3: every art pixel = S canvas px (S = 3). Press Start 2P is drawn on an 8-unit grid, so one glyph pixel = size ÷ 8. At 8 or 16 canvas px a glyph pixel is 1-2 canvas px ≈ 0.35-0.7 pt on the small phone (× 0.347): the blur that §3 exists to stop | "Multiples of 8 × S canvas px (24, 48 at S = 3)"; note that TextLabel glyphs are anti-aliased, not Pixelated |

## 2. Should-fix

| # | Where | Problem and evidence | Fix |
| --- | --- | --- | --- |
| S1 | `screen-contract.md:62` (K4, K7) | Gives the XAG mobile glyph target (18 px at 100 DPI ≈ 4.6 mm) with no conversion to canvas px, and tells the agent to flag text below it. Arithmetic: 4.57 mm × 163 pt/in ÷ 25.4 ≈ **29 pt**, so ≈ **84 canvas px** of glyph height on the small iPhone (÷ 0.347). Every style ladder is far below it (cartoon small 22-24 ≈ 8 pt `ui-style-cartoon:35`; stud button 25 `ui-style-stud:34`), and there is no default text rubric (the touch rubric has one) | Add the conversion line and a default PROPOSAL text rubric, or say the style ladders are pre-rubric starting values |
| S2 | `screen-contract.md:49` (K3) | The conversion assumes Roblox GUI px on a phone = iOS pt / Android dp. No doc line supports it; `06b:242` says the paper gives no mapping to Roblox pixels | Mark it as an assumption and add a check (on-device `AbsoluteSize` vs the device's pt size) |
| S3 | `ui-figma/references/roblox-handoff.md:46`, `:63`, `:67` vs `ui-style-pixel/SKILL.md:27`, `screen-contract.md:47` (K3, K5) | Handoff: pixel PNG "at 1×" with "integer UIScale steps", and baked art "at 1× of its on-screen size at 1920 × 1080". Pixel book: export at **1 art px** (= 1/S of the canvas size) and the fit scale is not an integer. One fitted UIScale on a phone is 0.347, so integer steps cannot apply there | Handoff: "pixel art exports at 1 art px (1/S of canvas size); integer scale only where the layout allows (PC)" |
| S4 | `ui-style-pixel/SKILL.md:24` (K5) | "(MCP cannot; figma-mcp §5)". View settings are in `figma-mcp.md` §7 (`:79`); §5 is reading back and exporting | Change to §7 |
| S5 | `.agents/roles/ui-ux-designer.md:33`, `evals/briefs.md:13` (K5) | Label "Figma-verified". `AGENTS.md:45` allows gate-verified / MCP-verified / owner-confirmed / not verified, and `review.md:59` repeats that list | Use "MCP-verified (Figma)" or ask the owner to add the label to AGENTS.md |
| S6 | `ui-figma/SKILL.md:48`, `figma-mcp.md:67` (K5) | Variant set `Idle, Hover, Pressed, Disabled, Selected` has no Focused, Loading/Pending or Cooldown state. `screen-contract.md:32` lists hover · pressed · focused (gamepad) · disabled · cooldown; cartoon `:62` and stud `:62` add pending | Add `Focused`, `Pending`, `Cooldown` to the variant list |
| S7 | `roblox-handoff.md:62` (K1) | "Design at 1920 × 1080 (all four tutorials)". The TA notes give no canvas size (`03-anime-photoshop.md` §1-§3); `screen-contract.md:47` correctly says TC, TS, TP | "TC, TS, TP; TA not stated" |
| S8 | `ui-style-pixel/SKILL.md:41`; `roblox-handoff.md:53`, `:55` (K3, K5) | Pixel book offers Builder Sans. Handoff: "Pick fonts from this list"; Builder Sans is not on it, and its Figma availability is not shown. The handoff's claim that Figma has every listed family is not sourced (the mirror covers Roblox only) | Drop Builder Sans or add it with a Figma check; say "confirm in Figma with `listAvailableFontsAsync`" (`figma-mcp.md:39` already says so) |
| S9 | `ui-design/references/motion.md:14` (K1) | "a small move plus a quick projectile fixed it (E M04)". The notes hold only "collision animation suggested the wrong damage rule" (`06b:43`); the fix detail is in no note | Cite the RP line, or drop the detail |
| S10 | `ui-figma/references/figma-mcp.md:13` (K6) | "one Pro team plan on 2026-10-20; use its key". An owner-account fact in a `scope: universal` note (`:3`); `rules/knowledge.md` §3: "Never mix scopes in one note" | Move it to the game profile or an overlay; keep "call `whoami`" here |
| S11 | `ui-ux-designer.md:33` (K7) | "the studio-operator captures Studio screenshots". `.agents/roles/README.md` lists studio-operator as **planned**: no such agent exists | "Request captures through the lead (studio-mcp skill)" |
| S12 | `ui-ux-designer.md:6` vs `:17` (K7) | Frontmatter `skills:` lists all four style books; the body says "only the one style book". In Claude Code, `skills:` on a subagent preloads each listed skill at start (harness behaviour, not checked in this repo), which loads all four books each run | Keep only ui-design, ui-figma, ui-basics, platform-policy in `skills:`; load the style book on demand |
| S13 | `ui-ux-designer.md:27`, `evals/briefs.md:13` vs `review.md:59`, `ui-basics/SKILL.md:28` (K5) | Self-review captures: "phone and PC" vs "phone, tablet, PC (and TV)" | Use one list everywhere (review §5) |
| S14 | `ui-style-pixel/SKILL.md:81` (K3) | Whole toolbar in a CanvasGroup at 0.3. `CanvasGroup.yaml:17-18`: CanvasGroup "always has ClipsDescendants set to true". Outer strokes (2S), glows and the edge-fade strip at the group edge get cut | Add "pad the CanvasGroup past the outermost stroke and glow" |
| S15 | `ui-style-pixel/SKILL.md:62` (K2) | Low-health blink "≤ 2 Hz", with no temporal flash test and no player control. `06a:125` RB-19 says "under three flashes" is not a safety rule; `:128` RB-22; `:124` RB-18 says players control blinking; review check 16 | Add "temporal flash check (review 16); player can turn it off" |
| S16 | `ui-style-pixel/SKILL.md:35`, `:38` vs `:85`, `:93` (K4) | "14 canvas-px (≈ 5 art px)", "5 canvas-px gaps (≈ 2 art px)": 14/3 = 4.67 and 5/3 = 1.67 are not integers, but the book says integer art-px placement only | Give integer art px (e.g. 5 art px = 15 canvas px; 2 art px = 6) |
| S17 | `ui-style-cartoon/SKILL.md:77`, `ui-style-stud/SKILL.md:77` (K3) | Build tables use `UIStroke` Inner / Outer as plain N. `UIStroke.yaml:11-13` "Some properties may require ... Improved UIStrokes beta"; the handoff (`:28`) says confirm in Studio, fallback nested Frame. The caveat is lost where the builder reads it | Add "(confirm Inner/Outer live, handoff §1; fallback nested Frame)" |
| S18 | `ui-style-anime/SKILL.md:77` (K7) | Oversized art "ImageLabel sibling above the card with ClipsDescendants off". The unit list is a scroll list, and a ScrollingFrame clips its children, so top-row art that breaks out of its card is cut | Note: leave top padding in the scroll list for the overshoot |

## 3. Nits

| # | Where | Note |
| --- | --- | --- |
| N-01 | `roblox-handoff.md:29` | "Never tween Thickness on text (U-08)": the rule is ui-basics **U-11** (`ui-basics/SKILL.md:43`) |
| N-02 | `roblox-handoff.md:27` | Beta gradient types: the docs also list **Elliptical** and the Scale / TileMode properties as beta (`ui/appearance-modifiers.md:79-81`, `:168`, `:201`) |
| N-03 | `image-generation.md:19`, `:51`; `roblox-handoff.md:70`, `:75` vs `screen-contract.md:13`, role `:39` | Placeholder `<screen>` vs `<screen-id>`; role write scope lists spec.md, refs/, export/ but not `figma-ids.json` (`figma-mcp.md:31`) |
| N-04 | `image-generation.md:18` | "places the image ... on the `Refs` page": `generate_image` has no page parameter; it creates a new image frame (tool schema). Add "then move it to Refs" |
| N-05 | `roblox-handoff.md:70` vs `figma-mcp.md:71` | `get_screenshot(nodeId, maxDimension)` vs `(fileKey, nodeId, maxDimension)`: the tool requires fileKey |
| N-06 | `review.md:15` | "(tags as given)", but 16 of 22 rows show no tag; most rows are OPINION gates in the source (`06b:65-86`) |
| N-07 | `ui-style-anime/SKILL.md:79` | "≤ 512² ... ui-design / handoff §3": the rule is only in handoff §3 |
| N-08 | `ui-design/SKILL.md:6`, `shops-rewards-onboarding.md:39` | The paper is dated 2026-10-21, one day after these notes (2026-10-20). Say "paper's stated date" |
| N-09 | `ui-design/SKILL.md:51` | D-13 "RA-79..82 V": RA-82 is OPINION (`05a:231`); the row text holds only V content |
| N-10 | `ui-style-stud/SKILL.md:79` | "T-free ImageLabel" is unclear |
| N-11 | `image-generation.md:39` vs `:46` | The stud style line "Roblox-like toy brick look" names a brand while the rule forbids "in the style of <named ... game>". Low risk (platform look), but word it as "toy-brick plastic look" |
| N-12 | `ui-style-cartoon/SKILL.md:44` | "~⅓ of its height (borrowed from TA@8:01)": TA gives no amount (`03:69` "Overlap amount: not stated") |
| N-13 | gate | `python tools/sync_harness.py --check` reports DRIFT for `preproduction` and `game-concept` files (other jobs); the generated `.claude/skills/ui-*` copies are identical to `.agents/skills/ui-*` |

## 4. K1 sample (checked against the notes)

OK = matches. ✗ = mismatch (see finding).

| Cited in book | Value | Note line | Result |
| --- | --- | --- | --- |
| radius 10 TC@2:43, @31:42 | 10 | 01a:96, :84 | OK |
| outline 3 TC@10:16-11:16 | 3 px black | 01a:144-145 | OK |
| halo 6 TC@11:45 | white 6 | 01a:146 | OK |
| halo shadow Y 0 TC@11:57 | Y 4 → 0 | 01a:147 | OK |
| rim 4 TC@38:22 | 4 Inside | 01a:169 | OK |
| lip "a couple" TC@9:58 | not stated | 01a:143 | OK (marked PROPOSAL) |
| panel stroke 5 dashed TC@3:21-4:55 | 5, dashed | 01a:98-101 | OK |
| well inner shadow 30 % TC@5:45-6:48 | Y 0, 30 % | 01a:117-120 | OK |
| Fredoka One TC@7:26 | yes | 01a:123 | OK |
| default Y 4 TC@6:05 | yes | 01a:118 | OK |
| text inset 9 TC@8:28 | 9 | 01a:125 | OK |
| gap 41 TC@18:02 | 41 | 01a:157 | OK |
| Soft light TC@14:24 / Overlay TC@22:07 | yes | 01a:151, :189 | OK |
| half-tone flip TC@22:48 | yes | 01a:191 | OK |
| selection colours TC@35:51 | yes | 01b:33 | OK |
| weight not copied TC@39:25 | yes | 01b:121 | OK |
| flatten breaks on resize TC@25:51 | yes | 01b:120 | OK |
| align drift TC@40:29 | yes | 01b:35 | OK |
| white-on-white highlights TC@28:33 | yes | 01a:214 | OK |
| Ctrl+D repeat TC@17:44 | yes | 01a:156 | OK |
| zoom/pan TC@19:21 | yes | 01a:71-72 | OK |
| rarity gold/purple/green TC@35:45 | yes | 01a:165-170 | OK |
| role colours TC@19:48, @25:11, @27:42 | green, red, grey | 01b:91 | OK |
| black depth copy TC@24:48 | black | 01a:201 | OK |
| 1920 × 1080 TC@1:00 | yes | 01a:61 | OK |
| radius 10 well TC@6:48 / close TC@29:11 | 10 | 01a:122, :226 | OK |
| grey well stroke TC@19:02 | Outside | 01a:129 | OK |
| outline 5 TS@3:36, @6:33 | 5 | 02a:63, :78 | OK |
| inner 4 TS@12:02 | 4 | 02a:81 | OK (see M7) |
| inner 5 TS@46:05 | 5 on shop | 02a:180 | OK (see M7) |
| lip 7 TS@1:00:59 | 7 | 02a:224 | OK |
| panel black TS@3:05 | opacity not stated | 02a:62 | OK (PROPOSAL) |
| title 64 / 4 / Y 4 TS@12:47-13:55 | yes | 02a:89-92 | OK |
| side text 25 / 3 / 3 TS@42:06, @59:54 | yes | 02a:174, :188 | OK |
| small 2 / Y 2 TS@19:32, @55:49 | yes | 02a:126, :210 | OK |
| counter 46 / 3 / Round TS@52:10, @55:54 | yes | 02a:198-200 | OK |
| font inaudible TS@13:01 | yes | 02a:90 | OK |
| padding 30, gap 24 TS@31:56, @30:29 | yes | 02a:145-147 | OK |
| **side buttons 70 × 70 TS@40:12** | 70, then scaled up | 02a:170-173 | ✗ M2 |
| stud tile 4 × 4 TS@10:20 | "perfect 4x4" | 02a:101 | OK |
| three studs TS@57:17 | yes | 02a:220 | OK |
| scale 5 → 7 TS@41:46 | yes | 02a:173 | OK |
| Round join TS@52:49 | yes | 02a:200 | OK |
| 9 digits TS@51:43 | yes | 02a:197 | OK |
| icon shadow Y 3 TS@17:17 | yes | 02a:124 | OK |
| vectorize TS@15:35 / bake TS@17:39 | yes | 02b:36-37 | OK |
| icon under text TS@47:50 | yes | 02a:182 | OK |
| sunburst Overlay TS@44:36 | yes | 02a:179 | OK |
| lock + marquee TS@58:42 | yes | 02a:42 | OK |
| Enter crop TS@27:52 | yes | 02a:103 | OK |
| gem copies TS@21:16 | yes | 02a:128 | OK |
| slow mode on TS@58:11 | yes | 02a:222 | OK |
| exit lip TS@9:09 | yes | 02a:112 | OK |
| Montserrat ExtraBold TA@21:28 | yes | 03:80 | OK |
| style not UX TA@9:52 | yes | 03:24 | OK |
| header over search TA@8:01 | yes | 03:69 | OK |
| bright = clickable TA@19:23 | yes | 03:90 | OK |
| white outline TA@24:54 | width not stated | 03:82 | OK technique / ✗ value M3 |
| icon breaks box TA@22:04 | yes | 03:81 | OK |
| 6 → 5 columns TA@28:18 | yes | 03:83 | OK |
| file lost TA@25:46 | yes | 03:24 | OK |
| rarity tiers TA@29:12 | mythical, legendary, uncommon | 03:84 | OK |
| **anime token numbers (7 rows)** | not stated | 03:187 | ✗ M3 |
| render copied TA@4:22 | yes | 03:175 | OK |
| canvas TP@0:13 | 1920 × 1080 | 04:20 | OK |
| pencil 1 px TP@5:46 | yes | 04:53 | OK |
| 2 px black TP@7:36 | yes | 04:54 | OK |
| panel 60 / 50 % TP@17:41, @26:48, @31:29 | yes | 04:90, :103, :115 | OK |
| slot 12 %, offset 14 TP@33:02-34:24 | yes | 04:117 | OK |
| title bar 20 % TP@22:01 | yes | 04:93 | OK |
| shine 7 % TP@1:00:15 | yes | 04:95 | OK |
| gap 5, group 70 % TP@13:06, @1:00:45 | yes | 04:78, :82 | OK |
| rows 4-5, bars 5-6 TP@40:12, @50:42 | yes | 04:131, :156 | OK |
| glow Normal 10 % TP@16:21-16:53 | yes | 04:81 | OK |
| Normal only TP@16:28 | yes | 04:225 | OK |
| padding 23 + 8 | yes | 04:114 | OK |
| leaderstats below core UI TP@35:16 | yes | 04:127 | OK |
| canvas group fix TP@40:57 | yes | 04:132 | OK |
| corners only TP@18:14 | yes | 04:62 | OK |
| mirror fix TP@19:30-21:56 | yes | 04:57 | OK |
| motion-blur fade TP@15:42 | yes | 04:60 | OK |
| zoom-out check TP@9:37 | yes | 04:64 | OK |
| Figma weak for pixel TP@5:51 | yes | 04:25 | OK |
| H01 83 / 14 / 3 % 2025 | VERIFIED | 05a:101 | OK |
| RA-45 44 × 44 / 28 × 28 pt | VERIFIED | 05a:179 | OK |
| RA-46 48 dp + 8 dp; 24 dp icon | VERIFIED | 05a:180 | OK |
| RA-47 15 mm / 24 mm | VERIFIED | 05a:181 | OK (≈ 96 pt arithmetic OK at 163 pt/in) |
| **RA-48 never average** | OPINION | 05a:182 | ✗ M4 |
| **RA-55 focus map** | OPINION | 05a:189 | ✗ M4 |
| **RA-32** | OPINION | 05a:156 | ✗ M4 |
| RB-02..04 26 / 18 / 18 px | VERIFIED | 06a:108-110 | OK |
| RB-05 200 % | VERIFIED | 06a:111 | OK |
| RB-08..11 4.5 / 3 / 3 / 7 :1 | VERIFIED | 06a:114-117 | OK |
| RB-13 colour not alone | VERIFIED | 06a:119 | OK |
| RB-17 TextScaled ignores text size | VERIFIED | 06a:123 | OK |
| RB-23 ratio 3 | VERIFIED | 06a:138 | OK |
| U05 > 2,000 buffs, 4 slots | VERIFIED facts | 05a:153 | OK |
| U01 45,000 players, return lower | VERIFIED | 05a:166 | OK |
| M01 200 / 300 ms | VERIFIED, one video | 05b:188-189 | OK |
| C02 ≈ 2.8 s once daily | EXPERIENCE | 05b:191 | OK |
| M11 70-700 ms | VERIFIED non-game | 05b:193 | OK |
| M07 40 / 80 ms network | VERIFIED scope | 05b:195 | OK |
| R14 odds before purchase, 100 % | VERIFIED | 05b:101-111 | OK |
| R22 prompt closed ≠ delivery | VERIFIED | 05b:99 | OK |
| T11 ad rules, conflict | VERIFIED / OPINION | 05b:113-123 | OK |
| RA-15 young audience claim ≠ buy | OPINION | 05a:139 | OK |
| RA-89 1024² = 4× 512² | VERIFIED | 05a:243 | OK |
| 22 checks, do-not list, failure modes | OPINION / mixed | 06b:39-90 | OK |
| **Hearthstone fix detail (M04)** | not in notes | 06b:43 | ✗ S9 |

## 5. K3 engine claims confirmed (no finding)

UIStroke `BorderStrokePosition` Inner / Center / Outer + `BorderOffset` (`ui/appearance-modifiers.md:310`; beta note `UIStroke.yaml:11-13`, handoff hedge correct) · sibling UIStrokes ordered by ZIndex, equal ZIndex undefined (`:374-376`) · UIStroke child UIGradient for gradient strokes (`:263`, `:277`) · no Thickness tween on text (`:258`) · tween gradient Offset / Rotation, not Color / Transparency (`ui/ui-gradient.md:56-64`) · UIShadow live, Text / Inset / ShowBehindParent beta (facts.md:109-110; `appearance-modifiers.md:443`) · radial / conical gradients beta (`:79-89`) · `ResampleMode = Pixelated` keeps hard pixel edges (`ImageLabel.yaml:209-221`) · `ScaleType = Tile` + `TileSize` UDim2 (`ImageLabel.yaml:324-335`) · 9-slice corners fixed, edges one axis (`ui/9-slice.md:38-46`) · CanvasGroup clips to UICorner, costs texture memory, static size (`CanvasGroup.yaml:12-31`) · CoreUISafeInsets for interactive UI (facts.md:75) · no blend property on GuiObjects (no match in `GuiObject.yaml`) · all 18 listed fonts plus Builder Sans exist as `rbxasset://fonts/families/*.json` (`_api-reference/datatypes/Font.yaml`) · `GuiService.ReducedMotionEnabled` (`production/publishing/accessibility.md:186`) · Figma `generate_image` model `gpt-image-2.5-sunburst` is in the tool's enum; the other two are Gemini (tool schema).
