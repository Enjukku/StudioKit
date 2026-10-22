---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 2 (brief v2)
supersedes: []
---
> Author: J018 maker feature-builder · claude-opus-5-5 · high · 2026-10-22

# J018 coverage: feature-builder

Books rebuilt (old state: `df13ff4`): `.agents/roles/feature-builder.md` (body only; frontmatter byte-identical, checked with `diff` against `git show df13ff4`), `.agents/skills/engineering-craft/` (SKILL.md; references `engine-first.md`, `probes.md`, `handoffs.md`; new `presentation.md`), `.agents/skills/ui-basics/` (SKILL.md; references `facts.md`, `ui-effects.md`; `evals/` untouched).
Where the self-review lives: `engineering-craft/SKILL.md` §6 (SR-01 to SR-19, each with its input; the Studio recipes and their false readings in `references/presentation.md` §10-§11) and `ui-basics/SKILL.md` §6 (U-S01 to U-S13). The role file's "Before you hand back" points to both. "Core principles for this craft" is `engineering-craft/SKILL.md` §7 (the skill the agent loads first); §1 says to re-read §3, §6 and §7 after a compaction (the self-review starts at about 18 KB).
Library numbers marked [inference] are written as PROPOSAL starting values (pending after 100 ms, merge window 100 ms, 8 live copies, toned value 0.5, refusal sound once per 0.5 s, a third repeat becomes a script). Engine facts added were checked in the docs mirror (paths in the books). Paid-random lines were diffed against `platform-policy/references/rules.md` § A (V4); the first diff missed the SKILL.md patterns P-01 (server-sent effective odds) and P-02 (one policy module, fail closed): fixed in repair round 1; the books now say § A, P-01 and P-02 win.

Counts: 52 findings tagged feature-builder: 49 landed, 3 landed in part with the rest rejected (MD-05, PP-09, SD-16; reasons below). 20 untagged findings used.

### a. Findings
Paths are under `.agents/skills/` unless they start with `role` (`.agents/roles/feature-builder.md`). EC = `engineering-craft/SKILL.md`; P = `engineering-craft/references/presentation.md`; H = `engineering-craft/references/handoffs.md`; UB = `ui-basics/SKILL.md`; UE = `ui-basics/references/ui-effects.md`.

| ID | Title | Landed in (file § section) | As | Or rejected: reason |
| --- | --- | --- | --- | --- |
| CR-01 | Judge in the game, at the game camera, in the real place, moving | EC §3 step 9, §4 EC-25, §7 row 2; P §10; EC §6 SR-16 | step; standard; core principle; self-review check | |
| CR-03 | Solve the problem behind the note; separate goals from tactics | role "Working with other agents" (restate the problem, re-check it after the fix); EC §7 row 16; EC §6 SR-19 | standard; core principle; self-review check | |
| CC-01 | One target experience, signed by every craft | EC §3 step 1 (quote the target-experience line), §4 EC-01; EC §6 SR-01 | step; self-review check | |
| CC-02 | One marker list is the timing contract | EC §4 EC-19; P §4 (one handler, the shared sync rule); H §14 (timing list events, no "Hit" marker); EC §6 SR-09; P §12 sword example | standard; self-review check; example | |
| GD-02 | Every action gets immediate feedback | EC §3 step 1 (feedback stack), §4 EC-17; P §1, §2; UB U-14; EC §6 SR-02, SR-08 | step; standard; self-review check | |
| GD-05 | Behaviour sets the tone before art does | EC §3 step 6 (a mechanic judged by behaviour ships first as the skeleton); EC §6 SR-05 | stage | |
| GD-06 | Movement patterns give enemies character | EC §3 step 6 (skeleton with plain Parts the designer judges by behaviour); EC §7 row 15 example (grey blocks) | stage; example | partial: choosing the pattern is the game-designer's; my part is the blocks-only playable build |
| GD-15 | Prove the fun with the crudest prototype before art | EC §3 step 6; role work method step 4; EC §7 rows 4, 15; EC §6 SR-05 | stage; core principle; self-review check | |
| GD-30 | Every hazard has written rules | role partner table (game-designer: hazard rules at the contract); P §1 "Truth fields"; EC §6 SR-13 | step; self-review check | |
| GD-34 | Feedback follows the confirmed outcome | EC §4 EC-17; P §2; UB U-14; EC §7 row 19; EC §6 SR-08; P §12 shop and sword examples | standard; core principle; self-review check; example | |
| GD-35 | Paid random reveals are honest | EC §4 EC-23, §5 last rule; P §8; EC §6 SR-15; P §12 egg example; `engine-first.md` paid random row | standard; quality bar; self-review check; example | V4: diffed against `platform-policy` § A and (repair round 1) P-01, P-02: eligibility through the policy module, fail closed; the panel shows the server-sent effective odds; platform-policy wins |
| MD-05 | Start texturing from baked AO and curvature; drive variation by rules | EC §4 EC-18 (rules and values as data) | standard (in part) | partial: baking and texturing are `modeling-craft` and `environment-craft` work; the builder does not texture. Only the "rules as data, one rule set per class" idea applies, to any placement script it writes |
| PP-09 | Keep separable parts separate, then judge them together | P §4 (every effect layer under one root, separable named layers) | standard (in part) | partial: separate Blender objects and material slots are the modeler's; the builder's analogue is separable presentation layers |
| PP-11 | Clean meshes, clean collision, organised UVs | EC §4 EC-25 (what looks solid collides); P §10 "Collision agrees with the look"; EC §6 SR-16 | standard; self-review check | mesh and UV parts are the modeler's |
| PP-20 | Plan the states first: clips interrupt and blend | H §14 (states, transitions, priorities and fades planned before keying); role partner table (animator row) | step | |
| PP-25 | Reuse first | EC §3 step 2, §4 EC-03 (reuse before new); EC §6 SR-03; role work method step 2 | step; standard; self-review check | |
| PP-28 | Automate every repeated step | EC §4 EC-15 (a third repeat becomes a script or a tool ticket, PROPOSAL) | standard | |
| PP-29 | One owner per file or area | role "Write scope" (never edit the partners' tables); role place in the job flow (owns table, kept) | standard | |
| PP-30 | Fix naming and folders before production | role "Context" (names of states, events and cues from `vocabulary.md`); EC §4 EC-18 | standard | |
| PI-04 | Block out first, in the engine, and play it | EC §3 step 6; EC §6 SR-05 | stage; self-review check | |
| PI-14 | "It would be cooler" is new scope | EC §4 EC-16, §5 rule 5; role stop rules; EC §7 row 18 | standard; core principle | |
| SD-01 | Sound's three jobs; every state change has a cue | EC §6 SR-02 (every state change has a cue or a written reason) | self-review check | |
| SD-05 | Stage the action: one sound per named stage | P §3 (stage timelines in seconds, shared stage names); H §14 events; EC §6 SR-09 | step; self-review check | |
| SD-06 | Attach sounds to game events, listed and tested | P §9 (debug `cue` line, hooks); EC §6 SR-08, SR-10 (one cue per event, one per merge window) | self-review check | |
| SD-16 | A shot is built from five layer jobs | H §13 (the builder plays the stage file the cue table names; no live layering) | standard (in part) | partial: layer design and baking are the sound designer's craft |
| SD-23 | Every floor material is a footstep callout | P §3 (footsteps from `Humanoid.FloorMaterial` through the footstep table; a missing material is reported); P §10 Footsteps row; EC §6 SR-07 | step; self-review check | |
| SD-25 | Mix as you go; music and effects together | role partner table (temp cues at the skeleton); H §13 (each cue on the bus the card names) | step | |
| SD-32 | Bake per-sound processing into the file | H §13 (no live audio effect the card does not name; live effects only for context) | standard | |
| UI-01 | Flow first, then style, then motion | UB §3 step 2 (functional pass before styling); UB §6 U-S01 | stage; self-review check | |
| UI-03 | Design for the audience and the device: phone first | UB §3 step 8, §4 U-03 (declared touch rubric); UB §6 U-S03 | step; standard; self-review check | |
| UI-05 | UI is every screen and state | UB §3 steps 1, 7; UB §6 U-S01, U-S12 | step; self-review check | |
| UI-06 | One UI ecosystem with written rules | UB §3 step 5, §4 U-05 (tokens from the rule sheet); EC §4 EC-18 | step; standard | |
| UI-09 | Proximity creates meaning | UB §3 step 4 (world values on their unit with a `BillboardGui`); `ui-basics/references/facts.md` BillboardGui row | step | |
| UI-12 | Motion goal: responsiveness | UB §4 U-14; UE §A button press, pending rows; UB §6 U-S07 | standard; self-review check | |
| UI-14 | Motion goal: from source to destination | UB §4 U-17; UE §B "Grow from source", fly-to-HUD; UB §6 U-S10 | standard; self-review check | |
| UI-15 | Motion goal: one motion table | UB §4 U-13; UE header (§A seeds the game's table); UB §6 U-S05 | standard; self-review check | |
| UI-17 | Seed the motion table with tested durations | UE §A (the seed, exits no longer than entrances); UB §4 U-13 | standard | |
| UI-18 | Errors and denials say the fix, at the control | UB §4 U-15; UE §A error row, §B refusal shake; P §7; UB §6 U-S08 | standard; quality bar; self-review check | |
| UI-19 | Counters tell the truth | UB §4 U-16; EC §4 EC-22; P §7; EC §6 SR-11; UB §6 U-S09 | standard; self-review check | |
| VR-08 | Real-time effects are built for cost | EC §4 EC-25; P §10 budget row; EC §6 SR-16 | standard; self-review check | |
| VR-17 | Build each effect under one root | P §4 (one root, one scale factor from data); P §10 Scale row; EC §7 row 17; EC §6 SR-16 | standard; core principle; self-review check | |
| VR-18 | Know the whole toolbox | EC §4 EC-03 (an emitter property beats imitating code); `engine-first.md` "Bursts and particle effects" row | standard | |
| VR-19 | Rate each effect per viewer | EC §4 EC-20; P §5 (toned value per clarity level; threats, pickups, own outcome never toned), §6 `clarity()`, §9 `Clarity` hook; EC §6 SR-12; P §12 sword example | standard; self-review check; example | |
| VR-20 | The drawn danger area is the real hit area | EC §4 EC-19; P §4, §9 (`DebugShape`); EC §6 SR-13 | standard; self-review check | |
| VR-21 | Camera and screen punches are rare, local, rotation-only | EC §4 EC-20; P §5; `probes.md` §4 shake probe; EC §6 SR-12, SR-10 (no `cam` line at the real rate) | standard; self-review check | |
| VR-22 | Hit-stop is local, short and scaled | P §4 (attacker's and target's clients only; one owner per track: stop-until time, base speed as last set through the owner, restore on interruption; the latency case with `DelayMs` 150; predicted stop only as a predicted contract row); `probes.md` §4 replication probe; `engine-first.md` hit-stop row; H §14; EC §6 SR-08, SR-17; P §12 sword example | step; self-review check; example | |
| VR-23 | Every intense channel has an off path | EC §4 EC-21, §5 rule 8; P §6 (five settings: motion, shake, flashes, screen effects, clarity); P §9 `Reduced`; EC §6 SR-14; EC §7 row 20 | standard; quality bar; self-review check; core principle | |
| VR-24 | Frequent effects are shorter, merged and capped | EC §4 EC-22; P §7; UB §4 U-18; EC §6 SR-10 | standard; self-review check | |
| VR-26 | Pulse and blink rates carry meaning | P §6 last bullet (rate class from the spec, server timer); UE §A pulses row (points to `ui-design` motion.md §8); EC §6 SR-13 (countdown ticks follow the server timer) | standard; self-review check | |
| WT-02 | One consistent physics lets players predict | P §3 (movement values from the game profile; code-driven motion derives from them); role "Read first" item 3 | standard | |
| WT-09 | Uneven spacing and eases sell gravity | UB §4 U-13 (eased, never linear); UE §A "Travel and growth" row | standard | |
| WL-29 | Plan routes in player metrics | P §3 (walk speed and jump height from the game profile, never hard-coded) | standard (in part) | route planning is level-design's; my part is reading the real values |
| WT-01 (untagged) | Anticipation must read | EC §4 EC-19 (tell sent at wind-up start); P §2 last bullet; EC §7 row 1 example | standard; core principle | |
| WT-13 (untagged) | Cause first, then effect, timed in tenths | P §3 (stage timelines in seconds from one start event); EC §7 row 8 | standard; core principle | |
| VR-25 (untagged) | Randomise decoration only | P §3 (random only on decorative fields); EC §7 row 12 | standard; core principle | |
| VR-09 (untagged) | The hit is one peak frame | P §4 (one marker handler starts emit and cue) | standard | |
| VH-02 (untagged) | Rank loudness across a set | P §7 (cull rank: threat, own action, pickups, others, ambient) | standard | |
| CR-17 (untagged) | Say what each input can prove | EC §4 EC-10; EC §6 input labels; P §11 | standard; self-review inputs | |
| CR-13 (untagged) | Close with an honest recap | EC §3 step 11; EC §6 SR-19; role "Before you hand back" | step; self-review check | |
| PI-07 (untagged) | One named problem per pass | EC §4 EC-05 step (2) | standard | |
| PI-09 (untagged) | Not precious | EC §4 EC-12; EC §7 row 15 | standard; core principle | |
| PI-08 (untagged) | Find the right number by bracketing | P §3 (tunable values as attributes for the designers' brackets); EC §7 row 14 | step; core principle | |
| RI-30 (untagged) | Leave a marked placeholder | EC §3 step 6 (stand-ins named); EC §4 EC-13 | step; standard | |
| WL-20 (untagged) | Read at the lowest graphics setting | EC §4 EC-25 (information layers never drop with quality); EC §6 SR-16 | standard; self-review check | |
| UI-11 (untagged) | The static state explains | UB §6 U-S05 (reduced end state still explains the event) | self-review check | |
| EX-06 (untagged) | Squash and stretch by a Roblox-safe route | UE §B pop row (a stretch keeps the area) | standard | |
| LC-01, LC-02 (untagged) | Reserved colours; colour-role table | EC §4 EC-18 (colours by role from tokens, never a free `Color3`); EC §6 SR-06 grep | standard; self-review check | |
| GD-13 (untagged) | Fairness from consistent tells | EC §4 EC-19 (no random fuse); P §4 | standard | |
| GD-07 (untagged) | Art and mechanics promise the same thing | EC §4 EC-25; P §10 collision row | standard; self-review check | |
| SD-30 (untagged) | Cues are data | EC §4 EC-18; P §3 cue table | standard | |
| SD-31 (untagged) | Fixed categories | H §13 (each cue on its bus) | standard | |

### b. Universal principles
| UP-ID | Applies | Where in "Core principles for this craft" (`engineering-craft/SKILL.md` §7) |
| --- | --- | --- |
| UP-01 | yes: code decides how fast and how truthfully the read reaches the player | row 1 |
| UP-02 | yes: Studio play mode, phone viewport, worst case, slow server | row 2 |
| UP-03 | no: ranking what is read first is the design crafts' decision (UI, VFX, art); the builder carries their tables exactly (rows 7, 17) and the cull rank in `presentation.md` §7 | — |
| UP-04 | yes (as order of work): rule and result path, then the event list and primary layer, then decoration | row 4 |
| UP-05 | no: shape and silhouette are visual crafts' work; nothing in code carries shape | — |
| UP-06 | yes (as anti-overengineering and caps): fewest modules, layers and live instances | row 6 |
| UP-07 | yes: one table per code (events, cues, motion rows, tokens, messages) | row 7 |
| UP-08 | yes: result after cause, one trigger, timelines in seconds | row 8 |
| UP-09 | no: exaggeration is a craft choice inside the specs the builder wires | — |
| UP-10 | no: the subject's character drives design choices; the builder wires them | — |
| UP-11 | no: one style is the art director's and UI designer's; the builder reads their tokens (row 7) | — |
| UP-12 | yes (limited): random variation only on fields a spec marks decorative | row 12 |
| UP-13 | yes: contract, feedback stack, engine limits, budget before code | row 13 |
| UP-14 | yes (limited): the built-in and an alternative are compared before custom infrastructure; tuning values exposed for designers' brackets | row 14 |
| UP-15 | yes: skeleton before presentation before polish; rewrite what keeps breaking | row 15 |
| UP-16 | yes: findings with failure scenario and evidence; problem behind each note; one change per measured pass | row 16 |
| UP-17 | yes: tables, test hooks, debug log, one root, engine features | row 17 |
| UP-18 | yes: stop criteria in the contract; extra polish is a follow-up | row 18 |
| UP-19 | yes: attempt and outcome, pending, refusals, true counters, honest reveals | row 19 |
| UP-20 | yes: reduced paths, more than one channel, local comfort settings | row 20 |

### c. Old book changes (old text at df13ff4)
| Old text (file:line at df13ff4) | Kept / sharpened / replaced by (new location) / moved / removed | Why |
| --- | --- | --- |
| role:14 "You are the studio's feature builder…" | sharpened (role intro adds the truthful-presentation bar) | the material shows presentation truth is part of the builder's work |
| role:18 skills read order | sharpened (adds `presentation.md`, the new skill sections) | new reference |
| role:19 "Project overlays … The game profile for packages and source mode." | sharpened (adds movement values and the transport layer) | WT-02, WL-29 |
| role:29 "Craft practice from Riot's artists and designers: `knowledge/jobs/J016-orchestration/riot-extracts.md` §4" | removed | job card fixed list: role files point to their own books, not to the J016 extracts; the craft now lives in the books |
| role:31-38 Work method steps 1-7 | replaced by role "Work method" steps 1-9 (all old steps kept; new skeleton, presentation and worst-case passes; "cooler" ideas in the stop rules) | GD-15, PI-04, GD-34, PI-14 |
| role:41-44 Working with other agents | kept; one bullet added (problem behind the note) | CR-03 |
| role:47 Write scope | sharpened (test hooks; never edit the partners' tables) | PP-29, EC-24 |
| role:50 Hand-back manifest | sharpened (stand-ins, test hooks added) | RI-30, EC-24 |
| role (none) | new "What you ask your partners for, and when", "Before you hand back" | owner spec point 1; V8, V10 |
| engineering-craft/SKILL.md:6 header | sharpened (J018 line) | rule |
| engineering-craft/SKILL.md:10 intro paragraph | sharpened (adds wiring what players see and hear) | scope of the new rows |
| engineering-craft/SKILL.md:13 §1 | sharpened (which steps apply; re-read after compaction) | V7 |
| engineering-craft/SKILL.md:16-24 §2 | sharpened (new rows: `presentation.md`, `ui-basics`, binding skills win) | new reference |
| engineering-craft/SKILL.md:27-34 §3 steps 1-8 | replaced by §3 steps 1-11 (old 1-8 kept as 1-5, 7, 10, 11; new 6 skeleton, 8 presentation, 9 worst case; checks per step) | GD-15, PI-04, UP-15, UP-04 |
| engineering-craft/SKILL.md:39 EC-01 | sharpened (feedback stack, target-experience line) | GD-02, CC-01 |
| engineering-craft/SKILL.md:41 EC-03 | sharpened (reuse before new; engine property over imitating code) | PP-25, VR-18 |
| engineering-craft/SKILL.md:43 EC-05 | sharpened (each change is the one named problem, the worst first) | PI-07 |
| engineering-craft/SKILL.md:45 EC-07 | sharpened (denied with a reason) | UI-18 |
| engineering-craft/SKILL.md:48 EC-10 | sharpened (what each input can prove) | CR-17 |
| engineering-craft/SKILL.md:50 EC-12 | sharpened (rebuild, do not defend) | PI-09 |
| engineering-craft/SKILL.md:51 EC-13 | sharpened (stand-ins, test hooks in the manifest) | RI-30, EC-24 |
| engineering-craft/SKILL.md:53 EC-15 | sharpened (a third manual repeat becomes a script or tool ticket) | PP-28 |
| engineering-craft/SKILL.md:54 EC-16 | sharpened ("cooler" ideas are new scope) | PI-14 |
| engineering-craft/SKILL.md:61 rule "No work outside the brief's files…" | sharpened (cooler ideas with cost) | PI-14 |
| engineering-craft/SKILL.md:63-68 §6 Self-check (5 lines) | replaced by §6 SR-01 to SR-19 with inputs (old lines kept as SR-01, SR-03, SR-04, SR-18) | V1, V5 |
| engineering-craft (none) | new EC-17 to EC-25, §5 rules 6-9, §7 core principles, `references/presentation.md` | owner spec points 1-2; V8 |
| engineering-craft/references/engine-first.md:1 header; table end | sharpened (header); 12 presentation rows appended | V8; facts checked in the mirror |
| engineering-craft/references/probes.md:1 header | sharpened; §4 open probes appended | the new hooks and checks rest on untested engine behaviour |
| engineering-craft/references/handoffs.md:1 header | sharpened (J018 line) | rule |
| engineering-craft/references/handoffs.md:41-53 build ticket | sharpened (feedback_stack field; checks C5, C6) | GD-34, UI-19 |
| engineering-craft/references/handoffs.md:192-197 to-UI ticket | sharpened (denial reasons; motion rows and message table returned) | UI-18, UI-15 |
| engineering-craft/references/handoffs.md:200 "returns screenshots per state at phone size … for a look check" | replaced by the captures of `presentation.md` §10 for the review slot | ui-design review §7 slot names the captures |
| engineering-craft/references/handoffs.md:203, 207 to/from VFX | sharpened (attempt and outcome events, viewers, data fields, hooks before the first capture) | VR-19, VR-20, GD-34 |
| engineering-craft/references/handoffs.md:214, 218 to/from sound | sharpened (cue table, pooled AudioPlayers, bus, merge window, debug cue line, no live effects beyond context; attempt vs outcome cues) | SD-30, SD-32, sound proposal row 22 |
| engineering-craft/references/handoffs.md:225 to/from animation | sharpened (states and fades planned before keying; timing list; listeners before `Play`; outcome layers on the result) | PP-20, CC-02 |
| engineering-craft/references/handoffs.md:229 `timing: {windup: 0.25, hit_marker: "Hit", recover: 0.4}` | replaced (events `windup_start`, `contact_candidate`, `cleanup`; `contact_confirmed` as the server result) | wrong: one marker named "Hit" mixes forecast and confirmed hit (animator's `game-timing.md` §4, timing-list template) |
| ui-basics/SKILL.md:6 header "A deep UI/UX designer role will come later…" | replaced (the role exists; it owns how a screen works and looks) | outdated |
| ui-basics/SKILL.md:11 §1 | sharpened (input is the UI designer's spec; functional pass allowed before a spec) | UI-01, UI-05 |
| ui-basics/SKILL.md:16-19 §2 | sharpened (motion table, release checks, platform-policy rows) | V6 pointers |
| ui-basics/SKILL.md:22 step 1 "Flow first … Agree the flow before visuals." | replaced by step 1 (read and restate the spec; the flow is the designer's) and step 2 (functional pass) | the flow is now designed by the ui-ux-designer; the builder's analogue is the functional pass |
| ui-basics/SKILL.md:25-28 steps 4-7 | sharpened (tokens from the rule sheet; motion and sound step; states add pending, success, empty; test adds smallest phone and opaque setting) | UI-15, UI-05, UP-20 |
| ui-basics/SKILL.md:35 U-03 "touch targets ≥ 44 pt" | sharpened (the project's declared touch rubric) | `ui-design` D-05 declares one rubric per project |
| ui-basics/SKILL.md:37 U-05 | sharpened (tokens from the rule sheet) | UI-06 |
| ui-basics/SKILL.md:39 U-07 | sharpened (never optimistic for money or rewards) | GD-34 |
| ui-basics/SKILL.md:42 U-10 | sharpened (PreferredTransparency multiply; comfort module; weakest backdrop) | UP-20; ui-ux-designer proposal row 27 (b) |
| ui-basics/SKILL.md:49 rule "No client-side grants…" | sharpened (no success before the result); new rule on literals | GD-34, UI-15 |
| ui-basics/SKILL.md:54-59 §6 Self-check (6 lines) | replaced by U-S01 to U-S13 with inputs (all six old lines kept: U-S03, U-S02, U-S02, U-S04 and U-S05, U-S12, U-S11) | V1 |
| ui-basics (none) | new U-13 to U-18 | UI-15, UI-12, UI-18, UI-19, UI-14, VR-24 |
| ui-basics/references/ui-effects.md:1, 5 header and intro | sharpened (§A seeds the game's motion table) | ui-ux-designer proposal row 26 |
| ui-basics/references/ui-effects.md:10 button press | sharpened (click and visual from one input event) | ui-ux-designer row 27 (c), CC-02 |
| ui-basics/references/ui-effects.md:11 purchase success "pending shown as success" | moved to the new Pending row | one place for the pending rule |
| ui-basics/references/ui-effects.md:12 error | sharpened (pressed control only; cause and fix; sound at most once per 500 ms; silence listed) | UI-18 |
| ui-basics/references/ui-effects.md:13-14 toast, currency | sharpened (merge window; tick on first arrivals, one closing sound) | VR-24, UI-19 |
| ui-basics/references/ui-effects.md:25, 27, 31 number roll, fly-to-HUD, reduced motion | sharpened (exact value on Completed; inset-matching start point; the comfort module) | UI-19, UI-14, VR-23 |
| ui-basics/references/facts.md:1 header | sharpened; rows added (world-to-screen inset, BillboardGui, PreferredTransparency pattern, server time) | facts the new steps rely on, checked in the mirror |

| engineering-craft/SKILL.md EC-06 (rebuild text: table semantics, iteration order, `const` probe line) | moved to `code-review` `references/luau-current.md` rows 42-45, where the same facts already live; EC-06 keeps strict mode, refinement, `export type`, the two never-ship items, native code and the pointer (repair round 1) | V6 one fact, one place; V7 head length |
| engineering-craft/SKILL.md EC-10 "Say what each input can prove: a log is script time …" (rebuild text) | moved: EC-10 points to the §6 inputs, which state what each input proves | one place (V6) |
| engineering-craft/SKILL.md EC-17 to EC-25, §3 steps 1 and 8, §2 presentation row, §6 preamble and SR detail; role work method step 6 (rebuild text) | sharpened to one-line rules with pointers into `presentation.md` (whose §10 now holds the recipe detail); nothing removed from `presentation.md` | review R1: the attempt-and-outcome rule stood in about ten places |
| ui-basics/SKILL.md U-14 (rebuild text) | sharpened: the UI part only (press frame, pending on the control, the next tap counts); the rule points to EC-17 | review R1 |
| engineering-craft/references/presentation.md §7 refusal UI detail (rebuild text) | moved to `ui-basics` U-15 (one place for the control's answer); §7 keeps the reason-code mapping, disabled reasons and world refusals | V6 |
| ui-basics/references/ui-effects.md:14 at df13ff4 "tick on gain, clink on spend" | restored (repair round 1): "tick on the first arrivals and one closing sound on gains; a soft clink on spend" | review R9: the spend sound was lost in the rebuild without a reason |
| engineering-craft/references/presentation.md §4 hit-stop "then the previous values restored" (rebuild text) | replaced: one owner per track and emitter with a stop-until time and the base speed, restore on interruption | wrong: overlapping stops leave the track frozen (review F2; model run d11) |
| engineering-craft/references/presentation.md §8 "The server checks `PolicyService`"; "odds panel is built from the same probability table" (rebuild text) | replaced: the policy module (fail closed), server-sent effective odds | wrong against `platform-policy` P-01, P-02 (review F3) |
| engineering-craft/references/presentation.md §9 "They run only in Studio (`RunService:IsStudio()`)"; SR-18 "test hooks Studio-only"; EC-24 "(Studio-only)"; role Write scope "Studio-only test hooks" (rebuild text) | replaced (repair round 2): hooks in the test build only (own source folder mapped only by a test project file), the IsStudio gate as the second guard, the production-build check in P §10 and SR-18 | wrong against `code-review` `references/testing.md:16`, `testing` SKILL.md:70 and the qa-lead's ask (review rev2 F1) |
| engineering-craft/references/presentation.md §4 "base speed (the speed the clip was started with; `TimeScale` 1)" (repair round 1 text) | replaced (repair round 2): the speed the game last set for that track, through the owner; the emitter's spec `TimeScale` | wrong when the game changes speed mid-clip (review rev2 R3) |
| engineering-craft/SKILL.md §5 rule 6 "no presentation delayed by a round trip" (rebuild text) | sharpened (repair round 2): "no attempt cue delayed by a round trip", plus the predicted-row exception | the old words read against the outcome layer, which must wait for the server (review rev2 R2) |
| ui-basics/SKILL.md U-S03, U-S04 and the C input "one per state per size" (rebuild text) | replaced (repair round 2): a numbers read (bounds against the ScreenGui rectangle, `TextFits`) for every state and size; stills for the main state per size and failures | light-check rule: up to 40 stills for answers the numbers give (review rev2 R4) |

### d. Command runs (V3) and proposal rows from other roles (V11)
Studio was not reachable during this job (`list_roblox_studios` returned no instance) and this machine has no Luau runtime (`luau`, `lune` absent; `rojo`, `selene`, `stylua` present). Every Studio recipe in the books is therefore labelled a first-use probe (`probes.md` §4; `presentation.md` §10), and the offline tests are tests the builder writes per game.

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| d1 (U-S06, S-18 pointer) | `python tools/art/look_check.py contrast --sample fb_ui_translucent.png --fg-box 428,338,700,372 --bg-box 410,260,870,330 --fg-stat p90 --bg-stat median --rule wcag-text --out fb_contrast_tr.json` | synthetic in-scene UI capture 1280 × 720: sky gradient and grass, a navy panel at 60 % transparency, white 28 px text over the sky part | ran; wrote the JSON; ratio 3.49, FAIL (right: white on a 40 %-navy-over-sky backdrop); the same with the panel opaque (PreferredTransparency 0): 16.40, PASS (right) |
| d2 (false reading) | same, `--fg-box 405,255,875,465` (the whole panel) | same image | 1.12, FAIL with no error: p90 sampled the sky through the panel, not the text. Wrong number with no error → proposal row to `ui-design` review §6; U-S06 says the text box must be tight |
| d3 (false reading) | same, `--bg-box 410,380,870,465` (panel over the grass) | same image | 8.51, PASS with no error for text that sits over the sky. → the background box sits directly behind the text, on the brightest backdrop (U-S06; proposal row) |
| d4 (SR-06, U-S05) | first form `grep -rnE 'TweenInfo\.new\(\|EasingStyle\.\|Color3\.' src tests` | synthetic Luau tree: a motion helper, a screen with an aliased `TweenInfo.new`, literal colour and text, a data table, a test | ran; missed `local TI = TweenInfo.new` then `TI(0.3)` (false PASS): pattern revised |
| d5 (SR-06, U-S05) | final literals grep exactly as written in `presentation.md` §10 (extracted from the file and run with `eval`) | same tree plus an edge file (one-word `.Text =`, `local T = TweenInfo` + `T.new`) | ran; 5 hits, all the planted literals and the helper line; still misses `T.new` through a stored alias and one-word strings passed to a helper: listed in `presentation.md` §11 |
| d6 (SR-06 asset ids) | `sound-design` review R-44 grep `grep -rnE 'rbxassetid://\|\.Asset\s*=' src tests` | same tree | ran; hit the literal `SoundId` and the concatenated `p.Asset = "rbxassetid://" .. id`; pointed to, not copied |
| d7 (SR-08 to SR-16, U-S07 to U-S11) | debug log, hooks, `execute_luau` reads, `NetworkSettings` delay, shake probe | Studio play-test | NOT RUN: no Studio instance; first use in a game is a probe, result recorded in the hand-back (`probes.md` §4) |
| d8 (SR-07, SR-11, SR-15) | offline Luau tests (id existence, affordability during count-up, reveal windup independence) | Luau specs | NOT RUN here: no Luau runtime; the builder writes and runs them per game (`testing`) |
| d9 (U-S06, repair round 1) | `python tools/art/look_check.py contrast --sample fb_ui_darktext.png --fg-box 428,468,700,502 --bg-box <box> --fg-stat p10 --bg-stat median --rule wcag-text --out fb_dark_<case>.json` | synthetic in-scene UI capture 1280 × 720: sky gradient and dark grass, a light #F0F0F0 panel at 60 % transparency, dark #1E1E1E 28 px text over the grass part | ran; wrote the three JSON files; bg box behind the text on the darkest part: 4.43, FAIL (right); bg box on the brightest (sky) part: 13.48, PASS with no error (false PASS under the old "brightest backdrop" rule); `--fg-stat p90` on dark text: 1.00, FAIL with no error (the stat sampled the panel). → U-S06: weakest backdrop by text tone, `p90` for light text, `p10` for dark text |
| d10 (SR-06, U-S05, repair round 1) | the literals grep of `presentation.md` §10, extracted from the file and run with `eval` from the sample's root | synthetic Luau tree: a screen script with single-quoted, back-quoted (interpolated), concatenated and one-word strings, `task.wait(0.28)`, `task.delay(0.35, …)`, `task.wait()`, `task.wait(cfg.holdSeconds)`, a motion helper, a message data module, a test; edge files with `toast("Need " .. n .. " more coins")`, `n .. " coins left"`, `local hold = 0.28` + `task.wait(hold)`, a quoted comment, `helper("Buy")`, `local T = TweenInfo` + `T.new` | ran; hit every planted literal except the listed misses (`n .. " coins left"`, a wait on a local number, `helper("Buy")`, `T.new` through a stored alias); no hit on `task.wait()` or a wait on a config value (right); hit the data module and a quoted comment (expected: read the line). The old pattern missed the single-quoted, interpolated, concatenated-in-a-call and literal-wait lines (false PASS with no error). Misses listed in `presentation.md` §11 |
| d11 (P §4 hit-stop, SR-17, repair round 1) | `python fb_hitstop_model.py` (a model of the two rules: save-and-restore vs one owner with a stop-until time) | stop A at 0 ms for 100 ms, stop B at 50 ms for 100 ms, 10 ms ticks; base speed 1 and 0.8; an interruption at 60 ms | ran; old rule: speed 0 at 150 ms and 300 ms (frozen track, reproduces F2); owner rule: 0 at 100 ms, 1.0 at 150 ms, 0.8 with base 0.8, 1.0 at once on interruption: PASS. A model of the book's text, not game code: the builder's offline Luau test is still written per game |
| d12 (SR-06, U-S05, repair round 2) | the literals grep of `presentation.md` §10, extracted from the file and run with `eval` from the sample's root | synthetic Luau tree (scratch `fb-r2/tree`): the d10 forms plus `notify("Not Enough Coins")`, `showBanner("Daily Reward Claimed")`, `setLabel(button, "Level Up")`, `wait(0.3)`, `delay(0.35, …)`, `BrickColor.Red()`, `BrickColor.new("Bright red")`, `self.wait(0.2)`, `Event:Wait()`, `GetService("…")`, `Instance.new("Part")`, a Title Case quoted comment | ran; 17 hits: every planted literal, the message data module and the quoted comment (expected: read the line); no hit on `GetService`, `Instance.new`, `task.wait()`, a config wait, `self.wait`, `Event:Wait()` (right). The round-1 pattern on the same tree: 10 hits, missing the three Title Case helper strings, both legacy calls and `BrickColor.Red()` (false PASS with no error, as the reviewer found). Remaining misses unchanged and listed in §11 |
| d13 (SR-18, P §10 production-build row, repair round 2) | `rojo build default.project.json -o prod.rbxlx` then `grep -c TestHook prod.rbxlx`; the same on `test.project.json` (Rojo 7.7.0 run from its aftman store) | synthetic Rojo project (scratch `fb-r2/proj`): `src/server`, `src/client`, `test/hooks/server` and `test/hooks/client` hook scripts with the IsStudio guard; the default project maps `src` only; the test project maps `src`, `test/hooks` and the two `TestHooks` folders | ran; wrote both place files; production 0 (right), test 7 (right; positive control). Planted leak (hook script copied into `src/server`): production 2 (right). `.rbxl` binary build of the test project: 4 hits where the XML gives 7, so the binary count is not reliable: the book says build `.rbxlx`. What gives a wrong 0 with no error: a place published from a Studio session synced from the test project, a hooks folder made by hand in Studio, a hook named otherwise: listed in §11 with the Studio read before a publish |

| Proposal row (from) | Target | Decision | Reason / where |
| --- | --- | --- | --- |
| `proposals/sound-designer.md` row 22 | `engineering-craft`: debug cue log `cue <cue-id> <event-id> <os.clock()>`, cue ids from one table, a hook firing an event N per second for T seconds | adopted | `presentation.md` §9 (the `cue` line keeps the four tokens, then `f` and `r`; `Rate` hook), §3 cue table; EC-18, EC-24; H §13 |
| `proposals/ui-ux-designer.md` row 26 | `ui-basics/references/ui-effects.md` §A: say §A seeds the motion table; rows for pulse classes, other players' events, refusal sound rate, eased travel | adopted, with pulse classes and other players' events as pointer rows | UE header and §A; the pulse and other-player values already live in `ui-design` motion.md §8, so §A points there (V6); refusal rate and eased travel added as §A rows; proposal row back to motion.md §8 to point to §A for those |
| `proposals/ui-ux-designer.md` row 27 | `ui-basics` steps: (a) motion values from shared data, (b) PreferredTransparency multiply, (c) the UI sound sync rule | adopted | (a) UB §3 step 6, U-13, U-S05; (b) U-10, U-S06, facts row; (c) U-13 (click and press visual from one input event; reward chime with the first confirmed frame), UE §A press row |
| `proposals/vfx-designer.md` row 27 (G3 recipe) | integrator delivers test hooks | supported; the recipe is not mine to edit | my books carry it (EC-24, `presentation.md` §9, H §12); my proposals row 2 names the hooks |
| `proposals/architect.md` row 19 | `presentation.md` §1: cite the presentation contract's row ids; take request → result, viewers, truth fields and cap owner from it | adopted | `presentation.md` §1 last sentence (one rule, one place) |
| `proposals/architect.md` row 20 | `handoffs.md` §0 needs-round row; §1 `interface` points to `module-contract.md` "Builder brief interface rows" | adopted | H §0 new row; H §1 `interface` comment |
| `proposals/qa-lead.md` row 22 | `presentation.md` §9: `Outcome` / `Seed` and `Set` hook attributes | adopted | `presentation.md` §9 table (policy flags only through the game's policy module, Studio-only); EC-24 |
| architect's `presentation-contract.md` §4 (not a proposal row) | `ReducedMotionEnabled` live change undocumented | adopted as a probe | `presentation.md` §6; `probes.md` §4 new row |
| `proposals/reviewer.md` row 20 | `presentation.md` §4 hit-stop: restore to the base speed held by one owner per track (stop-until time), also on interruption | adopted (repair round 1) | P §4, `engine-first.md` hit-stop row, H §14, SR-17, P §12 sword example; model run d11; proposal rows to the animator and vfx-design books for the same rule |
| `proposals/reviewer.md` row 23 | `handoffs.md` §3 builder → reviewer `refs`: presentation contract revision, feedback stack sheet, debug log of the hook runs; stand-ins in the manifest | adopted (repair round 1) | H §3 `refs` (comment: the last three when players see or hear the change; the manifest lists the stand-ins, EC-13) |
| `proposals/environment-designer.md` rows citing `EC/references/handoffs.md` | — | not applicable | "EC" there is `environment-craft`'s handoffs file, not this skill |
| `proposals/qa-lead.md` row 31 | `presentation.md` §10 literals grep: add `BrickColor\.`, or list it in §11 | adopted (repair round 2) | P §10 pattern has `BrickColor\.`; P §11 lists `BrickColor.Red()` and `BrickColor.new(...)` as caught; run d12 |
| `proposals/architect.md` row 25 | `presentation.md` §4: which clients run the stop; the replication probe; the predicted stop as a contract row with layer `predicted` | adopted (repair round 2) | P §4 (attacker's and target's clients, bystanders only by the per-viewer column; the replication question; the predicted stop recorded as a predicted row, never the outcome row), P §2 prediction bullet (predicted row), `probes.md` §4 new row, `engine-first.md` hit-stop row, H §14, P §12 sword example. The `roblox-playback.md` §9 half is the animator's book: my proposal row for it now carries the same words |

### e. V5 pass (scripted before hand-back)
Run on this file and the books: every finding ID tagged feature-builder in `matrix.md` has a row in table a (52 of 52); for each row with a runnable check in the library, the "landed in" cell names a self-review line (SR-, U-S) or says why it is a standard or a stage only; every quoted landed-in location exists in the named file (string search). Worked examples re-read after the rule changes: `presentation.md` §12 (shop, sword, egg), `engineering-craft` §7 examples, `handoffs.md` §1 and §11-§14 tickets.

### Repair round 1 (review `reviews/feature-builder-rev1-reviewer.md`, fix-first)
Keep list kept as it was: the feedback stack sheet and its tie to the architect's P-rows (P §1), the skeleton → presentation → worst-case order (EC §3), the attribute-driven test hooks and debug log format (P §9, extended only), the §6 self-review with inputs and P §11 false readings, the role's partner table, refusals at the control, true counters and honest reveal windups, the engine-first rows and open probes, every old rule (only the ones listed in table c moved).

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 | P §6: the comfort module answers the five settings of `presentation-contract.md` §4 (`reducedMotion()`, `shakeScale()`, `reduceFlashes()`, `screenEffects()`, `clarity()`); P §5: the toned value comes from the spec per clarity level, threats, pickups and the own outcome never toned; P §5 camera channels go through `shakeScale()` and `screenEffects()`; P §9: `Reduced` covers motion, shake, flashes and screen effects, new `Clarity` hook; P §10 Per viewer and Reduced rows; SR-12, SR-14; EC-21; `engine-first.md` reduced row; H §12 hook list. Proposal rows to the architect (hook list), qa-lead (hooks table) and reviewer (S3 accessor list) books |
| F2 | P §4: one hit-stop owner per track and emitter, stop-until time, base speed, restore on death, unequip, destroy and a new clip, overlap test; `engine-first.md` hit-stop row; H §14; SR-17 (offline overlap and interruption test); P §12 sword example. Model run d11 (old rule freezes, new rule ends at base). Reviewer row 20 adopted (table d). Proposal rows to the animator (`roblox-playback.md` §9 says "previous speed") and vfx-design books |
| F3 | P §8: eligibility through the game's policy module (P-02, fail closed), never `PolicyService` directly; the odds panel shows the server-sent effective odds (P-01), the client never computes its own; offline test with the policy call failing; P §12 egg example; SR-15; EC-23; `engine-first.md` paid random row (the call can error: Y/PolicyService.yaml:175-184). Coverage header and GD-35 row record the corrected V4 diff |
| F4 | Table d: rows for `proposals/reviewer.md` 20 and 23 (both adopted); H §3 `refs` adds the presentation contract revision, the feedback stack sheet and the debug log of the hook runs |
| R1 | Fixed in part. EC-17 to EC-25 are one-line rules with pointers; the header keeps the J018 phrase and the sources only; §1, §3 steps 1, 6, 8, the §2 row, the §6 preamble and SR-06/08/10 are shorter (recipe detail lives in P §10); EC-06 table facts and EC-10's input list moved to their one place (table c). Measured with Python: §6 starts at 16.0 KB and ends at 21.4 KB (was 18.1 to 23.3 KB). Declined the rest of the 19 KB target: what still sits before §6 is the old EC-01 to EC-16 craft core that the architect, qa-lead and reviewer also use, with its evidence; cutting it would drop rules that are still right. §1 already says to re-read §3, §6 and §7 after a compaction |
| R2 | P §4 latency bullet (`DelayMs` 150; predicted stop on the attacker's own client where the spec allows, ended at once on a denial; otherwise a hold or shorter stop agreed with the animator); P §10 attempt row; SR-08 (one still of the frozen pose); P §12 sword example; H §14; role partner table, animator row. Proposal row to the animator book for its capture check |
| R3 | P §10: widened literals grep (single, double and back quotes, interpolated strings, capitalised string before `..`, literal `task.wait` / `task.delay`), run verbatim from the book (d10); P §11 lists the remaining misses; SR-06 and the Literals row: a clean result still needs the code read of the tween, text and timer paths |
| R4 | U-S06: background box on the weakest backdrop by text tone (brightest for light text, darkest for dark), tight text box with `--fg-stat p90` / `p10`; the proposal row to `ui-design` review §6 corrected. Run d9 confirms the false PASS of the old rule and a new false reading (wrong stat) |
| R5 | U-15 and UE §A error row and §B refusal shake: tween the inner content frame's `Position` (a control laid out by `UIListLayout` or `UIGridLayout` ignores its own `Position`; `ui/list-flex-layouts.md:16`, `ui/grid-table-layouts.md:40`); P §7 points to U-15 instead of restating it |
| R6 | EC §1: steps 6 and 8 only when players see or hear the change; step 9 always runs (scale, rejected request, slow server, lifecycles), its burst, viewer and quality parts only for visible changes |
| R7 | SR-10 no `cam` line during the rate runs; SR-16 scale factor ×2 once, one still, after the `Model:ScaleTo` probe (P §10 Scale row); SR-07 every floor material has a footstep row (P §10 Footsteps row; terrain materials manual). Table a rows VR-17, VR-21, SD-23 now name their SR lines |
| R8 | P §9: `Rate` logs the playing-track count; `live track:<clip-id>` lines from `Animator:GetPlayingAnimationTracks()` (Y/Animator.yaml:128-140); P §11: the list includes fading tracks, so a count right after a burst reads high; SR-10 reads tracks against their cap |
| R9 | UE §A currency row: "tick on the first arrivals and one closing sound on gains; a soft clink on spend" (table c) |
| R10 | EC §7 row 2: phone cost from a phone-class profile with the expected player count (`performance`), never the viewport emulator |
| R11 | Not my file: proposal row to `testing/references/player-facing.md` §3 (builder's `Outcome` / `Seed`, `Set` names; `Clarity` for PF-16) |

V5 pass after the repair (scripted): every landed-in string above exists in its file; worked examples re-read after the rule changes: P §12 shop (refusal now through U-15, unchanged words), sword (owner, latency, clarity), egg (policy module, server-sent odds); EC §7 rows 1, 2, 19, 20; H §3, §12, §14. Fixed rules re-checked: role frontmatter byte-identical to `df13ff4`; SKILL.md 127 and 83 lines; descriptions 376 and 394 characters (unchanged); no section renumbered; no library ids or Riot names in the bodies; J018 phrase in every changed file's header.

### Repair round 2 (review `reviews/feature-builder-rev2-reviewer.md`, fix-first)
Keep list kept: the feedback stack sheet and its tie to the architect's P-rows (P §1); the skeleton → presentation → worst-case order and §1 conditions (EC §1, §3); the hit-stop owner with stop-until time, interruption restore and the overlap test (P §4, SR-17; only extended); the comfort module with five settings and the Clarity override (P §5, §6, SR-12, SR-14); paid reveals through the policy module with server-sent odds (P §8, SR-15); the attribute-driven hooks and the debug log format (P §9; table and log lines unchanged, the build rule added above them); the §6 self-review with named inputs, the EC-17..EC-25 one-line pointers and the §11 false readings (extended only); U-S06 contrast by text tone; the refusal shake on the inner content frame and the spend sound; the engine-first rows and open probes (two probes appended). Only the lines listed in table c changed meaning.

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 | P §9 "Test build only" (own source folder mapped only by a test project file; the default project never maps it; no game module names the hooks; the qa-lead gets both builds) and "Second guard" (IsStudio); P §10 new "Production build" row (`rojo build` to `.rbxlx`, `grep -c TestHook`: 0, test build above 0 as the control); P §11 its false readings; SR-18; EC-24; role work method step 6, Write scope (the test project file is project config: edit only when the owns row names it) and a new qa-lead row in the partner table. Run d13. Proposal rows: `code-review` S10 / PT-19 build check, G3 tool row for the gate |
| F2 | Table d: `proposals/qa-lead.md` row 31 adopted (P §10 pattern, §11); `proposals/architect.md` row 25 adopted (P §2, §4, `probes.md` §4, `engine-first.md`, H §14, P §12). My animator proposal row updated to the same words |
| R1 | P §10: the reviewer's widened pattern (Title Case strings to helpers, legacy `wait` and `delay`, `BrickColor.`), run verbatim from the book (d12, 17 hits, no new false hit); P §11 caught and missed lists updated |
| R2 | EC §5 rule 6: the predicted-row exception (P §2: small, own client, removed on denial; never money, rewards or paid reveals), and "no attempt cue delayed by a round trip"; P §2 prediction bullet ties prediction to the contract's predicted row; P §4 latency bullet: default the agreed hold or a shorter confirmed stop; a predicted stop is the game designer's choice, recorded as a predicted row, never the outcome row; H §14 |
| R3 | P §4: the base is the speed the game last set for that track (other speed changes go through the owner, which updates the base; a change during a stop applies when it ends) and the emitter's spec `TimeScale`; SR-17 and the P §4 offline test add "a speed change during a stop survives it"; `engine-first.md` hit-stop row; P §12 sword example (a slow debuff during the stop) |
| R4 | `ui-basics` §6: C input budget (main state per size, failures, the review slot's states); S input numbers for every state and size; U-S03 one S read per state and size (interactive elements outside the ScreenGui's rectangle, `TextFits` false: both 0; ScrollingFrame descendants skipped; TextScaled always fits); U-S04 the same `TextFits` read plus a code read for TextScaled; U-S13. New `probes.md` §4 row: whether the Client read sees the emulated screen and whether the ScreenGui reports the inset area. Not run: no Studio instance (listed `list_roblox_studios`: none) |
| R5 | U-15: a paid-random control for a restricted player is hidden or given a free path (`platform-policy` P-03) |
| R6 | P §9 "One run, one setting" (the hook script prints the active overrides at start; clear every hook attribute after the run); P §11 the saved-attribute false reading; SR-18 "hook attributes cleared after the runs" |
| R7 | Role work method steps 4 and 6: "(when players see or hear the change: `engineering-craft` §1)"; step 7 "Worst-case pass (always)" |

V5 pass after the repair (scripted): every landed-in string named above found in its file; worked examples re-read after the changed rules: P §12 sword (clients, debug speed change, SR-17), shop and egg (no rule they use changed); EC §7 rows 17, 19 (hooks, prediction: still true); H §3, §14. Fixed rules re-checked: role frontmatter byte-identical to `df13ff4` (diff of lines 1-10); SKILL.md 127 and 83 lines; descriptions unchanged; no section renumbered (P §9 gained bullets inside the section; probes §4 gained rows); LF endings in every changed file; no library ids or Riot names in the bodies. EC SKILL.md: §6 starts at 16.2 KB and §7 at 21.8 KB (§1 re-read line unchanged).

## Proposal sweep (J018 close)
Swept 2026-10-22 by the J018 close-out (feature-builder and reviewer books, one pass). Every row re-read in `proposals/`, its target opened at the current revision. `grep` of every proposals file for `engineering-craft`, `ui-basics`, `code-review`, `feature-builder` and `reviewer` just before hand-back: the rows below plus `sound-designer.md:22`, `ui-ux-designer.md:26` and `:27` (all three decided in table d, adopted) and `feature-builder.md:32` (my own maker's no-change row on the frontmatter). No other row targets these books.

| proposal file:line | decision (adopted / already in the book / declined) | where or why |
| --- | --- | --- |
| `proposals/architect.md:19` | already in the book | `engineering-craft/references/presentation.md` §1, last sentence of the intro (the sheet cites the contract's P-n rows and takes request → result, viewers, truth fields and cap owner from it) |
| `proposals/architect.md:20` | already in the book | `engineering-craft/references/handoffs.md` §0 row "architect ↔ animator, vfx-designer, sound-designer, ui-ux-designer · before the plan freezes"; §1 `interface` comment points to `architecture/references/module-contract.md` "Builder brief interface rows" |
| `proposals/architect.md:25` | already in the book | `engineering-craft/references/presentation.md` §4: the hit-stop bullet (attacker's and target's clients; bystanders only by the contract's per-viewer column), the replication-probe bullet (`probes.md` §4), the latency bullet (a predicted stop is a predicted contract row, never the outcome row); §2 prediction bullet. The `roblox-playback.md` §9 half is the animator's book |
| `proposals/qa-lead.md:22` | already in the book | `engineering-craft/references/presentation.md` §9 hooks table, rows `Outcome` / `Seed` and `Set` (policy flags only through the game's policy module) |
| `proposals/qa-lead.md:31` | already in the book | `engineering-craft/references/presentation.md` §10 literals grep has `BrickColor\.`; §11 literals bullet lists `BrickColor.Red()` and `BrickColor.new(...)` as caught (run d12) |
| `proposals/reviewer.md:20` | already in the book | `engineering-craft/references/presentation.md` §4 hit-stop bullet (one owner per track and emitter, stop-until time, base speed, restore on interruption), SR-17 offline overlap test, §12 sword example |
| `proposals/reviewer.md:23` | adopted | the narrowed remainder: `engineering-craft/references/handoffs.md` §3 `refs` now name the `Clarity` run among the debug-log runs and the production-build log (SR-18); comment "last four when players see or hear the change". Matches the reviewer's partner row (`.agents/roles/reviewer.md`, builder row) and `code-review/references/presentation.md` §1 S, §4 PT-19 |
