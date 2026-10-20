---
name: analytics
description: Plan and add player analytics in any Roblox game so the owner can see where players drop off, how far they get, why they leave and whether the economy flows - AnalyticsService funnel, onboarding, economy and custom events, custom fields, limits, Roblox Experiments (A/B tests through ConfigService), Creator Hub dashboards and the 2026 Open Cloud analytics APIs. Use when a feature adds a step new players must pass, a currency source or sink, or a moment players might quit; when asked "how is retention", "where do players quit", "did the update help"; and before an A/B test.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J001 step 9. Ported from the DestructionSimulator analytics skill (2026-10) with game details removed; numbers re-checked against the docs mirror (upstream 7400643). PA = `knowledge/external/roblox-creator-docs/production/analytics/`, Y = `knowledge/external/roblox-creator-docs/_api-reference/classes/`.

# Analytics: know why players stay or leave

## 1. When this skill starts
A feature is designed or changed (does it need events?), the owner asks a question about players, or a number should be A/B tested. The game's event plan lives in `knowledge/design/telemetry.md` (create it on first use): every event, its fields, where it fires and which question it answers. Change the plan in the same task as the code.

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
5. **Answer questions** from dashboards first, events second; compare our own updates over time (benchmarks need 100+ DAU).

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| T-01 | **Server only, published games only.** Client and Studio calls send nothing; keep the telemetry module silent in Studio | PA funnel-events.md:28 |
| T-02 | **One telemetry module**, server-side, every call in `pcall`. Other systems report facts to it; nobody calls AnalyticsService directly | ours |
| T-03 | **Log the success, not the attempt** (after the save or purchase returned) | PA event-types.md:53 |
| T-04 | **Method per case:** first-session steps → `LogOnboardingFunnelStepEvent(player, step, name, fields)`; one-time ordered paths → `LogFunnelStepEvent(player, funnelName, nil, step, name, fields)`; repeating flows (each shop visit) → `LogFunnelStepEvent` with a new `HttpService:GenerateGUID()` per run; currency in or out → `LogEconomyEvent(player, flowType, currency, amount, balanceAfter, transactionType, itemSku, fields)` with amount always positive; anything else → `LogCustomEvent(player, name, value, fields)`. Avoid `LogProgression*` (no Roblox chart) and deprecated `Fire*` methods | Y/AnalyticsService.yaml:705-716 |
| T-05 | **Limits** (reset daily): 120 + 20 × CCU requests per minute per server; 3 custom fields (`Enum.AnalyticsCustomFieldKeys.CustomField01..03.Name`), 8,000 value combinations then "Other"; 10 economy currencies; 20 transaction types, 100 item SKUs then "Other"; 10 funnels of ≤ 100 steps; 100 custom event names. Events roll off 90 days after the last data | PA event-types.md:57-130; custom-fields.md:17 |
| T-06 | **Fields over names.** One currency `XP` with a class field beats `WarriorXP`, `MageXP`. Bucket numbers (`1`, `2-5`, `6-20`) so fields stay few and readable | PA event-types.md:61 |
| T-07 | **Never per-frame or per-hit.** Aggregate high-frequency actions (seconds, counts) and log once per trip or session. Gate one-time steps with a saved flag instead of re-logging every join | PA funnel-events.md:128 |
| T-08 | **Funnel breakdowns use step 1's fields**: put segment fields (platform, new or returning) on step 1. Renumbering steps splits the chart; append instead | PA funnel-events.md:138 |
| T-09 | **A/B-testable numbers live in Configs.** Experiments test one config key (baseline + up to 2 variants) and report D1/D7 retention, playtime, ARPU, payer conversion. Server code reads `ConfigService:GetConfigForPlayerAsync(player)` then `snapshot:GetValue(key)`; the default comes from the game's content data. A number hard-coded in content cannot be tested | production/experiments.md:180-189 |
| T-10 | **Experiment discipline:** 14-60 days; one active experiment per key; size by the minimum detectable effect shown at setup (few players → only big differences show); stop on Early Harm Detection or a sample-ratio warning; never pick a winner from early results | cloud/guides/experiments.md:265-270; DF 4907734 (2026-09) |
| T-11 | **Agents can read results** through the Open Cloud Analytics Query, Events and Experiments APIs (live 2026-08-24) with an owner-made key scoped `universe.analytics:read`; key handling per `networking-security` N-11 | DF 4828676 (OrogeneIstari, 2026-08-24) |
| T-12 | **Watch updates by place version:** retention, playtime, crashes and client CPU on the Performance page; discovery numbers changed pipeline on 2026-10-12, so do not compare across that date | PA performance.md; DF 4930122 |

## 5. Rules (final check)
- No AnalyticsService call outside the telemetry module or from the client.
- No player-typed text or personal data in fields (`platform-policy` § F).
- No new event without a row in the telemetry plan saying which question it answers.
- No event per frame, hit or pickup.

## 6. Self-check before returning
- [ ] Each yes in step 1 has an event; each event has a plan row, a method, ≤ 3 bucketed fields and a firing point after success.
- [ ] Rate within 120 + 20 × CCU at a busy server (estimate events per player per minute).
- [ ] Tunable numbers that the owner may test are config keys.

Project overlay: if `knowledge/overlays/analytics.md` exists, read it after this file; it wins for this game.
