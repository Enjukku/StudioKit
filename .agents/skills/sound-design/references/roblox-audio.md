> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10. Revised by J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018).

# Roblox audio: objects, limits, uploads, policy, phones

Core rules used here (in SKILL.md): S-140 audio graph, S-150/S-219 client playback and server confirmation,
S-152 voice caps, S-156/S-157 phone-first bands, S-159/S-160 mono and device approval; SC-08 baked vs live, SC-10
movement and Doppler, SC-12 footsteps. Re-check API facts and quotas
at each milestone; the engine changes.

## A. Graph objects and documented ranges (O, Creator Docs mirror read 2026-10-10)

| Class | Job | Key properties (range) |
| --- | --- | --- |
| AudioPlayer | Plays an asset | `Asset` (use this; `AssetId` deprecated, S-222), Volume (0-10), PlaybackSpeed (0-20; pitch and length), Looping, LoopRegion, PlaybackRegion, IsReady, TimeLength |
| Wire | Connects SourceInstance → TargetInstance | pin names, e.g. a compressor's `Sidechain` pin |
| AudioFader | Bus gain | Volume (0-10; default not stated on the page; `AudioFader.yaml:44-47`, corrected 2026-10-21 by J008 fact-check AU12) |
| AudioEmitter / AudioListener | 3D speaker / microphone | Custom DistanceAttenuation (≤400 points), AngleAttenuation (0-180°), AcousticSimulationEnabled, GetAudibilityFor(listener) → 0-1 |
| AudioDeviceOutput | Real output | — |
| AudioCompressor | Dynamics, ducking via `Sidechain` pin | Threshold (−60 to 0 dB), Ratio (1-50), Attack (0.0001-0.5 s), Release (0.01-5 s), MakeupGain (−30 to 30 dB) |
| AudioLimiter | Master ceiling | MaxLevel (−12 to 0 dB), Release (0.001-1 s) |
| AudioFilter | Low-pass, high-pass, band, notch, shelf | Frequency (20-22,000 Hz), Gain (−30 to 30 dB), Q (0.1-10) |
| AudioEqualizer | 3-band EQ | Band gains (−80 to 10 dB), crossovers (200-20,000 Hz) |
| AudioReverb | One per space type | DecayTime (0.1-20 s), DecayRatio, Density, Diffusion (0.1-1), DryLevel, WetLevel (−80 to 20 dB), EarlyDelayTime (0-0.3 s), LateDelayTime (0-0.1 s), HighCutFrequency (20-20,000 Hz) |
| AudioDistortion | Saturation, roughness, phone harmonics | Level (0-1) |
| AudioPitchShifter | Pitch without length change | Pitch (0.5-2) |
| AudioTremolo | Slow AM only | Frequency (0.1-20 Hz): cannot make 30-150 Hz roughness |
| AudioAnalyzer | Metering | RMS and peak, not LUFS (S-209) |

Others exist (AudioEcho, AudioChorus, AudioFlanger, AudioGate, AudioChannelMixer/Splitter, AudioFDNReverb); check
their pages before use. Legacy `Sound`, `SoundGroup`, `SoundEffect` are discouraged, not removed.

## B. Wiring and runtime rules

| ID | Rule | Evidence |
| --- | --- | --- |
| S-141 | One AudioFader per bus (Music, SFX, UI, Ambience). | practice (docs) |
| S-142 | Master chain: AudioCompressor (Threshold −18 dB, Ratio 3, Attack 0.01 s, Release 0.2 s) → AudioLimiter (MaxLevel −1 dB, Release 0.1 s). (P values) | docs ranges + inference |
| S-143 | Ducking: wire the trigger bus into the `Sidechain` pin of an AudioCompressor on the Music bus; Threshold about −30 dB, Ratio 4-8, Attack 0.02 s, Release 0.5 s (P). Legacy `CompressorSoundEffect.SideChain` only for old `Sound` setups. | docs + inference |
| S-144 | Semitones: PlaybackSpeed = 2^(n/12) (+1 = 1.0595, +7 = 1.4983, +12 = 2.0); it changes length. Under about 0.3 s use PlaybackSpeed; if length must not change use AudioPitchShifter. Never stack both without computing the product. | docs + = |
| S-145 | 3D threats: AudioEmitter with custom distance and angle curves; gate hints, captions and voice budget with GetAudibilityFor. `SoundService.RolloffScale` does nothing for the graph. | docs |
| S-146 | Occlusion: try `AcousticSimulationEnabled` and measure its cost; fallback raycast emitter → listener, one AudioFilter low-pass step per wall. | docs + practice |
| S-226 | Acoustic simulation needs the global `SoundService.AcousticSimulationEnabled` gate plus emitter and listener settings. A scripted fallback interpolates filter and gain over 100-250 ms and never doubles the engine's occlusion. Critical warnings stay intelligible with it off. | docs + inference |
| S-147 | One AudioReverb per space type, not per sound. `SoundService.AmbientReverb` does not touch the graph. | docs |
| S-148 | Bake roughness into the asset or use AudioDistortion (AudioTremolo tops out at 20 Hz). | docs |
| S-149 | Pool AudioPlayers; never create and destroy one per hit. | inference |
| S-224 | Reset pooled players fully before reuse: time position, speed, gain, loop, parent, wires, connections, pending callbacks. | inference |
| S-151 | Preload only UI sounds, the player's own action, hit and collect cues, and first-area ambience; check `IsReady` before first play. Never preload everything. | docs |
| S-223 | Preload essentials asynchronously and inspect per-asset results; 5 s watchdog then a visual fallback; drop routine one-shots that miss their window by 150-250 ms instead of playing stale hits. (P) | docs + inference |
| S-228 | One response per authorised event per listener; event IDs block duplicate prediction and confirmation. Clients never send asset IDs or gain values to the server. | inference |
| S-217 | Agents allowlist event names, asset IDs, API fields, routes and numeric bounds (rest of S-217 is a SKILL.md guardrail). | inference |
| — | Baked vs live (SC-08): per-sound processing is baked into the file; live effects only for context: one AudioReverb per space type, an AudioFilter or AudioEqualizer for underwater or occlusion, an AudioCompressor for ducks. The order of live effects in a chain changes the result (`audio/effects.md:27`). Roblox has no live transient shaper: bake transients. | docs + inference |
| — | Doppler: `SoundService.DopplerScale` applies to legacy `Sound` only; the docs say it does not affect AudioPlayer or AudioEmitter (`_api-reference/classes/SoundService.yaml:178-195`), and the graph classes have no Doppler property. Assume no engine Doppler on graph emitters: a travel sound that needs a pitch pass-by gets it from a scripted PlaybackSpeed change (S-144) or a one-shot whoosh, or has none (SC-10); a Studio probe only confirms. | docs |
| — | Footsteps: `Humanoid.FloorMaterial` is the `Enum.Material` under the character, `Air` when airborne (`_api-reference/classes/Humanoid.yaml:365-372`); the footstep table maps it to a set (SC-12). | docs |
| — | Stage sounds keyed to animation markers fire through `AnimationTrack:GetMarkerReachedSignal` (`animation/events.md:12, 47-72`); the cue card names the timing list's event id, the integrator wires it from the same client event as the VFX. | docs |
| — | Cue ids map to asset ids and parts in one data table (content as data); no asset id in logic (`review.md` R-44). | inference |

## C. Uploads, rights and moderation

| ID | Rule | Evidence |
| --- | --- | --- |
| S-153 | One track; .ogg or .wav (also .mp3, .flac); ≤48 kHz; mono for SFX; <20 MB and <7 min. Budget 2,000 imports per 30 days (ID-verified; 100 unverified). Example: 60 cues × 6 variants = 360 imports. | docs |
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
| — | Phone speakers lose most output somewhere below 150-500 Hz (no single measured number). Missing-fundamental: harmonics imply the bass (S-157; AudioDistortion Level 0.1-0.3 or a saturated duplicate layer). | lead |

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
| Graph matches the card | `execute_luau` (Edit or Client data model): list AudioPlayer, AudioFader, AudioEmitter, AudioListener, AudioReverb and Wire instances with their key properties and wire ends; no edits | R-40 | lists only instances alive at the call: players a pool creates on first play are missing (the pooling row counts them) |
| Pooling (creation counter) | in a play-test, on the Client data model: count only new instances. Before the warm-up, put every AudioPlayer and Sound in the data model into a weak-keyed set (`setmetatable({}, {__mode = "k"})`) and connect to `game.DescendantAdded` to add every one it sees; warm-up = one 10 s burst at the real top rate (a pool that grows on demand reaches the burst's overlap here); then count during a second 10 s burst at the same rate each AudioPlayer or Sound the event brings that is not in the set (add it after counting), and print its full name: pooled = 0. No character spawns or respawns during the counted burst (the engine creates default character Sounds at spawn): if one does, run the burst again. The event fires on every re-parent, so a raw event count fails a pool that parks idle players at nil (S-224 resets `parent`). A count before and after the burst reads flat for create-and-destroy code too, so never use it. First use is a probe: confirm the connection outlives the `execute_luau` call, else run the burst inside the same call through the integrator's test hook | R-40 | false PASS: a player never parented into the data model (run the R-40 grep too); a template `:Clone()` escapes the grep (the counter sees it). False FAIL: a character spawn in the counted burst; a pool still growing because the second burst overlaps more than the first; a Sound another system creates during the burst: read each counted full name before a fix note |
| Distance curves | read each emitter's `DistanceAttenuationMode`: if `Custom`, its `GetDistanceAttenuation()` keys (an empty table = the default curve); otherwise `DistanceAttenuationBounds` and the mode (the custom curve is ignored, yet `GetDistanceAttenuation()` still returns it: `AudioEmitter.yaml:135-185, 349-365`); also the AudioListener's `GetDistanceAttenuation()`, which multiplies with the emitter's; compare with the card's studs | R-16 | `GetDistanceAttenuation()` returns a custom curve even when the mode ignores it: read the mode first; the heard level is emitter × listener curve |
| Floor materials in the place | list the `Material` of walkable, collidable parts and the terrain materials used; compare with the footstep table | R-14 | none found yet: first use is a probe |
| Cue counts and order | in a play-test, `get_console_output` after the integrator's debug log `cue` lines (format and hooks: `engineering-craft/references/presentation.md` §9; the first four tokens `cue <cue-id> <event-id> <t>`, then `f<frame> r<request-id>`): pair each cue with its request by `r`; one cue per event, one per merge window at the burst rate, no outcome cue after a rejected request (`Reject` hook) | R-41, R-42 | script time, not output time; times compare only within one machine (client lines with client lines); a cue played on a path that does not log is missing from the log, not from the game: read the trigger code before a fix note |

MCP captures are stills without sound: these checks prove wiring and trigger counts (script time), never what the
player hears or the output latency. Not yet run in a game job: treat the first use as a probe and record the result.
