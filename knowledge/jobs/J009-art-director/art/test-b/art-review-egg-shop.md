---
type: job
scope: game
status: draft
updated: 2026-10-21
source: "J009-T09 (lead brief, blind review); content/ui/egg-shop/ (spec.md, refs/, screens/, export/); skills art-direction, art-review, ui-design, ui-style-cartoon, platform-policy"
supersedes: []
---
> Author: art-director · claude-opus-5-5 · high · 2026-10-21

# Art review: egg shop (cartoon), J009-T09

## 1. Verdict
**Grade B-.** The main shop screen is a convincing, on-style cartoon shop that reads on the smallest phone, and the purchase flow is honest; but the reward moment shows no pet, the Review "Buy" sits under the Chances-popup "Buy" (one double tap can spend coins), and "Buy" is not the brightest control in grayscale.

Review verdict: **revise** (findings EF1, EF3, EF5, EF6) with **needs-decision** items (EF2, EF4, EF7). Nothing here is an approval: the owner judges the look at Gate 3.

## 2. Brief restated
| Field | Value | Source |
| --- | --- | --- |
| Moment | A child at the egg stand picks one egg, checks which pets can hatch and how likely each is, and buys it if they can afford it. Shop is a modal over the world. | spec.md §1 |
| Read first (max 2) | 1. the four eggs as the choice, each with its price; 2. the Buy action on the chosen egg. Next: the labelled Chances control; atmosphere: header, panel, backdrop. | my ranking from spec.md §3 decision record |
| Feeling | "Bubbly pet-sim shop where each egg is a glossy treasure, the green Buy is the chunkiest thing on each card, and every chance is printed in plain numbers." (PROPOSAL thesis) | spec.md §5 |
| Camera / device | 2D UI, landscape phone first; smallest supported phone 667 x 375 pt (brief `phone`) | brief; spec.md §1 |
| Art bible, anchors | **None.** `knowledge/design/game-profile.md` is empty; `knowledge/design/decisions.md` has no look rows. Per the brief, style match is judged against the screen's own target reference images (`refs/`) and the style book `ui-style-cartoon`. Both are PROPOSAL, not owner locks. | brief `no_art_bible` |
| Target reference | `refs/raw/egg_*_raw.png` (4 egg icons) and `refs/raw/backdrop_island_raw.png` (context backdrop). **No screen-level target reference image exists** (see EF7). | refs/prompts.md |
| Acceptance used | style book `ui-style-cartoon` §3-§6, §10; `ui-design` D-02, D-06, D-09, D-10, D-12, D-13; platform-policy §6; WCAG 2.x text 4.5:1 / non-text 3:1 (named per check) | — |

## 3. Evidence
### 3.1 Capture manifest (one row per image; fields not in the files are `missing`)
All captures: route = Figma export of file `gVgO2Ql80LUerCpQe02CtD` (spec.md header), canvas 1920 x 1080 PNG unless stated, no bible revision, no anchors, UI scale 1.0, input mode n/a (static frame), lighting/quality n/a (2D), device = none (Figma, not in-game; spec.md §14 says the same). Timestamps = file mtime.

| id | file | sha256 (12) | mtime | node | state | derived / notes |
| --- | --- | --- | --- | --- | --- | --- |
| e01 | screens/01-inspect-main-1920.png | d71998153972 | 2026-10-20 23:37:06 | 16:2 | inspect (normal), Lava card = not enough coins | the spec's candidate; grayscale and both phone files derive from it (mean abs diff 0.0 / 0.19, measured) |
| e01v2 | screens/01-inspect-main-1920-v2.png | d28020b0c0d0 | 23:56:50 | missing | same state, newer card faces | **not in spec.md**; no grayscale or phone file; 232,382 px differ from e01 (box 214-1749 x 380-1019) |
| e01g | screens/01-inspect-main-grayscale.png | 3adaa396932a | 23:37:12 | — | grayscale of e01 | |
| e01p | screens/01-inspect-main-phone-0.347x-667x375.png | e6e217969e24 | 23:37:12 | — | phone at f 0.347 (full-height fit) | |
| e01pg | screens/01-inspect-main-phone-grayscale.png | cd50139a5c0a | 23:37:12 | — | phone grayscale | |
| e02 | screens/02-odds-open.png | c893ab5871d9 | 23:37:07 | 17:4537 | Chances popup (Meadow) | |
| e03 | screens/03-review.png | b1d5b6b9ee7c | 23:37:08 | 17:5641 | Review | |
| e03p | screens/03-review-phone-0.347x.png | b4885d3a18c4 | 23:37:12 | — | Review at f 0.347 | |
| e04 | screens/04-commit.png | 540477e75d5f | 23:37:08 | 17:14121 | Buy pressed | |
| e05 | screens/05-pending.png | 3e18080c227a | 23:38:10 | 17:17080 | pending | |
| e06 | screens/06-confirmed.png | 9e281c6cafc0 | 23:37:10 | 18:16960 | confirmed (reward) | |
| e07 | screens/07-failed.png | bfed2c4dbc25 | 23:37:11 | 18:18747 | failed | |
| e08 | screens/08-not-enough-coins.png | b176704539ab | 23:37:11 | 18:19352 | not enough coins | |
| e00 | screens/00-components-page.png | 0cdf6bd07f09 | 23:38:10 | 1:2 | component states board (2400 x 1839) | |
| r1-r5 | refs/raw/egg_{meadow,ocean,lava,galaxy}_raw.png, backdrop_island_raw.png | — | — | 2:2-6:2 | target reference images | export/egg_*.png are the keyed builds |

Missing for a full review (section 8): phone and grayscale exports of e02-e08, any in-game capture, any motion clip, any sound.

### 3.2 Measurements (all JSON under `knowledge/jobs/J009-art-director/art/test-b/json/`, diagnostics under `diag/`, masks under `masks/`)
| Check | Run on | Result (measured) | JSON |
| --- | --- | --- | --- |
| Control boxes and overlaps | e01, e01v2, e02, e03, e06 | colour-predicate boxes; overlap e02 Buy -> e03 Buy = 31,360 px = **81.7 %** of the Review Buy face | `json/boxes.json` (script `diag/measure_boxes.py`) |
| value: Buy, Chances, +, Close, card faces | e01, e01v2 | subject median luminance: Buy 0.525, Chances 0.743 (Meadow) / 0.772 (Galaxy), + 0.599, Close 0.296; card face median Meadow 0.691 (e01) / 0.506 (e01v2), Galaxy 0.296 | `json/egg01-*-value.json`, `json/egg01v2-*-value.json` |
| contrast (WCAG text 4.5, non-text 3.0) | sampled pairs e01-e08 | muted ink #5A6280 on #F2F5F9 **5.50 pass**, on #FFFFFF **6.01 pass**; outline #010202 vs card #C3ECFF **16.58 pass**; outline vs green #B8FF8F **17.63 pass**; outline vs disabled #CCD2DA **13.72 pass**; focus ring #1A2457 vs #F6F6F7 **13.56 pass (non-text)**; diagnostics without rule: white fill vs card alone 1.23, white fill vs green 1.74, sunburst #FFEC8D vs panel #FFFFFE **1.19** | `json/contrast/E*.json`; samples `json/colour-samples.json` (script `diag/sample_colours.py`) |
| silhouette: build vs reference | export vs refs/raw, 4 eggs | IoU 0.995 / 0.997 / 0.996 / 0.998 (meadow / ocean / lava / galaxy) | `json/sil-egg_*-raw-vs-export.json` |
| silhouette: eggs vs each other | export/egg_meadow vs others | IoU 0.969 ocean, 0.943 lava, 0.967 galaxy | `json/sil-egg_meadow-vs-*.json` |
| thumb: eggs at phone slot | export/egg_*_256 at 75 x 75 (256 px x 0.294) | egg median luminance: meadow 0.501, ocean 0.386, lava 0.080, galaxy 0.035 | `json/thumb-egg_*-75.json` |
| thumb: whole screen | e01 at 667 x 375 and 564 x 318 (kit fit 0.294 stress test), Buy mask | Buy face box in the thumb 84 x 42 px at 564 x 318 (mask incl. outline, halo, lip) | `json/thumb-egg01-*.json`, `diag/01-inspect-main-1920.thumb564x318.png` |
| palette vs spec role swatches | e01, k 12 | diagnostic only (no tolerance): green top dE00 4.5, gold bottom 15.1 | `json/egg01-palette.json` |
| card gradient, focus ring, stitch | e01, e01v2, e03, e06-e08 | visible card-face span y400-740 dL* 15.6 (e01) / 26.9 (e01v2); focus ring outer edge x 965 = neighbour outline start x 965; panel stitch rows y 976-979 run under Cancel (face to y 982) | `json/egg01-card-gradient-Lstar.txt`, `json/egg-focus-ring-and-stitch.txt` |
| v1 / v2 / gray crop | e01, e01v2, e01g | side by side Meadow card | `diag/egg01-meadow-card-v1-v2-gray.png` |

Masks were made by colour predicate + connected component inside a search window (not by eye); overlays to check them: `diag/overlay-egg01.png`. No tolerance is approved for value, silhouette or palette, so those numbers are **diagnostics**; only the WCAG contrast rows carry pass/fail.

## 4. Checklist (art-review look-check §4)
| ID | Check | Status | Evidence |
| --- | --- | --- | --- |
| K01 | Evidence identity | **fail** | two candidates for state 01 (e01 in spec, e01v2 newer and unlisted); derived phone/grayscale files belong to e01 only (EF5) |
| K02 | Camera comparability | pass | all states are the same 1920 x 1080 canvas and backdrop; e01/e01v2 same frame |
| K03 | Silhouette identity | pass (diagnostic) | built eggs = their references, IoU >= 0.995; eggs share one outline (IoU 0.94-0.97), so identity is carried by surface pattern and colour, which still differ in grayscale (e01pg) |
| K04 | Value separation | **fail** (style book rule) | Buy face median 0.525 < Chances 0.743 in both versions; e01v2 Buy vs card face 0.525 vs 0.506 (EF3) |
| K05 | UI text contrast | pass | every sampled text pair passes WCAG 4.5:1 (5.50-17.63); outlined white text passes by the outline method (screen-contract §5) |
| K06 | Color meaning | needs-decision | green = primary action (spec §5) but the "+ coins" (Robux coin shop) button uses the same green (EF3) |
| K07 | Not color alone | pass | rarity = colour + word + 1-5 stars (e02); disabled = grey + "Need more" (e01); no colour-vision simulation capture: CVD part NOT REVIEWED |
| K08 | Palette drift | NOT REVIEWED (no bible roles) | spec swatches vs render diagnostic only (`egg01-palette.json`) |
| K09 | Detail competition | pass with note | on e01 nothing competes with the eggs; e06 celebration nearly vanishes (EF2) |
| K10 | Scale and proportion | pass | egg art 220-280 px, Buy 128 px high; at f 0.347 frequent controls 44.4 pt; at f 0.294 they fail (EF4) |
| K11 | Motion and effect overlap | NOT REVIEWED | no clip; motion exists only as PROPOSAL values (spec §12) |
| K12 | Anchor and lock consistency | partial | assets match refs (IoU >= 0.995); style-book signature mostly kept; e01 card highlight bars stop mid-face (book §4 Highlights) (EF5); no screen target ref (EF7) |
| K13 | Quality floor | NOT REVIEWED | no in-game or device capture |
| K14 | Marketing truthfulness | n/a | no marketing art in scope |
| K15 | Decision accountability | needs-decision | open: fit rule (EF4), pet art budget (EF2), screen target ref (EF7) |
| R-11 | Completeness | **fail** | reward and odds show a paw placeholder for every pet (EF2) |

## 5. Ranked findings
Order: purchase safety and the fantasy first, then hierarchy, then evidence and polish.

| Rank | Finding | Observation (measured / seen) | Consequence (interpretation) | Verdict (rule) | Owner role | Acceptance evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EF1 | The Review commit button sits under the Chances-popup Buy | e02 Buy face [230,690,550,810], e03 Buy face [230,712,550,832]: overlap 31,360 px = 81.7 % of the Review Buy (`boxes.json` overlaps) | A quick double tap on "Buy" in the Chances popup can open Review and commit at once, so the Review step that shows cost and balance can be skipped. Coins are Robux-buyable (spec §1), the audience is children. | **revise**: ui-design D-12 "preview != commit", shops §2 state machine (review is its own state) | ui-ux-designer | Same box method on the new e02/e03: the Review commit target overlaps no tap target of the screen before it (0 px), **or** the spec states an input rule that makes a second tap on the same spot unable to commit, with a test the builder can run |
| EF2 | The reward has no pet, and the celebration disappears | e06: the pet is a white paw in a blue circle; sunburst #FFEC8D vs panel #FFFFFE = 1.19:1 (`contrast/E8`); e02/e03 list every pet with the same paw icon in a rarity circle | The payoff of a pet-sim (seeing the pet you got, and seeing what you could get) is the weakest picture in the flow; the most emotional screen is a large, mostly empty white panel. The odds list tells names and rarity but cannot make a child want the Golden Deer. | **needs-decision**: pet art needs images beyond the J002 budget of 5 (refs/prompts.md "Used: 5 of 5"); completeness R-11 fails until it exists | owner (budget), then ui-ux-designer | e06 shows the actual pet art at the hero position with rarity word + stars; the celebration graphic separates from the panel (value ring on the reward group, `look_check value`, reported); e02 rows show each pet's picture at phone size (thumb at 564 x 318 or 667 x 375) |
| EF3 | Buy is not the brightest control in grayscale; "+ coins" shares the primary colour | Medians: Buy 0.525, Chances 0.743 (Meadow) and 0.772 (Galaxy) in e01 and e01v2; e01v2 Buy 0.525 vs Meadow card face 0.506 (contrast ratio 1.03); "+" 0.599, same green as Buy | In colour the green Buy reads as primary (I see it in e01); with hue removed (e01g, low saturation, some colour-vision deficiencies, sunlight) the white Chances is the loudest control on every card, and in e01v2 Buy almost merges with the card. The Robux coin-shop "+" is the same role colour as the buy action and lighter than it. Spec §14 self-review says "PASS"; the numbers do not support it. | **revise**: ui-style-cartoon §5.3 "Make it the brightest object in the panel", §10 "Primary action brightest in grayscale"; ui-design D-02 | ui-ux-designer (art director owns the role table: K06) | `look_check value` with the same masks (`masks/egg01-*`): Buy face median higher than Chances, "+" and Close on the shipped candidate, and Buy vs its card face ratio reported higher than e01v2's 1.03; "+" in a non-primary role colour or an owner exception |
| EF4 | At the kit's default phone fit, controls and small text fall under the declared rubric | Spec uses f 0.347 (full-height fit, spec §9, Q2 open). Kit default fit (ui-design screen-contract §5) gives f 0.294: Buy 128 px -> 37.6 pt (< 44 frequent); coin-card Chances 88 px -> 25.9 pt (< 28 minor); rarity tag 32 px -> 9.4 pt and small text 30 px -> 8.8 pt (< 11 essential); 3 px text outline -> 0.88 pt (outlined-text method asks >= 2 device px). Arithmetic from spec §9 sizes; thumb at 564 x 318 still looks legible (`diag/01-inspect-main-1920.thumb564x318.png`) | If the builder fits into the CoreUISafeInsets area (the kit's recommendation), the shop ships under its own touch and text rubric on the smallest phone. | **needs-decision** (spec Q2; screen-contract §5 allows another fit if the spec says so, which it does) | owner, then ui-ux-designer | Owner picks the fit rule; the spec's size table is redone at that f and every frequent control >= 44 pt, minor >= 28 pt, essential text >= 11 pt |
| EF5 | Two candidates for the main screen; the documented one breaks the highlight rule | e01 (spec) vs e01v2 (19 min newer, unlisted, no derived files); in e01 the card highlight bars stop in the middle of the face (`diag/egg01-meadow-card-v1-v2-gray.png`), in e01v2 they cross edge to edge; e01v2 card face is darker (visible span dL* 26.9 vs 15.6) | Reviewers and builders cannot tell which picture is the candidate; the one with the derived phone and grayscale files has bars that break the style book; the newer one fixes the bars but weakens Buy (EF3). | **revise**: art-review K01 evidence identity; ui-style-cartoon §4 Highlights "crossing the whole face edge to edge" | ui-ux-designer | One candidate named in spec.md §6 with its node; its grayscale and phone exports regenerated from it (mean abs diff 0 to the 1920 file after resize, as measured here) |
| EF6 | Popup polish: buttons on the panel border, focus ring touching its neighbour, a stray "-250" | Panel stitch rows y 976-979 run under the bottom buttons (Cancel face to y 982) in e02/e03/e05; the same in e06-e08; focus ring outer edge x 965 = neighbour outline x 965 (0 px gap) in e06/e07/e08; e06 shows a cut "250" above the panel at top-left (spec §14 calls it harmless) | Buttons look pushed into the frame instead of sitting in it; the focus ring reads as touching both buttons; the half-hidden number reads as a rendering bug at the happiest moment. | **revise** (low): ui-style-cartoon §4 Spacing "panel margin >= 30" (PROPOSAL token) | ui-ux-designer | e02-e08 recaptured: bottom buttons (incl. lip and outline) clear the stitch; >= 1 visible px between a focus ring and the next control; no partial numbers outside the popup |
| EF7 | No screen-level target reference image | refs/ holds 4 egg icons and a backdrop only; the style book says to make the screen's target reference image and build to it (citing owner J002-D12, which is not in `knowledge/design/decisions.md`; J002 folder is out of bounds for this blind test) | Composition and mood cannot be checked against an agreed picture, only against the style book; whether the popups are "bubbly" enough is a taste call nobody has anchored. | **needs-decision** (process) | owner / lead | Either a target screen image for 01 and 06 exists in refs/ with its prompt, or the owner says the style book alone is the target for test screens |

## 6. Cohesion table
| Channel | Consistent? | Evidence |
| --- | --- | --- |
| Color meaning | mostly | green = primary (Buy, Done, OK, Try again), white = secondary, red = close, gold = currency, navy = focus (spec §5, e01-e08); exception: "+ coins" green (EF3) |
| Shape meaning | yes | rounded depth blocks with black outline + white halo on every control, one radius ladder (e00, e01); eggs share one outline by design |
| Motion personality | NOT REVIEWED | no clip; spec §12 values are PROPOSAL |
| Sound personality | NOT REVIEWED | no audio or cue cards in scope |
| Material and age language | partly | main screen: glossy cartoon (gloss bars, half-tone, lips) matches the eggs' glossy cel shading (refs); popups switch to flat white sheets with dark ink body text (e02, e06-e08), a calmer, older "form" look |

## 7. What works (keep it)
- **Main screen read (e01):** four eggs, four prices, one action per card; in grayscale the eggs still differ by pattern (e01pg). The Galaxy card is visibly special (larger card, purple, FEATURED ribbon) without hiding the coin eggs.
- **Built eggs are the reference eggs:** IoU 0.995-0.998 between each raw reference and its export; no franchise content (refs/prompts.md).
- **Cartoon signature held:** black outline + white halo on every control, depth lips, header tab overlapping the panel, Fredoka text with outline, close button top-right overlapping the corner (style book §3, §5).
- **Honest shop contract:** labelled "Chances" (not a bare i), every pet with a real % and a computed Total 100 % (e02); Review repeats cost, balance now and after (e03); pending says nothing is spent yet (e05); failure says nothing changed (e07); not-enough keeps OK as primary and "Get coins" secondary (e08). This matches platform-policy §6 and ui-design D-12/D-13.
- **Text contrast:** every sampled pair passes WCAG 4.5:1 (5.50-17.63); rarity is never colour alone.
- **Disabled state with a reason:** "Need more" keeps the price visible on the Lava card.

## 8. Could not check
| Item | Artifact needed | Who can provide it |
| --- | --- | --- |
| Motion (press, popup in/out, pending spinner, reward pop, balance count) | phone recording at 60 fps of 01->03->05->06 (spec §12 tuning test) | builder / studio-operator after the Roblox build |
| Sound | cue list or clips | sound-designer (not in this job) |
| Device: real phone size, safe area, top bar, touch controls hidden | Device Simulator or phone capture on the smallest supported phone | studio-operator |
| Phone and grayscale of e02-e08 | exports at the chosen fit | ui-ux-designer |
| Colour-vision simulation | simulator capture (e.g. deuteranopia) of e01 and e02 | ui-ux-designer |
| Restricted-player path, loading and error states of the odds panel in context | frames (only the component board e00 shows them) | ui-ux-designer |
| Whether "Buy again" (e06) opens Review | spec line | ui-ux-designer |
| Player comprehension of "Chances" and of the reward | unlabelled player test | owner / playtest |

## 9. Tickets proposed and owner decisions
Tickets (briefs in `briefs-ui.md`, not sent): **J009-T09-B1** egg shop fixes (EF1, EF3, EF5, EF6 + questions) to ui-ux-designer, `inside: yes` only if the lead opens a J002 revision; otherwise `needs-decision`.

| Owner decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- |
| D-a Pet art for the reward and odds list (EF2) | (1) budget new pet images; (2) keep the paw placeholder for the test | (1), at least the 5 Meadow pets, because the reward is the core of the fantasy | the placeholder stays and EF2 stays open |
| D-b Phone fit rule (EF4, spec Q2) | (1) kit default f 0.294 (inset-fitted); (2) full-height f 0.347 with the top 167 px non-interactive | the owner's choice; the art director needs only one rule for all screens | spec default (2) stays and the risk stays written |
| D-c Screen target reference (EF7) | (1) one target image per key screen; (2) style book is enough for test screens | (1) for 01 and 06 when the game is real | (2) |
