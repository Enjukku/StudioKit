---
name: platform-policy
description: Keep a Roblox game inside Roblox's platform rules so it is not moderated, delisted or blocked in regions. Use when designing, building or reviewing anything players buy, roll, trade, chat, type, share or watch - paid random items (eggs, crates, wheels, luck boosts), developer products, passes, subscriptions, prices, ads, age checks, chat, text input, social links, media feeds, AI characters, player data, mature themes or franchise themes. Gives the rule, the PolicyService flag to check, the code pattern that makes compliance automatic, and the owner actions in Creator Hub.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J001 step 2. Evidence: `references/rules.md` (docs mirror upstream 7400643, live pages checked 2026-10-20, official Roblox DevForum announcements 2026). Updated 2026-10-21 with the J011 fact-check follow-ups (`knowledge/jobs/J011-progression-designer/policy-followups.md`).

# Platform policy: rules that keep the game live

## 1. When this skill starts
At **design time** for any feature in the trigger list (description), so the rule shapes the design, and again at **review** before merge. Policy is not a polish step: a paid egg without odds or a region gate is a removal risk on day one.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The rule, API and source for one area | `references/rules.md` § A paid random · B purchases · C ads · D age, chat, safety · E regions · F data · G AI · H off-platform and IP |
| What changed this year | `knowledge/reference/roblox/whats-new.md` § Platform policy |
| How the game saves receipts and player data | the game's data skill or system note |

## 3. Steps
1. **Classify the feature.** Answer yes or no for each: Robux or Robux-bought currency involved? Random outcome? Players trade? Players type or name things? Players see each other's content? Ads? Links or off-platform mentions? AI responses? New player data? Mature theme (violence, romance, scary, gambling look, private rooms)? Real brand or franchise?
2. **Open the matching sections** of `references/rules.md`. Copy each MUST that applies into the brief's acceptance checks, with its source line.
3. **Design the gate** with the patterns in §4. Decide what a restricted player sees (prefer hiding, §4 P-02).
4. **List owner actions** the code cannot do (§5) and put them in the hand-back.
5. **Review** with the self-check (§7) before merge.

## 4. Craft core (patterns that make compliance automatic)
| ID | Practice | Why / source |
| --- | --- | --- |
| P-01 | **One odds table.** The server roll and the odds UI read the same data table. The server sends each player their *effective* odds (with active boosts and once-only outcomes removed); the UI never computes its own copy. Odds show as numbers that sum to 100 % before the buy button, with a visible "Info"/"Details" label for long lists | A-rules `paid-random-items.md:53-75`. A copy drifts; a drift is a violation |
| P-02 | **One policy module.** At join, the server calls `GetPolicyInfoForPlayerAsync` in `pcall` (retry with backoff) and stores the flags for the session. Features ask the module, never PolicyService directly. If the call fails, **fail closed**: treat paid random as restricted, ads and paid trading as not allowed, content sharing off, until a retry succeeds (ours) | `PolicyService.yaml:85-184`; the call can error |
| P-03 | **Restricted players: hide, do not tease.** Hide the generator, ad unit or trade button, or give a free or fixed path. A visible button that refuses with an error is one of the six permitted treatments but confuses players: use it only when hiding is not possible | `paid-random-items.md:96-123`; DF 4654622 FAQ (official Roblox announcement, 2026-05-26) |
| P-04 | **One receipt pipeline.** One `ProcessReceipt` in one server Script; a data table maps ProductId → grant function; grant only after the player's save is loaded; record `PurchaseId` in the save **in the same write** as the grant; return `PurchaseGranted` only after the save succeeds; otherwise `NotProcessedYet` | `MarketplaceService.yaml:2247-2355`; same receipt can run on two servers |
| P-05 | **Prices from Roblox, never typed.** UI labels read `GetProductInfoAsync` at runtime on the client. Product ids live in data, prices never do | `regional-pricing.md:71,93-97` (Managed Pricing) |
| P-06 | **No free text when a preset works.** Pick-lists for names and messages. Where players must type: filter on the server after submit with `TextService:FilterStringAsync`, store the raw text only if needed, filter again for each display context | `ui/text-filtering.md:11-105` |
| P-07 | **Age and chat degrade, never block.** Features that need chat, voice or an age check check first and offer a version without them. Core gameplay never depends on `AgeChecked` | DF 4607091; `kids-and-select.md:43-45` |
| P-08 | **Questionnaire is part of done.** A feature that changes any maturity-questionnaire answer (paid random, trading, media sharing, AI, mature themes, social hangout) adds "resubmit questionnaire" to the owner actions | `content-maturity.md:67-73` |
| P-09 | **UserId keys only.** Player data keyed by UserId in the key or scope, so RTBF deletion templates can find it | `right-to-be-forgotten.md:15-31` |
| P-10 | **Numbers that move are links.** Thresholds, fees, revenue shares and region lists go into notes as a link plus the date read, never into code or skills as constants | `references/rules.md` § Numbers that change |

## 5. Owner actions (agents cannot do these; list them in the hand-back)
- Fill or resubmit the maturity questionnaire after a feature changes an answer.
- Creator Hub: mark developer products Listed for the Shop; set RTBF deletion templates; enable Chat & Voice Groups APIs if used; register ad campaigns.
- Account requirements for ads or Kids/Select reach (ID verification, 2FA).
- Any licence for a real brand or franchise.

## 6. Rules (final check)
- No paid random item without on-screen numeric odds before purchase and a `ArePaidRandomItemsRestricted` gate.
- No developer product granted outside `ProcessReceipt`; every grant idempotent on `PurchaseId`.
- No hard-coded prices; no off-platform links, handles or payment routes in the game.
- No custom or third-party ads; rewarded video only through `AdService`, never random rewards, never for under-13.
- All player-typed text filtered on the server before others see it.
- No playable or simulated gambling (a paid roll that pays back its own currency counts, rules § A); no personal data beyond Roblox ids.
- No pushy or urgent sales wording ("GET IT NOW"); use "View Item" or "See Price".
- When a source is missing or unclear, follow the stricter reading and mark it "ours" in the brief.

## 7. Self-check before returning
- [ ] Every trigger in §3 step 1 answered; each yes has its MUST rows in the acceptance checks with sources.
- [ ] Restricted-player experience defined for each PolicyService flag the feature touches.
- [ ] Odds UI and server roll read one table; boosts change the shown odds.
- [ ] Receipt path: one handler, PurchaseId stored with the grant, save before `PurchaseGranted`.
- [ ] Owner actions listed.
- [ ] Any number from a "changes often" item carries its source and date.

Project overlay: if `knowledge/overlays/platform-policy.md` exists, read it after this file; it wins for this game.
