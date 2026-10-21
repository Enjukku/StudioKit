---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J008-T01, Environment_Designer_Research_2026.txt lines 1-255
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Environment paper part 1: evidence rules, 15 rules, 10 cases, guiding the player, scale, lighting, atmosphere (lines 1-255)

Paraphrased notes. The paper (EP) stays outside git. Every row cites `EP:<line>`. Nothing here is fact-checked yet: claims are the paper's, listed in section 9 for the fact-check pass. The paper's date is 2026-10-21. The paper built, rendered, heard and measured nothing (EP:15): every test it names is an instruction, not a result.

## 0. How to read

| Key | Meaning |
| --- | --- |
| EP:n | line n of `Environment_Designer_Research_2026.txt`. One paragraph or one table row = one line. Source register = EP:763-1469. |
| Tag | The paper's tag, kept as is. VERIFIED = an official spec or a measured result. EXPERIENCE = a studio's or person's account, in its own production context. OPINION = the paper's workflow, reading, example, template or pass rule. UNKNOWN = the paper found no value; it stays UNKNOWN and is never turned into a fact. |
| Src | Source ID from the register (resolved in section 11). E00 = the paper's own proposal, not an outside source. "acc" = living documentation read on 2026-10-21 (undated; access date is not a release date). |
| Kind | `rule` = lesson that holds for any game. `case-only` = fact about one shipped game; do not keep as a rule. `no-copy` = the paper says not to transfer it. `limit` = what the evidence cannot show. `example` = the paper made it up for illustration; not a rule. |
| Stage | Work stage the lesson serves: int intake, bp blueprint, blk blockout, bld build, lit lighting, atm atmosphere, amb ambience, drs dressing, rev review. |
| GD | The game designer decides or must be asked (route, cover, pacing, state, dimensions). |
| Row IDs | EC evidence contract, RU the 15 rules, K01-K10 the ten cases (suffix = row), KC comparison table, G guiding the player, SC scale, L lighting, A atmosphere, RC recipe matrix, FC claims to check, X contradiction or limit. |
| Part 2 | Rules 8, 9, 10 and the sound side of cases belong to the ambience part (EP:256+, another note). Here they are kept as one-line pointers. |

## 1. Evidence contract and governing idea (EP:5-15)

| ID | EP | Lesson | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- |
| EC0 | 5 | Roles: the game designer owns layout, routes, interactions and pacing. The environment designer turns that layout into a coherent place with the art director, modeler, animator, VFX designer and sound designer. The owner decides. | OPINION | E00 | all |
| EC1 | 7 | A finished place is a playable spatial composition, not a heap of nice objects. Its shapes, light, sound and motion must tell the player where they are, what matters and what may happen next. The method states those intentions, builds in stages that can be inspected, and asks for proof from the real Roblox scene, not from one polished render. | OPINION | E00 | all |
| EC2 | 11 | Tag meanings (see section 0). Each source has one short key quote and a direct URL, both in the register. | contract | E00 | - |
| EC3 | 11 | Living documentation carries an access date only. Do not treat it as a publication date. | contract | E00 | - |
| EC4 | 13 | Numbers do different jobs and are not interchangeable: an upload ceiling, an API default, a tutorial setting, a studio measurement and a project target. | OPINION | E00 | all |
| EC5 | 13 | The lighting table holds exact source examples. It does not claim the same settings give the same mood in every scene. | OPINION | E00 | lit, atm |
| EC6 | 13 | UNKNOWN: source ranges, mix gains and low-end-phone budgets. Each is paired with a method to choose and measure the project value. | UNKNOWN | E00 | lit, atm, amb, rev |
| EC7 | 13 | The agent may propose settings. It must never say an invented setting came from a studio or from Roblox. | OPINION | E00 | all |
| EC8 | 15 | Nothing was built, imported, rendered, heard, playtested or benchmarked for the paper. API procedures are plans, not tested code. | limit | E00 | all |
| EC9 | 15 | What a source shows or what a studio describes informs us about that source. It does not measure this studio's own game. | limit | E00 | all |
| EC10 | 15 | Limits of evidence types: a screenshot can show a composition defect but cannot prove a soundscape works or a route feels comfortable. Sound-position data can show missing sources but cannot prove mix quality. | limit | E00 | rev |

## 2. The fifteen rules (EP:19-47)

| Rule | EP | Rule in my words | Tag | Src | Stage | Detail rows |
| --- | --- | --- | --- | --- | --- | --- |
| RU01 | 19 | Keep the game designer's route and interaction intent. Any layout change is proposed in the open, never hidden inside an art pass. | OPINION | E00 | bp, blk, rev | K01-d, G09 |
| RU02 | 21 | At each decision point, settle first what the player must spot; only then place side decoration. | OPINION | E00 | bp | G01-G03 |
| RU03 | 23 | Camera, collision envelope and movement abilities are production inputs from day one, not late checks. | OPINION | E00 | int, bp | SC02, SC03 |
| RU04 | 25 | Keep one scale convention across Blender, Studio, gameplay and audio. Roblox's standard is 1 stud = 28 cm. | VERIFIED + OPINION | B02; E00 | int, bld | SC01-SC08 |
| RU05 | 27 | Make a readable blockout and one representative target scene before multiplying detail over the stage. | OPINION | E00 | blk | K01-a, K01-e |
| RU06 | 29 | Light is composition and a runtime dependency. Review the scene at the supported graphics tiers. | OPINION | E00 | lit | L03, L05 |
| RU07 | 31 | Tell apart atmosphere that suggests depth from fog that hides information the player needs. | OPINION | E00 | atm | A01, K02-d |
| RU08 | 33 | Each zone gets a causal sound-and-motion plan, not just a different background loop. | OPINION | E00 | amb | part 2 |
| RU09 | 35 | Transition behavior and source lifecycle belong in the ambience contract. Fades alone do not cover streaming and respawn. | OPINION | E00 | amb | part 2 |
| RU10 | 37 | Sound and VFX specialists make their own craft assets. The environment designer specifies location, purpose and interaction. | OPINION | E00 | amb | part 2 |
| RU11 | 39 | Use reusable kits without letting every view read as the same repeated stamp. | OPINION | E00 | bld, drs | K01-c, K03-c |
| RU12 | 41 | After import, check hierarchy, pivots and dimensions. A successful importer run is not visual or gameplay acceptance. | VERIFIED + OPINION | B05; E00 | bld, rev | SC05, SC08, FC38 |
| RU13 | 43 | When an AI tool reads or changes the scene, name the intended Studio instance and data model. | VERIFIED + OPINION | B03; E00 | all | FC39 |
| RU14 | 45 | Set the budget from the heaviest typical play scene, run on real target phones. An idle editor view and any fixed object-count rule of thumb do not count. | OPINION | E00 | rev | L03, L05, X14 |
| RU15 | 47 | Ship a review packet: reproducible cameras, a playable route, ambience evidence, performance captures. The owner approves last. | OPINION | E00 | rev | G05, G07 |

## 3. Section 1: ten cases from shipped games (EP:49-137)

Source type for every case is a first-party studio account or interview (register EP:765: EXPERIENCE, not independent proof of cause). Each case has: what the source reports (case-only unless it carries a universal lesson), the transfer lesson (OPINION), and what not to copy.

### K01 VALORANT Icebox: kitchen, mid, B-site (EP:51-55; source C01, Riot, 2020-11-16)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| K01-a | 53 | Production path: playtested greybox, then art blockout, then production, with playtests every week while modeling goes on. | rule | EXPERIENCE | C01 | blk, bld |
| K01-b | 53 | Artists keep the gameplay walls and edges as tested. Kitchen and mid got extra breathing room. Interior values must not go too dark. | rule (dark interiors) / case-only (kitchen, mid) | EXPERIENCE | C01 | bld, lit |
| K01-c | 53 | Most detail sits above player height so angles distract less (first-person tactical shooter). A yellow B-site container and ordinary place names help callouts. A non-playable glacier bunker adds story without touching playable geometry. Tiling textures and trim sheets cover large structures; specific props may get custom textures. | case-only (camera and map facts); rule (kits for large structures, custom textures for hero props) | EXPERIENCE | C01 | bld, drs |
| K01-d | 55 | Separate the route contract from its decoration. Collision edges, cover, routes and engagement intent belong to the game designer. The environment agent suggests art changes and submits any that affect gameplay for sign-off. | rule | OPINION | C01 (motive) | bp, rev |
| K01-e | 55 | Blender: keep a locked reference collection of the accepted blockout. Studio: keep blockout or validation proxies identifiable and apart from the final look. Approve by diffing shots taken before and after the art pass with an identical camera, agent pose and route state. | rule | OPINION | C01 (motive) | blk, rev |
| K01-f | 55 | Measure the real horizon band the targets occupy. Do not apply an abstract "detail goes high" rule. A phone third-person view may show a different height band from a tactical first-person view. | rule | OPINION | C01 (motive) | rev |
| K01-g | 55 | Do not copy Icebox's architecture. Do not infer a universal doorway width from its screenshots. | no-copy | OPINION | C01 | bp |

### K02 League Summoner's Rift: quiet canvas, crisp information edges (EP:57-65; sources C02 2014-11-11 reprint, C03 2016-05-13)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| K02-a | 59 | Style account: simple forms and values; paths that nudge movement without shouting; a map that supports the characters instead of competing with them; painted and graphic treatments that tie a varied roster together. Weak source: a named Riot developer's article kept as a reprint on MOBAFire, not the recovered official original; original date not recovered. | rule (support, not compete) | EXPERIENCE | C02 | bp, bld |
| K02-b | 61 | The map update had to keep the minimum hardware spec. Cleaner environments made fog-of-war artifacts easier to see than before. Designers wanted a sharply defined visibility edge, not a boundary blurred more and more. | rule (hard info edge) | EXPERIENCE | C03 | atm, rev |
| K02-c | 63 | Historic League figures: visibility data 128x128; raising it to 256x256 would have cost 4 times the CPU in that implementation; the visual reconstruction output 512x512 with the underlying data unchanged. Not Roblox terrain or texture advice. | case-only (numbers) | VERIFIED | C03 | - |
| K02-d | 65 | Keep tactical information and decorative atmosphere apart: soft haze is fine while a true interaction boundary stays explicit. Capture navigation, characters and VFX together; a lovely empty map is not enough proof. Put a simple background under repeated decisions and keep rich detail for low-conflict areas. | rule | OPINION | C02, C03 (motive) | atm, rev |
| K02-e | 65 | Do not carry League's camera-based hierarchy unchanged into a first-person cave or a building game. | no-copy | OPINION | C02 | bp |

### K03 Ghost of Tsushima: Akashima wetland and vegetation regions (EP:67-71; source C04, Sucker Punch, 2020-07-09)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| K03-a | 69 | The team blended references from the real island and mainland Japan rather than copy geography. Akashima's wetlands read as one place through moss, low mist, incense by the bell and frogs. Less foliage variety and less texture noise, with stronger colour and translucency, made regions easier to remember. Guiding Wind lines up foliage, cloth and particles with the route. Hand-placing and revising vegetation was impractical, so procedural tools did it. | rule (restrained variety plus strong colour; wind as a route aid; procedural scatter) / case-only (Akashima details) | EXPERIENCE | C04 | bld, atm, drs |
| K03-b | 69 | Scope reported: 3 regions and more than 40 biomes. This is production scope, not a goal for a small team. | limit | EXPERIENCE | C04 | - |
| K03-c | 71 | Give each biome a narrow ecological vocabulary plus a written exception list. A swamp is not "all green plants plus fog". Specify: dominant ground cover, drainage, evidence of moisture, typical sound sources, human traces, and how it joins neighbouring terrain. | rule | OPINION | C04 (motive) | bp, drs |
| K03-d | 71 | Make scattering repeatable and mask-driven so a path change regenerates its margins. Keep authored exclusion zones around routes, doors, landmarks and interaction surfaces. | rule | OPINION | C04 (motive) | bld, drs |
| K03-e | 71 | Sound and VFX should serve the same weather state, not each pick its own random atmosphere. | rule | OPINION | C04 (motive) | atm, amb |
| K03-f | 71 | Do not port the console-scale count of animated grass blades, or film-like particle density, to phones before measuring what it costs. | no-copy | OPINION | C04 | rev |

### K04 Zelda Tears of the Kingdom: sky and surface (EP:73-77; source C05, Nintendo, 2023-05-09)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| K04-a | 75 | Too many sky islands made the view messy. Small islands at true scale looked like scattered specks from the ground, so the team changed the presentation instead of accepting literal scale. Caves changed how familiar cliffs invited exploration. Seamless vertical travel forced the sound staff to choose where the surface and sky audio contexts switch. | rule (literal scale can fail to read) / case-only (islands) | EXPERIENCE | C05 | bp, bld, amb |
| K04-b | 77 | Design a far landmark twice: as an object you can enter, and as a shape seen from its intended approach. Stylized massing, spacing or framing may serve the second need. Never change traversal dimensions without saying so. | rule | OPINION | C05 (motive) | bp, rev |
| K04-c | 77 | Keep a camera matrix: ground approaches, elevated routes, landing zones, reverse views. Log landmark screen occupancy and occlusion as diagnostics only; this source gives no minimum pixel size. | rule + limit | OPINION | C05 (motive) | rev |
| K04-d | 77 | A cave entrance should say "possible route" in line with the game's traversal rules, not just decorate a cliff. Treat a vertical biome change as one joint hand-off of look, movement and ambience. | rule | OPINION | C05 (motive) | bp, bld, amb |
| K04-e | 77 | Do not infer Nintendo's island sizes or transition heights from this interview. | no-copy | OPINION | C05 | - |

### K05 Overwatch Esperanca: historic centre and tech seawall (EP:79-83; source C06, Blizzard, 2022-10-18)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| K05-a | 81 | Portuguese architecture meets a futuristic seawall visible from both spawns. The map is split into three themes: classical architecture, residential streets and the historic centre. The central tower marks the objective's start. Pavement leads toward the tower. Sound was recorded in Portugal, so place identity comes from both what you see and what you hear. | case-only | EXPERIENCE | C06 | - |
| K05-b | 83 | Treat global orientation, district identity and local callout as three separate jobs. A horizon-scale landmark can identify the world without replacing a close route cue. | rule | OPINION | C06 (motive) | bp |
| K05-c | 83 | Give each district a material and architecture family, and keep gameplay surfaces readable across the variations. Specific places come from how they are used (workshops, shade, drainage, transit, commerce, maintenance) more than from a loose national mood board. | rule | OPINION | C06 (motive) | bld, drs |
| K05-d | 83 | Have qualified reviewers vet cultural references; looking recognizable does not excuse a stereotype. | rule | OPINION | C06 (motive) | rev |
| K05-e | 83 | Do not assume three districts is optimal. Do not assume decorative pavement guarantees navigation. | no-copy | OPINION | C06 | - |

### K06 The Last of Us: Boston quarantine zone vs Bill's Town (EP:85-89; source C07, Naughty Dog, 2023-02-07)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| K06-a | 87 | Boston quarantine zone: hard angular construction, little nature, blue overcast light, all to press the player down. A remade market kept scarcity instead of attractive abundance. Bill's Town sets natural beauty against traps and danger. Developers describe checking the original intent when adding detail. | rule (check intent when adding detail; scarcity can be the point) / case-only (these places) | EXPERIENCE | C07 | lit, drs |
| K06-b | 89 | Set dressing is evidence, not a decoration quota. Before placing an object, write down who used it, why it is still there, what state the place is in, and whether it falsely promises loot or interaction. | rule | OPINION | C07 (motive) | drs |
| K06-c | 89 | Use narrative density on purpose: one empty ration shelf can say more than ten generic containers (the paper's example, not a rule). Contrasts should hold at route scale, not only as two concept images. Capture the oppressive-to-open change with the player and UI visible. | rule; the "ten" is an example | OPINION | C07 (motive) | drs, rev |
| K06-d | 89 | "More detailed" and "more true to the world" are different. Do not import this game's horror mood or desaturated palette into a cheerful tycoon just because the craft is strong. | rule + no-copy | OPINION | C07 | drs |

### K07 Fortnite Chapter 4: readable interiors in a changing world (EP:91-97; source C08, Epic, 2023-01-26)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| K07-a | 93 | Time of day, building, destruction and doors made responsive lighting matter. More accurate global illumination made dark interiors and exposure swings that needed artistic control. Epic raised indirect-light strength, adjusted colour treatment and let skylight leak in, rather than add costly shadowed lights everywhere. | rule (state changes break lighting; fix with cheap global controls before many local lights) | EXPERIENCE | C08 | lit |
| K07-b | 95 | Numbers: indirect-light intensity 2.0; a 4 ms budget for global illumination plus reflections inside a 60 fps console target. They belong to Fortnite's Lumen and its hardware. They are not Roblox Lighting properties and not a mobile allowance. | case-only (numbers) | VERIFIED | C08 | - |
| K07-c | 97 | Accept lighting across gameplay states, not at one ideal sun angle. List the outdoor-to-indoor thresholds, doors, destruction and weather states that may change readability. Demand a capture of each, and use the platform's real profiling tools. Keep a route readable even where physical light would hide it. | rule | OPINION | C08 (motive) | lit, rev |
| K07-d | 97 | Do not copy Lumen parameter names or the console budget into Studio. Carry over the problem statement and the test method, not the engine recipe. | no-copy | OPINION | C08 | lit |

### K08 Journey: desert and distant mountain (EP:99-103; source C09, Santiago quoting Chen, 2010-06-29)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| K08-a | 101 | Pre-release creator statement: a vast unfamiliar world with one far mountain as an invitation; awe and a feeling of little power raise the value of other travellers. It shows design intent only. It is not a measured player response and not a full account of the shipped game. | limit | EXPERIENCE | C09 | - |
| K08-b | 103 | A destination can be felt before the path to it is clear. Pair a long-term landmark with shorter local cues. Reveal enough to keep curiosity going without showing every turn. Keep negative space so the focal object has a clear relation to what is around it. | rule | OPINION | C09 (motive) | bp, bld |
| K08-c | 103 | A reference image sets the goal for a single view; it says nothing about the other approaches. Check reverse routes and other camera heights. Never present an unreachable mountain as explorable if the game has set "visible means reachable". | rule | OPINION | C09 (motive) | rev |
| K08-d | 103 | Do not copy the emptiness without the movement, pacing and emotional premise that make crossing it worth it. | no-copy | OPINION | C09 | bp |

### K09 Half-Life: Alyx, City 17 and layered map production (EP:105-109; source C10, Valve AMA, 2020-01-22)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| K09-a | 107 | The Citadel core went in first, with construction built around it. The unfinished silhouette sets a time before Half-Life 2. A level designer says map files from level, environment and sound designers are combined through a layer-like system so more disciplines can add to one map. The team says it used Steam Audio for HRTF, DSP and occlusion. | case-only (facts) / rule (layered ownership) | EXPERIENCE | C10 | bp, bld, amb |
| K09-b | 109 | A landmark's building state can explain history with no sign: show load-bearing structure, unfinished joins, access and material staging that fit the story state. | rule | OPINION | C10 (motive) | bld, drs |
| K09-c | 109 | Give each agent explicit ownership and share one spatial reference. Merged work needs dependency checks so moving environment geometry cannot strand sound emitters or break occlusion assumptions. Use separate editable groups, not one baked monolithic export. | rule | OPINION | C10 (motive) | bld, rev |
| K09-d | 109 | The paper does not claim it watched the commentary, measured corridors or reproduced VR interaction scale. Do not carry VR reach distances or horror intensity to mobile. | no-copy + limit | OPINION | C10 | - |

### K10 Deadlock: occult city districts and Sunken Plaza (EP:111-115; source C11, Valve, 2026-09-29)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| K10-a | 113 | Valve's published feature list names three lanes (Broadway, Greenwich, York), districts such as Theater, Chinatown, Haunted Lot and Plaza, a Sunken Plaza that dulls outside sound and saps stamina, and themed institutions (an occult university, Wall Street warlocks). Descriptions only; no navigation was tested. | case-only | VERIFIED | C11 | - |
| K10-b | 115 | A single world premise can be expressed by city functions people recognize, by district identity and by local rules of behavior. A sunken area can set itself apart through form, how sound behaves there and its gameplay state, not colour alone. For an original Roblox world, make up your own cause-and-effect premise, then check that terrain, architecture, props, VFX and ambient zones all show matching consequences. | rule | OPINION | C11 (motive) | bp, bld, amb |
| K10-c | 115 | Do not pass off a guessed Deadlock palette, shader graph, blockout method, district size or art bible as something Valve said. This evidence supports a narrower claim than the long interviews above. Published visual identity is no licence to copy assets or names. | no-copy + limit | OPINION | C11 | - |

### KC Case evidence limits and comparison table (EP:117-131)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| KC0 | 119 | The inspected sources do not establish: phone-safe total triangle counts, standard Roblox room sizes, universal scene-building times, a needed prop count per square metre, sound radii, light brightness recipes, or validated screenshot-recognition thresholds. Engine values stay tied to their hardware, scene and implementation. Production time is unknown for each case unless published; a large studio's scope is no small-team estimate. | limit | OPINION | E00 | all |

| ID | EP | Game / studio | Learn | Do not copy | Tag, src |
| --- | --- | --- | --- | --- | --- |
| KC1 | 122 | Icebox / Riot | Keep tested geometry; keep callout cues distinct from decorative backdrop | Treating first-person detail placement as the rule for every camera | C01 EXPERIENCE; transfer OPINION |
| KC2 | 123 | Summoner's Rift / Riot | Quiet tactical canvas; exact information boundaries | The historic visibility grid as a Roblox map budget | C02-C03 EXPERIENCE/VERIFIED; transfer OPINION |
| KC3 | 124 | Akashima, Tsushima / Sucker Punch | Narrow biome vocabulary; wind, plants and ambience joined | Console vegetation density | C04 EXPERIENCE; transfer OPINION |
| KC4 | 125 | TOTK sky and surface / Nintendo | Judge scale from both the destination and the approach | Literal realism that costs landmark readability | C05 EXPERIENCE; transfer OPINION |
| KC5 | 126 | Esperanca / Blizzard | Global landmark, district language, local objective, culture | District count as a set optimum | C06 EXPERIENCE; transfer OPINION |
| KC6 | 127 | Boston QZ, Bill's Town / Naughty Dog | Set dressing that keeps the story state | Abundance added only as polish | C07 EXPERIENCE; transfer OPINION |
| KC7 | 128 | Fortnite Ch. 4 / Epic | Check lighting in every changing state | Treating Lumen settings or console costs as Studio goals | C08 EXPERIENCE/VERIFIED; transfer OPINION |
| KC8 | 129 | Journey desert / thatgamecompany | Negative space and a meaningful far destination | Vast emptiness with no movement or pacing to support it | C09 EXPERIENCE; transfer OPINION |
| KC9 | 130 | Alyx City 17 / Valve | Landmark build state; clear ownership across crafts | VR reach and camera assumptions | C10 EXPERIENCE; transfer OPINION |
| KC10 | 131 | Deadlock city / Valve | One premise across districts, behaviors and ambience | A guessed internal art bible, or desktop-level density | C11 VERIFIED; transfer OPINION |

Section 1 evidence summary (EP:133-137): KS1 (136) learn the craft choice and ignore the production size: 10 chosen cases; tag EXPERIENCE, transfers OPINION; sources C01-C11 and the dated register. KS2 (137) published numbers keep their engine context: the Fortnite 4 ms figure is no Roblox budget; tag VERIFIED historic report; source C08, 2023-01-26.

## 4. Section 2: guiding the player with the environment (EP:139-177)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| G01 | 143 | The route is a contract. Start from a route graph the game designer supplies or approves. For each node write: entry direction, intended next choice, optional exploring, encounter or interaction, required sightline, traversal ability, and the cost of a wrong choice. Then tie spatial evidence to that intent, picked from: visible landmark, framed opening, light contrast, change of material, distinct sound source, or a blend of these. The graph is a planning tool, not a claim that all good games have the same number of routes or landmarks. GD | rule | OPINION | E00 | int, bp |
| G02 | 145 | Split the far destination landmark from the local navigation cue. A far tower orients; a near doorway gives the next move. A tower visible through every wall may stop reading as a usable route. A doorway that looks like background facade can be misread even in a correct layout. Review how the two relate, not how nice each looks alone. | rule | OPINION | E00 | bp, rev |
| G03 | 147 | For every decision point write one cue sentence naming the approach, the intended continuation, and why it reads. Then test whether the real camera backs the sentence. In a review report, never write "clear" without naming the object, the camera and the task. (The sentence about a broken aqueduct and water sound is the paper's illustration.) | rule; aqueduct is an example | OPINION | E00 | bp, rev |
| G04 | 149 | Use leading lines only when their end supports the intended choice. Lamps leading to an exit help; an equally strong row leading to a dead wall gives a competing order. A bright cave mouth draws the eye and can hide what is beyond; whether that is right depends on the game designer's pacing and risk intent. Tell deliberate mystery from accidental ambiguity. GD | rule | OPINION | E00 | bp, lit |
| G05 | 153 | Capture three views per decision: the approach (is the cue found in time), the decision point (is the choice clear), the view after committing (is the next goal still readable). Add a return trip if backtracking is allowed. These are proposed review states, not an industry-fixed count. | rule | OPINION | E00 | rev |
| G06 | 155 | Roblox Camera API gives view transforms, field-of-view controls, viewport size and world-to-viewport projection. WorldRoot gives ray and shape queries. Together they can drive a tool that projects landmark bounds and probes sightlines. A point projected on screen does not prove the landmark is unblocked, recognizable or understood. One ray that hits the landmark does not prove enough silhouette is visible. | rule (+ engine claims FC36-FC37) | VERIFIED + OPINION | B09, B10; E00 | rev |
| G07 | 157 | For an AI review log: the visible part of the landmark, the screen region it fills, the competing shapes near it, and the state of UI and effects overlays. Compare with the approved target scene. Do not invent one screen fraction every landmark must fill. An objective may be quiet while exploring and loud in a timed escape; thresholds must keep that difference. GD | rule | OPINION | E00 | rev |
| G08 | 159 | Sound guidance needs a real source or an openly authored non-physical convention. A waterfall heard before it is seen implies direction and a terrain change. A non-positional stereo bed cannot be assumed to point at it: label that layer atmosphere, not navigation. Keep essential route information available in another channel for muted play. | rule | OPINION | E00 | amb, rev |
| G09 | 163 | When players miss the route, do not add arrows first. Find the cause: cue off-camera, hidden, too close to background shapes, contradicted by another cue, shown too late, or read as inaccessible. Fix at the least disruptive layer: a different framing opening, less competing detail, a landmark moved inside the approved layout, a clearer interaction shape, or a synced audio cue. If the fix would alter route length, cover or encounter timing, return it to the game designer. GD | rule | OPINION | E00 | rev |
| G10 | 167 | Totten presents prospect-refuge and survival-minded architectural thinking as useful influences on level design. | case-only | EXPERIENCE | C12 (2010-06-11) | bp |
| G11 | 169 | A practitioner text (undated; read 2026-10-21) challenges moving prospect-refuge into games. Mechanics and changing game state may matter more than the shape of an enclosure. It offers plainer terms: sightline, vista, cover, enclosure. Its Elden Ring example (author analysis) has an arena turn from threatening to safe after the fight in the same room. | case-only | EXPERIENCE | C13 | bp |
| G12 | 171 | Treat architectural psychology as a hypothesis, not a universal player model. Write "sheltered from these sightlines" apart from "safe under these game rules". One cave may feel calm, fought over or hostile, depending on spawns, resources, UI, sound and progression. Get the state from the game designer before the environment agent tries to convey it. Keeps Totten's spatial vocabulary without claiming biological certainty. GD | rule | OPINION | C12, C13 | bp, rev |

Section 2 evidence summary (EP:175-177): GS1 (176) retain approved geometry and gameplay edges; no universal cue count exists; tag EXPERIENCE with OPINION transfer; sources C01 (2020-11-16) and E00 (2026-10-21). GS2 (177) enclosure is not safety, so the game state must be stated; tag EXPERIENCE (a disagreement between sources); C12 2010-06-11 versus C13 accessed 2026-10-21.

## 5. Section 3: scale and proportion (EP:179-207)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| SC01 | 183 | In Roblox's standard unit table, 1 stud equals 28 cm. The same page says the engine converts no units itself and lets a project adopt another reading if it stays consistent. Use the standard unless the approved movement and asset pipeline truly needs another. It is a conversion convention, not a standard avatar height, and not an order to build photoreal proportions. | rule (+ FC34) | VERIFIED | B02 (acc) | int, bld |
| SC02 | 185 | The scale sheet lists: the true avatar envelope; camera mode and offsets; which avatar scaling is supported; movement speed plus abilities; how far interaction reaches; and any held or equipped item that alters clearance. Take them from the game designer and the runtime config. Do not assume the label R15 gives the whole player shape. Do not assume a door made for standing works during a jump, climb, mount or tool swing. GD | rule | OPINION | E00 | int, bp |
| SC03 | 187 | Three clearances, each with its own fix: visual (do they look like they fit), collision (does the real collision shape pass), camera (does the supported camera stay usable on the way through). An ornate arch can look wide while a plain box blocks it. An opening can pass collision while a third-person camera keeps clipping the lintel. | rule | OPINION | E00 | blk, rev |
| SC04 | 189 | Doorway: state the needed motion, the collision envelope that motion uses, and the design margin; derive the opening from them. Do not state one fixed "Roblox door width" unless the avatar, motion, camera and collision assumptions behind it are named. Path: add passing traffic, combat spacing, side obstacles, and whether it should feel tight. Ceiling: add jumping and overhead gear, not only walking. GD | rule | OPINION | E00 | bp, blk |
| SC05 | 193 | In both Blender and Studio, keep a calibration object and a player stand-in of known size. After import, compare one known dimension, the bounds of the main building and the orientation of the transform. Model API GetBoundingBox and GetExtentsSize measure the current model form; a name proves nothing. A box that includes a tall decorative antenna is a poor doorway measure, so pick the meaningful measuring target. | rule (+ FC35) | VERIFIED + OPINION | B06; E00 | bld, rev |
| SC06 | 195 | Exaggerated scale is allowed for shelter, grandeur or threat if intended. Record which relations may bend (silhouette proportion, roof height, rock size, door framing, decor thickness, distance squeeze). Keep gameplay openings and interaction spots tied to the route contract. A huge far castle does not force every inner room to share the exaggeration. | rule | OPINION | E00 | bp, bld |
| SC07 | 197 | Scale review: same spot with the playable character, a familiar prop and the real game camera. Then a second view without the familiar reference to see whether the place's own proportions carry the intended scale. A proposed check, not a set count. A place may be vague in absolute size and still navigate reliably. | rule | OPINION | E00 | rev |
| SC08 | 201 | Scene scale record, fields: unit convention; Blender scene unit setting; asset size before export; export scale and axis choices; importer settings; the Studio size that results; pivot convention; avatar and camera setup; traversal actions tested; known exceptions. Keep source-file scale separate from object transforms and export conversions. On a mismatch change one stage and re-measure; do not stack compensating factors until it looks about right. | rule | OPINION | E00 | bld, rev |

Section 3 evidence summary (EP:205-207): SS1 (206) declare and keep a unit convention: 1 stud = 28 cm standard; VERIFIED; B02 accessed 2026-10-21. SS2 (207) measure avatar, collision and camera clearance separately: door and path sizes are project-specific; OPINION; E00 2026-10-21; API B06, B09.

## 6. Section 4: lighting for style and readability (EP:209-227)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| L01 | 211 | Unified Lighting is fully released (2025-07-23). Its two controls are LightingStyle and PrioritizeLightingQuality; they replace the old Technology setting. Migration map: Future becomes Realistic + prioritized; ShadowMap becomes Soft + prioritized; Voxel becomes Soft + not prioritized. Do not teach choosing "Future" as the current workflow. | rule | VERIFIED | P02 (2025-07-23) | lit |
| L02 | 213 | LightingStyle: Realistic asks for advanced lighting and shadows; Soft asks for the flatter retro look. | rule | VERIFIED | P01 (acc) | lit |
| L03 | 213 | PrioritizeLightingQuality picks what degrades first. On keeps nearby shading quality longer and gives up distance; off favors distance. | rule | VERIFIED | P01 (acc) | lit |
| L04 | 213 | ClockTime and TimeOfDay are linked. ClockTime uses hours 0-24. GeographicLatitude moves the sun/moon position. ShadowSoftness runs 0-1 and applies to Realistic. | rule (numbers: FC03-FC05) | VERIFIED | P01 (acc) | lit |
| L05 | 213 | These controls state rendering intent. They do not promise every client draws the same shadow path. The 0-1 softness range is not a measured GPU budget. | limit | VERIFIED | P01 (acc) | lit, rev |
| L06 | 215 | Quality level alters draw distance, shading, how much geometry shows, textures, particle caps, trails and post effects. Exact behavior depends on platform and device; do not depend on it. | limit | VERIFIED | P03 (acc) | lit, rev |
| L07 | 215 | Derived rule: routes, hazards, exits and silhouettes must stay readable when optional visual support goes away. Light should reinforce a route; it must not make an otherwise invisible mandatory route exist. | rule | OPINION (from P03) | P03; E00 | lit, rev |
| L08 | 217 | Light objects: PointLight radiates in all directions; SpotLight sends a directional cone; SurfaceLight shines across one face of a part. Shared properties: Color, Brightness, Shadows. Range is in studs; raising Brightness does not raise Range. SpotLight Angle reaches 180 degrees. Studio's Show Light Guides shows direction and influence bounds. | rule (claims FC10-FC12) | VERIFIED | P32 (acc) | lit |
| L09 | 217 | Match the light's shape to its visible fixture. Write each light's position, orientation, range and shadow state into the scene manifest. | rule | OPINION | E00 | lit, rev |
| L10 | 219 | Pick the style from the approved art target. Compare representative phone captures with PrioritizeLightingQuality on and off. Soft is not automatically the phone setting, and Realistic does not always give the better play experience. Store these together: property values, device, client build, quality mode, camera transform and timing capture. Sign off the layout of values and silhouettes first, then spend on costly shadow detail. | rule | OPINION | E00 | lit, rev |
| L11 | 221 | Indoor tutorial: wrap enclosed spaces in Parts at least 1 stud thick to cut light leaks; its sample uses 2.5-stud-thick blockers around mesh walls and ceiling. It is a documented light-leak workaround; it does not set how thick visible walls must be in any style. | rule (conditional) | VERIFIED | P06 (acc) | lit, bld |
| L12 | 221 | Audit such blockers for stray collisions and for windows they close off. They must not quietly shrink or alter the traversable sizes the game designer set. GD | rule | OPINION | E00 | lit, rev |
| L13 | 227 | No universal light-count limit is established. Sign off on the intended look and on how readable the scene stays when degraded. | limit | OPINION | P01/P03 synthesis | lit, rev |

Section 4 evidence summary (EP:223-227): LS1 (224) configure current lighting, not legacy Technology: two current controls; VERIFIED; P02 2025-07-23. LS2 (225) softness range is no measured GPU budget: 0-1; VERIFIED; P01 acc. LS3 (226) enclosed-space blocker guidance is conditional: at least 1 stud; sample 2.5 studs; VERIFIED; P06 acc. LS4 (227) approve both intent and degraded readability: no universal light-count limit; OPINION; P01/P03 synthesis.

## 7. Section 5: atmosphere and scoped lighting recipes (EP:229-254)

| ID | EP | Lesson | Kind | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | 231 | Atmosphere Density hides objects and terrain; Offset changes how they blend with the sky. A bad balance can show sky through geometry or expose distant LoD changes. Haze and Color shape far mood. | rule | VERIFIED | P07, P08 (acc) | atm |
| A02 | 231 | Dependencies: Glare needs Haze above 0. A visible Decay needs both Haze and Glare above 0. Lighting's legacy fog properties are hidden when an Atmosphere exists. | rule (claims FC14-FC15) | VERIFIED | P07, P08 (acc) | atm |
| A03 | 231 | The Atmosphere article's slider examples are separate property demonstrations, not one calibrated preset. Do not combine them into a preset. | limit | VERIFIED | P07 (acc) | atm |
| A04 | 233 | Clouds draw only when parented under Terrain. Cover runs 0-1. Density affects transparency. Lighting and Atmosphere also change the perceived cloud colour. Dynamic clouds can follow global wind. | rule (claims FC16-FC17) | VERIFIED | P09 (acc) | atm |
| A05 | 233 | Treat skybox, atmosphere and clouds as one palette and one horizon composition. Do not infer that cloud cover turns on rain, puddles, wind audio or a weather gameplay state. | rule | OPINION | E00 | atm |
| A06 | 235 | Post effects offered: Bloom, Blur, ColorCorrection, DepthOfField, SunRays, ColorGrading. Effects parented to Lighting apply to everyone; effects parented to a Camera can be per player. None affect GuiObjects. | rule (claims FC18-FC19) | VERIFIED | P10, P11 (acc) | atm |
| A07 | 235 | ColorGradingEffect TonemapperPreset: Default or Retro. Retro copies the lower-contrast, lower-saturation look from before 2019. The docs suggest trying Retro with light brightness at most 1.0 for that recreation goal only; it is not a general brightness ceiling. | rule (conditional) | VERIFIED | P10, P11 (acc) | atm, lit |
| A08 | 235 | Post effects can change or vanish at low quality. | limit | VERIFIED | P10, P11 (acc); P03 | atm, rev |
| A09 | 239 | Recipe rules: the matrix below holds VERIFIED sample values, not approved project presets. RGB triples are 0-255 values from official examples. A dash = the paper did not extract that value (unspecified, not zero). A row copies only the stated subset; geometry, skybox, materials, other properties and device decide the result. Before adoption, re-derive each value against the art bible and with real phone captures. | limit | VERIFIED values; OPINION re-check | P04-P06; E00 | lit, atm |
| A10 | 248 | Traps: P05 shows Density 0.391 in a comparison picture but instructs 0.272; the paper uses the instruction. P06 sets ClockTime 15.6 while its prose says about 3:45 pm; keep the literal property value, not the prose. Neither sample states low-end-phone milliseconds. | limit | VERIFIED | P05, P06 (acc) | lit, atm |
| A11 | 248 | In the scene manifest keep `source_recipe` apart from `project_approved_settings`. | rule | OPINION | E00 | lit, atm, rev |
| A12 | 246 | Exposed mountain, swamp, cave, storm: values UNKNOWN until geometry, navigation visibility and art target exist. Do not invent a standard fog density per biome. No universally validated biome values were found. Withhold numeric approval; P03 and P07 explain why it depends. | limit | UNKNOWN (values); OPINION (withhold) | P03, P07 | atm, rev |

### RC Recipe matrix (EP:242-245). Sample values from official tutorials, not presets

A dash means not extracted by the paper (unspecified, not zero). Colours are RGB 0-255.

| Property | RC1 Cool ocean morning (Island Jump - Final; EP:242; P04) | RC2 Warm evening campfire (Lighting Outdoors - Complete; EP:243; P05) | RC3 Warm hazy cabin (Lighting Indoors - Complete; EP:244; P06) |
| --- | --- | --- | --- |
| LightingStyle | Realistic | Realistic | Realistic |
| ClockTime | 9 | 17 | 15.6 |
| GeographicLatitude | 78 | - | 323, optional |
| Ambient | (16,16,16) | (156,136,176) | (83,70,57) |
| OutdoorAmbient | (134,158,190) | (156,136,176) | - |
| ColorShift_Top | (196,222,255) | - | - |
| ShadowSoftness | 0 | - | - |
| EnvironmentDiffuseScale | - | 1 | - |
| EnvironmentSpecularScale | - | 1 | - |
| ExposureCompensation | - | - | 0.5 |
| PointLight | - | Color (255,179,73); Brightness 2; Range 48 studs; Shadows enabled | - |
| Atmosphere Density | 0.375 | 0.272 (instruction; the picture shows 0.391) | 0.5 |
| Atmosphere Offset | 0.17 | - | - |
| Atmosphere Haze | - | 1 | - |
| Atmosphere Color | - | (85,78,54) | - |
| SunRays | - | - | Spread 0.266; Intensity 0.023 |
| ColorCorrection | - | - | Contrast 0.05; Saturation 0.1 |
| Post effects, other | not specified | not specified | listed above only |
| Source note | P04, acc 2026-10-21; sample settings | P05, acc 2026-10-21; sample settings, not a phone benchmark | P06, acc 2026-10-21; sample settings |

| ID | EP | Retro and biome rows | Tag | Src |
| --- | --- | --- | --- | --- |
| RC4 | 245 | Retro presentation: Soft is the style option that matches, yet no retro art direction is forced to use it. No universal values exist. ColorGrading TonemapperPreset Retro. Documented experiment: all light Brightness at most 1.0. A style experiment, not a complete scene preset. | VERIFIED | P01, P10 (acc) |
| RC5 | 246 | Exposed mountain, swamp, cave, storm: UNKNOWN on Lighting, Atmosphere and post effects. See A12. | UNKNOWN; OPINION | P03, P07 |

Section 5 evidence summary (EP:250-254): AS1 (251) do not combine unrelated Atmosphere slider demos into a preset: Glare needs Haze above 0; VERIFIED; P07 acc. AS2 (252) clouds must be in the right hierarchy: Cover 0-1; VERIFIED; P09 acc. AS3 (253) keep art direction if post effects disappear: no fixed-quality promise across devices; VERIFIED + proposed acceptance rule; P03/P11 acc. AS4 (254) adopt example values only after project review: no universal biome preset; OPINION; scope of P04-P06.

## 8. Lesson map by work stage (for the skill author)

| Stage | Rows to read |
| --- | --- |
| int intake | EC0, RU03, RU04, SC01, SC02, G01 |
| bp blueprint | RU01, RU02, K01-d, K03-c, K04-b, K05-b, K08-b, K10-b, G01-G04, G10-G12, SC04, SC06 |
| blk blockout | RU05, K01-a, K01-e, SC03, SC04 |
| bld build | RU11, RU12, K01-c, K03-d, K05-c, K09-b, K09-c, SC05, SC08, L11 |
| lit lighting | RU06, K07-a, K07-c, L01-L13, RC1-RC5, A10, A11 |
| atm atmosphere | RU07, K02-b, K02-d, K03-e, A01-A12 |
| amb ambience | RU08-RU10 (part 2), K04-a, K04-d, K09-a, K10-b, G08 |
| drs dressing | K06-b, K06-c, K06-d, K03-c, K05-c, RU11 |
| rev review | RU14, RU15, K01-f, K04-c, K07-c, K08-c, G03, G05-G07, G09, SC05, SC07, SC08, L10, L13, A12 |

## 9. Claims to fact-check

Every Roblox engine claim, tool behavior, number and unit in EP:1-255. Kind: roblox = Roblox engine, docs or Studio/MCP behavior; industry = another game or engine (not a Roblox claim; check only the source fact); example = the paper's own illustration. "Hist." = historic other-engine number, never a Roblox budget. Check against the Roblox docs mirror first (`knowledge/external/roblox-creator-docs/`).

### 9.1 Lighting, atmosphere, post effects, terrain (clouds)

| ID | Claim or value | EP | Src | Kind | Tag |
| --- | --- | --- | --- | --- | --- |
| FC01 | Unified Lighting fully released, dated 2025-07-23; LightingStyle and PrioritizeLightingQuality replace the old Technology setting | 211 | P02 | roblox | VERIFIED |
| FC02 | Migration: Future -> Realistic + prioritized; ShadowMap -> Soft + prioritized; Voxel -> Soft + not prioritized | 211 | P02 | roblox | VERIFIED |
| FC03 | Realistic = advanced lighting and shadows; Soft = flatter retro look; PrioritizeLightingQuality on keeps near shading longer at distance's cost, off favors distance | 213 | P01 | roblox | VERIFIED |
| FC04 | ClockTime and TimeOfDay linked; ClockTime hours 0-24 | 213 | P01 | roblox | VERIFIED |
| FC05 | GeographicLatitude moves sun/moon; ShadowSoftness range 0-1 and applies to Realistic only | 213 | P01 | roblox | VERIFIED |
| FC06 | Graphics quality changes distance, shading, geometry, textures, particle limits, trails, post effects; some post effects fully off at low quality (QualityLevel) | 215, 235 | P03 | roblox | VERIFIED |
| FC07 | Controls express intent; no guarantee of one shadow path on every client | 213 | P01 | roblox | VERIFIED |
| FC08 | Indoor tutorial: blockers at least 1 stud thick reduce light leaks | 221, 226 | P06 | roblox | VERIFIED |
| FC09 | Indoor sample uses 2.5-stud-thick blockers around mesh walls/ceiling | 221, 226 | P06 | roblox | VERIFIED |
| FC10 | PointLight omnidirectional, SpotLight directional cone, SurfaceLight emits across a part face; shared Color, Brightness, Shadows | 217 | P32 | roblox | VERIFIED |
| FC11 | Light Range is in studs; raising Brightness does not raise Range | 217 | P32 | roblox | VERIFIED |
| FC12 | SpotLight Angle goes up to 180 degrees; Studio "Show Light Guides" shows direction and influence bounds | 217 | P32 | roblox | VERIFIED |
| FC13 | Atmosphere Density hides objects/terrain; Offset changes blend with sky; bad balance gives sky-through-geometry or visible LoD transitions; Haze and Color shape distant mood | 231 | P07, P08 | roblox | VERIFIED |
| FC14 | Glare needs Haze > 0; visible Decay needs Haze > 0 and Glare > 0 | 231, 251 | P07, P08 | roblox | VERIFIED |
| FC15 | Lighting's legacy fog properties are hidden when an Atmosphere object exists | 231 | P08 | roblox | VERIFIED |
| FC16 | Clouds render only when parented under Terrain; Cover range 0-1; Density affects transparency | 233, 252 | P09 | roblox | VERIFIED |
| FC17 | Lighting/Atmosphere influence perceived cloud colour; dynamic clouds can follow global wind (paper cites P09; the register also holds P12 Global wind, not cited here) | 233 | P09 | roblox | VERIFIED |
| FC18 | Post effects offered: Bloom, Blur, ColorCorrection, DepthOfField, SunRays, ColorGrading | 235 | P10, P11 | roblox | VERIFIED |
| FC19 | Lighting-parented post effects are global; Camera-parented can be per player; none affect GuiObjects | 235 | P10, P11 | roblox | VERIFIED |
| FC20 | ColorGradingEffect TonemapperPreset: Default vs Retro; Retro imitates the lower-contrast, lower-saturation pre-2019 look | 235 | P10, P11 | roblox | VERIFIED |
| FC21 | Docs suggest Retro with all light Brightness at most 1.0 (value 1.0; style experiment, not a ceiling) | 235, 245 | P01, P10 | roblox | VERIFIED |
| FC22 | RC1 values: Atmosphere Density 0.375 and Offset 0.17; ShadowSoftness 0; ClockTime 9; GeographicLatitude 78; ColorShift_Top (196,222,255); OutdoorAmbient (134,158,190); Ambient (16,16,16). Also check these against the tutorial's current text | 242 | P04 | roblox | VERIFIED (sample) |
| FC23 | RC2 values: ClockTime 17; Ambient and OutdoorAmbient (156,136,176); EnvironmentDiffuseScale 1; EnvironmentSpecularScale 1; PointLight with Color (255,179,73), Brightness 2, Range 48 studs and Shadows enabled; Atmosphere Density 0.272, Haze 1, Color (85,78,54) | 243 | P05 | roblox | VERIFIED (sample) |
| FC24 | P05 picture shows Density 0.391; instruction says 0.272 (which is current?) | 248 | P05 | roblox | VERIFIED (trap) |
| FC25 | RC3 values: ClockTime 15.6; GeographicLatitude 323 (optional); Ambient (83,70,57); ExposureCompensation 0.5; ColorCorrection Contrast 0.05 and Saturation 0.1; SunRays Spread 0.266 and Intensity 0.023; Atmosphere Density 0.5 | 244 | P06 | roblox | VERIFIED (sample) |
| FC26 | P06 prose says about 3:45 pm while the value is 15.6 (15.6 h = 15:36 by my arithmetic; 3:45 pm = 15.75 h; not in the paper) | 248 | P06 | roblox | VERIFIED (trap) |
| FC27 | Allowed range of GeographicLatitude: samples use 78 and 323, so check what range the property takes (my flag, not a paper claim) | 242, 244 | P04, P06 | roblox | check |
| FC28 | Property names: ColorShift_Top, OutdoorAmbient, EnvironmentDiffuseScale, EnvironmentSpecularScale, ExposureCompensation exist on Lighting with these names | 242-244 | P04-P06 | roblox | VERIFIED |
| FC29 | No Roblox terrain-material, water or terrain-scale claim exists in EP:1-255 beyond clouds under Terrain | - | - | note | - |

### 9.2 Audio

| ID | Claim or value | EP | Src | Kind | Tag |
| --- | --- | --- | --- | --- | --- |
| FC30 | No Roblox audio API or number is claimed in EP:1-255. Audio statements here are design rules and other-game reports; Roblox audio claims are in part 2 (EP:256+) | - | - | note | - |
| FC31 | A non-positional stereo bed cannot point to a source such as a waterfall (engine behavior assumed by the paper; check against Roblox positional vs non-positional sound behavior) | 159 | E00 | roblox | OPINION |
| FC32 | Valve team reports Steam Audio HRTF, DSP and occlusion in Alyx | 107 | C10 | industry | EXPERIENCE |
| FC33 | Sunken Plaza muffles outside sound (Deadlock); TOTK sound staff set where surface and sky audio contexts switch; Tsushima/Esperanca sound recording notes | 113, 75, 81 | C11, C05, C06 | industry | VERIFIED / EXPERIENCE |

### 9.3 Performance, streaming, scale, import, Studio and MCP

| ID | Claim or value | EP | Src | Kind | Tag |
| --- | --- | --- | --- | --- | --- |
| FC34 | 1 stud = 28 cm (Roblox standard physical-unit convention); engine does not convert units internally; another consistent interpretation is allowed | 25, 183, 206 | B02 | roblox | VERIFIED |
| FC35 | Model API has GetBoundingBox and GetExtentsSize | 193 | B06 | roblox | VERIFIED |
| FC36 | Camera API exposes view transforms, field-of-view controls, viewport dimensions, world-to-viewport projection (WorldToViewportPoint) | 155 | B09 | roblox | VERIFIED |
| FC37 | WorldRoot provides ray and shape queries (register key: GetPartBoundsInBox) | 155 | B10 | roblox | VERIFIED |
| FC38 | Importer: after import verify hierarchy, pivots, dimensions; success of the importer is not acceptance (register key quote: "Set Pivot to Scene Origin") | 41 | B05 | roblox | VERIFIED |
| FC39 | AI tools must address the Studio instance and data model explicitly (register key quote: every MCP tool call takes a studio_id parameter) | 43 | B03 | roblox / MCP | VERIFIED |
| FC40 | Graphics-tier behavior is platform and device specific; no cross-device fixed quality | 215, 253 | P03 | roblox | VERIFIED |
| FC41 | No universal light-count limit; no object-count limit; no phone-safe triangle count; no low-end phone ms for any lighting sample | 119, 227, 248 | E00 | roblox | OPINION / UNKNOWN |
| FC42 | Hist. League visibility data 128x128; 256x256 would be 4x CPU; reconstruction output 512x512 | 63 | C03 | industry | VERIFIED |
| FC43 | Hist. Fortnite indirect-light intensity 2.0; 4 ms GI + reflections; 60 fps console target | 95, 137 | C08 | industry | VERIFIED |
| FC44 | Tsushima scope: 3 regions, more than 40 biomes | 69 | C04 | industry | EXPERIENCE |
| FC45 | Esperanca: 3 sections/themes; seawall visible from both spawns | 81 | C06 | industry | EXPERIENCE |
| FC46 | Riot: weekly playtests during modeling (Icebox) | 53 | C01 | industry | EXPERIENCE |
| FC47 | Deadlock list: Broadway, Greenwich, York lanes; districts Theater, Chinatown, Haunted Lot, Plaza; Sunken Plaza muffles outside sound and drains stamina (C11 dated 2026-09-29) | 113 | C11 | industry | VERIFIED |
| FC48 | Paper examples, not facts: "ten generic containers" (89); the broken-aqueduct cue sentence (147); "three districts" is not claimed optimal (83) | 89, 147, 83 | E00 | example | OPINION |



## 10. Contradictions and limits

| ID | EP | Item | Handling in skills |
| --- | --- | --- | --- |
| X01 | 163-171 | Real disagreement: Totten (C12, 2010-06-11) treats prospect-refuge as a useful influence; the Level Design Book (C13, undated) says no shape is safe by itself and game state matters more. | Treat as hypothesis. Ask the game designer for the state ("safe under these rules") before the environment conveys safety. |
| X02 | 59 | C02 is a reprint on MOBAFire (2014-11-11 is the reprint date), not recovered official hosting; original date not recovered. | Use only the broad style idea; do not cite as an official Riot page. |
| X03 | 63 | League numbers 128x128, 256x256, 4x CPU, 512x512 are historic implementation figures. The register calls the 4x a projected impact. | Never use as a Roblox budget. |
| X04 | 95, 137 | Fortnite 2.0 and 4 ms are Lumen/console values. C08 is tagged EXPERIENCE/VERIFIED in the register: the numbers are VERIFIED only as a report of that implementation. | Never copy to Studio; keep the method, drop the values. |
| X05 | 101 | C09 is a pre-release statement of intent, not a player study or a full analysis of the shipped game. | Use for intent only. |
| X06 | 113-115 | C11 lists published features, not tested navigation outcomes or an art bible. | Do not infer Deadlock process or dimensions. |
| X07 | 169 | C13's Elden Ring example is the author's analysis, not a FromSoftware report. | Do not cite as a studio fact. |
| X08 | 107 | C10 is a Reddit AMA by a verified Valve account; the paper cites only Valve team replies, not fan comments. | Treat as developer testimony. |
| X09 | 69 | C04 page lists 2020-07-09 and a 2020-08-06 update. | Cite 2020-07-09 with the note. |
| X10 | 69, 119 | All ten cases come from large studios; scope (40+ biomes, console density) is no small-team estimate. Production time unknown per case. | Keep the craft decision, not the scale. |
| X11 | 11, 213-253 | All Roblox docs (B02, P01, P03-P11, P32) are undated living pages read on 2026-10-21. Only P02 has a date (2025-07-23). They may have changed. | Re-read the docs mirror before relying on a property name or value. |
| X12 | 248 | P05 gives 0.391 in a picture and 0.272 in the instruction; P06 gives 15.6 and "about 3:45 pm". | Use the literal instruction/property; flag in the manifest. |
| X13 | 231 | Atmosphere article sliders are isolated demonstrations. | Never merge them into one preset. |
| X14 | 235, 245 | Retro "brightness at most 1.0" is a documented experiment for one goal, not a ceiling. | Do not apply as a general light limit. |
| X15 | 246 | Biome lighting/fog values (mountain, swamp, cave, storm) are UNKNOWN. | Withhold numeric approval; measure per project. |
| X16 | 13, 119 | UNKNOWN items: source ranges, mix gains, low-end-phone budgets, phone-safe triangles, room sizes, build times, props per square metre, sound radii, light recipes, screenshot-recognition thresholds, universal cue count, light-count limit, door width, landmark screen fraction. | Do not invent. Fill by measuring in this project. |
| X17 | 15 | The paper ran no build, render, listen, playtest or benchmark. API procedures are plans. | Skills mark every test as to-do; results come from studio runs. |
| X18 | 215, 253 | Graphics-tier effects differ by device; post effects can vanish. | Judge readability with effects off. |
| X19 | 25, 41, 43 | Rules 4, 12, 13 carry both VERIFIED and OPINION marks: the source fact is VERIFIED, the studio use is OPINION. | Keep both marks when quoting. |
| X20 | 217 | No performance numbers for lights (cost, count, range limits for phones) are given. | Measure on target phones. |

## 11. Source IDs used in lines 1-255 (resolved from register EP:763-1469)

| ID | Source | Date and scope | Register line |
| --- | --- | --- | --- |
| E00 | The paper's own workflow, templates and rules | 2026-10-21; not an outside source or quote | 765 |
| C01 | Riot, The Art of VALORANT Map Environments (Zanotti) | 2020-11-16; EXPERIENCE; historic workflow, not Roblox guidance | 767 |
| C02 | Riot (Riototown), Defining the Rift's Visual Style | 2014-11-11 reprint date; EXPERIENCE; MOBAFire reprint, original date not recovered | 779 |
| C03 | Riot, A Story of Fog and War | 2016-05-13; EXPERIENCE/VERIFIED; implementation-specific numbers | 791 |
| C04 | Sucker Punch (Wang), Crafting the world of Tsushima | 2020-07-09, page lists 2020-08-06 update; EXPERIENCE | 803 |
| C05 | Nintendo, Ask the Developer Vol. 9 (TOTK part 3) | 2023-05-09; EXPERIENCE; sky scale and audio transitions | 815 |
| C06 | Blizzard (Pinto, de Mello Pereira), Voyage to Esperanca | 2022-10-18; EXPERIENCE | 827 |
| C07 | Naughty Dog (via Dornbush), The Last of Us building the world | 2023-02-07; EXPERIENCE | 839 |
| C08 | Epic (Wright, Narkowicz), Lumen in Fortnite Chapter 4 | 2023-01-26; EXPERIENCE/VERIFIED; console numbers not Roblox | 851 |
| C09 | Santiago quoting Chen, thatgamecompany's Journey | 2010-06-29; EXPERIENCE; pre-release intent | 863 |
| C10 | Valve, Half-Life: Alyx AMA | 2020-01-22; EXPERIENCE; developer replies only | 875 |
| C11 | Valve, City Never Sleeps (Deadlock) | 2026-09-29; VERIFIED; published features only | 887 |
| C12 | Totten, Towards a Digital Architecture | 2010-06-11; EXPERIENCE; article only, not the whole book | 899 |
| C13 | The Level Design Book, Prospect-refuge | undated, accessed 2026-10-21; EXPERIENCE; practitioner critique | 911 |
| B02 | Roblox, units | undated, acc 2026-10-21; VERIFIED | 931 |
| B03 | Roblox, Studio MCP server | undated, acc 2026-10-21; VERIFIED | 939 |
| B05 | Roblox, Importer | undated, acc 2026-10-21; VERIFIED | 955 |
| B06 | Roblox, Model API | undated, acc 2026-10-21; VERIFIED | 963 |
| B09 | Roblox, Camera API | undated, acc 2026-10-21; VERIFIED | 987 |
| B10 | Roblox, WorldRoot API (also alias A12) | undated, acc 2026-10-21; VERIFIED | 995 |
| P01 | Roblox, Global lighting | undated, acc 2026-10-21; VERIFIED | 1171 |
| P02 | Roblox DevForum, Unified Lighting full release | 2025-07-23; VERIFIED | 1181 |
| P03 | Roblox, QualityLevel API | undated, acc 2026-10-21; VERIFIED | 1191 |
| P04 | Roblox tutorial, Customize global lighting: Island Jump | undated, acc 2026-10-21; VERIFIED | 1201 |
| P05 | Roblox tutorial, Enhance outdoor environments | undated, acc 2026-10-21; VERIFIED | 1211 |
| P06 | Roblox tutorial, Enhance indoor environments | undated, acc 2026-10-21; VERIFIED | 1221 |
| P07 | Roblox, Atmospheric effects | undated, acc 2026-10-21; VERIFIED | 1231 |
| P08 | Roblox, Atmosphere API | undated, acc 2026-10-21; VERIFIED | 1241 |
| P09 | Roblox, Dynamic clouds | undated, acc 2026-10-21; VERIFIED | 1251 |
| P10 | Roblox, Post-processing effects | undated, acc 2026-10-21; VERIFIED | 1261 |
| P11 | Roblox, PostEffect API | undated, acc 2026-10-21; VERIFIED | 1271 |
| P32 | Roblox, Light sources | undated, acc 2026-10-21; VERIFIED; shapes and properties, not performance | 1461 |

## 12. Coverage map

| Item | Where |
| --- | --- |
| Evidence rules EP:5-15 | section 1 (EC0-EC10) |
| 15 rules EP:19-47 | section 2 (RU01-RU15) |
| Section 1, ten cases + limits + comparison + summary | section 3 (K01-K10, KC0-KC10, KS1-KS2) |
| Section 2 guiding the player + summary | section 4 (G01-G12, GS1-GS2) |
| Section 3 scale + summary | section 5 (SC01-SC08, SS1-SS2) |
| Section 4 lighting + summary | section 6 (L01-L13, LS1-LS4) |
| Section 5 atmosphere, recipes, traps + summary | section 7 (A01-A12, RC matrix, RC4-RC5, AS1-AS4) |
| Claims to fact-check | section 9 |
| Contradictions and limits | section 10 |
