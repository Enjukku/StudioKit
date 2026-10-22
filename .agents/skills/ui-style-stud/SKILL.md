---
name: ui-style-stud
description: Roblox game UI in the stud (classic Roblox toy-brick) style in Figma - chunky two-layer 3D blocks, thick outline, tiled stud texture, color by button role. Use when the UI style is stud, brick, block, toy, classic Roblox, obby or tycoon, or the owner says "Roblox bricks", "stud UI". Gives tokens, component recipes and the Roblox build. Read ui-design and ui-figma first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J002. Main source: TS (UI Genesis stud shop + HUD in Figma, `knowledge/reference/ui/02a`, `02b`), the most exact of the four tutorials; borrowed: TC, TA, TP. Values are one tutor's by-eye picks or PROPOSALs: tune per game, owner confirms. Revised by J018 maker ui-ux-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (the transparency setting, one spinning sunburst, measured self-check).

# Stud UI

## 1. When this skill starts
The game profile (or the owner) picks stud. Visual thesis default (PROPOSAL): *"Toy-brick UI that feels solid, playful and unmistakably Roblox, where each button's colour tells you its job."*

Before styling: make the screen's target reference image with ChatGPT and build to it (`ui-figma/references/image-generation.md` §2, owner J002-D12); effects from the VFX texture library (`ui-figma/references/effect-assets.md`).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Technique details (F-ids) | `ui-figma` SKILL.md §4 |
| Native vs baked, tile fills, fonts, export | `ui-figma/references/roblox-handoff.md` |
| Original step list with timestamps | `knowledge/reference/ui/02a-stud-recipes.md`, `02b-stud-techniques.md` |
| Stud tile texture or brick-style icons | `ui-figma/references/image-generation.md` (stud style line) |

## 3. Signature (TS §5)
Stud tile texture over every coloured top face (soft, Overlay) · two-layer block: light gradient face + darker solid lip · one thick outer outline (5 px) around face + lip · bright inner stroke (4 px) · **colour = role** · bold white text with thick outline and a hard offset shadow · sunburst behind icons · square HUD buttons · translucent black panel with a 5 px stroke over a blurred game scene · lengths in whole studs.

## 4. Tokens (canvas 1920 × 1080; TS time or PROPOSAL)
| Token | Value | Source |
| --- | --- | --- |
| Outer outline | 5 px, Outside, on panels and every block | TS@3:36, @6:33 |
| Inner stroke | ladder, Inside, brighter hue of the face: 3 px small blocks (≤ 80 px tall, e.g. the + button) · 4 px standard · 5 px large side buttons | TS@12:02, @45:56, @53:51 |
| Lip | 7 px on small buttons, equal everywhere | TS@1:00:59 |
| Face gradient | top light, bottom saturated, ≥ 20 L\* apart; any shine bars cross the whole face (ui-figma F-03, F-07) | G2 review |
| Radius | small, 4-8 px (PROPOSAL; TS never states one: blocks read near-square) | — |
| Panel | black fill at reduced opacity (PROPOSAL 55-65 %), 5 px stroke Outside; contrast measured at this default, since the player's Background Transparency setting only makes it more opaque (ui-figma handoff §1) | TS@3:05 |
| Stud tile | image fill Tile, Overlay; a square tile = 4 × 4 studs; size blocks in whole studs ("three studs long") | TS@9:50, @10:20, @57:17 |
| Title text | 64, stroke 4, drop shadow Y 4, blur 0, 100 % | TS@12:47-13:55 |
| Button text | TS uses 25 on side buttons (≈ 7 pt on a small phone: too small); phone-checked PROPOSAL ≥ 38 essential, stroke 3, shadow Y 3 | TS@42:06, @59:54 |
| Small text | stroke 2, shadow Y 2 | TS@19:32, @55:49 |
| Counter | 46, currency colour, stroke 3 Outside Round, shadow Y 3 | TS@52:10, @55:54 |
| Font | not audible in TS (13:01). PROPOSAL: Luckiest Guy (titles) + Fredoka One (labels); both in Figma and Roblox | handoff §2 |
| Role colours | green = go / base / index / buy-more · red = exit / sell · blue = shop / currency · orange = featured offer · pink-purple = rebirth · grey-white = settings | TS §3 |
| Spacing | panel padding 30 all sides; card gap 24 | TS@31:56, @30:29 |
| Side buttons | start 70 × 70, then scaled ≈ 1.4× to ≈ 98 px (inferred from the stroke going 5 → 7): ≈ 29 pt on a small phone, below 44 pt for frequent buttons (§9) | TS@40:12, @41:08-41:46 |

## 5. Component recipes
1. **Menu panel** (TS §3.1): rectangle, black at reduced opacity, 5 px Outside stroke; centred horizontally, top left free for the header.
2. **Header** (TS §3.2-3.3): rectangle as wide as the panel → vertical green gradient (face) → lip (F-03) touching the panel → outline (F-04, 5 px) → inner stroke 4 → stud tile Overlay inside a mask (F-07) → title text (F-10, 64 / 4 / Y 4). Leave room at the right for the exit button.
3. **Exit button** (TS §3.5): duplicate the header, square it, red faces, pink inner stroke, "X" from the title text. Exit lip shallower than the header if it looks too deep (TS@9:09).
4. **Featured offer card** (TS §3.6): orange block; group mask with the item art (gem or render), a rotated low-opacity copy behind and a bigger faint copy for depth (TS@21:16); buy button (§5.6) at one side; short description stroke 2; price group = Robux icon + live price text.
5. **Currency product cards ×3** (TS §3.7): duplicate the offer card, resize face + first mask layer together (Alt+drag both sides), blue faces, amount text 36 white centred ("+50 Cash"), no description; gap 24, padding 30 (Alt-check).
6. **Buy button**: green block, Robux icon (vector, white, stroke 3 Outside, hard shadow Y 3) + **live** price text; never type a Robux price as fixed art (ui-basics U-07).
7. **HUD toggle row** (TS §3.9): three blocks above the menu (e.g. sell red · base green · shop blue); label only; group `toggle buttons`.
8. **Side buttons** (TS §3.10): square blocks per role; icon centred over a sunburst (Overlay) inside the mask; label at the bottom overlapping the icon (icon under text); stack centred vertically on the left edge; slot for a toggle at the top ("slow mode on" shows its **current state**, TS@58:11).
9. **Currency counter** (TS §3.11): "$" + number in green, stroke 3, Round join, hard shadow; `+` button = small flat green block (solid, no gradient), inner stroke 3, outline 3, white "+" with stroke 2, shadow Y 2. Place bottom-centre clear of the jump button.
10. **Toggle / switch** (PROPOSAL): block with two variants `On` (green, "ON") and `Off` (grey, "OFF") plus the label of what it toggles.

## 6. States in stud
| State | Look (PROPOSAL) |
| --- | --- |
| Focus / hover | white 3 px ring outside the 5 px black (TA); studs a little brighter |
| Pressed | face moves down 7 px onto the lip (the brick "clicks in"), lip hidden; hit area unchanged |
| Disabled | grey faces, studs at 50 %, reason text |
| Selected / active tab | brighter face + a yellow accent ring (persistent; not the white focus ring); inactive tabs darker |
| Owned / purchased | buy button becomes "Owned" grey with a check; never a second buy |
| Pending purchase | label "..." , not pressable (ui-design purchase states) |

## 7. Borrowed from the other styles
| From | Technique | Why |
| --- | --- | --- |
| TC | white halo + soft floating shadow on product cards | separates cards from the dark panel |
| TC | group-mask highlight bars at Soft light, half-tone corners | adds shine where studs alone look flat |
| TC | selection colours / colour variables for role recolours | faster than per-layer fill copying |
| TA | icons breaking out of the card top; white hover outline | life on product cards |
| TP | edge-fade strip behind the HUD toggles; zoom-out check | readability over bright obby scenes |
| ui-design | role colours plus labels or icons | colour = role must not be colour only |

## 8. Roblox build
| Part | Build |
| --- | --- |
| Faces, lips, outlines, inner strokes, radius | **N**: Frames + UIGradient + UIStroke Inner (3 / 4 / 5 ladder) + backing Frame with UIStroke Outer 5. Confirm Inner / Outer is live in Studio (handoff §1); fallback nested Frames |
| Stud texture | **T**: ImageLabel `ScaleType = Tile`, `TileSize` = one stud tile scaled to the stud size, `ImageTransparency` ~0.6-0.8 Normal (PROPOSAL; Overlay is not available), or **B** bake the overlaid face per colour |
| Sunburst | **L**: a `Flare / burst-rays` id from the VFX library (`ui-figma/references/effect-assets.md`), ImageLabel at high `ImageTransparency` (Normal blend replaces Overlay); optional slow spin ≤ 1 rev / 8 s on one button at a time (it is the screen's one attention motion), off in reduced motion (PROPOSAL) |
| Hard-shadow text | **N**: dark TextLabel duplicate offset Y by the shadow value (UIShadow text mode is beta) |
| Translucent panel | **N**: BackgroundTransparency ≈ 0.4 |
| Blurred game background | not UI: it is the live world behind the menu |

## 9. Pitfalls (TS gaps fixed here)
- **Phone size.** ≈ 98 px side buttons ≈ 29 pt on a small phone: phone variants ≥ 150 canvas px for frequent buttons, or larger invisible hit areas (ui-design screen-contract §5).
- Stud noise behind text: keep studs off text areas or lower their opacity; check contrast on the weakest spot.
- Colour-only roles: add icons and labels.
- Static prices: price text is live data from Roblox.
- No purchase states in the video: §6 adds pending, owned, failed.
- Scale tool multiplies outlines: reset to 5 after scaling (TS@41:46).

## 10. Self-check
- [ ] Outline 5 everywhere; inner stroke from the 3 / 4 / 5 ladder; lip 7 on every block of a size; lengths in whole studs.
- [ ] Every button has role colour **and** icon or label; toggles show their current state.
- [ ] Prices live; purchase pending / owned / failed states present.
- [ ] HUD buttons pass the hit-target check on the phone layout frame (S-49: size, gap, nothing under the jump button or Roblox top-bar buttons) and still read at phone fit (S-23).
- [ ] Role colours checked with `look_check.py palette --roles` against the rule sheet (S-19); white text with stroke passes both contrast pairs over the stud face (S-18).
- [ ] Layer table N / B / T; stud tile exported once and reused.

Project overlay: if `knowledge/overlays/ui-style-stud.md` exists, read it after this file; it wins for this game.
