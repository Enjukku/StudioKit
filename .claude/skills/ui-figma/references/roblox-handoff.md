---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "J002; Roblox docs mirror (knowledge/external/roblox-creator-docs, upstream 7400643); ui-basics facts; research paper RP (R05-R07, R20)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Figma → Roblox handoff: what Roblox draws, what must be an image

Every Figma layer ends as one of three things in Roblox. Decide per layer **before** you polish, and write the decision in the spec's layer table.

| Mark | Meaning | Cost |
| --- | --- | --- |
| **N** native | Roblox draws it from properties: Frame/Text + UICorner, UIStroke, UIGradient, UIShadow, BackgroundTransparency | cheapest, recolourable, scales cleanly, text stays live |
| **B** baked | Exported PNG on an ImageLabel/ImageButton (often 9-slice) | texture memory; fixed colours; must be re-exported to change |
| **T** tiled | Small PNG repeated with `ScaleType = Tile` + `TileSize` (stud, half-tone, grain) | one small texture, any panel size |
| **L** library | An existing Roblox image id from the shared VFX library (`effect-assets.md`): sunbursts, glows, sparkles, rings, shines | no upload; shared with VFX; tint with `ImageColor3` |

## 1. Figma effect → Roblox (D = Roblox docs mirror, Y = `_api-reference/classes/`)

| Figma | Roblox | Mark | Note / evidence |
| --- | --- | --- | --- |
| Solid fill + opacity | `BackgroundColor3` + `BackgroundTransparency` (= 1 − opacity) | N | |
| Corner radius | `UICorner.CornerRadius` (UDim; per-corner live) | N | ui-basics U-08 |
| Linear gradient (any angle) | `UIGradient` Color + Transparency sequences, `Rotation` (Figma top→bottom = Rotation 90) | N | Radial, conical and elliptical gradients and the Scale / TileMode properties are **beta, not publishable** (DF 4846594; D ui/appearance-modifiers.md:79-201). Bake them |
| Stroke inside / center / outside | `UIStroke` `ApplyStrokeMode = Border`, `BorderStrokePosition` Inner / Center / Outer (+ `BorderOffset`) | N | Y/UIStroke.yaml:100-120; ui-basics facts says live, the class page still mentions the Improved UIStrokes beta for some properties: confirm in Studio before relying on Inner/Outer, fallback = nested Frame |
| Text stroke | `UIStroke` on the TextLabel (Contextual) | N | Never tween Thickness on text (ui-basics U-11) |
| Stroke round / miter join | `UIStroke.LineJoinMode` Round / Miter / Bevel | N | |
| Dashed stroke | none | B | bake the border as a 9-slice image |
| Two strokes on one shape (black line + white halo) | two sibling `UIStroke`s with **different** `ZIndex` (lower renders behind), e.g. black Thickness 3 ZIndex 2 + white Thickness 6 ZIndex 1 | N | D ui/appearance-modifiers.md:374-376 (same ZIndex = undefined order) |
| Drop shadow, hard (blur 0) = "3D" offset | duplicate object offset in Y, darker colour **or** `UIShadow` Offset, BlurRadius 0 | N | UIShadow live 2026-06-23, ≤ 100 on screen (U-08) |
| Drop shadow, soft / outer glow (X0 Y0, blur) | `UIShadow` BlurRadius, Spread, Color, Transparency | N | glow = coloured shadow at offset 0 |
| Text drop shadow | duplicate TextLabel offset down (the tutorials' "3D text") | N | UIShadow text mode is **beta** (DF 4934553) |
| Inner shadow / inner glow | none live | B | UIShadow Inset is beta. Bake, or fake with a gradient overlay frame |
| Layer blur / background blur | none for UI | B | bake into the image; never rely on live blur |
| Blend modes (overlay, soft light, color dodge, multiply…) | **none: Roblox UI composites Normal only** | B | TP (pixel tutor states it); D has no blend property on GuiObjects. **Bake method:** (1) recolourable controls: rebuild the gloss / highlight / half-tone as Normal white (or black) at 15-25 % and export it alone as a transparent overlay PNG that sits on the native face (one overlay per size, any colour); (2) when recolour is not needed: export face + gloss together per colour. An Overlay / Soft light layer exported alone over transparency does not work |
| Group mask / clipping mask | `ClipsDescendants` (rectangles, rotation OK) or `CanvasGroup` (clips to UICorner) | N / B | CanvasGroup costs texture memory; keep its size static (U-11). Complex masked highlights: bake |
| Image fill, Fill/Fit | `ImageLabel.ScaleType` Stretch/Crop/Fit | B | |
| Image fill, Tile | `ScaleType = Tile`, `TileSize` (UDim2) | T | stud texture, half-tones |
| Texture "overlay" on a coloured panel | Normal-blend tile at low opacity (`ImageTransparency`) **or** bake | T / B | check the tile still reads at phone size |
| Rotated element | `Rotation` | N | rotated clipping is default (U-09) |
| Canvas values after fitting | the builders' one outer `UIScale` scales children **including UIStroke and UICorner**, so canvas stroke and radius values stay in proportion; keep `UIStroke.StrokeSizingMode = FixedSize` (default) under a UIScale | N | D ui/size-modifiers.md:17; Y/UIStroke.yaml:217-250 |
| Flattened vector outline around face + lip (3D button silhouette) | a backing Frame (same UICorner) that spans face + lip, with the Outer UIStroke; face and lip Frames sit inside it. Custom shapes: one baked silhouette PNG | N / B | prefer N when the shape is a rounded rect |
| Pen-tool custom silhouette (anime header, pixel ornament) | 9-slice PNG with ornaments in the corners | B | ornament must sit inside the slice corners |
| Pixel art (1 px lines) | PNG at 1 art px + `ResampleMode = Pixelated`; when the fit scale is not an integer, pixel widths vary slightly: check on a phone (`ui-style-pixel` §3) | B | Y/ImageLabel.yaml:209-221 (Pixelated keeps hard pixel edges) |
| Text | TextLabel, `FontFace`, `AutomaticSize`/`TextWrapped` | N | **never bake changeable text, prices or counts into art** (RP R16, R22) |

**Rule of thumb.** Shapes, strokes, linear gradients, corners and shadows: native. Blend modes, inner shadows, blurs, dashes, radial gradients, textures and custom silhouettes: baked. A design that is 80 % native is cheap to restyle and recolour per rarity; say the native/baked ratio in the spec.

## 2. Fonts (both sides must have them)

Built-in Roblox families (D `rbxasset://fonts/families/*.json`, mirror 7400643) that Figma also has as Google Fonts: **Fredoka One**, **Montserrat**, **Luckiest Guy**, **Bangers**, **Press Start 2P**, **Nunito**, **Oswald**, **Roboto**, **Ubuntu**, **Titillium Web**, **Josefin Sans**, **Permanent Marker**, **Creepster**, **Denk One**, **Michroma**, **Jura**, **Sarpanch**, **Merriweather**. Use `FontFace` (Font.fromName / family asset), not the legacy Font enum (U-04).

- **Check the exact name in Figma** with `listAvailableFontsAsync` before building. Google Fonts replaced "Fredoka One" with the variable family "Fredoka" (2022); if Figma lists only "Fredoka", use Fredoka **Bold** / **SemiBold** for the cartoon look and keep Roblox's `FredokaOne` family; note the substitution and compare the two renders once.
- Pick fonts from this list. A font Roblox lacks (e.g. Alagard, used in the pixel tutorial) must be uploaded as a custom font if the game allows it, or replaced. Record which.
- Weight: Figma "Extra Bold" ↔ `Enum.FontWeight.ExtraBold`; check the family has it in Roblox.

## 3. Export

| What | How | Rule |
| --- | --- | --- |
| Canvas | Design at **1920 × 1080** (TC, TS, TP; TA not stated) | the spec states the canvas; builders fit with one outer `UIScale` (U-02) |
| Scale | Default: export baked art at **1×** of its on-screen size on the 1920 × 1080 canvas. If 1440p / 4K PC or console screens are supported, export icons and hero art at 1.5-2× (PROPOSAL) and check sharpness on the largest screen | memory follows pixel count: 1024² = 4× the memory of 512² (RP R07); ≤ 512² unless it covers a big area; small icons usually ≤ 256² (R06-R07): the memory rule wins over sharpness |
| 9-slice | Export the panel at the smallest size that holds the corner ornaments; give `SliceCenter` (the centre rectangle, in image px) and `SliceScale` if the corners must show smaller or larger than the exported pixels | corners never stretch; edges stretch on one axis; centre stretches both (R05); `SliceScale` scales the edges (Y/ImageLabel.yaml:299) |
| Sprite sheet | Many small icons of one family → one sheet; give `ImageRectOffset` / `ImageRectSize` per icon | loads faster (ui-basics facts.md, images row); unused area still costs memory (R07) |
| Alpha | PNG with transparency; keep a 2 px clear margin so strokes are not cut | |
| Pixel art | 1 art px per pixel (1/S of the canvas size, `ui-style-pixel` §3), no smoothing | `ResampleMode = Pixelated` |
| Same asset reused | one upload, one id, many uses | R07 |
| Animated GIF | not animated as a GUI image | R20; use a flipbook sprite sheet |
| Via MCP | `get_screenshot(fileKey, nodeId, maxDimension)` returns a PNG url (curl it to `content/ui/<screen-id>/export/`; check alpha after download); for exact scale, ask the owner to export from Figma | MCP renders at the requested longest edge; check pixel size after download |

## 4. Handoff package (per screen, `content/ui/<screen-id>/`)
- `spec.md`: purpose, decision record, states, layer table (name, size, position, N/B/T, colours as hex, stroke, radius, font + size, ZIndex order), spacing, 9-slice insets, motion records, open questions, PROPOSAL list.
- Figma link (file + node ids) and a screenshot per state and per device class.
- `export/` PNGs named `<screen-id>_<part>[_state].png`; `refs/` (generated images + `prompts.md`); `figma-ids.json` (node and variable id ledger).
- Changeable text, numbers and prices listed as live text fields with their data source, never in art.
