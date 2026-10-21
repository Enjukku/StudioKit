---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J009 G1
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J009 G1)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G1 for J009 (`job-card.md`, `brief.md`) | approve / change | approve | waits for your answer |
| 2 | When J009 runs. J002, J003, J004, J005 are open and J007 and J008 wait for G1; the company limit is 2 concurrent L jobs | (a) start extraction, fact-checks and the tool now; hold the G2 tests until J003 G2 is answered; (b) wait until a slot is free | (a): step 2 is cheap Sonnet work; test A needs your pick from the J003 pitch set | (a) |
| 3 | Look checks to build | (a) the 4 you named (value, silhouette, palette, thumbnail); (b) the 4 + color-vision simulation (published matrices, a screen for "color is the only signal"; the paper supports it as a screen, not proof) | (b): rule 9 of the paper (never rely on color alone) needs it and it is small. Edge density stays out (the paper calls it unreliable for stylized art) | (a) |
| 4 | Skill names | `art-direction` (design) + `art-review` (craft), or `art-design` + `art-craft` (kit pattern) | `art-direction` + `art-review`: the names say what each book is for | `art-direction` + `art-review` |
| 5 | "Environment designer" in the hand-offs | the `environment-designer` role J008 is building (it replaces content-builder) | hand off to `environment-designer`; if J008 is not built when J009 finishes, the brief still names it and the lead routes the ticket | `environment-designer` |
| 6 | Effort for the Sonnet helpers (extract, fact-check, grade) | high / medium | high, as in J004, J005, J007 | high |
| 7 | G2 test B subject | (a) J002 UI tests + J007 test models; (b) Studio captures of a first-game stage (read-only); (c) your choice | (b) if a first-game place is open in Studio: a real busy scene tests hierarchy best; else (a) | (a) |

# Decision digest: 2026-10-21 (J009 G2)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G2 result (`grades-g2.md`, `art/test-b/`, `output/art-direction/j009-t10/`) | accept and go to the direction test / run another review first | accept: diagnosis and measurement are strong (hidden cases 29/30, 0 false claims); grading was 2 steps too kind and is now calibrated to your grades (J009-D6) | waits for your answer |
| 2 | Direction test (test A) needs a concept | (a) your pick from the J003 pitch set; (b) the game designer's recommended pitch; (c) a concept you name | (a); it also gives the first real check of the new grade calibration | (b) |
| 3 | Anchors steer only shape today (`art_refs.py` tells the image model not to copy an anchor's light or rendering) | (a) keep: look comes from lock text; (b) add an optional `purpose` per anchor so palette, light or material anchors can steer those | (b), small tool change with tests, in a follow-up ticket | (a) |
| 4 | Marketing art from the image tool: may icons and thumbnails ship as final images? (`reference-images` says images are never the final asset) | yes for marketing only / no | yes for marketing only, with `store-icon` and `key-art` families in the art bible | no |
| 5 | Image record: add `model: not exposed` and the route to each generated image's record (the Codex image tool does not say which model version drew an image) | yes / no | yes (tiny, testable) | yes |
| 6 | The 2 vfx-design gaps found in the test (persistent state effect; pickup lying among debris) | route to the vfx-designer skill owner / leave | route as a follow-up | route |
