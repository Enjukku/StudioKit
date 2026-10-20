# Role roster

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20

Roles move in from the first game in phase 3; canonical format: see tools/sync_harness.py header. Models per tier come from `kit.json`.

| Role | Tier | Status |
| --- | --- | --- |
| orchestrator (lead, via orchestration skill) | lead | skill exists |
| game-designer | craft | planned |
| art-director | craft | planned |
| animator | craft | planned |
| sound-designer | craft | planned |
| vfx-designer | craft | planned |
| ui-ux-designer | craft | new |
| cutscene-director | craft | new |
| modeler | craft | new |
| character-rigger | craft | new |
| economy-designer | craft | new |
| content-builder (levels and world assets) | craft | planned |
| feature-builder | craft | planned |
| quick-builder | craft or mechanical | planned |
| architect | craft | planned |
| reviewer | craft | planned |
| qa-lead | craft | new |
| performance-engineer | craft | new |
| studio-operator | craft | planned |
| analyst | craft | planned |
| researcher | craft | planned |
| explore | mechanical | planned |
| doc-keeper | mechanical | planned |
| live-ops-designer | craft | later |
| marketing-store | craft | later |

**How roles are added (owner 2026-10-20):** the kit ships only the orchestrator (the `orchestration` skill) and the system. Every other role is built with `/build-agent` from material the owner supplies, using `templates/role.md` and `templates/skill/SKILL.md`. No role is trained without owner material.
