---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J012; owner's marketing paper, title checklist (knowledge/reference/marketing/03-launch-measurement-policy-process-templates.md §6.1 TP-TITLE); hook check (game-concept references/hook-promise.md §4)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Title checklist: <game> · candidate "<title>" · <date>

Workflow: `marketing-design` (what makes a title work), `marketing-craft` (how to test it). One copy per title candidate, in `knowledge/jobs/<job>/marketing/titles/`. The marketing agent fills it; the game designer checks items 1-3 against the build; the owner resolves any FAIL they want to keep.

**Rule of use.** Every item is PASS or FAIL with the named evidence. A FAIL blocks this candidate until it is fixed or the owner resolves it (decision id). A missing piece of evidence is FAIL, never "probably fine". All items PASS means **fit for testing**, not "this title will work": no source gives an optimal title length, word count, emoji count or update-tag lift for Roblox.

## A. Candidate
| Key | Value |
| --- | --- |
| title (exact characters, including any emoji) | |
| paired description, first sentence | |
| paired icon / thumbnail ids | |
| build version the title describes | |
| player fantasy (one line, from the vision record) | |
| what a new reader should picture (one line) | |
| languages | |

## B. Pass or fail
| # | Pass when | Evidence (file, capture, decision id) | Result |
| --- | --- | --- | --- |
| T1 | The title names a recognizable fantasy or action, not only a genre word | a plain-language line of what the player does in the released build | |
| T2 | Every promise in the title is playable in the version it advertises | a capture or build reference of the promised action; promise-ledger claim id | |
| T3 | Curiosity is answered by gameplay, not by a misleading image | one line: the reveal, and when a new player reaches it (minutes, from a playtest or capture) | |
| T4 | The title and the images tell of the same game | side-by-side sheet: title, icon, thumbnail, first playable objective | |
| T5 | It is distinct without copying another game's name | similarity search (Roblox search + charts, date) and a written naming reason | |
| T6 | Any brand, character or licensed word has cleared rights | the owner's rights record: scope, territory, expiry; or "no licensed terms" | |
| T7 | It reads on the real surface | captures of the candidate in the current Roblox phone and desktop interface (tile and game page) | |
| T8 | Any update tag (for example "UPDATE") names a real, current change | release id, and when the tag comes off | |
| T9 | Each translation keeps the meaning and adds no unintended claim | review of the whole title + paired image per language, by whom | |
| T10 | The test has a unit and an outcome | the analyst's spec: surface, metric with numerator and denominator, cohort, window, what stays unchanged | |
| T11 | Unfamiliar readers say the action back | comprehension check: who (age band, not names), how many, the exact question, their words; misreadings listed | |
| T12 | Roblox metadata rules hold: no repeated words or phrases, no keyword stuffing, the genre matches the gameplay, no giveaway or free-Robux bait | live publishing page read on <date> (`marketing-craft` references) | |

## C. Result
| Key | Value |
| --- | --- |
| verdict | fit for testing / blocked (items) |
| owner decision id (if a FAIL is kept) | |
| how it will be tested | comprehension check before launch; after launch a logged rename read with the analyst, labelled **observational** (Roblox has no native title or icon test: searched 2026-10-21, `marketing-design/references/discovery-promise.md` §2; re-check the docs) |
| previous title + date (for rollback and for the change log) | |
