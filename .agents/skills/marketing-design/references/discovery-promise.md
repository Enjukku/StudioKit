# Roblox discovery, titles, icons, thumbnails, the game page

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `marketing-design`. Sources: `knowledge/reference/marketing/01-discovery-titles-images-page.md` (ids DI, TI, IM, PG), fact-check `fact-check-roblox-discovery.md` (FD ids, read 2026-10-21). Tags: **V** = platform documents it (a fact about the platform, not about outcomes) · **E** = someone reported a result · **O** = the owner's paper's proposed practice. Roblox changes these pages often: re-read the live page (or the local mirror `knowledge/external/roblox-creator-docs/`) before you tell the owner a limit, and write the date you read it.

## 1. How Roblox finds players for a game (V unless marked)
| Fact | Use it as | Src |
| --- | --- | --- |
| Since 2026-10-19 a game needs at least one custom (non-default) thumbnail to get **Home recommendation** impressions. It is a gate, not a promise of impressions. Players who already played still see it in Continue. Unknown: whether the rule reaches Search or Charts, and whether an AI-made image counts as custom (Roblox is silent) | a custom 16:9 thumbnail exists before any launch push | DI-01..03, FD-01..03 |
| Discovery = retrieval, then ranking. Ads, search, friends, teleports, notifications and outside links can get a game **considered**; those players' play does not count for Recommended For You (RFY) ranking | ads buy players, never ranking | DI-07..08, FD-10 |
| RFY ranks on players who **joined organically from RFY**: play-through rate (PTR) and first-play bounce (replaced qualified PTR on 2026-06-15), then play days per user and playtime per user; next tier co-play days, qualified sessions, spend days, Robux per user. Per-user averages, not totals. The Day 1 / Days 2-7 / Days 8-28 windows apply to play days, playtime and the second tier, not to PTR | the first session must deliver what the thumbnail promised; a lying thumbnail raises clicks and then bounce | DI-04..13, FD-04..07 |
| Bounce bands: under 60 s and 61-180 s. Counted playtime caps at 60 min per user per game per day (a ranking cap, not a session limit) | read bounce bands before you blame the art | DI-10..11, FD-08..09 |
| Roblox says benchmarks do not affect RFY at all; seasonality, competitors and platform changes move impressions | never promise a benchmark or a CCU that "unlocks Home" | DI-14..15, DI-19, FD-07 |
| Misleading, reward-led (giveaway, free Robux) or too-similar metadata can reduce exposure; search reads natural-language intent | honest, specific words beat bait | DI-16..17, FD-11 |
| Top Playing Now is a real-time, CCU-based Charts sort; it is not RFY, visits, revenue or Trending | save sort, filter, time and metric with every chart screenshot | DI-21..23, FD-12 |

**Diagnosis order when a game gets few players (O):** playable audience and moderation → custom-thumbnail eligibility → the real acquisition source (Acquisition dashboard) → RFY PTR and bounce of the organic cohort → mature return-play windows. Do not promise a launch-day seed, a post-update boost, a CCU threshold or a universal benchmark: no official source states them (DI-18..20).

## 2. Titles: a promise system (O unless marked)
- **The title is the fantasy.** The game designer's hook test applies first (`game-concept` C-02, `references/hook-promise.md`): a reader can say the action from the title alone. Marketing sharpens it; it never invents a new promise.
- A clear activity gives understanding; a distinct condition gives curiosity; the real game gives the payoff. "What happens if…" works only when ordinary play answers it. Stakes describe a real challenge, never false scarcity or an unavailable reward (TI-04..05). A dramatic title that sets the wrong expectation buys visits without good play (TI-06).
- **Roblox's own rules (V):** keep the name consistent (renaming often makes the old name hard to find; FD-13 corrected: "recognizable" is the paper's word); repeated words or phrases can demote the game (FD-14); one or two well-placed emojis are acceptable, with no uplift claimed (FD-15); the description's first sentence says what the game is, with relevant keywords used naturally (FD-16); genre matches the gameplay (FD-17).
- **Unknown (V, FD-18):** any optimal Roblox title length, word count, emoji count or update-tag lift. A platform's maximum is not an optimum. Never state one.
- **No native title or icon test exists** (searched 2026-10-21: docs mirror, live thumbnails/FAQ/API pages, roadmap, DevForum; Creator Hub Experiments cover in-game config and matchmaking only; FD-73 and the T04 answer). So: a comprehension check before launch (unfamiliar readers say what they would do; their words recorded), and after launch a logged change read with the analyst, labelled **observational** (TI-15..16).

## 3. Icon and thumbnails
| Asset | Platform facts (V) | Job (O) | Src |
| --- | --- | --- | --- |
| Icon | square, at least 512×512; some places show it at about 150×150, so preview small; one icon per locale; moderated | identity: theme, tone, genre at a glance (Roblox's words). "Not a feature list" is the paper's reading, not Roblox's | IM-01..02, FD-19..24 |
| Home thumbnail | 16:9, ideally 1920×1080 (other ratios are stretched to 16:9); nothing essential at the bottom (metadata such as player count can cover it); personalization uploads under 3 MB and 1920×1080 (scope per image not stated: treat as per image, FD-27 corrected) | one real moment: hero, action, consequence; the moment ordinary play reaches | IM-03, FD-25, FD-27, FD-74 |
| Gallery | up to 10 images or videos | core action before secondary features | IM-05, FD-29 |

**Thumbnail personalization (V):** starts only with 2 or more active thumbnails, range 2-5; a multi-armed bandit, not a fixed A/B test: traffic starts spread, then shifts toward the stronger image per audience group, with some exploration kept (IM-04, IM-10..11, FD-26, FD-28, FD-35..36). The 2024 launch post warned that games under about 1,000 DAU may see no meaningful result (a warning, not an entry rule; not on today's docs page, FD-37). Staff advice (2025-02-13): do not restart within 7 days, keep several distinct thumbnails active, change them with substantial content updates (FD-39..40). Since 2025-07-01 a restarted test that includes your current winner keeps most traffic on it (FD-72).
**Metric (V):** the thumbnail dashboard reports **qPTR** = qualified Home-recommendation plays ÷ Home-recommendation impressions; RFY ranking moved to all-play PTR; a 2026-07-20 reply said alignment is in progress; no page says it is done (IM-06, IM-17, FD-30, FD-42..43). Always write the exact label, numerator, denominator, cohort and export time. Never relabel qPTR as PTR.
**Reported lifts (E, never forecasts):** Roblox "during testing": +8.5 % average qPTR, some games +50 %, no sample size or window (FD-38). Staff snapshot 2025-02-13: over 8,000 experiences, +12 % average relative lift, some +56 % (FD-41). Two separate snapshots: never merge them, never promise either.
**First set (O):** distinct concepts, each only if the game really has it: core action, social situation, progression payoff (IM-19). An AI's predicted click score is not player evidence (IM-20). Icon swaps and gallery order need their own observation; personalization results say nothing about them (IM-22).

## 4. The game page and native video
| Fact (V) | Src |
| --- | --- |
| YouTube embeds on game pages: removal announced to start 2026-09-30; new ones disabled since November 2025. No source confirms the removal happened: check a live game page before telling the owner (FD-44..45) | PG-01 |
| Replacement: free direct video upload (Creator Hub → Configure → Places → the place → Videos), then approval; 3 free uploads a month; rejected videos still use the quota; Xbox, PlayStation and VR do not show native video | PG-02, FD-31..33, FD-46 |
| Native video content: representative current gameplay; no outside footage, narration, voice-chat audio or lyrical music; sparse factual text; real-gameplay camera work, a logo, in-game UI text and catalog music without lyrics are allowed | FD-34 |
| Gameplay videos fully rolled out in Home RFY (2026-08-31). Roblox: show real current gameplay in the first seconds; avoid cinematic, dramatized trailers | PG-04..05, FD-47..48 |
| Reported (E): Superstar Baseball +30 % plays / +31 % playtime, Notoriety +41 % / +39 %, test window 2026-06-07 to 06-26, "directional, not guarantees", no sample sizes. Video annotations exist in Acquisition, Engagement and Retention since 2026-09-01; no deeper video analytics found | PG-06..08, FD-49..50 |

**Page checklist (O, PG-09):** honest title, genre and first-sentence summary · icon readable at small size · approved custom Home thumbnail · gallery shows the core action first · current approved native video · only rewards that exist · a specific, real reason to come back · device and age eligibility checked. A badge list is no proof its reward helps retention; never claim every visitor sees the video (PG-10..11). Keep the native video and voiced social edits apart: their rules differ (PG-12).
