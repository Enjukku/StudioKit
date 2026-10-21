---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J008-T04, DestructionSimulator stage sources (read-only)
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# First-game stage lessons for the environment designer (kit-neutral)

The first game's content builder made about 13 stages, buildings and landmarks from blueprints. The owner approved or rejected many of them. This note keeps what holds for ANY game, with the owner's words where they exist. Game names, theme names, the block style, part budgets and the break-physics rules are removed; numbers stay only as marked examples (class E) with their reason. Related: [[reference/environment/01-place-guidance-scale-light]], [[reference/environment/02-ambience-life-dressing-terrain]].

## 0. How to read

| Key | Meaning |
| --- | --- |
| ID | `FS-<group><nn>`. Groups: P plan and blueprint, R reference images, S scale and layout, T terrain and ground, B build and finish, L lighting, V review and Studio, H hand-off and process. |
| Class (Cl) | U = universal. E = game-specific example, kept only with its reason; do not copy the number. gap = no evidence found. |
| Kit stage | blueprint, reference, blockout, build, lighting, terrain, review, Studio, hand-off. |
| Owner's words | Word for word, in quotes, with the D-id and ledger line. "none verbatim" = only a paraphrase exists in the sources. |
| Evidence | `file:line`. The source column may name game themes in file paths; the lesson columns do not. |
| Verified | Nothing here is fact-checked against Roblox. Roblox facts in the old skills (walk speed, jump height, character size) are repeated only as the old game's numbers. |

Path key. Root = `C:\Users\Firew\Downloads\uterd\DestructionSimulator` (read-only).

| Short | Path |
| --- | --- |
| dec | knowledge/design/decisions.md (line = ledger row) |
| tf | knowledge/design/tried-and-failed.md |
| op | rules/owner-profile.md |
| ab | knowledge/design/art-bible.md |
| cb | .claude/agents/content-builder.md |
| bb, bbr | .agents/skills/brick-builder/SKILL.md, reference.md |
| af, ld | .agents/skills/art-fundamentals/SKILL.md, .agents/skills/level-design/SKILL.md |
| i2b, brp | knowledge/pipelines/image-to-brick.md, building-review-package.md |
| AG | AGENTS.md |
| log/x | knowledge/logs/x.md |
| sbN | knowledge/design/stages/NN-*.md (sb3 03-dream-doll-house, sb5 05-titanic-harbor, sb7 07-dino-park, sb9 09-airport, sb11 11-animal-city) |
| BPBn, BBn | content/stages/n-*/BLUEPRINT_BRIEF.md, BUILD_BRIEF.md (n = stage number) |
| LMB, RN13 | content/stages/02-landmarks/LANDMARK_BRIEF.md, content/stages/13-candy-kingdoms/plans/REVIEW_NOTES.md |

## 1. The owner's six named lessons: evidence check (C1)

| Named lesson | Rows | Evidence found | Strength |
| --- | --- | --- | --- |
| Blueprint and approval before building | FS-P01, P02, P05, P08 | dec:101 (D-091), dec:108, dec:172, tf:24 (F-012), op:19-21; the method was reused for stages 2-13 | Strong: owner words, one rejection, 8 later approvals |
| Real scale | FS-S01, S02, S03 | dec:101, tf:24, op:30, cb:16, log/agent-review/2026-10-09:10 | Strong: owner words and a rejected build |
| Terrain everywhere | FS-T01, T02 | dec:101, dec:116 (D-106), op:30, tf:24 | Strong: owner words twice |
| Windows on every face | FS-B01, B02 | dec:202 (D-192), ld:83, then copied into BPB9:19, BPB13:23, BB13:32 | Strong: one owner rejection, then a brief rule. No later complaint was found in the sources read |
| Renders reviewed before Studio | FS-V01, V02, V05 | op:19-24, brp:58, cb:25, the "Visual review" part of LMB:30, BB7:43, BB8:44, BB13:40 | Medium: the order is the owner's (profile); no verbatim quote; Studio was often not reached (FS-V08) |
| Own multi-angle review | FS-V03, V06 | AG:87-96 ("owner request, 2026-09-30"), cb:25, the same briefs | Medium: rule is explicit; no verbatim owner quote found; stage logs mostly say "not Studio-verified" |

Lessons the owner "already gave" were also pasted into later briefs as a list: BPB9:17-24, BPB13:21-25.

## 2. Lessons

### 2.1 Plan, blueprint, approval

| ID | Cl | Lesson | Evidence | Owner's words | Why it held | Removed | Kit stage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FS-P01 | U | Draw a measured blueprint (plan per storey, named rooms, furniture to scale, elevations, a player figure) and get the owner's OK before any building. A first build made without one was thrown away. | dec:101, dec:108, dec:172; tf:24; op:21; brp:53 | "you might have to start doing it like blueprint style" (D-091); "I want a blueprint of the house as well" (D-162); "The furniture in the floor plan, then I approved it and then they built it" (D-098) | Reused for stages 2-13; approvals at dec:172,180,186,188,206,215,216 | grid cells, compile steps | blueprint |
| FS-P02 | U | A complete blueprint holds: plan per floor with every room and prop to scale, front and side elevations (back for big ones), one section, a player figure on every sheet, a parts and materials table, new-prop table with sizes, estimate against budget, open questions. | BPB13:31,51; BPB9:28; i2b:28-36 | none | Same sheet set used by 6 stage chats | notes on how it breaks | blueprint |
| FS-P03 | U | Compare each ELEVATION with the reference silhouette before the blueprint is approved. A blueprint can be wrong while the build follows it faithfully: a boxy blueprint gave a boxy build; round-one drawings read as "one boxy block" and "a green building". | log/2026-10-13-stage7-dino-park-build:19; BPB13:32; BPB9:22; RN13:15-16; BB8:45 | none | Written into the next three stage briefs after stage 7 | - | blueprint, review |
| FS-P04 | U | Read every sheet image yourself before hand-off: labels readable, no overlaps, pieces inside walls, nothing floating, directions right. Redraw, then return. | BPB13:32; BPB9:30; log/2026-10-11-stage4-north-pole-blueprints:15 | none | Part of the brief's done-test | drawing tool details | blueprint |
| FS-P05 | U | Order for a stage: set list, then furniture / decoration / ground plan, then site plan (layout blueprint), then reference photos, then concept images, then building blueprints, then the shared prop kit, then buildings, then the stage frame (terrain, placement), then Studio. The owner fixed two points: site plan before building blueprints; references before building blueprints. | dec:192 (D-182), dec:198, dec:205, dec:211, dec:206 (D-230), dec:216 (D-260) | "before creating the building layout and blueprints, you should generate some reference photos using ChatGPT or using references online" (D-182); "we need to do the layout blueprint first" (D-201); "The layout is good. So you may go ahead and get started on generating the reference images" (D-199) | Stable from stage 7 to stage 13, each step approved with a ledger row | image tool names | blueprint |
| FS-P06 | U | Plan every decoration, furniture type and outdoor prop before building, and place them on the site plan, so layout and budget already know them. | dec:198 (D-188), dec:211 (D-201); sb11:63-134; sb7:45-92 | "we need to account for all the various decorations in the blueprint and where they should go" (D-188); "Just make sure everything is properly planned out" (D-188) | Became "Step 2" of every later brief | item counts | blueprint |
| FS-P07 | U | Check the site plan with a script, not by eye: overlaps, path network (junctions, one connected road set), heights, exits and ladders, water against the walkway, budget. A plan counted as ready only when the checks passed. | log/2026-10-11-stage3-dreamhouse-plans-and-first-builds:9; log/2026-10-11-stage5-titanic-harbor-blueprints:9; log/2026-10-12-stage6-toy-bedroom-blueprints:19 | none | Each stage plan shipped with a checks script | script names | blueprint |
| FS-P08 | U | Gates narrow as trust grows. After the owner approved a stage's set list, site plan and one round of references and blueprints, they said to continue without a stop, but still wanted results shown as they land. Agents never mark work owner-approved. | dec:174, dec:180, dec:201, dec:205, dec:214, dec:111; brp:10; dec:213 | "You no longer need my approval. You can just kind of go on and do your own thing" (D-170); "Don't worry about verifying the model in Studio. I'll take a look at it." (D-101) | Used for stages 2, 3, 7, 8, 10, 11 | - | hand-off |
| FS-P09 | U | Build set lists from what players expect to find at that kind of place (iconic things), not trivia. Give each stage a one-sentence hook. | sb3:10; sb5:15 (paraphrase); dec:176 (D-166); sb7:8; sb9:8; sb11:8 | "they should all be iconic references" (sb3:10) | The owner cut trivia ideas and kept the iconic ones | franchise inspiration labels | blueprint |
| FS-P10 | U | Stages must feel different as a whole. Repeating a kind of element across stages is fine. | dec:207 (D-194) | "I just want each stage to be different from one another" (D-194) | It undid a self-made rule that dropped good ideas | - | blueprint |
| FS-P11 | U | When the budget forces cuts, the owner says what to protect. Ask early. Seen: cut extras, not the main hall; cut rooms, not decoration; cheaper furniture first, not removal. | dec:209 (D-196); dec:183 (D-173); dec:204 (D-198); log/2026-10-11-stage3-dreamhouse-plans-and-first-builds:26 | "that way we have more room for decorations" (D-198) | Each cut order was stated once and held | part counts | blueprint |
| FS-P12 | U | A wrong number in a shared brief spreads to every drawing. A stair rule in a brief fitted no storey and was fixed later in a binding review-notes file. Check brief numbers against geometry before parallel agents start. | RN13:9; BB13:11 | none | Review notes won over group drawings | stair values | hand-off |
| FS-P13 | U | Read prop sizes from the shared prop data. Retyped sizes drifted to 0.3-0.8 of true size in 3 of 7 groups. Rooms were rearranged and pieces dropped, never shrunk. | log/2026-10-13-stage8-blueprint-audit:14,31 | none | Found by audit, fixed by reading data | - | blueprint |
| FS-P14 | U | Name a priority order in every brief: review notes, then blueprint (size, layout), then concept image (look, density), then photo and still notes. List known gaps in the concept images and decide them at blueprint time. | BB13:11-14; BB8:11-13; BB7:12; dec:188 (D-178) | none | Same order in 4 stage briefs | - | hand-off |

### 2.2 Reference and concept images

| ID | Cl | Lesson | Evidence | Owner's words | Why it held | Removed | Kit stage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FS-R01 | U | For real places, real photos and measured drawings come first. Generated images are a style hint only: one was inaccurate, one had wrong colour banding, one looked "strange". | dec:174 (D-164); dec:173 (D-163); LMB:10-12 | "I would prioritize our real references" (D-164); "we do still want to make it accurate" (D-163) | The owner rejected 3 of 9 generated hero images | image tool | reference |
| FS-R02 | U | Make all views from ONE 3D massing model and paint over it. Views generated one by one disagree (3 windows per wall in one sheet, 4 in another). | i2b:42-48; dec:82 (D-072) | "an adequate amount of reference images are generated for every angle" (D-072) | Adopted as the pipeline | compile tool names | reference |
| FS-R03 | U | Required view set: two opposite 3/4 views (one hides two faces), four elevations, roof plan, a plan per floor, one interior per major room, a cutaway for multi-storey. Per stage at least 15 consistent images: aerial from each side, a ground view of every zone, a mood image, entrance and exit views. | i2b:52-60; dec:34 (D-025) | none verbatim (D-025 is a decision text) | Checked by a coverage tool | tool names | reference |
| FS-R04 | U | Read sheets against a ruler: overlay a grid and read openings, wall ends and roof lines as cells. A model reads positions better against a grid than by proportion. | i2b:68 | none | Tool idea, no owner evidence | cell units | reference, blueprint |
| FS-R05 | U | Approve a stage-wide image set first and attach it as anchors to every structure image, so the world stays consistent. | i2b:60,64; dec:180 (D-170) | none | Used for stages 3-13 | - | reference |
| FS-R06 | U | Show reference and concept images to the owner before building. The owner offers to review them and approves them as a batch. | dec:168 (D-158); dec:210 (D-197); dec:216 (D-260) | "I can review all the reference images" (D-158) | Every stage had this gate | - | reference |
| FS-R07 | U | Reference packs list source and licence per image. Keep selected images, not bulk copies of a site. | dec:197 (D-187); log/2026-10-13-stage7-dino-park-build:10 | "I just didn't want the entirety of the wiki in our project" (D-187) | Owner rule, 2026-10-13 | policy detail (use the platform-policy skill) | reference |

### 2.3 Scale and layout

| ID | Cl | Lesson | Evidence | Owner's words | Why it held | Removed | Kit stage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FS-S01 | U | Build at real scale, measured against a player figure. Buildings at about real-life size felt like miniatures: cramped rooms, tiny furniture. | dec:101 (D-091); tf:24 (F-012); op:30; cb:16; log/agent-review/2026-10-09:10 | "it's almost like you're making a miniature on purpose rather than making it the real size" (D-091) | The owner rejected the builds, chose a bigger scale, and kept it for 13 stages | block grid | blueprint, blockout |
| FS-S02 | E | Example numbers: buildings 1.5 x real, furniture about 1.2 x real, a cottage 45 x 60 studs (real 8 x 11 m), doors about 7.5 x 12 studs. Reason: the character is 5.2 studs, so real-size rooms felt small. Do not copy: the kit sets its own scale convention. | dec:101; bbr:24; BPB13:22 | "Let's do a game scaled one point five x" (D-091) | Stable | the multiplier as a rule | blueprint |
| FS-S03 | U | Scale cues are what the player touches: doors, stairs, rails, chairs, counters. Furniture must work for the player. Furniture "too coarse for the room" was a repeated rejection. | af:47; cb:16; op:30; bbr:24 | none verbatim (profile: "Rooms and furniture make sense at player scale") | Same rejection seen by the agent review | part sizes | blueprint, review |
| FS-S04 | U | A scale gimmick (the player is toy-sized and furniture are the buildings) needs one stated conversion in the brief. Props meant to read as toys may be a little larger than the player. | log/2026-10-12-stage6-toy-bedroom-blueprints:8; dec:179 (D-169) | none | Approved | - | blueprint |
| FS-S05 | U | Replicas of real places keep the true shape and details; overall size is scaled down to fit the map; doors and stairs stay at player size. | dec:164 (D-154); dec:167 (D-157) | "I think the scaling is fine" (D-157) | Approved as drawn | - | blueprint |
| FS-S06 | U | Walk time is a layout decision. Keep walks to the next goal short and keep the next area visible ahead. When buildings were scaled up, the whole stage was scaled with them. | dec:97 (D-087); dec:105 (D-095); dec:25 (D-016); ld:47 | "not walking so far forward to get to the next stage" (D-087) | Owner asked twice | - | blockout |
| FS-S07 | E | Example numbers: a 300-stud path took about 19 s on foot; a hub was sized to cross in about 8 s. Reason: short mobile sessions. | dec:105; knowledge/design/stages/00-lobby.md:12 | none | - | game-specific walk speed | blockout |
| FS-S08 | U | Compose for the approach view: the main face of a landmark points at the route; the owner turned a building to face the path. | dec:118 (D-108); dec:181 (D-171); log/2026-10-13-stage11-animal-city:34 | "I want the opening of the church to be on the other side" (D-108) | Repeated in stages 5, 6, 11 | - | blueprint |
| FS-S09 | U | Name 2-3 iconic traits per structure in the brief and check them at real camera distance. A ship read as a ferry; a face on a mountain was drawn too small to read from the walk. | bb:38-40; af:39; log/2026-10-11-stage5-titanic-harbor-blueprints:10; RN13:10; log/2026-10-13-stage13-candy-kingdoms:31 | none | Found in review, then fixed in blueprint | - | blueprint, review |
| FS-S10 | U | Partial evidence: a massing-only model came before any image or blueprint. It fed the image set; no log shows a walk test of a blockout. | i2b:42-45; bb:15; log/2026-09-30-stage1-prototype:17 | none | The walk-test blockout step comes from the level-design skill, not from owner evidence | - | blockout |
| FS-S11 | U | Fix one scale convention once. Briefs of the same game gave door sizes of 4 x 7.2, 7.5 x 12 and 8 x 12 studs, and a stud-per-metre figure that disagrees with the ledger. | BPB9:18; dec:101; BPB13:22; sb9:66 | none | Seen while reading; not resolved in the sources | - | hand-off |

### 2.4 Terrain and ground

| ID | Cl | Lesson | Evidence | Owner's words | Why it held | Removed | Kit stage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FS-T01 | U | Every area and every stage has terrain with height changes and visible layers. Buildings set on a flat plane were rejected. | dec:101 (D-091); dec:116 (D-106); op:30; tf:24 | "each area needs to do terrain" (D-091); "we want a little bit of terrain in every stage" (D-106); rejected: "a very flat stump" (op:30) | Every stage brief has a ground section (sb11:122) | the game's thin layer over a hard floor | terrain |
| FS-T02 | U | Ground fits the theme: roads, pavements and plazas in a city; lawns and gardens round a house; landmarks propped up on a hill. | dec:116 (D-106) | none | - | - | terrain |
| FS-T03 | U | Roads and paths join with proper intersections. No stubs, no gaps. Every path joins the network or ends at a destination. Every door meets a path. | dec:167 (D-157); dec:178 (D-168); dec:213 (D-203); BPB13:23 | "make sure that there's appropriate pathways and that everything is interconnected via roads" (D-157); "Make sure like everything properly connects together. Like same with the pathways" (D-168) | Asked in 3 stages; added to the plan checks (FS-P07) | - | terrain, blueprint |
| FS-T04 | U | The main walkway is never interrupted by scenery: the river ends before it, no water beside it. | dec:168 (D-158) | "the tube is kind of just like the pathway, so it should be uninterrupted" (D-158) | - | the tube as a game device | blueprint |
| FS-T05 | U | Give players a way out of every pit, river and high place: ladders on both banks, climb routes. | dec:169 (D-159); log/2026-10-12-stage6-toy-bedroom-blueprints:9; log/2026-10-13-stage11-animal-city:40 | "a couple ladders on each side so players can get across" (D-159) | - | a rule that ladders cannot be damaged | blueprint |
| FS-T06 | U | Long real-world features follow the land. A wall drawn as a straight border strip was rejected for missing its twists and turns. | dec:167 (D-157) | "it's missing its twists and turns" (D-157) | Approved after redraw (D-158) | - | blueprint |
| FS-T07 | U | Boundaries look like the world: steep cliffs or decorative walls on theme, backed by a true invisible barrier. A boundary may look obviously like a barrier. | dec:103 (D-093); dec:104 (D-094); ld:52 | "a true invisible barrier" (D-093); "it can be obvious that it's a barrier" (D-094) | - | tall grass columns | terrain |
| FS-T08 | U | Check water level against floors of rooms inside hulls and basins in the site plan. | log/2026-10-13-stage8-build-wave2:40 | none | - | - | blueprint |
| FS-T09 | U | Do not pay detail for parts nobody uses. The owner cut a decorative half of a large landform and asked for coarser detail. | dec:131 (D-121) | "half of the mountain is completely useless and decorative" (D-121); "scale down the detail of the mountain" (D-121) | Cost and performance | part counts | build |
| FS-T10 | E | Ground cost was 3 x the plan's line (23k vs 6.9k parts) because cover depth was guessed. Measure one ground tile before budgeting. | log/2026-10-13-stage9-airport:23; log/2026-10-11-stage5-titanic-harbor-blueprints:20 | none | - | part units | blueprint |

### 2.5 Build and finish

| ID | Cl | Lesson | Evidence | Owner's words | Why it held | Removed | Kit stage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FS-B01 | U | Every face a player can see is finished. Back and side walls get windows or equal detail, dressed like the front. Players walk round buildings. | dec:202 (D-192); ld:83; BPB9:19; BPB13:23; BB13:32; old reason at content/stages/01-blockcraft/structures/village_house_a/PLAN.md:38 | "on the back of the buildings ... all the panels don't have windows, which looks a little bit strange" (D-192) | Copied into every brief of stages 8-13 | the old reason (a glass rule tied to the game's break physics) | build |
| FS-B02 | U | Walls on all four sides. Do not open a side so the viewer can look in, unless the owner asks. | dec:175 (D-165); dec:178 (D-168) | "The house doesn't need a open side. It can be solid walls all around it" (D-165) | Applied to later houses | - | build |
| FS-B03 | U | Every room a player can enter is furnished and dressed. Outsides and roofs are dressed too. Redo sparse floors. | dec:25 (D-016); dec:175; log/2026-10-11-stage4-north-pole-blueprints:10,12; BPB9:19 | "some of the rooms do look under-decorated. Like, the kitchen" (D-165) | A standing rule in 6 briefs | break-value rewards | build |
| FS-B04 | U | First builds come out plain and under-detailed (about half the detail budget). Plan at least one polish round and compare dressing density with the concept. Spend on signature details. | BB8:37,45; log/2026-10-13-stage7-dino-park-build:20; dec:140 (D-130) | "The builder agent, further polishing rounds is good" (D-130) | Seen in stages 7, 8, 13 | - | build |
| FS-B05 | U | A numeric match score is a floor, not the finish. The owner rejected builds for scale, detail, facing and organic shape, which an outline score cannot see. Make those four the done-test. | bb:27; cb:16; log/2026-10-10-skill-agent-review:18; log/agent-review/2026-10-09:10 | none verbatim | Agent review 2026-10-09 | outline tool, 0.85 number | review |
| FS-B06 | U | Check the facing of every directional piece (roofs, awnings, slopes, lecterns, carpets, doors, stairs, bows). | cb:16,25; AG:90; dec:118 | none verbatim | A repeated owner rejection | wedge pieces | review |
| FS-B07 | U | Organic things (trees, rock, caves) stay organic: one coherent canopy or landform silhouette, no boxy shapes, no overused sphere primitives. | dec:202 (D-192); log/2026-10-13-stage11-animal-city:30,32; log/2026-10-13-stage13-candy-kingdoms:33; log/agent-review/2026-10-09:10 | "the use of all these various like spheres also looks very odd" (D-192); "you can still use spheres for the trees, but you just gotta merge them in a way that makes it look appropriate" (D-192) | Fixed in rebuilds of two stages | part-shape limits | build |
| FS-B08 | U | Interactive details must work, or be clearly decoration. Doors that look like doors must open. | dec:102 (D-092) | "the doors didn't actually work" (D-092) | Owner play-test | hinge physics | build |
| FS-B09 | U | Window glass must read as glass at game distance, not as an empty hole. | dec:96 (D-086); log/2026-09-30-stage1-prototype:63 | "make glass more cartoony, like you can see the glass more" (D-086) | - | transparency number | build |
| FS-B10 | U | Tell a story of use: wear where hands and feet go, leftovers of living, dirt in low corners. | af:48; bb:40 | none | Old builder's checklist; no owner evidence | - | build |
| FS-B11 | U | Make a shared prop kit first and reuse it with colour and rotation variants. Reuse a few approved house types instead of one design per house. | dec:108 (D-098); dec:101; dec:206 (D-230); BB13:34; af:49 | "You don't need to make unique ones for every single village house" (D-098) | Kit first in stages 5-13 | block prefab format | build |
| FS-B12 | U | One owner for each shared asset set in parallel work (for example all outdoor props). Others check first and use the exact name. | BB8:41; BB7:39 | none | - | - | hand-off |
| FS-B13 | U | In a city, fill the streets with decoration and street furniture first. Not every building needs an interior. | dec:208 (D-195) | "making sure we fill the streets with decorations and furniture" (D-195); "you don't need to do interiors for everything" (D-195) | - | - | build |
| FS-B14 | E | Small dressing (string lights, wreaths, icicles) went on a cheap layer outside the part budget: a glowing line, not separate bulbs. Reason: phone cost. Kit analogue: decals, beams, attachments. | dec:185 (D-175); bbr:38-50 | "Glowing string with bulbs" (D-175) | Adopted | the trim format | build |
| FS-B15 | U | Each stage picks one dominant, one secondary and one accent colour and records them in its brief. | ab:76-80 | none | Art bible rule | colour lists | build |

### 2.6 Lighting

| ID | Cl | Lesson | Evidence | Owner's words | Why it held | Removed | Kit stage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FS-L01 | U | Lighting is set per stage, and a stage may get its own sky. The first stage read "too dim"; the target was a bright, vibrant, happy mood. The owner allowed brighter ground colours (grass) and said the buildings were fine. | dec:136 (D-126) | "the lighting is a little bit dim ... I kind of want it to be like vibrant" (D-126); "each stage I think will adjust the lighting ... maybe even new skybox for each stage" (D-126) | Stated once, no reversal | stage-1 mood word | lighting |
| FS-L02 | U | Lighting leans cartoon, not the engine default look. The owner picks from screenshots of presets. | dec:133 (D-123) | "make the lighting more cartoony" (D-123) | - | brand look | lighting |
| FS-L03 | U | Use the engine's own lighting objects and shadow settings, not a home-made system. Per-stage changes are property values only. Measure shadow cost before removing shadows (the saving was small). | dec:149 (D-139); tf:11 (F-018); dec:138 (D-128) | "Why are we like inventing our own stuff?" (D-139) | Owner reversal of a custom shadow system | shadow categories | lighting |
| FS-L04 | gap | NO EVIDENCE FOUND in the stage sources for atmosphere (fog, haze), ambient sound, ambient life, time of day or weather. District fog appears only as prop names in sb11:32,112,120. The research notes in [[reference/environment/02-ambience-life-dressing-terrain]] have no first-game backing. | grep of stage briefs and logs, 2026-10-21 | none | - | - | lighting |

### 2.7 Review and Studio

| ID | Cl | Lesson | Evidence | Owner's words | Why it held | Removed | Kit stage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FS-V01 | U | Review order for anything visible: (1) blueprint, approved before building; (2) offline renders next to the concept sheets, approved before Studio; (3) Studio placement and multi-angle review. | op:19-24; brp:58; cb:25; LMB:30-31; BB13:40-41 | none verbatim (profile paraphrase: "a render is enough", op:24) | Every stage brief from stage 2 on has this paragraph | render tool names | review |
| FS-V02 | U | Put each render beside the matching reference at the same angle and assemble one labelled review sheet. | LMB:31; BB13:41 | none | - | - | review |
| FS-V03 | U | Before the owner sees anything, shoot it yourself from front, side, back, a high 3/4 and player-eye height. Check direction of directional parts, floating or hidden parts, scale against the player, match to the concept. Fix, re-shoot, then report. Restore the owner's edit camera. | AG:87-96 | none verbatim (AG:87 says "owner request, 2026-09-30") | The rule sits in the project's top rulebook | - | review, Studio |
| FS-V04 | E | Example cap: up to 6 rounds to reach the floor, then up to 3 polish rounds, then escalate with what is still wrong. Reason: token cost. | cb:18; bb:28; dec:140 | none | - | the number | review |
| FS-V05 | U | A builder's "0 FAIL" is not a look check. A second reader compared sheets with concepts and found real failures (trees, a crown, a stair that was a lift). The owner spotted a crown off-centre in a render. | log/2026-10-13-stage11-animal-city:30,32,34,43; log/2026-10-13-stage7-dino-park-build:19-21 | none | - | validators | review |
| FS-V06 | U | Label every check (gate, MCP, owner-confirmed, not verified). Report the 3 weakest points left. | AG:83-86; BB13:46-47; cb:23 | none | - | - | hand-off |
| FS-V07 | U | Walk the route with real character movement: every entrance, stairs, room and exit. A first probe missed the stairs because of a wrong coordinate and was corrected. | log/2026-10-05-two-buildings-studio:14; log/2026-10-13-stage2-landmarks-studio:8; RN13:9 | none | - | door physics | Studio |
| FS-V08 | U | Studio is scarce: one instance, one driver at a time (the owner tried two windows and it failed). Most stage logs end "not Studio-verified" because another chat held Studio or the machine ran out of memory. Book the slot. | op:49; log/2026-10-13-stage7-dino-park-build:16; log/2026-10-13-stage6-placements:34; log/2026-10-12-stage3-dreamhouse-build-and-placement:15 | none | Pattern across 6 logs | chat tooling | Studio |
| FS-V09 | U | Before a screenshot, move the character or camera into the content (the client drew content only near the character). Restore the edit camera afterwards. | log/2026-10-14-stage8-polish-frame-studio:23; AG:95-96 | none | Streaming caveat; check against the kit's streaming notes | custom draw radius | Studio |
| FS-V10 | U | Read the engine docs first and use engine features where they fit; say why when you do not. | dec:138 (D-128); cb:19 | "we should settle for what is optimized and the best course of action on the Roblox engine according to Roblox themselves" (D-128) | Required in builder reports ("Docs read") | - | Studio, build |
| FS-V11 | U | Build and test the heaviest piece first, then decide. A ship was built first and played in Studio; verdict "smooth enough to continue". | dec:183 (D-173); log/2026-10-11-stage5-titanic-harbor-blueprints:63-71 | "I'm open to having 100,000 ... I think it shouldn't be too big of an issue" (D-173) | - | part frame | Studio |
| FS-V12 | E | Shipped content size counted: a stage's generated data (about 2-3 MB) went to every client at join and had a byte budget. Kit analogue: streaming and memory budgets, checked on a phone. Old logs measured only on a PC. | log/2026-10-13-stage8-build-wave2:50; dec:127 (D-117); log/2026-10-04-stage1-layout-materials:41 | none | - | the byte budget | Studio |

### 2.8 Hand-off and process

| ID | Cl | Lesson | Evidence | Owner's words | Why it held | Removed | Kit stage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FS-H01 | U | Assembling the stage (terrain, placements) is its own step with one owner. Builders return placement entries and never edit the stage file; a generated stage file is changed at its generator, not by hand (a hand edit was reverted). | BB13:20; BB7:26; log/2026-10-11-stage2-landmarks:8 | none | - | file names | hand-off |
| FS-H02 | U | Re-check placement against BUILT footprints, not planned slots. Props were re-checked against built outlines: 107 kept, 19 moved, 7 dropped; some builds ran 1-2 studs over their slot. | log/2026-10-13-stage6-placements:10-11; log/2026-10-13-stage8-build-wave2:43 | none | - | tool names | hand-off |
| FS-H03 | U | A shared brief has fixed parts: goal; references in priority order; frame facts (axes, origin, ids); tools; "rules agents miss"; visual review; done-when; return in about 350 words (counts vs budget, placements, review sheet paths, 3 weakest points, kept warnings). | BB13 (whole file); BB8; BB7; cb:23 | none | Same shape across 6 briefs | git rules | hand-off |
| FS-H04 | U | Never change a material or a test to pass a check. After a merge, check for deleted files and material changes: an agent switched a part type to pass a test, and a squash deleted 216 photos. | log/2026-10-11-stage2-landmarks:30; BB13:29; LMB:22 | none | - | - | hand-off |
| FS-H05 | U | Breadth first, polish later. The owner stopped polish runs three times to finish the whole stage first. Keep a dated polish backlog and the list of weakest points. | log/2026-10-13-stage8-build-wave2:22,49; log/2026-10-13-stage10-bikini-bottom:37; log/2026-10-13-stage11-animal-city:22 | "finish it up and just final polish later" (log stage 11, line 22; owner words as logged) | Contrast with FS-B04: polish is wanted, but after a full first pass | - | hand-off |
| FS-H06 | U | Status flow draft, then review, then approved. Only approved content ships. | i2b:16; brp:10 | none | - | manifest names | hand-off |
| FS-H07 | E | Parallel stage chats clashed on decision numbers (5 times in one day), on a shared index and on slow hooks. Fix used: number blocks per stage. The kit has its own ledger; keep one writer per file. | log/2026-10-13-stage9-airport:19; log/2026-10-13-stage11-animal-city:18; log/2026-10-13-stage10-bikini-bottom:29 | none | - | git details | hand-off |

## 3. How a stage was planned, and what a stage brief held

| Step | Output | Gate | Evidence |
| --- | --- | --- | --- |
| 1 Brainstorm (2-3 rounds) | set list with role, footprint, budget, interior, features; kept and cut log | owner picks | sb9:14-35,89; dec:176,181,192 |
| 2 Furniture, decoration, ground plan | room-by-room lists, zone dressing, terrain per zone, new pieces | none (inside brief) | sb11:63-134 |
| 3 Site plan | slots, heights, travel order, path network, checks script, plan and height images | owner | dec:167,168,198,205,209,212 |
| 4 References, concepts | real photos with licence notes; film stills; generated concept images | owner reviews | dec:173,201,210,216 |
| 5 Building blueprints | groups A-F sheets; orchestrator review notes | owner | dec:188,215,206,216 |
| 6 Prop kit, then buildings | each structure with a review sheet | self-review | BB13, BB8 |
| 7 Stage frame | terrain, placements, registration | gate | log/2026-10-14-stage8-polish-frame-studio:12-13 |
| 8 Studio | load, walk, multi-angle, speed check | studio operator | log/2026-10-13-stage2-landmarks-studio |

A stage brief held (kit blueprint template should keep the starred ones): hook* (sb7:8); look rule and leave-outs (sb9:5); set list with role, size, budget, rooms, features (i2b:28-34)*; research list with sources (sb7:12, sb11:59); main props and movers (sb9:35,48); overlap watch against other stages (sb9:56, sb11:55)*; owner replies and kept/cut log (sb9:60,89)*; fit check of estimate against frame (sb11:39)*; furniture per room, outdoor dressing per zone, ground per zone, new pieces (sb11:63-134)*; travel order and budget note (sb7:174-178)*.

## 4. Owner approvals and rejections about places (timeline, no verbatim beyond section 2)

| Date | Event | D-id | Rows |
| --- | --- | --- | --- |
| 2026-10-04 | Real-size builds rejected as miniatures; blueprint-first, bigger scale, terrain | D-091, F-012 | S01, P01, T01 |
| 2026-10-04 | Doors must work | D-092 | B08 |
| 2026-10-04 | Reuse of approved house workflow | D-098 | B11, P01 |
| 2026-10-06 | Terrain in every stage | D-106 | T01 |
| 2026-10-06 | Layout round: blueprints approved with edits; building turned to face the path | D-107, D-108 | S08 |
| 2026-10-07/09 | Over-count accepted; "nice enough" | D-109, D-125 | P11, H05 |
| 2026-10-09 | Useless decorative half cut; lighting too dim | D-121, D-126 | T09, L01 |
| 2026-10-10 | Use the engine's own lighting | D-139 | L03 |
| 2026-10-11 | Real references first; under-decorated kitchen; no open side; roads must join | D-164, D-165, D-168 | R01, B03, B02, T03 |
| 2026-10-11 | River must not cross the walkway; exits from the river | D-158, D-159 | T04, T05 |
| 2026-10-13 | Back walls need windows; sphere overuse; trees | D-192 | B01, B07 |
| 2026-10-13 | No ban on repeating elements across stages | D-194 | P10 |

## 5. The old builder's loop: what survives

| Old step | Keep | Drop |
| --- | --- | --- |
| Read the contract, stage brief and concept sheets (cb:15); stop and ask if the brief row is missing (bb:14) | Yes | pipeline names |
| Read taste table and rejected approaches first; check the 4 rejection causes in renders (cb:16) | Yes: make the list a checklist | - |
| Massing first, views painted over it (bb:15-16) | Yes | tool commands |
| Measure on a grid overlay (bb:17) | Idea only | cells |
| Blueprint with primitives, skeleton, materials, trims (bb:19-25) | Name parts and materials by what they are | block primitives, skeleton physics |
| Compile, validate, score per view (bb:26-27) | One verdict line per view | compiler, outline score |
| Iterate, cap rounds, escalate (cb:18; bb:28) | Cap idea | numbers |
| Cheap checks while iterating, full gate once before commit (bb:28) | Yes | - |
| Break-physics pass (bb:29) | No | all |
| Hand-off status review, not approved (bb:30) | Yes | - |
| Return about 400 words with counts, paths, verdict per view, decisions needed (cb:23) | Yes | - |

## 6. What the old content-builder did that the new role does not do

| Old duty | Evidence | Who has it now |
| --- | --- | --- |
| Built single buildings, landmarks and props part by part from concept art | cb:3,13 | modeler (assets); the environment designer places them |
| Built pets, weapons and hero movers | cb:3; bb description | modeler, character rigger, animator |
| Ran a block compiler, validator, stats and outline-compare tools | bb:26-27 | kit audit tools |
| Placed break set-pieces, special and treasure parts, weak joints; interlock targets | bb:29,42-48; cb:21 | not an environment duty |
| Applied building physics rules and material physics | bbr:9-20; dec:100 | not an environment duty |
| Worked to a part budget per structure | cb:21 | budgets come from the owner or a phone measurement (J008 brief) |
| Never drove Studio; waited for a studio operator | cb:25 | the new role does its own multi-angle review, then hands off |
| Never called an image service; asked the lead | bb:15 | reference-images skill |
| Never set the set list, layout or routes | sb notes; dec:211 | game designer; routes are proposals only |
| Never did lighting, sky, atmosphere or ambience | L04 gap | new role |
| Wrote generated game modules, stage registration, economy rows | LMB:28; dec:184 | engineering |

## 7. Gaps in the sources

- No first-game evidence for atmosphere, ambience, ambient life, time of day or sound (FS-L04). No evidence on using Blender for stages.
- No stage log measured on a phone. Studio verification is patchy: many stages were approved from renders and blueprints only (FS-V08).
- Owner words come from the ledger. The profile gives paraphrases ("a render is enough"); they are marked.
- Old documents contradict each other on scale and units (FS-S11; brp:77 warns of stale scale text). Read the ledger row, not the oldest example.
- Roblox figures in the old skills (walk 16 studs/s, jump 7.2, character 5.2 studs: ld:54) are NOT verified here.
