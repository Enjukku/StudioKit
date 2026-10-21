> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit reference: universal. J008. Sources: environment paper notes `knowledge/reference/environment/01-place-guidance-scale-light.md` (rows RU, K, G, SC) and `02-ambience-life-dressing-terrain.md` (rows SD, TN, CO); first-game lessons `04-first-game-stages.md` (rows FS); facts checked in `fact-check-*.md`. Route, pacing and encounter design belong to `level-design` (game designer); this file is how the environment makes that layout read. Tags: **V** VERIFIED, **E** EXPERIENCE, **O** OPINION, **U** UNKNOWN.

# Place reading: guidance, scale, dressing, terrain, cohesion

## 1. The route is a contract
| ID | Practice | Evidence |
| --- | --- | --- |
| PR-01 | **Keep the game designer's route.** Collision edges, cover, routes, openings and encounter intent are theirs. Any change that touches route length, cover or timing is proposed to the game designer in the open, never hidden in an art pass. | RU01 O; K01-d O (Riot greybox practice, K01-a E) |
| PR-02 | **A beautiful reference image is not a route.** Turn each key-place image into an annotated target: focal point, camera, walkable area, silhouette layers, material roles, light sources, ambient life, and every unclear point. Where the image fights gameplay, ask for a ruling. | CO02 O; DN01 O |
| PR-03 | **Keep the accepted blockout.** In Blender keep a locked reference collection of it; in Studio keep blockout or validation proxies named and apart from the final art. Approve the art pass by comparing shots from the same camera, pose and route state before and after. | K01-e O; BW25 O |

## 2. Guiding the player
| ID | Practice | Evidence |
| --- | --- | --- |
| PR-04 | **Decide what the player must notice at each decision point before any decoration.** For each node of the route graph write a cue sentence: approach, intended next move, and why it reads (landmark, framed opening, light contrast, material change, sound source, or a blend). Then check the real camera backs the sentence. Never write "clear" without naming the object, the camera and the task. | RU02 O; G01 O; G03 O |
| PR-05 | **Far landmark and near cue are different jobs.** A far tower orients; a near doorway gives the next move. A tower seen through every wall may stop reading as a route; a doorway that looks like facade gets missed. Review how the two work together. Global orientation, district identity and local callouts are three separate jobs. | G02 O; K05-b O |
| PR-06 | **Design a far landmark twice:** as a place you can enter and as a shape seen from its approach. Literal scale can fail: small things at true scale read as specks from afar, so stylized massing, spacing or framing may serve the far view, while traversal sizes stay as approved. | K04-a E (Nintendo); K04-b O |
| PR-07 | **A destination can pull before the path is clear.** Pair a long-term landmark with short local cues; reveal enough to keep curiosity going; keep negative space so the focal object relates clearly to its surroundings. Never present an unreachable landmark as explorable if the game says "what you see you can reach". | K08-b O; K08-c O |
| PR-08 | **Three views per decision:** the approach (is the cue found in time), the decision point (is the choice clear), and after committing (is the next goal readable). Add the return trip if backtracking is allowed. | G05 O |
| PR-09 | **Enclosure is not safety.** "Sheltered from these sightlines" and "safe under these game rules" are different statements. Get the game state from the game designer before trying to convey calm, danger or contest. | G12 O; G10-G11 E |
| PR-10 | **The environment supports the characters; it does not compete.** Keep simple backgrounds under repeated decisions and rich detail where the player stops to look. Judge the place with a typical character, a UI state, an ability effect and an interactive object in view: a background rich on its own can bury an attack. | K02-a E; K02-d O; CO03 O |

## 3. Scale
| ID | Practice | Evidence |
| --- | --- | --- |
| PR-11 | **One scale convention everywhere.** Roblox's standard is 1 stud = 28 cm; the engine does no unit conversion, so the project must keep one convention across Blender, Studio, gameplay and audio. It is a conversion, not an avatar height or an order to build photoreal proportions. | RU04 V+O; SC01 V (fact-check-performance-import) |
| PR-12 | **Camera, collision envelope and movement are inputs from day one.** The scale sheet holds: the real avatar envelope, camera mode and offsets, supported avatar scaling, walk speed and abilities (jump, climb, mount, tool swing), interaction reach, held items that change clearance. Take them from the game designer and runtime config. | RU03 O; SC02 O |
| PR-13 | **Three clearances, three fixes:** visual (does it look like it fits), collision (does the real collision shape pass), camera (does the third-person camera stay usable on the way through). An ornate arch can look wide while its collision blocks; an opening can pass collision while the camera clips the lintel. | SC03 O |
| PR-14 | **No universal door or path size.** Derive each opening from the motion it must allow, that motion's collision envelope and a design margin. Paths add passing traffic, combat spacing and whether they should feel tight; ceilings add jumps and overhead gear. | SC04 O; DN02 O |
| PR-15 | **Exaggerate on purpose.** Bigger-than-real scale for shelter, grandeur or threat is allowed when intended. Record which relations bend (roof height, rock size, door framing, distance squeeze); gameplay openings stay tied to the route contract. | SC06 O |
| PR-16 | **Scale review:** the same spot with the player character, a familiar prop and the real camera; then once without the familiar prop to see if the place's own proportions carry the scale. | SC07 O |

## 4. Set dressing
| ID | Practice | Evidence |
| --- | --- | --- |
| PR-17 | **Dressing is evidence, not a quota.** Before placing a cluster, write who used it, why it is still there, what state the place is in, and whether it falsely promises loot or interaction. Decide the reading (delivery, storage, barricade, abandonment) first, then the spread. | K06-b O; SD01 O |
| PR-18 | **Composition-critical vs swappable.** An arch that frames the goal is part of the composition contract; a rope on the floor can change. Tag each object's role in the scene manifest so a cleanup pass knows what needs review. | SD02 O |
| PR-19 | **Calm space is designed.** Walkable ground keeps a quiet value structure so characters, pickups and effects read; an alcove where the player stops can hold more. "Empty" is about function, not instance count. | SD03 O |
| PR-20 | **Repetition is composition.** Vary grouping, rotation, spacing, height, material treatment and surroundings before asking for more unique meshes. Judge a repeated facade from the camera path players use (a pan shows a repeating highlight or window beat that a still hides). | SD04 O; SD06 O; RU11 O |
| PR-21 | **Intersection can be construction.** A rock sunk into a bank is fine; a chair hovering over the floor is a defect. Record where overlap is approved, the ground contact expected and the clearance moving parts need. For each prop family record: support surface, pivot, slope handling, collision role, visibility priority, placement exclusions (route lanes, interaction approaches, camera corridors, sound anchors, VFX attach zones). Keep walk lanes clear of props instead of switching off collision on props players can reach. | SD07 O; SD08 O |
| PR-22 | **Detail where attention is.** A first-person shooter put detail above head height; a third-person phone camera sees a different band. Measure the band your camera really shows. | K01-c E; K01-f O |

## 5. Terrain and nature
| ID | Practice | Evidence |
| --- | --- | --- |
| PR-23 | **Terrain or mesh, by what the shape needs.** Terrain for continuous sculptable volume and smooth material blends; meshes for chosen silhouettes, hard stylized strata, overhangs, modular reuse or exact UV direction. Combine big terrain masses with rock and foliage kits; check seams from eye height and from the ends of traversal. No source proves one is always cheaper: compare on the target phone. | TN03 O; TNT4 O |
| PR-24 | **A biome is a coordinated set:** palette, material, wind and sound together, with a narrow vocabulary and a written exception list (dominant ground cover, drainage, signs of moisture, typical sound sources, human traces, how it meets its neighbors). A swamp is not "green plants plus fog". Restrained variety with strong colour makes regions memorable. | TN04 O; K03-a E; K03-c O |
| PR-25 | **Water is several jobs:** the visible surface, how the player moves in it, its sound sources, mist, and the shoreline dressing. | TN04 O |
| PR-26 | **Scatter repeatably.** Use masks and recorded seeds so a path change regenerates its margins; keep exclusion zones around routes, doors, landmarks and interaction surfaces. A new seed is a new scene, not a neutral rebuild. | K03-d O; H07 O |
| PR-27 | **Protect an organic landmark's silhouette at every viewing distance before adding cracks and detail.** | TN04 O |

## 6. Cohesion with the art director
| ID | Practice | Evidence |
| --- | --- | --- |
| PR-28 | **The art bible is a versioned input.** Before a stage, note its version, palette roles, shape families, material response, light direction, detail hierarchy, anchors, and what stays flexible. Naming the flexible parts keeps places from becoming clones. | CO01 O |
| PR-29 | **One target slice before multiplying detail.** Pick the hardest representative section (art, movement, light, ambience, performance together) and prove the style there at the supported tiers, with a character, UI and gameplay effects present. The art director reviews; the owner decides direction changes. | RU05 O; W04 O; ST05 O |
| PR-30 | **One world premise, shown everywhere.** Invent the place's cause-and-effect premise, then check terrain, architecture, props, VFX and ambience all show matching consequences. A landmark's build state can tell history with no sign. | K10-b O; K09-b O |
| PR-31 | **Respect real cultures.** Cultural references are checked by qualified reviewers; looking recognizable does not excuse a stereotype. Never copy another game's layout, landmarks, names or assets. | K05-d O; K10-c O; level-design §5 |
| PR-32 | **Review notes name the layer.** Location and camera, the observed defect, the intended reading, the likely cause, the responsible specialist, what must be kept, and the evidence needed. No mood-only notes. | CO08 O; RV04 O |
