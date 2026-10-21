---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J012; owner's marketing paper, weekly report (knowledge/reference/marketing/03-launch-measurement-policy-process-templates.md §6.6 TP-REPORT, §2 ME); analytics skill
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Weekly marketing report: <game> · <start> to <end> (<timezone>)

Workflow: `marketing-craft` (measurement), `analytics`. For the owner and the analyst. Copy to `knowledge/jobs/<job>/marketing/weekly/<yyyy-mm-dd>.md` (never name it `report*`: use the date).

**Rule of use.** Weekly is the owner's reporting rhythm, not a publishing or testing quota. Urgent policy, spend or misleading-creative problems go to the owner at once, not here. An unavailable value is `UNAVAILABLE`, never 0. Every rate shows its counts. No invented return on ad spend.

## A. Header
| Field | Value |
| --- | --- |
| data cut | extraction time; dashboard / export used |
| live build and creative versions | version ids, asset ids, change timestamps this week |
| decision requested | the choice, who decides, by when |
| result in three lines | what changed; evidence strength (causal / associated / self-report / insufficient); what is still uncertain |
| measurement breaks this period | dashboard or attribution changes (for example the 2026-10-12 Roblox recording change), outages |

## B. Metric dictionary
| Label (exact, as on the dashboard) | Numerator | Denominator | Eligibility | Surface | Paid / organic | Cohort | Window | Reporting delay |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## C. Acquisition
| Source | Impressions | Clicks (if defined) | Plays | Qualified plays (if defined) | Unique users | Spend + currency |
| --- | --- | --- | --- | --- | --- | --- |

## D. Arriving-player quality
| Cohort (source, start date) | Mature? | First-play bounce | Playtime | D1 | D7 | Other | Technical health |
| --- | --- | --- | --- | --- | --- | --- | --- |

## E. Creative tests
| Test | Hypothesis | Candidates | Allocation (adaptive / randomized / before-after) | Period | Population | Primary outcome | Guardrails | Counts | Uncertainty | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## F. Other channels
| Channel / video | View definition | Views | Engaged views | Watch metric | Outbound clicks | Roblox arrivals (source, link key) | Attribution limit |
| --- | --- | --- | --- | --- | --- | --- | --- |

## G. Creators
| Creator | Deliverables | Disclosure checked | Cost | Tracking | Measured outcome | Unmeasured spillover |
| --- | --- | --- | --- | --- | --- | --- |

## H. Cost and next action
| Field | Value |
| --- | --- |
| cost per defined outcome | outcome, cost lines (media, creator fee, production) kept separate |
| platform-attributed ROAS vs studio incremental estimate | two ledgers; label each forecast / attributed / incremental |
| next action | keep / revise / pause / investigate; why; reversible?; owner decision needed |
| missing evidence | what to track, what access, what result would change the recommendation |
