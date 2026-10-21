---
type: index
scope: universal
status: active
updated: 2026-10-20
source: J003
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Game-design reference: owner material for the game-designer (J003)

The two research papers stay outside git (owner's Downloads folder). These notes are paraphrased extractions; skills cite them by short name.

| Short | Note | Source (owner-supplied 2026-10-20) | Trust | Used by |
| --- | --- | --- | --- | --- |
| N1 | [[reference/game-design/01-ideation-hook]] | Part 1 lines 1-328: AI ideation evidence, 15 cases, rubric, hook | evidence-tagged paper; registry dated 2026-10-21 | game-concept |
| N2 | [[reference/game-design/02-preproduction-docs]] | Part 1 lines 329-534: preproduction, leads, documents, creative director, idea method, pitch template | same | game-concept, preproduction |
| N3 | [[reference/game-design/03-loops-systems]] | Part 2 lines 1-178: loops, principles, systems, Roblox audience and monetization | same | game-design |
| N4 | [[reference/game-design/04-levels-social-review]] | Part 2 lines 179-366: levels, social, playtests, critique, live content, AI review | same | game-design, level-design |
| FR | [[reference/game-design/fact-check-roblox]] | 56 Roblox claims checked (mirror + live pages, 2026-10-20): 50 confirmed, 5 partly, 1 unverified, 0 contradicted | checked | all four skills |
| FI | [[reference/game-design/fact-check-industry]] | AI-research, case and studio-practice numbers | checked | all four skills |
| DS | DestructionSimulator `.agents/skills/game-design`, `level-design`, `.claude/agents/game-designer.md` (read-only) | Riot "So You Wanna Make Games??" transcripts (2026-10-15) | practice, one source | game-design, level-design |
| hidden | `knowledge/jobs/J003-game-designer/hidden-cases.md` | Part 1 cases 16-18 (held out of the skills) | eval only | evals |

## Contradictions and how the skills settle them
| Topic | Conflict | Resolution |
| --- | --- | --- |
| Scored reviews | DS scores checks 0-2 and totals out of 16 / 20; the paper forbids pseudo-scientific totals | Pass / Fail / Unproven per check, no totals (game-design review §2, level-design §4) |
| Fix ranking | the paper lists 7 components (§7), 5 (procedure step 8) and 4 (finding template) | one list of 7 components (game-design review §3) |
| Rubric order | FAIL vs UNKNOWN not ordered; no criterion for "proven loop" though the owner's formula needs one | both block readiness (FAIL = redesign, UNKNOWN = test); RB9 Loop proof added (game-concept rubric) |
| Lead review table | the paper asks for decision owner and exit evidence but its table has neither | columns added (preproduction growth-order §2) |
| Status words | retired / superseded / implemented used inconsistently | one state list (preproduction documents §1) |
| "Independent critic" | undefined | a separate subagent or fresh pass that sees only candidates + rubric (game-concept idea-method §1) |
| Paid-random rounding | paper: "100 % with a rounding exception" | docs rule: 100 %, long decimals rounded to 4+ places past the first non-zero digit with a disclaimer (FR RC22) |
| Benchmarks and ranking | paper: "not direct ranking inputs" | docs: no effect on ranking at all (FR RC18) |
| Under-13 ads tension | paper says R15 and integrations guidance conflict | no page states it: OPINION, check Roblox's current flow (FR RC56) |
| Grow a Garden peak month | Roblox sources disagree | cite 21.6 million with no month (FR RC43) |
| Old designer "never pitches" | DS role only reviewed | the new role pitches and leads pre-production (owner 2026-10-20) |
