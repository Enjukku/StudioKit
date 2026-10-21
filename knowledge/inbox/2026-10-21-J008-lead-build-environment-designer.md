---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J008
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J008 lessons (build the environment-designer agent)

| # | What | Worked / failed | Lesson |
| --- | --- | --- | --- |
| 1 | 3 paper extractors by line range + 1 first-game extractor, each with "claims to fact-check" and "contradictions" sections; 3 fact-checkers split lighting / audio / performance-import | worked | 160 claims checked, 2 corrected (AudioFader Volume 0-10 not 0-3; `MeshStreamingAndImprovedLods` spelling), 0 contradicted. Split fact-checkers by engine area, not by note, so each reads one docs region |
| 2 | Owner asked mid-job for real Roblox look-development ("ambience lighting haze ... changing the skybox"); one Sonnet-high researcher read the docs mirror incl. Roblox's own showcase projects | worked | The paper alone gave checked facts but little craft. A docs-only look-dev pass (control map, Roblox scenes, skybox, runtime changes, open look-lab questions) is worth adding to any visual-role build |
| 3 | Fact-check found a wrong value in an existing kit skill (`sound-design` AudioFader 0-3) | worked | Ask fact-checkers for a "conflicts with existing kit skills" section; fix those in the same job |
| 4 | Hidden test: the held-out paper section (AI-built defects) was extracted into reference note 03, which the tested agent was allowed to read | failed | 5 of 8 hidden passes were lookup-assisted (grader). When a held-out set comes from the owner's paper, the extractor must write it to a separate `hidden-*` file in the job folder, never into `knowledge/reference/`; the test brief must name every forbidden file |
| 5 | The clean hidden signal (3 first-game failures) passed 1 of 3: the agent found one cause and one generic repair where the real fault had several parts | gap, fixed | Skills now require listing every mechanism and measuring each before a repair (`review.md` §6), plus a diagnosis table. Next test needs fresh held-out cases |
| 6 | A subagent stored its agent memory under the job folder (`knowledge/jobs/J005-.../.claude/agent-memory/`), which broke the KB lint gate | fixed | Subagents launched from a job folder can write project memory in the wrong place; the lead moved it to `.claude/agent-memory/<role>/`. Check the gate after every wave |
| 7 | Owner corrections, word for word | — | "Just make sure you run the agents." · "make sure we understand how to do ambience lighting haze, so on and so forth properly for the Roblox engine to get a good environment whether it's changing the skybox or whatever" · "You can look at the Roblox documentation to get an understanding." · "I don't feel like testing right now ... we're going to do a test by making doing a project that goes through the entire workflow ... So for now, just fix the current mistakes" |
