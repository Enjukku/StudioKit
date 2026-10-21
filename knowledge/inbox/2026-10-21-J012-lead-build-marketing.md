---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J012 steps 1-5
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Lessons: building the marketing agent (J012, steps 1-5)

| # | What happened | Lesson | Evidence |
| --- | --- | --- | --- |
| 1 | The owner asked to "test titles, icons and thumbnails with Roblox's testing tools"; the fact-check found no native title or icon test, and thumbnail personalization is a bandit | Check what a named platform tool really does before the brief promises it; say it at G1 and give the honest substitute (comprehension check + observational log) | `fact-check-roblox-discovery.md` T04 answers; J012 digest item 5 |
| 2 | No Roblox doc states the phone tile size of a Home thumbnail | A small-size check needs a measured surface size, not a guess: the tool refuses a thumbnail size without a source, and the skill tells the agent to measure it from a phone capture | `thumb_check.py`; `image-pipeline.md` §2 |
| 3 | Reusing `look_check.py` by import made the marketing check 419 lines with 15 tests and no second copy of the maths | When a sibling role already has a measuring tool, brief a thin wrapper and forbid re-implementation with a check (grep) | J012-T07 hand-back C3 |
| 4 | Three fact-checkers split by source family (Roblox discovery, Roblox ads and policy, everything else) found 16 corrections and 15 unverified rows, and 6 stale lines in `platform-policy` | Split fact-checks by source owner, reuse earlier fact-check rows by id, and ask each checker for "kit skill updates needed" | FD, FA, FS tables; PU-1..6 |
| 5 | One paper sentence I put in a skill (YouTube "no minimum cadence") was later unverified | Write skill lines that cite numbers or platform claims only after the fact-check arrives; draft structure first | `marketing-design` M-03 edit |
| 6 | The image model garbles words; the paper wants approved text only | Lock text out of the image families and add approved title text afterwards in an editor | art-bible `THUMBNAIL LOCK`, `GAME ICON LOCK` |
