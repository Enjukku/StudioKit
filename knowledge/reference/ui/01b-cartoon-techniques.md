---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "owner-supplied transcript 'Cartoon Guide.txt' (UI Genesis, YouTube), J002"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

# Cartoon pet-inventory UI in Figma (UI Genesis, tutor Hamuri) (continued)

First part (source card, conventions, earlier sections): [[reference/ui/01a-cartoon-recipes]]. Citation rules are stated there.

## 4. Technique catalogue

Tags: [SHARED] works for any of cartoon/stud/anime/pixel; [CARTOON] reads as cartoon specifically.

| id | technique | exact steps | values | tag | TC |
| --- | --- | --- | --- | --- | --- |
| TC-T01 | 3D depth lip | Select face, Ctrl+D, with the bottom copy: arrow-down a couple of times (or Shift+Down for bigger), Fill type Solid, darker shade of the face color | offset few px (not stated); lip is solid | [SHARED] | TC@9:58-10:10, TC@20:34-20:50, TC@32:10 |
| TC-T02 | Vertical gradient face | Fill -> Gradient. Default direction can be left-right: click rotate-gradient or drag handle (hover just beside the dot) to make it top-to-bottom. Click stops to set top light color and bottom darker color | 2 stops, top lighter | [SHARED] | TC@9:18-9:44, TC@19:48-20:23 |
| TC-T03 | Outline around a multi-layer shape | Select face + lip, Ctrl+D, right-click Flatten, drag the vector below the originals, add stroke Outside, delete the fill (leave only stroke); undo any trial moves | 3 px, black | [SHARED] | TC@10:16-11:09, TC@20:58-21:16 |
| TC-T04 | Double outline (black + white ring) | Duplicate the outline vector, drag below, rename `white stroke`, color white, weight 3 -> 6 so the white ring reads as a halo around the black line. Figma double strokes on one layer are not supported (colors blend), so two layers | black 3, white 6 | [SHARED] | TC@3:35-4:28, TC@11:16-11:45 |
| TC-T05 | Stroke position change | Stroke section: Inside / Center / Outside; Outside makes the stroke look thicker because it adds to size | Outside for outlines, Inside for inner lines | [SHARED] | TC@4:10-4:22 |
| TC-T06 | Dashed stroke | Stroke settings icon beside weight -> Style Dashed. Used on the panel face for a stitched look | dash length not stated | [SHARED] (visual is cartoon-friendly) | TC@4:42-4:55 |
| TC-T07 | Inner shadow on a flat input field | Effects +, switch Drop shadow to Inner shadow, set Y 4 -> 0, bump blur, opacity 25 -> 30% | Y0, 30% | [SHARED] | TC@5:45-6:48 |
| TC-T08 | Drop shadow "floating" | Effects +, Y 4 -> 0 (so glow-like around all sides), more blur, tune opacity. Put it on the lowest outline layer | not stated | [SHARED] | TC@11:57-12:40, TC@35:13-35:37 |
| TC-T09 | Group-mask for highlights and textures | Ctrl+D the face, Ctrl+G the copy, right-click the shape inside -> Use as mask; drop anything into the group: it clips to the silhouette | - | [SHARED] | TC@12:48-13:17 |
| TC-T10 | Highlight bars | Inside mask: 2 white rotated rectangles of different size, spaced apart; blend Soft light or Overlay | 2 bars | [CARTOON] | TC@13:25-14:51, TC@21:36-22:07 |
| TC-T11 | Blend mode choice | Appearance panel water-drop icon, hover each mode to preview. Soft light and overlay both used; soft light softer, overlay stronger | Soft light for card/header, Overlay for Equip button | [SHARED] | TC@14:24-14:51, TC@22:07 |
| TC-T12 | Halftone dots texture | Copy a dotted halftone image from a UI-resource site, paste inside the mask group, Alt+Shift resize, rotate, blend soft light or overlay; reuse by Ctrl+C/V across masks; flip horizontally/vertically with property buttons for opposite corners | corners only | [CARTOON] | TC@14:51-15:58, TC@22:15-23:08, TC@34:29 |
| TC-T13 | Selection colors recolor | Select a group, Properties -> Selection colors lists every fill/stroke; edit the entries to recolor the whole group (rarity swaps) | gold -> purple | [SHARED] | TC@35:51-36:49 |
| TC-T14 | Copy/paste a property | Click empty space in a property row (e.g. Stroke), Ctrl+C, select target, Ctrl+V. Color/style come along but weight did not; re-enter it | weight re-set to 4 | [SHARED] | TC@39:07-39:43 |
| TC-T15 | Align multiple frames | Select first card, Shift-click last, use Align vertical center in the Position row | fixes 1 px drift | [SHARED] | TC@40:29-40:54 |
| TC-T16 | Align text inside a shape | Select text first, Shift-click the shape (target), press Align vertical/horizontal center | - | [SHARED] | TC@7:43-8:02 |
| TC-T17 | Padding check with Alt | Select object, hold Alt, hover target to see px gaps; Alt + arrow keys to nudge; grow the container 1 px if a side is off | 9 top / 9 left, bottom fixed by +1 px | [SHARED] | TC@8:09-8:40 |
| TC-T18 | Grid gaps via Layers | Select all cards in Layers, hover: dashes with numbers show the gap. Adjust all at once (start 41) | 41 -> bigger | [SHARED] | TC@18:02-18:21 |
| TC-T19 | Repeat-duplicate | Ctrl+D, Shift+arrow to place one copy; the next Ctrl+D repeats the same offset | - | [SHARED] | TC@17:44-17:56, TC@38:06-38:19 |
| TC-T20 | 3D text | Ctrl+D the text, drag the copy below in Layers, nudge down a few px; stronger offset = stronger 3D; make the copy black for max contrast. Both with strokes | stroke 3; copy black | [CARTOON] | TC@23:34-23:40, TC@24:48-24:59 |
| TC-T21 | Text stroke | Add stroke to white text for readable cartoon type | 3 px; black | [CARTOON] | TC@16:27-16:34, TC@31:16, TC@27:22 |
| TC-T22 | Inner "rim" stroke on face | Top face, stroke Inside, 4 px, brighter tint of the face color (yellow, purple, green, pink, red, lighter grey) | 4 | [CARTOON] | TC@37:30-39:58 |
| TC-T23 | Gradient + 3D + outline + highlights stack | Combined recipe, same on every component (see section 3 note) | radius 10 | [CARTOON] | TC@19:39-23:14 |
| TC-T24 | Variant by duplication | Duplicate the finished component, recolor gradient stops and lip, retype text; resizing a variant needs flattened outline vectors remade first (flattened vectors do not scale well) | - | [SHARED] | TC@23:47-26:04 |
| TC-T25 | Alt-drag duplicate | Alt + drag copies an object (used for highlights and text) | - | [SHARED] | TC@16:34, TC@33:48 |
| TC-T26 | Shift-square | Hold Shift while drawing for equal sides | - | [SHARED] | TC@8:59, TC@29:11 |
| TC-T27 | Opacity to soften | Lower the layer opacity of the highlights when they look too bright on pale fills | not stated | [SHARED] | TC@28:33 |

## 5. Style signature (what reads as "cartoon")

- Rounded rectangles only; one radius (10) reused on panel, search bar, buttons, header, close button.
- Thick consistent outline on every control: 3 px black outside stroke on cards, buttons, close, header; text strokes 3 px.
- Light-to-dark vertical gradient on every face (bright top, darker bottom), plus a flat, darker, offset lip for chunky 3D depth.
- Outline is drawn around the combined face + lip, so the silhouette includes the lip.
- Panel uses white outer ring, dashed blue inner stroke, no thick black outline.
- Inner "rim" stroke (4 px, brighter tint of the face color) on card and button faces.
- Soft-light/overlay white highlight bars and halftone dots clipped into the face; applied to every colored item, positioned in corners.
- Rarity expressed by whole-card color swap (gold, purple, green), not by shape changes.
- Type: Fredoka One (rounded display), white fill, dark outline, offset 3D copy.
- Floating cards: soft drop shadow on a white outer ring; flat search bar: inner shadow.
- Flat, saturated, high-contrast palette; red = destructive, green = positive, grey = utility, blue = header, gold/purple = rare.

## 6. Roblox conversion notes

Source for engine facts: local docs mirror `knowledge/external/roblox-creator-docs/ui/ui-stroke.md`, `ui-gradient.md`, `ui-shadows-and-individual-corners.md`. Everything that is a conversion opinion is marked "inference" (the transcript says nothing about Roblox).

| Effect in video | Native in Roblox? | Notes |
| --- | --- | --- |
| Corner radius 10 | Yes, UICorner (px via Offset) | Per-corner radii are live (2026-06-23). Figma 10 px on 1920x1080 maps to about 10 px in Offset on the same frame; scale with UIScale (inference) |
| Gradient fill top-to-bottom | Yes, UIGradient (Rotation 90 for vertical; ColorSequence, 2 stops) | Gradient does not cascade to children; each face needs its own. Radial/conical types are beta (not publishable) |
| Solid lip (duplicate down, darker) | Yes, a second Frame behind with UICorner, offset down by the same px | Inference |
| Outside stroke around face + lip silhouette | Partial | UIStroke has BorderStrokePosition (Center/Inner/Outer) in the improved-strokes beta; the outline of a union of two shapes is not a single stroke, so use a third, larger backing frame in black with UICorner or bake the silhouette to an image (inference) |
| Double stroke (black + white ring) | Yes | Two UIStroke instances on one parent, distinct ZIndex (undefined order if equal), or two nested frames (inference) |
| Inside / Outside stroke position | Yes with BorderStrokePosition Inner/Outer (check beta gating); Center is the default | Check "Improved UIStrokes" beta before relying on it |
| Dashed stroke | No | No dash property; bake into an image or fake with a repeating tiled image (inference) |
| Drop shadow (Y 0, blur) | Yes, UIShadow (live since 2026-06-23): BlurRadius, Offset, Spread, Color, Transparency | Offset 0 for a glow-like ring |
| Inner shadow | No (live). UIShadow `Inset` is Studio Beta, not publishable | Bake into an image, or a darker top gradient strip (inference) |
| Blend modes soft light / overlay | No | Roblox UI has no blend modes. Bake the highlights and textures into the exported button image, or use semi-transparent white shapes in normal mode (inference) |
| Group-mask clipping of highlights | No native mask for arbitrary shapes | Bake into image; or ClipsDescendants (rectangular clip only; rounded clip needs an image) (inference) |
| Halftone dots texture | Via ImageLabel | Image with transparency. Tinting by ImageColor3 only; no blend mode |
| Text stroke | Yes, UIStroke (Contextual) around glyphs | Avoid tweening Thickness on text (performance warning in docs) |
| 3D text (duplicate lowered) | Yes, a second TextLabel offset down in darker color, or UIShadow text mode (beta) | Inference |
| Flatten + stroke vector | N/A | Export the result as a 9-slice image when many layered features are needed (inference) |
| Selection-colors recolor | N/A in-game | Recolor by data (rarity table drives gradient stops) (inference) |

## 7. UX notes (tutor, then gaps)

Tutor mentions or implies:
- Equal padding matters: text inside the search bar is checked to 9 px top and left, with 1 px correction (TC@8:09-8:40).
- Consistent card spacing; fill the screen; cards aligned on a common line (TC@18:02-18:21, TC@40:29-40:54).
- Color-coded semantics: green for equip, red for delete, grey for filter, red for close (TC@19:48, TC@25:11, TC@27:42, TC@29:35).
- Rarity read by card color, as the first visible cue (TC@35:45).
- Button text centered in its shape (TC@24:22-24:42).
- Floating depth separates cards from the panel (TC@11:50-11:57).
- Highlights sit in corners so the center stays clear for the icon and text (TC@22:34).

UX gaps (what a real game screen still needs; inference, nothing in the video):
- No hover, pressed, disabled, selected or equipped states for any card or button.
- No empty-inventory view, loading or error state.
- No scroll area or paging; fixed 3 rows (no overflow behavior).
- No long-name handling (truncate or autoscale text), no count/quantity badge, no lock icon.
- No rarity label beyond color (color-blind safe cue: add a shape or icon).
- Search bar has no clear button, focus or filled state; no icon.
- No tooltip, detail panel or confirmation for Delete Mode (destructive action needs a confirm).
- Text size is not tied to a minimum readable size for phones (48 px on a 1920x1080 frame is for the search bar only; card text sizes not stated).
- Close button position and hit size for touch not stated.
- No gamepad focus state.

## 8. Mistakes and fixes shown in the video

| Mistake | Fix | TC |
| --- | --- | --- |
| Default shadow Y = 4 makes the inner shadow look off-center | Set Y to 0 (done three times: inner shadow, drop shadow, panel shadow) | TC@6:05-6:17, TC@12:11-12:16, TC@35:26 |
| Search text padding uneven (9 / 8 / 15) | Alt-check and nudge text, then drag rectangle bottom edge 1 px | TC@8:09-8:40 |
| Trial outline: dragging the stroke vector out shows the fill still there | Remove the fill from the vector, undo the drag with Ctrl+Z | TC@10:56-11:04 |
| Everything white on white, shadow invisible | Temporarily color the strokes to see the effect, then return to white | TC@12:34-12:40 |
| Title text behind everything | Drag the text layer to the top of the Layers list | TC@16:11-16:16 |
| A second text appeared when duplicating the button | Delete the extra text layer | TC@24:04-24:09 |
| 3D text copy shows white | Set the copy's fill to black | TC@24:54 |
| Flattened vectors do not resize properly | Delete the outline vector and text before resizing the filter button, remake the outline by Ctrl+D, Flatten, outside stroke | TC@25:51-27:16 |
| Stroke pasted via Ctrl+V keeps the color but the weight is not carried | Re-enter weight 4 | TC@39:25-39:32 |
| Card duplicated and accidentally moved down 1 px | Select all cards (click first, Shift-click last), Align vertical center in the Position row | TC@40:22-40:54 |
| Grid spacing one pixel out | Accepted at TC@18:33; the Align fix at the end resolves the row alignment | TC@18:27-18:33 |
| Gap of 41 px too tight to fill the panel | Increase "a bit" | TC@18:13-18:21 |

## 9. Gaps and ambiguities

- No color is given as hex/RGB. Every color is a word (gold, darker orange, bright green, bluish, pinkish...).
- Not stated: card and button sizes, panel size, number of columns and rows (3 rows shown; cards per row not stated), final grid gap, shadow blur/opacity on panel and card, 3D lip offset px, text sizes other than the search 48, stroke weights on several texts and the close button, dash lengths, highlight bar sizes/angles, halftone scale.
- "Fidoka / Foca one" is speech-to-text for Fredoka One (inference from spelling and the font's cartoon use).
- "eye resources" (TC@15:05) is garbled; the context is a UI-resource site with icons and textures. Site name not usable.
- "D shortcut for text" (TC@16:05) conflicts with T used elsewhere (TC@6:55, TC@23:14); treated as a slip.
- "soft color" (TC@34:06-34:13) = Soft light blend mode (inference; "like always").
- "Three frames is good" (TC@21:10) = stroke weight 3 (inference).
- "pit frame" = pet frame (TC@17:44).
- "light outline" (TC@35:19) = `white outline` layer (inference).
- "clothes" (TC@29:40) = "close" (the button purpose).
- TC@28:15-28:28: speech is garbled and silent; the exact fix for the grey Filter highlights is inaudible. Possible blend-mode change or recolor (inference).
- TC@24:14-24:42, TC@24:33-24:42: only partial speech; the text-centering step is shown, not narrated.
- TC@36:20-36:32: "change the orange to a darker purple" appears after the top stop was already changed; which Selection-colors entries (the gradient entry vs two plain color entries) map to which stop is not clear.
- Green card tier name, and which rows use which rarity, are not stated.
- The red stroke in TC@39:37 is attributed to "the red button we're about to do" (Delete Mode); the delete button and rarity tier assignments are inferred.
- Layer stacks in section 3 are reconstructed from described drag operations; the tutor never shows a final layers panel.
- Icon (dog) and halftone images are external assets; no source file or license information given.
