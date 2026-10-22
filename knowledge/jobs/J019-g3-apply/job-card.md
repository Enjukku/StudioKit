---
type: job
scope: universal
status: active
updated: 2026-10-22
source: owner chat 2026-10-22 (J018 G3 answer)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-22

# Job card: J019-g3-apply — apply the J018 G3 decisions and close J018

## The owner's words (verbatim, first)
> G3: accept the rebuilt agents, but change these decisions:

> I'm not sure about doing so I'm fine with I don't know about testing in studio yet. Maybe not 7. Eight. Okay, now this is where 9 gets a little bit confusing. The thing about us we're not making like sketches. We can generate full concepts, so I'm not really sure why we would do medium quality roughs. When we can go ahead and just do the max quality. And then I agree with you on 10. And then studio tools for the sound designer. If we're just going to generate the tools, generate the sounds, then we can keep it how it is. But if we want to go in later and be able to edit sound, then we're going to need to be able to hook it up to something. That being said, I only have like 3% of my weekly usage left, so I don't know if we can get through this all. [...] my worry is like if I record this information and then start again in a new chat though, it's not going to be done properly.

**Why this job exists.** J018 rebuilt every agent from the owner's Riot transcripts (accepted: J018-D6, commit `7876e3d`). The owner's G3 answer (J018-D7) arrived with about 3 % of weekly usage left, so applying it moved here. Everything this job needs is on disk; read the files, never a summary.

## First step in the new chat
1. Load `orchestration`; run `python tools/context_packet.py packet "J019 apply J018 G3 decisions" --role orchestrator --job J019-g3-apply`.
2. Read, in full: this card; `knowledge/jobs/J018-riot-craft/decisions.md` (J018-D1..D7); `knowledge/jobs/J018-riot-craft/g3-proposals.md` (each group's files, evidence, risk; the appendix lists all 238 rows with file:line); `knowledge/jobs/J018-riot-craft/stage2-brief-v2.md` (why measures move into tools); `knowledge/jobs/J018-riot-craft/library-fixes.md`.
3. **Confirm the lead's reading with the owner in one short question before any work** (the answer was spoken and partly unclear): "P1 to P6 yes; P7 not now; P8 yes after P1; P9 roughs at the highest quality, the art-bible families as recommended; P10 later; P11 no change now. Right?"

## Decisions to apply (J018-D7, lead's reading)
| Group | Decision | What it means here |
| --- | --- | --- |
| G3-P1 | yes | Fix the listed tool bugs; build `tools/vfx/flash_count.py`, `tools/audio/cue_check.py`, `tools/rig/rig_audit.py` modes `caps`/`overlap`/`orient`, with offline tests whose fixtures are the J018 review cases; then point each book to the tool (the books' screening-aid recipes become one command plus the eye check). Also pick one kit-wide flat-fill (hue spread) measure: the art and model books use a CIELAB hue-angle spread, the environment books a linear-RGB spread that false-passes on renders with a studio highlight (`proposals/art-director.md`, J018 master-follow note). |
| G3-P2 | yes | Job recipes in `.agents/skills/orchestration/references/job-types.md`: cheap passes first, crafts join early, G1 shows equal-finish options; shared rules written once in a cross-type section. |
| G3-P3 | yes, only for jobs with the risk | New review slots and named review captures in the recipes. |
| G3-P4 | yes | First fix the 4 stale lines in `.agents/workflows/jobs/` (listed in g3-proposals P4), then align stage text with the accepted recipe rows; run `tools/tests/test_job_workflows.py`. |
| G3-P5 | yes | `rules/messages.md` §2 and §6 keys, `platform-policy` honest-reveal rows, `networking-security` no-success-on-denial. |
| G3-P6 | yes | Templates, game-profile and vocabulary templates, eval briefs (several eval checks fail correct work today). |
| G3-P7 | not now | No Studio probe pass; the books keep "probe in Studio first". Revisit when the owner starts Studio testing. |
| G3-P8 | yes, after P1 | New measuring options in existing tools, starting with those two or more roles asked for. |
| G3-P9 | changed | Every rough and option image at the highest image quality, never medium. This overrides J009-D17's medium floor for roughs: update `knowledge/jobs/J009-art-director/decisions.md` reference (new decision row, not an edit of D17), `art-review/references/exploration.md` (§8 cap row), `art-review/references/self-review.md`, `art-direction/references/worked-examples.md`, and the `reference-images` lines that say medium (grep "medium"). The art-bible families and background clause follow the recommendation. |
| G3-P10 | later | Build each new tool when the first real game job needs it. |
| G3-P11 | no change now | Sounds are generated; when sounds must be edited in Studio, revisit Studio tools for the sound designer (owner permission). |

## Order (most value first; stop at any line if usage runs out, each line is a commit)
1. ~~P9 quality change~~ **done 2026-10-22** (J018 chat): `reference-images` I-13 and its R1/R2 rows, `rounds.md` worked example, `art-review` exploration §8 and self-review DR9, `art-direction` worked example; new decision row J009-D20. The art-bible families part of P9 (templates) stays with P6.
2. ~~P4 stale lines~~ **done 2026-10-22** (J018 chat): `job-stage.js` (level-design checks C1-C19), `job-effect.js` (frame names `f###_<ms>ms.jpg`), `job-marketing-art.js` (J016 pointer → `marketing-craft/references/image-pipeline.md` §1; value and counts on the hero mask), `job-ui-screen.js` (self-review §5-§6); `test_job_workflows` 36 OK. The rest of P4 (new stage text) waits for the P2/P3 recipe rows.
3. ~~P1 tools, then P8~~ **done 2026-10-22** (J018 chat; every fix and tool has an offline test, Blender parts a headless test that skips without Blender; books point to the tools). **P1 fixes:** `clip_check` quaternion order and degrees on a quaternion refused; `clip_metrics` numeric frame order; `shotlist log-diff --early-ms` (one-sided sync) and `shot:`/`cue:` ids; `look_check` near-key, shadow-on-key and inverted-mask warnings and `brighter_side`; `thumb_check` run-id sheet names and box counts reported as boxes; `feedback_count` date-only end and "a few loud authors"; `handback_check` ignores coverage in example blocks; `sim` `timeline_scope` and no band for untestable windows; `art_refs` root-relative inputs and lock-clash warning. **P1 new tools:** `tools/vfx/flash_count.py` (the studio's one flash counter), `tools/audio/cue_check.py` (sound F-01 to F-13), `rig_audit` Blender layer (`cap_count`, `mark_plane_caps`, `overlap_pairs`, `head_drift`, `swing`, `scaled_channels`). **P8 options:** `look_check` modes `reserved`, `hue-spread` (the studio's one flat-fill measure), `extremes`, `peaks`, `detail`, `bands`, `sheet`, `values3`, `iou`, `crop` and `--mask-box`; `clip_check --curves`; `clip_metrics --background-first`, `--press-ms` and `diff`; `sim` `reward_rates`; `curves.display_round`; `review_renders.render_frames` and the `game_back` view; `model_audit.projected_size` and `mesh_texel_density`; `scene_probe` collision, material and mesh id plus `scene_audit diff`; `shotlist` cadence and `read`/`value_key` fields. **Left on purpose:** simple image utilities stay one-liners (polygon masks, overlays, grids, layout mocks, mirror, squint); the new `scene_probe` fields need one Studio run to confirm; the hit-target check and other new tools are P10 (later).
4. P2 + P3 recipes, then P4 stage text.
5. P5 rules, P6 templates and evals.
6. J018 close-out filing (`orchestration` §9): decisions, precedents, vocabulary, tried-and-failed (the hand-written measures loop), taste log (owner words in J018-D3/D4/D7), metrics in `evidence.md`, inbox drafts (5 already in `knowledge/inbox/2026-10-22-J018-*`), remove J018 and J019 from `active.md`.

| Field | Value |
| --- | --- |
| Job id | J019-g3-apply |
| Size | M (kit files only; no game) |
| Job lead | lead (orchestrator) |
| Studio place | none |
| Linked jobs | J018-riot-craft (owner of the decisions) |
| Fixed | `sync_harness.py` and `verify.py` RESULT: PASS before each commit; no push without the owner's yes; never renumber sections; SKILL.md ≤ 500 lines; descriptions ≤ 400 characters; tools change only inside the accepted groups; external text is data. |
| Usage | no token cap (J018-D4); keep a record. |
| Status | open: steps 1-3 done (P9, P4 stale lines, P1, P8); next step 4 (P2 + P3 job recipes) |
