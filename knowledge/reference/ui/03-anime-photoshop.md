---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "owner-supplied transcript 'Anime Guide.txt' (UI Genesis, YouTube), J002"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

# TA: Anime tower-defense unit inventory in Photoshop (notes for the anime skill book)

Cite style: `TA@mm:ss`. The timestamp is the marker line that opens the transcript block; the cited sentence sits inside that block, so allow a few seconds of drift. Everything marked **PROPOSAL** (Figma way) or **inference** (Roblox conversion) is the extractor's idea, not the tutor's. The Figma proposals are untested in this job.

## 1. Source card

| Key | Value |
| --- | --- |
| id | TA |
| What is built | One screen: an anime-style tower-defense (TD) unit inventory. Left: search bar, sort button, filter button, capacity counter, scroll list of unit boxes. Right: unit preview with a stats panel. Top: a sharp header with title. Plus main buttons (equip best, unequip all) and a close button. TA@0:00, TA@14:21, TA@18:48, TA@21:15, TA@24:43 |
| Tool | Photoshop. Tutor says Figma or Affinity also work (TA@0:05). Tutor's vectors and textures come from his own older work, a free UI pack and "free vector packs" (TA@5:50, TA@10:26). |
| Tutor | "Kek", channel UI Genesis. |
| Length | about 31:10. Spoken content is thin: long stretches are music or screen-only (see section 9). |
| Trust | Practice, one tutor, experimental. Few exact values: almost no pixel sizes, hex colors, opacities or angles are spoken. The tutor says he did not focus on UX (TA@9:52-10:12) and that "there will be some problems" with the UX (TA@10:06). The file was lost to a crash at about 25:46, so the last third (text on unit boxes, rarity rows) was done on a flat low-quality screenshot, not live layers (TA@25:46-26:12, TA@30:16). |
| Timestamp range used | TA@0:00-31:10 (outro promo at TA@30:32+ ignored). |
| Best use | Style decisions and principles, plus the recipe of effects (glow, dodge, gradient stroke). Not a source of numbers. |

## 2. Build order (as shown in the video)

| # | Part | Starts | Note |
| --- | --- | --- | --- |
| 1 | Foundation shapes (main panel body) | TA@0:48 | Random shapes, blend, color, gradients, test what works. |
| 2 | Foundation glow/blend styling | TA@1:24 | Inner and outer glows with dodge or overlay blend. Silent after about TA@1:54. |
| 3 | Outline styling | TA@3:45 | Reported finished at TA@3:45; the steps themselves are silent. |
| 4 | Search bar (dark inset, icon, placeholder text) | TA@3:58 | Also a character render dropped in (TA@4:28). |
| 5 | Header silhouette | TA@4:43 | Random shape, warp, pen tool, refine. |
| 6 | Header textures and gradients | TA@5:16 | Inner designs, gradient, shine (later removed). |
| 7 | Header claw texture: duplicate, clip, reflection, shadow | TA@7:29 | Unusual texture on purpose. |
| 8 | Header z-order over the search bar | TA@7:54 | Header exported as its own layer; z-index in Studio. |
| 9 | Header color experiments | TA@8:08 | Yellow and green side accents tried, later removed. |
| 10 | Title / text restyle: inverted stroke | TA@9:06 | Black text, white stroke. See ambiguity A3. |
| 11 | Side descriptions (units, left and right) | TA@9:36 | Filled in; UX not the focus. |
| 12 | Close button | TA@11:43 | Pure experiment; only philosophy spoken. |
| 13 | Sort and filter buttons | TA@14:21 | Curved rectangle, glow, overlay-stroke icon. |
| 14 | Capacity counter | TA@14:58 | Position tested many ways. |
| 15 | Foundation stripes and shine | TA@16:11 | Left side of the main UI. |
| 16 | Main buttons (equip best, unequip all) | TA@18:48 | Gradient overlay, inner glow, carved shine, outer glow. |
| 17 | Main button color variants | TA@19:56 | Hue/saturation duplicates. |
| 18 | Unit stats boxes, oversized icons, tier label | TA@21:15 | Montserrat ExtraBold, gradient stroke over gradient fill. |
| 19 | Unit list boxes with selection outline | TA@24:43 | Last step before the crash. |
| 20 | (File lost; finish on flat screenshot) | TA@25:46 | |
| 21 | Text on unit boxes, long-name handling | TA@27:44 | |
| 22 | Rarity row colors (duplicate rows, recolor) | TA@29:01 | Top row mythical, second legendary, third maybe uncommon. |

## 3. Component recipes (every step and value actually stated)

"Not stated" means the tutor never said it. Every row here is the tutor's statement, paraphrased; no Figma content in this section.

| Part | Steps stated | Values stated |
| --- | --- | --- |
| Foundation shapes | Make random shapes and see what looks nice; mix and match; blend; add colors and gradients; this comes from experience or references (TA@0:48-1:12). | Shape sizes, colors, gradient stops: not stated. |
| Foundation glow/blend | Use inner glows, outer glows and "all the blending options" to build a texture and the target style (TA@1:24-1:38). Best blend modes for these glows: overlay, color dodge, linear dodge, and others (TA@1:38-1:43). Needs correct angles, color tools, gradients and a good sense of color (TA@1:48-1:54). | Which glow gets which mode: not stated. Opacity, size, spread, angle, colors: not stated. |
| Outline styling | Outline of the foundation is stylized and finished (TA@3:45). | All steps and values: not stated (silent stretch). |
| Search bar | Make a black rectangle, then lower its opacity (TA@3:58-4:03). Make a search icon by hand (simple) or find one online (TA@4:09-4:15). Add placeholder search text to the right of the icon (TA@4:15-4:22). | Opacity, size, corner radius, text size: not stated. |
| Character render | A render found with a Google search was dropped in, probably from another game (TA@4:22-4:35). | Position and size: not stated. See section 8. |
| Header silhouette | Make a random shape; warp it; use the pen tool to sketch a sharp header; stretch and distort; refine until the silhouette is final (TA@4:43-5:16). | Shape points, size, angle: not stated. |
| Header details | Add small effects and designs and warp them too (TA@5:16-5:27). Add gradients and small shine effects, some removed later (TA@5:39-5:44). Add textures from his free UI pack and other learned techniques (TA@5:50-6:02). Tutor calls it not difficult but slow and thoughtful (TA@5:27-5:33). | Colors, gradient stops, opacities: not stated. |
| Header claw texture | Use a texture most people would not try, here a claw-like icon, to find something new (TA@7:29-7:49). Duplicate it, clip it to the header, make a reflection of it, then a shadow (TA@7:49-7:54). | Reflection opacity, shadow offset/blur/color: not stated. |
| Header over search bar | Import the header separately on top of the original UI and place it over the search bar so it seems to sit on top of it (TA@8:01-8:08). In Studio this becomes a z-index matter (TA@8:08-8:15). | Overlap amount: not stated. |
| Header colors | Try different colors on the header (TA@8:15-8:22). Yellow and green on the left and right sides probably removed later; fine to keep if liked (TA@8:22-8:28). | Exact hues: not stated (only "yellow", "green"). |
| Title / text style | Change the usual white text with black stroke to black text with white stroke, so colors are inverted (TA@9:06-9:23). Not pure black and white: the text color is about the same as the main UI background color, for consistency (TA@9:23-9:36). | Stroke width, exact colors, text size: not stated. |
| Side descriptions | Fill in descriptions for the units on the left and right sides (TA@9:36-9:47). | Content and layout: not stated. |
| Vector icons | Icons are older vectors the tutor made or combined, colored from simple icons or free vector packs (TA@10:20-10:34). | Not stated. |
| Close button | Lots of experimenting. Take time; do not rush in a few days; keep the process joyful (TA@11:43-12:19). | All visual steps and values: not stated. |
| Sort and filter buttons | Make a rectangle with some curving; try effects; make a glow; aim for "pristine and elegant" (TA@14:21-14:40). Filter icon: simple shapes, made black, then given a stroke, and the stroke blend mode set to overlay, so the icon looks part of the button and like an art piece (TA@14:40-14:58). | Glow color, corner curve, sizes, overlay stroke width: not stated. |
| Capacity counter | Add the unit inventory capacity (units the player owns). Move it right, left, up and down to find the spot (TA@14:58-15:10). | Position, text format (for example x/y): not stated. |
| Foundation stripes/shine | On the main UI, left side, add stripes or shine effects and see if they look good. Reduce opacity or brighten as needed (TA@16:11-16:23). | Stripe count, angle, width, opacity: not stated. |
| Main buttons | Make a basic shape; cut it out (carve); put text on it (TA@19:00-19:06). Add a gradient overlay, then an inner glow (TA@19:06-19:11). Carve glows into it to test whether the shine reads as crystalline or more clickable (TA@19:11-19:23). Add an outer glow for a shine effect so people want to click (TA@19:37-19:42). | Button size, radius, gradient stops, glow size/blend mode/opacity: not stated. Button text font and size: not stated. |
| Main button color variants | Duplicate the buttons and change colors with the hue/saturation adjustment. Other apps may have an adjustment-layer equivalent (TA@19:56-20:08). | Hue shift amounts, resulting colors: not stated. |
| Unit stats | Use older vectors; resize them; sharpen them or smooth them; put text next to each (TA@21:15-21:28). Font: Montserrat ExtraBold, his favorite on Roblox and elsewhere (TA@21:28-21:35). | Text sizes and colors: not stated. |
| Stats boxes | Remove the transparency of the boxes (make them solid) (TA@21:42-21:48). Add a stroke, then a gradient on the color under the main container, a stroke, and a gradient on top of the stroke (TA@21:48-22:04). Make the icon bigger than its box for a cartoony dynamic look (TA@22:04-22:10). Add a small tier label on top (TA@22:10-22:16). Duplicate, position, and recolor other containers and strokes for variety (TA@22:16-22:31). | Gradient stops, stroke width, icon overshoot size, label size: not stated. |
| Unit list boxes | Boxes with curved corners and strokes, plus a white outline used for selection (TA@24:43-24:54). On click or hover while scrolling, the white outline appears, making the list feel bouncy and nicer to use (TA@24:54-25:08). | Outline width, animation, easing: not stated. |
| Unit box text (post-crash) | Add text to the boxes. Leave enough room for long names; tutor's two test names are a short one and a long "ultimate" style one (TA@27:44-28:18). If the name is long: smaller text, and fewer columns (six down to five) so boxes get bigger and text can be bigger (TA@28:18-28:43). Place icons so they do not collide with text (TA@28:43-28:55). | Font sizes, box sizes: not stated. |
| Rarity rows | Duplicate the rows; change colors or gradients to mark tiers (TA@29:01-29:12). Top row mythical, second legendary, third could be uncommon "and so on" (TA@29:12-29:36). | Colors per tier, tier order beyond these examples: not stated. |

## 4. Style principles stated by the tutor

| # | Principle | Cite |
| --- | --- | --- |
| P1 | Glowy or bright reads as clickable and gets more clicks. Dark and high-contrast suits drama, not buttons, and buttons are what most UI is. | TA@19:23-19:37 |
| P2 | Build by experiment. Try shapes, colors, blends; keep what looks good, drop the rest. Experience and references drive it, not a formula. | TA@0:48-1:12, TA@19:48-19:56 |
| P3 | Good color sense, angles and gradients matter most for the glow stage. | TA@1:48-1:54 |
| P4 | The header should be a sharp, warped silhouette made with the pen tool, refined until it feels right. | TA@4:43-5:16 |
| P5 | Try unusual textures on purpose to find something new (the claw example). Clip the texture to the shape, then add a reflection and a shadow so it sits in the piece. | TA@7:29-7:54 |
| P6 | Header sits over the search bar (overlap) so it looks like it is on top; solve with z-index. | TA@8:01-8:15 |
| P7 | Remove effects that do not work (header shine, side colors) later; side colors are optional. | TA@5:39-5:44, TA@8:22-8:28 |
| P8 | Text: invert the common white-fill, black-stroke; use dark fill with white stroke; dark fill matches the panel background color, not pure black, for consistency. | TA@9:06-9:36 |
| P9 | Tutor's stated aim for real UI: good for UI and UX. This video is style only. | TA@9:47-10:12 |
| P10 | Take your time; the creative process should be full of interest and passion, not rushed in days. | TA@11:50-12:19 |
| P11 | Sort and filter buttons should look pristine and elegant; icon stroke set to overlay so the icon belongs to the button. | TA@14:26-14:58 |
| P12 | Icons and vectors bigger than their box give a cartoony, dynamic look. | TA@22:04-22:10 |
| P13 | Make boxes solid (no see-through) with gradient fill plus gradient stroke; recolor the set for variety. | TA@21:42-22:31 |
| P14 | Hover or select adds a white outline; this feels bouncy and enjoyable. | TA@24:54-25:08 |
| P15 | Leave room for long names; fewer columns means bigger boxes and bigger text; keep icons clear of text. | TA@27:57-28:55 |
| P16 | Rarity shown by color tiers on duplicated rows. | TA@29:01-29:12 |
| P17 | Keep the mind easy; do not overthink. Mastery takes hours and days. | TA@20:08-20:17, TA@31:04 |

## 5. Technique catalogue

Columns: id · Photoshop technique (as stated) · purpose · Figma equivalent (**PROPOSAL**) · Roblox native or baked (**inference**) · tag · timestamp.

| id | Photoshop technique | Purpose | Figma equivalent (PROPOSAL) | Roblox native / baked (inference) | Tag | TS |
| --- | --- | --- | --- | --- | --- | --- |
| TA-T01 | Random shapes, mix and match, gradients, blend | Build the main panel body by exploration | Several vector/rectangle layers with gradient fills; boolean union/subtract; group; try per-layer blend mode | Panel shape as a baked image (9-slice if the shape allows) or Frame + UICorner + UIGradient for simple shapes. Complex silhouette: baked. | [SHARED] | TA@0:48 |
| TA-T02 | Inner glow with blend mode overlay, color dodge or linear dodge | Add inner light and texture to panels and buttons | Inner shadow effect with X0 Y0, blur and spread, light color. Figma effects have no own blend mode, so for dodge/overlay duplicate the shape on top, give it a gradient or glow fill, and set that layer's blend mode: Overlay, Color dodge, or Plus lighter (closest to linear dodge). | Roblox UI has no blend modes. Bake the result into the image, or fake with a semi-transparent lighter Frame + UIGradient (no true dodge). | [SHARED] | TA@1:30-1:43 |
| TA-T03 | Outer glow with the same blend modes | Make edges shine so buttons look clickable | Drop shadow X0 Y0, blur, light/colored, opacity; or a blurred duplicate under/over with Plus lighter or Screen | Native: UIStroke (colored, thick, transparent) approximates a hard glow; soft blur glow needs a baked image or ImageLabel glow sprite. UIShadow-style drop shadow if available (not verified). | [SHARED] | TA@1:30-1:43, TA@19:37 |
| TA-T04 | Stylized outline (layered outline built over the foundation) | Define panel edge | Multiple strokes on one layer (Figma allows several strokes), inside or outside, gradient stroke; or duplicate vector offset | UIStroke (one gradient via UIGradient) for simple cases; double or complex outlines: baked | [SHARED] | TA@3:45 |
| TA-T05 | Black rectangle with lowered opacity | Search bar as a dark inset well | Rectangle, fill black, opacity about low (value not stated; tune), corner radius; optional inner shadow | Native: Frame, BackgroundColor3 black, BackgroundTransparency, UICorner | [SHARED] | TA@3:58-4:03 |
| TA-T06 | Pen tool silhouette plus warp/distort/stretch | Sharp angular header shape | Pen tool, then edit vector points / vector network; Figma has no warp, so do point edits or skew via Transform; flatten for final | Baked image for header (non-rectangular); use 9-slice only if the middle is flat | [ANIME] | TA@4:43-5:16 |
| TA-T07 | Gradients and small shine on header; some removed | Light the header; keep only what works | Gradient fills (linear/radial), small white shapes with Overlay or Screen, opacity tuned | Baked into header image | [ANIME] | TA@5:39-5:44 |
| TA-T08 | Unusual texture, duplicated, clipped to the header, with reflection and shadow | Original-looking detail that sits inside the shape | Place texture as image fill or vector; select it and the header shape, "Use as mask" or put in a frame with Clip content; copy, flip, fade with gradient mask for reflection; Drop shadow. | Baked into header image. ClipsDescendants only clips to rectangles, so not usable for angled shapes. | [ANIME] | TA@7:29-7:54 |
| TA-T09 | Header exported separately, placed over search bar | Overlap makes depth: header on top | Separate component or layer placed higher in the layer list; keep the search bar slightly under | Native: separate ImageLabel with higher ZIndex (tutor says "z-index in Studio") | [SHARED] | TA@8:01-8:15 |
| TA-T10 | Inverted text: dark fill, white stroke; fill color about equal to panel background | Text that blends with the panel and still reads | Text fill dark panel-matched color (use a color style); text stroke white, position Outside, round join, to avoid spikes | Native: TextLabel plus UIStroke (white, Contextual/text mode); panel color as a shared Color3 constant | [ANIME] | TA@9:06-9:36 |
| TA-T11 | Black icon with stroke whose blend mode is overlay | Icon looks merged with its button | Icon fill black; add stroke; set that stroke paint blend mode to Overlay (verify per-paint blend mode in the current Figma), else put a duplicate outline on top with Overlay | Baked icon (icon plus overlay stroke flattened) | [SHARED] | TA@14:40-14:52 |
| TA-T12 | Curved rectangle button with glow | Sort/filter buttons, elegant | Rectangle with corner radius and smoothing; gradient fill; glow as T02/T03 | Native for simple form: Frame + UICorner + UIGradient + UIStroke; glow baked | [ANIME] | TA@14:26-14:40 |
| TA-T13 | Stripes or shine overlays on the foundation, opacity tuned | Texture and flow on large panels | Rotated thin rectangles in a masked group, gradient to transparent, Soft light/Overlay/Screen, opacity slider | Baked into panel image, or a stripes ImageLabel with transparency | [ANIME] | TA@16:11-16:23 |
| TA-T14 | Button: gradient overlay + inner glow + carved glows + outer glow | Crystalline, clickable main button | Gradient fill; Inner shadow (glow) ; shape cut-outs via Subtract and light fills; Drop shadow glow; keep as a component with variants | Mostly baked button image + live TextLabel on top; states (hover/press) via tween of image color or size | [ANIME] | TA@19:06-19:42 |
| TA-T15 | Hue/saturation to duplicate buttons in new colors | Color variants without redrawing | Figma has no adjustment layer. Options: (a) component with color variables per variant, recolor gradient stops; (b) overlay a Hue-blend layer in a clipped group; (c) generate variants by script | Bake one image per color, or use a grayscale/neutral base image tinted via ImageColor3 (inference: tint only multiplies, so base should be light) | [SHARED] | TA@19:56-20:08 |
| TA-T16 | Montserrat ExtraBold text | Consistent bold label font | Text style, font Montserrat, weight ExtraBold | Native font family exists in Roblox fonts (verify weight availability) | [SHARED] | TA@21:28-21:35 |
| TA-T17 | Solid box + gradient on fill + stroke + gradient on stroke | Rich card body and edge | Rectangle with gradient fill; add stroke and set stroke paint to gradient; component with variant colors | Native: Frame + UIGradient (fill) + UIStroke + UIGradient (child of the stroke) + UICorner | [SHARED] | TA@21:42-22:16 |
| TA-T18 | Icon larger than its box | Cartoony, dynamic card | Place the icon outside the box clip (do not clip the frame), drop shadow under the icon | Native: ImageLabel sibling drawn above the card with larger size; ZIndex over the card and ClipsDescendants off | [SHARED] | TA@22:04-22:10 |
| TA-T19 | Tier label on card | Show tier or rarity | Small auto-layout text pill, positioned top | Native: TextLabel inside a small Frame | [SHARED] | TA@22:10 |
| TA-T20 | Duplicate boxes, recolor strokes and containers | Variants for stats and rarity | Component variants with color variables per rarity | Data-driven recolor from a rarity table: set UIGradient colors in code (inference) | [SHARED] | TA@22:16-22:31, TA@29:01 |
| TA-T21 | White outline on hover or select | Feedback, bouncy feel | Variant "hover/selected": outer white stroke, optional slight scale; prototype with Smart animate | Native: UIStroke Enabled (or Transparency) tween on hover/select; scale tween | [SHARED] | TA@24:54-25:08 |
| TA-T22 | Sharpen vs smooth vector icons | Clean icons at their size | Vector icons, pixel snap off for smooth edges | Export at 2x or 3x; keep simple | [SHARED] | TA@21:21-21:28 |
| TA-T23 | Fewer columns for bigger boxes; text scale for long names | Readable names | Auto-layout grid with fixed card size per column count; test with a long name string | Native: UIGridLayout + UIAspectRatioConstraint + TextLabel TextScaled with UITextSizeConstraint | [SHARED] | TA@27:57-28:43 |

## 6. Style signature (what makes it read as anime)

- Sharp, angular, warped header silhouette that overlaps the content below it (TA@4:43-5:16, TA@8:01).
- Glow and shine everywhere important: inner glow, outer glow, dodge or overlay blends, stripe shines (TA@1:30-1:43, TA@16:11, TA@19:06-19:42).
- Crystalline, faceted-looking main buttons with carved light cut-outs (TA@19:11-19:16).
- Oversized character renders and icons that break their boxes (TA@22:04-22:10, TA@4:22).
- Rarity by color-gradient tiers on rows, with named tiers such as mythical and legendary (TA@29:01-29:12).
- Inverted text: dark panel-matched fill, white stroke (TA@9:06-9:36).
- Gradient-on-fill plus gradient-on-stroke cards, solid not transparent (TA@21:42-22:16).
- Experimental textures clipped into shapes with reflection and shadow (TA@7:29-7:54).
- White selection outline for feedback (TA@24:54-25:08).
- Font: Montserrat ExtraBold (TA@21:28-21:35).
- Not spoken but visible in the stated parts (inference): bright saturated palette on a mid-tone panel; dark inset wells (search bar) for contrast against glowing controls.

## 7. UX notes and gaps

The tutor says UX was not the focus and admits problems (TA@9:52-10:12). A real inventory built from this look would still need the following. Items are the extractor's list (inference), except where a timestamp is given.

| Area | Gap |
| --- | --- |
| States | Hover, pressed, disabled, selected, locked/empty for every button and card. Only the white hover/select outline is shown (TA@24:54). |
| Selected vs equipped | The look has one white outline for selection. Equipped needs a separate mark (badge or color), so the player can tell "picked" from "in the team". |
| Sorting meaning | Sort and filter buttons have icons only. Needs a label, a visible active sort (key + direction), and active-filter count. |
| Capacity | Counter exists (TA@14:58) but format and full state (at limit, over limit, what to do) not defined. Needs a warning color when near full. |
| Long names | Handled only with a smaller font and fewer columns (TA@28:18-28:43). Needs a max length, truncation rule, and a test with the longest unit name and with localized text. |
| Rarity | Color alone fails for color-blind players; add a tier text or shape cue (the tutor adds a tier label on the stats boxes, TA@22:10). Tier order: tutor gave only three examples (TA@29:12). |
| Destructive buttons | Unequip all is as glowy as equip best. A confirm step or a calmer look is needed for bulk actions (inference). |
| Readability | Heavy glow and stripes behind text can cut contrast; check contrast on phone. Dark text with white stroke on a panel-matched color needs a contrast check. |
| Touch | Hit size of sort, filter and close not stated. Needs a phone-size check. |
| Overlap | Header over the search bar can block taps if ZIndex and input sink are not set (inference). |
| Scroll | Scroll bar, empty list, loading list: not shown. |
| Safe area | Not covered. |

## 8. Warnings

| Warning | Detail | Safe path |
| --- | --- | --- |
| DO NOT COPY: character render from another game | The tutor dropped in a character render found by a Google search; he guessed it came from an existing anime TD game and was unsure (TA@4:22-4:35). Franchise or another game's art is third-party IP. Copying it risks takedown and moderation under Roblox rules and copyright law. | Use the studio's own renders, hand-made or generated originals with clear rights. Use placeholders until the real art exists. Record the source of every image. |
| Unknown provenance of vectors and textures | Icons were "found" or "photobashed", or came from free vector packs and Pinterest (TA@10:20-10:34); textures came from the tutor's own free pack (TA@5:50-5:56). Licenses are not stated. | Draw or generate icons ourselves, or use assets with a license that allows game use. Log each source. |
| Franchise look | Anime style itself is free to use, but characters, logos and names from a franchise are not (see the platform-policy skill for franchise themes). | Original characters, original names. |
| Tutor's own pack and reuse | The tutor says a recreated file will be sold later; this is a promo and is ignored here. Do not rely on it. | n/a |

## 9. Gaps and ambiguities

**Long stretches with music only or no narration** (the screen shows work we cannot see):
- TA@1:54-3:45: about 1m50 of outline and glow work, silent.
- TA@6:02-7:23: header continuing; only "Heat" music tags.
- TA@8:28-9:06; TA@10:34-11:43; TA@12:19-14:21 (about 2 min, the close button); TA@15:10-16:11; TA@16:23-18:48 (about 2.5 min); TA@20:17-21:15; TA@22:31-24:27; TA@25:08-25:46; TA@26:17-27:44; TA@29:36-30:10.

**Values never stated** (all "not stated"): every pixel size, hex color, gradient stop, angle, opacity (including the search bar black), glow size/spread, stroke width, corner radius, shadow offset/blur, text size and spacing, tween or animation timing, icon overshoot amount, hue shift amounts.

**Ambiguities**
- A1: Which glow uses which blend mode (overlay, color dodge, linear dodge) is not stated; only that all three work well (TA@1:30-1:43).
- A2: The character render at TA@4:28 appears while making the search bar; its role (unit preview on the right) is inferred, not stated.
- A3: The text change at TA@9:06 says "the text"; it is unclear if it is the header title only or all panel text. Treat as the general text style, with the title as the first use.
- A4: The "claw icon" texture (TA@7:42) is called "whatever this is" by the tutor; its shape is not known.
- A5: The unit stats are described as "on the right side" (TA@21:15) and the unit list "on the left" (TA@24:43); the exact layout is visual only.
- A6: "Tear label" (TA@22:10) is transcribed oddly; read as "tier label" given the later rarity discussion.
- A7: After the crash, rows and text were finished on a flat low-quality screenshot; quality there is not representative (TA@26:04-26:12, TA@30:16).
- A8: Whether stripes/shine (TA@16:11) were kept at the end is not stated.
- A9: Figma per-paint blend modes, text stroke options and Roblox font weights are proposals not checked in this job.
