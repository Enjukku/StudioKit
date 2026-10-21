> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `orchestration`. Owner-approved (J016-D4). Evidence per row (papers, Riot transcripts, kit): `knowledge/jobs/J016-orchestration/design-jobtypes.md`. Revised by orchestrator-fixer W1 · claude-opus-5-5 · high · 2026-10-21 (J016 G3 audit): stage map, repair stage, code review, interface rounds, cross-type rules.

# Job recipes

Every recipe follows `rules/company.md` §4. Stages per saved workflow `.agents/workflows/jobs/job-<type>.js`, one call each: `direction` → G1 → `proof` → G2 → `build` → G3; `repair` applies a G3 change to the affected layers only. M jobs skip `proof` (it runs inside `build`). Args: `.agents/workflows/jobs/README.md`.

| Stage | Recipe rows it runs |
| --- | --- |
| `direction` | Direction leads (D1 proposals, D2 exchange, D3 direction sheet and signatures) → G1 shows |
| `proof` (L) | Contract draft; Interfaces before the proof; Proof and its reviews → G2 |
| `build` | Interfaces after G2; Production order; Check-ins; Integrator; Review order (M: the proof and its reviews first) → G3 |
| `repair` | Return paths for the owner's G3 change: only the affected makers, in dependency order; then recapture and refreeze; then the review chain again on the new candidate |

- **Review orders:** scripts run first and the lead's readiness check runs last. Technical checks (reviewer, qa-lead, performance-engineer) run beside the creative order; the arrows order only the creative reviews. Every candidate with code (player code, wiring, remotes, saves) adds the `reviewer` (`code-review` + area skills, `rules/company.md` §7).
- **After every repair round** the candidate is recaptured and refrozen before the next review round.
- **Studio:** where a recipe names two Studio users, they take the Studio in turn (`rules/company.md` §9). Studio MCP captures stills, not video or sound: sync is judged from the Output log (event, VFX and cue start times on one clock) and labelled so; listening is an owner-confirmed line in the gate packet.

## 1. Cutscene
| Item | Recipe |
| --- | --- |
| Job lead | **film-director**; it is also the sequence integrator and keeps continuity from boards to final frames |
| Direction leads | film-director (beat contract, camera mode, staging, 2 approaches) · art-director (look per beat: palette, light, shape; 2-3 reference images) · architect (runtime choice, camera ownership, streaming, skip and every ending; what to probe in Studio) · game-designer consulted for the gameplay state sheet |
| G1 shows | the beat contract, 2 pictured approaches (board thumbnails or reference images), the recommendation, scope, usage |
| Contract | beat sheet + shot list (`templates/jobs/beat-sheet.md`, `tools/film/shotlist.py`): stable event ids, start/end, trigger, camera, animation state, VFX cue, sound cue, player control, skip consequence, revision |
| Proof (G2) | storyboards first (a pending board batch stops the proof before the animatic), then a timed Blender animatic with temporary sound and effect cues, on a greybox set where the set is missing; the architect runs the Studio probes it named at D1 before the animatic review. Reviews before the owner: film → art-director (composition, look reachable) → architect (cost) |
| Interfaces before the proof | animator, environment-designer, vfx-designer, sound-designer and architect state needs against the beat sheet draft (revision named); film-director merges; ≤ 2 rounds |
| Interfaces after G2 | animator ↔ character-rigger ↔ modeler (a new cast without a usable rig is a prerequisite: a character job first, `orchestration` §3; found later → `needs-decision` before the animatic) · environment-designer ↔ film (sets, landmarks, light per beat) · **vfx-designer ↔ sound-designer co-design each cue's envelope** (wind-up, peak, tail) on the event ids · ui-ux-designer (letterbox, subtitles, skip) · architect (player contract `contract-player.md` with the Code file owners table) · feature-builder (player contract, endings) |
| Production order | set and animation in parallel → VFX and sound prototype on the stable event ids early, then finish against the animation → one combined early pass of picture, VFX and sound reviewed before final polish |
| Check-ins | film reviews animation blocking before polish; art-director reviews the rough set and look before final light |
| Integrator | film-director (scene data via `shotlist.py luau`); feature-builder builds or extends the player against the contract |
| Review order | scripts (`shotlist.py check`, `log-diff`, gate) → qa-lead (skip, every ending, control and camera restored, repeat trigger, multiplayer, streaming) ∥ performance-engineer (phone) ∥ reviewer (the player code) → **film-director** (staging, timing, camera, clarity, with sound) → **art-director** (integrated look) → sound sync check |
| Return paths | a look problem in one shot → its maker (modeler, light, VFX); timing unchanged → sound only confirms. A visual peak moves → beat-list revision → animator, VFX and sound acknowledge and recheck. A skeleton change → animation and VFX attachments stale |
| Gap | the animator role is planned (J006): run a stand-in with the animator brief and `rig-pipeline` |

## 2. Character or creature
| Item | Recipe |
| --- | --- |
| Job lead | **art-director**; the game-designer owns its role in play |
| Direction leads | game-designer (what it does, gameplay role, signature action, camera, numbers) · art-director (2-3 visual directions as reference images, **2-3 identity anchors**, shape language) · character-rigger + animator (motion profile; rig-costly parts such as capes and coattails flagged with a cheap fallback) |
| G1 shows | 2-3 pictured directions with anchors marked, the recommendation, the signature move, what is costly to animate |
| Contract | the rig sheet (`rig-pipeline`, `templates/rig/rig-sheet.md`) + the art-director's reference set (extra views, answers on material intent) |
| Interfaces | `rig-pipeline` S1-S2 before the proof (motion needs → rig plan → K2); S3-S6 after G2. Playable: the architect writes the wiring contract (`contract-wiring.md`, Code file owners) beside S0 |
| Proof (G2) | blockout at player scale + proxy rig + the signature pose or move, captured at the game camera in Studio against the game's background. Reviews: art-director (silhouette, anchors) → animator (usable) → game-designer (role reads) |
| Production order | modeler (cuts, geometry, textures) → rigger (rig + tests) → animator (clips + timing list) → VFX and sound for its actions on the timing list → UI icon renders of the shipped model |
| Check-ins | art-director reviews the model at the game camera on the real background before texture polish (paint-overs); each hand-off is checked by the receiver (K-checks) |
| Integrator | animator for the imported revision (`rig-pipeline` S7); feature-builder when it is wired into gameplay |
| Review order | scripts (`model_audit.py`, `rig_audit.py`) → consumer K-checks → **art-director** (identity, silhouette, value at the game camera) → **game-designer** (role reads in play) → performance-engineer (on-screen count, phone); reviewer beside them when it is wired into gameplay |
| Return paths | a costume part blocks motion → rig note → modeler (one exact note); a look change forced by a limit → owner with both options rendered |
| Variant mode (skin, recolour, themed version) | fixed: base rig, clips, identity anchors; open: costume, palette. Skip S1 unless there are new moving parts. No geometry change (palette only): the model step is texture-only and S4-S6 are skipped on the released base rig. Selling it is a second job (feature, with money: `orchestration` §2). Review adds: the base is recognisable in every view; no disadvantage for players who own it |

## 3. Stage
| Item | Recipe |
| --- | --- |
| Job lead | **environment-designer** (owns and integrates the place) |
| Decision rights | routes, cover, sight lines, blocking surfaces: **game-designer**; look: art-director; budgets: performance-engineer. Art stays inside the approved greybox; composition changes are asked for, never made silently |
| Direction leads | game-designer (the stage's job, route graph, encounters, pacing, its hook) · art-director (2-3 key-place reference images, value band) · environment-designer (built-where, landmarks, ambience idea) · performance-engineer (budget) |
| G1 shows | the route graph, the **blueprint draft** (so the owner approves the blueprint before any building, J008), the first view, 2-3 pictured looks, the recommendation |
| Contract | route graph + blueprint approved at G1 (game-designer + environment-designer), refined in the proof stage: a refinement that changes an approved item (route, footprint, landmark, heights) goes to the owner before the greybox is built; other refinements are listed at G2 or G3 · ambience map (environment → sound, VFX) · kit piece list (environment → modeler) · a player-size scale reference in every space |
| Proof (G2) | a playable greybox in Studio: walk-test and playtest captures, first view, landmark read, route times. Reviews: game-designer (judges the play captures) → art-director (composition and value in blockout) → performance-engineer |
| Production order | art blockout snapped to the approved greybox → kit pieces (modeler) and art production → light and atmosphere → ambience (sound) and ambient VFX. Playtests continue during art; lighting and polish only after the space plays well |
| Check-ins | the game-designer checks placement, materials, set dressing and VFX placement as the build grows |
| Integrator | environment-designer (Studio writer for place content) |
| Review order | scripts (scene audit, budgets, floating parts) → **game-designer** judges the studio-operator's playtest captures (play wins over art readability) → **art-director** (camera set, value ladder, rest areas next to detail) → sound and VFX ambience check → qa-lead (collision, falls, stuck spots) |
| Return paths | an art change that alters sight lines or collision → game-designer; a new surface material → sound may refuse it for time → environment picks another |

## 4. UI screen
| Item | Recipe |
| --- | --- |
| Job lead | **ui-ux-designer**; the game-designer owns the player's decision |
| Direction leads | game-designer (the decision the screen serves; shops and odds: progression-designer + `platform-policy`) · ui-ux-designer (state list, focus map, 2-3 target reference images in the game's style book) · art-director (style cohesion) · feature-builder or architect (data and remotes available) |
| G1 shows | the decision record, the grey-box wireframe with real content, 2-3 pictured style targets, the recommendation |
| Contract | state map + spec (`content/ui/<screen-id>/spec.md`): states, events, data fields, sizes for the smallest phone |
| Proof (G2, L only) | a clickable Figma prototype of every state at phone size. Reviews: game-designer (decision clear) → art-director → feature-builder (buildable) |
| Production order | Figma build to the target image → handoff → feature-builder implements (`ui-basics`) ∥ UI sounds and UI effects from the VFX library |
| Integrator | feature-builder |
| Review order | gate PASS + reviewer (code) → qa-lead (every state, touch and gamepad, longest text) → **ui-ux-designer** against its target image → **art-director** → **game-designer** (the decision works) |
| Return paths | a state or readability failure returns to the state map or layout, not to styling |

## 5. Gameplay feature
| Item | Recipe |
| --- | --- |
| Job lead | **game-designer** (player behaviour and acceptance); technical lead **architect** |
| Direction leads | game-designer (feature spec: what the player does, feels, decides; acceptance cases incl. failures) · architect (engine features, risky claims, probes, client/server placement, file owners) · progression-designer for numbers · `platform-policy` for money, odds, ads |
| G1 shows | the behaviour in player words, the risky claims and how the proof tests them, scope, usage |
| Contract | feature contract: behaviours, state names, events (the hooks UI, VFX and sound attach to), tuning keys in data, acceptance checks written by the briefer |
| Proof (G2) | a playable grey-box prototype in Studio (feature-builder, minimal) that tests the risky claim and the fun; the studio-operator plays it and the game-designer judges the play captures. Visible parts: the ui-ux-designer's target image and the vfx-designer's key frames are made beside the prototype and shown at G2 |
| Production order | architect plan → feature-builder (failing case first) ∥ progression tables ∥ UI, VFX and sound against the event names; qa-lead writes protected acceptance tests |
| Integrator | feature-builder |
| Review order | gate PASS → reviewer ∥ qa-lead ∥ performance-engineer (if heavy) → **game-designer** judges the play captures → **art-director** for visible parts |
| Return paths | wrong incentives → game-designer or progression-designer; wrong behaviour → feature-builder; a fourth review round on one approach → reconsider with the architect |

## 6. Effect
| Item | Recipe |
| --- | --- |
| Job lead | **vfx-designer** |
| Direction leads | game-designer (the gameplay event, its timing window, what must stay readable) · vfx-designer (frame script, importance, technique) · sound-designer (the sound's job: cue, feedback or emotion) · art-director only when the effect sets a new look |
| Contract | one event timeline (wind-up, hit, tail; times in seconds with the source frame) shared by the animator's timing list, the VFX frame script and the sound cue card, same event ids |
| Cooperation | VFX and sound co-design the envelope before either builds. Gameplay length comes from design; the animator sets beats inside it; VFX follows; sound keys to the picture events |
| Proof | one capture at the game camera in a busy scene, with the temporary sound's cue times in the Output log (MCP captures are stills; listening is owner-confirmed); for an M job shown at G3 |
| Integrator | feature-builder or quick-builder wires the spec; studio-operator records the capture |
| Review order | scripts (budget numbers, flash safety) → **game-designer** (does it hide information players need?) → **art-director** (brightest point where the eye must go; value ladder) → sound sync from the Output log cue times (listening: owner-confirmed); reviewer beside them when wiring code changed |
| Return paths | a timing change → the timing-list revision → VFX and sound recheck |

## 7. Marketing art
| Item | Recipe |
| --- | --- |
| Job lead | **marketing** |
| Direction leads | marketing (the hook; the brief's strategy names the hero of the image) · game-designer (the art must tell the truth about play) · art-director (style, identity anchors) · trend-scout optional (what competitors show now) |
| G1 shows | 3-5 rough thumbnails at the real slot size, the preferred one stated |
| Proof (G2 = green light) | the chosen thumbnail with value and light set, tested at real size (`thumb_check.py`) and in the real layout; after green light the big shapes stay |
| Production order | render → polish → a layered file (foreground, midground, background) → the family of crops planned at the start |
| Integrator | marketing |
| Review order | scripts (`thumb_check.py`, `look_check.py` value) → **art-director** (identity read largest, silhouette, style rules) → **game-designer** (truthful to play) |
| Return paths | a wrong face or identity draws the first note every time: fix it before the review |

## Not recipes
- **New game pre-production:** the `preproduction` skill's growth order; it produces the briefs these recipes consume.
- **Live update or event:** the live-ops plan is split by the lead into jobs of the types above.

## Cross-type rules (all types)
| Rule |
| --- |
| One written target experience shared by design, art and engineering before craft work; name the type of fun, not "fun" |
| Constraint owners state limits before design (rig, sound time, tech, budget) |
| Show work early and rough; ask one question tied to the goal, never "do you like it?" |
| Take a note for its problem, not its suggested fix |
| Close doors: a decided question stays decided (the decision log) |
| Judge at the real camera, size and context, never in the editor or a beauty shot |
| Reuse shared libraries (VFX texture library, sound library, kit pieces, asset catalogs) before making new |
| A craft may diverge from a reference for readability or budget, and says so up front |
| Consensus is not the goal; judge against the target, not majority taste |
