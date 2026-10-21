---
type: job
scope: game
status: draft
updated: 2026-10-21
source: "J009-T09 (lead brief, blind review); content/ui/anime-summon/ (spec.md, refs/, screens/); skills art-direction, art-review, ui-design, ui-style-anime, platform-policy"
supersedes: []
---
> Author: art-director · claude-opus-5-5 · high · 2026-10-21

# Art review: anime summon (banner + reveal), J009-T09

## 1. Verdict
**Grade B+.** A clear, premium, honest summon screen: the two crystal Summon buttons and the featured unit own the frame (measured), tier odds and pity are readable on the phone before any tap; but the commit step is not stable (Confirm sits partly over Summon x1, and the pressed button jumps when it turns into "Summoning..."), the disabled Cancel gets louder than the enabled one, and yellow carries five meanings.

Review verdict: **revise** (AF1, AF2, AF3, AF7) with **needs-decision** items (AF4, AF5, AF6). Nothing here is an approval: the owner judges the look at Gate 3.

## 2. Brief restated
| Field | Value | Source |
| --- | --- | --- |
| Moment | In the lobby, the player wants to summon the featured Mythic (Kaida) or any strong unit with gems, knowing what each summon can give and how likely each result is; full-screen menu. | spec.md §1 |
| Read first (max 2) | 1. the featured unit with its rarity and its own chance; 2. the Summon x1 / x10 actions with their cost. Next: tier chances, pity, ODDS & UNITS; atmosphere: backdrop, rune, header. | my ranking from spec.md §3 |
| Feeling | "A premium summoning altar: sharp violet panels, one glowing crystal action, and the featured unit with its rarity front and centre, every chance printed in plain numbers." (PROPOSAL thesis); style book thesis: "sharp, energetic and premium" | spec.md §5; ui-style-anime §1 |
| Camera / device | 2D UI, landscape phone first; smallest phone 667 x 375 pt, fit f 0.294 (564 x 318 export) | brief; spec.md §9 |
| Art bible, anchors | **None** (game profile empty, no look rows in decisions.md). Style match judged against the target reference images (`refs/raw`, `refs/keyed`) and the style book `ui-style-anime` (itself PROPOSAL). | brief `no_art_bible` |
| Target reference | 4 character images (Kaida, Sora, Yume, Toma) and the VFX library shortlist; **no screen-level target reference image** (AF6). | refs/prompts.md |
| Acceptance used | ui-style-anime §3-§6, §9-§10; ui-design D-02, D-04, D-09, D-10, D-12-D-14; platform-policy §6; WCAG 2.x text 4.5:1 / non-text 3:1 (named per check) | — |

## 3. Evidence
### 3.1 Capture manifest
All captures: route = Figma export of file `Ob2rRbGBRlmP5JmGyVOlUG` (spec.md header), 1920 x 1080 PNG unless stated, no bible revision, no anchors, UI scale 1.0, input n/a, lighting/quality n/a, device = none (Figma, not in-game; spec.md §15). Timestamps = file mtime (2026-10-21).

| id | file | sha256 (12) | mtime | node | state | notes |
| --- | --- | --- | --- | --- | --- | --- |
| a01 | screens/01-main-1920.png | a9883480126e | 00:30:29 | 12:2 | main banner | + grayscale 2e7d2414ce31, phone 564 x 318 3cb0386a6138, phone @2x 30d857127dc9, phone grayscale aba1a1e5aac8 |
| a02 | screens/02-odds-open.png | 3371b840e1f5 | 00:26:20 | 13:130 | odds open | captured **before** the banner contrast fix (spec §6 note); phone + grayscale exist |
| a03 | screens/03-review.png | 2c0c0e762716 | 00:38:42 | 13:372 | Review (x10) | phone + grayscale exist |
| a04 | screens/04-commit.png | badbf7b63256 | 00:38:43 | 13:503 | Confirm pressed | no phone file |
| a05 | screens/05-pending.png | 270f280b6802 | 00:27:05 | 13:641 | pending | captured before the banner fix; phone + grayscale exist |
| a06 | screens/06-reveal-1x.png | e3e230a1fb41 | 00:29:27 | 14:1014 | reveal x1 (Mythic) | phone + grayscale exist |
| a07 | screens/07-reveal-10x-summary.png | 284d4187be1e | 00:29:27 | 14:1097 | x10 summary | phone + grayscale exist |
| a08 | screens/08-failed.png | 186b85f6cf4e | 00:38:43 | 13:789 | failed | phone + grayscale exist |
| a09 | screens/09-not-enough-gems.png | d33ea8742895 | 00:38:44 | 13:924 | not enough gems | phone + grayscale exist |
| a00 | screens/00-components-page.png | e348e4ede59f | 00:29:28 | 6:2 | components board (1665 x 2400) | **stale**: banner card shows "0.5 % per summon" in pink; a01 (1 min later) shows white (AF7) |
| r1-r4 | refs/raw/gen1-4_*.png, refs/keyed/{kaida,sora,yume,toma}.png | — | — | 2:2, 3:2, 4:2-4:5 | target reference images (character art) | |

Missing for a full review: a Review frame for x1, the pity-active (89/90) odds and Review frames, a reveal for a non-Mythic x1, the SKIP control, any in-game capture, motion, sound.

### 3.2 Measurements (JSON under `knowledge/jobs/J009-art-director/art/test-b/json/`, diagnostics `diag/`, masks `masks/`)
| Check | Run on | Result (measured) | JSON |
| --- | --- | --- | --- |
| Control boxes and overlaps | a01, a03, a04, a05, a06, a07 | Summon x1 face [963,883,1397,1037]; Review Confirm [983,780,1377,914]; overlap 12,214 px = **23.1 %** of Confirm (band y 883-914); pressed Confirm (a04) [983,790,1377,924]; pending button (a05) [913,718,1447,852]; reveal Done (a06) over Summon x10: 79.0 % | `json/boxes.json` (script `diag/measure_boxes.py`) |
| value: controls and hero | a01, a03, a05, a06 | subject median / ring median / ratio: Summon x1 0.453 / 0.030 / **6.30**; Summon x10 0.448 / 0.030 / 6.25; hero (a01) 0.277 / 0.109 / 2.06; ODDS & UNITS 0.044 / 0.004 / 1.73; "+" 0.043 / 0.035 / 1.09; hero (a06) 0.276 / 0.082 / 2.46; Cancel enabled (a03) 0.044 / 0.009 / 1.57; **Cancel disabled (a05) 0.183 / 0.014 / 3.65** | `json/ani01-*-value.json`, `json/ani03-cancel-value.json`, `json/ani05-cancel_disabled-value.json`, `json/ani06-hero-value.json` |
| contrast (WCAG text 4.5, non-text 3.0) | sampled pairs a01-a07 | all pass: muted #C9C3F5 on panel top #40319A **5.94**, on sampled backgrounds 6.59-11.10; rarity words 6.76-11.43 (EPIC on panel top 4.68, the lowest); pity/yellow 8.35-10.22; ink on crystal 5.87 (darkest face) to 12.41; white on banner 12.39; focus ring 12.48 (non-text); disabled CANCEL: fill vs grey alone 2.76 / 1.93 (fail alone), outline #140F3A vs grey 6.45 (pass, outline method) | `json/contrast/A*.json`; samples `json/colour-samples.json` |
| silhouette: hero vs reference | refs/raw/gen1 vs refs/keyed/kaida | IoU 0.938; the screen hero is the keyed reference (template match RMSE 5.94 at 478 x 700 on a01, 9.81 at 640 x 937 on a06) | `json/sil-kaida-raw-vs-keyed.json`, `json/boxes.json` hero_template_match |
| thumb: phone | a01 at 564 x 318 (hero mask, Summon mask); keyed hero at 140 x 206 | hero box 140 x 204 px in the phone frame, median 0.269 vs ring 0.148 (1.61); Summon face 127 x 45 px | `json/thumb-ani01-564x318-*.json`, `json/thumb-kaida-hero-phone.json`, `diag/01-main-1920.thumb564x318.png` |
| palette vs spec role swatches | a01, k 12 | Legendary #FFE58A and pity yellow #FFD34D both nearest to cluster #FDD660 (dE00 5.59 and 1.99); diagnostic | `json/ani01-palette.json`, `diag/01-main-1920.palette.png` |

Masks: colour predicate + connected component (crystal faces, glass strokes) or template match of the keyed reference (hero); overlay `diag/overlay-ani01.png`, `diag/overlay-ani06.png`. Value, silhouette and palette numbers are **diagnostics** (no approved tolerance); only the WCAG rows carry pass/fail.

## 4. Checklist (art-review look-check §4)
| ID | Check | Status | Evidence |
| --- | --- | --- | --- |
| K01 | Evidence identity | **fail** (minor) | a00 board older than a01 and shows the pre-fix pink banner line; a02/a05 captured before the banner fix (spec §6 says so) (AF7) |
| K02 | Camera comparability | pass | one canvas; popups over the same dimmed a01 |
| K03 | Silhouette identity | pass (diagnostic) | hero = keyed reference (IoU 0.938, RMSE 5.94); the hero breaks out above the banner card (a01) as the style book asks; at phone the hero is 140 x 204 px |
| K04 | Value separation | pass (diagnostic) with one fail | Summon x1/x10 ratio 6.3 vs hero 2.06 vs ODDS & UNITS 1.73 vs "+" 1.09: the order matches the read-first ranking; **disabled Cancel 3.65 > enabled Cancel 1.57** (AF3) |
| K05 | UI text contrast | pass | every sampled pair >= 4.68:1; outlined disabled label passes by the outline method |
| K06 | Color meaning | needs-decision | yellow = Legendary, RATE-UP, NEW, pity/rules, gem debit (AF4) |
| K07 | Not color alone | pass | rarity = colour + word + pip count (a01, a02, a06, a07); NEW is a word badge; no CVD simulation capture: CVD part NOT REVIEWED |
| K08 | Palette drift | NOT REVIEWED (no bible roles) | spec swatches vs render diagnostic (`ani01-palette.json`) |
| K09 | Detail competition | pass | rune, sparkles and stripes stay behind text (a01, a06); nothing animated behind text by spec |
| K10 | Scale and proportion | pass | at f 0.294: Summon 50 pt high, action buttons 44.1 pt, close 44.1 pt, "+" 35.3 pt (minor) (spec §9 arithmetic; not re-measured on device) |
| K11 | Motion and effect overlap | NOT REVIEWED | no clip; R1-R10 are PROPOSAL values (spec §13); the commit jump (AF2) is measured from end frames only |
| K12 | Anchor and lock consistency | partial | hero = reference; style-book signature kept in chamfers, crystal primary, header overlapping popups, oversized art breaking cards; header on a01 is a plain slanted slab (AF6) |
| K13 | Quality floor | NOT REVIEWED | no device capture |
| K14 | Marketing truthfulness | n/a | — |
| K15 | Decision accountability | needs-decision | AF4, AF5, AF6 |
| R-11 | Completeness | partial | 13 of 17 units have no art (a07 repeats Toma Shield 6 times) (AF5) |

## 5. Ranked findings
| Rank | Finding | Observation (measured / seen) | Consequence (interpretation) | Verdict (rule) | Owner role | Acceptance evidence |
| --- | --- | --- | --- | --- | --- | --- |
| AF1 | The Review Confirm sits partly over Summon x1 | Confirm [983,780,1377,914] overlaps Summon x1 [963,883,1397,1037] by 12,214 px = 23.1 % of Confirm; the pressed Confirm (a04) moves 10 px further down into that band. Only the x10 Review is drawn; if the x1 Review uses the same layout, a double tap on Summon x1 can land on Confirm. Done on the reveal (a06) covers 79 % of Summon x10 (a second tap opens Review x10, no spend). | A fast double tap can turn "open Review" into "spend 50 gems" without reading the Review; gems are Robux-bought (spec §1). | **revise**: ui-design D-12 "preview != commit"; shops §2 (review is its own state); x1 Review frame NOT REVIEWED | ui-ux-designer | A drawn x1 Review; with the same box method, its Confirm overlaps no tap target of a01 (0 px), or the spec states an input rule that makes the second tap unable to confirm, with a test |
| AF2 | The pressed button jumps at the moment of spending | Confirm pressed (a04) [983,790,1377,924] -> "SUMMONING..." (a05) [913,718,1447,852]: 72 px up, 140 px wider; the popup bottom moves up ~63 px and Cancel changes from dark glass to light grey | The player's finger is on a button that moves and changes size exactly when gems are committed; it reads as a different screen, not as "your press was received". Spec §13 R1 says "hit area never moves". | **revise**: spec §13 R1 (own rule); ui-design D-14 (input acknowledgement and confirmed result are separate beats). Motion itself NOT REVIEWED | ui-ux-designer | a04 and a05 recaptured: the pressed button keeps its box (same box method, difference 0 px except the press offset), the popup keeps its frame; the pending label fits |
| AF3 | Disabled Cancel is louder than enabled Cancel | Median luminance Cancel enabled (a03) 0.044, ratio 1.57; Cancel disabled (a05) 0.183, ratio 3.65 (4.2x lighter); the disabled face is a light metallic grey with shine bars | During pending the dead control becomes the second brightest thing in the popup and competes with "Waiting for the server..." (the line the player must read). | **revise**: ui-design D-02 (priority = salience); ui-style-anime §6 Disabled "glow off, desaturate" | ui-ux-designer | `look_check value` with `masks/ani05-cancel_disabled.png` on the new a05: disabled Cancel median <= enabled Cancel median in a03 (same mask method), label still passes the outlined-text method |
| AF4 | Yellow carries five meanings | Legendary word #FFE58A; RATE-UP chip; NEW badge (#FFE680 -> #E89A00, spec §10); pity/rule text #FFD34D (a02, a03, a06, a07); gem debit "-50"/"-500" #FFD34D (a06, a07). Palette: Legendary and pity yellow fall in one cluster (#FDD660, dE00 5.59 / 1.99) | In the x10 summary a NEW badge sits on a Legendary card in nearly the same hue; the debit reads like a reward. Words carry every meaning, so this is not a colour-only failure, but colour stops helping. | **needs-decision**: art-direction C-10 "one meaning per treatment"; no bible exists to set roles | owner (role table), then ui-ux-designer | A role table in the spec with one meaning per hue for this screen set; palette check shows the tier hue and the rule/debit hue in different clusters |
| AF5 | The reveal repeats the banner and most units have no art | The x1 reveal hero is the same keyed image as the banner hero (template match on a01 and a06); a07 shows Toma Shield 6 times because only 4 portraits exist (refs/prompts.md: 4 of 5 images used); by look, the Mythic card's portrait is the only one whose head stays inside the card, while Legendary, Epic and Rare heads break out of the top | The Mythic result, the screen's top payoff, shows nothing the player did not see before the summon, and in the x10 grid it is the least "breaking out" card. The x10 summary cannot be judged for variety. | **needs-decision** (image budget) + low revise for the Mythic crop | owner (budget), ui-ux-designer (crop) | Reveal shows a pose or framing different from the banner; Mythic card art breaks out like the others (look, owner); a07 recaptured with distinct units when art exists |
| AF6 | Style match is partial: tidy, not "sharp and energetic" | Seen: the a01 header is a slanted slab with a small accent, no points or notch, and does not overlap a panel (spec §14 says so); crystal facets and shine are faint at phone size (a01 phone); there is no screen-level target reference image to compare composition with | The screen reads as clean premium esports more than the warped, energetic anime signature of the style book; the hierarchy is right, the energy is low. This is taste, not a broken rule. | **needs-decision** (owner taste); ui-style-anime §3 Signature | owner, then ui-ux-designer | Owner says which of "calm premium" or "sharp, energetic" this game wants; if the latter, a01 header and crystal buttons reviewed again at phone size |
| AF7 | Evidence lags the latest fix | a00 board (00:29:28) shows the banner "0.5 % per summon" in pink, a01 (00:30:29) in white; a02 and a05 were captured before the banner fix | A builder copying the component board ships the failing pink line (2.78:1 per spec §10). | **revise** (low): art-review K01 | ui-ux-designer | a00, a02, a05 re-exported from the current Figma; the banner line on a00 matches a01 |

## 6. Cohesion table
| Channel | Consistent? | Evidence |
| --- | --- | --- |
| Color meaning | partly | cyan crystal = the action that moves forward (Summon, Confirm, Done, OK, Try again) on every screen; dark glass = secondary; rarity hues fixed across a01/a02/a06/a07; yellow overloaded (AF4) |
| Shape meaning | yes | chamfered panels, cards and buttons everywhere; angular header overlapping every popup (a03, a08, a09) |
| Motion personality | NOT REVIEWED | no clip; spec §13 sets "same anticipation for every rarity, no fake-out" (good intent, unverified) |
| Sound personality | NOT REVIEWED | sound markers only (spec §13) |
| Material and age language | yes | crystal + dark glass + rune library textures read as one premium fantasy set; character art (cel shaded, rim lit) matches the UI's cool palette |

## 7. What works (keep it)
- **Hierarchy matches the moment (measured):** Summon buttons ratio 6.3, hero 2.06, ODDS & UNITS 1.73, "+" 1.09; the gem shop entry is deliberately calm, so the screen does not push buying more gems.
- **Odds honesty on the main screen:** tier chances, the featured unit's own 0.5 %, pity "37 / 90" and "Sure Mythic in 53 summons" are on a01 before any tap; full list with "TOTAL 100 % (1 + 4 + 20 + 75)" one labelled tap away (a02); Review repeats chances, pity effect, cost and balance after, and "cannot be undone" (a03). Matches platform-policy §6 and ui-design D-13.
- **Readable on the phone:** every sampled text pair passes WCAG 4.5:1 (lowest EPIC on panel top 4.68); a01 phone export shows chances, pity and costs legible at 564 x 318.
- **Safe defaults:** Done is primary after a reveal, OK is primary on "not enough gems" (a09); x1 and x10 have equal weight; Again goes through Review (spec §3).
- **Reference fidelity and originality:** the hero is the target reference image itself (IoU 0.938, RMSE 5.94); all characters are invented originals; library textures, no copied art.
- **x10 summary structure:** sorted top rarity first, count line, NEW only on first copies (a07).

## 8. Could not check
| Item | Artifact needed | Who can provide it |
| --- | --- | --- |
| x1 Review layout (AF1) | frame 03 for x1 | ui-ux-designer |
| Pity-active state (count 89, "Summon n of 10 is a sure Kaida") | frames for a02 and a03 at 89/90 | ui-ux-designer |
| Reveal motion, equal anticipation per rarity, no fake-out, flash rate, SKIP | phone recording at 60 fps (spec §13 tuning test) | builder / studio-operator |
| Sound | cue cards or clips | sound-designer |
| Device: safe area, top bar, touch controls hidden over Summon x10 (spec Q3) | Device Simulator capture on the smallest phone | studio-operator |
| Colour-vision simulation of rarity tiers | simulator capture of a02 and a07 | ui-ux-designer |
| Restricted-player path | spec only (§7.5), no frame by design | — |
| Player comprehension of pity and "rate-up" | unlabelled player test | owner / playtest |

## 9. Tickets proposed and owner decisions
Tickets (briefs in `briefs-ui.md`, not sent): **J009-T09-B2** anime summon fixes (AF1, AF2, AF3, AF7 + AF5 crop) to ui-ux-designer, `inside: yes` only if the lead opens a J002 revision; otherwise `needs-decision`.

| Owner decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- |
| D-d Colour roles for yellow (AF4) | (1) yellow = Legendary only; rules, NEW and debit get other treatments; (2) keep as is | (1): the tier colour is the one players learn | as is |
| D-e Unit art budget (AF5) | (1) budget a reveal pose for the featured unit and portraits for the other units; (2) keep placeholders for the test | (1) for the featured unit's reveal at least | placeholders |
| D-f Anime energy level (AF6) | (1) calm premium (as built); (2) sharper, more energetic header and buttons per the style book | owner taste; the art director has no anchor to decide it | as built |
