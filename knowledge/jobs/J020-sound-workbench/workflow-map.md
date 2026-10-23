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
| 3 | Prompt and generate 4-8 takes | sound designer | ElevenLabs, prompt book rebuilt from your guide; `eleven.py` moved into the kit |
| 4 | Measure every take and rank it against the card | workbench | **new editor**: measure + pick |
| 5 | Fit edits from a written recipe, in the book's order, all baked into the file (space too) | workbench | **new editor**: edit |
| 6 | Re-measure, plus a spectrogram picture; a take that still misses → change the prompt and regenerate (at most 3 rounds), never pile on edits | sound designer | workbench |
| 7 | Layer the important sounds (click + body + tail, each generated alone) and make variant sets for frequent sounds | workbench | workbench: layer, variants |
| 8 | Export Ogg with a log of every edit (redo from the original take at any time) | workbench | workbench |
| 9 | Upload (your approval rule per game) | lead | `upload_roblox.py` moved into the kit |
| 10 | Play only in Roblox: the graph places and plays the sound and sets volume; no effects | feature-builder | Roblox audio graph |
| 11 | Prove each sound plays on its event (debug cue log) | studio operator | Studio |
| 12 | You judge in play-tests; each flag becomes a lesson in the books | owner | play-test |

## 4. The editor (what it is, for the design step after G1)
A command-line tool made for the agent: text recipes in, numbers and spectrogram pictures out, every step logged and redone from the original take, tests built from the faults the GreatWallSim review found. It runs on what the kit already has (numpy, scipy, soundfile, pyloudnorm) plus ffmpeg for the effects that are hard to make sound clean (pitch without a length change, time stretch, some reverb). It replaces `audio_edit.py` and joins `cue_check.py` into one tool, so there is one way to measure.

**Limit, said plainly:** the agent cannot hear. The editor proves numbers (timing, loudness, phone audibility, seams, notes). Whether a sound feels right stays your call in the play-test.

## 5. Questions for you
1. **Volume in Roblox:** is setting volume, 3D distance and turning other sounds down under an important one fine? That is playback, not editing. My recommendation: yes.
2. **Rooms:** a sound that plays in different spaces (a cave and a hall) gets one file per space with its reverb baked in. More files, but no Roblox effects. OK?
3. **Listening:** I take check-ins A, B and C out of the books and use your play-tests only. OK?
4. **GreatWallSim:** it keeps its own tools until the kit editor replaces them through a kit sync. OK?
5. **Regenerate limit:** at most 3 prompt rounds per cue, then it goes to you as "cannot make it fit yet" with the numbers. OK, or another number?
