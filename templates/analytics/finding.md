---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J013 (G2 gap: no template for a question or investigation file); analysis-design reporting.md §1, diagnosis.md §10
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# <The question in the owner's words, as a title>

Workflow: `analysis-craft` §3.1 (question) or §3.2 (deep investigation). Copy to `knowledge/jobs/<job>/analyst/<short-name>.md` (name by content, never `report*`, `summary*`, `findings*`, `analysis*`); calculations in `calc/` next to it.

**Rules of use.** Part 1 is for the owner: plain words (`ste-writing`), at most about 25 lines, no statistics terms, **no hypothetical, example or made-up number** (explain mechanisms in words; examples go to Part 2 marked hypothetical). Before writing, apply the question-type checks in `analysis-craft` §3.1 (price change, benchmark, event, test, sudden drop) and name each check in Part 2. Part 2 holds everything a checker needs. Every number cites a source id from Part 2 A.

---

## Part 1 — For the owner

| | |
| --- | --- |
| **What this answer is for** | <the decision it serves, in the owner's words; if the question did not say, ask: "What will you decide with this?" and answer anyway> |
| **What happened** | <one finding in 1-3 sentences: which players, what changed, how much, compared with what. Two causes stacked: name the bigger one first and say which part the game owns> |
| **Why we think so** | <3-5 numbered points, each with counts and its source id [S#]> |
| **How sure we are** | <High / Medium / Low>. Numbers right? <…> Know why? <…> Worth acting? <…> |
| **What we recommend** | <one action> · who: <role, via the lead> · players: <…> · how we will know it worked: <measure and threshold> · check on: <date> |
| **What to expect** | <optional: what the fix will and will not bring back, labelled estimate> |
| **Your decision** | <the choice with a default, or "none"> |

---

## Part 2 — For the team and for checking

### A. Sources
| Id | What | File (pull id, `show` or `stats` output, script + output) |
| --- | --- | --- |
| S1 | | |

### B. Metric contract
| Decision | Unit | Eligible players | Window (UTC) | Numerator / denominator | Version and breaks | Source |
| --- | --- | --- | --- | --- | --- | --- |

### C. Data checks
Status run (age, warnings) · point status (`Projected`, `NotStatisticallySignificant`) · maturity for every cohort (`stats maturity`) · reconciliation (segments add up to totals) · measurement breaks · faults found and how they were bounded.

### D. Timeline
| Date (UTC) | What changed (build, config, event, marketing, measurement) | What moved |
| --- | --- | --- |

### E. Analysis
<who arrived (mix: `stats mix`), where in time, which segments, which step; comparisons with their basis (matched weekdays, placebo period)>

### F. Competing explanations
| Explanation | If true we would see | What we saw (for) | What we saw (against) | Status |
| --- | --- | --- | --- | --- |

### G. Diagnosis checklist (deep investigations: all 13 rows)
| # | Step | PASS / FAIL | Evidence or the missing measurement |
| --- | --- | --- | --- |

### H. Limits and next measurements
<what we do not know; N1, N2… the next measurements or tests, each with the command or owner action>

### I. Hand-offs and owner actions
| To | Brief file | Ask |
| --- | --- | --- |
