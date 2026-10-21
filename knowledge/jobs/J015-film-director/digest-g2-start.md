---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J015 step 6 start
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J015 G2 start)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | Studio for the G2 Roblox capture. The only open Studio is `TestBench.rbxl`, which belongs to the engineering job (J010-T14, performance scenarios); driving it from this job could spoil those measurements | (a) you open a second Studio with an empty Baseplate place saved as `FilmTest.rbxl`; the film director plays the boss-reveal timings there with a throw-away probe script and captures them; (b) wait until J010-T14 is done, then use TestBench; (c) skip the Roblox capture for G2 and show only boards + animatic | (a): the Roblox step is the one the paper cannot prove from Blender | the Roblox step waits; G2 shows boards + animatic, Roblox marked "not run" |
| 2 | Job number: this job was opened as J013 at the same moment as the analyst job (J013-analyst) and the live-ops job (now J014). Renamed to J015; ticket and decision ids keep their numbers (J015-T01..T09, J015-D1..D7) | info | — | — |

## Usage so far (estimate vs actual)
| | Estimate (G1) | Actual |
| --- | --- | --- |
| Agents | 9 | 9 so far (4 extract, 3 fact-check, 1 tool build, 1 test running); grader not yet run |
| Models / effort | Sonnet high ×7; Opus medium ×1; Opus high ×1 + lead | Sonnet high ×7; Opus medium ×1; Opus high ×1 (test) + lead |
| Images | 5-8 | test running (max 8) |
