---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016 G3 audit
supersedes: []
---
> Author: auditor-e · claude-opus-5-5 · high · 2026-10-21

# Tabletop run of the J016 flow at 322c8ad: three owner requests, end to end

Method. I played the lead, then each agent, using only what the files tell that agent at that step. Files at commit 322c8ad. Tools I used (all read-only): `context_packet.py` with the briefs' own task strings; `wf_harness.mjs` with fake agents for call order (R1 L all stages; R2 L with `money` and `numbers` set; R3 M with `variant`, `base` and `playable` set). I did not open any `hidden-*` file. I took hidden-file paths only from packet JSON. Labels: **run** = command output this session; **read** = file lines; **silent** = no file answers the question (the likely guess follows).

Game assumption: the template `knowledge/design/game-profile.md` (every field empty except source mode `files`). There is no `art-bible.md` and no `knowledge/systems/`. To run the three requests on a real game, the kit expects these to exist already: a filled game profile (play camera, narrowest aspect, budgets, review order, Studio place ids: `game-profile.md:17-30`), `knowledge/design/art-bible.md` with an anchor register (`reference-images/SKILL.md:11`), a test place and its `studio_id`, the boss's model and rig (R1), the archer's released rig and clips at `content/rigs/<base>/` and `content/anim/<base>/` (R3, `job-character.js:48-49`), a save module and a currency system (R2, R3), a shop (R3), and a gate (`python tools/verify.py`).

## Trace R1: "Make a 20-second boss intro cutscene for our game: the boss lands on the wall and roars."

| # | Who acts | File:line that tells them | Produces | To whom, format | Owner gate |
| --- | --- | --- | --- | --- | --- |
| 1 | lead | `AGENTS.md:27` (load `orchestration`); `orchestration/SKILL.md:11` (read twice, check `active.md`, git status) | nothing yet | — | — |
| 2 | lead | `AGENTS.md:21` packet "for your role" | **run:** `--role orchestrator` exits 2 "unknown role"; `--job J099-tabletop` exits 2 "unknown job"; with no flags the packet ranks film-direction, roblox-assembly and Event Sequencer and does not rank `game-profile.md` | — | — |
| 3 | lead | `company.md:28` (L lists "cutscene"); `SKILL.md:23` (boss intro → cutscene, job lead film-director) | size L, recipe cutscene: one answer for each (E2 ok) | job card | — |
| 4 | lead | `SKILL.md:37-40`, `templates/jobs/job-card.md` | folder, job card (owner's words first, L, leads film/art/architect, game-designer consulted `job-types.md:11`), `active.md` row, `crew.md`. Usage estimate in tokens: **silent** on how to estimate. Prerequisite check (art bible, boss rig, test place): **silent** | files | — |
| 5 | lead | `workflows/jobs/README.md:26` | `Workflow job-cutscene {job, stage: direction, size: L}`; sequence = job slug (`job-cutscene.js:30`) | workflow args | — |
| 6 | 4 leads in parallel | `job-cutscene.js:165-183` | proposals in `direction/proposal-<role>.md`. Art-director makes ChatGPT images; `reference-images/SKILL.md:38` needs the owner's yes before each download batch, which a workflow subagent cannot get → **stall or guess (TT-02)**. No art bible → the skill says write it first (`SKILL.md:11`), which is outside `owns` (`job-cutscene.js:180`) → **guess (TT-13)** | §2-shaped brief (no `peers`, no `owner_words`); hand-back schema | — |
| 7 | 4 leads | `job-cutscene.js:187-196` | `exchange/r1-<role>.md` | exchange-note format | — |
| 8 | film-director, then art + architect sign | `job-cutscene.js:199-232` | `direction.md` rev1 (template `direction-sheet.md`), sign files, ≤1 resolution round | files + schema | — |
| 9 | lead | `job-cutscene.js:233-237` (returns `g1`); `SKILL.md:69-71` | G1 packet: pictures (art images if downloaded, film blockout stills), recommendation, trade-off, usage estimate; one digest | owner, `decision-digest.md` | **G1** |
| 10 | lead | `SKILL.md:16`, `README.md:26` | records the owner's words and revision in `decisions.md`; calls stage proof with `gate` words. The args carry no approved revision (TT-14) | workflow args | — |
| 11 | film-director | `job-cutscene.js:243-254` | `beat-sheet.md` rev1 + `shots.json`; readiness table; `new_cast_needed` is returned and **ignored** (TT-12) | consumers listed | — |
| 12 | animator stand-in, env, vfx, sound, architect | `job-cutscene.js:256-280` | `exchange/p<n>-<role>.md`; film merges ≤2 rounds. The stand-in's packet uses `--role character-rigger` (`:130`, TT-24) | exchange notes | — |
| 13 | environment-designer (if greybox) | `job-cutscene.js:283-294` | greybox set. Studio "only the studio_id the lead names in the job card": the template has no such field, and proof does not need `studioId` (`:40`) → **guess (TT-32)** | files | — |
| 14 | sound, vfx (parallel); film | `job-cutscene.js:295-320` | temp cues, frame-script marks; boards (reference-images: download yes again, TT-02) + timed animatic | files | — |
| 15 | art → architect | `job-cutscene.js:322-351` | `reviews/animatic-rev<n>-<role>.md`, ≤2 repairs. The Studio probe the architect named at D1 (`:168`) never runs (TT-23) | review format | — |
| 16 | lead | `SKILL.md:53`, `:70` | G2 packet: animatic + boards | owner | **G2** |
| 17 | 6 crafts, then film | `job-cutscene.js:357-375` | `exchange/b1-*.md`, locked beat sheet. If the boss has no usable rig → `needs-decision` "open a character job" **after G1 and G2** (TT-12) | digest | extra owner decision |
| 18 | env → art check-in → env; animator → film check-in → animator; UI | `job-cutscene.js:380-432` | set (Studio, only writer), clips + `timing-list.md`, UI spec. Animator inputs name no rig path (`:409`, TT-24) | files | — |
| 19 | vfx ∥ sound | `job-cutscene.js:435-451` | both read the timing list and both b1 notes: sound gets picture timing (works) | files | — |
| 20 | animator, film, feature-builder, film | `job-cutscene.js:453-485` | import, scene data, player code (owns "the source files the architect named … (see the job card)" `:473` → **guess (TT-04)**), candidate captures | `evidence.md` | — |
| 21 | qa ∥ perf (Studio), film → art → sound (captures) | `job-cutscene.js:488-551` | reviews, repairs by maker, recapture. **No code review** of the player code (TT-03) | review format | — |
| 22 | lead | `SKILL.md:62-66`, `:70` | readiness, G3 packet | owner | **G3** |
| 23 | lead + doc-keeper | `SKILL.md:73-82` | vault filing. Lesson drafts from workflow agents: none (TT-10) | files | — |

E1 for R1: G3 is reachable on paper when the boss already has a rig. The trace stalls at step 6 (image downloads), at step 17 when the cast is new, and at step 20 (file owners are a guess). Code review never runs.

## Trace R2: "Add a daily reward chest that gives coins each day you log in."

| # | Who acts | File:line | Produces | To whom, format | Owner gate |
| --- | --- | --- | --- | --- | --- |
| 1 | lead | `AGENTS.md:21`, `:40` | **run:** the owner-text packet ranks `knowledge/jobs/J011-progression-designer/evals-hidden.md` #6, with its rubric excerpt printed (TT-01). Coins + saved claim state → platform-policy, data-saving, networking-security, analytics apply (`AGENTS.md:40`) | — | — |
| 2 | lead | `company.md:27-28` | M ("a system") **or** L ("feature with UI + VFX + sound"). The crafts are known only at P1 (`job-feature.js:290`, after G1) → two answers (TT-08). Recipe: feature (`SKILL.md:27`) or UI screen ("reward reveal", `design-jobtypes.md:80`) → closest type (`SKILL.md:32`) | job card | — |
| 3 | lead | `job-feature.js:4` whenToUse "money?, numbers?"; meaning only in comments `:31-32` | must set `money: true`, `numbers: true`. `SKILL.md:14` documents only `{job, stage}` (TT-05) | workflow args | — |
| 4 | game-designer, architect, progression-designer | `job-feature.js:197-230` | proposals (game profile is empty); with `money` the skills add platform-policy (`:129-134`) | files | — |
| 5 | same | `job-feature.js:232-268` | exchange notes, `direction.md` rev1, signatures | files | — |
| 6 | lead | `job-feature.js:268-272`; `job-types.md:72` | G1 in player words, risky claims, usage. The options have no pictures (`:83`) although `company.md:30` says pictures (TT-22) | owner | **G1** |
| 7 | game-designer | `job-feature.js:273-292` | `contract-daily-reward.md` rev1, `crafts_not_needed`; input `direction.md` not pinned (`:282`) | consumers | — |
| 8 | arch, prog, ui, vfx, sound (parallel) | `job-feature.js:296-312` | needs notes. VFX and sound "read each other's note if it exists" while they run at the same time; the loop ends if no conflicts (`:307`) | exchange notes | — |
| 9 | feature-builder (Studio) | `job-feature.js:323-339` | grey-box prototype, no UI/VFX/sound (`:329`) | `prototype/notes.md` | — |
| 10 | studio-operator → game-designer → architect | `job-feature.js:346-379` | captures per case (no light-check rule, TT-11), reviews, ≤2 repairs | review format | — |
| 11 | lead | `job-feature.js:670` | G2: prototype captures | owner | **G2** |
| 12 | architect; qa-lead | `job-feature.js:417-458` | plan with analytics events (analytics skill not loaded, `:420`, TT-25), builder brief, test seeds; protected acceptance tests | files | — |
| 13 | builder ∥ prog ∥ ui ∥ vfx ∥ sound | `job-feature.js:463-538` | code; tables; UI makes its target image in build (`ui-ux-designer.md:39`), so the owner never sees it before G3 (TT-07), and the download needs the owner's yes (TT-02); VFX and sound "agree the envelope" with no channel (`:508`, `:523`, TT-06) | files | — |
| 14 | feature-builder | `job-feature.js:541-560` | integration (+`analytics` skill `:545`), gate PASS | `evidence.md` | — |
| 15 | studio-operator; reviewer ∥ qa ∥ perf; game-designer → art-director | `job-feature.js:562-628` | captures ("a clip per case … every visible state" `:573`), code review (present), reviews; code 3 rounds, others 2 | review format | — |
| 16 | lead | `SKILL.md:62-71` | readiness, G3 | owner | **G3** |

E1 for R2: G3 is reachable on paper only when the lead sets `money`. Agents must guess at step 13 (envelope, image download, a reference the owner has not seen).

## Trace R3: "Make a gold version of the archer skin to sell in the shop."

| # | Who acts | File:line | Produces | To whom, format | Owner gate |
| --- | --- | --- | --- | --- | --- |
| 1 | lead | `AGENTS.md:40` (load platform-policy at design time) | **run:** the owner-text packet gives the same 12 hits for art-director, modeler, game-designer, character-rigger and ui-ux-designer (TT-16). No platform-policy note is in the top 12 | — | — |
| 2 | lead | `company.md:27-28`; `SKILL.md:24`, `:32` | M (recolour inside the style) **or** L (asset + sale = several crafts) (TT-08). Recipe: character variant for the skin. The sale is "shop logic" (`job-feature.js:4`); the closest type is character, so the sale has no recipe (TT-09) | job card | — |
| 3 | lead | `job-character.js:4`, `:33-35` | args `variant`, `base`, `playable`, `studioId` (proof onward `:54`): none of these is in `SKILL.md` (TT-05) | workflow args | — |
| 4 | game-designer (+platform-policy), art-director, rigger, animator stand-in | `job-character.js:251-297` | proposals. Art: palette directions that keep the base anchors "in the art bible anchor register" (`:196`): absent in the template (TT-13). Image downloads need the owner's yes (TT-02) | files | — |
| 5 | same; art-director synthesises | `job-character.js:299-340` | `direction.md` with directions beside the base. Price: **silent** (only "how players get it", `:255`) | files | — |
| 6 | lead | `job-character.js:337-339` | G1: pictured directions | owner | **G1** |
| 7 | (M) proof inside build: art ref set, gameplay sheet, rigger S0, modeler blockout, rigger proxy pose; art → animator → designer review | `job-character.js:344-500`, `:945-948` | reference set, rig sheet; S1-S2 skipped (`:389`) | files | — (M: no G2) |
| 8 | modeler S3 → art check-in → polish; rigger S4-S6; icons | `job-character.js:527-711` | full geometry and rig rebuild for a palette-only change (`:527`, `:595`, TT-27) | files | — |
| 9 | animator import; feature-builder wiring (data-saving, platform-policy, networking-security) | `job-character.js:731-760` | equip ownership check + saved equip. "If the job card names no files … return blocked" (`:756`) → **stall** (no field, no architect, TT-04). Purchase, price and shop listing: **not in any step** (TT-09) | code | — |
| 10 | animator capture; qa scripts → art → game-designer ∥ perf | `job-character.js:761-790` | reviews. **No code review** of the save wiring (TT-03) | review format | — |
| 11 | lead | `SKILL.md:66` readiness | the owner's "to sell in the shop" has no evidence → a second job or `needs-decision` | digest | **G3** or an extra decision |

E1 for R3: the skin can reach G3. The sale stalls at step 9 or step 11 because no recipe step builds it.

## Checks

| Check | Result | Findings |
| --- | --- | --- |
| E1 reach G3 | R1 conditional; R2 conditional on the `money` arg; R3 the skin yes, the sale no | TT-02, TT-04, TT-09, TT-12, TT-13 |
| E2 one size, one recipe | R1 yes; R2 and R3 no | TT-08, TT-09 |
| E3 handoff formats | briefs, exchange notes, reviews and hand-backs have formats and receivers. Gaps: no `peers` or `owner_words`; findings lack expected/observed; contract-change notices cannot reach consumers by message; lesson drafts have no channel | TT-06, TT-10, TT-19, TT-20, TT-21 |
| E4 binding rules reach | platform-policy, data-saving, networking-security: R2 only with `money`; R3 wiring only. Analytics: R2 at integration only; R3 never. Reference first: R2 UI/VFX not owner-seen. Light checks: not to the capture maker. Code review: missing in R1 and R3 | TT-03, TT-05, TT-07, TT-09, TT-11, TT-25, TT-26 |
| E5 owner only at gates + digest | gates and digest are correct; reference-image download approval asks the owner outside both | TT-02, TT-22, TT-31 |
| E6 context given / withheld | packets give the held-out keys to working agents; the role boost does nothing; the packet does not withhold D1 proposals; the lead has no packet role | TT-01, TT-15, TT-16, TT-17, TT-18 |

## Review block (rules/messages.md §6)

```text
<spec>
artifact: StudioKit@322c8ad (AGENTS.md, rules/, .agents/skills/orchestration/, .agents/roles/, .agents/workflows/jobs/job-{cutscene,feature,character}.js, templates/jobs/, tools/context_packet.py)
reviewer: auditor-e
looked_at_first: [orchestration/SKILL.md, references/job-types.md, rules/company.md, rules/messages.md, rules/knowledge.md, the three workflow scripts, harness runs, packet runs; design.md only to tell a defect from intended behaviour]
findings:
  - id: TT-01
    class: blocking
    where: "tools/context_packet.py:57 (DEFAULT_EXCLUDE), :371-375 (_excluded); rules/knowledge.md:51"
    expected: "held-out keys (hidden-*) are never opened or listed by content (knowledge.md:51); briefs say 'Never open a file whose name starts with hidden-' and 'open only what it [the packet] cites' (job-cutscene.js:101-104)"
    observed: "the packet indexes and lists hidden keys, with excerpts, and tells the agent to open them"
    evidence: "run, with the workflows' own task strings: 'icon renders of the shipped model: archer-gold' → rank 1 knowledge/jobs/J007-modeler/hidden-answers.md, read_next 'open knowledge/jobs/J007-modeler/hidden-answers.md L56-63'; 'answer the modeler's counter-proposals: archer-gold' → same file rank 1 + read_next; 'rebind and retest on the fixed geometry' → J008 hidden-answers.md #9; 'apply owner change: daily-reward' → J013 hidden-rerun2/q4.md #6; R2 owner text → J011 evals-hidden.md #6 with its rubric lines printed; 'cutscene letterbox, subtitles and skip UI' → read_next 'open knowledge/jobs/J015-film-director/evals-hidden.md L42-49'; grader keys (J014 grader/T07-key.md) at #10-12. grep 'hidden' tools/context_packet.py = 0 lines. kit.json context.exclude not set."
    smallest_fix: "exclude hidden-*, *-hidden*, grade*-hidden*, grader/ and hidden-run*/ paths at index time (kit.json context.exclude or a name filter in _excluded), add one retrieval eval case that fails if any such path appears, and extend the knowledge.md:51 name rule to the evals-hidden.md and grader/ forms"
  - id: TT-02
    class: blocking
    where: ".agents/skills/reference-images/SKILL.md:38; rules/company.md:19; .agents/workflows/jobs/README.md:10"
    expected: "a workflow subagent can finish its visual step without talking to the owner (crafts never go to the owner, company.md:19; a workflow cannot pause, README.md:10; owner questions only at gates and in the one digest, SKILL.md:69)"
    observed: "reference-images step 4 says the generating agent must 'ask the owner once per batch to approve the downloads … never download without that yes'. Agents that must do this inside a workflow: art-director D1 (job-cutscene.js:175, job-character.js:274), film-director boards P5 (job-cutscene.js:314-315), art-director reference set (job-character.js:349-356), ui-ux-designer B4 (ui-ux-designer.md:39, job-feature.js:492). None has a channel to the owner"
    evidence: "R1 step 6 and 14, R2 step 13, R3 step 4 and 7. The agent must choose: download without the yes (breaks the rule), skip the pictures (G1 has none), or return blocked (the stage fails)"
    smallest_fix: "add one rule in reference-images §4 and the workflow briefs: inside a job stage, the generator leaves the images in their ChatGPT tabs and lists the batch in its hand-back; the lead puts one download question per stage in the digest; or the lead records one standing yes per job in decisions.md and the brief cites it"
  - id: TT-03
    class: blocking
    where: "job-cutscene.js:45-61 (ROLE has no reviewer), :490-498; job-character.js:59-71, :781-790; job-types.md:19, :35"
    expected: "'before any merge: code-review' (AGENTS.md:40); 'Before merge your change goes to the reviewer' (feature-builder.md:17)"
    observed: "the cutscene player code (B6-player :470) and the variant's ownership and save wiring (S7-wiring job-character.js:748) go to G3 with no reviewer step. The job-feature chain has one (job-feature.js:585)"
    evidence: "harness build runs: R1 labels end qa-lead, film-director, performance-engineer, art-director, sound-designer; R3 labels end qa-lead, performance-engineer, art-director, game-designer; no 'reviewer:' label"
    smallest_fix: "when a stage wrote code, add the reviewer (skills code-review + the area skills, effort high for saves) to the tech list of both review chains and to job-types.md §1, §2 review order"
  - id: TT-04
    class: blocking
    where: "job-cutscene.js:473; job-character.js:756; templates/jobs/job-card.md:7-16; orchestration/SKILL.md:38"
    expected: "code briefs state the files owned (SKILL.md:88); the owner of that list writes it where the brief points"
    observed: "R1 B6 owns 'the source files the architect named for the cutscene player (see the job card)'. The architect names them only in direction/proposal-architect.md (D1, :180). The cutscene build stage has no architect plan step. Nobody writes the files into the job card, and the template has no field for them. R3 S7 wiring: 'If the job card names no files for this wiring, return blocked'. The character recipe has no architect"
    evidence: "R1 step 20 (the feature-builder guesses the file list, which changes what it may edit); R3 step 9 (stalls at blocked)"
    smallest_fix: "add a 'Files owned (code)' row to job-card.md and a step in SKILL.md §3/§1.5: the lead copies the architect's file owners there before build (for character jobs the lead asks the architect once); or point both briefs at the architect's proposal/plan file"
  - id: TT-05
    class: blocking
    where: "job-feature.js:31-32, :52-53, :124-134; job-character.js:33-35; orchestration/SKILL.md:14; workflows/jobs/README.md:10"
    expected: "platform-policy, data-saving and networking-security reach every agent on a coin or save feature (AGENTS.md:40); the lead knows every arg that turns them on"
    observed: "the rules and skills attach only when args.money is true (default false); the builder and reviewer drop to medium effort. SKILL.md documents args {job, stage}; README says 'plus type-specific keys' and lists none. The meaning of money ('Robux, currency, purchases or saved value') is a code comment. Same for numbers (progression-designer joins), variant, base, playable"
    evidence: "R2 step 3: a lead that follows SKILL.md:14 literally runs job-feature without money; then no brief carries MONEY_RULES, and qa-lead and the reviewer get no data-saving skill. R3 step 3: without playable the variant is never wired"
    smallest_fix: "add an args column to SKILL.md §2 (cutscene: sequence; character: asset, variant, base, playable; feature: feature, numbers, money; with one line of meaning each), and make job-feature return blocked when money is not given explicitly"
  - id: TT-06
    class: blocking
    where: "job-feature.js:507-535 (B5, B6), :296-307 (P2)"
    expected: "VFX and sound co-design each shared event's envelope before either builds (job-types.md:86; owner goal 'sound needs the VFX timing')"
    observed: "B5 and B6 start in parallel. Each is told to 'agree with' the other and 'read its note if it exists'. No peers id is given (grep peers in job-feature.js = 0), no envelope file is named, no step merges the envelopes, and sound's inputs are [contract, PLAN] only (:525). P2 is also parallel and ends after round 1 when no conflict is listed (:307)"
    evidence: "R2 step 8 and 13; harness build labels: 'vfx-designer: B5-vfx', 'sound-designer: B6-sound' in one parallel lane set"
    smallest_fix: "run B6 after B5 with content/vfx/<feature>/ frame scripts as a sound input, or add one envelope round (both write exchange notes, the game-designer merges the envelope times into the contract) before the lanes"
  - id: TT-07
    class: blocking
    where: "job-feature.js:83 (OPTION has no pictures), :329 (prototype avoids UI, VFX, sound), :492-503 (B4 after G2); reference-images/SKILL.md:63"
    expected: "'No visual build starts from a reference the owner has not seen when the work is new-look (an L job's G2)' (reference-images/SKILL.md:63); 'Visual work starts from an approved reference image' (AGENTS.md:48)"
    observed: "in an L feature with a visible chest and reveal, G1 has no pictures, G2 is a grey-box without UI or effects, and the UI target image is made and chosen by the ui-ux-designer inside build (ui-ux-designer.md:39: 'the owner picks when the brief has a gate'; B4 has no gate). The owner sees the look first at G3"
    evidence: "R2 steps 6, 9, 11, 13"
    smallest_fix: "when the contract lists visible parts, the G2 packet adds the UI target image and VFX key frames (made in proof) for the owner, or B4/B5 return their target images for a digest yes before styling"
  - id: TT-08
    class: blocking
    where: "rules/company.md:27-28"
    expected: "sizing gives one answer for each request before work starts (company.md:22)"
    observed: "R2: M 'a system' vs L 'feature with UI + VFX + sound'. The crafts are known only at the P1 contract (job-feature.js:290), after G1. R3: M 'an asset inside an approved style' (recolour) vs L 'several crafts' (asset + sale + saved ownership). The answer decides whether the owner gets G2"
    evidence: "R2 step 2, R3 step 2; workflows default to L when size is omitted (job-feature.js:29, job-character.js:30)"
    smallest_fix: "add two sizing lines to company.md §2: 'crafts not yet known → size by the most likely contract and resize at G1'; 'anything sold, granting currency or saving player data → L unless the owner says otherwise' (or state the intended rule)"
  - id: TT-09
    class: blocking
    where: "orchestration/SKILL.md:32; job-character.js:749-757; job-types.md:37"
    expected: "every part of the owner's request has a recipe step, and the paid item gets platform-policy, data-saving (receipt) and analytics where they are built (AGENTS.md:40)"
    observed: "'Mixed or unclear → the lead picks the closest type'. For R3 the closest type is character variant. Its wiring only checks ownership before equip and saves the equip state. No step sets a price, builds the purchase (ProcessReceipt or pass), lists it in the shop, or logs the sale (no 'analytics' in job-character.js). No ui-ux-designer is in its ROLE. R2: 'popup, reward reveal' is a UI-screen item (design-jobtypes.md:80) but sits inside the feature job"
    evidence: "R3 steps 2, 9 and 11: the owner's 'to sell in the shop' has no evidence at readiness"
    smallest_fix: "extend the 'Mixed' row: when a request spans two recipes, open one job per recipe with a shared contract (as for live updates, SKILL.md:31); for 'sell a variant', name the pair job-character (variant) + job-feature (money, numbers)"
  - id: TT-10
    class: blocking
    where: "job-cutscene.js:103 (and the same BASE_RULES in job-feature.js, job-character.js); templates/jobs/handback.schema.json (additionalProperties false); job-cutscene.js:81"
    expected: "every agent writes a lesson draft at a gate answer or job end (knowledge.md:105; SKILL.md:82; role files, e.g. film-director.md:50); hand-backs list 'Docs read' (AGENTS.md:22; job-feature.js:109)"
    observed: "workflow briefs say 'Write only inside owns', and no owns contains knowledge/inbox/. The role-file fallback 'lesson_draft: in the hand-back' (art-director.md:55) and a 'Docs read' list cannot pass the schema, which refuses unknown fields. grep 'lesson' in the three scripts = 0"
    evidence: "R1 step 23: at close the lead has no drafts from the 25+ workflow agents; the learning loop (J016-D2) starts empty"
    smallest_fix: "add lesson_draft (cause, layer, text) and docs_read to HANDBACK_PROPS and handback.schema.json; the lead files the drafts at each gate"
  - id: TT-11
    class: blocking
    where: ".agents/roles/studio-operator.md:15-18, :30; job-feature.js:573"
    expected: "owner rule J005-D8 (knowledge/jobs/J005-character-rigger/decisions.md:22; company.md:101): numbers for every case, images only for a failing number plus a few key cases"
    observed: "the studio-operator's Read first does not include company.md. Its work method says to shoot 5 views of all visible work, and its R2 capture brief asks for 'a clip per case, phone and desktop shots of every visible state'. The light-check line is only in the reviewers' briefs (:583), and the reviewers can judge only those captures"
    evidence: "R2 steps 10 and 15"
    smallest_fix: "add company.md §7 to the studio-operator's Read first, replace :30 with the light-check rule, and add the J005-D8 line to the capture briefs (job-feature P4, RV capture)"
  - id: TT-12
    class: blocking
    where: "job-cutscene.js:94, :254, :375; job-types.md:15"
    expected: "one answer to 'the boss has no rig'; found before the owner approves G1 scope and usage"
    observed: "job-types.md:15 says to run the rig-sheet steps inside the cutscene for a new cast. The workflow returns needs-decision 'the lead opens a character job' (:375). P1 already returns new_cast_needed and readiness_missing (:94), but proof ignores them (:254), so the stop comes at B1 lock after G1 and G2"
    evidence: "R1 steps 11 and 17"
    smallest_fix: "check new_cast_needed after P1 and return needs-decision before the animatic; change job-types.md:15 to the same rule"
  - id: TT-13
    class: blocking
    where: "orchestration/SKILL.md:10-18, :36-40; reference-images/SKILL.md:11; job-cutscene.js:180; job-character.js:196"
    expected: "the lead checks the job's prerequisites (game profile fields, art bible, base assets, test place) at intake, or the brief owns what the skill tells the agent to create"
    observed: "with the template game the reference-images skill tells the art-director to write the art bible first and get the owner's approval of its locks. The D1 brief owns only the proposal and content/art/refs/, and no gate asks for the lock approval. The variant's fixed 'identity_anchors: the base anchors in the art bible anchor register' points at a file that does not exist"
    evidence: "R1 step 6, R3 step 4; ls knowledge/design (no art-bible.md); game-profile.md:17-30 empty"
    smallest_fix: "add an intake step in SKILL.md §1: list the missing prerequisites (art bible, filled profile rows, base rigs, studio_id) and put them in the G1 digest, or open the art-bible work before D1"
  - id: TT-14
    class: recommendation
    where: "job-cutscene.js:247, :362, :385; job-feature.js:282; README.md:10 (args carry gate words, not the approved revision)"
    expected: "every input with its revision (messages.md:82); approval bound to a revision (company.md:34)"
    observed: "proof and build briefs list direction.md and beat-sheet.md without @rev. This conflicts with messages.md:82. It is a recommendation, not blocking, because BASE_RULES send agents to decisions.md, where the lead records the approved revision, and job-feature's contractIn() already uses '@<the revision approved at G2, named in decisions.md>'"
    evidence: "R1 steps 10-11, R2 step 7"
    smallest_fix: "use the contractIn() pattern for direction.md and the beat sheet, or add args.approved {direction: n} and pin it"
  - id: TT-15
    class: recommendation
    where: "AGENTS.md:21; tools/context_packet.py:1049, :1086"
    expected: "the lead and every brief can run its packet"
    observed: "the lead has no role file, and '--role orchestrator' exits 2. '--job' exits 2 before the folder exists, or on a wrong slug. Then every workflow agent's packet line fails, and no file says what to do"
    evidence: "run: 'unknown role `orchestrator`', 'unknown job `J099-tabletop`', exit 2"
    smallest_fix: "accept --role orchestrator (the orchestration skill), and fall back to no job block with a warning instead of exit 2"
  - id: TT-16
    class: recommendation
    where: "rules/knowledge.md:38; tools/context_packet.py (ROLE_BOOST)"
    expected: "--role ranks the role's notes higher"
    observed: "no note has a roles: field (grep: only knowledge.md and inbox/README.md, as examples). The R3 ranked lists are the same for 5 roles"
    evidence: "run: the same 12 paths for art-director, modeler, game-designer, character-rigger and ui-ux-designer"
    smallest_fix: "tag the role-critical notes (recipes, platform-policy references, docs-map) with roles:, or boost the role's own skills' files"
  - id: TT-17
    class: recommendation
    where: "tools/context_packet.py read_next"
    expected: "'load skill X' points to SKILL.md"
    observed: "read_next says 'load skill `architecture` (.agents/skills/architecture/evals/briefs.md)'. The same happens for film-craft, ui-design, sound-design and rigging-craft: an eval brief, with its pass criteria, is given as the skill's entry"
    evidence: "packet sweep: 'build the feature: daily-reward', 'feature UI states: daily-reward', 'fix review findings: daily-reward' and others"
    smallest_fix: "point read_next at the skill's SKILL.md; decide whether skill evals/ are indexed at all (question Q3)"
  - id: TT-18
    class: recommendation
    where: "tools/context_packet.py:111 (JOB_BOOST), knowledge.md:47"
    expected: "D1 proposals are withheld from other leads"
    observed: "the packet has no filter for direction/proposal-*. D1 agents start in parallel, and a slower agent's packet with --job boosts the job folder. Not observed in a run (no live job)"
    evidence: "grep 'proposal|withh' tools/context_packet.py = 0 lines"
    smallest_fix: "skip direction/proposal-* in packets when the task contains 'direction proposal'"
  - id: TT-19
    class: recommendation
    where: "orchestration/SKILL.md:16, :56, :59; templates/jobs/crew.md:8"
    expected: "briefs carry peers ids from crew.md; repairs resume the maker by id"
    observed: "no workflow brief has peers (grep = 0 in the three scripts). agent() returns no id, so the lead cannot fill crew.md for workflow agents. Repairs spawn fresh FIX agents. Contract-change notices (messages.md:135) become change-table rows only. Role files tell agents to use 'your brief's peers or crew.md' (e.g. film-director.md:24)"
    evidence: "R1 steps 12, 17, 19; R2 step 13"
    smallest_fix: "state in SKILL.md §6 and in the role files that inside a workflow the sideways channel is exchange/ files only"
  - id: TT-20
    class: recommendation
    where: "job-cutscene.js:114-149 (brief builder); messages.md:37"
    expected: "owner_words in briefs that touch taste"
    observed: "workflow briefs have no owner_words key. They say 'Read job-card.md first' and add the last gate's words to the intent"
    evidence: "brief() in all three scripts"
    smallest_fix: "add args.owner_words (from the job card) and print it in every creative brief"
  - id: TT-21
    class: recommendation
    where: "job-cutscene.js:86-87 (FINDING), job-feature.js:88-89, job-character.js:99-100"
    expected: "findings name expected and observed (messages.md:155)"
    observed: "the schema has no expected or observed fields, and the repair briefs pass JSON.stringify(findings) to the maker"
    evidence: "job-cutscene.js:536"
    smallest_fix: "add expected and observed to FINDING"
  - id: TT-22
    class: recommendation
    where: "rules/company.md:30; job-types.md:72"
    expected: "one G1 rule"
    observed: "company.md says G1 options are 'shown as pictures'. The approved feature recipe shows the behaviour in player words, with no pictures field. This is intended (design-jobtypes.md §5) but company.md does not say so"
    evidence: "R2 step 6"
    smallest_fix: "company.md:30 adds 'features: player words; pictures where the contract has visible parts'"
  - id: TT-23
    class: recommendation
    where: "job-cutscene.js:168, :40, :322-326"
    expected: "the Studio probes the architect names at D1 run before G2"
    observed: "proof has no probe step and needs no studioId. The architect only reviews the animatic for cost"
    evidence: "R1 step 15; harness proof labels: no architect probe"
    smallest_fix: "an architect probe step in proof when its D1 proposal lists probes (studioId then required)"
  - id: TT-24
    class: recommendation
    where: "job-cutscene.js:130, :409; job-character.js same pattern"
    expected: "the stand-in animator gets animator context and the cast's rig"
    observed: "the packet is --role character-rigger, so the role block shows the rigger's role file and skills. The B3 inputs list no rig or model path"
    evidence: "R1 steps 12 and 18"
    smallest_fix: "keep the docs row (it is shared) but suppress the rigger role file in the stand-in packet; add the cast rig path (from the readiness table) to B3 inputs"
  - id: TT-25
    class: recommendation
    where: "job-feature.js:419-420"
    expected: "analytics loaded when the design adds a currency source (AGENTS.md:40)"
    observed: "the architect plans the analytics events with skills [architecture, engineering-craft, performance]. Analytics loads only at integration (:545). No analyst or progression check on what to log"
    evidence: "R2 step 12"
    smallest_fix: "add analytics to the B1 skills when money or numbers is set"
  - id: TT-26
    class: recommendation
    where: "job-character.js:749-757"
    expected: "the rules the work must keep are restated in the brief (messages.md:34)"
    observed: "the skills are named (data-saving, platform-policy), but none of job-feature's MONEY_RULES text is restated"
    evidence: "compare job-feature.js:124-128"
    smallest_fix: "share MONEY_RULES with job-character for variant wiring"
  - id: TT-27
    class: recommendation
    where: "job-character.js:527, :595; job-types.md:37"
    expected: "a palette-only variant has a light path"
    observed: "S3 'Build the final model … the rigger's cuts', S4 and S5 rebind and export all run. The agent must decide alone whether 'build' means copying the base and retexturing"
    evidence: "R3 step 8; harness R3 build: 22 agents"
    smallest_fix: "variant + no geometry change → S3 is texture-only and S4-S6 are skipped (base rig released)"
  - id: TT-28
    class: recommendation
    where: "rules/company.md:67"
    expected: "the close-out pointer targets the filing rules"
    observed: "it points to 'rules/knowledge.md §5' (Notes). Filing is §7 (AGENTS.md:68 uses §7)"
    evidence: "knowledge.md:101"
    smallest_fix: "§5 → §7"
  - id: TT-29
    class: recommendation
    where: "AGENTS.md:45"
    expected: "one gate command"
    observed: "AGENTS.md names powershell tools/verify.ps1, which does not exist. claude.md:34 and the workflows use python tools/verify.py"
    evidence: "ls tools/verify* → tools/verify.py only"
    smallest_fix: "AGENTS.md:45 → python tools/verify.py"
  - id: TT-30
    class: recommendation
    where: "AGENTS.md:22; company.md:92, :124; design.md:176"
    expected: "a workflow agent knows whether it may spawn explore or researcher"
    observed: "workflow agents are at depth 2 (lead → workflow → agent), and the kit limit is 2. AGENTS.md tells them to send a scout, which would be depth 3. The fallback 'no agent tool: grep yourself' covers this only when the tool is missing"
    evidence: "R1 step 6 for the architect and film-director (both have Agent)"
    smallest_fix: "AGENTS.md:22: 'inside a workflow, grep the mirror yourself'"
  - id: TT-31
    class: recommendation
    where: "SKILL.md:38, :70, :105; README.md:26"
    expected: "the lead can state the usage estimate at G1 and the actual usage at each gate"
    observed: "no per-recipe baseline exists, and the workflow results carry an agent count only (no usage)"
    evidence: "harness runs: R1 47 agents L, R2 33, R3 34 (M) on the clean path"
    smallest_fix: "a per-recipe agent-count and token baseline table in job-types.md (seed with the harness counts), and the actual from the Workflow result (Q1)"
  - id: TT-32
    class: recommendation
    where: "job-cutscene.js:292, :40"
    expected: "the greybox step knows its studio_id"
    observed: "'only the studio_id the lead names in the job card': the job card has no such field, and the proof stage does not take studioId"
    evidence: "R1 step 13"
    smallest_fix: "pass args.studioId to proof when greybox is possible, or say Blender only"
  - id: TT-33
    class: new request
    where: "job-feature.js:90-91 (CRAFT_OUT ui/vfx/sound), :187 (MAKERS without modeler); job-types.md"
    expected: "a feature that needs a world prop (a 3D chest) has someone to model it"
    observed: "no recipe or lane covers a standalone prop. The modeler appears only in the character and stage recipes"
    evidence: "R2: if the game-designer's contract puts the chest in the world, repair routing returns needs-decision"
    smallest_fix: "owner decision: a prop lane in job-feature (modeler + art-director check-in), or a 'prop' recipe"
keep:
  - "STATUS, coverage, built_on, checks with evidence in every schema; evidence fields before status (all three scripts)"
  - "independent D1 with other proposals in avoid; one exchange; job-lead synthesis; signatures; exactly one resolution round (job-cutscene.js:165-232)"
  - "bad args and missing studioId return blocked before any agent starts; one Studio writer sequencing in production and review chains"
  - "recapture and refreeze after every repair round (job-cutscene.js:543-549, job-character.js REFREEZE)"
  - "unroutable maker roles return needs-decision instead of dropping work"
  - "job-feature MONEY_RULES: complete rules in full words, restated in every brief; reviewer with the harm order; code 3 rounds vs other 2"
  - "job-character's explicit 'return blocked with the files you need' instead of a guess (job-character.js:756)"
  - "contractIn()'s '@<the revision approved at G2, named in decisions.md>' pin"
  - "the light-check line in every review-chain brief; variant fixed items with needs-decision on change"
  - "cutscene check-ins (art before final light, film before polish) and VFX/sound both reading the animator's timing list (job-cutscene.js:435-451)"
  - "the packet's Job block listing the canonical job files with revisions"
verdict: fix-first
</spec>
```

## Questions (no evidence yet; not verdicts)

| Id | Question | Why it matters |
| --- | --- | --- |
| Q1 | Does the Workflow tool result give token usage per run? | TT-31; SKILL.md:105 needs the actual usage at every gate |
| Q2 | When a workflow subagent downloads in the built-in browser, does a permission prompt reach the owner, and does that count as the "yes" in reference-images §4? | If it does, TT-02 becomes a wording fix |
| Q3 | Are `.agents/skills/*/evals/briefs.md` meant to be read by working agents? | TT-17; they hold pass criteria |
| Q4 | Can a workflow return the agent ids it spawned? | TT-19; crew.md and resume by id |
