---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [level-design, environment-designer, game-designer, art-director, modeler, vfx-designer, ui-ux-designer, film-director, marketing, reference-images, orchestrator, architect, sound-designer, reviewer, qa-lead, feature-builder, progression-designer]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# World and level readability

Worlds and levels that play clearly and still feel like real places: what the player must read, how routes and first views guide them, how scale and story make a place believable.
WL-01 to WL-05 put gameplay reads first (critical information, items, affordances, believable constraints, hazards). WL-06 to WL-11 plan the level (rank the screen, first view, spawn routes, forward paths, entrances, conventions). WL-12 to WL-20 make the play space readable (markers, height cues, flat floors, predictable geometry, dead space, themed blockout, material rules, clean floors, low settings). WL-21 to WL-28 make it a believable world (scale, story, identity, the whole space, depth, distance checks). Environmental storytelling (a small extract topic) is folded in here.
Related: detail and rest in `visual-hierarchy.md` (VH-05), value bands in `value-contrast.md` (VC-05, VC-06), effect footprints in `vfx-reads-timing.md`, map design as gameplay in `game-design-fun.md`.
Stage 1c (DestructionSimulator cross-check) added WL-29 (routes in seconds at walk speed, ledges against jump height) and WL-30 (the scored ten-check level review); the (DS) line in WL-23 comes from the same check.

### WL-01 Gameplay readability beats beauty; test it in the busiest moment
- principle: The player must instantly know where to go, where they are, who is ally and who is enemy, and how much health and threat there is. Environment and effects art must never hurt that read. Bridge the tension between art that looks great and art that plays great by asking "how does my art enhance gameplay?", not by chasing a perfect piece.
- why: Players decide in fractions of a second; information that needs study is missed. The best art can distract and hurt players, and the most intense play spaces suffer most.
- apply: Each level, environment and VFX brief lists the critical facts for its screens (route, location, ally or enemy, health, threat) and the gameplay read each piece must support (cover, sightline, route, hazard); each fact gets a dedicated read (team colour or Highlight, landmark, path contrast, HUD bar). Reviews run on play-test captures with characters and effects on screen; the strictest priority goes to where the most intense play happens.
- check: Capture the busiest expected moment (many players plus effects) at the game camera on a phone-size viewport: for each critical fact, it is found at a glance; character and attack read against the background (`look_check.py value` subject/ring ratio); the reviewer's first question is "what is the gameplay read here, and does any art element weaken it?" before style questions.
- mistake: Testing readability in an empty scene; "sometimes that best art distracts from the game, and it hurts players" (R02:434-436); "you don't wanna get too lost in creating the perfect piece of art" (R09:1018-1020).
- examples:
  - R00a: "have you ever been in a team fight in League of Legends?" (R00a:99-131).
  - R02: play-test feedback: "your texture was way too crazy. Tone it down" (R02:430-438, 820-834).
  - R09: bombsites, where the most intense play happens, get the strictest readability priority (R09:52-58, 72-76, 1018-1022).
- roblox_fit: Phones shrink everything and many players and effects share the screen, so the busy case is the default. Highlight can mark allies and enemies but only 255 display at once (knowledge/external/roblox-creator-docs/effects/highlighting.md:37).
- roles: art-director, environment-designer, level-design, game-designer, ui-ux-designer, vfx-designer, modeler, reviewer, qa-lead
- also: visual-hierarchy, value-contrast, critique-feedback
- sources: R00a-F02 (R00a:99-131); R02-F23 (R02:430-438, 820-834); R09-F04 (R09:52-58, 72-76, 1018-1022)

### WL-02 Items must be identifiable on the ground, even partly hidden
- principle: "It's not that the effects should look cool, it should be readable." Players must identify an item on the ground in a split second, even with part of it hidden behind a box.
- why: Wrong pickups cost games; decisions are fast.
- apply: Item silhouettes per type differ in their top and side profiles; variants keep the type's recognition features (CD-04); test partial occlusion.
- check: Capture items on the ground at the game camera with 30-50 % occluded by a box: a reviewer names the type correctly.
- mistake: Variant reskins that blur type differences.
- examples:
  - R12: a magazine hidden by a box corner; Phantom versus Guardian or Vandal confusion is a real disadvantage (R12:417-431).
- roblox_fit: Top-down and third-person cameras see items from above, so the top silhouette matters most [inference].
- roles: art-director, modeler, vfx-designer, game-designer, level-design, reviewer, qa-lead
- also: shape-silhouette, character-design
- sources: R12-F35 (R12:417-431)

### WL-03 Every piece says "what I am" and "what you can do here"
- principle: An environment communicates a believable setting and the gameplay information at the same time: a cliff that is clearly a cliff and clearly climbable.
- why: Players read both together and can act without a tutorial.
- apply: For each interactive element, write two lines: setting ("I'm obviously a rocky cliff") and gameplay ("clear ledge climbing"). The gameplay part reads with a shape, value or colour treatment used consistently everywhere (same ledge look, all shootables share one look).
- check: Show a game-camera capture to a fresh agent with no notes: it names both what the place is and what can be done there; in grayscale and at thumbnail size, gameplay surfaces still stand out.
- mistake: Places that look nice but hide what is interactive, or are readable but look like a test level.
- examples:
  - R00b: the cliff with ledges, the eerie hallway with a sack of goo to shoot, a pool that may or may not be safe (R00b:1831-1859).
- roblox_fit: Phone screens make small cues hard to see; test at thumbnail size with `look_check.py thumb`.
- roles: environment-designer, level-design, game-designer, modeler, vfx-designer, qa-lead
- also: game-design-fun, visual-hierarchy
- sources: R00b-F05 (R00b:1831-1859)

### WL-04 One gameplay constraint, many fictional answers
- principle: A gameplay constraint can be dressed many ways (a boundary as a wall, a building, or a cliff over the ocean); pick the answer that makes the place most beautiful and believable.
- why: All options serve the same gameplay, so the choice is free to serve mood and story; an obviously artificial wall breaks belief.
- apply: For each constraint (boundary, choke point, cover, height gate), list 2-3 fictional solutions and pick with the art director by fit with the setting; record the choice in the stage notes.
- check: At the game camera no boundary reads as an arbitrary invisible or plain wall; for each, answer "why is this here in the world?" in one line.
- mistake: Solving a constraint with the first generic blocker.
- examples:
  - R00b: a gameplay boundary as wall, building, or cliff overlooking the ocean (R00b:1815-1829).
- roblox_fit: Invisible walls are common on Roblox; prefer a believable visual blocker with a collision part matched to it.
- roles: environment-designer, level-design, game-designer, art-director
- also: style-identity
- sources: R00b-F04 (R00b:1815-1829)

### WL-05 Hazards explain themselves
- principle: A hazard visually explains where it comes from and is contained by believable structure (fences, rails).
- why: Players accept a place that makes sense.
- apply: Each hazard gets a visible source and containment in the brief and the build [inference].
- check: From one capture, a reviewer says where the hazard comes from.
- mistake: Skinning a hazard without explaining it ("we were just trying to skin it").
- examples:
  - R09: the lava would get a visible source and more structure in the fences (R09:1132-1141).
- roblox_fit: Same.
- roles: environment-designer, art-director, modeler, level-design
- also: style-identity, game-design-fun
- sources: R09-F50 (R09:1132-1141)

### WL-06 Rank the environment work: it is 90 % of the screen
- principle: The environment is about 90 % of the screen and there is always more to build than time allows, so rank work by what matters most to the experience, decided with the game designer, not rock by rock.
- why: Without the environment the player sees "an empty void"; polishing every piece equally burns the budget on things no one looks at.
- apply: Before building a stage, the environment designer writes a ranked list with the game designer: play spaces and routes first, landmarks and first view next, filler last. Effort, unique assets and triangles follow the rank; background takes reused kit pieces [inference].
- check: Capture the 3-5 most-visited views at the game camera: every top-ranked item is visible and finished in them; count unique assets per area against the ranked list.
- mistake: Treating every tree and rock as equally important.
- examples:
  - R00b: "it's basically 90% of the screen"; artists rank with designers and concept artists (R00b:1695-1749).
- roblox_fit: Phones have a low draw budget, so ranking also decides where parts and triangles go (meshes max 20,000 triangles: knowledge/external/roblox-creator-docs/art/modeling/specifications.md:34).
- roles: environment-designer, art-director, level-design, orchestrator, game-designer
- also: pipeline-production, process-iteration
- sources: R00b-F01 (R00b:1695-1749)

### WL-07 The first view tells where you are and what to do
- principle: Start a level with an establishing view that tells the player where they are and what they are about to do; on first sight of a play space, the player has a general idea of where the key actions happen.
- why: First-time players need the space to explain itself; orientation comes before action.
- apply: Level design sets spawn position and facing so the first view after spawn (or teleport) frames the goal or main landmark; list the 3-5 key actions per space and give each a visible cue [inference]. A cutscene is optional; the spawn camera can do it.
- check: Capture the first frame after spawn at the default camera: the goal or landmark is visible and is the strongest focal point; a reviewer unfamiliar with the map names where each key action happens.
- mistake: Spawning players facing a wall, with no view of where to go.
- examples:
  - R00b: Ratchet & Clank levels open with an establishing composition (R00b:1887-1899).
  - R09: on the lava site you know where to smoke and where to plant behind safe cover (R09:437-444).
- roblox_fit: Set SpawnLocation orientation and the default camera; on phones the first view must read at small size.
- roles: level-design, environment-designer, game-designer, film-director, art-director, qa-lead
- also: composition-focus, game-design-fun
- sources: R00b-F07 (R00b:1887-1899); R09-F22 (R09:437-444)

### WL-08 Spawns first, then the route to the objective
- principle: In a blockout, place the spawns first, then build the path that bridges spawn to objective; side areas come after.
- why: The spawn-to-objective route defines timing and the first player experience; everything else hangs off it.
- apply: Blockout order: spawn points, objective, routes between, side areas [inference beyond "spawns first"].
- check: The first blockout review shows spawns and objectives placed and connected before any side area or detail.
- mistake: Building side areas before the main route works [inference].
- examples:
  - R09: Diego starts with the attacker spawn, then bridges to B site (R09:108-110, 136).
- roblox_fit: SpawnLocation sets where players respawn (knowledge/external/roblox-creator-docs/_api-reference/classes/SpawnLocation.yaml:9-17).
- roles: level-design, game-designer, environment-designer
- also: process-iteration, game-design-fun
- sources: R09-F06 (R09:108-110, 136)

### WL-09 Paths face forward; no doubling back in multiplayer maps
- principle: From spawn, paths face forward so players always feel progress; avoid turning around or looping back. Keep the layout simple so players reach the action fast. A player who never gets lost is the sign of good level design.
- why: Doubling back "feels weird" in multiplayer; simple layouts cut time to fun.
- apply: Draw the route graph from each spawn; no edge from spawn to objective reverses direction by more than about 90 degrees [inference]; side loops only where intended. Exploration games may backtrack on purpose.
- check: Top-down capture with routes drawn; a walk-through capture never turns the camera back to reach the objective; measure time from spawn to first contact [inference].
- mistake: Dead-end-and-return layouts copied from exploration games into multiplayer maps.
- examples:
  - R09: VALORANT spawns where everything faces forward, versus Metroidvania backtracking (R09:184-201, 792-794).
- roblox_fit: Mobile players steer with a thumbstick, so reversals cost more [inference].
- roles: level-design, game-designer, environment-designer
- also: game-design-fun
- sources: R09-F11 (R09:184-201, 792-794)

### WL-10 Keep the layout simple: two ways in per side
- principle: Under the art, maps are simple: each objective gives each team two ways in.
- why: Two options give choice without overwhelming.
- apply: Route graph default for team objective maps: two entries per team per objective [inference: default].
- check: Count entries per team on the top-down capture.
- mistake: Many tangled entries that overwhelm new players [inference].
- examples:
  - R09: Ascent A has main and tree for attackers; the minimap shows the map is less daunting than it seems (R09:474-496).
- roblox_fit: Same.
- roles: level-design, game-designer
- also: game-design-fun
- sources: R09-F24 (R09:474-496)

### WL-11 One orientation convention across all maps
- principle: Use one spatial convention across every map so players orient in a new map at once ("where's B? just look to your left").
- why: Players transfer knowledge from old maps to new ones.
- apply: The game designer and level designer define cross-map conventions (shop always right of spawn, exit always ahead) in the game profile; every new map keeps them [inference].
- check: New-map review lists the conventions and confirms each holds from the spawn view.
- mistake: Each map with its own logic [inference].
- examples:
  - R09: on a new map, attackers still find B by looking left (R09:136-146).
- roblox_fit: Fits hubs and multi-map Roblox games with a fixed spawn camera direction [inference].
- roles: level-design, game-designer, environment-designer
- also: game-design-fun
- sources: R09-F08 (R09:136-146)

### WL-12 Mark objectives on the approach and in the floor
- principle: In-world markers point to objectives, from subtle (a worn sign where only the A is legible) to obvious (a huge letter on the landmark). Put markers where players approach, the biggest on the landmark everyone sees coming in, and separate the objective area in the floor with a border so it says "here" without UI.
- why: Markers guide the approach; inside the site a marker is redundant; a floor border marks the most important space.
- apply: Environment designers place markers on approach routes and on the main landmark facing the approaching side; modelers cut the objective floor as its own piece with a border trim or decal inside the environment palette (value does the read) [inference].
- check: From each spawn route, a game-camera capture shows an objective marker before entry; the landmark marker reads at thumbnail size (`thumb_check.py`); a top-down or game-camera capture at thumbnail size shows the objective outline.
- mistake: Markers only inside the objective, where they are redundant.
- examples:
  - R09: Sunset's parking sign with only the A legible; a huge B on the tower facing attackers (R09:146-153, 1082-1089).
  - R09: a trim border around the bombsite floor (R09:700-705).
- roblox_fit: On phones, signs must be large; a Decal or a separate Part with a distinct material is cheap [inference].
- roles: environment-designer, level-design, art-director, ui-ux-designer, modeler
- also: visual-hierarchy, composition-focus
- sources: R09-F09 (R09:146-153, 1082-1089); R09-F38 (R09:700-705)

### WL-13 Head-height cues and directional patterns guide the eye
- principle: Subtle head-height indicators (a crate at player height, a trim line on walls at head height) guide where players look; patterns flowing in one direction lead the eye toward where enemies may come from. Where a prop already shows player height, no extra cue is needed.
- why: Players pre-aim and scan at head height; consistent cues make that automatic, and line direction leads the eye.
- apply: Add a trim line or ledge at character head height on long sightline walls; run pattern lines toward enemy entries [inference on placement]. Head height = the game's character eye height measured in Studio [inference].
- check: From each defensive or key position at the game camera: a head-height cue is visible on main sightline walls; pattern lines point toward entries, not away.
- mistake: A redundant indicator where a crate already shows height (R09:642-644).
- examples:
  - R09: Abyss trim lines double as head-height indicators; a downward-flowing pattern points to where defenders come from (R09:638-654).
- roblox_fit: In third-person or top-down phone games, height cues matter more for jump and cover reads than for aim [inference].
- roles: environment-designer, modeler, level-design, art-director
- also: composition-focus, visual-hierarchy
- sources: R09-F33 (R09:638-654)

### WL-14 Flat play spaces; every height change is intentional
- principle: Keep play spaces mostly flat; put elevation only in chosen spots with short ramps; keep things smooth at head level. Verticality is allowed only on purpose; a target a few pixels off the expected line can decide a fight.
- why: Friction from terrain makes players feel the map killed them.
- apply: Level design sets a standard eye-height plane per area and lists every deliberate elevation with its reason; modelers keep walk-area floors flat (no bumpy rocks under feet) [inference].
- check: Captures along each route at the game camera: every place where a likely enemy sits far above or below the expected line is on the intentional list [inference].
- mistake: Long ramps and random height changes; mossy rocks under feet (R09:1013-1015).
- examples:
  - R09: boxes someone can jump onto force "a huge flick" and are avoided unless intended (R09:282-298, 1011-1046).
- roblox_fit: For third-person or top-down phone games the principle becomes "no surprise height that hides threats from the camera" [inference].
- roles: level-design, environment-designer, game-designer, modeler, qa-lead
- also: game-design-fun
- sources: R09-F14 (R09:282-298, 1011-1046)

### WL-15 Predictable geometry: players lose to opponents, not to the map
- principle: Blockouts and much of the final geometry are clean boxes; "what is an angle but a sliced cube". Collision stays as simple and predictable as the visible shape.
- why: Predictable geometry gives fair fights.
- apply: Modelers keep collision close to the blockout's box shapes; decoration sits outside the collision envelope [inference].
- check: Collision view in Studio: collision is simple boxes matching the visible shape; no snag points along routes.
- mistake: Unpredictable geometry that makes players "lose because of the map".
- examples:
  - R09: cubes are predictable (R09:497-507).
- roblox_fit: Box collision is cheap; set complex meshes to box or hull collision fidelity [unverified].
- roles: level-design, environment-designer, modeler, game-designer
- also: shape-silhouette, pipeline-production
- sources: R09-F25 (R09:497-507)

### WL-16 Name dead space and oversized areas in self-review
- principle: Critique your own blockout for dead space, no-man's land and oversized areas, and fix them by iteration.
- why: Dead space is time with no decisions.
- apply: The level designer's self-review lists dead areas and compares sizes with comparable spaces [inference].
- check: Top-down capture: mark areas that no route or fight uses; each is cut, shrunk or given a purpose.
- mistake: Leaving no-man's land.
- examples:
  - R09: "there's a big no man's land here"; "probably too big for a normal bombsite" (R09:386-389, 516-520, 1124-1128).
- roblox_fit: Same.
- roles: level-design, game-designer, environment-designer, reviewer
- also: critique-feedback, game-design-fun
- sources: R09-F27 (R09:386-389, 516-520, 1124-1128)

### WL-17 In a themed game, the blockout already reads as a place
- principle: When the game has a strong theme, the gray box uses shapes that could be real structures of that theme, so the blockout tells the story and helps art; abstract shapes force artists to invent sense for weird geometry.
- why: Art can build on a blockout that already reads as a place.
- apply: Level design's blockout uses theme-plausible shapes; ask the environment designer early when a shape is abstract [inference].
- check: The environment designer names a real-world structure for each major blockout shape.
- mistake: Abstract blockout shapes that art must justify later.
- examples:
  - R09: The Last of Us's destroyed Seattle had cars, high-rises and shops in the gray box (R09:422-437).
- roblox_fit: Same.
- roles: level-design, environment-designer, art-director, modeler
- also: style-identity, process-iteration
- sources: R09-F21 (R09:422-437)

### WL-18 Materials follow gameplay rules
- principle: When a surface's behaviour matters (can it be shot through, broken, climbed), the gameplay rule comes first and the material follows it, one material per gameplay piece; surfaces no one plays around give art freedom.
- why: Players learn material = behaviour; mixed materials confuse.
- apply: Level design marks each relevant surface's gameplay property; modelers and environment designers pick materials from a material-to-rule table [inference]; sound uses the same table for impacts.
- check: Material audit: every gameplay-relevant surface's material matches its rule.
- mistake: Mixed materials on one gameplay piece.
- examples:
  - R09: a back wall can be wood ("you're not gonna shoot anyone behind that wall"); site metal, the rest concrete (R09:392-403, 606-622).
- roblox_fit: Only relevant if the game has penetration or destruction; raycasts can read the hit Material [unverified].
- roles: level-design, environment-designer, modeler, game-designer, sound-designer
- also: materials-detail, game-design-fun
- sources: R09-F19 (R09:392-403, 606-622)

### WL-19 Floors stay clean enough for the smallest gameplay object
- principle: Floors in play areas must stay readable for small gameplay objects (traps, pickups, tripwires); decorative ground cover is added, then cut back to "a whisper".
- why: Small gameplay items on busy floors get lost.
- apply: Keep ground clutter sparse in play areas and test with the game's smallest gameplay object placed on each floor type [inference].
- check: Game-camera capture with the smallest gameplay object on each floor type: still visible at phone size (`thumb_check.py` on the crop).
- mistake: Overdressing floors ("you add so much and then you just leave like a whisper", R09:938).
- examples:
  - R09: grass cards kept minimal for traps and tripwires (R09:936-943).
- roblox_fit: Phone screens make small objects tiny; stricter on Roblox [inference].
- roles: environment-designer, modeler, vfx-designer, level-design, reviewer
- also: materials-detail, visual-hierarchy
- sources: R09-F44 (R09:936-943)

### WL-20 It must read at the lowest graphics setting
- principle: Many players (and top players by choice) run low detail settings; a map must read at low detail and not feel noisy at high.
- why: Readability cannot depend on decoration that a setting removes.
- apply: Capture each key position at the lowest and highest graphics quality; gameplay cues exist in both [inference].
- check: Two captures per key position (lowest and highest quality): every gameplay cue is present in both; the high setting is not noisier in the player band.
- mistake: Readability that depends on detail the low setting removes [inference].
- examples:
  - R09: Diego thought Corrode was "so detailed" until he switched from low to high (R09:951-969).
- roblox_fit: Roblox scales graphics quality and lowers shadow quality at low settings (knowledge/external/roblox-creator-docs/performance-optimization/improve.md:419); test at several quality levels (performance-optimization/design.md:31).
- roles: environment-designer, art-director, architect, qa-lead
- also: pipeline-production
- sources: R09-F46 (R09:951-969)

### WL-21 Scale: a player-sized reference in every blockout and scene
- principle: Scale is easy to get wrong and ruins belief. Always block out with a character in the scene and put known-size objects (doors, stairs, railings, chairs, plants, grass) near big structures; without them a thing "could be the size of five buildings".
- why: Players judge size against their own avatar and familiar objects; a known-size object also makes the focal point look grander.
- apply: Put a standard player character in every greybox and every model review scene (Blender and Studio). Size interaction props (doors, stairs, railings, seats) to the character first, then the rest; place known-size props near large focal props.
- check: Capture the character next to each interaction prop at the game camera and measure heights in studs against the character; flag furniture or doors off by more than the style allows; every scene has at least one familiar-size object near the focal prop.
- mistake: A whole room blocked out without a character, ending in "a twenty-foot desk" (R00b); "How big is the player? ... You don't know" (R13:390-394).
- examples:
  - R00b: the twenty-foot desk (R00b:2013-2035).
  - R02: grass blades tell the fox is about human size (R02:500-518, 984-990).
  - R13: plants beside the shrine set its size and make the disk look grand (R13:388-404).
- roblox_fit: The Roblox greybox sample keeps doorways and hallways at least 10 studs wide and walls at least 10 studs tall, with a default jump height of 5 studs and camera room (knowledge/external/roblox-creator-docs/tutorials/curriculums/environmental-art/greybox-your-environment.md:77). Roblox often exaggerates doorways for the third-person camera.
- roles: environment-designer, level-design, modeler, art-director, film-director, marketing, reference-images, reviewer, qa-lead
- also: composition-focus, pipeline-production
- sources: R00b-F14 (R00b:2013-2035); R02-F27 (R02:500-518, 984-990); R13-F17 (R13:388-404)

### WL-22 Environmental storytelling: someone lives here, time has passed
- principle: Layout and props tell who lives here, what happened, climate and age. Signs of use and time (wear, cracks, leaves under trees, repairs, laundry, food remnants, chipped and buried rocks) make a place feel inhabited instead of dead and stale.
- why: Players infer history and inhabitants from what is left behind, which deepens the fantasy without text; a spotless place pulls them out.
- apply: For each stage write 3 story facts (climate, age, who lives here, what happened) and for each hero prop 1-2 history facts; assign each to visible props, wear and layout, inside the hierarchy (backdrop-level contrast). Reference-image prompts include the facts.
- check: A fresh agent viewing captures without notes states at least one intended story fact; each main area has at least one story cluster [inference]; hero props show age or use.
- mistake: "a dead level"; "it just feels very stale. You can't get lost in it" (R02:734-736); spotless "first person ever here" spaces.
- examples:
  - R00b: Horizon Zero Dawn's collapsed robots; Kingdom Come camps with food remnants, boarded potholes, bandits' laundry (R00b:1941-1987).
  - R02: the pedestal's broken side and cracks make it lived in (R02:410-414, 724-740).
  - R09: leaves on the ground under trees; fingerprints on a realistic gun (R09:456-473).
  - R13: the shrine half buried in sand, rocks chipped by centuries of hot weather, possible fossils (R13:355-379).
- roblox_fit: Story props must be big enough to read at the game camera on a phone; use decals and a few props within part and texture budgets [inference].
- roles: environment-designer, modeler, art-director, level-design, game-designer, film-director, reference-images
- also: materials-detail, style-identity
- sources: R00b-F12 (R00b:1941-1987); R02-F32 (R02:410-414, 724-740); R09-F23 (R09:456-473); R13-F15 (R13:355-379)

### WL-23 Give each zone or team an identity symbol
- principle: Recurring statues, tablets and symbols in the world tell lore ("oh, what is that?") and give each team or zone an identity players use for orientation and belonging.
- why: Players infer a world from objects; symbols help them know where they are.
- apply: Each team base or zone gets a recurring symbol or creature statue visible from its entry; small lore props sit near paths.
- check: List per zone: at least one identity prop visible from its entry at the game camera [inference]; symbols are large enough to read on a phone.
- check (DS): From every route fork at the game camera at least one landmark is visible; each zone's main landmark is visible from most of the zone and has a unique black-fill silhouette, not only a unique colour (DS:level-design/SKILL.md:36).
- mistake: Zones that look the same, so players cannot tell where they are [inference].
- examples:
  - R02: owls for red side and stags for blue side on Summoner's Rift; a tablet with five-versus-five hieroglyphs (R02:164-174, 274-278).
- roblox_fit: Works in team games and hubs; keep symbols large for phones.
- roles: environment-designer, level-design, game-designer, art-director, modeler
- also: style-identity, composition-focus
- sources: R02-F10 (R02:164-174, 274-278)

### WL-24 Build and judge the whole space, not only the hero prop
- principle: A great single prop is not enough; build the full environment and judge each prop inside it.
- why: A prop's quality only matters in context; the whole set shows scale, story and cohesion problems a single prop hides.
- apply: Brief props as part of a set ("the whole bar", not "a tequila bottle"); review new props inside their stage at the game camera, not alone on a turntable.
- check: Every prop approval includes at least one in-stage capture at the game camera.
- mistake: "Anyone can make, like, a badass tequila bottle" and stop there (R00b).
- examples:
  - R00b: push yourself to make the whole bar (R00b:2203-2215, 2237-2253).
- roblox_fit: No change.
- roles: environment-designer, modeler, art-director
- also: critique-feedback, style-identity
- sources: R00b-F17 (R00b:2203-2215, 2237-2253)

### WL-25 Distance lowers contrast and detail (atmospheric perspective)
- principle: Reduce contrast and detail with distance; it creates depth and pushes attention to the nearer, sharper play space.
- why: Distant low-contrast areas read as far and stop competing.
- apply: Use Atmosphere and fog to drop distant contrast; use simpler distant models; keep high-detail work in the near and mid ground the player uses.
- check: Capture from the play camera: `look_check.py value` on near and far bands shows contrast falling with distance.
- mistake: Full-contrast, full-detail backgrounds that compete with the play space [inference].
- examples:
  - R00a: Uncharted and God of War reduce detail in the distance (R00a:368-378).
- roblox_fit: Atmosphere Density and Offset blend distant objects into the sky (knowledge/external/roblox-creator-docs/environment/atmosphere.md:29, 46), which also lowers phone draw cost [inference].
- roles: environment-designer, art-director, film-director, marketing, level-design
- also: composition-focus, light-colour
- sources: R00a-F12 (R00a:368-378)

### WL-26 A small, low-contrast busy background adds life
- principle: A busier, "crawly" background crowd or activity makes more seem to happen while the main characters stay clear, provided it is small and lower contrast.
- why: Background activity adds story density without competing.
- apply: Background crowds and props at small scale and lower contrast behind the play space or in key art; use real crowd references for natural grouping.
- check: Squint or blur test: the background reads as texture and the main characters are still read first.
- mistake: A busy background at the same contrast as the subject [inference].
- examples:
  - R05: more zombies in the background, from crowd references (R05:526-527, 712-716).
- roblox_fit: Use cheap far-away parts, decals or billboards; keep NPC counts inside the performance budget [unverified].
- roles: environment-designer, art-director, marketing, level-design, vfx-designer
- also: visual-hierarchy, composition-focus
- sources: R05-F25 (R05:526-527, 712-716)

### WL-27 A few upright grass cards give the ground depth
- principle: Painted ground is flat; a few upright grass cards give it depth.
- why: Vertical breaks catch light and silhouette against the ground.
- apply: Place a few planes with grass texture at edges and rest areas, never covering play-area floors (WL-19).
- check: Side-view capture shows ground depth; play floors stay clean.
- mistake: Many cards that cover small gameplay objects [inference].
- examples:
  - R02: he wanted grass cards for depth (R02:970-974).
- roblox_fit: Alpha cards cost overdraw on phones [unverified]; keep them few.
- roles: environment-designer, modeler
- also: materials-detail
- sources: R02-F38 (R02:970-974)

### WL-28 Work from far away; zoom out every round
- principle: Do not work zoomed in. Keep returning to the game distance: the first read must hold when you squint (it looks human, the coat reads as a coat). Working only close makes you focus on details that harm the overall design.
- why: Players see things small and far; detail done close up is invisible at game size. It is the mistake seen most in new character artists (R03).
- apply: Every review round includes a capture at the game camera distance and phone size before any close-up; only zoom in after the far read passes.
- check: `look_check.py thumb` or `thumb_check.py` measures each round, plus a blurred (squint) capture at the game camera: name the subject and each major part; a piece that only works close up fails.
- mistake: "working really close to the character" and losing the far read (R03:198-206); detailing only at high zoom.
- examples:
  - R03: squint test: still a human, coat still a coat; even shading painted from far away (R03:198-208, 1034-1036).
  - R12: "I'm zooming out a lot ... to understand it's still readable" (R12:357-359).
- roblox_fit: Phones with a third-person camera and many players make far zoom the default view [inference].
- roles: modeler, art-director, environment-designer, vfx-designer, ui-ux-designer, marketing, reference-images, reviewer, qa-lead
- also: critique-feedback, shape-silhouette, visual-hierarchy
- sources: R03-F08 (R03:198-208, 1034-1036); R12-F32 (R12:357-359)

### WL-29 Plan routes in player metrics: seconds at walk speed, ledges against jump height
- principle: Distances mean nothing to the player; time does. Measure every route in seconds at the real walk speed, keep walks between goals short (shorter still for short phone sessions), make the loop's return trips short or worth taking, and put a reward or a new view at each natural pause. Any ledge higher than the jump height is a wall.
- why: Long empty walks are dead time that ends phone sessions; a return trip walked many times per session multiplies every wasted second; a ledge that looks climbable but is not reads as a bug.
- apply: The level brief states the session shape (first visit, return visit, short phone session) and the movement metrics. Keep a route table per stage: distance, seconds at walk speed, what the player sees or does on the way. PROPOSAL default [inference, DS]: no walk over about 15 s without something to do or see; return trips (sell, restock, respawn to goal) get shortcuts, new views or things to do on the way. Ledges meant to be climbed stay under the jump height; ledges meant to block stay clearly above it.
- check: For each route, distance divided by walk speed stays under the brief's limit; a walk capture at the default speed shows something to do or see within each limit; every ledge on the main route is measured against the jump height in Studio.
- mistake: Judging routes from a top-down view in studs only; a decorative ledge just under jump height that lets players climb out of the map; a 40-second walk back to sell.
- examples:
  - DS: at 16 studs per second, 160 studs is 10 s (DS:level-design/SKILL.md:47).
- roblox_fit: Default WalkSpeed is 16 studs per second (knowledge/external/roblox-creator-docs/_api-reference/classes/StarterPlayer.yaml:358-364) and default JumpHeight is 7.2 studs (StarterPlayer.yaml:243-249); a game that changes them uses its own values from the game profile.
- roles: level-design, environment-designer, game-designer, progression-designer, feature-builder, reviewer, qa-lead
- also: game-design-fun, process-iteration
- sources: DS:level-design/SKILL.md:21-22, 47-49, 54, 67

### WL-30 Score a level review on ten fixed checks
- principle: A level review covers the same ten checks every time, scores each 0-2 and reports the total out of 20, so rounds compare and nothing is skipped: job, first view, route, landmarks, hierarchy, pacing, progress, boundaries, scale, story and theme.
- why: Free-form reviews drift to whatever the reviewer noticed first; a fixed, scored list shows whether a change helped and which check still fails.
- apply: Score (2 points when): (1) the layout serves the stated target experience and goal (GD-04); (2) the spawn view shows place, action and next goal (WL-07); (3) a new player finds the main route without text and no dead end lacks a reason (WL-09, WL-16); (4) each zone has a unique visible landmark and decision points are marked (WL-23, WL-12); (5) goals win the squint test and calm and busy areas alternate (VH-05); (6) targets ramp in size, value or challenge, a climax exists, and no walk exceeds the limit (GD-11, WL-29); (7) the player can see how close the goal is (GD-10); (8) every edge is believable, on theme and reads as impassable (WL-04, GD-07); (9) touch points fit a player (WL-21); (10) the things players expect from the theme are present and props tell how the place is used (SI-05, WL-22). Output: a ranked findings table (check, what is wrong, where, why it matters to the player, fix proposal, cost small, medium or large), a marked-up top-down image numbered to the table, a could-not-check list (CR-17) and PROPOSAL labels; the owner decides.
- check: The review shows all ten scores, the total and the capture behind each score; the re-review after fixes rescores all ten.
- mistake: Scoring only the checks that fail; a total without the captures behind it.
- examples:
  - DS: the level review checklist and its output format (DS:level-design/SKILL.md:58-78).
- roblox_fit: Top-down and game-camera captures through the Studio MCP, with route arrows and problem circles drawn on them [inference].
- roles: level-design, environment-designer, game-designer, reviewer, qa-lead
- also: critique-feedback, game-design-fun
- sources: DS:level-design/SKILL.md:58-78
