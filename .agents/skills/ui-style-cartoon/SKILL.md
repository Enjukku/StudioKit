---
name: ui-style-cartoon
description: Roblox game UI in the cartoon style in Figma - chunky rounded controls, thick black outline with white halo, bright gradients, 3D lip, bubbly outlined text. Use when the UI style is cartoon, bubbly, cute, simulator, pet or tycoon, or the owner says "make it cartoony", "chunky buttons". Gives tokens, component recipes and the Roblox build. Read ui-design and ui-figma first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J002. Main source: TC (UI Genesis cartoon pet inventory in Figma, `knowledge/reference/ui/01a`, `01b`); borrowed: TS (stud), TA (anime), TP (pixel). Every value is one tutor's by-eye pick or a PROPOSAL: tune per game, owner confirms.

# Cartoon UI

## 1. When this skill starts
The game profile (or the owner) picks cartoon. `ui-design` gave the decision record, states and wireframe; `ui-figma` gives the techniques (F-ids below). Visual thesis default (PROPOSAL): *"Cartoon UI that feels bouncy, friendly and rewarding, where the primary action is the brightest, chunkiest thing on screen."*

Before styling: make the screen's target reference image with ChatGPT and build to it (`ui-figma/references/image-generation.md` §2, owner J002-D12); effects from the VFX texture library (`ui-figma/references/effect-assets.md`).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Technique details (F-01..F-23) | `ui-figma` SKILL.md §4 |
| Native vs baked, fonts, export, 9-slice | `ui-figma/references/roblox-handoff.md` |
| Original step list with timestamps | `knowledge/reference/ui/01a-cartoon-recipes.md`, `01b-cartoon-techniques.md` |
| Icon / item art prompts | `ui-figma/references/image-generation.md` (cartoon style line) |

## 3. Signature (what makes it read as cartoon, TC §5)
Rounded rectangles only, one radius per size step · thick black outline around face **and** lip · white halo ring outside the outline · light-to-dark vertical gradient face + darker solid lip · inner rim stroke in a brighter tint · white highlight bars and half-tone dots clipped into the face, in corners · Fredoka One, white with black outline and a dark depth copy · saturated, high-contrast palette · cards float on soft shadows.

## 4. Tokens (canvas 1920 × 1080; PROPOSAL unless a TC time is given)
| Token | Value | Source |
| --- | --- | --- |
| Corner radius | ladder: 10 px controls and cards, 16 px panels (PROPOSAL for 16) | TC@2:43, @31:42 |
| Outline | **5 px** black, Outside (TC used 3 at PC size; 3 px ≈ 0.9 pt on a small phone, so 5 is the phone-checked PROPOSAL from the G2 test) | TC@10:16-11:16; G2 |
| Halo | white **10 px** Outside under the 5 px black (5 px of white shows; TC's 3 + 6 has the same 1:2 ratio), + drop shadow Y 0, soft blur, low opacity | TC@11:45, @11:57; G2 |
| Rim stroke | 4 px Inside, brighter tint of the face | TC@38:22 |
| Lip | darker solid copy, ladder **8 px buttons / 10 px cards** (phone-checked PROPOSAL, G2 test; TC says "a couple of times") | TC@9:58; G2 |
| Panel | white face, 5 px dashed blue inner stroke, white 5 px Outside halo, soft shadow | TC@3:21-4:55, @35:13 |
| Input well | white, inner shadow X 0 Y 0 30 %, radius 10, grey Outside stroke | TC@5:45-6:48, @19:02 |
| Font | Fredoka One (Roblox `FredokaOne`; in Figma check the name: it may be listed as "Fredoka", then use Bold, handoff §2) | TC@7:26 |
| Text ladder | title 64-72 / button 44-48 / body 36-40 / essential minimum 38 / non-essential minimum 31 (phone-checked PROPOSAL, ui-design screen-contract §5); stroke ladder 5 (≥ 64) · 4 (44-48) · 3 (≤ 40) black Outside, Round join; depth = black copy or drop shadow blur 0, Y = stroke | TC@16:27, @24:48; TS@13:29 |
| Face gradient | 2 stops, top light / bottom saturated mid-tone, ≥ 20 L\* apart (pale cards too: deepen the bottom, do not lighten the top) | F-03; G2 review |
| Highlights | 2 white bars, slanted, crossing the whole face edge to edge (only the face edge cuts them), Soft light (cards, headers) or Overlay (buttons) | TC@13:25-14:51, @22:07; G2 review |
| Half-tone | dot image, corners only, Soft light | TC@14:51 |
| Role colours | positive green · danger red · utility grey-white · header blue · currency gold (PROPOSAL from TC buttons) | TC@19:48, @25:11, @27:42 |
| Rarity | common grey · uncommon green · rare blue · epic purple · legendary gold (PROPOSAL; TC shows gold, purple, green) + text label | TC@35:45 |
| Focus ring | white 4-6 px on coloured surfaces; navy (e.g. #1B2559) 6 px on the white panel, where white would vanish (G2 test, PROPOSAL) | G2 |
| Spacing | text inset 9; card gap ≈ 40+; panel margin ≥ 30 (PROPOSAL from TC@8:28, @18:13, TS@31:56) | |

## 5. Component recipes (each is a component with variants, F-15)
1. **Main panel** (TC §3.1): rectangle, white face, radius 10-16 → Inside dashed stroke 5 px, light blue → duplicate below as `halo`: Outside 5 px white + drop shadow Y 0 → group `panel`. Over a game screenshot, add a 50-60 % dark scrim behind it if the scene is busy (from TP).
2. **Header tab** (TC §3.9): depth block (F-03) in blue, outline 3 (F-04), group mask with 2 highlight bars + half-tones at both ends (F-07), title text (F-10). Let it overlap the panel's top edge (technique from TA@8:01; ~⅓ of its height is a PROPOSAL); its width hugs the title with padding, so long titles never clip.
3. **Primary button** (TC §3.5): depth block in green → outline → rim 4 bright green → mask: 2 highlight bars Overlay + half-tone in two opposite corners (flip H/V) → label + depth copy. Make it the brightest object in the panel (F-19).
4. **Danger / secondary buttons** (TC §3.6-3.7): duplicate the component; danger = red gradient + pink rim + black depth text; utility = white → grey gradient, highlights at lower opacity (white on white loses them, TC@28:33). Destructive actions get a confirm state (TC gap).
5. **Close button** (TC §3.8): square (Shift), radius 10, red gradient, pink Inside stroke, lip without stroke, black outline, "X" white with stroke and depth from the ladder; highlights copied from another button. Top-right of the panel, overlapping the corner; hit area ≥ the touch rubric (ui-design screen-contract §5).
6. **Search / input well** (TC §3.2): F-12 well; placeholder Fredoka One grey, 9 px inset all round (Alt-check); add a magnifier icon and a clear (×) button (TC gap).
7. **Item card** (TC §3.3): tall depth block in the rarity colour → outline + halo with soft shadow → rim 4 → mask: highlights Soft light + half-tone → item icon centred, may break the top edge (TA) → name (white, stroke) and level/qty line → **rarity label or icon** (colour is never alone, ui-design D-09) → state badges: `equipped` check, `new` dot, `locked` padlock. Grid: auto layout wrap, equal gaps; long names: fewer columns or smaller text, never clip (TA@28:18).
8. **Rarity variants** (TC §3.4): one variant property `Rarity`; each variant's face gradient stops come from the rarity token table (gradients cannot bind variables, F-14); lip and rim are solid, so they can bind rarity variables.
9. **Currency counter** (borrowed TS §3.11): icon + number in the currency colour with white stroke 3, Round join, hard shadow Y 3; a small `+` depth button to its right; stress-test with 9 digits and abbreviate (1.2M).
10. **HUD side button** (borrowed TS §3.10): square depth block per role colour, icon over a sunburst (from the VFX library, `ui-figma/references/effect-assets.md`), label under the icon. Size by the phone rubric, not by eye.
11. **Popup / toast** (PROPOSAL): mini panel (recipe 1) + header tab; toasts: white pill with the outline token, icon + one line, no highlights.
12. **Rewards and rare items**: sparkles, glows and sunbursts from the VFX library, behind the item, never over text.

## 6. States in cartoon
| State | Look (PROPOSAL) |
| --- | --- |
| Focus / hover | white 3-4 px ring outside the black outline (TA@24:54); scale 1.03-1.05 |
| Pressed | face drops by the lip depth, lip shrinks; highlights dim; hit area unchanged |
| Disabled | grey face, grey outline, no shadow; label and reason at full opacity (contrast) |
| Selected | brighter face + gold ring (persistent; never the white focus ring) |
| Equipped / owned | check badge in a corner (separate from selected) |
| Loading / pending | label replaced by "..." or a spinner; button not pressable |

## 7. Borrowed from the other styles (cross-pollination)
| From | Technique | Why it helps cartoon |
| --- | --- | --- |
| TS | hard drop-shadow text depth (blur 0, 100 %, Y ≈ stroke) | cleaner than a duplicate layer and maps to one rule |
| TS | Alt-hover padding + spacing readout, 30 px margins | the cartoon tutor fixes padding by eye in places |
| TS | Scale tool caution (strokes multiply) | keeps outline weight consistent |
| TA | white hover/selection outline; icons breaking out of cards; header overlapping the panel | life and depth without more texture |
| TA | bright = clickable, dark = passive | keeps hierarchy when every card is colourful |
| TP | dark translucent scrim behind the panel; zoom-out check | readability over busy simulator worlds |
| VFX library | sunbursts, sparkles, glows, rings (`effect-assets.md`) | real game effects, no drawing, shared textures |

## 8. Roblox build (per part; `ui-figma/references/roblox-handoff.md`)
| Part | Build |
| --- | --- |
| Face gradient, radius, rim, outline, halo | **N**: Frame + UICorner + UIGradient (Rotation 90) + UIStroke Inner (rim) on the face; backing Frame with UIStroke Outer 5 black (ZIndex 2) + white 10 (ZIndex 1). Confirm Inner / Outer is live in Studio (handoff §1); fallback nested Frames |
| Lip | **N**: second Frame behind, offset down |
| Soft shadow | **N**: UIShadow, Offset 0, BlurRadius ~12-20 (PROPOSAL) |
| Highlights + half-tones (Soft light / Overlay) | **B**: rebuilt as Normal white 15-25 % and exported as one transparent gloss overlay per control size (handoff §1 bake method), so rarity recolours stay native |
| Dashed panel stroke | **B**: 9-slice border image |
| Text, stroke, depth | **N**: TextLabel (Fredoka One) + UIStroke + a dark duplicate TextLabel offset down |
| Sunbursts, sparkles, glows | **L**: VFX library ids |
| Icons, item art | **B** |
Native share is high in this style: rarity recolours are just colour changes.

## 9. Pitfalls (TC gaps fixed here)
- No states in the video: every control here has §6 states.
- Rarity by colour only: add the label or icon.
- Equal loudness: everything glossy competes; keep highlights off secondary controls if the primary does not stand out in grayscale.
- Flattened outlines break on resize: use the backing-rectangle outline (F-04).
- Text sizes not checked for phones: convert with screen-contract §5.

## 10. Self-check
- [ ] Outline and halo identical everywhere; radius, lip and text from the ladders (one step per control size).
- [ ] Primary action brightest in grayscale; rarity readable without colour.
- [ ] Every component has §6 states; destructive actions confirm.
- [ ] Layer table marks N / B; gloss overlays exported per size; text live.
- [ ] Screenshots at phone and PC size next to the TC reference look.

Project overlay: if `knowledge/overlays/ui-style-cartoon.md` exists, read it after this file; it wins for this game.
