---
type: decision
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (J016)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J016 decisions (owner's words)

| ID | Date | Decision | Owner's words |
| --- | --- | --- | --- |
| J016-D1 | 2026-10-21 | Step 2 (compare with the owner's sketch) is dropped; the flow is designed from the research | "Don't worry about my sketch. My sketch is outdated. Your information is more up to date. And because of such, you should design the flow after all the research that you've done." |
| J016-D2 | 2026-10-21 | Scope adds a context design: routing agents to the right context, passing context between agents, growing the vault with the project, recording what worked and what failed so every part of context keeps improving | "I also want you to think about how we handle context ... How do we make it so all the agents appropriately go to their correct context? How do we convey the correct context to various agents going back and forth? How do we build our vault so that the agents get integrated into the project over time? How do we record failures and successes and what worked and what didn't so the system keeps evolving and evolving in every aspect of context?" |
| J016-D3 | 2026-10-21 | Owner updated Claude Code before the pilot (now 2.1.306: workflow-resume and resumed-subagent fixes included) | "I've gone ahead and restarted Claude Code. It should be all up to date now." |
| J016-D5 | 2026-10-21 | **G2 passed:** the cutscene workflow's shape (`.agents/workflows/jobs/job-cutscene.js`, map page version 3) is the pattern for the other six job workflows; then steps 6 and 7 | "I approve the cutscene workflow's shape. Build the other six job workflows the same way, then continue with steps 6 and 7." |
| J016-D4 | 2026-10-21 | **G1 passed.** The flow design (`design.md`, `design-jobtypes.md`) and the context design (`design-context.md`) are the base for steps 4-8, with every recommendation on the map page (version 2): 7 job types incl. effect and marketing art; Riot lessons as a pointer per role now, full craft-skill edits as a later job; all 48 kit skill descriptions shortened in step 4; context packet gets role and job options (code change with tests, in this job); the two context hooks and the optional hand-back hook are shipped as scripts and the owner applies them in settings | "I approve the flow and context design, with all recommendations on the page. Start step 4." |
| J016-D6 | 2026-10-21 | Add `SendMessage` to the tool lists of the 11 working roles that lacked it (analyst, art-director, game-designer, live-ops-designer, marketing, progression-designer, reviewer, sound-designer, studio-operator, trend-scout, vfx-designer); helpers (doc-keeper, explore, researcher) stay without | "Okay, go ahead and add the 11 tools to the working roles that they lack." |
| J016-D7 | 2026-10-21 | The image roles get the built-in browser (`mcp__Claude_Browser__*`): art-director, vfx-designer and marketing generate their own images; the owner's yes per download batch still applies | "The image roles and browser, yes, the VFX designer should be able to also use the browser to get images." |
| J016-D8 | 2026-10-21 | No cutscene pilot now. The first real cutscene job (a GreatWallSim cutscene is the candidate) runs on the new design and serves as the pilot | "I don't plan to make any cutscene right now, but yeah, it would be, it could be used for the that game, yes." |

## Lead decisions at G3 (the lead's own calls inside the approved design; not owner decisions)
Made 2026-10-21 to resolve audit findings that left a choice open; every fixer followed them (commit 763a11e). Cited as LD1-LD16 in the fix notes and reviews.

| ID | Decision | Where it is written |
| --- | --- | --- |
| J016-LD1 | Tool lists are agent permissions: only the owner changes them; until then roles without `SendMessage` use exchange notes and the lead relays notices | `rules/company.md` §5 |
| J016-LD2 | Image steps write prompts first; they generate only with the browser and the owner's yes for the batch; otherwise `images: pending`, and the lead runs the batch between stages | `reference-images` §4 |
| J016-LD3 | Saved workflows use no agent ids: sideways work through files in a fixed order; repairs are fresh calls | `rules/company.md` §5 |
| J016-LD4 | In a hand-run stage the lead's chat spawns every craft | `rules/company.md` §6 |
| J016-LD5 | After the repair round limit a stage returns `needs-decision` to the lead; only scope, taste or budget goes to the owner | `rules/company.md` §7-8 |
| J016-LD6 | A mixed request splits into one job per type, with one owner job per shared interface | `orchestration` §2 |
| J016-LD7 | L = a new look or several separate outputs; one output with supporting crafts inside an approved style = M | `rules/company.md` §2 |
| J016-LD8 | Any file or folder whose name contains `hidden` is withheld from every agent, packet, index and scout | `rules/knowledge.md` §3 |
| J016-LD9 | Workflow flags that switch rules or gates have no silent default | `.agents/workflows/jobs/README.md` |
| J016-LD10 | Code file owners live in the contract header, set by the architect | `rules/company.md` §4 |
| J016-LD11 | Hand-backs carry `docs_read` and an optional `lesson`; the lead writes inbox drafts | `rules/messages.md` §3 |
| J016-LD12 | The dependency map is the Consumers table of each contract header | `rules/company.md` §5 |
| J016-LD13 | Review files use `type: job`; copied templates carry frontmatter on line 1 | `rules/knowledge.md` §5 |
| J016-LD14 | No section renumbering in rules or skills | `AGENTS.md` §4 |
| J016-LD15 | Every candidate with code gets the reviewer in its review chain | `rules/company.md` §7 |
| J016-LD16 | The lead checks the recipe's prerequisites at intake | `orchestration` §3 |
