> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-20. Kit reference: universal (J004). Format: `rules/messages.md` §2 (brief) and §3 (hand-back). The game-designer side of this exchange: `game-concept/references/idea-method.md` §2 and `preproduction/references/handoffs.md` §3.1.

# Hand-offs from the trend scout

The scout sends **files, not chat**: the weekly page and the opportunity cards live in files; the message points to them. Two readers: the **game-designer** (in kit) and **marketing** (role `marketing`, J012).

| To | When | What they get | What they never get |
| --- | --- | --- | --- |
| owner + game-designer | every week; at once on a breakout flag that passes the gates | weekly page (Markdown + HTML), top 3 cards with the 9 record fields | a game design, a pitch, a green light |
| marketing | every week, section "outside trends" and "rising games" as it bears on titles, thumbnails and timing; on request | trend signals on promises, title and thumbnail patterns, timing windows, audience vocabulary, rights flags | creative wording or art; marketing decides execution |
| analyst | never by default | — | own-game player data stays with the analyst; the scout only reads public and licensed market data |

## 1. Weekly hand-off to the game-designer

```text
<intent>
This week's market scan is ready. It shows which Roblox games and loops are rising with dated, labelled numbers, which outside trends may move into Roblox, and up to 3 research opportunities written as "proven loop + new theme + twist".
Use the cards as evidence for "why now" in your pitches; they are research priorities, not approvals.
Read section 1 (3 sentences) and section 2 (cards) first; the tables after them are the evidence.
</intent>
<spec>
id: <job-id>-T<nn>
from: trend-scout
to: game-designer
model: opus
effort: high                     # game-designer role, owner J003-D3
skills: [game-concept, market-trends]
refs:
  - <TREND_DATA_DIR>/pages/trend-week-<YYYY-MM-DD>.md     # take: cards O1-O3, rising games, loop families; avoid: treating 3P-E numbers as facts
  - <TREND_DATA_DIR>/pages/trend-week-<YYYY-MM-DD>.html   # take: charts of the watchlist history
  - <previous week's page>                                 # take: section 7 (what changed or was wrong)
fixed:
  week_ending: <YYYY-MM-DD>                     # this scan
  data_coverage: <% per window>                 # trends tool output
  record_fields: [observation date, rising player behaviour, audience, evidence (source, metric, date), comparison period, outside trigger, alternative explanation, proven loop, lasting or temporary]   # game-concept idea-method §2
  number_labels: [OFF, 3P-S, 3P-E, DEV, DER, MAN, UNKNOWN]   # market-trends §labels
  rights_flags: <card id: pass / HOLD / fail>   # market-trends copying-and-rights
open: [which cards to pitch from, themes, twists, fantasy, title]
avoid: [quoting a 3P-E revenue or playtime number as a fact, using a HOLD card's branded theme, calling a 24h/7d momentum ratio "weekly growth"]
owns: [knowledge/design/concepts/ (the game-designer's own files)]
not_in_scope: [changing the scan, its numbers or its labels; asking the scout to design]
rules:
  - Every number keeps its label and date when you reuse it; UNKNOWN stays UNKNOWN.
  - Cards are research priority, not build approval; the owner decides.
  - HOLD means the branded or copied version may not be used; an original design on the same abstract loop may continue.
  - Anything players buy, roll, trade or watch follows platform-policy.
  - Questions about a number go back to the trend-scout as a ledger ticket, with the claim ID from the evidence ledger.
  - Never name a file report*, summary*, findings* or analysis*.
deliver: hand-back only if you use or reject a card: card id + used / rejected + one-line reason (feeds the scout's performance table)
checks:
  - C1: each card you use is cited by card id and week in your concept record
return: hand-back to trend-scout (rules/messages.md §3), copy to lead
</spec>
```

## 2. Hand-off to marketing

```text
<intent>
Marketing makes titles, icons, thumbnails, the store page and ads that make players think "I need to do that".
This scan shows which promises, title shapes, thumbnail patterns and outside themes are drawing players now, and how long they may last, so marketing can test variants against what is current rather than what was current last season.
The signals are evidence for your tests, not wording or art to copy.
</intent>
<spec>
id: <job-id>-T<nn>
from: trend-scout
to: marketing
model: opus
effort: medium                   # roster: marketing → Opus medium (J012-D1)
skills: [marketing-design, marketing-craft, market-trends]
refs:
  - <TREND_DATA_DIR>/pages/trend-week-<YYYY-MM-DD>.md   # take: §3 rising games (titles, thumbnails seen), §5 outside trends, §8 rights flags
  - .agents/skills/game-concept/references/hook-promise.md   # take: the hook and title tests
fixed:
  week_ending: <YYYY-MM-DD>
  signals: <list: title pattern / thumbnail pattern / theme / meme / song / event, each with platform, exact ID, dated measure + label>
  windows: <per signal: rising / peaking / fading, with the dates it rests on>
  rights_flags: <per signal: pass / HOLD / fail>      # market-trends copying-and-rights
open: [which signals to test, wording, composition, variants]
avoid: [other games' names, characters, logos or thumbnail art; a song or sound without a licence; a meme character as a mascot; promising gameplay the game does not have]
owns: [knowledge/jobs/<job-id>/marketing/]
not_in_scope: [the game's design, paid ad buys, posting or publishing anything]
rules:
  - A trend's popularity grants no right to its name, character, song or art; HOLD signals are not used.
  - Thumbnails and videos show the real game (Roblox thumbnail rules, platform-policy).
  - No inferred ages or personal data of viewers; creators are named by exact channel ID only.
  - Numbers keep their labels and dates.
  - Never name a file report*, summary*, findings* or analysis*.
deliver: hand-back with the signals used and the test results, when tests run
checks:
  - C1: every variant that uses a signal cites the signal ID and its rights flag = pass
return: hand-back to trend-scout and lead (rules/messages.md §3)
</spec>
```

## 3. Asks into the scout (from the game-designer or the lead)
The game-designer's ask format is `preproduction/references/handoffs.md` §3.1: question, audience, comparison period, loop families, the 9 record fields. Answer with `knowledge/jobs/<job-id>/trend-scout/opportunities.md` and a §3 hand-back. Not in scope for the scout: writing concepts, judging fun, buying data, creating accounts.
