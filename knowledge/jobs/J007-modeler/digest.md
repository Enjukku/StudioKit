---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J007 G1
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J007 G1)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G1 for J007 (`job-card.md`, `brief.md`) | approve / change | approve | waits for your answer |
| 2 | When J007 runs. J002, J003, J004 and J005 are open; the company limit is 2 concurrent L jobs | (a) start extraction and fact-checks now, hold the G2 tests until J005's rigger exists; (b) wait until J005 G3 | (a): step 2 is cheap Sonnet work and reuses J005's fact-checks; test B is better with the real rigger | (a) |
| 3 | How the modeler reaches Tripo | (a) you run Tripo Studio with the prompt pack the modeler writes and drop the files in a folder; (b) a small `tools/art/tripo.py` on the Tripo API, key in an environment variable, offline tests | (b) if you have or want a Tripo API key: the agent can then run the hero route alone; else (a) | (a) |
| 4 | G2 test subjects | A: a simple sword or pickaxe (hand-built, medium). B: a hero pet or creature (Tripo, high). Or name your own | A + B as proposed: they test both routes and both effort levels | A sword, B a small pet |
| 5 | Style for the test references (no game art bible in the kit) | (a) the art-bible template's starter locks; (b) one of your game's art bibles | (a): kit tests stay game-neutral | (a) |
| 6 | Effort for the Sonnet helpers (extract, fact-check, grade) | high / medium | high, as in J004 and J005 | high |
