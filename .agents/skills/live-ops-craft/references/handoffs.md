> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `live-ops-craft`. Format: `rules/messages.md` §2 (brief) and §3 (hand-back). Owner J014 brief 2026-10-21: hand-offs to the analyst, game designer, progression designer, trend scout, marketing and the engineering team, in the brief format. The other sides: `analysis-craft/references/handoffs.md` §4 (analyst → live-ops), `marketing-craft/references/handoffs.md` §5 (marketing → live-ops), `trend-scan/references/handoffs.md`, `progression-craft/references/data-handoff.md`. Revised by J018 maker live-ops-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§1 craft rows, §3 tier placement, §4 promise and grey-box verdict, §6 event kit, new §9 to the art director).

# Hand-offs: who gets what from live-ops

Live-ops sends **files, not chat**: the update plan, the update brief, the event design, the feedback sort and the patch-notes fact sheet hold the content; each brief points to them. Every ask is a ticket in the job ledger, inside the owner-approved plan. New scope, crew or budget → `needs-decision` to the lead. Model and effort below come from each role's file.

## 1. Who, when, what
| To | When | Gets | Never ask them for |
| --- | --- | --- | --- |
| analyst | weekly intake; before release (measurement); after release (reading) | the hypothesis, cohort, exposure, primary outcome, guardrails, comparison, windows, decision rule; questions about denominators and silent cohorts | a "win" before the window closes; a cause the data cannot show |
| game designer | after the owner picks, for play | player promise, loop fit, activity constraints, acceptance criteria, edge cases, the question the update answers | a feature list dressed as finished design |
| progression designer | before ranking (feasibility) and after the pick (amounts) | effort distribution target, reward purpose, flows, ownership, catch-up, expiry and migration, monetization limits | a multiplier picked to "feel exciting" |
| trend scout | when an event or theme leans on a trend | the theme, the audience, the build-and-review lead time | "what's hot" without dates and rights |
| marketing | after the pick (calendar rows, fact sheet); the event kit when the build is credible (`event-review.md` §1); again when the build is live | calendar rows, benefit, audience, exact dates, eligibility, reward terms, channel limits, fallback wording; patch-notes fact sheet | wording for anything not live in the build on its date |
| engineering (architect for new systems; feature-builder for money, saves, remotes; quick-builder for table and config changes), via the lead | estimate request before ranking; build brief after the pick | scope, dependencies, interfaces, device limits, save and entitlement behaviour, exposure ids, safe-disable needs, event timing and rewards as config and data, acceptance criteria | a date before their estimate |
| art-director (§9) | the concept round of event-scope work (`event-review.md` top), before any production art | the promise, the target experience, the nearest existing themes, the variants and their base items, what fans want | a finished image before the theme is picked |
| vfx, sound, ui, environment, animation, modeling crafts, through the lead's job recipes | after the tier rows and the grey-box verdict | their row of the craft-ask table (`event-review.md` §1) with the capture they will be judged on | how to build it; a look that promises what the activity does not do |

## 2. Live-ops → analyst (measurement plan, before release)
```text
<intent>
We will ship <update> to fix <problem> for <cohort>. Before players see it, we must agree what result would mean it worked, what would mean harm, and what we will do in each case, so nobody reads the launch spike as success.
</intent>
<spec>
id: <job>-T<nn>
from: live-ops-designer
to: analyst
model: sonnet
effort: medium                                   # analyst role
skills: [analysis-design, analysis-craft]
refs:
  - knowledge/jobs/<job>/live-ops/plan-<date>.md     # take: rank-1 hypothesis, evidence, guardrails
  - knowledge/jobs/<job>/live-ops/brief-<decision id>.md   # take: scope, exposure, release dates
fixed:
  decision_id: <id>                              # owner decision, <date>
  release: <date, time, timezone>; build <version>; config <key/version or none>
  eligible_players: <definition>                 # brief
open: [comparison design (Experiment if a config gates it, else observational), windows, metric labels, guardrail margins]
avoid: [a verdict before the window ends; blending new, continuing and reactivated players]
owns: [the measurement plan file]
not_in_scope: [logging code (the analytics skill and engineering)]
rules:
  - Name the method label: randomized (Roblox Experiment), or observational (before/after, event chart).
  - Every rate shows its counts and denominator.
deliver: measurement plan (templates/analytics/ab-test-plan.md if an Experiment; else the update measurement brief in analysis-design experiments-updates §7)
checks:
  - C1: cohort, exposure, primary outcome, guardrails, comparison, windows and decision rule all filled, or the reason one cannot be measured
return: hand-back to live-ops-designer, copy to lead
</spec>
```

## 3. Live-ops → progression designer (feasibility, then amounts)
```text
<intent>
The owner chose <update / event>. Players must be able to finish <goal> through ordinary play, late joiners included, without flooding the economy or making old rewards worthless.
</intent>
<spec>
id: <job>-T<nn>
from: live-ops-designer
to: progression-designer
model: opus
effort: high                                     # progression-designer role
skills: [progression-design, progression-craft]
refs:
  - knowledge/jobs/<job>/live-ops/event-<slug>.md    # take: activity loop, dates, cohort, catch-up need
  - <analyst finding>                                # take: observed earning distributions, session opportunities
fixed:
  window: <start - gameplay end - claim end, timezone>   # owner decision <id>
  target_cohort: <cohort>                            # plan
  reward_purpose: <what the reward must make players feel or do>
  tier_table: <path to the game's reward-tiers.md, model revision>   # progression designer
open: [amounts, issuance range, sinks, expiry and conversion rules, catch-up mechanics]
avoid: [a multiplier chosen to look exciting; power that obsoletes old content; paid power as the fix for a spike the event created]
owns: [the event's economy section and tables]
not_in_scope: [the activity design (game designer), the dates]
rules:
  - Paid random items follow platform-policy §A (odds, PolicyService, every outcome a benefit).
  - Model alt accounts, automation, trading and stacked bonuses.
  - Every event reward is placed in the game's tier table; a new top-tier reward carries the same rarity proof as the core track (a re-simulated rate); no event celebration out-ranks the core track's top tier.
deliver: amounts, issuance range with assumptions, abuse cases, catch-up path, effect on existing ownership, the event's tier rows (tier, trigger, rate, text name)
checks:
  - C1: a player who starts at the median late-join day can finish through healthy play (show the trace)
  - C2: the event's tier rows pass the tier table's rate and order checks for every named policy (`reward-tiers.md` §8)
return: hand-back to live-ops-designer, copy to lead
</spec>
```

## 4. Live-ops → game designer (play spec after the pick)
```text
<intent>
<cohort> should <behaviour> because <mechanism>. The update must answer: <question>. It has to feel like this game, not a bolted-on mode.
</intent>
<spec>
id: <job>-T<nn>
from: live-ops-designer
to: game-designer
model: opus
effort: high                                     # game-designer role
skills: [game-design]
refs:
  - knowledge/jobs/<job>/live-ops/brief-<decision id>.md   # take: problem, hypothesis, player journey, new/returning/veteran paths
  - knowledge/jobs/<job>/live-ops/feedback-<date>.md       # take: the themes with excerpts; avoid: treating requests as specs
fixed:
  scope: <must deliver> ; excluded: <list>       # owner decision <id>
  window: <dates>                                # owner decision
  target_experience: <one or two kinds of fun>  # brief
  promise: <one sentence, player words>        # owner decision; every craft brief quotes it
open: [the activity, entrance, feedback, edge cases inside the scope]
avoid: [a new system where an existing mechanic can carry it]
owns: [the play spec]
not_in_scope: [reward amounts (progression designer), dates]
rules:
  - Returning players do not need every system added while they were away.
  - The activity is proven in its crudest playable form (plain Parts or a config build) and judged from the studio-operator's play captures before any art brief.
  - Every action has an attempt cue on input and the big layer only on the confirmed result.
deliver: play spec with interaction acceptance criteria and edge cases; the grey-box verdict; the feedback stack; for a limited mode, luck placement and a balance-pass list over every unit
checks:
  - C1: entrance findable by a new player and a returning player (state how it is tested)
  - C2: a request the server rejects shows no success layer (the capture that shows it)
return: hand-back to live-ops-designer, copy to lead
</spec>
```

## 5. Live-ops → engineering, via the lead (estimate request before ranking)
```text
<intent>
The owner will choose between <options>. I need honest effort and lead time for each before any date reaches players, because a promise the team cannot keep breaks trust.
</intent>
<spec>
id: <job>-T<nn>
from: live-ops-designer
to: architect (new system) | feature-builder (money, saves, remotes) | quick-builder (table or config change)   # the lead routes
model: opus
effort: medium (high for money, saves, remotes)  # engineering roles
skills: [engineering-craft]                     # + data-saving, platform-policy for money or saves; + networking-security for anything client-callable (AGENTS.md §2)
refs:
  - knowledge/jobs/<job>/live-ops/plan-<date>.md     # take: options, scope, dependencies
fixed:
  options: [<id>: <one line each>]
open: [how to build, reuse, risks]
avoid: [an estimate without testing, support and safe-disable time]
owns: [the estimate file]
not_in_scope: [building anything before the owner's decision]
rules:
  - Active effort and elapsed lead time separately; ranges with a confidence label.
  - State what saved state each option changes and whether a config switch can disable it.
deliver: per option: effort range, lead time, dependencies, risks, persistent-state impact, disable path
checks:
  - C1: every option has both numbers or "cannot estimate: <missing input>"
return: hand-back to live-ops-designer, copy to lead
</spec>
```
After the pick the build brief is the update brief (process.md §3) with the builders' row, routed by the lead.

## 6. Live-ops → marketing (calendar and facts; answers marketing §5)
```text
<intent>
Players should hear about <update> only when it is real, in words that match what they will find. Here are the facts; the voice is yours; the owner publishes.
</intent>
<spec>
id: <job>-T<nn>
from: live-ops-designer
to: marketing
model: opus
effort: medium                                   # marketing role
skills: [marketing-design, marketing-craft]
refs:
  - knowledge/jobs/<job>/live-ops/patch-<version>.md   # take: the fact sheet and notes, checks P1-P5
  - knowledge/jobs/<job>/live-ops/event-<slug>.md      # take: dates, eligibility, reward terms
fixed:
  calendar: [<id, what is new for players, build, live date, event id>]
  limits: up to 10 ongoing or upcoming events; update announcements 60 characters, once per 3 days; personalized notifications 13+ opted in, one per user per day (FR-12..FR-16, read 2026-10-21)
open: [wording, channel choice, images]
avoid: [present tense for unbuilt scope; urgency words to younger players (FR-57); a Discord link inside the game]
owns: [announcement drafts]
not_in_scope: [publishing (owner), dates]
rules:
  - Every item has a build version and the date it is live.
  - No false scarcity or restarting timers in any offer copy (FR-54).
  - The launched thing is the hero; one crop-safe master feeds the event kit; the event changes one brand property (`marketing-design` §4 M-15, M-22).
deliver: announcement and event-listing drafts for the owner; the event kit list (icon, thumbnails, listing, in-game banner) from one master
checks:
  - C1: every claim maps to a fact-sheet line
return: hand-back to live-ops-designer, copy to lead
</spec>
```

## 7. Live-ops → trend scout (does this trend qualify?)
```text
<intent>
We are thinking of themeing <event> on <trend>. A trend only helps if it will still matter when we can ship, fits our players and is ours to use.
</intent>
<spec>
id: <job>-T<nn>
from: live-ops-designer
to: trend-scout
model: sonnet
effort: medium                                   # trend-scout role
skills: [market-trends, trend-scan]
fixed:
  earliest_ship: <date>                          # builder estimate <file>
  audience: <game's audience and age label>
open: [sources, how to show growth or fade]
avoid: [undated numbers; tracker estimates without their label]
owns: [the trend note]
not_in_scope: [event design]
rules:
  - Every number keeps its label (official / third-party sampled / estimate / derived) and date.
deliver: first-seen date, growth or fade, audience overlap, saturation, rights flags, useful life vs earliest_ship
checks:
  - C1: a "still relevant at earliest_ship?" answer with its evidence
return: hand-back to live-ops-designer, copy to lead
</spec>
```

## 8. What live-ops hands back
To the lead or the owner, in `rules/messages.md` §3: `STATUS`, coverage of every item in scope, evidence (files, tool outputs, decision ids), the open choices taken, owner actions, the next decision with a recommendation and a default.

## 9. Live-ops → art director (event theme, variants, limited items)
```text
<intent>
The owner chose <event / variant line>. Players must recognise every variant as the thing they love, see a theme that is clearly new next to our last one, and feel the event as the promise says. I need the theme and the anchors settled while a change is still cheap.
</intent>
<spec>
id: <job>-T<nn>
from: live-ops-designer
to: art-director
model: opus
effort: high                                     # art-director role
skills: [art-direction, art-review, reference-images]
refs:
  - knowledge/jobs/<job>/live-ops/brief-<decision id>.md   # take: promise, target experience, cohort, story line, tone shift, twist line
  - knowledge/jobs/<job>/live-ops/feedback-<date>.md       # take: what fans want, with counts
fixed:
  promise: <one sentence>                        # owner decision <id>
  nearest_themes: [<earlier events and theme lines>]
  variants: [<variant id: base item>]
open: [style levers, theme cues, colourways, the motif, a top-tier style break proposal]
avoid: [production art before the theme rough is picked; reserved gameplay colours in event decor]
owns: [the theme niche line, the anchors-kept list per variant, the theme rough]
not_in_scope: [reward tiers (progression designer), activity design (game designer), dates]
rules:
  - Each variant keeps its base's identity anchors (`game-design/references/systems-economy.md` §8).
  - A top-tier style break is a proposal for the owner, never a default.
deliver: theme niche line; theme rough at equal finish with the options; anchors-kept list per variant; colourway value check
checks:
  - C1: variant next to base, flat key, same distance: every anchor present (their review capture)
return: hand-back to live-ops-designer, copy to lead
</spec>
```
