---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "owner-supplied transcript 'Stud Guide.txt' (UI Genesis, YouTube), J002"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

# Stud-style shop menu and HUD in Figma: step notes (J002-T02)

Cite as `TS@mm:ss` or `TS@h:mm:ss`. Tags: `[SHARED]` = works in any style book, `[STUD]` = specific to the stud look. "inference" = my opinion, not in the transcript. "not stated" = the tutor gave no value.

## 1. Source card

| Key | Value |
| --- | --- |
| What is built | One 1920x1080 Figma board: a Roblox "stud" shop menu (header, exit button, hero product, three currency product cards) plus HUD pieces (3 top toggle buttons, 5 left-side buttons, currency counter with plus button, slow-mode button) |
| Tool | Figma (desktop or web), one plugin ("Vectorize bitmap", runs Photopea), a UI-resources website for the background, stud tile, sunburst and icon bitmaps (site name not stated) |
| Who | Intro by Kek (UI Genesis); tutorial built by Hamudi (spelled Hamuri in the intro). Sold later as a $5 Figma file (ignored here) |
| Timestamps | TS@0:00 to TS@1:01:13 (outro after). Chapters: Figma basics 0:48, Background 1:25, Main Frame 2:33, Header 3:49, Exit Button 7:31, Stud Texture 9:29, Buy Button/Robux Icon 15:01, Gem Icon 20:09, Smaller Box 22:05, Top Buttons 34:04, Left Buttons 39:19, Currency 51:25, Slow Mode Button 56:31 |
| Footage gap | Chapter "Footage Error (Box in Main Frame)" TS@14:41-15:01: the hero frame box, its buy button and its price text appear to be built here, but the steps are not narrated. Recipe 3.5 is reconstructed from later steps and is marked |
| Trust | Practice material. One tutor. Values are tuned by eye = starting points, not rules. Some numbers are inaudible or contradictory (see section 10) |

## 2. Canvas and setup

| Item | Value / action | TS |
| --- | --- | --- |
| Frame | Frame tool, right panel "Presentation" preset 1920x1080 | 1:00-1:07 |
| Panels | Right = properties, left = layers, bottom = tools | 0:48-0:54 |
| Pan | Hold Space + left-drag | 1:14 |
| Zoom | Ctrl + scroll wheel | 1:20 |
| Background | Copy a game-scene bitmap from the UI resources site, Ctrl+V into Figma, enlarge to cover the frame. A search filter "remove stud" was applied first (reason not stated) | 1:32-2:00 |
| Lock | Lock the background layer so it cannot move by accident | 2:00 |
| Blur | Effects section: change the default Drop shadow entry to Layer blur; drag-scrub the value (hover the icon, click-drag). Value not stated; "looks good" by eye | 2:07-2:27 |
| Menu centering | Alignment tool, horizontal centre only. Vertical not centred because a header is added later | 2:47-2:59 |
| Scrub values | Hover a value's icon (opacity %, stroke weight, blur) and click-drag to change it | 2:20, 3:11, 3:36 |
| Big nudge | Shift + arrow = large step; arrow = 1 px | 7:49, 21:16 |
| Undo | Ctrl+Z used often to undo accidental moves and stroke attempts | 6:20, 15:28, 19:51 |
| Unlock a locked layer | Needed before resizing the locked outline vector in a duplicated card | 23:02-23:12 |
| Marquee on locked frame | Because the main frame is locked, click-drag around the left buttons selects only them | 58:42 |

## 3. Component recipes

Naming convention used: `<thing> button`, `price`, `top`, `base background`, `shop frame`, `dev products`, `left side buttons`, `toggle buttons`, `bottom`. Every component is a Group (Ctrl+G, rename by double-click on the layer name).

### Generic "stud 3D block" (the pattern every button and header follows) [SHARED pattern, STUD texture]

Layer stack top→bottom (nesting partly inference from TS@22:48, 28:12, 35:42, 1:00:40; exact z-order of the stud image is not shown):

1. `group mask` containing: mask shape (the "first layer"), stud image(s) (Overlay), optional icon, optional sunburst (Overlay)
2. `main shape` group containing: top layer (gradient fill + inner stroke), bottom layer (solid darker colour, offset down), flattened outline vector (no fill, outer stroke)
3. text (stroke + hard drop shadow) sits above, or under for icons (see 3.10)

Resize rule for any block: select `main shape` AND the first layer inside `group mask` together, then resize (TS@22:48, 24:43). Alt+drag to change both sides (TS@24:51).

### 3.1 Main frame (menu panel) TS@2:33-5:46

1. Bottom toolbar shape tool, click-drag a rectangle in the canvas centre, size by eye (about the middle of the board; px not stated) (2:40-2:47).
2. Alignment tool: centre horizontally (2:53).
3. Fill: change to black (3:05), then lower fill opacity by scrubbing the % field. Value not stated (3:11-3:20).
4. Stroke: click + on Stroke, scrub weight, settle 5 px (3:36-3:44). Later change position Inside → Outside (5:39).
5. Final rename: `base background` (33:31). Two leftover helper layers deleted at 33:18.
6. After the header exists, the frame is nudged down with arrow keys so frame and header align (7:24).

Layer stack: stroke 5 outside · black fill at reduced opacity.

### 3.2 Header (3D two-layer block + flattened outline) TS@3:49-7:06

1. Shape tool: rectangle matching the main frame width (3:55), adjust until perfectly aligned (4:01).
2. Fill → Gradient. Rotate it so the run is vertical (top to bottom) (4:07-4:12). Edit stops: the darker stop to a "not so bright" green first, then the white stop to a brighter green (4:19-4:30). Which stop sits on top is not stated; tutor says colours can be tweaked later.
3. Move this layer up with arrow keys, planning the 3D lip (4:37).
4. Ctrl+D to duplicate. Select the bottom copy, move it down with arrow keys until it touches the main frame (4:48-4:56).
5. Bottom copy: fill type → Solid, darker green (5:07-5:20). Both layers are almost the same colour at first (5:01).
6. Select both and shrink (header was too big) (5:26).
7. Set main frame stroke to Outside (5:39). Decision: outer stroke 5 px everywhere (6:33).
8. Outline trick: select both header layers, Ctrl+D, Ctrl+E (flatten) → one vector (5:53-6:00). Drag the vector to the bottom of the stack. Delete its fill so only the outline remains (6:08-6:14; with no fill it looks empty, so Ctrl+Z once to restore position, then add stroke). Stroke is Inside by default → set Outside, weight 5 so it matches the main frame stroke (6:20-6:33). Slightly enlarge the whole header (6:46).
9. Group the layers (Ctrl+G), rename `header` (6:58-7:06).
10. Select inside, shrink and move away to leave room for the exit button (7:13). Nudge main frame down 1:1 so edges line up (7:24).
11. Stud texture over the top layer: see 3.4. Inner stroke: select top layer, + Stroke, keep Inside, weight 4 (tried 3 first for the exit button, 4 chosen), brighter green (11:56-12:10).
12. Title text: see 3.3.

Layer stack top→bottom: stud image (blend Overlay, but see section 10) · top layer (green vertical gradient, inner stroke 4 bright green) · bottom layer (solid darker green, offset down) · flattened outline vector (no fill, stroke 5 outside).

### 3.3 Header title "SHOP" text (also used as generic outlined 3D text) TS@12:28-14:26

1. Press T, click on canvas, type the word, click away (12:33-12:40).
2. Font size 64 (12:47-12:52).
3. Font: changed here but name is inaudible (13:01). Not stated.
4. Stroke: first 5 "so it is equal everywhere" (13:14-13:20), then reduced to 4 because 5 is too much (13:48-13:55). Final 4.
5. Effects: + Drop shadow, position 4 (Y; X not stated, default presumed 0), blur 0, opacity 100 (13:29-13:48) = hard 3D shadow.
6. Nudge text up a little (13:55-14:01).
7. Rename duplicates: both groups were named `header`; second renamed `exit button` (14:07).

### 3.4 Stud texture (tiled fill, overlay) [STUD] TS@9:29-11:10

1. On the UI resources site, search "stud"; right-click image → Copy image (9:38-9:44).
2. In Figma Ctrl+V with the header top layer selected: the image fills the whole shape (9:50).
3. Click the image fill in the Fill row, change mode Fill → Tile, then scrub the scale to resize the tile (9:50-10:07). Click away. Move the layer slightly up (10:07-10:13).
4. For the exit button: Ctrl+D the texture, Ctrl+V into the button. Exit button is a square, "perfect 4x4" of the stud image, so no tiling or resizing needed (10:20-10:33).
5. Textures look harsh: select the image layer, Appearance section, blend-mode dropdown (eyedrop icon), hover each mode to preview; choose Overlay (10:39-11:04). Repeat for the exit texture (11:04-11:10).
6. Later changes: corner texture and second texture on cards made smaller (26:33-26:44); stud texture edited by pressing Enter (image edit mode) then dragging to resize, Enter to exit (27:52-28:00); Alt-drag to match shape (25:52). "Highlights" opacity lowered on the shop left button (43:45-43:54, value not stated).

### 3.5 Exit button TS@7:31-11:49, 14:07-14:26

1. Select whole `header` group, Ctrl+D, Shift+Right arrow to move far, arrows to fine-tune (7:36-7:56).
2. Resize smaller to a square (8:02).
3. Ctrl+click selects only the top layer inside the group (plain click selects the whole group) (8:16-8:22).
4. Gradient: change both stops to red; top end a bit brighter (8:34-8:49).
5. Ctrl+click the bottom layer, set darker red (8:56-9:02).
6. 3D lip too deep: Ctrl+click header's main shape, Ctrl+Shift+click exit button's main shape, drag the bottom edge down/make them taller at the bottom to hide part of the lip (9:09-9:29).
7. Stud texture + Overlay (see 3.4). Top layer brighter red (11:18-11:24).
8. Inner stroke: + Stroke on main shape, 3 px first then 4 px, bright pink / lighter red (11:31-11:49).
9. Label: duplicate the header text (Ctrl+D), Shift+arrows onto the button, rename `X`, centre (14:14-14:26). X glyph is implied.

Layer stack as the header, red palette.

### 3.6 Hero product frame (button, Robux icon, price, description, gem in group mask) TS@14:41-21:56 (partly off-footage)

Hierarchy named by the tutor: `hero frame` > {`main shape`, `group mask` (mask shape, stud image, gem icon, gem duplicates), `button` group (its own main shape, vector, group mask), `price` group (price text + `Robux icon`), `description` text}. Hero frame colour palette is orange (revealed at 28:46 when recoloured to blue).

Steps (button box, price text and card box are built off-footage 14:41-15:01; not stated):
1. Robux icon: see technique T17 for vectorizing. Result: white fill, stroke 3 outside, layer opacity 100 (was 0 after import), resize with Shift+Alt, drag onto the button (16:36-17:10). Drop shadow Y 3 (instead of 4), blur 0, opacity 100 (17:17-17:27). Rename `Robux icon`, drag under the button group in the hero frame; group price text + Robux icon and name `price` (18:23-18:41).
2. Layout flip: select the entire button group and drag to the other side of the card; keep the price/icon where it is; nudge left to align with the button (18:46-18:53).
3. Description text: add text, content a short placeholder line (not stated), fill white, resize text box, stroke 2 (smaller text), Ctrl+D and move the copy down (second line / shadow-like repeat) (18:59-19:58). A Ctrl+D slip was undone first (19:46).
4. Gem art: any in-game item or a render fits; the tutor drags the gem icon inside the group mask, text layers into the hero frame, deletes an unknown leftover layer (20:09-20:47).
5. Gem polish: keep normal size, optionally duplicate the gem, rotate slightly, lower opacity; duplicate the main gem bigger at lower opacity behind (21:16-21:49). Values not stated. Stud texture can be dragged below it inside the mask (20:57).
6. Rename and group (see 3.8).

Layer stack top→bottom (inference from names): description · price (price text, Robux icon) · button group · group mask (gem, gem copies, stud image, mask shape) · main shape (orange gradient top layer, darker bottom layer, outline vector).

### 3.7 Currency product cards (x3) TS@22:05-33:50

1. Duplicate the whole hero frame group; Shift+Down arrow to move; collapse nested groups (22:10-22:42).
2. Unlock the outline vector (it was locked), select `main shape` plus the first layer of `group mask`, resize to card size so three fit (22:48-23:19).
3. Resize stud image to fit; text size 36, centred; delete the short description line ("it is just money") (23:33-23:48).
4. Button resize: switch the bottom toolbar tool from Move to Scale so strokes and corners do not stretch (23:56-24:09). Go back to Move and stretch the button horizontally with Alt+drag on main shape + first mask layer (24:35-24:57). Measured gap readings while Alt-hovering: 20, aim 23 (24:57-25:06); bottom 21 (25:28-25:44). Target: equal gap on both sides.
5. Same Alt+drag on the stud texture so it follows the shape (25:52). Gem moved into place, texture corner pieces made smaller, button dragged down (26:06-26:52).
6. Group name: hero frame copy renamed `currency product` (first typed "currency pass" then corrected) (26:59-27:11).
7. Centre button and gem: Ctrl+click the gem, centre; Ctrl+click title, move up; gem up (27:20-27:36).
8. Recolour to blue: collapse masks, open `main shape`, top layer → bluish gradient, other stop changed, inner stroke recoloured, bottom layer → darker blue instead of orange (28:12-28:46). Check outer stroke is equal-sized after resizing (28:52-29:07).
9. Text colour white; layer name `+50 cash`; align centre (29:15-29:33). Gem smaller (29:38).
10. Duplicate twice: collapse, Ctrl+D, Shift+Right arrow; centre the middle card horizontally with the alignment tool; duplicate again (29:44-30:08). Not perfectly aligned.
11. Spacing: select all three; hover between layers shows the gap in px = 23; increased to 24 so it lines up with the top; tutor wavers on whether the 1 px matters (30:16-30:42). Final spacing: likely 24 (see section 10).
12. Group all three, rename `dev products` (30:42-30:50); Shift+Up arrow once (30:50). Keep equal padding all around.
13. Padding checks with Alt held over a frame: left 32, right 30, bottom 30; move left card group 2 px → 30/30/30 (31:25-31:56). Header: resize its bottom three layers by 1 px (32:04-32:11). Top padding 22 measured; main frame was 31, moved up 1 px to 30 (32:33-33:05).

Per-card amount text and prices for cards 2 and 3 are not shown (only `+50 cash` named).

### 3.8 Shop frame grouping TS@33:18-34:04

1. Rename main frame `base background`; group header + exit button as `top`; group `hero frame` + `dev products`; group all as `shop frame`; move down a little.

### 3.9 Top toggle buttons (sell / base / shop) TS@34:04-39:14

Inspired by a "Grow a Garden"-style layout (34:13).
1. Ctrl+click the hero `button` group, Ctrl+C, collapse `shop frame`, Ctrl+V. Drag outside the shop frame and up (34:13-34:32).
2. Inside the pasted group: delete the Robux icon; drag the text out of its group (the empty group deletes itself); retype text `base`; centre (34:39-34:58). Name `base button` (37:32).
3. Shop: Ctrl+D base, Shift+Right arrow; rename `shop`; blue: Ctrl+click top frame selected the stud layer by mistake, so open `main shape` and select its top layer; recolour to blue using the copy-fill trick (TS-T28, see section 4) (35:05-36:26). Inner stroke blue (36:31). Bottom layer darker blue (36:53). Accidental whole-group move fixed (36:56-37:00). A piece was hanging past the edge, set to 45 (dimension not stated, 37:06-37:14).
4. Sell: Ctrl+D base, Shift+Left arrow, rename `sell` (teleports to the sell merchant), centre text (37:38-37:55). Top layer gradient to red; bottom red too strong, toned down; inner stroke red; trial colours (38:01-38:43).
5. Group all three via click-top-layer then Shift+click-bottom-layer in the panel, Ctrl+G, name `toggle buttons` or `teleport buttons` (38:55-39:14).

Order left→right: sell (red), base (green), shop (blue). Roles: sell = teleport to sell merchant (37:44); base and shop destinations implied, not explained.

### 3.10 Left side buttons (shop, rebirth, index, settings) TS@39:19-51:25, 58:42-1:00:27

Shop (the master) 39:19-46:05:
1. Copy the `base` button, paste outside its group, place at left (39:39-39:52).
2. Open `main shape`, select everything inside, drag left edge to make 70x70 (perfect square) (39:59-40:12).
3. Adjust stud texture and group mask to the new shape; centre; Shift+Alt resize; lengthen one; repeat on the other (40:19-41:02).
4. Too small: switch to Scale tool and scale whole button up (41:08-41:32). Ctrl+click the text and resize (41:40).
5. Scale side effect: outline vector stroke scaled to 7; set back to 5 to match the rest (41:46-42:00).
6. Text properties: stroke 3, drop shadow 3 (tried 2) (42:06-42:20).
7. Blue colour: Ctrl+click top layer on a blue button, click empty spot in Fill row, Ctrl+C; select this button's top layer, delete its fill, Ctrl+V (42:28-42:47). Inner stroke found at 3, colour pasted the same way, weight 3 (43:01-43:13). Bottom layer darker blue, resize the bottom lip (43:19-43:28).
8. Name `shop`; align text horizontally; drag it down (43:33-43:45).
9. Lower highlight opacity (too bright) (43:45-43:54). Value not stated.
10. Icon: a shop icon that already has an outline (not perfect, 44:07); place inside the button group; rename button `Robux shop` (44:27); centre with alignment tool (45:14-45:19).
11. Sunburst: UI resources site → search "sunburst" → copy image; select `group mask`, Ctrl+V; resize, centre, blend Overlay (44:36-45:01).
12. Too wide: Alt+drag on main shapes + first mask layer to narrow (45:33-45:49). Inner stroke raised to 5 (45:56-46:05).

Rebirth 46:05-48:25: duplicate `Robux shop`, Shift+arrow to the new slot, gradient → purplish/pink (pink too bright, then top pinkish and lower stop darker "reverse", 46:28-47:05), stroke purplish-pink (47:12), bottom layer darker purple (47:19). Icon with outline replaces the shop icon (47:24-47:30). Layer order: icon placed under the text so text overlaps it (47:50-47:56). Rename `rebirth`, retype text `Rebirth`, centre (48:05-48:18). Move down, align.

Index 48:43-49:43: duplicate the pair down, rename `index`. Green; stroke 3; bottom layer darker green; icon dragged into the group and under the text (49:12-49:29); centre.

Settings 49:43-51:20: rename `settings`. Main layer gradient grey at bottom, almost white on top; stroke bright white; bottom layer darker grey (49:59-50:22). Text smaller (50:38-50:52).

Group fixes: Ctrl+Shift-click all texts and shrink one step (50:45-50:57); Shift+Alt resize buttons (51:14). Text sizes tried 30, 28, 27, final 25 (59:24-59:54). Ctrl+click each text and re-centre with the alignment tool after each size change (59:54-1:00:08). Drag all texts down (1:00:14).

Group: marquee-select the left column (background is locked), Ctrl+G, rename `left side buttons`, centre vertically with the alignment tool (58:42-59:09).

Shared per-button palette: shop blue, rebirth pink/purple, index green, settings grey/white (roles by colour).

### 3.11 Currency counter and plus button TS@51:25-56:31

Cash text:
1. Text tool, type `$` then a long run of nine digits (comma use not stated), click away, then fill green (51:31-51:56).
2. Size 46 (52:10).
3. Stroke weight: 4 tried; 5 "maybe too much"; 3 tried; stroke position was Center, set to Outside (52:17-52:36). Final in group fix: stroke 3, drop shadow 3 (55:54-56:00).
4. Effects: Drop shadow, blur 0, opacity 100 (52:42-52:49). Join type Sharp → Round on stroke settings (52:49-52:56). Y offset at first not stated.
5. Move up to give breathing room. Remove several nines because the number was too wide (53:02-53:08).

Plus button (all steps TS@53:14-56:07):
1. Shape tool, Shift+drag a small square at the right of the number (53:22-53:30).
2. Fill solid green (no gradient, button is small) (53:30-53:37).
3. Ctrl+D; move the bottom copy down with arrow keys; darker green (53:44-53:51).
4. Top layer: + Stroke, Inside, 3 px, brighter green (53:51-54:03).
5. Select both, Ctrl+D, Ctrl+E (flatten), send to bottom, delete fill, stroke Outside 3 px (54:03-54:23).
6. Group the pieces (54:23).
7. Text `+`: T tool, white, stroke 3 then 2, Drop shadow blur 0, opacity 100, Y 3 then 2, stroke join Round (54:34-55:49). The subtle result "fits better" (55:49).
8. Button too big, shrunk; placed in the currency group (56:00-56:07).
9. Select first layer, Shift+click last in the panel, Ctrl+G, rename `bottom` (56:13-56:31).

Layer stack `bottom` top→bottom: `+` text · plus button (stroke-outline vector, darker green bottom layer, bright-stroked green top layer) · cash text (green, stroke 3 outside round, hard shadow 3).

### 3.12 Slow-mode button TS@56:31-1:01:07

1. Duplicate the `index` button (green) (56:31-56:37); switch back to Move; place at top of the left column (56:37-56:43).
2. Remove the icon; resize main shape + first mask layer (56:50-56:57).
3. Stud texture bigger, button made "three studs long" (57:03-57:23); texture moved down a bit (57:29).
4. Delete the sunburst (57:37). Lighten the colour, it was too dark (57:49).
5. Text: move to centre, type `slow mode on` (57:56-58:11); press Enter to commit and check (58:11).
6. Rename `slow mode` (58:36).
7. Fix 3D lip: Ctrl+click bottom two layers (outline vector and darker layer), resize so the lip is 7 px, equal to the other buttons' 7 px (counted by eye) (1:00:32-1:00:59). Move the whole button up a few pixels (1:01:07).

Continued in [[reference/ui/02b-stud-techniques]].
