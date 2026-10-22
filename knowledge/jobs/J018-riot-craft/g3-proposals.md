---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 G3
supersedes: []
---
> Author: J018 G3 consolidator · claude-opus-5-5 · high · 2026-10-22

# J018 G3: changes that need your decision

## What this page is

During J018 the makers wrote 353 proposal rows in 20 files (`proposals/`). 116 rows target the Riot library or other roles' books. The library keeper decided those rows (`library-fixes.md`). The close-out sweeps decided the rest (each `coverage/<role>.md`, "Proposal sweep").

238 rows target files that change only with your yes: job recipes, saved job workflows, `rules/`, `tools/`, templates, eval briefs, shared skills outside J018 and role frontmatter. This page merges them into 11 decisions. The appendix lists every row and its decision.

Nothing in these files changed during J018. Check: `git status` and `git log` show no change to `tools/`, `templates/`, `rules/`, `.agents/workflows/jobs/`, `job-types.md`, `studio-mcp`, `platform-policy` or any `evals/` after the J006 commit `df13ff4`.

**How to answer.** Give one word per decision. "Yes" accepts the recommendation as written. "No", "later" or your own words change it. A decision you do not answer gets its default.

## Summary

| ID | Decision | Rows | Recommendation | Default if you do not answer |
| --- | --- | --- | --- | --- |
| G3-P1 | Make the kit tools give right numbers | 22 | yes | Known tool bugs stay. Books keep hand-written measures. |
| G3-P2 | Job recipes: cheap passes first, crafts join early | 33 | yes | Recipes keep the old order. |
| G3-P3 | Job recipes: review evidence and review slots for truth | 17 | yes, only for jobs with that risk | No new review slots. |
| G3-P4 | Saved workflows follow the recipes, stale text fixed | 27 | yes | Stale lines stay. Workflows skip the new stages. |
| G3-P5 | Binding rules: honest reveals, no success on denial, review keys | 5 | yes | Rules stay only in the role books. |
| G3-P6 | Templates, game records and eval briefs carry the new stages | 50 | yes | Agents add fields by hand. Some eval checks fail correct work. |
| G3-P7 | Studio probes and capture recipes, run once | 13 | yes | These checks stay "not verified". |
| G3-P8 | New measuring options in existing tools | 44 | yes, after G3-P1 | Books keep one-line commands outside the tool record. |
| G3-P9 | Option images: new art bible families, medium-quality roughs | 7 | yes | Old locks stay. Roughs stay at medium. |
| G3-P10 | New kit tools | 15 | later | Later. |
| G3-P11 | Sound designer: Studio tools and preloaded skills | 2 | no | No change. |

Rows counts include 5 rows that split across two decisions (see the appendix).

## G3-P1 Make the kit tools give right numbers

**What would change**
1. Fix known bugs in existing tools. Each bug gives a wrong number with no error today.
   - `tools/anim/clip_check.py`: read quaternion letters in Blender's order (w, x, y, z). Warn when a channel does not match the bone's rotation mode. Refuse or convert degrees on a quaternion channel.
   - `tools/art/look_check.py`: use a tight key tolerance on flat render backgrounds. Warn when subject pixels are near the key colour, or a shadow lies on the key. Report the unlisted silhouette area. Report which side of the ring is brighter.
   - `tools/vfx/clip_metrics.py`: correct the frame name in the docstring. Order frames by number. Warn when a frame file is skipped.
   - `tools/film/shotlist.py log-diff`: a one-sided sync window. Accept `shot:<id>`. Fail when planned ids are missing.
   - `tools/art/thumb_check.py`: warn on an inverted mask. Report boxes given, not pieces. Never overwrite another run's sheet. Refuse a stretched crop.
   - Small fixes in `tools/liveops/feedback_count.py`, `tools/progression/sim.py`, `tools/hooks/handback_check.py` and `tools/art/art_refs.py`.
2. Build three tested tools. Each replaces a measuring recipe that the books now print by hand.
   - `tools/vfx/flash_count.py`: the flash counter of `vfx-craft/references/measure.md` §6, plus a red-flash count and a first-frame warning.
   - `tools/audio/cue_check.py`: the sound file measures F-01 to F-13 of `sound-design/references/review.md` §4.
   - `tools/rig/rig_audit.py`: new modes `caps`, `overlap` and `orient`.
3. Each tool gets offline tests. The fixtures are the J018 review cases with their true values. After that, each book names one command and keeps the eye check.

**Why (evidence)**
- After wave 2 round 3, six roles each ended with one blocking finding of one class: a measuring recipe in the book gave a wrong number with no error (`stage2-brief-v2.md` v3).
- Each later round found a rarer case. The flash counter failed in four review rounds (vfx rev1-rev4, film rev3-rev4, marketing rev3). The sound measures failed in four rounds (sound rev1-rev4). The rig cap count failed in four rounds (character-rigger rev1-rev4).
- The lead stopped that loop and sent these measures to G3 (`stage2-brief-v2.md`, v3 addendum).
- The bugs are in the code now (read at HEAD). `clip_check.py:379` maps quaternion letters with "xyzw", so `.w` reads z. A 30° tilt against ±15° measured 0 and passed (character-rigger review F2).
- `clip_metrics.py:35` sorts frames by name. `f1000` comes before `f101`, so a flash at 33167 ms read 33500 ms (vfx repair round 3).
- `shotlist.py:1174` compares the absolute offset. A sound cue 30 ms early passes a 40 ms tolerance, but the sync rule allows one frame early (16.7 ms).
- The default key tolerance 40 removed a lit head from every black-fill. The box was 768 px high, the true height 932 px (modeler rev3).

**Who asked:** character-rigger, environment-designer, film-director, game-designer, level-design, live-ops-designer, marketing, modeler, orchestration, progression-designer, qa-lead, reference-images, sound-designer, vfx-designer.

**Recommendation: yes.** Silent wrong numbers were the most expensive fault in J018. Tests keep each fixed case fixed.

**Risk.** This is a medium tools job. A new tool can have its own edge cases, but its tests stop old cases coming back. The `clip_check.py` fix can change old rig results: earlier quaternion range checks may have passed falsely. The books need a second small edit to name the new commands.

**Default if you do not answer.** No change. The books keep the hand recipes as labelled screening aids with an eye check (brief rule V14). The known bugs stay.

## G3-P2 Job recipes: cheap passes first, crafts join early

**What would change.** `.agents/skills/orchestration/references/job-types.md`:
1. Cross-type rules, written once: a craft that keys from another's output states its needs before the producer builds. One marker list per job. Gates close the options not picked, with a return condition. Every gate packet has a could-not-check list.
2. "G1 shows" (character, stage, UI, cutscene, marketing): 2-3 options at equal finish, each from its own hook, the warm-up labelled. Each option is shown in grey and black-fill at the size players see it. One recommendation, with why the others lost.
3. The proof (G2) is a cheap pass. Character: the signature pose and the 2-3 hardest stress poses in black-fill at the game camera. Stage: a grey value pass, with the key light chosen in grey. Effect: a blocking pass before textures. Cutscene: blocking and value strips before boards. Marketing: a 3-value study and 2-3 light set-ups.
4. Crafts join earlier. The animator gives frame lengths, markers and reaction windows at feature and character direction. Sound joins at feature direction, at the stage kit list and in a character needs round. The architect collects the crafts' needs before the plan freezes. The reward tier table is in the feature contract. The modeler checks the reference set. A new enemy gets a plain-block behaviour test before the modeler starts. The art director is consulted on a new colour role. The direction states the R15 rig limits.
5. Order inside production: the feature skeleton before presentation. The animator's markers go to VFX and sound before either builds. Temp sound sits on the blocking markers. The UI motion storyboard has sound and VFX on one beat list. A UI read-order failure returns to the grey pass.

**Why (evidence)**
- The rebuilt books put cheap passes first (grey, black-fill, blocking, options at equal finish). The orchestration book already holds the general rules (`coverage/orchestration.md` V11 table: S §4.1, §5.2, §8). The recipes still show the old order, so a job lead who follows a recipe skips these stages.
- The character recipe has no behaviour test. The game designer must block the job or skip its own rule (game-designer rev3 R9, `job-types.md:42`).
- The art director first sees the stage light at the final review (`art-director.md:31`).
- VFX and sound key from animation markers that do not exist yet when they start (`animator.md:31`, `sound-designer.md:26`).

**Who asked:** animator, architect, art-director, character-rigger, environment-designer, feature-builder, film-director, game-designer, level-design, marketing, modeler, orchestration, progression-designer, reference-images, sound-designer, ui-ux-designer, vfx-designer.

**Recommendation: yes.** Changes cost least before the build. The recipes and the lead's book then agree.

**Risk.** The start of each job takes longer and uses more images before G1. Recipes get longer. To limit this, write shared rules once in "Cross-type rules" and keep recipe rows to placements only.

**Default if you do not answer.** The recipes do not change. The lead applies the general rules from the orchestration book. The recipe-specific steps do not happen.

## G3-P3 Job recipes: review evidence and review slots for truth

**What would change.** `job-types.md` proof, integrator and review rows:
1. The integrator delivers the Studio-only test hooks and the debug log at the wiring step, before any partner's first capture (feature, effect, UI).
2. Named review captures: a rejected request, a slow confirmation, a two-client view with a bystander, the server's hit shape as an overlay, grayscale with sound off and reduced motion, the lowest graphics setting, a roster lineup for a new character, one capture per paid-reveal tier, the smallest phone.
3. New review slots, only when the job carries the risk:
   - the reviewer checks the plan before the builder starts, for money, saves, remotes, trades or paid random items
   - the qa-lead runs protected acceptance for effects with gameplay truth, UI truth rows, stage measures and sold variants
   - the progression designer reviews shop, odds and progress screens
   - the live-ops designer reviews event jobs on named captures.
4. The gate packet names two owner listens: the key event alone, then the full mix, on a phone speaker and on headphones.

**Why (evidence)**
- Truth checks need inputs that the recipes do not name. They end on could-not-check lists or are found late.
- The DestructionSimulator reviewer found money farms only at merge (`reviewer.md:17`).
- The game designer cannot judge "does the effect hide information" from single stills (`game-designer.md:18`).
- No recipe gives the live-ops designer a review slot (`live-ops-designer.md:19`).
- The orchestration book already asks for a rejected-request capture (S §13, §14). The recipe text does not.

**Who asked:** architect, art-director, feature-builder, game-designer, live-ops-designer, progression-designer, qa-lead, reviewer, sound-designer, ui-ux-designer, vfx-designer.

**Recommendation: yes, only for jobs with the risk.** A new slot runs only when the job has a server-confirmed result, money, saves, paid random items, a frequent effect or a sold variant. This catches truth faults at the cheapest stage.

**Risk.** More agent calls, tokens and Studio captures per job. One more exchange before the build for money features. The studio operator gets a longer capture list.

**Default if you do not answer.** No new slots. The crafts run these checks as self-review only. A later wiring change can break them and nobody sees it.

## G3-P4 Saved workflows follow the recipes, stale text fixed

**What would change.** `.agents/workflows/jobs/job-*.js`:
1. Stale text, wrong today (found by grep at HEAD):
   - `job-stage.js:591` says "level-design 14 checks". The level review now has the fixed checks C1-C19, each re-rated every round.
   - `job-effect.js:366` names frames `f###_<ms>.jpg`. `clip_metrics.py` reads only `f###_<ms>ms.jpg`, so the captures cannot be measured.
   - `job-marketing-art.js:290` points to the J016 `riot-extracts.md`. The craft now lives in `marketing-craft/references/image-pipeline.md` §1.
   - `job-ui-screen.js` names the self-review "§5". It is now `ui-design/references/review.md` §5-§6.
   - The marketing scripts step measures whole masters. It needs a hero mask.
2. New stage text, only for the recipe rows you accept in G3-P2 and G3-P3: the direction stage of every workflow, the character blockout, value gate and stress poses, the stage grey pass and light checks, the cutscene stages, the UI stages, the feature reviewer call, and two image batches with your pick between them.

**Why (evidence)**
- A saved workflow runs its own text. Inside a workflow, the books' new stages are skipped unless the intent and checks name them (`orchestration.md:21`).
- A reviewer briefed with "14 checks" stops at C14 and skips C15-C19 (`level-design.md:29`).
- Frames named as the effect workflow says cannot be measured (`vfx-designer.md:24`).

**Who asked:** art-director, character-rigger, environment-designer, film-director, level-design, marketing, modeler, orchestration, reference-images, reviewer, ui-ux-designer, vfx-designer.

**Recommendation: yes.** Fix the stale text first. Then change stage text only where you accepted the recipe row. The workflows then run the same jobs as the recipes.

**Risk.** Each edit needs `tools/tests/test_job_workflows.py` and a smoke run. A wrong check can block a stage.

**Default if you do not answer.** No change. The stale lines stay, and the saved workflows run the old stages.

## G3-P5 Binding rules: honest reveals, no success on denial, review keys

**What would change**
1. `.agents/skills/platform-policy/references/rules.md` §A gets the reveal-honesty checks:
   - one identical windup for every result, up to the result frame
   - no higher-tier layer on a lower result
   - no celebration of a result worth less than its price
   - luck effects never imply better odds
   - odds never covered or animated by effects
   - a frame compare of the lowest and the highest tier.
2. `.agents/skills/networking-security/SKILL.md` N-14: a denied or unavailable result never shows a success layer, sound or label.
3. `rules/messages.md` §2 and `templates/jobs/intent-brief.md`: optional keys `budget` and `stop`.
4. `rules/messages.md` §6 and `templates/jobs/review.md`: keys `could_not_check` and `weakest_part`, and per finding `protect` and `retest`.
5. The "Odds" label question (`ui-ux-designer.md:33`): no policy text change. The policy names only "Info" or "Details". The books show both words ("Odds · Details").

**Why (evidence)**
- The honest-reveal rules live only in the design books now. The policy reviewer does not run them (`game-designer.md:24`).
- Success shown on a denied request is the most common presentation fault in the library. N-14 does not say it (`reviewer.md:26`). The architect sweep confirmed that `architecture` R-19 holds the rule.
- Reviewers write what they could not check in free text below the spec block. A fixed key makes it checkable (`reviewer.md:19`).

**Who asked:** game-designer, orchestration, reviewer, ui-ux-designer.

**Recommendation: yes.** The binding files then hold the rules the rebuilt books already follow. The new keys are optional, so old hand-backs stay valid.

**Risk.** Every agent reads `rules/messages.md`. The hand-back hook (`tools/hooks/handback_check.py`) and `templates/jobs/handback.schema.json` may need the same keys. The policy text must match `paid-random-items.md` exactly.

**Default if you do not answer.** No change. These rules stay only in the role books.

## G3-P6 Templates, game records and eval briefs carry the new stages

**What would change**
1. Templates get slots for what the rebuilt books ask agents to write:
   - `templates/anim/` (timing list, animation set, motion profile, motion spec) and `templates/rig/rig-sheet.md`
   - `templates/environment/` (stage blueprint, review packet, ambience map)
   - `templates/film/` and `templates/jobs/beat-sheet.md`
   - `templates/marketing/` (thumbnail brief, icon checklist, short-video plan, a new `surfaces.md`)
   - `templates/model/asset-record.md` and `templates/live-ops/` (event design, update plan)
   - new `templates/level/route-graph.md` with a route JSON example
   - `templates/jobs/` (job card, direction sheet, decision digest, a new gate-packet skeleton). Closed doors stay one table in the job's `decisions.md`.
2. Per-game records:
   - `templates/skill/art-bible.md` direction rows: value bands (grey value with luminance), separation targets, reserved colours, key light per place, shape vocabulary, identity anchors (one count), palette roles, motion line, UI thematic, tier exceptions. One copy, as in `art-review/references/art-bible.md` §7.
   - `knowledge/design/game-profile.md`: smallest phone viewport, on-screen character height, asset naming rule.
   - `knowledge/design/vocabulary.md`: the shared event names, at the first game job.
   - `tools/progression/examples/*/design.md`: a reward tier table in each worked example.
3. Eval briefs (`evals/briefs.md` of animation-craft, architecture, art-review, environment-craft, marketing-craft, modeling-craft, rigging-craft, sound-design, ui-design, vfx-design and code-review, plus new evals for `testing`) test the new stages. Checks that now contradict the rebuilt books or `platform-policy` are fixed.

**Why (evidence)**
- The books tell agents to add these fields to their own copy. A filled template can skip them.
- The art bible has no rows for the numbers that five crafts check. Each check falls back to PROPOSAL values (`art-director.md:17`, `modeler.md:26`, `environment-designer.md:31`, `:36`, `ui-ux-designer.md:28`).
- Some eval checks fail correct work today: sound-design 3.5, 4.2, 4.3 (sound reviews rev1 R8, rev2 R2), vfx-design 1.4 and 3.3 (vfx review R6), rigging-craft 1.4 (rigger review R7), animation-craft A6 (animator repair round 2).
- The `testing` skill has no evals (`qa-lead.md:28`).

**Who asked:** animator, architect, art-director, character-rigger, environment-designer, film-director, game-designer, level-design, live-ops-designer, marketing, modeler, orchestration, progression-designer, qa-lead, reviewer, sound-designer, ui-ux-designer, vfx-designer.

**Recommendation: yes.** Templates point to the book sections and do not copy their rules (one rule, one place). Filled templates and graders then match the books.

**Risk.** About 30 files change. Templates get longer. Changed evals change scores, so old and new eval results do not compare.

**Default if you do not answer.** No change. Agents keep adding fields by hand. Graders can fail correct runs.

## G3-P7 Studio probes and capture recipes, run once

**What would change.** Run each probe once in Studio. Record the result and the recipe in `.agents/skills/studio-mcp/references/probes.md` (and one line in `SKILL.md` §4):
- graphics quality: `settings().Rendering.EnableFRM` false, `EditQualityLevel` lowest and highest, then restore. One probe for all roles, not `QualityLevel`
- flat-key and mask captures: a plain magenta backdrop, shadows off, then restore
- layer cuts: UI off, effects off, characters off, and all three off (environment only), plus row markers
- a top-down capture, the movement values and the jump-ladder steps
- capture field of view and aspect, and a held item in the hand in Play
- Bone scale in an imported clip
- the Device Simulator at named sizes, reduced motion, the largest text
- frame folders `f###_<ms>ms.jpg` from a trigger, and a freeze with `TimeScale = 0`
- a named event capture set
- drive game code through Studio-only attributes, never through a required module.

**Why (evidence)**
- Ten roles wrote checks that need these captures. The books mark them "probe first" or not verified.
- Two roles proposed different quality properties (`game-designer.md:33`, `environment-designer.md:37`). The docs say `QualityLevel` applies only while the frame-rate manager is on (`RenderSettings.yaml:256-261`). The probe settles it.
- An in-scene capture gives `invalid-mask` in `look_check.py`, so black-fill checks need a flat key (`game-designer.md:35`).

**Who asked:** art-director, character-rigger, environment-designer, feature-builder, game-designer, level-design, live-ops-designer, modeler, ui-ux-designer, vfx-designer.

**Recommendation: yes.** One probe pass replaces about ten improvised recipes. It needs one Studio session.

**Risk.** It needs a Studio place and the studio operator. Some probes can show that MCP cannot do a step. Then the fallback is recorded. Every probe must restore the scene.

**Default if you do not answer.** No probes. These checks stay "not verified" in reviews.

## G3-P8 New measuring options in existing tools

**What would change.** New options in tools that exist, with duplicates merged (about 20 options from 44 rows):
- `look_check.py`: reserved-colour share by colour distance, band boxes, near-black and clipped-white counts, the brightest region, a ring per subject with a contrast rank, masks with boxes, mirror and squint views, a contact sheet, detail density at phone size, palette roles as rendered, silhouette footprint numbers, thumbnail crop and subject height, a ring against a given ground colour, an expected component count, a small-mask option, letterbox exclusion.
- `thumb_check.py`: polygon masks, grid and crop modes, mirror and 3-value panels, a sharpness estimate, a sliver measure.
- `clip_metrics.py`: an idle-frame background, a region, a press-relative onset, rise and fall times, a flash block, information-area boxes, effect masks.
- `clip_check.py`: curve checks (spacing, arcs, overlap, twinning, holds) and an orientation hold.
- `review_renders.py` (or a new `pose_renders.py`): posed black-fill renders at the game camera, a back view, the phone aspect, a background colour, lit grey and flat views.
- `model_audit.py`: projected part height at the game camera, texel density.
- `scene_probe.luau` and `scene_audit.py`: material, collision and mesh id, and a compare with the approved blockout.
- `shotlist.py`: a cadence line, read and value fields. `sim.py`: a reward-rate summary. `curves.py`: display rounding.

**Why (evidence)**
- Each option replaces a one-line command that sits outside the tool's record. Brief rule V13: a measure longer than a few lines belongs in a tested tool.
- Several one-liners gave wrong numbers with no error. A k-means palette merged a 0.072 % reserved-red accent, ΔE 24 (`art-director.md:19`).
- A whole-frame palette read sky as team colour, 0.338 against 0.0 in a box (`environment-designer.md:28`).
- The median background inverted every number when an effect stayed in 70 % of the frames (`vfx-designer.md:17`).

**Who asked:** animator, art-director, character-rigger, environment-designer, film-director, game-designer, level-design, marketing, modeler, progression-designer, qa-lead, reference-images, ui-ux-designer, vfx-designer.

**Recommendation: yes, after G3-P1.** Build it as one tools job. Build first the options that two or more roles asked for. Every craft then gets the same numbers, with tests.

**Risk.** This is the largest group. The tools grow, and each option needs fixtures and a line in `tool-modes.md`. Build only options that a book check names (anti-overengineering).

**Default if you do not answer.** No change. The books keep their one-line commands as labelled screening aids.

## G3-P9 Option images: new art bible families, medium-quality roughs

**What would change**
1. `templates/skill/art-bible.md` families and locks:
   - a `view` family: exactly one orthographic view (front, side, back, top or the game camera)
   - a `rough` family: a flat 3-value study, no rendering, no text (marketing calls it `thumbnail-rough`)
   - a `paintover` family: an edit of a capture that changes only the named elements
   - an exact background clause for the character, creature, prop, model and pose locks: flat even light grey, no gradient, no floor shadow.
2. You confirm the reading of your decision J009-D17. Rough (R1) and iterate (R2) images use medium for every family. High is for the green-lit finals of icons, characters, creatures, hero models, key art and marketing images.

**Why (evidence)**
- A "back view" request contradicts the three-quarter locks, and the lock wins. `art_refs.py print` assembled both with no error (`reference-images.md:17`). Modelers and riggers need back and side views.
- Full-render locks make every rough look finished. A scene rough then needs a hand-traced mask before any number means something (`marketing.md:25`).
- A light-grey gradient with a white collar broke the part count (`reference-images.md:19`).
- J009-D17 lists those families as high. A 3-5 option round at high makes roughs the most expensive images of a job (`reference-images.md:29`, `marketing.md:26`).

**Who asked:** art-director, marketing, reference-images (the modeler and the character-rigger asked for the views).

**Recommendation: yes.** Options are judged on big shapes, at a lower cost. Build views become possible.

**Risk.** New families change the prompts of every game that uses the template. Medium roughs show less detail at your pick. You pick on shape, and the final is made at high.

**Default if you do not answer.** The template keeps its current locks. The books keep I-13 (roughs at medium) as the lead's reading of J009-D17 until you say otherwise.

## G3-P10 New kit tools

**What would change.** New tools:
- one debug-log checker (`fx_log.py` and `log_check.py` merged)
- one frame-sequence compare (`seq_compare.py`, asked by three roles)
- one route-time tool (`route_times.py`, asked by two roles)
- `contract_check.py`, `present_scan.py`, `spec_check.py`, `hit_targets.py`, `packet_check.py`
- a video and audio check (it needs ffmpeg: an install decision for you)
- shared Luau modules in `templates/code/` (test hooks, debug log, comfort settings, hit-stop owner)
- a `verify.py` gate check that the production build holds no test hooks.

**Why (evidence).** Each tool replaces a manual count or grep in the rebuilt books. No real game job has run these checks yet.

**Who asked:** architect, feature-builder, game-designer, level-design, marketing, orchestration, qa-lead, reviewer, ui-ux-designer, vfx-designer.

**Recommendation: later.** Build each tool when the first real game job needs it. Real games are the test bed (J018-D3), and the kit builds no tool before its first use. Build the `verify.py` hook check with the first game that adds test hooks.

**Risk of "later".** Manual counts in bursts stay slow and can be wrong. Each game can write its own hook modules.

**Default if you do not answer.** Later. No change now.

## G3-P11 Sound designer: Studio tools and preloaded skills

**What would change.** `.agents/roles/sound-designer.md` frontmatter:
- `tools:` add six Studio MCP tools, `execute_luau` among them
- `skills:` preload `platform-policy` and `studio-mcp`.

**Why it was asked.** Self-review lines R-14, R-16 and R-40 to R-42 need the audio graph, the floor materials and the cue log from Studio (`sound-designer.md:19-20`).

**Who asked:** sound-designer.

**Recommendation: no.** The tools line is your permission (J018-D2 point 1). `execute_luau` runs any code, so it is not read-only. One agent drives each Studio instance (AGENTS.md §3), and the studio operator runs these checks. J017 keeps role skills on demand, and the sound book loads `platform-policy` before any paid reveal.

**Risk of "no".** Sound checks in Studio wait one round for the studio operator.

**Default if you do not answer.** No change.

## Appendix: every in-scope row

Abbreviations: `job-types.md` = `.agents/skills/orchestration/references/job-types.md`. `job-*.js` = `.agents/workflows/jobs/`. Tool paths are under `tools/`. `art-bible.md` = `templates/skill/art-bible.md`. File:line points into `proposals/`. A row with two group ids splits across two decisions. "Merged" names the row that carries the same change.

| proposal file:line | target | short change | group id or "closed: why" |
| --- | --- | --- | --- |
| animator.md:17 | anim/clip_check.py | `curves` checks: spacing, arcs, overlap, twinning, holds, beat gaps | G3-P8 |
| animator.md:18 | model/review_renders.py or new anim/pose_renders.py | posed black-fill renders at the game camera, contact sheet, preview video | G3-P8 |
| animator.md:19 | templates/anim/timing-list.md | freeze frame, sync rule, attempt and outcome column, verb, end-of-state tells | G3-P6 |
| animator.md:20 | templates/anim/animation-set.md | reaction window, play rate, pushed moments, reduced variant, beat sheet line | G3-P6 |
| animator.md:21 | templates/anim/motion-profile.md | feel words, identity anchors, costly parts with fallback | G3-P6 |
| animator.md:22 | templates/anim/motion-spec.md | personality, reduced motion, pulse class, truth fields | G3-P6 |
| animator.md:23 | templates/rig/rig-sheet.md §B (and rig-pipeline) | standard animator needs in the rig sheet, template half (merged: character-rigger.md:17) | G3-P6 |
| animator.md:28 | animation-craft/evals/briefs.md | test new stages, count plan-stage images apart from the 8-image cap | G3-P6 |
| animator.md:30 | job-types.md character, Proof | signature pose in black-fill at the game camera, picked from 2-3 options | G3-P2 |
| animator.md:31 | job-types.md effect, Cooperation | blocking markers to VFX and sound before they build | G3-P2 |
| animator.md:32 | job-types.md character, Direction | game designer states reaction window and play rate | G3-P2 |
| architect.md:17 | job-types.md §5 feature | crafts' needs round before the plan freezes | G3-P2 |
| architect.md:18 | job-types.md §5 feature, Review order | presentation captures named, architect reviews cost and contract | G3-P3 |
| architect.md:21 | new contract_check.py | cross-file event-id check, literal lint | G3-P10 |
| architect.md:23 | architecture/evals/briefs.md | E-05 melee hit, E-06 coin pickups | G3-P6 |
| architect.md:24 | knowledge/design/vocabulary.md | shared event names at the first game job | G3-P6 |
| art-director.md:17 | art-bible.md | direction-record rows (bands, separation, reserved colours, key light, shape, anchors, palettes, motion, UI thematic, exceptions) | G3-P6 |
| art-director.md:18 | art-bible.md | `paintover` family and lock | G3-P9 |
| art-director.md:19 | art/look_check.py | `reserved` measure by colour distance | G3-P8 |
| art-director.md:20 | art/look_check.py | `bands` measure per band box | G3-P8 |
| art-director.md:21 | art/look_check.py | `--mirror`, `--squint`, `sheet` mode | G3-P8 |
| art-director.md:22 | art/look_check.py silhouette | area and box ratios in native pixels | G3-P8 |
| art-director.md:23 | art/look_check.py | supports the `detail` mode (merged: modeler.md:35) | G3-P8 |
| art-director.md:24 | studio-mcp probes.md | layer-cut and environment-only captures, row markers | G3-P7 |
| art-director.md:26 | art-review/evals/briefs.md | hooks, grey pass, cold read, paint-overs, new E6 | G3-P6 |
| art-director.md:29 | knowledge/design/game-profile.md | smallest phone viewport, quality floor (merged: modeler.md:27) | G3-P6 |
| art-director.md:31 | job-types.md stage, Check-ins | 2-3 grey lighting variants, paint-over on the first rough | G3-P2 |
| art-director.md:32 | job-types.md stage Proof and Review, job-stage.js | capture set: layer cuts, environment-only, lowest quality, mask, row markers | G3-P3, G3-P4 |
| art-director.md:33 | job-types.md effect, Direction | consult the art director on a new colour role or shape code | G3-P2 |
| art-director.md:34 | job-types.md character, G1 shows | options that passed the grey pass, grey and black-fill at phone size | G3-P2 |
| art-director.md:37 | art/look_check.py | `extremes` measure: near-black and clipped white | G3-P8 |
| art-director.md:39 | art-bible.md, reference-images | supports the `thumbnail-rough` family (merged: marketing.md:25) | G3-P9 |
| art-director.md:40 | role frontmatter | none | closed: no change proposed |
| art-director.md:42 | art/look_check.py value | brightest region, one dark and light measure | G3-P8 |
| art-director.md:43 | art-bible.md | one count for identity anchors | G3-P6 |
| character-rigger.md:17 | templates/rig/rig-sheet.md §B, §C, §F | standard needs, design-for-motion keys, posed-plan and spin-hold rows | G3-P6 |
| character-rigger.md:18 | rig/rig_audit.py and tests | `caps`, `overlap`, `orient` modes with J018 fixtures | G3-P1 |
| character-rigger.md:19 | anim/clip_check.py | quaternion letter order, rotation-mode warning, degrees on quaternions | G3-P1 |
| character-rigger.md:20 | anim/clip_check.py | `orient_hold` check | G3-P8 |
| character-rigger.md:21 | model/review_renders.py | posed mode, black-fill, edge-touch flag (merged: animator.md:18) | G3-P8 |
| character-rigger.md:25 | studio-mcp probes.md | Bone scale probe | G3-P7 |
| character-rigger.md:27 | job-types.md character, Proof | 2-3 hardest stress poses with overlap and cap numbers | G3-P2 |
| character-rigger.md:28 | job-character.js S2, K1 | design-for-motion and read-control checks | G3-P4 |
| character-rigger.md:29 | job-character.js P3 | stress poses and their numbers in the proxy-pose call | G3-P4 |
| character-rigger.md:30 | job-types.md character, Direction | state R15 limits for shared clips | G3-P2 |
| character-rigger.md:31 | art/look_check.py silhouette | `--min-frac`, `unlisted_area_px` | G3-P1 |
| character-rigger.md:32 | rigging-craft/evals/briefs.md | check 1.4: numbers per pose, images only on failure | G3-P6 |
| environment-designer.md:17 | job-stage.js P4 | grey value pass, key light chosen in grey | G3-P4 |
| environment-designer.md:18 | job-stage.js B2 art production | floor read and band checks | G3-P4 |
| environment-designer.md:19 | job-stage.js B2 place-kit | in-set capture of each kit piece (merged: modeler.md:20) | G3-P4 |
| environment-designer.md:20 | job-stage.js B3 light | lowest and highest setting, light direction kept, post effects off | G3-P4 |
| environment-designer.md:21 | job-stage.js FZ freeze | review list answered, could-not-check list, image budget | G3-P4 |
| environment-designer.md:22 | job-types.md §3 stage | read plan in the contract, grey value pass in the proof, numbers in the art review | G3-P2 |
| environment-designer.md:23 | templates/environment/stage-blueprint.md | read plan section, band, reserved colours, first view, story fact | G3-P6 |
| environment-designer.md:24 | templates/environment/review-packet.md | lowest and highest, review list table, could-not-check list | G3-P6 |
| environment-designer.md:25 | templates/environment/ambience-map.md | signature element, floor materials, emotion, sight lines | G3-P6 |
| environment-designer.md:26 | art/look_check.py thumb | scale `--box`, `--crop` for small objects | G3-P8 |
| environment-designer.md:27 | art/look_check.py value | `--dark-below`, `--light-above` (merged: art-director.md:37) | G3-P8 |
| environment-designer.md:28 | art/look_check.py | `colour` mode: reserved share, chroma, hue spread, grey reference | G3-P8 |
| environment-designer.md:29 | env/scene_probe.luau, env/scene_audit.py | material, collision, mesh id, compare with the greybox | G3-P8 |
| environment-designer.md:30 | studio-mcp probes.md | quality-level probe, flat-key recipe | G3-P7 |
| environment-designer.md:31 | art-bible.md | reserved-colour table, light temperature, palette roles (merged: art-director.md:17) | G3-P6 |
| environment-designer.md:35 | art/look_check.py value | report which side is brighter, help text | G3-P1 |
| environment-designer.md:36 | art-bible.md | separation targets row (merged: art-director.md:17) | G3-P6 |
| environment-designer.md:37 | studio-mcp probes.md | one quality probe: EnableFRM off, EditQualityLevel | G3-P7 |
| environment-designer.md:38 | environment-craft/evals/briefs.md | read plan, grey pass, floor and band checks | G3-P6 |
| environment-designer.md:42 | art/look_check.py palette | roles as rendered, nearest-role distance verdict | G3-P8 |
| environment-designer.md:45 | role frontmatter | none | closed: no change proposed |
| feature-builder.md:17 | job-types.md §5 feature, Production order | skeleton, then presentation, then worst case | G3-P2 |
| feature-builder.md:18 | job-types.md §4-§6, Integrator | test hooks and debug log at the wiring step | G3-P3 |
| feature-builder.md:19 | job-types.md §5 feature, Contract | feedback stack with denial reasons before the builder | G3-P2 |
| feature-builder.md:20 | new studio/fx_log.py | debug-log counter (merged: qa-lead.md:24) | G3-P10 |
| feature-builder.md:21 | new templates/code/ | shared TestHooks, FxLog, Comfort, HitStop modules | G3-P10 |
| feature-builder.md:30 | studio-mcp SKILL.md §4 | drive game code through watched attributes | G3-P7 |
| feature-builder.md:32 | role frontmatter | none | closed: no change proposed |
| feature-builder.md:39 | verify.py | gate check: production build holds no test hooks | G3-P10 |
| film-director.md:17 | film/shotlist.py check | cadence line, equal-length warning | G3-P8 |
| film-director.md:18 | film/shotlist.py log-diff | one-sided sync window, `--require-all` (merged: sound-designer.md:18) | G3-P1 |
| film-director.md:19 | film/shotlist.py | `read`, `value_key` shot fields | G3-P8 |
| film-director.md:20 | art/look_check.py value | exclusions on the whole frame, or `--frame-box` | G3-P8 |
| film-director.md:21 | art/look_check.py value | brightest region, balance centre | G3-P8 |
| film-director.md:22 | art/look_check.py compare-subjects | per-subject masks, `--rank-stat` | G3-P8 |
| film-director.md:23 | art/look_check.py --mask | `--min-mask-frac` | G3-P8 |
| film-director.md:24 | film/shotlist.py log-diff | accept `shot:<id>` | G3-P1 |
| film-director.md:25 | new vfx/flash_count.py | seconded, with film fixtures | G3-P1 |
| film-director.md:27 | templates/jobs/beat-sheet.md | premise, hook, sell list, budget, intensity, options and pick | G3-P6 |
| film-director.md:28 | templates/film/shot-list.md | picture-plan and conventions tables | G3-P6 |
| film-director.md:29 | templates/film/storyboard-brief.md | read fields, blocking still, stale step number | G3-P6 |
| film-director.md:33 | job-types.md §1 cutscene, G1 shows | 2-3 approaches as greybox contact sheets at equal finish | G3-P2 |
| film-director.md:34 | job-types.md §1 cutscene, Proof and Review | blocking and value strips before boards | G3-P2 |
| film-director.md:35 | job-cutscene.js D1 | same change as film-director.md:33 | G3-P4 |
| film-director.md:36 | job-cutscene.js P1, P4 | picture plan, blocking stills as board input | G3-P4 |
| film-director.md:37 | job-cutscene.js P3, P5 | value plan input, value, rhythm and beat checks | G3-P4 |
| game-designer.md:17 | job-types.md feature, Direction | animator consulted for frame lengths and markers | G3-P2 |
| game-designer.md:18 | job-types.md effect, Review | hit-shape overlay, two-client and rejected-request captures | G3-P3 |
| game-designer.md:19 | job-types.md character, Proof | roster lineup capture | G3-P3 |
| game-designer.md:20 | job-types.md stage | route table in seconds and hazard sheets in the contract, lowest-setting capture | G3-P2 |
| game-designer.md:24 | platform-policy rules.md | reveal-honesty checks | G3-P5 |
| game-designer.md:25 | templates/jobs/ closed-doors.md | closed-doors template (merged: orchestration.md:17, one table in decisions.md) | G3-P6 |
| game-designer.md:26 | new seq_compare.py | frame-sequence compare | G3-P10 |
| game-designer.md:27 | new level/route_times.py | route table from a route graph | G3-P10 |
| game-designer.md:30 | job-types.md character, Direction | plain-block behaviour test before the modeler | G3-P2 |
| game-designer.md:32 | vfx/clip_metrics.py | (1) docstring frame name, (2) onset fraction or region | G3-P1, G3-P8 |
| game-designer.md:33 | studio-mcp SKILL.md | quality probe through QualityLevel (merged: environment-designer.md:37) | G3-P7 |
| game-designer.md:34 | role frontmatter | none | closed: no change proposed |
| game-designer.md:35 | studio-mcp SKILL.md | flat-key capture recipe and probe | G3-P7 |
| level-design.md:17 | job-types.md §3 stage, G1 shows | 2-3 layout options with route times | G3-P2 |
| level-design.md:18 | job-stage.js direction focus | options pass, node geometry, route JSON, teaching, pacing | G3-P4 |
| level-design.md:19 | job-stage.js walk test | jump ladder, top-down, lowest setting, flat-key landmarks, zone entries | G3-P4 |
| level-design.md:20 | new level/route_times.py | co-signs game-designer.md:27 | G3-P10 |
| level-design.md:21 | studio-mcp probes.md | top-down capture, movement values, flat key with shadows off | G3-P7 |
| level-design.md:23 | new templates/level/route-graph.md, route.example.json | level plan template | G3-P6 |
| level-design.md:24 | art/look_check.py keyed modes | warn on subject pixels near the key colour | G3-P1 |
| level-design.md:27 | art/look_check.py keyed modes | warn on a shadow on the key | G3-P1 |
| level-design.md:29 | job-stage.js:591 | "14 checks" to C1-C19, re-rated each round | G3-P4 |
| level-design.md:31 | art/look_check.py compare-subjects | own ring per subject | G3-P8 |
| live-ops-designer.md:17 | templates/live-ops/event-design.md | target experience, fans, niche, variants, event review section | G3-P6 |
| live-ops-designer.md:18 | templates/live-ops/update-plan.md | target experience, atypical option, constraints, success test | G3-P6 |
| live-ops-designer.md:19 | job-types.md | concept round as proof, live-ops review slot | G3-P3 |
| live-ops-designer.md:20 | studio-mcp or studio operator | named event capture set | G3-P7 |
| live-ops-designer.md:21 | liveops/feedback_count.py | codebook, split, anon authors, loud authors, bare-date warning | G3-P1 |
| marketing.md:17 | job-types.md §7 marketing art | warm-up, hooks, animator pose, proof passes, pass order | G3-P2 |
| marketing.md:18 | job-marketing-art.js:290 | stale J016 pointer to image-pipeline.md §1 | G3-P4 |
| marketing.md:19 | job-marketing-art.js D3 | warm-up, hooks, masks, IoU, animator pose | G3-P4 |
| marketing.md:20 | job-marketing-art.js scripts step | hero mask, never whole frame or `--box` for counts | G3-P4 |
| marketing.md:21 | job-marketing-art.js green light | deliverable list | G3-P4 |
| marketing.md:22 | templates/marketing/thumbnail-brief.md | image brief lines | G3-P6 |
| marketing.md:23 | templates/marketing/thumbnail-icon-checklist.md | mask source, IoU, self-review lines | G3-P6 |
| marketing.md:24 | templates/marketing/short-video-plan.md | beat times, flash count, sync fields | G3-P6 |
| marketing.md:25 | art-bible.md | `thumbnail-rough` family | G3-P9 |
| marketing.md:27 | art/thumb_check.py | (b, c, d, j) bug fixes, (a, e-i, k) new modes | G3-P1, G3-P8 |
| marketing.md:28 | art/look_check.py silhouette | `--frame` IoU | G3-P8 |
| marketing.md:29 | new video and audio check | frames, onsets, audio from video (ffmpeg) | G3-P10 |
| marketing.md:30 | new templates/marketing/surfaces.md | tile size per surface | G3-P6 |
| marketing.md:34 | marketing-craft/evals/briefs.md | E1 checks for the new route | G3-P6 |
| marketing.md:35 | new vfx/flash_count.py | marketing cases, red count, first-frame warning | G3-P1 |
| marketing.md:37 | role frontmatter | no change | closed: no change proposed |
| modeler.md:17 | job-character.js P2 | silhouette gate checks | G3-P4 |
| modeler.md:18 | job-character.js S3 | value gate, read plan to the art check-in | G3-P4 |
| modeler.md:19 | job-character.js after P1, job-types.md character | modeler checks the reference set | G3-P2, G3-P4 |
| modeler.md:20 | job-stage.js B2 kit | in-set capture with a player | G3-P4 |
| modeler.md:21 | model/review_renders.py | back game-camera view, phone aspect, background colour | G3-P8 |
| modeler.md:22 | model/review_renders.py | lit grey and flat unlit views | G3-P8 |
| modeler.md:23 | model/model_audit.py | projected part height at the game camera | G3-P8 |
| modeler.md:24 | art/look_check.py | `--mirror` (merged: art-director.md:21) | G3-P8 |
| modeler.md:25 | templates/model/asset-record.md | read plan, iconic qualities, self-review table | G3-P6 |
| modeler.md:26 | art-bible.md | bands with luminance, key light, shape, anchors (merged: art-director.md:17) | G3-P6 |
| modeler.md:27 | knowledge/design/game-profile.md | phone viewport, character height on it | G3-P6 |
| modeler.md:30 | modeling-craft/evals/briefs.md | read plan, silhouette and value gates | G3-P6 |
| modeler.md:31 | art/look_check.py | `--mask` with `--box`, `--top-percent` | G3-P8 |
| modeler.md:32 | studio-mcp probes.md | mask capture probe | G3-P7 |
| modeler.md:33 | model/model_audit.py | `--texel-density` | G3-P8 |
| modeler.md:35 | art/look_check.py | `detail` mode, chroma channel | G3-P8 |
| modeler.md:36 | studio-mcp probes.md | capture field of view and aspect, held item in Play | G3-P7 |
| modeler.md:37 | modeling-craft/evals/briefs.md | in-hand capture, detail and iconic checks | G3-P6 |
| modeler.md:38 | art/look_check.py key-auto, model/review_renders.py | tight key tolerance on flat backgrounds, background colour in the JSON | G3-P1 |
| orchestration.md:17 | templates/jobs/direction-sheet.md, knowledge/jobs/README.md | closed doors as one table in decisions.md, goal question, stop and budget | G3-P6 |
| orchestration.md:18 | templates/jobs/job-card.md | four lines, stop criteria, budget, doors closed | G3-P6 |
| orchestration.md:19 | templates/jobs/decision-digest.md | goal word column | G3-P6 |
| orchestration.md:20 | templates/jobs/intent-brief.md, rules/messages.md §2 | `budget` and `stop` keys | G3-P5 |
| orchestration.md:21 | job-*.js direction stages | research board, warm-up, options, goal question, closed doors | G3-P4 |
| orchestration.md:22 | job-types.md Cross-type rules | closed doors, one marker list, could-not-check list, rejected-request capture | G3-P2 |
| orchestration.md:23 | job-types.md Cross-type rules | consumers state needs before producers build | G3-P2 |
| orchestration.md:24 | new jobs/packet_check.py | gate-packet linter | G3-P10 |
| orchestration.md:25 | hooks/handback_check.py | ignore `coverage:` inside a code block | G3-P1 |
| orchestration.md:26 | knowledge/design/game-profile.md | asset naming and folder rules field | G3-P6 |
| orchestration.md:27 | templates/jobs/ gate packet | skeleton with a `Shown:` line and a could-not-check section | G3-P6 |
| progression-designer.md:17 | job-types.md §4 UI, Review order | progression review of shop, odds and progress screens | G3-P3 |
| progression-designer.md:18 | job-types.md §5 feature | reward tier table in the contract before UI, VFX and sound | G3-P2 |
| progression-designer.md:20 | progression/sim.py | reward-rate summary kept under `--lean` | G3-P8 |
| progression-designer.md:21 | progression/sim.py | label the run-1 timeline, null band when not testable | G3-P1 |
| progression-designer.md:22 | progression/curves.py | `display_round` helper | G3-P8 |
| progression-designer.md:29 | progression/examples/*/design.md | reward tier table in the worked examples | G3-P6 |
| progression-designer.md:31 | role frontmatter | none | closed: no change proposed |
| qa-lead.md:17 | job-types.md §5 feature, Contract | player-facing rows and test hooks at contract time | G3-P3 |
| qa-lead.md:18 | job-types.md §6 effect, Review order | qa-lead protected acceptance for truth effects | G3-P3 |
| qa-lead.md:19 | job-types.md §4 UI, Review order | qa-lead truth rows | G3-P3 |
| qa-lead.md:20 | job-types.md §3 stage, Review order | ledges, collision compare, settings, spawns | G3-P3 |
| qa-lead.md:21 | job-types.md §2 character variant, Review | a sold variant changes no stat or hit box | G3-P3 |
| qa-lead.md:24 | new qa/log_check.py | debug-log checker (merged: feature-builder.md:20) | G3-P10 |
| qa-lead.md:25 | new seq_compare.py | seconded | G3-P10 |
| qa-lead.md:26 | new vfx/flash_count.py | seconded | G3-P1 |
| qa-lead.md:27 | job-types.md §6 effect, Integrator | test hooks at the wiring step (seconded) | G3-P3 |
| qa-lead.md:28 | new testing/evals/ | eval brief with player-facing rows | G3-P6 |
| qa-lead.md:30 | env/scene_audit.py | collision in the probe, `diff` with the blockout (merged: environment-designer.md:29) | G3-P8 |
| reference-images.md:17 | art-bible.md | `view` family and lock | G3-P9 |
| reference-images.md:18 | art-bible.md | `rough` family (endorses marketing.md:25) | G3-P9 |
| reference-images.md:19 | art-bible.md locks | exact background clause | G3-P9 |
| reference-images.md:20 | art/look_check.py silhouette | `--expect-components`, near-threshold parts | G3-P8 |
| reference-images.md:21 | art/look_check.py thumb | `--subject-height` | G3-P8 |
| reference-images.md:22 | art/art_refs.py | inputs from the repo root, warn on a lock conflict | G3-P1 |
| reference-images.md:25 | art/look_check.py value | `--ring-colour` | G3-P8 |
| reference-images.md:26 | art/look_check.py palette --roles | share per role | G3-P8 |
| reference-images.md:27 | job-types.md character, stage, UI, G1 shows | equal finish, hooks, grey and black-fill at real size | G3-P2 |
| reference-images.md:28 | job-character.js, job-stage.js, job-ui-screen.js | two image batches with the pick between them | G3-P4 |
| reference-images.md:29 | owner decision J009-D17 | roughs at medium, finals at high | G3-P9 |
| reviewer.md:17 | job-types.md §5 feature (and §4 UI) | reviewer plan check before the builder for money, saves, remotes | G3-P3 |
| reviewer.md:18 | job-feature.js | reviewer call after the architect plan | G3-P4 |
| reviewer.md:19 | rules/messages.md §6, templates/jobs/review.md | `could_not_check`, `weakest_part`, `protect`, `retest` | G3-P5 |
| reviewer.md:24 | code-review/evals/briefs.md | E-06 to E-14 | G3-P6 |
| reviewer.md:25 | new review/present_scan.py | screening patterns S1-S10 with fixtures | G3-P10 |
| reviewer.md:26 | networking-security SKILL.md N-14 | no success layer on a denied result | G3-P5 |
| sound-designer.md:17 | new audio/cue_check.py | sound measures F-01 to F-13 with fixtures | G3-P1 |
| sound-designer.md:18 | film/shotlist.py log-diff | asymmetric tolerance | G3-P1 |
| sound-designer.md:19 | role frontmatter `tools:` | add six Studio MCP tools | G3-P11 |
| sound-designer.md:20 | role frontmatter `skills:` | preload platform-policy, studio-mcp | G3-P11 |
| sound-designer.md:21 | templates/environment/ambience-map.md | floor-material table, partly met in the hand-off brief (merged: environment-designer.md:25) | G3-P6 |
| sound-designer.md:25 | sound-design/evals/briefs.md | calibration brief, fix checks 3.5, 4.2, 4.3 | G3-P6 |
| sound-designer.md:26 | job-types.md effect, Production order | temp sound on blocking markers, final after the timing lock | G3-P2 |
| sound-designer.md:27 | job-types.md stage | floor-material list at the kit list | G3-P2 |
| sound-designer.md:28 | job-types.md character | sound needs round on the character card | G3-P2 |
| sound-designer.md:29 | job-types.md feature, Direction | sound reads the feedback stack, returns a cue list | G3-P2 |
| sound-designer.md:30 | job-types.md all recipes with sound | two owner listens in the gate packet | G3-P3 |
| ui-ux-designer.md:17 | job-types.md §4 UI, Direction and G1 | designer's information list, flow, wireframes, grey pass at G1 | G3-P2 |
| ui-ux-designer.md:18 | job-types.md §4 UI, Production order | sound and VFX join the motion storyboard | G3-P2 |
| ui-ux-designer.md:19 | job-types.md §4 UI, Review and Proof | capture packet for the UI review | G3-P3 |
| ui-ux-designer.md:20 | job-types.md §4 UI, Return paths | read-order failure returns to the grey pass | G3-P2 |
| ui-ux-designer.md:21 | job-ui-screen.js | direction, proof, build refs (§5-§6), captures | G3-P4 |
| ui-ux-designer.md:22 | art/look_check.py compare-subjects | contrast rank, ring per subject | G3-P8 |
| ui-ux-designer.md:23 | vfx/clip_metrics.py | region, idle background, press-relative onset | G3-P8 |
| ui-ux-designer.md:24 | new seq_compare.py | supports game-designer.md:26 | G3-P10 |
| ui-ux-designer.md:25 | new ui/hit_targets.py | tap-target check from Figma bounds | G3-P10 |
| ui-ux-designer.md:28 | art-bible.md | UI rows (merged: art-director.md:17) | G3-P6 |
| ui-ux-designer.md:33 | platform-policy rules.md §A | is "Odds" a valid label (no text change recommended) | G3-P5 |
| ui-ux-designer.md:34 | studio-mcp SKILL.md | Device Simulator, reduced motion, largest text, press frames | G3-P7 |
| ui-ux-designer.md:37 | ui-design/evals/briefs.md | new stage checks, mood calibration brief | G3-P6 |
| ui-ux-designer.md:38 | role frontmatter | none | closed: no change proposed |
| vfx-designer.md:17 | vfx/clip_metrics.py | (1, 10, 11) docstring, signed-ms warning, numeric order, (2-9) new options | G3-P1, G3-P8 |
| vfx-designer.md:18 | new vfx/flash_count.py | tested counter with 260 fixture folders | G3-P1 |
| vfx-designer.md:21 | new vfx/spec_check.py | spec.json lint | G3-P10 |
| vfx-designer.md:22 | art/look_check.py | mask with box, unaligned IoU, overlap boxes | G3-P8 |
| vfx-designer.md:23 | studio-mcp probes.md (and a vfx recorder) | frame-folder recorder, TimeScale freeze probe | G3-P7 |
| vfx-designer.md:24 | job-effect.js capture() | frame names `f###_<ms>ms.jpg`, folder rules | G3-P4 |
| vfx-designer.md:25 | job-types.md §6 effect, Proof | blocking pass before textures | G3-P2 |
| vfx-designer.md:26 | job-types.md §6 effect, Review order | art director checks grey and black-fill at blocking | G3-P2 |
| vfx-designer.md:27 | job-types.md §6 effect, Integrator | test hooks at the wiring step | G3-P3 |
| vfx-designer.md:28 | vfx-design/evals/briefs.md | calibration brief, fix checks 1.4 and 3.3 | G3-P6 |
| vfx-designer.md:33 | role frontmatter | none | closed: no change proposed |

Rows out of scope (116): they target the Riot library (decided in `library-fixes.md`) or other roles' rebuilt books (decided in each `coverage/<role>.md` "Proposal sweep (J018 close)"). Two withdrawn notes (`film-director.md:39-40`) target role books and are not rows.
