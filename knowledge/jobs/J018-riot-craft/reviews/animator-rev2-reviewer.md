---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer animator · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: animator books, round 2

Scope: `.agents/roles/animator.md` (body), `.agents/skills/animation-design/` (SKILL.md, references/), `.agents/skills/animation-craft/` (SKILL.md, references/; evals not changed), as in the working tree on 2026-10-22 after repair round 1, against git `df13ff4`. Inputs: `knowledge/reference/craft/riot/` (README, `universal-principles.md` = master, topic files, `matrix.md`), `coverage/animator.md`, `proposals/animator.md`, `job-card.md`, `reviews/animator-rev1-reviewer.md`. Line numbers are working-tree lines.

## Round 1 findings: status

| Round 1 id | Status | Evidence |
| --- | --- | --- |
| F1 (SD-04 verb, SD-22 end-of-state tell) | fixed | `game-timing.md:174-175`; check `review.md:104` B-16; steps at SKILL.md:37, :40; role file :38, :53 |
| F2 (look-turn rule lost; head-lag sign too broad) | fixed | `principles.md:92` split into look-turn and spin; `body-and-species.md:19`, `:45`; `review.md:123` S-15; coverage section c row added |
| F3 (image budget of the plan stages) | fixed | `review.md:73` plan-stage budget; SKILL.md:38 one contact sheet per key clip; §9 #6 check number-first (SKILL.md:126); `principles.md:108` P-08.11; `game-timing.md:50` bracket moved to its owners |
| F4 (fresh viewer with no method) | fixed | `review.md:84` defines the fresh read and the mirrored look; `principles.md:5`; SKILL.md:136 |
| F5 (timing picks from stills) | fixed, one residual gap (R2 below) | `review.md:10`; `blender-keying.md:75` playable preview (`ImageFormatSettings.media_type` 'VIDEO' exists in the bundled Blender API docs); `game-timing.md:50` |
| F6 (SKILL.md size, compaction) | partly fixed (R3 below) | 30,481 → 25,779 characters; §8 now starts at character 18,013 and ends at 19,152 |
| F7 (check-in with no named reviewer) | fixed | `animation-craft/SKILL.md:28`, `:91`; role file :41 |
| F8 (sync window vs sound-design) | fixed | `game-timing.md:178`; `review.md:138` G-04; proposal row kept |
| F9 (tables and headers) | fixed; (d) has one inaccuracy (R4 below) | CD-21 row now in the rejected column; SKILL §4 heading; `roblox-playback.md:62`; citation policy written in coverage section c; files now LF |

```text
<spec>
artifact: .agents/roles/animator.md (body) + .agents/skills/animation-design/** + .agents/skills/animation-craft/** (not evals) @ working tree 2026-10-22 after repair round 1, base df13ff4
reviewer: J018 reviewer animator (opus, high)
looked_at_first: [the 13 book files read in full before the coverage table; git show df13ff4 of the two SKILL.md files and the word diff of animation-craft/SKILL.md; git diff --stat df13ff4 and git status; section-heading diff old vs new for all 13 files; universal-principles.md (index, motion line of every UP, UP-16 in full); matrix.md animator column (139 ids, script-compared with the coverage table); the principle/apply/check/mistake lines of all 155 tagged and untagged findings the coverage table lists; tools/anim/clip_check.py --help and check names in source; tools/art/look_check.py thumb and silhouette --help; tools/model/review_renders.py exists; bundled Blender API docs (ImageFormatSettings.media_type); animation-craft/evals/briefs.md (common checks, briefs 1 and 2); proposals/animator.md; job-card.md fixed list]
findings:
  - id: F1
    class: blocking
    where: "coverage/animator.md:33 (CD-25); animation-design/references/principles.md:53 (P-04.4); references/worked-examples.md §1"
    expected: "C1: CD-25's rule for the animator lands as a rule with its check: a promo, splash or cutscene still of a character starts from a one-sentence premise and reuses the signature ability's key pose from the game's animation set; check: the still's pose matches a frame of the clip."
    observed: "P-04.4 only says that a held pose ('hit pause, promo still') carries a few flow lines: that is RH-05's content. Worked example §1 is an emote, not a promo pose. 'Premise' appears nowhere in the books, and nothing says that a promo pose reuses the in-game key pose. An animator asked for a marketing or cutscene pose would make a new pose with no link to the game."
    evidence: "grep -i 'promo|premise|marketing|showcase' over the 13 book files: only principles.md:44, :53, :80 and review.md:98, none of which carries the rule. Library character-design.md CD-25 apply: 'character poses reuse the ability's key pose from the game's animation set'; check: 'compare with a frame from the clip'."
    smallest_fix: "Append to principles.md P-04.4 (or a new P-05.11 row): 'A promo, splash or cutscene still of a character reuses the signature ability's key pose from the set, with its line of action and hook shapes, staged for the brief's one-sentence premise; it is not a new generic pose.' Sign: 'the still's black-fill overlaps the clip's key frame (look_check.py silhouette --compare), or the difference is recorded.' Point coverage row CD-25 to it. Alternatively, move CD-25 to the rejected column with a reason (promo posing belongs to film-director and marketing) and say there what the animator supplies."
  - id: R1
    class: recommendation
    where: "animation-design/references/worked-examples.md:10 (beat 2), :12 (Drivers), :16 (Secondary)"
    expected: "The worked example models the repaired P-07.5 rule: in a look-turn the eyes lead, then the head, then the body; the head holds its world direction only in a spin or fast body turn."
    observed: "Beat 2 is a glance at the camera (a look-turn), and the picked option is the hop; the spin option lost. But Drivers says 'the head holds its world direction through the turn, then turns late and fast to the camera', which is the spin rule applied to a look-turn. This is stage-2 text from before the F2 repair. An agent copies worked examples, so it learns the wrong rule."
    evidence: "principles.md:92 and body-and-species.md:19 (the repaired rule) vs worked-examples.md:12; worked-examples.md:12 'The hop wins ... the spin hid both arms'."
    smallest_fix: "Drivers: 'in the glance the eyes reach the camera first, then the head, then the chest; if the hop turns the body, the head holds its world direction and turns late and fast'. Secondary: 'a blink on the fast head turn'."
  - id: R2
    class: recommendation
    where: "animation-design/references/review.md:10 (item 5); SKILL.md:38 (step 6), :42 (step 10); review.md:100 (B-12); principles.md:103 (P-08.6); roles/animator.md:37"
    expected: "A timing pick that is sent away has someone who can make it. The check-in reviewers the books name (film-director, proof reviewer, VFX, sound) are agents, and like the animator they see stills only. The owner sees work only at the gates."
    observed: "The books say that the 'reviewer or owner picks on a playable preview'. An agent reviewer cannot watch the video. So during a job the pick still rests on stills or waits for a gate, and the books do not say which take is used until then."
    evidence: "roblox-playback.md:62 'These are stills'; blender-keying.md:75 'It is for them to watch at normal speed'; craft SKILL.md:28 names agent reviewers."
    smallest_fix: "One sentence in review.md §1 item 5: 'An agent reviewer judges takes by the same beat-gap numbers and strips. Until the owner watches the previews at the next gate, the take with the better recorded reasons is used and marked PROPOSAL, and both previews go into the gate packet.'"
  - id: R3
    class: recommendation
    where: "animation-design/SKILL.md §8 (:105-112), §9 (:116-140)"
    expected: "rules/assistants/claude.md (Compaction): after compaction each skill keeps its first 5,000 tokens; steps and rules sit at the top."
    observed: "Better than round 1, but the end of §8 starts at character 18,013 and ends at 19,152. That is 4,800 to 5,200 tokens, depending on the characters-per-token rate for this table-heavy text, so its last lines may be cut. §9 (Core principles, about 6,600 characters) is always past the limit, so after compaction the agent loses its core principles until it re-reads the skill."
    evidence: "Character offsets of the § headings computed from the working-tree file (CR removed)."
    smallest_fix: "Optional. Cut about 1,000 characters from §5 and §6 (their full forms are in worked-examples.md and the craft skill). Or add one line under §1: 'After compaction, re-read §8 and §9 of this file before handing on a plan.'"
  - id: R4
    class: recommendation
    where: "animation-craft/references/roblox-playback.md:62"
    expected: "Tool claims match the tool. With `--box`, look_check makes 'subject = union of these boxes' (mask_source 'box')."
    observed: "The book says that `thumb --size <WxH> --box ...` around the subject 'also re-measures its value and silhouette'. With a box the subject is the rectangle, so the silhouette numbers describe the box, not the character. Only the value ring against the surroundings is meaningful."
    evidence: "python tools/art/look_check.py thumb --help (--box text)."
    smallest_fix: "Change the words to 'to also re-measure its value against the surroundings', or use a `--mask` drawn from the effects-hidden capture when a silhouette is needed."
  - id: R5
    class: recommendation
    where: "roles/animator.md:67 (feature-builder row); animation-design/references/review.md:145 (G-11), :148 (G-14)"
    expected: "Every in-game self-review line names who supplies the test-place hooks it needs, as G-05 does with 'a test hook that rejects a hit'."
    observed: "G-11 needs a clip that is triggered 100 times at one per second, with the playing-track count in the Output log. G-14 needs to see the gameplay hit area in the capture. The animator does not write game code, and the feature-builder row asks only for the reject hook. Without these hooks, G-11 and G-14 end as 'not verified' in most runs."
    evidence: "Role file write scope :75 (no game source code); review.md:145, :148; library VR-20 check (debug shape overlay of the server area) and VR-24 check (100 triggers)."
    smallest_fix: "Feature-builder row, 'Ask for': add 'a rate trigger for frequent clips that logs the playing-track count, and a debug overlay of the hit area in the test place'."
  - id: R6
    class: recommendation
    where: "proposals/animator.md:28 (evals row); animation-craft/evals/briefs.md:14 (A6)"
    expected: "The eval proposal lets a grader score the new plan stages without failing the light-check rule."
    observed: "Common check A6 allows 'images only for failing numbers plus ≤ 8 key frames'. A grader who follows A6 will count the contact sheets and playable previews against that cap. The proposal row adds new checks but does not change A6."
    evidence: "review.md:73 (plan-stage images have their own budget) vs briefs.md:14."
    smallest_fix: "Add to the evals proposal row: 'A6: count plan-stage images (one contact sheet per key clip, previews) separately, as review.md §5 says.'"
  - id: R7
    class: recommendation
    where: "coverage/animator.md:93 (RI-15)"
    expected: "Each rejection has a sound reason."
    observed: "The reason says that RI-15 is 'a study method for UI and style'. The library's apply line names 'a new UI or motion style'. The substance is already carried: body-and-species.md:56 takes mechanics and timing from reference and never copies a clip. So the row is covered, not out of scope."
    evidence: "references-ideation.md RI-15 apply; body-and-species.md:56."
    smallest_fix: "Change the row to a landing ('body-and-species §6: take timing and mechanics from reference clips, never copy; covers the structural study') or reword the reason."
keep:
  - "All round 1 keeps still hold: anticipation sized by who reacts, the plan stages in order (who reacts, anchors and hook shapes, beat sheet with subtext, one black-fill contact sheet per key clip, recorded pick), blocking then check-in, the per-pass self-review lines with N/K/C inputs, the blender-keying §8 compute table, attempt vs outcome, paid reveals with one windup, every-player rules, C-22..C-27, variants keep the base, §9 with all 20 UP rows."
  - "The repairs are real fixes, not just added words: the verb and end-of-state tell now reach the step (§3.5, §3.8), the check (B-16), the plan self-check (§8), the role file and the hand-back line; the look-turn vs spin split is applied the same way in principles, body-and-species, S-15 and the compute row."
  - "review.md §5 'plan-stage images are making, not checks' with one contact sheet per key clip: it keeps the owner's light-check rule and keeps the thumbnail stage."
  - "The fresh-read definition (review.md §8 intro): write the read before you open the brief, then compare; the reviewer repeats it blind. Any agent can run it."
  - "The playable-preview recipe and the honest 'you see stills' line: timing is judged from beat gaps and frame strips, not from a guess."
  - "The hit-stop bracket moved to its owners (gameplay owner with VFX); the animator supplies freeze-frame takes. This keeps the decision rights of game-timing §1."
  - "The F6 cut kept every old rule: I compared the old SKILL.md steps, P-rows, §5-§8 with the new books and found nothing lost. The tween-cost line is now in craft SKILL §6, and the underside study is in body-and-species §1."
verdict: fix-first
</spec>
```

## Checks C1-C7

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | FAIL (1 row) | All 139 matrix ids for animator have a row (script compare: 0 missing). I checked the 175 rows (139 tagged, 16 untagged, 20 UP) against the library's principle, apply and check lines and the book text. 1 failed: CD-25 is a keyword only (F1). The SD-04 and SD-22 failures from round 1 are now carried. Rejections CF-18 and CF-19 are sound. RI-15 is really covered, so its reason should change (R7). CD-21 is now a partial landing with its reason in the right column. |
| C2 core principles | PASS | `animation-design/SKILL.md` §9 is in the skill the agent loads first. UP-01..UP-20 are each stated for animation with an example and a check. Each row agrees with the master's motion line. UP-16 now has the fresh read and the mirror; UP-10 has the verb. No contradiction, and nothing important is missing. |
| C3 self-review | PASS with gaps | The lines run on clip_check numbers, the compute table, the ≤ 8 key frames with look_check, Studio captures and the Output log. The round 1 gaps (fresh viewer, timing from stills) are closed. Remaining gaps: G-11 and G-14 need test-place hooks that nobody is asked for (R5), and timing picks have no agent who can watch the preview (R2). |
| C4 kit rules and engine | PASS | The light-check budget is now explicit. The sync window difference is handled until the proposal is decided. The tool modes I checked exist (clip_check checks and flags; look_check silhouette --compare, thumb --size/--box; review_renders.py). The Blender `media_type = 'VIDEO'` exists. The engine facts were verified in round 1 and have not changed. No protected file was edited; changes outside the books are proposals. One wording inaccuracy about `--box` (R4). |
| C5 nothing valuable lost | PASS | The look-turn rule is restored. I compared the old SKILL.md files with the new ones after the F6 cut and walked the craft SKILL word diff: every removed item is kept, moved or replaced. The CONSTANT-or-copied-pairs choice was narrowed to copied pairs, which the library supports. |
| C6 fixed rules | PASS | Animator changes are limited to the 13 book files and the two job files (the other modified paths belong to the modeler, game-designer and preproduction work and to the lead's crew.md). The role frontmatter is byte-identical to df13ff4 (md5 match). SKILL.md has 140 and 107 lines. Descriptions are 399 and 387 characters. Section headings are only appended (design §9, game-timing §7-9, principles §10, review §8a-c, keying §7-8, playback §9-10). The J018 phrase is in all 13 headers. No Riot, game, champion or artist names, library ids or transcript lines in the bodies ('tips' hits are only 'tool tips' and 'fingertips'). No tips section. Evals unchanged. |
| C7 better work | YES | See below. |

## C7: will the agent make better work?

I read the books as the agent would for eval brief 1: a heavy two-handed greatsword, startup 0.5 s, active 0.15 s, recovery 0.6 s, cancel after 0.35 s.

**Old books.** The old books give the window mapping, the separate events and "heavy is not slow playback".

**New books.** The new books add these steps:
- First the agent must ask who reacts. Is the knight the player, with a tight coil inside startup, or an enemy, with the load held for the reaction window? The brief does not say, so the agent records the question with its owner instead of guessing.
- It writes a beat sheet ("hnnn, WHUM, KRANG"; subtext: commits everything).
- It lists the blade and the source of power as hook shapes.
- It puts 2-3 load and contact options on one black-fill contact sheet and records the pick.
- It blocks root first with copied-pair holds. It runs B-01..B-16, and with no reviewer named, it records its own check-in.
- It writes the timing list with stage names, the freeze frame (blade clear of the body) and the sync rule.
- It proves the impact with effects hidden and in grayscale.
- It checks the tip arc and gravity spacing from sample numbers, not by eye.

The output is clearly more readable, fairer and better documented. It costs one contact sheet more than the old books, not dozens of images. The same holds for the drawbridge (prop personality, truth of the walkable state, reduced-motion behaviour in the spec).

**Weak spots:**
- One finding landed as a keyword (F1).
- The worked emote still shows the spin rule on a look-turn (R1).
- Timing picks have no one who can watch the preview during the job (R2).
- §9 falls outside the part of the skill kept after compaction (R3).
- Two in-game checks lack a named supplier for their test hooks (R5).

None of these makes the work worse than the old books. F1 is a one-line fix.
