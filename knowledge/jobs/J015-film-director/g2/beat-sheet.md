---
type: job
scope: universal
status: draft
updated: 2026-10-21
source: J015-T09 brief (lead), paper example knowledge/reference/film/03-vocabulary-method-templates-review.md §9
supersedes: []
---
> Author: film-director · claude-opus-5-5 · high · 2026-10-21

# Beat sheet: J015 G2 `boss-reveal`

> Revision: 5 (same revision as `boss-reveal.shots.json`), 2026-10-21. Status: **PROPOSAL** until the owner approves the beat contract (decision id: none yet). Timings below are measured in the greybox animatic (`animatic-manifest.md`); the acting durations inside them are my proposals for the owner to direct.

## Beat contract (owner approves this first)
| Field | Value |
| --- | --- |
| Player's situation before | In play, with control. The player has walked into a flooded, moonlit stone observatory. A pulsing amber beacon sits on a pedestal in the middle; a huge kneeling statue sits behind it in a shaft of moonlight; a lit arch on the left wall is the way out. The player knows only: "there is a prize". |
| Change in knowledge or feeling | Curiosity → intention (in play, by the player's own walk and interact) → uncertainty (the beacon dies before the hand reaches it) → recognition (their own avatar looks up and backs away) → concrete threat (the statue the player walked past is alive, holds the beacon's light and has seen them) → agency (fight for the beacon on the right, or leave by the exit on the left). |
| Consequential character action | The guardian wakes and plants its hand between the explorer and the beacon. |
| State after | Explorer one step back from the pedestal, facing the guardian; guardian crouched over the beacon in its encounter start pose; exit open and lit at screen left; player has control. |
| Why interrupt | A spatial deception (the statue is alive) needs a precise reveal order the player cannot be trusted to frame alone, and it must end on a readable arrangement. The approach and the decision to take the beacon do not need a takeover, so they stay in play. |
| Camera mode | **Hybrid** (film-direction D-02). Beat 1 (the paper's shot A) stays player-directed; the authored camera starts on the player's own interact press and runs 4 shots (B-E, 175 frames = 5.833 s at 30 fps); E ends on a frame the play camera inherits. Reason: the intention must be the player's choice, not an acted one; only the deception needs the camera. Alternative kept for the owner: fully authored, the paper's A first (see "Alternatives"). |
| Essential information (must also survive a skip) | 1. The statue is a living guardian. 2. It now holds/guards the beacon. 3. The exit is open on the left. These are all visible in the E end frame, which the skip lands on directly. |
| Optional atmosphere | The beacon's last pulse, the ripples, the moonlight on the rising head, the amber eyes matching the beacon, the vocal. |
| Platform limits | Mild fantasy threat, no injury shown, no gore, no franchise look (`platform-policy` checked at design time: no purchases, rolls, chat or player data in this moment, so no policy flag; horror intensity stays "a statue wakes", no jump scare, no shake). |

## Beats
| Beat | Shots | Frames (s) or ending event | Player knows before | Event that changes it | Whose intention | Question carried forward | What the player sees / feels | Fixed (value + source) | Open per craft | Owner notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 (play) | none (was paper shot A) | until the player presses interact at the pedestal | nothing yet | the beacon's pulse (light + `sfx.beacon.pulse`) draws them in; the statue is in the line of approach | player | "can I take it?" | curiosity → intention, by their own walk | the statue is on the approach line, the exit visible from the entry (blocking map) | environment: how the beacon calls; the statue must read as architecture | approve hybrid? |
| 2 | B | f1-37 (0.000-1.233 s), cut when the first ripple reaches the pedestal foot | "the beacon is a prize" | beacon collapses to an ember before contact (+20), hand stops (+26), ripples from the statue's base (+28) | player (reaching) | "what moved?" | intention → uncertainty | cut frame measured in Blender (ripple travel 4.708 studs, arrival f38) | sound: the stopped pulse; VFX: ripple read | does the collapse read as "refused", not "broken"? |
| 3 | C | f38-73 (1.233-2.433 s), cut 2 frames after the step back lands | "something is wrong behind the beacon" | stone crack off screen (+3) → head turns up (+7..+17) → step back (+20..+34) | explorer reacts | "what is it looking at?" | uncertainty → recognition, through the avatar | crack before the look (sound is the stimulus) | animator: the realisation in body and head | reaction before reveal (recommended)? |
| 4 | D | f74-137 (2.433-4.567 s), cut 2 frames into the strike anticipation | "it is the statue" | rise (0..30), head enters the moon shaft (+16, measured), eyes ignite (+32), gaze to explorer (+40..+50), vocal (+50), arm draws back (+52) | guardian | "what will it do?" | recognition → concrete threat | eyes after the head is lit (measured order) | VFX: eye glow; sound: rise, vocal | static (recommended) or tilt? music here? |
| 5 | E | f138-175 (4.567-5.833 s), control returns on the last frame | "it is coming for me" | strike lands between explorer and beacon (+6, measured), settle (+30), beacon faint pulse (+20) | guardian, then player | "fight or leave?" | threat → agency | FOV 70 (Roblox default, Camera.yaml:269); end frame = play camera pose | engineering: camera handoff; UI: prompt | music entry on the strike? |

## Gameplay state sheet (agree with the game designer and engineering)
| Item | Value |
| --- | --- |
| When control stops | On the interact press at the beacon's prompt (server validates the interact; the server starts the encounter state; the client plays the sequence). |
| What the avatar does | Moved to the mark (-2.5, 0) facing the beacon behind the cut into B; plays the reach, look-up and step-back (engineering decides how: animation track or a local stand-in; avatar variety applies). |
| What keeps running elsewhere | ASSUMPTION (no game design yet): the guardian is passive until control returns; nothing can damage the explorer during the sequence. Other players in the same server: UNKNOWN (open question 4). |
| What can interrupt | Death (should not happen: guardian passive), leaving, disconnect, a newer scene, a missing streamed asset. |
| Audience | One player (the one who pressed interact). Shared server behaviour: open question 4. |
| Skip policy | Individual skip, offered from the first frame (PROPOSAL; the first game never ruled on skip timing, N4 P-04). |
| Who decides completion | The server owns the encounter state from the interact; the cinematic only presents it. No reward, damage or beacon pickup depends on the cinematic finishing (film-direction §5). |

| Ending | Resulting story state | View the player gets | First safe action | Server transition requested |
| --- | --- | --- | --- | --- |
| Finish | guardian awake, crouched over the beacon; encounter started | E end frame (camera pose in `boss-reveal.shots.json` shot E `camera`) | move: left toward the exit, or toward the guardian | encounter start (already sent at interact) |
| Skip | same as finish | cut straight to the E end frame (no strike replay, no cues replayed; music starts if the owner picks music on E) | same | none extra |
| Repeated skip | one result; later presses ignored | same | same | none |
| Failure (guardian model not streamed, actor missing, camera taken) | encounter state still starts | fall back to the E end frame with the guardian in its start pose; if the guardian is missing, keep play camera and show the prompt; never hold on an empty mark | move | none extra; log the failure |
| Death or respawn mid-sequence | should not occur (guardian passive); if it does: teardown, normal respawn | respawn view | respawn flow | none from the cinematic |
| Disconnect and rejoin | server keeps the encounter state; on rejoin: no cinematic replay (PROPOSAL) | play camera | move | server releases any cinematic hold on disconnect |
| Late join (shared) | UNKNOWN (open question 4) | — | — | — |
| Repeat attempt (after losing the encounter) | guardian already known | PROPOSAL: no replay; or E only (1.267 s) | move | encounter restart |

## Readiness (film-craft step 1)
| Item | Needed for | State | Ticket (not sent; this run writes briefs only) |
| --- | --- | --- | --- |
| Explorer | all shots | **player avatar** (any): proxy only; acting must read with body and head, not face | animator brief `brief-animator.md` |
| Guardian model + rig | D, E (B, C partly) | missing: needs torso rise from a kneel, head pitch, one-arm strike, emissive eyes, a crouched encounter pose | character-rigger ask (not written: out of this run) |
| Observatory set | all | missing: flooded floor, plinth, pedestal, moon oculus, exit arch on the north-north-west wall | environment-designer ask (not written) |
| Beacon prop + light states | B, E | missing: pulse, collapse to ember, faint pulse | VFX brief `brief-vfx.md` |
| Sounds (9 cues) | all | missing; TEMP tones only in the animatic | sound-designer ask (cue sheet ready) |
| Game art bible | boards | missing: kit template locks used (`--bible templates/skill/art-bible.md`) | — |

## Alternatives (each with a recommendation)
| Choice | Option A | Option B | Recommendation |
| --- | --- | --- | --- |
| Camera mode | Hybrid: beat 1 in play, authored B-E (5.833 s) | Fully authored with the paper's shot A (establishing wide, avatar walks itself to the beacon) | **Hybrid**: the intention is the player's own act; the previs E frame re-establishes geography anyway. Option B guarantees the player has seen the exit before the reveal, at the cost of taking control at the moment of curiosity |
| Shot D camera | Static low wide (scale, beacon and explorer in frame in 22/22 sampled frames) | Tilt following the head (eyes larger; beacon in frame 6/22, explorer 0/22; peak 1.123 deg/frame) | **Static**, plus a VFX eye glow that reads at small size; tilt as owner option (`previs/shotD_static_vs_tilt.png`) |
| Reaction order | Reaction (C) before reveal (D) | Reveal first, then reaction | **Reaction first** (alarm before object, film-direction D-08) |
| Music | No music until the strike in E; music marks "now it is a fight" | Music enters on the eyes in D | **On the strike in E**: D keeps sound-led (rise, delayed vocal) |
| Exit placement | North-north-west wall: retreat away from the guardian (previs v13+) | Past the guardian (tested v3-v12: exit and guardian overlapped in the play view) | **Away from the guardian**: the frame in E is the choice, left vs right |
