---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J016 G3
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J016 G3 lessons (quality audit, rehearsal and fixes before the pilot)

| # | type | cause | layer | what happened | evidence link | proposed change |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | win | win | `orchestration` §13 (verification) | Five lane audits plus one tabletop run of three owner requests found 57 blocking defects in kit 0.6.0 before any real job ran, for about 1.5 M tokens. The tabletop found cross-file stalls the per-file audits missed (money rules behind an undocumented flag, a split request with no owner for the shared data) | `knowledge/jobs/J016-orchestration/reviews/`, `pilot-plan.md` §4 | Before piloting a process change: lane audits by independent reviewers plus one tabletop run, then fix, then a selective recheck |
| 2 | failure | context missing | `rules/company.md` §5; `/improve` step 1.7 probes | The rules promised direct messages to 14 roles whose `tools:` lists lack `SendMessage`. Only a live Haiku rehearsal showed it; docs reading and the gate did not | `pilot-plan.md` R2a; capability check C22 | Keep the C22 probe in the after-update probe list; a role's flow text never promises a tool its list lacks |
| 3 | failure | tool failure | `rules/company.md` §5 (tool lists are the owner's) | The lead's edit of two role tool lists was refused as self-modification. That is correct: tool lists are agent permissions | this job's transcript, 2026-10-21 | Tool-list changes always go to the owner digest with the exact lines; never edit them |
| 4 | failure | craft error | `testing` skill (trace table per binding rule) | The J016 packet change was tested for its flags, not for the withheld-context table, so held-out keys, other leads' proposals and another game's notes reached agents | feature-builder lesson in its hand-back; `reviews/context-322c8ad-auditor-d.md` B1-B3 | A context-tool brief lists each withheld row as a test row with a real-repo, paths-only check |
| 5 | failure | brief gap | `orchestration` §10 (briefs) | The lead's audit briefs asked for `type: review`, which is not a valid type; three review files failed the lint | `reviews/*-322c8ad-*.md` frontmatter | Before a brief names a frontmatter type, check `rules/knowledge.md` §5 |
| 6 | failure | interface conflict | `orchestration` §7 (integration) | Four parallel fixers each matched the lead decisions, but their seams broke: one cause label spelled two ways (rules vs schema), a needs-decision line left in the old form. The rechecks found 1+1+1+3 new blocking issues from the fixes | `reviews/*-763a11e-*.md` | After parallel fixers, the lead greps the shared labels, enums and status words across all their files before the recheck |
| 7 | failure | review broke correct work | `rules/messages.md` §7; repair briefs | A Haiku reviewer over-read an acceptance check ("3-4 % of screen" judged not a size); the maker did not dispute it and added invented PROPOSAL numbers | `pilot-plan.md` R3-R4 | A repair brief tells the maker to test each finding against the acceptance check's own words before fixing |
| 8 | win | win | `rules/company.md` §7 (selective recheck) | Resuming the original auditors for the recheck kept their context and found the fix-introduced defects; the cost was high: each resume resent 0.3-0.54 M tokens | `pilot-plan.md` §4 usage | Resume a reviewer whose context is small; for a large one, a fresh rechecker with the finding list and the cited lines may cost less. Measure it at the next recheck |
| 9 | win | win | `rules/knowledge.md` §9 | The retrieval drop after J016 was not the tool: two content edits (a shortened skill description, a renamed brief section) caused it, measured case by case on one tree at one moment | feature-builder repair hand-back; `knowledge/logs/improve/2026-10-21-retrieval.json` | When retrieval drops after a content change, measure old and new tools on the same tree first |
