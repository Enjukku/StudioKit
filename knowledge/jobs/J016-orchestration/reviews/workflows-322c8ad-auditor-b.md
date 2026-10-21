---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016 G3 audit
supersedes: []
---
> Author: auditor-b · claude-opus-5-5 · high · 2026-10-21

# Review: the seven saved job workflows at 322c8ad, by auditor-b

Brief J016-A2. Read-only audit. Scripts read before any summary. Harness and unit tests run; no Workflow tool, no Studio, no browser.
Line numbers are for files at 322c8ad (the scripts, tests and harness have no changes in the working tree).
Short paths: `cut` = .agents/workflows/jobs/job-cutscene.js, `chr` = job-character.js, `stg` = job-stage.js, `ui` = job-ui-screen.js, `fea` = job-feature.js, `eff` = job-effect.js, `mkt` = job-marketing-art.js.

```text
<spec>
artifact: .agents/workflows/jobs/*.js@322c8ad, tools/workflows/wf_harness.mjs@322c8ad, tools/tests/test_job_workflows.py@322c8ad
reviewer: auditor-b (general-purpose, J016-A2)
looked_at_first: [the seven scripts in full, wf_harness.mjs, test_job_workflows.py, harness label dumps per stage, a scratch copy of the harness that records concurrent agent() calls (system temp, not in the repo); then job-types.md, company.md, messages.md, handback.schema.json, roles README + role frontmatter + .claude/agents tool lists, capability-check.md C07-C11, decisions.md J016-D5]
tests: "python -m unittest tools.tests.test_job_workflows -v → Ran 4 tests in 2.486s, OK (node v24.19.0)"

findings:
  # ---------------------------------------------------------------- blocking
  - id: F1
    class: blocking
    where: "cut:554-578 (repair), cut:499-513 (reviewChain round 0)"
    expected: "README contract: 'After every repair round the candidate is recaptured and refrozen before the next review round'; the owner's G3 change is a repair round (chr:932-936 REFREEZE, stg:837 freeze, eff:704 capture, ui:620-626 integrate + candidate())."
    observed: "repair() runs R1-scope, then R2 per affected role, then reviewChain('repair') directly. No clip import, no scene-data rebuild, no capture. Harness, stage repair, affected [animator, vfx-designer]: R1-scope, R2-animator, R2-vfx-designer, RV-repair-r0-qa-lead, RV-repair-r0-film-director, ..."
    evidence: "Real run: the round-0 reviewers judge ${FILM}/captures/ recorded before the owner's change; a changed clip in Blender is never imported, so qa-lead plays the old scene. The review chain can report 'clean' on the pre-change candidate and the owner sees an unchanged G3."
    smallest_fix: "After the R2 loop: re-import changed clips (B6-import brief), regenerate scene data (B6-scene), then the B7 capture brief, then reviewChain('repair')."
  - id: F2
    class: blocking
    where: "cut:488-550 (reviewChain), cut:534-549 (FIX, RECAP)"
    expected: "job-types.md:19 cutscene review order starts 'scripts (shotlist.py check, log-diff, gate) →'; company.md §7 scripts first on the frozen candidate; chr:781-783 and stg:753-762 have a scripts step every round."
    observed: "reviewChain starts with qa/perf and film/art/sound. The gate and shotlist.py run only as maker checks in B6 (cut:466, cut:474). After FIX (cut:534-540: one check, 'each finding is fixed with evidence') and RECAP (cut:543-549: capture only) nothing reruns the gate, shotlist.py check or log-diff."
    evidence: "Real run: a feature-builder fix that breaks the gate, or a film fix that breaks the shot list, goes straight to creative review and can reach G3 with a failing gate."
    smallest_fix: "At the top of each round, one scripts reviewer (qa-lead or studio-operator) runs shotlist.py check, shotlist.py log-diff on the candidate's playback log and the gate; FAIL lines are blocking findings for their maker; creative and Studio reviews wait when it blocks (chr:811-817 pattern)."
  - id: F3
    class: blocking
    where: "cut:525-549 (repair rounds), cut:567 (stage repair order)"
    expected: "job-types.md:20 return paths: 'A visual peak moves → beat-list revision → animator, VFX and sound acknowledge and recheck. A skeleton change → animation and VFX attachments stale'; chr:842-911 pipeOrder + receiver rechecks; eff:341-385 dependency order + timing recheck."
    observed: "Makers fix in Object.keys order of the findings (insertion order), one generic brief, owns 'your own output folder for this job' (cut:538). No dependency order, no recheck of VFX and sound when film or animator timing moves, no re-import or shotlist.py luau before RECAP ('Record the repaired candidate again exactly as before', cut:545)."
    evidence: "Real run: sound fixes first, then the animator moves a beat: sound is stale and nothing rechecks it. An animator fix to a clip in Blender is not imported, so RECAP records the old clip and round 1 re-finds the same defect; two rounds are spent and the stage ends needs-decision."
    smallest_fix: "Sort makers film-director → environment-designer → modeler/character-rigger → animator → vfx-designer → sound-designer → ui-ux-designer → feature-builder; if film or animator changed timing, add empty VFX and sound recheck items (eff:363-379); before RECAP, import changed clips and regenerate scene data. Same order in repair() at cut:567."
  - id: F4
    class: blocking
    where: "cut:259-266 (P2, parallel), cut:359-365 (B1, parallel), cut:435-450 (B5, parallel)"
    expected: "job-types.md:15 'vfx-designer ↔ sound-designer co-design each cue's envelope (wind-up, peak, tail) on the event ids'; owner J016 goal 'sound needs the VFX timing'. eff:434-471 shows the working shape: vfx note → sound note that reads it → merge, ≤ 2 rounds."
    observed: "Every VFX/sound step runs inside one parallel() with 'read each other's note if it exists' (cut:261) / 'read the other's note when it exists' (cut:361). B5 builds both in parallel from the B1 notes."
    evidence: "In parallel() both start before either note exists, so each reads nothing; no later step has either one read the other's finished note. The envelope is set by the film-director's lock (cut:367-373), not co-designed. The cooperation the owner asked for does not happen in the pilot."
    smallest_fix: "Between B1 and B1-lock, one envelope exchange: vfx-designer note on the event ids, then sound-designer note that reads it (sequential), then the lock merges both (eff:434-471). Optionally the same in P2."
  - id: F5
    class: blocking
    where: "cut:378-451 (Production)"
    expected: "job-types.md:16 'set and animation in parallel → VFX and sound prototype on the stable event ids early, then finish against the animation → one combined early pass of picture, VFX and sound reviewed before final polish' (Riot K4, capability-check K4)."
    observed: "VFX and sound start only after B3-polish returns (cut:433 waits for animDone; B5 at cut:435). No VFX/sound prototype runs during set and animation; no review of a combined picture + VFX + sound pass before polish. The only trace is a sentence in the B5-sound intent ('make an early combined mix plan', cut:445)."
    evidence: "Real run: the first time picture, effects and sound meet is the integrated candidate; a timing mismatch is found in the review chain and costs a repair round across three crafts instead of a check-in."
    smallest_fix: "Add a VFX and sound prototype lane to the parallel at cut:380 on the locked beat sheet; after B3-blocking, one film-director check-in on the combined rough (blocking playblast + prototype VFX + prototype sound) before B3-polish and B5."
  - id: F6
    class: blocking
    where: "cut:358-359 (B1 planners)"
    expected: "company.md §9 'Parallel agents per stage | as many as independent artifacts, max 5'."
    observed: "planners = [anim, env, vfx, sound, ui, build]: 6 agents in one parallel(). Scratch concurrency harness: cutscene build maxc 6."
    evidence: "Limit breach in the pilot stage; every other workflow stays ≤ 5 (scratch harness max: chr 3, stg 5, ui 4, fea 4, eff 2, mkt 1)."
    smallest_fix: "Move the feature-builder plan (or the UI plan) out of the parallel into a following call, or merge it into the architect's direction-stage notes."
  - id: F7
    class: blocking
    where: "cut:380-432 (B2 set ∥ B3 animation ∥ B4 UI)"
    expected: "company.md §9 'worktrees do not isolate Studio or Blender'; README contract 'the built-in browser serves one agent at a time'; stg:188-190 BLENDER_ONLY / NO_BLENDER / NO_BROWSER rules in every parallel brief."
    observed: "B2-set-rough (environment-designer; environment-craft works in Blender and Studio; role: 'decides what is built in Blender ... in Roblox Studio ... or split') runs beside B3-blocking ('Block the acting for every shot in Blender', cut:408) and B4-ui (ui-ux-designer: default UI image route is ChatGPT in the built-in browser, ui-figma references/image-generation.md:18-22). The env role and the animator stand-in also load reference-images. No production brief carries a Blender or browser rule (grep: the only rules are cut:175 and cut:292)."
    evidence: "Scratch harness pairs: 'animator: B3-blocking || environment-designer: B2-set-rough', 'ui-ux-designer: B4-ui || environment-designer: B2-set-rough'. Real run: two agents drive the one Blender MCP scene (active object and selection are global), or two agents share the ChatGPT browser tabs."
    smallest_fix: "B2 env: 'Studio only; do not use Blender in this step' (or the reverse); B3: Blender only; B4: no image generation in this step, or the only browser user with every other parallel brief saying no browser (stg:188-190)."
  - id: F8
    class: blocking
    where: "cut:426-431 (B4-ui deliver spec.md), cut:469-476 (B6-player)"
    expected: "job-types.md:15 ui-ux-designer (letterbox, subtitles, skip) and feature-builder (player contract, endings); a brief gives the receiver every input it needs (messages.md §2); AGENTS.md §2 'Anything client-callable: also load networking-security'; roles README:24 feature-builder 'high for money, saves, remotes'."
    observed: "B4 delivers content/ui/<seq>-cutscene/spec.md. B6-player inputs are only [${FILM}/, BEATS] (cut:472): no UI spec, no direction.md gameplay state sheet. Skills engineering-craft, testing only; effort medium. owns: 'the source files the architect named for the cutscene player (see the job card)' but no step in build has the architect name them. B6-scene (film-director) gets the UI spec (cut:464) but the film-director never writes game code (role file)."
    evidence: "Real run: letterbox, subtitles and the skip prompt are either not built or built without the spec; a skip in a multiplayer cutscene (gameplay state sheet: audience, skip policy, who decides completion) is a client-callable request built without networking-security, and a saved 'seen' flag without data-saving."
    smallest_fix: "B6-player inputs + content/ui/<seq>-cutscene/spec.md and ${DIR}/direction.md; skills + ui-basics, networking-security (+ data-saving when completion is saved); effort high when it adds a remote; rule 'If the job card names no files, return blocked with the files you need' (chr:756)."
  - id: F9
    class: blocking
    where: "cut:490-498 (review chain roles), chr:774-791 (review chain roles), chr:746-760 (S7-wiring)"
    expected: "AGENTS.md §2 'before any merge: code-review'; platform-policy / data-saving / networking-security 'at design time and again at review'. ui:525-546, fea:585, eff:638-646 run a reviewer on code."
    observed: "Cutscene: B6-player writes code; the chain is qa, perf, film, art, sound; no reviewer. Character with playable: S7-wiring touches remotes and, for a variant, ownership saves (skills data-saving, platform-policy at chr:752); the chain is scripts (qa), art, game-designer, perf; no reviewer, no data-saving or networking-security at review."
    evidence: "Real run: cutscene player code and character wiring (equip remote, saved ownership) reach G3 without a code review; an unvalidated equip remote or a save written before load is not looked for by anyone."
    smallest_fix: "When the stage wrote code (cutscene always; character when playable), add a reviewer beside the creative order: gate first, then the code-review harm order, skills code-review + networking-security (+ data-saving, platform-policy for a variant); code findings get 3 rounds (ui:528)."
  - id: F10
    class: blocking
    where: "cut:478-484 (B7), cut:543-549 (RECAP), cut:497 (sound review); ui:513-521 (B6 capture)"
    expected: "messages.md §9 'a check that cannot be run' is a brief defect; eff:327 states the limit: 'If the Studio MCP cannot record audio, say so: sound sync is then judged from the Output log and labelled so.'"
    observed: "B7 check: 'a synchronized capture with sound exists for the full sequence and for each ending (MCP-verified)'; UI B6 check: 'a clip with sound exists for every transition'. Studio MCP's capture tool is screen_capture, a still image with optional camera (.agents/skills/studio-mcp/references/tools.md:18); no listed tool records video or audio."
    evidence: "Real run: B7 returns not verified / blocked, then `if (!ok(cap)) return failed` (cut:484; ui:521) ends the build stage at its last step after all production spend; or the agent reports a pass without evidence. The sound reviewer (cut:497) is asked to judge 'the mix on phone speaker and headphones' from captures with no audio."
    smallest_fix: "Use eff:327: stills at the named cameras plus the Output log of event, VFX and cue start times on one clock; sync judged from the log and labelled; listening is an owner-confirmed line in the G3 packet."
  - id: F11
    class: blocking
    where: "cut:175 + cut:182; chr:274 + chr:283 + chr:356; stg:357 + stg:366; eff:206 + eff:214 + eff:222; mkt:155-157"
    expected: "reference-images SKILL.md:38: default route 'ChatGPT in the agent's built-in browser, owner J009-D16'; the Codex route (art_refs.py run) is a fallback, 'older model, lower quality'; 'ask the owner once per batch to approve the downloads ... never download without that yes'. A workflow cannot pause for the owner (capability-check C07). Owner J016 goal: quality over token cost."
    observed: "The image step is given to art-director (cut, chr, stg, eff new look), vfx-designer (eff not new look) and marketing (mkt). Their tool allowlists have no browser tool: .claude/agents/art-director.md:6 'tools: Read, Grep, Glob, Write, Edit, Bash, WebFetch, Agent'; vfx-designer, marketing and game-designer the same kind of list (.agents/roles/*.md:7). MCP tools must be named to be allowed (studio-operator.md:7 lists mcp__Roblox_Studio__*). The working-tree note C22 in capability-check.md (not in 322c8ad) confirms an allowlist removes unlisted tools. mkt:156 pins 'generate through tools/art/art_refs.py (manifest, then run)', the fallback route."
    evidence: "Real run: the one agent allowed to make images cannot open ChatGPT; it falls back to Codex (if installed) or returns no pictures. Even with a browser, downloads need an owner yes mid-run. The checks 'every picture listed in options exists on disk' then fail and direction returns failed (cut:185, chr:286, stg:370, eff:225). ui-screen avoids this: ui-ux-designer has no allowlist, and ui:219 keeps ChatGPT page screenshots as G1 pictures when no yes comes."
    smallest_fix: "(a) Owner decision: add mcp__Claude_Browser__* to the art-director, vfx-designer, marketing (and game-designer if it makes images) allowlists, or route image steps to a role without an allowlist; (b) copy ui:219 into every image brief (page screenshots stand in until the owner approves downloads at the gate) and relax the 'exists on disk' check to 'exists on disk or as a page screenshot'; (c) mkt:156 names the browser route as default and Codex as fallback."
  - id: F12
    class: blocking
    where: "cut:328-352 (proof review loop)"
    expected: "company.md §2 'Approval is bound to a revision'; review inputs pinned to the revision under review (messages.md §2)."
    observed: "PR-fix owns ${DIR}/beat-sheet.md (cut:347) and may write a new revision, but returns S_HANDBACK (no revision field); `rev` is never updated in the loop. Round 2 and 3 reviewers get beat-sheet.md@rev${rev} (cut:334) and the stage returns beat_sheet: ...@rev${rev} for the G2 packet (cut:352)."
    evidence: "Real run: when a fix changes the beat sheet, later reviewers check the animatic against the old revision, and the lead shows the owner at G2 a beat-sheet revision that is not the one the animatic matches; the G2 approval binds to the wrong revision."
    smallest_fix: "Give PR-fix the S_CONTRACT schema and set rev = film.beat_sheet_revision after each fix (as P2-merge does at cut:279)."
  - id: F13
    class: blocking
    where: "cut:382-388 (B2-set-rough), cut:406-411 (B3-blocking), cut:426-431 (B4-ui), cut:436-442 (B5-vfx); fea:491-502 (B4-ui), fea:506-517 (B5-vfx)"
    expected: "AGENTS.md §3.5 'Visual work starts from an approved reference image'; messages.md §1 creative briefs add refs 'starting with the approved reference image', with take/avoid notes and an avoid list; owner J016 goal 'reference images first for visual work, style books'. ui:189, ui:362, ui:447, ui:452 show the pattern (STYLE_BOOK skill, the G1 target image, 'No reference image means no styling: ... return blocked')."
    observed: "These briefs have no refs and no avoid: no approved reference image, no art bible, no style book. Both UI briefs load only ui-design, ui-figma (no ui-style-<book>); the ui-ux-designer role does not preload a style book."
    evidence: "Real run: the set, the animation, the cutscene UI and the effects are built from the direction sheet's prose and the agent's own guess at the style; the art check-in and review chain then catch drift that a reference would have prevented (repair rounds on taste)."
    smallest_fix: "Add refs to each: the direction sheet's approved images (path, take, avoid), knowledge/design/art-bible.md (locks, value ladder); for the two UI briefs add the STYLE_BOOK skill (ui:189 text) and the no-reference-no-styling rule."
  - id: F14
    class: blocking
    where: "ui:29, ui:636-641, ui:4 (whenToUse), ui:298 (direction outcome); eff:32 (secondary)"
    expected: "company.md:27 'A job that changes the look is sized L' (L → G1 + G2 + G3)."
    observed: "ui-screen treats 'M with newLook' as a valid job: build runs the proof inside build (ui:639) and the direction outcome tells the lead 'build (M; args.newLook true when the job changes the look)'. job-effect defaults correctly (SIZE L when newLook) but accepts an explicit size M with newLook silently."
    evidence: "Real run: a screen in a new look reaches the owner first at G3, with no G2 on the prototype: the gate the rule requires for a look change is skipped."
    smallest_fix: "ui: return blocked for size M with newLook ('a look change is sized L, rules/company.md §2'); eff: the same check for an explicit M with newLook."
  - id: F15
    class: blocking
    where: "fea:129-134 (moneySkills), fea:154, fea:188 (CODE_SKILLS), fea:585 (reviewer skills)"
    expected: "AGENTS.md §2 'Anything client-callable: also load networking-security'; spec B3 networking-security where the recipe touches remotes. A gameplay feature (combat move, quest, upgrade) is client-callable without money."
    observed: "networking-security is named only when args.money is true (moneySkills returns [] otherwise). Without money: architect, feature-builder and reviewer briefs name engineering-craft/testing/architecture/code-review only. Also moneySkills is appended only when a brief has o.skills (fea:154): D2 exchange, signatures, P2-needs, proof reviews, FIX for non-builders and R2 get no money skills even with money true."
    evidence: "Real run: a combat-move feature's remote is planned, built and reviewed without the networking-security skill loaded (FEATURE_RULES fea:121 restates validation order, but the skill's exploit checklist is never read); a money feature's architect proof review (fea:357-365) reads no platform-policy skill."
    smallest_fix: "Add networking-security for arch, build, review and qa always; append moneySkills even when o.skills is absent (`(o.skills || []).concat(moneySkills(r))`)."
  - id: F16
    class: blocking
    where: "mkt:260-263 (slot sizes missing)"
    expected: "Workflow resume: 'the longest unchanged prefix of agent() calls returns cached results instantly' (workflow-authoring reference)."
    observed: "Outcome: 'then rerun stage direction (the proposals resume from cache)'. The D1 prompts do not change when the owner adds the screenshot to surfaces.md."
    evidence: "Real run: a resumed run returns the cached marketing proposal with the same slot_sizes_missing, so the stage returns the same needs-decision again; the owner's screenshot round is wasted and the lead is told to repeat it."
    smallest_fix: "Say 'rerun stage direction fresh (not resumed)', or check slot sizes in a small first step whose prompt names the surfaces.md revision, so the cache key changes."

  # ---------------------------------------------------------------- recommendations
  - id: R1
    class: recommendation
    where: "cut:221, cut:515; chr:323, chr:813, chr:822-825; ui:284, ui:576; fea:256, fea:601; eff:264, eff:650; stg:408"
    expected: "Real runtime: agent() 'Returns null if the user skips the agent mid-run or the subagent dies'; company.md §8 'Nobody drops work silently'. stg:780 and mkt:317, mkt:354, mkt:371 fail on a null review or signature."
    observed: "A null signature is counted as signed (s && !s.signs); a null review is dropped by filter(Boolean) and the round can return clean."
    evidence: "If perf-engineer dies, the cutscene chain reports 'clean' without a phone check; a dead signer leaves an unsigned direction sheet reported done."
    smallest_fix: "Treat a null signature or review as failed with 'rerun' (stg:780 pattern) in every workflow."
  - id: R2
    class: recommendation
    where: "cut:29, chr:31, stg:31, fea:29, mkt:32"
    expected: "company.md §2: an M build runs the proof inside; ui:43-45 and eff:45-47 validate size."
    observed: "size defaults to L. A build call for an M job without size skips the proof and no G2 happened either."
    evidence: "A forgotten arg silently removes the only proof of an M job."
    smallest_fix: "Require args.size in {M, L} for proof and build (ui:43-45)."
  - id: R3
    class: recommendation
    where: "cut and chr briefs (e.g. cut:247, cut:362, cut:385, cut:504; chr:351, chr:411, chr:572)"
    expected: "messages.md §2 'An input without a revision is a defect in the brief'. stg:133 (PINS rule), ui:187 (pin()), eff:186 (tl()), fea:194 (contractIn() names the G2-approved revision) handle it."
    observed: "cutscene and character pass bare paths (direction.md, beat-sheet.md, reference-set, rig sheet) with no rule on which revision counts."
    evidence: "A build call can read a direction or beat-sheet revision newer than the one the owner approved."
    smallest_fix: "Add stg:133 PINS to BASE_RULES in cut and chr, and name the approved revision ('the revision approved at G1/G2 in decisions.md') as fea:194 does."
  - id: R4
    class: recommendation
    where: "brief() in cut:122, chr:143, stg:143, ui:144, fea:144, eff:143 (mkt:173 does it)"
    expected: "messages.md §1 'put the owner's own sentences in owner_words, unchanged'."
    observed: "Six workflows put the gate words only in <intent>; only mkt emits an owner_words field. CHANGE appears only in intent prose."
    evidence: "messages.md §9 check 'a number, path, revision or ID only in prose' applies to the owner's words; a reviewer of the brief cannot find them in the spec."
    smallest_fix: "Emit owner_words: [GATE, CHANGE] in every brief() (mkt:173)."
  - id: R5
    class: recommendation
    where: "cut:283-294 (P3 greybox), cut:40"
    observed: "The rule 'if you use Studio, only the studio_id the lead names in the job card' sits beside studioRule(false) 'do not write to Studio in this step'; stage proof does not require studioId."
    evidence: "Two rules in one brief that contradict each other; the agent picks one."
    smallest_fix: "Blender only in P3, or require studioId for proof and pass studioWrite when greybox is needed."
  - id: R6
    class: recommendation
    where: "cut:538, cut:573; fea:391, fea:645"
    observed: "Fix and repair briefs own 'your own output folder for this job'. chr ownsOf (chr:202-214), stg FIX_OWNS (stg:64-74), ui own (ui:430, ui:612) and eff ownsOf (eff:190-197) name paths."
    smallest_fix: "An owns map per role, as in chr:202-214."
  - id: R7
    class: recommendation
    where: "cut:33, chr:38, fea:36, eff:39, mkt:37"
    observed: "Stage repair runs with an empty change. stg:45-47 and ui:51-53 refuse it."
    smallest_fix: "Return blocked when stage is repair and args.change is empty."
  - id: R8
    class: recommendation
    where: "stg:283-295 (repairByMaker), stg:547, stg:330"
    observed: "Reviewers send a missing capture to maker studio-operator; its FIX runs with studioWrite false (isEnv false) and NO_BLENDER/NO_BROWSER, so it cannot recapture. The next playtest brief does not carry the finding."
    smallest_fix: "Carry studio-operator findings into the next playtest brief, as fea:192-193 and fea:385 do (captureAsks)."
  - id: R9
    class: recommendation
    where: "chr:715-731; fea:506-532; stg:471-473, stg:663-686; ui:328-335"
    observed: "VFX and sound run in one parallel() with 'read the other's note if it exists' (same race as F4). The recipes for these types do not demand envelope co-design, but shared cues exist (character signature action, feature events)."
    smallest_fix: "Where a cue is shared, use the eff:434-471 sequence."
  - id: R10
    class: recommendation
    where: "cut:492"
    observed: "perf q 'phone frame time and memory during playback' without 'a phone verdict needs a phone, else BLOCKED for that line' (stg:741, chr:789, fea:587 have it)."
    smallest_fix: "Add the phone line."
  - id: R11
    class: recommendation
    where: "cut:166-177 (D1)"
    expected: "AGENTS.md §2 mature or franchise themes → platform-policy at design time and again at review; film-director role: story content with romance, injury, horror, franchise themes → load platform-policy."
    observed: "No cutscene brief names platform-policy, at direction or at review."
    smallest_fix: "A conditional rule in D1 and the film/art review briefs."
  - id: R12
    class: recommendation
    where: "FIX briefs: cut:536, chr:855, stg:288, ui:416, fea:389, fea:400, eff:351, mkt:399"
    observed: "Findings are pasted as JSON into <intent> prose; the review files are also in inputs."
    expected: "messages.md §1 'No number, path, revision or ID appears only in the prose'; §8 'Prefer a path to pasted content'."
    smallest_fix: "Put the finding ids and review-file paths in a spec field (findings: [...]); keep intent prose."
  - id: R13
    class: recommendation
    where: "tools/workflows/wf_harness.mjs:15-48, tools/tests/test_job_workflows.py:41-71"
    observed: "What the fake harness and tests cannot catch: agent() returning null or a non-done status; affected roles in the repair test (always []), blockOnce, refuseSign, conflicts and greybox scenarios (none used by tests); concurrent Studio, Blender or browser use; meta literal purity and phase titles; agentType existing in .claude/agents and model/effort matching role files; brief fields beyond <intent>/<spec>/'checks:' (packet --role/--job, inputs@rev, owns, skills). test_medium_build only checks agent count > L."
    evidence: "F1, F6, F7 and R1 all pass the 4 tests."
    smallest_fix: "Add scenarios nullAgent and statusBlocked; run repair with affected roles; record overlapping agent() calls whose briefs say 'only Studio writer' / Blender / browser (a 6-line change, done in a scratch copy for this audit); assert parallel width ≤ 5; check agentType/model/effort against .agents/roles."

  # ---------------------------------------------------------------- new request
  - id: N1
    class: new request
    where: "studio-mcp skill, references/tools.md:18"
    observed: "No route records synchronized video with audio from Studio; cutscene, UI and effect reviews want it."
    smallest_fix: "Scope review: an owner-run or tool route for a short video + audio capture (named recorder, file path, studio_id), then the capture briefs can require it."

questions:
  - {q: "How do Studio MCP screen_capture images reach disk? Every review brief judges captures 'in <folder>/', but tools.md:18 names no save-to-path option.", default: "the capturing agent saves via a documented route; until confirmed, label captures 'in hand-back only'"}
  - {q: "studio-operator's allowlist (.claude/agents/studio-operator.md tools: Read, Grep, Glob, Bash, mcp__Roblox_Studio__*) has no Write/Edit, but stg:204, stg:760, fea:573, eff:333, eff:612 make it write walk-test.md, review files and capture-log.md. The session's agent list shows Write, Edit for it. Which list is in force?", default: "add Write to its allowlist (owner decision, like C22)"}
  - {q: "Do permission prompts (downloads, Studio MCP writes, browser) reach the owner during a Workflow run, and can a workflow subagent use the built-in browser at all?", default: "probe once before the pilot (C-probe), else treat image making as a pre-stage lead step"}
  - {q: "cut:510, chr:819, stg:774, ui:571, fea:591-593 start agent() calls from raw async functions beside awaited calls; the invocation order depends on completion timing. Is the resume cache keyed by call order?", default: "never resume a stage run; rerun it (C10 already says so for 2.1.296)"}
  - {q: "No brief carries `peers`: agent() returns no agent id, and C22 (working tree) says 14 of 24 roles cannot SendMessage. Should BASE_RULES say 'inside a workflow, sideways work goes through exchange files only'?", default: "yes, one line in BASE_RULES"}

keep:
  - "One stage per call; bad args return blocked before any agent (test passes for all 7); studioId gates per stage; mkt never uses Studio."
  - "Identical HANDBACK_PROPS, TAIL_PROPS, FINDING and schema() in all 7 (diff of the shared block shows only additions); evidence fields before status; additionalProperties false; every property required."
  - "Identical BASE_RULES in all 7: job card first, packet with --role and --job, docs-map rows before design or build, built_on, owns, hidden- files, no report* names, labelled checks."
  - "One Studio writer: the scratch concurrency harness found 0 overlapping Studio-writer briefs in 7 workflows × proof/build/repair, with and without repair rounds. Tech reviews run one after another in Studio beside capture-only creative reviews."
  - "Bounded loops everywhere: interface ≤ 2, repair ≤ 2, code review 3 (ui:528, fea:609), K-checks ≤ 2 note rounds (chr:233-242), feature chain ≤ 6 rounds."
  - "Unroutable maker or affected role → needs-decision (harness: all 7 return needs-decision for an unknown role)."
  - "Independent D1 proposals with an explicit avoid list of other leads' proposals; one exchange; synthesis by the recipe's job lead; signatures; one resolution round."
  - "opts.phase on every agent() call (no phase() race); meta is a pure literal in all 7 and every phase name matches meta.phases."
  - "ROLE tables match the role files and roles README (model and effort); the animator stand-in is general-purpose, Opus high, with rig-pipeline (orchestration SKILL.md:34); packet uses the shared character-rigger/animator docs-map row because context_packet rejects an unknown role (exit 2)."
  - "Cutscene: needs-decision → job-character when a new cast needs a rig (cut:375); film check-in on blocking and art check-in on the rough set (cut:389-417); RECAP after each review repair round (cut:543-549)."
  - "Stage: blueprint approved before any building (stg:431, stg:507-509, stg:522); BLENDER_ONLY/NO_BLENDER/NO_BROWSER (stg:188-190); returnPaths (stg:217-270); PINS (stg:133); freeze + recorded playtest after every repair."
  - "Effect: sequential envelope co-design (eff:434-471); honest audio limit (eff:327); dependency-ordered applyFixes with timing recheck (eff:341-385)."
  - "Character: K1/K2/S4/S6 receiver checks with one exact note; pipeOrder repairs with receiver rechecks and REFREEZE (chr:842-911); LIMITS with doc sources (chr:186-192); variant mode."
  - "UI: layer routing of findings (ui:199); SHOP_RULE; download fallback (ui:219); feature-builder last as the only Studio writer in repairs (ui:433-437)."
  - "Feature: gate PASS required before any review (fea:556, fea:410, fea:661); captureAsks (fea:192-193); contractIn() names the G2-approved revision (fea:194); MONEY_RULES."
  - "Marketing: no Studio, owner actions only, image steps never parallel, big shapes frozen after green light."
verdict: fix-first
</spec>
```

## Coverage per workflow (B1-B8)

Mark: ok = checked, no blocking problem; F/R = checked, finding id; n/a = does not apply.

| Check | cutscene | character | stage | ui-screen | feature | effect | marketing-art |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 step order vs recipe (harness labels, all 4 stages) | F2 F3 F4 F5 | ok | ok | ok | ok | ok | ok |
| B2 sizes S/M/L | R2 | R2 | R2 | F14 | R2 | F14 (secondary) | R2 |
| B3 brief completeness | F8 F11 F12 F13 R3 R4 R6 R11 | F11 R3 R4 | F11 R4 | R4 | F13 F15 R4 R6 | F11 R4 | F11 |
| B4 agentType, model, effort | ok (F8: builder effort for a remote) | ok | ok | ok | ok | ok | ok |
| B5 safety (Studio, Blender, browser, determinism, file I/O, bounded loops, routing, recapture) | F1 F6 F7 F10 R5 | ok (F9 review) | R8 | F10 | ok | ok | ok |
| B6 real runtime (meta, args, options, parallel, schema, return, phases, top-level return, null) | R1 | R1 | ok | R1 | R1 | R1 | F16 |
| B7 unit tests | run once for all: Ran 4 tests, OK | | | | | | |
| B8 consistency (contract, fields, failure handling) | drift: no scripts step, no recapture in repair, no reviewer, no PINS, no change check | drift: no reviewer, no PINS | reference shape | ok | drift: money-only networking-security | reference shape | drift: Codex image route |

Plain statement: job-stage.js has no blocking problem of its own; its one blocking item is the shared image-route problem F11. job-character.js, job-ui-screen.js, job-feature.js, job-effect.js and job-marketing-art.js each have one or two blocking items. job-cutscene.js, the pilot workflow, has 13 of the 16 blocking items.
