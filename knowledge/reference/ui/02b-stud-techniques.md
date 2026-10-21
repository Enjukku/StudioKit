---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "owner-supplied transcript 'Stud Guide.txt' (UI Genesis, YouTube), J002"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

# Stud-style shop menu and HUD in Figma: step notes (J002-T02) (continued)

First part (source card, conventions, earlier sections): [[reference/ui/02a-stud-recipes]]. Citation rules are stated there.

## 4. Technique catalogue

| id | technique | exact steps | values | tag | TS |
| --- | --- | --- | --- | --- | --- |
| TS-T01 | Board size | Frame tool → right panel Presentation → 1920x1080 | 1920x1080 | [SHARED] | 1:00-1:07 |
| TS-T02 | Pan/zoom | Space + left-drag; Ctrl + scroll | n/a | [SHARED] | 1:14-1:20 |
| TS-T03 | Context background | Paste game screenshot, enlarge to cover, lock, Effects: swap Drop shadow for Layer blur, scrub value | blur not stated | [SHARED] | 1:32-2:27 |
| TS-T04 | Scrub-by-hover | Hover icon of a value (opacity %, weight, blur, scale) → click-drag | n/a | [SHARED] | 2:20, 3:11, 3:36 |
| TS-T05 | Alignment tool | Select layer(s) → alignment tool, right panel: centre horizontal / vertical | n/a | [SHARED] | 2:47, 59:02 |
| TS-T06 | Translucent panel | Fill black → lower fill opacity; + Stroke weight 5 | 5 px; opacity not stated | [SHARED] | 3:05-3:44 |
| TS-T07 | Two-layer 3D block | Rectangle + vertical gradient; Ctrl+D; bottom copy solid darker, moved down by arrow keys until it touches the frame | lip ~7 px on slow mode (1:00:59); other lips by eye | [SHARED] | 4:07-5:20 |
| TS-T08 | Flattened outer outline | Select both block layers → Ctrl+D → Ctrl+E → send to bottom → delete fill → stroke Outside | stroke 5 | [SHARED] | 5:53-6:33 |
| TS-T09 | Group + name every part | Ctrl+G, double-click name; names: header, exit button, price, top, base background, shop frame, dev products, toggle buttons, left side buttons, bottom | n/a | [SHARED] | 6:58, 26:59, 30:42, 33:31, 56:31, 58:56 |
| TS-T10 | Shift+arrow big nudge | Shift + arrow keys | large step (px not stated) | [SHARED] | 7:49 |
| TS-T11 | Ctrl+click inside a group | Ctrl+click picks the layer, plain click picks the group | n/a | [SHARED] | 8:16 |
| TS-T12 | Ctrl+Shift multi-select inside groups | Hold Ctrl+Shift, click several inner layers (e.g. two main shapes, several texts) | n/a | [SHARED] | 9:09, 50:45, 59:15 |
| TS-T13 | Stud tile fill | Paste stud image on shape → click image fill → mode Fill → Tile → scrub scale; Enter enters image edit mode to rescale | tile scale by eye; exit square used the 4x4 stud directly | [STUD] | 9:50-10:33, 27:52 |
| TS-T14 | Overlay blend for texture | Appearance → blend-mode dropdown (drop icon) → hover options → Overlay | Overlay | [SHARED] | 10:47-11:10 |
| TS-T15 | Inner brighter stroke | Top layer → + Stroke, Inside, brighter hue of the fill | 4 px (3 trial); later 5 on left buttons, 3 on some | [SHARED] | 11:31-12:10, 46:05 |
| TS-T16 | Equal stroke weight rule | Pick one outer weight (5) and keep outer outlines equal everywhere; text stroke 4 on title | 5 outer, 4 title | [SHARED] | 13:14-13:48 |
| TS-T17 | 3D text via hard shadow | Text stroke + Effects: Drop shadow blur 0, opacity 100, Y = stroke-like offset | 64 pt title: stroke 4, Y 4; small text: stroke 2, Y 2; left buttons: 3/3 | [SHARED] | 13:35-13:48, 42:06 |
| TS-T18 | Vectorize bitmap icon | Select icon → Actions (toolbar) → Plugins & widgets → search "vectorize" → Vectorize bitmap (Photopea inside) → OK → Ctrl+S in the plugin → drag vector out of the inserted group → fill black→white, stroke 3 Outside, set layer opacity 100 | stroke 3, shadow Y 3 | [SHARED] | 15:35-17:27 |
| TS-T19 | Better outline route | Add stroke in Photopea/Photoshop, export, import to Figma | n/a | [SHARED] | 17:39-17:53 |
| TS-T20 | Hard shadow on icons | + Effect Drop shadow, Y 3, blur 0, opacity 100 | Y 3 | [SHARED] | 17:17-17:27 |
| TS-T21 | Shift+Alt resize | Hold Shift + Alt, drag corner: proportional from centre | n/a | [SHARED] | 16:59, 40:48, 51:14 |
| TS-T22 | Group mask for card art | Put art (gem, stud, sunburst) inside a group whose first layer is the mask shape | n/a | [SHARED] | 20:39-21:04 |
| TS-T23 | Duplicate-and-recolour variants | Ctrl+D a finished component, Ctrl+click top/bottom layers, change gradient stops, inner stroke, bottom layer | per colour | [SHARED] | 22:10, 28:12 |
| TS-T24 | Scale tool vs Move | Bottom toolbar: Move → Scale; Scale keeps proportions of strokes/effects but multiplies stroke weight (5 became 7), fix after | stroke 5→7→5 | [SHARED] | 23:56-24:15, 41:08-42:00 |
| TS-T25 | Alt+drag both sides | On selected shapes, Alt+drag an edge: grows/shrinks both sides | n/a | [SHARED] | 24:43-24:57 |
| TS-T26 | Alt-hover padding | Select a layer, hold Alt, hover a neighbour: numbers show the distance | 30/30/30 final | [SHARED] | 31:25-31:56 |
| TS-T27 | Spacing readout | Select several layers; hover between them: gap in px shown; adjust until equal | 23→24 | [SHARED] | 30:16-30:29 |
| TS-T28 | Copy a fill | Ctrl+click the source layer, click an empty spot in the Fill row (copies the fill), Ctrl+C; select target, delete its fill, Ctrl+V | n/a | [SHARED] | 36:01-36:26, 42:28-42:47 |
| TS-T29 | Panel range select | Click top layer in the layers panel, Shift+click bottom layer, Ctrl+G | n/a | [SHARED] | 38:55-39:08, 56:13 |
| TS-T30 | Strip a duplicate | Remove icon; drag text out of group (empty group deletes itself) | n/a | [SHARED] | 34:39-34:45 |
| TS-T31 | Multi-size text | Ctrl+Shift-click all text layers, step the size together, Ctrl+click each and re-centre with the alignment tool | 30/28/27/25 final 25 | [SHARED] | 59:15-1:00:14 |
| TS-T32 | Stud count sizing | Resize block so its length is a whole number of studs | three studs | [STUD] | 57:17-57:23 |
| TS-T33 | Icon under text | Move icon below the text layer so the label overlaps it | n/a | [SHARED] | 47:50, 49:23 |
| TS-T34 | Sunburst overlay | Paste sunburst image into the group mask, resize/centre, blend Overlay | not stated | [SHARED] | 44:36-45:01 |
| TS-T35 | Round stroke join | Stroke settings: Join Sharp → Round (avoids spikes on bold text) | Round | [SHARED] | 52:49-52:56 |
| TS-T36 | Stress-test numbers | Type a nine-digit cash value to test width | 9 digits | [SHARED] | 51:43-53:08 |
| TS-T37 | Marquee select on locked frame | Lock the big frame, drag-select over buttons | n/a | [SHARED] | 58:42 |
| TS-T38 | Decor duplicates | Duplicate gem, rotate, lower opacity; second bigger copy at low opacity | not stated | [SHARED] | 21:16-21:44 |
| TS-T39 | Match lip pixel counts | Compare visible lip heights across buttons by counting px, resize bottom two layers | 7 px | [SHARED] | 1:00:32-1:00:59 |
| TS-T40 | Per-role colour rule | Duplicate and recolour (gradient, inner stroke, lower layer) per role | see section 5 | [STUD] | 28:12, 38:01, 46:28, 49:59 |

## 5. Style signature (what reads as "stud")

- Stud tile texture over the coloured top face, 4x4 studs per image, scaled down on small parts; Overlay blend so the studs read as soft highlights (9:50-11:10).
- Chunky 3D blocks: a lighter gradient top face + a darker bottom copy offset by a few px (lip about 7 px on small buttons) (4:48, 1:00:59).
- Thick outer outline in one weight, 5 px, flattened into one vector around the block silhouette (6:33); 4 px bright inner stroke on the top face (12:02).
- Colour = role, each button gets a gradient top face, a matching inner stroke and a darker lower layer in its role hue: header green, exit red, hero/offers orange, currency cards blue, sell red, base green, shop blue, rebirth pink/purple, index green, settings grey/white, plus button green (see sections 3.x).
- Type: bold white or green text with a thick outline and a hard offset shadow (stroke 2 to 4 px, shadow Y 2 to 4, blur 0, opacity 100); font name not stated.
- Deco: sunburst overlay behind icons, rotated translucent gem copies in the hero card (21:16, 44:36).
- Dark translucent black panel behind everything with a 5 px stroke, over a blurred scene (3:05, 2:07).
- Left-side buttons start as 70x70 squares (40:12); exit button is also a square (8:02).

## 6. HUD layout lessons

| Place | What the tutor shows | TS |
| --- | --- | --- |
| Top, above the shop frame | Three toggle buttons sell · base · shop, like another popular Roblox game | 34:04-39:14 |
| Left, vertical stack | Slow mode at the top, then shop, rebirth, index, settings; stack centred vertically with the alignment tool | 56:37, 58:56-59:09 |
| Bottom | `bottom` group: green cash number and a plus button to its right | 51:25-56:31 |
| Centre | Shop frame: header + exit on top, hero frame, three currency cards, equal padding | 33:12 |
| Grouping | Everything named, each cluster one group, align the group not the parts | 58:56 |
| Roblox top bar | Not mentioned. Inference: leave the top-left corner clear for the default Roblox menu; the board has no safe-area guides. |

Other lessons: text must not touch the button edges (reduce size and re-centre) (59:02); overly large numbers shrink by trimming digits (53:08); icon-under-text order (47:50).

## 7. Roblox conversion notes

| Effect | Native in Roblox UI | Or baked | Note |
| --- | --- | --- | --- |
| Translucent black panel + 5 px outside stroke | Frame BackgroundTransparency + UIStroke (Thickness 5, Border mode, outside) | n/a | inference: transparency value not stated |
| Gradient top face | UIGradient (Rotation 90 for top→bottom) | n/a | inference |
| Darker bottom layer offset down | Second Frame behind, offset in Y | n/a | inference |
| Flattened outer outline vector | Frame behind with UIStroke on a union-sized frame | bake into the image | inference |
| Inner stroke (Inside) | Inset child Frame with UIStroke | bake into the image | inference: UIStroke alone draws outside |
| Stud tile fill | ImageLabel, ScaleType Tile, TileSize | n/a | Figma Tile mode maps to Tile |
| Overlay blend | not available as a blend mode | Bake an overlay-processed texture, or tune the texture's own ImageTransparency | inference |
| Sunburst overlay | ImageLabel with ImageTransparency | Bake the overlay result | inference |
| Group mask | Frame with ClipsDescendants | n/a | inference: rectangular only |
| Gem icon, rotated copies | ImageLabel, Rotation, ImageTransparency | n/a | inference |
| Outlined icon (vectorized) | not native | Export as PNG with the stroke/shadow baked in | tutor: bitmap strokes need a vector or Photopea (15:09-15:28) |
| Text stroke | UIStroke on TextLabel (Contextual, Round join) | n/a | inference |
| Hard text drop shadow | duplicate black TextLabel offset in Y behind the real one | Bake into the image for fixed labels | inference |
| Layer blur on background | no UI blur; use a pre-blurred screenshot image | n/a | inference |
| Fixed px values (70x70, stroke 5) | Convert to Scale + UIAspectRatioConstraint; pair with UIScale | n/a | inference |

## 8. UX notes

Stated or implied by the tutor:
- Equal padding everywhere (30 px around cards, equal 24 px gaps) (30:16-33:12).
- Colour = role (see section 5) so players tell buttons apart quickly.
- Readable text: outlined, shadowed, centred, with room to the edge (59:02).
- Price display: Robux icon next to the price in the hero frame (17:10-18:41).
- Currency cards carry no description because "just money" is self-explanatory (23:41-23:48).
- Slow-mode toggle: label states the current state ("slow mode on") (58:11).
- Plus button beside the cash number as the shortcut to buy more currency (53:14).

Gaps a real shop still needs (all inference):
- States: hover, pressed, disabled, owned, selected; none shown.
- Real Robux price must come from the platform; price text here is static.
- Purchase pending, confirmed, failed, and insufficient funds feedback.
- Exit button focus order, gamepad focus ring, touch target size (small toggle and plus button).
- Localised text growth and long numbers; only a nine-digit test is shown.
- Contrast: white text on the pale grey/white settings button depends on its outline (50:14).
- Content per card: amounts and prices for cards 2 and 3 are not shown.
- Paid random items or limited-time offers would need extra disclosure (see `platform-policy`).

## 9. Mistakes and fixes shown

| Mistake | Fix | TS |
| --- | --- | --- |
| Header too big | Shrink both layers together | 5:26 |
| 3D lip too deep on header/exit | Drag top shapes taller at the bottom | 9:09-9:29 |
| Harsh stud texture | Overlay blend | 10:39-11:04 |
| Stroke 5 on title too strong | 4 | 13:48 |
| Stroke on a bitmap outlines the whole image box | Undo, vectorize, then stroke | 15:09-15:28 |
| Imported vector invisible (opacity 0) | Set layer opacity 100 | 16:48 |
| Menu moved by accident while editing icon | Undo / re-nudge | 17:34 |
| Ctrl+D slip on description | Undo, reselect, duplicate again | 19:46 |
| Locked vector blocked card resize | Unlock | 23:02 |
| Padding off by 1-2 px (23 vs 24; 32/30/30) | Move by 2 px, check with Alt | 30:29, 31:56 |
| Main frame padding 31 | Move up 1 px to 30 | 33:05 |
| Ctrl+click picked the stud layer | Open `main shape`, select top layer | 35:34 |
| Accidental whole-group move | Undo | 36:56 |
| Scale tool stretched stroke to 7 | Reset to 5 | 41:46 |
| Stroke position Center on cash text | Outside | 52:29 |
| Slow mode lip smaller than others | Resize bottom two layers until 7 px | 1:00:32 |
| Typo group name "currency pass" | Renamed `currency product` | 26:59 |

## 10. Gaps and ambiguities

- Font name: inaudible at 13:01; no font named later. Not stated.
- Main frame opacity, background blur, highlight opacity, gem copy opacity and rotation: not stated.
- Header gradient stop order (which stop on top) and exact colours: not stated, hex values never given.
- Header stud layer blend: Overlay at 11:04, but at 12:15 the tutor says he keeps "normal for now" on the header; unclear whether the stud layer or another blend.
- Hero frame, hero button and price were built off-footage (14:41-15:01). Sizes and the description text are not stated.
- Card spacing: 23 measured, 24 tried, tutor unsure it matters (30:29-30:42).
- Cash stroke: 3 or 4 mentioned; group fix at 55:54 lands on 3.
- Cash drop shadow Y: not stated at first; 3 at 56:00.
- "Make it 45" at 37:14: which dimension is not stated.
- Whether the cash number has commas: not stated.
- Top-button sizes and font size: not stated. Left buttons start 70x70, then are scaled up with the Scale tool (stroke 5 → 7, so ≈ 1.4×, ≈ 98 px; TS@41:08-41:46) and narrowed (TS@45:33).
- Text content of cards 2 and 3 and of the hero description: not stated.
- Position of the cash/plus group within the board: not stated.
