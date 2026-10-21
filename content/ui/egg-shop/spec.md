---
type: spec
scope: game
status: proposed
updated: 2026-10-20
source: "J002-T07 brief (lead); skills ui-design, ui-figma, ui-style-cartoon, ui-basics, platform-policy; Figma file gVgO2Ql80LUerCpQe02CtD"
supersedes: []
---
> Author: ui-ux-designer · claude-opus-5-5 · high · 2026-10-20

# Egg shop (cartoon) — screen spec

Figma: https://www.figma.com/design/gVgO2Ql80LUerCpQe02CtD (pages `Refs` 0:1, `Components` 1:2, `Shop` 1:3). Node ledger: `figma-ids.json`. Screens: `screens/`. Image log: `refs/prompts.md`.
Number tags used below: **[S]** style-book token (`ui-style-cartoon` §4, TC time given there) · **[V]** verified rule with source · **[A]** arithmetic from a [V] rule · **[P]** PROPOSAL (owner has not confirmed) · **[U]** unspecified, no source exists.

## 1. Player moment
| Field | Value |
| --- | --- |
| Goal (one sentence) | A kid wants to pick one egg, know what pets can come out of it and how likely each is, and buy it if they can afford it. |
| Already knows | Coins come from play; eggs give random pets (genre norm, assumption). |
| Game state | Standing at the egg stand, not in danger; the shop is a modal over the world. |
| Input | Touch first (Roblox DAU 2025 mobile 83 % [V] ui-design D-05); mouse and gamepad must also work. |
| Locale | English copy here; text boxes leave room to grow (§11). |
| Cost of failure | Real money (Robux egg) or Robux-buyable coins → high. A mistaken buy cannot be undone. |
| Accessibility | Colour-blind safe rarity, Larger text, reduced motion (§12). |

Assumptions (game profile is empty, so I state them and continue): coins can be bought with Robux (brief says assume yes), so all four eggs are paid random items under platform-policy § A. Smallest supported phone = 375 pt short side (iPhone SE landscape 667×375). Touch rubric = Apple 44 pt frequent / 28 pt minor (brief default). Balance shown = 1,240 coins (sample).

## 2. Evidence ledger
| Claim used | Tag | Source | Scope |
| --- | --- | --- | --- |
| Paid random = Robux or Robux-bought currency; odds as numbers before purchase, total 100 %; labelled "Info/Details"-type control, not a bare (i) | V | platform-policy references/rules.md § A (`paid-random-items.md:16-57`) | all 4 eggs |
| `ArePaidRandomItemsRestricted` → player must not use the generator; hiding preferred | V | rules.md § A; P-03 (DF 4654622) | all 4 eggs |
| Robux price read at runtime (`GetProductInfoAsync`), never typed | V | platform-policy P-05; ui-basics U-07 | Galaxy egg |
| Celebrate only after the server confirms | V/O | ui-design shops §2 (R22) | states 05-06 |
| Touch 44 pt frequent / 28 pt minor | V (rubric), choice = brief | ui-design D-05 | §9 |
| Canvas→device factor 375/1080 = 0.347 | A | screen-contract §5 | §9 |
| Roblox top bar height on a phone ≈ 58 pt | **U** (my memory, not in the docs mirror; measure `GuiService.TopbarInset`) | — | §9 safe area |
| All timings / easings | P | ui-basics/references/ui-effects.md starting values | §12 |
| Contrast numbers | A | WCAG formula, computed 2026-10-20 (`spec` §9) | §9 |

## 3. Decision record (T01)
| Field | Fill |
| --- | --- |
| Goal | Choose an egg and buy one pet roll, or leave. |
| Info needed | Egg name, price + currency, balance, every possible pet + rarity + real % (from server table), whether affordable, what "Buy" does. |
| Actions | Chances (per egg) · Buy (per egg) · + coins · Close (X, Back, gamepad B) · in popups: Buy/Commit, Cancel/Back, Done, Buy again, Try again, OK, Get coins. |
| Consequence | Chances: opens the odds popup, no cost. Buy (card): opens Review, no cost. Buy (Review): spends the price for 1 random pet. Robux egg: Review → Roblox purchase prompt. Get coins: opens the coin shop (Robux). |
| Proof it registered | Press: button drops by its lip (Commit). Accepted: "Buying…" + spinner, Cancel/X disabled (Pending). Confirmed: pet + rarity + "Added to your pets", counter shows new balance with "-250" (Confirmed). |
| Recovery | Back/Cancel/X return to the shop with focus on the card that opened the popup; Failed offers Try again / Back and says nothing was spent. |
Every component on screen maps to a row above (RA-57). The annotation sticker and the context backdrop are not UI.

## 4. Wireframe: two structures compared (step 4)
| | A. Card grid + popups (chosen) | B. List left + detail pane right (always-open odds) |
| --- | --- | --- |
| How | 1 featured + 3 coin cards; each card: price, labelled **Chances**, **Buy**. Buy → Review popup that repeats the full odds. | Egg list on the left; selecting an egg shows odds + Buy on the right at all times. |
| For | Big egg art sells the fantasy (pet-sim norm); 2 taps to buy, never 1; odds are 1 tap away **and** on screen again before commit. | Odds always visible; fewer popups. |
| Against | Odds not on the card face itself. | Odds table (5 rows × 84 px) + list cannot fit at phone-legible sizes beside 4 eggs; the featured egg loses its stage; selection ≠ purchase is harder for kids to read. |
| Winner | **A**: every purchase path passes a screen that shows all odds (Review), the labelled Chances button gives odds before any buy intent, and egg art stays large. |

## 5. Visual grammar
Style book: `ui-style-cartoon` (brief). Visual thesis [P]: *"Bubbly pet-sim shop where each egg is a glossy treasure, the green Buy is the chunkiest thing on each card, and every chance is printed in plain numbers."*
| Element | One job |
| --- | --- |
| Green depth button | primary action (Buy, Done, OK, Try again) |
| White depth button (no gloss) | secondary / info (Chances, Back, Cancel, Get coins) |
| Grey depth button, grey outline | disabled, label states why ("Need more", "Loading") |
| Red square X | close |
| Navy 6 px ring | gamepad / keyboard focus (and card selection) |
| Sky-blue card / purple card + gold ribbon | coin egg / featured Robux egg |
| Gold pill | coin balance (currency) |
| Rarity pill = colour + word + 1-5 stars | rarity, never colour alone |

## 6. State list
Screen: entry (opens on Inspect, focus on Meadow Buy) · normal (01) · empty (n/a: the shop always has ≥ 1 egg; if the egg table fails to load, show Odds panel `State=Error` and no Buy) · max content (9-digit balance → counter abbreviates "1.2M"; longest egg name wraps to 2 lines) · loading (featured price "…", Buy "Loading" disabled; odds panel `State=Loading`, Buy blocked) · pending (05) · error/failed (07) · not enough currency (01 Lava card + 08) · not eligible (restricted player, §7.3) · success (06) · recovery (focus restore, §8).
Per item (egg): affordable / not affordable / price loading / selected (focus ring). Owned/equipped/claimed: n/a (eggs are consumed). New: n/a for this test.
Per control: idle · focus (hover = focus look on PC) · pressed · disabled-with-reason · pending. Cooldown: n/a.

| Frame | Node | Screenshot |
| --- | --- | --- |
| 01 Inspect (main) | 16:2 | `screens/01-inspect-main-1920.png`, `-phone-0.347x-667x375.png`, `-grayscale.png`, `-phone-grayscale.png` |
| 02 Odds open | 17:4537 | `screens/02-odds-open.png` |
| 03 Review | 17:5641 | `screens/03-review.png`, `03-review-phone-0.347x.png` |
| 04 Commit | 17:14121 | `screens/04-commit.png` |
| 05 Pending | 17:17080 | `screens/05-pending.png` |
| 06 Confirmed | 18:16960 | `screens/06-confirmed.png` |
| 07 Failed | 18:18747 | `screens/07-failed.png` |
| 08 Not enough coins | 18:19352 | `screens/08-not-enough-coins.png` |
| Components overview | 1:2 | `screens/00-components-page.png` |

## 7. Purchase and odds
### 7.1 State machine (shops §2)
| State | Frame | Shows | Never |
| --- | --- | --- | --- |
| inspect | 01 | egg, price + currency icon, labelled Chances, Buy | buy on one tap of a card |
| odds open | 02 | every pet, rarity (colour+word+stars), real %, Total 100 %, Buy, Back | rounded totals without a note |
| review | 03 | price, balance now, balance after, full odds again, Buy (focus), Cancel | price in art |
| commit | 04 | Buy pressed (lip gone); server request sent once; repeat taps ignored | a second request |
| pending | 05 | "Buying…" + spinner; Cancel and X disabled; "Waiting for the server… No coins are spent until it says yes."; balance unchanged | anything that looks like success |
| confirmed | 06 | sunburst (first celebration), pet, rarity tag, "Added to your pets.", counter 990 with "-250"; Done (focus), Buy again | celebration before the server grant |
| failed | 07 | "The egg was not bought. No coins were spent. Your pets did not change."; Try again (focus), Back | a pet that seems owned |
| not enough coins | 01 Lava card + 08 | card: grey "Need more", price still shown; popup: cost, have, need N more; OK (focus), Get coins (secondary) | a hidden price; Get coins as the primary |
| recovered | — | back to 01, focus on the card that started the flow | dead end |

Server rule for builders (ui-basics U-07, networking-security): Buy sends one request with the egg id; the server checks balance, rolls from the same odds table it sent the client, saves, then answers. The UI changes balance and shows the pet only from that answer. A late answer after the shop closed is dropped (U-12).

### 7.2 Robux (featured Galaxy egg)
Card price = live `MarketplaceService:GetProductInfoAsync(productId)` text (sample "99" in Figma, layer `price-live (…)`), fixed word "Robux" beside it. Until it loads: "…" and a disabled Buy "Loading" (`Egg card / Featured State=PriceLoading`). Flow: Buy → our Review (odds + "Robux" price) → Roblox purchase prompt (Roblox's own review/commit) → Pending until `ProcessReceipt` grants and saves → Confirmed. Prompt closed without purchase → back to Review, nothing changes. Prompt finished ≠ success (V R22).

### 7.3 Paid-random compliance (platform-policy)
- Odds: from **one** server table; the client shows the player's effective odds (P-01). Placeholder table below is **[P]**; every egg totals exactly 100 %, no rounding needed.
- Restricted players (`ArePaidRandomItemsRestricted` true, or PolicyService call failed → fail closed, P-02): coins can be bought with Robux, so **all four eggs** are restricted, not just the Robux egg. Proposal: hide the whole egg stand for them and offer a fixed-price pet stand (direct purchase at a disclosed price). Needs owner decision (Q1).
- Owner actions: maturity questionnaire declares paid random items (P-08); developer product for the Galaxy egg Listed in Creator Hub if sold outside the game.

| Egg [P] | Price [P] | Pets (rarity) and chance [P] | Total |
| --- | --- | --- | --- |
| Meadow | 250 coins | Bunny (Common) 60 % · Duckling (Uncommon) 25 % · Fox (Rare) 10 % · Owl (Epic) 4.5 % · Golden Deer (Legendary) 0.5 % | 100 % |
| Ocean | 1,000 coins | Crab 60 % · Turtle 25 % · Dolphin 10 % · Octopus 4.5 % · Pearl Whale 0.5 % (same rarity ladder) | 100 % |
| Lava | 5,000 coins | Ember Mouse 60 % · Fire Fox 25 % · Lava Lizard 10 % · Phoenix Chick 4.5 % · Magma Dragon 0.5 % | 100 % |
| Galaxy (featured) | live Robux | Star Kitty (Common) 40 % · Moon Bunny (Uncommon) 30 % · Comet Pup (Rare) 20 % · Nebula Owl (Epic) 9 % · Galaxy Dragon (Legendary) 1 % | 100 % |
Only Meadow's table is drawn in Figma (frames 02-05); the others are data for the builder. The "Total" row shows the sum computed from the table, so a bad table is visible.

## 8. Focus map (gamepad / keyboard)
| Screen | Initial focus | Traversal | Back (B / Esc) | Modal trap | Focus on close |
| --- | --- | --- | --- | --- | --- |
| 01 | Meadow Buy | rows: [Featured Chances, Featured Buy, Meadow Chances…]; up/down within a card (Chances ↔ Buy), left/right across cards, no wrap; up from any card → + coins / Close | closes shop | — | world |
| 02 | Back | Buy ↔ Back (vertical); odds rows are not focusable (read-only) | = Back | yes | the Chances button that opened it |
| 03/04 | Buy | Buy ↔ Cancel | = Cancel | yes | the card's Buy |
| 05 | none movable (all disabled) | — | ignored while pending | yes | — |
| 06 | Done | Done ↔ Buy again (horizontal) | = Done | yes | the card's Buy |
| 07 | Try again | Try again ↔ Back | = Back | yes | the card's Buy |
| 08 | OK | OK ↔ Get coins | = OK | yes | the Lava card's Buy |
Hint glyphs follow `UserInputService.PreferredInput` (U-06). Nothing needs hover or long-press.

## 9. Size math (smallest phone) and safe area
Factor f = 375 pt ÷ 1080 = **0.347** [A] (screen-contract §5; full-height fit). Rubric: frequent 44 pt → ≥ 127 canvas px; minor 28 pt → ≥ 81 px [A].
| Control | Canvas px (incl. lip) | × 0.347 = pt | Class | Result |
| --- | --- | --- | --- | --- |
| Coin card Buy | 260 × 128 | 90.2 × 44.4 | frequent | PASS (44) |
| Featured Buy | 224 × 128 | 77.7 × 44.4 | frequent | PASS |
| Featured Chances | 256 × 128 | 88.8 × 44.4 | minor | PASS |
| Coin card Chances | 260 × 88 | 90.2 × 30.5 | minor | PASS (28) — FAIL if the owner rates it frequent |
| Close X | 128 × 128 | 44.4 × 44.4 | frequent | PASS |
| + coins | 92 × 92 | 31.9 × 31.9 | minor | PASS |
| Popup buttons (Buy, Cancel, Back, Done, OK…) | 320–380 × 128 | ≥ 111 × 44.4 | frequent | PASS |
Gaps between neighbouring targets: card Chances→Buy 16 px = 5.6 pt; Review Buy→Cancel 22 px = 7.6 pt; featured Chances→Buy 20 px = 6.9 pt; hit areas never overlap (PASS on "no overlap"; no Apple gap rule exists; Android's 8 dp gap would fail — not our rubric).
**Risk (needs decision, Q2):** with `ScreenInsets = CoreUISafeInsets` the ScreenGui is shorter than the screen by the top bar. If the builder fits the 1080 canvas into that inset area, f = (375 − 58) ÷ 1080 = 0.294 [U top bar] and every 128 px button becomes 37.6 pt (FAIL 44, PASS 28). Proposal: compute the outer `UIScale` from the full viewport height, keep the top 167 canvas px (58 pt ÷ 0.347) free of interactive UI — done in this layout: header tab (not interactive) starts at y 130, Close starts at y 172, everything else ≥ 236 — and put interactive parts in a CoreUISafeInsets ScreenGui positioned with the same scale. Builder must confirm in the Device Simulator.
Bottom: lowest interactive edge = 1018 (card Buy incl. lip) → 62 px above the bottom ≈ 21.5 pt, clear of the home indicator (≈ 21 pt [U]). The modal covers the default thumbstick/jump zones: proposal [P] hide touch controls while the shop is open (`GuiService.TouchControlsEnabled = false`, property **UNVERIFIED** in this task).

Text (font size → pt at 0.347): Title 64 → 22.2 · Button 44 → 15.3 · Body 36 → 12.5 · rarity tag 32 → 11.1 · Small 30 → 10.4 (non-essential only: column heads, footnotes, status lines). Declared text rubric [P]: essential text ≥ 32 px (≥ 11 pt). The XAG mobile glyph target (≈ 4.6 mm ≈ 29 pt glyph ≈ 85 canvas px) is not met by any text here → **UNVERIFIED**, owner decision Q3.
Contrast [A]: ink #2A2F45 on white 13.2:1, on #F2F5F9 12.1:1; muted #5A6280 on white 6.0:1, on #F2F5F9 5.5:1 (PASS 4.5). White label fill on green face 2.7:1 alone, but every white label has a 3-5 px black outline: black vs green #7CF05A 14.5:1, vs card sky #82CBF6 11.8:1 (outline-carried legibility; method not defined in the skills, see skill-gaps G-07). Focus ring #1B2559 on white 14.4:1, on card 8.1:1.

## 10. Layer table (N native / B baked / T tiled)
| Part (Figma name) | Size on canvas | Mark | Roblox build |
| --- | --- | --- | --- |
| context-backdrop | 1920×1080 | — | not UI (the live 3D world) |
| scrim / modal-dim | 1920×1080 | N | Frame #0B1230, BackgroundTransparency 0.55 / 0.45 |
| Panel face + halo + float shadow | 1640×840 (shop), 1600×780 (popup), r 16 | N | Frame white + UICorner 16 + UIStroke Outer 10 white + UIShadow BlurRadius ~18 [P] |
| Panel dash-stitch (dashed 5 px #9BD3FF, inset 12) | 9-slice | **B** | `export/panel_stitch_9slice.png` (to export), SliceCenter = 24,24,24,24 [P] |
| Depth block: halo, outline, lip, face gradient, rim | per control | N | backing Frame + UIStroke Outer 5 #000 (ZIndex 2) + UIStroke Outer 10 #FFF (ZIndex 1); lip Frame offset +8/+10; face Frame + UIGradient Rotation 90 + UIStroke Inner 4 rim |
| fx: highlight bars (OVERLAY / SOFT_LIGHT) + half-tone (SOFT_LIGHT) | per control size | **B** | one transparent "gloss overlay" PNG per control size, Normal blend, baked from Figma with the blend applied; no blend modes at runtime |
| Labels, prices, names, %, balance, counts | — | N | TextLabel FontFace Fredoka One + UIStroke (Round join, never tween Thickness) + a dark duplicate TextLabel offset +3/+4 (text depth) |
| Icons (coin, chances, paw, spinner, check, star, warning, plus) | 26–96 px | **B** | one sprite sheet ≤ 256² (ImageRectOffset per icon) |
| Robux icon | 50 px | **B** | Roblox's official Robux icon asset — the Figma one is a placeholder |
| Egg art ×4 | 220–280 px | **B** | `export/egg_*_256.png` (coin cards), `egg_galaxy.png` 512 (featured / popup) |
| Sunburst (06 only) | 520² | **B** | PNG, rotation tween allowed (Normal blend) |
| Focus ring | control + 44 | N | UIStroke on a Frame, or SelectionImageObject |
| Rarity pill | auto width | N (+ B stars) | Frame + UIGradient + UIStroke 4 + TextLabel; stars from the sprite sheet |
Native share ≈ 80 % of layers (all shapes, strokes, gradients, text); baked = gloss overlays, stitch border, icons, egg art, sunburst. Blend modes, the dashed stroke and the inner-shadow-free design: nothing relies on a runtime blend mode, inner shadow, blur or dashed stroke (the backdrop blur is the game world, not UI; Roblox does not blur UI — show the real world behind the 45 % scrim).

## 11. Live text fields (never in art)
| Field | Source | Max tested | Wrap | Truncate? |
| --- | --- | --- | --- | --- |
| Egg name | egg data table | "Galaxy Egg" (10 ch); box 272/500 px wraps to 2 lines | yes, grows down; egg art shrinks | never |
| Coin price | egg data table | "5,000" | no | never |
| Robux price | `GetProductInfoAsync` (live, regional) | 4 digits | no | never |
| Balance | server | 9 digits → "1.2M" abbreviation [P] | no | abbreviate only |
| Pet name, rarity word, chance % | server odds table | "Golden Deer", "LEGENDARY", "0.5%" | 1 line; row grows | never (name, %, rarity) |
| Need-more amount | computed from live balance | "3,760 more" | no | never |
| Popup titles | fixed copy | "NEED MORE COINS" (15 ch at 64 px in an 800 px tab) | no | never — the 560 px tab clipped "YOU GOT A PET!", fixed by an 800 px tab |
Locale growth (×3 for short strings) **not tested** (UNVERIFIED).

## 12. Motion beats (all values [P], from ui-basics ui-effects.md; tune on a phone recording)
| Beat | Element / property | Timing [P] | Notes |
| --- | --- | --- | --- |
| Input acknowledged | button face + label Position Y +lip | press 50 ms ease-out; release 120–150 ms small overshoot | same on every button; never shrinks the hit area |
| Popup in / out | popup group: UIScale 0.92→1 + dim fade | in 225 ms / out 195 ms | from the button that opened it; reversal does not queue |
| Result pending | spinner Rotation loop | 1 rev / 800 ms [P] | starts if no answer in 100 ms |
| Result confirmed | sunburst fade + slow spin; pet badge pop UIScale 1→1.12→1 | 225 ms enter, burst 300 ms | only after the server answer; reveal animation itself is out of scope (VFX/animation job) |
| Info visible | pet name + rarity tag | at once with the pop (never hidden behind the anim) | skip (tap anywhere) jumps here |
| Balance change | counter "-250" float + count-down | pop 150, float 600, fade 200, count ≤ 600 | real balance applied at once; display may count |
| Error | failed popup body shake ±4 px, 3 cycles | 280 ms | no whole-screen shake |
| Input available again | Done / Try again focus | when the popup enter ends (≤ 225 ms) | |
| Reduced motion (`GuiService.ReducedMotionEnabled`) | all of the above | tween time 0 or 120 ms fade | same information, no travel, no sunburst spin |
Tuning test: record 01→03→05→06 on the smallest phone at 60 fps; count frames from tap to first visible change (target ≤ 100 ms) and from server answer to readable pet name.

## 13. Tokens: book vs used (C5)
| Token | `ui-style-cartoon` §4 [S] | Used | Why |
| --- | --- | --- | --- |
| Radius | 10 controls, 12-16 panels | 10 / 16 | same |
| Outline | 3 px black | **5 px** black | 3 px × 0.347 = 1 pt on the smallest phone, too thin to read as "thick"; 5 px (TS value) = 1.7 pt |
| Halo | 6 px white | **10 px** (5 visible outside the black) | keeps TC's 1:2 outline:halo ratio after the outline change |
| Rim | 4 px Inside | 4 px | same |
| Lip | 4 btn / 6 card [P] | **8 btn / 10 card** | 4 px = 1.4 pt; vanished in the 0.347× check |
| Text ladder | 56-64 / 36-40 / 28-32 / 22-24 | 64 / 44 / 36 (+32 rarity) / 30 | phone legibility: essential ≥ 32 px; 22-24 px = 7.6-8.3 pt is too small |
| Text stroke / depth | 3 px, copy 3-4 down | 5 (64) · 4 (44) · 3 (≤ 36); depth = drop shadow blur 0 Y = stroke (TS borrow) | one effect style per step |
| Highlights | 2 bars, Soft light cards / Overlay buttons | same; **off on Utility (white) buttons** | style-book pitfall: primary must win in grayscale |
| Half-tone | corners, Soft light | vector dots component `fx/halftone`, 2 opposite corners | the TC texture is a third-party image; drew an original |
| Panel | white, dashed blue Inside 5, halo 5 | white, dashed stitch **inset 12**, halo 10 | inset reads as stitching at phone size |
| Role colours | green / red / grey-white / blue / gold | #7CF05A→#2FB52A, #FF7A7A→#E0303F, #FFFFFF→#D3DAE4, #5CC8FF→#2C7BEF, #FFE45C→#FFAE1A [P] | book gives words only |
| Rarity | grey/green/blue/purple/gold + label | same + 1-5 stars [P] | word + star count = two non-colour cues |
| Focus | white 3-4 px outline (TA) | **navy #1B2559 6 px ring, 22 px out** | a white ring is invisible on the white cartoon panel |
| Disabled | desaturated, grey rim, label 50 % | grey face + **grey outline, no shadow**, label 100 % | label carries the reason, so it stays readable; grey outline makes it recede |
Figma variables: `Primitives` (54, scopes []), `Color` (26 semantic aliases), `Size` (11 floats). Gradients cannot bind to variables (SOLID-only binding), so gradient stops are written from the table above by script.

## 14. Self-review (ui-design review.md §1, labels per AGENTS.md §3)
| # | Check | Result | Evidence |
| --- | --- | --- | --- |
| 02 Text size | PASS against my [P] 11 pt rubric; UNVERIFIED against XAG glyph target | §9 |
| 03 Text enlargement 200 % | UNVERIFIED | not testable in Figma |
| 04 Contrast | PASS for ink/muted; outlined white text = outline-carried | §9 |
| 05 Touch | PASS at f 0.347; risk at 0.294 (Q2) | §9 |
| 06 Safe areas | PASS in layout (top 167 px non-interactive); top-bar height UNVERIFIED | §9 |
| 07/08 Navigation, focus | specified (§8); not verified on a device | — |
| 09 State semantics | PASS (Figma-verified): idle/focus/pressed/disabled/pending distinct in `00-components-page.png` | screenshots |
| 11 Critical cues | PASS: rarity = colour + word + stars; disabled = grey + words; Robux = icon + word | 02, 01-grayscale |
| 13/14/15 Motion | values PROPOSAL with tuning test; not recorded | §12 |
| 17 Localisation | UNVERIFIED (English only; one clipped title found and fixed) | §11 |
| 18 Paid randomness | PASS: all outcomes, real %, total 100 %, labelled "Chances", odds again in Review | 02, 03 |
| 19 Price and grant | PASS in design: live Robux price, no celebration before 06 | 05, 06 |
| Grayscale: primary loudest | PASS after fix (Utility gloss off, Disabled recedes) | `01-inspect-main-grayscale.png` |
| Phone 0.347× look | PASS: names, prices, Buy readable; annotation sticker is not UI | `01-inspect-main-phone-0.347x-667x375.png` |
All screenshots are **Figma-verified**, not in-game.
Found and fixed during review: scrim/dim lost its opacity when bound to a variable (whole shop invisible behind popups); Chances label overflowed the featured button; Buy was not the loudest in grayscale; popup titles wrapped; two close buttons visible behind popups; pending line overlapped the footnote.
Known leftovers: in 06 the counter's "-250" peeks above the popup edge behind the dim (harmless, shows the real balance changed); the Commit frame (04) differs from Review only by the pressed Buy, which is the honest difference.

## 15. PROPOSAL list (owner to confirm)
1. Egg names, coin prices (250 / 1,000 / 5,000), featured = Galaxy egg for Robux, sample price 99.
2. All pet names, rarities and odds in §7.3.
3. Layout A (card grid + popups), featured card left and larger.
4. Copy: "Chances" (not "Odds") as the control label; "Need more"; "Buying…"; "Waiting for the server… No coins are spent until it says yes."; "IT DID NOT WORK"; "YOU GOT A PET!".
5. Colours (§13), focus colour #1B2559, scrim 45 % / dim 55 %.
6. Sizes: outline 5, halo 10, lip 8/10, text ladder 64/44/36/32/30, buttons 128 high, Chances 88 high on coin cards.
7. Motion values (§12).
8. Done is primary after a pet (not "Buy again"); OK is primary on "Need more coins" (not "Get coins").
9. Hide touch controls while the shop is open.
10. Restricted players: hide the whole egg stand, offer a fixed-price pet stand (Q1).

## 16. Open questions (defaults I will use)
- Q1 Restricted players (`ArePaidRandomItemsRestricted`): hide all 4 eggs and offer a fixed-price stand? Default: hide all 4.
- Q2 Canvas fit: full-height `UIScale` (44 pt holds) vs inset-fitted (37.6 pt)? Default: full-height, top 167 px non-interactive.
- Q3 Text rubric: accept ≥ 11 pt essential text, or follow the XAG 4.6 mm glyph target (would need ~85 px text)? Default: 11 pt.
- Q4 Is "Chances" a frequent control (needs 128 px)? Default: minor (88 px).
- Q5 Does the game sell coins for Robux at all? If not, the three coin eggs are not paid random and only the Galaxy egg needs the gate. Default: yes (brief).
