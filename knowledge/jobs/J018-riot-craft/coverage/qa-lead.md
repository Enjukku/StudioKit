---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 2 (brief v2); stage 3 repair rounds 1 and 2
supersedes: []
---
> Author: J018 maker qa-lead · claude-opus-5-5 · high · 2026-10-22 (repair rounds 1 and 2 the same day: see the end)

# J018 coverage: qa-lead

Books rebuilt (old state: git `df13ff4`, also the state at start): `.agents/roles/qa-lead.md` (body only; frontmatter lines 1-10 byte-identical, checked with `diff`), `.agents/skills/testing/` (SKILL.md; references `methods.md` and `records.md` revised; new `player-facing.md` and `worked-examples.md`; the skill has no `evals/`).
SKILL.md: 124 lines (≤ 500); description 397 characters after repair round 1 (adds "and what they see matches the server"); §1-§6 (steps, craft core, rules, self-review) end at about 19.0 KB; §7 "Core principles for this craft" follows, and §1 says to re-read §3, §6 and §7 after a compaction. All files LF.
Where the self-review lives: `testing/SKILL.md` §6 (QS-01 to QS-21, each with its input and the image budget); the PF-rows it checks are in `references/player-facing.md` §2; the role file's "Before you hand back" points to §6.

Counts: 77 findings tagged qa-lead: 58 landed (20 of them partly after repair round 2: VR-19 and VR-21 now say what they leave to the crafts, the rest of the finding rejected with its reason in the row), 19 rejected with reasons (no QA oracle: the read, look or sound judgement belongs to a craft). 12 untagged findings used. Library numbers marked [inference] are written as PROPOSAL starting values (lag ≤ 67 ms at 30 fps, pending after about 100 ms, ±5 % edge, refusal sound once per 0.5 s, celebration under about 2 s, 100 triggers at 1 per second, a burst of about 20 per second, 3:1 marker floor). Roblox claims marked [unverified] are written as "probe" (quality level, Network Simulator, reduced-motion route, Device Simulator capture). Engine facts added were checked in the docs mirror: `RenderSettings.EditQualityLevel` and `EnableFRM` (PluginSecurity, `_api-reference/classes/RenderSettings.yaml:66-120`), `GuiService.ReducedMotionEnabled` read-only (`GuiService.yaml:262-277`), `StudioTestService:ExecuteMultiplayerTestAsync` plugin only, ≤ 8 clients (`StudioTestService.yaml:76-80`), Network Simulator beta and `NetworkSettings` properties (`studio/network-simulator.md:1-30, 200-240`), `ColorCorrectionEffect.Saturation` −1 full desaturation (`ColorCorrectionEffect.yaml:76-84`), `StarterPlayer.CharacterWalkSpeed` 16 (`StarterPlayer.yaml:358-364`); the jump (repair round 1): `StarterPlayer.CharacterUseJumpPower` defaults to true (`StarterPlayer.yaml:330-340`), so `JumpPower` 50 governs (`Humanoid.yaml:640-650`) and the 7.2-stud `CharacterJumpHeight` does not apply; PF-12 points to the level designer's probe (`level-design/references/review-artifact.md` §6.6). V4: the paid-random lines (T-16, PF-06, worked example 2) were diffed against `platform-policy/references/rules.md` §A (odds before purchase totalling 100 % or the rounding disclaimer, the Info or Details label for long lists, odds change with modifiers and once-only outcomes, `ArePaidRandomItemsRestricted`): no conflict; the books point to §A and say it wins.

Partner consistency (V10), read-only: `vfx-design/references/review.md` (IG-02 to IG-14), `vfx-craft/references/measure.md` (§1 hooks, §3 marker contrast, §6 flash counter), `ui-design/references/review.md` (§6 S-33 lag line, S-44 reveal difference, S-37 to S-41), `game-design/references/review.md` §7, `animation-design/references/review.md` (G-03, G-04), `sound-design/references/review.md` (R-41, R-42), and the wave-3 files written beside mine: `engineering-craft/references/presentation.md` (§9 hook attributes and debug log lines: my hook list uses its names), `architecture/references/presentation-contract.md` (its P-n rows and §6 check seeds feed my trace table; my catalogue is PF-n to avoid a clash), `code-review/references/testing.md` (player-facing fixture row). Sync rule, pending 100 ms, merge window, live-copy cap 8, refusal 0.5 s, flash cap (≤ 3 per second, design target 2) and pulse cap (3 Hz) are the partners' values, pointed to, not restated as new numbers.

### a. Findings

Paths are under `.agents/skills/testing/` unless they start with `role` (`.agents/roles/qa-lead.md`).

| ID | Title | Landed in (file § section) | As | Or rejected: reason |
| --- | --- | --- | --- | --- |
| CD-06 | Keep the likeness the same in every product | — | — | rejected: likeness is the art director's identity check; QA has no likeness oracle. The data side of variants is PF-13 |
| CF-05 | Lock a safe square around the crop | — | — | rejected: key-art and icon crops are marketing and art-director work; safe-area placement of HUD controls is checked in PF-11 (fixed zone clear of the thumb controls) |
| CR-01 | Judge in the game, at the game camera, in the real place, moving | SKILL §3 step 4, T-13, §7 row 2; player-facing §1 (conditions matrix); self-review QS-08, QS-16 | step; standard; core principle; self-review check |  |
| CR-02 | Ask a goal question, never "do you like it?" | records §3 (goal and layer field); SKILL §7 row 16; self-review QS-19 | standard; self-review check |  |
| CR-03 | Solve the problem behind the note; goals vs tactics | records §3 (a received solution restated as its problem; smallest_fix as the fix direction stated as what must hold, never code, plus `retest:` rows (repair round 1, F3); re-run the original row after a fix); role "Working with other agents"; self-review QS-19 | standard; self-review check |  |
| CR-06 | Notes are direct and visual; the maker drives; conflicts go up | records §3 (conflicting expectations go to the lead; maker fixes); role "Working with other agents" | standard | partial: paint-overs are the crafts'; my evidence is the log line, probe output or still |
| CR-08 | Diagnose by layer; re-check after a fix | records §3 (layer field; smallest_fix names one fix direction and its retest rows; re-run the original row and the rows sharing its data or event); SKILL §7 row 16; self-review QS-19 | standard; core principle; self-review check |  |
| CR-09 | Fresh eyes: flip the image, change the reviewer | SKILL T-06 (one agent never invents, triggers and grades its own fault) | standard (kept) | partial: mirroring images is a craft self-review; QA does not judge drawn balance |
| CR-11 | The project's needs come first; map every feedback item | role "Hand-back" (coverage lists every behaviour in scope with its verdict); self-review QS-17, QS-20 | standard; self-review check |  |
| CR-15 | Start from the player's pain points | SKILL T-03 (the owner's reported scene), T-02, T-08 | standard (kept, sharpened) |  |
| CR-17 | Say what each input can prove; could-not-check list | SKILL T-20, T-07 (label), §5 rule; player-facing §5; records §2 items 2-3; self-review QS-13, QS-18 | standard; quality bar; self-review check |  |
| CC-02 | One marker list is the timing contract | player-facing PF-14 (events fire once on their ids; marker times against the timing list), PF-15 (sync rule, device only), §3 sources; SKILL §7 row 8; self-review QS-04 | step; standard; self-review check |  |
| GD-02 | Every action gets immediate feedback; short celebration | player-facing PF-01 (attempt cue), PF-03 (distinct outcomes; celebration ends before the next decision); self-review QS-02 | standard; self-review check |  |
| GD-07 | Art and mechanics promise the same thing | player-facing PF-12 (looks solid blocks, looks open passes, ledges against jump height); self-review QS-04 | standard; self-review check |  |
| GD-13 | Fairness from clear expectations and consistency | player-facing PF-08 (same tell every time: attacker at a fixed position and facing, the log as oracle, two captures compared as the screening aid), PF-04 (no random fuse); SKILL T-18; worked-examples §1 | standard; example |  |
| GD-21 | Low mental load on the player's own character | — | — | rejected: own-move recognisability at the key pose is the animator's and game designer's silhouette judgement; no QA oracle |
| GD-30 | Every hazard has written rules | player-facing PF-12 (a test per hazard rule); worked-examples §1 (damage rule at 11.9 and 12.1 studs); self-review QS-04 | standard; example; self-review check |  |
| GD-34 | Feedback follows the real outcome | SKILL T-14, §5 rule, §7 row 19; player-facing PF-02, PF-03; methods §2 (presentation faults); self-review QS-02, QS-14 | standard; quality bar; core principle; self-review check |  |
| GD-35 | Paid random reveals are honest | SKILL T-16, §5 rule; player-facing PF-06; worked-examples §2; self-review QS-05 | standard; quality bar; example; self-review check |  |
| LC-01 | Reserve the gameplay colours; pair with shape | player-facing PF-07 (second channel in data), PF-08 (no hue literal in logic; code scan) | standard; self-review check (QS-05) | partial: the reserved-hue pixel share is the art director's measure |
| LC-21 | Test colours where parts overlap | — | — | rejected: a modelling and art-direction value check; no QA oracle |
| LC-24 | Check colour on a phone before it ships | — | — | rejected: colour-profile and device colour checks are the art director's and marketing's; my device runs are performance and sync (PF-15) |
| PP-01 | Set budgets before building; phones first | SKILL §5 rule (phone performance without a phone is BLOCKED; kept); role "Working with other agents" (performance-engineer owns captures) | standard (kept) | partial: triangle and texture budgets are the modeler's and performance-engineer's checks |
| PP-11 | Clean meshes, clean collision | player-facing PF-12 (walk along walls: no snag) | standard; self-review check (QS-04) | partial: mesh and UV cleanliness is the modeler's audit |
| PP-12 | Build to the shared rig | player-facing PF-13 (sockets equal the base) | standard | partial: joint matching and shared-clip playback are the rigger's and animator's checks |
| PP-13 | Keep the contact points fixed in every variant | player-facing PF-13 (socket and attachment positions equal the base, probe) | standard; self-review check (QS-05) |  |
| PP-20 | Plan the states first; clips interrupt and blend | player-facing PF-14 (every transition in the state list exercised with no error) | standard; self-review check (QS-04) | partial: pops and foot slides are the animator's judgement |
| PP-21 | Read the curves behind the motion | — | — | rejected: per-control curves are the animator's `clip_check.py` work; my equivalent "read the numbers, not the picture" is T-15 (data oracles), which rests on GD-34 and VR-20 |
| PP-23 | Fix gimbal flips at the source | — | — | rejected: rigging and animation export craft |
| PP-27 | Block out on a grid; snap art to the approved blockout | player-facing PF-12 (collision and cover equal the approved blockout, tested routes replayed) | standard; self-review check (QS-04) |  |
| PP-29 | One owner per file; clear names on every submission | SKILL T-06 (acceptance where the builder cannot write), T-10 (the sequence is the test name), T-07 (revision on every result); role "Write scope" | standard (kept) |  |
| PI-02 | Gates freeze decisions | SKILL T-06, T-07 (a pass on an older revision does not carry over), §7 row 15 | standard; core principle |  |
| PI-04 | Block out first, in the engine, play it before detail | SKILL §3 step 3 (hooks and rows at plan time), §7 row 15; self-review QS-06 | step; core principle; self-review check | partial: the greybox itself is the builder's and level designer's |
| PI-07 | One named problem per pass; worst first | records §3 (one finding per problem); SKILL §7 row 16 | standard; core principle |  |
| PI-11 | A time box forces the readable choice | SKILL §7 row 18; self-review QS-21 (stop criteria) | core principle; self-review check |  |
| PI-12 | Know when it is done: stop criteria, repeating notes | SKILL §7 row 18; records §3 (a round with only repeats closes the loop); self-review QS-21 | core principle; standard; self-review check |  |
| SS-02 | Judge the silhouette filled solid | — | — | rejected: silhouette reading is the crafts' and art director's |
| SS-03 | Break the silhouette with broad cuts | — | — | rejected: modelling craft |
| SD-01 | Sound's three jobs; screen covered | player-facing PF-03 (each outcome its own cue), PF-07 (every warning a second channel; sound off) ; self-review QS-04, QS-16 | standard; self-review check | partial: naming events with the screen covered is the sound designer's listening test |
| SD-06 | Attach sounds to events, listed and tested | player-facing PF-14 (each event fires once on its id), §3 sources (sound event list); self-review QS-04 | standard; self-review check |  |
| SD-26 | Review the key event solo, then in the full mix | — | — | rejected: listening is the sound designer's and the owner's; I have no audio input (PF-15) |
| SD-27 | Sound notes in technical terms | — | — | rejected: I give no sound notes; findings rest on the log |
| UI-03 | Design for the device: phone first | player-facing §1 (smallest supported phone, Device Simulator), PF-11 (thumb zones), PF-09; self-review QS-08 | step; standard; self-review check |  |
| UI-10 | Critical information in fixed, prominent places | player-facing PF-11 (fixed zone at the smallest phone), PF-09 (critical facts present) | standard; self-review check (QS-04) |  |
| UI-12 | Motion goal: responsiveness | player-facing PF-01; §4 press lag | standard; self-review check (QS-02) |  |
| UI-17 | Seed the motion table with tested durations | player-facing PF-01 (same on every button), PF-05 (count-up under its motion-table cap) | standard; self-review check (QS-03) | partial: the table values are the UI designer's |
| UI-18 | Errors and denials say what is wrong and how to fix it | player-facing PF-11, PF-02 (refusal cue); worked-examples §2; self-review QS-14 | standard; example; self-review check |  |
| UI-19 | Counters tell the truth | SKILL T-15; player-facing PF-05; methods §2 (affordability reads the tweened counter fault); worked-examples §2, §3; self-review QS-03 | standard; example; self-review check |  |
| VC-02 | Values first; a grayscale proof | player-facing §1 (grayscale condition), PF-07 | step (condition); self-review check (QS-16) | partial: value structure is the crafts' |
| VC-05 | A value and saturation band per layer | — | — | rejected: art director's measure; no QA oracle |
| VC-06 | Test every character against every background; markers 3:1 | player-facing §4 (marker contrast, borrowed; `fg_sample.hex` guard against a stray box), PF-09 (busiest stage area, lowest quality) | step; self-review check (QS-10) |  |
| VC-08 | Head, shoulders and hands carry the read | — | — | rejected: character value craft |
| VR-06 | Budget each effect's footprint for the worst-case crowd | player-facing PF-09 (busiest moment, every player's effect at once), §1 | condition; self-review check (QS-08) | partial: the footprint measure is the VFX designer's (IG-02) |
| VR-07 | Never cover what the player needs to see | player-facing PF-09 (I run the conditions; the cover measure is IG-02) | condition; self-review check (QS-08) |  |
| VR-08 | Real-time effects are built for cost | SKILL §5 rule (phone performance BLOCKED without a phone); player-facing §1 (quality-scaled effects keep their information layers), PF-09 | quality bar; condition |  |
| VR-13 | Strobes stay low; the focus never flashes | SKILL T-17, §5 rule; player-facing PF-07, §4 flash count; self-review QS-16 | quality bar; self-review check |  |
| VR-19 | Rate each effect per viewer | player-facing PF-16 (bystander camera; at every `Clarity` level threats and pickups keep `LocalTransparencyModifier` 0; the `Viewer` and `Clarity` hooks prove the branch, two clients prove the path, else BLOCKED: repair round 2), §1 (two clients), §3 hooks `Clarity`, `Viewer`; worked-examples §1 PF-16; self-review QS-05 | standard; example; self-review check | partial: the importance ratings per viewer and the attention cap are the VFX designer's spec; the player-count sweep for time-to-find is a playtest, not a test oracle |
| VR-20 | The drawn danger area is the real hit area | SKILL T-15, §5 rule; player-facing PF-04, §3 `DebugShape`, §4 drawn size; methods §1 (data-field oracle), §2 (ring from its own constant); worked-examples §1; self-review QS-03 | standard; quality bar; example; self-review check |  |
| VR-21 | Camera punches rare, local, gated | player-facing PF-10 (no `cam` line during either repetition run: repair round 2), PF-16 (bystander camera never moves; no `cam` line under `Viewer` = bystander), PF-07 (reduced removes camera motion); worked-examples §3 PF-10 burst | standard; example; self-review check (QS-05, QS-15, QS-16) | partial: the channel-against-importance band, rotation-only shake and the wall-clipping check are the VFX designer's spec review and the reviewer's code read |
| VR-22 | Hit-stop is local, short, scaled | player-facing PF-16 (a hit-stop pauses nothing on the server or the other client) | standard | partial: the freeze length and pose are the VFX designer's and animator's (IG-11) |
| VR-23 | Every intense channel has an off path | SKILL T-17, §5 rule, §7 row 20; player-facing PF-07, `Reduced` hook; methods §2 (reduced variant drops the telegraph); self-review QS-16 | standard; quality bar; core principle; self-review check |  |
| VR-24 | Frequent effects shorter, merged, capped | SKILL T-10; player-facing PF-10; worked-examples §3; self-review QS-15 | standard; example; self-review check |  |
| VR-26 | Pulse and blink rates carry meaning; never above 3 Hz | player-facing PF-07 (no pulse or blink above 3 Hz at full contrast; countdowns step on the server timer; rates from the spec, the VFX designer's IG-08 box reading on a folder; a spec-only rate stays D), PF-04 (countdown = server timer); SKILL T-17, §5 rule, §7 row 20 ("PF-07 caps"), QS-16 (a spec-only rate is labelled D, on-screen rate not verified until the box reading: repair round 2); worked-examples §1, §3 (honest ends name the on-screen rate as not verified) | standard; quality bar; example; self-review check (QS-16) |  |
| VH-04 | Judge noise in motion, with lighting and effects on | player-facing §1 (busiest moment, effects on), PF-09 | condition | partial: naming the character in a glance is the craft's read |
| VH-07 | Recognisable in under a second | — | — | rejected: a craft read; no QA oracle |
| WT-01 | Anticipation must read; long enough to react | player-facing PF-04 (tell length against the timing list over 20 runs; telegraph removed on the damage frame); worked-examples §1 | standard; example; self-review check (QS-03) | partial: the pose silhouette is the animator's |
| WT-06 | Shift the weight before a foot moves | — | — | rejected: animation craft |
| WL-01 | Readability beats beauty; test the busiest moment | SKILL T-13, §7 row 1; player-facing PF-09, §1 | standard; core principle; self-review check (QS-08) |  |
| WL-02 | Items identifiable on the ground, partly hidden | — | — | rejected: a craft read; no QA oracle |
| WL-03 | Every piece says what I am and what you can do | player-facing PF-12 (what looks climbable or open behaves so) | standard | partial: the setting read is the environment designer's |
| WL-07 | The first view tells where you are | player-facing PF-12 (spawn positions and facing equal the approved layout) | standard (data check) | partial: what the first view shows is the level designer's call |
| WL-14 | Flat play spaces; height changes intentional | — | — | rejected: level design judgement |
| WL-20 | It must read at the lowest graphics setting | SKILL T-13; player-facing §1 (lowest and highest quality), PF-04, PF-09, PF-12; self-review QS-08 | condition; standard; self-review check |  |
| WL-21 | Scale: a player-sized reference | — | — | rejected: scale belief is the environment and level designers'; the measurable part (ledges against the jump height) lands from WL-29 |
| WL-28 | Work from far away; zoom out every round | player-facing §1 (game camera, smallest phone) | condition | partial: a craft working habit; my form is the conditions |
| WL-29 | Plan routes in player metrics; ledges against jump height | player-facing PF-12 (ledges against the jump measured in the game's place, the level designer's §6.6 probe; JumpPower 50 by default, not the 7.2-stud JumpHeight) | standard; self-review check (QS-04) |  |
| WL-30 | Score a level review on ten fixed checks | — | — | rejected: the level designer's review; my stage rows are PF-12 |
| VR-25 (untagged) | Randomise decoration only; lock meaning | SKILL T-19 (test the range where it lives), §7 row 12; methods §1 range row (engine ranges: the read of every semantic layer on the candidate, `Lifetime`, `Speed`, `Rotation`, `RotSpeed` Min = Max, `Size`, `Transparency`, `Squash` envelopes 0, `FlipbookStartRandom` false, `SpreadAngle` as the spec; code-rolled ranges: both ends offline with an injected random source; `Seed` only repeats a server roll), §2 (planted fault: envelope or random start on a semantic layer); worked-examples §1 (T-19 row, planted envelope fault); self-review QS-12 (repair round 2) | standard; core principle; example; self-review check |  |
| UI-05 (untagged) | UI is every screen and state | player-facing PF-11 (every state reached); self-review QS-04 | standard; self-review check |  |
| UI-06 (untagged) | One UI ecosystem with written rules for meaning | player-facing PF-08 | standard; self-review check (QS-05) |  |
| UI-15 (untagged) | One motion table | player-facing PF-08 (motion rows in shared data), PF-01 (same press on every button) | standard |  |
| GD-16 (untagged) | Cosmetics never change the gameplay read or cost gameplay | player-facing PF-13 | standard; self-review check (QS-05) |  |
| GD-17 (untagged) | Cosmetics change no stats | player-facing PF-13 (data diff) | standard; self-review check (QS-05) |  |
| GD-31 (untagged) | Art stays inside the blockout's gameplay | player-facing PF-12 (collision and cover equal the approved blockout: tested routes and angles replayed; scripted diff proposed) | standard; self-review check (QS-04) |  |
| WL-15 (untagged) | Predictable geometry | player-facing PF-12 (no snag) | standard |  |
| SD-30 (untagged) | Cues are data; no asset id in logic | player-facing PF-08, §4 code scan (points to the builder's literals grep and the sound designer's R-44) | standard; self-review check (QS-05) |  |
| PI-14 (untagged) | "It would be cooler" is new scope | records §3 (anything outside the brief is a new request); SKILL §7 row 18 | standard |  |
| CR-13 (untagged) | Close with an honest recap | self-review QS-21; worked-examples (each ends with an honest end) | self-review check; example |  |
| VR-01 (untagged) | Review muted first (DS check) | player-facing §1 (sound off), PF-07 | condition |  |

### b. Universal principles

| UP-ID | Applies | Where in "Core principles for this craft" |
| --- | --- | --- |
| UP-01 | yes: my first rows prove the player can know what happened and what threatens them | `testing/SKILL.md` §7 row 1 |
| UP-02 | yes: player-facing rows run under the conditions players meet | §7 row 2 |
| UP-03 | no: spending contrast and ranking reads is the makers' and art director's craft; I check that critical facts are present (UP-01), not which is read first | — |
| UP-04 | no: big-before-small is a making order; my nearest form (rows and hooks before tests) is UP-13 and UP-15 | — |
| UP-05 | no: shape and silhouette reads are craft judgements with no QA oracle; the shape-paired-with-colour part is tested under UP-20 | — |
| UP-06 | yes, limited: the fewest checks that give the strongest proof (one row per behaviour, one shared check per symptom) | §7 row 6 |
| UP-07 | yes: one code tested as data and repeats | §7 row 7 |
| UP-08 | yes: cause before effect in the log; tells end on the damage frame | §7 row 8 |
| UP-09 | no: exaggeration is a making choice | — |
| UP-10 | no: the subject's character is the makers' and designers' | — |
| UP-11 | no: style identity is the art director's; the gameplay side of variants is tested under UP-07 and UP-19 (PF-13) | — |
| UP-12 | yes, limited: variation only on decoration; both range ends tested | §7 row 12 |
| UP-13 | yes: sources, trace table and hooks before tests (the master lists it for engineering and review; my trace table is the same habit) | §7 row 13 |
| UP-14 | no: I do not make options; the nearest habit (several oracles per rule) is T-04 | — |
| UP-15 | yes: hooks at plan time; acceptance frozen with the candidate | §7 row 15 |
| UP-16 | yes: findings name the goal, layer and evidence | §7 row 16 |
| UP-17 | yes: tests and hook requests the builder can use; repeated checks become shared checks or tools | §7 row 17 |
| UP-18 | yes: stop criteria for a test set | §7 row 18 |
| UP-19 | yes | §7 row 19 |
| UP-20 | yes | §7 row 20 |

### c. Old book changes

| Old text (file:line at df13ff4) | Kept / sharpened / replaced by / moved / removed | Why |
| --- | --- | --- |
| `roles/qa-lead.md:28` "Craft practice from Riot's artists and designers: `knowledge/jobs/J016-orchestration/riot-extracts.md` §4 (row qa-lead)" | removed; its content (art and mechanics agree, never blindside the player) now lives in `player-facing.md` PF-12, PF-08 | J018 fixed list: role files point to their own books, not to the J016 extracts |
| `roles/qa-lead.md:14` intro sentence | sharpened (adds "where players meet it" and the truth rows) | the role now owns presentation truth |
| `roles/qa-lead.md:18` skills order line | sharpened (§6, §7, `player-facing.md`; `platform-policy` §A wins) | new book layout |
| `roles/qa-lead.md:30-36` Work method 1-6 | replaced by Work method 1-8 (sources, hooks at plan, conditions) | the order now asks for hooks before the build and names conditions |
| `roles/qa-lead.md:38-42` Working with other agents | sharpened (expected and observed result; a note's solution restated as its problem; crafts own looks) | CR-03, CR-06 |
| `roles/qa-lead.md:46-50` Hand-back | sharpened (hooks, conditions, labels, could-not-check list) | CR-17 |
| new | role "What you ask partners for, and when"; "Before you hand back" | V8 |
| `testing/SKILL.md:6` header | sharpened (J018 phrase and author tag) | brief |
| `testing/SKILL.md:10` intro | sharpened (adds the presentation half) | — |
| `testing/SKILL.md:12-13` §1 | sharpened (craft work wired in; re-read §3, §6, §7 after compaction) | V7 |
| `testing/SKILL.md:15-22` §2 table | sharpened (new rows for `player-facing.md`, `worked-examples.md`, `studio-mcp`) | — |
| `testing/SKILL.md:24-30` §3 steps 1-6 | replaced by steps 1-8: sources (new), trace table with PF-rows, hooks at plan time (new), data and conditions, oracle (data oracles added), write and run, protect and run, report with inputs | UP-13, UP-15, CR-01, CR-17 |
| `testing/SKILL.md:37` T-03 | sharpened: "real conditions" added | CR-01, WL-01, WL-20 |
| `testing/SKILL.md:39` T-05 | sharpened: presentation faults added to the example list | GD-34, VR-20 |
| `testing/SKILL.md:41` T-07 | sharpened: conditions and the label added to each result | CR-17 |
| `testing/SKILL.md:43` T-09 | sharpened: rendering at a quality level added to engine behaviour | WL-20 |
| `testing/SKILL.md:44` T-10 | sharpened: repetition at the real rate added | VR-24 |
| new | T-13 to T-20 | J018 material |
| `testing/SKILL.md:48-53` §5 rules | kept; four rules added (no truth by eye, no PASS beyond the input, the blocking presentation faults, hooks only in the test build); "sound sync without device: not verified" added to the phone line | GD-34, VR-20, VR-23, CR-17 |
| `testing/SKILL.md:55-61` §6 self-check (5 lines) | replaced by QS-01 to QS-21 by stage with inputs and the image budget; the five old lines are kept inside QS-01, QS-07, QS-11, QS-13, QS-20 | V1, V5 |
| new | §7 Core principles for this craft | J018-D2 point 2 |
| `methods.md:1` header | sharpened (J018 phrase) | brief |
| `methods.md:5-13` §1 oracles | kept; three rows added (server result in the log, gameplay data field, seeded range ends) | T-15, T-19 |
| `methods.md:17` §2 step 2 | sharpened: presentation faults | T-05 |
| `methods.md:22-27` §3 | sharpened: pointer to the conditions matrix (one place) | V6 |
| `records.md:1` header | sharpened | brief |
| `records.md:27-28` result card items 2-3 | sharpened (labels and conditions; could-not-check) | CR-17 |
| new | `records.md` §3 Findings | CR-02, CR-03, CR-06, CR-08, PI-07 |
| `roles/qa-lead.md:24` "stage (after the sound and VFX ambience check)" | dropped in the rebuild, restored in repair round 1 | the stage recipe still orders it (`job-types.md` §3 Review order); review R5 |
Nothing old was removed as wrong; every old rule is still in the books.

### d. Command runs (V3, V12)

Samples in `C:\Users\Firew\AppData\Local\Temp\claude\C--Users-Firew--claude-spares-spare-5bnXLW\15d0fbc0-e7e9-4bea-af68-9ddb5da374ba\scratchpad\qa-lead-v3\` (generators `make_press.py`, `make_flash.py`, `make_reveal.py` kept there). The input forms match what the books name: frames `f###_<ms>ms.jpg` at 30 fps; press folders cropped to the control with idle frames before the press; busiest-scene folders in scene (sky, ground, players), fixed camera; reveal folders starting on the press frame; JPEG quality 95.

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| PF-01 press lag | `python tools/vfx/clip_metrics.py <folder>` then the S-33 lag line from `ui-design/references/review.md` §6, press ms 433 | 20-frame press folder, cue on the frame after the press | runs, writes `metrics.json`; pre-press max 0, cue 467, lag 34 ms (33 ms real: ms in names are rounded): PASS, right answer |
| PF-01 | same | press folder with no press look | `cue None`: UNVERIFIED by the book's rule (not a false PASS) |
| PF-01 | same | small cue, then a full-crop popup 2 frames later | lag 34 ms, `onset_ms` 467: right here; the book keeps the partner's warning that `onset_ms` is never the lag |
| PF-07 flash count | `python flash_pulse_vfx.py <folder> 30` (the studio counter, `vfx-craft/references/measure.md` §6, saved unmodified, 43 lines) | busiest-scene folder, 3 full-screen flashes in 1 s | 3 and 3: at the cap (design target 2): right answer |
| PF-07 | same | 4 full-screen flashes in 1 s | 4 and 4: FAIL over the cap: right answer |
| PF-07 | same | 4 flashes in 1 s over 5 % of the frame | 0 at 10 %, 4 at 3 %: right answer; shows why both counts are read |
| PF-06, PF-08 reveal difference | the S-44 one-liner from `ui-design/references/review.md` §6, egg box 270,130,370,250 | two lowest-tier folders (noise pair) | every windup frame (0.56-0.69 mean, 0 changed px): the floor |
| PF-06 | same | lowest vs top tier, no tell in the windup | windup frames at the floor; result frames 51.4 mean, about 8,030 px: right answer |
| PF-06 | same | lowest vs top tier with a 10 px gold glint in windup frames 8-14 | 101-118 changed px on frames 8-14 against 0: caught |
| PF-06 | same, whole-frame box | same | the mean moves only 1.43 → 1.46 (inside noise), the count still shows 101-118: recorded as the false reading "a loose box dilutes the mean" |
| PF-07, PF-09 marker contrast | `python tools/art/look_check.py contrast --sample <still> --fg-box 316,221,324,226 --bg-box 300,240,340,260 --min-ratio 3 --tolerance-source "QA PROPOSAL"` | in-scene still, yellow ring on mid sand | 2.85, fail: right answer |
| PF-07 | same | ring on bright sand | 1.44, fail: right answer |
| PF-07 | same | ring on dark ground | 8.45, pass: right answer |
| PF-07 | same, foreground box 310,215,330,235 (loose) | ring on dark ground | 1.0, fail with no error: recorded as a known false reading (a box that strays off a thin ring samples the ground) |
| PF-08 code scan | the code scan of `testing/references/player-facing.md` §4 (`grep -rnE` for asset-id strings and colour constructors in `src/**/*.luau`), data modules dropped | synthetic `src/` with a data module and a logic file holding an asset string, a colour literal and a bare numeric id | 2 hits in the logic file, the data module dropped; the bare number missed: recorded as a known miss |
| PF-07, PF-09 marker contrast guard (repair round 1, R2) | `python tools/art/look_check.py contrast --sample ring_dark.png --fg-box 310,215,330,235 --bg-box 300,240,340,260 --min-ratio 3 --tolerance-source "QA PROPOSAL"`, then the same with `--fg-stat p90` | in-scene still, yellow ring on dark ground, loose box | median: 1.0 fail with `fg_sample.hex` #3C4632 = the ground's `bg_sample.hex` (the guard catches the stray box); p90: 8.45 pass with #FFF05A (the ring): right answer. On mid sand p90 gives 2.85, the same as the tight box. Wrong with no error when: a dark marker on light ground read with p90 (use p10), or a box that holds a brighter highlight than the marker |
| PF-08 code scan (repair round 1, F6) | the builder's literals grep (`engineering-craft/references/presentation.md` §10) and R-44's grep (`sound-design/references/review.md`), unmodified, from the source root | synthetic `src/` (`C:\Users\Firew\AppData\Local\Temp\claude\C--Users-Firew--claude-spares-spare-5bnXLW\15d0fbc0-e7e9-4bea-af68-9ddb5da374ba\scratchpad\qa-lead-rep1\src`): a data module, and a logic file with `Color3.fromRGB`, `fromHex`, `fromHSV`, `BrickColor.Red()`, `BrickColor.new("Bright red")`, an `http://www.roblox.com/asset/?id=` `SoundId`, an `.Asset =` id, a joined id, a `Texture` id | the colour grep hits fromRGB, fromHex, fromHSV and `BrickColor.new("Bright red")` (through its quoted-string pattern) plus the data module (dropped by the rule); R-44 hits the `.Asset =`, the joined id and the `Texture` id. Both miss `BrickColor.Red()` and the `asset/?id=` id with no error: listed as known misses in `player-facing.md` §4 and proposed to the owners |
| PF-12 jump (repair round 1, F2) | `inspect_instance` on `StarterPlayer` and `Workspace`, then the level designer's ladder probe | a default place with a 7.0-stud ledge | NOT RUN: `list_roblox_studios` returned no Studio again; the docs mirror lines above give JumpPower 50 by default, so the starting value (6.4 studs, level-design §6.6) makes the 7.0-stud ledge a wall |
| Studio rows (quality level, Network Simulator, `DelayMs`, Reduce Motion route, Device Simulator capture, grayscale effect, debug log read) | Studio MCP | — | NOT RUN: `list_roblox_studios` returned no Studio. Each is written as "probe once and record" in `player-facing.md` §1 and §4 |

Proposal rows from other roles against my books (V11): at the first hand-back a grep of the proposal files then present found no row whose target is `testing` or the qa-lead role. Repair round 1, grep of all 20 files: `proposals/feature-builder.md` row "`.agents/skills/testing/`" (acceptance cases: rejected request, burst merges with the counter exact, affordability during a count-up, identical windup over seeded rolls, reduced override keeps the information) is **adopted**: met by PF-02, PF-05, PF-06, PF-07 and PF-10 (with the `Reject`, `Rate`, `Set`, `Outcome`/`Seed` and `Reduced` hooks). The architect's and reviewer's rows that name the qa-lead target `job-types.md` and `job-feature.js`, not my books: nothing to adopt. Related rows I support (recorded in `proposals/qa-lead.md`): vfx-designer row "Integrator delivers the test hooks" (job-types §6) — seconded; game-designer row `tools/vfx/seq_compare.py` — seconded (my PF-06 and PF-08 use the same comparison); sound-designer row "debug cue log convention" (engineering-craft) — already met by `engineering-craft/references/presentation.md` §9, which my books use; vfx-designer and others' `flash_count.py` tool row — seconded.

V5 pass (scripted, before hand-back): every landed-in location above was opened; every row whose finding has a runnable check names a QS line or a PF row that a QS line covers (QS-02 → PF-01, PF-02, PF-03; QS-03 → PF-04, PF-05, PF-06; QS-04 → PF-11, PF-12, PF-14; QS-05 → PF-06, PF-07, PF-08, PF-10, PF-13, PF-16; QS-08 → PF-09; QS-12 → T-19; QS-14 → PF-02; QS-15 → PF-10; QS-16 → PF-07; QS-18 → PF-15). The three worked examples were re-read after the PF renumbering and the hook-name change.

### Repair round 1 (stage 3 review `reviews/qa-lead-rev1-reviewer.md`, verdict fix-first)

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 hook names | fixed: `player-facing.md` §3 hooks table (two rows `Outcome`/`Seed` and `Set` replace the "not in the builder's set yet" row), PF-03, PF-05, PF-06 (incl. the restricted path), PF-11; `SKILL.md` §3 step 3, QS-12 (`Seed` for both range ends); `worked-examples.md` §1-§3 hook lines. Retest: grep "not in the builder" and "not yet in" over the five files → 0. `proposals/qa-lead.md` row 6 marked met |
| F2 jump default | fixed: PF-12 now uses the jump measured in the game's place (level-design `review-artifact.md` §6.6 probe, value in the game profile), reads `CharacterUseJumpPower`, `CharacterJumpPower` or `CharacterJumpHeight` and `Workspace.Gravity` first, and says JumpPower 50 governs by default, so the 7.2-stud JumpHeight does not apply; the starting value is pointed to, not copied (V6). `WalkSpeed` 16 kept. Docs mirror re-checked (`StarterPlayer.yaml:330-340`, `Humanoid.yaml:640-650`). Studio retest NOT RUN (no Studio connected; table d) |
| F3 smallest_fix | fixed: `records.md` §3 smallest_fix is now the smallest fix direction stated as what must hold, never code or how to build it, then `retest:` rows; the "a suggested solution in a note I receive is restated as its problem first" clause kept; `SKILL.md` §7 row 16 and its example (fix direction + retest PF-02); QS-19; the role's "Working with other agents" line for failing acceptance tests |
| F4 pulse cap | fixed: PF-07 adds "no pulse or blink above 3 Hz at full contrast; countdowns step toward the event on the server timer", with the VFX designer's IG-08 box reading pointed to; T-17, the §5 blocking rule, QS-16 and §7 row 20 name "the PF-07 caps" (flash and pulse); worked examples §1 (ring pulse) and §3 (glint pulse). The review's retest expected "3 Hz" also in QS-16 and §5; under R3 and V6 the number lives only in PF-07 and the others name the cap, so grep "3 Hz" → PF-07 only, and grep "PF-07 cap" / "PF-07 pulse" / "PF-07 flash" → SKILL.md 4, worked-examples 2 |
| F5 image budget | fixed: PF-04 is numbers for every tier, skin, quality level and viewer (drawn size against the data radius, the after-last-tick count, 20 fuse logs); stills with `DebugShape` only for one key case (lowest quality, threatened view: warning, contact, end = 3) and for failing or borderline numbers; worked example §1 says 24 numbers, 3 stills. Retest: stills named per row in the worked examples ≤ 4 |
| F6 copied scan | fixed: the `player-facing.md` §4 code-scan row points to the builder's literals grep (`engineering-craft/references/presentation.md` §10, limits §11) and R-44 (`sound-design/references/review.md`); my own grep block removed. Both partner greps run on a synthetic tree (table d): fromHex and fromHSV hit; `BrickColor.Red()` and `asset/?id=` ids are missed by both, so they are listed as known misses and proposed to the owners (proposals rows) |
| R1 tell comparison | adopted: PF-08 places the attacker at one fixed position and facing before each `Trigger` and makes the log the oracle (same `cue` and `vfx` ids at the same `f` offsets from `evt`); the frame difference is the screening aid; §4 known false readings add "an attacker at a different position or facing"; worked example §1 PF-08 row rewritten |
| R2 marker contrast guard | adopted: §4 marker-contrast row adds the `fg_sample.hex` guard and the `--fg-stat p90` (light) / `p10` (dark) rerun, run on the sample (table d); proposal row to the vfx-craft owner of the recipe |
| R3 one number, one place | adopted: the flash cap number stays only in PF-07 (pointing to IG-07); T-17, §5, §7 row 20 and worked example §3 say "the PF-07 caps" |
| R4 restore pointer | fixed: role "Write scope" points to `studio-mcp` §3 step 5 and its probes P-05 |
| R5 stage order | fixed: "(after the sound and VFX ambience check)" restored in the role's "Your place in the job flow"; added to table c |
| R6 V11 | fixed: the feature-builder row against `testing` adopted (met by PF-02, PF-05, PF-06, PF-07, PF-10), line above table d's end; `proposals/qa-lead.md` row 6 marked met |
| R7 §7 reasons | fixed: `SKILL.md` §7 intro now carries the reason itself ("they judge how a thing reads or is made, which has no test oracle; their data side is tested under 1, 7, 19 and 20"); no pointer to the job file |
| R8 description | fixed: description adds "and what they see matches the server" (397 of 400 characters) |
| keep list | kept unchanged: conditions matrix (§1), PF catalogue with data and server-log oracles and "never the eye as the oracle for a truth", hooks at plan time by the builder's names, the "what each input can prove" table and the could-not-check list, the screening-aid rule with the asymmetric log rule, presentation faults in the planted-fault list, `records.md` §3 fields other than smallest_fix, the role's "What you ask partners for, and when" table, every old rule |

V5 pass after the repair: every landed-in location changed in this round (records §3; SKILL §3 step 3, T-17, §5, QS-12, QS-16, QS-19, §7 intro, rows 16 and 20; player-facing PF-03 to PF-08, PF-11, PF-12, §3, §4; worked examples §1-§3; role lines 24, 53, 58) was opened after the edit; the three worked examples were re-read against the changed PF-04, PF-07, PF-08 and hook rows. Files written with LF endings; role frontmatter lines 1-10 still identical to `df13ff4` (`diff`).

### Repair round 2 (stage 3 review `reviews/qa-lead-rev2-reviewer.md`, verdict fix-first)

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 range ends | fixed: `SKILL.md` T-19 (test the range where it lives; `Seed` never reaches a particle range), QS-12 (inputs D, C, T: the read of every semantic layer plus both ends of every code-rolled range; "a `Seed` run alone is not this check"), §7 row 12; `methods.md` §1 row renamed "Range ends, by where the range lives" (engine ranges: after a `Trigger`, `inspect_instance` or one `execute_luau` read of each layer the effect `spec.json` marks `semantic`: `Lifetime`, `Speed`, `Rotation`, `RotSpeed` Min = Max, keypoint `Envelope` of `Size`, `Transparency`, `Squash` 0, `FlipbookStartRandom` false, `SpreadAngle` as the spec; pointed to the VFX designer's SP-06 and CP-09, not copied; code-rolled ranges: an injected random source at the lowest then highest value; its false readings listed: renamed layer skipped silently (count read against marked), a layer wrongly marked decorative, emit-time script randomness, a `Rotation` range on a symmetric sprite), §2 planted fault added; `player-facing.md` §3 `Outcome`/`Seed` row no longer serves ranges; worked example §1 T-19 row and a planted envelope fault. Engine facts checked in the docs mirror: no seed property on ParticleEmitter, Beam or Trail (grep 0); `Lifetime`, `Rotation`, `RotSpeed`, `Speed` are NumberRange; `Size`, `Transparency`, `Squash` are NumberSequence whose keypoint envelope draws a random value per particle (`ParticleEmitter.yaml:796-814, 983-1001`); `SpreadAngle` is a random emit angle (`:858-866`). Note on the review's retest: `Size` is not a NumberRange in the engine, so "Size NumberRange(10,12)" is modelled as a size envelope on the ring's keypoints; the retest is in table d below |
| R1 camera on repeats | adopted: PF-10 adds "no `cam` line during either run (a frequent event never moves the camera)"; worked example §3 burst row; VR-21 marked partial for the importance band, rotation-only and wall-clipping parts (VFX designer's spec review, reviewer's code read) |
| R2 `Clarity` hook | adopted: `player-facing.md` §3 hooks row `Reduced`, `Clarity`, `Viewer` with the builder's values and "they prove the branch, not the path"; PF-16 adds "at every clarity level threats and pickups stay full (`LocalTransparencyModifier` 0, read on the client)" and splits the scenario: one client with `Viewer` and `Clarity` proves the branch (MCP-verified; the builder's Per viewer check, pointed to), two clients prove the path, else that half is BLOCKED; `SKILL.md` §3 step 3 hook list; worked example §1 PF-16 row. V11: `proposals/feature-builder.md` row 36 **adopted** (hook-name half met in round 1, `Clarity` half now) |
| R3 spec-only rates | adopted: QS-16 "a rate read only from the spec is labelled D, and its on-screen rate stays not verified until the box reading on a folder"; PF-07 points to it ("a spec-only rate stays D, QS-16"); worked examples §1 and §3 honest ends name the ring's and the glint's on-screen pulse rate as not verified (spec only) |
| R4 `evidence` key | adopted: `records.md` §3 splits `observed` (what happened, one line) from `evidence` (the log line, probe output or still with its path and label; a finding without evidence is a question), matching `rules/messages.md` §6; `goal and layer` kept |
| keep list | kept unchanged: every round 1 fix; conditions matrix with probe-once routes; the PF catalogue with data and server-log oracles and "never the eye as the oracle for a truth"; hooks asked for at plan time by the builder's names; the "what each input can prove" table and the could-not-check list; the screening-aid rule with the asymmetric log rule; the borrowed measures as pointers with their false readings; records §3 smallest_fix as "what must hold" plus retest rows; PF-04 numbers for every variant with 3 key stills; PF-12 on the measured jump; the role's "What you ask partners for, and when"; every old rule. The role file needed no change this round |

Table d, repair round 2 (V3, V12; script `C:\Users\Firew\AppData\Local\Temp\claude\C--Users-Firew--claude-spares-spare-5bnXLW\15d0fbc0-e7e9-4bea-af68-9ddb5da374ba\scratchpad\qa-lead-rep2\qa-lead_range_read.py`):

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| QS-12 / methods §1 engine range read | `inspect_instance` / `execute_luau` on the semantic layers | — | NOT RUN in Studio: `list_roblox_studios` returned no Studio. Written as a property read per layer (no code block in the book, V13) |
| QS-12 rule logic | a Python model of the read on a synthetic property dump of the shape a read returns (spec with Ring and Flash marked semantic, Dust decorative) | clean; a 0.1 size envelope on Ring; `FlipbookStartRandom` on Flash; Ring renamed RingFX; `Rotation` 0-360 on Flash; `SpreadAngle` 15 on Ring | clean PASS (the decorative Dust envelope ignored); envelope FAIL; random start FAIL; renamed: no property failure, caught only by "read 1 of 2 marked" (listed false reading and its count guard); symmetric rotation FAIL (listed false reading: confirm with the VFX designer); spread FAIL. Wrong with no error when: the count guard is skipped, or a script applies the randomness at emit time |
| QS-12 code-rolled range | an injected random source returning the lowest, then the highest value | a slam footprint function with a data radius and a decorative dust range | radius identical at both ends, dust varies: right answer. Two `Seed` runs of the server roll would give identical server lines whatever the emitter carries: the reason the `Seed` route left QS-12 |

V10 conflict found while fixing F1: the VFX craft book's own spec example (`vfx-craft/references/plan-and-spec.md` §C, layer L04 marked `semantic: true`) carries `Lifetime` [0.3, 0.4] and `Rotation` [0, 360], while its rule SP-06 says "no random range on a semantic layer". My read follows SP-06 and lists the symmetric-rotation case as a false reading; proposal row filed to the VFX designer's book.

V11 after this round: grep of all proposal files for `testing`, `qa-lead`, `player-facing`, `PF-` and `QS-`: `feature-builder.md` rows 29 (adopted, round 1) and 36 (adopted, this round); no other row targets my books.

V5 pass after the repair: every location changed this round (SKILL T-19, §3 step 3, QS-12, QS-16, §7 row 12, header; methods §1 range row, §2, header; player-facing PF-07, PF-10, PF-16, §3 hook rows, header; records §3, header; worked examples §1 hooks, PF-16 and T-19 rows, planted faults, honest end, §3 burst row and honest end, header) was opened after the edit; every coverage row whose finding has a runnable check names its QS line (VR-19 QS-05, VR-21 QS-05/QS-15/QS-16, VR-25 QS-12, VR-26 QS-16); the three worked examples were re-read against the changed T-19, PF-07, PF-10 and PF-16. Files written with LF endings.

## Proposal sweep (J018 close)

Close-out sweep by orchestrator-sweep for qa-lead · claude-opus-5-5 · high · 2026-10-22. Last grep of all 20 proposal files for `testing`, `qa-lead`, `player-facing`, `methods.md`, `records.md`, `worked-examples`, `PF-` and `QS-`: no row beyond the three below targets my books (the architect's and reviewer's rows that name the qa-lead target `job-types.md` and `job-feature.js`).

| proposal file:line | decision (adopted / already in the book / declined) | where or why |
| --- | --- | --- |
| feature-builder.md:29 | already in the book | `testing/references/player-facing.md` PF-02 (rejected request, no success layer, `Reject`), PF-05 (burst ends exact, buying right after a gain, `Set`), PF-06 (windup identical for every tier, `Outcome`/`Seed`), PF-07 (reduced keeps every warning, `Reduced`), PF-10 (burst at the real rate merges labels and cues); adopted in repair round 1 |
| feature-builder.md:32 | declined | no change asked ("none") and the target is the feature-builder's own frontmatter; nothing in the qa-lead books depends on it (`testing` stays in the builder's preloaded pair) |
| feature-builder.md:36 | already in the book | `testing/references/player-facing.md` §3 hooks table: `Outcome` = `<event id>:<outcome or tier>` or `Seed`, `Set` = `<key>:<value>` (rounds 1), `Reduced`; `Clarity` = all / reduced / essential; `Viewer` (round 2); PF-16 uses `Clarity`; grep "not in the builder" over the testing books = 0 |

No book change this sweep.
