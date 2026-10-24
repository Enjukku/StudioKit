> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `orchestration`. Owner-approved (J016-D4). Evidence per row (papers, Riot transcripts, kit): `knowledge/jobs/J016-orchestration/design-jobtypes.md`. Revised by orchestrator-fixer W1 · claude-opus-5-5 · high · 2026-10-21 (J016 G3 audit): stage map, repair stage, code review, interface rounds, cross-type rules. Revised by orchestrator · claude-opus-5-5 · high · 2026-10-22 (J019, owner decision J018-D7 on G3-P2 and G3-P3): cheap passes first, crafts join early, equal-finish options at G1, risk-gated review slots, named review captures; evidence per row: `knowledge/jobs/J018-riot-craft/g3-proposals.md` appendix. Revised by orchestrator-writer · claude-opus-5-5 · default · 2026-10-24 (J023, owner G1 J023-D5; binding design `knowledge/jobs/J023-flow-speed/design.md` B-G): lighter direction (choice owners propose, constraint owners write limits sheets, no sign-off), one joint needs meeting, M without a proof stage, selective recheck, captures on the studio-operator, short agents. Rewritten by J024 writer · claude-opus-5-5 · default · 2026-10-24 (J024 design, `knowledge/jobs/J024-flow-cuts-r2/design.md` §1-§9): no proof stage and no G2, no roughs, D1 plan + N1 needs and limits tables + merge, one capture-and-scripts run, fewer reviewers, per-type rows. Revised by orchestrator (side session) · claude-opus-5-5 · default · 2026-10-24 (J027): building a game from the design baseline.

# Job recipes

Every recipe follows `rules/company.md` §4. Stages per saved workflow `.agents/workflows/jobs/job-<type>.js`, one call each: `direction` → G1 → `build` → G3; `repair` applies a G3 change to the affected layers only. **No job type has a proof stage or G2** (J024, owner J023-D6, D7): a call with `stage: "proof"` returns `blocked` before any agent ("no proof stage (J024): direction → G1 → build → G3"). L and M differ only in direction: L brings 2-3 options at equal finish (pictured) and may set a new look; M brings one direction inside the approved style. The build stage is the same for both sizes. Args: `.agents/workflows/jobs/README.md`.

| Stage | Recipe rows it runs |
| --- | --- |
| `direction` | **D1 plan** (one run, the job lead: the direction and the type's plan, revision 1, written to hold for every option) → **N1** (in parallel, one run each: the Needs row crafts write needs tables, the Limits row constraint owners write limits tables; each reads only the plan and its own brief) → **merge** (one run, the job lead: `direction.md` with every conflict, its owner and resolution; plan revision 2; the G1 packet rows; the conditional crafts the plan needs) → **N2** and a second merge only on a conflict the job lead cannot settle (only those crafts, only the conflicting rows, once) → G1 shows |
| `build` | Production order (one run per craft, the plan's dependency order; conditional crafts only when the merge named them) → Integrator → Capture and scripts → Review order → G3 |
| `repair` | Return paths for the owner's G3 change: only the affected makers, in dependency order, with capped repair briefs (`rules/messages.md` §6); then the capture-and-scripts run on the refrozen candidate; then the review chain (round 0 in full, later rounds selective) |
| `proof` | none: refused with `blocked` (J024) |

- **No roughs (J024).** Each craft builds the real, polished part once, in one run. Removed everywhere: rough, temp, prototype, blockout, greybox, proxy, value-strip, board, animatic, first-spec and proof passes, every check-in between a rough and a final, and every review of a rough. A craft may rough things out inside its own run (its own blockout, proxy pose, quick probe); it never hands a rough on and nothing waits on it. A check that caught real problems is a measured self-check in the maker's run, measured again in the integrated review (the rigger's posed-proxy clearances, J005; the film-director's 4:3-centre read, J015).
- **Needs and limits** (`rules/company.md` §4 step 2; format `rules/messages.md` §4, `templates/jobs/needs-table.md`): ≤ 12 rows per table, an `omitted:` line for the rest. Each craft confirms the merged plan or names an incompatibility in its first build hand-back (`needs-decision`). Build never re-asks for timings, cue ids, joint lists or materials; a later need is a contract change.
- **Conditional crafts** ("only if the plan lists", "when `<flag>`") are switched by an explicit field in the D1 or merge hand-back, or by an arg or a `risks` token; off by default.
- **Production order:** marker producers before consumers (animator → VFX → sound; modeler → rigger → animator; UI design → builder); independent crafts run in parallel (≤ 5 at once; one Studio, Blender and browser user at a time). VFX writes each envelope first; sound answers on it.
- **Capture and scripts:** one `studio-operator` run (Sonnet) per review round on the frozen candidate: it imports or plays it, runs the gate and the type's measuring scripts (`look_check.py`, `clip_check.py`, `thumb_check.py`, scene audit, `shotlist.py` diff, budgets), captures key frames (numbers for every case, images at key frames and where a number fails), takes the named captures the row lists, and reads the Output-log cue times. Its hand-back adds `visual_flags` (measured visual numbers outside their range; `[]` when none) and `cue_log` (event, VFX and cue start on one clock). A scripts FAIL stops the other reviews until it is fixed. Studio probes a maker needs also run on the studio-operator; Opus roles never take routine captures; a maker's own check of its import or build stays with the maker.
- **Review orders:** after capture and scripts, the reviewers in the type's row; the lead's readiness check runs last. The **job lead's integrated review** always runs: it measures key frames itself (`look_check.py` at the game camera and phone size; the J015 near-black shot), checks the gameplay read, and checks sound sync from `cue_log` against the marker list. By rule (`rules/company.md` §7): the `reviewer` when the candidate changed code; the `qa-lead` only for the player-facing logic the row names; the `performance-engineer` only when `risks` names `performance`; the `art-director` only with a new look (`newLook: true`; marketing `launch: true`) or when `visual_flags` is not empty (it then reviews in that round). The sound-designer, game-designer, progression-designer, architect, VFX designer, animator and feature-builder do not review, except as a type's job lead.
- **Risk-gated slots:** a row or slot marked *(risk: …)* runs only when the job card's Risks row names that risk; otherwise it is skipped and the card says so. The job lead fills the Risks row when the job opens and updates it when scope changes.
- **Named captures** (*rejected request*, *two-client*, *lowest graphics*, ...) are defined once in "Named review captures" at the end; the studio-operator takes them in the capture-and-scripts run.
- **After every repair round** the candidate is refrozen and the capture-and-scripts run repeats before the next review round. Round 0 runs the whole review order; a later round reruns only the capture-and-scripts run, the qa-lead where the chain has one, the `reviewer` when code changed, every reviewer with a blocking finding, and the dependents of a repaired layer (the job lead's integrated review after any visual or timing repair; the art-director after a visual repair, only when it is in the chain); every other verdict is carried (`rules/company.md` §7, Selective recheck). Limits: 2 rounds, code 3.
- **Studio:** where a recipe names two Studio users, they take the Studio in turn (`rules/company.md` §9). Studio MCP captures stills, not video or sound: sync is judged from the Output log and labelled so; listening is an owner-confirmed line in the G3 packet.
- **Quality risks this flow accepts (J024 design §9).** With no G2, the owner first sees built work at G3: a wrong big shape costs a repair of finals, not a cheap proof; the plan agreed at G1 with pictures and selective repairs are the mitigation. Without a separate rough review, the catches of the J015 greybox and the J005 posed proxy rest on the maker's in-run self-check plus the integrated review. With fewer domain reviewers, the gameplay read, sound sync and prices are judged by the job lead and measured numbers; listening stays owner-confirmed at G3. Fewer runs can mean bigger runs: measure real-job tokens with `tools/usage_report.py`.

## 1. Cutscene
| Item | Recipe |
| --- | --- |
| Job lead | **film-director**; it is also the scene-assembly integrator and keeps continuity from the beat sheet to final frames |
| D1 plan | L: 2-3 approaches for the key beat (image prompt rows); M: one. The beat sheet (`templates/jobs/beat-sheet.md`) and the shot list (`tools/film/shotlist.py`): the beat contract and camera mode, stable event ids, every shot's camera (size, angle, FOV, move) and length, the marker list, the gameplay state sheet and every ending; no value strips, boards or animatic. A new cast without a usable rig stops direction with `needs-decision` and a linked character job (`orchestration` §3), before build |
| Needs (N1) | animator, environment-designer, vfx-designer, sound-designer; ui-ux-designer only if the plan lists on-screen UI beyond the stock player (title cards, subtitles, choices): the merge returns it as `build_args.ui`, and the lead passes it to `build` as the `ui` arg (a workflow call cannot carry the merge result to the next call) |
| Limits (N1) | architect (player contract `contract-player.md`, camera ownership, streaming, skip and every ending, code file owners) · art-director when `newLook` · performance-engineer when `performance` |
| G1 shows | the beat contract and the agreed beat sheet; L: 2-3 approaches for the key beat at equal finish (cross-type rules); the recommendation and why the others lost; scope, usage |
| Production order | environment-designer final set (lit to the plan's value and light per beat) ∥ animator clips + import → vfx-designer on the marker list → sound-designer on the VFX envelope → ui-ux-designer if listed → feature-builder: the player, skip and every ending against the player contract |
| Integrator | film-director (scene data via `shotlist.py luau`) |
| Capture and scripts | `shotlist.py check` and `log-diff`, gate; key frames per shot at the game camera and phone size with the 4:3-centre read; Output-log cue times |
| Review order | **film-director** integrated (staging, timing, camera, clarity: the first-second read per shot, read order and value lines on the captures; sound sync from `cue_log`) ∥ qa-lead (always: skip, every ending, control and camera restored, repeat trigger, multiplayer, streaming) ∥ reviewer (always: the player code); art-director and performance-engineer by rule |
| Return paths | a look problem in one shot → its maker (modeler, light, VFX); timing unchanged → sound only confirms. A visual peak moves → beat-sheet revision → animator, VFX and sound acknowledge and recheck. A skeleton change → animation and VFX attachments stale |

## 2. Character or creature
| Item | Recipe |
| --- | --- |
| Job lead | **art-director**; the game-designer gives the role in play through its needs table |
| D1 plan | L: 2-3 visual directions (image prompt rows) with 2-3 identity anchors and the shape language; M: one. The character sheet: read plan, size at the game camera, moves (signature action), sell list, costly parts |
| Needs (N1) | game-designer (gameplay role, signature action, camera, numbers; the reaction window for each threat's tell and the play rate of each action) · character-rigger (rig plan: `rig-pipeline` S0 sheet + S2 cuts, joints and pivots; rig-costly parts such as capes with a cheap fallback; with the standard R15 body for shared clips, its limits: no clavicles and no fingers; its posed-proxy clearances measured inside its own run) · animator (S1 motion needs) · modeler (its reference check items) · vfx-designer and sound-designer (the sockets, markers and materials they key from; the sound-designer reads the character card) |
| Limits (N1) | architect (wiring contract `contract-wiring.md`, code file owners) when `playable` · performance-engineer when `performance` |
| Behaviour test *(risk: new-enemy)* | in `direction`, after the merge: the studio-operator captures plain Parts moving with the planned pattern, speed and attack radius; the game-designer judges it. No model brief before its verdict |
| G1 shows | L: 2-3 pictured directions at equal finish (cross-type rules), anchors marked; the options that failed as a numbers list; the agreed character sheet; the recommendation, the signature move, what is costly to animate; the behaviour-test verdict when it ran |
| Production order | art-director reference set (the final model sheet from the G1 pick: extra views, material intent; a pending image batch stops the stage) → modeler final geometry from the approved reference in one run (reference check, cuts, caps and sockets, UVs, textures, icon renders, its own silhouette gate and audit) → character-rigger (S4 check, S5 rig, tests) → animator (S6 acceptance, S7 clips + timing list + import) → vfx-designer → sound-designer on the timing list; feature-builder wiring when `playable` |
| Integrator | animator for the imported revision (`rig-pipeline` S7); feature-builder when it is wired into gameplay |
| Capture and scripts | `model_audit.py`, `rig_audit.py`, `clip_check.py`; at the game camera on the game's background: the signature pose in black-fill at phone size, the hardest rig-sheet §B stress poses with the part-overlap and cap-exposure numbers, the *roster lineup* |
| Review order | **art-director** integrated (identity, silhouette, value at the game camera, the role read against the roster lineup) ∥ reviewer and qa-lead when `playable`; performance-engineer by rule |
| Return paths | a costume part blocks motion → rig note → modeler (one exact note); a look change forced by a limit → owner with both options rendered |
| Variant mode (skin, recolour, themed version) | fixed: base rig, clips, identity anchors; open: costume, palette. Skip S1 unless there are new moving parts. No geometry change (palette only): the model step is texture-only and S4-S6 are skipped on the released base rig. Selling it is a second job (feature, with money: `orchestration` §2). Review adds: the base is recognisable in every view; no disadvantage for players who own it; *(risk: sold variant)* qa-lead checks the variant changes no stat, collision, hit box or socket position against the base (`testing` PF-13) |

## 3. Stage
| Item | Recipe |
| --- | --- |
| Job lead | **environment-designer** (owns and integrates the place) |
| Decision rights | routes, cover, sight lines, blocking surfaces: **game-designer** (its needs table; the agreed blueprint); look: art-director; budgets: performance-engineer. Art stays inside the agreed blueprint and route graph; composition changes are asked for, never made silently |
| D1 plan | L: 2-3 key-place directions (image prompt rows); M: one. The blueprint: spaces, landmarks, first view, built-where, light plan, ambience zones (the ambience map draft), the kit piece list, a player-size scale reference per space |
| Needs (N1) | game-designer (route graph, route table in seconds at walk speed, hazard sheets, read rank, the placement it needs) · modeler (new kit pieces) · vfx-designer (ambient effects) · sound-designer (ambience zones; the floor-material list before materials are built) |
| Limits (N1) | performance-engineer when `performance` · art-director when `newLook` (value band, reserved colours) |
| G1 shows | the route graph with the layout options considered and why the others lost; the agreed blueprint (the owner approves it before any building, J008); the first view; L: 2-3 pictured looks at equal finish; the recommendation |
| Production order | modeler new kit pieces, only if the plan lists them → environment-designer builds the final place (terrain, dressing, light, atmosphere, sky; key light chosen in grey and the scene audit inside its own run) → vfx-designer ambient effects ∥ sound-designer ambience → environment-designer places the ambience and freezes |
| Integrator | environment-designer (Studio driver for place content) |
| Capture and scripts | scene audit, budgets, floating parts; route times at walk speed, ledges against the jump height, collision and cover against the blueprint, spawn positions and facing; the camera set, *layer cuts*, *environment-only*, *lowest graphics* and the main landmark's mask capture |
| Review order | **environment-designer** integrated (gameplay read first: routes, landmarks, first view against the route numbers; then value and light; ambience from `cue_log`); art-director and performance-engineer by rule |
| Return paths | an art change that alters sight lines or collision → game-designer; a new surface material not on the floor-material list → sound may refuse it for time → environment picks another |

## 4. UI screen
| Item | Recipe |
| --- | --- |
| Job lead | **ui-ux-designer** |
| D1 plan | L (`newLook`): 2-3 target images (prompt rows) in the game's style book; M: one. The screen contract: the decision the screen serves, every screen and state (empty, error, loading, disabled with its reason, reward, pending), the information list with read rank, the flow with taps per task, the focus map, the motion beat list on the screen's event names |
| Needs (N1) | feature-builder (data fields, events, remotes) · sound-designer (UI cue list on the event names) · vfx-designer only if the plan lists UI effects (world-to-HUD beats) |
| Limits (N1) | architect (code file owners, interface, `contract-code.md`) · progression-designer when `shop` (prices, odds rows, progress numbers; `platform-policy`) · art-director when `newLook` · performance-engineer when `performance` |
| G1 shows | the decision record; the flow sheet with taps per task; the agreed screen contract; L: 2-3 target images at equal finish (cross-type rules); the recommendation |
| Production order | *(risk: a purchase or paid reveal)* reviewer plan check (as §5) → ui-ux-designer final Figma build to the target image and the Roblox handoff (motion on the plan's beat list) → feature-builder implements and integrates in one run (`ui-basics`) ∥ sound-designer UI cues; vfx-designer if listed |
| Integrator | feature-builder; test hooks and debug log at the wiring step (cross-type rules) |
| Capture and scripts | gate; `look_check.py value --compare-subjects`; Device Simulator stills of every state at the *smallest phone* and a PC size; the screen over the busiest gameplay moment; frame folders (`f###_<ms>ms.jpg`) of each press and key transition by the S-33 capture rules; *(risk: paid reveal)* one capture per *paid-reveal tier*; a *rejected request*; reduced motion on; the largest text size |
| Review order | **ui-ux-designer** integrated against its target image (rank 1 read first at phone fit; sound sync from `cue_log`) ∥ reviewer (always: the screen code) ∥ qa-lead when `shop`, `paid-random`, `server-result` or `shop-screen` (every state, touch and gamepad, longest text; the truth rows: a rejected request and the pending path, counters exact after a burst, refusals at the control; every shown number against the display fixtures and odds rows equal to the server's data, `progression-craft/references/data-handoff.md` §4-§5); art-director and performance-engineer by rule. The owner judges motion feel at normal speed at G3 |
| Return paths | a state or readability failure returns to the screen contract or layout, not to styling; a read-order failure (the first-noticed element is not rank 1 at phone fit) returns to the read rank |

## 5. Gameplay feature
| Item | Recipe |
| --- | --- |
| Job lead | **game-designer** (player behaviour and acceptance); technical lead **architect** |
| D1 plan | L: 2-3 approaches; M: one. The feature contract: behaviours in player words, state names, events (the hooks UI, VFX and sound attach to), failure cases with the denial reasons and their messages, acceptance cases, the feedback stack per action, tuning keys in data, the risky claims and how build tests them, and the presentation list (which of UI, VFX, sound and animation it needs) |
| Limits (N1) | architect (presentation contract `architecture/references/presentation-contract.md`, engine features, probes, client/server placement, code file owners) · progression-designer when `numbers` (*(risk: rewards)* the reward and celebration tier table) · `platform-policy` for money, odds, ads · performance-engineer when `performance` |
| Needs (N1) | ui-ux-designer, vfx-designer, sound-designer, animator: each only if the presentation list names it |
| G1 shows | the behaviour in player words, the risky claims and how build tests them, the agreed feature contract, scope, usage; pictures only where the contract has visible parts |
| Production order | *(risk: money, saves, remotes, trades or paid random items)* reviewer plan check (one exchange: invariant cards, request and result shapes, grant ids, the presentation contract's attempt, confirmed, pending, denied and reduced rows; `code-review/references/review-method.md` §7) → qa-lead protected acceptance tests first, from its trace table (`testing/references/player-facing.md` §3) → feature-builder builds and integrates (failing case first) ∥ progression tables when `numbers` → UI, VFX, sound, animator, each if listed, against the contract's event ids |
| Integrator | feature-builder; test hooks and debug log at the wiring step (cross-type rules) |
| Capture and scripts | gate; the play captures: a *rejected request*, a *slow confirmation*, *two-client*, *grayscale, sound off, reduced motion*, the real rate and a burst, *lowest graphics* |
| Review order | **game-designer** integrated on the play captures (gameplay read; sound sync from `cue_log`) ∥ reviewer (always) ∥ qa-lead (always: the protected suite); art-director and performance-engineer by rule |
| Return paths | wrong incentives → game-designer or progression-designer; wrong behaviour → feature-builder; a fourth review round on one approach → reconsider with the architect |

## 6. Effect
| Item | Recipe |
| --- | --- |
| Job lead | **vfx-designer** |
| D1 plan | L (`newLook`): 2-3 options; M: one. The effect timeline: frame script (wind-up, hit, tail; times in seconds with the source frame), the marker list (the same event ids for the animator's timing list, the VFX frame script and the sound cue card), the importance tier, play rate and worst-case count, the technique |
| Needs (N1) | sound-designer · feature-builder (wiring, hooks, the server's truth edge) · animator when `animated` |
| Limits (N1) | game-designer when `danger-area` or `frequent-effect` (the gameplay window, what must stay readable) · art-director when `newLook` · performance-engineer when `performance` |
| G1 shows | the agreed effect timeline; L: the options at equal finish; the recommendation |
| Production order | animator final clip + import when `animated` (timing list) → vfx-designer final spec, once (its own blocking and texture pick inside its run) → sound-designer cues on the VFX envelope → feature-builder (quick-builder when `small`) wiring, with the test hooks (a rate trigger that logs live copies, a hook that makes the server reject the request, a see-through debug part of the server's hit shape) |
| Integrator | the wiring builder |
| Capture and scripts | budget numbers, `tools/vfx/flash_count.py`, clip numbers for every case and at most 4 key stills (build, peak, result, tail) at the game camera in a busy scene; the *two-client* and *rejected request* captures; Output-log cue times; measured rows *(risk: danger-area)* `testing` PF-04, the drawn area against the debug shape over 20 fuse runs, with the *hit-shape overlay* capture, and *(risk: frequent-effect)* PF-10, 100 triggers and a burst against the cap |
| Review order | **vfx-designer** integrated (does it hide information players need; brightest point where the eye must go; sound sync from `cue_log`) ∥ reviewer (always: the wiring) ∥ qa-lead only when `server-result` (`testing` PF-02 rejected request) or `paid-random` (PF-06 identical windups); `danger-area` and `frequent-effect` are measured rows in the capture-and-scripts run and switch on the game-designer's limits table in direction; art-director and performance-engineer by rule |
| Return paths | a timing change → the timing-list revision → VFX and sound recheck |

## 7. Marketing art
| Item | Recipe |
| --- | --- |
| Job lead | **marketing** |
| D1 plan | L: 3-5 thumbnails from different hooks (layout, story or camera) as prompt rows at the real slot size, after a labelled warm-up; M: one. The asset kit plan: sell list, the launched thing as hero, display sizes, the family of crops with each safe square (`marketing-craft/references/image-pipeline.md` §1). No needs crafts: D1 writes `direction.md` itself |
| Limits (N1) | art-director when `launch` (style, identity anchors) · trend-scout when `trends`; a merge runs only when a limits table exists |
| G1 shows | the labelled warm-up, then the options, each at the real slot size; the preferred one with reasons tied to the sell list |
| Production order | marketing makes the final piece once: silhouette, value and light studies inside its own run, then render, colour and rebalance, polish, a layered file (foreground, midground, background, effects, light, title) and the planned crops |
| Integrator | marketing |
| Capture and scripts | `thumb_check.py` at player sizes and in the real layout, `look_check.py` value, on the studio-operator |
| Review order | **marketing** integrated review and package; art-director when `launch` or `visual_flags` |
| Return paths | a wrong face or identity draws the first note every time: fix it before the review |

## Not recipes
- **New game pre-production:** the `preproduction` skill's growth order; it produces the briefs these recipes consume.
- **Building a game from the design baseline (J027):** the game's roadmap `knowledge/design/roadmap.md` (template `templates/roadmap.md`; owner J027-D4) holds the goal in the owner's words and its success test, the milestones in order with their exit tests, and under each milestone the craft rows and the jobs that serve it. The last pre-production step writes it, before the first build session. One craft row per area of the `orchestration` §2 craft-owner table that the milestone needs: owner role, route (a job of the types above, a role session, a role subagent), start trigger (now, a milestone, or the grey-box verdict of a named mechanic: `preproduction` P-15) and status. A builder's grey-box UI, effects or sounds are named stand-ins, never the craft's row done. When a trigger fires the lead starts that row the same turn, without asking (owner J027-D3). Each owner ask is checked against the roadmap before it goes to a running session: an ask for a craft with no open row or session starts that row; an ask that serves no milestone is added to one, or becomes one digest question with a default. Every job card names the milestone it serves. The lead updates the roadmap at every gate (G1, G3), every job close and every row start or finish.
- **Live update or event:** the live-ops plan is split by the lead into jobs of the types above. For a job that comes from a live-ops update brief for an event, theme, variant line or limited item: the live-ops concept round (2-3 premise one-pagers, owner pick) fixes the premise: the job's direction takes the picked premise, promise and theme as fixed and does not reopen them. The job keeps its own direction, build and review chain, because a premise page cannot test the craft read (silhouette, routes, timing, read order at phone size) (lead decision J019-LD1). A live-ops review slot runs after integration and before G3: the event review E-01 to E-19 on its capture set (`live-ops-craft/references/event-review.md` §2-§3).

## Cross-type rules (all types)
| Rule |
| --- |
| One written target experience shared by design, art and engineering before craft work; name the type of fun, not "fun" |
| Constraint owners state limits before build, in one limits table in N1; they are not called again in direction |
| Agree early on the plan, not on roughs: the needs and limits tables meet the job lead's plan before G1; ask one question tied to the goal, never "do you like it?" |
| Take a note for its problem, not its suggested fix |
| Gates close doors: a decided question stays decided (the decision log); the options not picked are recorded closed with a "may return only if" condition, and later briefs carry them in `avoid` |
| Judge at the real camera, size and context, never in the editor or a beauty shot |
| Reuse shared libraries (VFX texture library, sound library, kit pieces, asset catalogs) before making new |
| A craft may diverge from a reference for readability or budget, and says so up front |
| Consensus is not the goal; judge against the target, not majority taste |
| A consumer states its needs against the plan before its producer builds: a craft that keys from another's output (VFX and sound from animation, rigger from modeler, sound from the floor-material list) writes its needs table in N1, not after the build |
| Options shown at G1 (directions, layouts, approaches, target images, thumbnails): L 2-3 (marketing 3-5), each from its own hook, at equal finish, with the labelled warm-up as the baseline; each shown in colour, grey and black-fill at the size players see it; one recommendation with the reasons the others lost; options that failed a check are listed with the reason, never shown as equals (`reference-images`, `orchestration/references/gates-and-feedback.md` §3) |
| No proof pass and no rough hand-off (J024). Value and light are chosen in grey inside the maker's own run, before colour |
| One marker list per job where animation, VFX and sound meet; a retime is a contract change to all of them the same turn (`orchestration/references/briefs-and-handoffs.md` §3) |
| Every G3 packet carries the could-not-check list and owner-confirmed lines for feel at normal speed and, when the job has sound, two listens: the key event alone, then the full mix, each on a phone speaker and on headphones |
| A job whose result the server confirms adds a *rejected request* capture to its review evidence: no success layer plays |
| With player code (feature, effect, UI), the integrator delivers the Studio-only test hooks and the debug log at the wiring step, before the capture-and-scripts run (`engineering-craft/references/presentation.md` §9; hook names: `testing/references/player-facing.md` §3) |
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
