---
name: ui-style-anime
description: Make Roblox game UI in the anime style in Figma - sharp angular pen-tool headers that overlap the content, glow and shine on what matters, crystalline main buttons, solid cards with gradient fill plus gradient stroke, oversized character or item art that breaks its box, rarity gradient tiers, dark panel-matched text with a light stroke (Montserrat ExtraBold), white selection outlines. Use when the game's UI style is anime, gacha, tower-defense, fighting or RPG style, or the owner says "make it look like an anime game", "flashy", "like an anime TD inventory". Gives tokens, a recipe per component (panel, header, search, sort/filter, main buttons, unit card, stats box, capacity, close), states, borrowed fundamentals, and the Roblox build per part. Read ui-design and ui-figma first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J002. Main source: TA (UI Genesis anime TD inventory, Photoshop, experimental, few numbers, file lost mid-video; `knowledge/reference/ui/03-anime-photoshop.md`). Figma steps here are mapped from TA's Photoshop moves and rebuilt on the TC / TS Figma fundamentals, so most values are **PROPOSAL**. Tune per game; owner confirms.

# Anime UI

## 1. When this skill starts
The game profile (or the owner) picks anime. Visual thesis default (PROPOSAL): *"Anime UI that feels sharp, energetic and premium, where the character and its rarity are the hero and the primary button glows."* TA's own warning: the video shows style, not UX (TA@9:52). `ui-design` supplies the UX.

Before styling: make the screen's target reference image with ChatGPT and build to it (`ui-figma/references/image-generation.md` §2, owner J002-D12); effects from the VFX texture library (`ui-figma/references/effect-assets.md`).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Technique details (F-ids) | `ui-figma` SKILL.md §4 |
| Native vs baked (glows, blends, custom silhouettes) | `ui-figma/references/roblox-handoff.md` |
| TA principles and steps with timestamps | `knowledge/reference/ui/03-anime-photoshop.md` |
| Character renders, item art, sparkles | `ui-figma/references/image-generation.md` (anime style line; originals only) |

## 3. Signature (TA §6)
Sharp, warped header silhouette overlapping the panel below · glow and shine on important things only · crystalline buttons with carved light cuts · oversized renders and icons breaking their boxes · rarity as colour-gradient tiers **with** a tier label · dark panel-matched text with a white stroke (inverted from the usual) · solid cards with a gradient fill and a gradient stroke · white selection outline · Montserrat ExtraBold.

## 4. Tokens (canvas 1920 × 1080). **Every number here is PROPOSAL**: TA states almost no values (`03-anime-photoshop.md` §9); a TA time cites the technique only
| Token | Value | Source |
| --- | --- | --- |
| Font | Montserrat ExtraBold (Figma style name **"ExtraBold"**, no space; Inter's is "Extra Bold": always read it with `listAvailableFontsAsync`; Roblox Montserrat family) | TA@21:28; J002-T09 |
| Text style | by surface: **light face** (crystal buttons, header, badges) → fill = a dark ink from the panel's hue (not pure black) + white stroke 3-4 px Outside Round (TA's signature); **dark face** (deep panels, dark glass, grey) → white fill + ink stroke. The dark fill disappears on the deep panels this book prescribes. Check both contrasts (ui-design screen-contract §5 outlined text) | TA@9:06-9:36; J002-T09 |
| Panel | deep saturated base (e.g. navy / violet), angled or chamfered corners via pen tool; stripes or shine at 5-15 % | TA@0:48, @16:11 |
| Header | pen-tool silhouette with sharp points, 1-2 accent colours, clipped texture + reflection + shadow; overlaps panel top by ⅓-½ of its height | TA@4:43-8:15 |
| Glow (inner) | **optional, off by default**: Inner shadow X 0 Y 0, blur 8-16, spread 0-2, light tint at 40-60 %. It is bake-only (UIShadow Inset is beta) and multiplies the bake per state and colour; use it only on the hero part | TA@1:30 → F-08; J002-T09 |
| Glow (outer) | Drop shadow X 0 Y 0, blur 12-24, the button's hue at 40-60 % | TA@19:37 |
| Shine / stripes / carved cuts | cross the whole shape edge to edge, never stop in a hard line inside it (ui-figma F-07, owner J002-D9). Carved light cuts (facets) count as shine: each facet touches the face edge (corner triangles, edge bands); free-floating cuts inside the face are not allowed | J002-D9; J002-T09 |
| Card | solid (no transparency), gradient fill + gradient stroke 4 px; **chamfered corners** by default (the sharp signature, §3); a radius ladder 8 (cards) / 6 (wells) only when the game wants a softer anime look; one choice per game | TA@21:42-22:16; J002-T09 |
| Focus ring | white 4-6 px outside the card | TA@24:54 |
| Rarity tiers | gradient pairs per tier + tier label (e.g. Common grey · Rare blue · Epic purple · Legendary gold · Mythical red-pink, PROPOSAL; TA shows mythical, legendary, uncommon) | TA@29:12 |
| Grid | 5 columns rather than 6 when names are long | TA@28:18 |

## 5. Component recipes
1. **Main panel**: pen-tool shape (chamfer two opposite corners) → base gradient → thin light stroke 2 px Inside at 40 % → mask group with 2-3 diagonal stripe rectangles at Soft light 10 % on the left third (TA@16:11) → dark scrim behind on busy scenes.
2. **Header** (TA §3): pen tool (`createVector` with SVG path data through the API), sharp asymmetric silhouette (points, notch), flatten → gradient → inner glow → clip a texture inside (F-07) → duplicate the texture flipped and faded as a reflection + a soft shadow (TA@7:49) → title text (dark fill, white stroke) → place it overlapping the panel and the search bar; tell the builder its ZIndex is above them and that it must not block taps on what it covers.
3. **Search well** (TA §3): black rectangle at 40-55 % opacity, radius 6, magnifier icon + placeholder; clear (×) button.
4. **Sort / filter buttons** (TA@14:21): rounded rectangle, base gradient, subtle outer glow; icon black with a stroke at Overlay (bake) so it reads as part of the button; **label or tooltip** with the active sort and filter count (TA gap).
5. **Primary button** ("Equip best", TA@18:48): shape with carved light cuts (Subtract small shapes, fill them light) → gradient → inner glow → outer glow → label dark-fill white-stroke or white with dark stroke, whichever passes contrast. Brightest object on screen (F-19). Colour variants from colour variables (TA used hue/saturation; F-14).
6. **Bulk / destructive button** ("Unequip all"): same shape, **calmer** (no outer glow, darker hue) + confirm step (TA gap).
7. **Unit card** (TA §3 list boxes; in a scroll list leave top padding for art that breaks out, because a ScrollingFrame clips): solid card, rarity gradient fill + gradient stroke 3 px → render or icon larger than the card, breaking out at the top (do not clip the frame, F-16) → name at the bottom in a dark strip, wraps to 2 lines → tier label pill → badges `equipped` (distinct from the white selection outline) · `locked` · `new`.
8. **Stats box** (TA@21:15): solid boxes, gradient fill + gradient stroke, oversized stat icon, value right-aligned, tier label on top; values aligned in a column (Persona-style disciplined data inside an expressive frame, ui-design style-choice §4).
9. **Capacity counter** (TA@14:58): "34 / 50" near the list header; warning colour + icon at ≥ 90 % (PROPOSAL); full state says what to do.
10. **Close button**: small angular shape matching the header, glow on hover only; top-right, hit area to the touch rubric.
11. **Summon banner and reveal (gacha)**: tested in J002-T09 (`content/ui/anime-summon/`). Rules first: `platform-policy` (paid random items) and ui-design `shops-rewards-onboarding.md` §2-§5.
    - **Banner screen**: info column (banner name, end time, chance per tier **in numbers**, pity meter with "n / max" and "sure X in n summons") + hero banner card (oversized render breaking out of the card, rate-up tag, rarity tag, name, % per summon, one-line role) + a labelled "Odds" control (opens the full unit list; totals 100 %) + Summon ×1 / ×10 as equal crystal buttons with the live cost.
    - **Review popup**: cost, balance before → after, chance per summon, pity effect, "cannot be undone", Confirm (focus) / Cancel. Pending: no magic effects, "waiting for the server", nothing spent yet.
    - **Reveal**: library rune circle + sunburst behind the hero (sunburst only after the server confirms), rarity tag at ≈ 1.4× size, name, "Added to your units", balance change, pity line. Anticipation looks and lasts **the same for every rarity**; no fake-out.
    - **×10 summary**: all 10 cards (sorted top rarity first), a count line ("1 Mythic · 1 Legendary · …"), NEW only on first copies; after a reveal, Done is primary and Again goes through Review (never a direct spend).

## 6. States in anime
| State | Look (PROPOSAL) |
| --- | --- |
| Focus / hover | white 3 px ring + outer glow up (TA@24:54) |
| Pressed | glow down, face 2-3 px lower, light cuts dim; hit area unchanged |
| Selected | persistent rarity-coloured or gold ring + brighter face (not the white focus ring) |
| Equipped | check badge (separate from selected) |
| Disabled | glow off, desaturate, reason text |
| Rarity reveal | rarity colour **and** label; follows ui-design reward states |

## 7. Borrowed fundamentals (why this book is stronger than TA alone)
| From | Technique | Why |
| --- | --- | --- |
| TC | group mask for clipped textures and highlights; outlines around multi-layer shapes | exact Figma method for TA's clipping |
| TC / TS | Alt-hover padding, auto layout grids, align to fix drift | TA places things by eye |
| TS | hard-shadow text and one outline weight | consistent readable labels |
| TS | resize face + mask together; Scale tool caution | keeps glows and strokes intact |
| TP | mirrored ornament components; edge-fade strips | symmetric header ornaments, fading accent bars |
| TP | zoom-out check | glow and texture detail disappear at phone size |

## 8. Roblox build
| Part | Build |
| --- | --- |
| Custom header / panel silhouettes, carved buttons, glows, dodge/overlay layers, stripes | **B**: export per size; 9-slice when the middle is flat |
| Card gradient fill + gradient stroke | **N**: Frame + UIGradient; UIStroke with its own child UIGradient; UICorner |
| Outer glow on rectangles | **N**: UIShadow (Offset 0, coloured) |
| Outer glow on chamfered or custom shapes | **B** baked into the button PNG, or **N** UIShadow on a hidden rectangle behind it (looser fit) |
| Inner glow (optional) | **B** (UIShadow Inset is beta); costs one bake per state and colour |
| White selection outline | **N**: second UIStroke toggled or tweened in Transparency |
| Oversized art | **N**: ImageLabel sibling above the card with ClipsDescendants off |
| Text | **N**: Montserrat ExtraBold + UIStroke |
Expect more baked art than cartoon or stud: budget texture memory (≤ 512² unless large, handoff §3). Magic circles, runes, swirls, energy wisps and sparkles come from the VFX library (**L**, `ui-figma/references/effect-assets.md`) before anything is drawn.

## 9. Pitfalls (TA gaps fixed here)
- **Copied art.** TA used a character render from another game found on Google: never. Use own or generated originals (image-generation rules) and log the source.
- Glow everywhere = no hierarchy: glow the primary action and the hero only.
- Header covering taps: ZIndex and input sinking must be specified.
- Rarity by colour only: tier label always.
- Long names: test the longest; fewer columns, wrap to 2 lines.
- Dark-fill text on a dark panel: use the surface rule in §4 (dark face → white fill); measure contrast on the real panel.

## 10. Self-check
- [ ] Hero (character / rarity) and primary button are the loudest; secondary controls calm.
- [ ] All art original, logged; no franchise characters or logos (`platform-policy`).
- [ ] Every card has selected ≠ equipped, rarity label, locked and new states.
- [ ] Contrast measured for dark-fill text; longest name tested.
- [ ] Baked parts listed with sizes; texture budget stated.

Project overlay: if `knowledge/overlays/ui-style-anime.md` exists, read it after this file; it wins for this game.
