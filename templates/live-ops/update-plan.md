---
type: template
scope: universal
status: active
updated: 2026-10-22
source: J014; owner's live-ops paper §5 ranked update plan + §11 method (knowledge/reference/live-ops/01 §ranking, 02 §process); owner brief 2026-10-21
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21; revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6)

# Ranked update plan: <game> · decision period <start> to <end>

Workflow: `live-ops-craft` §3 steps 1-8. For the owner. Copy to `knowledge/jobs/<job>/live-ops/plan-<yyyy-mm-dd>.md` (never name it `report*` or `summary*`).

**Rule of use.** The owner chooses; silence is not approval. Urgent harm (lost progress, failed purchases, safety, broken access, exploitable currency) goes to row 0 and to the owner at once; it never competes with features. Effort comes from the builders, economy feasibility from the progression designer, numbers and denominators from the analyst: never guess them. Unknown impact is written `unknown; test required`, never a made-up decimal. No date for any row without a builder estimate and approved capacity.

## A. Header
| Field | Value |
| --- | --- |
| studio objective this period | owner's words + decision id |
| evidence cutoff | date and time; analyst report id; feedback sort id; trend page date |
| capacity | who estimated (role), available builder time after maintenance and release support, already committed work |
| constraints (capacity, policy, age label) | written before any option (`live-ops-design` §7 row 13) |
| success test | how we will know the update worked (`live-ops-design` §7 row 13) |
| missing inputs | what is not available (write it; never fill it) |
| recommendation in one line | rank 1 + why, in player words |

## B. Evidence packet
| Source | What it says (paraphrase) | Population / denominator | Window | Data quality notes | Label (VERIFIED / EXPERIENCE / OPINION / studio-measured) |
| --- | --- | --- | --- | --- | --- |
| analyst weekly report | | | | | |
| feedback sort (distinct authors per theme) | | | | | |
| trend scout page | | | | | |
| release state / incidents | | | | | |

## C. Ranked candidates
| Rank / status | Candidate and player problem (cohort) | Hypothesis: for <cohort>, <problem> prevents <behaviour>; changing <cause> should improve <metric> through <mechanism>, giving <target experience>, without harming <guardrails> | Evidence and uncertainty (sources, dates, counter-evidence) | Impact (reach, effect range or `unknown`, durability) and primary metric | Effort / dependencies (builder estimate: active effort, elapsed time; maintenance; risks) | Who builds (roles) | Policy flags | Decision requested |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 urgent (if any) | specific harm + affected players | — | measurement, reproducibility | harm stopped | estimate + safe mitigation | | | fix / mitigate now under agreed authority |
| 1 recommended | | | | | | | | approve scope and trade-off |
| 2 cheaper alternative | same objective, smaller scope | | what it can and cannot test | | | | | choose instead / keep in reserve |
| 3 | | | | | | | | |
| defer / reject | | | missing evidence or poor fit | | opportunity cost | | | revisit trigger / retire |

## D. Attachments (required for rank 1 and 2)
| Field | Value |
| --- | --- |
| confidence rationale | what evidence supports problem and mechanism; what does not |
| counter-evidence | what argues against the recommendation |
| economy implications | from the progression designer, or `not yet reviewed` |
| new / returning / veteran impact | access, comprehension, progression, preserved identity |
| measurement plan | analyst-agreed: cohort, primary outcome, guardrails, comparison (observational / Roblox Experiment), window, decision rule |
| rollback / disable | reversible config vs irreversible player state; who decides |
| communication commitments | what may be announced, when, by whom (marketing writes the voice) |
| explicit exclusions | what is not in this update |
| opportunity cost | what maintenance, fix or event beat this displaces |
| atypical option considered | one line (`live-ops-craft/references/process.md` §2 item 9) |

## E. Owner decision record
| Field | Value |
| --- | --- |
| chosen option and changes | owner's words, date, decision id |
| rejected alternatives and reasons | |
| capacity / budget authorized | |
| authorized date (only with builder estimate) | |
| success criteria | |
| permitted emergency actions | |

If the owner picks against the recommendation, keep the evidence as it was, record the reason and revise the brief. Never rewrite the evidence to make the choice look inevitable.
