---
type: job
scope: universal
status: draft
updated: 2026-10-24
source: J023 research
supersedes: []
---
> Author: researcher (general-purpose) · claude-sonnet-5-5 · default · 2026-10-24

# J023 research: the cutscene and effect job flows, step by step

Read-only map. It recommends nothing. Per step it gives who, reads, writes, hand-off, why the step exists (with the evidence id and file:line) and what would break if the step were removed or merged (evidence, or "no evidence found").

## 0. How this was made, and what it cannot show

**Method.** I read the recipe (`job-types.md`), the lead's playbook, the two saved scripts line by line, and the J016 design files they cite. Agent counts come from the kit's own test harness (`tools/workflows/wf_harness.mjs`, fake agents, no tokens) run through `tools/tests/test_job_workflows.py` helpers. Each count is a real run of the real script, not an estimate. A count I could not run (a case the harness cannot produce) is marked FORMULA and shown with its sum. Scratch scripts: `C:\Users\Firew\AppData\Local\Temp\claude\C--Users-Firew-Downloads-uterd-StudioKit\c7f5f258-1725-438d-b398-66f05c5ca3f6\scratchpad\count*.py` (not part of the repo).

**Counting rules.** "Agent run" = one `agent()` call in a saved script. Not counted: the lead's own work (job card, gate packets, readiness, close, doc-keeper filing), image batches the lead runs with the owner, and the scouts a hand-run lead may spawn (`CO:95`). Every agent also reads `job-card.md` and `decisions.md` and runs the context packet (`CS:154-155`, `CS:205`); that is not repeated in the "reads" column.

**Evidence key** (file:line; "Pn:n" and "Rnn:n" are owner papers and Riot transcript lines, cited second-hand through the J016 design files, which I did not re-open):

| Code | File |
| --- | --- |
| JT | `.agents/skills/orchestration/references/job-types.md` |
| SK | `.agents/skills/orchestration/SKILL.md` |
| BH / GF | `.agents/skills/orchestration/references/briefs-and-handoffs.md` / `gates-and-feedback.md` |
| CO | `rules/company.md` |
| RD | `.agents/workflows/jobs/README.md` |
| CS / EF | `.agents/workflows/jobs/job-cutscene.js` / `job-effect.js` |
| DES / DJT / DC | `knowledge/jobs/J016-orchestration/design.md` / `design-jobtypes.md` / `design-context.md` |
| CAP | `knowledge/reference/studio/claude-code-capabilities.md` (K1 `CAP:49`, K2 `:50`, K3 `:51`, K4 `:52`, K5 `:53`, K6 `:54`, K7 `:55`; C26 `:43`, C27 `:44`) |
| TT | `knowledge/jobs/J016-orchestration/reviews/tabletop-322c8ad-auditor-e.md` (findings TT-02 `:114`, TT-03 `:121`, TT-04 `:128`, TT-06 `:142`, TT-10 `:170`, TT-12 `:184`) |
| G3P | `knowledge/jobs/J018-riot-craft/g3-proposals.md` (G3-P2 `:74-95`, G3-P3 `:97-122`) |
| PP / DEC | `knowledge/jobs/J016-orchestration/pilot-plan.md` / `decisions.md` (LD1-LD16 `DEC:31-46`) |

DC ids used: E6 `DC:30` (typed exchange 62.5 % vs memory alone 36.5 %), E7 = K1 `DC:31`, E8 `DC:32` (a brief without its rules: 76.5 % to 0 %), E9 `DC:33` (files not chat), E10 `DC:34` (80 % of incomplete runs reported completion), E17 `DC:41` (same book, correlated errors), E20 `DC:44` (closed doors), E23 `DC:47` (owner words verbatim).

**Evidence honesty.** Searched: J016 `design*.md`, capability record, tabletop audit E, J018 `g3-proposals.md`, `pilot-plan.md`. Not searched: the Riot transcripts, the J019 and J021 job folders, and the role files. The J016 pilot ("one short cutscene three ways") was deferred (`PP:18`, `PP:68`): `DES:208` says no controlled study shows this flow beats the old one, and `DES:151` calls the round limits "pilot settings, not measured optima". So the "what breaks" column mostly says "design rationale, no incident found". Where an audit finding shows a real failure, it is cited.

**Roles and models** come from the script's `ROLE` table (`CS:69-87`, `EF:83-95`). Opus unless marked Sonnet. "m" = medium effort, "h" = high.

---

# PART A: CUTSCENE (`job-cutscene.js`, recipe `JT:20-34`)

Job lead and integrator: film-director (`JT:23`; `DJT:36`, P2:55, K6 `CAP:54`).

## A1. Stages, gates and sizes

| | M cutscene | L cutscene |
| --- | --- | --- |
| Workflow calls (each its own call; the owner gate sits between; a script cannot pause: C07 `CAP:24`) | `direction` → G1 → `build` (runs `proof()` first, then `production()`: `CS:944-948`) → G3 | `direction` → G1 → `proof` → G2 → `build` (production only) → G3 |
| Owner gates | 2 (G1, G3) | 3 (G1, G2, G3) |
| Agent runs, no repairs | 56 | 56 (identical: harness `build M` = 45 = proof 15 + build 30; L = 15 + 30) |
| Where the proof is judged | inside `build`, owner sees it at G3 | owner sees it at G2 |
| `repair` (after G3) | 1 call | 1 call |
| Owner image yes-batches | G1 look images (art-director), and the storyboards (a pending batch stops the stage: `CS:442`) | same |

Surprise: M saves the G2 gate but **zero agent runs**. `proof()` runs in full inside M `build` (`CS:944-946`), including the 12-run interface, strips, probes and animatic work.

## A2. Step table

Notation: `DIR` = `knowledge/jobs/<job>/`; `FILM` = `content/film/<seq>/`; "G-x" = parallel group. Every "why" cites the recipe or script line first, then the evidence id.

### Direction stage (same for M and L: `CS:263-339`)

| # | Step (script id) | Stage | Who (role · model · effort · group) | Reads | Writes | Hands to | Why it exists (evidence) | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | D1 proposals ×4 (`CS:270-284`) | direction | film-director · opus · m (Blender); art-director · opus · m (browser images); architect · opus · h; game-designer · opus · h. G-D1 parallel, 4 | `art-bible.md`, `templates/jobs/beat-sheet.md`; **not** each other's files (`CS:273,278`) | `DIR/direction/proposal-<role>.md`; film: `direction/stills-film-director/`; art: `direction/image-prompts.md`, `content/art/refs/` | step 2 (same four) | Independent first ideas so no lead copies another's: K1 `CAP:49` (11.1 % of correct answers flipped by upstream text; 77 of 82 harmful flips copied it), `DES:104`, `DES:138`; constraint owners state limits before design: `DJT:135` | K1 is a general-agents study, no cutscene incident found. Merging the architect or game-designer into the film proposal would drop the limits-first rule (`DJT:135`, R01:94-99). Game-designer is only "consulted" in the recipe (`JT:24`) but runs here (see A5) |
| 2 | D2 exchange ×4 (`CS:286-295`) | direction | same four. G-D2 parallel, 4 | the other three proposals | `DIR/exchange/r1-<role>.md` (agree/conflict/missing) | step 3 | One exchange, only conflicts that would change production: `DES:105`, P1:194, P1:196; `CO:58`, `CO:130` | No incident evidence. `DES:151,208`: round limits are pilot settings, never measured |
| 3 | D3 synthesis (`CS:298-309`) | direction | film-director · opus · m | 4 proposals, 4 exchange notes, `templates/jobs/direction-sheet.md` | `DIR/direction.md` rev 1 (options, recommendation, failed options, closed doors with "may return only if", Studio probes list, could-not-check) | step 4 | One direction sheet by the job lead: `DES:106`, `CO:12`; closed doors: `GF:55-64`, E20 `DC:44` | Without it there is no G1 packet (`CS:336` builds `g1` from it). No incident found for merging into step 4 |
| 4 | D3 signatures ×2 (`CS:311-321`) | direction | art-director · opus · m ∥ architect · opus · h. G-D3 parallel, 2 | `direction.md@rev` | `DIR/direction/sign-<role>.md` | step 5 if any `signs:false`, else the owner (G1) | Others sign their part or name an incompatibility: `CO:13`, `DES:106` (P1:190, P1:194) | No incident evidence. Game-designer and film do not sign (`CS:311`) |
| 5 | D3 resolution, 0-1 (`CS:323-332`) | direction | film-director · opus · m | `direction.md`, sign files | `direction.md` next rev | owner (G1) | One resolution round, then what stays open becomes a G1 question: `CO:130`, `DES:151` | Pilot setting only |
| G1 | owner | gate | lead shows `g1` object (`CS:336-337`): options, recommendation, trade-off, failed options, closed doors | | `decisions.md` row, closed doors | proof (L) / build (M) | `CO:30`, `SK:76-79` | |

### Proof (L: stage `proof`; M: first half of stage `build`) (`CS:342-533`)

| # | Step | Stage | Who | Reads | Writes | Hands to | Why it exists (evidence) | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | P1 contract (`CS:344-359`) | proof | film-director · opus · m | `direction.md@G1 rev`, beat-sheet and shot-list templates, `shotlist.py` | `DIR/beat-sheet.md` rev 1, `FILM/<seq>.shots.json`, readiness table; returns `new_cast_needed` | step 7; or `needs-decision` if a cast member has no rig (`CS:356`) | One contract with stable event ids = the dependency map: `JT:26`, `DJT:39`, `CO:72`, LD12 `DEC:42`. New-cast check right after P1: TT-12 `TT:184` (before the fix, the stop came after G1 and G2) | All later steps key on its ids. TT-12 is the evidence for the early new-cast stop |
| 7 | P2 needs round ×5 per round, 1-2 rounds (`CS:362-393`) | proof | animator · opus · m ∥ environment-designer · opus · h ∥ architect · opus · h ∥ lane (vfx-designer · opus · h, then sound-designer · opus · m answers vfx's note). G-P2: 4 lanes, 5 runs | `beat-sheet@rev`; sound also reads `exchange/p<r>-vfx-designer.md` | `DIR/exchange/p<r>-<role>.md` (agree/conflict/missing) | step 8 if any conflict or missing, else step 9 | Consumers state needs against the draft before producers build: `JT:28`, `CO:60`, `DES:29`, `DES:108`, `DES:150`; typed exchange beat free memory: E6 `DC:30`; one timing change cascades to animation, effects, sound: K4 `CAP:52` | TT-06 `TT:142` (in job-feature, not cutscene): with no channel, VFX and sound built in parallel and never agreed the envelope. No cutscene-specific incident found. See A4 for what this round does and does not do |
| 8 | P2 merge, 0-2 (`CS:383-392`) | proof | film-director · opus · m | `beat-sheet`, 5 exchange notes | beat sheet next rev + change-table row naming consumers | round 2 (all 5 again) or step 9 | The decision owner merges: `SK:56`, `CO:60`; contract-change notice: `rules/messages.md:142-153` | Without the merge the notes are not the contract (`CO:76`) |
| 9 | P3a blocking + value strips (`CS:399-408`) | proof | film-director · opus · m (Blender) | beat sheet, `direction.md`, `film-craft` steps 5-6, `look_check.py` | `FILM/strips/` (blocking strip, value strip, `look_check.py value` numbers) | step 10 | Cheap passes first; value chosen in grey before colour; strips are the boards' layout input: `JT:27`, `JT:139`, G3P:79 item 3 and `G3P:417` | G3P:76-89: the old order let boards come first; no incident number found. Boards cost image batches, so a bad layout wastes one |
| 10 | P3a value review, 1-3 rounds (`CS:409-421`) | proof | art-director · opus · m | strips, beat sheet, `direction.md` | `DIR/reviews/value-strip-rev<r>-art-director.md` | step 11 if blocking, else step 12; `needs-decision` at round 3 | Art reviews the value strip before any board: `JT:27`; reviewers read, makers write, K2 `CAP:50` (a review chain lost 36 correct answers, repaired 6 of 371) | No incident found. Merging with step 18 (animatic review) would put value problems after the boards exist |
| 11 | P3a strips fix, 0-2 (`CS:422-430`) | proof | film-director · opus · m | the review, strips | strips new rev | step 10 | Two repair rounds, then diagnose: `CO:107,132`, P1:232, P2:215 | |
| 12 | P4 storyboards (`CS:433-442`) | proof | film-director · opus · m (browser: the only browser user) | beat sheet, strips | `FILM/boards/` + contact sheet, `content/art/refs/storyboard/`; or `boards/image-prompts.md` and `images:pending` | step 13-16 group; **stage returns `blocked` if pending** (`CS:442`) | Storyboards are the layout input of the animatic and what the owner sees at G2: `JT:27`, `DJT:40`; owner's yes per image batch: TT-02 `TT:114`, LD2 `DEC:32` | TT-02: without the batch rule a workflow agent must download without the owner's yes, skip the pictures, or block |
| 13 | P3 Studio probes (`CS:445-453`) | proof | architect · opus · h (Studio driver). G-P3 parallel with 14-16 | `direction.md`, `proposal-architect.md`, beat sheet | `DIR/architect/probes/probes.md` (per probe: claim, test, Output lines, result) | step 17 (animatic), step 19 | The runtime, camera ownership, skip and endings are risky claims tested in the proof, not guessed: `JT:27`, `DJT:37` | No incident found. Without it the build reaches integration before learning the skip teardown cannot work |
| 14 | P3 greybox set, 0-1 (`CS:454-462`) | proof | environment-designer · opus · h (Blender); only when `needs_greybox` | beat sheet, `direction.md` | `content/stages/<seq>-greybox/` | step 17 | "Greybox set where the set is missing": `JT:27` | Without it the animatic has no space for the shot cameras |
| 15 | P4 temp VFX marks (`CS:464-470`) | proof | vfx-designer · opus · h (inside G-P3, first of a pair) | beat sheet | `content/vfx/<seq>-temp/frame-scripts.md` | step 16 | Temporary effect cues in the animatic: `JT:27`; sound keys to picture events: `DJT:112` | Merging 15 and 16: the dependency VFX → sound is why they run one after the other (TT-06 `TT:142`) |
| 16 | P4 temp sound (`CS:471-477`) | proof | sound-designer · opus · m | beat sheet, VFX frame scripts | `output/sound/<seq>-temp/` | step 17 | Owner judges timing with sound: `JT:27`, `JT:141` | |
| 17 | P5 animatic (`CS:486-495`) | proof | film-director · opus · m (Blender); maker self-review "silent, then with sound" inside the step | beat sheet, boards, temp sound/VFX, probes, greybox | `FILM/` animatic movie + manifest | step 18 | The cheap integrated proof: `CO:31`, `JT:27`, DES:30, K5/K6 `CAP:53-54` | This is the G2 artifact; removing it removes G2 |
| 18 | PR review: art, 1-3 rounds (`CS:498-515`) | proof | art-director · opus · m | `FILM/`, `direction.md`, beat sheet, probes | `DIR/reviews/animatic-rev<r>-art-director.md` | step 19 | Domain-lead review before the owner: `CO:98`, `DES:128`; independent look first: `CO:104`, E17 `DC:41` | No incident found |
| 19 | PR review: architect (same rounds) | proof | architect · opus · h (runs after 18; the two are sequential, not parallel: `CS:504`) | same | `animatic-rev<r>-architect.md` | step 20 or owner (G2/G3) | Cost flags against the probe results: `JT:27` | |
| 20 | PR fix, 0-2 (`CS:521-529`) | proof | film-director · opus · m | the two reviews, beat sheet | animatic new rev (+ beat-sheet rev if it changed) | steps 18-19 | `CO:107` | After round 3 with blocking: `needs-decision` (`CS:532`) |
| G2 | owner (L only) | gate | animatic + boards + `could_not_check` + owner-confirmed lines | | words in `decisions.md` | build | `CO:31`, `GF:18` | |

### Build (stage `build`; `CS:589-757`)

| # | Step | Stage | Who | Reads | Writes | Hands to | Why it exists (evidence) | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 21 | B1 plan: animator, environment, ui (`CS:599-602`) | build | animator · opus · m ∥ environment-designer · opus · h ∥ ui-ux-designer · opus · m. G-B1 parallel (5 lanes, 7 runs) | beat sheet, `FILM/`, `direction.md` | `DIR/exchange/b1-<role>.md` | step 26 | Full craft planning after G2, before costly work: `JT:29`, `CO:60` | No rigger/modeler lane (see A5 #2). No incident found for UI planning |
| 22 | B1 player contract (`CS:603-607`) | build | architect · opus · h | beat sheet, `FILM/`, `direction.md`, `probes.md` | `DIR/contract-player.md` (camera ownership, skip, endings, Output line format, **Code file owners**, `adds_remote`, `saves_data`) + `b1-architect.md` | 23, 26; sets effort of builder and reviewer | Code file owners table set by the architect: LD10 `DEC:40`; TT-04 `TT:128` (without it the builder guessed its files) | TT-04 shows the failure |
| 23 | B1 builder needs (`CS:607`) | build | feature-builder · opus · m (high if the contract says remotes/saves) | player contract | `b1-feature-builder.md` | 26 | Builder states what it needs from the contract before building | |
| 24 | B1 VFX envelope (`CS:610-611`) | build | vfx-designer · opus · h | beat sheet, `FILM/`, `direction.md` | `b1-vfx-designer.md` (per cue: wind-up, peak, tail, onset, coverage) | 25 | VFX and sound co-design each cue's envelope on event ids: `JT:29`, `DJT:41`, R00:2965-2971, R00:3830-3834 | TT-06 `TT:142` |
| 25 | B1 sound envelope (`CS:612`) | build | sound-designer · opus · m (after 24) | + `b1-vfx-designer.md` | `b1-sound-designer.md` | 26 | Sound keys to picture events | |
| 26 | B1 lock (`CS:623-632`) | build | film-director · opus · m | the 7 notes, beat sheet, player contract | beat sheet **locked revision** (agreed envelopes, change table) | steps 27-37 | One reconciling owner; may not edit the architect's contract: `CS:625`, `CO:60` | Without a lock the parallel production crafts build on different revisions (`DES:152`, stale rule `CO:81`) |
| 27 | B2 set rough (`CS:639-646`) | build | environment-designer · opus · h (Studio) | beat sheet, `FILM/`, `b1-environment-designer.md` | `content/stages/<seq>/`, place content | 28 | Rough pass first, art checks before final light: `JT:31`; a stage-job finding by analogy, G3P:88 ("the art director first sees the stage light at the final review", `art-director.md:31`) | |
| 28 | B2 art check-in (`CS:648-655`) | build | art-director · opus · m | rough set stills | `DIR/reviews/set-rough-art-director.md` (paint-over notes) | 29 | Check-ins during work, not only at the end: `JT:31`, `DES:113`, R02:460-470, R03:790-806 | |
| 29 | B2 set final (`CS:657-665`) | build | environment-designer · opus · h (Studio) | rough, notes | final set | 38+ | | |
| 30 | B4 UI spec (`CS:667-674`) | build | ui-ux-designer · opus · m. Parallel lane with 27-29 and the picture lane | beat sheet, `b1-ui-ux-designer.md`, player contract | `content/ui/<seq>-cutscene/spec.md` | 40 (builder) | Letterbox, subtitles, skip: `JT:29` | |
| 31 | B3 animation blocking (`CS:678-683`) | build | animator · opus · m (Blender). G-B3: with 32-33 | beat sheet, `FILM/`, `b1-animator.md` | `content/anim/<seq>/` blocking playblasts | 34 | Show early and rough: `SK:62`, `DES:113` | |
| 32 | B5 VFX prototype (`CS:685-692`) | build | vfx-designer · opus · h. G-B3 | beat sheet | `content/vfx/<seq>/` frame scripts + first-pass `spec.json` | 33, 34 | VFX and sound prototype early on stable ids: `JT:30`, `DJT:42`, K4 `CAP:52` | |
| 33 | B5 sound prototype (`CS:693-699`) | build | sound-designer · opus · m | beat sheet, VFX files | `output/sound/<seq>/` prototype + cue list | 34 | | |
| 34 | B3 combined check-in (`CS:705-711`) | build | film-director · opus · m | anim playblasts, VFX, sound, beat sheet | `DIR/reviews/combined-film-director.md` (notes per maker) | 35, 36, 37 | One combined early pass of picture, effects and sound before polish: `JT:30`, `DJT:42` (P1:426, R04:164-180, R07:198-215) | |
| 35 | B3 animation polish (`CS:712-718`) | build | animator · opus · m (Blender) | clips, combined notes, beat sheet | exported clips + `content/anim/<seq>/timing-list.md` ("the job's one marker list": `CS:714`) | 36 | VFX and sound finish against the animation: `JT:30` | |
| 36 | B5 VFX final (`CS:721-728`) | build | vfx-designer · opus · h | timing list, beat sheet, VFX, combined notes | final `spec.json`, frame scripts | 37 | | |
| 37 | B5 sound final (`CS:730-738`) | build | sound-designer · opus · m | timing list, VFX final, sound proto, notes | cue cards, prompts, mix plan, listening-test plan | 38 | "Final sound only after timing locked": `JT:104` pattern, `JT:30` | |
| 38 | IMP clips (`CS:536-544`) | build | animator · opus · m (Studio) | `content/anim/<seq>/` | `import-record.md` | 39 | Roblox import is the animator's step: `JT:48` (S7) | |
| 39 | SCN scene data (`CS:545-554`) | build | film-director · opus · m (Studio) | beat sheet, `FILM/`, VFX, sound, UI spec, import record, player contract | scene data (`shotlist.py luau`), place content, `evidence.md` scene rows | 40 | Film-director is the sequence integrator: `JT:32`, K6 `CAP:54` | |
| 40 | PLY player code (`CS:555-573`) | build | feature-builder · opus · m (high on remotes/saves) (Studio) | player contract, state sheet, UI spec, beat sheet, `FILM/` | code in the contract's Code file owners + tests, `evidence.md` rows | 41 | Builder builds the player against the contract: `JT:32`, LD10 `DEC:40` | |
| 41 | CAP candidate capture (`CS:574-586`) | build | **film-director** · opus · m (Studio) | `evidence.md`, beat sheet, player contract | `evidence.md` candidate revision + protected list; `FILM/captures/candidate/` (stills, `output.log`) at phone aspect and desktop | 42 | Freeze one revision-pinned candidate: `CO:64`, `DES:91` | |
| 42 | RV scripts (`CS:778-781`) | build | **qa-lead** · opus · m | `shotlist.py check`, `log-diff`, the gate | `DIR/reviews/candidate-r<n>-scripts.md` | 43-48, or repair if FAIL | Scripts first: P2:199, P2:346, `DES:125`; a FAIL stops the other reviews: `CS:783-785` | A cheap model/script saves reviewer time (`DES:125`) |
| 43 | RV qa-lead (`CS:788-789`) | build | qa-lead · opus · m (Studio) | candidate, captures | `reviews/candidate-r<n>-qa-lead.md` | 44 | Skip, every ending, control and camera restored, repeat trigger, multiplayer, streaming: `JT:33` | |
| 44 | RV performance (`CS:790-791`) | build | performance-engineer · opus · h (Studio, after 43) | same | `reviews/...-performance-engineer.md` | owner readiness | Phone budget: `JT:33` | Phone verdict needs a phone, else BLOCKED (`CS:790`) |
| 45 | RV code (`CS:794-797`) | build | reviewer · opus · m (high on remotes/saves) (no Studio) G-R2 | `evidence.md`, player contract, the owned code | `reviews/...-reviewer.md` | | Every candidate with code has the reviewer: LD15 `DEC:45`, `CO:100`; TT-03 `TT:121` (before the fix the cutscene player went to G3 unreviewed) | TT-03 is the evidence |
| 46 | RV film (`CS:800`) | build | film-director · opus · m. G-R3 creative chain, sequential 46→47→48 | captures, `output.log`, beat sheet | `reviews/...-film-director.md` | 47 | Creative review in the recipe's order: staging, timing, camera, first-second read: `JT:33`, `DJT:45` (P1:430-432, P2:497-500) | The same agent made steps 39 and 41 (the maker reviews the candidate it built). Independent-look rule `CO:104` concerns reading the artifact before the hand-back; no incident found |
| 47 | RV art (`CS:801`) | build | art-director · opus · m | captures | `reviews/...-art-director.md` | 48 | Integrated look: `JT:33` | |
| 48 | RV sound sync (`CS:802`) | build | sound-designer · opus · m | `output.log`, files | `reviews/...-sound-designer.md` | readiness | Sound onset 0 to +40 ms after the first lit frame, from the Output log; listening stays owner-confirmed: `JT:18`, `BH:34` | |
| 49 | RV event captures, risk `event` only (`CS:815-822`) | build | studio-operator · sonnet · m (Studio) | candidate | `FILM/captures/<tag>/event/` | 50 | Live-ops slot, risk-gated: `JT:123`, G3P:118 | skipped line goes into the card (`CS:241`) |
| 50 | RV live-ops, risk `event` only (`CS:824-826`) | build | live-ops-designer · opus · m | event captures | `reviews/...-live-ops-designer.md` | readiness | | |
| 51 | FIX round (`CS:854-911`) | build / repair | the makers named by findings, in order film → env → modeler → rigger → animator → vfx → sound → ui → builder; then IMP (if animator/modeler/rigger ran), SCN, CAP | `reviews/`, `evidence.md`, beat sheet | fixed files; new candidate capture | back to 42 | Repairs go to the maker with the finding: `SK:66`; recapture and refreeze every round: `RD:14` | Each repair is a fresh call, not a resumed agent (`CO:79`) |
| G3 | owner | gate | lead readiness + captures + could-not-check + owner-confirmed lines | | words in `decisions.md` | close, or `repair` | `CO:32`, `SK:73` | |

### Repair stage (after G3, `CS:914-935`)

| # | Step | Who | Does | Then |
| --- | --- | --- | --- | --- |
| 52 | R1 scope | film-director · opus · m | maps the owner's note to beats and crafts (`affected_roles`); `new_scope` stops at `needs-decision` (`CS:924`); `timing_changed` adds animator, VFX, sound (`CS:928-931`) | row 51 for the affected makers only, then the **whole** review chain again (rows 42-50, `CS:934`) |

## A3. Counts per cutscene job (harness-run unless marked FORMULA)

| Piece | Minimum (no repairs) | Max, one maker per repair round (harness) | Ceiling, every maker in every round (FORMULA) |
| --- | --- | --- | --- |
| direction | 11 | 12 (a signature refused) | 12 |
| proof | 15 (+1 with greybox) | 22 measured with one interface conflict round + greybox; 21 with both animatic repairs; 12 with the value-strip loop exhausted | **33** = 1 + 12 (2 need-rounds with a merge each) + 1 strips + 5 (3 value reviews, 2 fixes) + 1 boards + 1 probes + 1 greybox + 2 temps + 1 animatic + 8 (3 PR rounds ×2 + 2 fixes) |
| build (L) | 30 (32 with `event`) | 50 (art finding, film repairs, 3 review rounds, needs-decision); 57 (code finding, 4 reviews and 3 builder repairs) | **95** = 23 + 6 reviews ×7 + 3 code repairs ×2 + 2 other repairs ×12. Rounds: code 3, other 2 (`CS:837`). With `event`: 107 |
| whole job, L or M | **56** (59 with greybox and `event`) | 12 + 33 (FORMULA) + 57 = **102** | 12 + 33 + 95 = **140** |
| `repair` stage | 11 (film-only fix; scope 1 + fix 1 + scene 1 + capture 1 + 7 reviews) | 20 for the first round with all 9 makers (harness) | each extra round up to 12 + 7 |

Agent runs by role in the minimum 56 (harness labels): film-director 12, art-director 7, architect 7, sound-designer 6, animator 5, vfx-designer 5, environment-designer 4, game-designer 2, ui-ux-designer 2, feature-builder 2, qa-lead 2, reviewer 1, performance-engineer 1. Before the animatic starts (P5) the minimum is 11 + 12 = 23 runs, which matches the 24 runs in the J023 card (`job-card.md:25`).

Cost per run is not measured here. Only smoke data exists: an M cutscene build of 50 Haiku agents used 3.5 M tokens, and each agent pays about 30-70 k tokens of fixed context before work (`PP:76`, C26 `CAP:43`). C27 `CAP:44` says a start-up record per role was measured in J017 (not opened).

Owner-facing counts: gates L 3 / M 2; exchange rounds: direction D2 ×1, interface needs ×1-2, craft planning ×1 (3 to 4 in total), plus one direction resolution round (`CO:130,131`); stage calls L 3 / M 2 (+ `repair`).

## A4. The needs and interface steps in detail (the owner's "crafts agree before production")

Three places hold this in the script. Result files are named; the owner can open them.

**1. Direction exchange (D2, row 2, all L and M).** Four leads (film, art, architect, game-designer) each read the other three proposals and write only conflicts that would change production. No merge round: the film-director takes them into the direction sheet (row 3).

**2. The needs round before the proof (P2, rows 7-8; `CS:362-393`).**
- Draft: the film-director's `beat-sheet.md` rev 1, which names 7 consumers (`CS:351`): animator, environment-designer, vfx-designer, sound-designer, ui-ux-designer, feature-builder, architect.
- Who states needs: 5 of them answer: animator, environment-designer, architect, vfx-designer, sound-designer. UI and feature-builder are not asked here (recipe says the same: `JT:28` names animator, environment, vfx, sound, architect).
- Format: one exchange note per role per round, `DIR/exchange/p<r>-<role>.md`, items agree / conflict / missing evidence, naming the beat id and who decides or which test settles it (`CS:367-369`; format `rules/messages.md:122-140`; "Looks good" is not enough, `DES:150`).
- Order: animator, environment and architect write in parallel and do not read each other. The VFX note is written first (it proposes each cue's envelope: onset, peak time, length); the sound note is written after it and answers on that file (`CS:373-374`). Sound reads only the VFX note.
- Merge: the film-director merges all five into the next beat-sheet revision with a change-table row naming consumers (`CS:383-390`). The merge runs only if the round had any conflict or missing item (`CS:381-382`).
- Rounds: at most 2 (`CS:362`). Round 2 reruns **all five** agents even if one had a conflict. Anything still open after round 2 becomes a G2 question (`CS:385`). Cost: 5 runs (no conflict) / 11 (one conflict round) / 12 (two).
- Result: `beat-sheet.md` (revisions) + `exchange/p1-*.md`, `p2-*.md`.

**3. Craft planning after G2 (B1, rows 21-26; `CS:590-633`).**
- 7 agents write plans in 5 parallel lanes: animator, environment-designer, ui-ux-designer, architect (writes `contract-player.md` and its own note), feature-builder (reads the architect's contract), vfx envelope then sound answer.
- Files: `DIR/exchange/b1-<role>.md` and `contract-player.md`.
- Merge: the film-director's B1 lock writes the locked beat sheet. One round only, no second round (`CS:623-632`). Conflicts become resolved items or owner questions. The film-director may not edit the architect's contract (`CS:625`).
- The architect's contract also sets whether the builder and reviewer run at high effort (`CS:621`, `CS:89-95`).

**Who agrees with whom, and who does not.** The only two-way exchange is VFX then sound (rows 7, 24-25). The animator's needs and plan are never read by VFX or sound in P2 or B1; the animator's output reaches them through the film-director's merged beat sheet and later the animator's timing list (row 35, which VFX and sound finish against: rows 36-37). The four crafts (animation, VFX, sound, environment) never exchange notes with each other directly in a file. The film-director is the single merge point both times. Modeler and rigger are never asked (see A5 item 2). The VFX/sound envelope is therefore designed in four places: P2 (row 7), P4 temp marks (rows 15-16), B1 (rows 24-25), B5 prototype and finals (rows 32-33, 36-37).

## A5. Where the hand-run recipe and the saved script differ

| # | Recipe says | Script does | Lines |
| --- | --- | --- | --- |
| 1 | game-designer is "consulted" for the state sheet (`JT:24`) | full D1 and D2 runs (2 runs); does not sign | `CS:268,271,287-295,311` |
| 2 | Interfaces after G2 include animator ↔ character-rigger ↔ modeler (`JT:29`) | no rigger/modeler lane in build; only a `new_cast_needed` flag at P1 and at the lock; modeler and rigger run only as repair makers | `CS:356,631,762,857-858` |
| 3 | VFX ↔ sound envelope is listed under "Interfaces after G2" (`JT:29`); "before the proof" lists needs only (`JT:28`) | the envelope is also proposed and answered in P2 before the proof | `CS:372-376` vs `610-614` |
| 4 | Proof reviews "film → art → architect" (`JT:27`) | film's review is the self-review inside P5; art then architect run sequentially | `CS:488,498-515` |
| 5 | The studio-operator takes the named captures (`JT:16`) | candidate capture and recapture are done by film-director (Opus); the scripts check is done by qa-lead (Opus); studio-operator (Sonnet) appears only for risk `event` captures | `CS:574-586,778,815` |
| 6 | qa-lead ∥ performance-engineer ∥ reviewer (`JT:33`) | qa-lead then performance one after the other (one Studio driver); the reviewer and the creative chain run beside them | `CS:786-793` |
| 7 | For a cutscene the one marker list is the beat sheet (`BH:30`) | the script calls `timing-list.md` "the job's one marker list" | `CS:714` |
| 8 | Event slot "after integration and before G3" (`JT:123`) | after the creative chain | `CS:812` |
| 9 | M jobs skip the proof stage (`JT:5`, `JT:11`) | M runs every proof step inside `build`; same 56 runs | `CS:944-948` |
| 10 | Hand-run: crafts get peer ids and may use `SendMessage`; repairs resume the maker (`SK:61,66`; `CO:76-79`) | no ids, no messages; repairs are fresh calls | `CS:159`, `CS:854-911` |
| 11 | Builder and reviewer high on money/saves/remotes (`.agents/roles/README.md:23-24`) | raised only after the architect's contract exists; the repair stage assumes high because it did not read the contract | `CS:89-95` |
| 12 | Environment-designer: high for new/big stages, medium for small (`README.md:20`) | pinned high for the whole cutscene set | `CS:74` |

## A6. Plain walk-through of one L cutscene, from request to G3

You ask for a cutscene, for example a boss entrance. The lead writes your words down exactly, decides the job is large, and opens a folder for it. Four specialists (the film director, the art director, the engineer who plans the technology, and the game designer) each write a short plan on their own, without seeing the others' plans. Each then reads the other plans once and lists only the disagreements that would change the work, and the film director writes one direction sheet that the art director and the engineer sign. That is about 11 agent runs, and you have seen nothing yet. You then pick a direction from two or three pictured options (gate 1). Next the film director turns your pick into a numbered list of beats and shots; the animator, set builder, effects artist, sound designer and engineer each say what they need or what clashes, and the film director fixes the list. Cheap rough versions follow: grayscale blocking, storyboards, and a timed rough film with placeholder sound and effects, while the engineer tests in Roblox Studio that skipping and every ending will work; two reviewers check it, and you watch the rough film (gate 2). After your yes, the specialists plan once more (now with the interface person and the code builder), and the film director locks the list. Then they build: the set, the animation, and rough effects and sound; the film director looks at them together before polish; the animator polishes and writes the timing list; effects and sound finish against it. One person at a time puts everything into Studio (animation clips, scene data, the player code) and records the whole sequence. Scripts check the recording first; then a tester, a performance engineer, a code reviewer, and the film director, art director and sound designer each review it, and every failure goes back to its maker for up to two or three rounds. Last, the lead checks that every claim has evidence, lists what could not be checked, and shows you stills and logs; you watch and listen yourself and give the final yes (gate 3). The minimum is 56 agent runs; with every repair round used it is about 100.

---

# PART B: EFFECT (`job-effect.js`, recipe `JT:96-107`)

Job lead: vfx-designer (`JT:99`). Required args decide the shape: `animated` (adds the animator, `EF:518`), `newLook` (adds the art-director, forces size L, `EF:73`), `small` (quick-builder wires, `EF:96`), `risks` (qa-lead `server-result|danger-area|paid-random|frequent-effect`; live-ops `event`: `EF:43-48`).

## B1. Stages, gates and sizes

| | M effect | L effect (a new look) |
| --- | --- | --- |
| Workflow calls | `direction` → G1 → `build` (`proof()` then `production()`: `EF:863-868`) → G3 | `direction` → G1 → `proof` → G2 → `build` → G3 |
| Owner gates | 2 | 3 |
| Agent runs, no repairs, no risks, not animated | 35 (harness: M build 26 = proof 15 + build 11) | 35 |
| Same, animated | 40 | 40 |

Same surprise as the cutscene: M saves the G2 gate, not the agent runs. Worse, M's proof review chain can end `needs-decision` inside `build` with no gate before it (`EF:807-809`).

## B2. Step table

### Direction (`EF:267-369`)

| # | Step | Stage | Who | Reads | Writes | Hands to | Why it exists (evidence) | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | D1 proposals, 3 (4 with `newLook`) (`EF:276-290`) | direction | game-designer · opus · h; vfx-designer · opus · h (2 key-frame sheets via reference-images, or words only for a new look); sound-designer · opus · m; art-director · opus · m (newLook only). G-D1 parallel | `game-profile.md`, `art-bible.md`; not each other | `DIR/direction/proposal-<role>.md` (+ `image-prompts.md`, `content/art/refs/` for the image maker) | 2 | Independent first ideas: K1 `CAP:49`; the gameplay length comes from design, sound keys to picture: `JT:102`, `DJT:112` | No effect-specific incident found. The recipe says art-director only for a new look (`JT:100`) |
| 2 | D2 exchange, 3-4 (+1 art consult if vfx says `adds_colour_role` or `adds_shape_code`) (`EF:299-319`) | direction | same roles ∥ art-director (consult) | the other proposals; consult reads the vfx proposal and the art bible | `DIR/exchange/r1-<role>.md`; `consult-art-director.md` | 3 | One exchange: `DES:105`; art joins when the effect adds a colour role or shape code: G3P:356 (`art-director.md:33`) | No incident found |
| 3 | D3 synthesis (`EF:324-335`) | direction | vfx-designer · opus · h | proposals, exchange, consult | `DIR/direction.md` rev 1 | 4 | `DES:106` | The G1 result has no structured failed-options/closed-doors fields (`EF:141,365`); the text rule asks for them (`EF:326`) |
| 4 | D3 signatures, 2-3 (`EF:337-348`) | direction | game-designer, sound-designer (+ art-director if newLook or consult). G-D3 parallel | `direction.md@rev` | `DIR/direction/sign-<role>.md` | 5 if any refuses, else G1 | `CO:13` | No incident found |
| 5 | D3 resolution, 0-1 (`EF:350-361`) | direction | vfx-designer · opus · h | `direction.md`, sign files | `direction.md` next rev | G1 | `CO:130` | |
| G1 | owner | gate | `g1` object (`EF:365`): options, recommendation, trade-off, could-not-check | | words, closed doors in `decisions.md` | proof (L) / build (M) | `CO:30` | |

### Proof (L: stage `proof`; M: first half of `build`) (`EF:502-633`)

| # | Step | Stage | Who | Reads | Writes | Hands to | Why it exists (evidence) | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | P1 gameplay window (`EF:505-517`) | proof | game-designer · opus · h | `direction.md` | `DIR/gameplay-window.md` rev 1 (trigger, confirm moment, telegraph lead, recovery, total length in seconds with config keys; rate; max on screen) | 7 or 8 | "Gameplay length comes from design": `JT:102`, `DJT:112`; fixed for every craft after | The game-designer already wrote the window in its D1 proposal (`EF:270`); step 6 turns it into the contract file. No incident found for merging |
| 7 | P1 timing list, only if `animated` (`EF:518-530`) | proof | animator · opus · m | window rev, `direction.md` | `content/anim/<effect>/timing-list.md` rev 1 (the draft blocking markers) + a playblast | 8 | Animator sends blocking markers to VFX and sound before either builds: `JT:102`, G3P:337 (`animator.md:31`); K4 `CAP:52` | G3P:337: before this rule VFX and sound keyed from markers that did not exist yet |
| 8 | P1 event timeline (`EF:531-544`) | proof | vfx-designer · opus · h | window, timing list, `direction.md` | `DIR/contract-timeline.md` rev 1 (event id, phase, time, source, consumers; envelopes empty) | 9 | One event timeline shared by animator, VFX, sound: `JT:101`, `DJT:111`; LD12 `DEC:42` | |
| 9 | E vfx envelope, 1-2 rounds (`EF:549-558`) | proof | vfx-designer · opus · h | timeline, markers (+ round 1 sound note in round 2) | `DIR/exchange/env-r<n>-vfx-designer.md`, `content/vfx/<effect>/frame-script.md` | 10 | VFX and sound co-design the envelope before either builds: `JT:102`, `DES:29`; TT-06 `TT:142` | TT-06 is the evidence: with no envelope channel they built in parallel and never agreed |
| 10 | E responses: sound-designer · opus · m, and animator · opus · m if animated, parallel (`EF:559-572`) | proof | G-E2: 1-2 runs | timeline, the vfx note, markers | `env-r<n>-sound-designer.md`, `env-r<n>-animator.md` | 11 | Typed exchange (agree/conflict/missing): E6 `DC:30` | The animator checks fit but may not retime (`EF:560`) |
| 11 | E merge, runs every round (`EF:574-584`) | proof | vfx-designer · opus · h | timeline, the notes | `contract-timeline.md` next rev + change-table row | round 2 if open, else 12 | Decision owner merges: `CO:60`. Cannot move a gameplay time or an animation beat | Unlike the cutscene, the merge runs even with zero conflicts (`EF:574` before the break at `585`) |
| 12 | P3 first spec: the blocking pass (`EF:590-601`) | proof | vfx-designer · opus · h. G-FS parallel with 13 | timeline, window, `direction.md`, markers | `content/vfx/<effect>/brief.md`, `frame-script.md`, `spec.json` (placeholder sprites, real sizes and timing, real truth edge) | 14/15 | Blocking pass before any texture pick: `JT:103`, G3P:561 (`vfx-designer.md:25`) | Texture pick before art's blocking check is the thing the rule prevents; no incident number |
| 13 | P3 temp sound (`EF:602-612`) | proof | sound-designer · opus · m | timeline, markers | `output/sound/<effect>-temp/` | 15 | Temp sound on the blocking markers so the owner judges timing: `JT:104`, G3P:536 | |
| 14 | IMP proof clip, only if animated (`EF:372-381`) | proof | animator · opus · m (Studio) | clip, timing list | `import-record.md` | 15 | Importer checks markers survive: `JT:48` | |
| 15 | W proof wiring (`EF:383-412`) | proof | feature-builder (quick-builder if `small`) · opus · m (Studio) | `spec.json`, temp sound, timeline, `game-profile.md`, import record | wiring files, Studio-only test hooks (`Rate`, `Reject`, `DebugShape`), `capture-setup.md` | 16 | Hooks before any partner's first capture: `JT:143`, G3P:100; temporary wiring still gets the reviewer: `RD:13`, LD15 | |
| 16 | CAP proof-r0 (`EF:421-442`) | proof | studio-operator · sonnet · m (Studio) | `capture-setup.md`, `spec.json`, timeline | `output/vfx/<effect>/captures/proof-r0/` (≤ 4 key stills, 30 fps dark-place frames `f###_<ms>ms.jpg`, Output log) | 17-22 | Numbers for every case, at most 4 stills (J005-D8): `CO:105`, `JT:103` | |
| 17 | RV scripts (`EF:736-747`) | proof/build | studio-operator · sonnet · m (Studio) | captures, `spec.json`, profile | `DIR/reviews/<tag>-scripts.md`, `metrics.json` (`clip_metrics.py`, `flash_count.py`, budgets, gate) | 18 | Scripts first, flash safety: `JT:106`, `DES:125` | **A FAIL does not stop steps 18-22** (see B5 item 1) |
| 18 | RV vfx self-review + freeze (`EF:749-758`) | proof/build | vfx-designer · opus · h | captures, scripts file, frame script, timeline | `evidence.md` (candidate revision + protected list), `reviews/<tag>-vfx-designer.md` | 19-22 | Maker self-review before others: `CO:98`, `DES:126` (P2:205) | A fifth/sixth run of the same maker on the same capture; no incident found |
| 19 | RV game-designer (`EF:724`, `790`) | proof/build | game-designer · opus · h. G-R3 sequential 19→20→21 | capture, evidence, timeline, `spec.json`, `direction.md`, scripts file | `reviews/<tag>-game-designer.md` | 20 | "Does it hide information players need?": `JT:106`, G3P:112 (the designer cannot judge this from single stills) | |
| 20 | RV art-director (`EF:726-728`) | proof/build | art-director · opus · m | same (+ own blocking check in the final pass) | `reviews/<tag>-art-director.md` | 21 | Brightest point where the eye must go; grey + black-fill at proof, value ladder at final: `JT:103,106` | |
| 21 | RV sound sync (`EF:729`) | proof/build | sound-designer · opus · m | same | `reviews/<tag>-sound-designer.md` | readiness | Onset 0 to +40 ms after the first lit frame (JU-29): `EF:729` | |
| 22 | RV code (`EF:769-777`) | proof/build | reviewer · opus · m. G-R2 parallel with 19-21 | wiring files, `spec.json`, `capture-setup.md` | `reviews/<tag>-reviewer.md` | | LD15 `DEC:45` | |
| 23 | Repair round (`EF:447-499`, `810-822`) | proof/build | makers in order game-designer → animator → vfx → sound (sound added if time moved) → wire sync; then CAP | `reviews/`, `evidence.md`, timeline | fixed files, `capture` | back to 17 | Dependency order, timing change makes VFX and sound recheck: `JT:107`; recapture every round: `RD:14` | Round limit: 2 for **all** findings (`EF:807`) |
| G2 | owner (L only) | gate | proof capture + clean review | | words | build | `CO:31`, `GF:18` | |

### Build (stage `build`; `EF:636-710`)

| # | Step | Stage | Who | Reads | Writes | Hands to | Why it exists (evidence) | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 24 | B1 final timing list, only if animated (`EF:640-652`) | build | animator · opus · m | clips, window, timeline | exported clip + final `timing-list.md` | 25 | Final sound only after the timing list is locked: `JT:104` | |
| 25 | B1 lock (`EF:653-663`) | build | vfx-designer · opus · h | timeline, window, final timing list, `decisions.md` | `contract-timeline.md` locked rev | 26 | One reconciling owner; a gate note that changes the window is `needs-decision` | |
| 26 | B2 spec (`EF:669-682`) | build | vfx-designer · opus · h | locked timeline, `spec.json`, reviews | final `spec.json`, `frame-script.md` (textures, reduced-flash and reduced-motion variants) | 27 | `JT:104` | |
| 27 | B2 cue cards (`EF:683-695`) | build | sound-designer · opus · m | locked timeline, markers, `spec.json`, temp sound | `output/sound/<effect>/` cue cards, prompts, mix plan, listening-test plan | 28 | Final sound after the lock: `JT:104` | |
| 28 | IMP final clip, if animated (`EF:699-702`) | build | animator · opus · m (Studio) | | `import-record.md` | 29 | | |
| 29 | W candidate wiring (`EF:703`) | build | feature-builder or quick-builder · opus · m (Studio) | `spec.json`, cues, locked timeline | code, tests, hooks, `capture-setup.md` | 30 | | |
| 30 | CAP candidate-r0 (`EF:707`) | build | studio-operator · sonnet · m (Studio) | | captures at phone and desktop, plus named captures the risks need | 31 | `JT:16` named captures | |
| 31 | Review chain, rounds 0-2 (`EF:716-824`) | build | steps 17-22 again, plus: qa-lead · opus · m (Studio) if a truth risk is named (`PF-02`/`04`/`06`/`10`: `EF:47-48`); live-ops-designer · opus · m if `event` | as in 17-22 | `reviews/candidate-r<n>-*.md`, qa-lead's protected tests | owner (G3) | `JT:106` risk-gated slots; G3P:118 | |
| G3 | owner | gate | | | | close | `CO:32` | |
| 32 | `repair` (`EF:827-855`) | repair | vfx-designer · opus · h scope step; then makers, wire sync, capture, review chain rounds 0-2 | | | | | |

## B3. Counts per effect job (harness-run unless marked FORMULA)

| Piece | Minimum | Max, one maker per repair round (harness) | Ceiling (FORMULA) |
| --- | --- | --- | --- |
| direction | 9 (not new look, no consult); 11 with art consult; 12 new look | 10 / 12 / 13 (a signature refused) | same |
| proof | 15 static; 18 animated | 33 static; 36 animated (art finding, vfx repairs, 3 review rounds) | 40 static; 46 animated: pre-review work 12 (static) or 16 (animated), both with 2 envelope rounds + 3 reviews ×6 + 2 repairs ×(5 static / 6 animated) |
| build | 11 static; 13 animated; +1 qa-lead, +1 live-ops with those risks | 29 static no risks; 39 animated with qa + live-ops and a timing move | 33 / 37 without qa/live-ops; 39 / 43 with both |
| whole job, L or M | **35** static, **40** animated (37 / 42 with a truth risk and `event`) | 10 + 33 + 29 = **72** static; 10 + 36 + 39 = **85** animated with risks | 12 + 40 + 39 = **91** static; 13 + 46 + 43 = **102** animated, new look |
| `repair` stage | 10 static (scope 1 + vfx fix 1 + wire sync 1 + capture 1 + 6 reviews) | 13 animated with all five makers (harness), then up to 2 review rounds | |

Agent runs by role at the minimum (static): vfx-designer 11, sound-designer 8, game-designer 6, studio-operator 4, feature-builder 2, reviewer 2, art-director 2. Animated adds animator 5.

Owner-facing counts: gates L 3 / M 2; exchange rounds: direction D2 ×1, envelope ×1-2 (a merge each round), no other exchange; stage calls L 3 / M 2 (+ `repair`); the full 6-8 reviewer chain runs **twice** (once on the proof, once on the final), so 12 to 16 review runs at the minimum.

## B4. The needs and interface steps in detail

1. **D2 exchange (row 2):** game-designer, vfx-designer, sound-designer (and art-director for a new look) read each other once; an art-director consult note appears when VFX proposes a new colour role or shape-code entry (`EF:293-296`).
2. **The contract chain (rows 6-8):** a fixed sequence, not a conversation. The game-designer writes the window (`gameplay-window.md`). The animator (only if `animated`) places the beats inside it as a draft timing list: the markers VFX and sound key to before they build (`EF:521`). The vfx-designer writes the one event timeline (`contract-timeline.md`) from those two with empty envelopes.
3. **The envelope round (rows 9-11):** this is the crafts-agree-together step.
   - Who: VFX proposes, then sound and (if animated) the animator answer in parallel on VFX's file, then VFX merges. Four agents when animated, three when not.
   - Files: `DIR/exchange/env-r<n>-vfx-designer.md`, `env-r<n>-sound-designer.md`, `env-r<n>-animator.md`; the merged result is the next revision of `DIR/contract-timeline.md` plus `content/vfx/<effect>/frame-script.md`.
   - Rounds: 1, or 2 if any conflict or missing item came back (`EF:585`). The merge runs every round. Open items after round 2 become an owner question for the next gate (`EF:576`).
   - Limits: VFX may not move a gameplay time (game-designer's) or an animation beat (animator's); it asks the decision owner (`EF:554,576`).
   - Not in this job: environment, modeler, rigger, UI, architect. The sound-designer does not see the animator's note and the animator does not see sound's (each answers on VFX's file only).
4. **The lock (row 25) before final sound (row 27):** final VFX and cue cards wait for the locked timeline and final timing list (`JT:104`).

## B5. Where the hand-run recipe and the saved script differ

| # | Recipe says | Script does | Lines |
| --- | --- | --- | --- |
| 1 | Scripts first; a FAIL stops the other reviews (`RD:13`, `JT:106`; the cutscene does this) | the scripts step runs, then the maker self-review, the code review, the qa-lead and the creative chain all run regardless of its result | `EF:736-797` vs `CS:783-785` |
| 2 | Code findings get 3 repair rounds, other findings 2 (`CO:107,132`; `RD:15`; cutscene does) | rounds 0-2 for every finding, so code gets 2 | `EF:731,807` vs `CS:837` |
| 3 | Proof reviewers: the art-director's blocking check (`JT:103`) | the proof runs the full chain: scripts, vfx self-review, game-designer, art, sound sync and reviewer (6 runs) | `EF:631,716-797` |
| 4 | game-designer is a direction lead; the window is the designer's | the designer writes the window in D1 (`EF:270`) and again as `gameplay-window.md` (`EF:505`) and again reviews twice | `EF:270,505,790` |
| 5 | vfx-designer: high for new or important, medium for small (`.agents/roles/README.md:15`) | pinned high for every call | `EF:84` |
| 6 | Builder high on money/saves/remotes (`README.md:24`) | wiring builder always medium; the quick-builder variant is told to stop if money/saves/remotes appear | `EF:89,402-404` |
| 7 | G1 shows options with failed options and closed doors (`JT:138`, `RD:64`) | the `g1` result has no `failed_options` or `closed_doors` fields; they sit in `direction.md` text only | `EF:141,365` vs `CS:138-139,336-337` |
| 8 | "For an M job shown at G3" (`JT:103`) | M `build` runs the whole proof plus its review chain, which can stop with `needs-decision` before any owner gate | `EF:864-867,807-809` |
| 9 | Hand-run: peer messages and resumed makers (`SK:61,66`) | files only, fresh calls (`EF:158`) | |
| 10 | A "needs round" before the proof is a cutscene concept (`JT:28`); the effect recipe has only a Cooperation row (`JT:102`) | the script has two chained steps before the envelope (window, timing list, timeline) | `EF:505-544` |

---

# PART C: Cross-cutting findings the owner asked to know

**Three most surprising.**
1. **M saves one owner gate and zero agent runs.** Both scripts run the whole proof (and the effect's six-reviewer chain, the cutscene's interface and animatic work) inside M `build`. Cutscene 56 = 56, effect 35 = 35 (`CS:944-948`, `EF:863-868`).
2. **The same cues are designed four or five times.** In a minimum cutscene, VFX runs 5 times and sound 6; the VFX/sound envelope is proposed in P2, again as temp marks, again in B1, then as prototype and final. The film-director runs 12 times and is the only merge point in every round.
3. **The two scripts do not follow the same rules.** The effect script lets all reviewers run after a failed scripts check (the cutscene stops) and caps code repairs at 2 (rules and the cutscene say 3). In the cutscene the candidate captures are taken by the film-director and the scripts step is run by the qa-lead (both Opus); the recipe names the studio-operator for captures (`JT:16`) and the effect script gives its scripts step to the Sonnet operator (`EF:736`).

**Could not map or did not verify.**
- Tokens and wall time per step: not measured (only the Haiku smoke figure in `PP:76`).
- What each role file tells the agent to do inside a step (only the script's brief text was read).
- The lead's own steps (job card, packets, readiness, close, doc-keeper) and image batches are outside the counts.
- No Riot transcript, J019 or J021 folder was opened; all R-ids are second-hand through `DES`/`DJT`.
- Ceiling counts are formulas (no harness input produces every maker in every round); the parts are harness-verified (all-9-makers repair round = 12 runs including import, scene and capture).
- Repair outcomes depend on what reviewers find, so "max" assumes every allowed round is used.
