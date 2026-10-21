# Captures, the look-check tool and the review checklist

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `art-review`. Sources: `knowledge/reference/art-direction/02` §5, `04` §4.3-4.5; tool `tools/art/look_check.py` (tests `tools/tests/test_look_check.py`). Formulas: WCAG relative luminance and contrast ratio (A04-A06), CIEDE2000 (Sharma, Wu & Dalal 2005 test pairs), see FC-A.

## 1. The capture manifest (one row per image, kept as text next to the images)
Record missing fields as `missing`; never guess them from the picture (04:§4.4).
| Field | Example |
| --- | --- |
| capture id, file, timestamp | `c04`, `captures/c04.png`, 2026-11-02 14:10 |
| game/build, asset revision | `place v41`, `boss_mesh r3` |
| art-bible revision, anchors in force | `rev 3`, `a02, a05` |
| viewport px, orientation, crop, encoding | `1170x2532 portrait, none, PNG` |
| camera transform, FOV or ortho scale, gameplay distance | `third person, 70°, 14 studs` |
| capture state | normal distance / closest view / smallest presentation; quiet / busiest |
| time of day, lighting style, post stack, quality tier | `noon, Soft, Bloom+CC, quality 3` |
| UI scale, HUD and safe-area state, input mode | `1.0, HUD on, CoreUISafeInsets, touch` |
| player pose, encounter state | `idle`, `slam wind-up` |
| capture device or route | `iPhone 12 (Studio MCP)` / `Blender render` / `ChatGPT image (route, model)` |
| derived files | look-check JSON paths, diagnostic images |
| **UI screens instead of camera fields:** canvas size, export scale, fit factor (UIScale), safe-area mode, Figma file + node id or build path, frame/state id, which screen came before it in the flow | `1920x1080 @1x, f 0.347, CoreUISafeInsets, node 1:3 / state 04-commit, after 03-review` |

Capture rules: keep originals next to derived images; no beauty grade before measuring; before/after pairs share camera, pose and light (a lighting test changes only light, and says so); put an approved anchor in the same scene for style comparisons; three evidence channels stay apart — neutral material render (shape and material), silhouette render (outline, negative space), full game capture (does identity survive light, clutter, UI and effects) (04:CP1-CP4).

## 2. Running the tool and reading the JSON
`python tools/art/look_check.py <check> <image> [options] --out <review folder>/<capture>-<check>.json --out-dir <review folder>/diag`
| Check | Use it for | Read | Never conclude |
| --- | --- | --- | --- |
| `value` | value hierarchy; does the subject separate from its own surround | `subject`, `ring` (p5-p95, mean), `subject_ring_ratio`; the luminance image | a pass for world art without a project tolerance; accessibility; motion readability |
| `contrast --pair FG,BG --rule <r>` | UI text and UI components only | unrounded ratio; pass/fail against the named rule (wcag-text 4.5, wcag-large 3.0, wcag-nontext 3.0, xbox-text 4.5, xbox-large 3.0, xbox-hc 7.0) | anything about world props or enemies; mixing standards (WCAG exempts inactive text, Xbox asks 3:1 for it); the Xbox 36/72/144 px values define "large" text on mobile, they are not a minimum size (FC-A FA08-FA12) |
| `silhouette` | outline identity, size at the camera, change vs an anchor | `bbox_px`, `bbox_frac`, `area_frac`, `components` (sheets: one per view), `iou` with `--compare` and its alignment | appeal; recognition by players; a universal pixel minimum |
| `palette --roles roles.json` | role colors drifting from the bible | clusters (Lab, hex, share); per role `delta_e` to the nearest cluster; the swatch strip | "the right number of colors"; style match from a histogram; where colors sit (look at the patches) |
| `thumb --size WxH` | the real icon slot, thumbnail crop or phone viewport | the small image and sheet; `value` and `silhouette` re-run on it | a universal thumbnail size (use the real slot) |

**Verdicts.** `measured` = numbers only. `pass`/`fail` only when you pass a tolerance (`--rule`, or `--min-ratio` / `--min-iou` / `--max-delta-e` with `--tolerance-source "<D-id or standard>"`). `invalid-mask` = no usable subject mask: fix the mask before reading anything (R-03).

**Masks.** Default `--key auto` keys a flat border color and fills enclosed key-colored areas (so light fur on a light-grey background stays subject). Use `--keep-holes` when an enclosed gap is part of the silhouette (a handle loop), `--mask` for game captures (object-ID or a hand mask from Studio), `--component N` for one view of a sheet. Check the silhouette image before trusting any number; a mask that includes background voids every later statistic (04:CP5). Ground shadows count as subject; mask them out when they matter.

**UI screens.** Auto-key rarely finds a subject on a full screen: mask a control with `--box x0,y0,x1,y1` (add `--box-key` to drop its panel color), keep neighboring controls out of the ring with `--exclude-box`, and keep the ring narrow (a few px) where controls sit close. "Is the primary the brightest control?": `value --compare-subjects` with one named box per control. Text contrast from a rendered screen: `contrast --sample <image> --fg-box ... --bg-box ...` (sampled rendered colors, not guesses). Box coordinates come from the spec, the Figma node or a measured mask — never from eyeballing the image.

**Roles file** (from the bible's color roles): `{"danger": "#e8582a", "reward": "#ffd34d", "interactable": "#4fc3f7"}`. Compare authored swatches with base-color renders and lit captures separately (R-06).

## 3. What the tool cannot do
Motion, timing, sound, device performance, player recognition, appeal. Edge density and color-vision simulation are not built (J009-D5; edge density is unreliable for stylized outlines, 02:M11). Screen share of an effect or panel: mask it (or key it on a capture with the effect isolated) and read `silhouette` `area_frac`; record how the mask was made. For color-blind checks, ask for a simulator capture (e.g. Color Oracle, record the mode) and a non-color channel; for recognition, run an unlabeled identification test and report uncertainty (02:M6, M9).

## 4. Review checklist (15 rows; status: pass / fail / needs-decision / NOT REVIEWED, each with evidence)
| ID | Check | Procedure | Pass when | On fail → ticket to |
| --- | --- | --- | --- | --- |
| K01 | Evidence identity | manifest vs asset revision, bible and anchor ids, file hashes | every input belongs to the candidate | recapture (lead / Studio operator) |
| K02 | Camera comparability | viewport, camera, FOV, pose, exposure match for before/after | identical, or the variation is stated | recapture before judging proportions |
| K03 | Silhouette identity | `silhouette` at the intended footprint; name identity features, facing, nearest confusable asset | identity features survive the required views | modeler (shape); animator (pose) |
| K04 | Value separation | `value` with a subject mask across the required backgrounds | the essential cue meets its project test | owner of the cue's light, material or effect, coordinated |
| K05 | UI text and component contrast | `contrast` with the named rule, lowest-contrast background sample | meets the adopted rule for that role | ui-ux-designer |
| K06 | Color meaning | role labels and swatches vs the bible's color roles | no unapproved role change, no ambiguous essential state | art director resolves the role; specialist implements |
| K07 | Not color alone | original, grayscale, a recorded color-vision simulation; state identification | meaning survives without hue | owner of the cue (add shape, icon, pattern, motion, sound) |
| K08 | Palette drift | `palette --roles` on masked regions + patch review | within the approved tolerance or approved variation | base color (modeler / UI) or light (environment) |
| K09 | Detail competition | layer cut (no UI, no FX, full) + downsample of the busiest capture | the task hierarchy survives | the competing layer's owner |
| K10 | Scale and proportion | known dimensions vs a player reference and the anchor | contract dimensions and identity proportions hold | modeler / environment-designer |
| K11 | Motion and effect overlap | timestamped clip: anticipation, event, recovery; sound on and off | the cue reads in context and on time | animator / vfx-designer / ui-ux-designer |
| K12 | Anchor and lock consistency | each locked attribute vs the anchors, plus the drift check | every lock passes or has an approved exception | the asset's owner; bible fix by the art director |
| K13 | Quality-floor appearance | lowest supported quality / baseline phone capture | silhouette, hierarchy and meaning survive | environment-designer / vfx-designer / engineering |
| K14 | Marketing truthfulness | icon at its small size, thumbnail at its crop, next to in-game captures | same identity; only experiences the game has | marketing |
| K15 | Decision accountability | evidence per row; owner approvals for new directions | no unresolved critical fail, no undocumented override | owner digest |
| K16 | UI flow: tap-through | overlay consecutive screens; a commit target must not sit under the previous screen's tap target | no accidental double-tap commit | ui-ux-designer |
| K17 | UI flow: layout stability | idle vs pressed vs pending boxes for the same control | hit area and position hold (or the spec allows it) | ui-ux-designer |
| K18 | UI states: salience | disabled, locked and placeholder states vs enabled | no disabled or placeholder element out-ranks the live choice | ui-ux-designer |
The UI designer self-reviews against `ui-design/references/review.md` (22 checks); the art director checks hierarchy, style match, color meaning, cohesion and K16-K18 as visual evidence, and routes every fix to the UI designer.

Plus, for places and casts, the first game's repeat offenders: completeness (every face, room and path), ground continuity, furniture scale, facing, character read (R-11, R-12).

Source: paper checklist (04:CK01-CK15, OPINION), procedures not run by the paper; hand-offs become tickets in the kit (lead-notes N8).
