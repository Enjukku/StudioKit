> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-design`. Paper notes: `knowledge/reference/modeling/03-*.md` (ENV ids), `01-*.md` (CS2, CS8-CS10). Placement, terrain and lighting belong to the environment designer (`environment-design`). Revised by J018 maker modeler · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): pieces that live in a place (§6).

# Buildings, kits and environment pieces

## 1. Who does what
The modeler makes every **reusable** asset: kit pieces, props, plants, hero buildings, anything rigged. The environment designer places them, builds terrain, one-off landforms and light (`environment-design` "who owns what"; `environment-craft/references/blender-to-studio.md`). New pieces are asked for with a brief (`environment-craft/references/handoffs.md` §3).

## 2. A kit has an interface contract before the first piece (ENV03, ENV12 [O])
| Field | Example of what to write |
| --- | --- |
| Grid and module size | from player clearance and gameplay sizes; a project choice, not a universal stud count (RT9-1) |
| Snap origin | corner or base anchor for grid pieces; hinge origins on moving parts (ENV08 [V] B17, ENV09) |
| Forward and up axes | stated once for the whole kit |
| Neighbours | which pieces must meet which (wall-wall, wall-corner, wall-roof, floor-stair) |
| Trim and texture direction | which way trims and tiles run, shared texel scale |
| View | playable interior, closed shell, camera cutaway or breakable: this decides which backs exist (ENV16) |

## 3. Build order
1. **Test assembly first** (ENV02, ENV13 [O]): a straight wall, outside and inside corners, a door and a window opening, floor and ceiling, a height change, a roof join. Judge the assembled corners, never pieces alone (ENV04). Typical failures: wall thickness or trim eats the neighbour's space at a corner; a roof slope leaves a gap against another module (ENV14).
2. **Openings at real player size** (ENV10, ENV15 [O]): the visible arch, the collision opening and the camera path must agree. Test with the player dummy.
3. **Big shapes carry the read, small trims carry detail** (ENV05 [O]); keep entrances, floors, hazards and walkable space readable at the game camera before dressing (ENV17).
4. **Variants on purpose** (ENV19, ENV06 [O]): a new mesh only when silhouette, function or story changes; colour or wear → tint or material. Mirrored variants are not free: check texture direction and collision (ENV21).
5. **Canonical vs placed** (ENV20 [O]): keep the canonical asset apart from placed copies, so a fix spreads on purpose. Upload once; duplicate in Studio (budgets §5).

## 3a. Kit lessons from the second game (FM48-FM57 [E]/owner)
- **Pilot, then copy**: build one member of a kit, get it approved, then build the rest "the same way" from data, one entry per variant (FM17, owner, first game).
- Derive module sizes from every size the game can make, not from one example (FM48).
- A mesh cannot stretch on one axis without stretching its detail: model the surface skin, and scale the plain inside as a primitive (FM49).
- Tall or deep kits: a bottom support zone, a repeating middle, a finished top (FM50).
- Make seams symmetric about the module edge so any two neighbours join flush, no gap, no z-fight; test two side by side (FM51).
- Bigger stacked pieces cut part count but repeat their painted detail: use two or more paint variants per tier (FM52).
- A blockout proves sizes and joins; it is not the look (FM53). The accepted rebuild had real modelled detail (chamfers, recessed panels, framed trims), one atlas at equal texel density, and paint baked with the neighbours in place (FM54).
- Never change an approved mesh to fix a placement problem; change the placement data (FM57, owner, first game).
- Budget the assembled worst case (total triangles, parts, unique meshes) and measure the heaviest assembly in Studio; record estimate and measurement side by side (FM43-FM44).

## 4. Style rules for built things (CS8, ENV18 [O])
Lean, sag and wear follow one written reason (age, weight, material), not random rotation of every module; mating edges stay usable. Exaggeration keeps doors, floor levels and collision honest (CS8-c).

## 5. Do not
- Delete hidden faces only because the beauty camera cannot see them; collision, shadows and other cameras may (ENV16, CS9-c [O]).
- Copy another game's module size, camera scale or cut-down factor (CS9-a: one sample's numbers, not a standard).
- Assume a Blender linked duplicate or an atlas means one draw call (budgets §5).

## 6. Pieces that live in a place
The environment is the backdrop: routes, cover, hazards and objectives read before decoration. Kit pieces and props serve that read. Every Check below that applies is a line of your self-review (`review.md` §5 GR5).
| Standard | How | Check |
| --- | --- | --- |
| Art stays inside the blockout's gameplay | import the approved greybox into Blender at its world origin and scale and build on the same snap grid; bespoke shells export at their world position (importer: Set Pivot to Scene Origin off), reusable kit pieces export at their snap origin (§2) and the environment designer places them; collision, cover and sightlines never move without the level designer's sign-off | art bounding boxes vs blockout parts differ by less than one snap step |
| Backdrop pieces are calm | environment pieces sit in the environment value band (no pure black, no reserved hues) with lower saturation than characters; detail clusters above head height or at edges, the player band calm | `review.md` §5 VL5 on a capture with a character in front; CL2 on the colour render (the place's own reserved-hue share is the art director's check on the environment-only capture) |
| One shape vocabulary | rocks, trims and ornaments use the game's shape family (for example knife-like rocks, rectangular trims) | silhouette sheet of the set: one family dominates |
| Size steps in groups | rocks, crystals, plants and debris ship as big, medium and small pieces, never three of one size | `review.md` §5 SL4 |
| Backdrop gesture | plants and backdrop props: simple surfaces and a few triangles, but a clear, elegant curve that reads from afar; grass cards only a few, at edges and rest areas, never over play floors | black-fill: each plant is a clear curve, not a blob |
| No visible duplicates | pieces are built to read differently when rotated; two or more variants per repeated piece; a bespoke layout gets unique shells sharing one trim sheet instead of a forced kit | in a game-camera capture no piece shows twice at the same angle |
| Trim sheets | one trim sheet with a normal map per environment family; a boring strip is fixed by remapping UVs to another strip, not by modelling more | texture sets per environment counted; a side-lit capture shows the normal detail |
| Grounding | the standard in `read-and-form.md` §8; for set pieces, leave room for the environment designer's blend (paint, decal, debris) | `review.md` §5 GR1 |
| Story through use and time | each hero prop carries 1-2 history facts (age, who uses it, what happened) as wear, chips, repairs or burial, at a size the game camera reads | a cold read of the capture names one history fact |
| Theme cues | 2-3 signature materials or shapes of the setting appear on its pieces so the place is not generic (crystals in the rocks of a space desert) | a cold read names the theme without UI |
| Identity symbols and landmarks | zone symbols (a statue, a banner shape) read in black-fill and are the tallest, clearest shape where they mark a goal; objective floors are their own piece with a border trim | black-fill of the level view: the landmark is the tallest shape |
| Head-height cues | long sightline walls carry a trim or ledge line at the character's eye height (measured in Studio) where the level designer asks for one | the line sits at the measured eye height |
| Hazards explain themselves | a hazard piece shows its source and believable containment (rails, fences, a darker rim) | your cold read of one capture says where the hazard comes from |
| Materials follow gameplay | the standard in `read-and-form.md` §8; floors match their footstep material in the sound table; an interactive surface reads its use the same way everywhere (a climbable ledge looks like a ledge) | `review.md` §5 GR4 |
| Predictable geometry | the standard in `read-and-form.md` §8; height changes only where the level plan lists them | Studio collision view; a walk along each route finds no snag |
| Judge it in the whole set | the standard in `read-and-form.md` §8; the assembled capture has a player and known-size objects in frame | `review.md` §5 GR3 |
