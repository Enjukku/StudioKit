---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "J002; Figma MCP server skills read 2026-10-20: figma-use (SKILL.md, gotchas.md, plugin-api-patterns.md, component-patterns.md, validation-and-recovery.md), figma-generate-design, figma-generate-library, figma-create-new-file, figma-use-motion; owner decisions J002-D3, J002-D6"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Building in the owner's Figma through the Figma MCP

Owner decision J002-D3 (2026-10-20): "the Figma can access use my Figma". The agent may create files and build screens in the owner's Figma account. Account check: `whoami`; use the plan `key` the brief or the game profile names for `create_new_file` (if the account has several plans and none is named, ask). The Figma server's own skills are the binding API rules; this page is the game-UI digest of them. Re-read the server skill when an API error is not covered here.

## 1. Which Figma server skill to load (`get_figma_skill`, then pass `skillNames`)
| Task | Load before the call | `skillNames` value |
| --- | --- | --- |
| Any `use_figma` call | `skill://figma/figma-use/SKILL.md` (mandatory every time) | `resource:figma-use` |
| A visible screen, panel, popup, HUD | + `skill://figma/figma-generate-design/SKILL.md` | `resource:figma-use,resource:figma-generate-design` |
| The `Components` page: tokens, variables, components with variants | + `skill://figma/figma-generate-library/SKILL.md` | `resource:figma-use,resource:figma-generate-library` |
| Prototyping a motion record in Figma | + `skill://figma/figma-use-motion/SKILL.md` | `resource:figma-use,resource:figma-use-motion` |
| `create_new_file` | `skill://figma/figma-create-new-file/SKILL.md` | — |
If `create_session` exists, call it first with the fileKey and pass its `sessionId` to every call.

**What applies to a new game-UI file.** figma-generate-design and figma-generate-library are written for code-to-design work against a published design system. For a new game-UI file use: wrapper frame first, componentize, foundations before components, variable scopes, variant grid layout, evidence-based validation, one screenshot per phase. Skip unless the file really has them: Code Connect, `get_libraries` / `search_design_system` (run them once; an empty result means build locally), `html_to_figma`, and WEB code syntax on variables (Roblox has no CSS; leave code syntax empty).

## 2. Build order for a game UI file
1. **Inspect** (read-only `use_figma`): pages, components, variables, styles, naming. Match what exists.
2. **Foundations** (`Components` page, generate-library): variable collections `Primitives` (raw hexes, scopes `[]`), `Color` (roles: primary, positive, danger, utility, currency, text, outline; rarities), `Spacing`, `Radius`; set **scopes explicitly** (fills `FRAME_FILL, SHAPE_FILL`; text `TEXT_FILL`; strokes `STROKE_COLOR`; gaps `GAP`; radii `CORNER_RADIUS`); never leave a mode named "Mode 1". Text styles per ladder step; effect styles for the style's shadows (e.g. `Shadow/Float`, `Text/Depth` = drop shadow blur 0, 100 %).
3. **Components** in dependency order: icon components → button → card → panel → screen parts. Each control: `createComponent()`, TEXT property for its label (`addComponentProperty` returns the key string; link it with `componentPropertyReferences`), INSTANCE_SWAP for its icon (never one variant per icon), variants `State=…` (and `Rarity=…`), `combineAsVariants`, then **lay the variants out in a grid and `resizeWithoutConstraints`** (they stack at 0,0). Keep a set ≤ 30 variants; split otherwise.
4. **Screen** (generate-design): create a **wrapper frame first** (1920 × 1080, placed right of existing content), then build every section inside it; never build top-level and reparent in a later call (silently fails). Place instances, set label text with `setProperties`.
5. **Validate**: return ids + counts + bounds from every write; `get_metadata` only when evidence is missing; one composition screenshot, one after a fix. Look for clipped text, overlaps, placeholder text ("Button"), wrong font.
6. **Ledger on disk**: keep `content/ui/<screen-id>/figma-ids.json` (fileKey, page ids, component and variant ids, variable ids). IDs never survive between calls in memory; never guess one.

## 3. Plugin API rules that bite game UI (figma-use)
| Rule | Game-UI consequence |
| --- | --- |
| Colours 0–1; paint `color` is `{r,g,b}` only, opacity on the paint; variable values use `{r,g,b,a}` | hex ÷ 255; translucent panels = paint `opacity` |
| fills / strokes / effects are read-only arrays: clone, edit, reassign | |
| `setBoundVariableForPaint` returns a **new** paint and **drops the paint's opacity to 1**; paint-field binding works on **SOLID** paints only | translucent scrims and panels: bind first, then reassign `{...node.fills[0], opacity}` **on the existing node** and read `node.fills[0].opacity` back (setting it at creation was not enough: 6 scrims stayed opaque in J002-T09); gradient faces (cartoon, stud, anime) cannot bind stops to variables: rarity and role recolours use **variants** or a script that rewrites gradient stops from the token table |
| Load every font before any text write (`loadFontAsync`); style names differ per family and file ("Extra Bold" in Inter, "SemiBold" in Fredoka): always read them with `listAvailableFontsAsync`, never guess | check Fredoka One, Montserrat, Luckiest Guy, Press Start 2P exist before building; after building, **assert** every text node uses the intended family |
| `lineHeight`, `letterSpacing` are `{value, unit}` objects | |
| Text wraps only with `textAutoResize = 'HEIGHT'` + explicit width (`resize`); FILL alone collapses it to a thread | item names that wrap to 2 lines |
| `resize()` resets sizing modes to FIXED: resize first, then HUG / FILL; FILL only after `appendChild` to an auto-layout parent; a HUG parent collapses FILL children; `counterAxisAlignItems` has no STRETCH | grids: `layoutMode HORIZONTAL`, `layoutWrap WRAP`, `itemSpacing` + `counterAxisSpacing` |
| `width`/`height` are read-only: use `resize()` | |
| `rotation` pivots on the node's origin, not its centre | rotated highlight bars and sunbursts drift: set x/y after rotating and check the screenshot |
| Icons: `figma.createNodeFromSvg(svg)` with `width`, `height` and `viewBox`; `currentColor` imports as black; never draw icons from rotated lines | |
| No `figma.notify`, no `createImageAsync`, no URL fetch | images arrive by `upload_assets` (POST bytes) or `generate_image`; reuse an image elsewhere by copying its `imageHash` (one stud tile, many fills: `scaleMode: 'TILE'`, `scalingFactor`) |
| New top-level nodes sit at (0,0) | place right of the rightmost node |
| A TEXT component property's default belongs to the whole variant set, not to each variant | set per-variant text after `combineAsVariants` with `setProperties` on instances; a variant that must show other text ("…" while loading) unlinks that text from the property; on the Components page put a preview row of instances with real labels under each set, so a reviewer does not read the set default on every variant |
| Variables with the same name in two collections (a colour and a size) confuse name lookups | prefix by type (`color/…`, `size/…`) and look up with `getLocalVariablesAsync('COLOR')` / `('FLOAT')` |
| Constraints enum is `MIN`, `CENTER`, `MAX`, `STRETCH`, `SCALE` (`TOP_BOTTOM`, `LEFT_RIGHT` throw) | depth-block layers: `STRETCH` on both axes |
| Flips have no API shortcut | set `relativeTransform`; draw rotated highlight bars as SVG parallelograms instead of rotating rectangles |
| `figma.createVector()` can come with a default dark stroke | set `strokes = []` right after creating every vector (shine bars, facets, masks, lips), then add the stroke you want: in J002-T09 every shine bar first rendered as an outlined line |
| A frame with `clipsContent = true` cuts off any child that reaches outside it | button rows, popups and card frames that hold focus rings, glows or break-out art: `clipsContent = false`; clip only on a mask or an fx frame meant to clip (a popup's button row clipped every focus ring top and bottom in J002-T09) |
| `clone()` of a variant inside a set drops its `componentPropertyReferences` | after cloning variants (e.g. a new `Size=` axis), relink every TEXT / BOOLEAN / INSTANCE_SWAP reference and check an instance's props |
| A `use_figma` script that throws is rolled back completely | nothing from that call exists: re-read the canvas if unsure, then rerun the whole script without the failing line |
| Mutating calls run **one at a time**; read-only per-page discovery may fan out in parallel, one page switch per call | |
| On error obey `safeToRetryWithoutCanvasRead` (true: fix and retry; false: read the canvas first) | |
| Deliverables are editable layers; a flattened picture of the whole UI never counts as the design | matches `roblox-handoff.md`: only parts marked B are images |

## 4. The tutorials' moves as Plugin API
| Tutorial move | Plugin API |
| --- | --- |
| Frame 1920 × 1080 | `createFrame()` / `createAutoLayout()`, `resize(1920,1080)` |
| Rectangle, corner radius | `createRectangle()`, `cornerRadius` or `topLeftRadius`… |
| Custom silhouette (anime header, pixel ornament) | `createVector()` with `vectorPaths: [{windingRule:'NONZERO', data:'M … Z'}]` (SVG path data), or `createNodeFromSvg` |
| Vertical gradient | `{type:'GRADIENT_LINEAR', gradientStops:[{color:{r,g,b,a},position:0},…], gradientTransform:[[0,1,0],[-1,0,1]]}` (top→bottom; confirm in the screenshot) |
| Stroke inside / outside, weight, dashed, round join | `strokes`, `strokeWeight`, `strokeAlign 'INSIDE'|'OUTSIDE'|'CENTER'`, `dashPattern [a,b]`, `strokeJoin 'ROUND'` |
| Drop / inner shadow, glow, layer blur | `effects = [{type:'DROP_SHADOW'|'INNER_SHADOW', color:{r,g,b,a}, offset:{x,y}, radius, spread, visible:true, blendMode:'NORMAL'}]`, `{type:'LAYER_BLUR', radius, visible:true}`; glow = shadow at offset 0 |
| Blend mode | `node.blendMode = 'OVERLAY'|'SOFT_LIGHT'|'COLOR_DODGE'|'PLUS_LIGHTER'|'MULTIPLY'|'SCREEN'` (bake later) |
| Duplicate / flatten / group | `clone()`, `figma.flatten([a,b], parent)`, `figma.group([…], parent)` |
| Group mask | in a group, the bottom child `isMask = true` clips the children above it |
| Image tile fill | `{type:'IMAGE', imageHash, scaleMode:'TILE', scalingFactor}` |
| Align / spacing | auto layout `itemSpacing`, `padding*`, `primaryAxisAlignItems`; or compute x/y from parent bounds |
| Selection-colours recolour | traverse `node.query('*')` and swap matching paints (gradients included) |
| States | variants `State=Idle|Hover|Pressed|Disabled|Selected`, laid out in a grid |
| Vectorize bitmap plugin | not available via MCP: use an SVG, draw vectors, or bake the outline in a raster editor |

## 5. Reading back and exporting
- `get_screenshot(fileKey, nodeId, maxDimension)` → PNG url (curl it) for self-review and baked exports (`roblox-handoff.md` §3). `await node.screenshot()` inside `use_figma` returns an inline image.
- `get_metadata` for structure (hierarchy, bounds, names).
- Share the file link and node ids in the hand-back.

## 6. Motion prototypes (optional; figma-use-motion)
Figma can keyframe a node (`applyManualKeyframeTrack`, easing objects such as `{type:'EASE_OUT'}`, `EASE_IN_AND_OUT`, springs; durations in **seconds**) and apply animation styles. The API may not be enabled for the account: on `"… is not a supported API"` stop and say so. Never animate the top-level frame itself. Screenshots show only the resting state; to check motion use `export_video` (slow, costly: small width, low fps, 4-6 frames you need) and extract frames with ffmpeg. Values stay PROPOSAL (`ui-design/references/motion.md`).

## 7. Limits
- View settings (pixel grid, pixel preview, snap to pixel grid) are the owner's app settings; the API cannot switch them. For pixel work keep every x, y, width, height and stroke an integer and ask the owner to switch them on.
- Plugins (vectorize, remove background) cannot run through MCP.
- `generate_image` (Figma AI credits) is used only when the owner asks; ChatGPT in the built-in browser is the default (`reference-images` §4) (`image-generation.md` §1). Tell the owner how many images each route used.
