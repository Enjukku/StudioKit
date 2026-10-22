> Author: J018 maker feature-builder · claude-opus-5-5 · high · 2026-10-22. Part of `engineering-craft`; built also from the owner's Riot transcripts (J018). Facts checked in the docs mirror (paths relative to `knowledge/external/roblox-creator-docs/`; Y = `_api-reference/classes/`). Numbers marked PROPOSAL are starting values a check may change; design values (timings, tiers, caps, rates) come from the partners' tables, never from this file.

# Wiring what players see and hear

The rule side lives in `architecture` (R-04 clocks, R-05 simulation vs presentation, R-13 three outcomes) and `networking-security` (N-02, N-03, N-14). This file is how the builder turns the partners' specs into code that tells the truth fast: the sheet I fill, the order I wire in, the hooks and log I ship, and the Studio checks behind §6 of the skill.

## 1. The feedback stack sheet (filled in the contract, EC-01, SR-02)
The game designer's feature spec holds the design values (`preproduction` `references/documents.md` §6: stages, attempt cue, outcome tiers, refusals, frequency, counters, channels and comfort). My sheet restates each row as code: which handler, which request and result id, which table row, which data field. One row per player action or game event the player must notice; values come from the partners' files with the revision named; an empty cell is a question to the owner of that table, with a PROPOSAL meanwhile. When the architect's presentation contract covers the action (`architecture` `references/presentation-contract.md` §2), the sheet cites its row ids (P-n) and takes the request → result, viewers, truth fields and cap owner from it; it fills only what the contract leaves to the builder.

| Column | Holds | Source |
| --- | --- | --- |
| Action / event id | the id from the timing list or vocabulary | animator, `vocabulary.md` |
| Attempt cue | what answers the input on the client (press state, tick, swing clip, small flash), the frame (input frame or the next) | UI spec, cue card, effect spec |
| Request → result | remote, request id, the result event and its three outcomes (done, denied with reason, unavailable) | architect's plan |
| Outcome response | per outcome tier: layers, clip, cue, hit-stop tier, label; starts on the result event | VFX, sound, animator, UI |
| Refusal | per denial reason: message id (cause and fix), icon, cue, which control answers | UI spec, sound |
| Pending | after how many ms (PROPOSAL 100), what shows | UI spec |
| Rate | expected rate, burst rate, merge window, live-copy cap, cull rule | specs; PROPOSAL until set |
| Viewers | the variant for self, ally, enemy, bystander | VFX read card |
| Reduced | the reduced variant of each intense channel and what information it keeps | every spec |
| Truth fields | gameplay values a visual must match (radius, fuse, active end) and their data field | gameplay data |

## 2. Attempt and outcome (EC-17)
- The input handler plays the attempt cue first, in the same frame, then sends the request. Nothing in the attempt path waits on the network, a yield or an asset load (preload attempt cues).
- The outcome layer starts in the client handler of the server's result for that request id. Size comes from the result's tier field, never from the attempt.
- The server answers every request with one of three outcomes (`architecture` R-13); a denial carries a reason code the client maps to its refusal (§7).
- Pending: a timer started at send shows the pending state at the sheet's threshold; the result cancels it. A result that arrives after the screen closed or the character respawned is dropped (generation token, `architecture` R-11).
- Prediction (showing something before the server answers) only where the spec allows it, as its own predicted row in the presentation contract (`architecture` `references/presentation-contract.md` §2 Layer: on the acting player's own client, small, never the confirmed outcome's layer), with a clean rollback (a predicted hit marker that the server denies is removed in the same frame the denial arrives); money, rewards and paid reveals are never predicted.
- Escalation (x2, x3, CRIT) counts confirmed results only and resets on the idle rule in data.
- A threat's tell: the server fires the tell event at wind-up start with the server time it resolves (`Workspace:GetServerTimeNow`, Y/Workspace.yaml:1524); the client starts the tell at once and schedules its end against that time. Sending the tell together with the damage hands the player a warning they cannot use.

## 3. One event list and the tables (EC-18)
| Table | Owner | Code reads |
| --- | --- | --- |
| Timing list (`content/anim/<asset>/timing-<action>.json`) | animator | event ids, marker names, seconds; never retimes gameplay windows |
| Cue table (cue id → asset id → parts, bus, voice cap) | sound designer | the pooled player sets `Asset` from it (`sound-design` `roblox-audio.md` §B) |
| Motion table (`content/ui/_system/motion-table.md` → data) | UI designer | duration, easing, overshoot, reduced variant per row (`ui-basics` U-13) |
| Effect `spec.json` (`content/vfx/<effect-id>/`) | VFX designer | layers, stage starts in seconds, budget, per-viewer and reduced fields, semantic or decorative marks |
| Style tokens and colour roles | UI designer, art director | colours by role, never a free `Color3` |
| Message table (reason code → text template, icon) | UI designer | refusals and disabled reasons |
| Gameplay data (radius, fuse, windows, tiers) | game designer | the server and the visuals read the same rows |
- Stage timelines (tell, build, hit, result) are rows in seconds scheduled from one start event; phones vary their frame rate, so never frames.
- Random ranges apply only to fields the spec marks decorative; contact time, area, fuse, team colour and tier stay fixed.
- Expose the values a designer brackets as attributes in the Studio test place (read live, written back to data after the owner's pick), so a bracket is a property change, not a code change.
- Movement values (gravity, walk speed, jump height) come from the game profile once; code-driven motion (knock-back, jump pads, lifts) derives from them so everything moves by one physics.
- Footsteps: `Humanoid.FloorMaterial` (`Air` when airborne, Y/Humanoid.yaml:365-372) picks the set from the sound designer's footstep table; a floor material missing from the table is reported, never given a default sound.
- Offline id test (SR-07): load every table and assert each id the feature names exists, and each row the sheet lists is used.

## 4. Markers, sync, hit-stop and truth (EC-19)
- Connect `track:GetMarkerReachedSignal(name)` before `track:Play()` (`animation/events.md:12, 47-72`; `animation-craft` `roblox-playback.md` §4). One marker handler starts the VFX emit and the cue in the same call; no `task.delay` between them unless the timeline gives one. Sync rule (shared with sound, VFX, animator): the sound onset lands on the first lit contact frame or up to about 40 ms after it, never more than one frame early; code can only make the trigger common, the file's onset is the sound designer's.
- `contact_candidate` (pose) is not `contact_confirmed` (gameplay): confirmed-hit layers wait for the result (§2).
- Hit-stop (on a confirmed hit; on the attacker's and the target's clients only, bystanders only where the contract's per-viewer column says so; the server never pauses): `AnimationTrack:AdjustSpeed(0)` on the attacker's and target's tracks (Y/AnimationTrack.yaml:320-324) and `ParticleEmitter.TimeScale = 0` on the hit's own emitters (Y/ParticleEmitter.yaml:962-968) for the tier's length from data. A hit-stop always ends: one hit-stop owner per track and per emitter holds the base speed and a stop-until time. The base is the speed the game last set for that track (every other speed change on it, such as an attack-speed stat or a slow, goes through the owner, which updates the base; during a stop the new base takes effect when the stop ends) and, for an emitter, the `TimeScale` its spec sets (1 if none). A new stop only extends the stop-until time and never saves the current speed (two overlapping stops would save 0 and leave the track frozen); when the time passes, the owner sets the base back, and it also does so at once on death, unequip, destroy and a new clip on that track. Physics, other players and the server keep running. Length 0 where the data says none (explosions, projectile throwers, rapid fire, crowds). Offline test (SR-17): stop A at 0 ms for 100 ms and stop B at 50 ms for 100 ms leave the track at its base speed at 150 ms; a stop cut by death ends at base; a speed change to 0.8 during a stop leaves the track at 0.8 after it.
- Whether a pause set on another player's replicated character track holds on the observing client, and whether the owning client's own pause replicates to everyone (then bystanders would see the stop without asking), is not in the docs (Y/Animator.yaml:217-232 covers only clips started on the owning client): run the probe in `probes.md` §4 before relying on either.
- Under latency the confirmed stop starts one round trip after the contact pose, so the frozen pose is not the animator's freeze frame (in Play Solo the gap is near 0 and hides this). Test with `DelayMs` = 150. Default: the hold of the contact pose or a shorter confirmed stop, agreed with the animator. A predicted stop (the attacker's own client starts it on `contact_candidate` and ends it at once on a denial; on a miss the attacker sees a short freeze) is the game designer's choice, recorded as a predicted row in the contract (§2), never as the outcome row. Write the pick in the sheet.
- Effects: every layer under one root; size and height from one scale factor in data; `ParticleEmitter:Emit` for bursts; stage starts from the spec's seconds.
- Drawn danger areas, rings and countdowns read the same data row the server uses; the danger visual ends on the server's end event; the debug shape (§9) is built from that row too.
- A state with a timer gets its building end tell from the timing list event (for example `shield_break_warn`), fired from the server's timer.

## 5. Per viewer and camera channels (EC-20)
- The server fires one event with the actor id and ids; each client resolves its relation (self, ally, enemy, bystander) from the game's team data and draws that variant from the spec.
- Other players' non-threat effects: `LocalTransparencyModifier` on their emitters, beams and trails (local only, not replicated: Y/ParticleEmitter.yaml:502-511), value from the spec for the player's clarity level (the comfort module's `clarity()`, §6; PROPOSAL all 0.5, reduced 0.75, essential 0.9 until the spec sets them). Threats and pickups to the viewer who must act, and the player's own outcome, stay full at every clarity level.
- Must-find actors may get a `Highlight` (255 per client cap, `effects/highlighting.md:37`): count them.
- Camera shake, FOV punches, slow motion and screen tints run only for the local player's own events at the tiers the spec allows, scaled or removed by the comfort module (`shakeScale()`, `screenEffects()`, §6); shake rotates, never translates, applied each frame after the camera update (`RunService:BindToRenderStep` above `Enum.RenderPriority.Camera`; exact offset: probe, `probes.md` §4); a local tint is a `ColorCorrectionEffect` under `Workspace.CurrentCamera` (Y/ColorCorrectionEffect.yaml:22-27).
- Team colour follows the viewer's relation and always has a shape or outline twin.

## 6. Reduced paths and more than one channel (EC-21)
- One comfort module answers the five settings of the architect's comfort and clarity service (`architecture` `references/presentation-contract.md` §4): `reducedMotion()`, `shakeScale()` (0 = off), `reduceFlashes()`, `screenEffects()` (off removes full-screen tints, vignettes, FOV punches, push-ins and speed lines) and `clarity()` (all, reduced, essential: tones only other players' non-threat effects, §5). It reads `GuiService.ReducedMotionEnabled` (Y/GuiService.yaml:262; `production/publishing/accessibility.md:184-208`), the game's own settings, and the Studio overrides `Reduced` and `Clarity` (§9). Every intense channel calls it; nothing reads the raw setting elsewhere. Whether the setting signals a change while the game runs is not in the docs: read it when a screen or effect starts until the probe in `probes.md` §4 says otherwise.
- Reduced variants from the spec: tweens snap (time 0) or fade; shake 0; flashes become a steady shape or glow with a fill countdown; with screen effects off, FOV punches, push-ins, speed lines, vignettes and full-screen tints are removed and what a tint told (low health, a buff) stays as a HUD edge or icon with its number. The information (where, when, what happened, every threat and pickup) survives every setting.
- Translucent UI backgrounds multiply their transparency by `GuiService.PreferredTransparency` (`accessibility.md:104-129`; `ui-basics` U-10).
- Status by colour always also by icon, text or shape; every gameplay sound has a visual twin; comfort settings change only the local screen.
- Pulses and blinks run at the rate class the spec gives (never above 3 per second at full contrast) and follow the server's timer.

## 7. Frequent events, counters and refusals (EC-22)
- Merge: same-kind events inside the window (PROPOSAL 100 ms) add into one label and one cue; the label shows the sum.
- Cap and pool: live copies per effect and voices per cue capped from the spec (PROPOSAL 8 copies of a frequent effect); the oldest or lowest-ranked copy is culled first (rank: a threat to the viewer, own action, pickups, other players, ambient); pooled instances are reset fully before reuse (properties, parent, connections, pending callbacks).
- Counters: the client keeps the true value from the server; logic and affordability read it at once; the shown value tweens toward it inside the motion table's cap and is set exactly when the tween ends or a new value arrives; no sound per digit.
- Refusals: the reason code maps to a message template ("Need {n} more {currency}") and icon from the message table. On a screen, how the control answers (message at the control, shake, sound rate) is `ui-basics` U-15; a disabled control shows its reason before the press, computed by the same check function the server mirrors. World refusals (a blocked hit, a full backpack) get a why cue and a distinct, rate-limited sound (PROPOSAL once per 0.5 s).

## 8. Paid random reveals (EC-23; `platform-policy` § A and P-01, P-02 bind and win)
- The server asks the game's policy module first, never `PolicyService` directly (`platform-policy` P-02: flags read at join in `pcall` with retry; while the call fails, paid random is treated as restricted), then rolls, commits through the data layer, and sends the result; the client never rolls.
- The reveal reads one windup row for every tier; the code that picks the windup has no access to the result (pass it only the item kind). Tier layers, rarity colour and escalation are scheduled from the result event onward; a tap after the result skips to it; a batch gives only the best result the full ceremony.
- The odds panel shows the effective odds the server sends each player (`platform-policy` P-01), built on the server from the same probability table and modifier function the roll uses, so a luck boost or a once-only outcome changes the shown odds at once; the client never computes its own copy. They sum to 100 % or carry the rounding note `platform-policy` § A gives.
- Offline tests (SR-15): over many seeded rolls the windup id is identical for every tier; no tier layer is scheduled before the result event; the odds the server sends equal the roll's table with the modifiers applied; with the policy call failing, and for a restricted player, the request never reaches the generator.

## 9. Test hooks and the debug log (EC-24)
Partners ask for these at the wiring step (`vfx-craft` `references/measure.md` §1, the animator's and sound designer's role files, the qa-lead's `testing` `references/player-facing.md` §3).
- **Test build only.** The hook scripts and the two `TestHooks` folders live in their own source folder (for example `test/hooks/`) that only a test project file maps (for example `test.project.json`: the default tree plus that folder). The default project file, from which the published place is built, never maps it (`code-review` `references/testing.md`: publish only the production build). No game module names the hooks: the hook script connects to the real events, or sets a test seam the module exposes (nil in the production build). The qa-lead gets both builds with the candidate; the check is the production-build row of §10.
- **Second guard.** The hook script stops at once unless `RunService:IsStudio()`.
- **Driven by attributes** on one folder, because an MCP command's `require` reaches a separate copy of a module (`studio-mcp` C-04): the MCP sets an attribute, the game's hook script reacts.
- **One run, one setting.** At start the hook script prints every hook attribute that is set (`hooks Reject=<v> DelayMs=<v> ...`); after each run, clear every hook attribute. An attribute set in Studio is saved with the place, so a leftover `DelayMs`, `Reject` or `Reduced` changes the next run with no error.

| Attribute on `ServerStorage.TestHooks` (server) or `ReplicatedStorage.TestHooks` (client) | Does |
| --- | --- |
| `Trigger` = event id | fires that event once through the real path |
| `Rate` = `"<event id>:<per second>:<seconds>"` | fires it at that rate (100 at 1 per second; a burst of about 20 per second) and logs the live-copy count and the playing-track count each second (`live` lines) |
| `Reject` = reason code or empty | the server denies the next requests with that reason |
| `DelayMs` = number | the server waits before answering (pending path) |
| `Reduced` = true / false / empty | overrides the comfort module's reduced settings at once (motion, shake 0, flashes, screen effects off) |
| `Clarity` = all / reduced / essential / empty | overrides the comfort module's clarity setting |
| `Viewer` = self / ally / enemy / bystander / empty | overrides the local relation for per-viewer checks |
| `DebugShape` = true | draws a see-through part of the server's area from the same data row |
| `Outcome` = `"<event id>:<outcome or tier>"`, or `Seed` = number | forces the next result (or the roll's seed) on the server, so each tier and denial can be shown on demand |
| `Set` = `"<key>:<value>"` | sets one test state on the server (balance, cooldown, timer, inventory full, a policy flag through the game's own policy module, never `PolicyService` itself) |
| `FxLog` = true | turns the debug log on |
Debug log lines (`print`, client unless marked; fields separated by spaces; `t` = `os.clock()` in ms on that machine; `f` = a frame counter incremented on `RenderStepped`; `r` = request id). The first four tokens of `cue` lines match the sound designer's convention.
```text
evt <event-id> <source: input|result|marker|server> <t> f<f> r<r>
cue <cue-id> <event-id> <t> f<f> r<r>
vfx <effect-id> <event-id> <t> f<f> r<r>
ui <motion-row> <event-id> <t> f<f> r<r>
cam <channel> <event-id> <t> f<f>
live <effect-or-cue-id | track:<clip-id>> <count> <t>
```
`track:<clip-id>` counts that clip's tracks in `Animator:GetPlayingAnimationTracks()` (Y/Animator.yaml:128-140) on the local player's and the test actors' Animators. Lines compare only within one machine's clock. Turn `FxLog` off for performance captures: printing during a run adds frame cost (`studio-mcp` C-05).

## 10. Judging in Studio (EC-25, SR-08 to SR-17)
Every recipe below is a screening aid; its known false readings are in §11. First use in a game is a probe: record what it showed in the hand-back.

| Check | How (`studio-mcp`; every call names its `studio_id`) | SR |
| --- | --- | --- |
| Attempt and outcome | play-test; set `FxLog`; press through `user_mouse_input` or `Trigger`; `get_console_output`; compare the `evt input` and attempt lines' `f`, then the `evt result` and outcome lines' order by `r`; repeat with `Reject` and with `DelayMs` = 500; for a hit-stop, also `DelayMs` = 150 and one still of the frozen pose | SR-08 |
| Markers | listeners connected before `Play` (code read); the VFX and cue lines of one `evt marker` share its `f`; no gameplay code reads a marker | SR-09 |
| Repetition | `Rate` 100 at 1 per second, then a burst of about 20 per second; count `cue` and `ui` lines per merge window; read the `live` lines (copies and `track:` counts) against the caps; no `cam` line during either run; the creation counter of `sound-design` `roblox-audio.md` §G for new instances in the second burst | SR-10 |
| Per viewer | `Viewer` = bystander, `Trigger` another player's event; read the emitters' `LocalTransparencyModifier` (`execute_luau` on Client) at `Clarity` = all, then essential: non-threat values follow the spec's level, threats and pickups stay 0; no `cam` line | SR-12 |
| Scale | after the `Model:ScaleTo` probe (`probes.md` §4), set the effect's scale factor ×2 once in data; one still at the game camera: every layer stays aligned with its root | SR-16 |
| Footsteps | one `execute_luau` read of the distinct `Material` values of the parts in the play area, against the footstep table's rows; terrain materials come from the environment designer's material list (manual) | SR-07 |
| Truth | `DebugShape` on; stills at warning, contact and end at the game camera (`screen_capture`, at most 3); the last `vfx` danger line is not after the server's end line | SR-13 |
| Reduced | `Reduced` = true; the reduced branch lines appear for motion, shake, flashes and screen effects (no `cam` shake, FOV or tint line); one still of the busiest moment | SR-14 |
| Budget | at the worst case, count live particles (`ParticleEmitter` count × rate × lifetime is the estimate; the spec's budget block), emitters, playing voices and Highlights with one `execute_luau` read on Client | SR-16 |
| Slow network (optional) | Studio's Network Simulator (beta per its docs page, `studio/network-simulator.md`; enabled by the owner) or `settings().Network.InboundNetworkMinDelayMs` set from `execute_luau` (PluginSecurity, Y/NetworkSettings.yaml:173-197: probe once) | SR-08 |
| Partners' captures | name them in the hand-back: per UI state at the smallest phone and a PC size, the busiest moment, a rejected request, reduced on, a frame folder of each press for the UI designer's S-33, one capture per reveal tier for S-44 | SR-19 |
| Literals | the literals grep below, from the source root (asset ids: `sound-design` review R-44); every hit must be the one motion helper, a data or token module, or a test; a clean result still needs the code read of the screen's tween, text and timer paths | SR-06, U-S05 |
| Collision agrees with the look | for parts the feature places: list `CanCollide` parts with `Transparency` 1 and visible non-colliding parts in the play area, and compare with the spec | SR-16 |
| Production build | from the repo root: `rojo build default.project.json -o prod.rbxlx`, then `grep -c TestHook prod.rbxlx`: 0; the same two commands on `test.project.json`: above 0 (the positive control); build to `.rbxlx` (XML text), never `.rbxl` for this check; use the project file names and hook names of the game and the manifest | SR-18 |

Literals grep (Git Bash, from the source root; tested on a sample tree with single-quoted, back-quoted, interpolated and concatenated strings, Title Case strings passed to helpers, `task.` and legacy waits and delays, `BrickColor`, §11):
```text
grep -rnE "TweenInfo\.new|EasingStyle\.|Color3\.|BrickColor\.|\.Text\s*=\s*[\"'\`]|[\"'\`][A-Z][a-z]+( [A-Za-z0-9{]+)+|[\"'\`][A-Z][a-z]+ [\"'\`]\s*\.\.|(^|[^.A-Za-z_])(task\.)?(wait|delay)\(\s*[0-9.]" src
```

## 11. Known false readings of these recipes
- The debug log is script time: two lines on one frame can still reach the screen or speaker frames apart; output latency and sound sync need a device capture with audio (owner).
- A branch that does not log is missing from the log, not from the game: before a fix note, read the code path.
- `f` counts rendered frames on the client only; a server line has no `f`. Compare server and client lines by `r` and order, never by `t`.
- `get_console_output` can drop or merge lines in a long burst; for repetition counts read `LogService:GetLogHistory()` filtered by prefix in one `execute_luau` call (`studio-mcp` probes P-03), and never during a performance run.
- A creation count before and after a burst reads flat for create-and-destroy code: use the counter in `roblox-audio.md` §G, not a before and after count.
- The live-particle estimate (rate × lifetime + bursts) is not a measured count; a budget near its cap is checked on stills of the peak.
- A Studio still is one moment: it proves a layout or a pose, never timing; `screen_capture` during Play may be overridden by the camera scripts (set the camera to Scriptable first, `probes.md` §3).
- Play Solo runs server and client in one process: delays and frame times there are not a phone's.
- The literals grep (tested on a sample tree): it catches single, double and back quotes, interpolated strings (`Need {n} more coins`), Title Case strings passed to a helper (`notify("Not Enough Coins")`), a capitalised string before `..`, literal `task.wait(0.28)`, `task.delay(0.35, ...)` and the legacy `wait(0.3)` and `delay(0.35, ...)`, `BrickColor.Red()` and `BrickColor.new(...)`, and an alias `local TI = TweenInfo.new`; it does not hit `GetService("...")`, `Instance.new("...")`, `task.wait()`, a wait on a config value or `Event:Wait()`. It misses `local T = TweenInfo` followed by `T.new(...)`, a one-word string passed other than through `.Text =` ("Buy" sent to a helper), a lower-case player string, also after a variable (`n .. " coins left"`, even on a `.Text =` line), a duration held in a local number and then waited on, and colours built from `Color3` values stored elsewhere; it hits data modules, test files, debug prints and comments (read the line). A clean grep is not proof: the code read of the screen's tween, text and timer paths decides.
- `GetPlayingAnimationTracks` includes tracks that are fading out (Y/Animator.yaml:134-140): a `track:` count right after a burst reads high for the fade time; read the count again after the longest fade before calling a leak.
- The `Reduced`, `Clarity` and `Viewer` overrides prove the branch, not the path from the player's real setting: read the comfort module's setting reads once in the code.
- Hook attributes are saved with the place: a run started after another run's `DelayMs`, `Reject`, `Reduced` or `Outcome` was left set reads wrong with no error. Read the hook script's start line before trusting any reading.
- The production-build grep proves only the place built from files. A place published from a Studio session synced from the test project, or a hooks folder made by hand in Studio, carries the hooks anyway: before a publish from Studio, one `execute_luau` read that `ServerStorage`, `ReplicatedStorage`, `ServerScriptService` and `StarterPlayer` hold no `TestHook*` child. A `.rbxl` (binary) build can hide names in compressed chunks: use `.rbxlx`. A hook script or folder named otherwise is missed: grep the names in the manifest.

## 12. Worked examples
**Shop purchase (UI, money).** Sheet: attempt = button sinks (motion row `button_press`) and `sfx.ui.press` in the press frame; request `Shop.Purchase` with request id; outcomes: done → badge, item flight and coin count-down on `Shop.PurchaseResult` (tier by item rarity); denied `not_enough_coins` → "Need {n} more coins" at the button, shake row `refusal_shake`, `sfx.ui.denied` at most once per 0.5 s; unavailable → "Shop is busy, try again" with retry; pending "Buying…" after 100 ms (PROPOSAL). Checks: SR-08 with `Reject` = `not_enough_coins` (no badge, no chime lines) and `DelayMs` = 500 (pending line near 100 ms, press line unmoved); SR-11 buy right after a gain while the count-up runs.

**Sword hit (combat, per viewer).** The swing clip starts on input; `contact_candidate` plays the whoosh tail and a small spark (attempt); the server's `Combat.HitResolved` (with request id and hit tier) starts the impact layers, the hit cue and, on the attacker's and the target's clients, a hit-stop of the tier's length through the track's hit-stop owner (two quick hits extend one stop, never stack saved speeds; a slow debuff during the stop applies after it); a bystander sees the impact at the toned value for their clarity level and no shake; the target sees it full. Checks: SR-08 with `Reject` (a miss shows the swing and spark only) and with `DelayMs` = 150 (the frozen pose is the contact pose or the hold agreed with the animator), SR-09 (impact VFX and cue share `f`), SR-12 with `Viewer` = bystander, SR-17 offline (overlapping and interrupted stops end at base speed; a speed change during a stop survives it).

**Egg hatch (paid random).** The server asks the game's policy module (closed while its call fails), rolls, commits, then sends `Egg.Result`; the client plays the one `egg_windup` row, then the tier ladder from the result event; the odds panel shows the `EggOdds` the server sends, with the active luck modifier already applied. Checks: SR-15 offline (windup identical over 1,000 seeded rolls per tier), and the UI designer's S-44 frame comparison on one capture per tier.
