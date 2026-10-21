---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J008 G1
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J008 G1)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G1 for J008 (`job-card.md`, `brief.md`) | approve / change | approve | waits for your answer |
| 2 | When J008 runs. J002-J005 and J007 are open; the company limit is 2 concurrent L jobs | (a) start extraction and fact-checks now, run the G2 test after J007's modeler exists; (b) wait until J005 and J007 close | (a): step 2 is cheap Sonnet work; the test stage can place stand-in blocks until the modeler exists | (a) |
| 3 | Who builds what between the environment designer and the modeler | (a) environment designer: one-off place geometry (blockout, terrain, landforms, cave shells), kit assembly, light, air, ambience, placement; modeler: every reusable asset; (b) modeler builds all meshes, environment designer only assembles | (a): it matches "it builds in Blender" and keeps the modeler on assets that repeat | (a) |
| 4 | Who writes the small runtime that blends ambience zones in a place | (a) the environment designer places zone volumes and points; a builder (feature-builder, planned) writes the runtime once per game; (b) the environment designer writes it | (a): game code stays with code roles; the map and the zones stay data | (a) |
| 5 | G2 test | A: a 3-zone slice (swamp, waterfall, cave, high ridge) at high effort; B: one fix on it at medium effort. Or name a stage from your game | A + B as proposed: they use your own examples and test both effort levels | A + B |
| 6 | Effort for the Sonnet helpers (extract, fact-check, grade) | high / medium | high, as in J004, J005 and J007 | high |
| 7 | Studio and Blender for G2 | open a separate Studio test place and Blender with the MCP add-on when the test starts | yes; tests never touch a live game place (J005-D6 pattern) | the lead asks you when the test starts |
