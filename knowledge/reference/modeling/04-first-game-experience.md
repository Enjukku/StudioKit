---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J007-T04, DestructionSimulator + GreatWallSim (read-only)"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# First-game experience with models (kit-neutral lessons)

Paraphrased notes from two earlier games. Rows are evidence for the modeler, not rules; a row becomes a rule only when the lead or the owner promotes it. Owner words are word for word and short, each with a decision id and date or a file:line. Rigging lessons the rigger already has stay in `knowledge/reference/rigging/03-first-game-experience.md` and are cited by FG id, not repeated.

## 0. How to read

| Key | Meaning |
| --- | --- |
| DS | the first game (a destruction game; folder DestructionSimulator). Paths are inside that folder. |
| GW | the second game (folder GreatWallSim). Paths are inside that folder. |
| FM01... | row id in this note, in reading order. |
| Tag | EXPERIENCE = something that happened or was measured. OWNER = an owner decision or correction (word for word where a quote is given). OPINION = an agent's rule or proposal that was written down but not tested by the owner or by a measurement. |
| game-specific? | no, or yes / partly with what was removed from the lesson. |
| applies to | hand (hand-built in Blender), Tripo (image-to-3D), kit (modular pieces), import (export and Studio), review, hand-off, budget. |
| Numbers | every number keeps its unit and context and is marked "first-game value, not a kit rule" unless an owner decision made it general. Owner decision J007-D5 (20,000 triangles per mesh is only the upload ceiling; creatures and characters under about 7,000) is the only general budget here. |
| Files read | DS: .claude/agents/content-builder.md; .agents/skills/brick-builder/ (SKILL.md, reference.md); .agents/skills/art-fundamentals/SKILL.md; content/art/refs/model/*.json (19 files); content/art/anchors/model; knowledge/design/decisions.md; tried-and-failed.md rows F-012, F-018. GW: knowledge/design/ model-list, hero-assets-import, dam-section-kit, characters, secret-hero, asset-hookup-audit, decisions; knowledge/logs/ three logs; knowledge/systems/ dam-section-kit and environment-import; art/style-locks.md; art/models/README.md; tried-and-failed.md row TF-MAPCOL1. |

## 1. Reference images and locks

How the first games made, wrote down and recorded the images a model starts from.

| id | lesson | evidence | tag | game-specific? | applies to |
| --- | --- | --- | --- | --- | --- |
| FM01 | A model is built from an owner-approved reference image that exists first. Builds started without one were rejected as poorly built, although colours and style were fine. | GW D-008 2026-10-16 (decisions.md:16): "it's poorly built"; "I need you to generate reference photos with ChatGPT" | OWNER | no | hand, review |
| FM02 | Say what the model must NOT look like. A style described only by what it is drifted to the nearest cliche and was rejected. Every lock the studio wrote afterwards carries a "NOT ..." clause. | GW D-012 2026-10-16 (decisions.md:20): "you made them look like they are Legos"; GW art/style-locks.md:21, :33, :37, :41 | OWNER | yes: removed the toy-brick and stud style and its flair rules | hand, Tripo |
| FM03 | Keep model locks as named text blocks that a tool reads by their first words, one block per use (multi-view sheet, single subject for image-to-3D, character, environment). A lock states: number and angle of views, background, light, scale figure, "no text, no labels, no logos", nothing floating, symmetric where the real thing is. | GW art/style-locks.md:6, :21, :33, :41; DS content/art/refs/model/king_model_p8.json (lock text stored inside the prompt) | EXPERIENCE | yes: removed the actual style words | hand, Tripo |
| FM04 | Use two locks for two jobs. Hand-building gets a 2x2 sheet of the same object (front, side, back, high three-quarter; near-orthographic; scale figure; the 2x2 layout is a first-game value, not a kit rule). Image-to-3D gets one subject in one view. | GW art/style-locks.md:21 against :41; DS D-153 (decisions.md:163) | EXPERIENCE | no | hand, Tripo |
| FM05 | An image-to-3D reference shows exactly one subject in one view, in an open stance with nothing overlapping, on a plain background, with no props, effects or extra views. Extra views made the tool build extra models. The subject fills about 85% of the frame (first-game value, not a kit rule). | DS D-153 2026-10-11 (decisions.md:163): "the extra angles just make it make other models"; "it should probably be T posing"; DS refs/model/king_model_hp.json | OWNER | no | Tripo |
| FM06 | Turn the subject so anything attached to the back (tail, cape, pack) shows. The first reference set used about 20 degrees and was moved to about 40 degrees (first-game value, not a kit rule). | DS D-155 2026-10-11 (decisions.md:165); DS refs/model/golem_model.json (20 degrees) against king_model_hp.json (40 degrees) | OWNER | no | Tripo |
| FM07 | When several subjects share one world, put one shared style lock on all of them. Subjects made one by one looked like different worlds. | DS D-153 2026-10-11 (decisions.md:163): "they don't look like they exist in the same world" | OWNER | partly: removed the cast and its toy-line style | Tripo, review |
| FM08 | When the style is undecided, render the same subject in several candidate styles and let the owner pick one. Store the pick as an anchor image and attach it as an input to every later reference. | DS D-155 2026-10-11 (decisions.md:165): "I like style one the best"; the pick is an input image in DS refs/model/king_model_hp.json and king_model_p8.json | OWNER | yes: removed the style names | Tripo, review |
| FM09 | A reference gives shape and design. The look can be applied later in the 3D tool; the owner asked only for the reference image. | DS D-150 2026-10-11 (decisions.md:160): "I would just need the reference photo" | OWNER | yes: removed the character | hand, Tripo |
| FM10 | Refine a reference by locking it. Attach the last good image, say "keep it exactly the same", change one thing per pass, and fix proportions before face and detail. One subject needed 12 recorded passes (first-game value, not a kit rule). | DS refs/model/king_model_p3.json ("PROPORTIONS ARE THE PRIORITY"), king_model_p5.json to king_model_p8.json ("Change ONLY ...") | EXPERIENCE | yes: removed the character and its face details | Tripo, hand |
| FM11 | Record each reference beside its image: id, family, full prompt, input images, tool session id, source path, seconds. Keep an anchors folder for approved images and a rejected folder for rejected ones. | DS content/art/refs/model/*.json (19 files); DS content/art/anchors/model/; DS content/art/refs/_rejected/; GW characters.md:23 (rejected sheets kept in a folder) | EXPERIENCE | no | review, hand-off |
| FM12 | For a subject that exists in the real world, real photos and measured drawings are the primary reference. An AI image of a known place came out inaccurate (wrong colours, odd shapes) and served only as a style hint. | DS D-164 2026-10-11 (decisions.md:174): "I would prioritize our real references"; "the ChatGPT White House ... is not very accurate" | OWNER | partly: removed the place names | hand, review |

## 2. Owner gates and what the owner approved

How approval was asked for and given, and what the owner removed or kept.

| id | lesson | evidence | tag | game-specific? | applies to |
| --- | --- | --- | --- | --- | --- |
| FM13 | Approval comes per batch of reference sheets; the whole approved batch is then built. | GW D-014 2026-10-16 (decisions.md:22): "Approve batch 2. Start building the props in Blender in this style."; D-053 (decisions.md:61): "these references are really good." | OWNER | no | hand-off |
| FM14 | A sheet whose shape or size is wrong goes back before any build. The corrected sheet is shown to the owner first. | GW D-062 2026-10-16 (decisions.md:70): "that's not how a lantern post should be and it's also way too short"; D-046 (decisions.md:54): a sheet rejected because the object did not read as the real thing | OWNER | yes: removed the object names | review, hand-off |
| FM15 | A large structure gets a measured plan (floor plans, views, a player figure for scale) approved before building. A first set built without plans was rejected as miniatures with cramped interiors. | DS D-091 2026-10-04 (decisions.md:101): "you might have to start doing it like blueprint style"; "it's almost like you're making a miniature on purpose rather than making it the real size"; DS tried-and-failed.md:24 (F-012) | OWNER | partly: removed the building type | hand, review |
| FM16 | The size factor over real life is the owner's choice. Record it once and apply it to every model. First game: buildings 1.5 x real size, furniture about 1.2 x (first-game value, not a kit rule). | DS D-091 (decisions.md:101); DS brick-builder/reference.md:24 | OWNER | yes: removed the game and its brick scale | hand, budget |
| FM17 | Pilot then copy. Build one member of a kit from scratch, get it approved, then build each next member "the same way" with a pipeline driven by data (one entry per variant plus any new part builder). | GW D-155 2026-10-19 (decisions.md:163): "Dam 2 looks good. Build theme 3 (ancient Egypt / Anubis) the same way."; GW dam-section-kit.md:186-192 | OWNER | yes: removed the kit subject | kit, hand-off |
| FM18 | The owner cuts detail that costs triangles without helping the read, and prefers plain primitives to modelled micro-detail. | GW D-157 2026-10-19 (decisions.md:165): "That's probably a lot of triangles that aren't necessarily needed."; DS D-043 2026-09-30 (decisions.md:52, no quote): modelled studs are "unnecessary triangles" | OWNER | yes: removed the ornament and stud details | budget, hand |
| FM19 | Choose each variant's ornament from the subject's own material or theme. A generic industrial rail-and-post set repeated on every variant was rejected. | GW D-142 2026-10-18 (decisions.md:150): "the fences, you keep keeping it industrial. Make it more befitting of the theme of the material" | OWNER | yes: removed the themes | kit, review |
| FM20 | Variants differ in design, driven by material, not only in colour. Use engine built-in materials for lower tiers and custom materials only for the top tiers. | GW D-140 2026-10-18 (decisions.md:148): "you need a different dam design for each one"; "It should be based on the material"; "only our higher tier walls probably need it" | OWNER | yes: removed the subject | kit, budget |
| FM21 | A prop that copied the reference game's styling was rejected when it did not fit the game's own theme. Take style from the game's own lock, not from a teardown of another game. | GW D-054 2026-10-16 (decisions.md:62): "That doesn't really make sense for a game." | OWNER | yes: removed the theme | review |
| FM22 | Keep an approved simple placeholder when the owner likes it. Do not replace it with a modelled version. | GW D-052 2026-10-16 (decisions.md:60): "nice and simple" | OWNER | yes: removed the object | hand-off |
| FM23 | The owner may make the Tripo model himself from a clean single image. The modeler's work then starts at splitting, cleaning and rigging. This matches the J007 decision that the owner runs Tripo. | GW D-069 2026-10-16 (decisions.md:77, decision text); GW D-148 2026-10-18 (decisions.md:156): "I'm going to have both models built in Tripo"; GW secret-hero.md:23 | OWNER | partly: removed the characters | Tripo, hand-off |

## 3. Hand-building

The earlier builder's method and what the owner kept rejecting. Rows from the two art skills are rules the first games wrote down, tagged OPINION.

| id | lesson | evidence | tag | game-specific? | applies to |
| --- | --- | --- | --- | --- | --- |
| FM24 | Proxy first. Block out proportions and silhouette at the game camera before detail, because changes are cheap then. Use the greybox render as an input to image generation so reference sheets match measured size. | DS brick-builder/SKILL.md:15; DS art-fundamentals/SKILL.md:42; DS D-072 (decisions.md:80) | OPINION | partly: removed the brick compile step | hand |
| FM25 | List the required views per object and run a check that stops work when one is missing (opposite three-quarter views, four sides, top, plan per floor, one interior per room, cutaway for multi-storey). | DS brick-builder/SKILL.md:16; DS D-072 (decisions.md:80) | OPINION | partly: floor and room views are building-specific | hand, review |
| FM26 | Measure the reference before modelling. Overlay a unit grid on each orthographic sheet and write footprint, heights and openings into the brief. | DS brick-builder/SKILL.md:17 | OPINION | partly: removed the brick-grid units | hand |
| FM27 | Score outline match against the reference per view and write one verdict line per view. First-game floor: overlap 0.85 on every orthographic view (first-game value, not a kit rule). The number checks the outline only, so it is a floor and not the finish. | DS brick-builder/SKILL.md:27 | EXPERIENCE | partly: removed the tool name | hand, review |
| FM28 | After the number passes, check by eye what the owner has rejected before: scale, detail fitted to use, facing of directional pieces, organic shapes built boxy. Polish rounds that fix these are wanted. | DS content-builder.md:16; DS brick-builder/SKILL.md:27; DS D-130 2026-10-10 (decisions.md:140): "The builder agent, further polishing rounds is good" | OWNER | partly: removed the brick specifics | hand, review |
| FM29 | Cap the loop. First-game stop rule: 6 rounds to reach the floor plus up to 3 polish rounds, then return the remaining differences and the last compare file (first-game value, not a kit rule). | DS content-builder.md:18; DS brick-builder/SKILL.md:28 | OPINION | no | hand, hand-off |
| FM30 | Edit the source (blueprint, script, model.py), never the exported output by hand. Re-render only the views that changed. | DS brick-builder/SKILL.md:28; GW characters.md:60; GW dam-section-kit.md:166 (one command rebuilds everything) | EXPERIENCE | no | hand |
| FM31 | Build next to a player-sized reference. Touch points (doors, stairs, rails, seats) sit at player scale; a room built without a reference ends with giant furniture. | DS art-fundamentals/SKILL.md:47; DS brick-builder/SKILL.md:39 | OPINION | no | hand, review |
| FM32 | The owner's repeated rejections of structure models: too small, furniture too coarse for the room, directional pieces facing the wrong way (wedges, carpets, lecterns), boxy shapes where the art is organic. Check each in the render before hand-off. | DS content-builder.md:16; DS D-091 (decisions.md:101) | OWNER | partly: removed the building types | hand, review |
| FM33 | Name 2-3 iconic traits per object in the brief (2-3 is a first-game value, not a kit rule). They must still read in a render at the real camera distance; spend detail there and keep large calm surfaces elsewhere. | DS brick-builder/SKILL.md:38; DS art-fundamentals/SKILL.md:39-40 | OPINION | no | hand, review |
| FM34 | Judge silhouette as a solid black shape at the real camera angle and at phone size. If two different things share a silhouette, change one. | DS art-fundamentals/SKILL.md:35, :40 | OPINION | no | review |
| FM35 | Test the extreme poses of a design before polishing it (collars, scarves, plates that block an arm raise). Modular pieces should look different when rotated, mirrored, scaled or recoloured, yet not be spotted as copies. What a thing looks like should match how it behaves. | DS art-fundamentals/SKILL.md:43, :49, :50 | OPINION | no | hand, kit, review |
| FM36 | Held props and accessories must read from the front at game view. A first prop did not read and a second was hidden; redo size and angle until it reads. | GW characters.md:85 (owner review 2026-10-16) | OWNER | yes: removed the props | hand, review |
| FM37 | Accessories on a head must look right from the side. Fit the dome to the head top and mount it as an accessory so it scales with the head. | GW characters.md:77 (owner hat note), :83 | OWNER | partly: removed the hats | hand, import |
| FM38 | Where a moving limb holds a prop, put joint covers centred on the pivots so the limb does not come off the body when it turns. | GW characters.md:84 (owner review 2026-10-16) | OWNER | yes: removed the character | hand |
| FM39 | A rideable model needs a cut-out for the rider and a seat at the rider's sit height. Render a seated test figure from high and side views as a standing QA step. | GW characters.md:87-89 (owner review 2026-10-16) | OWNER | partly: removed the vehicles | hand, review |
| FM40 | After a rig fix, an animator review found props and accessories clipping the body and props that did not scale with a scaled-up form. Check clearance in the key poses and scale props with the form. | GW characters.md:103; GW D-098 2026-10-17 (decisions.md:106, decision text) | EXPERIENCE | yes: removed the characters | review, hand |

## 4. Generated meshes (Tripo)

Only what is new. Fused limbs, open shells, variants by bending, one atlas shared by cut parts and the separate-parts method are already in the rigging note as FG01-FG14 and are not repeated here.

| id | lesson | evidence | tag | game-specific? | applies to |
| --- | --- | --- | --- | --- | --- |
| FM41 | When a generated mesh fuses several repeated limbs, building one clean limb and copying it was chosen over cutting the fused ones apart or redoing them by hand. | DS D-167 2026-10-11 (decisions.md:177): chose "One clean arm, copied 6x" | OWNER | yes: removed the character | Tripo, hand |

## 5. Budget and detail

Fixed by the owner (J007-D5, 2026-10-21): 20,000 triangles per mesh is only the Roblox upload ceiling, not a target; creatures and characters stay under about 7,000. Owner words: "we should probably keep it like under 7k or whatever" (StudioKit J007 decisions.md, J007-D5). All first-game numbers below are context only.

| id | lesson | evidence | tag | game-specific? | applies to |
| --- | --- | --- | --- | --- | --- |
| FM42 | First-game triangle counts per kind, for scale only: hero body sets 2,828-4,902 triangles, rigid vehicles 2,376-4,152, props 152-6,380; proposed prop targets under 2,000 and under 500 for repeated pieces (first-game value, not a kit rule). No single character passed 7,000. | GW characters.md:63-76; GW art/models/README.md (props table); GW model-list.md:5 | EXPERIENCE | no | budget |
| FM43 | A repeated kit needs a budget for the assembled worst case, not only per mesh: total triangles, mesh parts and unique meshes, then a Studio measurement of the heaviest assembly. First game: planned about 100k triangles and 320 parts, built 70.6k and 487, measured +68.7k triangles, +18 draw batches, 458 instances (first-game value, not a kit rule). | GW dam-section-kit.md:82, :182; GW logs/2026-10-20-dam-kit-swap.md:13 | EXPERIENCE | yes: removed the kit subject | budget, kit |
| FM44 | Estimates drift. The part count came out about 50% above the plan (first-game value, not a kit rule) because every stack step was one unit (no greedy merge); merging would have repeated the paint. Record the estimate and the measured value side by side. | GW dam-section-kit.md:53, :82, :182 | EXPERIENCE | yes: removed the kit subject | budget, kit |
| FM45 | Texture memory: one 1024 x 1024 colour atlas per variant set is about 4 MB uncompressed and 0.7-1.4 MB compressed (first-game value, not a kit rule). Keep only the current variant resident and preload the next one late. The first atlas section added +1.3 MB in Studio. | GW dam-section-kit.md:139, :344-345; GW logs/2026-10-20-dam-kit-swap.md:14 | EXPERIENCE | yes: removed the kit subject | budget, import |
| FM46 | Do not send every variant to every client. The first plan shipped all ten sets at join; the build keeps variants in server storage and replicates only the current one, with the next one preloaded on the server. | GW dam-section-kit.md:101, :327; GW systems/dam-section-kit.md:11; GW logs/2026-10-20-dam-kit-swap.md:8 | EXPERIENCE | yes: removed the kit subject | import, budget |
| FM47 | Skip normal and roughness maps when the painted look does not need them; the saving is memory. The character sets in the same game used all five maps, so choose per kind. | GW dam-section-kit.md:139; GW characters.md:83 | OPINION | no | budget |

## 6. Kits and modular reuse

Lessons from one section kit of 22-25 pieces per variant, ten variants, built 2026-10-18 to 2026-10-19.

| id | lesson | evidence | tag | game-specific? | applies to |
| --- | --- | --- | --- | --- | --- |
| FM48 | Derive module sizes from the whole table of sizes the game can make, not from one example. The kit must work for every size in the range. | GW dam-section-kit.md:25-35; GW D-135 2026-10-18 (decisions.md:143): "Based on the sizing of the wall" | OWNER | yes: removed the kit subject | kit |
| FM49 | Model only the surface skin and scale the plain interior as a primitive part, because a mesh cannot stretch along one axis without stretching its detail. | GW dam-section-kit.md:39-47, :61-67; GW logs/2026-10-20-dam-kit-swap.md:11-13 | EXPERIENCE | yes: removed the kit subject | kit |
| FM50 | Split a tall or deep kit into three zones: support at the bottom, a repeating middle, a finish at the top. The owner described it this way and it became the piece list. | GW dam-section-kit.md:5 (D-135 2026-10-18): "The middle is the other stuff. And then the top has the railing." | OWNER | yes: removed the kit subject | kit |
| FM51 | Make seams symmetric about the module edge (a half piece on each side, mirrored) so any two neighbours join whichever finishes first. Test two side by side: halves met flush, no gap, no z-fight. | GW dam-section-kit.md:65, :177, :375 | EXPERIENCE | yes: removed the kit subject | kit, import |
| FM52 | Stack by whole units with larger pieces to cut part count, but a piece repeated at many heights repeats its painted detail. Use two or more paint variants per tier and a setback every few units on tall stacks. | GW dam-section-kit.md:53, :178, :180, :275 | EXPERIENCE | yes: removed the kit subject | kit |
| FM53 | A blockout proves sizes and joins. It is not the look: flat boxes and a procedurally painted atlas were rejected as flat and stretched, and the owner asked for a restart. | GW dam-section-kit.md:128, :132 (2026-10-18): "I want details, and I want it to look really nice."; :160: "retry ... from scratch" | OWNER | yes: removed the kit subject | kit, review |
| FM54 | The accepted rebuild modelled real detail (chamfers, recessed panels, framed trims), unwrapped each piece at equal texel density into one atlas, and baked the paint with the neighbouring pieces in the scene so stacked occlusion matches. | GW dam-section-kit.md:171-177 | EXPERIENCE | yes: removed the kit subject | kit, hand |
| FM55 | Run a review loop per variant before the owner sees it: build, render side by side with the reference at the same angle, art-director review, fix. All ten variants needed fixes after the first review. | GW dam-section-kit.md:141, :184, :196, :209, :219, :232, :244, :254, :264, :275, :286 | EXPERIENCE | yes: removed the kit subject | kit, review |
| FM56 | The same defects came back in every variant: low value range, small marks read as something else at distance, detail too small at phone size, blown highlights (29% of pixels above 235 in one render; first-game value, not a kit rule), a variant too close in value to an earlier one. Check these by number first. | GW dam-section-kit.md:209, :219, :232, :244, :254, :264, :275 | EXPERIENCE | yes: removed the variant names | review |
| FM57 | Do not change an approved mesh to fix a placement problem. Change the placement data. | GW D-171 2026-10-20 (decisions.md:179): "We don't need to change the models or meshes of the dams"; "We just need to change the ladder position." | OWNER | yes: removed the subject | kit, hand-off |
| FM58 | Plan mirrored copies at export time. The first build concluded that a mesh part cannot be mirrored in place, so one end of the kit had no cap until a mirrored copy is uploaded (first-game claim, not verified here). | GW systems/dam-section-kit.md:17; GW dam-section-kit.md:336 | EXPERIENCE | yes: removed the kit subject | kit, import |
| FM59 | Keep colour variation of a repeated mesh cheap: the same mesh with a colour or material swap per tier, plus a tint applied in game. | GW model-list.md:15, :53; GW dam-section-kit.md:184 | OPINION | yes: removed the tiers | kit, budget |

## 7. Textures and surfaces

| id | lesson | evidence | tag | game-specific? | applies to |
| --- | --- | --- | --- | --- | --- |
| FM60 | A painted look needs both real modelled detail and a baked painted texture. Parts with colours from data alone were replaced by one colour atlas per variant set. Glow parts stay separate emissive parts and are not baked into the atlas. | GW dam-section-kit.md:66 against :130-141, :157 | EXPERIENCE | yes: removed the kit subject | hand, kit |
| FM61 | A model that looks plain draws owner asks for more painting and texturing. Put a texture pass in the plan. | GW D-081 2026-10-17 (decisions.md:89): "do some more like painting and texturing to make it look a little more interesting"; GW characters.md:83 (owner note on textures and shine) | OWNER | yes: removed the objects | hand |
| FM62 | Back faces are culled in Roblox. Panels that faced into the shape were invisible in game although Blender renders showed them. Faces closer than about 0.4 stud to another surface z-fight at distance (first-game value, not a kit rule). Check face direction in the engine. | GW dam-section-kit.md:198 | EXPERIENCE | no | hand, import |
| FM63 | Check a procedural pattern generator's real output scale against the number requested. The first game's generator drew its tiles at about half the size given. | GW dam-section-kit.md:220 (the Blender Brick node) | EXPERIENCE | no | hand |
| FM64 | A body-part texture can keep alpha 0 cells so the player's own skin colour shows through (alpha mode Overlay on avatar parts). | GW hero-assets-import.md:16; GW characters.md:83 | EXPERIENCE | no | import |

## 8. Export, import and Studio checks

| id | lesson | evidence | tag | game-specific? | applies to |
| --- | --- | --- | --- | --- | --- |
| FM65 | Use 1 Blender unit = 1 stud and apply all scale before export. Axis map: Roblox (x, y, z) = (-Blender X, Blender Z, Blender Y); a model's Blender front (-Y) faces Roblox -Z. Checked on the first imports (first-game convention, not a kit rule). | GW environment-import.md:19-22; GW dam-section-kit.md:374 | EXPERIENCE | no | import, hand |
| FM66 | The first import is a pilot check of axes, scale, joints and pivots. The plan listed FBX import as unverified until one piece went in. | GW dam-section-kit.md:120, :374-376 | EXPERIENCE | no | import |
| FM67 | Imported mesh parts arrive with an empty TextureID and default collision settings. Set both explicitly, at runtime or in the template. | GW dam-section-kit.md:376 | EXPERIENCE | no | import |
| FM68 | Uploading a texture returns a Decal asset id; MeshPart.TextureID needs the image id behind it. Read it from the loaded Decal and store it. Test moderation by preloading through a temporary instance, because a bare id string failed in Edit even for known-good textures. | GW dam-section-kit.md:321, :372-373 | EXPERIENCE | no | import |
| FM69 | Plain material colours may be lost on import. The first-game importer read base colour from the .blend and treated textured objects as keeping their texture (first-game claim, not verified here). | GW environment-import.md:11, :37 | OPINION | no | import |
| FM70 | Importer contract for large scene pieces: unique mesh names per piece, one material per object, no coplanar faces across objects (offset at least 0.05 stud; first-game value, not a kit rule), a separate low-poly collision object for walkable ground, a naming mark for render-only objects, placements as base-centre position plus yaw plus uniform scale. | GW environment-import.md:36-39, :41-50 | OPINION | partly: removed tile sizes and tool names | import, hand-off |
| FM71 | Walkable and colliding meshes keep Default collision fidelity. Merged multi-piece meshes use PreciseConvexDecomposition. Box or Hull only on parts nobody collides with. Test with foot-height checks, not surface tops only. | GW D-170 2026-10-20 (decisions.md:178): "make these ones have more accurate collisions"; GW tried-and-failed.md:14 (TF-MAPCOL1): "you're floating. A lot of the quarry, you can float." | OWNER | partly: removed the map pieces | import, budget |
| FM72 | Do not turn CastShadow off as a speed trick without a measurement. The first game's attempt saved 0.3-0.8 ms render CPU on desktop (first-game value, not a kit rule), popped shadows and was dropped. | DS tried-and-failed.md:11 (F-018), owner 2026-10-10: "why not just leave the Roblox lighting and shadow settings? Why are we inventing our own stuff?" | OWNER | no | import, budget |
| FM73 | Read the matching engine docs page before making anything that becomes an Instance. Build the engine's way unless it is measurably worse, and list "docs read" in the hand-back. | DS D-128 2026-10-09 (decisions.md:138): "we shouldn't just settle for what works"; "we don't overcomplicate work that could have been simplified using pre-existing mechanics"; DS content-builder.md:19 | OWNER | no | import, hand-off |
| FM74 | Decorative kit meshes: collision, query and touch off, one invisible collider per module, RenderFidelity Automatic. These were plan values checked by the gate, not by a Studio collision test. | GW dam-section-kit.md:97, :333; GW systems/dam-section-kit.md:13 | OPINION | yes: removed the kit subject | import, budget |
| FM75 | Name the parts of the target rig exactly, keep the standard attachments, and write the folder layout the code expects as a table (name, class, rule). | GW hero-assets-import.md:9-14 | EXPERIENCE | partly: removed the hero ids | import, hand-off |
| FM76 | Keep seat, pivot and effect points in one stats file per model in Blender floor space, with the mapping to Roblox written beside them in the import list. | GW hero-assets-import.md:36-47; GW characters.md:60 | EXPERIENCE | no | import, hand-off |
| FM77 | Import can leave rig attachments offset from their joints (all 2.0 studs high in one case) because the exporter moved bones but not meshes. Parts then assemble as a pile. Fix with a one-off place tool plus a runtime guard that checks each joint sits inside its child part's box and both sides agree (tolerances 0.3 and 0.05 stud; first-game value, not a kit rule). | GW characters.md:97-100 | EXPERIENCE | partly: removed the hero names | import |
| FM78 | Never apply an exporter fix and a place fix together; the model then sits 2 studs low (first-game value, not a kit rule). Make the fix tool idempotent and let it move only the models that fail. | GW characters.md:99 | EXPERIENCE | no | import |
| FM79 | Swapping a body part at runtime can disconnect the neck and kill the player: 6 of 28 direct switches in Studio, until the neck requirement was turned off (first-game value, not a kit rule). | GW characters.md:105 | EXPERIENCE | no | import |
| FM80 | Imported vehicle joints arrive flat (parent = root, pivot at the mesh centre) while animation clips expect a hierarchy with pivots on the bones. Repair in the place from bone data and verify with a read-only script that matches every clip pose pair to the rig. Bone names from the FBX do not reach the clips; clips use pose names. (Rigger overlap.) | GW characters.md:102; GW logs/2026-10-17-hero-vehicle-rigs.md:8-10, :16-17, :24-26 | EXPERIENCE | partly: removed the vehicles | import, hand-off |
| FM81 | A capture with a camera override did not redraw joint changes on anchored copies and showed a stale rest pose. Re-shoot with the pose baked into parts. A capture alone is not proof; back it with numbers. | GW logs/2026-10-17-hero-vehicle-rigs.md:28 | EXPERIENCE | no | review |

## 9. Review and hand-off

| id | lesson | evidence | tag | game-specific? | applies to |
| --- | --- | --- | --- | --- | --- |
| FM82 | Review render set per model: front, side, back, high three-quarter and player-eye views plus a grey 5-stud figure for scale (first-game value, not a kit rule). Under the owner's light-check rule (J007-D7) this is one set per hand-off, taken after the numbers pass. | GW characters.md:44; GW art/models/README.md:68 | EXPERIENCE | no | review |
| FM83 | Builders that run in parallel check offline and do not drive Studio. One operator does the Studio review once, after merge. | DS content-builder.md:25 | OPINION | no | review, hand-off |
| FM84 | The owner may take the Studio model review himself and waive the agent's visual acceptance. Fixes and optimisation must still be verified, and the waiver does not mean approved. | DS D-101 2026-10-05 (decisions.md:111): "Don't worry about verifying the model in Studio. I'll take a look at it." | OWNER | no | review, hand-off |
| FM85 | Environment pieces are screenshot-reviewed at player scale before reporting. Gaps between pieces and misplaced pieces drew a harsh owner review. | GW D-036 2026-10-16 (decisions.md:44): "incredibly sloppy" | OWNER | partly: removed the map layout | review |
| FM86 | Briefs to builders name the full workflow, not only the goal. | GW D-136 2026-10-18 (decisions.md:144): "Make sure all your prompts are very detailed" | OWNER | no | hand-off |
| FM87 | Read the owner's past rejections for this kind of model before building. | DS content-builder.md:16 | OPINION | no | hand-off |
| FM88 | Earlier hand-back format: branch, count against budget, bytes shipped and the container that ships them, validate result, render paths, a verdict per view, decisions needed; about 400 words (first-game value, not a kit rule). | DS content-builder.md:23 | OPINION | partly: removed the brick count | hand-off |
| FM89 | Upload is an owner gate. Nothing goes up before the owner approves; a dry run lists exactly what would upload; the owner runs the command with his key file outside the repo. | GW dam-section-kit.md:307, :314-319; GW D-168 2026-10-19 (decisions.md:176): "Go ahead with the upload plan." | OWNER | partly: removed the ids and commands | hand-off, import |

## 10. Records and hook-up

| id | lesson | evidence | tag | game-specific? | applies to |
| --- | --- | --- | --- | --- | --- |
| FM90 | Model list format: one table per area with id, what, size (W x H x D in studs, height = up), priority (first playable or later) and notes that carry the built triangle count. A header line holds style, scale and file layout. Dropped rows stay, marked with the owner's date. Open questions sit at the bottom. Every row is a PROPOSAL until the owner approves renders. | GW model-list.md:3-9, :83, :86-89 | EXPERIENCE | partly: removed the ids | hand-off |
| FM91 | Uploaded is not in the game. An audit of 65 prop ids and 20 hero model ids (first-game value, not a kit rule) found hero models and textures with 0 code references, and content baked into the place cannot be judged from code. Mark rows USED, UNUSED, STALE or PLACE? and finish the PLACE? rows with a read-only Studio scan. | GW asset-hookup-audit.md:5, :10-22, :100-109, :142-145 | EXPERIENCE | partly: removed the asset lists | import, hand-off |
| FM92 | Keep an id registry per asset family, written by the upload tool, plus a generated code table. Count uploaded against referenced per family, one grep per name. | GW asset-hookup-audit.md:8, :12-22 | EXPERIENCE | no | import, hand-off |
| FM93 | Track models built but never uploaded (39 folders had no id; first-game value, not a kit rule) so they are neither lost nor uploaded without approval. | GW asset-hookup-audit.md:98 | EXPERIENCE | no | hand-off |

## 11. Already in the rigging note (not repeated)

| id | covers | model-relevant point |
| --- | --- | --- |
| FG01 | fused bridges between parts | merged generated meshes fuse neighbours; weights cannot fix it |
| FG03 | variants by bending a rigged body | build variants from one cut base |
| FG05 | closing open shells | inspect open edges before any cap or fill |
| FG06 | one atlas shared by cut parts | each cut part needs its own UVs and texture |
| FG07 | tail clipping through a cape | clearance between moving parts and cloth |
| FG10, FG11, FG13, FG14 | separate parts, hidden joints, face kit, own face | the separate-parts method; see 03-first-game-experience.md |

## Dropped as game-specific

| dropped | why |
| --- | --- |
| Brick format, compiler, validate rules B1-B10, detail-piece catalog, roof pitch tables, trims | the brick system is the first game's own engine and style, no use for another game |
| Brick and stud style, toy-line style, hand-painted style pick, construction theme, ten themed looks, ornament and glyph tables | look and theme belong to each game's art bible |
| Material rows, material physics, fun-to-destroy heuristics, collapse and building physics rules | gameplay design, not modeling |
| Dam grid, section sizes, quota-by-player-count tables, stairs, ladders, collider plan for the dam | the first game's own layout; the method behind them is kept as kit rows |
| Hero list, transforms, cast, villain, story and film rigs, secret-hero design, wheel odds and pity, gift tables, UI and Figma decisions, store and leaderboard models | game and character design |
| Landmark naming and signs rule (D-156), real-world place list | a first-game IP decision; policy belongs to platform-policy |
| Asset ids, group id, upload command strings, key-file handling detail | ids are game data; keys stay outside notes |
| Anchors keys, tile sizes, tool names (art_refs, brickc, import_environment, charlib, dam_kit_run) | first-game tools; only the contract ideas are kept |
| Face kit, own-face-per-character, eye rig, head-as-own-part rules (D-184 to D-186) | already in the rigging note as FG10, FG13, FG14 |
| Hero part-name list and R15 armature detail beyond the import contract | belongs to the rigger notes |

## Conflicts with the owner budget or the research paper

The research paper itself was not read in this task. Checks were made against the paper notes in `03-environment-export-review.md` and against J007-D5.

| topic | conflict |
| --- | --- |
| Collision fidelity | DS content-builder.md:19 told builders to give meshes CollisionFidelity Box or Hull. GW D-170 and TF-MAPCOL1 (2026-10-20) found that Box and Hull on walkable meshes made players float, and reverted it. The collision row follows the later rule. The paper notes (DNT08) also warn against an old four-option collision list. |
| Shadows | DS F-018 (do not use CastShadow as a speed trick) against GW dam-section-kit.md:333 (CastShadow off on rails, balusters, lanterns and glow parts, not measured). The two first games disagree; there is no measurement for the second. Treat as open. |
| Render fidelity and streaming | Both games set RenderFidelity Automatic as a rule. The notes in 03-environment-export-review.md (F22, TRI06) say that with mesh streaming on, RenderFidelity is ignored and generated levels of detail decide the distant look. The first-game rule does not mention streaming. Not checked against the paper itself in this task. |
| Budget | No conflict with owner J007-D5: no character passed 7,000 triangles and nothing passed 20,000 per mesh. Some first-game props (6,380 and 4,660 triangles) were above the first game's own proposed 2,000 per prop (GW model-list.md:5; art/models/README.md props table), and the assembled kit was 62k-81k triangles in view. The paper notes (HND03, step 16) say a missing budget must not be replaced by another game's spec, so no first-game number is a kit budget. |
| Import limits | GW environment-import.md:36 states 20,000 triangles per mesh object and textures up to 1024 x 1024. The 20,000 matches J007-D5 as an upload ceiling. The texture limit is a first-game statement, not verified here; the fact-check pass decides. |
| Light checks | The first games reviewed with full image sets (5 views per model, per-piece side-by-side sheets, stack sheets). The owner's rule J005-D8 and J007-D7 asks for numbers first and images only on failure. The first-game render volume is not a model for the kit. |
