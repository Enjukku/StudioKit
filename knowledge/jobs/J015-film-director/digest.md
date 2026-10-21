---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J015 G1
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J015 G1)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G1 for J015 (`job-card.md`, `brief.md`) | approve / change | approve | waits for your answer |
| 2 | Shot-list script. The paper supports it: one shot id across boards, previs and Roblox; one interval rule `[start, next-start)` (frames 1-31 at 30 fps are 31 frames, not 1 s); exact frame rates as fractions; a script can find missing ids, gaps, overlaps and missing cues, but cannot judge whether a cut works | (a) one data file per sequence (`<sequence>.shots.json`) + `tools/film/shotlist.py`: `check` (ids, gaps, overlaps, cue references, UNKNOWN allowed only before previs lock), `table` (Markdown shot list for people), `blender` (camera markers and frame range for the animatic) and `blender-diff` (reads the animatic back, reports drift), `luau` (data module for Roblox playback); offline tests; (b) Markdown shot list only, no script | (a), small: no camera-path export to Roblox unless the G2 test shows it is needed | (a) |
| 3 | Who writes the Roblox cutscene player code (camera timeline, cues, skip, every exit, clean-up). Kit craft roles do not write game code; the paper puts camera ownership, authority and clean-up with engineering | (a) the film director writes the scene data and the playback contract (exits and tests from the paper) and checks the result in Studio; a reusable kit cutscene player is a separate engineering job (architect → feature-builder → qa-lead), proposed as a follow-up; (b) the film director writes the player code too | (a). For the G2 test, a throw-away Studio probe plays the camera timings for capture; it is not shipped | (a) |
| 4 | Skill names | `film-direction` + `film-craft`, or `cinematic-design` + `cinematic-craft` | `film-direction` (what and why; read by animator, VFX, sound, UI too) + `film-craft` (how) | `film-direction` + `film-craft` |
| 5 | Storyboards. You asked for ChatGPT boards. The first game chose Blender stills with the real models instead, because AI images kept changing the cast and scale; the paper also says AI panels cannot prove geometry or continuity | (a) ChatGPT boards for intent and composition (one panel per request, approved references attached, continuity check per panel); once models exist, Blender previs stills are the spatial truth; (b) ChatGPT boards only | (a) | (a) |
| 6 | Effort for the Sonnet helpers (extract, fact-check, grade) | high / medium | high, as in J004, J009, J012 | high |
| 7 | G2 test subject. The earlier game's film never reached an animatic, so there is no finished example to compare with | (a) the paper's own 5-shot boss reveal (original, not game-specific; all its timings and lenses are UNKNOWN, so the agent must solve them): beat sheet, shot list, 5 boards, timed Blender animatic, Roblox playback capture of the same timings, self-review; shown next to the paper's plan; (b) a scene from a game you name | (a) | (a) |
| 8 | The animator role is planned (J006), not built | the film director writes animator briefs (acting intent per shot); the lead holds them until the role exists | as stated | as stated |
