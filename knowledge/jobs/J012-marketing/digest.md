---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J012 G1
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J012 G1)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G1 for J012 (`job-card.md`, `brief.md`) | approve / change | approve | waits for your answer |
| 2 | When J012 runs. J005, J008, J009, J010, J011 are open and J007 waits for G1 | (a) start extraction, fact-checks and the tool now; hold the G2 test until a slot is free; (b) wait | (a): steps 2-5 are mostly Sonnet work | (a) |
| 3 | Thumbnail check. `look_check.py` already has `thumb` (resample to the real size, then value and silhouette) and `value` (subject vs surround contrast) | (a) a thin wrapper `tools/art/thumb_check.py` over `look_check.py`: icon and thumbnail at the real Roblox display sizes, one contact sheet (small preview next to the title, grayscale, text hidden), subject/surround value contrast, count and size of separate subjects as the "one clear moment" measure; tests; (b) no new code, the skill only says which `look_check` commands to run | (a): one command before every owner review, and one sheet for you to look at. Limit: "one clear moment" is only partly measurable; the agent's own look at the sheet stays a step | (a) |
| 4 | Skill names | `marketing-design` + `marketing-craft` (kit pattern), or `game-marketing` + `marketing-craft` | `marketing-design` + `marketing-craft` | `marketing-design` + `marketing-craft` |
| 5 | "Test with Roblox's testing tools". The paper says only thumbnails have a native tool, and it is an adaptive bandit, not an A/B test; it warns that games under about 1,000 DAU may get no clear result. One icon shows per locale; titles have no native test, so a rename is a before/after observation. (Fact-checkers confirm this live) | (a) thumbnails: personalization with 2-5 distinct concepts; titles and icons: a comprehension check before launch plus a logged change read with the analyst, labelled "observational"; (b) the same, plus you name people for comprehension checks | (a); the agent never calls a result a "winner" without the analyst's denominator and cohort | (a) |
| 6 | Effort for the Sonnet helpers (extract, fact-check, grade) | high / medium | high, as in J004, J009 | high |
| 7 | G2 test subject | (a) the game you pick from the J003 pitch set (G2 sent 2026-10-21): title candidates, icon, 3 thumbnails, page draft, launch timeline; (b) a kit test game from a one-page brief; (c) your choice | (a): a real hook gives a real test; if no pick by G2, (b) | (a), else (b) |
| 8 | Art-bible families. The kit has `icon` for flat UI icons, which is a different job from a game icon | add `thumbnail` (16:9 key art of a real moment, world lock) and `game-icon` (square, world lock); ChatGPT draws 3:2 or square, so thumbnails are drawn wide and cropped to 16:9 with the subject in the safe area | add both | add both |
| 9 | Analyst and live-ops-designer are planned, not built | the marketing agent uses the `analytics` skill and writes the hand-off briefs; the lead holds tickets until each role exists | as stated | as stated |
