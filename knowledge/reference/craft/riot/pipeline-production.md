---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [modeler, environment-designer, character-rigger, animator, art-director, reference-images, vfx-designer, sound-designer, marketing, level-design, game-designer, live-ops-designer, ui-ux-designer, film-director, architect, feature-builder, orchestrator, reviewer, qa-lead]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Pipeline and production

ADDED TOPIC (prefix PP). How assets are built so they run on phones, survive the hand-off to the next craft, and stay cheap to change: budgets, meshes and UVs, building for the rig and for motion, kits and reuse, environment order, tools, files and marketing deliverables. Folds in the extract topics pipeline-tech, performance-budget and asset-kit.
PP-01 to PP-11 are meshes, textures and files for one asset. PP-12 to PP-17 build for the rig and for motion. PP-18 to PP-23 are rig and clip craft. PP-24 to PP-27 are environments at scale. PP-28 to PP-30 are tools, files and names. PP-31 to PP-33 are marketing deliverables.
Related: detail budgets in `materials-detail.md` (MD-02), costume for motion in `character-design.md` (CD-12), effect cost in `vfx-reads-timing.md` (VR-08), hand-offs in `cross-craft.md`.

### PP-01 Set triangle and texture budgets before building; phones first
- principle: The engine draws every polygon and holds every texture in memory in real time; a sculpt can be millions of polygons. Many players are on phones, so triangle counts and texture sizes stay low, and only what the game camera can see gets work.
- why: High polygon and texture cost hurts play on weak devices; access for everyone matters more than fine detail.
- apply: The brief sets triangle and texture budgets per asset before modelling; Tripo outputs are reduced before import; the smallest texture that holds at the game camera is used. PROPOSAL default for a hero character: below League's 15,000-triangle cap (R03:148-168) because many characters share a phone screen [inference].
- check: Triangle count per mesh in Blender and texture size per asset against the budget; captures from the real game cameras show which sides need detail.
- mistake: Shipping the sculpt; going "too high on both" (R13:632).
- examples:
  - R00a: millions of polygons "can really kill the game's performance" (R00a:1258-1284).
  - R13: topology and textures "pretty low, especially for 2026 standard"; TFT's fixed camera lets painting cheat (R13:628-639, 792-803).
- roblox_fit: Each mesh max 20,000 triangles (knowledge/external/roblox-creator-docs/art/modeling/specifications.md:34; parts/models.md:159); texture guidance 256 for 5x5 studs, 512 for 10x10, 1024 for 20x20 (art/modeling/texture-specifications.md:24-27). Roblox cameras are often player-controlled, so less can be cheated than in TFT. Load `performance` for budgets.
- roles: modeler, environment-designer, art-director, architect, level-design, qa-lead
- also: materials-detail, world-level-readability
- sources: R00a-F34 (R00a:1258-1284); R13-F28 (R13:628-639, 792-803)

### PP-02 Rich form first, then a budgeted game mesh with loops where it bends
- principle: Build the organic form at full detail first so it keeps natural subtlety, then a low-poly game mesh over it, capped by the budget, with edge loops where the body bends so it deforms cleanly.
- why: Modelling low first "can distort the human aspect" (R03:153-155); loop placement decides whether elbows and knees fold cleanly.
- apply: In Blender block and refine the form (or use a Tripo mesh as the "high"), then retopologise to the budget; edge loops at elbows, knees, shoulders, mouth and eyes; UV after.
- check: Triangle count in Blender; loops present at every joint; a bend test with the rig shows clean folds.
- mistake: Modelling low first and losing the natural form.
- examples:
  - R03: high-poly sculpt, retopology, UV, then paint; League skins capped at 15,000 triangles (R03:148-176).
- roblox_fit: A Roblox tutorial character uses under 10,000 triangles per part (knowledge/external/roblox-creator-docs/resources/beyond-the-dark/custom-characters.md:89); mouth and eye loops: art/characters/creating/modeling-best-practices.md:69, 81.
- roles: modeler, character-rigger, animator
- also: character-design
- sources: R03-F05 (R03:148-176)

### PP-03 Put detail in textures, not polygons
- principle: Unwrap the model and bake high-poly detail onto the low-poly mesh (normals, colour), and paint forms the geometry does not have (fur tufts, small carvings) into the texture instead of modelling them.
- why: Texture detail is far cheaper than geometry.
- apply: In Blender UV-unwrap, bake normal and colour from the detailed version to the low mesh, export maps to SurfaceAppearance; check painting against a wireframe or matcap render so painted forms agree with the real surface.
- check: Low-poly with baked maps versus high-poly at the game camera: the read is the same; a wireframe-overlay render shows painted forms placed on real geometry.
- mistake: Adding polygons for detail the texture could carry.
- examples:
  - R00a: the UV map as a peeled orange; detail baked onto the low mesh (R00a:1286-1336).
  - R02: fur tufts painted, not modelled, checked against the wireframe (R02:546-560).
- roblox_fit: Maximum texture 1024x1024 (knowledge/external/roblox-creator-docs/art/modeling/texture-specifications.md:131).
- roles: modeler, environment-designer, character-rigger
- also: materials-detail
- sources: R00a-F35 (R00a:1286-1336); R02-F29 (R02:546-560)

### PP-04 Keep texel density consistent across assets
- principle: Group assets onto texture maps so resolution per area is the same across the scene; hand-painted textures blur close up, which is fine at game distance.
- why: Consistent resolution looks consistent; one sharper asset looks out of place.
- apply: Default one 1024 map per hero asset; group small props onto shared maps; measure texel density per asset.
- check: Texel density per asset within a set range; no asset visibly sharper or blurrier than its neighbours at the game camera.
- mistake: Mixed resolutions side by side [inference].
- examples:
  - R02: statue and pedestal on one 1024 map, grass on its own (R02:776-804).
- roblox_fit: A 1024 texture uses four times the memory of a 512 (knowledge/external/roblox-creator-docs/performance-optimization/improve.md:567).
- roles: modeler, environment-designer, architect, reviewer
- also: materials-detail
- sources: R02-F33 (R02:776-804)

### PP-05 Mirror UVs on symmetric parts; unique UVs where story detail goes
- principle: Mirrored UVs halve texture space and paint time on symmetric designs, but anything painted appears on both sides; asymmetric story detail (cracks, damage, badges, text) needs unique UV space.
- why: Mirroring saves memory and time; mirrored wear or text reads artificial.
- apply: In Blender overlap mirrored UV halves for symmetric parts; reserve unique UV space for asymmetric details; hero props with cracks get unique UVs on at least the visible front.
- check: The UV layout shows symmetric parts overlapped; renders show no identical marks on both sides and no mirrored text or logos.
- mistake: Painting cracks on mirrored UVs (R02:412-416); a projection "big X" from symmetric UVs (R02:304-306).
- examples:
  - R02: the fox re-UV'd unique to paint a single crack across its face (R02:136-146, 412-418, 686-712).
  - R03: Zyra's asymmetric skin cannot mirror and takes more time (R03:930-947).
- roblox_fit: Unique UVs on a 1024 map lower texel density (knowledge/external/roblox-creator-docs/art/characters/creating/texturing-setup.md:45); choose per asset.
- roles: modeler, environment-designer, character-rigger, art-director
- also: materials-detail
- sources: R02-F08 (R02:136-146, 412-418, 686-712); R03-F40 (R03:930-947)

### PP-06 When geometry changes, re-project; marry texture and geometry last
- principle: When texturing exposes a geometry problem, change the mesh and project the existing texture onto it instead of repainting. At the end, after the texture layout is locked, pull the silhouette to follow the major painted details (not all of them) so geometry and paint agree.
- why: It keeps work done; a silhouette that agrees with the painted detail looks cohesive; doing it before the texture is stable means redoing it.
- apply: Blender: selected-to-active bake of the old texture to the new UVs; in polish, move edge vertices to match major painted cracks or carvings, then reimport.
- check: No seams or stretching after re-projection; the silhouette render shows the major painted features in the outline where visible at the game camera.
- mistake: Geometry that "doesn't really follow the shape of those painted details" (R13:994-996); marrying them before the texture is stable.
- examples:
  - R02: stones removed, re-UV'd and re-projected (R02:580-588, 636-646).
  - R13: rock vertices pulled to match painted chips (R13:982-1020).
- roblox_fit: Studio Reimport updates the mesh in place (knowledge/external/roblox-creator-docs/art/modeling/reimport.md); stay within the triangle budget.
- roles: modeler, environment-designer, character-rigger, art-director, orchestrator
- also: materials-detail, shape-silhouette
- sources: R02-F30 (R02:580-588, 636-646); R13-F38 (R13:982-1020)

### PP-07 Project the concept onto the model as a starting texture
- principle: Project the approved 2D concept onto the 3D model from a matching view as a rough first texture, then fill the gaps and clean up; "better than nothing" as a base.
- why: It puts the right colours and values in the right places from the start.
- apply: In Blender, align a camera to the reference view, use project-from-view or texture-paint projection to bake the reference onto the model, then fill gaps and repaint; treat it as a base only.
- check: Render at the reference camera: colours and values sit on the right parts; renders from other angles show no stretched or empty areas.
- mistake: Leaving unprojected gaps or stretched projections.
- examples:
  - R13: edit-projection drags the concept onto the model, then gaps are closed (R13:444-466).
- roblox_fit: Final textures fit Roblox texture sizes (knowledge/external/roblox-creator-docs/art/modeling/texture-specifications.md:24-27).
- roles: modeler, environment-designer, reference-images
- also: materials-detail, references-ideation
- sources: R13-F21 (R13:444-466)

### PP-08 For stylised assets, a low-poly painted workflow keeps changes cheap
- principle: Hand-painted stylised assets start low-poly directly (no high-poly bake); a shape change is a re-export and the paint follows, unlike a high-to-low bake pipeline.
- why: Fast iteration on shape without redoing bakes.
- apply: For stylised Roblox assets, model low-poly in Blender with painted or flat textures; the Blender file is the source; update the Studio asset by reimport instead of reinserting.
- check: After a model change, the reimported asset keeps its place and settings in Studio.
- mistake: A high-poly bake pipeline where it is not needed.
- examples:
  - R13: a plant enlarged, exported and replaced with a live texture update (R13:596-620).
- roblox_fit: Studio Reimport updates existing meshes and textures without new instances (knowledge/external/roblox-creator-docs/art/modeling/reimport.md).
- roles: modeler, environment-designer, art-director, orchestrator
- also: process-iteration
- sources: R13-F26 (R13:596-620)

### PP-09 Keep separable parts separate, then judge them together
- principle: Block each garment or part as its own object, and export every part you may want to treat separately as its own group, so it can be locked, retextured or replaced alone; judge the combined result.
- why: Separate parts keep early decisions separable and stop changes bleeding across parts; the whole still reads as one image.
- apply: In Blender keep garments, props, plants and ground as separate, clearly named objects or material slots; review renders show the combined character or scene.
- check: The object list shows each logical part as a separate named object; a change to one leaves the others unchanged; reviews use combined renders.
- mistake: One merged mesh where changes bleed across parts.
- examples:
  - R01: a new layer per garment, then merged (R01:168-172, 381-383).
  - R13: plants locked while painting the ground under them (R13:476-489).
- roblox_fit: A MeshPart takes one material (knowledge/external/roblox-creator-docs/art/modeling/texture-specifications.md:29), so separate parts are often separate MeshParts anyway.
- roles: modeler, environment-designer, character-rigger, reference-images, art-director, feature-builder
- also: process-iteration
- sources: R13-F22 (R13:476-489); R01-F09 (R01:168-172, 381-383)

### PP-10 Paint across joined meshes so joins disappear
- principle: Project paint over meshes that meet (an object and its base or ground) for a seamless blend; props added later need their own UV space.
- why: It hides the joins between object and ground.
- apply: In Blender paint or bake the blend in a shared texture or vertex colour across the join; give added props their own UV islands.
- check: No hard seam where object meets ground at the game camera.
- mistake: A visible seam line at every join [inference].
- examples:
  - R02: moss painted across statue and pedestal; UVs added for a hidden mascot (R02:762-772, 890-898).
- roblox_fit: Separate MeshParts cannot share one paint layer; blend with decals or vertex colour [inference].
- roles: modeler, environment-designer
- also: materials-detail
- sources: R02-F39 (R02:762-772, 890-898)

### PP-11 Clean meshes, clean collision, organised UVs
- principle: Keep topology in quads where edits are expected, UVs laid out so a teammate can pick the file up, meshes clean because gameplay systems read them, and collision simple so players do not snag on random rocks.
- why: Work passes between makers; gameplay systems and raycasts read the mesh; snag geometry feels unfair.
- apply: In Blender: quads where editing is planned, laid-out UV islands, simple collision separate from detail; the feature builder's raycast systems rely on that collision [inference].
- check: Model audit (`modeling-craft`): non-quad faces only where no edit is planned, clean UV layout, collision of a few simple shapes; a Studio walk test along walls finds no snags.
- mistake: "If it was all triangulated, I'd have to like manually cut in these things" (R09:866-867).
- examples:
  - R09: vertex painting a blend works only because the mesh is clean (R09:228-233, 737-749, 862-867, 894-900).
- roblox_fit: MeshPart collision fidelity can be set simpler for walls [unverified]; Roblox triangulates on import, so quads matter in the Blender source [inference].
- roles: modeler, environment-designer, character-rigger, feature-builder, qa-lead
- also: world-level-readability
- sources: R09-F39 (R09:228-233, 737-749, 862-867, 894-900)

### PP-12 Build to the shared rig: reuse its joints, match it, model what it moves
- principle: Before designing, list what the rig already supports (extra joint chains such as coattails or a hair strand) and what it lacks; use existing joints for new parts. A new skin is overlaid on the base mesh and armature so joints and fingers match, or the shared animations do not translate. Model every part the rig must move (an open-able mouth, eyelids, teeth).
- why: New joints cost animation and tech time while reused joints give motion for free; mismatched joints break every shared clip; fixing a face after rigging takes "little surgeries".
- apply: Modelers and the art director read the rig sheet (`rig-pipeline`) first; concept prompts name the available dangling parts and forbid parts with no joint; the new mesh is overlaid on the base armature in Blender and joint positions compared; the rig sheet lists moving parts and the mouth is modelled separable or open where it must move.
- check: Every moving costume part maps to a joint in the rig sheet (unmapped parts = 0, or each is a logged scope request); joint-by-joint offsets against the base are within tolerance and the shared clips play on the new mesh (`clip_check.py`); a test pose with the mouth fully open and eyes closed shows no distortion.
- mistake: Long hanging sleeves when "no joints currently exist on Caitlyn's rig for that" (R01:94-99); "you need to adjust these ... otherwise the animations won't translate" (R03:876-878); lips modelled sewn shut (R03:880-886).
- examples:
  - R01: Lunar Wraith's two coattail chains reused as a ringmaster's tails (R01:76-99, 136-138, 144-150, 240-243).
  - R03: overlaying the previous skin to match joints and fingers (R03:864-878).
  - R03: a yell animation failed on a sewn-shut mouth (R03:878-908).
- roblox_fit: Roblox rigs use Motor6D or skinned Bones (knowledge/external/roblox-creator-docs/_api-reference/classes/Bone.yaml; art/modeling/skin-a-simple-mesh.md); shared R15 rigs reuse animations the same way [unverified]; facial topology needs circular mouth loops (art/characters/creating/modeling-best-practices.md:69).
- roles: modeler, character-rigger, animator, art-director, reference-images, orchestrator, qa-lead
- also: character-design, cross-craft
- sources: R01-F03 (R01:76-99, 136-138, 144-150, 240-243); R03-F37 (R03:864-878); R03-F38 (R03:878-908)

### PP-13 Keep the contact points fixed in every variant
- principle: Keep a held item's contact points (grip, barrel underside, stock at the shoulder, hand positions) the same in every variant, with room so hands do not clip; everything else may vary.
- why: Every animation depends on them.
- apply: Variant models keep the base's socket and attachment positions; leave clearance where hands sit.
- check: Socket positions measured against the base match; the shared clips play without hand or body clipping.
- mistake: Moving the grip or shortening the barrel so the hand clips through the item.
- examples:
  - R01: the barrel underside extended so her left hand has room; side elements vary freely (R01:656-669, 872-883).
- roblox_fit: Contact points become Attachments and grip offsets on the Tool and the hand; variants keep the same positions [inference].
- roles: modeler, character-rigger, animator, reviewer, qa-lead
- also: character-design, weight-timing
- sources: R01-F41 (R01:656-669, 872-883)

### PP-14 Design moving parts with room to move
- principle: Designed moving parts (sliding barrels, opening blades, a stock that retracts) make inspect and action clips satisfying, but each piece must slide into the next and retract away from the body without clipping.
- why: Animations reuse the same moving parts; a design that blocks them clips in every clip; a static object leaves only hand motion.
- apply: Modelers cut moving parts as separate meshes with pivots and nesting cross-sections (rig-pipeline sockets); the animator plans inspect, equip or fire clips using them; sound gets a cue per mechanical move [inference].
- check: The model has named moving parts with pivots; frame-stepping the fire or inspect clip at the game camera shows no part intersecting the arms (`clip_check.py` samples show the parts moving).
- mistake: Decorations that stop the barrel sliding; a fully static object.
- examples:
  - R01: Caitlyn's gun body, outer and inner barrels all move; the stock shrinks into the gun so it clears the arms (R01:100-112, 858-864).
  - R12: parts that "advance" for a future inspect animation, like an opening knife (R12:233-236, 360-364, 452).
- roblox_fit: Separate MeshParts joined by Motor6D, or Bones in one skinned mesh; moving parts count toward instance budgets [unverified].
- roles: modeler, character-rigger, animator, vfx-designer, art-director, sound-designer, reviewer
- also: character-design, weight-timing
- sources: R01-F04 (R01:100-112, 858-864); R12-F17 (R12:233-236, 360-364, 452)

### PP-15 Spend expensive features only where they earn it
- principle: Some features are very expensive downstream (capes, loose cloth, tassels, long hair, new joint chains, a hanging whip). Use them only when they clearly make a better, more aspirational design or carry the theme, and the character is not also expensive elsewhere.
- why: Scope is finite; months of work can go into something that barely changes the look.
- apply: The design hand-back lists each costly element with the reason it earns its cost; any extra beyond the brief is a logged ticket with a theme-value line that the orchestrator approves or cuts. In our pipeline each flowing part means extra bones, weights and keyed secondary motion; default to rigid or bundled shapes [inference].
- check: Count dangling or flowing parts on the final sheet: each has a written reason; the rigger confirms the count is in budget.
- mistake: Designing for one's own love of fabric; adding an exciting part that does not carry the theme.
- examples:
  - R11: after Darius the team "would never do another cape again"; Yasuo's cape needed delicate work (R11:87-91, 106-111, 122-129).
  - R01: a fully realised hanging whip weighed against the cost of a new joint chain (R01:257-263).
- roblox_fit: No cloth simulation for characters in our pipeline; flowing parts are keyed bones or layered clothing (WrapLayer cages: knowledge/external/roblox-creator-docs/art/accessories/layered-clothing.md:136); every extra part counts against the character triangle budget (art/characters/specifications.md:378).
- roles: art-director, modeler, character-rigger, animator, reference-images, game-designer, orchestrator, architect
- also: character-design, process-iteration
- sources: R11-F05 (R11:87-91, 106-111, 122-129); R01-F15 (R01:257-263)

### PP-16 Designs must work in 3D, in the round
- principle: Parts must interact in space (a lapel continues behind the neck, a hat brim extends back), not be a 2D image slapped onto a body.
- why: 2D-only designs leave the 3D maker to invent the missing views.
- apply: Concept images include side and back views; modelers check every part in the round.
- check: Turntable renders at 4 angles show no flat or floating parts.
- mistake: "A 2D image slapped on top."
- examples:
  - R01: the hat brim extended further back so it sits in 3D (R01:397-407, 585-588).
- roblox_fit: No change; third-person cameras show backs and sides.
- roles: modeler, character-rigger, reference-images, art-director
- also: references-ideation, character-design
- sources: R01-F27 (R01:397-407, 585-588)

### PP-17 Explore variants over an in-game mannequin
- principle: Paint new ideas over an existing in-game model with the least bulky costume, so iteration is fast and stays on model.
- why: Proportions, rig and camera are already right; only the new idea changes.
- apply: Make a mannequin render of the base character in Blender or Studio (plain or least-bulky variant) from the game camera and use it as the image-edit input for variant concepts.
- check: Every variant concept overlays the mannequin silhouette at the same scale; proportions match.
- mistake: Starting from a bulky variant that hides the body (R01:70).
- examples:
  - R01: Pool Party Caitlyn's light costume as the base for the ringmaster idea (R01:66-74).
- roblox_fit: A Roblox character render at the game camera is a cheap base [inference].
- roles: art-director, reference-images, modeler
- also: references-ideation, character-design
- sources: R01-F02 (R01:66-74)

### PP-18 Rigs are tested in extreme poses before animation
- principle: Rigging places bones in the mesh and weights decide how much each bone moves each part; the goal is deformation without odd results, proved before the animator starts.
- why: Bad weights show as stretching, pinching or the wrong part moving.
- apply: The rigger places bones at real joints and paints weights by script in Blender, then renders a set of extreme test poses before hand-off.
- check: Test-pose renders from fixed cameras show no stretching, collapsed volume or parts following the wrong bone.
- mistake: "Odd results" from weights found only in animation.
- examples:
  - R00b: bones inside the mesh plus painted weights (R00b:2371-2411).
- roblox_fit: Roblox supports rigid Motor6D rigs and skinned Bones (choose per `rigging-design`); a KeyframeSequence Pose stores only a CFrame, no scale (knowledge/external/roblox-creator-docs/_api-reference/classes/Pose.yaml:54-68).
- roles: character-rigger, modeler, animator
- also: character-design
- sources: R00b-F21 (R00b:2371-2411)

### PP-19 Controls are puppet strings with planted feet
- principle: Give animators a small set of intuitive controls that move the bones like puppet strings, solving problems such as keeping a foot planted while the body moves and switching so a limb follows the body.
- why: Animators work faster and make fewer contact errors when controls match how they think.
- apply: The rigger delivers a control manifest in Blender (IK legs with foot plant, FK/IK switch where needed, root and body controls), each control named and described.
- check: Test clip moving the hips with feet on IK: foot slide measured by `clip_check.py contact_slide` stays within the rig sheet's tolerance; switched to FK, the leg follows the body.
- mistake: Animating raw bones; sliding feet.
- examples:
  - R00b: a foot planted while the body moves; the whole leg following the body when swimming (R00b:2413-2437).
- roblox_fit: Controls live in Blender and Roblox receives baked clips; runtime IKControl exists for in-game foot or hand placement (knowledge/external/roblox-creator-docs/animation/inverse-kinematics.md).
- roles: character-rigger, animator
- also: weight-timing
- sources: R00b-F22 (R00b:2413-2437)

### PP-20 A character is many clips that interrupt and blend: plan the states first
- principle: In a game you cannot predict which animation plays when; a character is many clips interacting, interrupting and blending under game conditions (walk-jog-run by speed, aim by direction, reactions by distance).
- why: Transitions are what players see most; clips made alone pop when combined.
- apply: The animator and feature builder define the state list, transitions and blend parameters before keying; clips are made to blend (matching poses at transitions) with set priorities.
- check: Play-test captures of every transition (idle to walk to run, attack interrupted by hit, jump while running): no pops or foot slides; `clip_check.py loop_seam` on loops.
- mistake: Clips made in isolation that pop when combined.
- examples:
  - R00b: running while shooting, reloading and jumping; walk, jog and run blended by speed (R00b:3237-3309).
- roblox_fit: AnimationTrack priorities (knowledge/external/roblox-creator-docs/animation/editor.md:292-298), weights through AdjustWeight (_api-reference/classes/AnimationTrack.yaml:287), fadeTime on play (AnimationTrack.yaml:251), and the Graph Editor state machine (animation/graph-editor-state-machine.md).
- roles: animator, feature-builder, architect, character-rigger, qa-lead
- also: weight-timing, cross-craft
- sources: R00b-F39 (R00b:3237-3309)

### PP-21 Read the curves behind the motion
- principle: Look at each control's per-axis curve, not only the moving picture: odd motion shows as curves "going crazy", and a flat stretch shows where travel stops.
- why: The eye misses small pops when everything moves at once; a single-axis curve shows exactly where and when.
- apply: Dump Blender f-curves or `clip_check.py` samples per control and axis to find spikes, flips and plateaus.
- check: Per major control, sampled values per frame show no sudden jumps (flip or pop), no unintended plateaus (stalls) and no spikes past key values (`clip_check.py pops`).
- mistake: Judging only by eye with the whole body moving.
- examples:
  - R04: translate X and Z curves flattening means "she's not having any more move horizontally through space" (R04:194-211, 604-612).
- roblox_fit: Roblox's Curve Editor shows tangents (knowledge/external/roblox-creator-docs/animation/curve-editor.md:61-65); our reading happens in Blender and `clip_check.py`.
- roles: animator, reviewer, qa-lead
- also: weight-timing, critique-feedback
- sources: R04-F08 (R04:194-211, 604-612)

### PP-22 Shape eases with tangents, not extra keys
- principle: Shape ease-in and ease-out with tangent handles rather than adding keys; fewer keys are easier to read and change.
- why: The computer does the smooth maths while the animator controls the shape; extra keys add bumps.
- apply: In Blender use Bezier handles on f-curves to shape eases; avoid extra keys for easing; know that a new key can bend a weighted curve unexpectedly.
- check: Key count per control stays low; f-curves are smooth without extra bumps.
- mistake: Adding keys to fix eases (R04:586).
- examples:
  - R04: a tangent handle dragged to shape the jump ease instead of a new key (R04:556-588).
- roblox_fit: KeyframeSequence poses use fixed easing styles, not free tangents (knowledge/external/roblox-creator-docs/_api-reference/enums/PoseEasingStyle.yaml); Blender curves become baked keys on export [unverified]; CurveAnimation supports tangents (animation/curve-editor.md:63-65).
- roles: animator
- also: weight-timing
- sources: R04-F27 (R04:556-588)

### PP-23 Fix gimbal flips at the source
- principle: When rotations flip, work through it by keying on ones until fixed; use rotation modes that avoid gimbal lock.
- why: Interpolation flips cause wiggly arms and knee pops.
- apply: In Blender use quaternion rotation for spin-heavy controls and bake on ones before export.
- check: `clip_check.py pops` shows no sudden rotation jumps.
- mistake: Wiggly arms and knee pops left in (R04:1088).
- examples:
  - R04: "I'll just keep it on ones until it's fixed" (R04:906-912, 1086-1088).
- roblox_fit: KeyframeSequences use quaternions; Euler conversion can show gimbal lock (knowledge/external/roblox-creator-docs/animation/curve-editor.md:26, 39).
- roles: animator, character-rigger, qa-lead
- also: weight-timing
- sources: R04-F44 (R04:906-912, 1086-1088)

### PP-24 Kits for repeated layouts, unique shells for bespoke ones; no visible duplicates
- principle: Large worlds cannot be built piece by piece: build reusable modular kits ("elaborate Legos") with enough variance to look different and generic enough not to read as duplicates; rotating or manipulating a piece makes it look new. Gameplay-driven irregular layouts do not suit kits; then shells are unique per place, sharing trim sheets.
- why: Reuse saves memory, draw cost and build time; visible repeats break belief; forcing a kit onto a bespoke layout bends the gameplay.
- apply: Per stage decide kit or unique shells. Kits: walls, floors, trims, props, rocks, each designed to read differently when rotated; one shared trim or texture set; placement with random rotation and scale within limits. Bespoke layouts: unique shells plus shared trim sheets (MD-17).
- check: Count unique meshes and textures per stage against the budget; in game-camera captures no piece is visible twice in one view at the same angle.
- mistake: Custom-building every piece; identical pieces side by side; forcing a kit onto a layout it does not fit.
- examples:
  - R00b: a crate turned around to look like another crate; one rock used many ways (R00b:2037-2097, 2127-2131).
  - R09: VALORANT shells are mostly unique per location, with a kit for quick shells (R09:682-699).
- roblox_fit: Packages let a kit piece be reused and mass-updated (knowledge/external/roblox-creator-docs/projects/assets/packages.md:3, 14); a shared SurfaceAppearance trim-sheet package across modular assets (tutorials/curriculums/environmental-art/assemble-an-asset-library.md:93).
- roles: environment-designer, modeler, level-design, architect, art-director
- also: materials-detail, world-level-readability
- sources: R00b-F15 (R00b:2037-2097, 2127-2131); R09-F37 (R09:682-699)

### PP-25 Reuse first: search the zoo and existing effects before making new
- principle: Keep an asset zoo (materials, props, decals, VFX of an area) and, before making anything new, reuse and combine proven assets from earlier work, then recolour and retime them.
- why: Speed and a consistent look.
- apply: Before a new texture, prop or emitter, search the game's library (Studio MCP `search_game_tree`, the effects folder, approved asset IDs); reuse, recolour, retime; make new only where the zoo lacks one.
- check: The hand-back names which assets were reused and which are new.
- mistake: Making everything from scratch and running out of time.
- examples:
  - R06: clouds, lightning, rain and candy meshes pulled from earlier champions' effects and combined (R06:41-44, 126-128, 275, 283-286).
  - R09: Sunset's goo pit reused for lava; VFX from Haven (R09:552-554, 624-626, 840-842, 1058-1066).
- roblox_fit: Reuse means cloning emitters and attachments from an effects library or packages; recolour through ColorSequence.
- roles: vfx-designer, environment-designer, modeler, sound-designer, feature-builder, orchestrator
- also: style-identity, cross-craft
- sources: R06-F04 (R06:41-44, 126-128, 275, 283-286); R09-F29 (R09:552-554, 624-626, 840-842, 1058-1066)

### PP-26 Environment order: blockout, composition, kit, dressing, mechanics, then light and polish
- principle: Concept sets theme and tone; the designer's grey blockout fixes where players go; environment art roughs over it; composition and kit come next, then set dressing, then the mechanic's visuals; lighting, post-processing and polish go in only when the space is play-tested and working.
- why: Gameplay constraints are fixed before art is spent; lighting and polish depend on final geometry; the mechanic's look is judged in a finished context.
- apply: Stage jobs run: art-bible mood image, Studio greybox with plain Parts, rough kit over the greybox, refine with play-test captures, set dressing, mechanic visuals, then Lighting, Atmosphere, post effects and polish. Each stage has a capture review before the next.
- check: The job record shows a play-tested greybox before final art; capture reviews exist per stage; the lighting pass is dated after the last route change.
- mistake: Polishing art and light before the layout is proven.
- examples:
  - R00b: concept, grey blocks, rough art, refine and play-test, then lighting, post and polish (R00b:1751-1789).
  - R09: composition, kit and quick details, set dressing, then the lava and its VFX (R09:654-658, 836-838, 1150-1156).
- roblox_fit: The Roblox docs recommend the same greybox step and placeholder packages updated to detailed versions later (knowledge/external/roblox-creator-docs/tutorials/curriculums/environmental-art/greybox-your-environment.md:17; projects/assets/packages.md:19).
- roles: environment-designer, level-design, game-designer, art-director, orchestrator, modeler
- also: process-iteration, world-level-readability
- sources: R00b-F02 (R00b:1751-1789); R09-F34 (R09:654-658, 836-838, 1150-1156)

### PP-27 Block out on a grid; snap the art to the approved blockout
- principle: Stay on grid while getting broad ideas down, add small signals (railings at hazard edges) once the layout works, and after approval import the blockout into the modelling tool at world position and snap every art piece to it, so tested gameplay spaces stay exact.
- why: Snapping speeds iteration; art that drifts off the blockout changes tested angles.
- apply: Level design and modelers use a fixed snap increment in Studio and Blender; the modeler imports the Studio blockout into Blender at the same origin and scale (one fixed stud-to-metre conversion recorded in the game profile [inference]), builds on the grid, and exports back to the same position; hazard edges get a rail or curb after the layout passes play-test.
- check: Blockout part positions are multiples of the snap increment; bounding boxes of art shells versus blockout parts differ by less than one snap step; the tested angles are replayed after art; hazard edges have a visible barrier.
- mistake: Going off grid early; art drifting off the blockout [inference].
- examples:
  - R09: railings around the lava dock once the gist worked (R09:332-346).
  - R09: the designer's grid blocks exported to Maya and matched piece by piece (R09:342-346, 669-679).
- roblox_fit: Studio has move and rotate snap increments [unverified]; exact stud-to-metre ratio [unverified].
- roles: level-design, environment-designer, modeler, qa-lead
- also: world-level-readability, process-iteration
- sources: R09-F18 (R09:332-346); R09-F36 (R09:342-346, 669-679)

### PP-28 Automate every repeated step
- principle: The job of tech art is to streamline how art is made and put into the game. Every asset needs implementation steps (strip unused parts, set settings, name, split, connect); build tools that remember what the maker always does.
- why: Repeated confirmations waste time and cause errors ("just please remember what I always do!").
- apply: Each export and import route (Blender to FBX to Studio) is a script with fixed defaults (strip unused data, apply naming, split parts, set properties); agents call the script, not a manual sequence. When an agent repeats a manual step across jobs, file a tool ticket (PROPOSAL: a step done 3 or more times [inference]).
- check: The import check runs on every asset: names match the convention, no unneeded components, required properties set; hand-backs show no repeated manual sequences that a script already covers.
- mistake: Clicking the same dialog "day in and day out".
- examples:
  - R00b: "our main job is to streamline how art is made and put into the game" (R00b:2365-2369).
  - R00b: "confirm, confirm, confirm ... just please remember what I always do!" (R00b:2497-2541).
- roblox_fit: Blender Python, the Studio MCP and Rojo are our tools; Studio MCP and Rojo can apply properties by script.
- roles: architect, feature-builder, orchestrator, character-rigger, modeler
- also: cross-craft
- sources: R00b-F20 (R00b:2365-2369); R00b-F23 (R00b:2497-2541)

### PP-29 One owner per file or area; clear names on every submission
- principle: Many people editing at once can delete, misplace or overwrite work; version control records every change and, most importantly, who is working on what. Split shared spaces into areas per discipline so makers do not step on each other, and name every submission clearly so a broken build can be traced.
- why: Interdependent work means constant hand-offs; separation prevents collisions and clear names speed recovery.
- apply: One owner per file or Studio container at a time, recorded in the job card; each role owns its own folder or model in the place (Blockout, Lighting, Art_SiteB); commits carry trailers and name the area and change; a crossing edit goes through the job's sideways-exchange note; check what changed before reporting state.
- check: Before editing a shared file, git status and the job card show no other owner; no two roles edit the same container in a job without a logged hand-over; commit messages name area and change.
- mistake: Overwriting a teammate's work; "toe stepping" on shared files; unclear submissions that break the build (R09:126, 524-526).
- examples:
  - R00b: version control "lets you know if someone else is working on a file" (R00b:2541-2611).
  - R09: VALORANT maps split into many sublevels per discipline; a good changelist name tells what broke (R09:114-134, 524-530).
- roblox_fit: Rojo files mode plus git for code; place content separated by folders and models in the data model [inference]; Team Create has its own script locking [unverified].
- roles: orchestrator, architect, environment-designer, feature-builder, qa-lead
- also: cross-craft
- sources: R00b-F24 (R00b:2541-2611); R09-F07 (R09:114-134, 524-530)

### PP-30 Fix naming and folders before production
- principle: Naming and folder structure look simple but become a huge problem at thousands of files; set them early, keep them, and build tools for mass renaming.
- why: Findability and automation depend on predictable names.
- apply: Each game defines asset naming and folder rules before production; scripts enforce them and rename.
- check: A lint over asset names and folders finds no off-convention names.
- mistake: "Inefficient naming styles" kept too long.
- examples:
  - R00b: naming conventions and folders "can become a huge problem if not handled and maintained" (R00b:2611-2641).
- roblox_fit: The Roblox docs organise content into folders by type (trim sheets, decals, modular assets, props) (knowledge/external/roblox-creator-docs/tutorials/curriculums/environmental-art/assemble-an-asset-library.md:29).
- roles: architect, orchestrator, modeler, environment-designer, feature-builder
- also: none
- sources: R00b-F25 (R00b:2611-2641)

### PP-31 Make final images at their final resolution
- principle: Upscaling a small image "gets very blurry": it invents no detail. Make finals at their final size.
- why: Upscaling loses detail and sharpness.
- apply: Generate or render at the final output size (thumbnail 1920x1080, icon 512x512); work small only for early options (PI-05); upscale only with a dedicated pass and a re-check.
- check: Pixel dimensions of the final file match the target; a 100 % zoom shows no upscale blur.
- mistake: Starting small and upscaling late (R05:693-696).
- examples:
  - R05: 72 to 300 ppi upscaling went blurry (R05:693-696).
- roblox_fit: Icon 512x512 (knowledge/external/roblox-creator-docs/production/publishing/experience-icons.md:55); thumbnail 1920x1080 (production/publishing/thumbnails.md:54); `thumb_check.py` reports the master checks.
- roles: marketing, art-director, reference-images, ui-ux-designer
- also: composition-focus
- sources: R05-F23 (R05:693-696)

### PP-32 One key art feeds a whole asset kit; deliver switchable layers
- principle: One key art becomes many assets ("like 20", up to "probably like 50": crops, wallpapers, backdrops, end cards, social headers, store art), so the release looks like one event everywhere. Deliver files with layers the next maker can switch (classic version, extra lighting, effects) to make variants without asking again.
- why: Consistency across every surface; downstream crafts make variants on their own.
- apply: Marketing briefs list the asset kit (icon, thumbnails, in-game banner, social, update art); the master is composed crop-safe (hero centred, room at the sides) with layered sources. Blender and Studio deliverables keep effects, lights and props in named, toggleable groups.
- check: Crop the master to each target ratio: hero and title survive every crop (`thumb_check.py` on each); each named variant is produced by toggling groups only.
- mistake: A master that works in one crop only [inference]; flattened files that force a remake.
- examples:
  - R05: an end card and a logo bumper themed to the key art; 20 to 50 pieces from one image (R05:731-748, 874-876, 894-896, 904-906).
  - R05: a layered file with toggleable classic and extra-effect versions (R05:861-872).
- roblox_fit: Roblox needs a square icon (512x512) and 16:9 thumbnails (knowledge/external/roblox-creator-docs/production/publishing/experience-icons.md:55; thumbnails.md:54); named Folders and Models in Studio [inference].
- roles: marketing, live-ops-designer, ui-ux-designer, film-director, art-director, environment-designer, vfx-designer, orchestrator
- also: composition-focus, cross-craft
- sources: R05-F27 (R05:731-748, 874-876, 894-896, 904-906); R05-F37 (R05:861-872)

### PP-33 The icon and thumbnail are the box art: highest effort, tested at grid size
- principle: Like box art in a rental store, the tile in a browse grid is still what brings many players in for the first time.
- why: Browsing players choose from small tiles.
- apply: Treat the game icon and thumbnails as the box art: highest effort, tested at the real grid size next to competitor tiles.
- check: `thumb_check.py icon` at 150x150 and `thumb_check.py thumbnail --size` at the measured tile size, placed next to competitor tiles: the subject reads and stands apart.
- mistake: An icon judged only at full size [inference].
- examples:
  - R05: Blockbuster box art versus the Twitch browse grid (R05:748-754).
- roblox_fit: Icons scale down to 150x150 (knowledge/external/roblox-creator-docs/production/publishing/experience-icons.md:34); load `marketing-design`.
- roles: marketing, live-ops-designer, art-director
- also: composition-focus, visual-hierarchy
- sources: R05-F28 (R05:748-754)
