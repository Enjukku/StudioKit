> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10. Revised by J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Revised by J020 step 8 sound-designer · claude-opus-5-5 · high · 2026-10-23: playback fields 51-56, the `card.json` part (§D), the play-test log. Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021-D4, on 982592c): field 43 carries the target-experience sentence. Revised by J020 step 8 follow-up sound-designer · claude-opus-5-5 · high · 2026-10-24: §D: rank built, per-layer targets, loop seam rule, family folders.

# Cue card

One card per sound event. Every field gets a value or "n/a". Tag every number (M)/(X)/(O)/(=)/(P). Short card for minor
cues: fields 1-6, 12-19, 22, 26, 30, 43, 45, 47, 51, 53, 55. The machine part of every card is `card.json` in the cue
folder (§D), read by `soundbench`.

## A. Fields

| # | Field | Fill with | Units | Rules |
| --- | --- | --- | --- | --- |
| 1 | Cue ID and name | Stable ID used in code and content | `SFX-<AREA>-<NAME>` | — |
| 2 | Trigger | Event, code path, client or server | text | S-150, S-203 |
| 3 | Target emotion | 1-2 recipe rows | emotion names | S-01 |
| 4 | Arousal and valence | Level, direction | low/mid/high, rising/falling; +/0/− | S-01, S-02 |
| 5 | Priority and loudness slot | Tier and relative level | tier 1-7; dB re loudest | S-107, S-108 |
| 6 | Total length | Start to −40 dB | ms | S-194, S-53, S-130 |
| 7 | Layer: transient | Content, length, band, level | ms, Hz, dB | S-23, S-76 |
| 8 | Layer: body | Content, length, band, level, pitch drop | ms, Hz, dB, st | S-24, S-76 |
| 9 | Layer: sub (optional) | Content, length, band; headphones-only? | ms, Hz, Y/N | S-15, S-117 |
| 10 | Layer: tail | Content, length, band, level, dry or reverb send | ms, Hz, dB | S-76, S-84 |
| 11 | Key, scale, root, ladder | Root note; step, cap, reset | note; st; steps; ms | S-60..S-62, S-114 |
| 12 | Variants | Count; shuffle-bag exclude-last N | count; N | S-88, S-89 |
| 13 | Pitch randomisation | Range | ± cents | S-90 |
| 14 | Volume randomisation | Range | ± dB | S-91 |
| 15 | Size or intensity scaling | Driving parameter and law | e.g. +3 dB per doubling | S-78, S-79, S-81 |
| 16 | Cooldown | Min gap between plays of this ID | ms | S-94 |
| 17 | Voice cap and steal policy | Copies; drop newest or steal quietest/oldest | count; policy | S-152 |
| 18 | Ducking | Who ducks it (the cue's own duck: field 54) | dB, ms | S-109..S-111, S-211 |
| 19 | Spatial | Angle curve; rear; occlusion (2D or 3D: field 51; falloff: field 52) | studs, dB, ° | S-11, S-118, S-225, S-145, S-146 |
| 20 | Roblox objects | Instances, wiring, bus; no effect but the zone reverb (J020-D1) | class names | S-140..S-149 |
| 21 | Load and playback side | Preload Y/N; client or server | — | S-150, S-151 |
| 22 | Sync | Trigger event id; file onset (F-01); inside the S-133 window of the first lit contact frame; haptic and offset | event; ms | S-74, S-131, S-133 |
| 23 | Mobile check | Phone-speaker pass; partials >300 Hz; mono drop | pass/fail; dB | S-156..S-160, S-229 |
| 24 | Headphone check | Sub not boomy; no sustained 2-5 kHz; no AM 30-150 Hz on positive cues | pass/fail | S-08, S-22 |
| 25 | Repetition check | Machine-gun test; misophonia check | pass/fail | S-96, S-101 |
| 26 | Policy check | Net value > 0 if celebratory; every paid outcome gives real benefit (S-167); win sound beside the plain value (S-163); outcome meaning tested; paid-random rules; original or licensed | pass/fail | S-161..S-173, S-232..S-234 |
| 27 | Evidence | Rule IDs used; list every (P) value | IDs | — |
| 28 | AI prompt and settings | Prompt per texture or layer; duration, influence, model; takes per round (field 56) | text; s; 0-1 | S-123..S-127 |
| 29 | Check plan | Self-review lines with their inputs; the `render` targets; the debug cue log lines that prove it on its event | text | `review.md` §2-§3 |
| 30 | Status | PROPOSAL / rendered (`render` exit 0) / proven on its event (debug cue log) / owner play-tested | enum | — |
| 31 | Primary player outcome | Detect, identify, confirm or feel | text | S-183 |
| 32 | Perceived vs induced emotion | Two fields | names | S-183 |
| 33 | Truth conditions | Server confirm? Prediction allowed? Dedup key; cancel or rollback | Y/N; key; text | S-219, S-228 |
| 34 | Event rate | Per minute; max burst per second; aggregation window | /min; /s; ms | S-66, S-194, S-200 |
| 35 | Rhythm and modulation | BPM and onsets/s separately; spectral Hz and modulation Hz separately | BPM; /s; Hz; Hz | S-174, S-175 |
| 36 | Numeric provenance | Tag summary | tags | S-176 |
| 37 | Accessibility | Caption; visual indicator; sound-off equivalent; reduced intensity; haptic meaning | text | S-191, S-221 |
| 38 | Delivery | FLAC (G-8), rate, channels; peak dBFS, true peak dBTP; loudness and its measure; the render log and tool versions | units | S-104, S-153, S-209, S-210 |
| 39 | Rights manifest | Creator or provider; licence evidence; date; input provenance; destinations; moderation; experience permission | text | S-216, S-227 |
| 40 | Verification statuses | Evidence reviewed, file analysed (F-xx), auditioned (the owner's play-test, never your own), game-tested; phone, headphones, mono, sound-off, 1,000-event fixture | passed/failed/not-run | S-204, S-217 |
| 41 | Load and expiry | Load watchdog; late-event expiry | ms | S-223 |
| 42 | Change gate | Fields an agent may tune (with bounds); fields needing designer review; fallback; rollback | lists | S-217 |
| 43 | Job and story point | Cue, feedback or emotion; the story point in one line; the target-experience line quoted (kind of fun + the sentence of what the player must feel); that sentence picks the `emotion-recipes.md` row and the prompt's emotional intent; field 44 stays the mechanic word | text | SC-01 |
| 44 | Verb and texture | The mechanic verb (as on the clip card and frame script); how the texture moves like it | text | SC-03 |
| 45 | Stages | Stage → event id @ timing revision → attempt or outcome → layers (`craft-process.md` §2) | table | SC-04 |
| 46 | Identity | Signature element; character feel words; nearest similar to differ from; tone words; identity-sheet check | text | SC-11 |
| 47 | Carry and viewers | Hearing distance in studs; far version; tier per viewer (own, ally, threatened, bystander) | studs; tier | SC-07 |
| 48 | Sources and options | Texture prompts, takes per round, odd variant, the rank table against the targets (no reference sound, CD-2), why the pick won, rounds used, stand-ins with their better source | text | SC-14 |
| 49 | Build | Library parts used (tier); `recipe.json` steps with purpose; everything baked, only the room live; unprocessed tried | list | SC-08, SC-09, SC-15 |
| 50 | Play-test log | The owner's flags from their play-tests, word for word, date, build revision; the fix and the `lesson` each became (the check-ins A, B, C are retired, J020-LD3) | text | `review.md` §2 |
| 51 | 2D or 3D | 2D or 3D, and the reason (does where it comes from, or how far, tell the player something?); for a player's action, the actor version (2D) and the others version (3D) | enum; text | SC-07; `roblox-audio.md` §H1 |
| 52 | Falloff (3D) | `DistanceAttenuationMode` (InverseTapered, Linear, LinearSquared, Inverse, or Custom with its points); bounds min and max; angle if directional; the listener (`Character`, or the camera in a cutscene) | mode; studs; ° | `roblox-audio.md` §H2 |
| 53 | Takes the room | Yes (through the zone reverb on the SFX bus) or no (bypasses it); the file stays dry of room | Y/N | J020-D10; `roblox-audio.md` §H3 |
| 54 | Ducks | None, or the four answers: would the player miss something without it; what goes down (buses); how much and how fast (depth, attack, release); why | text; dB; ms | J020-D11; `roblox-audio.md` §H4; S-109..S-111 |
| 55 | Targets | The numbers `render` checks (§D): timing (onset and which onset it binds to, main transient, attack rise, sound length), spectrum (band shares, phone loss, key), level with its measure named, true peak, form; each `must` or `aim`, tagged (P) | units | `review.md` §4; S-76, S-133, S-156 |
| 56 | Takes and rounds | Tier (minor 3, frequent 4, important 6 takes per round; important layers one prompt each); rounds used (at most 3, then to the owner with the numbers) | count | J020-D7, J020-D9 |

## B. Filled example: wooden crate break (generic action game)

| # | Value |
| --- | --- |
| 1 | `SFX-WORLD-CRATE-BREAK`, "wooden crate break" |
| 2 | Client, on a replicated break event; one play per break cluster per frame, never per physics contact (S-79, S-203) |
| 3 | Power + satisfaction |
| 4 | Arousal mid (small) to high (large), rising with cluster size; valence + |
| 5 | Own action tier 2, −3 dB (P); other players tier 5, −9 dB (P) |
| 6 | Small 250-400 ms; large up to 600 ms (P) |
| 7 | "Crack": dry wood snap, 5-15 ms, 2-6 kHz, 0 dB, attack <5 ms (P) |
| 8 | "Thud": 80-200 ms (small) to 300 ms (large), 60-200 Hz with partials 120-480 Hz for phones, −2 dB; large tier 4-5 st lower (P) |
| 9 | Large tier only: 30-60 Hz falling over 200-400 ms, −6 dB, headphones-only feel (P) |
| 10 | "Splinter rattle": 150-400 ms (large: spread 200-1,200 ms), 1-8 kHz, −8 dB, random micro-timing; dry, space from the zone's AudioReverb (P) |
| 11 | Unpitched; no ring in 2-5 kHz; no ladder |
| 12 | 6 per size tier × 3 tiers = 18 imports (P); shuffle-bag excluding last 2 |
| 13 | ±50 to ±100 cents (P) |
| 14 | ±1.5 dB (P) |
| 15 | Severity 0-1 from pieces or mass (S-199); tiers 1 / 2-7 / 8+ pieces (P); +3 dB per doubling inside a tier, capped at the next tier (S-202); layers small = crack + thud, medium + rattle, large all 4 (S-78) |
| 16 | 80-150 ms per tier ID (P) |
| 17 | 4-6 per tier ID; debris ≤8 voices per 100 ms; steal quietest, then oldest (P) |
| 18 | Ducked 6-9 dB by critical warnings (P) |
| 19 | No angle curve; occlusion: none (acoustic simulation not in use, S-146) |
| 20 | Own: pooled AudioPlayers (`Asset`) → Wire → SFX AudioFader → zone AudioReverb → AudioDeviceOutput. Others: pooled AudioPlayers → Wire → AudioEmitter on an Attachment at the cluster centroid; AudioListener (`Character`) → Wire → SFX AudioFader → zone AudioReverb → AudioDeviceOutput (the bus route of 3D sounds: Studio probe, `roblox-audio.md` §H2) |
| 21 | Preload Y for the player's own break; client playback |
| 22 | Trigger: `break_confirmed` event; file onset ≤ 5 ms (F-01); inside the S-133 window of the first lit break frame; same frame as hitstop start; light haptic on own large breaks (P) |
| 23 | Crack and rattle carry identity on the phone; body audible through 120-480 Hz partials; mono drop ≤3 dB; 180-250 Hz high-pass preview stays recognisable |
| 24 | Sub not boomy; no sustained 2-5 kHz scrape; no 30-150 Hz AM |
| 25 | 10 s machine-gun test of a chain reaction; 1,000-selection fixture; no wet sounds |
| 26 | Original or licensed with manifest; not an outcome cue (net-value rule n/a); uploaded under the experience owner |
| 27 | S-75, S-76, S-78, S-79, S-80, S-81, S-84, S-88, S-90, S-152, S-157, S-199, S-200, S-202, S-203; (P) in 5-10, 12-19, 22 |
| 28 | See `ai-generation-prompts.md` §C crate rows; one prompt per size tier; v2 model, 0.7 s / 2 s, influence 0.5-0.6 (P) |
| 29 | `render` on every variant (field 55 targets); R-20 to R-25, R-31 (variants within ±1 dB), R-33 (tiers step down in pitch); R-41 debug cue log in a 10 s chain reaction (one cue per cluster, caps held); R-45 own 2D, others 3D. Repeats and the small < medium < large order by ear: the owner's play-test |
| 30 | PROPOSAL |
| 31 | Hear which material broke and roughly how much, in sync with the picture |
| 32 | Perceived: power, satisfaction. Induced: satisfaction (asked apart from liking) |
| 33 | Server confirms; owner's client may predict the crack only (P); dedup key = break-event ID; on rejection body and debris never play |
| 34 | Up to about 10 clusters/s in chains (P); secondary contacts coalesced in 50-100 ms |
| 35 | BPM n/a; crack 2-6 kHz, body 60-200 Hz; modulation none |
| 36 | All (P) except class names (O) and 2^(n/12), 10^(dB/20) (=) |
| 37 | Caption "[crates collapse]" only for large off-screen breaks; reduced intensity: sub off, debris −6 dB (P) |
| 38 | Mono FLAC at the take's rate (44.1 kHz); true peak ≤ −1 dBTP; level F-13 a within the break family; render log and tool versions recorded |
| 39 | Provider, model, date, plan evidence, prompt; moderation and experience permission checked |
| 40 | All not-run |
| 41 | Watchdog 5 s; late-event expiry 150-250 ms (P) |
| 42 | Agent may tune jitter inside S-90/S-91 bounds and cooldown inside 80-150 ms; peak level, voice caps, duration need designer review; fallback: silence + visual debris |
| 43 | Feedback and emotion: "the crate you hit really broke"; target line: "smashing everything feels powerful" |
| 44 | n/a (no ability verb); material wood: dry, splintering, short |
| 45 | crack on `break_confirmed` (outcome); thud same event; rattle +30-80 ms after it; no attempt cue (the swing has its own) |
| 46 | No signature (world prop); wood family of the sound-code table; tone words "chunky, toy-like" |
| 47 | Own breaks tier 2; other players' breaks tier 5, silent by 60 studs (P) |
| 48 | Prompts "dry pine planks snapping", "wooden pallet splintering", "cardboard box crushed" (odd); frequent tier: 4 takes per round per size tier, kept as the variant set (2 more from seeded `variants` to reach 6); ranked against field 55; round 1 of 3; stand-in: none |
| 49 | Parts: crack (raw → `highpass` 150 Hz), thud (`varispeed` −4 st, `highpass` 50 Hz), rattle (spliced takes); all baked; edit pass trim (main transient) → fade out 20 ms → mono → loudness F-13 a → peak → FLAC; the room from the zone reverb |
| 50 | none yet |
| 51 | Actor rule: the player who breaks it hears it 2D; other players hear it 3D at the cluster centroid (where it broke and how far matters to them) |
| 52 | Others: `Inverse`, bounds 13 to 60 studs (full near, −6 dB per doubling after, S-118) (P); no angle; listener `Character` |
| 53 | Yes: wood breaking in a cave should sound like the cave |
| 54 | None: frequent and small, the player would miss nothing (question 1 fails) |
| 55 | onset ≤ 3 ms on the main transient (must); true peak ≤ −1 dBTP (must); sound length 250-600 ms by tier (aim); 500 Hz-5 kHz share ≥ 0.10 (must); phone loss ≤ 12 dB (aim); below 120 Hz ≤ 0.25 on small and medium (aim); level F-13 a −14 LUFS ±1 within the family (must); mono drop ≤ 3 dB (must) (all P) |
| 56 | Frequent: 4 takes per round per size tier; rounds used: not run |

## C. JSON blank

```json
{
  "id": "", "name": "", "trigger": "", "target_emotion": [], "arousal": "", "valence": "",
  "priority_tier": null, "level_db_rel": "", "length_ms": "",
  "layers": {"transient": "", "body": "", "sub": "", "tail": ""},
  "key": {"pitched": false, "root": "", "scale": "", "ladder": {"step_st": null, "cap": null, "reset_ms": null}},
  "variants": {"count": null, "exclude_last": null}, "pitch_jitter_cents": "", "volume_jitter_db": "",
  "scaling": "", "cooldown_ms": null, "voice_cap": {"max": null, "steal": ""},
  "ducking": {"ducked_by": ""}, "spatial": {"angle_curve": "", "occlusion": ""},
  "roblox_objects": "", "preload": false, "playback_side": "client", "sync": {"visual_offset_ms": "", "haptic": ""},
  "checks": {"mobile": "not-run", "headphones": "not-run", "repetition": "not-run", "policy": "not-run"},
  "evidence_rule_ids": [], "proposal_values": [],
  "ai_prompt": {"text": "", "duration_s": null, "prompt_influence": null, "model": ""},
  "check_plan": "", "status": "PROPOSAL",
  "primary_outcome": "", "perceived_emotion": "", "induced_emotion": "",
  "truth": {"server_confirm": true, "prediction": "", "dedup_key": "", "rollback": ""},
  "event_rate": {"per_min": null, "burst_per_s": null, "aggregation_ms": null},
  "rhythm": {"bpm": null, "onsets_per_s": null, "spectral_hz": "", "modulation_hz": ""},
  "provenance": "", "accessibility": {"caption": "", "visual": "", "sound_off": "", "reduced": "", "haptic": ""},
  "delivery": {"format": "flac", "rate_hz": null, "channels": null, "peak_dbfs": null, "true_peak_dbtp": null, "loudness": "", "level_measure": "", "tool": ""},
  "rights": {"provider": "", "licence": "", "date": "", "inputs": "", "destinations": "", "moderation": "", "experience_permission": ""},
  "verification": {"evidence_reviewed": "not-run", "file_analysed": "not-run", "auditioned": "not-run", "game_tested": "not-run", "phone": "not-run", "headphones": "not-run", "mono": "not-run", "sound_off": "not-run", "fixture_1000": "not-run"},
  "load": {"watchdog_ms": null, "expiry_ms": null},
  "change_gate": {"agent_tunable": [], "needs_review": [], "fallback": "", "rollback": ""},
  "job": "", "story_point": "", "verb": "", "stages": [{"stage": "", "event_id": "", "timing_rev": "", "kind": "attempt", "layers": []}],
  "identity": {"signature": "", "feel_words": [], "differ_from": "", "tone_check": ""},
  "carry": {"hearing_distance_studs": null, "far_version": "", "tier_by_viewer": {}},
  "sources": {"prompts": [], "takes_per_round": null, "rounds_used": null, "odd_variant": "", "rank_table": "", "pick_reason": "", "stand_ins": []},
  "build": {"parts": [], "recipe": "recipe.json", "unprocessed_tried": false},
  "playtest_log": [{"date": "", "build_rev": "", "owner_words": "", "fix": "", "lesson": ""}],
  "playback": {"space": "2D", "reason": "", "actor_version": "", "others_version": "",
               "falloff": {"mode": "", "min_studs": null, "max_studs": null, "custom_points": [], "angle": ""},
               "listener": "Character", "takes_room": false,
               "ducks": {"needed_because": "", "what": [], "depth_db": null, "attack_ms": null, "release_ms": null, "why": ""}},
  "targets_file": "card.json"
}
```

## D. `card.json`: the machine part read by soundbench

One per cue folder (`content/audio/<cue-id>/card.json`), written before the first take (SKILL.md §2 step 4). `render`
checks the delivered file against it (exit 0 pass, 1 a target failed, 2 refused or bad input, 3 family incomplete); `rank` scores
each round's takes against it (exit 0 use, 1 regenerate or owner, 2 refused; `craft-process.md` §5). Every field is checked when read: an unknown key or a typo is an error, never a dropped target.
Values are start values (P) until a play-test confirms them (`editor-design.md` §7; schema: `tools/audio/soundbench/card.py`).

| Part | Holds | Rules |
| --- | --- | --- |
| `cue`, `kind`, `category`, `tier` | id; kind (hit, impact, ui_click, pickup, chime, stinger, countdown, tell, warning, whoosh, riser, voice, sustained, ambience, loop_bed, loop_music); sfx, ui, music, ambience, voice; minor, frequent, important | the kind sets which onset `trim` and the onset target bind to, whether sustained-only operations are allowed, and whether variants are refused (tell, warning, countdown) |
| `level` | `measure` (F-09 for one-shots, F-13a for a family of siblings, LUFS-I only for 0.4 s or more), target, tolerance, `must` | **name the measure**: F-09 RMS is never called LUFS (S-209); `loudness` in the edit pass uses the same function |
| `targets` | each `{min, max, must}`: `onset_ms` (with `binds_to`: `F-01` for rising sounds, `main_transient` for hits; default from the kind), `main_transient_ms`, `attack_rise_ms`, `attack_share_5ms`, `sound_ms`, `file_ms`, `true_peak_dbtp`, `sample_peak_dbfs`, band shares (`below_120`, `band_120_500`, `band_500_5k`, `above_5k`), `phone_loss_db`, `mono_drop_db`, `loop_seam`, `clicks`, `edge_clicks` (a first or last sample far from zero: `trim` fades a start that begins mid-waveform), `tail_snr_db`, `roughness`, `flatness` | `must` = render fails without it; `aim` (`must: false`) = listed as a miss, not a failure. Use `must` for what breaks the cue (late onset, clipping, no phone band, a paid-reveal level), `aim` for taste ranges. `loop_seam` (with `why`) only tightens R-26's must limit of 2; loosening needs `must: true` and a non-empty `why` (logged in `limit_from`) |
| `key` | root and scale | for `to_key` and pitched parts |
| `form` | loop, mono, variants (count) | 3D cues: mono until the stereo-emitter probe. `loop: true` adds the must rows `form.loop_*` at render; `variants: n` asks for n files `out/<cue>-v<k>.flac` (from the round's `takes` or a seeded `variants` block) and adds `form.variants` and `variants.level_spread` (R-31); refused for tell, warning, countdown (`craft-process.md` §6) |
| `family` | id, `paid_reveal`, siblings | a paid-reveal family runs F-13 b and the F-03 1 dB check across siblings on every render (D-03, hard). Every member's cue folder sits side by side in one parent folder (members are found by scanning the sibling folders). Write every member's card before the first render of any member: a missing or one-sided card is refused (exit 2); a member not rendered yet gives exit 3 (family incomplete: re-render after the siblings); each render writes `<family-id>.family.json` beside the cue folders |
| `playback` | `space` 2D or 3D, `falloff` (mode, bounds), `takes_room`, `ducks` | stored and passed to the log; the editor does not act on it: Roblox plays it (fields 51-54) |
| layer targets (in `recipe.json`, not the card) | each `layers[]` entry's `targets`, same names and form as the card's | judged on the layer as placed, alone, as rows `layer[<name>].<target>`; **every layer of an important cue needs them** (render refuses otherwise); `layer[<name>].edge_clicks` (max 0) is added by render: must for important cues, aim for the others |

```json
{"cue": "SFX-COMBAT-HIT", "kind": "hit", "category": "sfx", "tier": "minor",
 "level": {"measure": "F-09", "target": -12.0, "tolerance": 1.0, "must": true},
 "targets": {"onset_ms": {"max": 3, "binds_to": "main_transient", "must": true},
             "true_peak_dbtp": {"max": -1.0, "must": true},
             "band_500_5k": {"min": 0.10, "must": true},
             "phone_loss_db": {"max": 12, "must": false},
             "sound_ms": {"min": 150, "max": 400, "must": false}},
 "form": {"loop": false, "mono": true, "variants": 0},
 "playback": {"space": "3D", "falloff": {"mode": "inverse", "max_studs": 80}, "takes_room": true, "ducks": null}}
```
