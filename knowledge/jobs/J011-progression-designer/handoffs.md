---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J011 step 4 (owner hand-off list, J011 brief)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J011 hand-off briefs: progression designer ↔ the studio

The owner's hand-off list: "to the game designer (goals in, curves out), engineering (data tables), UI (how progress is shown), the analyst and live-ops designer (planned), in the brief format." Each brief below is the shape the progression designer sends (`rules/messages.md` §2). `<...>` is filled per job. The craft-skill table (`progression-craft/references/data-handoff.md` §4) is the short version; these are the full templates. Planned roles (analyst, live-ops designer) do not exist yet: the progression designer writes the brief and the lead routes it.

## 1. Game designer → progression designer (goals in)
```text
<intent>
<the experience: what the player should feel from the first minute to the first month, in the owner's words; what becomes easier, what stays hard, which choices open, what must never be bought away; who plays, how long, on what device>
</intent>
<spec>
id: <job>-T<nn>
from: game-designer
to: progression-designer
model: opus
effort: high
skills: [progression-design, progression-craft, platform-policy]
refs: [knowledge/design/game-profile.md, <feature spec>, <tuning table draft>, knowledge/design/decisions.md rows <ids>]
fixed: {<owner decisions with ids: e.g. rebirth exists, no paid power, session target if decided>}
open: [curves, coefficients, model players, thresholds, options to offer]
not_in_scope: [loop changes, content list changes (ask back), game code]
rules: [every number labelled; feelings are hypotheses; no universal pacing numbers; paid random / ads / younger players per platform-policy; owner decides every value]
deliver: knowledge/jobs/<job>/progression/{timeline.md, model.json, runs/, chart.html, options.md}
checks: [C1 every timeline row has a verdict with evidence; C2 report ledger residual 0; C3 2-3 options + recommendation + default]
return: G2 sample first (timeline + one run + chart)
</spec>
```

## 2. Progression designer → game designer (curves out)
Sends `options.md` + charts: per option, what the player feels differently and when (timeline rows), trade-offs, uncertainty, the assumptions list, the recommendation and a default. Asks back when an option needs a loop or content change (a plateau needs a learning goal; a wall needs an exit). `fixed`: model revision, report paths. Check: the game designer can name for each option which timeline rows change.

## 3. Progression designer → engineering (data tables)
```text
<intent>
The game must read exactly these progression values so the pacing the owner approved is the pacing players get. <one paragraph: which system, which timeline rows depend on it, what goes wrong for players if a value or rounding rule drifts>
</intent>
<spec>
id: <job>-T<nn>
from: progression-designer
to: architect | feature-builder | quick-builder
model: opus
effort: medium (high for money, saves, remotes)
skills: [engineering-craft, architecture, data-saving (if saved values change), networking-security (if client-callable)]
refs: [content/progression/<model>.json rev <r>, <export>.json, fixtures.json, change-report.md (live changes)]
fixed:
  ids, units, caps, rounding and modifier order, prerequisites, reset keep/remove lists   # model rev <r>, owner <decision id>
  fixtures: <file> (exact expected values)   # model rev <r>
open: [file layout, runtime format, code structure, how definitions are loaded]
not_in_scope: [changing any value (ask back), game design]
rules: [the server is the authority for currency and grants; definitions are read-only data (architecture R-07); every fixture reproduced exactly in a test; rounding never changed silently; existing saves follow the change report and data-saving; paid random odds come from the same table the server rolls (platform-policy P-01)]
deliver: <code paths owned by engineering>
checks: [C1 a test reproduces every fixture exactly; C2 balance revision visible at runtime (log or attribute); C3 representative old saves load as the change report says]
return: change manifest to progression-designer and lead
</spec>
```

## 4. Progression designer → ui-ux-designer (how progress is shown)
Intent: at each timeline point, what the player must see to feel the target (first minute: what my action changed; first session: my next goal and what it unlocks). `fixed`: the values shown and their source table, display rounding (display only), the odds table for any random reward (`platform-policy`), what a reset keeps. `open`: layout, style, motion. Checks: on a phone, the next goal, its cost or requirement and its benefit are readable in the first minute; a reset screen states what is kept before the player confirms.

## 5. Progression designer → analyst (planned)
Intent: each timeline target must be testable with live data. `fixed`: per target the event (milestone reached, attempt/fail, economy source/sink with ending balance), the denominator (eligible players, non-completers kept), active vs calendar, cohort rule, the model revision tag, and the predicted value per policy. Rules: log after the authoritative grant; ≤ 5 economy currencies until confirmed; no progression chart promised from `LogProgressionEvent` (`analytics`, `progression-design/references/live-data.md`). Checks: each target maps to one query with its denominator.

## 6. Progression designer → live-ops designer (planned)
Intent: events add fun without breaking the approved timeline. `fixed`: sources and sinks an event may add, caps, what must never be bought, the model and policies to re-simulate any event change. Rules: the normal route is never balanced around events; event rewards labelled and re-simulated; paid random and ads per `platform-policy`. Checks: the change report shows milestone times with and without the event under the same policies.

## 7. Into the progression designer from the analyst (after launch, planned)
The analyst sends data with denominators and revisions; the progression designer returns the `live-data.md` §5 proposal (observation → explanations → test → smallest lever → re-simulated outcome → what to measure → owner decision).
