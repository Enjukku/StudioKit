---
type: job
scope: universal
status: draft
updated: 2026-10-21
source: J016 step 1 (P1, P2, Riot transcripts R00-R13, kit skills)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J016 step 1 — Flow per job type (PROPOSAL until G1)

Keys as in `design.md`. Every type follows the general flow (`design.md` §3). This file says, per type: who leads, which leads agree the direction, the shared contract, who cooperates sideways, the cheap proof, the order of production, the integrator, the review order and the return paths.

## Which job types, and why these
| Type | Why it is its own recipe | Evidence |
| --- | --- | --- |
| Cutscene | picture, motion, effect and sound must hit one timeline; camera and endings | P1:252, P2:235; R04:164-180, R07:211-215 |
| Character or creature | model ↔ rig ↔ animation dependency; identity at game camera | P1:256, P2:236; R03:864-900; R00:1134-1562 |
| Stage | play layout comes before art; art stays inside the greybox | P1:256, P2:237; R02:454-470; R09:668-680; R00:1757-1785 |
| UI screen | function and states before style | P1:256, P2:238; R00:4573-4885 |
| Gameplay feature | player behaviour and acceptance tests before code is split | P1:256, P2:239; R00:5767-5785 |
| **Effect** (a hit, pickup, reveal, telegraph, with its sound) | the most frequent cross-craft job in a Roblox game; gameplay timing ↔ animation ↔ VFX ↔ sound, and readability rules no other type has | R06:49-80, R06:204-210; R07:198-215; R04:166-168; R00:3552-3832; P1:169; K4 |
| **Marketing art** (icon, thumbnails, key art and its family) | its own gate rhythm (thumbnail → green light → render → polish), real-size reads, layered delivery, truth to the game | R05:144-176, R05:732-797; R08:656-712; R10:97-209; kit `marketing` role |
| Variant of an existing asset (skin, recolour, themed version) | **not a separate recipe**: the character recipe in variant mode (base rig, animations and 2-3 identity anchors fixed; motion-needs step skipped unless new moving parts) | R03:864-878; R12:73-81; R11:214-226; R10:528-537 |
| New game pre-production | **kept as is**: the `preproduction` skill's growth order (one owner decision per step) produces the briefs these recipes consume | kit `preproduction/references/growth-order.md` |
| Live update or event | **not a recipe**: the live-ops plan is split by the lead into jobs of the types above | kit `live-ops-designer` role |

**Stages per saved workflow** (one call each, your gate between): `direction` → G1 → `proof` → G2 → `build` → G3; `repair` applies a G3 change to the affected layers only. M jobs: `direction` → G1 → `build` (the proof runs inside `build` and is shown at G3). S jobs: no workflow (C07; `design.md` §3).

---

## 1. Cutscene (story cutscene, boss intro, reveal, ending, short camera moment)
| Item | Value | Evidence |
| --- | --- | --- |
| Job lead | **film-director** (also the sequence integrator, the role layout plays at Blizzard: keeps continuity from boards to final frames) | P2:55 (H06); K6; kit `film-director` role |
| Direction leads | film-director (beat contract, camera mode, staging, 2 approaches) · art-director (look per beat: palette, light, shape; 2-3 reference images) · architect (feasibility: runtime choice, camera ownership, streaming, skip and every ending; what to probe in Studio) · game-designer consulted for the gameplay state sheet | P1:416; P2:490; kit `templates/jobs/beat-sheet.md` gameplay state sheet |
| G1 shows | the beat contract, 2 pictured approaches (board thumbnails or reference images), the recommended one, scope and usage | P1:414-416; R05:170-176 |
| Shared contract | the **beat list + shot list** (`tools/film/shotlist.py`), owned by the film-director: stable event ids, start/end, trigger, camera, animation state, VFX cue, sound cue, player-control state, skip consequence, revision | P1:167, P1:418; P2:156, P2:465-478 |
| Proof (G2) | storyboards + a **timed Blender animatic** with temporary sound and temporary effect cues, on a greybox set where the set is missing; reviewed by film → art (composition, look feasible) → architect (cost flags) before you see it | P1:420-422; P2:491-493; kit `film-craft` §3 steps 4-5 |
| Sideways after G2 | **crafts planning exchange** before costly work: animator (acting per shot, rig features needed) ↔ character-rigger ↔ modeler (only if new cast: run the character recipe's interface stage) · environment-designer (sets, landmarks, light per beat) ↔ film · **VFX ↔ sound co-design each cue's envelope** (anticipation, peak, decay) on the event ids · UI (letterbox, subtitles, skip) · feature-builder (player contract, endings). Each writes needs against beat list rev N; film reconciles to rev N+1; ≤ 2 rounds | P1:169, P1:424; P2:149-156; R00:2965-2971, R00:3830-3834 (wind-up shared by motion, effect and sound) |
| Production order | environment set and animation in parallel → VFX and sound **prototype on the stable event ids early**, finish against animation (staggered behind it) → one combined early pass of picture + VFX + sound reviewed before final polish (mix early) | K4; P1:426; R04:164-180; R07:198-215 |
| Check-ins | film reviews animation **blocking** before polish; art reviews rough set and look before final light | P2:201; R00:878-884 (show early, no grand reveals) |
| Integrator | film-director assembles scene data (`shotlist.py luau`), feature-builder builds or extends the player against the contract; one Studio writer at a time | kit `film-craft` §3 step 7; P1:294 |
| Review order (frozen candidate) | scripts (`shotlist.py check`, `log-diff`, gate) → QA (qa-lead: skip, every ending, control and camera restored, repeat trigger, multiplayer, streaming) ∥ performance-engineer (phone) → **film** (staging, timing, camera, emotional clarity, with sound) → **art-director** (integrated look: do VFX, light, animation and set cooperate) → sound sync check → lead readiness | P1:430-432; P2:497-500 |
| Return paths | art finds a prop unreadable → modeler or lighting fix; event timing unchanged → sound only confirms. A visual peak moves → beat list rev bump → animator, VFX and sound acknowledge and recheck. Skeleton changes → animation and VFX attachments stale | P2:503; P1:234 |
| Gap | **animator role is planned (J006)**: until it exists the lead runs a stand-in with the animator brief and `rig-pipeline` (same pattern as the modeler stand-in, kit J005-D2) | kit `.agents/roles/README.md:14` |

## 2. Character or creature (player character, NPC, pet, boss; variant mode for skins)
| Item | Value | Evidence |
| --- | --- | --- |
| Job lead | **art-director** (identity and look carry most risk); game-designer co-owns the role and gameplay read | P2:47 (Illaoi: design, narrative, concept, animation explore together); R00:5393-5423 (mechanics and art must imply the same theme) |
| Direction leads | game-designer (what it does, its gameplay role, signature action, constraints: camera, numbers) · art-director (2-3 visual directions as reference images, **2-3 identity anchors**, shape language) · character-rigger + animator (motion profile and **rig-costly parts flagged with a cheap fallback**: capes, coattails, parts over joints) | R00:616-662 (constraints before concept); R01:76-112, R11:87-129, R03:908-928 (rig cost first); R12:73-81, R11:214-226 (identity anchors) |
| G1 shows | 2-3 pictured directions with anchors marked, the recommended one, the signature move, what is costly to animate | R05:170-176; R01:257-263 |
| Shared contract | the **rig sheet** (`rig-pipeline`), with the art-director's reference set (extra views, material intent answers) | kit `rig-pipeline` §3; R03:270-276, R03:834-846 |
| Proof (G2) | **blockout at player scale + proxy rig + the signature pose or move, captured at the game camera in Studio**, against the game's background; reviewed by art (silhouette, anchors) → animator (usable) → game-designer (role reads) | P2:53 (inspect one representative pose and camera); R00:1183-1199 (proxy checked in game); R03:234-238 |
| Interfaces | rig-pipeline S1-S2 before proof (motion needs → rig plan → K2), S3-S6 after G2 | kit `rig-pipeline` |
| Production order | modeler (cuts, geometry, textures) → rigger (rig + tests) → animator (clips + **timing list**) → VFX and sound for its actions key to the timing list → UI icon renders of the shipped model | kit `rig-pipeline` §5; R04:166-180 |
| Check-ins | art reviews the model at game camera on the real background before texture polish (paint-over notes); the next craft checks each hand-off (K-checks) | R03:790-806; R00:1540-1562 |
| Integrator | animator for the imported revision (rig-pipeline S7); feature-builder when it is wired into gameplay | kit `rig-pipeline` S7 |
| Review order | scripts (`model_audit.py`, `rig_audit.py`) → consumer K-checks → **art-director** (identity, silhouette, value at game camera) → **game-designer** (role reads in play) → performance (on-screen count, phone) → lead readiness | R03:198-208; R08:724-741; R00:1115-1170 |
| Return paths | motion blocked by a costume part → rig note → modeler (one exact note) · look change forced by a limit → owner with both options rendered | R00:1540-1562; kit `rig-pipeline` §1 |
| Variant mode | fixed: base rig, clips, anchors; open: costume, palette; skip S1; review adds "base still recognisable in every view" and "not a disadvantage to players" | R12:73-81, R12:390-394; R03:864-878 |

## 3. Stage (level, hub, lobby, arena, world area)
| Item | Value | Evidence |
| --- | --- | --- |
| Job lead | **environment-designer** (owns the place and integrates it) | kit `environment-designer` role |
| Decision rights | **routes, cover, sight lines, blocking surfaces: game-designer**; look: art-director; budgets: performance-engineer. Art stays inside the greybox; composition changes are asked for, not made | R02:454-460; R09:606-622, R09:596-604; extract C §6 veto table |
| Direction leads | game-designer (the stage's job, route graph, encounters, pacing, the hook) · art-director (look direction: 2-3 key-place reference images, value band) · environment-designer (built-where, landmarks, ambience idea) · performance-engineer (budget) | R09:20-28 (hook first); R00:1731-1751 (priorities agreed with design and concept) |
| G1 shows | the route graph, the first view, 2-3 pictured looks, the recommendation | P2:49 |
| Shared contract | **route graph + blueprint** (game-designer + environment-designer), the **ambience map** (environment → sound, VFX), the **kit piece list** (environment → modeler); a player-size scale reference in every space | kit `level-design`, `environment-design`; R02:502-518, R00:2017-2035 |
| Proof (G2) | a **playable greybox** in Studio: walk test and playtest captures, first view, landmark read, timing of routes; reviewed by game-designer (play) → art (composition and value in blockout) → performance | K5; R00:1757-1785; P1:256 |
| Production order | art blockout snapped to the approved greybox → kit pieces (modeler) and art production → light and atmosphere → ambience (sound) and ambient VFX; **playtests continue during art**; lighting and polish only after the space plays well | K5; R00:1781-1785; R09:668-680 |
| Check-ins | the game-designer is "embedded": the environment-designer checks placement, materials, set dressing and VFX placement with it as it works | R02:460-470; R09:596-622, R09:806-818, R09:1068-1080 |
| Integrator | environment-designer (Studio writer lease for place content) | kit `environment-designer` write scope |
| Review order | scripts (scene audit, budgets, floating parts) → **game-designer playtest** (routes, readability in play; playtest wins over art readability) → **art-director** (camera set, value ladder, rest areas next to detail) → sound / VFX ambience check → QA (collision, falls, stuck spots) → lead readiness | R02:822-836; R02:806-818, R13:749-790 (value ladder); R02:490-500 (clumped detail) |
| Return paths | art change that alters sight lines or collision → game-designer; new surface material → sound may refuse for time → environment picks another | P2:49; R02:472-480; R09:848-856 |

## 4. UI screen (HUD, menu, shop, inventory, popup, reward reveal, onboarding)
| Item | Value | Evidence |
| --- | --- | --- |
| Job lead | **ui-ux-designer** | kit `ui-ux-designer` role |
| Direction leads | game-designer (the player's decision the screen serves; for shops and odds: progression-designer + `platform-policy`) · ui-ux-designer (state list, focus map, 2-3 target reference images in the game's style book) · art-director (style cohesion) · feature-builder or architect (data and remotes available) | R00:4573-4599 (UX flow first); kit `ui-design` §3 |
| G1 shows | the decision record, the grey-box wireframe with real content, 2-3 pictured style targets, recommendation | R00:4867-4885 (function before polish) |
| Shared contract | **state map + spec** (`content/ui/<screen-id>/spec.md`): states, events, data fields, sizes for the smallest phone | P1:256; kit `ui-figma` handoff |
| Proof (G2, L only) | a clickable Figma prototype of every state at phone size; reviewed by game-designer (decision is clear) → art-director → feature-builder (buildable) | P2:238 |
| Production order | Figma build to the target image → handoff → feature-builder implements (`ui-basics`) ∥ UI sounds (sound) and UI effects from the VFX library | kit `ui-ux-designer` steps 4-7 |
| Integrator | feature-builder | kit `ui-basics` |
| Review order | gate PASS + code review (reviewer) → QA (every state, touch and gamepad, longest text) → **ui-ux** self-review against the target image → **art-director** → **game-designer** (player decision works) → lead readiness | R00:4893-4949 (motion goals); kit `ui-design/references/review.md` |
| Return paths | a state or readability failure returns to the state map or layout, not to styling | P2:238 |

## 5. Gameplay feature (a system players use: combat move, shop logic, quest, upgrade)
| Item | Value | Evidence |
| --- | --- | --- |
| Job lead | **game-designer** (owns the player behaviour and acceptance); technical lead **architect** | P1:256; P2:180-181 |
| Direction leads | game-designer (feature spec: what the player does, feels, decides; acceptance cases incl. failures) · architect (engine features, risky claims, probes, client/server placement, file owners) · progression-designer for numbers · `platform-policy` for money, odds, ads | kit `preproduction` feature spec; kit `engineering-craft`; R00:2457-2497 (ask what the request is for) |
| G1 shows | the behaviour in player words, the risky claims and how the proof will test them, scope, usage | P1:198 (no data structures for the owner) |
| Shared contract | **feature contract**: behaviours, state names, events (the hooks sound, VFX and UI attach to), tuning keys in data, acceptance checks written by the briefer | R00:4329-4349 (sounds hang on named events); kit `orchestration` §3 code briefs |
| Proof (G2) | a **playable grey-box prototype** in Studio (feature-builder, minimal) that tests the risky claim and the fun; game-designer plays it (studio-operator for multi-client) | R00:5767-5785; P1:57 (Riot prototype: proof the audience likes it) |
| Production order | architect plan → feature-builder builds (failing case first) ∥ progression tables ∥ UI, VFX, sound against the event names; qa-lead writes protected acceptance tests | kit `engineering-craft`, `testing` |
| Integrator | feature-builder | kit role |
| Review order | gate PASS → reviewer (harm order) ∥ qa-lead (trace table, planted faults) ∥ performance-engineer (if heavy) → **game-designer** design validation in play → **art-director** for visible parts → lead readiness | kit `code-review`; P2:239 |
| Return paths | wrong incentives → game-designer / progression; wrong behaviour → feature-builder; a fourth review round on one approach → reconsider with the architect | P2:239; kit `anti-overengineering.md` rule 20 |

## 6. Effect (a hit, slash, explosion, pickup, reveal, telegraph, aura; with its sound)
| Item | Value | Evidence |
| --- | --- | --- |
| Job lead | **vfx-designer** | kit `vfx-designer` role |
| Direction leads | game-designer (the gameplay event, its timing window, what must stay readable) · vfx-designer (frame script, importance, technique) · sound-designer (the sound's job: cue, feedback or emotion) · art-director only when the effect sets a new look | R00:4059-4105 (three jobs of sound); R06:30-33; kit `vfx-design` |
| Shared contract | **one event timeline** (anticipation, hit, tail with times in seconds and the source frame) shared by the animator's timing list, the VFX frame script and the sound cue card, same event ids | kit `rig-pipeline` §5; R04:950-958; R06:204-210; R07:273-275 |
| Cooperation | **VFX and sound co-design the envelope** (wind-up, peak, decay) before either builds; gameplay length comes from design, the animator sets beats inside it, VFX follows staggered, sound keys to picture events | P1:169; R04:166-174; R07:211-215; R00:2965-2971 |
| Proof | one capture of the effect with temp sound at the game camera, in a busy scene; for an M job shown at G3 | R06:65-68 (judge in game, not the editor) |
| Integrator | feature-builder or quick-builder wires the spec; studio-operator records the capture | kit `vfx-designer` (never writes code) |
| Review order | scripts (budget numbers, flash safety) → **game-designer** (does it hide information players need? one-hex rule analogue) → **art-director** (brightest point where the eye must go; pure white and black saved; value ladder) → sound sync on the capture → lead readiness | R06:49-80, R06:131-174; R02:806-818 |
| Return paths | timing change → animator timing list rev → VFX and sound recheck | R04:178-180 |

## 7. Marketing art (icon, thumbnails, key art and its family)
| Item | Value | Evidence |
| --- | --- | --- |
| Job lead | **marketing** | kit `marketing` role |
| Direction leads | marketing (the hook and the brief's strategy: what is the hero of the image) · game-designer (the promise: art shows what play really gives) · art-director (style, identity anchors) · trend-scout optional (what competitors look like now) | R05:55-61, R05:160-164; kit `preproduction` promise review |
| G1 shows | **3-5 rough thumbnails** at the real slot size, the preferred one stated | R05:144-176; R08:292-294, R08:554-566 |
| Proof (G2 = green light) | the chosen thumbnail with value and light set, tested at real size (`thumb_check.py`) and in the real layout; **after green light the big shapes do not move** | R08:656-712; R05:483-487 |
| Production order | render → polish → **layered file** (foreground / midground / background) → the family of crops planned at the start | R05:732-797, R05:868-872 |
| Review order | scripts (`thumb_check.py`, `look_check.py` value) → **art-director** (identity read largest, silhouette, style rules) → game-designer (truthful to play) → lead readiness | R08:724-741; R01:648-656; kit `marketing` role |
| Return paths | a wrong face or identity draws the first note every time: fix it before the review | R08:820-838 |

---

## Cross-type rules the transcripts add (all types)
| Rule | Evidence |
| --- | --- |
| One written target experience shared by design, art and engineering before craft work; name the type of fun, not "fun" | R00:5213-5308; R00:5417-5423 (Shen: tank to design, assassin to art) |
| Constraint owners state limits before design (rig, sound time, tech, budget) | R01:94-99; R04:184-190; R06:36-37; R02:472-480 |
| Show work early and rough; ask one question tied to the goal, never "do you like it?" | R00:860-884; R08:554-566 |
| Take a note for its problem, not its suggested fix | R00:2175-2201 |
| Close doors: a decided question stays decided (the decision log) | R00:840-858 |
| Judge at the real camera, size and context, never in the editor or a beauty shot | R01:271-275; R03:198-208; R06:65-68; R04:384-386; R07:587-590 |
| Reuse shared libraries (VFX texture library, sound library, kit pieces) before making new | R06:41-44; R07:113-118 |
| A craft may diverge from a reference for readability or budget, and says so up front | R06:36-37; R04:704-708 |
| Consensus is not the goal; judge against the target, not majority taste | R00:1036-1056 |
| Riot shows no named sign-off chain or round counts: the gates above are this studio's design (both papers' proposal), not copied Riot practice | extract A §5, E §C7 |
