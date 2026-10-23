---
type: job
scope: universal
status: draft
updated: 2026-10-23
source: J020 stage 0 (understanding pass)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-23

# J020 workflow map: how a sound goes from idea to game (for the owner's G1 review)

**What I read (2026-10-23):** the sound designer role (`.agents/roles/sound-designer.md`), its skill (`sound-design`: SKILL.md 206 lines, 14 reference files, 1,517 lines), the kit measuring tool `tools/audio/cue_check.py`; in GreatWallSim: `tools/audio/eleven.py`, `audio_edit.py`, `upload_roblox.py`, `manifest.csv` (423 rows), `knowledge/design/audio-plan.md` (§1-§21), `audio-review-redo.md` (36 files measured) and your sound decisions (D-017, D-064, D-075, D-077, D-082, D-084, D-165). **Not read yet:** your ElevenLabs prompting guide (it changes step 3 below).

## 1. The workflow today

| # | Step | Who | Tool | How well it works |
| --- | --- | --- | --- | --- |
| 1 | Frame the sound: its job (cue, feedback, emotion), the action, how often it plays, who hears it, phone or headphones | sound designer | cue card (template) | Good. The books are detailed and careful |
| 2 | Stage it on the animation and VFX timing (one sound per stage, the hit on the contact frame) | sound designer + animator + VFX | timing list | Good on paper; no game job has run the new recipes yet |
| 3 | Write the ElevenLabs prompt (textures, not object names) | sound designer | prompt book (from ElevenLabs' docs, 2026-10-10) | Fair. Not built from your guide |
| 4 | Generate takes | sound designer | GreatWallSim `eleven.py` (sound effects v2, music, voice) | Works, with a credit budget stop. Only in GreatWallSim |
| 5 | Pick a take | tool | `audio_edit.py` picker | Weak. It only rejects silent or clipped takes and picks the nearest length. It does not use the cue card |
| 6 | Edit (the book's 8-step design pass: clean, pitch, low cut, compress, add space, compress, transient, saturation) | tool | `audio_edit.py` | **Partial.** Has: trim, fades, high and low cut, saturation, pitch (it also changes the length), loudness to a target, a peak limiter, seamless music loops, layering at exact times, Ogg export. **Missing:** EQ boosts and cuts, compression, transient shaping, pitch without a length change, time stretch, reverb and echo, noise and hum removal, movement (chorus), variant sets |
| 7 | Measure | sound designer | kit `cue_check.py` (tested) and GreatWallSim `analyse()` | The kit tool is good. The two tools measure loudness of short sounds differently (review finding F17), so they disagree by 1.5-4.6 LU |
| 8 | Review | sound designer | numbers only | **Works.** It found real faults without hearing: footsteps silent on phones, hits 30-60 ms late, a "locked" sound that was only hiss, wrong notes. But its scripts were throwaway, not a tool |
| 9 | Upload | owner approval | `upload_roblox.py` | Works (314 of 314 approved) |
| 10 | Play in the game | feature-builder | Roblox audio graph | Had a bug: every first play was silent until it was fixed (audio plan §21a). Now a debug cue log shows each play |
| 11 | Judge | owner | play-tests (D-064) | The books still ask for three listening check-ins (A, B, C). That conflicts with your D-064 and J020-D3 |

**GreatWallSim's tools, in one line:** carefully made and honest (every file records its edits and says "auditioned: not-run"). But they are written for that one game (its universe id is in the code), have no tests, and cover only the simple half of editing.

## 2. Conflicts with your rules (to fix in the books)

| Book line | Says | Your rule | Change |
| --- | --- | --- | --- |
| SC-08, SC-10, design pass, `roblox-audio.md` | room reverb, underwater filter and pass-by pitch live in Roblox | J020-D1: no audio editing in Roblox | all of these baked into the files (one file per space where a sound plays in different rooms) |
| Steps 5, 6, 11; review §2; role file | owner listening check-ins A, B, C; "approve nothing before check-in C" | D-064, J020-D3: you judge in play-tests | "done" = measured + plays on its event in the game; feel = your play-test; your flags become lessons |
| Step 6 | "picked against the category reference" | J020-D3: no reference sounds | picked against the cue card's targets |

## 3. The workflow I propose

| # | Step | Who | Tool |
| --- | --- | --- | --- |
| 1 | Frame and stage the cue (cue card, timing list) | sound designer | books (unchanged) |
| 2 | Write targets on the card as numbers: start, attack, length, bands, phone loss, loudness slot, notes | sound designer | cue card |
| 3 | Prompt and generate takes: minor cue 1, frequent cue 2, hero cue 3 (J020-LD1) | sound designer | ElevenLabs, prompt book rebuilt from your guide; a new kit generate step (GreatWallSim's `eleven.py` only as reference, J020-D5) |
| 4 | Measure every take and rank it against the card | workbench | **new editor**: measure + pick |
| 5 | Fit edits from a written recipe, in the book's order, all baked into the file (space too) | workbench | **new editor**: edit |
| 6 | Re-measure, plus a spectrogram picture; a take that still misses → change the prompt and regenerate (at most 3 rounds), never pile on edits | sound designer | workbench |
| 7 | Layer the important sounds (click + body + tail, each generated alone) and make variant sets for frequent sounds | workbench | workbench: layer, variants |
| 8 | Export Ogg with a log of every edit (redo from the original take at any time) | workbench | workbench |
| 9 | Upload (your approval rule per game) | lead | a new kit upload step (GreatWallSim's `upload_roblox.py` only as reference) |
| 10 | Play only in Roblox (J020-D8): most sounds 2D (same volume everywhere); 3D only for sounds that come from a place, with a falloff range per sound; volume and ducking by fader volume (J020-LD4); no effects | feature-builder | Roblox audio graph (§6) |
| 11 | Prove each sound plays on its event (debug cue log) | studio operator | Studio |
| 12 | You judge in play-tests; each flag becomes a lesson in the books | owner | play-test |

## 4. The editor (what it is, for the design step after G1)
A command-line tool made for the agent: text recipes in, numbers and spectrogram pictures out, every step logged and redone from the original take, tests built from the faults the GreatWallSim review found. It runs on what the kit already has (numpy, scipy, soundfile, pyloudnorm) plus ffmpeg for the effects that are hard to make sound clean (pitch without a length change, time stretch, some reverb). It is built new (J020-D5); GreatWallSim's `audio_edit.py` is only a reference for what it does well (careful loudness, loops, layering at exact times, an edit log per file) and stays unchanged in that game (J020-D6). It joins `cue_check.py` into one tool, so there is one way to measure. It covers every edit the book's design pass needs: clean (trim, fades, noise, hum, rumble), pitch with and without a length change, time stretch, EQ (cuts, boosts, shelves), compression, transient shaping, saturation, designed space (reverb, echo) baked in, movement (chorus, flanger), layering, variant sets, loops, loudness and peak limits.

**Limit, said plainly:** the agent cannot hear. The editor proves numbers (timing, loudness, phone audibility, seams, notes). Whether a sound feels right stays your call in the play-test.

## 5. Your answers (2026-10-23)
| # | Question | Answer |
| --- | --- | --- |
| 1 | Volume and 3D in Roblox | J020-D8: play and place only; 3D for the few sounds that come from a place |
| 2 | Rooms | left to the lead: J020-LD2 |
| 3 | Listening check-ins | replaced by your play-tests: J020-LD3 |
| 4 | GreatWallSim | keeps its tools unchanged; the kit is built new: J020-D5, J020-D6 |
| 5 | Regenerate limit | 3 rounds: J020-D7 |
| — | Takes per prompt | J020-LD1: 1, 2 or 3 by cue type |

## 6. Roblox sound playback (Roblox Creator Docs mirror, read 2026-10-23: `audio/objects.md` "2D audio", "3D audio"; `_api-reference/classes/AudioEmitter.yaml`; `_api-reference/enums/DistanceAttenuationMode.yaml`, `SoundService.yaml` ListenerLocation)
| Kind | When | How it is wired | Falloff |
| --- | --- | --- | --- |
| 2D | most sounds: UI, own feedback, rewards, music, most effects | AudioPlayer → Wire → AudioDeviceOutput (through a fader bus) | none: same volume wherever the player is |
| 3D | a sound that should come from a place: a waterfall, a machine, another player's action | AudioPlayer → Wire → AudioEmitter on the part; the AudioListener (camera or character, `SoundService.ListenerLocation`) → Wire → AudioDeviceOutput | per emitter: `DistanceAttenuationMode` presets (Linear, LinearSquared, Inverse, InverseTapered) between `DistanceAttenuationBounds` (full volume inside the minimum, silent at the maximum; default 4 to 10,000 studs), or `Custom`, a volume-over-distance curve set with `SetDistanceAttenuation()` (the docs' example: half volume at 50 studs, silent at 70) |

### When a sound is 2D or 3D (the rule every cue card follows; J020-LD5)
The docs define the two kinds: 2D "plays from no particular location, remaining at the same volume regardless of the player's position"; 3D "plays from a particular location [...] increasing or decreasing in volume depending on the player's position and orientation". The choice below is the studio's rule built on that definition.

| Question about the sound | Answer → kind | Examples |
| --- | --- | --- |
| Is it about me, the player: my input, my result, my reward, my purchase, a screen? | 2D | button clicks, my coin pickup, level up, purchase, my own footsteps and jumps |
| Must every player hear it the same wherever they stand? | 2D | music, narration, a round start, a flood warning, the dam-built fanfare |
| Does it tell me *where* something is, so I can find it, face it or avoid it? | 3D | a threat's tell, an enemy, another player's action, a pickup to look for |
| Does it belong to a place I can see, and should it fade as I walk away? | 3D | a waterfall, a machine, a fire, a fountain, wind at a cliff edge |
| Is it the general mood of a whole area? | 2D bed for the area, plus 3D point sources for the visible things in it | a forest bed (2D) with a stream (3D) |

When in doubt: 2D. Most sounds are 2D (J020-D8); a 3D sound must name what its position tells the player.

### Setting a 3D sound (from the docs)
| Setting | What it does (docs) | Studio rule |
| --- | --- | --- |
| `DistanceAttenuationBounds` (min, max) | full volume inside min; silent at or beyond max; default 4 to 10,000 studs | min = the size of the thing (you are "at" it); max = where it must be gone. Write both on the cue card in studs |
| `DistanceAttenuationMode` | `Linear`: even fade between min and max. `LinearSquared`: steeper fade (Linear squared). `Inverse`: min ÷ distance, "mirroring how sounds attenuate in the real world" (never quite silent before max). `InverseTapered`: Inverse near min, LinearSquared near max, so it still ends silent at max. `Custom`: your own curve (`SetDistanceAttenuation()`; the docs' example: half volume at 50 studs, silent at 70) | ambience and world sources: `InverseTapered`; gameplay cues that must stay clear to a set range, then stop: `Linear`; `Custom` only when the card needs a shape the presets cannot give |
| Angle (`SetAngleAttenuation()`) | quieter when you are behind the emitter's look direction | only for sounds that point one way (a speaker, a cannon mouth); default none |
| `SoundService.ListenerLocation` | where the "ear" is: `Character`, `Camera`, `Default` (camera, in games with voice chat) or `None` (script) | one per game, in the game profile; with a third-person camera, `Character` keeps distances true to where the player stands (PROPOSAL, check in the first game) |
| `AcousticSimulationEnabled` | muffling through walls, bending round corners, echo, done by the engine | off (J020-D1) |
| `AudioInteractionGroup` | an emitter is heard only by listeners in the same group | default; only for split audio worlds |

The books change to match (in the build stage): `roblox-audio.md` keeps the graph, 2D and 3D and the falloff rules above, and drops the live AudioReverb, AudioEqualizer, AudioFilter and compressor ducking (J020-D1, J020-LD4); each cue card names 2D or 3D, and for 3D its falloff mode and range.
