---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J014 G2 test output (g2/feedback-data/sorts/counts-2026-10-20-from-1.1.1.md)"
supersedes: []
---
# Feedback counts - 2026-10-13T16:00:00Z to 2026-10-21T00:00:00Z (start in, end out)

Tool: `feedback_count/0.1.0`. Counts are exact; author keys are never printed.

## A. Sampling (counts)
| Source | Items in window | Sampled authors (distinct, tagged or not) | Untagged items | Dedup rule | Cross-source overlap |
| --- | --- | --- | --- | --- | --- |
| in-game | 14 | 14 | 1 | author_key within source | unknown (no shared key scheme) |
| discord | 33 | 26 | 2 | author_key within source | unknown (no shared key scheme) |
| comments | 26 | 26 | 6 | author_key within source | unknown (no shared key scheme) |

## B. Urgent items (also counted in their themes)
| Source | Item ids |
| --- | --- |
| in-game | ig-010, ig-013, ig-016 |
| discord | dsc-037, dsc-038, dsc-041, dsc-044, dsc-045, dsc-049, dsc-050, dsc-069, dsc-072 |
| comments | rbx-039, rbx-045 |

## C. Themes per source (share = theme authors / sampled authors of that source only)
| Theme id | Source | Distinct authors / sampled authors | Share of sampled authors | Messages (intensity) | Flags |
| --- | --- | --- | --- | --- | --- |
| access.zone-gate-path-unclear | in-game | 1 / 14 | 7.1 % | 1 |  |
| access.zone-gate-path-unclear | comments | 1 / 26 | 3.8 % | 1 |  |
| audio.music-loop-short | discord | 1 / 26 | 3.8 % | 1 |  |
| audio.music-loop-short | comments | 1 / 26 | 3.8 % | 1 |  |
| bug.moth-stuck-in-net | in-game | 1 / 14 | 7.1 % | 1 |  |
| bug.moth-stuck-in-net | discord | 1 / 26 | 3.8 % | 1 |  |
| bug.moth-stuck-in-net | comments | 1 / 26 | 3.8 % | 1 |  |
| content.wants-more-collectibles | discord | 1 / 26 | 3.8 % | 1 |  |
| crate.odds-incomplete | discord | 1 / 26 | 3.8 % | 1 |  |
| crate.odds-not-shown | in-game | 1 / 14 | 7.1 % | 1 |  |
| crate.odds-not-shown | discord | 3 / 26 | 11.5 % | 3 |  |
| economy.dust-surplus-nothing-to-buy | in-game | 1 / 14 | 7.1 % | 1 |  |
| economy.dust-surplus-nothing-to-buy | discord | 3 / 26 | 11.5 % | 3 |  |
| economy.dust-surplus-nothing-to-buy | comments | 4 / 26 | 15.4 % | 4 |  |
| economy.dust-too-scarce | in-game | 2 / 14 | 14.3 % | 2 |  |
| economy.dust-too-scarce | discord | 1 / 26 | 3.8 % | 1 |  |
| economy.spark-swap-generous | discord | 2 / 26 | 7.7 % | 2 |  |
| event.leftover-currency | comments | 1 / 26 | 3.8 % | 1 |  |
| event.too-short | comments | 1 / 26 | 3.8 % | 1 |  |
| liked.game | in-game | 1 / 14 | 7.1 % | 1 |  |
| liked.game | discord | 2 / 26 | 7.7 % | 2 |  |
| liked.game | comments | 4 / 26 | 15.4 % | 4 |  |
| onboarding.lantern-placement-fails | in-game | 1 / 14 | 7.1 % | 1 |  |
| onboarding.lantern-placement-fails | discord | 1 / 26 | 3.8 % | 1 |  |
| onboarding.next-step-unclear | discord | 1 / 26 | 3.8 % | 1 |  |
| onboarding.next-step-unclear | comments | 1 / 26 | 3.8 % | 1 |  |
| perf.pond-lag-phone | discord | 1 / 26 | 3.8 % | 3 |  |
| perf.pond-lag-phone | comments | 1 / 26 | 3.8 % | 1 |  |
| privacy.personal-data-posted | discord | 1 / 26 | 3.8 % | 1 |  |
| progress.nothing-new-after-pond | discord | 3 / 26 | 11.5 % | 3 |  |
| progress.nothing-new-after-pond | comments | 2 / 26 | 7.7 % | 2 |  |
| purchase.beads-not-delivered | in-game | 1 / 14 | 7.1 % | 1 |  |
| purchase.beads-not-delivered | discord | 2 / 26 | 7.7 % | 3 |  |
| purchase.beads-not-delivered | comments | 1 / 26 | 3.8 % | 1 |  |
| return.no-daily-reason | discord | 1 / 26 | 3.8 % | 1 |  |
| rewards.not-motivating | in-game | 2 / 14 | 14.3 % | 2 |  |
| rewards.not-motivating | discord | 3 / 26 | 11.5 % | 3 |  |
| rewards.not-motivating | comments | 3 / 26 | 11.5 % | 3 |  |
| save.progress-lost | in-game | 1 / 14 | 7.1 % | 1 |  |
| save.progress-lost | discord | 2 / 26 | 7.7 % | 2 |  |
| save.progress-lost | comments | 1 / 26 | 3.8 % | 1 |  |
| shop.restock-unclear | discord | 1 / 26 | 3.8 % | 1 |  |
| social.cannot-exchange-moths | discord | 2 / 26 | 7.7 % | 4 |  |
| social.cannot-exchange-moths | comments | 1 / 26 | 3.8 % | 1 |  |
| social.no-competitive-play | discord | 2 / 26 | 7.7 % | 2 |  |
| social.no-competitive-play | comments | 1 / 26 | 3.8 % | 1 |  |
| theme.frog-interest | in-game | 1 / 14 | 7.1 % | 1 |  |
| theme.frog-interest | discord | 1 / 26 | 3.8 % | 1 |  |
| theme.frog-interest | comments | 1 / 26 | 3.8 % | 1 |  |
| ui.small-screen-crowded | comments | 1 / 26 | 3.8 % | 1 |  |

## Cross-source overlap
Overlap: **unknown**. No shared key scheme declared (--same-key-scheme); counts are per source only. No combined total is printed.
