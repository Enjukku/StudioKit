---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J014-T08 hand-back (live-ops-designer, G2 test on the synthetic pack)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Skill gaps found in the G2 test (T08) and the fixes

| # | Gap (agent's words, short) | Fix | File |
| --- | --- | --- | --- |
| 1 | Urgent items: template says "not counted as themes"; tool and feedback-ops say they count | Routed at once **and** counted | `templates/live-ops/feedback-sort.md` rule + §B |
| 2 | No source for the Roblox rating-prompt export | `reviews` = Roblox built-in prompt export; `comments` = other public comments | `feedback-ops.md` §1 table; template §A rows |
| 3 | Rows with no author id | `anon-<file>-<row>`; "at most N authors"; denominator = rows | `feedback-ops.md` §1 |
| 4 | Staff posts | excluded and counted in a new "excluded" column | `feedback-ops.md` §1; template §A |
| 5 | Discord pseudonyms across channels and renames | per user id (stage 2 salted hash) else per display name across the export; map only in `FEEDBACK_DATA_DIR/keys/` | `feedback-ops.md` §1 |
| 6 | Ranking without scope estimates | label "pre-estimate"; no committed date | `process.md` §1b |
| 7 | Roles missing from capacity | "not yet reviewed" + ask the lead | `process.md` §1b |
| 8 | Analyst capacity too small | decision rule still written; cheapest read; else "unmeasured", owner decides | `process.md` §1b |
| 9 | Urgent harm with no agreed authority | ask the owner the same day with the compliant state as the recommendation; standing authority → owner digest item 12 | `process.md` §1b; `digest.md` |
| 10 | "Exploitable currency" undefined | ledger check (issued = spent + converted + held), source check, concentration | `process.md` §1b |
| 11 | Release-to-start gap, time gate | new row "release that carries the event" | `templates/live-ops/event-design.md` §B |
| 12 | Claim end when rewards are instant | `n/a: rewards granted instantly` allowed | `event-design.md` §B |
| 13 | Estimate brief skills for money / saves | + data-saving, platform-policy; + networking-security | `handoffs.md` §5 |
| 14 | No in-game report or news route | always-available "Report a problem" + a first-session prompt; P5 says "no in-game route" when missing | `evidence-feedback.md` §3; `feedback-plan.md`; `patch-notes.md` P5 |
| extra | Feedback plan's example prompt (after the 3rd round) misses early quitters | first-session prompt required | `feedback-plan.md` §3, §6 |

## Fixes from the grade (T09, 24.5 / 26)
| # | Weak point | Fix | File |
| --- | --- | --- | --- |
| G1 | Biggest silent problem got only "diagnose later"; the save-loss measure for an urgent item waited for the pick | urgent measurement goes to the analyst now; the biggest silent problem gets a cheap next step this period | `process.md` §2 step 8, §5 |
| G2 | Package option not totalled against free days; data-only assumption unconfirmed | total days per role across parts; list assumptions to confirm | `process.md` §2 step 7 |
| G3 | Entrance at a board most players never open | entrance row asks how many eligible players already pass it | `event-design.md` §C |
| G4 | Draft player message promised compensation | no compensation promise before the owner decides | `process.md` §5 |
