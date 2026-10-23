> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10. Revised by J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Revised by J020 step 8 sound-designer · claude-opus-5-5 · high · 2026-10-23: Roblox only plays and places (J020-D1, D8, D10, D11, D12); playback rules in §H from the docs mirror (read 2026-10-23).

# Roblox audio: objects, limits, uploads, policy, phones

Core rules used here (in SKILL.md): S-140 audio graph, S-150/S-219 client playback and server confirmation,
S-152 voice caps, S-156/S-157 phone-first bands, S-159/S-160 mono and phone screening; SC-07 2D or 3D, SC-08 everything
baked but the room, SC-10 movement and Doppler, SC-12 footsteps. **Roblox only plays and places** (J020-D1, D8): volume, 2D or
3D with its falloff, the room (one zone reverb per space type, J020-D10) and ducks by fader volume (J020-D11); every
other alteration is baked into the file (`craft-process.md` §6). How a sound is played: §H. Re-check API facts and quotas
at each milestone; the engine changes.

## A. Graph objects and documented ranges (O, Creator Docs mirror read 2026-10-10)

| Class | Job | Key properties (range) |
| --- | --- | --- |
| AudioPlayer | Plays an asset | `Asset` (use this; `AssetId` deprecated, S-222), Volume (0-10), PlaybackSpeed (0-20; pitch and length), Looping, LoopRegion, PlaybackRegion, IsReady, TimeLength |
| Wire | Connects SourceInstance → TargetInstance | pin names |
| AudioFader | Bus gain | Volume (0-10; default not stated on the page; `AudioFader.yaml:44-47`, corrected 2026-10-21 by J008 fact-check AU12) |
| AudioEmitter / AudioListener | 3D speaker / microphone | DistanceAttenuationMode (Custom default, InverseTapered, Linear, LinearSquared, Inverse), DistanceAttenuationBounds (default 4-10,000 studs), Custom DistanceAttenuation (≤400 points), AngleAttenuation (0-180°), AcousticSimulationEnabled, AudioInteractionGroup, GetAudibilityFor(listener) → 0-1 (§H) |
| AudioDeviceOutput | Real output | — |
| AudioCompressor | **Not used** (J020-D1, LD4: ducks are fader volume) | Threshold (−60 to 0 dB), Ratio (1-50), Attack (0.0001-0.5 s), Release (0.01-5 s), MakeupGain (−30 to 30 dB) |
| AudioLimiter | Master ceiling: **not by default** (S-142; open question) | MaxLevel (−12 to 0 dB), Release (0.001-1 s) |
| AudioFilter | **Not used** (J020-D1, CD-1) | Frequency (20-22,000 Hz), Gain (−30 to 30 dB), Q (0.1-10) |
| AudioEqualizer | **Not used** (J020-D1, CD-1) | Band gains (−80 to 10 dB), crossovers (200-20,000 Hz) |
| AudioReverb | **The one effect used:** one per space type on the SFX bus, switched by a zone script (J020-D10, LD6; §H) | DecayTime (0.1-20 s), DecayRatio, Density, Diffusion (0.1-1), DryLevel, WetLevel (−80 to 20 dB), EarlyDelayTime (0-0.3 s), LateDelayTime (0-0.1 s), HighCutFrequency (20-20,000 Hz) |
| AudioDistortion | **Not used**: saturation is baked (`saturate`) | Level (0-1) |
| AudioPitchShifter | **Not used**: pitch is baked (`varispeed`, `pitch`) | Pitch (0.5-2) |
| AudioTremolo | **Not used** | Frequency (0.1-20 Hz): cannot make 30-150 Hz roughness |
| AudioAnalyzer | Metering | RMS and peak, not LUFS (S-209) |

Others exist (AudioEcho, AudioChorus, AudioFlanger, AudioGate, AudioChannelMixer/Splitter, AudioFDNReverb): **not used**
(J020-D1, CD-1; it may return only if the owner asks). The ranges above are kept as docs facts for reading old places. Legacy `Sound`, `SoundGroup`, `SoundEffect` are discouraged, not removed.

## B. Wiring and runtime rules

| ID | Rule | Evidence |
| --- | --- | --- |
| S-141 | One AudioFader per bus (Music, SFX, UI, Ambience). | practice (docs) |
| S-142 | **Changed by J020-D1:** no master AudioCompressor. A master AudioLimiter as a pure safety ceiling (it stops clipping when many sounds sum; it shapes no single sound) is an open question for the owner; until answered, none, and headroom comes from the bus levels and the voice caps (S-79, S-152). | J020-D1 |
| S-143 | **Replaced (J020-D11, LD4):** ducking is a volume change on the AudioFader buses from a script (a tween down over the attack, held, back over the release), decided per moment with the four questions of §H; no compressor sidechain. Depth, attack and release start values: `mix-and-loudness.md` S-109 to S-111 (P). | J020 decisions |
| S-144 | Semitones: PlaybackSpeed = 2^(n/12) (+1 = 1.0595, +7 = 1.4983, +12 = 2.0); it changes length. A fixed pitch change is baked into the file (`varispeed`, or `pitch` with the length kept, `craft-process.md` §6), never AudioPitchShifter (J020-D1). Runtime PlaybackSpeed (pitch jitter S-90, ladders S-60, a charge's speed tween) is an open question under J020-D1: until the owner answers, prefer baked variant files. | docs + = |
| S-145 | 3D threats: AudioEmitter with the falloff of §H (a preset mode and bounds, or a Custom curve) and an angle curve when the source points one way; gate hints, captions and voice budget with GetAudibilityFor. `SoundService.RolloffScale` does nothing for the graph. | docs |
| S-146 | Occlusion: `AcousticSimulationEnabled` (engine muffling, bending, echo; 3D sounds only) is a Studio probe in the first real game, measuring its cost and quality, not a default (J020-LD5, LD6). The scripted AudioFilter fallback is retired (J020-D1). | docs + J020 |
| S-226 | Acoustic simulation needs the global `SoundService.AcousticSimulationEnabled` gate plus emitter and listener settings. No scripted filter fallback (J020-D1). Critical warnings stay intelligible with it off. | docs + inference |
| S-147 | One AudioReverb per space type, not per sound, on the SFX bus, its settings switched by a zone script when the player enters a space; music and UI bypass it; one uploaded file serves every space (J020-D10, LD6; §H). `SoundService.AmbientReverb` does not touch the graph. | docs + J020 |
| S-148 | Bake roughness into the asset (J020-D1; AudioTremolo tops out at 20 Hz anyway). | docs + J020 |
| S-149 | Pool AudioPlayers; never create and destroy one per hit. | inference |
| S-224 | Reset pooled players fully before reuse: time position, speed, gain, loop, parent, wires, connections, pending callbacks. | inference |
| S-151 | Preload only UI sounds, the player's own action, hit and collect cues, and first-area ambience; check `IsReady` before first play. Never preload everything. | docs |
| S-223 | Preload essentials asynchronously and inspect per-asset results; 5 s watchdog then a visual fallback; drop routine one-shots that miss their window by 150-250 ms instead of playing stale hits. (P) | docs + inference |
| S-228 | One response per authorised event per listener; event IDs block duplicate prediction and confirmation. Clients never send asset IDs or gain values to the server. | inference |
| S-217 | Agents allowlist event names, asset IDs, API fields, routes and numeric bounds (rest of S-217 is a SKILL.md guardrail). | inference |
| — | Baked, the room live (SC-08, J020-D1, D10): every per-sound alteration (EQ, pitch, compression, saturation, transients, layering, the sound's own tail) is baked into the file with `soundbench`; in Roblox only volume, 2D or 3D and falloff, the zone reverb and fader ducks. Underwater or muffled states get a baked variant file, not a live filter. The docs allow many audio players through one effect (`audio/effects.md:23`), which is why one reverb per space type is enough. | docs + J020 |
| — | Doppler: `SoundService.DopplerScale` applies to legacy `Sound` only; the docs say it does not affect AudioPlayer or AudioEmitter (`_api-reference/classes/SoundService.yaml:178-195`), and the graph classes have no Doppler property. Assume no engine Doppler on graph emitters: a travel sound that needs a pitch pass-by gets it baked into a one-shot whoosh (first choice, J020-D1), from a scripted PlaybackSpeed change (S-144; open question), or has none (SC-10); a Studio probe only confirms. | docs |
| — | Footsteps: `Humanoid.FloorMaterial` is the `Enum.Material` under the character, `Air` when airborne (`_api-reference/classes/Humanoid.yaml:365-372`); the footstep table maps it to a set (SC-12). | docs |
| — | Stage sounds keyed to animation markers fire through `AnimationTrack:GetMarkerReachedSignal` (`animation/events.md:12, 47-72`); the cue card names the timing list's event id, the integrator wires it from the same client event as the VFX. | docs |
| — | Cue ids map to asset ids and parts in one data table (content as data); no asset id in logic (`review.md` R-44). | inference |

## C. Uploads, rights and moderation

| ID | Rule | Evidence |
| --- | --- | --- |
| S-153 | One track; `.mp3`, `.ogg`, `.wav` or `.flac`; ≤48 kHz; <20 MB and <7 min (`audio/assets.md:39-40`). **Upload FLAC** (G-8): "Studio transcodes imported audio before saving it as an asset" (`audio/assets.md:58`), so a lossy upload adds a codec; Ogg only for a file over 20 MB. Mono for SFX that play 3D (a stereo file on an AudioEmitter: Studio probe). Budget 2,000 imports per 30 days (ID-verified; 100 unverified). Example: 60 cues × 6 variants = 360 imports. | docs |
| S-154 | Upload all game audio under the account or group that owns the experience; re-verify the same-owner rule before launch. | docs (2022) |
| S-155 | Original or licensed audio only; no profane lyrics. Creator Store partner audio (APM, Monstercat, Pro Sound Effects, Nettwerk, Position Music) is allowed. | docs |
| S-227 | Three release gates per asset: usage rights, moderation, permission in the destination experience. A valid ID or upload proves none of them. | docs |
| S-173 | Before uploading AI audio, check moderation, ownership and licence (with S-216). | inference |

## D. Paid random items (Roblox policy)

| ID | Rule | Evidence |
| --- | --- | --- |
| S-165 | Gate every Robux-paid random item (or one bought with Robux-bought currency) behind `PolicyService:GetPolicyInfoForPlayerAsync().ArePaidRandomItemsRestricted`; restricted players get one of the allowed treatments. | docs |
| S-166 | Odds disclosure, rounding, modifiers and restricted players: `platform-policy` `references/rules.md` §A is the rule and wins (odds as numbers before purchase; only a long list may move behind a visible worded "Info" or "Details" label; a bare (i) is not enough; odds update under luck boosts and once-only outcomes). The sound side is D-03 and S-164. | docs (via platform-policy) |
| S-167 | Every paid random outcome gives real benefit; no empty outcomes. | docs |
| S-169 | No simulated or real gambling for Robux or valuable items. | docs |
| S-172 | Regions and ages: never hard-code them; Roblox sets eligibility through `ArePaidRandomItemsRestricted` per player (`platform-policy`). | docs (via platform-policy) |

Sound rules for reveals: S-164, S-168 in `reward-and-juice.md`.

## E. Phone speakers and devices

| ID | Rule | Evidence |
| --- | --- | --- |
| S-158 | High-pass UI and fast-repeat SFX near 100-150 Hz so phone speakers do not waste headroom. (P) | inference |
| S-229 | Device matrix per essential cue: modest phone speaker, laptop speaker, ordinary headphones, quiet device volume, mono, each channel alone. A 180-250 Hz high-pass preview exposes bass dependence (diagnostic, not a phone model). | inference |
| S-230 | Hero impacts carry two identities: a low body for capable systems plus a shorter crack, texture and midrange impact that survive phones. If a layer vanishes in mono, fix phase, do not add gain. | inference |
| S-231 | If the game can detect a switch from speakers to headphones, reduce output ≥3 dB. | standard (H.872) |
| — | Phone speakers lose most output somewhere below 150-500 Hz (no single measured number). Missing-fundamental: harmonics imply the bass (S-157; baked `saturate` or a saturated duplicate layer; never AudioDistortion, J020-D1). | lead |

## F. Gaps

| ID | Gap | In-house test |
| --- | --- | --- |
| G-06 | Engine voice limit (none published) | Spawn N looping AudioPlayers on the lowest target phone; count audible voices and frame time; set caps below the knee |
| G-07 | Phone-speaker response | Sine sweep on 3 target phones with a reference mic; record −3 and −10 dB points |
| G-14 | Sub-bass on phones | Same hero cue with and without sub; rate "heavy" on phone and headphones |
| G-18 | Engine latency and AV sync on phones | High-speed video of tap-to-sound and break-to-sound |
| G-19 | 2026 audio privacy and moderation turnaround | Test uploads under the group; read the current Creator Dashboard audio page |
| G-20 | Paid-random-item age rules outside Brazil | Read the help centre and DevForum announcements before shipping |

## G. Studio checks (read-only; skill `studio-mcp`, every call names its `studio_id`)

When your tools line has no Studio MCP, ask the studio operator or the lead to run these and return the output.

Each check is a screening aid: its last column lists the false readings found so far. A failing or borderline reading
is checked by eye on the listed instances, the code line or the log lines before any fix note goes out.

| Check | How | Self-review line | Known false readings |
| --- | --- | --- | --- |
| Graph matches the card | `execute_luau` (Edit or Client data model): list AudioPlayer, AudioFader, AudioEmitter, AudioListener, AudioReverb and Wire instances with their key properties and wire ends, every other audio effect instance (there should be none), and `SoundService.DefaultListenerLocation`; no edits | R-40, R-45 | lists only instances alive at the call: players a pool creates on first play are missing (the pooling row counts them) |
| Pooling (creation counter) | in a play-test, on the Client data model: count only new instances. Before the warm-up, put every AudioPlayer and Sound in the data model into a weak-keyed set (`setmetatable({}, {__mode = "k"})`) and connect to `game.DescendantAdded` to add every one it sees; warm-up = one 10 s burst at the real top rate (a pool that grows on demand reaches the burst's overlap here); then count during a second 10 s burst at the same rate each AudioPlayer or Sound the event brings that is not in the set (add it after counting), and print its full name: pooled = 0. No character spawns or respawns during the counted burst (the engine creates default character Sounds at spawn): if one does, run the burst again. The event fires on every re-parent, so a raw event count fails a pool that parks idle players at nil (S-224 resets `parent`). A count before and after the burst reads flat for create-and-destroy code too, so never use it. First use is a probe: confirm the connection outlives the `execute_luau` call, else run the burst inside the same call through the integrator's test hook | R-40 | false PASS: a player never parented into the data model (run the R-40 grep too); a template `:Clone()` escapes the grep (the counter sees it). False FAIL: a character spawn in the counted burst; a pool still growing because the second burst overlaps more than the first; a Sound another system creates during the burst: read each counted full name before a fix note |
| Distance curves | read each emitter's `DistanceAttenuationMode`: if `Custom`, its `GetDistanceAttenuation()` keys (an empty table = the default curve); otherwise `DistanceAttenuationBounds` and the mode (the custom curve is ignored, yet `GetDistanceAttenuation()` still returns it: `AudioEmitter.yaml:135-185, 349-365`); also the AudioListener's `GetDistanceAttenuation()`, which multiplies with the emitter's; compare with the card's mode and studs | R-16, R-45 | `GetDistanceAttenuation()` returns a custom curve even when the mode ignores it: read the mode first; the heard level is emitter × listener curve |
| Floor materials in the place | list the `Material` of walkable, collidable parts and the terrain materials used; compare with the footstep table | R-14 | none found yet: first use is a probe |
| Cue counts and order | in a play-test, `get_console_output` after the integrator's debug log `cue` lines (format and hooks: `engineering-craft/references/presentation.md` §9; the first four tokens `cue <cue-id> <event-id> <t>`, then `f<frame> r<request-id>`): pair each cue with its request by `r`; one cue per event, one per merge window at the burst rate, no outcome cue after a rejected request (`Reject` hook) | R-41, R-42 | script time, not output time; times compare only within one machine (client lines with client lines); a cue played on a path that does not log is missing from the log, not from the game: read the trigger code before a fix note |

MCP captures are stills without sound: these checks prove wiring and trigger counts (script time), never what the
player hears or the output latency. Not yet run in a game job: treat the first use as a probe and record the result.

## H. Playback: 2D or 3D, falloff, the room, ducking (J020-D8, D10, D11, D12; docs mirror read 2026-10-23)

Roblox only plays and places sounds (J020-D1, D8). Every cue card names 2D or 3D with the reason, for 3D the falloff
mode and bounds, whether it takes the room, and whether it ducks (`cue-card.md` fields 51-55). Sources:
`audio/objects.md:41-126`; `_api-reference/classes/AudioEmitter.yaml:135-185`; `_api-reference/enums/DistanceAttenuationMode.yaml:24-72`;
`_api-reference/enums/ListenerLocation.yaml`; `_api-reference/classes/SoundService.yaml:117-129` (DefaultListenerLocation);
`audio/effects.md:23`. The rule is the studio's, built on the docs and on `knowledge/jobs/J020-sound-workbench/research-2d-3d.md`.

**What the docs say.** 2D audio "plays from no particular location, remaining at the same volume regardless of the
player's position or orientation" (`audio/objects.md:43`): AudioPlayer → Wire → (AudioFader bus) → AudioDeviceOutput.
3D audio "plays from a particular location in the 3D space, increasing or decreasing in volume depending on the
player's position and orientation to the sound" (`audio/objects.md:75`): AudioPlayer → Wire → AudioEmitter on the part;
AudioListener → Wire → AudioDeviceOutput. Roblox has no blend between 2D and 3D and no Doppler on the graph.

### H1. The rule: 2D or 3D

**One question for every sound: does where it comes from, or how far away it is, tell the player something?** Yes → 3D.
No → 2D. Most sounds are 2D (J020-D8); 3D is right in many cases (J020-D12).

**Sounds made by a player: the actor rule.** One event often needs two versions. The player who acts hears it 2D
(steady, close, always clear; 3D on one's own character pans badly). Every other player hears it 3D from the actor's
position, so they can tell who did it, where and how far.

| Source | The actor (me) | Other players | Range (start values, PROPOSAL) |
| --- | --- | --- | --- |
| Footsteps, jump, land | 2D, quiet | 3D | combat or hide-and-seek: far (60-100 studs); social and simulator games: near (20-40) |
| Attacks, abilities, tools, emotes | 2D | 3D | by importance: a dangerous ability far (80-150), a cosmetic emote near (20-30) |
| Hit on a target | 2D hit confirm for the attacker | 3D at the target | the target's own player hears the hit 2D as feedback |
| Rewards, level ups, purchases | 2D | 3D, quieter, capped, or none | near (20-40); never spam others with a crowd's rewards |
| Voice lines from a character | 2D | 3D | near to middle (30-60) |

**Other sources**

| Source | Kind | Why | Range (start values, PROPOSAL) |
| --- | --- | --- | --- |
| UI, menus, screens, shop | 2D | about me, no place | — |
| Music, game narration | 2D | not a thing in the world; spreading score in space makes players mistake it for world sound | — |
| Global game events: round start, timer, flood warning, server announcements | 2D | every player must hear them wherever they are | — |
| An event for one area only (a boss roar in its arena) | 2D for the players inside (triggered by the area), or 3D with a range the size of the area | everyone in the area must hear it; outside, no one | the area's size |
| Enemies and NPCs: steps, idles, barks | 3D | where they are | near to middle (20-60) |
| Threat tells and enemy attacks | 3D | the player must face or avoid them; never sound-only (a visual tell too) | far (80-200) |
| Projectiles, vehicles, mounts, anything moving | 3D, the emitter rides the moving part | direction and approach | by speed and danger |
| World objects: doors, chests, machines, shops, portals | 3D at the object | belongs to the place | near (10-40) |
| Pickups and secrets to find | 3D, short | leads the player to them | near (10-30) |
| Point ambience: waterfall, fire, fountain, river | 3D at the source | fades as you walk away | the object's size to 60-150 |
| Long sources: a river, a coast, a crowd | 3D, several emitters along it, or one moved to the nearest point by a script (Studio probe first) | a single emitter sounds like one spot | as above |
| Area mood (forest, cave, city) | 2D bed for the area, crossfaded when the player changes area, plus 3D for its visible sources | the mood is everywhere in the area | — |
| Music playing inside the world (a radio, a stage) | 3D | it is a thing in the world | middle (40-80) |
| Explosions and big world events | 3D with a long range; a 2D distant layer only if every player must know it happened | where it happened, and how far | far (150-400) |

Voice chat is Roblox's own system, not our files. When no row fits: ask the question; if the answer is no, 2D.

### H2. Setting a 3D sound

| Setting | What it does (docs) | Studio rule |
| --- | --- | --- |
| `DistanceAttenuationBounds` (min, max) | full volume inside min; "fully attenuated at or beyond the maximum distance"; default 4 to 10,000 studs; used only when the mode is a preset (`AudioEmitter.yaml:135-152`) | min = the size of the thing (you are "at" it); max = where it must be gone. Both on the card in studs; never leave the 10,000 default |
| `DistanceAttenuationMode` | **Defaults to `Custom`** (`AudioEmitter.yaml:167-183`). `Linear`: (max − d) ÷ (max − min). `LinearSquared`: that squared, a steeper fade. `Inverse`: min ÷ d, "mirroring how sounds attenuate in the real world" (never quite silent before max). `InverseTapered`: the lesser of Inverse and LinearSquared, so it follows Inverse near min and still ends silent at max. `Custom`: your own curve from `SetDistanceAttenuation()` (≤400 points); the docs' example halves the volume at 50 studs and is silent at 70 (`audio/objects.md:116-118`). A preset ignores the custom curve | ambience and world sources: `InverseTapered`; gameplay cues that must stay clear to a set range, then stop: `Linear`; `Custom` only for a shape the presets cannot give (the far version's two curves, SC-07). Set the mode explicitly: the default is Custom |
| Angle (`SetAngleAttenuation()`) | quieter behind the emitter's look direction | only for sounds that point one way (a speaker, a cannon mouth); default none |
| `SoundService.DefaultListenerLocation` | where the "ear" is: `Character` ("the world being heard from the position of your character while matching the orientation of your camera": a listener on an Attachment on the character's PrimaryPart, turned each frame to face the camera), `Camera`, `Default` (on the camera, in voice-chat experiences) or `None` (made by a script) | `Character` in every game: distance from the character, direction from the camera. In cutscenes the listener moves to the camera by script (Studio probe in the first cutscene) |
| `AcousticSimulationEnabled` | muffling through walls, bending round corners, echo, by the engine; 3D sounds only; emitter and listener both on | not by default; a Studio probe in the first real game (cost and quality) as a second route for fitting the space (J020-LD5, LD6) |
| `AudioInteractionGroup` | an emitter is heard only by listeners in the same group | default; only for split audio worlds (or a separate listener per bus, if the bus probe below needs it) |

**Open probes (first real game):** how a stereo file plays on an AudioEmitter (until then, mono exports for 3D cues);
how 3D sounds reach the category buses and the zone reverb (the listener's output wired into the SFX bus, or one
listener per bus by interaction group); the cutscene listener move.

### H3. Fitting the space: the room (J020-D10, LD6)

One uploaded file serves every space; no per-space copies. The game has one `AudioReverb` per space type (outside,
small room, hall, cave, ... from the identity sheet's Space types row), wired on the SFX bus (many audio players can
go through one effect, `audio/effects.md:23`). A zone script switches the reverb's settings when the player enters a
space. Music and UI skip it. The files stay dry of room sound (their designed tail stays); each card says whether
the cue takes the room (footsteps, voices, impacts: yes; UI, music: no). Reverb settings are PROPOSAL until the
owner's play-test. Acoustic simulation: H2.

### H4. Ducking (J020-D11, LD4)

Ducking lowers other sounds for a moment so an important one is heard. It is decided per moment, never a blanket
rule. Each cue card answers four questions:
1. **Would the player miss something that matters without it?** Only must-hear sounds duck others: a threat tell, a warning, a key voice line, the biggest reward moment. Small, frequent sounds never duck anything.
2. **What goes down:** usually music and ambience; other effects only when they hide the cue.
3. **How much and how fast:** depth, attack and release (start values `mix-and-loudness.md` S-109 to S-111, PROPOSAL).
4. **Why:** one line.

It is a volume change on the AudioFader buses from a script (a tween down, hold while the cue plays, tween back),
never an AudioCompressor sidechain (J020-D1). One duck request per event (S-109/S-211); overlapping ducks take the
deepest, never the sum (P).
