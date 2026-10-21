---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J016
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J016 lessons (orchestration and context redesign, through G1 and step 4)

| # | type | cause | layer | what happened | evidence link | proposed change |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | win | win | `orchestration` skill §13 (verification) | A Sonnet researcher spot-checked the 7 paper claims that drove the design against their primary sources: 5 confirmed, 2 overstated (a "most robust predictor" claim the paper does not make; a count that was the paper's own arithmetic). Cost about 27K tokens | `knowledge/jobs/J016-orchestration/capability-check.md` §2 | Before a design rests on a research paper, spot-check its 5-10 load-bearing claims with a cheap agent |
| 2 | failure | context missed | kit skill descriptions; `tools/verify.py` check f | The skill list's budget dropped the descriptions of 24 of 48 kit skills in the lead's own session, so the lead could not see when to use them. Found only because the lead looked at its own list | capability-check C20 | Descriptions ≤ 400 characters (gate check); route crafts through roles and the packet |
| 3 | win | tool failure (avoided) | `rules/knowledge.md` §8.5; `/improve` step 1.7 | Two Haiku probes (about 170K tokens) showed what the docs did not say: subagents cannot list each other, and on 2.1.296 a message arrived only after the receiver finished. After the owner's update to 2.1.306 the same probe showed mid-task delivery | capability-check C01-C03 | Re-run the probes after every Claude Code update |
| 4 | win | win | `orchestration` skill (workflow authoring) | A Node harness with fake agents tested all four stages of the cutscene workflow in 10 cases with zero tokens and found nothing broken after the lead's own review fixed 4 issues (browser and Studio sharing, review captures, unroutable makers) | `tools/workflows/wf_harness.mjs`; `tools/tests/test_job_workflows.py` | Every job workflow runs under the harness in the gate |
| 5 | owner-correction | owner taste change | J016 job card | The owner dropped the planned sketch comparison | "Don't worry about my sketch. My sketch is outdated. Your information is more up to date. And because of such, you should design the flow after all the research that you've done." | — |
| 6 | owner-correction | win | J016 decisions | G1 answer | "I approve the flow and context design, with all recommendations on the page. Start step 4." | — |
