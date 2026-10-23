> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `orchestration`. Owner-approved (J016-D4). Evidence per row (papers, Riot transcripts, kit): `knowledge/jobs/J016-orchestration/design-jobtypes.md`. Revised by orchestrator-fixer W1 · claude-opus-5-5 · high · 2026-10-21 (J016 G3 audit): stage map, repair stage, code review, interface rounds, cross-type rules. Revised by orchestrator · claude-opus-5-5 · high · 2026-10-22 (J019, owner decision J018-D7 on G3-P2 and G3-P3): cheap passes first, crafts join early, equal-finish options at G1, risk-gated review slots, named review captures; evidence per row: `knowledge/jobs/J018-riot-craft/g3-proposals.md` appendix.

# Job recipes

Every recipe follows `rules/company.md` §4. Stages per saved workflow `.agents/workflows/jobs/job-<type>.js`, one call each: `direction` → G1 → `proof` → G2 → `build` → G3; `repair` applies a G3 change to the affected layers only. M jobs skip `proof` (it runs inside `build`). Args: `.agents/workflows/jobs/README.md`.

| Stage | Recipe rows it runs |
| --- | --- |
| `direction` | Direction leads (D1 proposals, D2 exchange, D3 direction sheet and signatures) → the recipe's direction checks (character: behaviour test) → G1 shows |
| `proof` (L) | Contract draft; Interfaces before the proof; Proof and its reviews → G2 |
| `build` | Interfaces after G2; Production order; Check-ins; Integrator; Review order (M: the proof and its reviews first) → G3 |
| `repair` | Return paths for the owner's G3 change: only the affected makers, in dependency order; then recapture and refreeze; then the review chain again on the new candidate |

- **Review orders:** scripts run first and the lead's readiness check runs last. Technical checks (reviewer, qa-lead, performance-engineer) run beside the creative order; the arrows order only the creative reviews. Every candidate with code (player code, wiring, remotes, saves) adds the `reviewer` (`code-review` + area skills, `rules/company.md` §7).
- **Risk-gated slots:** a row or slot marked *(risk: …)* runs only when the job card's Risks row names that risk; otherwise it is skipped and the card says so. The job lead fills the Risks row when the job opens and updates it when scope changes.
- **Named captures** (*rejected request*, *two-client*, *lowest graphics*, ...) are defined once in "Named review captures" at the end; the studio-operator takes them on the frozen candidate.
- **After every repair round** the candidate is recaptured and refrozen before the next review round.
- **Studio:** where a recipe names two Studio users, they take the Studio in turn (`rules/company.md` §9). Studio MCP captures stills, not video or sound: sync is judged from the Output log (event, VFX and cue start times on one clock) and labelled so; listening is an owner-confirmed line in the gate packet.

## 1. Cutscene
| Item | Recipe |
| --- | --- |
| Job lead | **film-director**; it is also the sequence integrator and keeps continuity from boards to final frames |
| Direction leads | film-director (beat contract, camera mode, staging, 2-3 approaches for the key beat) · art-director (look per beat: palette, light, shape; 2-3 reference images) · architect (runtime choice, camera ownership, streaming, skip and every ending; what to probe in Studio) · game-designer consulted for the gameplay state sheet |
| G1 shows | the beat contract; 2-3 approaches for the key beat as greybox contact sheets (shaded and black-fill) at equal finish (cross-type rules); the recommendation and why the others lost; scope, usage |
| Contract | beat sheet + shot list (`templates/jobs/beat-sheet.md`, `tools/film/shotlist.py`): stable event ids, start/end, trigger, camera, animation state, VFX cue, sound cue, player control, skip consequence, revision |
| Proof (G2) | the film-director's blocking strip and value strip first (grayscale key frames, measured with `look_check.py`), as the boards' layout input; the art-director reviews the value strip. Then storyboards (a pending board batch stops the proof before the animatic), then a timed Blender animatic with temporary sound and effect cues, on a greybox set where the set is missing; the architect runs the Studio probes it named at D1 before the animatic review. Reviews before the owner: film → art-director (composition, look reachable) → architect (cost) |
| Interfaces before the proof | animator, environment-designer, vfx-designer, sound-designer and architect state needs against the beat sheet draft (revision named); film-director merges; ≤ 2 rounds |
| Interfaces after G2 | animator ↔ character-rigger ↔ modeler (a new cast without a usable rig is a prerequisite: a character job first, `orchestration` §3; found later → `needs-decision` before the animatic) · environment-designer ↔ film (sets, landmarks, light per beat) · **vfx-designer ↔ sound-designer co-design each cue's envelope** (wind-up, peak, tail) on the event ids · ui-ux-designer (letterbox, subtitles, skip) · architect (player contract `contract-player.md` with the Code file owners table) · feature-builder (player contract, endings) |
| Production order | set and animation in parallel → VFX and sound prototype on the stable event ids early, then finish against the animation → one combined early pass of picture, VFX and sound reviewed before final polish |
| Check-ins | film reviews animation blocking before polish; art-director reviews the rough set and look before final light |
| Integrator | film-director (scene data via `shotlist.py luau`); feature-builder builds or extends the player against the contract |
| Review order | scripts (`shotlist.py check`, `log-diff`, gate) → qa-lead (skip, every ending, control and camera restored, repeat trigger, multiplayer, streaming) ∥ performance-engineer (phone) ∥ reviewer (the player code) → **film-director** (staging, timing, camera, clarity: the first-second read per shot, read order and the value lines on the captures, with the sound cue times from the Output log) → **art-director** (integrated look) → sound sync check |
| Return paths | a look problem in one shot → its maker (modeler, light, VFX); timing unchanged → sound only confirms. A visual peak moves → beat-list revision → animator, VFX and sound acknowledge and recheck. A skeleton change → animation and VFX attachments stale |

## 2. Character or creature
| Item | Recipe |
| --- | --- |
| Job lead | **art-director**; the game-designer owns its role in play |
| Direction leads | game-designer (what it does, gameplay role, signature action, camera, numbers; the reaction window for each threat's tell and the play rate of each action) · art-director (2-3 visual directions as reference images, **2-3 identity anchors**, shape language) · character-rigger + animator (motion profile; rig-costly parts such as capes and coattails flagged with a cheap fallback; when the game uses the standard R15 body for shared clips, its limits: no clavicles and no fingers, so wind-ups go into upper-torso and upper-arm range and hand reads into hand poses or swaps; a custom rig is an owner choice with its cost) |
| Behaviour test *(risk: a new enemy or creature with gameplay behaviour)* | in `direction`, after D3: the studio-operator captures plain Parts moving with the planned pattern, speed and attack radius; the game-designer judges it. No modeler brief before its verdict |
| G1 shows | 2-3 pictured directions that passed the grey pass, at equal finish (cross-type rules), anchors marked; the options that failed as a numbers list; the recommendation, the signature move, what is costly to animate; the behaviour-test verdict when it ran |
| Contract | the rig sheet (`rig-pipeline`, `templates/rig/rig-sheet.md`) + the art-director's reference set (extra views, answers on material intent) + the modeler's reference check before S1 (iconic qualities, gaps to decide, material intent per region, missing views; one note to the art-director: `modeling-design/references/reference-check.md` §7) |
| Interfaces | `rig-pipeline` S1-S2 before the proof (motion needs → rig plan → K2); the sound-designer reads the character card (feel words, size, age, material, nearest similar character) and returns a character sound plan with the signature before clips; S3-S6 after G2. Playable: the architect writes the wiring contract (`contract-wiring.md`, Code file owners) beside S0 |
| Proof (G2) | blockout at player scale + proxy rig, captured in Studio at the game camera against the game's background: the signature pose (picked from 2-3 options, black-fill at phone size) and the 2-3 hardest rig-sheet §B stress poses with the part-overlap and cap-exposure numbers (`rig_audit.py`), plus a *roster lineup*. Reviews: art-director (silhouette, anchors) → animator (usable: reads the black-fill and the stress numbers) → game-designer (role reads, against the roster lineup) |
| Production order | modeler (cuts, geometry, textures) → rigger (rig + tests) → animator (clips + timing list) → VFX and sound for its actions on the timing list → UI icon renders of the shipped model |
| Check-ins | art-director reviews the model at the game camera on the real background before texture polish (paint-overs); each hand-off is checked by the receiver (K-checks) |
| Integrator | animator for the imported revision (`rig-pipeline` S7); feature-builder when it is wired into gameplay |
| Review order | scripts (`model_audit.py`, `rig_audit.py`, `clip_check.py`) → consumer K-checks → **art-director** (identity, silhouette, value at the game camera) → **game-designer** (role reads in play) → performance-engineer (on-screen count, phone); reviewer beside them when it is wired into gameplay |
| Return paths | a costume part blocks motion → rig note → modeler (one exact note); a look change forced by a limit → owner with both options rendered |
| Variant mode (skin, recolour, themed version) | fixed: base rig, clips, identity anchors; open: costume, palette. Skip S1 unless there are new moving parts. No geometry change (palette only): the model step is texture-only and S4-S6 are skipped on the released base rig. Selling it is a second job (feature, with money: `orchestration` §2). Review adds: the base is recognisable in every view; no disadvantage for players who own it; *(risk: sold variant)* qa-lead checks the variant changes no stat, collision, hit box or socket position against the base (`testing` PF-13) |

## 3. Stage
| Item | Recipe |
| --- | --- |
| Job lead | **environment-designer** (owns and integrates the place) |
| Decision rights | routes, cover, sight lines, blocking surfaces: **game-designer**; look: art-director; budgets: performance-engineer. Art stays inside the approved greybox; composition changes are asked for, never made silently |
| Direction leads | game-designer (the stage's job, route graph, encounters, pacing, its hook; the route table in seconds at walk speed and the hazard sheets) · art-director (2-3 key-place reference images, value band) · environment-designer (built-where, landmarks, ambience idea) · performance-engineer (budget) |
| G1 shows | the route graph with the 2-3 layout options considered (top-down route sketches with route times) and why the others lost; the **blueprint draft** (so the owner approves the blueprint before any building, J008); the first view; 2-3 pictured looks at equal finish (cross-type rules); the recommendation |
| Contract | route graph + blueprint approved at G1 (game-designer + environment-designer), with the route table and hazard sheets, refined in the proof stage: a refinement that changes an approved item (route, footprint, landmark, heights) goes to the owner before the greybox is built; other refinements are listed at G2 or G3 · the read plan (environment-designer), built on the route table, hazard sheets and read rank and on the art-director's value bands and reserved colours · ambience map (environment → sound, VFX) · kit piece list (environment → modeler) with the floor-material list to the sound-designer before materials are built · a player-size scale reference in every space |
| Proof (G2) | a playable greybox in Studio: walk-test and playtest captures, first view, landmark read, route times; the grey value pass (key light direction chosen in grey; first view measured). Reviews: game-designer (judges the play captures) → art-director (composition and value in blockout) → performance-engineer |
| Production order | art blockout snapped to the approved greybox → kit pieces (modeler) and art production → light and atmosphere → ambience (sound) and ambient VFX. Playtests continue during art; lighting and polish only after the space plays well |
| Check-ins | the game-designer checks placement, materials, set dressing and VFX placement as the build grows; the art-director reviews 2-3 grey lighting variants at the game camera before the light pass, and gives a paint-over on the first rough art over the greybox before set dressing |
| Integrator | environment-designer (Studio driver for place content) |
| Review order | scripts (scene audit, budgets, floating parts) → **game-designer** judges the studio-operator's playtest captures (play wins over art readability) → **art-director** (camera set plus the *layer cuts*, *environment-only*, *lowest graphics* and the main landmark's mask capture with the depth and head-height row markers; the environment band, reserved colours and focus numbers beside the value ladder and rest areas next to detail) → sound and VFX ambience check → qa-lead (collision, falls, stuck spots; ledges against the jump height; collision and cover diffed against the approved blockout; every gameplay cue present at the lowest and highest graphics quality; spawn positions and facing) |
| Return paths | an art change that alters sight lines or collision → game-designer; a new surface material not on the floor-material list → sound may refuse it for time → environment picks another |

## 4. UI screen
| Item | Recipe |
| --- | --- |
| Job lead | **ui-ux-designer**; the game-designer owns the player's decision |
| Direction leads | game-designer (the decision the screen serves; the information list per moment with read times, the read rank and the screen's feedback stack, before the UI flow: `preproduction/references/documents.md` §6, §9; shops and odds: progression-designer + `platform-policy`) · ui-ux-designer (state list, focus map, flow, 2-3 target reference images in the game's style book) · art-director (style cohesion) · feature-builder or architect (data and remotes available) |
| G1 shows | the decision record; the flow sheet with taps per task; 2-3 wireframe options with real content and the recommended pick with its reasons; the grey value pass (luminance image + `look_check.py value --compare-subjects` numbers); 2-3 pictured style targets at equal finish (cross-type rules) |
| Contract | state map + spec (`content/ui/<screen-id>/spec.md`): states, events, data fields, sizes for the smallest phone; the code contract `contract-code.md` with the Code file owners, written by the architect after the needs rounds |
| Proof (G2, L only) | a clickable Figma prototype of every state at phone size; the owner judges motion feel at normal speed on it. Reviews: game-designer (decision clear) → art-director → feature-builder (buildable) |
| Production order | *(risk: a purchase or paid reveal)* reviewer plan check (as §5) → the motion storyboard on one beat list with the sound-designer (UI cue list keyed to the screen's event names) and, when rewards fly from the world, the vfx-designer (world-to-HUD beats) → Figma build to the target image → handoff → feature-builder implements (`ui-basics`) ∥ UI sounds and UI effects from the VFX library |
| Integrator | feature-builder; test hooks and debug log at the wiring step (cross-type rules) |
| Review captures (studio-operator, for the ui-ux-designer's slot) | Device Simulator stills of every state at the *smallest phone* and a PC size; the screen over the busiest gameplay moment; frame folders (`f###_<ms>ms.jpg`) of each press and key transition by the S-33 capture rules (cropped to the control with a margin, or inside its face when the world moves behind it; more idle frames before the press than after; the press frame's ms noted); *(risk: paid reveal)* one capture per *paid-reveal tier*; a *rejected request*; reduced motion on; the largest text size |
| Review order | gate PASS + reviewer (code) → qa-lead (every state, touch and gamepad, longest text; the truth rows: a rejected request and the pending path, counters exact after a burst and a buy during the count-up, refusals at the control, reduced motion on, the *smallest phone*) → **ui-ux-designer** against its target image on the review captures → *(risk: shop, odds or progress screen)* **progression-designer** (every shown number against the display fixtures, odds rows equal to the server's data, the next goal and its requirement readable at two timeline points, each reward's tier and text name equal to the tier table; `progression-craft/references/data-handoff.md` §4-§5) → **art-director** → **game-designer** (the decision works); the owner judges motion feel at normal speed on the Studio build |
| Return paths | a state or readability failure returns to the state map or layout, not to styling; a read-order failure (the first-noticed element is not rank 1 at phone fit) returns to the grey value pass |

## 5. Gameplay feature
| Item | Recipe |
| --- | --- |
| Job lead | **game-designer** (player behaviour and acceptance); technical lead **architect** |
| Direction leads | game-designer (feature spec: what the player does, feels, decides; acceptance cases incl. failures; the feedback stack per action) · architect (engine features, risky claims, probes, client/server placement, file owners) · progression-designer for numbers · `platform-policy` for money, odds, ads · animator consulted when a player action has a gameplay window or feedback (frame lengths and named markers, such as contact, release and impact, for the spec's timing stages, before any clip is keyed) · sound-designer consulted when the feature has player feedback (reads the feedback stack, returns the cue list per state change or the reason for none) |
| G1 shows | the behaviour in player words, the risky claims and how the proof tests them, scope, usage |
| Contract | feature contract: behaviours, state names, events (the hooks UI, VFX and sound attach to), tuning keys in data, acceptance checks written by the briefer; the feedback stack per action with the denial reasons and their messages (`preproduction/references/documents.md` §6), filled before the builder's contract; the player-facing rows and the test hooks the builder delivers, in the qa-lead's trace table at contract time (`testing/references/player-facing.md` §3); *(risk: the feature adds rewards)* the progression-designer's reward and celebration tier table (tier, trigger, measured rate per event) before UI, VFX and sound production |
| Interfaces before the proof | before the architect freezes the plan: the animator (timing list draft for actions with motion), vfx-designer (importance per viewer, caps, per-viewer and reduced variants, budget block), sound-designer (cue ids, voice cap, merge needs) and ui-ux-designer (states, denial reasons, motion-table rows) state needs against the feedback stack (revision named); the architect merges them into the presentation contract (`architecture/references/presentation-contract.md`); ≤ 2 rounds |
| Proof (G2) | the skeleton as a playable grey-box prototype in Studio (feature-builder, minimal: the server rule and result path playable with named stand-ins and the sound-designer's temp cues) that tests the risky claim and the fun; the studio-operator plays it and the game-designer judges the play captures. Visible parts: the ui-ux-designer's target image and the vfx-designer's key frames are made beside the prototype and shown at G2 |
| Production order | architect plan with the presentation contract → *(risk: money, saves, remotes, trades or paid random items)* reviewer plan check (one exchange: invariant cards, request and result shapes, grant ids, the presentation contract's attempt, confirmed, pending, denied and reduced rows; `code-review/references/review-method.md` §7) → feature-builder skeleton (failing case first; the G2 proof for L) → presentation pass: UI, VFX and sound against the contract's event ids ∥ progression tables → worst-case pass; the qa-lead writes protected acceptance tests from its trace table |
| Integrator | feature-builder; test hooks and debug log at the wiring step (cross-type rules) |
| Review order | gate PASS → reviewer ∥ qa-lead ∥ performance-engineer (if heavy) ∥ architect (cost and contract, `architecture/references/review-checklist.md`) → **game-designer** judges the play captures (a *rejected request*, a *slow confirmation*, *two-client*, *grayscale, sound off, reduced motion*, the real rate and a burst, *lowest graphics*) → **art-director** for visible parts |
| Return paths | wrong incentives → game-designer or progression-designer; wrong behaviour → feature-builder; a fourth review round on one approach → reconsider with the architect |

## 6. Effect
| Item | Recipe |
| --- | --- |
| Job lead | **vfx-designer** |
| Direction leads | game-designer (the gameplay event, its timing window, what must stay readable) · vfx-designer (frame script, importance, technique) · sound-designer (the sound's job: cue, feedback or emotion) · art-director only when the effect sets a new look, adds a colour role or adds a shape-code entry |
| Contract | one event timeline (wind-up, hit, tail; times in seconds with the source frame) shared by the animator's timing list, the VFX frame script and the sound cue card, same event ids |
| Cooperation | VFX and sound co-design the envelope before either builds. Gameplay length comes from design; the animator sets beats inside it and sends the blocking markers (draft timing list) to VFX and sound before either builds; a retime is re-sent in the same hand-back. VFX follows; sound keys to the picture events |
| Proof | the blocking pass: placeholder sprites, real sizes and timing, the real truth edge; clip numbers for every case and at most 4 key stills (build, peak, result, tail), at the game camera in a busy scene, with the temporary sound's cue times in the Output log (MCP captures are stills; listening is owner-confirmed); checked in before any texture pick; the art-director checks its grey and black-fill stills (`vfx-design/references/review.md` §I3). For an M job shown at G3 |
| Production order | temp sound on the blocking markers (owner check-in on the first playable) → VFX textures and build → final sound processing only after the timing-list revision is locked |
| Integrator | feature-builder or quick-builder wires the spec, with the test hooks at the wiring step (cross-type rules; here a rate trigger that logs live copies, a hook that makes the server reject the request, and a see-through debug part of the server's hit shape); studio-operator records the capture |
| Review order | scripts (budget numbers, `tools/vfx/flash_count.py`) → *(risk: gameplay truth: a danger area, an outcome layer on a request, a paid reveal, a frequent effect)* qa-lead protected acceptance beside the creative order (`testing` PF-02 rejected request, PF-04 drawn area on the debug shape over 20 fuse runs, PF-06 identical windups, PF-10 100 triggers and a burst) → **game-designer** (does it hide information players need? on the *hit-shape overlay*, *two-client* and *rejected request* captures) → **art-director** (brightest point where the eye must go; value ladder; on the coloured build, after its blocking check) → sound sync from the Output log cue times (listening: owner-confirmed); reviewer beside them when wiring code changed |
| Return paths | a timing change → the timing-list revision → VFX and sound recheck |

## 7. Marketing art
| Item | Recipe |
| --- | --- |
| Job lead | **marketing** |
| Direction leads | marketing (the hook; the brief's strategy names the hero of the image) · game-designer (the art must tell the truth about play) · art-director (style, identity anchors) · animator consulted when a character is the hero (the signature move's key pose at the still's camera) · trend-scout optional (what competitors show now) |
| G1 shows | a labelled warm-up of the typical idea, then 3-5 rough thumbnails from different hooks (layout, story or camera), each at the real slot size with its sheet; the preferred one stated with reasons tied to the sell list |
| Proof (G2 = green light) | on the chosen thumbnail: silhouette, a 3-value study and 2-3 light set-ups compared; every planned crop's safe square marked; tested at real size (`thumb_check.py`) and in the real layout; after green light the big shapes stay |
| Production order | render → colour and rebalance → detail and polish → a layered file (foreground, midground, background, effects, light, title) → the family of crops planned at the start (`marketing-craft/references/image-pipeline.md` §1) |
| Integrator | marketing |
| Review order | scripts (`thumb_check.py`, `look_check.py` value) → **art-director** (identity read largest, silhouette, style rules) → **game-designer** (truthful to play) |
| Return paths | a wrong face or identity draws the first note every time: fix it before the review |

## Not recipes
- **New game pre-production:** the `preproduction` skill's growth order; it produces the briefs these recipes consume.
- **Live update or event:** the live-ops plan is split by the lead into jobs of the types above. For a job that comes from a live-ops update brief for an event, theme, variant line or limited item: the live-ops concept round (2-3 premise one-pagers, owner pick) counts as that job's proof, and a live-ops review slot runs after integration and before G3: the event review E-01 to E-19 on its capture set (`live-ops-craft/references/event-review.md` §2-§3).

## Cross-type rules (all types)
| Rule |
| --- |
| One written target experience shared by design, art and engineering before craft work; name the type of fun, not "fun" |
| Constraint owners state limits before design (rig, sound time, tech, budget) |
| Show work early and rough; ask one question tied to the goal, never "do you like it?" |
| Take a note for its problem, not its suggested fix |
| Gates close doors: a decided question stays decided (the decision log); the options not picked are recorded closed with a "may return only if" condition, and later briefs carry them in `avoid` |
| Judge at the real camera, size and context, never in the editor or a beauty shot |
| Reuse shared libraries (VFX texture library, sound library, kit pieces, asset catalogs) before making new |
| A craft may diverge from a reference for readability or budget, and says so up front |
| Consensus is not the goal; judge against the target, not majority taste |
| A consumer states its needs against the contract draft before its producer builds; a craft that keys from another's output (VFX and sound from animation, rigger from modeler, sound from the floor-material list) is consulted at direction or at the needs round, not after the build. The recipe rows say where |
| Options shown at G1 (directions, layouts, approaches, wireframes, thumbnails): 2-3 (marketing 3-5), each from its own hook, at equal finish, with the labelled warm-up as the baseline; each shown in colour, grey and black-fill at the size players see it; one recommendation with the reasons the others lost; options that failed a check are listed with the reason, never shown as equals (`reference-images`, `orchestration/references/gates-and-feedback.md` §3) |
| The proof is the cheapest pass that tests the read: grey, black-fill, blocking, proxy, placeholders, temp sound; nothing polished. Value and light are chosen in grey before colour |
| One marker list per job where animation, VFX and sound meet; a retime is a contract change to all of them the same turn (`orchestration/references/briefs-and-handoffs.md` §3) |
| Every gate packet carries the could-not-check list and owner-confirmed lines for feel at normal speed and, when the job has sound, two listens: the key event alone, then the full mix, each on a phone speaker and on headphones |
| A job whose result the server confirms adds a *rejected request* capture to its review evidence: no success layer plays |
| With player code (feature, effect, UI), the integrator delivers the Studio-only test hooks and the debug log at the wiring step, before any partner's first capture (`engineering-craft/references/presentation.md` §9; hook names: `testing/references/player-facing.md` §3) |
| Risk-gated review slots run only for the risks the job card names; a slot skipped for no risk is a line in the card, not a silent gap |

## Named review captures
The studio-operator takes them on the frozen candidate; a recipe row names the ones its reviewers need. Each capture names its camera, size and place.

| Name | What it shows | Needs |
| --- | --- | --- |
| rejected request | the server refuses the request: no outcome cue, celebration or balance change; the refusal plays | hook `Reject` |
| slow confirmation | the pending state under added latency; no early success | hook `DelayMs` |
| two-client | the busiest expected moment from the acting or threatened player and a bystander, side by side | two Studio clients |
| hit-shape overlay | the server's hit shape as a see-through part over the drawn area at warning, contact and end | hook `DebugShape` |
| grayscale, sound off, reduced motion | the read with colour, sound and motion each removed | reduced-motion setting in the game |
| lowest graphics | the busiest view at the lowest graphics quality (shadows and detail dropped) | Studio quality setting |
| layer cuts, environment-only | the same view with effects off, UI off, and UI, effects and characters off together | the stage's capture recipe |
| roster lineup | the new character next to existing roster members at the same scale, at the game camera | released roster models |
| paid-reveal tier | one frame folder per tier from the press frame, the lowest tier twice | hook `Outcome` or `Seed` |
| smallest phone | Device Simulator at the smallest supported phone | the game profile's device list |
