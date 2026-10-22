---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer animator · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: animator books, round 3

Scope: `.agents/roles/animator.md` (body), `.agents/skills/animation-design/` (SKILL.md, references/), `.agents/skills/animation-craft/` (SKILL.md, references/; evals not changed). I reviewed the working tree on 2026-10-22, after repair round 2, against git `df13ff4`. Inputs: `knowledge/reference/craft/riot/` (README, `universal-principles.md` = master, topic files, `matrix.md`), `coverage/animator.md`, `proposals/animator.md`, `job-card.md`, `reviews/animator-rev1-reviewer.md`, `reviews/animator-rev2-reviewer.md`. Line numbers are working-tree lines.

## Earlier findings: status

| Round | Id | Status | Evidence |
| --- | --- | --- | --- |
| 1 | F1 (SD-04 verb, SD-22 end-of-state tell) | fixed (round 2 confirmed; still holds) | `game-timing.md:40-41`; `review.md:104` B-16; SKILL.md:39, :42; role :38, :53 |
| 1 | F2 (look-turn rule) | fixed, holds | `principles.md:93`; `body-and-species.md:19`, `:45`; `review.md:124` S-15; `worked-examples.md:12` now agrees |
| 1 | F3 (plan-stage image budget) | fixed, holds | `review.md:73`; SKILL.md:40, :104; role :45 |
| 1 | F4 (fresh viewer method) | fixed, holds | `review.md:84`; `principles.md:5` |
| 1 | F5 (timing from stills) | fixed, holds | `review.md:10`; `blender-keying.md:76`; `game-timing.md:50` |
| 1 | F6 (SKILL size and compaction) | fixed | §8 ends at character 17,953 of 24,580 (about 4,500-4,850 tokens at 3.7-4 characters per token), inside the 5,000 kept; SKILL.md:19 tells the agent to re-read §8 and §9 after a compaction |
| 1 | F7 (check-in with no named reviewer) | fixed, holds | `animation-craft/SKILL.md:28`, `:91`; role :41 |
| 1 | F8 (sync window vs sound-design) | fixed, holds | `game-timing.md:44`; `review.md:139` G-04; `sound-design/SKILL.md:80` still says −35 to +100 ms, as the book states |
| 1 | F9 (tables and headers) | fixed | coverage CD-21 row; SKILL §4 heading; `roblox-playback.md:62` (corrected again in round 2) |
| 2 | F1 (CD-25 keyword only) | fixed | `principles.md:84` P-06.11 (rule and sign); `review.md:105` B-17; `game-timing.md:64` hand-off row; `worked-examples.md:18`; `blender-keying.md:75` (set the clip's key frame, never re-pose); SKILL.md:86; role :69. It matches the library's apply and check lines |
| 2 | R1 (worked emote used the spin rule) | fixed | `worked-examples.md:12` (eyes, head, chest in the glance; world-hold only if the hop turns the body), `:16` (blink on the fast head turn) |
| 2 | R2 (no one can watch a preview during the job) | fixed | `review.md:10`; SKILL.md:40; role :37; B-12 `review.md:100` |
| 2 | R3 (compaction edge) | fixed | see round 1 F6 above |
| 2 | R4 (`thumb --box` claim) | fixed | `roblox-playback.md:62`; `look_check.py thumb --help`: `--box` makes the box the subject, `--mask` exists, and they cannot be used together. The book offers them as alternatives |
| 2 | R5 (test-place hooks with no supplier) | fixed | role :67 (feature-builder row); `review.md:146` G-11, `:149` G-14 |
| 2 | R6 (eval A6 cap) | fixed | `proposals/animator.md:28` evals row |
| 2 | R7 (RI-15 rejection) | fixed | `body-and-species.md:58`; coverage row RI-15 |

```text
<spec>
artifact: .agents/roles/animator.md (body) + .agents/skills/animation-design/** + .agents/skills/animation-craft/** (not evals) @ working tree 2026-10-22 after repair round 2, base df13ff4
reviewer: J018 reviewer animator (opus, high)
looked_at_first: [the 13 book files read in full before the coverage table; git diff --stat and git status; git show df13ff4 of design SKILL §5-§8 against the trimmed §5-§7; word diff of the role file; section-heading prefix check old vs new on all 13 files; character offsets of the SKILL § headings; grep of the bodies for Riot, game, champion and artist names, library ids, transcript lines and tips; frontmatter of the role file and the two SKILL.md files against df13ff4; description lengths]
then: [matrix.md animator column compared by script with the coverage table (139 ids, 0 missing; 175 rows with the 16 untagged and 20 UP rows); the principle, apply, check and roblox_fit lines of all 155 tagged and untagged findings, each held against the book text at its landed-in location; universal-principles.md UP-01..UP-20 principle and motion lines against SKILL §9; tools: look_check.py thumb and silhouette --help, clip_check.py --help, tools/model/review_renders.py (Workbench world colour as the background); docs mirror spot checks: characters/index.md (clavicles, fingers), AnimationTrack.yaml AdjustSpeed (0 pauses), GuiService.yaml ReducedMotionEnabled, PoseEasingStyle.yaml, Pose.yaml (CFrame only), FaceControls.yaml, ParticleEmitter.yaml TimeScale, Camera.yaml FieldOfView (vertical); sound-design S-133 and vfx-design T-09; rules/company.md:105 and rig-pipeline §4a (light checks); rig-pipeline and job-types (where a proxy rig comes from); grep for kit files that cite animator steps or animation-skill sections; animation-craft/evals/briefs.md (common checks, brief 5)]
findings:
  - id: R1
    class: recommendation
    where: "animation-design/SKILL.md:127 (§9 #5); coverage/animator.md:105 (SS-05)"
    expected: "C1: SS-05 lands as a rule with its check. For animation: aggressive subjects move with sharp, angular timing and paths; friendly ones with soft arcs and eases. The check is that the mood the brief asks for (dangerous, friendly, stable) is named from the black-fill and the beat gaps alone."
    observed: "The rule exists only as a clause in the §9 #5 standard. There is no P-row and no self-review line. The §9 #5 check ('action and character named; limbs separate') does not test the mood. B-14 and §9 #10 name feel words only when another character's clip is in the set. An agent can therefore make a threat that moves in soft arcs and pass every line."
    evidence: "grep 'aggressive|soft arcs|friendly ones' over the 13 book files: only SKILL.md:127. Library shape-silhouette.md SS-05 check: 'a reviewer labels the mood (dangerous, friendly, stable) from the fill alone'."
    smallest_fix: "Extend the §9 #5 check: '... a fresh read of the key-pose black-fills and the beat gaps names the mood the brief asks for (dangerous, friendly)'. Optionally add a principles.md §4 row (P-04.7: sharp, angular spacing and paths for threats; soft arcs and longer eases for friendly subjects; sign: a fresh read names the mood)."
  - id: R2
    class: recommendation
    where: "animation-design/references/review.md:148 (G-13)"
    expected: "C3: each self-review line can run with our tools. Studio MCP gives stills at an uncontrolled capture time (roblox-playback.md:62: 'These are stills: timing comes from the Output log')."
    observed: "G-13 asks for the lowest and highest results to be compared 'frame by frame, up to the result frame' from captures (input C). Stills cannot show this frame by frame. In practice the line ends as 'not verified', or the agent claims it from two stills."
    evidence: "review.md:148; roblox-playback.md:62; review.md:75 ('a still shows a pose, not timing')."
    smallest_fix: "G-13: 'the lowest and highest results play the same windup clip id or sequence up to the result event (data and the timing list), the Output log shows the same event times for both, and captures at the same marker times match'. Input: data, log, C."
  - id: R3
    class: recommendation
    where: "animation-design/SKILL.md:40 (§3 step 6); roles/animator.md:37 (step 3)"
    expected: "C7: a step can run at the point where the order puts it. For a new character the thumbnail pass comes right after S1, before the rigger's K1. The proxy rig comes only at the proof (job-types.md:42), and the real rig only at S5."
    observed: "Step 6 says 'pose 2-3 clearly different options ... on the real or proxy rig'. At that time neither rig may exist. body-and-species.md:60 has the answer (a posed Blender mannequin with the rig's proportions), but step 6 does not point to it."
    evidence: "rig-pipeline SKILL.md:50 (S4 proxy sweep is the rigger's), orchestration job-types.md:42 (proxy rig at the proof); SKILL.md:40."
    smallest_fix: "Step 6: '... on the real or proxy rig, or, before either exists, the posed mannequin with the rig's proportions (`references/body-and-species.md` §6)'."
  - id: R4
    class: recommendation
    where: "the 'you see stills / the owner picks on playable previews / PROPOSAL take' rule: roles/animator.md:37; SKILL.md:40, :44; review.md:10, :73, :100, :146; principles.md:5, :104; blender-keying.md:76. The plan-stage budget: role :45; SKILL.md:40, :104, :114; review.md:73; craft SKILL.md:95; blender-keying.md:74; principles.md:109"
    expected: "Owner: 'better work, not longer books'. One rule is stated in full in one place, and other places point to it."
    observed: "The text in these places agrees today. But each repair round edited 6-10 places for one rule. The next change to the rule (for example after the owner sees the first gate packet) risks drift between the copies. The books grew from 122,958 to 192,557 bytes (+57 %). Most of that growth is useful: the self-review lines, the P-rows and the timing grammar. These repeated sentences are not useful growth."
    evidence: "grep -c 'playable preview|see stills': 9 hits in 5 files; 'plan-stage|contact sheet': 13 hits in 6 files; byte counts df13ff4 vs working tree."
    smallest_fix: "Optional. Keep the full text in review.md §1 item 5 and §5. Elsewhere use one short clause and a pointer ('timing picks: review.md §1 item 5'). Do not change the meaning."
  - id: R5
    class: recommendation
    where: "animation-design/references/game-timing.md:44 and review.md:139 (G-04); proposals/animator.md:25 (sound-design row)"
    expected: "An interim rule that hangs on an owner decision has a clean-up step."
    observed: "The sync rule says 'until it is aligned (J018 proposal), the sound-designer's book governs'. If the owner says yes at G3, the clause and the MEASURED fallback in G-04 become stale. The proposal row does not ask for their removal."
    evidence: "the lines cited."
    smallest_fix: "Add to the proposals row: 'on yes, delete the interim clause in game-timing §4 and the MEASURED fallback in review G-04'."
  - id: R6
    class: recommendation
    where: "animation-design/references/sets-and-states.md:27"
    expected: "Cross-references point to the section that holds the fact."
    observed: "'priority settles the rest joint by joint (`animation-craft` §5)': craft §5 is the code-driven motion spec. Priority is in §4 C-03 and in roblox-playback.md §3. This wrong pointer was already there at df13ff4 (line 24), so it is not a regression. The maker can fix it cheaply while in the file."
    evidence: "git show df13ff4:.agents/skills/animation-design/references/sets-and-states.md line 24; animation-craft/SKILL.md:41 (§4), :72 (§5)."
    smallest_fix: "Change to '(`animation-craft` §4 C-03)'."
keep:
  - "Every keep from rounds 1 and 2 still holds. The items: anticipation sized by who reacts; the plan stages in order (who reacts and feel words with their visible change, anchors and hook shapes with the side the camera sees, beat sheet with subtext and verb, one black-fill contact sheet per key clip with a recorded pick); blocking, then the check-in (named or self-recorded); the self-review lines per pass with N/K/C inputs; the blender-keying §8 compute table; attempt vs outcome; paid reveals with one windup; every-player reads (effects hidden, grayscale, reduced motion, 3 per second); C-22..C-27; variants keep the base; the hit-stop freeze frame supplied by the animator, with the bracket left to its owners; §9 with all 20 UP rows."
  - "The round 2 CD-25 repair is a full landing, not a keyword. It has a rule (P-06.11), a self-review line (B-17), a hand-off row, a craft recipe ('set the clip's key frame on the rig, never re-pose it'), a worked example and a partner-table row. A promo or cutscene still now shows the character players meet in play."
  - "The compaction fix: §8 now sits inside the part of the skill that survives compaction, and the skill tells the agent to re-read §8 and §9. The §4 trim moved the signs to principles.md without losing any. I compared the old §5-§8 with the new SKILL and the references: 'comedy' as a reason to key, the elevator and sign examples, the swinging-sign and trapdoor examples and the owner split of collision and outcomes are all still in body-and-species §4, worked-examples, motion-specs §1 and game-timing §1."
  - "The partner table in the role file ('what you ask for, and when'), with the feature-builder's test-place hooks. Each in-game line now has a named supplier for its input."
  - "The honest limits are written as rules. The agent sees stills, so timing is judged from beat gaps and strips. Sound sync is 'not verified' without a device capture. A missing phone gives BLOCKED. A number with no tolerance is MEASURED."
verdict: pass
</spec>
```

## Checks C1-C7

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | PASS (175 checked, 0 failed) | All 139 matrix ids for animator have a row (script compare: 0 missing). I checked 175 rows: 139 tagged, 16 untagged and 20 UP rows. For each, I held the library's principle, apply and check lines against the book text at the landed-in location. CD-25, SD-04 and SD-22, which failed in earlier rounds, are now full landings. One landing is thin: SS-05 has its rule but only a partial check (R1). It is counted as passed. The rejections are sound: CF-18 (camera height belongs to the film-director and marketing) and CF-19 (accent placement belongs to VFX and the environment). CD-21 is a partial landing with a sound reason, and RI-15 now lands. |
| C2 core principles | PASS | `animation-design/SKILL.md` §9 is in the skill the agent loads first. It is inside the part that survives compaction only up to §8, but SKILL.md:19 tells the agent to re-read §9. Each of UP-01..UP-20 is stated for animation, with an example and a check, and each agrees with the master's motion line. Small gaps are covered in the references: UP-10's 'premise of a shot' is in P-06.11, UP-16's paint-overs are in review §4, and UP-19's 'frequent things stay short' is in game-timing §2. No contradiction. |
| C3 self-review | PASS with one gap | The lines run on clip_check, the sample-curve compute table, the ≤ 8 key frames with look_check, Studio captures, the Output log and the builder's test hooks. One line (G-13) asks for a frame-by-frame comparison from stills (R2). |
| C4 kit rules and engine | PASS | Light checks agree with rules/company.md:105 and rig-pipeline §4a, and plan-stage images keep a separate, stated budget. Server authority and the `files` source mode are kept. Tool modes exist: clip_check flags; look_check silhouette --compare, thumb --size, --box and --mask; the review_renders world-colour pattern. Engine facts were re-checked in the mirror (clavicle and finger joints on advanced R15 only, Pose stores a CFrame, AdjustSpeed 0 pauses, ReducedMotionEnabled, PoseEasingStyle, FaceControls, TimeScale, vertical FieldOfView). Protected files are untouched. Recipe and workflow changes are G3 proposals. |
| C5 nothing valuable lost | PASS | I walked the role-file word diff, the old design SKILL §5-§8 against the trimmed text and the references, and coverage §c. Every removed item is kept, moved or replaced, or the library shows it was wrong (stepped-key blocking, the J016 riot-extracts pointer). No other kit file cites the renumbered work-method steps or SKILL steps. |
| C6 fixed rules | PASS | git status shows the animator's 13 book files and the J018 job files. The other modified paths belong to the modeler, game-designer and preproduction makers and to the lead's crew.md. The role frontmatter (lines 1-10) and both SKILL frontmatters are identical to df13ff4. The SKILL files have 142 and 107 lines. The descriptions have 399 and 387 characters. Section headings are only appended in all 12 skill files; the role file gained one unnumbered section, which does not move any § reference. The J018 phrase is in all 12 skill headers and in the role comment. The bodies have no Riot, game, champion or artist names, no library ids, no transcript lines and no tips section. The grep hits are header lines, 'messages', 'blade tip' and 'tool-tip'. Evals are unchanged. |
| C7 better work | YES | See below. |

## C7: will the agent make better work?

I read the books as the agent would for eval brief 5. In that brief the agent accepts the teddy rig, makes an idle loop, a walk loop and a wave, exports them and prepares the import. Up to 8 pets are on screen, on phones, with a third-person camera.

**With the old books,** the agent accepts the rig with numbers first. It writes the feel words and makes the loops with seam and slide checks. Then it exports, does the round trip and writes the import steps. The output is correct and safe, but the personality is unchecked: 'soft, light, friendly' has no visible sign and no test.

**With the new books,** the agent adds these steps:
- Each feel word gets a visible change, for example 'soft: round arcs, slow settles'.
- It lists the identity anchors (ears, belly patch) for the side the third-person camera sees, which is the back.
- It writes beat sheets with subtext for the wave and for the personality idle.
- It makes one black-fill contact sheet of 2-3 wave options at phone size and picks with a goal question. It makes two wave timing takes and judges them by beat gaps. The previews go into the G2 packet, and the better-reasoned take stands as a PROPOSAL.
- It blocks the walk root-first with copied-pair holds and records its own check-in, because the brief names no check-in reviewer.
- It runs S-01 (weight over the support when a foot lifts), S-14 (no twinning) and S-13 from the samples. S-13 is n/a with a reason when the rig has no shoulders.
- It offsets the phase of the 8 pets.
- It takes captures with effects hidden and in grayscale.
- It ends with a could-not-check list (sound sync, the phone row BLOCKED) and one named weakness.

The pet will read better at phone size and feel like a character, not a machine. The cost is about two contact sheets and two previews, inside the stated plan budget. The same holds for briefs 1 and 4, which the earlier rounds walked.

**Weak spots:**
- The 'sharp vs soft' motion language has no check (R1).
- One in-game line cannot run from stills (R2).
- The thumbnail step points to a rig that may not exist yet (R3).
- One rule is repeated in 6-10 places. This makes the books longer and risks drift (R4).
- The agent's own 'fresh read' is a weak stand-in, because the agent cannot forget the brief it keyed to. The blind reviewer repeat at the check-in is the real test.

None of these makes the work worse than with the old books. There is no blocking problem.
