---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [modeler, environment-designer, art-director, reference-images, vfx-designer, ui-ux-designer, marketing, level-design, architect, feature-builder, orchestrator, reviewer]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Materials and detail

Surfaces, edges, wear and how much detail to put where.
MD-01 to MD-03 set how much detail and what kind (indicate, budget by display size, edges as finish). MD-04 to MD-08 are the material working method (regions, baked masks and recipes, maps, materials with light, test small). MD-09 to MD-12 make surfaces believable (wear, imperfection, ornament with a reason, function and support). MD-13 grounds objects in the world. MD-14 to MD-17 are specific material rules (gold, cracks, glints, trim sheets).
Related: detail placement and rest areas in `visual-hierarchy.md` (VH-05), form shading in `value-contrast.md` (VC-09 to VC-13), texture budgets and UVs in `pipeline-production.md`.

### MD-01 Indicate detail; do not spell it out
- principle: Show a material or a mass (hair, grass, fur, quilting, satin) with the least information that reads: clumps, a few tapered marks, three value blocks. Inside a correct value structure, a few loose marks read as detail from a distance; the image must look good with or without the small details.
- why: The eye fills in; extra rendering becomes noise, muddies the read and costs time. Detail is perceived, not counted.
- apply: Hair as 3-6 large clumps with a few tapered dark, saturated shadow marks per clump; grass and ground cover as soft clumps with a few blades pulled out in chosen spots; a cylinder needs darker edges and one rounded highlight; satin needs local colour, highlight and shadow blocks (the ratio sets shine). Reference prompts ask for "clumped, simplified" hair and foliage. Spend effort on the focal subject.
- check: At game size and thumbnail size the material type is recognisable; hair reads as clumps with clear light and dark; a grayscale capture shows no high-frequency stripe noise; detailed grass is a small share of the ground area. A piece that only works zoomed in fails.
- mistake: Spelling out every strand or blade ("it's just so noisy", R02:424-426); "zooming in and try to paint all those intricate little corners ... Don't do that" (R13:317-319).
- examples:
  - R13: scribbles on the golden plate read as detail zoomed out; painters with fading sight got better by losing detail (R13:299-321, 404-406, 501-507).
  - R01: a quilted leather lapel with minimal marks; satin in three blocks (R01:391-393, 954-968).
  - R03: Caitlyn's hair: thick-to-thin dark strokes, shadows only where shapes hide from light (R03:506-515, 548-558).
  - R02: fluffy grass with areas of rest, as on Summoner's Rift (R02:124-128, 420-430).
- roblox_fit: Phones show assets small and Roblox loads lower texture quality first on weak devices (knowledge/external/roblox-creator-docs/art/modeling/texture-specifications.md:24), so fine detail is often lost anyway. Terrain grass decoration is uniform; ground clumping comes from material patches and a few placed meshes [unverified].
- roles: modeler, art-director, environment-designer, vfx-designer, reference-images, ui-ux-designer, level-design, reviewer
- also: visual-hierarchy, value-contrast, shape-silhouette
- sources: R13-F13 (R13:299-321, 404-406, 501-507); R01-F26 (R01:391-393, 954-968); R03-F22 (R03:506-515, 548-558); R02-F06 (R02:124-128, 420-430)

### MD-02 Budget detail by display size, camera distance and player speed
- principle: Put detail only where the player can see it at their size, camera distance and speed. In-game assets are functional and simple; marketing and splash art may be intricate. Areas players run past get macro forms only; stop points and landmarks get more. Texture only the sides the camera can see: a fixed camera can skip backs, an orbiting camera cannot.
- why: Close-up detail is wasted when the camera is far or the player runs past "at Mach 10" (R02); details give tangibility only as the sum seen at viewing distance.
- apply: Each brief names its display size and detail tier (in-game model, shop icon, key art). Environment detail tiers per area (path, stop point, landmark). Work and judge at the game camera distance, stepping back often. Roblox third-person cameras usually orbit, so props near paths get all sides; a locked top-down camera can skip backs.
- check: Capture at the game camera, speed and phone size (`thumb_check.py` for icons and in-game assets): detail that vanishes there is waste and is removed; an orbit capture around props near paths shows no untextured sides.
- mistake: Bringing splash-level detail into the game model; "if you do get too close ... you make things that are not even important" (R02:392-394); over-polishing details nobody sees.
- examples:
  - R01: lapel filigree simple in the in-game concept, intricate in the splash (R01:409-419, 946-952).
  - R10: heavy rope, hooks and straps are scribbles up close but sell the force together (R10:863-881).
  - R02: the Rift's far camera made fine detail irrelevant; blurry close-up texture sharpens at game distance (R02:392-412, 784-790, 962-970).
  - R02: Rift "was all from one angle"; do the other side "in case this is a game where you rotate around it" (R02:406-412, 744-746, 976-978).
- roblox_fit: Mesh budget 20,000 triangles each (knowledge/external/roblox-creator-docs/art/modeling/specifications.md:34); texture resolution 256, 512 or 1024 for 5, 10 or 20-stud objects (art/modeling/texture-specifications.md:25-27). Most Roblox games have a free orbit camera; assume all sides visible unless locked.
- roles: art-director, reference-images, modeler, marketing, ui-ux-designer, environment-designer, level-design, vfx-designer, orchestrator, reviewer
- also: world-level-readability, pipeline-production, visual-hierarchy
- sources: R01-F28 (R01:409-419, 946-952); R10-F24 (R10:863-881); R02-F20 (R02:392-412, 784-790, 962-970); R02-F21 (R02:406-412, 744-746, 976-978)

### MD-03 Finish comes from crisp edges and planes, balanced with soft
- principle: A texture looks finished through sharp, clean edges and chiselled planes, not more detail: an edge pass makes hard materials feel hard. Balance it: not every edge is sharp or highlighted (that feels stiff and unbelievable), and organic transitions stay soft. Soft airbrush everywhere looks mushy.
- why: The eye reads crisp edges as polish and as material hardness; uniform softness reads mushy, uniform hardness mechanical.
- apply: In the polish pass sharpen edges of carvings, trims and key forms (crisp bevel highlights, clean value breaks) and keep organic transitions soft. Curvature-driven edge highlights on hard materials, varied by a noise mask so part of the edges are dimmer (PROPOSAL default: 20-40 % of edges dimmer [inference]); soft materials (grass, fur, cloth) get soft edges. Modelers prefer clear plane changes and bevels over blobby surfaces; reference prompts ask for "planar, defined light and shadow shapes". UI and VFX: crisp key edges and cores, soft falloff [inference].
- check: Grayscale render at the game camera: main forms have defined light and shadow edges, no area is one smooth gradient; edges on the stone silhouette and key planes read; edge brightness varies; scan for zones where every edge is hard (stiff) or all soft (mushy).
- mistake: Adding more detail to look finished; "it always makes everything look super soft" (R10:295); "if every edge is highlighted, it makes it not believable" (R02:578-580); making "every single edge" sharp so it "feel[s] very stiff" (R13:643-644).
- examples:
  - R13: carvings on the metal ring cleaned with a sharp edge read as detail from afar; final cleanup "clean up even more edges" (R13:495-521, 640-646, 1050-1054).
  - R10: switching from airbrush to a flat brush to carve planes (R10:291-301).
  - R02: "stonework is really sharp, and it gives it that hard feel"; without edges "the mesh can look pretty mushy" (R02:114-118, 564-580).
- roblox_fit: On phones edge highlights are often the only material cue at distance, and soft gradients blur further [inference].
- roles: modeler, environment-designer, art-director, vfx-designer, ui-ux-designer, reference-images, marketing, reviewer
- also: value-contrast, shape-silhouette
- sources: R13-F24 (R13:495-521, 640-646, 1050-1054); R10-F13 (R10:291-301); R02-F05 (R02:114-118, 564-580)

### MD-04 Block material regions before shading
- principle: Before any shading, split the model into flat colour regions, one per material. Later passes change value only inside a region, so the "which part is which material" read stays clean.
- why: Clean material boundaries are decided once; shading can then be fast and loose without messy edges.
- apply: In Blender assign one material slot (or ID colour) per material before detail; in Roblox keep one Part colour or SurfaceAppearance region per material. Reference-images: ask for a flat-colour "material ID" version of the concept sheet [inference].
- check: Flat (unlit or emission) render at the game camera: each material region is one flat colour with clean edges; the region count matches the concept's materials.
- mistake: Painting detail before boundaries are set, so edges get "messy" (R03:74).
- examples:
  - R03: Caitlyn's red, blue, white and gold masked out before painting (R03:70-76).
- roblox_fit: Fewer material regions also mean fewer textures to load on phones [inference]; SurfaceAppearance adds PBR maps to a MeshPart (knowledge/external/roblox-creator-docs/art/modeling/surface-appearance.md:40).
- roles: modeler, art-director, reference-images
- also: pipeline-production, process-iteration
- sources: R03-F01 (R03:70-76)

### MD-05 Start texturing from baked AO and curvature; drive variation by rules
- principle: Bake ambient occlusion and curvature first and paint on top, keeping the shadows they place; let data drive placement (curvature for edge wear, height and slope for rock, dirt and grass) and reuse the same rule set for every asset of a material class.
- why: AO puts shadows "where we want them" and curvature finds every edge, so the texture stays tight; rule-driven placement gives natural variation fast and makes a set consistent.
- apply: Blender: bake AO and a curvature (pointiness) mask, multiply AO into the colour map at reduced strength, drive edge highlights from curvature at lowered strength, clean triangle artefacts. Keep material recipes (AO + curvature + noise) as Python data reused per material class. Terrain and part materials: a Studio or Blender script assigns materials by height and slope (rock on steep, grass on flat, dirt at transitions). A toon look comes from flat materials, controlled Lighting and value bands, not shaders.
- check: Flat (unlit) render: forms read from the texture alone and the contact shadow is defined; two assets of the same material side by side match; top-down and game-camera captures show rock on steep faces and grass on flats with no hand-placed seams.
- mistake: Painting over and losing the lighting detail the AO gave (R02:174-176); curvature artefacts highlighting triangles (R02:146-148); hand painting every surface.
- examples:
  - R02: occlusion and curvature in 3D Coat: "there's no actual lighting in here ... this is all just flat texture" (R02:98-118, 174-180, 366).
  - R00b: vertex colour by height for terrain, dirt on steep slopes, clamped light for toon shading (R00b:2641-2715).
  - R02: Substance rule sets texture a dragon statue exactly like the fox (R02:250-260).
- roblox_fit: Meshes get no baked AO from Roblox lighting, so bake it into the ColorMap [inference]. Terrain is 4x4x4-stud voxels, each with a material (knowledge/external/roblox-creator-docs/parts/terrain.md:13, 21-23); MaterialVariant custom materials use a different shader from base materials (parts/materials.md:248); custom shader code is not offered [unverified].
- roles: modeler, environment-designer, art-director, architect, feature-builder
- also: pipeline-production, value-contrast
- sources: R02-F04 (R02:98-118, 174-180, 366); R00b-F26 (R00b:2641-2715); R02-F15 (R02:250-260)

### MD-06 Material maps sell the surface; push, then pull back
- principle: A material is a set of inputs (colour, roughness, metalness, normal, transparency); the same image means different things in different channels. Colour plus normal (how light hits bumps) together sell a surface; pushing a value too far looks wrong, so push and pull back.
- why: Light response, not only colour, tells the material.
- apply: Build materials from colour, normal, roughness and metalness maps in Blender for SurfaceAppearance; tune strengths at the game camera under the game's Lighting and back off when overdone.
- check: Capture under the game's Lighting at game distance: the surface reads as its material; no overdone bumps or glossy plastic look.
- mistake: Cranking a map up "too much".
- examples:
  - R00a: a cracked-rock material from colour, normal and height maps; the height "too much" (R00a:1338-1446).
- roblox_fit: SurfaceAppearance supports ColorMap, NormalMap, RoughnessMap and MetalnessMap (knowledge/external/roblox-creator-docs/art/modeling/surface-appearance.md:63-114); no height map and no custom shaders, so height goes into geometry or the normal map.
- roles: modeler, environment-designer, vfx-designer, art-director
- also: pipeline-production, light-colour
- sources: R00a-F36 (R00a:1338-1446)

### MD-07 Choose materials and lighting together
- principle: The materials of a space and how the light interacts with them set the mood; rough, wet, metal and soft surfaces react to light differently.
- why: The light response carries the feeling.
- apply: Choose materials and lighting together in the art bible (for example wet stone under low, cold light); test every key material in Studio under the stage's final Lighting, not default light.
- check: Capture key materials under the final lighting at the game camera and compare with the mood anchor image.
- mistake: Picking materials under default light and lighting later.
- examples:
  - R00b: "the materials of the space, and how the lighting interacts with those materials" (R00b:1907-1913).
- roblox_fit: Material response depends on Roblox materials or SurfaceAppearance and Lighting.Technology; preview at the target graphics quality [unverified].
- roles: environment-designer, modeler, art-director
- also: light-colour, world-level-readability
- sources: R00b-F09 (R00b:1907-1913)

### MD-08 Test a new material on a small patch first
- principle: Make a small finished "microcosm" of a new material to find the method, then apply it everywhere. Medium noise first, then pull out shapes with highlights.
- why: It decides the look before the whole asset is committed and breaks up bland flat areas.
- apply: Render a small test patch (one block or swatch) of each new material and get it approved before the full pass.
- check: An approved test-patch render exists before the full material pass; the patch shows noise then highlight shapes, not a flat fill.
- mistake: A mesh that is "kind of flat ... bland" (R02:324).
- examples:
  - R02: random squiggles at low opacity, then colour-select and reinforce (R02:324-358, 388-390).
- roblox_fit: A material zoo place in Studio (VC-05) holds the patches.
- roles: modeler, environment-designer, reference-images
- also: process-iteration, references-ideation
- sources: R02-F17 (R02:324-358, 388-390)

### MD-09 Wear and condition tell the story
- principle: Flat, hard-edged, sterile props have no life. Put wear where hands and feet go (handles, rails, steps, edges), grime where dirt gathers, and choose material and condition to tell history (custom polished leather versus scrounged, worn cotton).
- why: Use marks tell who touched it and make objects believable; players read a character's history from wear, fit and material.
- apply: Modelers add chipped edges and darker grime or worn paint at touch points; material briefs carry a story reason (new and polished versus scrounged and worn), expressed through material choice and SurfaceAppearance roughness and wear, at the art bible's stylisation level. Reference prompts mention use wear.
- check: Close and game-camera captures: touch points show wear; no prop has perfectly untouched surfaces unless it is meant to be new; the condition contrast reads at the game camera, not only in close-ups.
- mistake: "very flat, hard-edged, sterile. There was no love" (R00b:2217-2235).
- examples:
  - R00b: wear around door handles, schmutz and grime (R00b:2217-2235).
  - R11: a darker Katarina without the custom leathers, more dishevelled (R11:245-252, 259-265).
- roblox_fit: Wear must be large enough to read at phone size; prefer painted value shifts in the texture over fine geometry [inference].
- roles: modeler, environment-designer, art-director, reference-images
- also: world-level-readability, character-design
- sources: R00b-F18 (R00b:2217-2235); R11-F20 (R11:245-252, 259-265)

### MD-10 Controlled imperfection makes it hand-made
- principle: Make subjects less than perfect, as if sculpted in clay: small dents, cracks, uneven edges and colour accents. Small inconsistencies make art feel hand-crafted.
- why: Perfect, uniform shapes read as machine-made and sterile; for AI and procedural output this "AI look" risk is high.
- apply: In Blender add slight bevel variation, chips, noise displacement or texture irregularity and a few colour accents, small relative to the main shape; vary stroke and edge strength; break symmetry slightly; avoid exact repeats and obvious tiling.
- check: Close-up and game-camera captures: forms show some irregularity; no exact repeats, perfectly even edges or visible tiling; hero props have no perfectly uniform flat colour areas.
- mistake: Sterile, perfect output.
- examples:
  - R13: rocks painted with dents, cracks and colour accents (R13:893-901).
  - R02: one-layer messy blending for a "handcrafted feel" (R02:232-240, 570-576).
- roblox_fit: Prefer texture over extra triangles for irregularity on phones [inference]; avoid obvious tiling of Roblox materials over big areas (Texture StudsPerTile: knowledge/external/roblox-creator-docs/parts/textures-decals.md:116).
- roles: modeler, environment-designer, art-director, reference-images
- also: style-identity
- sources: R13-F35 (R13:893-901); R02-F13 (R02:232-240, 570-576)

### MD-11 Ornament: one shaped motif, added late, small, with a reason
- principle: Replace a plain standard trim with one more interesting shape (filigree), simple enough not to add noise. Surface patterns come last, small, with a function (a grip texture) and in a support colour while the rest stays darker.
- why: Interest at the right scale; noise at the wrong one. A late pattern supports without breaking the big read.
- apply: Trims get one shaped motif, not many fine lines. Patterns go on functional zones only (grips, steps), as normal map or texture, tinted in an accent colour at low contrast.
- check: At the game camera the trim reads as one shape; the pattern is invisible at thumbnail size and visible close up.
- mistake: Plain standard trim, or over-busy filigree; pattern everywhere.
- examples:
  - R01: gold filigree on the lapel instead of a flat golden outline (R01:319-325).
  - R12: the grip pattern recoloured blue (R12:410-416).
- roblox_fit: Texture resolution limits detail (knowledge/external/roblox-creator-docs/art/modeling/texture-specifications.md:25-27).
- roles: modeler, art-director, reference-images, ui-ux-designer
- also: shape-silhouette, visual-hierarchy
- sources: R01-F21 (R01:319-325); R12-F34 (R12:410-416)

### MD-12 Functional parts and visible support make objects believable
- principle: Keep buttons, dials, switches, grips and soft parts (a rubber pad so the shoulder does not hurt): the brain wants to know how to use an object. When a cut or motif removes mass, add visible structure (braces, bolts, thickness) so it reads heavy, not fragile.
- why: Signs of use let viewers imagine holding it; visible support explains how the form holds together, and weight reads as quality.
- apply: Each prop, weapon or machine gets 1-3 functional details in the focal zone; split materials along a clean line where function changes (hard against rubber). After motif cuts in Blender, add braces or thickness at joints while keeping the silhouette clean.
- check: From one render a reviewer says how the object is held and operated; material split lines are straight and aligned; black-fill shows no thin unsupported necks.
- mistake: Pure decoration with no functional parts; fragile-looking forms after cutting in a motif [inference].
- examples:
  - R12: buttons kept, a rubber stock pad, a trigger cut-out comfortable for the finger (R12:142-151, 228-232, 237-241, 409).
  - R12: the bottom of a thunderbolt cut away and replaced with support "to make the gun a little bit heavy" (R12:181-183).
- roblox_fit: Functional details must be medium-size to survive phone view; thin parts alias on phones [inference].
- roles: modeler, art-director, environment-designer, ui-ux-designer, reference-images
- also: shape-silhouette, character-design
- sources: R12-F14 (R12:142-151, 228-232, 237-241, 409); R12-F15 (R12:181-183)

### MD-13 Ground every object: base, blended seams, colour bleed
- principle: Objects must sit in the world, not float on it: give hero props a ground base, paint across hard intersections where meshes clip into terrain, bleed a little of the object's colour onto the ground, and seat hazards with a darker blend; next to an already busy material, blend to a flat colour instead of adding detail.
- why: Hard straight intersections read as low-poly and pasted on; a defined footprint anchors the object and separates it from its surroundings; real objects bounce colour onto what is around them.
- apply: Hero props get a base patch (mound, plinth, ground patch) one value step from the open ground. Blend rock and prop bases into the ground with painted or vertex-colour transitions, sand piles or small debris over the seam. Tint the ground around plants and props with a soft hint of their hue. Add a darker ring around hazards and keep neighbouring surfaces plain.
- check: Capture at the game camera: no prop looks floating; no straight, clean intersection lines where props meet terrain; the ground near each prop carries a hint of its hue; hazard edges have a transition and the surfaces beside them are low-detail.
- mistake: Straight clipping seams that "make it feel very low poly" (R13:624); props that float or blend into the floor.
- examples:
  - R13: a sand base under the shrine (R13:489-491); rock bases painted over the terrain edge (R13:622-627, 637-640); grass-coloured ground under plants (R13:850-854).
  - R09: a darker blend near lava; "blending to a flat color just because there's already gonna be so much happening" (R09:843-846, 860-864, 929-935).
- roblox_fit: Terrain and part seams also show straight cuts; cover them with decals, small parts or terrain painting [inference]; vertex colour baked in Blender or Decals for blends [unverified].
- roles: environment-designer, modeler, art-director, level-design, vfx-designer
- also: world-level-readability, composition-focus, light-colour
- sources: R13-F23 (R13:489-491); R13-F27 (R13:622-627, 637-640); R13-F33 (R13:850-854); R09-F43 (R09:843-846, 860-864, 929-935)

### MD-14 Gold stays saturated in shadow
- principle: Gold gets muddy when shaded toward grey and black. Shade it toward more saturation (warm orange-brown), especially on close, intricate gold where facing surfaces bounce light into each other.
- why: Metals reflect their own colour; grey shading reads as dirty bronze.
- apply: Gold shadows and inner-facing areas move to higher saturation, not grey; avoid grey colour mixes on gold in SurfaceAppearance; same for gold UI frames and gold VFX [inference].
- check: Sample shadow pixels on gold: saturation equal to or above the mid-tone; no grey.
- mistake: Beginners "go towards the grays and the blacks" (R03:652-658).
- examples:
  - R03: Caitlyn's adjacent gold trims (R03:650-669).
- roblox_fit: Metallic materials depend on environment reflection [unverified]; check gold under the real map lighting.
- roles: modeler, art-director, environment-designer, ui-ux-designer, vfx-designer, reference-images
- also: light-colour
- sources: R03-F26 (R03:650-669)

### MD-15 Cracks taper; one width looks man-made
- principle: Natural cracks vary in width and taper; a single-width crack looks man-made. A thin highlight along the crack's edge sells depth.
- why: Natural damage tapers.
- apply: Taper crack strokes and decals; add a highlight edge along the crack line. Same for VFX ground cracks.
- check: Zoom on cracks in a capture: width varies along each crack and ends taper.
- mistake: "one width ... looks too man-made" (R02:672-674).
- examples:
  - R02: a crack along the fox's face with a highlight (R02:668-674).
- roblox_fit: Same for decals and VFX cracks.
- roles: modeler, environment-designer, vfx-designer
- also: none
- sources: R02-F31 (R02:668-674)

### MD-16 A few small glints sharpen hard materials
- principle: A few small bright glints on edges sharpen stone and metal and add scale cues.
- why: Tiny highlights define the material.
- apply: Place a few small highlights on edges facing the key light; keep them few (VC-07).
- check: Glints are visible at the game camera and few in number; they sit on light-facing edges.
- mistake: Glints sprinkled everywhere [inference].
- examples:
  - R02: glints on stone (R02:864-870).
- roblox_fit: Tiny glints vanish on phones; size them for the game camera [inference].
- roles: modeler, environment-designer
- also: value-contrast
- sources: R02-F36 (R02:864-870)

### MD-17 One trim sheet with a normal map can dress a whole environment
- principle: A trim sheet (strips of detail on one texture, with a normal map faking height) dresses many surfaces by mapping faces to different strips; a boring strip is fixed by remapping UVs to another strip, not by modelling more.
- why: The normal map makes flat faces catch light as if they had height; one shared texture saves memory and keeps style consistent.
- apply: The modeler builds one trim sheet per environment in Blender and maps faces by UV to strips; use it in Roblox through SurfaceAppearance or MaterialVariant [inference].
- check: Count texture sets per environment (target: few); a side-lit capture shows the normal detail reading.
- mistake: Modelling more geometry to fix a boring strip (R09:910-924).
- examples:
  - R09: a tower strip switched to a herringbone trim (R09:906-928).
- roblox_fit: Phone texture memory is limited, so one shared sheet helps [unverified]; trim sheets appear in knowledge/external/roblox-creator-docs/art/blender.md (line not checked).
- roles: modeler, environment-designer
- also: pipeline-production
- sources: R09-F41 (R09:906-928)
