---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J014; owner's live-ops paper §7 patch notes template + communication sequence (knowledge/reference/live-ops/02 §communication); J014-D4 (live-ops writes the facts, marketing the voice, owner publishes)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Patch notes (facts draft): <update name> · <version>

Workflow: `live-ops-craft` (communication). The live-ops designer fills this with **facts only**, from the shipped build. Marketing turns it into the player-facing voice. The owner publishes (J014-D4). Copy to `knowledge/jobs/<job>/live-ops/patch-<version>.md`.

**Rule of use.** Every line matches the build that is live, with shipped values, not planned values. No "all lag fixed", no fix date that nobody estimated, no exploit steps, no player names or personal data. "You asked, we did" only where the feedback sort links the theme to this change. Unbuilt optional scope never appears.

## Fact sheet (for marketing and the owner)
| Field | Value | Source (build, config version, decision id) |
| --- | --- | --- |
| update name, version, release time + time zone | | |
| player-facing summary: what is better or newly possible | | |
| who can play, how to enter (requirements, place) | | |
| event dates: start; gameplay end; separate reward-claim end | | |

## Notes (draft order)

**New content**
- <addition; where it is; limits that matter>

**Balance and progression**
- <old value → new value, from the shipped data table>
- <why it changed; which situations; uncertainty if any>
- <currency or reward migration; purchase effects; the path for returning players>

**Quality-of-life and fixes**
- <player-visible problem that is now resolved>

**Known issues**
- <scope; a safe workaround if any; when the next status update comes; no invented fix date>

**From your feedback**
- <theme (distinct authors, source, window) → verified problem → change, or the decision to wait and why>

**What to expect next**
- <approved next beat ("now") or investigation ("exploring"); label which is a commitment>

**Feedback route**
- <in-game feedback route for everyone; community channels only where the current age rules allow; no personal information>

## Checks before hand-off to marketing
| # | Check | Result |
| --- | --- | --- |
| P1 | every value matches the shipped build or config version named above | |
| P2 | every date has a time zone; gameplay end and claim end are separate | |
| P3 | each "from your feedback" line links to a feedback-sort theme id | |
| P4 | no exploit steps, personal data, unestimated date or unbuilt scope | |
| P5 | the in-game route to the same information exists (Discord is never the only explanation); if the game has none, write "no in-game route" here and the plan lists it as a candidate fix | |
