---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016 G3 audit recheck (J016-A2, selective, rules/company.md §7)
supersedes: []
---
> Author: auditor-b · claude-opus-5-5 · high · 2026-10-21

# Recheck: the seven job workflows at 763a11e, by auditor-b

Selective recheck of `workflows-322c8ad-auditor-b.md`: blocking findings F1-F16, the keep list, and new defects the fixes introduced. I read the scripts before the commit message. Line numbers are at 763a11e (working tree clean at the start). During the recheck another chat changed one lesson-cause enum string in all seven scripts and the schema ('found by' → 'defect found by'). That change is uncommitted, moves no line and touches no finding; every cited line was compared with `git show 763a11e:<file>`. Short paths: `cut` = .agents/workflows/jobs/job-cutscene.js, `chr` = job-character.js, `stg` = job-stage.js, `ui` = job-ui-screen.js, `fea` = job-feature.js, `eff` = job-effect.js, `mkt` = job-marketing-art.js. Harness runs used the required args from the README table (size, studioId, images, change, plus the type flags).

```text
<spec>
artifact: .agents/workflows/jobs/*.js@763a11e, .agents/workflows/jobs/README.md@763a11e, tools/workflows/wf_harness.mjs@763a11e, templates/jobs/handback.schema.json@763a11e
reviewer: auditor-b
looked_at_first: [job-cutscene.js in full; the fix sites in the other six; the harness; the schema; harness runs (labels, timeline, dumps) and a sweep of 7 workflows × 4 stages × 5 scenarios ({}, blockAlways, images pending, affected+timing+conflicts+greybox+refuseSign, nullLabel) with 0 harness violations; then README, company.md §5-7, orchestration SKILL.md:16]
tests: "python -m unittest tools.tests.test_job_workflows -v → Ran 32 tests in 7.632s, OK"

recheck:
  - {id: F1, state: closed, evidence: "cut:819-840 repair → applyRound cut:771-816 (import cut:804-807, assemble cut:808-811, recapture cut:812-814) → reviewChain. Harness repair, affected [animator, sound-designer], timing: R1-scope, FIX-repair-animator, FIX-repair-vfx-designer, FIX-repair-sound-designer, IMP-repair-fix, SCN-repair-fix, CAP-repair-fix, RV-repair-r0-scripts, ..."}
  - {id: F2, state: closed, evidence: "cut:700-706: a qa-lead scripts step (shotlist.py check, log-diff on output.log, gate) opens every round; a blocking FAIL holds the other reviews. Labels: RV-candidate-r0-scripts and RV-candidate-r1-scripts lead their rounds."}
  - {id: F3, state: closed, evidence: "cut:756-816: makers in MAKERS order (film → env → modeler → rigger → animator → vfx → sound → ui → feature-builder); a moved time adds VFX and sound rechecks (cut:777-778); a UI change adds the player recheck (cut:779); then re-import, scene data, recapture. Owns per role in FIX_OWNS cut:759-768."}
  - {id: F4, state: closed, evidence: "VFX then sound, sound reading the VFX note, at P2 cut:341-345, P4 cut:385-401, B1 cut:532-536, B5 prototype cut:606-623 and finals cut:643-660. M-build timeline: P2-needs-r1-vfx 6-10 → sound 11-12; B1-envelope-vfx 29-32 → sound 33-35; B5-vfx-proto 44-49 → sound-proto 50-51; B5-vfx 59-60 → B5-sound 61-62."}
  - {id: F5, state: closed, evidence: "cut:597-641: the VFX and sound prototype runs beside B3-blocking (timeline 43-51), then B3-combined-checkin (52-56) before B3-polish (57-58) and the finals."}
  - {id: F6, state: closed, evidence: "cut:521-537: 5 lanes (two of them sequential pairs). Harness maxConcurrent 5 on cutscene build; the harness now fails any run above 5 (wf_harness.mjs:142)."}
  - {id: F7, state: closed, evidence: "Every cutscene brief carries a Blender rule and an image rule (cut:196: BLENDER_ONLY or NO_BLENDER; imageRule or NO_IMAGES). Production: env in Studio with NO_BLENDER, animator BLENDER_ONLY, UI NO_IMAGES. The harness checks exclusive Studio/Blender/browser holds (wf_harness.mjs:108-138): 0 violations in the sweep."}
  - {id: F8, state: closed, evidence: "cut:477-495 wirePlayer: inputs player contract, direction.md (state sheet), UISPEC; skills ui-basics, networking-security (+ data-saving via saves()); effort from the architect's adds_remote/saves_data (cut:79-83, cut:543); owns from the contract's Code file owners table, blocked when empty (cut:488)."}
  - {id: F9, state: closed, evidence: "cut:716-719 reviewer every round (effort high when risky); chr:880-885 reviewer when playable. Harness character build playable=true: RV-candidate-r0-reviewer present; playable=false: absent."}
  - {id: F10, state: closed, evidence: "CAPTURE_LIMIT cut:153 and ui:148; capture checks need stills + output.log (cut:506, ui:570-572); the sound review judges sync from output.log, and listening is an owner-confirmed line (cut:724)."}
  - {id: F11, state: open (partly), evidence: "Closed in cut, eff and mkt: image steps write prompts, return images.state pending, and the checks accept pending (cut:251, cut:277; eff:257, eff:284; mkt:329; mkt:185-188 stops the stage on a pending green light or render). Still open in the synthesis steps of three workflows. Their D1 image steps may return pending: chr:345, stg:407, ui:276. For chr and stg it is always pending: the art-director's allowlist is unchanged (.claude/agents/art-director.md:6, no mcp__Claude_Browser__*). For ui it is pending whenever imagesApproved is false, the default at direction. But the synthesis checks still say '2-3 directions, each with pictures that exist on disk and its anchors marked' (chr:371), '2-3 looks, each with pictures that exist on disk' (stg:434) and '2-3 style targets, each with pictures that exist on disk' (ui:301). Real run: the job lead cannot pass that check, so it returns not done and the direction stage fails at chr:373, stg:437 and ui:303. Or it returns done with a failing check. The harness passes because fakes ignore checks. Smallest fix: use the cut:277 wording ('pictures on disk or rows in a pending prompts file') in all three."}
  - {id: F12, state: closed, evidence: "cut:443-452: PR-fix returns S_CONTRACT and beatsRev follows it; the reviewers and the G2 result use beats() (cut:430, cut:439). test_cutscene_proof_fix_pins_the_new_beat_sheet passes."}
  - {id: F13, state: closed, evidence: "visual briefs get args.images + art bible refs and NO_REF_RULE (cut:183, cut:197; fea:186-187); the UI briefs load the style book (cut:592, fea:596). Build stages refuse to start without images (cut:50; fea:541-543 when UI or VFX is in scope)."}
  - {id: F14, state: closed, evidence: "ui:51-52 and eff:56-58 refuse size M with newLook ('a look change is sized L'); newLook is a required boolean. test_a_look_change_is_never_sized_m passes."}
  - {id: F15, state: closed, evidence: "fea:151-157 areaSkills: networking-security for architect, builder, reviewer and qa with or without money; fea:182-183 appends area skills even when o.skills is absent."}
  - {id: F16, state: closed, evidence: "mkt:297 'rerun stage direction fresh (a new run, not resumed: a resumed run returns the cached proposal and the same gap)'; README 'Running one' says the same rule in general."}

keep_check:
  - {item: "one stage per call; bad args blocked before any agent; studioId gates; mkt never uses Studio", state: holds, evidence: "all 7 return blocked with 0 agents and a required list for a build call without size (harness); mkt:168 no Studio"}
  - {item: "identical shared schema, evidence before status, additionalProperties false", state: holds and is stronger, evidence: "the harness compares every agent() schema with templates/jobs/handback.schema.json (wf_harness.mjs:54-69); the template adds docs_read and an optional lesson (valid: required ⊆ properties)"}
  - {item: "identical BASE_RULES", state: holds with two known variants, evidence: "cut/chr/eff/fea/mkt identical (same md5); stg keeps the revision clause in its own PINS rule; ui appends SHOP_RULE"}
  - {item: "one Studio writer; tech reviews in Studio one after another beside capture-only creative reviews", state: holds, evidence: "sweep: 0 exclusive-resource violations; cut:708-731"}
  - {item: "bounded loops", state: holds, evidence: "blockAlways ends needs-decision in every proof, build and repair; cut reviewChain ≤ 6 rounds, code 3 / other 2 (cut:742)"}
  - {item: "unroutable maker or role → needs-decision", state: holds, evidence: "repair with affected [lighting-artist]: needs-decision, 1 agent, in all 7"}
  - {item: "independent D1 proposals; one exchange; synthesis; signatures; one resolution round", state: holds, evidence: "cut:241-302 and the same shape in all 7; a null signature now fails (cut:291)"}
  - {item: "opts.phase on every call; pure meta literals; phase titles in meta", state: holds, evidence: "no template literal, concatenation or spread in any meta block; the harness fails a phase not in meta.phases (wf_harness.mjs:132)"}
  - {item: "ROLE tables match role files; animator stand-in general-purpose Opus high", state: holds, evidence: "the harness checks role file and tier model (wf_harness.mjs:128-131); cut:74. Effort is not checked by the harness; I read it: matches the roles README, raised to high where the architect's contract says remotes or saves (cut:80-83)"}
  - {item: "stage blueprint approval before building; Blender/browser rules; returnPaths; PINS", state: holds, evidence: "stg:472-473, stg:576"}
  - {item: "effect sequential envelope, honest audio limit, dependency-ordered fixes", state: holds, evidence: "eff:476, eff:364, eff:380"}
  - {item: "character K-checks, pipeOrder, REFREEZE, LIMITS, variant mode", state: holds, evidence: "chr:289-292, chr:1010-1011"}
  - {item: "UI layer routing, SHOP_RULE, download fallback", state: holds (fallback replaced by the LD2 pending path), evidence: "ui:230, ui:130, ui:151"}
  - {item: "feature gate PASS before review, captureAsks, contractIn", state: holds, evidence: "fea:509, fea:660, fea:772, fea:234, fea:481"}
  - {item: "marketing: no Studio, owner actions, one image maker at a time, frozen big shapes", state: holds, evidence: "mkt:168, mkt:264, mkt:177-183, mkt:437"}
  - {item: "cutscene RECAP after each review repair round", state: holds and extended to the repair stage, evidence: "cut:812-814"}

new_issues:
  - id: N1
    class: blocking
    where: "ui:497-500 (B1 Figma build), ui:560-577 (capture and review chain)"
    expected: "rules/company.md §7: reviews go up on one frozen candidate, before the owner; §2: approval is bound to a revision. README: 'Visual work never starts without an approved image path in its brief'."
    observed: "Rule at ui:500: 'Icons and item art pending as prompts stay placeholder frames marked PENDING in Figma and the handoff; the lead runs the batch before G3.' The stage goes on to the feature-builder implementation, code review, capture and the review chain with the placeholders, and returns done with images_pending (harness: ui-screen build {images: pending} → done, pend 1). No step brings the batch's icons into Figma and Roblox after the lead's batch, and no step reviews them."
    evidence: "Real run: either G3 shows a screen with PENDING frames, or the lead's batch adds icons after the review chain, and the owner sees a revision no reviewer judged. The owner's goal ('work goes back up through reviews before it reaches me') breaks."
    smallest_fix: "Stop the build stage when B1 returns images pending, as mkt:185-188 does (blocked; the lead runs the batch; rerun with the paths in args.images). Or add one integrate-and-recapture round after the batch before the review chain."
  - id: N2
    class: recommendation
    where: "mkt:342-349 (D3 signatures), cut:282-289, stg sign step"
    observed: "When the roughs or look images are pending, the art-director is told to 'Look at the roughs at their real slot size and in their real layout first (the contact sheets and mocks)' (mkt:345). For marketing and the art-director these never exist at that point, because their allowlists have no browser. The signer either signs prompts it cannot see or names an incompatibility, which forces the resolution round."
    smallest_fix: "When images are pending, the signer judges the prompt rows and the lead's batch result is checked by the art-director before the G1 packet (a short check step, or a fresh rerun of the signatures with args.images)."
  - id: N3
    class: recommendation
    where: "cut:408-415 (P5 boards pending), chr:418-420 (reference set pending)"
    observed: "The boards (cut) and the multi-view reference set (chr) may be pending through the proof reviews; the lead's batch makes them after the reviewers judged the proof, and they reach G2 unreviewed."
    smallest_fix: "Name in the G2 outcome that the batch images are shown as 'not reviewed'; or have the art-director check them after the batch."

questions_still_open:
  - {q: "studio-operator's allowlist is unchanged (.claude/agents/studio-operator.md:6, no Write/Edit). It still writes review files and logs in stage, feature and effect (e.g. the scripts reviews, capture-log.md). Is Bash writing the intended route?", default: "add Write (owner decision)"}
  - {q: "How do screen_capture stills reach disk? Every capture brief now names stills in a folder.", default: "probe once before the pilot"}

verdict: fix-first (F11 in chr:371, stg:434, ui:301; N1 in ui:500). job-cutscene.js has no open blocking finding and no new blocking defect.
</spec>
```

## Coverage

| Item | State | Where |
| --- | --- | --- |
| F1 | closed | cut:771-840 |
| F2 | closed | cut:700-706 |
| F3 | closed | cut:756-816 |
| F4 | closed | cut:341-345, 385-401, 532-536, 606-623, 643-660 |
| F5 | closed | cut:597-641 |
| F6 | closed | cut:521-537; harness max 5 |
| F7 | closed | cut:148-150, 196 |
| F8 | closed | cut:477-495 |
| F9 | closed | cut:716-719; chr:880-885 |
| F10 | closed | cut:153, ui:148 |
| F11 | open in chr, stg, ui | chr:371, stg:434, ui:301 |
| F12 | closed | cut:443-452 |
| F13 | closed | cut:183-197; fea:186, 596, 612 |
| F14 | closed | ui:51-52; eff:56-58 |
| F15 | closed | fea:151-157, 182-183 |
| F16 | closed | mkt:297 |
| keep list | all 16 items hold | see keep_check |
| new issues | 1 blocking (N1), 2 recommendations (N2, N3) | ui:500; mkt:345; cut:408, chr:418 |
| unit tests | Ran 32 tests, OK | tools/tests/test_job_workflows.py |
