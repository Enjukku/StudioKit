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
