---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J003
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J003 lessons (build the game-designer agent)

| # | What | Worked / failed | Lesson |
| --- | --- | --- | --- |
| 1 | 4 Sonnet-high extractors split by paper section, each with a "claims to fact-check" and "weak spots" list | worked | The weak-spot lists found the paper's internal contradictions (status words, fix-ranking lists, missing table columns) before skill writing; keep both lists in every extraction brief |
| 2 | 2 fact-checkers split Roblox vs industry, working from the extractors' claim lists | worked | 126 claims checked: 109 confirmed, 1 corrected (Kid Icarus wager), 12 partly, 4 unverified, 0 contradicted. Owner papers were strong; the checks mainly narrowed scope (peak vs daily, appendix vs main result) |
| 3 | Hidden test kept in the job folder (`hidden-cases.md`) | failed partly | The G2 pitch agent ran `head` on every job-folder file and saw one held-out answer key. Hidden keys need a name rule (`hidden-*`, never opened) in the role, or a home outside agents' listing paths |
| 4 | Skill said "independent critic in a separate subagent" | gap | The game-designer role has no Agent tool. Skills must give the fallback for roles that cannot spawn agents (separate pass from a file + lead re-runs) |
| 5 | Parallel chats (J004 trend-scout, reference-images, J005 character-rigger) changed `rules/messages.md` and `AGENTS.md` mid-job and ran the sync tool | handled | Check `git status` before the skill-writing step and again before sync; align hand-offs with roles being built in parallel (J004 skill names) |
| 6 | Owner corrections, word for word | — | "run all the Sonnet models on high" · "make sure that the game designer, whenever it's used, is automatically set to Opus on high effort" |
