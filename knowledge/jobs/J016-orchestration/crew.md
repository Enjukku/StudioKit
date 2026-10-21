---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016 G3 (audit and rehearsal), lead's spawn results
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J016 crew (G3: audit and rehearsal)

Agents started before G3 are listed in the lead's transcript only (steps 1-7). Ids are for resumes and peer messages.

| Ticket | Role | Model · effort | Agent id | Writes | Status |
| --- | --- | --- | --- | --- | --- |
| J016-A1 | auditor A (general-purpose): core rules | opus · high | a84068b2d33d2da6e | reviews/core-rules-322c8ad-auditor-a.md | done (findings: reviews/) |
| J016-A2 | auditor B (general-purpose): job workflows | opus · high | ab7e6baa278b1dc8b | reviews/workflows-322c8ad-auditor-b.md | done (findings: reviews/) |
| J016-A3 | auditor C (general-purpose): roles, templates | opus · high | a2bd4fbae5117a22e | reviews/roles-templates-322c8ad-auditor-c.md | done (findings: reviews/) |
| J016-A4 | auditor D (general-purpose): context system | opus · high | a97173c47996487b9 | reviews/context-322c8ad-auditor-d.md | done (findings: reviews/) |
| J016-A5 | auditor E (general-purpose): tabletop run | opus · high | a5ad5ad9fd2aab104 | reviews/tabletop-322c8ad-auditor-e.md | done (findings: reviews/) |
| J099-R1-vfx | vfx-designer (rehearsal) | haiku · low (override) | af89943e7576e5687 | scratchpad only | done |
| J099-R1-sound | sound-designer (rehearsal) | haiku · low (override) | a32140e21513a25f6 | scratchpad only | blocked at R2 (no SendMessage tool) |
| J099-R3-review | art-director (rehearsal reviewer) | haiku · low (override) | a09d4b7f5482833fb | scratchpad only | done |
| J099-R5 | earlier mid-task probe receiver (resumed after compaction) | haiku | a30a7057ef7ecab3c | none | done |
| J016-Q1 | claude-code-guide: SendMessage in tool allowlists | sonnet | a1fdbbc26181d8171 | none | done (C22) |
| J016-W1 | fixer W1 (general-purpose): core rules, orchestration skill, reference-images rule | opus · high | acaa6e2b3b2cef4c7 | AGENTS.md, CLAUDE.md, rules/*, kit.json preamble, orchestration skill | working |
| J016-W2 | feature-builder (fixer W2): context tools, hooks, improve/integrate, vault files | opus · high | ac937f99a50958a5a | tools/context_packet.py, kb_index.py, eval_context.py, hooks, tests, vault headers | working |
| J016-W3 | fixer W3 (general-purpose): job workflows, harness, hand-back schema | opus · high | afb89893ae74ac3ec | .agents/workflows/jobs/*, wf_harness.mjs, test_job_workflows.py, handback.schema.json | working |
| J016-W4 | fixer W4 (general-purpose): role files text, templates | opus · high | a09f40dc252b375da | .agents/roles/* (not tools lines), templates/role.md, templates/jobs/* | working |
