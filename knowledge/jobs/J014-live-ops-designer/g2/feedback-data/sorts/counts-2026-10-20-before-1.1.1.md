---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J014 G2 test output (g2/feedback-data/sorts/counts-2026-10-20-before-1.1.1.md)"
supersedes: []
---
# Feedback counts - 2026-09-29T00:00:00Z to 2026-10-13T16:00:00Z (start in, end out)

Tool: `feedback_count/0.1.0`. Counts are exact; author keys are never printed.

## A. Sampling (counts)
| Source | Items in window | Sampled authors (distinct, tagged or not) | Untagged items | Dedup rule | Cross-source overlap |
| --- | --- | --- | --- | --- | --- |
| in-game | 8 | 8 | 0 | author_key within source | unknown (no shared key scheme) |
| discord | 36 | 24 | 2 | author_key within source | unknown (no shared key scheme) |
| comments | 34 | 34 | 9 | author_key within source | unknown (no shared key scheme) |

## B. Urgent items (also counted in their themes)
| Source | Item ids |
| --- | --- |
| comments | rbx-023, rbx-032 |

## C. Themes per source (share = theme authors / sampled authors of that source only)
| Theme id | Source | Distinct authors / sampled authors | Share of sampled authors | Messages (intensity) | Flags |
| --- | --- | --- | --- | --- | --- |
| access.zone-gate-path-unclear | in-game | 1 / 8 | 12.5 % | 1 |  |
| access.zone-gate-path-unclear | discord | 1 / 24 | 4.2 % | 1 |  |
| audio.music-loop-short | comments | 1 / 34 | 2.9 % | 1 |  |
| catch.net-timing-too-strict | in-game | 1 / 8 | 12.5 % | 1 |  |
| catch.net-timing-too-strict | discord | 2 / 24 | 8.3 % | 2 |  |
| catch.net-timing-too-strict | comments | 1 / 34 | 2.9 % | 1 |  |
| catch.too-easy | discord | 1 / 24 | 4.2 % | 1 |  |
| catch.too-easy | comments | 1 / 34 | 2.9 % | 1 |  |
| content.wants-more-collectibles | comments | 1 / 34 | 2.9 % | 1 |  |
| content.wants-more-decorations | discord | 1 / 24 | 4.2 % | 1 |  |
| crate.odds-not-shown | comments | 2 / 34 | 5.9 % | 2 |  |
| crate.repeat-outcomes-feel-unfair | comments | 2 / 34 | 5.9 % | 2 |  |
| economy.dust-too-scarce | in-game | 1 / 8 | 12.5 % | 1 |  |
| economy.dust-too-scarce | discord | 2 / 24 | 8.3 % | 2 |  |
| economy.dust-too-scarce | comments | 2 / 34 | 5.9 % | 2 |  |
| economy.spark-swap-generous | discord | 1 / 24 | 4.2 % | 1 |  |
| event.end-time-unclear | discord | 1 / 24 | 4.2 % | 1 |  |
| event.leftover-currency | discord | 1 / 24 | 4.2 % | 1 |  |
| event.too-short | discord | 1 / 24 | 4.2 % | 1 |  |
| liked.feedback-form | discord | 1 / 24 | 4.2 % | 1 |  |
| liked.feedback-form | comments | 1 / 34 | 2.9 % | 1 |  |
| liked.game | in-game | 2 / 8 | 25.0 % | 2 |  |
| liked.game | discord | 2 / 24 | 8.3 % | 2 |  |
| liked.game | comments | 5 / 34 | 14.7 % | 5 |  |
| liked.music | discord | 2 / 24 | 8.3 % | 2 |  |
| liked.music | comments | 2 / 34 | 5.9 % | 2 |  |
| liked.parade | discord | 3 / 24 | 12.5 % | 3 |  |
| liked.parade | comments | 4 / 34 | 11.8 % | 4 |  |
| liked.terrarium | discord | 1 / 24 | 4.2 % | 1 |  |
| onboarding.next-step-unclear | discord | 1 / 24 | 4.2 % | 1 |  |
| onboarding.next-step-unclear | comments | 3 / 34 | 8.8 % | 3 |  |
| perf.event-plaza-lag | comments | 1 / 34 | 2.9 % | 1 |  |
| perf.pond-lag-phone | in-game | 1 / 8 | 12.5 % | 1 |  |
| perf.pond-lag-phone | comments | 1 / 34 | 2.9 % | 1 |  |
| return.no-daily-reason | discord | 1 / 24 | 4.2 % | 1 |  |
| rewards.not-motivating | in-game | 1 / 8 | 12.5 % | 1 |  |
| rewards.not-motivating | discord | 1 / 24 | 4.2 % | 1 |  |
| rewards.not-motivating | comments | 2 / 34 | 5.9 % | 2 |  |
| social.cannot-exchange-moths | in-game | 1 / 8 | 12.5 % | 1 |  |
| social.cannot-exchange-moths | discord | 4 / 24 | 16.7 % | 11 | one loud author: 7 of 11 messages from one author |
| social.cannot-exchange-moths | comments | 1 / 34 | 2.9 % | 1 |  |
| social.no-competitive-play | discord | 1 / 24 | 4.2 % | 1 |  |
| theme.frog-interest | discord | 2 / 24 | 8.3 % | 2 |  |

## Cross-source overlap
Overlap: **unknown**. No shared key scheme declared (--same-key-scheme); counts are per source only. No combined total is printed.
