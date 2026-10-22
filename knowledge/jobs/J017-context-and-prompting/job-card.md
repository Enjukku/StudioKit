---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (after J016)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J017 — Lower the start-up context of every agent; prompt each model the way Anthropic recommends

| Field | Value |
| --- | --- |
| Job id | J017-context-and-prompting |
| Size | M (measure and research, one proposal at G1, then changes across roles, skills and workflow briefs) |
| Job owner (agent) | lead (orchestrator) |
| Status | **closed 2026-10-21 (J017-D4).** G1 J017-D1, G3 J017-D4; owner decisions D2 (second Blender server stays), D3 (UI designer keeps the whole Figma connector) |

## Owner's words (2026-10-21)
"So how do we improve this further? You said we use a lot of usage just booting up skills, right? So how do we fix that?"
"First is the Claude prompting guide. Are we creating prompts properly? https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices And this is specific towards each model. So are we prompting Sonnet 5.5 properly? Are we prompting Opus 5.5 properly? Are we prompting Haiku 5.5 properly?"
"This might be helpful for lowering the amount of context we automatically boot up while still getting a similar result."

## Steps
| # | Step | Gate |
| --- | --- | --- |
| 1 | Measure what each role loads at start (rules, role file, preloaded skills, memory, tool definitions) from the smoke-run journals and the files | — |
| 2 | Fact sheet from the prompting guide, per model, with citations | — |
| 3 | Compare our briefs, role files, skills and workflow briefs with the guide | — |
| 4 | Proposal: what to cut or move, expected tokens saved, how quality is protected and measured | **G1** |
| 5 | Changes, gate, one before/after measurement | **G3** |

## Evidence (at close)
| Measure | Value |
| --- | --- |
| Start-up saved, 10 trimmed roles | 29-33 k tokens for 6 roles (rigger, qa-lead, environment, feature-builder, performance, architect); film-director 22 k; ui-ux-designer 16 k; modeler and quick-builder had no before (`startup-cost.md` "After") |
| Controls (tools unchanged) | sound-designer 30.2 → 29.8 k; reviewer 30.6 → 28.3 k (Agent tool removed) |
| Broken by the change | none found: right servers per role, SendMessage in all 12 probes, on-demand skill reads 11 of 11 |
| Quality after the prompt changes (B) | not measured yet: the first real jobs show it (`proposal.md` C.3; any drop reverts that change) |
| Usage | measurement probes about 0.8 M Haiku tokens; research, audit and changes: not counted separately |

## Filing at close (rules/knowledge.md §7, adapted for a kit job)
| Record | Filed to | Why there |
| --- | --- | --- |
| Owner decisions D1-D4 | this folder's `decisions.md` | kit process decisions |
| Prompting facts per model | `knowledge/reference/studio/prompting-guide-2026-10.md` | reference for every brief writer and `/improve` |
| Start-up cost before and after, method | this folder's `startup-cost.md` | the baseline for the next measurement |
| Capability: how to measure an agent's start-up cost | `knowledge/reference/studio/claude-code-capabilities.md` C27 | the living record |
| Lessons | `knowledge/inbox/2026-10-21-J017-orchestrator.md` | the weekly `/improve` pass |
| Precedents, vocabulary, taste log, systems, catalogs | none | no game artifact |

## Open follow-ups (not blocking)
- Watch the first real jobs for quality after the prompt changes (first-pass acceptance, defects you find after internal review) against `J016-orchestration/evidence.md`.
- Medium effort for narrow Opus steps (exchange, sign): one A/B at a time, later (`proposal.md` B "All").

**Retrospective:** the tool lists were the big lever; the remaining start-up cost is mostly the Studio server (about 20 k) and, for the UI designer, the Figma connector (about 45 k, kept by the owner).
