> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10

# Mix, loudness, music system and player options

Core rules used here (in SKILL.md): S-102/S-207/S-104 loudness target and peaks, S-107/S-108 priority and level
slots, S-109/S-211 ducking, S-18 loudness-matched A/B. Roblox objects for buses, compressors and emitters:
`roblox-audio.md`.

## A. Loudness and measurement

| ID | Rule | Evidence |
| --- | --- | --- |
| S-103 | Measure loudness on a whole play capture with all buses, never on single sounds. | practice (Sony) |
| S-105 | Loudness range (LRA): casual 5-10 LU, action 15-20 LU, >20 excessive; mixed action-casual games (e.g. destruction) 8-12 LU. (P) | practice + inference |
| S-106 | Mix at the lower target in a quiet room, then raise per output route. | practice (Crytek) |
| S-208 | Passive gameplay (between rounds, spectating, respawn wait) drops at least 3 LU automatically. | standard (H.872) |
| S-209 | dBFS (sample peak), dBTP (true peak), LUFS (programme loudness), dB SPL (at the ear) differ. Roblox Volume is an amplitude multiplier: Volume = 10^(dB/20). Never label Volume or AudioAnalyzer RMS as LUFS or SPL. | = + practice |
| S-210 | Normalise within a cue family, not every asset to one LUFS number. Keep original, edited master and runtime export; listen to the platform transcode. | inference |
| S-121 | One project reference level; waiting areas never exceed it and stay quiet enough for speech. | practice (Disney) |
| S-112 | Compress heavy sounds at the source; keep a limiter on the master always. | practice (Crytek) |

Standards context (M-46, M-70): Sony −24 LUFS home, −18 portable, ±2 LU; Meta Quest −16 LUFS (2026); ITU-T H.872
(2024) also asks for a headphone switch −3 dB (S-231), a mid/high-cut EQ preset and subtitles on by default.

## B. Bus layout, ducking and layering

| ID | Rule | Evidence |
| --- | --- | --- |
| S-110 | Critical warning or dialogue ducks music and ambience 6-9 dB; an open menu ducks gameplay 3-6 dB. (P) | lead |
| S-111 | Duck attack 10-50 ms; release 300-700 ms for music, 500-1500 ms for speech-heavy music. (P) | lead |
| S-212 | Keep two rankings: information priority (must be heard now) and voice-survival priority (must not be cut); both may change with context (music can rank high in rhythm games). | inference |
| S-113 | Each layer owns a band: high-pass every non-sub layer near 100 Hz so one layer carries the sub; align transients to the same sample, offset only tails. | lead |
| S-117 | Sub-bass (below about 120 Hz) is reserved for hero events. | lead |
| S-118 | World-event distance curve: full level near, then −6 dB per doubling from 4 m (about 13 studs at 3.33 studs per metre). Custom AudioEmitter curve. (P) | practice + inference |
| S-225 | Short interactions: full level within 4-8 studs, silent by 30-60 studs. (P) | inference |
| S-122 | Crowd or ambient reactions start within about 200 ms of the visible event and scale with it; never a standing cover for dull moments. | practice + inference |
| — | Readable busy scenes: one foreground clue + one bed + ≤2 intermittent details; duck ambience 3-6 dB with a 100-200 ms lead-in for a clue (M-91, P). | lead |

## C. Music system

| ID | Rule | Evidence |
| --- | --- | --- |
| S-115 | Start with 2 layers (calm, intense); layer fade-in 2 s; state debounce 1-3 s; 2, 4 or 8-bar segments; stingers 2-5 s. (P) | inference (tutorial) |
| S-213 | Adaptive contract: equal-length, sample-aligned stems (foundation, pulse, texture, accent); state changes queue to the next bar, urgent cues bypass; fades 0.5-2 s; hysteresis 1-3 s; keep a logical playhead and rejoin it, never restart at 0. Verify engine scheduling before phase-locked stems. (P) | lead |
| S-116 | Next-area audio starts 0.5-2 s before a teleport or screen change (J-cut); test 0, 0.5, 1, 2 s. | lead |
| S-119 | Lobbies, shops, queues play music (pleasure r up to 0.26); never use bed music to raise arousal (r=0.042). | study |
| S-120 | Never claim tempo drives spending (140 stores: no total effect). | study |
| — | Tempo norms for genre beds (DJ guide, M-20): house 120-130, trance 126-140, DnB 170-175, hip-hop 85-110 BPM; hard techno moved to 145-160 after 2021. Per-genre game tempos: `genre-presets.md`. | practice |
| — | One theme in several context versions (start, replay, overtime, wrap-up) keeps identity across moods (M-82, M-83, lead). | lead |

## D. Player options and accessibility

| ID | Rule | Evidence |
| --- | --- | --- |
| S-139 | Separate volume sliders for music, SFX and speech. | practice (Roblox docs) |
| S-138 | Calm sound option: rounder waveforms and a high-shelf cut above 2 kHz. | lead |
| S-214 | Safe-listening options: mid/high-cut EQ preset; one "smart listening" preset enabling all of them; captions on by default. | standard (H.872) |
| S-221 | Every critical task is completable muted, in mono and with haptics off. Captions for non-speech events; visual direction or type indicators; haptics supplement only. Check caption density at peak action. | lead + standard |
| S-234 | Young players: never rely on a high device volume; provide sliders and a reduced-intensity option; keep peaks controlled (a game cannot measure the child dose of 75 dB(A), 40 h/week). | standard + inference |
| S-215 | Log audio telemetry: volume-slider changes, mutes, session time. | standard (H.872) |
| S-218 | Before an A/B, register 1 primary outcome, the smallest useful change, exclusions and a stopping rule; keep null and adverse results with device and audience details. | inference |

Traced into rules above: M-10 (real recordings for vehicles; keep UI and voice readable over engine beds);
M-11 → S-116; M-13 → S-117; M-21 → S-100 hook; M-40 → S-108, S-109 (Roblox has no HDR: use priority ducking);
M-41 (HDR bus −12 to −18 dB) → S-118; M-42 → S-107, S-109, S-93; M-43 → S-115; M-45 → S-114; M-47 → S-105;
M-54, M-88 → S-120; M-55 → S-119; M-58 → S-138; M-68, M-69 → S-122; M-76 → S-213; M-93 → S-221.

## E. Gaps

| ID | Gap | In-house test |
| --- | --- | --- |
| G-10 | How Roblox's volume chain and device volume shift the H.872 target | 10-min loopback captures of the game and 5 top Roblox games on PC and phone; measure LUFS and LRA |
| G-08 | Headphone vs speaker share of players | In-game one-tap question or a settings toggle (no known output-device API, unverified) |
| G-09 | Mobile share of sessions | Creator Dashboard analytics by platform |
