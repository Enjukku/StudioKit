---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "owner-supplied transcript 'Cartoon Guide.txt' (UI Genesis, YouTube), J002"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

# Cartoon pet-inventory UI in Figma (UI Genesis, tutor Hamuri)

Citation form: `TC@mm:ss` = the transcript timestamp marker printed just before the cited sentence. Markers are about 5 to 10 s apart, so a step may start a few seconds after its marker. Speech-to-text errors are corrected only where the meaning is clear; each correction is listed in section 9.

## 1. Source card

| Key | Value |
| --- | --- |
| What is built | One 1920x1080 inventory screen: white dashed-blue panel, search bar, 3 rows of "pet" cards (gold = legendary, purple = epic, green = a third tier whose name is not stated), 3 buttons (Equip Best green, Delete Mode red, Filter grey), red close button, blue "Inventory" header. TC@0:00-0:42 intro, TC@0:42-40:54 build |
| Tool | Figma (design file, Frame + shape + text tools, no plugins). Assets (pet icon, halftone texture) come from a UI-resources website, copy/pasted as images (TC@14:51-15:24, TC@17:06-17:19) |
| Presenter | Intro by Kek (channel owner); build by "Hamuri" (UI Genesis staff). Slow real-time, no speed-up (TC@0:05-0:18) |
| Trust | Practice, one tutor, values tuned by eye = starting points. Colors are never given as hex or RGB; most px values are "a bit", "a couple". Treat every number here as a seed to be re-tuned against the target game |
| Timestamp range | TC@0:42 (frame) to TC@40:54 (last alignment fix). TC@41:07-41:48 is outro and sales text (ignored) |
| Order of build | Main frame, search bar, pet frame (card), cloned grid, equip-best button, delete-mode and filter buttons, close button, header, fixes (shadow), rarity recolor, inner strokes, final alignment |

## 2. Canvas and setup

| Item | Value | TC |
| --- | --- | --- |
| Frame tool | Toolbar next to Move, shortcut F | TC@0:48-0:54 |
| Frame size | Right panel preset "Presentation", 1920x1080 | TC@1:00 |
| Frame fill | Solid, "a bit darker" than default white; exact color not stated (white is "too bright") | TC@1:06-1:44 |
| Fill types shown, not used | Solid, gradient, pattern, image, video | TC@1:31-1:38 |
| Properties panel | Right side; shows the selected object only (resolution, opacity, fill, stroke, effects, appearance/blend mode, selection colors, alignment row at top) | TC@1:13-1:25, TC@2:07 |
| Shape tool | Bottom toolbar -> shapes -> rectangle; click-drag; Shift while dragging = perfect square | TC@1:50, TC@8:59, TC@29:11 |
| Text tool | T (tutor says "D" once at TC@16:05; T is used everywhere else, treat D as a slip) | TC@6:55, TC@23:14 |
| Corner radius field | Click-drag the value left/right, or type the number | TC@2:43 |
| Align (top of properties) | Left, center horizontal, right, top, middle vertical, bottom. With a single object selected it aligns to the parent frame | TC@2:07-2:24 |
| Align two objects to each other | Select object A first, Shift-click object B (target), then press an align button | TC@7:43-8:02 |
| Layers panel | Left. Shift-click to multi-select; Ctrl+G group; double-click to rename; arrow beside group expands | TC@3:50, TC@5:08-5:31 |
| Zoom | Ctrl + scroll wheel | TC@19:21 |
| Pan | Hold mouse wheel and drag, or hold Space and left-drag | TC@19:21-19:33 |
| Duplicate | Ctrl+D (selection duplicated in place, above the original) | TC@3:50 |
| Nudge | Arrow keys = small step; Shift+arrow = "bigger jumps" (step sizes not stated; Figma standard 1 px / 10 px = inference) | TC@13:56 |
| Duplicate by drag | Alt + click-drag copies the object | TC@16:34, TC@33:48 |
| Resize from center keeping ratio | Hold Alt and Shift while dragging a corner | TC@15:44-15:50 |
| Padding / distance probe | Select object, hold Alt, hover other objects: red numbers show px gap. Keep Alt held and use arrow keys to nudge | TC@8:09-8:22 |
| Undo | Ctrl+Z | TC@11:04 |
| Copy/paste | Ctrl+C / Ctrl+V for images, shapes, and single property blocks (see TC-T14) | TC@15:17, TC@39:07 |
| Layer naming used | "base frame", "white outline", "main background", "search bar", "black stroke", "white stroke", "group mask", "mask group", "pet frame", "golden frames", "equip button", "exit button" | TC@3:57-5:31 etc. |

## 3. Component recipes

Common cartoon pattern (used in every component): (1) face shape with vertical gradient, (2) duplicate pushed down and re-filled solid darker = 3D lip, (3) duplicate both, flatten, remove fill, outside stroke = black outline around the whole silhouette, (4) optional masked highlights and halftones, (5) text with stroke and a duplicated, lowered copy for a 3D look. Radius 10 is the default everywhere ("10 like always", TC@31:42).

Color words are the tutor's; no hex values exist in the video.

### 3.1 Main background panel (group "main background")

Layer stack top to bottom (inside the group): `base frame` -> `white outline`. Later a drop shadow is added on `white outline` (step 12).

| # | Step | Value | TC |
| --- | --- | --- | --- |
| 1 | Rectangle with shape tool, drag to a large size, then Align center horizontally and middle vertically to the 1920x1080 frame | size "decent", not stated | TC@1:50-2:24 |
| 2 | Fill | white (starts grey-ish, lightened to "maybe full white") | TC@2:31 |
| 3 | Corner radius | 10 | TC@2:43-2:56 |
| 4 | Add stroke (+ in Stroke), color "bluish" | color not stated | TC@3:03-3:10 |
| 5 | Stroke weight | about 5 (set by dragging the weight icon) | TC@3:21-3:28 |
| 6 | Rename this layer `base frame`, Ctrl+D, rename the lower copy `white outline` | - | TC@3:50-4:04 |
| 7 | On `white outline`: stroke position Inside -> Outside; color -> white | weight stays 5 (not changed, inference) | TC@4:10-4:28 |
| 8 | Back on `base frame`: stroke settings icon next to weight, Style Solid -> Dashed | dash and gap lengths not stated (defaults) | TC@4:42-4:55 |
| 9 | Lighten the blue ("too dark", then "that blue looks perfect") | color not stated | TC@4:55-5:01 |
| 10 | Select both layers, Ctrl+G, rename `main background` | - | TC@5:08-5:31 |
| 11 | Later: enlarge base frame ("a bit bigger") to fit the content | not stated | TC@18:57 |
| 12 | Drop shadow on `white outline` layer: Effects + (default drop shadow), Y -> 0, blur larger, opacity raised | X, blur, opacity, color not stated ("a bit stronger", "we can kind of see it now") | TC@35:13-35:37 |

Result: panel face with a dashed blue inner line, separated from the dark frame by a thick white outer ring plus soft shadow.

### 3.2 Search bar (group "search bar")

Layer stack top to bottom: `Search` text -> rectangle (white, inner shadow, grey inside-then-outside stroke).

| # | Step | Value | TC |
| --- | --- | --- | --- |
| 1 | Rectangle, drawn in the upper area | width/height not stated | TC@5:31-5:39 |
| 2 | Fill | white | TC@5:39 |
| 3 | Effects + (inserts a Drop shadow); open the effect type menu and pick Inner shadow | - | TC@5:45-5:58 |
| 4 | Open effect settings (button beside effect name): shadow sits low because Figma defaults Y = 4; set Y = 0 | X not stated (assumed 0) | TC@6:05-6:17 |
| 5 | Blur | increased "a bit", final not stated | TC@6:24 |
| 6 | Shadow opacity | default 25% -> 30% (drag the percent) | TC@6:30-6:48 |
| 7 | Shadow color | default; "can change", not changed | TC@6:30 |
| 8 | Corner radius | 10 | TC@6:48 |
| 9 | Text tool, type "search"; font Fredoka One (spoken "Fidoka / Foca one"); size 48 then "a little smaller" | final size not stated; fill color made "lighter" (grey) later | TC@6:55-7:36, TC@8:46 |
| 10 | Drag text into place; select text, Shift-click rectangle, Align vertical center | - | TC@7:36-8:02 |
| 11 | Pad check (Alt): top 9, bottom 8, left 15. Nudge text with arrows until top = 9 and left = 9 | final padding 9 top and left | TC@8:09-8:28 |
| 12 | Bottom gap still 8: select rectangle, drag its bottom edge down 1 px; Alt check now equal | rect height +1 | TC@8:33-8:40 |
| 13 | Text color lighter | not stated | TC@8:46 |
| 14 | Group (Ctrl+G), rename `search bar` | - | TC@16:53-17:00 |
| 15 | Inside the group: rectangle -> add stroke, grey, "thicker", position Inside -> Outside | weight not stated | TC@19:02-19:21 |
| 16 | Later resize: drag bar down a bit, re-center text (Align vertical center again; was already centered) | not stated | TC@28:44-29:03 |

### 3.3 Pet frame / card (group "pet frame"; first card = gold "legendary")

Layer stack top to bottom (inference from the drag-to-top instructions):
`Level 1` text -> `Doggy` text -> pet icon (inside the group) -> `group mask` (halftone image, highlight bars; blend soft light) containing a mask shape at its bottom -> top face shape (gradient, later inner stroke) -> bottom lip shape (solid darker) -> `black stroke` (outline-only vector) -> `white stroke` (outline-only vector, drop shadow).
Note: the mask group is created before the black/white strokes, so exact stacking of the strokes below the face is by flatten + "drag it right under" (TC@10:44-10:50).

| # | Step | Value | TC |
| --- | --- | --- | --- |
| 1 | Rectangle, taller than wide (not a square), dragged to align with the panel | w/h not stated | TC@8:52-9:11 |
| 2 | Fill -> Gradient (default linear, top to bottom). Top stop "goldenish", bottom stop darker orange (click each stop) | hex not stated | TC@9:18-9:44 |
| 3 | Corner radius added | value not stated (10 elsewhere) | TC@9:50 |
| 4 | 3D lip: Ctrl+D, select the bottom copy, press Down arrow "a couple of times", Fill type -> Solid, darker color | px not stated (about 2 presses = 2 px, inference) | TC@9:58-10:10 |
| 5 | Silhouette outline: select both shapes, Ctrl+D, right-click -> Flatten (becomes one vector), add stroke Outside, then delete the fill so only the outline remains | stroke weight 3; ordering: drag the new vector beneath the face shapes | TC@10:16-11:09 |
| 6 | Rename this vector `black stroke` (color black) | 3 | TC@11:16, TC@11:45 |
| 7 | White ring: Ctrl+D `black stroke`, drag below, rename `white stroke`, stroke color white, weight 3 -> 6 ("equal sized": 3 black + 3 visible white outside the black, i.e. total 6 centered/outside, inference) | 6 | TC@11:16-11:45 |
| 8 | Float shadow on `white stroke`: Effects + (drop shadow), Y 4 -> 0, blur up, opacity raised, then opacity lowered. Stroke color was temporarily changed to see the shadow, then set back to white | blur, opacity, color not stated | TC@11:57-12:40 |
| 9 | Highlight mask: Ctrl+D the top face, Ctrl+G, right-click inner shape -> "Use as mask". Name group `group mask` | - | TC@12:48-13:44 |
| 10 | Highlight: shape tool long thin rectangle, rotate slightly, fill white, drag into the mask group in Layers | size/angle not stated | TC@13:25-13:44 |
| 11 | Move it with arrows (Shift+arrow for large moves); Ctrl+D a second bar, move, resize smaller for variety | - | TC@13:56-14:19 |
| 12 | Select both bars -> Appearance (water-drop icon) -> blend mode. Tutor compares overlay and soft light and picks Soft light ("just a bit softer") | Soft light | TC@14:24-14:51 |
| 13 | Halftone: copy a dotted texture image from the UI-resources site, paste (Ctrl+V). It is white-on-white so barely visible; drag layer into `group mask` so it clips; resize with Alt+Shift; move down; blend Soft light (overlay also allowed) | scale/position not stated | TC@14:51-15:58 |
| 14 | Title: text tool, "doggy"; drag to top of layer stack (it was behind); collapse the mask group; center, move toward top; fill white; add stroke black, thicker; resize | font, size, stroke weight not stated for this text | TC@16:05-16:34 |
| 15 | Second text: Alt+drag the title to copy, move down without Alt, retype "level 1" | - | TC@16:34-16:47 |
| 16 | Group everything except the search bar into group `pet frame`. Add pet icon (from UI-resources site; user's own icon), center, flip horizontal, scale up, push the title text lower; icon goes inside the `pet frame` group | - | TC@16:53-17:38 |
| 17 | Grid: Ctrl+D the group, Shift+Right arrow to nudge the copy; further Ctrl+D repeats the same offset automatically. "A couple of times" | count of cards per row not stated | TC@17:44-17:56 |
| 18 | Gaps: select all cards (Layers, Shift-click), hover: the padding dashes show 41 px. Increase it "a bit" to fill the panel | final gap not stated; 41 start | TC@18:02-18:21 |
| 19 | Alt-check: one px off, accepted ("not the end of the world") then fixed at the end (see section 8) | - | TC@18:27-18:33 |
| 20 | Group row -> `golden frames`; Ctrl+D, Shift+Down arrow "a couple of times" or hold it, to make more rows | rows: 3 shown, not stated | TC@18:46-18:57 |
| 21 | Gold inner stroke: open a card, select top face, add stroke (default Inside), color brighter yellow, weight thickened to make it visible | weight not stated | TC@37:30-37:54 |
| 22 | Delete the other cards, Ctrl+D the finished card, drag/nudge until it snaps into the right place, then repeat Ctrl+D | - | TC@38:00-38:19 |

### 3.4 Rarity variants

| Rarity | Procedure | Values | TC |
| --- | --- | --- | --- |
| Gold ("legendary", "maybe") | Base card above. Gradient top = gold, bottom = darker orange. Inner stroke = brighter yellow | stroke weight "thickened" | TC@9:31-9:44, TC@37:41 |
| Purple ("epic") | Select a full row group, Properties -> scroll to "Selection colors" (list of every color in the group). Click the "linear" (gradient) entry: top stop -> pinkish purple. Change the orange entry -> darker purple. Change the darker bottom (lip) color -> darker purple | colors not stated | TC@35:45-36:49 |
| Purple stroke | Open one card, top shape: stroke Inside, weight 4, bright purple. Delete other cards, re-duplicate | 4 | TC@38:22-38:35 |
| Green (tier name not stated) | Top shape: stroke Inside, weight 4, bright green | 4 | TC@38:54-39:07 |
| Property copy | Click empty space in the Stroke section (selects whole property block), Ctrl+C, select another shape, Ctrl+V: color copies, weight does not; set weight 4 and recolor | 4 | TC@39:07-39:43 |

Row-to-rarity mapping is implied (row 1 gold, row 2 purple, row 3 green); the video never shows which row is which.

### 3.5 Equip Best button (group "equip button")

Layer stack top to bottom: `Equip Best` text (stroked) + 3D text copy -> `mask group` (dotted halftones, highlight bars; overlay) containing mask shape -> top face (gradient) -> bottom lip (solid darker green) -> outline vector (flattened, 3 px outside).

| # | Step | Value | TC |
| --- | --- | --- | --- |
| 1 | Rectangle (landscape), fill gradient (default left->right) | size not stated | TC@19:39-19:48 |
| 2 | Rotate gradient to vertical: "rotate gradient" button, or drag the gradient handle (hover just off a stop dot) | top-to-bottom | TC@19:55-20:15 |
| 3 | Top stop bright green, bottom stop darker green | hex not stated | TC@20:15-20:23 |
| 4 | Corner radius | 10 | TC@20:28 |
| 5 | 3D lip: Ctrl+D, drag down, nudge down; set to solid, darker green | px not stated | TC@20:34-20:50 |
| 6 | Outline: select both, Ctrl+D, Flatten, drag under both layers, stroke Outside, thicker | 3 | TC@20:58-21:16 |
| 7 | Highlight mask: Ctrl+D the main face, Ctrl+G, right-click inner shape -> Use as mask | - | TC@21:22-21:36 |
| 8 | Draw a rotated bar, Ctrl+D second smaller bar, move both into the group (rename `mask group`), recolor highlights | color not stated (white implied) | TC@21:36-22:02 |
| 9 | Blend mode: Overlay this time ("I like overlay this time") | Overlay | TC@22:07 |
| 10 | Halftone: Ctrl+C the dotted image from the earlier `group mask`, paste into this mask group, Shift+Up to lift, make smaller, rotate, keep it in corners only | scale/rotation not stated | TC@22:15-22:41 |
| 11 | Ctrl+D the halftone, flip horizontally in properties, Shift+Right arrow, then flip vertically | - | TC@22:48-23:08 |
| 12 | Group -> `equip button` | - | TC@23:14 |
| 13 | Text: T, "equip best", center, stroke thicker; 3D text: Ctrl+D the text, drag the copy down, nudge down | stroke weight not stated here (3 on other texts); copy color not stated (see Delete) | TC@23:14-23:40 |

### 3.6 Delete Mode button (red variant of Equip)

| # | Step | Value | TC |
| --- | --- | --- | --- |
| 1 | Select whole `equip button` group, Ctrl+D, Shift+arrow to move; double-click text to edit to "delete mode" (a stray duplicate text appeared and was deleted) | - | TC@23:47-24:14 |
| 2 | Reduce text size, center text in the button (align) | size not stated | TC@24:14-24:42 |
| 3 | 3D text copy: Ctrl+D, drag down in layers, nudge down. A deeper offset gives a stronger 3D feel. The copy is white by default; set its fill to black for a clearly visible lip, "we don't want that much" so offset stays small | offset not stated; color black | TC@24:42-24:59 |
| 4 | Recolor: select face, gradient green -> red; then the same for the bottom lip layer; refine highlights | colors not stated | TC@25:06-25:38 |
| 5 | Red inner stroke on top face later (copy stroke from another button, weight 4, set red) | 4 | TC@39:07-39:43 |

### 3.7 Filter button (small grey variant)

| # | Step | Value | TC |
| --- | --- | --- | --- |
| 1 | Select the group, Ctrl+D, Shift+Right arrow, open the group; delete both text layers and the outline vector (a flattened vector does not scale cleanly, remake later) | - | TC@25:38-26:04 |
| 2 | Open the mask; select the masked bottom rectangle plus the other layers; resize smaller; resize/relocate highlights and halftones to the smaller shape | not stated | TC@26:09-26:50 |
| 3 | Remake outline: select top and bottom shapes, Ctrl+D, Flatten, drag to bottom, stroke Outside | 3 | TC@26:55-27:16 |
| 4 | Text: T, "Filter", stroke | 3, position by dragging | TC@27:16-27:35 |
| 5 | Face gradient white -> grey; bottom lip likewise grey | colors not stated | TC@27:42-27:56 |
| 6 | Top is too bright: adjusted; highlight shapes look wrong on grey; lower the opacity of the highlight shapes to soften; the top stop brightened slightly | opacity not stated | TC@28:04-28:44 |
| 7 | 3D text added last: Ctrl+D the Filter text, select the lower copy, nudge down "a few steps" | steps not stated | TC@40:04-40:22 |
| 8 | Inner stroke: paste the copied stroke onto the top face, weight 4, then a lighter inside stroke | 4 | TC@39:51-39:58 |

The section 28:23-28:28 sentence is garbled ("we will use salt"); likely a blend mode choice (see section 9).

### 3.8 Close / exit button (group "exit button")

Layer stack top to bottom: X text (stroke) + 3D copy -> masked highlights (added late) -> top face (red gradient, pinkish inside stroke) -> bottom lip (solid darker red, no stroke) -> black outline vector.

| # | Step | Value | TC |
| --- | --- | --- | --- |
| 1 | Square (Shift), smaller, corner radius 10 | size not stated | TC@29:11-29:28 |
| 2 | Fill gradient, reddish | colors not stated | TC@29:35-29:40 |
| 3 | Stroke Inside, pinkish | weight not stated | TC@29:40-29:54 |
| 4 | Ctrl+D, drag down, Shift+arrow; remove the stroke from the lower copy (it inherited the stroke); nudge up; fill -> Solid darker red | px not stated | TC@29:54-30:18 |
| 5 | Outline: select both, Ctrl+D, Flatten, drag below, stroke Outside, color black | weight not stated (3 elsewhere) | TC@30:24-30:40 |
| 6 | Group (Ctrl+G) -> `exit button`; nudge up a little for placement | - | TC@30:46-30:53 |
| 7 | Text "X": T, type X, center, bigger, add stroke | 3; 3D: Ctrl+D copy dragged down | TC@31:03-31:21 |
| 8 | Late: highlights for the exit button. Open the button, select main face, Ctrl+D, Ctrl+G, Use as mask; copy the highlight shapes from another button (Ctrl+C), select the mask shape, Ctrl+V, position | - | TC@36:55-37:24 |

### 3.9 Header (blue)

Layer stack top to bottom: `Inventory` text (stroke + 3D bottom copy) -> `group mask` (highlights, dotted halftones; soft light) -> top face (blue gradient) -> bottom lip (solid darker blue) -> outline vector (outside stroke).

| # | Step | Value | TC |
| --- | --- | --- | --- |
| 1 | Rectangle, resized, corner radius | 10 | TC@31:36-31:50 |
| 2 | Gradient, rotate via the rotate-gradient button or drag; top = bright blue, bottom = darker blue | hex not stated | TC@31:50-32:10 |
| 3 | 3D lip: Ctrl+D, Shift+Down, fill Solid, darker blue | px not stated | TC@32:10-32:26 |
| 4 | Resize smaller and move right of center | not stated | TC@32:32-32:44 |
| 5 | Outline: select both, Ctrl+D, Flatten, drag all the way down, stroke Outside, thicker | weight not stated ("looking clean") | TC@32:44-33:02 |
| 6 | Text "Inventory": text tool, drag to place, add stroke; 3D by duplicating and using the lower copy | stroke weight, size, font not stated | TC@33:02-33:23 |
| 7 | Mask group: Ctrl+D face, Ctrl+G, Use as mask. Highlights: Alt+drag duplicate (tutor prefers Alt-drag over Ctrl+D), resize one, both into `group mask` | - | TC@33:23-34:00 |
| 8 | Blend mode on highlights "soft color like always" = Soft light (see section 9) | Soft light | TC@34:06-34:13 |
| 9 | Halftone dots added at the top-left, Ctrl+D copy moved to the other side, flipped or rotated, moved right, rotated more | - | TC@34:29-34:52 |
| 10 | Final padding fix for the "S" of Inventory, "fine" | - | TC@34:58-35:06 |

### 3.10 Title text and text 3D (summary across components)

| Component text | Fill | Stroke | 3D copy | TC |
| --- | --- | --- | --- | --- |
| Search label | grey (lightened) | none | none | TC@7:13, TC@8:46 |
| Pet name "Doggy", "Level 1" | white | black, "a bit thicker", weight not stated | not done | TC@16:27-16:47 |
| Equip Best / Delete Mode | white | thicker, not stated | lower duplicate, fill black for delete | TC@23:26-24:59 |
| Filter | white | 3 | lower duplicate, a few px | TC@27:22-27:29, TC@40:04 |
| X | white | 3 | lower duplicate | TC@31:16-31:21 |
| Inventory | white | stroke, not stated | lower duplicate | TC@33:08-33:23 |

Font: Fredoka One for the search text (TC@7:26-7:31); other texts use the same family implicitly ("you can never go wrong with Fredoka one"), not stated per text.

Continued in [[reference/ui/01b-cartoon-techniques]].
