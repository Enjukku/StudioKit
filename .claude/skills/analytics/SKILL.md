---
name: analytics
description: Plan and add player analytics in any Roblox game so the owner can see where players drop off, how far they get, why they leave and whether the economy flows - AnalyticsService funnel, onboarding, economy and custom events, custom fields, limits, Roblox Experiments (A/B tests through ConfigService), Creator Hub dashboards and the 2026 Open Cloud analytics APIs. Use when a feature adds a step new players must pass, a currency source or sink, or a moment players might quit, and when an A/B-testable number must become a config. This skill owns the logging code; reading the data ("how is retention", "where do players quit", "did the update help", reading a test) belongs to the analyst (`analysis-design`, `analysis-craft`).
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J001 step 9. Ported from the DestructionSimulator analytics skill (2026-10) with game details removed; numbers re-checked against the docs mirror (upstream 7400643). Updated 2026-10-21 with the J011 fact-check follow-ups AN-1..AN-4 (`knowledge/jobs/J011-progression-designer/policy-followups.md`). PA = `knowledge/external/roblox-creator-docs/production/analytics/`, Y = `knowledge/external/roblox-creator-docs/_api-reference/classes/`.

# Analytics: know why players stay or leave

## 1. When this skill starts
A feature is designed or changed (does it need events?) or a number should be A/B tested. The analyst's measurement spec (`analysis-craft/references/event-planning.md`) says what each event means and which decision it serves; this skill says how to log it. Questions about players go to the analyst. The game's event plan lives in `knowledge/design/telemetry.md` (create it on first use): every event, its fields, where it fires and which question it answers. Change the plan in the same task as the code.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Event methods, parameters, examples | PA `event-types.md`, `funnel-events.md`, `economy-events.md`, `custom-events.md`, `custom-fields.md` |
| A/B tests | `knowledge/external/roblox-creator-docs/production/experiments.md`, `cloud/guides/experiments.md`, `production/configs.md` |
| Retention, engagement, monetisation, performance dashboards | PA `retention.md`, `engagement.md`, `monetization.md`, `performance.md`, `custom-dashboards.md`, `alerts.md` |
| New 2026 tools | `knowledge/reference/roblox/whats-new.md` § Analytics |

## 3. Steps
1. **Ask the three questions** of the feature: does it add a step a new player must pass? Does currency enter or leave? Is there a moment a player might give up? Each yes → an event row in the plan.
2. **Pick the method** (§4 table) and the fields (≤ 3, bucketed values).
3. **Wire it** through the game's one telemetry module on the server, after the action succeeded.
4. **Check after publishing:** Creator Hub → Analytics → View Events (near-live); charts after about 24 h.
5. **Questions about the data** go to the analyst (`analysis-design`, `analysis-craft`): it reads dashboards and the Open Cloud pulls and answers in the owner's shape.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| T-01 | **Server only, published games only.** Client and Studio calls send nothing; keep the telemetry module silent in Studio | PA funnel-events.md:28 |
| T-02 | **One telemetry module**, server-side, every call in `pcall`. Other systems report facts to it; nobody calls AnalyticsService directly | ours |
| T-03 | **Log the success, not the attempt** (after the save or purchase returned) | PA event-types.md:53 |
| T-04 | **Method per case:** first-session steps → `LogOnboardingFunnelStepEvent(player, step, name, fields)`; one-time ordered paths → `LogFunnelStepEvent(player, funnelName, nil, step, name, fields)`; repeating flows (each shop visit) → `LogFunnelStepEvent` with a new `HttpService:GenerateGUID()` per run (only `LogFunnelStepEvent` takes a `funnelSessionId`; Roblox keeps the 10 most recent ids per player per funnel, so an older id that comes back counts as a new run); paths players walk in any order between named places → `LogJourneyEvent(player, journeyName, nodeName, journeySessionId, fields)`, which is in the API reference only (no guide page, Sankey chart in Creator Hub not confirmed): check that the chart exists before relying on it; currency in or out → `LogEconomyEvent(player, flowType, currency, amount, balanceAfter, transactionType, itemSku, fields)` with amount always positive; anything else → `LogCustomEvent(player, name, value, fields)`. Avoid `LogProgression*` (no Roblox chart) and deprecated `Fire*` methods. A player with no events in a funnel for 180 days counts as new in it | Y/AnalyticsService.yaml:598-656,705-716; PA funnel-events.md:19,107 |
| T-05 | **Limits** (reset daily): 120 + 20 × CCU AnalyticsService requests per minute; the page does not say whether this is per server or per game, or how CCU is counted, so budget under 20 calls per player per minute on average (safe under both readings, ours); 3 custom fields (`Enum.AnalyticsCustomFieldKeys.CustomField01..03.Name`), 8,000 value combinations then "Other"; economy currencies: plan **5 or fewer** (the limits table says 10 resource types, the API reference and the Economy dashboard say 5; Roblox has not settled it); 20 transaction types, 100 item SKUs then "Other"; 10 funnels of ≤ 100 steps; 100 custom event names. Events roll off 90 days after the last data | PA event-types.md:57-130 (rate :76-78, resource types :93); economy-events.md:121; Y/AnalyticsService.yaml:474; custom-fields.md:17 |
| T-06 | **Fields over names.** One currency `XP` with a class field beats `WarriorXP`, `MageXP`. Bucket numbers (`1`, `2-5`, `6-20`) so fields stay few and readable | PA event-types.md:61 |
| T-07 | **Never per-frame or per-hit.** Aggregate high-frequency actions (seconds, counts) and log once per trip or session. Gate one-time steps with a saved flag instead of re-logging every join | PA funnel-events.md:128 |
| T-08 | **Funnel breakdowns use step 1's fields**: put segment fields (platform, new or returning) on step 1. Renumbering steps splits the chart; append instead | PA funnel-events.md:138 |
| T-09 | **A/B-testable numbers live in Configs.** Experiments test one config key (baseline + up to 2 variants) and report D1/D7 retention, playtime, ARPU, payer conversion. Server code reads `ConfigService:GetConfigForPlayerAsync(player)` then `snapshot:GetValue(key)`; the default comes from the game's content data. A number hard-coded in content cannot be tested. A config snapshot does not update by itself: listen to `UpdateAvailable` and call `Refresh` (or `GetValueChangedSignal`); new values arrive in about 15-60 s; `SetTestingValue` lasts one session; a restored config value must be published again | production/experiments.md:180-189 |
| T-10 | **Experiment discipline:** 14-60 days; one active experiment per key; size by the minimum detectable effect shown at setup (few players → only big differences show); stop on Early Harm Detection or a sample-ratio warning; never pick a winner from early results. Early Harm Detection needs 10,000+ enrolled players before it flags anything and watches only playtime, ARPU and payer conversion, so in a small game no flag means not enough data, not safe. Save and purchase checks stay outside any experiment's winner decision | cloud/guides/experiments.md:265-270; DF 4907734 (2026-10-01); `knowledge/reference/analyst/01-roblox-platform-facts.md` RF-44..46 |
| T-11 | **Agents read data through Open Cloud** (live 2026-08-24): Analytics Query API with scope `universe.analytics:read`; Experiments API reads (list, get, stats with the SRM flag; no documented per-metric results endpoint) with `universe:read`; the Events API only manages the event calendar (`universe.event:read`) and returns no numbers. The analyst's tool is `tools/analytics/`; key handling per `networking-security` N-11 | DF 4828676 (OrogeneIstari, 2026-08-24); `knowledge/reference/analyst/01-roblox-platform-facts.md` §4 |
| T-12 | **Watch updates by place version:** crashes, frame rate, memory and client CPU break down by place version on the Performance page (retention and playtime are on their own pages, without a version split); discovery numbers changed pipeline on 2026-10-12, so do not compare across that date | PA performance.md:40-44; DF 4930122 |

## 5. Rules (final check)
- No AnalyticsService call outside the telemetry module or from the client.
- No player-typed text or personal data in fields (`platform-policy` § F).
- No new event without a row in the telemetry plan saying which question it answers.
- No event per frame, hit or pickup.

## 6. Self-check before returning
- [ ] Each yes in step 1 has an event; each event has a plan row, a method, ≤ 3 bucketed fields and a firing point after success.
- [ ] Rate under 20 calls per player per minute on average at a busy server (inside 120 + 20 × CCU under either reading of its scope).
- [ ] Tunable numbers that the owner may test are config keys.

Project overlay: if `knowledge/overlays/analytics.md` exists, read it after this file; it wins for this game.
