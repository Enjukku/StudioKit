> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10. Revised by J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018).

# Cue card

One card per sound event. Every field gets a value or "n/a". Tag every number (M)/(X)/(O)/(=)/(P). Short card for minor
cues: fields 1-6, 12-19, 22, 26, 30, 43, 45, 47.

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
| 18 | Ducking | Whom it ducks (depth, attack, release); who ducks it | dB, ms | S-109..S-111, S-211, S-143 |
| 19 | Spatial | 2D/3D; distance and angle curves; rear; occlusion | studs, dB, ° | S-11, S-118, S-225, S-145, S-146 |
| 20 | Roblox objects | Instances, wiring, bus, effects | class names | S-140..S-149 |
| 21 | Load and playback side | Preload Y/N; client or server | — | S-150, S-151 |
| 22 | Sync | Trigger event id; file onset (F-01); inside the S-133 window of the first lit contact frame; haptic and offset | event; ms | S-74, S-131, S-133 |
| 23 | Mobile check | Phone-speaker pass; partials >300 Hz; mono drop | pass/fail; dB | S-156..S-160, S-229 |
| 24 | Headphone check | Sub not boomy; no sustained 2-5 kHz; no AM 30-150 Hz on positive cues | pass/fail | S-08, S-22 |
| 25 | Repetition check | Machine-gun test; misophonia check | pass/fail | S-96, S-101 |
| 26 | Policy check | Net value > 0 if celebratory; every paid outcome gives real benefit (S-167); win sound beside the plain value (S-163); outcome meaning tested; paid-random rules; original or licensed | pass/fail | S-161..S-173, S-232..S-234 |
| 27 | Evidence | Rule IDs used; list every (P) value | IDs | — |
| 28 | AI prompt and settings | Prompt; duration, influence, candidates | text; s; 0-1 | S-123..S-127 |
| 29 | Check plan | Self-review lines with their inputs; check-in questions; loudness-matched A/B pairs (S-18) | text | S-18; `review.md` §2-§3 |
| 30 | Status | PROPOSAL / tuned in Studio / designer-confirmed | enum | — |
| 31 | Primary player outcome | Detect, identify, confirm or feel | text | S-183 |
| 32 | Perceived vs induced emotion | Two fields | names | S-183 |
| 33 | Truth conditions | Server confirm? Prediction allowed? Dedup key; cancel or rollback | Y/N; key; text | S-219, S-228 |
| 34 | Event rate | Per minute; max burst per second; aggregation window | /min; /s; ms | S-66, S-194, S-200 |
| 35 | Rhythm and modulation | BPM and onsets/s separately; spectral Hz and modulation Hz separately | BPM; /s; Hz; Hz | S-174, S-175 |
| 36 | Numeric provenance | Tag summary | tags | S-176 |
| 37 | Accessibility | Caption; visual indicator; sound-off equivalent; reduced intensity; haptic meaning | text | S-191, S-221 |
| 38 | Delivery | Format, rate, channels; peak dBFS, true peak dBTP; loudness and window; tool and version | units | S-104, S-209, S-210 |
| 39 | Rights manifest | Creator or provider; licence evidence; date; input provenance; destinations; moderation; experience permission | text | S-216, S-227 |
| 40 | Verification statuses | Evidence reviewed, file analysed (F-xx), auditioned (an owner check-in answer, never your own), game-tested; phone, headphones, mono, sound-off, 1,000-event fixture | passed/failed/not-run | S-204, S-217 |
| 41 | Load and expiry | Load watchdog; late-event expiry | ms | S-223 |
| 42 | Change gate | Fields an agent may tune (with bounds); fields needing designer review; fallback; rollback | lists | S-217 |
| 43 | Job and story point | Cue, feedback or emotion; the story point in one line; the target-experience line quoted | text | SC-01 |
| 44 | Verb and texture | The mechanic verb (as on the clip card and frame script); how the texture moves like it | text | SC-03 |
| 45 | Stages | Stage → event id @ timing revision → attempt or outcome → layers (`craft-process.md` §2) | table | SC-04 |
| 46 | Identity | Signature element; character feel words; nearest similar to differ from; tone words; identity-sheet check | text | SC-11 |
| 47 | Carry and viewers | Hearing distance in studs; far version; tier per viewer (own, ally, threatened, bystander) | studs; tier | SC-07 |
| 48 | Sources and options | Texture prompts, takes, odd variant, reference sound, options and why the pick won, stand-ins with their better source | text | SC-14 |
| 49 | Build | Library parts used (tier); processing steps with purpose; what is baked, what is live; unprocessed tried | list | SC-08, SC-09, SC-15 |
| 50 | Check-in log | A, B, C: question, the owner's answer word for word, date, revision heard | text | `review.md` §2 |

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
| 18 | Ducks nothing; ducked 6-9 dB by critical warnings |
| 19 | 3D, AudioEmitter at the cluster centroid; full level to about 13 studs, −6 dB per doubling after (P); update obstruction after walls fall (S-201) |
| 20 | Pooled AudioPlayers (`Asset`) → Wire → AudioEmitter on an Attachment; AudioListener → Wire → SFX AudioFader → master AudioCompressor → AudioLimiter → AudioDeviceOutput |
| 21 | Preload Y for the player's own break; client playback |
| 22 | Trigger: `break_confirmed` event; file onset ≤ 5 ms (F-01); inside the S-133 window of the first lit break frame; same frame as hitstop start; light haptic on own large breaks (P) |
| 23 | Crack and rattle carry identity on the phone; body audible through 120-480 Hz partials; mono drop ≤3 dB; 180-250 Hz high-pass preview stays recognisable |
| 24 | Sub not boomy; no sustained 2-5 kHz scrape; no 30-150 Hz AM |
| 25 | 10 s machine-gun test of a chain reaction; 1,000-selection fixture; no wet sounds |
| 26 | Original or licensed with manifest; not an outcome cue (net-value rule n/a); uploaded under the experience owner |
| 27 | S-75, S-76, S-78, S-79, S-80, S-81, S-84, S-88, S-90, S-152, S-157, S-199, S-200, S-202, S-203; (P) in 5-10, 12-19, 22 |
| 28 | See `ai-generation-prompts.md` §C crate rows; 4 candidates each; keep 1-2 |
| 29 | R-20 to R-25 on every file; R-41 debug cue log in a 10 s chain reaction; check-in C (owner, loudness-matched): jitter ±50 vs ±100 cents; 4 vs 6 vs 10 variants; phone vs headphones. Pass: the owner cannot spot a repeat in a 10 s storm and orders small < medium < large |
| 30 | PROPOSAL |
| 31 | Hear which material broke and roughly how much, in sync with the picture |
| 32 | Perceived: power, satisfaction. Induced: satisfaction (asked apart from liking) |
| 33 | Server confirms; owner's client may predict the crack only (P); dedup key = break-event ID; on rejection body and debris never play |
| 34 | Up to about 10 clusters/s in chains (P); secondary contacts coalesced in 50-100 ms |
| 35 | BPM n/a; crack 2-6 kHz, body 60-200 Hz; modulation none |
| 36 | All (P) except class names (O) and 2^(n/12), 10^(dB/20) (=) |
| 37 | Caption "[crates collapse]" only for large off-screen breaks; reduced intensity: sub off, debris −6 dB (P) |
| 38 | Mono .ogg, 48 kHz; peak ≤ −1 dBFS; loudness-matched within the break family; tool and version recorded |
| 39 | Provider, model, date, plan evidence, prompt; moderation and experience permission checked |
| 40 | All not-run |
| 41 | Watchdog 5 s; late-event expiry 150-250 ms (P) |
| 42 | Agent may tune jitter inside S-90/S-91 bounds and cooldown inside 80-150 ms; peak level, voice caps, duration need designer review; fallback: silence + visual debris |
| 43 | Feedback and emotion: "the crate you hit really broke"; target line: "smashing everything feels powerful" |
| 44 | n/a (no ability verb); material wood: dry, splintering, short |
| 45 | crack on `break_confirmed` (outcome); thud same event; rattle +30-80 ms after it; no attempt cue (the swing has its own) |
| 46 | No signature (world prop); wood family of the sound-code table; tone words "chunky, toy-like" |
| 47 | Own breaks 2D-close tier 2; other players' breaks 3D tier 5, silent by 60 studs (P) |
| 48 | Prompts "dry pine planks snapping", "wooden pallet splintering", "cardboard box crushed" (odd); 4 takes each; picked vs the category reference; stand-in: none |
| 49 | Parts: crack (raw → cleaned), thud (pitched down 4 st, low cut 50 Hz), rattle (spliced takes); all baked dry; room from the zone reverb |
| 50 | not run |

## C. JSON blank

```json
{
  "id": "", "name": "", "trigger": "", "target_emotion": [], "arousal": "", "valence": "",
  "priority_tier": null, "level_db_rel": "", "length_ms": "",
  "layers": {"transient": "", "body": "", "sub": "", "tail": ""},
  "key": {"pitched": false, "root": "", "scale": "", "ladder": {"step_st": null, "cap": null, "reset_ms": null}},
  "variants": {"count": null, "exclude_last": null}, "pitch_jitter_cents": "", "volume_jitter_db": "",
  "scaling": "", "cooldown_ms": null, "voice_cap": {"max": null, "steal": ""},
  "ducking": {"ducks": "", "ducked_by": ""}, "spatial": {"mode": "2D", "distance_curve": "", "angle_curve": "", "occlusion": ""},
  "roblox_objects": "", "preload": false, "playback_side": "client", "sync": {"visual_offset_ms": "", "haptic": ""},
  "checks": {"mobile": "not-run", "headphones": "not-run", "repetition": "not-run", "policy": "not-run"},
  "evidence_rule_ids": [], "proposal_values": [],
  "ai_prompt": {"text": "", "duration_s": null, "prompt_influence": null, "candidates": 4},
  "check_plan": "", "status": "PROPOSAL",
  "primary_outcome": "", "perceived_emotion": "", "induced_emotion": "",
  "truth": {"server_confirm": true, "prediction": "", "dedup_key": "", "rollback": ""},
  "event_rate": {"per_min": null, "burst_per_s": null, "aggregation_ms": null},
  "rhythm": {"bpm": null, "onsets_per_s": null, "spectral_hz": "", "modulation_hz": ""},
  "provenance": "", "accessibility": {"caption": "", "visual": "", "sound_off": "", "reduced": "", "haptic": ""},
  "delivery": {"format": "", "rate_hz": null, "channels": null, "peak_dbfs": null, "true_peak_dbtp": null, "loudness": "", "tool": ""},
  "rights": {"provider": "", "licence": "", "date": "", "inputs": "", "destinations": "", "moderation": "", "experience_permission": ""},
  "verification": {"evidence_reviewed": "not-run", "file_analysed": "not-run", "auditioned": "not-run", "game_tested": "not-run", "phone": "not-run", "headphones": "not-run", "mono": "not-run", "sound_off": "not-run", "fixture_1000": "not-run"},
  "load": {"watchdog_ms": null, "expiry_ms": null},
  "change_gate": {"agent_tunable": [], "needs_review": [], "fallback": "", "rollback": ""},
  "job": "", "story_point": "", "verb": "", "stages": [{"stage": "", "event_id": "", "timing_rev": "", "kind": "attempt", "layers": []}],
  "identity": {"signature": "", "feel_words": [], "differ_from": "", "tone_check": ""},
  "carry": {"hearing_distance_studs": null, "far_version": "", "tier_by_viewer": {}},
  "sources": {"prompts": [], "takes": null, "odd_variant": "", "reference": "", "pick_reason": "", "stand_ins": []},
  "build": {"parts": [], "steps": [], "baked": [], "live": [], "unprocessed_tried": false},
  "checkins": {"A": "", "B": "", "C": ""}
}
```
