---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J014 grader material (hidden-grader/T07-counts-after-1.1.1.md)"
supersedes: []
---
# Feedback counts - 2026-10-13T16:00:00Z to 2026-10-21T00:00:00Z (start in, end out)

Tool: `feedback_count/0.1.0`. Counts are exact; author keys are never printed.

## A. Sampling (counts)
| Source | Items in window | Sampled authors (distinct, tagged or not) | Untagged items | Dedup rule | Cross-source overlap |
| --- | --- | --- | --- | --- | --- |
| in-game | 14 | 14 | 2 | author_key within source | unknown (no shared key scheme) |
| discord | 33 | 26 | 3 | author_key within source | unknown (no shared key scheme) |
| reviews | 26 | 26 | 6 | author_key within source | unknown (no shared key scheme) |

## B. Urgent items (also counted in their themes)
| Source | Item ids |
| --- | --- |
| in-game | ig-013, ig-016 |
| discord | dcf-037, dcf-038, dcf-041, dcf-050, dcg-012 |
| reviews | rbx-039, rbx-045 |

## C. Themes per source (share = theme authors / sampled authors of that source only)
| Theme id | Source | Distinct authors / sampled authors | Share of sampled authors | Messages (intensity) | Flags |
| --- | --- | --- | --- | --- | --- |
| audio.music-loop | discord | 1 / 26 | 3.8 % | 1 |  |
| audio.music-loop | reviews | 1 / 26 | 3.8 % | 1 |  |
| bug.moth-stuck | in-game | 1 / 14 | 7.1 % | 1 |  |
| bug.moth-stuck | discord | 1 / 26 | 3.8 % | 1 |  |
| bug.moth-stuck | reviews | 1 / 26 | 3.8 % | 1 |  |
| content.more-rewards | in-game | 2 / 14 | 14.3 % | 2 |  |
| content.more-rewards | discord | 4 / 26 | 15.4 % | 4 |  |
| content.more-rewards | reviews | 4 / 26 | 15.4 % | 4 |  |
| crate.odds-not-shown | in-game | 1 / 14 | 7.1 % | 1 |  |
| crate.odds-not-shown | discord | 4 / 26 | 15.4 % | 4 |  |
| economy.dust-surplus | in-game | 1 / 14 | 7.1 % | 1 |  |
| economy.dust-surplus | discord | 2 / 26 | 7.7 % | 2 |  |
| economy.dust-surplus | reviews | 3 / 26 | 11.5 % | 3 |  |
| economy.upgrade-too-cheap | discord | 1 / 26 | 3.8 % | 1 |  |
| economy.upgrade-too-cheap | reviews | 1 / 26 | 3.8 % | 1 |  |
| economy.upgrade-too-costly | in-game | 1 / 14 | 7.1 % | 1 |  |
| economy.upgrade-too-costly | discord | 1 / 26 | 3.8 % | 1 |  |
| event.ended-too-soon | reviews | 1 / 26 | 3.8 % | 1 |  |
| feature.pvp | discord | 2 / 26 | 7.7 % | 2 |  |
| feature.pvp | reviews | 1 / 26 | 3.8 % | 1 |  |
| feature.trading | discord | 2 / 26 | 7.7 % | 4 |  |
| feature.trading | reviews | 1 / 26 | 3.8 % | 1 |  |
| onboarding.confusing-start | discord | 1 / 26 | 3.8 % | 1 |  |
| onboarding.confusing-start | reviews | 1 / 26 | 3.8 % | 1 |  |
| onboarding.lantern-placement-mobile | in-game | 1 / 14 | 7.1 % | 1 |  |
| onboarding.lantern-placement-mobile | discord | 1 / 26 | 3.8 % | 1 |  |
| perf.lag-pond-area-mobile | discord | 1 / 26 | 3.8 % | 3 |  |
| perf.lag-pond-area-mobile | reviews | 1 / 26 | 3.8 % | 1 |  |
| praise | in-game | 1 / 14 | 7.1 % | 1 |  |
| praise | discord | 1 / 26 | 3.8 % | 1 |  |
| praise | reviews | 1 / 26 | 3.8 % | 1 |  |
| progress.next-zone-unclear | in-game | 1 / 14 | 7.1 % | 1 |  |
| progress.next-zone-unclear | reviews | 1 / 26 | 3.8 % | 1 |  |
| progress.nothing-after-pond | discord | 3 / 26 | 11.5 % | 3 |  |
| progress.nothing-after-pond | reviews | 2 / 26 | 7.7 % | 2 |  |
| purchase.not-delivered | in-game | 1 / 14 | 7.1 % | 1 |  |
| purchase.not-delivered | discord | 2 / 26 | 7.7 % | 3 |  |
| purchase.not-delivered | reviews | 1 / 26 | 3.8 % | 1 |  |
| save.progress-lost | in-game | 1 / 14 | 7.1 % | 1 |  |
| save.progress-lost | discord | 2 / 26 | 7.7 % | 2 |  |
| save.progress-lost | reviews | 1 / 26 | 3.8 % | 1 |  |
| trend.frog-skins | in-game | 1 / 14 | 7.1 % | 1 |  |
| trend.frog-skins | discord | 1 / 26 | 3.8 % | 1 |  |
| trend.frog-skins | reviews | 1 / 26 | 3.8 % | 1 |  |
| ui.crowded-mobile | reviews | 1 / 26 | 3.8 % | 1 |  |

## Cross-source overlap
Overlap: **unknown**. No shared key scheme declared (--same-key-scheme); counts are per source only. No combined total is printed.
