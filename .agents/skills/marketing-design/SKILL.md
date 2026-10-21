---
name: marketing-design
description: What and why of a Roblox game's marketing - one promise across title, icon, thumbnails, page and video, discovery, ads, creators, honest testing. Use when a game is pitched, named, launched or updated, for "nobody finds the game", "the thumbnail doesn't get clicks", "players click but leave", "make a better title", "should we run ads". Marketing reads first; marketing-craft is the how.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J012 from the owner's marketing research paper (2026-10-21; VERIFIED / EXPERIENCE / OPINION tags kept) and three fact-checks (`knowledge/reference/marketing/fact-check-*.md`, FD / FA / FS ids, read 2026-10-21). Tags here: **V** platform-documented fact · **E** someone's reported result, never a forecast · **O** the paper's proposed practice.

# Marketing design: sell the game players will really get

## 1. When this skill starts
It answers five questions, in this order:
1. **What does the game promise?** The player fantasy and the one moment that proves it, reachable in ordinary play (from the game designer's hook and promise ledger).
2. **Who is it for, and what do they already want?** Audience, age band, devices, the words they use (trend scout, dated).
3. **How will they meet it?** Which Roblox surfaces and outside channels, and what each one needs (§3).
4. **How will we know it worked?** The decision, metric, cohort and window, agreed with the analyst before anything goes live.
5. **What may we not do?** Platform rules, younger players, rights, and the owner's gate.

The marketing agent owns the answers as **proposals**. The owner approves the promise, every final asset, every external message and every spend (paper rule 15). How to make and check the assets: `marketing-craft`.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Roblox discovery and RFY facts, titles, icon and thumbnail facts, personalization, the game page and native video | `references/discovery-promise.md` |
| Short video and trailers, creators, Roblox Ads Manager, updates / events / notifications, community and Discord | `references/channels.md` |
| Truth rules, ads and younger players, ad integrations, rights, player data, the release gate, owner-only actions, don'ts | `references/policy-rights.md` |
| Cases (Roblox and other studios): what they show, what they do not | `references/cases.md` |
| How to do the work: steps, tools, templates, tests, hand-offs | `marketing-craft` |
| The hook test, the promise ledger, the title as fantasy | `game-concept` (C-02, C-08, `references/hook-promise.md`) |
| Marketing art that matches the game | `art-direction/references/platform-evolution-marketing.md` §3 |
| Trend numbers and their labels | `market-trends` |
| Platform rules in code (ads, paid random items, PolicyService) | `platform-policy` |

## 3. Steps
1. **Start at the concept, not at launch.** Marketing joins the game designer at preproduction step 1: title candidates and the first image test the concept itself (`preproduction` growth order). *Check:* the promise line and its moment are in the vision record.
2. **One promise, everywhere.** Title, description, icon, thumbnails, native video, social edits, announcements and the first session promise the same achievable thing; each claim has a playable promise-ledger row (`policy-rights.md` §1).
3. **Earn the click with the real moment.** Titles name the action and a real stake; the icon carries identity; each thumbnail shows one hero, one action, one consequence the game really has (`discovery-promise.md` §2-3).
4. **Deliver in the first session.** RFY ranks on what organically arrived players do next (PTR, first-play bounce, play days, playtime): marketing that overpromises is punished by the platform, not only by players (`discovery-promise.md` §1). Bring onboarding friction to the game designer instead of buying more impressions.
5. **Pick channels by fit, not by habit.** Native video and page first; then updates and events tied to real changes; short video where the game films well; creators with a bounded first deliverable; ads only as a measured test with a loss ceiling (`channels.md`).
6. **Test honestly.** Define the decision with the analyst first. Name the method: adaptive (thumbnail personalization), observational (titles, icons), attributed (ads, share links), randomized (only real experiments). Inconclusive is a valid result (`marketing-craft/references/testing-measurement.md`).
7. **Gate with the owner.** Nothing goes out without the seven-item release gate and a decision id (`policy-rights.md` §6).

## 4. Craft core (what separates great marketing from weak)
| ID | Practice | Evidence |
| --- | --- | --- |
| M-01 | **Optimize promise-to-play, not clicks.** A click from the wrong player costs ranking: RFY weighs PTR and first-play bounce of organic RFY players, then play days and playtime per user | V: RFY signals (FD-04..09); O: paper's central rule (MP:7) |
| M-02 | **The title is the fantasy, said plainly.** Action + distinct condition; the game answers any "what happens if". Keep the name stable; no repeated words; emojis at most one or two; genre matches | O: TI-04..06; V: Roblox naming rules (FD-13..17); `game-concept` C-02 |
| M-03 | **No title, video or posting optimum exists.** Never state a best length, word count, emoji count, posting hour or cadence; test your own game | V: FD-18; YouTube gives no numeric cadence, only "consistent, sustainable", and says publish time is not known to affect long-term performance (FS-04..05); O: OQ-04, OQ-06 |
| M-04 | **Icon = identity; thumbnail = one moment.** Icon: theme, tone, genre at about 150×150. Thumbnail: the moment ordinary play reaches, readable at the phone tile, nothing essential at the bottom | V: FD-19..25, FD-74; O: IM-19 |
| M-05 | **A custom thumbnail is the entry ticket** to Home recommendations since 2026-10-19; it guarantees nothing | V: FD-01..02 |
| M-06 | **Real gameplay early.** Native video in RFY: current gameplay in the first seconds, no cinematic trailer; reported lifts are directional, not forecasts | V: FD-47..48; E: FD-49 |
| M-07 | **Adaptive is not A/B.** Thumbnail personalization is a bandit over 2-5 images; no native title or icon test exists; ad creative delivery is documented as even. Label every result by its method | V: FD-26, FD-35..36, FA-11; T04 answer |
| M-08 | **Every number keeps its denominator.** qPTR is not PTR; views, sessions and unique players differ; immature cohorts are pending; 2026-10-12 changed Roblox's recording | V: FD-30, FD-42..43, FD-51..52; O: ME-19, ME-24 |
| M-09 | **Ads buy consideration, never ranking.** Ad-arrived players do not count for RFY; plan an ad test as a bounded experiment with a loss ceiling and a holdout where possible; two ledgers (platform-attributed vs studio incremental) | V: FD-10, FA-58 (E: Roblox-reported 21-campaign medians); O: AD-17 |
| M-10 | **Creators: buy a deliverable and an audience, not followers.** Written quote per campaign, disclosure inside the video, rights and reuse separate, one share link each, aggregate reports only | O: CR-01..08; V: disclosure rules (FS-12..14, FS-20, FS-32..33); share links (FD-68) |
| M-11 | **Return messages need a real reason.** Announcements, events and notifications point to something live; a sending limit is not a cadence target | V: FD-53..64; O: UP-10 |
| M-12 | **Younger players change the rules.** No ad personalization under 18; no urging children to buy; rewarded video 13+; PolicyService required; no pushy messages to minors | V: FA-31..37, FA-50..51 |
| M-13 | **Borrow loops and craft lessons, never expression.** Cases are hypotheses, not forecasts; trends are not licenses | O: RU-06, PO-20; V: FA-53..54; `references/cases.md` |
| M-14 | **The owner holds every external lever.** The agent drafts, measures and recommends; publishing, spending, outreach and contracts are owner actions with decision ids | O: paper rule 15, RG-01..07; `policy-rights.md` §6 |

## 5. Rules (final check, short)
- No promise the build does not deliver. No future feature as live. No fake UI, Robux, prices, rewards, odds or timers in any asset.
- No invented optimum, benchmark, fee, CPM, CPP, minimum spend or forecast. Platform limits are stated as limits with a read date.
- Case results and platform-reported lifts are EXPERIENCE with scope, never targets.
- Ads and younger players, paid random items, player data: `platform-policy` + `references/policy-rights.md`.
- No franchise, character, music, logo or competitor art without the owner's rights record.
- The owner approves the promise, assets, messages and spend; the agent never acts externally.

## 6. Self-check before returning
- [ ] The promise line, its moment and its promise-ledger row are named before any asset.
- [ ] Every Roblox fact used has its source id and read date; re-read the live page if older than the decision.
- [ ] Every test names its method label and its analyst spec.
- [ ] Age, ad, rights and data rules checked for every channel used.
- [ ] Owner decisions listed with a recommendation and a default; nothing external done.

Project overlay: if `knowledge/overlays/marketing-design.md` exists, read it after this file; it wins for this game.
