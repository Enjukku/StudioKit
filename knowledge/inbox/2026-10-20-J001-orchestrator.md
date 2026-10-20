---
type: lesson
scope: universal
status: draft
updated: 2026-10-20
source: J001
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# J001 lessons: rebuilding engineering skills

| Field | Content |
| --- | --- |
| date | 2026-10-20 |
| job | J001 |
| agent | orchestrator |
| type | win |
| what happened | Each skill went: cheap researcher extracts cited facts (mirror path:line + dated staff posts) → lead spot-checks 3-5 surprising claims in the API yaml → lead writes SKILL.md + references + evals → owner review per skill. Spot checks caught nothing false but confirmed surprising facts (e.g. `Player:LoadCharacter` deprecated for `LoadCharacterAsync`). Owner: "Don't take this as like gospel ... this is just research." Owner papers were treated as input, checked against the docs, with a kit verdict where they did not fit Roblox. |
| evidence link | `knowledge/jobs/J001-engineering-skills/job-card.md`; commits 69b1bd6..(step 7) |
| proposed rule | For engineering skills, require a researcher fact sheet with path:line citations and a lead spot-check of the most surprising claims before writing. |

| Field | Content |
| --- | --- |
| type | win |
| what happened | The mirror's API yaml carries no beta markers; four project-authored UI pages still said "beta" months after release. Staff DevForum posts decide live vs beta. |
| evidence link | `knowledge/reference/roblox/whats-new.md` |
| proposed rule | Live or beta status of a Roblox feature comes from the newest staff post, never from the presence of an API in the yaml. |
