---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J014 synthetic test data (test-pack/capacity.md)"
supersedes: []
---
SYNTHETIC TEST DATA (J014-T07). Not a real game, not real players.

# Builder capacity: Mothlight Meadow, next 4 weeks (2026-10-21 to 2026-11-17)

Written by the engineering lead on 2026-10-20. "Active days" are days of real work. "Elapsed" is calendar time from the owner's approval to a release, including waiting. Work is released only in these windows: **Tuesday and Thursday 15:00 UTC** (2026-10-22, 10-27, 10-29, 11-03, 11-05, 11-10, 11-12, 11-17). No planned release within 24 hours before an event starts. Urgent fixes may use any time.

## 1. Active days after maintenance

| Role | Active days in 4 weeks | Maintenance and release support | Already committed | Free | Elapsed per typical item | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| feature-builder (code, saves, purchases, networking) | 12 (3 days a week) | 4 (1 day a week) | 3: Reed Pond phone performance pass, 2026-10-21 to 10-27 | **5** | Small change: 2 working days after approval. A change that touches purchases or saves adds 1 working day for the reviewer and 1 for QA | One builder. One task at a time |
| quick-builder (data tables, config, small UI tweaks) | 8 (2 days a week) | 2 | 0 | 6 | 1 to 3 working days | Does not touch purchases, saves or remotes |
| ui-ux-designer | 4 | 0 | 0 | 4 | 3 working days per screen, including the Figma file and hand-off | |
| modeler (creatures, cosmetics) | 4 | 0 | 0 | 4 | A new creature or cosmetic set: 5 working days after the owner approves the reference image. A re-colour of existing assets: 1 to 2 working days | |
| vfx-designer | 2 | 0 | 0 | 2 | 2 working days | |
| sound-designer | 1 | 0 | 0 | 1 | 2 working days | |
| environment-designer | 3 | 0 | 0 | 3 | 4 working days to re-dress an existing area | |
| analyst | 6 reserved for the weekly page | 6 | 0 | 1 | A measurement spec for a new feature: 2 working days lead time | |
| marketing (voice for patch notes and announcements) | 2 | 0 | 0 | 2 | 1 working day | |

## 2. Rules that affect time
- Maintenance covers: dependency monitoring and small bug fixes of up to 0.5 day each. Anything larger, or anything that needs an investigation first, is **not** inside maintenance. It takes free days and needs the owner's go-ahead.
- Every player-visible release needs the owner's final look (Gate 3). Owner turnaround: 2 working days. The owner does not answer on Saturday and Sunday.
- Every change that touches purchases, saves or remotes needs the reviewer and QA before it is released.
- No reference-image approval means no art work starts.

## 2b. Earliest release window by kind of work
Worked out by the engineering lead from the rules above, assuming the owner approves on Wednesday 2026-10-21, the reference-image approval takes 2 working days, and the committed performance pass is not paused.

| Kind of work | Earliest window | Why |
| --- | --- | --- |
| Data or config only (quick-builder, no code) | Tue 2026-10-27 | Owner look by 10-23 |
| Re-colour of existing art plus data | Thu 2026-10-29 | Modeler 1 to 2 days, then the owner look |
| Small code change by the feature-builder (no purchases or saves) | Tue 2026-11-03 | The builder is free from 2026-10-28; 2 working days; then the owner look |
| Change that touches purchases or saves | Thu 2026-11-05 | Adds reviewer and QA days |
| New creature or cosmetic set | Thu 2026-11-05 | Reference image approved about 10-23, modeler 5 working days, integration, then the owner look |
| New system (several builder days) | Tue 2026-11-10 | Uses the 5 free builder days, then review, QA and the owner look |

## 3. The date the owner cares about (synthetic owner note)
**Halloween weekend, Saturday 2026-10-31.** The owner wants something live that weekend and says the weekend matters more than any other date in the next four weeks. This is a stated preference, not a locked decision (no decision id). An event that starts Friday 2026-10-30 at 15:00 UTC would cover the whole weekend.

## 4. What past work actually took (for reference; not an estimate for new work)
| Past item | Active days by role | Elapsed |
| --- | --- | --- |
| Lantern Parade event (1.1.0) | feature-builder 4, quick-builder 3, ui-ux-designer 2, modeler 3, vfx-designer 1.5, sound-designer 0.5, environment-designer 2 | 17 calendar days from brief to release (2026-09-21 to 2026-10-08) |
| "Tell us" form (1.1.0) | feature-builder 2, reviewer 1, ui-ux-designer 1 | 6 calendar days |
| Net hitbox fix (1.0.2) | quick-builder 0.5 | 1 day |

## 5. Already decided
- The Reed Pond phone performance pass runs 2026-10-21 to 10-27 and is released in the 2026-10-27 window.
- Weekly maintenance continues. Nothing else is committed.
