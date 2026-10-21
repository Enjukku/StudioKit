# Job workflows

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016, owner approval J016-D4); revised by workflow-fixer W3 · claude-opus-5-5 · high · 2026-10-21, J016 G3 (audit fixes: args table, images, code review, recapture, files only). Kit folder: universal.

One saved Claude Code workflow per job type. `tools/sync_harness.py` copies each `job-<type>.js` byte for byte to `.claude/workflows/`, where `meta.name` becomes the slash command `/job-<type>`. Never edit the copies. Codex runs the same stages by hand from the `orchestration` skill's `references/job-types.md`.

## Contract every job workflow keeps
| Rule | Why |
| --- | --- |
| One stage per call: `direction`, `proof` (L only), `build`, `repair`. An arg that switches a rule or a gate has no default: a missing or wrong one returns `blocked` before any agent starts, with the list of what is needed (`required`) | a workflow cannot pause for the owner (capability check C07); lead decision LD9 |
| Images: an image step writes its prompts first and generates only when its tools include the built-in browser and `imagesApproved` is true; otherwise it writes `image-prompts.md` next to its deliverable, returns `images: pending` and the stage result lists the batch in `images_pending`. Pending G1 pictures do not fail direction (signers judge the prompt rows); a pending batch that later steps in the same call build on (storyboards, a reference set, UI icons and item art, kit model sheets, a green light or render) stops the stage as `blocked` there, so nothing is built or reviewed on unapproved images. The lead runs the batch with the owner between stages and passes the approved paths in `images`. Visual work never starts without an approved image path in its brief | lead decision LD2; `reference-images` §4; AGENTS.md §3.5 |
| No agent ids and no messages: sideways work goes through files in a fixed order (the producer writes, the consumer answers on that file, the owner of the contract merges). VFX writes each envelope first; sound answers on it | lead decisions LD1, LD3; owner goal "sound needs the VFX timing" |
| Review chain: scripts first in every round (a FAIL stops the other reviews until it is fixed), then Studio checks one after the other beside the code review and the creative order. Every candidate with code (player code, wiring, remotes, saves) has the `reviewer` | `rules/company.md` §7; lead decision LD15 |
| Repairs go to the makers in dependency order; a moved time makes VFX and sound recheck. After every repair round the candidate is re-imported, rebuilt and recaptured before the next review round | reviewers never judge stale captures |
| Repair rounds: code findings 3, other findings 2, interface rounds 2; then `needs-decision` | `rules/company.md` §9; lead decision LD5 |
| A role the workflow cannot route (a finding's maker or an affected role) returns `needs-decision`; a dead agent (null) is `failed`, never a pass | nobody drops work silently (`rules/company.md` §8) |
| Every `agent()` call sets `agentType` (the role), `model`, `effort` and the hand-back schema of `templates/jobs/handback.schema.json` (evidence before answers, `docs_read`, optional `lesson`); findings carry expected and observed | `rules/messages.md` §2-3, §6; lead decision LD11 |
| Every brief is built in the `rules/messages.md` §2 shape: `<intent>`, `<spec>` with packet line, `owner_words`, refs, inputs with revisions, owns, rules, `findings` for repairs, deliver, checks | quality: complete briefs |
| Code file ownership comes from a contract's Code file owners table, set by the architect (`templates/jobs/contract-header.md`); a builder whose row is empty returns `blocked` | lead decision LD10 |
| At most 5 agents at once; one Studio writer (`studioId` from the lead), one Blender user and one built-in browser user at a time | `rules/company.md` §9 |
| Studio MCP captures stills only: sync is judged from the Output log (event, VFX and cue start on one clock); listening is an owner-confirmed G3 line. Capture briefs carry the check budget: numbers for every case, images at key frames and where a number fails, and report captures made and looked at | owner J005-D8; Studio MCP `screen_capture` |
| M jobs run the proof inside `build` (`proof` refuses size M); a look change is sized L | `rules/company.md` §2 |
| A planned role (animator) runs as a stand-in on `general-purpose` with its brief | `orchestration` skill §2 |
| The script never reads or writes files and never uses `Date.now()` or `Math.random()` | workflow runtime limits |

## Args per workflow
Every workflow takes `job` (the job folder id) and `stage`. "Stages" says where the arg is required; "opt" means optional with the default named.

| Workflow | Arg | Stages | Meaning |
| --- | --- | --- | --- |
| all | `size` | all | `M` or `L` (`rules/company.md` §2). `proof` needs `L` |
| all | `gate` | opt | the owner's words at the last gate, verbatim (shown in `owner_words`) |
| all | `imagesApproved` | opt, `false` | the owner's yes for this stage's image batch, recorded in `decisions.md`; without it image steps return `pending` |
| all but marketing art | `studioId` | proof, build, repair (stage, feature, effect, character, cutscene); build, repair (UI) | the one Studio instance this run writes to |
| all | `change` | repair | the owner's G3 change request, verbatim |
| cutscene | `images` | proof, build, repair | owner-approved reference images (the G1 look; then boards) |
| cutscene | `sequence` | opt, job slug | the sequence id under `content/film/` |
| character | `variant`, `playable` | all | `true`/`false`: variant mode (base rig, clips, anchors fixed; palette-only skips S4-S6); wired into gameplay (architect wiring contract, reviewer) |
| character | `base` | all, when `variant` | the base asset id |
| character | `images` | proof, build, repair | owner-approved directions; then the reference set |
| character | `asset` | opt, job slug | the asset id |
| stage | `images` | build, repair | owner-approved key-place references (the greybox proof has no art) |
| stage | `stageId` | opt, job slug | the stage id under `content/stages/` |
| UI screen | `shop`, `newLook` | all | `true`/`false`: the screen sells, prices or rolls (platform-policy, progression-designer); the job changes the look (must be `L`) |
| UI screen | `images` | proof, build, repair | the chosen target image first, then other approved references |
| UI screen | `screen` | opt, job slug | the screen id under `content/ui/` |
| feature | `money`, `numbers` | all | `true`/`false`: Robux, currency, purchases or saved value (money rules and skills); numbers players feel (progression-designer) |
| feature | `images` | build, repair, when the contract has visible UI or effects | the owner-approved UI target image and VFX key frames from G2 (made in the proof) |
| feature | `feature` | opt, job slug | the feature id |
| effect | `newLook`, `animated` | all | `true`/`false`: the effect sets a new look (art-director joins; must be `L`); it rides on an animation (timing list) |
| effect | `images` | proof, build, repair | owner-approved key frames or look references |
| effect | `effect`, `small` | opt: job slug, `false` | the effect id; `small` routes wiring to the quick-builder |
| marketing art | `piece`, `launch` | all | `icon`, `thumbnails` or `key-art`; `true`/`false`: a new game's launch art (marketing at high effort) |
| marketing art | `images` | proof, build, repair | the chosen rough (green light); then the green-lit image |
| marketing art | `trends` | opt, `false` | the trend-scout joins direction |

A stage result carries `status`, `outcome`, `steps`, `images_pending` (batches for the lead), `lessons` (every agent's lesson draft, for the lead to file in `knowledge/inbox/`), and the stage's own fields (`g1`, `beat_sheet`, `blocking`, `new_requests`, `required` when blocked).

## Test
`python -m unittest tools.tests.test_job_workflows` runs every script here under `tools/workflows/wf_harness.mjs` with fake agents (no tokens). The harness fails a run on: an `agent()` call without role, model, effort or schema; a schema that differs from the hand-back template; a role file missing or a model off its tier; a phase not in `meta.phases`; more than 5 agents at once; two agents holding the Studio, Blender or the browser at once; a brief that names peer messages. The tests check: bad and missing args are refused before any agent; every stage ends `done`; repair rounds are bounded; a dead agent is never a pass; pending images are listed; the cutscene recaptures after repairs, runs scripts first every round, runs VFX before sound, reviews the combined pass before polish and stops for a new cast before the animatic; code review runs wherever code is in the candidate. It is part of the gate (skipped where Node.js is not installed).

## Running one (the lead)
Only after the owner has asked for the job and answered the previous gate. Example: `Workflow({name: "job-cutscene", args: {job: "J021-boss-intro", stage: "proof", size: "L", studioId: "<id>", images: ["content/art/refs/<approved>.png"], gate: "<owner's G1 words>"}})`. A resumed run returns the cached result of every step whose brief did not change: resume after new args (for example `images` after a pending batch), but rerun fresh when only a file the agents read changed (for example a measured slot size). Report the agent count and usage at the next gate; file every entry of the result's `lessons` in `knowledge/inbox/`.
