---
type: spec
scope: game
status: proposed
updated: 2026-10-21
source: "J002-T09 brief (lead); skills ui-design, ui-figma, ui-style-anime, ui-basics, platform-policy, reference-images; Figma file Ob2rRbGBRlmP5JmGyVOlUG; VFX library catalog"
supersedes: []
---
> Author: ui-ux-designer · claude-opus-5-5 · high · 2026-10-21

# Anime summon (banner + reveal): screen spec

Figma: https://www.figma.com/design/Ob2rRbGBRlmP5JmGyVOlUG (pages `Refs` 0:1, `Components` 1:2, `Summon` 1:3). Node ledger: `figma-ids.json`. Screens: `screens/`. Image log: `refs/prompts.md` (keying script `refs/key.py`). Library textures: `library-picks.md`. Book problems: `skill-gaps.md`.
Number tags: **[S]** style-book token (`ui-style-anime` §4, itself PROPOSAL) · **[V]** verified rule with source · **[A]** arithmetic from a [V] rule · **[P]** PROPOSAL (owner has not confirmed) · **[U]** unspecified.

## 1. Player moment
| Field | Value |
| --- | --- |
| Goal (one sentence) | The player wants to summon the featured unit (Kaida) or any strong unit with gems, knowing exactly what each summon can give and how likely each result is. |
| Already knows | Gems come from play and from the gem shop (Robux); summons give random units (genre norm, assumption). |
| Game state | In the lobby, not in a match; the summon screen is a full-screen menu. |
| Input | Touch first (Roblox DAU 2025 mobile 83 % [V] D-05); mouse and gamepad also complete every task. |
| Locale | English copy; boxes leave room (§12). |
| Cost of failure | High: gems can be bought with Robux, so every summon spends real money indirectly, and a summon cannot be undone. |
| Accessibility | Rarity never by colour alone; reduced motion keeps every meaning; text ≥ 11 pt on the smallest phone. |

Assumptions (game profile is empty): gems are bought with Robux (brief), so every summon is a paid random item. Smallest phone: 667 × 375 pt landscape; canvas fit f = 0.294 (lead J002-D8, screen-contract §5). Touch rubric: Apple 44 pt frequent / 28 pt minor (brief). Sample data: balance 1,240 gems, pity count 37 / 90, banner ends in 6d 12h. All unit names are invented originals.

## 2. Evidence ledger
| Claim used | Tag | Source | Scope |
| --- | --- | --- | --- |
| Paid random = Robux or Robux-bought currency; all outcomes with numeric odds before purchase, total exactly 100 %; labelled control, not a bare (i) | V | platform-policy rules.md § A (`paid-random-items.md:16-57`) | every summon |
| Pity is a probability modifier: its numeric effect is shown before purchase, and the shown odds change while it is active | V | rules.md § A (`paid-random-items.md:75`) | §7.4 |
| `ArePaidRandomItemsRestricted` true → player must not use the generator; hiding is preferred; blocking only the button is discouraged | V | rules.md § A; P-03 (DF 4654622) | §7.5 |
| Odds UI and server roll read one table | V/O | platform-policy P-01 | §7.1 |
| Robux prices read live, never typed | V | P-05; ui-basics U-07 | gem shop link |
| Celebrate only after the server confirms; skip reaches the same result; 10x ends on a full summary | V/O | ui-design shops §2, §5 | §6, §13 |
| Fit f = min(safe w / 1920, safe h / 1080) ≈ 0.294; 44 pt = 150 px, 28 pt = 96 px, 11 pt = 38 px | A | screen-contract §5; lead J002-D8 | §9 |
| Top-bar height 58 pt | U | screen-contract §5 (UNVERIFIED) | §9 |
| All motion durations / easings | P | ui-basics ui-effects.md starting values | §13 |
| L* and contrast values | A | CIE L* and WCAG formulas, script `refs/lab.py`, 2026-10-21 | §10 |

## 3. Decision record
| Field | Fill |
| --- | --- |
| Goal | Spend 50 gems for 1 summon or 500 gems for 10 summons on the Storm Oracle banner, or leave. |
| Info needed | Featured unit and its own chance; chance per rarity tier; every unit with its %; pity rule and the player's count; price; balance; balance after; what happens after (unit added, cannot undo). |
| Actions | Odds & Units · Summon ×1 · Summon ×10 · + (gem shop) · Close (X, B, Esc) · in popups: Confirm / Cancel · Back · Try again · OK / Get gems · Done / Again. |
| Consequence | Odds & Units: opens the full odds, no cost. Summon ×N: opens Review, no cost. Confirm: spends N × 50 gems for N separate rolls. Again: opens Review again (never spends directly). + / Get gems: opens the gem shop (Robux). |
| Proof it registered | Press: the button face drops by its lip (04). Accepted: Confirm shows a spinner + "SUMMONING…", Cancel goes disabled, the line "Waiting for the server… No gems are spent until it says yes." (05). Confirmed: reveal with unit, rarity word, "Added to your units.", balance −N (06, 07). |
| Recovery | Cancel / Back / B return to 01 with focus on the button that opened the popup. Failed (08) says nothing was spent and offers Try again / Back. Not enough gems (09) says the gap and offers OK / Get gems. |
Every component maps to a row. Decoration with a narrative job only: the backdrop rune, swirl, sparkles (they say "summon" and "rare"), and they never sit behind small text (§10).

## 4. Wireframe: two structures compared
| | A. Info column + banner hero + bottom buttons (chosen) | B. Full-bleed hero, odds only behind a button |
| --- | --- | --- |
| How | Left: banner info panel with the 4 tier chances and pity on the main screen; labelled ODDS & UNITS below it. Right: banner card with the hero breaking out of the top. Bottom right: Summon ×1 and ×10, equal weight. | Hero fills the screen; title and buttons float over the art; odds only in a popup. |
| For | Tier odds and pity are on screen **before** any tap; the full list is one labelled tap away and repeated in Review; the hero still owns half the screen. | Most dramatic look. |
| Against | Less art space. | Odds hidden one level deeper; text over busy art fails contrast on phones; nothing to read in grayscale except the hero. |
| Winner | **A**: honesty and phone legibility beat drama; the hero still breaks out of its box (anime signature). |

## 5. Visual grammar
Style book `ui-style-anime`. Visual thesis [P]: *"A premium summoning altar: sharp violet panels, one glowing crystal action, and the featured unit with its rarity front and centre, every chance printed in plain numbers."*
| Element | One job |
| --- | --- |
| Cyan crystal block (gradient + lip + 2 full-height shine bars + corner facets + outer glow) | the action that moves forward (Summon, Confirm, Done, OK, Try again) |
| Dark violet glass block, no glow | secondary (Odds & Units, Cancel, Back, Again, Get gems, +, Close) |
| Grey block, white label with ink stroke | disabled, the label says why ("LOADING…") |
| White 6 px ring + soft white glow | focus (gamepad / keyboard; hover on PC = the same look) |
| Rarity = gradient colour + **word** + **pip count** (1-4 diamonds) | rarity; never colour alone |
| Yellow NEW badge with ink text | unit not owned before this summon |
| Yellow text | pity and rules that change odds |
| Angular header with cyan + pink tail accents | screen / popup title (decor + title only, not interactive) |
| Library rune, swirl, sparkles, glow, sunburst (L) | "summoning" mood; the sunburst appears only after a confirmed result |
Glow is on the two Summon buttons, the popup primary, and the hero. Both Summon buttons have the same weight on purpose, so the screen does not push the bigger spend.

## 6. States
Screen states: entry (01, focus on Summon ×1) · normal (01) · empty (n/a: a banner always exists; if the banner fails to load, Banner card `State=Loading` and Summon disabled "LOADING…") · max content (balance "99,999,999" fits the 210 px amount box at 44 px? **UNVERIFIED**; rule: abbreviate ≥ 1,000,000 as "1.2M" [P]; longest unit name "Kaida, Storm Oracle" wraps to 2 lines everywhere) · loading (Odds panel `Loading`, Summon `Disabled` "LOADING…") · pending (05) · error (08; Odds panel `Error`) · not enough currency (09) · not eligible (restricted player, §7.5, spec only) · success (06, 07) · recovery (§8).
Per item (unit card): idle · focus · NEW (boolean) · rarity ×4 · size Full / Compact. Owned / equipped are not on this screen (unit list).
Per control: idle · focus · pressed · pending · disabled-with-reason (Summon, Action); close: idle · focus · pressed.

| Frame | Node | Screenshots (`screens/`) |
| --- | --- | --- |
| 01 Main banner (inspect) | 12:2 | `01-main-1920.png`, `01-main-phone-0.294x.png` (564×318), `01-main-phone-0.294x-at2x-1128x636.png`, `01-main-grayscale.png`, `01-main-phone-grayscale.png` |
| 02 Odds open | 13:130 | `02-odds-open.png`, `-phone-0.294x`, `-grayscale` |
| 03 Review (×10) | 13:372 | `03-review.png`, `-phone-0.294x`, `-grayscale` |
| 04 Commit (Confirm pressed) | 13:503 | `04-commit.png` |
| 05 Pending | 13:641 | `05-pending.png`, `-phone-0.294x`, `-grayscale` |
| 06 Reveal 1x (confirmed) | 14:1014 | `06-reveal-1x.png`, `-phone-0.294x`, `-grayscale` |
| 07 Reveal 10x summary | 14:1097 | `07-reveal-10x-summary.png`, `-phone-0.294x`, `-grayscale` |
| 08 Failed | 13:789 | `08-failed.png`, `-phone-0.294x`, `-grayscale` |
| 09 Not enough gems | 13:924 | `09-not-enough-gems.png`, `-phone-0.294x`, `-grayscale` |
| Components board | 6:2 | `00-components-page.png` |
Note: 02-05, 08, 09 were captured before the last banner-card contrast fix (§10). That card is dimmed under the scrim in those frames; Figma shows the fixed version (instances).

## 7. Purchase, odds and pity
### 7.1 State machine (ui-design shops §2)
| State | Frame | Shows | Never |
| --- | --- | --- | --- |
| inspect | 01 | tier chances, featured 0.5 %, pity 37 / 90, ODDS & UNITS, two Summon buttons with cost | a spend on one tap |
| odds open | 02 | every unit with %, tier totals, computed TOTAL 100 % (1 + 4 + 20 + 75), pity rule in numbers, Back | rounded numbers without a note (none are rounded) |
| review | 03 | cost 500, balance 1,240 → 740, chances per summon, pity effect, "cannot be undone", Confirm (focus) / Cancel | price in art |
| commit | 04 | Confirm pressed (face down by the lip, hit area unchanged); **one** request sent; repeat taps ignored | a second request |
| pending | 05 | spinner + "SUMMONING…", Cancel disabled, "Waiting for the server… No gems are spent until it says yes.", balance unchanged; no rune, no glow, no sunburst | anything that looks like a result |
| confirmed 1x | 06 | rarity word + pips + colour, NEW, name, fact, "Added to your units.", balance −50, pity line; Done (focus), Again ×1 | a reveal before the server answer |
| confirmed 10x | 07 | all 10 cards (sorted Mythic → Rare), count line "1 Mythic · 1 Legendary · 2 Epic · 6 Rare", "All 10 were added", balance −500, pity line; Done (focus), Again ×10 | a summary that hides any card |
| failed | 08 | "The summon did not go through. No gems were spent. Your units did not change."; Try again (focus), Back | a unit that seems owned |
| not enough gems | 09 | cost, have, need (500 / 320 / 180), where to get gems, "Nothing was spent"; OK (focus), Get gems (secondary) | Get gems as the default |
| recovered | — | back to 01, focus on the Summon button that started it | a dead end |

Server rule for builders (ui-basics U-07, networking-security, platform-policy P-01): Confirm sends one request `{bannerId, count, oddsVersion}`. The server checks balance and that `oddsVersion` is the table it sent this player, rolls `count` times from that table (pity applied per roll), saves units + balance + pity in one write, then answers with the ordered results. The UI shows balance, units and pity only from that answer. A changed table (banner rotated) → 08 with the text "The banner changed. Check the new chances." [P]. A late answer after the screen closed is dropped (U-12); the units are still in the unit list.
Timeout: no answer in 10 s [P] → 08 (the server stays the source of truth; when the answer arrives later the unit list shows it).

### 7.2 Odds table [P] (shown on 01 by tier, on 02 in full, on 03 by tier)
| Tier | Tier total | Units and chance per summon |
| --- | --- | --- |
| Mythic (4 pips) | 1 % | Kaida, Storm Oracle (rate-up) 0.5 % · Ren Ashveil 0.25 % · Hoshi Vale 0.25 % |
| Legendary (3) | 4 % | 1 % each: Sora Flint, Mira Quill, Taiga Rook, Juno Spark |
| Epic (2) | 20 % | 4 % each: Yume Lark, Kenta Drift, Daro Pike, Lio Vesper, Suki Brand |
| Rare (1) | 75 % | 15 % each: Toma Shield, Pip Arrow, Rina Wisp, Bo Hammer, Lulu Fern |
| **Total** | **100 %** | 17 units; exact values, no rounding, so no disclaimer is needed |
A ×10 is 10 separate summons with the same chances (text on 02). No ×10 guarantee is added, so none is shown.

### 7.3 Gems and Robux
Gems are bought only in the gem shop (out of scope), opened by `+` (120 × 120) and "GET GEMS" (09). Robux prices there come from `MarketplaceService:GetProductInfoAsync` (P-05). The summon screen itself never shows a Robux price. "+" is dark glass (no glow) so it does not compete with Summon. Above a popup's scrim, the balance shows but "+" is hidden (no shop jump inside a modal).

### 7.4 Pity [P]
Rule shown on 02 and summarised on 01, 03, 06, 07: "if 89 summons in a row give no Mythic, summon 90 gives Kaida, Storm Oracle (100 %). Any Mythic sets the count back to 0." Each roll inside a ×10 counts. **Odds change while the pity is active (V `:75`):** at count 89 the odds panel and Review show "Your next summon: Kaida, Storm Oracle 100 %"; when a ×10 crosses the pity, Review says "Summon n of 10 is a sure Kaida" [P copy, not drawn]. Open: does the count carry to the next banner? (Q4).

### 7.5 Restricted players (spec only, no frame: not in the deliver list)
`ArePaidRandomItemsRestricted` true, or the PolicyService call failed (fail closed, P-02): every summon is paid random (gems can be bought), so the **summon entry in the lobby is hidden** (P-03) and this screen never opens. Alternative paths for the owner and economy designer to choose (Q1): (a) a fixed-price unit shop (each unit at a disclosed gem price); (b) an earn-only currency that can summon (then that banner is not paid random). The UI must not show a Summon button that refuses.

### 7.6 Owner actions (platform-policy §5)
Resubmit the maturity questionnaire (paid random items). Confirm the VFX library may be used in this game (effect-assets §3). Developer products for gems Listed in Creator Hub if sold outside the game.

## 8. Focus map (gamepad / keyboard)
| Screen | Initial focus | Traversal | Back (B / Esc) | Modal trap | Focus on close |
| --- | --- | --- | --- | --- | --- |
| 01 | Summon ×1 | row 1: + → Close; row 2 (bottom): Odds & Units ↔ Summon ×1 ↔ Summon ×10 (no wrap); up from bottom row → + | closes the screen | — | lobby |
| 02 | Back | Back only (odds rows are read-only text; the panel scrolls with the right stick if it overflows at 200 % text) | = Back | yes | Odds & Units |
| 03 / 04 | Confirm | Cancel ↔ Confirm | = Cancel | yes | the Summon button that opened it |
| 05 | none (both disabled) | — | ignored while pending | yes | — |
| 06 | Done | Again ×1 ↔ Done | = Done | yes | Summon ×1 |
| 07 | Done | cards (5 × 2 grid, read-only detail on A [P]) ↔ Again ×10 ↔ Done | = Done | yes | Summon ×10 |
| 08 | Try again | Back ↔ Try again | = Back | yes | the Summon button |
| 09 | OK | Get gems ↔ OK | = OK | yes | the Summon button |
During the reveal animation: A / tap / Enter = Skip (visible "SKIP" button, 400 × 150, top-right [P], not drawn as a frame). Hints follow `UserInputService.PreferredInput`. Nothing needs hover or long-press; no hold-to-summon.

## 9. Size math at f 0.294 (C5)
f = min(safe w / 1920, safe h / 1080). Smallest phone 667 × 375 pt, top bar T = 58 pt [U] → safe h 317 → 317 / 1080 = **0.294** (height-bound; width 667 / 1920 = 0.347). Rubric [V rule, P choice]: frequent 44 pt → 44 / 0.294 = **150 px**; minor 28 pt → **96 px**; essential text 11 pt → **38 px**; non-essential 9 pt → 31 px.
| Control | Canvas px | × 0.294 = pt | Class | Result |
| --- | --- | --- | --- | --- |
| Summon ×1 / ×10 | 440 × 170 | 129.4 × 50.0 | frequent | PASS |
| Confirm / Cancel / Done / Again / Back / OK / Try again / Get gems | 400 × 150 | 117.6 × 44.1 | frequent | PASS (at the line) |
| Pending Confirm (05) | 540 × 150 | 158.8 × 44.1 | — (disabled) | PASS |
| Odds & Units | 560 × 150 | 164.6 × 44.1 | frequent | PASS |
| Close X | 150 × 150 | 44.1 × 44.1 | frequent | PASS |
| + (gem shop) | 120 × 120 | 35.3 × 35.3 | minor | PASS 28 (FAIL 44 if rated frequent) |
| Unit card in 07 (tap for detail [P]) | 320 × 300 body | 94.1 × 88.2 | minor | PASS |
Gaps between neighbours: Summon ×1 ↔ ×10 40 px = 11.8 pt; popup buttons 40 px = 11.8 pt; + ↔ Close 34 px = 10.0 pt; cards 28 px = 8.2 pt. No hit areas overlap. (Android's 8 dp gap = 27 px would also pass.)
Safe area: with this fit the whole canvas is inside `CoreUISafeInsets`, so the top bar is outside the canvas. The backdrop (B) sits in a separate ScreenGui with `ScreenInsets = None` and fills the screen. Touch controls: the screen is a full-screen menu; proposal [P] hide the default thumbstick and jump while it is open (property **UNVERIFIED**); the `no-go` guide layer (12:192, hidden) marks both zones; Summon ×10 sits over the jump zone, which is only safe if the controls are hidden (Q3).

Text sizes (canvas px → pt): header 64 → 18.8 · reveal name 76 → 22.3 · banner title / unit name 56 → 16.5 · button 48 → 14.1 · cost / amount 44 → 12.9 · body 40 → 11.8 · **smallest UI text 38 → 11.2** (rarity words, NEW, chance rows, pity, unit names on cards, captions). Nothing on a screen is below 38 px. Thick lines: lip 10 px (2.9 pt), focus ring 6 px (1.8 pt), rarity / card strokes 5 px (1.5 pt) all ≥ 5 px; the dark silhouette outline is 4 px (1.2 pt) on purpose (an edge, not a cartoon "thick line") [P].

## 10. Gradients, shine and contrast (C4)
**Face gradients (top → bottom, L\*), every one ≥ 20:**
| Face | Top | Bottom | ΔL\* |
| --- | --- | --- | --- |
| Crystal (Summon, primary, gem-shop face) | #9CF4FF 91.2 | #1A8FD6 56.8 | **34.4** |
| Glass (secondary, close, +, gem pill) | #4C44A6 34.9 | #1A1545 10.5 | **24.4** |
| Disabled | #8A8AA0 58.1 | #4A4A5E 32.2 | **26.0** |
| Panels (info, popups, odds) | #40319A 28.4 | #100A33 5.1 | **23.3** |
| Banner card | #5B3FC8 37.8 | #160D45 8.0 | **29.7** |
| Header | #5B4BE0 42.2 | #1E1660 13.8 | **28.4** |
| Rarity Rare / Epic / Legendary / Mythic (card face, tag stroke, pity fill) | #7CC4FF 76.7 / #D49BFF 72.7 / #FFE58A 91.3 / #FF9AC4 75.0 | #2E5FE0 44.4 / #7A2BD6 39.1 / #E08A0C 65.0 / #E01A5A 48.7 | **32.2 / 33.6 / 26.3 / 26.4** |
| Card strokes (white → rarity bottom) | #FFFFFF 100 | per rarity | 35.0-60.9 |
| Banner stroke | #FF9AC4 75.0 | #5B4BE0 42.2 | 32.8 |
| NEW badge | #FFE680 91.4 | #E89A00 69.7 | **21.8** |
| Gem icon | #F7B2FF 81.2 | #A21FD0 43.1 | 38.1 |
| Backdrop (01-05, 08, 09) | #33268F 23.9 | #050314 1.3 | 22.6 |
| Reveal backdrop (06, 07) | #40209A 25.1 | #06031A 1.6 | **23.5** (was 12.3 with #2A1060; fixed during review) |
Grayscale check (`01-main-grayscale.png`): button tops and bottoms read different; Summon buttons are the brightest controls.

**Shine and stripes cross edge to edge (owner J002-D9):** every shine bar is a parallelogram from y = −20 to y = h + 20, clipped only by the shape's own mask (`fx (mask: face)` groups): Summon and Action buttons (2 bars + 2 corner facets bounded by the edges), unit cards (2 bars), odds panel (3 stripes, full height), banner card (2 stripes, full height), info panel (1 stripe + ring texture crossing the edge). No bar ends inside a shape. Visible in `00-components-page.png` and every frame.

**Contrast [A]** (weakest background): white on panel bottom 18.4, on panel top 10.9; muted #C9C3F5 on panel top 5.9; yellow #FFD34D on panel top 6.9; rarity words on the panel top: Rare 5.3, Epic 4.7, Legendary 7.9, Mythic 5.0; rarity words on the ink strip 8.6-14.5; white on the ink strip 18.1; ink label on crystal at label height (t 0.3, ≈ #75D6F2) ≈ 10, at cost-row height (t 0.72, ≈ #3FABE1) ≈ 6.5; white label on glass ≥ 7.8; ink on NEW badge bottom 7.8; ink on RATE-UP chip 12.7. Outlined text (screen-contract §5): ink fill vs white stroke 18.1 on crystal labels.
Found and fixed in review: banner "0.5 % per summon" in pink measured **2.78** on the lightest real pixel of the banner column → changed to white (worst 5.47); banner fact text in muted measured 3.28 → white; disabled labels ink on grey (2.1 at the bottom) → white fill + ink stroke (white vs grey ≥ 4.6); rune circle moved out of the banner text column.

## 11. Layer table (N native · B baked · T tiled · L library)
| Part (Figma name) | Size on canvas | Mark | Roblox build |
| --- | --- | --- | --- |
| backdrop gradient + light beams (edge-fade bars) | 1920 × 1080 | B | one PNG 960 × 540 stretched (soft gradient), ScreenGui `ScreenInsets = None` [P]; the beams could be N (Frame + UIGradient Transparency 1→0.93→1, Rotation) |
| fx/CI-0173 backdrop rune | 980² | L | ImageLabel rbxassetid://14197282370, ImageTransparency 0.9 |
| Header (angular face, accents, top light) | hugs title, h 120 | B + N | silhouette PNG 9-slice (SliceCenter on the flat middle, corners keep the points [P 60,0,120,0]); title = TextLabel Montserrat ExtraBold 64, ink fill + UIStroke white 5 Round; ZIndex above the panel it overlaps; `Active = false` so it never sinks taps |
| Info panel / popups / odds panel face (chamfer, gradient, inside stroke) | 640 × 630 · 1120 × auto · 1640 × 960 | B | chamfer 9-slice PNG with the gradient baked (vertical gradient → stretch on Y keeps it); or N: Frame + UIGradient Rotation 90 + UIStroke 3 Inner #8F86FF 0.3 + per-corner UICorner can't chamfer → B chosen |
| stripes inside panels / banner (`fx (mask: face)`) | full height | B | Normal white 4-7 % bars baked into the panel PNG (no blend mode) |
| fx/CI-0065 clipped ring (info panel) | 520² | L | ImageLabel rbxassetid://12362738407 inside a CanvasGroup clipped to the panel, ImageTransparency 0.86 (or baked into the panel PNG) |
| Crystal button: outline, lip, face gradient, rim, 2 shine bars, 2 facets, glow | 440 × 170 / 400 × 150 | B | one PNG per variant and size (Idle, Pressed, Disabled; Focus = Idle + N ring); shine and facets are Normal white 18-40 %, already baked in Figma without blend modes; outer glow = N UIShadow (Offset 0, Color #3FE0FF, BlurRadius 28 [P]) on a hidden rectangle, or baked; 9-slice SliceCenter [P 40, 40, 400, 120] |
| Glass button / close / + | 400 × 150 · 150² · 120² | B (or N) | same as crystal without glow; a simple N alternative: Frame + UIGradient + UIStroke (corners would be round, not chamfered) |
| Focus ring | control + 28 | N | UIStroke 6 white on a backing Frame, or `SelectionImageObject` with a chamfer ring PNG; UIShadow white 0.45 |
| Labels, costs, balance, names, %, pity, counts | — | N | TextLabel Montserrat (ExtraBold / Bold) + UIStroke Round (never tween Thickness) |
| Icons (gem, close, spinner, check, warning, plus, odds) | 46-96 px | B | one sprite sheet 256² (ImageRectOffset per icon) |
| Rarity tag | hugs, h 64 | N | Frame #140F3A + UIStroke 5 with child UIGradient (rarity top→bottom) + pips (sprite) + TextLabel; chamfer corner = optional PNG mask (B) |
| NEW badge | 124 × 58 | N | Frame + UIGradient + UIStroke 4 ink + TextLabel |
| Unit card face + stroke | 320 × 420 / 320 × 300 | N | Frame + UIGradient (rarity) + UIStroke 5 with UIGradient (white → rarity bottom); chamfer = B mask if wanted |
| Unit card shine bars | full height | B | one transparent overlay PNG per card size (white 16-22 %, any rarity) |
| Unit art | 320 × 312 / 320 × 206 | B | per-unit portrait PNG ≤ 512² (`ScaleType = Crop`); sits above the card with `ClipsDescendants = false` (breaks out 40 px); a ScrollingFrame list needs 40 px top padding |
| Hero art (banner, reveal) | 478 × 700 · 640 × 937 | B | per-unit full-body PNG 683 × 1000 (1024² budget only on the reveal; R07 memory rule) |
| name strip, pips chip | — | N | Frame #140F3A 0.94 / 0.9 + UICorner |
| fx/CI-0225, SW-0160, SP-0129, FL-0227, FL-0269, FL-0532 | see `library-picks.md` | L | ImageLabel with the id, ImageColor3 tint, ImageTransparency, Rotation for slow spins |
| Pity meter | 568 × 150 | N | track Frame + UIStroke; fill Frame Size X = count / 90, UIGradient mythic |
| Scrim | 1920 × 1080 | N | Frame #05031A BackgroundTransparency 0.28 |
| no-go guide | — | — | design guide only, hidden |
Share: by layer count about 55 % N, 30 % B, 15 % L. Baked parts: panel / header / button silhouettes (chamfers and baked stripes), icons, character art. Nothing relies on a runtime blend mode, inner shadow, blur or dashed stroke (the Figma file has none). Texture budget [P]: button and panel 9-slices ≤ 512², icons 256², portraits 512², heroes 683 × 1000 (2 on screen at most).

## 12. Live text fields (never in art)
| Field | Source | Longest tested | Wrap | Truncate? |
| --- | --- | --- | --- | --- |
| Unit name | unit data | "Kaida, Storm Oracle" (19 ch): 2 lines on cards (292 px) and banner (460 px), 1 line on reveal (860 px) | yes, grows down | never |
| Rarity word | unit data | "LEGENDARY" (fits 292 px at 38 px) | no | never |
| % values | server odds table (P-01) | "0.25 %" | no | never |
| Tier totals / TOTAL | computed from the table | "TOTAL 100 % (1 + 4 + 20 + 75)" | no | never |
| Balance | server | "1,240"; ≥ 1,000,000 → "1.2M" [P]; 9-digit raw **UNVERIFIED** | no | abbreviate only |
| Cost | banner data | "500" | no | never |
| Pity count / caption | server | "37 / 90", "Sure Mythic in 53 summons" | no | never |
| Banner end | server time | "Ends in 6d 12h" (real end time only; no fake countdown) | no | never |
| Titles | fixed copy | "NOT ENOUGH GEMS" (header hugs the title) | no | never |
Locale growth (×3 for short strings) not tested (**UNVERIFIED**); headers and tags hug their text, popup bodies wrap.

## 13. Reveal motion records (all values [P], starting from `ui-basics/references/ui-effects.md`; not built here)
| # | Beat | Element / property | Value [P] | Rule |
| --- | --- | --- | --- | --- |
| R1 | Input acknowledged | Confirm face + label Position Y + lip (10 px) | press 50 ms ease-out; release 120 ms | hit area never moves |
| R2 | Pending | spinner Rotation; label "SUMMONING…"; Cancel disabled | spinner appears if no answer in 100 ms; 1 rev / 800 ms | no rune, glow or colour in this beat; timeout 10 s → 08 |
| R3 | Result confirmed | popup out (UIScale 1→0.92, fade) then reveal backdrop in | out 195 ms, in 225 ms | starts only on the server answer |
| R4 | Anticipation | CI-0225 fade 0→0.5 + SW-0160 spin | 400 ms fade; spin 1 rev / 8 s | **same length and same look for every rarity**; no fake-out (never show a higher rarity colour first) |
| R5 | Rarity signal | FL-0532 sunburst + rune tint go to the **actual** rarity colour; rarity tag (word + pips) appears with it | 250 ms | colour, word and pips together |
| R6 | Information visible | hero art UIScale 0.94→1 + fade; name, NEW, "Added to your units.", balance −N, pity line | 225 ms; all text at once | skip lands here |
| R7 | Input available | Done gets focus | when R6 ends (≈ 1.1 s after the answer) | Again never spends without Review |
| R8 | Decoration | sunburst slow spin; sparkles FL-0227 / FL-0269 twinkle (scale 0.85↔1, transparency 0.1↔0.4) | 1 rev / 24 s; twinkle 1.2 s loops; stops after 6 s | nothing behind text moves |
| R9 | 10x stagger | cards fade + rise 12 px, in summary order | 80 ms apart, 200 ms each (total ≈ 0.9 s) | count line and buttons visible from the start; stagger cancels on any tap |
| R10 | Balance | counter "−N" chip, count-down display | chip 150 ms in, 600 ms hold, 200 ms out; count ≤ 600 ms | real balance applies at once |
**Skip:** visible SKIP button and tap-anywhere from R3 to R6 (1x: lands on 06; 10x: lands on 07 with all cards). Skip never changes results; nothing implies that tap speed, holding or timing changes odds (there is no hold-to-summon and no "tap to stop" mini-game).
**Reduced motion** (`GuiService.ReducedMotionEnabled` / `@ReducedMotionEnabledTrue`): R3-R9 become one 120 ms cross-fade to the final frame; sunburst static at 0.15; no spin, scale, twinkle or stagger; every word, colour, pip and number is identical to 06 / 07.
**Flashing:** no full-screen white flash is specified. The sunburst and glow brightness change once (R5). Temporal check (review 16) is **UNVERIFIED** until a phone recording is analysed (≤ 3 flashes / s).
Sound markers (for the sound designer, not in scope): R1 press, R2 loop (quiet), R5 rarity sting (same length for all rarities, louder layers for higher rarity only after confirm), R6 owned chime.
Tuning test: record 01→03→05→06 and →07 on the smallest phone at 60 fps; frames from tap to first change (target ≤ 100 ms) and from server answer to readable name (target ≤ 1.2 s) [P].

## 14. Tokens: book vs used
| Token | `ui-style-anime` §4 [S] | Used [P] | Why |
| --- | --- | --- | --- |
| Font | Montserrat ExtraBold ("Extra Bold" in Figma) | Montserrat **ExtraBold** + Bold (Figma style name has no space for Montserrat) | checked with `listAvailableFontsAsync` |
| Text style | dark panel-matched fill + white stroke 3-4 | ink #140F3A + white 4-5 on light faces and headers; **white + ink stroke** on dark glass and grey | dark fill vanishes on dark faces (book allows "whichever passes") |
| Panel | deep base, chamfered, stripes 5-15 % | #40319A→#100A33, chamfer 36, stripes 4-7 % full height | stripes stay behind text |
| Header | pen tool, overlaps ⅓-½ | pen-tool arrow silhouette, overlaps popups by 56 / 120 ≈ ½; on 01 it does not overlap (no panel under it) | — |
| Glow (inner) | inner shadow, blur 8-16 | **none** | inner shadow is B-only and the faces already read; kept the bake list short |
| Glow (outer) | drop shadow blur 12-24, 40-60 % | 28 blur, spread 2, #3FE0FF 60 % on crystal only | readable at 0.294 |
| Shine | edge to edge | 2 bars 46 / 18 px + 2 corner facets, white 18-40 % | owner J002-D9 |
| Card | gradient fill + gradient stroke 4, radius 8 | stroke **5**, chamfer 22 instead of radius | 4 px = 1.2 pt; chamfer matches the angular look |
| Focus ring | white 4-6 px | white 6 px + white glow | — |
| Rarity tiers | grey / blue / purple / gold / red-pink + label | Rare blue · Epic purple · Legendary gold · Mythic red-pink (no grey Common tier in this banner) + word + 1-4 pips | second cue = pip count |
| Lip | "subtle" | 10 px (8 on close) | ≥ 8 px phone rule |

## 15. Self-review (review.md §1 and §5; labels per AGENTS.md §3)
| # | Check | Result | Evidence |
| --- | --- | --- | --- |
| 02 | Text size | PASS against the 11 pt rubric (≥ 38 px everywhere) — MCP-verified (Figma) | §9 |
| 03 | 200 % text | UNVERIFIED | not testable in Figma |
| 04 | Contrast | PASS after fixes (3 failures found and fixed) | §10 |
| 05 | Touch | PASS at f 0.294 | §9 |
| 06 | Safe areas | PASS by fit rule; top-bar height and hiding touch controls UNVERIFIED | §9 |
| 07 / 08 | Navigation, focus | specified, not run on a device | §8 |
| 09 | State semantics | PASS: idle / focus / pressed / pending / disabled distinct; selected ≠ NEW | `00-components-page.png` |
| 11 | Critical cues | PASS: rarity = word + pips + colour; disabled = grey + word | `*-grayscale.png` |
| 13-15 | Motion | records with PROPOSAL values and a test; reduced motion keeps all meaning | §13 |
| 16 | Temporal safety | UNVERIFIED | §13 |
| 17 | Localisation | UNVERIFIED (English only) | §12 |
| 18 | Paid randomness | PASS: every unit and %, total 100 %, labelled ODDS & UNITS, tier odds on the main screen and in Review, pity in numbers | 01, 02, 03 |
| 19 | Price and grant | PASS in design: no reveal before the answer; balance changes only on 06 / 07 | 05, 06, 07 |
| — | Grayscale: primary loudest | PASS: Summon buttons and hero brightest; + calmed to glass | `01-main-grayscale.png` |
| — | Phone 0.294× look | PASS: chances, pity, costs and buttons readable at 564 × 318 | `01-main-phone-0.294x.png` |
| — | Overlaps / layers through popups | PASS after fixes: balance counter peeked over the odds panel (hidden in 02); "−500" overlapped the count line (moved left of the counter); "SUMMONING…" overflowed the button (button 540 wide in 05); NEW badge covered faces (moved to the strip edge); 10x cards touched the buttons (rows tightened). Dimmed main screen under the 72 % scrim is intended | screenshots |
All screenshots are **MCP-verified (Figma)**, not in-game.

## 16. PROPOSAL list (owner to confirm)
1. Banner "Storm Oracle", all unit names, Kaida as the rate-up Mythic, all odds in §7.2.
2. Prices 50 / 500 gems, no ×10 discount, no ×10 guarantee.
3. Hard pity 90 → Kaida 100 %, reset on any Mythic (§7.4).
4. Layout A (§4); equal weight for ×1 and ×10; Done is primary after a reveal; OK is primary on "not enough gems".
5. Copy: "ODDS & UNITS", "CHANCE PER SUMMON", "Sure Mythic in N summons", "Waiting for the server… No gems are spent until it says yes.", "SUMMON FAILED", "NOT ENOUGH GEMS", "Added to your units.", "AGAIN ×1 / ×10".
6. Colours and gradients (§10), scrim 72 %, focus ring white 6 px.
7. Sizes: Summon 440 × 170, actions 400 × 150, close 150, + 120, cards 320 × 460 / 320 × 340, text ladder 76 / 64 / 56 / 48 / 44 / 40 / 38.
8. Motion values R1-R10 and reduced-motion behaviour (§13).
9. Hide default touch controls while the screen is open.
10. Restricted players: hide the summon entry; alternative path to choose (Q1).
11. Balance abbreviation from 1,000,000 ("1.2M").

## 17. Open questions (defaults I used)
- Q1 Restricted players: fixed-price unit shop, or an earn-only summon currency? Default: hide the summon entry, no alternative drawn.
- Q2 Is "+" (gem shop) a frequent control (needs 150 px)? Default: minor, 120 px.
- Q3 Can the default touch controls be hidden while this screen is open (`GuiService.TouchControlsEnabled`, UNVERIFIED)? If not, Summon ×10 must move out of the jump zone.
- Q4 Does the pity count carry to the next banner? Default: yes [P].
- Q5 Should a ×10 guarantee (at least one Epic) exist? Default: no; if yes, its numbers go on 02 and 03.
