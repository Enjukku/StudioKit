---
type: template
scope: universal
status: active
updated: 2026-10-22
source: J014; owner's live-ops paper §4 event design template + launch checklist (§10) (knowledge/reference/live-ops/01 §events, 02 §rules); platform-policy
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21; revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6)

# Event design: <event name> · <decision id> · v<n>

Workflow: `live-ops-craft` (event steps). For the owner, then the game designer, progression designer, builders, marketing and the analyst. Copy to `knowledge/jobs/<job>/live-ops/event-<slug>.md`. Every value the owner has not approved is marked `PROPOSAL`.

**Rule of use.** An event is a temporary player proposition: an entrance, a repeatable activity, a reward structure and a stated end. A themed lobby is a theme; a discount is an offer. Length comes from observed play opportunities and team coverage, never from a "best length". Completion must be possible through healthy play, with a late-start and missed-day path. Urgency is a true end with clear consequences; no fake stock counters, resetting timers, hidden requirements or streak loss. Every reward amount comes from the progression designer.

## A. Proposition
| Field | Value |
| --- | --- |
| player promise (one sentence, player words) | |
| primary goal and target cohort | active / lapsed / new / friends playing together |
| evidence | analyst finding, feedback theme (distinct authors), trend report; each with its date |
| mechanism | why this activity should change that cohort's behaviour |
| core-game fit | the existing fantasy, action or social link it strengthens |
| trend check (if themed on a trend) | first-seen date, growth or fade, audience overlap, useful life vs build-and-review time, rights |
| target experience | one or two kinds of fun from the game profile (`live-ops-craft/references/process.md` §3) |
| what fans want | theme ids, distinct authors per source, the count file |
| theme niche | against the nearest existing theme, one line |
| story line; twist line | the subject's role in the theme; when an iconic item changes, the twist line |
| tone shift | against the last run, and its limit |
| reward family | the named theme family and motif |
| variants | per variant: the anchors-kept list (art director's); new version, or the same subject in a new scene |
| new world or zone | escape line; how it differs from the last world |
| craft-ask table and capture set | paths: what each craft is asked for, when, and the capture it is judged on (`live-ops-craft/references/event-review.md` §1-§2) |

The rows from target experience down are the event brief lines of `live-ops-craft/references/process.md` §3 (the one list; what each line must hold is there); its tier rows are in §C. Fill each or write `n/a: <reason>`.

## B. Time
| Field | Value |
| --- | --- |
| start / gameplay end / reward-claim end | exact timestamps with time zone (UTC + local times shown to players); claim end may be `n/a: rewards granted instantly` |
| release that carries the event | build or config version, release window, dormant until start (time gate), gap between release and start, fallback window |
| length rationale | observed play opportunities and content consumption; team coverage |
| calendar beats | what changes, when, why each beat matters |
| synchronized moment (if any) | time, encore or other route for players who miss it, failure rehearsal |

## C. Play
| Field | Value |
| --- | --- |
| eligibility and entrance | new, active, returning; devices; regions; policy limits; where the entrance is, and how many eligible players already pass that place (analyst); a hard-to-find entrance needs a costed pointer |
| activity loop | entry → meaningful action → feedback → reward → optional next visit |
| effort and catch-up | earning distribution (not only the average); late-start and missed-day paths; low-frequency players |
| rewards | deterministic / random; free / paid; functional / cosmetic; tradable / bound; will it return?; tier per reward (progression designer's tier table) |
| economy impact (progression designer) | expected issuance range, sinks, persistent inventory, expiry and conversion rules, abuse cases (alt accounts, automation, trading) |
| monetization | price and value; eligibility; odds where any paid random item; no assumed conversion lift |

## D. Proof and safety
| Field | Value |
| --- | --- |
| success (analyst) | primary metric, denominator, baseline, comparison (observational / Roblox Experiment), window |
| guardrails | core retention, stability, fairness, economy, reward and purchase integrity, player pressure |
| production (builders) | builder estimates, reuse, dependencies, QA, support, moderation |
| communication (marketing) | event listing, announcement, in-game explanation, end reminders; channel age rules |
| failure plan | disable switch, safe reward handling, fallback activity, incident owner |
| exit | cleanup, unclaimed rewards, kept achievements, statement on whether it returns |
| decision after the event | repeat / revise / retire / investigate; analyst review date |

## E. Launch checklist (a fail in a must row blocks release; owner preference does not override a platform rule)
| # | Check | Must | Result | Evidence / source + read date |
| --- | --- | --- | --- | --- |
| L1 | content and audience approved by the owner | yes | | decision id |
| L2 | dates and prices true everywhere they appear | yes | | |
| L3 | rewards and odds shown correctly; odds total 100 %; boosts change shown odds; whole Robux → currency → roll chain checked | yes | | `platform-policy` §A |
| L4 | PolicyService gates for paid random items and paid trading; restricted players get a free or fixed path | yes | | `platform-policy` P-02, P-03 |
| L5 | communications allowed per channel (notifications 13+ opt-in, no false time pressure; social links per current eligibility) | yes | | |
| L6 | ad disclosures and eligibility (brand events) | if any brand | | |
| L7 | asset and theme rights recorded | yes | | |
| L8 | sensitive real-world events not used commercially | yes | | Community Standards |
| L9 | maturity questionnaire still true (horror, violence, gambling look) | yes | | owner action if it changes |
| L10 | data collection safe (no personal data, text filtered) | yes | | |
| L11 | expiry and conversion behaviour tested; entitlements tested | yes | | QA evidence |
| L12 | named incident responder and disable path | yes | | |

## F. Event review on named captures
Checklist, inputs and pass rules: `live-ops-craft/references/event-review.md` §3 (capture ids: §2). Status: gate-verified / MCP-verified / owner-confirmed / not verified / n/a: <reason>.
| ID | Input (capture ids, files) | Result | Status |
| --- | --- | --- | --- |
| E-01 | | | |
| E-02 | | | |
| E-03 | | | |
| E-04 | | | |
| E-05 | | | |
| E-06 | | | |
| E-07 | | | |
| E-08 | | | |
| E-09 | | | |
| E-10 | | | |
| E-11 | | | |
| E-12 | | | |
| E-13 | | | |
| E-14 | | | |
| E-15 | | | |
| E-16 | | | |
| E-17 | | | |
| E-18 | | | |
| E-19 | | | |

**Could not check**
| Line | Missing input | Capture or check that would close it |
| --- | --- | --- |
| | | |

One honest weakness of the event:
