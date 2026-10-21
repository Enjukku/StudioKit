---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J014 grader material (hidden-grader/T07-counts-full.md)"
supersedes: []
---
# Feedback counts - 2026-09-29T00:00:00Z to 2026-10-21T00:00:00Z (start in, end out)

Tool: `feedback_count/0.1.0`. Counts are exact; author keys are never printed.

## A. Sampling (counts)
| Source | Items in window | Sampled authors (distinct, tagged or not) | Untagged items | Dedup rule | Cross-source overlap |
| --- | --- | --- | --- | --- | --- |
| in-game | 22 | 22 | 2 | author_key within source | unknown (no shared key scheme) |
| discord | 69 | 32 | 6 | author_key within source | unknown (no shared key scheme) |
| reviews | 60 | 60 | 15 | author_key within source | unknown (no shared key scheme) |

## B. Urgent items (also counted in their themes)
| Source | Item ids |
| --- | --- |
| in-game | ig-013, ig-016 |
| discord | dcf-037, dcf-038, dcf-041, dcf-050, dcg-012 |
| reviews | rbx-039, rbx-045 |

## C. Themes per source (share = theme authors / sampled authors of that source only)
| Theme id | Source | Distinct authors / sampled authors | Share of sampled authors | Messages (intensity) | Flags |
| --- | --- | --- | --- | --- | --- |
| audio.music-loop | discord | 1 / 32 | 3.1 % | 1 |  |
| audio.music-loop | reviews | 2 / 60 | 3.3 % | 2 |  |
| bug.moth-stuck | in-game | 1 / 22 | 4.5 % | 1 |  |
| bug.moth-stuck | discord | 1 / 32 | 3.1 % | 1 |  |
| bug.moth-stuck | reviews | 1 / 60 | 1.7 % | 1 |  |
| content.more-moths | reviews | 1 / 60 | 1.7 % | 1 |  |
| content.more-rewards | in-game | 3 / 22 | 13.6 % | 3 |  |
| content.more-rewards | discord | 6 / 32 | 18.8 % | 6 |  |
| content.more-rewards | reviews | 6 / 60 | 10.0 % | 6 |  |
| controls.net-too-easy | discord | 1 / 32 | 3.1 % | 1 |  |
| controls.net-too-easy | reviews | 1 / 60 | 1.7 % | 1 |  |
| controls.net-too-hard | in-game | 1 / 22 | 4.5 % | 1 |  |
| controls.net-too-hard | discord | 2 / 32 | 6.2 % | 2 |  |
| controls.net-too-hard | reviews | 1 / 60 | 1.7 % | 1 |  |
| crate.odds-not-shown | in-game | 1 / 22 | 4.5 % | 1 |  |
| crate.odds-not-shown | discord | 4 / 32 | 12.5 % | 4 |  |
| crate.odds-not-shown | reviews | 2 / 60 | 3.3 % | 2 |  |
| crate.value-poor | reviews | 2 / 60 | 3.3 % | 2 |  |
| economy.dust-surplus | in-game | 1 / 22 | 4.5 % | 1 |  |
| economy.dust-surplus | discord | 3 / 32 | 9.4 % | 3 |  |
| economy.dust-surplus | reviews | 3 / 60 | 5.0 % | 3 |  |
| economy.upgrade-too-cheap | discord | 1 / 32 | 3.1 % | 1 |  |
| economy.upgrade-too-cheap | reviews | 1 / 60 | 1.7 % | 1 |  |
| economy.upgrade-too-costly | in-game | 2 / 22 | 9.1 % | 2 |  |
| economy.upgrade-too-costly | discord | 3 / 32 | 9.4 % | 3 |  |
| economy.upgrade-too-costly | reviews | 1 / 60 | 1.7 % | 1 |  |
| event.ended-too-soon | discord | 2 / 32 | 6.2 % | 2 |  |
| event.ended-too-soon | reviews | 1 / 60 | 1.7 % | 1 |  |
| event.parade-positive | discord | 3 / 32 | 9.4 % | 3 |  |
| event.parade-positive | reviews | 4 / 60 | 6.7 % | 4 |  |
| feature.pvp | discord | 3 / 32 | 9.4 % | 3 |  |
| feature.pvp | reviews | 1 / 60 | 1.7 % | 1 |  |
| feature.trading | in-game | 1 / 22 | 4.5 % | 1 |  |
| feature.trading | discord | 4 / 32 | 12.5 % | 15 | one loud author: 9 of 15 messages from one author |
| feature.trading | reviews | 2 / 60 | 3.3 % | 2 |  |
| onboarding.confusing-start | discord | 2 / 32 | 6.2 % | 2 |  |
| onboarding.confusing-start | reviews | 4 / 60 | 6.7 % | 4 |  |
| onboarding.lantern-placement-mobile | in-game | 1 / 22 | 4.5 % | 1 |  |
| onboarding.lantern-placement-mobile | discord | 1 / 32 | 3.1 % | 1 |  |
| perf.lag-pond-area-mobile | in-game | 1 / 22 | 4.5 % | 1 |  |
| perf.lag-pond-area-mobile | discord | 1 / 32 | 3.1 % | 3 |  |
| perf.lag-pond-area-mobile | reviews | 3 / 60 | 5.0 % | 3 |  |
| praise | in-game | 3 / 22 | 13.6 % | 3 |  |
| praise | discord | 6 / 32 | 18.8 % | 6 |  |
| praise | reviews | 5 / 60 | 8.3 % | 5 |  |
| progress.next-zone-unclear | in-game | 2 / 22 | 9.1 % | 2 |  |
| progress.next-zone-unclear | discord | 1 / 32 | 3.1 % | 1 |  |
| progress.next-zone-unclear | reviews | 1 / 60 | 1.7 % | 1 |  |
| progress.nothing-after-pond | discord | 3 / 32 | 9.4 % | 3 |  |
| progress.nothing-after-pond | reviews | 2 / 60 | 3.3 % | 2 |  |
| purchase.not-delivered | in-game | 1 / 22 | 4.5 % | 1 |  |
| purchase.not-delivered | discord | 2 / 32 | 6.2 % | 3 |  |
| purchase.not-delivered | reviews | 1 / 60 | 1.7 % | 1 |  |
| save.progress-lost | in-game | 1 / 22 | 4.5 % | 1 |  |
| save.progress-lost | discord | 2 / 32 | 6.2 % | 2 |  |
| save.progress-lost | reviews | 1 / 60 | 1.7 % | 1 |  |
| trend.frog-skins | in-game | 1 / 22 | 4.5 % | 1 |  |
| trend.frog-skins | discord | 2 / 32 | 6.2 % | 3 |  |
| trend.frog-skins | reviews | 1 / 60 | 1.7 % | 1 |  |
| ui.crowded-mobile | reviews | 1 / 60 | 1.7 % | 1 |  |

## Cross-source overlap
Overlap: **unknown**. No shared key scheme declared (--same-key-scheme); counts are per source only. No combined total is printed.
