---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "owner-supplied transcript 'PixleArt Guide.txt' (YouTube), J002"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

# Pixel rogue-like HUD in Photoshop (Kakuza): extraction for the pixel skill book

Conventions. `TP@mm:ss` = source timestamp line that sits just before the statement (the transcript prints each timestamp above its text, so a value may fall a few seconds after the cited stamp). `PROPOSAL` = Figma or Roblox mapping the tutor did not say; `inference` = my reasoning, not stated. "not stated" = the tutor gave no number. Owner decision J002-D5: pixel style is made in Figma with the pixel grid on and snap to pixel grid at 1 px. Tags: [PIXEL] = specific to the pixel look; [SHARED] = reusable in other style books.

## 1. Source card

| Key | Value |
| --- | --- |
| Built | Pixel rogue-like HUD, 1920 x 1080 canvas: presentation background, 5-slot toolbar, inventory (frame, title bar, search bar, item container), leaderstats list, party panel (4 player tabs), close button |
| Tool | Photoshop (layer styles, pencil tool, symmetry, selection contract, motion blur). Canvas 1920 x 1080 px, 72 resolution (TP@0:13-0:20). Tutor says Photopea has a pencil too (TP@5:51) |
| Genre refs named | Rogue Lineage, Deepwoken-style toolbars (spelled "Deep Lo" in the transcript) (TP@6:56) |
| Narrated range | 0:00 to about 1:02:35 (TP@1:02:35 "first half" ends). Chapters: Background 0:45, Pencil tool 5:46, Toolbar 6:56, Inventory frame 17:11, Leaderstats 35:03, Party 42:09, Close button 56:02 |
| Not narrated | 1:03:15 to 1:36:44: music only, section titles only (section 8). The tutor says the second UI uses the same techniques plus a few outer/inner glows and drop shadows, a drawing tablet, and mostly strokes plus the pencil (TP@1:02:40-1:03:02) |
| Trust | Practice, one tutor; narrated to about 1:02:35, music-only after. The tutor calls it a beginner's guide (TP@9:49), values are by eye, no pixel sizes for most shapes, and several values are garbled in the auto-transcript (section 10). Treat numbers as starting values, not specs |
| Tutor claim to discount | "Pixel UIs are not made in Figma because it is vector-only; only Photoshop/Photopea have the pencil" (TP@5:51). The owner chose Figma anyway (J002-D5); the proposals below show how to cover the gap and where it stays weak |
| Ignored | Promo and Discord link at 1:03:02 |

## 2. Presentation background (not part of the game UI)

Purpose: the tutor says pixel UI designers show their work on a dark, grungy backdrop (TP@0:33). It is a presentation board only; nothing here ships to Roblox. Keep it for mock-up screens so the HUD is judged on a dark scene. [SHARED]

| # | Step | Value | TP |
| --- | --- | --- | --- |
| 1 | New file, background to layer | 1920 x 1080 px, resolution 72; right-click background, Layer from Background | 0:13-0:26 |
| 2 | Paste a grunge texture (web image search "grunge texture") into a new layer | texture choice by eye | 0:39-0:51 |
| 3 | Duplicate (Ctrl J), move up, flip vertical; merge both. Gives a mirrored, seamless edge | flip V | 0:58-1:05 |
| 4 | Scale up the merged layer; duplicate, flip horizontal, butt it against the edge, merge again | flip H; scale "play with values" | 1:05-1:31 |
| 5 | Centre, zoom out, enlarge; Ctrl-drag a corner to distort, then warp for a less regular look | amounts not stated | 1:31-2:04 |
| 6 | Filter > Sharpen once, set blend mode Normal to Overlay | opacity "30, maybe 50" | 2:04-2:18 |
| 7 | Vignette: new layer; elliptical marquee, fill any colour, deselect, centre, enlarge, leave gaps at edges; Ctrl-click the layer thumbnail to load it as a selection; Ctrl+Shift+I inverts; hide the helper; new layer; black fill of the inverse | selection leaves gaps at the edges | 2:18-3:03 |
| 8 | Filter > Blur > Gaussian Blur on the black fill, then lower layer opacity | blur radius not stated ("a value I like"); opacity about 60 | 3:03-3:22 |
| 9 | Texture too flat: Adjustments > Contrast up, brightness up | brightness/contrast "from 30, keep 40" (garbled; ambiguous) | 3:22-3:34 |
| 10 | Duplicate the texture, add a layer mask, erase part so the repeat is not obvious; apply mask; set both layers to Normal, merge, set Overlay again | not stated | 3:40-4:17 |
| 11 | Second web texture, new layer under the vignette, scale up, Sharpen, Overlay, Ctrl I to invert | opacity about 30 | 4:23-5:03 |
| 12 | Merge all into one background. Crop to canvas: Ctrl+A, lasso tool, right-click, Layer via Cut; delete the old oversized layer | n/a | 5:15-5:46 |

Figma PROPOSAL (not a Photoshop port): one 1920 x 1080 frame, two texture image fills, each set to Overlay blend (Figma has Overlay, Multiply, etc.) at 30-50% and 30%, flip with Shift+H / Shift+V on duplicates, vignette as a radial gradient fill (black edges to transparent centre) on a full-frame rectangle at about 60%, frame clips the overflow so no cut step is needed. Roblox: not shipped; board only.

## 3. Core pixel method

| Method | What the tutor does | Value | TP | Tag |
| --- | --- | --- | --- | --- |
| Pencil, not brush | Right-click the brush tool, choose Pencil. Pencil gives hard pixel steps; brush at 100 hardness still looks soft when zoomed. Brush-texture tricks exist but "not viable" | 1 px (set explicitly) | 5:46-6:44, 18:00 | [PIXEL] |
| 2 px black stroke as outline | Layer Style > Stroke on the drawing layer. Whatever is drawn gets a black 2 px edge automatically, so the pencil only draws the light inner lines. Used on frames, text, icons, bars; copied with Copy/Paste Layer Style | size 2, colour black; position not stated | 7:36-7:47, 12:43 | [PIXEL] |
| Shift-click straight lines | Click one point, hold Shift, click the next: perfect straight lines around a box | n/a | 7:47-8:04 | [PIXEL] |
| Symmetry | Symmetry button while pencil/brush is active. Dual axis draws on all four quadrants around the canvas centre (centre the object first). Vertical used for the title-bar ornament; horizontal-only for the player icon; turn it off to edit one side | dual axis / vertical / horizontal | 8:28-8:49, 24:19-24:30, 45:57-46:11 | [PIXEL] |
| Recover when symmetry was skipped | Copy the drawn quadrant with a marquee, paste, black gradient fill, ruler at centre, erase the box so only the corner remains, Ctrl J + flip horizontal, select both, Ctrl J + flip vertical, drag into place; merge black parts; Copy Layer Style, Clear Layer Style on all, merge, Paste Layer Style (removes the double stroke at seams) | 4 corners from 1 | 19:30-21:56 | [PIXEL] |
| Contract 1 px outline box | Draw a filled rectangle (white), Ctrl-click layer, Select > Modify > Contract 1 px, Delete. Leaves an exact 1 px box outline. Also used on circle and health bar | 1 px | 22:35-22:47, 44:06-44:19, 49:04-49:22 | [PIXEL] |
| Sharpen to keep edges crisp | Filter > Sharpen after blur, mask fades or resize (once on the faded leaderboard; twice on resized party tab elements). Duplicating the contracted circle layer also made it "very sharp" | 1-2 passes | 36:30-36:38, 44:19-44:28, 53:51-54:09 | [PIXEL] |
| Motion blur (angle 0) for fading bars | Black rectangle, Filter > Blur > Motion Blur angle 0 gives a bar whose ends fade out; used behind toolbar, leaderstats, party name strips, close button. Add Gaussian blur if too edgy | angle 0; distance not stated | 15:42-16:15 | [SHARED] |
| Erase ornaments inward | Draw a shape on the frame edge, then erase the inside of it so only a thin contour remains; refill gaps with the panel's black so it merges | n/a | 18:31-19:25 | [PIXEL] |
| Corner-only ornaments on main frames | Do not decorate the whole edge; keep ornaments in corners so attention stays on the content | n/a | 18:14-18:25 | [PIXEL] |
| Soft mask for fades | On bigger panels, a layer mask with a soft round brush (not the pencil, hardness off, black) fades an edge. Sharpen afterwards | n/a | 36:07-36:38 | [SHARED] |
| Check from a distance | Zoom out (Ctrl -) to judge read at game scale after detailing at high zoom | n/a | 9:37-9:49, 10:30 | [SHARED] |

## 4. Component recipes

Common style (used in every recipe): fills are black at partial opacity; lines are 1 px light pencil lines with the 2 px black stroke style; text uses the same stroke style; fades use motion-blur strips or gradient overlay. Colours of lines are "white" where stated; other colours not stated.

### 4.1 Toolbar (5 slots) (TP@6:56-17:04, 1:00:45-1:01:03)

| Part | Recipe | Value | TP |
| --- | --- | --- | --- |
| Base | Square marquee (Shift), paint-bucket fill black, deselect, Ctrl+A, centre with Move tool, free transform from centre (Alt) to resize | size not stated | 7:02-7:30 |
| Drawing layers | 3 layers: base fill, a stroked layer with pencil lines, a top layer for extra shapes. Stroke layer: Layer Style Stroke 2 px black; pencil 1 px; shift-click box outline; dual-axis symmetry for ornaments | 3 layers | 7:36-9:37 |
| Depth styles tried | Gradient Overlay: adjust scale, darker, preset colour; Inner Shadow black, Multiply, opacity 100, distance only, global light off, angle -90. Inner shadow was then turned off; final gradient overlay opacity 46 | gradient 46; inner shadow dropped | 10:07-11:26 |
| Number label | Free space by painting black (symmetry off). Text tool, font Alagard. Typed a test digit at size 24, stroke 2 px, then size 28 or 30 "for readability". Labels 1 to 5 | 24 then 28-30; stroke 2 | 11:44-12:55, 14:01-14:10 |
| 5 slots | Duplicate the slot until it touches the next, then nudge right with the arrow key 5 times: 5 px gap. Group, Ctrl+A, centre on screen | gap 5 px | 13:06-13:56 |
| More depth | Gradient overlay on the slot box: increase scale, reverse, opacity 15; remove the stroke from the lowest layer; Copy Layer Style, select all slot layers (Ctrl+Shift), Paste Layer Style | opacity 15 | 14:23-15:13 |
| Backing strip | Toolbar blends into background. New layer, black rectangle, made smaller and narrower, Motion Blur angle 0, layer opacity 50 (key 5), optional Gaussian blur | opacity 50; blur sizes not stated | 15:19-16:15 |
| Glow | Gradient overlay lowered to 10 on that layer; Outer Glow blend Normal (Roblox only supports Normal), size and range increased, very soft, opacity 10; copied to all slots. Tutor: subtle in Photoshop, "definitely" visible in Roblox | glow opacity 10; gradient 10 | 16:21-16:59 |
| Whole toolbar | Select all toolbar layers, group opacity 70 (at 100 it was too dark, now "transparent") | 70% | 1:00:45-1:01:09 |

Figma PROPOSAL: slot = component (base rect + 1 px inner highlight rects + 2 px outside stroke), 5 instances in auto layout with spacing 5 and integer sizes; label = text with pixel font and 2 px outside stroke; gradient overlay = linear gradient fill at 15%; outer glow = drop shadow, 0 offset, blur large, 10% black (Figma has no spread-tuned "glow" with Normal mode, drop shadow is closest); group at 70% opacity. Roblox (inference): slot background Frame with BackgroundTransparency 0.3; outline UIStroke Thickness 2; corner ornaments baked as ImageLabel with ResampleMode Pixelated; glow baked soft image (bilinear, not Pixelated) or UIGradient/transparent frame.

### 4.2 Inventory frame (TP@17:11-25:40, 1:00:15-1:00:39)

| Part | Recipe | Value | TP |
| --- | --- | --- | --- |
| Body | Big rectangle, black fill, centred; layer opacity 60 | 60% | 17:17-17:47 |
| Outline layer | New layer with Stroke 2 px black; pencil size 1 | 2 px / 1 px | 17:47-18:00 |
| Ornament | Corner-only, drawn by hand, inside erased, gaps filled black. Rebuilt as 4 mirrored corners (section 3 recovery) | shape by eye | 18:14-21:56 |
| Title bar | New layer, paste layer style, white 1 px rectangle via fill + contract 1 px + delete; place near top; fill inside, colour to white, opacity 20. Text INVENTORY in capitals, white, centred, tried several fonts, size "bigger" (not stated); same layer style | white 20%; size not stated | 22:01-23:54 |
| Title ornament | New layer, white pencil, layer style pasted, vertical symmetry only; small "glitching away" marks at left/right ends so the bar seems to fade; layer mask on the white rectangle gives a faint shine so the eye reads detail that is not there | not stated | 24:06-26:15 |
| Frame shine | Two white rectangles rotated: one with opacity 7; one masked, bottom-left erased with a soft brush: glassy look | 7% | 1:00:15-1:00:39 |

Figma PROPOSAL: frame = component with 4 corner-ornament instances (one corner designed, flipped H/V for others), fill black 60%, title bar white 20% with 1 px inside-stroke, shine = two rotated white rects (one 7%, one with gradient-opacity mask). Roblox (inference): Frame BackgroundTransparency 0.4; ornaments as 4 baked ImageLabels or one 9-slice image (ScaleType Slice) with Pixelated; title text real TextLabel with UIStroke.

### 4.3 Search bar (TP@26:21-28:37)

| Part | Recipe | Value | TP |
| --- | --- | --- | --- |
| Body | Black rectangle centred just below the title bar, opacity 50 | 50% | 26:48-27:08 |
| Label | Duplicate of the title text; text SEARCH, size about 30, opacity 40 to 50 | 30; 40-50% | 27:15-27:36 |
| Line | Pencil line on the bar with stroke; too prominent, so Gradient Overlay: darker, fading at the ends, angle 100, scale max, a "92" value (unclear which parameter) | angle 100; scale max; 92 | 27:54-28:32 |
| Font | Custom pixel font used only because it is not going into Studio; for Roblox use a font from the FontFace list (section 7) | n/a | 27:31-27:49 |

Figma PROPOSAL: black rect 50%; hairline = 1 px rect filled with horizontal gradient, ends to 0% opacity (replaces the gradient-overlay fade). Roblox (inference): Frame + UIGradient Transparency for the fade; TextLabel placeholder in grey.

### 4.4 Item container (TP@28:44-34:57)

| Part | Recipe | Value | TP |
| --- | --- | --- | --- |
| Box | New layer, rectangle, paint-bucket fill. Top edge aligned to the end of the title frame's black stroke. Distance from the search bar measured with Shift+Down (10 px per step): 23 px. Bottom padding matched by dragging a marquee copy of the gap (drag moves only the selection): short by 8 px, so extend the bottom edge 8 px (free transform, Shift, one side). Legacy free transform must be off | padding 23 px; fix 8 px | 29:09-31:16 |
| Opacity | Box opacity 50 | 50% | 31:29 |
| Widening ornaments | Ruler at centre; marquee both ornament layers, Layer via Cut each half; move each half outward 22 px (left and right); fix seam with copy/clear/paste layer style, delete leftover extra, merge | 22 px | 31:34-33:02 |
| Slots | New layer white box at top-left of container (Ctrl-click container to select, then Move/transform): offset 14 px from edge (tried 12 first, kept 14). Same offset on the other corners. All set to opacity 20 then fine-tuned; the tutor prefers 12 (10, 15 also fine). Merge slot boxes; copy at 10 + 4 = 14 px steps; repeat | offset 14; opacity about 12; step 14 | 33:02-34:24 |
| Scroll cue | Mask the slot layer so the last row is cut off, signalling scroll. Scrollbar not drawn here | n/a | 34:24-34:45 |
| Grouping | Group as "container" in the inventory | n/a | 34:52 |

Figma PROPOSAL: container = frame, fill black 50%, auto layout padding 14 with grid or wrap layout of white 12% rects; mask rect clips the last row. Slot size not stated, choose per game. Roblox (inference): ScrollingFrame + UIGridLayout, slot Frames BackgroundTransparency 0.88; the cut-off cue arrives free from clipping.

### 4.5 Leaderstats (top-right list) (TP@35:03-42:03, 57:55-59:45)

| Part | Recipe | Value | TP |
| --- | --- | --- | --- |
| Placement | Not at the very top: Roblox core GUI covers the top-right (TP@35:16). Placed at the extreme right edge using rulers | n/a | 35:16-35:33 |
| Strip | Big rectangle, Motion Blur, erase the part past the right edge, then a soft-brush mask to fade the bottom; sharpen afterwards | blur distance not stated | 35:38-36:38 |
| Scrollbar | Pencil, opacity max, size 1 px, layer style, drawn with dual-axis symmetry in the canvas centre, then moved to the right edge | 1 px | 36:49-37:32 |
| Row | Text name, regular weight, size 20 (later bold), box under it with the left side faded using the eraser (no mask), stroke via pasted layer style, white frame opacity 20. A second text for the roleplay name in the row; the tutor realises the player name is the one in brackets | size 20; frame 20% | 37:38-40:05 |
| Row spacing | Rows duplicated; padding 4 then 5 ("five actually"), later spaced more | 4-5 px | 40:12-40:34 |
| Overflow | Rows merged and masked so they cut off at the bottom. Fix for the awkward cut: use a canvas group (Roblox) or cut at a row boundary | n/a | 40:51-41:10 |
| Right padding | Scrollbar moved 1 px right, all rows 1 to 2 px | 1-2 px | 41:18-41:41 |
| Top clean line | Top lacked an effect: move 10 px, new layer, paste layer style, draw a clean line; second line, smaller, 5 px lower, opacity 50 (reduce both), nudge so it looks cut off; both lines shifted right a bit | 10 px; 5 px; 50% | 57:55-59:39 |

Figma PROPOSAL: strip = rect with horizontal and vertical gradient-opacity masks; rows = component (name text bold + roleplay text + 20% white rect with fade) in auto layout spacing 4-5; scrollbar = 1 px rects. Roblox (inference): ScrollingFrame with UIListLayout Padding 4-5; fade via UIGradient transparency; CanvasGroup fixes overlap alpha on fading rows (section 7).

### 4.6 Party panel (4 player tabs) (TP@42:09-56:02, 59:45-1:00:15)

| Part | Recipe | Value | TP |
| --- | --- | --- | --- |
| Portrait | Ellipse marquee + Shift = circle, black fill, opacity 55 then 60; later all circles reduced to 50 | 60%, final 50% | 42:20-42:40, 1:00:03-1:00:09 |
| Name strip | Two rectangles beside the circle, motion blur as before, erased where they overlap the circle, vertical size enlarged and centred, duplicated and merged to fade out further to the right, opacity 60. Later the lower strip made 5 px smaller twice | 60%; 5 px | 42:40-44:00, 48:30-48:50 |
| Circle outline | Select circle, fill white new layer, contract 1 px, delete inside, duplicate to sharpen, Sharpen, add 2 px stroke. White pencil ornaments with dual-axis symmetry | 1 px ring | 44:06-45:26 |
| Player icon | Coloured icon placed above the strip: pencil in colour, horizontal symmetry only, erase excess | colour not stated | 45:32-46:22 |
| Icon bevel | Bevel and Emboss: depth increased, size 10, values 90 and 45 or 4 (garbled), highlight/shadow mode tried on overlay; "stands out more from a distance" | size 10; others unclear | 46:28-47:17 |
| Name text | Same layer style as other text, size 24 | 24 | 48:00-48:24 |
| Health bar | White rectangle, contract 1 px, delete = outline; stroke 2 px; gradient overlay copied from the search bar, direction white to black (not reverse); red fill under it; shrink, group as "health bar" | 1 px; stroke 2 | 48:57-50:48 |
| Mana bar | Duplicate health bar 6 px lower; Hue/Saturation to blue | 6 px | 50:42-51:27 |
| Label | Text 100 percent on the bars | not stated | 54:22-54:36 |
| Tab assembly | Rasterize, mask unwanted bits, group icon + bars + strip as a "tab"; icon was too large so scaled to 75 percent then sharpened; duplicate 4 times; group "party" | 75%; 4 tabs | 52:30-55:08 |
| Recolors | Hue/Saturation per tab: second teal, third green, fourth pink | by eye | 55:16-55:44 |
| Shadow | Soft background shadow behind the party UI so it reads as UI, not a 3D object | not stated | 59:45-59:58 |
| Bar detail | Pencil detail on the health bar, copied to the other bars | not stated | 1:01:09-1:02:28 |

Spacing between bars: 5 px or 6 px (TP@50:42-52:00).

Figma PROPOSAL: tab = component with variant for colour; icon = 1 px rect stack with highlight/shadow rects (bevel); bars = 1 px outside-stroke rect with inner gradient fill, red and blue via variable; recolor with colour variables (Figma has no hue slider on vectors, use separate fill variants). Roblox (inference): bars as Frame with Size scale from health fraction inside a UIStroke frame; icon baked Pixelated.

### 4.7 Close button (TP@55:56-57:48)

| Part | Recipe | Value | TP |
| --- | --- | --- | --- |
| Strip | Rectangle below the inventory, motion blur as usual, smaller, opacity reduced; duplicated into the inventory group | opacity not stated | 56:09-56:42 |
| Label | Text CLOSE, larger, centred; second hint "press G to close" (transcript garbled), size 20, lower opacity then made fully opaque again; strip made 1 px bigger; inventory dragged lower | 20 | 56:50-57:41 |
| Alt placement | Could sit on top of the frame instead | n/a | 57:48 |

Figma PROPOSAL: gradient-faded black rect + text; Roblox (inference): TextButton with the key hint as a separate TextLabel (for mobile and console, show a tap or button glyph instead).

## 5. Technique catalogue

Roblox column: N = native UI object; B = baked image; P = needs ResampleMode Pixelated (ImageLabel/ImageButton property, `Enum.ResamplerMode`; local docs ImageLabel.yaml:210-218).

| ID | Photoshop technique | Purpose | Figma equivalent (PROPOSAL) | Roblox | Tag | TP |
| --- | --- | --- | --- | --- | --- | --- |
| TP-T01 | Duplicate + flip V/H + merge for texture seam | Seamless-looking texture | Duplicate, Shift+V / Shift+H flips, overlap | Not shipped | SHARED | 0:58-1:31 |
| TP-T02 | Sharpen filter on texture | Crisper grain | Raster texture pre-sharpened outside Figma; Figma image fill has contrast/exposure adjusts | Not shipped | SHARED | 2:04 |
| TP-T03 | Overlay blend 30-50% | Tint scene with texture | Layer blend mode Overlay at 30-50% | Not supported (only Normal) | SHARED | 2:10 |
| TP-T04 | Elliptical vignette: ellipse, invert selection, black fill, Gaussian blur, 60% | Darken edges | Full-frame rect with radial gradient black-edge to transparent, 60% | N (UIGradient) or B | SHARED | 2:18-3:22 |
| TP-T05 | Brightness/contrast on texture | Fix flat texture | Image fill adjustments | Not shipped | SHARED | 3:22 |
| TP-T06 | Mask erase to break repetition | Avoid systematic look | Mask or gradient-opacity layer | Not shipped | SHARED | 3:40 |
| TP-T07 | Second texture, Ctrl I invert, overlay 30% | Edge detail | Second image fill, Overlay 30%; invert via adjust or pre-inverted asset | Not shipped | SHARED | 4:23-5:03 |
| TP-T08 | Select all + Layer via Cut | Crop oversized layer | Frame clip content | Not shipped | SHARED | 5:21-5:39 |
| TP-T09 | Pencil 1 px (not brush) | Hard pixel edges | 1 x 1 px rectangles on the pixel grid (snap 1 px), unioned; or draw in a pixel editor and import PNG 1:1. Figma has no raster pencil | B + P | PIXEL | 5:46-6:44 |
| TP-T10 | Layer Style Stroke 2 px black | Auto outline around any drawn pixels | Stroke 2 px, position Outside (Inside blurs less on 1 px shapes), on the unioned shape; share as a style or component | N (UIStroke Thickness 2) for boxes and text; B for ornaments | PIXEL | 7:36 |
| TP-T11 | Shift-click lines | Straight edges | Line/rect at integer coordinates; hold Shift to constrain | N or B | PIXEL | 7:53 |
| TP-T12 | Symmetry dual / vertical / horizontal | Draw one quadrant | Draw one corner as component, instances flipped (Shift+H, Shift+V) | B (baked) or 4 ImageLabels | PIXEL | 8:28 |
| TP-T13 | Copy quadrant, flip twice, merge, re-apply style | Fix missing symmetry | Same as T12; instances make this one step | B | PIXEL | 19:30-21:56 |
| TP-T14 | Corner-only ornament, erase inside | Focus on content | Draw ornament as outline path; subtract with Boolean subtract | B + P | PIXEL | 18:14-18:37 |
| TP-T15 | Copy / Clear / Paste Layer Style | Same look everywhere, fix seams | Shared effect/paint styles, components; Union to remove seam | N | SHARED | 14:45, 21:37 |
| TP-T16 | Contract selection 1 px + delete | Exact 1 px outline box | Rectangle with 1 px Inside stroke and no fill (cleaner) | N (UIStroke 1) or B | PIXEL | 22:35 |
| TP-T17 | Sharpen after scale/blur | Restore crisp edges | Avoid: design at final px size, no scaling; do not rely on a sharpen step | B + P | PIXEL | 36:30, 53:51 |
| TP-T18 | Motion blur angle 0 on black bar | Bar that fades at both ends | Linear gradient fill, opacity stops 0 to 100 to 0 (no motion blur in Figma) | N (UIGradient Transparency) | SHARED | 15:42 |
| TP-T19 | Soft-brush layer mask | Fade a panel edge | Gradient-opacity mask on a group; variable/progressive blur is not needed | N (UIGradient) | SHARED | 36:07 |
| TP-T20 | Gradient Overlay (angle 100, scale max) | Fade a hairline | Linear gradient on 1 px rect | N (UIGradient) | SHARED | 27:54 |
| TP-T21 | Inner shadow Multiply -90 (dropped) | Depth | Inner shadow effect; tutor dropped it | N (UIStroke / stacked frames) or B | SHARED | 10:53 |
| TP-T22 | Outer glow Normal 10% | Soft halo | Drop shadow, offset 0, large blur, 10% | B (soft, bilinear, not Pixelated) | SHARED | 16:21 |
| TP-T23 | Bevel & Emboss on icon | Pops at distance | Stack: 1 px lighter rects on top-left, 1 px darker on bottom-right | B + P | PIXEL | 46:28 |
| TP-T24 | Hue/Saturation recolour | Per-player colour | Colour variables / variants (no non-destructive hue shift) | N (ImageColor3 tint on white image) | SHARED | 51:09, 55:16 |
| TP-T25 | Shift+arrow 10 px nudge to measure padding | Consistent padding | Snap 1 px; Shift+arrow moves 10 px by default; use auto layout padding | N (UIPadding) | SHARED | 29:39 |
| TP-T26 | Marquee drag to measure a gap | Equalise margins | Duplicate a spacer rect, or Smart Selection/spacing guides | N | SHARED | 30:20 |
| TP-T27 | Pixel font text + 2 px stroke | Readable pixel labels | Text with pixel font, 2 px Outside stroke | N (TextLabel + UIStroke); font from list | PIXEL | 12:24-12:55 |
| TP-T28 | Translucent panel (50-60%) | See world behind | Fill black with opacity, not layer opacity | N (BackgroundTransparency) | SHARED | 17:41 |
| TP-T29 | Group opacity 70% | Soften toolbar | Group layer opacity 70% | N (GroupTransparency via CanvasGroup) | SHARED | 1:00:45 |
| TP-T30 | Rotated 7% white rects, masked | Glassy shine | Rotated rects + gradient-opacity mask | N or B | SHARED | 1:00:15 |
| TP-T31 | Ruler + Layer via Cut + move 22 px | Split and widen a frame | Frame as 9-slice parts; resize with constraints | N (Slice) | SHARED | 31:34 |
| TP-T32 | Mask last row | Scroll cue | Clip content / mask | N (ScrollingFrame clip) | SHARED | 34:24 |
| TP-T33 | Zoom out to check | Distance read | Zoom to 100% and 50%; also preview on a phone frame | n/a | SHARED | 9:37 |
| TP-T34 | Soft shadow behind party | Separate UI from 3D scene | Drop shadow behind group | B | SHARED | 59:45 |

## 6. Style signature (what reads as "pixel / rogue-like")

- Dark, translucent black panels: 50 to 60% for frames, 50% for containers and search, 60 to 50% for portraits, 70% group on the toolbar.
- 1 px light lines inside a 2 px black stroke; the black stroke does the outlining, so shapes never need a coloured border.
- Corner-only ornaments; flat edges elsewhere; ornaments hollowed so the panel shows through.
- Edges fade out (strips with ends to transparent) rather than closing with a box; the tutor repeats this on toolbar, leaderstats, name strips, close button.
- Faint white fills at 12 to 20% for slots and title bar; hairline gradient lines; no gloss except subtle shine at 7%.
- Pixel font (Alagard) at 24 to 30 with 2 px stroke; capitals for titles.
- Restraint: tutor says no more than 2 px stroke (TP@12:43) and the tutor keeps details to what reads at distance.
- Hard 1 px bars (health/mana) in red and blue with a fading gradient.

## 7. Roblox notes

Tutor states:
- Only Normal blend mode is supported in Roblox (TP@16:28), so glows use Normal; Overlay/Multiply effects in the board do not ship.
- Alagard is a custom font; for Roblox use a font on the FontFace list. See the list by adding a TextLabel and expanding the FontFace property (TP@27:36-27:49).
- Roblox core GUI covers the top-right, so do not place leaderstats at the very top (TP@35:16).
- Canvas groups fix the overlap/alpha problem when faded rows cut off (TP@40:57-41:04).
- Outer glow barely shows in Photoshop but "definitely" shows in Roblox (TP@16:53).

Inference (not stated):
- Roblox opacity = 1 - BackgroundTransparency, so 60% black panel is transparency 0.4, 50% is 0.5, 70% group is GroupTransparency 0.3 on a CanvasGroup.
- Baked pixel images need `ImageLabel.ResampleMode = Pixelated` (nearest neighbour); smooth things (glows, shadows) must stay on Default or they get blocky. Pixel art also needs integer-multiple display sizes to stay crisp; avoid fractional scale (verify in Studio).
- 2 px strokes, 1 px boxes, translucent fills, fades (UIGradient Transparency) can be native objects; hand-drawn ornaments and bevelled icons must be baked.
- Local docs also warn UIGradient on text with stroke can spike frame time (ui-gradient.md:55); use UIStroke for text outline.
- Alagard licence not checked; check before uploading as a Roblox font asset.

## 8. What the advanced version adds (music only, section titles only)

Transcript shows no steps for these. Section titles with the timestamp of the first line after each title:

| Section title | From | Notes |
| --- | --- | --- |
| Inventory Lineart | 1:03:15 | Same method on a more complex inventory; not narrated |
| Inventory Coloring | 1:07:49 | Colour pass after lineart |
| Inventory Header | 1:12:24 | Header/title area |
| Character Drawing | 1:14:18 | Character art in the UI |
| Chains | 1:16:56 | Chain decoration |
| Blood | 1:17:21 | Blood decoration |
| Inventory Boxes | 1:18:49 | Slot boxes |
| Scrolling Bar | 1:20:03 | Scrollbar |
| Interaction Elements | 1:21:12 | Buttons or controls |
| Healthbar Lineart | 1:26:47 | Bar outline |
| Healthbar Coloring | 1:28:07 | Bar colour |
| Status Effects | 1:31:34 | Status icons |
| Toolbar | 1:32:13 | Full toolbar |
| Leaderstats | 1:33:58 | Leaderstats |
| Party | 1:34:53 | Party panel |
| Outro | 1:36:38 | End |

Narrated hints about this half (TP@1:02:40-1:03:02): reuses all earlier techniques, drawing tablet, a few outer and inner glows, maybe drop shadows, otherwise strokes and the pencil. Nothing else is claimed.

## 9. UX notes and gaps

Stated by the tutor:
- Check at a distance: detail is invisible zoomed out (TP@9:37-9:49); bevel helps the icon "stand out from a distance" (TP@47:04).
- Readability: label text raised to 28-30 (TP@12:49); name row too opaque, so reduced (TP@38:12).
- Transparency vs contrast: toolbar at 100% too dark, 70% better (TP@1:00:52); search line too prominent, faded (TP@27:54); toolbar blends into background, backing strip added (TP@15:19).
- Close hint: "press G to close" label next to CLOSE (TP@57:04).
- Party shadow separates UI from 3D scene (TP@59:51).

Missing from the tutorial (inference):
- States: no hover, pressed, selected, disabled, empty slot, active toolbar slot, low-health, loading.
- No contrast check (white 12% slots on a 50% black panel over a textured scene), no text size at phone scale, no safe areas.
- Key hint "G" is keyboard-only; no touch or gamepad equivalent.
- No tooltips, no item rarity colours, no scroll indicator logic.
- Only one resolution (1920 x 1080); no mobile layout.

## 10. Gaps and ambiguities

- Sizes of nearly every shape are by eye; only these are stated: canvas 1920 x 1080, stroke 2, pencil 1, slot gap 5, padding 23 (+8), container offset 14, nudge 22, spacing 4/5/6/10, label sizes 20/24/28-30/30.
- Gaussian blur radius, motion blur distance, glow size/range not stated.
- Brightness/contrast "from 30, keep 40" is garbled; "92" on the search gradient does not say which parameter; bevel values (90, 45/4) are unlabelled.
- Pencil colour is not stated for most lines (white only for title bar and ring).
- "Press G2 flows" is the likely garble of "press G to close" (assumed; spec text).
- Test digit typed before labels; the number-label position is not stated.
- The 22 px split-and-move step: purpose not explained (widening the frame is my reading).
- Number of party tabs: four implied by recolors (second teal, third green, fourth pink); not stated.
- Whether the Alagard stroke is Inside/Outside/Center is not stated.
- Title lines in the transcript are printed just before the first timestamp of the section, so chapter starts are a few seconds earlier than shown.
