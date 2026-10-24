---
type: job
scope: universal
status: draft
updated: 2026-10-24
source: J023 research (research/*.md), lead checks of job-feature.js:842-910 and :965-971, simulation on agent a1d9019c2 (upgrades-booth P3a)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-24

# J023 options for the owner (G1)

| ID | Change | Today (evidence) | Saves | Quality risk and guard |
| --- | --- | --- | --- | --- |
| A | Session size 500 k (chosen, J023-D1) or 300 k | Costliest agent: 92 % of its reading above 300 k, 46 % above 500 k (real-runs.md) | Estimate on that agent: 500 k → 67 % of actual tokens; 300 k → 42 % | Compaction drops detail; job state is in files. Owner's call |
| B | Re-check only what failed (the rule `rules/company.md` §7 already says so), keep the gate, the protected suite and the reviewer who found it | Every repair round re-runs the capture and every reviewer (`job-feature.js:842-910`; same in all scripts, flow-feature-ui-marketing.md) | About half the review runs per repair round (estimate) | Repairs did add new defects (J016: 6 new blockers; J020) → the gate, protected list and qa suite still run every round |
| C | One joint needs meeting after G1: all crafts write against one contract draft and read each other's notes; one merge; answers reused, not asked again | Cutscene asks the same cues 4-5 times, needs relayed through the film-director (12 runs); character needs are pairwise and VFX first appears at S7 (flow-*.md) | Fewer repeat runs; the job lead stops relaying | Better alignment, VFX and sound join early (owner J023-D2) |
| D | Direction: independent options only where there is a real choice (look, approach); no separate sign-off runs (job lead lists conflicts, each lead confirms in its next task); constraint owners write one limits sheet | Exchange + sign-off 5 % of tokens in the intro job; evidence for D2/D3 not tested on real jobs (lead-and-evidence.md) | 3-5 runs per job | A missed conflict surfaces later; the sheet lists every conflict for G1 |
| E | Make M smaller: M builds in the approved style without the separate proof stage, one direction lead | M = L work minus a gate: feature 36 = 36, character 46 = 46, cutscene 56 = 56 (harness counts) | About a third of an M job's runs (estimate) | Problems seen at G3 instead of G2; M is by definition inside an approved style |
| F | Right model, short agents: captures and Studio probes on the Sonnet studio-operator (as the recipes say); long making agents split by shot or piece | Scripts give captures to Opus film-director and qa-lead; the top 5 agents each read 46-73 M with 120-190 calls | Tokens, no step change | None for captures; more hand-offs for split agents |
| G | Less waiting: one digest per stage with defaults; the existing loosening rule (fewer gates after 3 right jobs of a type) | 35-62 % of wall time had no agent running (real-runs.md) | Wall time only | Fewer owner looks only where a type proved itself |
| H | Books: one home per duplicated rule | Role + skills are 2-25 k tokens; agents start at 76-97 k, mostly harness | About 5-10 % of an agent's start | Rules stay findable in one place; evals before and after |
