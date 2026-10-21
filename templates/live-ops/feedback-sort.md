---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J014; owner's live-ops paper §6 player feedback sorting template + taxonomy + counting rules (knowledge/reference/live-ops/02 §feedback); J014 digest item 5 (count tool)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Player feedback sort: <game> · <window start> to <window end> · build <version>

Workflow: `live-ops-craft` (feedback steps). For the owner and the analyst. Copy to `knowledge/jobs/<job>/live-ops/feedback-<yyyy-mm-dd>.md`. Counts come from `tools/liveops/feedback_count.py` (`live-ops-craft/references/feedback-ops.md` §3), never from the model's reading.

**Rule of use.** Count **distinct authors** per theme, per source, per window. Message volume is a separate "intensity" column. Never write a Discord share as "% of players": report theme authors / sampled authors of that source. A loud minority is neither the whole player base nor automatically wrong: weigh severity and reproducibility with prevalence. Silence is not satisfaction: check silent cohorts in behaviour data with the analyst. Safety, exploit, purchase and data-loss reports go to their owner at once (§B) **and** still count in their themes, so prevalence stays visible. Keep the problem apart from the requested solution.

## A. Sampling
| Source | Collection method and who could answer | Eligible / exposed / responding (counts and definitions) | Window | Dedup rule (author within source; rows with no author id) | Excluded items (staff posts, bots, abuse) and count | Cross-source overlap | Unavailable fields |
| --- | --- | --- | --- | --- | --- | --- |
| in-game | | | | | | | |
| Discord | | | | | | | |
| reviews (Roblox built-in rating prompt export) | | | | | | | |
| comments (other public comments) | | | | | | | |
| support reports | | | | | | | |

Codebook version and reviewer: <version, who checked ambiguous items>

## B. Urgent routing (routed at once; also counted in their themes)
| Item id | Kind (safety / exploit / purchase / data loss) | Routed to | When | Status |
| --- | --- | --- | --- | --- |

## C. Themes
Tags per item: area/system · player goal · symptom · suspected cause · requested solution · sentiment · severity · cohort (observed, never inferred) · device/build · reproducible? · date. One item may carry several tags; an author counts once per theme.

| Theme id | Player goal / symptom (problem, not solution) | Evidence: short faithful excerpts, source, date (no personal data) | Distinct authors / sampled authors, per source | Messages (intensity) | Cohort and severity | Behaviour check (analyst) or `unknown` | Contradicting sub-theme | Candidate response (fix / research / explain / defer) | Owner / status / player-facing follow-up |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## D. Loud vs silent
| Theme | Who is loud (source, author share) | Same friction in silent cohorts? (new, non-payers, mobile, returning, veterans) | Evidence | Read |
| --- | --- | --- | --- | --- |

## E. Quality checks
| # | Check | Result |
| --- | --- | --- |
| Q1 | counts produced by `feedback_count.py count`; tool output file named; `validate` exit 0 | |
| Q2 | raw examples read for every theme used in a plan | |
| Q3 | ambiguous and contradicting items reviewed; the decision recorded | |
| Q4 | excluded items sampled with reasons (abuse removed under community rules is listed, criticism is never excluded as abuse) | |
| Q5 | new themes marked apart from repeated discussion | |
| Q6 | evidence that contradicts the preferred proposal kept | |
| Q7 | no sensitive trait inferred from language, usernames or spending | |
