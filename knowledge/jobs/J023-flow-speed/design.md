---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J023-D5 (owner G1 on options.md A-G); research/*.md
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-24

# J023 design: the shortened job flow (binding for the J023 builders)

Goal (J023-D3): same quality, fewer agent runs and tokens, less waiting. Every quality check that caught a real problem stays (`research/lead-and-evidence.md`). No owner gate is removed. Recipes (`orchestration/references/job-types.md`), the saved scripts (`.agents/workflows/jobs/*.js`) and `rules/company.md` must say the same thing after the change.

## B. Re-check only what failed (all 7 scripts)
Round 0 of a review chain runs as today. In every later round, after a repair:
1. Always run: the scripts check or gate for that job (as today), a fresh capture when the job's reviews judge captures, the **qa-lead** protected suite where the chain has a qa-lead, and the **reviewer** (code review) when the repair changed any code-owning maker's files.
2. Run every reviewer that raised a **blocking** finding in the previous round.
3. Run a reviewer whose area depends on a repaired layer: the job lead's integrated creative review when any visual or timing maker repaired; the art-director when any visual maker repaired. Each script states its dependency map in one table near the review chain.
4. Every other reviewer keeps its previous verdict. The stage result lists it as `carried: <reviewer> (round n, revision r)`.
5. Repair-round limits stay (2; code 3). A dead or empty review is never a pass (existing test).

## C. One joint needs meeting (all scripts with more than one craft)
- **When:** once, after G1 (L: before the proof; M: at the start of build). It replaces every separate needs or interface round and every later step that asks a craft again for timings, cue ids, joint lists or materials.
- **Who:** every craft the recipe names as a consumer of the contract (for example animator, character-rigger, modeler, vfx-designer, sound-designer, environment-designer, ui-ux-designer, architect, feature-builder). VFX and sound join here even in character and stage jobs.
- **How:**
  - Round 1, in parallel: each craft writes one exchange note against the same contract draft (`rules/messages.md` §4).
  - Round 2: each craft reads all round-1 notes and adds only agree / conflict / missing evidence about the others' needs. Skip it when round 1 has no conflict and no missing evidence.
  - The decision owner (the job lead) merges once into the next contract revision.
  - Owner limit: at most 2 rounds (`rules/company.md` §4), then a decision or a small test.
- **After:** later steps read the merged contract. They never re-ask. A new need found later is a contract change (`rules/messages.md` §5), not a new round.

## D. Lighter direction (all scripts)
- **D1 proposals:** independent proposals only from leads that own a real choice (look, approach, layout, mechanism). Constraint owners (architect, performance-engineer, progression-designer when it gives limits) write one limits-and-needs sheet in D1, in parallel, and are not called again in direction.
- **D2 exchange:** runs only when the job lead's synthesis finds a conflict between proposals. Then only the leads in that conflict, once.
- **D3:** the job lead writes `direction.md` with every conflict, its owner and its resolution. No separate sign-off runs. Each lead confirms or names an incompatibility in its first hand-back of the next stage (an incompatibility is a `needs-decision` to the lead).

## E. M jobs are smaller (all scripts)
- **M direction:** the job lead alone, plus the constraint owners' limits sheets. No look options (M is inside an approved style, `rules/company.md` §2).
- **M build:** no separate proof stage. It goes from the joint needs meeting straight to production in the approved style, with the recipe's check-ins and the full review chain (round 0) before G3.
- **L stays:** L keeps G2 and its proof.
- The test that today asserts "M build runs the proof inside" changes to assert that M build runs no proof calls and fewer agents than L proof + build.

## F. Right model, short agents (all scripts)
- **Captures, screenshots and Studio probes:** run by the `studio-operator` (Sonnet), as the recipes' model table says. The role that needs the probe names it in its hand-back. Opus roles never take routine captures.
- **Short agents:** a making step that covers several independent pieces (shots, strips, cue groups, kit pieces, screens) runs one agent per piece or per small group. Each piece has its own output file, and the job lead or integrator merges them. The rule for each agent's size is `rules/assistants/claude.md` Session size (500 k, J023-D1). Start with the cutscene P3a strips (the measured worst run).

## G. Less waiting (orchestration skill and `rules/company.md`)
- At the start of each stage, the lead asks all of that stage's owner questions in one digest, each with a default.
- Image batches are sent in one batch per stage.
- After a gate answer, the lead starts the next stage in the same turn, from a fresh session when the chat is past the session size.
- **Loosening:** each job's `evidence.md` records whether the job type came back right (first-pass acceptance at each gate). When a type has 3 in a row, the lead proposes fewer gates for that type (`rules/company.md` §2, existing rule).

## Not in scope
H (shorter books) waits.
