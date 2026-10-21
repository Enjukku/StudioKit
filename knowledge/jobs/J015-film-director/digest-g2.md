---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J015 G2 (test J015-T09, gap fixes J015-T10 and lead edits)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J015 G2)

What to look at: `g2/boards/contact-sheet.png`, `output/J015-g2/movie/boss-reveal_r5_animatic_TEMPsound.mp4` (and `animatic_r5_frames.png`), `g2/review.md` §"The paper's plan next to mine".

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G2: is the film director directing well enough to continue to G3 (Roblox step + grader)? | approve / change (say what) | approve, with item 2 fixed first | waits for your answer |
| 2 | Shot E (the frame that hands control back) is too dark: whole-frame median WCAG luminance 0.0024 (`look_check.py value`, frame 175). The agent's review did not catch it; the skills now require a value check on key frames (gap G19) | (a) the agent relights E and re-measures, then the Roblox step; (b) leave it for the Roblox step | (a) | (a) |
| 3 | Hybrid: the paper's shot A (walk to the water) becomes play; only the deception is authored (4 shots, 5.8 s) | hybrid / fully authored with the paper's A | hybrid | hybrid |
| 4 | Shot D: static low wide (keeps beacon and explorer in frame 22/22 samples) or the paper's tilt (6/22, 0/22) | static / tilt | static, with an eye-glow brief to VFX | static |
| 5 | Music entry | on the strike in E / on the eyes in D / none until play | on the strike | on the strike |
| 6 | Studio for the Roblox step (also in `digest-g2-start.md`) | (a) open a second Studio, empty Baseplate saved as `FilmTest.rbxl`; (b) wait for J010-T14 to finish with TestBench | (a) | Roblox step waits |
| 7 | Evidence labels: `AGENTS.md` §3 has four (gate-verified, MCP-verified, owner-confirmed, not verified). Numbers from a script an agent writes in the task (Blender projections, frame measurements) fit none; the test agent called them gate-verified, which overstates | (a) add a fifth label "measured offline (script path)" to `AGENTS.md` §3 for every agent; (b) keep four; such numbers are "not verified (measured offline: script)" (what film-craft now says) | (a): it is honest and useful to every craft | (b) |
| 8 | Repeat attempts at the boss | no replay / E only / full with skip | no replay | no replay |

## Gaps fixed after the test (18 from the agent + 1 from the lead review)
| Gap | Fix | Where |
| --- | --- | --- |
| G1, G3, G4 | tool: props-only push for the first animatic; no "no drift" on UNKNOWN plans; cue markers round trip | `tools/film/shotlist.py` (J015-T10) |
| G2, G10, G11, G12, G13 | greybox stills as layout inputs when models are missing; lowercase image ids; a test art bible copy with a neutral world lock; prop-state and contact checks; regenerate as an edit, keep a reserve | `film-craft/references/storyboards.md`, `templates/film/storyboard-brief.md` |
| G5, G14 | static shots need a pose too; poses kept in the shot list, labelled unconverted, until the axis probe; greybox light traps | `film-craft/references/blender-previs.md` |
| G6 | script measurements labelled "not verified (measured offline)" | `film-craft` C-17; item 7 above |
| G7, G8, G19 | planning-stage review rows; phone proxy (safe frame, screen size, value contrast with `look_check.py`) | `film-craft/references/review.md`, `film-craft` step 8, C-18 |
| G9 | cuts on events; acting durations are proposals until the owner times them | `film-direction` D-13, `film-craft` step 5 |
| G15 | hybrid: the play beat's information becomes a level-design requirement | `film-direction/references/game-cinematics.md` |
| G16 | game profile gets play camera, supported displays and cinematic rate rows | `knowledge/design/game-profile.md` |
| G17 | one home for before/after state and the continuity ledger: `shot-table.md` | `templates/film/shot-list.md` |
| G18 | brief scope; lesson draft moved to the inbox | `knowledge/inbox/2026-10-21-J015-T09-film-director.md` |

## Usage (estimate vs actual)
| | Estimate (G1) | Actual |
| --- | --- | --- |
| Agents | 9 | 10 (4 extract, 3 fact-check, 2 tool, 1 test); grader not yet run |
| Models / effort | Sonnet high ×7; Opus medium ×1; Opus high ×1 + lead | Sonnet high ×7; Opus medium ×2; Opus high ×1 + lead |
| Images | 5-8 | 8 (5 panels accepted, 3 edit-regenerations) |
