> Author: J018 maker architect · claude-opus-5-5 · high · 2026-10-22. Part of `architecture`: built also from the owner's Riot transcripts (J018); repair rounds 1 and 2 after the stage 3 reviews. Engine facts cite the docs mirror (`knowledge/external/roblox-creator-docs/`); PROPOSAL numbers are starting values a check may change.

# The presentation contract

The presentation contract is the part of the decision record (or of `contract-code.md`, `contract-wiring.md`, `contract-player.md`) where gameplay hands over to animation, VFX, sound, UI and camera. It answers, for every event the player sees or hears: what starts it, where it runs, what it carries, who draws what for whom, how loud it may be for each viewer, what the reduced version keeps, how often it fires, and which data it reads. It connects the crafts' documents; it never copies their values.

## 1. What it reads, and who owns each value
Each value lives in one place. The contract names the document by path and revision and refers to values by key or event id, never by a copied number.
| Value | Lives in | Owner |
| --- | --- | --- |
| Feedback stack: named stages, attempt cue, outcome tiers, failure and refusal cues, celebration, frequency and merge window, counters, channels and comfort | feature spec field 9 (`preproduction/references/documents.md` §6) | game-designer |
| Threat and hazard rules: reaction window, tell, danger area, hazard rule | threat and hazard sheets (`documents.md` §7) | game-designer |
| Read rank and information list per moment | `documents.md` §9 | game-designer |
| Event ids, times in seconds, markers, gameplay windows copied read-only, interruption and cleanup | timing list (`templates/anim/timing-list.md`, JSON copy beside it) | animator |
| Effect importance per viewer, loudness tier and caps, reduced and per-viewer variants, budget block | VFX read card and `spec.json` (`content/vfx/<effect-id>/`) | vfx-designer |
| Cue ids → asset ids, buses, voice caps, pooling | the cue table and mix plan (`sound-design/references/roblox-audio.md`) | sound-designer |
| UI states (pending, denied with reason, disabled with reason), motion-table rows, refusal texts | `content/ui/<screen-id>/spec.md`, `content/ui/_system/motion-table.md` | ui-ux-designer |
| Truth values: radius, fuse, cooldown, odds, prices, balances | the gameplay data module (content as data) and the server state | values: game- or progression-designer; file: the builder named in the owns table |
| Names of events, states and cues | `knowledge/design/vocabulary.md` | filed by the lead; new names proposed in the contract |
| The builder's wiring sheet and test hooks | `engineering-craft/references/presentation.md` (feedback stack sheet, test hooks, debug log) | feature-builder; for an action this contract covers, its sheet cites my row ids and copies no source, payload, viewer, truth or cap-owner value |
A value missing from its owner's document is UNKNOWN with that owner, never filled in by me.

## 2. Event rows
One row per player-visible event. Row ids P-1, P-2 ... are local to the contract.
| Field | Holds |
| --- | --- |
| Row id, event id | P-n; the vocabulary name (the timing-list id where motion is involved), the same name in the timing list, the frame script and the cue card |
| Layer | attempt · outcome (tier) · failure · refusal · tell · end-of-state tell · pending · cleanup · predicted (only where the feature spec allows it; on the acting player's own client; removed in the frame the denial arrives; small, never the confirmed outcome's layer; never money, rewards or paid reveals) |
| Source | input on the client · server result (remote, payload) · replicated state · animation marker (clip, marker name) · server timer value |
| Payload | request id, actor, target, outcome, tier, cause, reason code, position, the truth keys the layer needs |
| Runs on, presenter | client (the default for every picture and sound; server only for gameplay); the one client presenter module that owns the row, its caps and its pools |
| Consumers | animation (clip, event), VFX (effect id), sound (cue id), UI (state, motion row), camera (channel) |
| Per viewer | what self, ally, bystander and threatened player each see and hear. The server sends facts, never a picture. Threats and pickups stay full for whoever must act; other players' non-threat effects are toned locally; camera and screen channels only for the local player's own top-tier events; hit-stop only on the attacker's and the target's clients (§5) |
| Comfort | the intense channels used (shake, flash, tint, FOV, fast motion, slow motion) and each reduced variant; the information it keeps |
| Rate | expected rate and burst; merge window; live-copy cap; the one module that owns the cap and the pool (copies reset before reuse; callers never spawn their own) |
| Information | the two or more channels that carry the fact (shape, text, motion, sound, colour), so that grayscale, sound off, reduced motion and the lowest graphics quality each still leave at least one |
| Truth | the data fields and server values the layer reads (area, fuse, timer, balance) |
| Check seed | the test or capture that proves the row and who runs it (§6) |

## 3. Filling it, in order
1. Read the feature spec's feedback stack, threat and hazard sheets and read rank at their revisions; list the rows they imply (AR-06 counts them).
2. Ask before you fill, in the job's exchange notes against the contract revision: the game-designer, animator, vfx-designer, sound-designer and ui-ux-designer each for what the role file's partner table lists ("What you ask your partners for, and when"). Two rounds at most. A craft not in the crew, or a stage with no exchange order: read its documents if they exist, mark the missing values UNKNOWN with that owner (§1) and go on; `needs-decision` only when an unknown blocks the build.
3. Fill each row (§2). The attempt row plays on the client on the input frame: small, local, no server wait. Outcome rows start from the server result, sized by tier, never from a marker; a marker may start a contact-candidate cue (small, presentation only), never the confirmed outcome. A prediction is its own predicted row (§2 Layer) with its source (for example the attacker's hit-stop on `contact_candidate`) and its removal on denial; where the spec does not allow one, the outcome waits a round trip and the animator agrees the hold of the contact pose (seed "Hit-stop", §6). Slow confirmation shows the pending row; a rejected request shows no outcome row. Picture and sound of one row start from one client event, timed by marker names or timing-list ids in seconds, never by guessed delays or frame counts. A paid-random reveal: the windup row's source is the request, identical for every outcome; only the reveal row reads the result tier.
4. Name the presenter module that owns each row, the comfort service it reads (§4), and the test hooks and debug log lines the seeds need, by the names in `engineering-craft/references/presentation.md` §9 (one list, never copied here).
5. Write the check seeds (§6) into the qa-lead's trace table.
6. Bump the contract revision when any row changes and tell every consumer in the same hand-back.

## 4. The comfort and clarity service
One client module, read-only for everyone else:
| Setting | Source | Effect |
| --- | --- | --- |
| Reduced motion | `GuiService.ReducedMotionEnabled` (read-only, not replicated: `_api-reference/classes/GuiService.yaml:262-277`) | tweens snap (time 0) or fade (`production/publishing/accessibility.md:186-188`); camera-driven motion off; poses and tells unchanged |
| Shake | the game's setting (off, low, full); default off when reduced motion is on | shake strength; off removes it; the weight stays in pose, timing and sound |
| Flashes | the game's setting; default reduced when reduced motion is on | a flash or blink becomes a steady shape or glow with a fill countdown |
| Screen effects | the game's setting | full-screen tints, vignettes and FOV punches removed |
| Effect clarity | the game's setting (all, reduced, essential) | tones other players' non-threat effects; never hides a threat, a pickup or the player's own outcome |
Rules: this table is the one owner of which setting removes what (J019): effect and UI code ask the Flashes and Shake rows, never `ReducedMotionEnabled` directly; the defaults above make a player's Roblox reduced-motion setting also calm flashes and shake, and the player can change each. Settings change only the local screen; they never replicate and never change gameplay; every reduced variant keeps footprint, contact, outcome, threats and pickups. Whether `ReducedMotionEnabled` signals a change while the game runs is not in the docs: probe in Studio before relying on a live update; otherwise read it when a screen or effect starts.

## 5. Engine facts the contract leans on (checked in the docs mirror)
| Fact | Docs | Use |
| --- | --- | --- |
| Animation markers fire through `AnimationTrack:GetMarkerReachedSignal`, with an optional string parameter | `animation/events.md:12, 47-72` | presentation keys from named markers, never from guessed delays |
| A character's animations started on its owning client replicate to the server and other clients; an NPC's must be loaded and started on the server to replicate; an `Animator` created on a client does not replicate | `_api-reference/classes/Animator.yaml:217-232` | the contract says where each clip starts; whether marker signals fire on an observing client for another player's or an NPC's track is not stated: probe before relying on it |
| `LocalTransparencyModifier` on ParticleEmitter, Beam and Trail is a local multiplier that does not replicate | `_api-reference/classes/ParticleEmitter.yaml:502-511`; `Beam.yaml:325-335`; `Trail.yaml:278-291` | per-viewer toning of other players' effects |
| Shadows degrade as graphics quality drops and are off below quality level 4 | `performance-optimization/improve.md:418-421` | no gameplay fact rides on a shadow |
| ParticleEmitter Rate caps at 400 per second per emitter, 100 on mobile | `effects/particle-emitters.md:212` | particle-only information can thin out on phones: pair it with a mesh, text or sound |
| Highlight: 255 at once per client; extras are silently ignored | `effects/highlighting.md:37` | an outline for must-find actors is budgeted per client; past the cap it silently fails |
| Packages update every copy, placeholders included | `projects/assets/packages.md:14, 19` | kits and greybox placeholders |
Hit-stop has no global time scale: on the attacker's and the target's clients, the presenter pauses both characters' tracks (`AnimationTrack:AdjustSpeed(0)`, speed 0 pauses: `_api-reference/classes/AnimationTrack.yaml:320-324`) and the hit's own particles (`ParticleEmitter.TimeScale` 0: `ParticleEmitter.yaml:962-968`), and the one hit-stop owner of each track and emitter sets the base speed back when the stop ends and at once on interruption, never a saved previous speed, so two overlapping stops cannot leave a track frozen (`engineering-craft/references/presentation.md` §4); bystanders get it only if the per-viewer column says so; the server never pauses.
Probes before the contract relies on them (the docs do not say): (1) marker signals on an observing client for another player's or an NPC's track (above); (2) a live change signal of `ReducedMotionEnabled` (§4); (3) `AdjustSpeed(0)` on a character track replicated from another client: does it hold on the observing client, and does the owning client's own pause replicate to everyone (then bystanders see hit-stop without asking)?

## 6. Check seeds (what proves the rows, and who captures)
The thresholds live in the crafts' books; the seeds point to them.
| Seed | Proves | Captured by | Pass rule lives in |
| --- | --- | --- | --- |
| Rejected request | no outcome layer, celebration or reward sound for a denied or invalid request; the refusal shows its reason | qa-lead test or studio-operator frame folder (builder hook `Reject`) | `game-design/references/principles.md` §7 checks |
| Slow confirmation | pending state, never early success | qa-lead (builder hook `DelayMs`, or Studio's network simulator) | same |
| Two-client bystander | the bystander's camera never moves, flashes or tints from another player's event; toned effects do not hide the bystander's own threat | studio-operator or qa-lead multi-client run; the builder hook `Viewer` is a one-client screen, not the proof | `vfx-design/references/review.md` §I |
| Grayscale + sound off + reduced motion | every threat, pickup, team, tier and outcome still identified | studio-operator captures | `vfx-design` §4, `ui-design/references/review.md` §6 |
| Real rate and burst | one label and one sound per merge window, caps held, final counter exact | qa-lead (builder hook `Rate`) | `game-design/references/principles.md` §7 |
| Lowest graphics quality | every gameplay fact present at the lowest and highest quality | studio-operator | `environment-design` E-08; this contract's information column |
| Truth overlay | the drawn edge sits on the server area at warning, contact and end | vfx-designer with a debug shape from the same data | `vfx-design` §4 truth |
| Hit-stop | two stops 50 ms apart on one track, and one cut by death, both end at base speed; with a 150 ms server delay the frozen pose is still the contact pose or the agreed hold | builder's offline overlap test; one still with the builder's `DelayMs` hook (qa-lead or studio-operator) | `engineering-craft/references/presentation.md` §4 |
| Marker sync | picture punch and sound transient inside the studio's shared sync window | a device capture; Studio stills leave it not verified | the sync rule in `animation-design/references/game-timing.md` §4 |
When the job has protected acceptance tests (`testing` T-06), the qa-lead turns the rejected-request, slow-confirmation, truth-overlay, reduced and lowest-quality seeds into protected rows with the same hooks and captures, so a craft's self-review and the acceptance run prove the same thing.
Studio MCP captures are stills: feel at normal speed and sound sync are judged on a playable preview or a device capture; without one they stay not verified.
