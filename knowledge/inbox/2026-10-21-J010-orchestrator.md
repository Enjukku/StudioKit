---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J010-engineering-team
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J010 lessons (engineering team, docs routing)

| What | Evidence | Lesson |
| --- | --- | --- |
| Usage was not reported at G1b; the owner asked why testing was "so long" and "so costly" | owner 2026-10-21; study + paper 3.25 M tokens, test bench 1.65 M (Studio scenarios alone 0.71 M, about 4 h) | Estimate tokens, not agent counts, at G1; report the meter (`get_usage`) at every gate. Studio benches are the most expensive step: offer the smallest scenario set first |
| Owner chose the cheaper plan when shown options with costs | J010-D3 ("do the recommended") | Give plan options with token and time estimates, one recommendation |
| Kit rule "numbers are proposals until the owner confirms" made the new architect ask the owner technical budgets; it lost 2 of 3 graded tasks | scores-architect.md | Technical budgets are PROPOSAL values recorded for the gate, not questions (EC-16) |
| New and old agents tied on plain logic tasks (feature-builder 58/58 both) | scores-feature-builder.md | Claude writes good general code; differences show on Roblox-specific engine behaviour. Harder or engine-bound tasks are needed to separate agents |
| Owner's insight: the lever is routing agents to the right Roblox docs pages | owner 2026-10-21 | The context packet skipped the docs mirror (0/30 routing). Packet docs section 16/30, + Haiku scout 13/14 of the misses = 29/30 |
| Hidden test sets written before the build and a builder that wrote its own pre-tuning cases gave honest estimates (8/14 own vs 16/30 held out) | scores-docs-routing.md | Keep held-out cases outside the builder's view; ask builders to report their own pre-tuning cases separately |
