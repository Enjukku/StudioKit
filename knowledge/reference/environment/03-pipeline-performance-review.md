---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J008-T03, Environment_Designer_Research_2026.txt lines 435-1469
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Environment paper part 3: workflow and kits, Blender-Studio hybrid, performance budgets, review, process, defects, limits (lines 435-762)

Paraphrased notes. The paper (EP) stays outside git. Every row cites `EP:<line>`. Nothing here is fact-checked: the claims are the paper's, listed in section 10 for the fact-check pass. Source IDs resolve in [[reference/environment/00-source-register]]. Research date of the paper: 2026-10-21.

**Paper limit that governs every row (EP:15, restated EP:587, 745, 761):** no stage was built, imported, rendered, heard, play-tested or benchmarked for the paper. API procedures are plans, not tested code. Every check in sections 7 and 8 is a proposal, not a result. A screenshot can show a composition defect but not that sound works or that a route feels comfortable; position data can show a missing source but not mix quality.

## 0. How to read

| Key | Meaning |
| --- | --- |
| EP:n | Line n of `Environment_Designer_Research_2026.txt`. One paragraph or one table row = one line. Source register = EP:763-1469. |
| Tag | The paper's tag. VERIFIED = an official specification or measured result (for Roblox pages: only what the page states; "recommended starting value" is not a limit). EXPERIENCE = a studio or practitioner account. OPINION = the paper's proposal, interpretation or acceptance rule. UNKNOWN = the paper says no source gives the value; it must never become a fact. |
| [O] / [V] | Inside a row with two tags, [O] marks a clause that is OPINION; unmarked clauses carry the row's first tag. |
| Src | Paper source ID. E00 = the paper's own proposal, not an outside source. "acc" = living page, accessed 2026-10-21 (an access date is not a publication date, EP:11). |
| Stage | Which of the paper's 15 process steps (ST01-ST15, section 5) the lesson serves. The mapping of sections 11-14 rows to steps is mine, not the paper's. "all" = every step. |
| Row IDs | W workflow/kits (sec 11), H hybrid (sec 12), PF performance fact, BT budget-table row, RV review lesson (sec 14), ST process step, DF defect, DN do-not, OQ open question, AX ambience exclusion, ES evidence-summary row, RA/RC/RS/MP/RJ/RP review and audit checks, BW built-where/import decision, N number, CP/CB/CM/CA claims (performance, Blender, Studio MCP, audio), X contradiction/limit. |

## 1. Section 11: production workflow and reusable kits (EP:435-471)

| ID | EP | Lesson | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- |
| W01 | 439 | The workflow is a proposal, not a claim that all studios use the same gates; a tiny prop needs no formal review meeting. Purpose: stop costly detail work from burying unsolved spatial or technical problems. Count: the paper names eight passes (my count), W02-W09. | OPINION | E00 | all |
| W02 | 441 | Pass 1, brief and layout intake. Collect: the approved route graph and what the player does along it, the camera, target devices, art-bible version, theme, how mood progresses and how many players are expected at once. List which landmarks are mandatory and which stage states can change. Raise a question only when the answer affects a hard-to-undo build choice; otherwise log the assumption and keep the blockout easy to change. | OPINION | E00 | ST01 |
| W03 | 443 | Pass 2, blockout. Simple geometry for navigable volumes, height changes, thresholds, destination relationships. Prove traversal and camera before decoration. A top-down map is not enough: the eye-level route can fail on a clean plan. Capture real approach views and the interaction states. | OPINION | E00 | ST04 |
| W04 | 445 | Pass 3, target slice. Pick one representative section that combines art, movement, light, ambience and performance in the hardest way. It should surface the pipeline's risks rather than flatter it with the easiest asset. Calibrate scale and material response there, and find the least visual treatment that still works on the lowest supported tier. | OPINION | E00 | ST05 |
| W05 | 447 | Pass 4, kit and primary art. Build reusable structural families and the largest organic forms; set silhouette layers and material zones. Keep gameplay placeholders and collision references until replacements have equal validated behavior. Keep the blockout evidence even when the art looks finished. | OPINION | E00 | ST06, ST07 |
| W06 | 449 | Pass 5, lighting and atmosphere. Set global direction and local emphasis with the character and gameplay effects in the scene. Record baseline settings and where any adopted tutorial values came from. Look at the intended mood and also at what the scene shows when an effect that depends on quality level is missing. | OPINION | E00 | ST08 |
| W07 | 451 | Pass 6, ambience. Build the approved zone map, source placement, state changes, hand-offs. Test: approach, crossing, retreat, standing still, teleport, respawn, streaming in and out. Sound designer gives the listening judgment; the environment designer checks spatial cause and that the map is correct. | OPINION | E00 | ST09 |
| W08 | 453 | Pass 7, set dressing and polish. Add secondary story and ecology detail only where the composition supports it. Test repetition, contact, camera interference, spread of quiet space. Remove detail that costs attention or performance without helping the intended reading. | OPINION | E00 | ST10 |
| W09 | 455 | Pass 8, integrated review. Walk the approved route again with the regular UI, characters, multiplayer load, abilities and ambient effects running; collect visual and audio evidence and a performance trace. If a change was made to fit a budget, rerun the clarity and ambience checks it can affect; optimization has artistic side effects. | OPINION | E00 | ST12, ST13 |
| W10 | 459 | Kit contract, one per kit family. Fields: semantic role, size, attachment rules, pivot, allowed transforms, material resources, collision form, source file, export preset, imported asset reference, variation policy. Add examples of valid and of prohibited joins. A kit that only looks right in its author's own layout is not yet robust. | OPINION | E00 | ST06 |
| W11 | 461 | The grid is a project convention, not a universal number. Structural modules meet at compatible boundaries; organic dressing may break the visible grid but keeps predictable attachment anchors. If the game allows destruction or rearranging, construction seams and unsupported interiors can show: review those states too. | OPINION | E00 | ST06 |
| W12 | 465 | Change control: log the reason for each change and the contracts it touches. Review scope follows the changed dependency, not the file type. Examples: a texture fix may need a style comparison; moving a large rock may need sightline, collision and audio-occlusion retests; a "cosmetic" lighting edit can alter route visibility; a large source-file reorganization may change nothing at runtime if the exported scene is the same. | OPINION | E00 | ST15 |

## 2. Section 12: Blender and Roblox Studio hybrid workflow (EP:473-532)

Table EP:481-489 (what to build where) is in section 8 as BW01-BW08; export and import rules are BW rows too.

| ID | EP | Lesson | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- |
| H01 | 477 | Pick the authoring surface by task. Blender: mesh shape, sculpted organic form, UV layout, baked surface detail, building a reusable asset. Studio: Roblox-specific appearance, terrain integration, collision behavior, audio placement, streaming, gameplay context. Keep these duties explicit; do not assume one app owns the whole environment. The paper says these are proposed choices, not claims that an app cannot do other things. | OPINION | E00 | ST03 |
| H02 | 479 | Blender 5.2.2 LTS, released 2026-09-15, is the latest stable LTS the paper verified. [O] Pin the version used by production automation and record changes before regenerating assets; a newer development build is not automatically the right target. | VERIFIED; [O] | B01, E00 | ST03 |
| H03 | 491 | Footnote to the built-where table: every row is a proposed choice (OPINION E00). What the importer supports is documented in B05; runtime limits are covered in the platform sections. | OPINION | E00, B05 | ST03 |
| H04 | 495 | Treat the .blend file as structured production data. Keep stable meaningful names and split export from non-export collections; store the source meshes, material assignments, planned pivots and calibration objects; and generate a manifest before anything is exported. Do not write automation that locates its target only by what is selected or by a vague default name. | OPINION | E00 | ST03, ST11 |
| H05 | 497 | Blender's mesh API separates vertices, edges, loops, polygons; BMesh can tessellate quads and n-gons into triangles. Mesh.validate can fix or remove invalid geometry, so it is not purely observational: inspect a copy when the review must not change the source, and keep the original before cleanup. | VERIFIED | B08, B11 | ST11 |
| H06 | 499 | Proposed build recipe, in order: find the intended collection; make or reuse canonical mesh data; apply transforms and materials from the manifest; evaluate the geometry for inspection; compute dimensions and triangulated counts; render the approved cameras; compare results; export just the intended content. Where a modifier or instance alters geometry, count what comes out, not the raw source mesh. The exact API for reading evaluated meshes must be confirmed on the installed Blender version before use. | OPINION | E00 | ST03, ST11 |
| H07 | 501 | Use fixed placement inputs when a scene is generated repeatedly: record seed, asset set, placement exclusions and source revision. Changing the seed produces a different scene candidate; it is not a neutral rebuild. Fixed inputs do not make a scene good; they make a defect repeatable, so the art director can compare a true before and after. | OPINION | E00 | ST07, ST10 |
| H08 | 513 | Blender MCP contract. Find the installed provider, its tool schema and version before any operation. Check Blender version and current file identity; use that provider's supported Python execution or equivalent. Limit edits to named collections and bounded tasks; read back the manifest and render through the supported interface; verify returned artifact paths and contents. Do not assume Studio MCP tool names exist in Blender. The paper established no canonical Blender MCP provider or version and made no connection: this is a contract, not a tested transport. | OPINION; provider UNKNOWN | E00 | ST03 |
| H09 | 517 | Studio MCP, as the docs describe it: a tool `list_roblox_studios` to find instances; every call must carry `studio_id`. Listed tools: `get_studio_state`, `start_stop_play`, `screen_capture`, `execute_luau`, `inspect_instance`, `search_game_tree`. `execute_luau` runs in a chosen Edit, Client or Server context; `screen_capture` can be aimed with a custom camera position and target point. The docs describe capabilities; the paper never connected to a live Studio session. | VERIFIED | B03 | ST03, ST11 |
| H10 | 519 | Proposed observe-change-verify transaction: resolve the intended place; inspect state; read relevant instances and properties; write a bounded change plan; apply the authorized edit; read back; capture the view. Do not blindly repeat a command after an uncertain result: running the same stage build twice can duplicate hidden sources, lights or geometry while screenshots still look alike. | OPINION | E00 | ST11 |
| H11 | 521 | Read-only scene reports should cover what the task needs from: lighting properties, audio anchors, collision flags, resource references, dimensions, transform, parent, type and instance identity. Report unknown or inaccessible fields; never substitute a default. Screenshot and scene report complement each other (presentation vs structure). | OPINION | E00 | ST11 |

## 3. Section 13: environment performance and measured stage budgets (EP:534-608)

Rows PF are the paper's source-based paragraphs. Budget table = BT. The 7-step measurement method (EP:575-587) and the stress test (EP:589) are in section 7 as MP01-MP08.

| ID | EP | Lesson | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- |
| PF01 | 536 | Instance streaming loads and unloads Workspace content. Roblox recommends these starting values: StreamingMinRadius 64 and StreamingTargetRadius 1024 studs, Target larger than Min, stream-out mode Opportunistic, integrity mode PauseOutsideLoadedArea. They are starting settings, not guaranteed load or memory limits. Loaded content may remain beyond Target when memory allows; raising Min costs memory and bandwidth. [O] Audit scene assets by what a client must hold at a given route and camera, not by total saved-place count. | VERIFIED; [O] | P16 acc | ST12 |
| PF02 | 538 | Frustum streaming is opt-in, adds camera-view loading on top of normal streaming, and is set server-side per player. It does not replace ordinary streaming and does not stop replication of instances hidden behind walls. It can cost client memory and CPU, and its reach is set by draw distance and an engine-wide cap. Automatic mode responds to narrow FOV, movement and far-away cameras; quick camera turns can make distant instances load and unload repeatedly. Content kept only by Opportunistic frustum streaming stays 1.5 seconds after it leaves the eligible area. [O] Turn it on for a shown distant-view need, not as a general speed-up. | VERIFIED; [O] | P17 acc | ST12 |
| PF03 | 540 | SLIM makes lightweight composite model stand-ins with LoDs, which may keep rendering after the full instances stream out. Needs: streaming, a place saved to Roblox, Team Create; set Model.LevelOfDetail to SLIM. Suits static world models; runtime geometry or property changes and animations are excluded from static-model SLIM. Studio and Developer Console debug tints show transcoding and LoD state. A local-only place does not prove cloud transcoding. [O] Keep moving foliage, doors and destructibles apart from static composite architecture; test both the full and the substitute view. | VERIFIED; [O] | P18 acc | ST05, ST12 |
| PF04 | 542 | With MeshStreamingAndImprovedLoDs on, per-MeshPart RenderFidelity is ignored and the improved cloud transcoder and mesh streaming apply. The announcement (2026-04-27) described a phased rollout and later removal of the property. [O] Check supported properties and rollout state in the Studio build and client under test; do not assume a planned July switch or the removal has happened; old fixed-distance RenderFidelity recipes are not authoritative on this path. | VERIFIED; [O] | P19 2026-04-27 | ST12 |
| PF05 | 544 | Texture streaming picks resident detail on the fly. 4096x4096 rendering is offered only for supported instance types; it is not a given for each asset on each device. P27's status table lists 4K as disabled on low-end Android under 3.5 GB. Atlases are advised only when the textures are normally seen together on batchable parts; otherwise requesting one atlas region loads the mip of the whole atlas. [O] Keep shared kits; avoid giant atlases that mix unrelated stages. | VERIFIED; [O] | P27 status 2026-03-23; P30 2026-01-30 | ST06, ST12 |
| PF06 | 548 | Mesh instancing needs shared MeshContent plus matching SurfaceAppearance, or matching TextureContent, or (when neither exists) matching material. Re-importing identical geometry under other asset IDs can lose the gain. Anchor static objects. Use simpler collision geometry where interaction needs no detail; turn off CanCollide/CanTouch/CanQuery only where unneeded. Transparent overlap and heavy shadow-casting density add render cost. [O] Build a deduplicated asset kit rather than re-importing the whole assembled world over and over. | VERIFIED; [O] | P21 acc | ST06, ST11 |
| PF07 | 550 | CollisionFidelity=Tunable adds a CollisionPrecision value. Staff say 0 means Hull and 1 means close-to-exact decomposition where possible; it is not a linear accuracy scale and does not promise perfect collision. Existing algorithms do not generally correspond to particular slider positions. A decomposition stays stored until someone regenerates it; some APIs outside the Properties panel support only the default precision. [O] Check walkable surfaces and camera blockers in collision visualization; never infer collision from a render-mesh screenshot. | VERIFIED; [O] | P20 2026-09-17 | ST04, ST11 |
| PF08 | 554 | Preface to the budget table: the sources give no universal low-end-phone figures for parts, triangles, MB or ms. The table keeps a platform limit apart from a studio's own measured allocation. UNKNOWN means a decision that must be made, not a licence for unlimited content. | OPINION (evidence limit) | E00 | ST05, ST12 |
| PF09 | 569 | Scene Analysis is fully released (2026-07-10). Its views: instance, script-memory, unparented-instance, audio-memory, animation-memory, triangle composition. Triangle composition separates shadows, opaque, transparent, Terrain, grass, particles, sky, UI. The paper says SceneAnalysisService offers matching tables via MCP, named GetInstanceCompositionAsync and GetTriangleCompositionAsync. Studio statistics on a local machine do not equal phone results. Unparented instances alone do not show a leak. | VERIFIED | P23 2026-07-10; P22 acc | ST12 |
| PF10 | 571 | MicroProfiler reports task timings and frame spikes in Studio and client. Mobile capture is switched on in the client Settings and opened from a development machine on the same network at the displayed address. Real hardware is needed: emulation cannot reproduce thermal throttling, device memory or all rendering. The hardware guide advises 10-15 minutes of active mobile play to watch for thermal degradation; that is not proof that longer sessions are safe. FPS = 1000 / frame-time in ms; if the owner picks 30 or 60 FPS, the exact derived intervals are 100/3 ms and 50/3 ms, not new measured budgets. | VERIFIED | P24, P25 acc | ST12 |
| PF11 | 593 | Disagreement 1. The performance guide says shadows are off below quality level 4; the QualityLevel page warns that feature behavior is platform and device specific. [O] Treat the broad warning as the rule: test the target device and do not rely on a quality number to promise that gameplay stays visible. | VERIFIED; [O] | P21, P03 acc | ST05, ST12 |
| PF12 | 595 | Disagreement 2. The performance guide advises Automatic or Performance for RenderFidelity, while the 2026 mesh-streaming post says the setting has no effect once the new path is enabled. They apply to different active paths: find out which path is active before optimizing. | VERIFIED | P21, P19 | ST12 |
| PF13 | 597 | Disagreement 3. P27's broad table (2026-03-23) shows low-end iOS supported; a later staff diagnosis (2026-07-10) says a 3 GB iPad gets reduced resolution and ties full 4K to about 3.5 GB or more. Being supported by streaming does not show that 4K stays resident. Test the exact device class and do not claim 4K for all iPads. | VERIFIED | P27, P29 | ST12 |
| PF14 | 599 | Disagreement 4. Staff (2026-09-04) traced widespread stuck-at-lowest-LoD meshes to another feature that interacted with it, and said that feature was rolled back. A scoped platform incident, not proof that all mesh streaming is broken. [O] When several unchanged scenes regress, keep traces, build and client details and look for engine changes before rebuilding authored assets. | VERIFIED; [O] | P31 2026-09-04 | ST13 |
| PF15 | 601 | Not a conflict. Renderer occlusion culling and frustum streaming do different jobs: the renderer may skip hidden draw calls while the frustum streamer still counts hidden instances for replication. | VERIFIED | P17, P21 | ST12 |

### 3.1 Stage budget table (EP:556-565)

Column "Budget for low-end phones" as the paper words it. UNKNOWN = no source gives a transferable value.

| ID | EP | Item | Budget for low-end phones | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| BT01 | 557 | Whole-stage visible triangles, draw calls, resident parts/instances | UNKNOWN. Measure for each route and camera, device, and streaming state | OPINION (measurement requirement) | P22, P25 acc |
| BT02 | 558 | Single imported general mesh | Ceiling documented at 20,000 triangles; neither an asset goal nor a sum for the stage | VERIFIED | P26 acc |
| BT03 | 559 | Instance streaming starting radii | Min 64 studs, Target 1024 studs; these do not cap memory | VERIFIED | P16 acc |
| BT04 | 560 | Terrain | 4x4x4-stud cell representation; safe rendered/occupied volume UNKNOWN | VERIFIED (representation); OPINION (withholding a budget) | P15 |
| BT05 | 561 | Per-emitter particle rate | Mobile ceiling 100 per second; a total that is safe for the stage is UNKNOWN | VERIFIED (ceiling) | P13 acc |
| BT06 | 562 | Local lights / shadow casters / transparent layers | UNKNOWN; varies with overlap, camera and quality level | OPINION | P03, P21 acc |
| BT07 | 563 | Texture residency / geometry memory / total client memory | UNKNOWN and device-specific; being able to use 4K is not an allocation | OPINION | P27 2026-03-23; P25 acc |
| BT08 | 564 | Ambient sounds and animated props | UNKNOWN; who owns audio and its memory must be counted inside the whole gameplay load | OPINION | P22, P25 acc |
| BT09 | 565 | Frame-time acceptance | The studio sets its own target; a chosen FPS must not be called an official minimum for everyone | OPINION | P24 acc |

## 4. Section 14: reviewing the environment (EP:610-677)

The capture rules, the 15-row check table, the seven sound passes and the camera set are in section 7 (RA, RC, RS). Rows below are the remaining lessons.

| ID | EP | Lesson | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- |
| RV01 | 614-618 | Pointer: capture metadata (RA01), camera categories (RA02) and the UNVERIFIED rule (RA03) are in section 7. | OPINION | E00 | ST12, ST14 |
| RV02 | 639 | Data checks are narrower than experience checks. A collision query can point at a probable placement fault, yet it cannot say whether an overlap was intended. A color histogram can show that the palette shifted, not what role those colors play in the story. A screen-space projection can show that a landmark is small, not that players miss it. Use them as diagnostics that focus the review, never as replacements for it. | OPINION | E00 | ST11, ST12 |
| RV03 | 641 | Ambient audio: check where each source lives, its transform, distance rules, zone state, graph links and streaming life cycle; then get a real listening review. If the tool cannot capture or judge audio, return "auditory acceptance pending", not an inferred pleasing mix. The missing modality must stay visible in the report. | OPINION | E00 | ST12, ST14 |
| RV04 | 645 | Feedback record, per issue: ID, severity, scene and state, camera or source, what was observed, the intended reading, likely cause, proposed change, what must be preserved, responsible craft, retest evidence, and an owner decision when needed. Keep observed fact apart from hypothesis. "The waterfall emitter is missing from the loaded zone" can be shown with structure; "the waterfall is emotionally weak" needs a defined target and a listening judgment. | OPINION | E00 | ST13, ST14 |
| RV05 | 647 | Priority: gameplay failure, wrong source behavior, performance failure and major style drift come before cosmetic polish. The order can change with release goals, but the reason must be recorded. Do not bury a blocked doorway under a long list of small material tweaks. | OPINION | E00 | ST13 |
| RV06 | 651 | AudioAnalyzer reports PeakLevel and RmsLevel. The server does no audio processing, so run analysis on the client. Spectrum processing can be turned off when only levels are wanted. [O] These levels are not LUFS, not sound-pressure readings and not a judgment that a sound is convincing. | VERIFIED; [O] | A14 acc | ST12 |
| RV07 | 653 | Wire.Connected marks an active, valid connection, including valid source/target pins and no cycle. [O] It does not certify the full listening experience. | VERIFIED; [O] | A15 acc | ST11, ST12 |
| RV08 | 655 | The seven-pass sound review (EP:657-669) is the paper's pass/fail review contract; see RS01-RS07. Images plus position data can confirm where things are, but not tone, masking, loop joins, harshness, realism or how smooth it feels. | OPINION | E00 | ST12 |

## 5. Section 15: the process, defects, don'ts, open questions (EP:679-761)

### 5.1 The 15-step process (EP:683-711). All steps: OPINION, E00.

| ID | EP | Step | Stage links |
| --- | --- | --- | --- |
| ST01 | 683 | Gather the route graph, the interactions, the camera, the player's collision envelope, the target phones and the art-bible version. Flag open decisions and keep early work reversible. | W02 |
| ST02 | 685 | Annotate each key-place reference image as a spatial target: skyline, focal point, traversal, materials, light sources, ambient life, and any unclear geometry. Ask for a ruling where an image clashes with gameplay. | DN01 |
| ST03 | 687 | Set scale and a calibration fixture in the apps used. Record unit convention, pivots, axes, import options. Prove one asset round trip before bulk construction. | H01-H11, BW |
| ST04 | 689 | Build the blockout and test route, collision and camera on it. Capture the real approach views as well as the top-down plan, and keep the approved route dimensions visible while art takes over. | W03 |
| ST05 | 691 | Choose a representative target slice; prove the visual style at supported graphics tiers with character, UI and gameplay effects present. Art director reviews; the owner decides on consequential direction changes. | W04 |
| ST06 | 693 | Design the modular kit and the main natural forms. Record valid joins, asset resources, variation rules, collision form and who owns which part of the scene. | W10, W11 |
| ST07 | 695 | Assemble primary art while keeping the route contract. Validate contact, silhouette layers and camera corridors before secondary detail. | W05 |
| ST08 | 697 | Set lighting and atmosphere from a recorded baseline. Copied tutorial values are experiments: check how scene-dependent they are. Test both mood and critical readability. | W06 |
| ST09 | 699 | Write the ambience map and the source contracts: what is heard, what moves, where each source sits, what states alter them and how transitions behave. Sound and VFX specialists make their own assets and implementation details. | W07 |
| ST10 | 701 | Add ambient life and set dressing selectively. Protect quiet gameplay space, source visibility and focal hierarchy. Review repeated patterns while moving. | W08 |
| ST11 | 703 | Inspect the scene data and write the manifest. Check imported dimensions, pivots, collision, materials, source graphs and approved exclusions. | RP05-RP07 |
| ST12 | 705 | Walk the integrated route with streaming and ordinary gameplay activity on. Collect visual, audio and performance evidence on representative devices. Never present an emulator or editor result as a phone benchmark. | W09, MP |
| ST13 | 707 | Triage failures by cause and craft owner. Retest every contract the repair touches, especially when optimizing removed visual or audio information. | W09, RV04 |
| ST14 | 709 | Submit the review packet listing open issues, exceptions and evidence. The owner decides if the stage meets the creative and product goal; the agent must not hide uncertainty to win approval. | RA, RC |
| ST15 | 711 | Keep the approved revision and its test states. For later changes, repeat the affected route, source and budget checks instead of assuming a small edit is harmless. | W12 |

### 5.2 Common AI-built defects and cause-oriented repair (EP:713-723). All OPINION, E00.

| ID | EP | Defect | Cause the paper names | Repair it proposes |
| --- | --- | --- | --- | --- |
| DF01 | 715 | Flat lighting; stage with no focal point | No deliberate hierarchy, not simply too little brightness | Compare the target focal region with competing surfaces; adjust that light/material relationship instead of adding lights everywhere. If there is no focal point, the fix may be a bolder large form or a clearer line of sight, not a brighter small prop. |
| DF02 | 717 | Clutter | Treating every free surface as a place to put something | Reapply the route and attention exclusions; remove low-value clusters. Empty space can be intended; when it is not, add a meaningful structural or story relationship, not uniform scatter. |
| DF03 | 719 | Wrong scale | An unverified conversion, or an asset made without the player reference | Fix the source of the mismatch before resizing single objects. Floating props: validate contact. Visible repetition: review composition with a moving camera. Weak terrain joins: check silhouette and collision from both sides. |
| DF04 | 721 | Silent or same-sounding zones; abrupt sound changes; sound not matching picture | No ambience map, or one global loop used everywhere | Work with the sound designer to add layers that belong to each place and have a visible cause, plus transition logic. For sudden changes also check streaming, source parenting and duplicate playback. A sound that disagrees with the picture can be a state-coordination fault, not a bad asset. |
| DF05 | 723 | Excessive stage cost | Not traced to actual resources and work; instance count alone cannot tell a marker from an expensive dynamic system | Reduce the measured bottleneck while keeping the scene's essential information. If the scene only passes with ambience or effects off, the integrated stage has not passed. |

### 5.3 Do-not list (EP:725-745)

| ID | EP | Do not | Tag | Src |
| --- | --- | --- | --- | --- |
| DN01 | 727 | Accept a beautiful reference image as proof of the intended route; the route belongs to the game-design contract. | OPINION | E00 |
| DN02 | 729 | Call any universal door size, fog density, sound range or stage count researched without a source that gives that exact value for that scope. | OPINION | E00 |
| DN03 | 731 | Mix export-scale recipes that conflict; record and measure the full chain. | VERIFIED; [O] | B04, B05 |
| DN04 | 733 | Assume a linked Blender object guarantees runtime instancing after import. | VERIFIED; [O] | B07 |
| DN05 | 735 | Treat a successful MCP command as proof that the right Studio instance or data model was changed. | VERIFIED; [O] | B03 |
| DN06 | 737 | Run validation that modifies data on the only copy of the source when the job is only to inspect. | VERIFIED; [O] | B08 |
| DN07 | 739 | Use gameplay-critical sound as the only cue when muted play is supported. | OPINION | E00 |
| DN08 | 741 | Let the environment designer quietly take over craft decisions that belong to the sound, VFX, rigging or gameplay specialist. | OPINION | E00 |
| DN09 | 743 | Swap low-tier captures and phone traces for a high-quality editor beauty shot. | OPINION | E00 |
| DN10 | 745 | Present proposed checks as tests that were completed, or call a mix that nobody reviewed accepted sound design. | OPINION | E00 |

### 5.4 Open questions and ambience exclusions (EP:747-755)

| ID | EP | Item | Tag | Src |
| --- | --- | --- | --- | --- |
| OQ01 | 749 | Unresolved, project-dependent numbers: the geometry and instance load a stage can safely show; texture residency; allocation of lights and shadows; number of concurrent ambient sources; cost of acoustic simulation; particle overdraw; transition length; source gain and range; and the least visual separation the real camera and audience need. Next evidence: run the approved target slice on named devices, recording settings and using typical gameplay. | UNKNOWN (the numbers); OPINION (next step) | E00 |
| OQ02 | 751 | No public source sets out a single premium Roblox environment preset, or a complete numeric art bible for any studio named. Some sources give goals and production choices, not measured performance: keep that difference when turning the paper into agent instructions. A project may fill an UNKNOWN field with a labeled project value plus its test result, but must never claim afterwards that the literature supplied it. | OPINION; UNKNOWN | E00 |
| AX01 | 755 | Do not treat every biome as the same loop with another name. | OPINION | E00 |
| AX02 | 755 | Do not mask a mandatory gameplay cue with decorative water. | OPINION | E00 |
| AX03 | 755 | Do not assume the tallest point is always the windiest. | OPINION | E00 |
| AX04 | 755 | Do not make every small prop audible. | OPINION | E00 |
| AX05 | 755 | Do not switch the whole mix abruptly at a zone boundary. | OPINION | E00 |
| AX06 | 755 | Do not promise that rich acoustic simulation will run all the time on a low-end phone. | OPINION | E00 |
| AX07 | 755 | Do not infer audible quality from a valid Wire. | OPINION | E00 |
| AX08 | 755 | Do not declare an unlistened mix approved. | OPINION | E00 |
| AX09 | 755 | Numeric source ranges and gains, fade durations, exact per-phone concurrency and measured effect costs stay unresolved until the real game and assets are tested. This is a deliberate evidence limit and not permission to invent numbers. | UNKNOWN | E00 |

## 6. Section evidence summary tables (the paper's own, every row of its five tables)

Columns follow the paper: rule / number / mark / source and date. Included so each paper claim can be traced.

| ID | EP | Rule | Number | Mark | Src, date |
| --- | --- | --- | --- | --- | --- |
| ES01 | 470 | Keep layout intent that was tested | No universal length for a phase | EXPERIENCE; the implementation is OPINION | C01 2020-11-16; E00 2026-10-21 |
| ES02 | 471 | Keep a kit contract and its revision history | Measure dimensions; do not guess a grid | OPINION | E00 2026-10-21 |
| ES03 | 530 | Pin a Blender build that exists | 5.2.2 LTS, 2026-09-15 | VERIFIED | B01 (dates in the register) |
| ES04 | 531 | Check units, pivots and hierarchy on import | One calibration kit first, then the bulk transfer | OPINION | E00 2026-10-21; B04/B05 |
| ES05 | 532 | State each Studio MCP operation's target explicitly | studio_id; Edit, Client or Server context for execution | VERIFIED | B03 acc |
| ES06 | 604 | Profile what the client really does, not place totals | No universal cap for a stage | OPINION | P22/P25 acc |
| ES07 | 605 | Use the fully released tool, not beta-era instructions | Released 2026-07-10 | VERIFIED | P23 |
| ES08 | 606 | Extra camera streaming raises resource demand | Opportunistic content stays 1.5 s | VERIFIED | P17 acc |
| ES09 | 607 | Tunable precision is only qualitative | 0 is Hull; 1 is near-exact where possible | VERIFIED | P20 2026-09-17 |
| ES10 | 608 | Test edges and revisits before sign-off | Temporary Target of 64 | VERIFIED | P28 acc |
| ES11 | 672 | Pick the modern spatial query that tells boxes from the real occupied shape | No universal polling rate for zones | VERIFIED (API); OPINION (scheduling) | A12 acc |
| ES12 | 673 | A persistent ambient source must survive stream-out or be rebuilt | Measured per project; no universal radius | VERIFIED (behavior); OPINION (contract) | A13/A05 acc |
| ES13 | 674 | A particle-rate ceiling is not a goal | 100 per second per emitter on mobile; lifetime cap 20 seconds | VERIFIED | A16 acc |
| ES14 | 675 | Check AudioAnalyzer on a client | Zero output on the server | VERIFIED | A14 acc |
| ES15 | 676 | Phone source budget, waterfall gain, crossfade duration, cave decay | UNKNOWN | OPINION: demand measured or authored project values | No primary numeric value found that transfers |
| ES16 | 677 | A screenshot-only review cannot approve what a soundscape sounds like | Listening evidence is required | OPINION (review rule) | This paper, 2026-10-21 |
| ES17 | 760 | Deliver spatial, visual, audio and performance proof | The proposed 15-step process | OPINION | E00 2026-10-21 |
| ES18 | 761 | Tests that are unknown or not performed cannot pass | No benchmark and no listening test were done for the paper | OPINION (reporting rule) | E00 2026-10-21 |

## 7. Review and audit checks proposed by the paper

All are proposals (OPINION E00 unless a Src says otherwise); none was run (EP:587, 745, 761). "Evidence needed" is what the review packet must hold for the check to count. The paper gives no numeric pass thresholds for any of them: thresholds come from the approved contract or from a measured project limit. Without that contract or measurement the result is UNVERIFIED, never PASS (RA03).

### 7.1 Capture rules and camera set

| ID | EP | Check | Evidence needed |
| --- | --- | --- | --- |
| RA01 | 614 | Each capture records the scene revision, camera, viewport, graphics setting, time and weather, avatar state, UI state and any relevant effects, plus the route or inputs needed to reproduce it. A chosen beauty camera helps presentation but never replaces real player views. | Capture metadata block per image/clip; reproduction input sequence |
| RA02 | 616 | Camera categories, picked by the stage's risks: player-eye approach, decision-point, reverse-route, high overview, top-down layout, contact/clearance close-up, skyline, stress-scene. Categories, not a required count; a tiny arena and a multi-level stage need different coverage. | One named camera per risk, with transform/FOV |
| RA03 | 618 | Pass/fail holds only against an approved contract. Missing contract or missing measurement gives UNVERIFIED, not PASS. | The approved contract or measurement, cited per check |

### 7.2 The 15 proposed review checks (EP:620-635)

| ID | EP | Check | Test and pass condition (paper's idea) | Evidence needed |
| --- | --- | --- | --- | --- |
| RC01 | 621 | Route guidance | At every approved decision point the intended next action is recognizable; conflicting cues are fixed | Approach, decision and departure views from the player's side; playtest notes |
| RC02 | 622 | Focal hierarchy | The required landmark stays visible and distinguishable in the approved target comparison | Real gameplay camera with normal UI and effects |
| RC03 | 623 | Scale and passage | The measured opening and the collision envelope meet the approved traversal requirements | Eye-level passage clip, dimensions, collision view |
| RC04 | 624 | Camera clearance | The supported camera does not clip badly or force awkward framing during required movement | Clips of traversal and of turning around |
| RC05 | 625 | Lighting readability | The information needed to read the character and action survives each supported graphics state | High-tier and low-tier captures taken in matched conditions |
| RC06 | 626 | Atmosphere | Required sightlines stay usable; target depth and mood match the approved reference | Near, middle and far views in the relevant time/weather states |
| RC07 | 627 | Ambience identity | Each zone's list of sources and its listening review agree with the approved map | Zone data, a recorded walk-through, and the sound designer's review |
| RC08 | 628 | Sound and picture agreement | What is heard and what moves in the ambience have the approved cause-and-effect link | Close-up of the source, an approach clip, and the state record |
| RC09 | 629 | Transition behavior | Crossing, retreat, teleport and respawn give the approved blend without lifecycle defects | Boundary route recording, source-state logs |
| RC10 | 630 | Contact and placement | Required supported objects have valid contact; intended overlap is documented | Contact views, bounded geometry checks |
| RC11 | 631 | Repetition | Repeated resources do not make an unintended dominant pattern | Long approach, lateral sweep, overview |
| RC12 | 632 | Cohesion | Shape, palette, material and detail locks agree with the art-bible version | Comparison with the target, with characters, UI and VFX in view |
| RC13 | 633 | Runtime budget | Captured frame time, memory and counters stay inside measured project limits | Representative target-phone trace, not an editor estimate |
| RC14 | 634 | Streaming | Required cues and sources stay correct through loading and unloading | Fast traversal, reversal, teleport and stressed-client test |
| RC15 | 635 | Handoff completeness | Source revisions, asset references, settings, exceptions and owners are all recorded | Stage manifest and review packet |

### 7.3 Diagnostics and audio passes

| ID | EP | Check | Evidence needed |
| --- | --- | --- | --- |
| RA04 | 639 | Data diagnostics (collision query, palette histogram, screen-space projection) only point the review at likely problems; they never decide artistic intent or player recognition. | Diagnostic output plus a human/visual judgment |
| RA05 | 641 | Audio structure check: source paths, transforms, distance rules, zone state, graph connections, streaming lifecycle; then a real listening review. If audio cannot be captured or judged by the tool, report "auditory acceptance pending". | Source dump; recorded output; sound-capable reviewer |
| RS01 | 657 | Data pass: each planned source maps to an approved asset or anchor; every required wire is connected; listener and interaction groups were chosen on purpose; no use of a deprecated property remains unreviewed; each enabled curve is the approved revision. | Source/wire/curve inventory against the approved ambience map |
| RS02 | 659 | Coverage pass: samples along the route give the expected zone weights and the intended dominant source; no unowned gaps, no unintended triple-loud overlaps, no old-zone gain left over after respawn or teleport. Log values for both travel directions. | Per-sample zone weights and gains, both directions |
| RS03 | 661 | Causality pass: exported source IDs and visual IDs agree on active state, location and weather event. Take a close-up of the source and the matching view from the player's eyes; compare timestamped video rather than stills to check timing. | Source IDs, timestamped video pairs |
| RS04 | 663 | Streaming pass: traverse and return across streaming boundaries repeatedly; no duplicate loop instances, no missing rebuilt source, no steadily growing connection/instance counts, compared with the same stationary baseline after cleanup. | Instance/connection counts per revisit; stationary baseline |
| RS05 | 665 | Acoustic pass: test the entrance, a door or opening, a bend, a deep interior and the way back, at high and low device quality. Averages must not hide audible jumps at transitions. | Captures at both qualities along that path |
| RS06 | 667 | Performance pass: frame and memory results on the declared low-end phone, busiest source/effect overlap, gameplay active. FAIL or UNTESTED when the declared project budget has no evidence. | Phone trace with the busiest overlap |
| RS07 | 669 | Perceptual pass: a reviewer who can hear audits the captured output, or the creative director listens. Images plus position data confirm placement only, not tone, masking, loop joins, harshness, realism or smoothness. With no listening review, mark UNVERIFIED, never PASS. | Audition by a reviewer; otherwise the check stays UNVERIFIED |

### 7.4 Budget measurement steps (EP:569-589) and reject conditions

| ID | EP | Step | Evidence needed |
| --- | --- | --- | --- |
| MP01 | 575 | Freeze a representative route, camera transforms and FOV, player load, weather/time, combat/UI workload and build ID. Include spawn, densest vista, close waterfall spray, interior-to-exterior move, skyline, cave and repeated return trips. | Frozen test script + build ID |
| MP02 | 577 | Capture low-quality and high-quality visual pairs and real-device Automatic mode. Keep the loss of sky, shadow, fog, foliage and particles visible; do not hide it with a beauty angle. | Paired captures; Automatic-mode phone capture |
| MP03 | 579 | Export Scene Analysis snapshots next to screenshots; collect MicroProfiler traces and client-memory notes from the real low-end target. Find the CPU, GPU, physics, texture or streaming pressure before deleting detail. | Scene Analysis export; MicroProfiler trace; memory notes (phone) |
| MP04 | 581 | Cold-load and warmed traversal; keep playing to expose heat-related loss. Start with the documented 10-15 minute thermal check (P25), then extend to the real expected session. Acceptable tail frame times stay a project decision. | Time-stamped trace over the session on the device |
| MP05 | 583 | Change one cost-bearing category at a time while keeping camera and route; compare paired traces and silhouettes. Turn measured accepted maxima into project budgets with device, build and workload provenance, not platform-wide rules. | Before/after trace pairs; budget row with provenance |
| MP06 | 585 | Go back to earlier zones and check that counts of effects, sounds and instances return to the expected life-cycle state. Record growth that stays unexplained; one high-memory sample does not prove a leak. | Counts per revisit |
| MP07 | 587 | Apply the reject conditions RJ01-RJ05. They are proposed approval gates, not results of tests. | The route/test records for each gate |
| MP08 | 589 | Stress edges and revisits (VERIFIED P28 acc, with [O] use): Roblox recommends exercising full traversal, distant teleports and revisits, including a stress run at StreamingTargetRadius=64. [O] Treat it as a temporary compatibility stress, not as the shipped 1024 setting; normal Target stays larger than Min (the stress case does not claim equal radii are ideal). | Stress-run record at Target 64 |
| RJ01 | 587 | Reject when a route or hazard disappears. | Traversal record |
| RJ02 | 587 | Reject when a landmark becomes misleading after streaming or LoD. | Streaming/LoD views |
| RJ03 | 587 | Reject when collision blocks an approved opening. | Collision visualization |
| RJ04 | 587 | Reject when ambience fails after re-entry. | Re-entry source state/log |
| RJ05 | 587 | Reject when the chosen device targets fail. | Phone trace vs declared target |

### 7.5 Process-level checks from sections 11-12 and 15

| ID | EP | Check | Evidence needed |
| --- | --- | --- | --- |
| RP01 | 451 | Ambience states tested: approach, crossing, retreat, standing still, teleport, respawn, stream in/out. | One record per state |
| RP02 | 455 | After a budget-driven change, rerun the clarity and ambience checks it can touch. | Before/after RC and RS results |
| RP03 | 443, 689 | Blockout: real approach views and interaction states captured; approved route dimensions kept visible during art replacement. | Eye-level views; named anchors |
| RP04 | 465 | Retest scope follows the changed dependency (sightline, collision, audio occlusion, style comparison), not the file type. | Change log naming the contracts touched |
| RP05 | 509 | After import: dimensions, orientation, pivot, hierarchy, material resources, normals, collision, permission context; compare with a calibration object and a known route fixture. | Import report vs calibration object |
| RP06 | 519 | Observe-change-verify on Studio: read back after each edit, then capture the view; no blind repeat after an uncertain result. | Read-back data + capture |
| RP07 | 521 | Scene report holds the fields listed in H11; unknown fields reported as unknown. | Scene report |
| RP08 | 499 | Triangle counts and dimensions computed on the evaluated output (modifiers/instances applied), on a copy. | Count report on the evaluated mesh |
| RP09 | 459, 461 | Kit review: valid/prohibited join examples; destruction/rearrangement states if the game allows them. | Join examples; seam views |
| RP10 | 703-711 | ST11-ST15 as checks: manifest, integrated run on devices, triage with retest, review packet with exceptions, preserved approved revision. | Manifest; packet; revision tag |

## 8. Built-where and import decisions

Decision points for what to build where, the Blender to Studio round trip, pivots, instancing, collision and the scale chain. All OPINION E00 unless a Src marks VERIFIED.

### 8.1 Paper table: what to build where (EP:481-489)

| ID | EP | Element | Build where | Why | How to bring it over |
| --- | --- | --- | --- | --- | --- |
| BW01 | 482 | Sculpted cliff or hero rock | Blender, then Studio | Control over silhouette, topology, UVs and baked detail | Export a compatible mesh; then validate scale, material, pivot and collision in Studio |
| BW02 | 483 | Traversable route blockout | Studio, or a shared simple blockout | Quick iteration against the true avatar and camera | Keep named anchors and route dimensions through art replacement |
| BW03 | 484 | Reusable building kit | Blender for the mesh modules, Studio for putting them together | Keeps asset craft separate from game context | Canonical resource references, documented joins, import settings |
| BW04 | 485 | Broad voxel terrain and water | Studio Terrain | Native terrain tools and runtime behavior | Use approved height and color inputs or bounded terrain operations; check seams against meshes |
| BW05 | 486 | Lighting and atmosphere | Studio | Studio is the final renderer and handles the graphics tiers | Keep a record of scene settings; do not expect Blender lighting to import identically |
| BW06 | 487 | Ambient source and zone placement | Studio | Right listener, scene scale, lifecycle | Place agreed source anchors and zone metadata; sound designer builds the mix |
| BW07 | 488 | Ambient particles and moving props | Specialist assets plus Studio assembly | Effects have to share world state and the scene budget | VFX and animation hand-off with attachment points and tested ranges |
| BW08 | 489 | Distant skyline | Blender assets or Studio assembly, as fits | Matters for silhouette and depth composition, not near detail | Check current LoD/streaming behavior; do not rely on full-detail residency |

### 8.2 Export, import, round trip, pivots, scale chain, instancing, collision

| ID | EP | Decision point | Rule or choice | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| BW09 | 505 | Export preset | Roblox general export guidance: FBX; Path Mode Copy with embedded textures; Apply Scalings = FBX Unit Scale; Add Leaf Bones off; Bake Animation off unless animation is needed. Asset categories may add rules. The same page has an old-looking image description naming a 0.01 transform scale: do not stack it on another scale workflow without a test. [O] Follow the current text and the project's measured calibration; do not mix incompatible recipes. | VERIFIED; [O] | B04 acc |
| BW10 | 507 | Importer formats and options | Importer takes FBX, glTF and OBJ meshes; FBX and glTF carry multiple objects and hierarchy and materials. glTF hierarchy can differ from FBX (intermediate Models, a _Node name suffix). Importer exposes scene-position and scene-origin-pivot choices. [O] Record these options: they affect a modular kit even when the surface looks right. | VERIFIED; [O] | B05 acc |
| BW11 | 509 | Post-import verification | Check dimensions, orientation, pivot, hierarchy, material resources, normals, collision, permission context. Compare the result with the calibration object and a known route fixture. A clean import tells you only that the importer took the file. | OPINION | E00 |
| BW12 | 687, 531 | Calibration fixture and round trip | Set scale and a calibration fixture in the intended apps; record unit convention, pivots, axes, import options; prove one asset round trip (one calibration kit) before bulk construction or transfer. | OPINION | E00, B04/B05 |
| BW13 | 525 | Scale chain (repair order) | If scale is wrong, isolate in this order: scene units, object transforms, export conversion, importer scaling. Do not resize all descendants first. The unit convention itself (1 stud = 28 cm, B02) is in EP:25, outside this range (T01 holds it). | OPINION | E00 |
| BW14 | 525 | Pivot | If a pivot is wrong, compare the source origin with the import pivot options (see BW10). | OPINION | E00 |
| BW15 | 525 | glTF object path changed | Repair the semantic mapping; do not hard-code a guessed name. | OPINION | E00 |
| BW16 | 525 | Material looks different | Compare the supported runtime maps and the lighting before re-baking textures. | OPINION | E00 |
| BW17 | 525 | Route becomes blocked | Look at collision on its own, apart from the render mesh. | OPINION | E00 |
| BW18 | 548, 733 | Instancing | Runtime instancing depends on shared MeshContent plus matching SurfaceAppearance/TextureContent/material (P21). A linked Blender duplicate shares mesh data in Blender (B07) but does not guarantee runtime instancing after import. [O] Build a deduplicated kit; never re-import the assembled world again and again. | VERIFIED; [O] | P21, B07 |
| BW19 | 548, 550 | Collision | Use simpler collision geometry where interaction needs no detail; disable CanCollide/CanTouch/CanQuery only where unneeded; Tunable CollisionPrecision is qualitative (0 Hull, 1 near-exact). [O] Verify walkable surfaces and camera blockers in collision visualization. | VERIFIED; [O] | P21, P20 |
| BW20 | 544 | Texture packing | Atlas only textures usually seen together on batchable parts; otherwise one atlas region loads the whole atlas mip. [O] Keep shared kits; avoid giant mixed-stage atlases. | VERIFIED; [O] | P27 |
| BW21 | 540 | Static vs moving | SLIM suits static world models; runtime geometry/property changes and animations are excluded. [O] Split moving foliage, doors, destructibles from static composite architecture. | VERIFIED; [O] | P18 |
| BW22 | 495, 499 | Manifest-driven export | Export and non-export collections, stable names, manifest before export; export only intended content; never target by selection or ambiguous default name. | OPINION | E00 |
| BW23 | 513 | Blender vs Studio tooling | Blender MCP and Studio MCP are separate: discover the Blender provider and schema first; do not assume Studio tool names exist in Blender; edit named collections only. | OPINION | E00 |
| BW24 | 517, 735 | Studio targeting | Name the `studio_id` on every call; choose Edit/Client/Server context; a successful command does not prove the right instance changed. | VERIFIED; [O] | B03 |
| BW25 | 447, 483, 689 | Replacing the blockout | Keep gameplay placeholders, collision references and approved route dimensions until the replacement has equal validated behavior. | OPINION | E00 |
| BW26 | 558 | Mesh size | Single imported general mesh ceiling is 20,000 triangles. It is not an asset target or a stage total (BT02). | VERIFIED | P26 acc |

## 9. Number register (EP:435-762)

"not established" = the paper says no source gives it. Unit as the paper gives it.

| ID | Value | Unit / meaning / scope | EP | Src, date | Tag |
| --- | --- | --- | --- | --- | --- |
| N01 | 5.2.2 LTS | Blender version the paper verified; patch released 2026-09-15 (5.2 released 2026-07-14, register) | 479, 530 | B01 | VERIFIED |
| N02 | 0.01 | transform scale named in an old-looking image description on the export page; not to be stacked with another scale workflow | 505 | B04 acc | VERIFIED (text); OPINION (handling) |
| N03 | 64 | studs, recommended StreamingMinRadius starting value | 536, 559 | P16 acc | VERIFIED |
| N04 | 1024 | studs, recommended StreamingTargetRadius starting value | 536, 559 | P16 acc | VERIFIED |
| N05 | 64 | StreamingTargetRadius for the temporary stress test; unit not stated at EP:589 | 589, 608 | P28 acc | VERIFIED (recommended); OPINION (use) |
| N06 | 1.5 | seconds, opportunistic frustum-only content lingers after leaving eligible areas | 538, 606 | P17 acc | VERIFIED |
| N07 | 4096 x 4096 | texture size available for supported instance types, not all assets or devices | 544 | P27, P30 | VERIFIED |
| N08 | 3.5 GB | below it 4K is disabled on low-end Android (P27 table); about this memory or more is tied to full 4K (P29) | 544, 597 | P27 2026-03-23; P29 2026-07-10 | VERIFIED |
| N09 | 3 GB | iPad class that receives reduced texture resolution (staff diagnosis) | 597 | P29 2026-07-10 | VERIFIED |
| N10 | 20,000 | triangles, ceiling per individual general mesh | 558 | P26 acc | VERIFIED |
| N11 | 4 x 4 x 4 | terrain cell representation; the paper writes "stud" for the unit | 560 | P15 | VERIFIED |
| N12 | 100 | particles per second, mobile ceiling per emitter | 561, 674 | P13/A16 acc | VERIFIED |
| N13 | 20 | seconds, particle lifetime cap; appears only at EP:674 | 674 | A16 acc | VERIFIED |
| N14 | 10-15 | minutes of active mobile play for the thermal check; not proof longer is safe | 571, 581 | P25 acc | VERIFIED |
| N15 | 1000 / frame time (ms) | = FPS | 571 | P24 acc | VERIFIED |
| N16 | 100/3 | ms (about 33.3), derived interval at 30 FPS; my arithmetic check: 1000/30 = 100/3. Not a measured budget | 571 | derived | arithmetic |
| N17 | 50/3 | ms (about 16.7), derived interval at 60 FPS; 1000/60 = 50/3. Not a measured budget | 571 | derived | arithmetic |
| N18 | 0 and 1 | CollisionPrecision ends: 0 Hull, 1 near-exact when possible; not a linear percentage | 550, 607 | P20 2026-09-17 | VERIFIED |
| N19 | 4 | quality level below which shadows are off (performance guide); QualityLevel page says behavior is device-specific | 593 | P21, P03 acc | VERIFIED |
| N20 | 2026-07-10 | Scene Analysis full release (first announced 2026-05-05, register) | 569, 605 | P23 | VERIFIED |
| N21 | 2026-04-27 | mesh streaming and improved LoDs announcement; planned July transition and property removal not confirmed | 542 | P19 | VERIFIED |
| N22 | 2026-09-17 | tunable collision precision announcement | 550, 607 | P20 | VERIFIED |
| N23 | 2026-09-04 | staff reply: mesh LoD incident, feature rolled back | 599 | P31 | VERIFIED |
| N24 | 2026-03-23 | P27 status table date (first post 2025-12-12, register) | 544, 597 | P27 | VERIFIED |
| N25 | 2026-01-30 | 4K texture release recap | 544 | P30 | VERIFIED |
| N26 | 2026-07-10 | staff reply on a 3 GB iPad (same date as N20, different source) | 597 | P29 | VERIFIED |
| N27 | 15 | process steps (EP:683-711) and review checks (EP:621-635); structure counts, not performance values | 683-711, 621-635 | E00 | OPINION |
| N28 | not established | whole-stage visible triangles, draw calls, resident parts/instances on a low-end phone | 557 | P22/P25 | UNKNOWN |
| N29 | not established | safe terrain volume; stage-safe total particles; light, shadow-caster and transparent-layer counts; texture residency; geometry memory; total client memory; ambient sound and animated-prop counts | 560-565 | P15, P13, P03, P21, P27, P25, P22, P24 | UNKNOWN |
| N30 | not established | phone source budget; waterfall gain; crossfade duration; cave decay; numeric source ranges and gains; fade durations; per-phone concurrency; effect costs | 676, 749, 755 | none | UNKNOWN |
| N31 | not established | universal door size, fog density, sound range, stage count: the paper only says not to treat them as researched without a scoped source | 729 | none | OPINION (no sourced value) |
| N32 | not established | universal phase duration (ES01); a guessed grid instead of measured dimensions (ES02); universal stage cap (ES06); universal zone polling rate (ES11); universal source radius (ES12) | 470-471, 604, 672, 673 | C01, E00, P22/P25, A12, A13/A05 | as in the ES rows (OPINION; VERIFIED API for ES11, ES12) |
| N33 | not established | frame-time acceptance target: the studio picks it; a chosen FPS is not an official universal minimum | 565 | P24 acc | OPINION |

## 10. Claims to fact-check (for the fact-check agents)

Tag is the paper's. "[O]" = the paper's own opinion clause, not a sourced fact. Each row is the paper's claim, not a checked fact.

### 10.1 Performance and streaming

| ID | Claim | EP | Src | Tag |
| --- | --- | --- | --- | --- |
| CP01 | Recommended streaming start: StreamingMinRadius 64, StreamingTargetRadius 1024 studs; Target larger than Min; Opportunistic stream-out; PauseOutsideLoadedArea integrity mode | 536, 559 | P16 | VERIFIED |
| CP02 | Loaded content can stay beyond Target when memory allows; raising Min uses more memory and bandwidth | 536 | P16 | VERIFIED |
| CP03 | Frustum streaming is opt-in, additive, server-controlled per player; does not replace ordinary streaming; does not cull replication behind walls | 538 | P17 | VERIFIED |
| CP04 | Frustum streaming can raise client memory/CPU; effective range depends on draw distance and an engine maximum | 538 | P17 | VERIFIED |
| CP05 | Automatic mode responds to narrow FOV, movement, distant cameras; rapid rotation can churn far instances | 538 | P17 | VERIFIED |
| CP06 | Opportunistic frustum-only content lingers 1.5 s after leaving eligible areas | 538, 606 | P17 | VERIFIED |
| CP07 | Occlusion culling (renderer) and frustum streaming (replication) have different jobs | 601 | P17, P21 | VERIFIED |
| CP08 | SLIM: lightweight composite representations with LoDs that may render after full instances stream out | 540 | P18 | VERIFIED |
| CP09 | SLIM needs streaming, a place saved to Roblox, and Team Create; set Model.LevelOfDetail = SLIM (register key quote covers only the saved-place part) | 540 | P18 | VERIFIED |
| CP10 | Static-model SLIM excludes runtime geometry/property changes and animations | 540 | P18 | VERIFIED |
| CP11 | Studio/Developer Console debug tints show SLIM transcoding/LoD state; a local-only place does not prove cloud transcoding | 540 | P18 | VERIFIED |
| CP12 | With MeshStreamingAndImprovedLoDs on, per-MeshPart RenderFidelity is ignored; phased rollout; property removal planned; a July transition planned | 542, 595 | P19 (2026-04-27) | VERIFIED |
| CP13 | Performance guide recommends Automatic/Performance RenderFidelity | 595 | P21 | VERIFIED |
| CP14 | Texture streaming picks resident detail dynamically; 4096x4096 available for supported instance types | 544 | P27, P30 | VERIFIED |
| CP15 | 4K disabled on low-end Android below 3.5 GB (P27 status 2026-03-23); low-end iOS shown as supported | 544, 597 | P27 | VERIFIED |
| CP16 | A 3 GB iPad gets reduced resolution; full 4K tied to about 3.5 GB or more | 597 | P29 (2026-07-10) | VERIFIED |
| CP17 | Atlases only for textures usually seen together on batchable parts; else one atlas region loads the whole atlas mip | 544 | P27 | VERIFIED |
| CP18 | Instancing needs shared MeshContent plus matching SurfaceAppearance, or TextureContent, or material | 548 | P21 | VERIFIED |
| CP19 | Re-importing identical geometry under different asset IDs can lose instancing | 548 | P21 | VERIFIED |
| CP20 | Anchor static objects; simpler collision where detail is not needed; disable CanCollide/CanTouch/CanQuery only when unneeded | 548 | P21 | VERIFIED |
| CP21 | Transparent overlap and heavy shadow-casting density add render cost | 548 | P21 | VERIFIED |
| CP22 | CollisionFidelity=Tunable adds CollisionPrecision; 0 Hull, 1 near-exact when possible; qualitative; algorithms do not generally map to slider values | 550, 607 | P20 (2026-09-17) | VERIFIED |
| CP23 | Decomposition persists until regenerated; some APIs beyond the Properties panel support only default precision | 550 | P20 | VERIFIED |
| CP24 | Single general mesh ceiling is 20,000 triangles | 558 | P26 | VERIFIED |
| CP25 | Terrain is a 4x4x4-stud cell representation (paper adds the unit "stud") | 560 | P15 | VERIFIED |
| CP26 | Mobile particle rate ceiling 100/s per emitter | 561, 674 | P13/A16 | VERIFIED |
| CP27 | Particle lifetime cap 20 s (appears only at EP:674; register scope for A16 names only the 100/s) | 674 | A16 | VERIFIED |
| CP28 | Performance guide: shadows disabled below quality level 4 | 593 | P21 | VERIFIED |
| CP29 | QualityLevel docs: feature behavior is platform/device specific | 593 | P03 | VERIFIED |
| CP30 | Scene Analysis fully released 2026-07-10; views and triangle-composition categories as listed in PF09 | 569, 605 | P23, P22 | VERIFIED |
| CP31 | Local Studio statistics do not match phone results; unparented instances alone do not show a leak | 569 | P22 | VERIFIED |
| CP32 | MicroProfiler: mobile capture enabled in client Settings, opened from a dev machine on the same network at the displayed address | 571 | P24, P25 | VERIFIED |
| CP33 | Emulation cannot reproduce thermal throttling, device memory and all rendering | 571 | P25 | VERIFIED |
| CP34 | Hardware guide recommends 10-15 minutes of active mobile play for thermal degradation | 571, 581 | P25 | VERIFIED |
| CP35 | FPS = 1000 / frame time in ms; 30 FPS = 100/3 ms and 60 FPS = 50/3 ms (arithmetic only) | 571 | P24 | VERIFIED; arithmetic |
| CP36 | Roblox recommends full traversal, distant teleports, revisits, and a stress test at StreamingTargetRadius=64 | 589, 608 | P28 | VERIFIED |
| CP37 | Staff (2026-09-04): a separate interacting feature caused lowest-LoD meshes and was rolled back | 599 | P31 | VERIFIED |

### 10.2 Scale, import and Blender

| ID | Claim | EP | Src | Tag |
| --- | --- | --- | --- | --- |
| CB01 | Blender 5.2.2 LTS released 2026-09-15 is the latest stable LTS | 479, 530 | B01 | VERIFIED |
| CB02 | Mesh API separates vertices, edges, loops, polygons; BMesh can tessellate quads and n-gons into triangles | 497 | B08, B11 | VERIFIED |
| CB03 | Mesh.validate can correct or remove invalid geometry (it mutates) | 497, 737 | B08 | VERIFIED |
| CB04 | The evaluated-mesh API name must be checked against the installed Blender version (paper does not name it) | 499 | none | OPINION |
| CB05 | Roblox export guidance: FBX; Path Mode Copy with embedded textures; Apply Scalings = FBX Unit Scale; Add Leaf Bones disabled; Bake Animation disabled unless needed | 505 | B04 | VERIFIED |
| CB06 | Asset categories may have extra export rules | 505 | B04 | VERIFIED |
| CB07 | The export page has an old-looking image description naming a 0.01 transform scale | 505 | B04 | VERIFIED |
| CB08 | Importer accepts FBX, glTF, OBJ; FBX and glTF support multiple objects, hierarchy, materials | 507 | B05 | VERIFIED |
| CB09 | glTF hierarchy can differ from FBX: intermediate Models, _Node suffix | 507 | B05 | VERIFIED |
| CB10 | Importer exposes scene-position and scene-origin-pivot choices | 507 | B05 | VERIFIED |
| CB11 | Blender linked duplicates share mesh data; paper says this does not guarantee runtime instancing | 733 | B07 | VERIFIED; [O] |
| CB12 | Blender lighting does not import equivalently into Studio | 486 | none | OPINION |
| CB13 | Studio Terrain accepts approved height/color inputs or bounded terrain operations | 485 | none | OPINION |
| CB14 | Scale-fault order: scene units, object transforms, export conversion, importer scaling | 525 | none | OPINION |
| CB15 | Roblox supports particular runtime material maps to compare against (paper does not list them) | 525 | none | OPINION |
| CB16 | Unit convention 1 stud = 28 cm (B02) is at EP:25, outside this range; check with T01 | 25 | B02 | VERIFIED |

### 10.3 Studio MCP

| ID | Claim | EP | Src | Tag |
| --- | --- | --- | --- | --- |
| CM01 | `list_roblox_studios` exists; every tool call takes `studio_id` | 517, 532 | B03 | VERIFIED |
| CM02 | Tools exist: `get_studio_state`, `start_stop_play`, `screen_capture`, `execute_luau`, `inspect_instance`, `search_game_tree` | 517 | B03 | VERIFIED |
| CM03 | `execute_luau` selects Edit, Client or Server data-model context | 517, 532 | B03 | VERIFIED |
| CM04 | `screen_capture` accepts a custom camera position and look-at target | 517 | B03 | VERIFIED |
| CM05 | SceneAnalysisService exposes tables through MCP (GetInstanceCompositionAsync, GetTriangleCompositionAsync); unclear whether a named MCP tool or `execute_luau` is meant | 569 | P22, P23 | VERIFIED |
| CM06 | A successful MCP command does not prove the right instance or data model changed | 735 | B03 | VERIFIED; [O] |
| CM07 | No canonical Blender MCP provider or version was established; no Blender connection was made | 513 | none | UNKNOWN |
| CM08 | Studio MCP tool names should not be assumed to exist in Blender MCP | 513 | none | OPINION |

### 10.4 Audio

| ID | Claim | EP | Src | Tag |
| --- | --- | --- | --- | --- |
| CA01 | AudioAnalyzer exposes PeakLevel and RmsLevel; spectrum processing can be disabled when only levels are needed | 651 | A14 | VERIFIED |
| CA02 | Server audio processing is disabled, so AudioAnalyzer analysis belongs on the client ("server output zero") | 651, 675 | A14 | VERIFIED |
| CA03 | Wire.Connected marks an active valid connection (valid source/target pins, no cycle). The register key quote describes data flow, not the property name: check the property | 653 | A15 | VERIFIED |
| CA04 | Modern spatial queries separate bounding boxes from the actual occupied shape (WorldRoot) | 672 | A12 (=B10) | VERIFIED (API) |
| CA05 | A persistent ambient source must survive or be rebuilt after stream-out | 673 | A13/A05 | VERIFIED (behavior); OPINION |
| CA06 | A deprecated-property assumption is a review item (register A11: AssetId deprecated, Asset current); the body at EP:657 names no property | 657 | A11 (register) | VERIFIED |
| CA07 | Legacy Sound and the advanced audio graph differ (register A10); acoustic simulation left beta (register A09, update 2026-09-22); the paper warns against promising it on low-end phones | 755 | A09, A10 | OPINION (the warning) |

## 11. Contradictions and limits

| ID | EP | Item | Handling in skills |
| --- | --- | --- | --- |
| X01 | 15, 587, 745, 761 | The paper ran no build, import, render, listen, playtest or benchmark. Every check here is a proposal. | Mark each check "to do". Results come from this studio's runs. Never write "passed". |
| X02 | 554, 557-565, 676 | Low-end-phone budgets (triangles, draw calls, instances, particles total, lights, memory, ambient sources, frame time) are UNKNOWN. | Leave the cell empty until measured on a named device and build. Never invent or borrow a number. |
| X03 | 536, 559, 589 | Stress test at StreamingTargetRadius=64 equals StreamingMinRadius=64 while the same page says Target must be larger than Min. The paper reconciles: the stress is temporary and not a statement that equal radii are ideal. | Use Target 64 only as a stress run. Ship 1024 / Min 64 as starting values. Check P28 vs P16. |
| X04 | 536 | The 64 / 1024 radii are Roblox's recommended starting values, not limits; the paper tags the paragraph VERIFIED. | Label as starting values, never as limits. |
| X05 | 593 | "Shadows off below quality 4" (P21) vs QualityLevel page that says device-specific (P03). | Test the target device. Do not promise visibility from a quality number. |
| X06 | 595, 542 | P21 recommends Automatic/Performance RenderFidelity; P19 says it is ignored on the new path. P19 also plans a July transition and removal that the paper cannot confirm. | Inspect the active path and the real property list in the tested Studio and client. |
| X07 | 597 | P27 (2026-03-23) shows low-end iOS supported; P29 (2026-07-10) says a 3 GB iPad is reduced and ties full 4K to about 3.5 GB or more. | Test per device class; no blanket 4K claim. |
| X08 | 599 | P31 was a scoped incident with a rollback (2026-09-04), not evidence that mesh streaming fails in general. | If unchanged scenes regress, keep traces and look for engine changes first. |
| X09 | 505 | The export page text (current) and an old-looking image description (0.01 scale) disagree on scale handling. | Follow the text plus a measured calibration; never combine recipes. |
| X10 | 507 | glTF hierarchy differs from FBX (extra Models, _Node suffix). | Map objects by meaning, not by guessed names. |
| X11 | 674, 561 | The 20 s particle lifetime cap appears only at EP:674; the 100/s ceiling is a per-emitter value and not a scene budget. A16 and P13 are one page cited under two IDs. | Fact-check the 20 s value; keep the ceiling out of budgets. |
| X12 | 560 | The paper gives the terrain cell as 4x4x4 studs; the register quote for P15 gives a 4x4x4 grid of cells without the unit. | Check the unit on the Terrain API page. |
| X13 | 540 | Team Create as a SLIM requirement is not in the register quote for P18. | Check the SLIM page. |
| X14 | 569 | "Through MCP" for SceneAnalysisService is not tied to a named tool. | Check whether a Studio MCP tool exists or whether `execute_luau` is used. |
| X15 | 653 | Wire.Connected as the property name is not in the register quote for A15. | Check the Wire page. |
| X16 | 513 | No canonical Blender MCP provider or version was established. | Discover the provider and schema each time; log version. |
| X17 | 571, 581 | The 10-15 minute thermal check is the documented start, not proof that longer play is safe. | Extend to the real session length; the target frame-time tail is a project decision. |
| X18 | 569, 571 | Local Studio statistics and emulators are not phone results. | Label any editor/emulator number as such; never as a phone benchmark (ST12). |
| X19 | 651, 653 | AudioAnalyzer levels are not LUFS or SPL; a valid Wire does not mean it sounds right. | "Auditory acceptance pending" until a listening review exists. |
| X20 | 749, 751, 755 | Open numbers (OQ01, AX09) and the lack of a universal premium Roblox preset or complete quantitative art bible for any studio. | Fill only with labeled project values from tests; never credit the literature. |
| X21 | 470 | ES01 pairs an EXPERIENCE source (C01, a historic Riot workflow) with the paper's own implementation OPINION; no phase duration is established. | Cite C01 as a studio account only, never as a Roblox rule. |
| X22 | 479 | Newer Blender development builds exist; they are not the pinned target. | Pin 5.2.2 or log the change; re-check API names (CB04). |

## 12. Coverage map (check C1)

| Paper part | EP | Where |
| --- | --- | --- |
| 11 workflow, kit contract, change control, summary | 435-471 | W01-W12, ES01-ES02, RP01-RP04, RP09 |
| 12 hybrid, data, MCP, handoff, summary | 473-532 | H01-H11, BW01-BW26, ES03-ES05, RP05-RP08 |
| 13 performance, budget table, procedure, disagreements, summary | 534-608 | PF01-PF15, BT01-BT09, MP01-MP08, RJ01-RJ05, ES06-ES10 |
| 14 review, 15 checks, sound review, summary | 610-677 | RV01-RV08, RA01-RA05, RC01-RC15, RS01-RS07, ES11-ES16 |
| 15 process (15 steps) | 683-711 | ST01-ST15 |
| Common AI-built defects | 715-723 | DF01-DF05 |
| Do-not list | 727-745 | DN01-DN10 |
| Open questions | 749-751 | OQ01-OQ02 |
| Additional ambience exclusions | 755 | AX01-AX09 |
| Section 15 evidence summary | 760-761 | ES17-ES18 |
| Register | 763-1469 | [[reference/environment/00-source-register]] |
