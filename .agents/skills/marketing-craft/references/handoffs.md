# Hand-offs: marketing and the roles it works with

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `marketing-craft`. Format: `rules/messages.md` §2 (brief) and §3 (hand-back). Owner J012 brief 2026-10-21: marketing works from the start with the game designer, trend scout, art director and analyst; hand-offs also to the live-ops designer. The other sides: `preproduction/references/handoffs.md` §3.2 (game designer → marketing), `trend-scan/references/handoffs.md` §2 (trend scout → marketing), `art-review/references/feedback-briefs.md` (art director → marketing).

Marketing sends **files, not chat**. Asks to another role are tickets in the job ledger, inside the approved brief. A role marked *planned* does not exist yet: the brief goes to the lead, who holds it (J012-D6).

| To | When | Marketing asks for | Marketing never asks for |
| --- | --- | --- | --- |
| game-designer | concept and preproduction step 1; each new feature that marketing will show | the promise ledger (which claims are playable now), the signature moment and when a new player reaches it, the audience, what is not built yet | a feature added only so an ad can show it |
| trend-scout | before title and thumbnail work; weekly | dated, labelled signals on audience words, title and thumbnail patterns, timing, rights flags | creative wording; a number without its label |
| art-director | before any image; for every image before the owner | the art bible with the `thumbnail` and `game-icon` families, approved anchors, a review of each candidate at real size | the message or the title (marketing owns them) |
| analyst *(planned)* | before every test and launch; weekly | the test spec (decision, metric label, denominator, cohort, window, guardrails), readings of results | a "winner" without counts |
| live-ops-designer | update and event planning; week 3 after launch | the calendar of real playable changes, event ids, dates, what is new for returning players | a hype message for a change that is not live |

## 1. Marketing → game-designer (promise check)
```text
<intent>
We are preparing the title, icon and Home thumbnails for <game>. Each must show a moment a new player really reaches, so the people who click enjoy what they find. I need to know which promises are playable in the launch build and how fast a new player meets the signature moment.
</intent>
<spec>
id: <job>-T<nn>
from: marketing
to: game-designer
model: opus
effort: high                                  # game-designer, owner J003-D3
skills: [game-concept, preproduction]
refs:
  - knowledge/jobs/<job>/marketing/titles/    # take: the title candidates and the claims each makes
  - knowledge/jobs/<job>/marketing/briefs/    # take: the moments each image concept shows
fixed:
  launch_build: <version>                     # owner / release plan
  claims_to_check: [<claim ids from the promise ledger, or "new: <text>">]
open: [how you check each claim (playtest, capture, build notes)]
avoid: [adding a feature so that a marketing claim becomes true; changing the promise ledger without the owner]
owns: [knowledge/design/promise-ledger.md (yours)]
not_in_scope: [title wording, image composition]
rules:
  - A claim is "playable" only if ordinary play in the launch build reaches it; give the time or path a new player takes.
  - Planned or cut claims stay out of present-tense marketing.
  - Never name a file report*, summary*, findings* or analysis*.
deliver: the promise ledger rows for each claim id, status playable / planned / cut, with the evidence
checks:
  - C1: every claim id in claims_to_check has a status and evidence
return: hand-back to marketing (rules/messages.md §3)
</spec>
```

## 2. Marketing → trend-scout (signals for packaging)
```text
<intent>
We are naming and packaging <game> (<one-line fantasy>). I need the words and images its audience uses now, which title and thumbnail patterns are rising or saturated in its genre, and timing risks, with dates and labels, so we stand out without copying anyone.
</intent>
<spec>
id: <job>-T<nn>
from: marketing
to: trend-scout
model: sonnet
effort: medium                                # trend-scout roster
skills: [market-trends, trend-scan]
refs:
  - knowledge/design/game-profile.md          # take: genre, audience, fantasy
fixed:
  genre_and_loop: <loop line>                 # game designer's vision record
  window: <dates>                             # launch timeline
open: [which sources, which comparison games]
avoid: [revenue or playtime estimates presented as facts; competitor art or names as material to reuse]
owns: [the scout's own pages]
not_in_scope: [title wording, image making]
rules:
  - Every number keeps its label (OFF, 3P-S, 3P-E, DEV, DER, MAN, UNKNOWN) and date.
  - Rights flags on any branded or franchise term.
  - Legal-only sources (trend-scan source registry); no scraping.
deliver: a dated section with audience words, title and thumbnail patterns (rising / saturated, evidence), timing risks, rights flags
checks:
  - C1: each pattern has a source, a date and a label
return: hand-back to marketing, copy to lead
</spec>
```

## 3. Marketing → art-director (art lock and review)
```text
<intent>
I need the icon and Home thumbnails for <game> to look like the game the player will get, and to read at the size players see them. Please confirm the marketing families and anchors in the art bible, then review the candidates at real size against in-game captures before the owner sees them.
</intent>
<spec>
id: <job>-T<nn>
from: marketing
to: art-director
model: opus
effort: high                                  # art-director, owner J009-D1
skills: [art-direction, art-review, reference-images]
refs:
  - knowledge/jobs/<job>/marketing/briefs/<brief>.md          # take: the message and the moment
  - content/art/refs/thumbnail/ and content/art/refs/game-icon/   # the candidates
  - <capture paths>                                            # the in-game proof of each moment
  - <thumb_check sheets and JSON>                              # measured small-size read
fixed:
  small_sizes: icon 150x150 (Roblox icons doc); thumbnail <WxH> (capture <id>)
  art_bible_revision: <rev>
open: [direction notes, which candidates to keep, lock or anchor proposals for marketing art]
avoid: [rewriting the message or the title; approving anything for the owner]
owns: [your review file in knowledge/jobs/<job>/art/]
not_in_scope: [making the final images]
rules:
  - The owner approves every lock, anchor and final image.
  - Marketing art may dramatize the fantasy but never shows another game (art-direction platform-evolution-marketing §3).
deliver: ranked findings per candidate, with acceptance evidence
checks:
  - C1: each candidate reviewed at its real small size next to its capture, or marked NOT REVIEWED
return: hand-back to marketing (rules/messages.md §3)
</spec>
```

## 4. Marketing → analyst (planned; to the lead until built)
```text
<intent>
We want to learn whether <change> brings players who enjoy <game>, not only more clicks. Please define the test before it starts, so the result can be read honestly.
</intent>
<spec>
id: <job>-T<nn>
from: marketing
to: analyst (planned: lead holds)
model: sonnet
effort: medium                                # analyst roster
skills: [analytics]
refs:
  - .agents/skills/marketing-craft/references/testing-measurement.md   # take: §1 test types, §2 spec fields
fixed:
  change: <thumbnail set v2 / title rename / ad creative set>          # campaign record
  tool: <personalization / none (observational) / Ads Manager>
  start: <date>
open: [metric choice inside the dashboard, windows, guardrails, sample judgement]
avoid: [calling adaptive allocation an A/B test; mixing ad and organic cohorts]
owns: [the test spec file]
not_in_scope: [creative choices]
rules:
  - Exact dashboard labels (qPTR vs PTR); counts beside rates; immature cohorts "pending".
  - Mark 2026-10-12 (Roblox recording change) in any window that crosses it.
deliver: the test spec (testing-measurement §2 fields) and, at the read date, the reading
checks:
  - C1: decision, metric, denominator, cohort, window, guardrails and disconfirming result all filled before start
return: hand-back to marketing, copy to lead
</spec>
```

## 5. Marketing → live-ops-designer (its side: `live-ops-craft/references/handoffs.md` §6)
```text
<intent>
Players come back for a real new reason. I need the update and event calendar so announcements, notifications and thumbnails match what is really live, on the day it is live.
</intent>
<spec>
id: <job>-T<nn>
from: marketing
to: live-ops-designer
model: opus
effort: medium                                # live-ops-designer roster
skills: [live-ops-design, live-ops-craft]
fixed:
  window: <dates>
  limits: Roblox update announcements 60 characters, once per 3 days; up to 10 ongoing or upcoming events; personalized notifications 13+, one per user per day per game (read <date>, marketing-design channels §4)
open: [which changes and events, their dates]
avoid: [announcing anything not live in the build on the date]
owns: [the live-ops calendar]
not_in_scope: [message wording, images]
rules:
  - Each item has a build version and the date it is live.
deliver: calendar rows: id, what is new for players, build, live date, event id if any
checks:
  - C1: every row has a build version and a live date
return: hand-back to marketing, copy to lead
</spec>
```

## 6. What marketing hands back
To whoever asked (usually the lead or the game designer), in `rules/messages.md` §3: STATUS, coverage of every item in scope, evidence (sheets, JSON, captures, decision ids), decisions made, owner actions needed (upload, activate, publish, spend: the owner does them), and the next decision with its default.
