---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J014 G2 test output (g2/feedback-data/sorts/counts-2026-10-20-full.md)"
supersedes: []
---
# Feedback counts - 2026-09-29T00:00:00Z to 2026-10-21T00:00:00Z (start in, end out)

Tool: `feedback_count/0.1.0`. Counts are exact; author keys are never printed.

## A. Sampling (counts)
| Source | Items in window | Sampled authors (distinct, tagged or not) | Untagged items | Dedup rule | Cross-source overlap |
| --- | --- | --- | --- | --- | --- |
| in-game | 22 | 22 | 1 | author_key within source | unknown (no shared key scheme) |
| discord | 69 | 32 | 4 | author_key within source | unknown (no shared key scheme) |
| comments | 60 | 60 | 15 | author_key within source | unknown (no shared key scheme) |

## B. Urgent items (also counted in their themes)
| Source | Item ids |
| --- | --- |
| in-game | ig-010, ig-013, ig-016 |
| discord | dsc-037, dsc-038, dsc-041, dsc-044, dsc-045, dsc-049, dsc-050, dsc-069, dsc-072 |
| comments | rbx-023, rbx-032, rbx-039, rbx-045 |

## C. Themes per source (share = theme authors / sampled authors of that source only)
| Theme id | Source | Distinct authors / sampled authors | Share of sampled authors | Messages (intensity) | Flags |
| --- | --- | --- | --- | --- | --- |
| access.zone-gate-path-unclear | in-game | 2 / 22 | 9.1 % | 2 |  |
| access.zone-gate-path-unclear | discord | 1 / 32 | 3.1 % | 1 |  |
| access.zone-gate-path-unclear | comments | 1 / 60 | 1.7 % | 1 |  |
| audio.music-loop-short | discord | 1 / 32 | 3.1 % | 1 |  |
| audio.music-loop-short | comments | 2 / 60 | 3.3 % | 2 |  |
| bug.moth-stuck-in-net | in-game | 1 / 22 | 4.5 % | 1 |  |
| bug.moth-stuck-in-net | discord | 1 / 32 | 3.1 % | 1 |  |
| bug.moth-stuck-in-net | comments | 1 / 60 | 1.7 % | 1 |  |
| catch.net-timing-too-strict | in-game | 1 / 22 | 4.5 % | 1 |  |
| catch.net-timing-too-strict | discord | 2 / 32 | 6.2 % | 2 |  |
| catch.net-timing-too-strict | comments | 1 / 60 | 1.7 % | 1 |  |
| catch.too-easy | discord | 1 / 32 | 3.1 % | 1 |  |
| catch.too-easy | comments | 1 / 60 | 1.7 % | 1 |  |
| content.wants-more-collectibles | discord | 1 / 32 | 3.1 % | 1 |  |
| content.wants-more-collectibles | comments | 1 / 60 | 1.7 % | 1 |  |
| content.wants-more-decorations | discord | 1 / 32 | 3.1 % | 1 |  |
| crate.odds-incomplete | discord | 1 / 32 | 3.1 % | 1 |  |
| crate.odds-not-shown | in-game | 1 / 22 | 4.5 % | 1 |  |
| crate.odds-not-shown | discord | 3 / 32 | 9.4 % | 3 |  |
| crate.odds-not-shown | comments | 2 / 60 | 3.3 % | 2 |  |
| crate.repeat-outcomes-feel-unfair | comments | 2 / 60 | 3.3 % | 2 |  |
| economy.dust-surplus-nothing-to-buy | in-game | 1 / 22 | 4.5 % | 1 |  |
| economy.dust-surplus-nothing-to-buy | discord | 3 / 32 | 9.4 % | 3 |  |
| economy.dust-surplus-nothing-to-buy | comments | 4 / 60 | 6.7 % | 4 |  |
| economy.dust-too-scarce | in-game | 3 / 22 | 13.6 % | 3 |  |
| economy.dust-too-scarce | discord | 3 / 32 | 9.4 % | 3 |  |
| economy.dust-too-scarce | comments | 2 / 60 | 3.3 % | 2 |  |
| economy.spark-swap-generous | discord | 2 / 32 | 6.2 % | 3 |  |
| event.end-time-unclear | discord | 1 / 32 | 3.1 % | 1 |  |
| event.leftover-currency | discord | 1 / 32 | 3.1 % | 1 |  |
| event.leftover-currency | comments | 1 / 60 | 1.7 % | 1 |  |
| event.too-short | discord | 1 / 32 | 3.1 % | 1 |  |
| event.too-short | comments | 1 / 60 | 1.7 % | 1 |  |
| liked.feedback-form | discord | 1 / 32 | 3.1 % | 1 |  |
| liked.feedback-form | comments | 1 / 60 | 1.7 % | 1 |  |
| liked.game | in-game | 3 / 22 | 13.6 % | 3 |  |
| liked.game | discord | 4 / 32 | 12.5 % | 4 |  |
| liked.game | comments | 9 / 60 | 15.0 % | 9 |  |
| liked.music | discord | 2 / 32 | 6.2 % | 2 |  |
| liked.music | comments | 2 / 60 | 3.3 % | 2 |  |
| liked.parade | discord | 3 / 32 | 9.4 % | 3 |  |
| liked.parade | comments | 4 / 60 | 6.7 % | 4 |  |
| liked.terrarium | discord | 1 / 32 | 3.1 % | 1 |  |
| onboarding.lantern-placement-fails | in-game | 1 / 22 | 4.5 % | 1 |  |
| onboarding.lantern-placement-fails | discord | 1 / 32 | 3.1 % | 1 |  |
| onboarding.next-step-unclear | discord | 2 / 32 | 6.2 % | 2 |  |
| onboarding.next-step-unclear | comments | 4 / 60 | 6.7 % | 4 |  |
| perf.event-plaza-lag | comments | 1 / 60 | 1.7 % | 1 |  |
| perf.pond-lag-phone | in-game | 1 / 22 | 4.5 % | 1 |  |
| perf.pond-lag-phone | discord | 1 / 32 | 3.1 % | 3 |  |
| perf.pond-lag-phone | comments | 2 / 60 | 3.3 % | 2 |  |
| privacy.personal-data-posted | discord | 1 / 32 | 3.1 % | 1 |  |
| progress.nothing-new-after-pond | discord | 3 / 32 | 9.4 % | 3 |  |
| progress.nothing-new-after-pond | comments | 2 / 60 | 3.3 % | 2 |  |
| purchase.beads-not-delivered | in-game | 1 / 22 | 4.5 % | 1 |  |
| purchase.beads-not-delivered | discord | 2 / 32 | 6.2 % | 3 |  |
| purchase.beads-not-delivered | comments | 1 / 60 | 1.7 % | 1 |  |
| return.no-daily-reason | discord | 2 / 32 | 6.2 % | 2 |  |
| rewards.not-motivating | in-game | 3 / 22 | 13.6 % | 3 |  |
| rewards.not-motivating | discord | 4 / 32 | 12.5 % | 4 |  |
| rewards.not-motivating | comments | 5 / 60 | 8.3 % | 5 |  |
| save.progress-lost | in-game | 1 / 22 | 4.5 % | 1 |  |
| save.progress-lost | discord | 2 / 32 | 6.2 % | 2 |  |
| save.progress-lost | comments | 1 / 60 | 1.7 % | 1 |  |
| shop.restock-unclear | discord | 1 / 32 | 3.1 % | 1 |  |
| social.cannot-exchange-moths | in-game | 1 / 22 | 4.5 % | 1 |  |
| social.cannot-exchange-moths | discord | 4 / 32 | 12.5 % | 15 | one loud author: 9 of 15 messages from one author |
| social.cannot-exchange-moths | comments | 2 / 60 | 3.3 % | 2 |  |
| social.no-competitive-play | discord | 3 / 32 | 9.4 % | 3 |  |
| social.no-competitive-play | comments | 1 / 60 | 1.7 % | 1 |  |
| theme.frog-interest | in-game | 1 / 22 | 4.5 % | 1 |  |
| theme.frog-interest | discord | 2 / 32 | 6.2 % | 3 |  |
| theme.frog-interest | comments | 1 / 60 | 1.7 % | 1 |  |
| ui.small-screen-crowded | comments | 1 / 60 | 1.7 % | 1 |  |

## Cross-source overlap
Overlap: **unknown**. No shared key scheme declared (--same-key-scheme); counts are per source only. No combined total is printed.
