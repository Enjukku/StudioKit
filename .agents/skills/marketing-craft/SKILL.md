---
name: marketing-craft
description: The marketing agent's how - titles, icons, thumbnails and key art (staged route, art_refs.py, thumb_check.py), game page, short videos, announcements, creator briefs, ad tests, launch timeline, weekly report. Use for "make the thumbnails", "check the icon", "name the game", "write the page", "plan the launch", "brief a creator", "set up an ad test". Read marketing-design first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J012 from the owner's marketing research paper (2026-10-21) and three fact-checks (`knowledge/reference/marketing/fact-check-*.md`, FD / FA / FS ids, read 2026-10-21). Note ids (PR, TP, ME, ...) point to `knowledge/reference/marketing/01-03`. Revised by J018 maker marketing · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): the image step became the staged key-art route (brief, research, thumbnail round, green light, render, colour, detail, layered master, crop family), with a self-review list (`references/image-review.md`) and worked examples; after the stage 3 review the route is written once, in `references/image-pipeline.md` §1; repair round 2: K-14 final size and icon plan, K-16 a pointer. Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021): belief check consumer.

# Marketing craft: from promise to package to proof

## 1. When this skill starts
After `marketing-design` has answered: what the game promises, who it is for, which moment proves it. Needed first: the vision record and the promise ledger (game designer), the art bible (art director), and for a launch the release plan. A game with no playable hook yet gets a title workshop and a capture plan, not a campaign (PR-01).

Effort: medium by default; **high** for a new game's title, icon and launch plan (owner J012-D1).

After a compaction, re-read §3 step 5, §6, `marketing-design` §4 and §7, and the stage you are in (`references/image-pipeline.md` §1).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Icon, thumbnail and key-art route: the stages from brief to owner package, what to run at each, `thumb_check.py` inputs and limits, short commands, worked examples | `references/image-pipeline.md` |
| The self-review I run on every image before it leaves me (MR-01..MR-33: what to look for, which input, which budget, which lines at which stage) | `references/image-review.md` |
| Which "test" each tool really runs, the analyst's spec, reading results, share links, Open Cloud, the weekly report | `references/testing-measurement.md` |
| Page, native video, short video, announcements, events, notifications, creators, Ads Manager, community: the work steps | `references/channel-kits.md` |
| Briefs to the game designer, trend scout, art director, analyst, live-ops designer, animator, modeler or environment designer (staged renders); what to ask each and when | `references/handoffs.md` |
| Roblox facts, truth and policy rules behind every step | `marketing-design` and its references |
| Templates | `templates/marketing/`: `title-checklist.md`, `thumbnail-icon-checklist.md`, `thumbnail-brief.md`, `short-video-plan.md`, `launch-timeline.md`, `weekly-report.md` |
| Image tool and locks | `reference-images`; `tools/art/art_refs.py`; `tools/art/thumb_check.py` (over `look_check.py`) |
| Measurement basics, events in code | `analytics` |
| Source notes and fact-checks | `knowledge/reference/marketing/` |

## 3. Steps (the campaign; each step has a check)
Work folder: `knowledge/jobs/<job>/marketing/`. One **campaign record** there (`campaign.md`): brief, policy checks with dates, sources, asset versions, rights, capture provenance, metric dictionary, owner decisions, live timestamps, results, next action (PR-14).
1. **Promise.** With the game designer: what the player does, what makes it distinct, the payoff the current build shows; unbuilt features listed and kept out of present tense (PR-01). *Check:* every claim you will use has a promise-ledger row marked playable (handoffs §1).
2. **Signals.** Ask the trend scout for audience words, rising and saturated title and thumbnail patterns, timing and rights flags (PR-02, handoffs §2). *Check:* every signal you use keeps its label and date.
3. **Decision and metric.** With the analyst: the decision, surface, metric label, denominator, cohort, window, guardrails, what counts as misleading traffic, before anything goes live (PR-03, `testing-measurement.md` §2). If the problem line holds a belief about players ("players click but leave", "nobody finds the game"), name it in the spec and use the analyst's belief check from the job card (`orchestration` SKILL §1 step 1); never pull data yourself. No data yet: write "untested" in `campaign.md` and design the first test to test it. *Check:* spec filled; the belief and its reading (or "untested") are in the campaign record.
4. **Message hierarchy.** One plain promise line, the proof, 5-10 title candidates, the first description sentence, a real reason to play now. Reject swappable genre slogans (PR-04). Each title through `title-checklist.md` incl. a comprehension check. *Check:* T1-T12 PASS or owner-resolved.
5. **Images: the key-art route.** Big to small through the stages of `image-pipeline.md` §1, from the brief to the owner package, each stage frozen before the next; the standards are `marketing-design` §4 M-15..M-23, the self-review is `image-review.md`, then the art director and the game designer (PR-05..06). *Check:* sheet + JSON + checklist per image and per crop; every MR line labelled by what proved it; no image reaches the owner with an unexplained FAIL.
6. **Proof capture.** Real gameplay from the shipping build for the native video, the gallery and social edits; version, scene, permissions, any staging recorded (PR-07; `channel-kits.md` §1-2). Ask for the captures early (the moment at the game camera, the device, the build), since the key art's research board needs them too. *Check:* every clip traces to a build and a claim id.
7. **Channel kit.** Page text, gallery order, native video, short-video plans, announcement and event drafts, creator brief, ad test plan, community plan, each checked against the destination's current rules on the day (PR-08, `channel-kits.md`). *Check:* every limit you rely on has a source and a read date.
8. **Policy and rights.** `platform-policy` + `marketing-design/references/policy-rights.md`: disclosures, age rules by format, PolicyService, rights record; unclear rights, minor creators or other countries → owner for qualified review (PR-09). *Check:* the three separate checks (ads, paid random items, earnings) recorded.
9. **Owner package.** Recommended assets and the rejected ones with reasons, the sheets, the release-gate items, budget options without commitment (`channel-kits.md` §6), measurement limits, a rollback (the current live assets) (PR-10). *Check:* every decision the owner must make is listed with a recommendation and a default; nothing is published by default.
10. **After the owner acts:** compare the live state with the approved set (asset ids, text, timestamps, campaign settings, links). An accepted upload is not proof it is approved, visible or shown to every eligible player (PR-11). *Check:* live-state table in the campaign record.
11. **Read results with the analyst** at the agreed date: raw counts, exact labels, paid and organic apart, mature cohorts only, 2026-10-12 marked if crossed; inconclusive is an allowed answer (PR-12, `testing-measurement.md` §3). Weekly: `weekly-report.md`.
12. **Next bounded revision.** Name what failed: understanding, audience fit, page friction, game quality, measurement or policy. More impressions never fix a false promise or a bad first session (PR-13). *Check:* one proposed change, one reason, what would disprove it.

For a new game, steps 1-9 follow `templates/marketing/launch-timeline.md` (four weeks before to four after, owner's window).

## 4. Craft core (what separates great marketing work from weak)
| ID | Practice | Evidence |
| --- | --- | --- |
| K-01 | **Small size is the real size.** Judge every icon at about 150×150 and every thumbnail at the measured phone tile, with the title under it, before the full-size image, and judge roughs only there. Say the action from the small preview in one sentence or it fails; then place the tile in the grid of the tiles it competes with | Roblox icon docs (FD-20); no tile size documented, so measure it (T04 answer); owner's check (J012 brief); detail made at full size is invisible at the tile |
| K-02 | **Measure what you cannot see reliably**: format, subject count and dominance, subject vs surround luminance, bottom band, with `thumb_check.py` and a hero mask; then look at the sheet. Numbers locate a problem; they never grade. Know where a number lies silently: an inverted mask, `--box` or coarse-polygon counts, a black-fill of my own drawing instead of the image's outline, a re-run overwriting the sheet, an upscale that passes every format check, a stretched crop (`image-pipeline.md` §2, §4) | `thumb_check.py` (J012-T07); `look_check.py` method (J009); re-tested on real input types in J018 |
| K-03 | **One hero, one action, one consequence** per thumbnail, at a moment ordinary play reaches, at the peak of the action or just before it. Distinct concepts across the set (core action / scale / social / progression payoff), each from a different hook, not palette swaps | paper IM-19 (O); `game-concept` C-08 first image; options that differ only in colour give nothing to choose between |
| K-04 | **The image model never writes words.** Title text is added afterwards and checked at small size; a text-free version is kept | art-bible `THUMBNAIL LOCK`; AI text errors (PR-06 failure checks) |
| K-05 | **Proof before polish.** Capture the promise in the build first; then make key art that dramatizes the same moment, with the character's signature key pose from the animator, not a new pose. Key art is labelled key art | PR-06..07 (O); Roblox native video rules (FD-34); a still posed apart from the game shows a character players never meet |
| K-06 | **Native video ≠ social edit.** Native: current gameplay early, no outside footage, narration, voice chat or lyrical music. Social: platform-specific edit, captions clear of the app's buttons, reviewed muted and with sound | FD-34, FD-48; SV-11 (O) |
| K-07 | **Name the test honestly.** Personalization = adaptive allocation; title and icon changes = observational; ad creatives = attributed. Write the label in the plan and in every report | FD-35, FA-11..12, TI-15 |
| K-08 | **The analyst's spec comes first**: decision, exact metric label, denominator, cohort, window, guardrails, disconfirming result. No spec, no test | PR-03, ME-18..19 (O) |
| K-09 | **Every limit has a date.** Platform numbers (sizes, quotas, ad minimums, prices, rates) go into plans as value + source + date read; anything only seen in a logged-in form is checked by the owner there | FA corrections (thumbnail count 10 vs 25, Engagement beta, minimums); `platform-policy` P-10 |
| K-10 | **Owner package, not owner surprise.** Options with a recommendation and a default, rejected work with reasons, a rollback, and every external action listed as an owner action | RG-01..07, PR-10 (O); `orchestration` §2 |
| K-11 | **Keep the record.** The campaign record beats a saved winning prompt: another agent can explain what was promised, what changed and why | PR-14 (O) |
| K-12 | **Stages that freeze.** Each stage of the route (`image-pipeline.md` §1) is judged only at its level and frozen before the next; after green light the big shapes do not move, and a structural note at polish becomes the next update's ticket | change costs rise at every stage; detail cannot rescue a wrong big read |
| K-13 | **The first output is a warm-up.** Make the typical idea first on purpose, label it, then make 3-5 roughs that must beat it, one atypical; equal finish; pick with reasons; never polish one option before the pick | the first idea sits inside everyone's expectation; uneven polish biases the choice |
| K-14 | **One master feeds the whole kit.** Plan every crop at the start, mark each crop's safe square before composing the rest, build the master in toggleable layers (foreground, midground, background, effects, light, title), make finals at final size (route c) or as the largest crop of the model's output with its size recorded (routes a/b, `references/image-pipeline.md` §1 stage 6). A new game's icon is its own brief and round (identity); an update or event icon is a crop of the master | one key art becomes the icon, tiles, ads, event and social art; a flattened or one-crop master forces a remake |
| K-15 | **Fresh eyes on my own image.** Grey, a 3-value study, a mirrored copy, and the art director's cold read before mine is final; fix one named problem per pass, worst first, by layer | the eye adapts to an image it has looked at too long |
| K-16 | **Image budget per stage.** Light checks as `references/image-review.md` §1 runs them; the budgets per stage are in `references/image-pipeline.md` §1, the video stills budget in `references/channel-kits.md` §3 | owner's light-check rule (J005-D8) |

## 5. Rules (final check, short)
- Never publish, post, upload, activate, spend, convert Robux, contact a creator or sign anything. List them as owner actions.
- No claim without a playable promise-ledger row. No fake UI, currency, prices, rewards or odds in any image.
- No invented optimum (title length, video length, posting time, cadence) and no invented cost (fee, CPM, CPP, minimum spend). Platform limits are limits, not targets.
- Reported lifts and case results are EXPERIENCE with their scope, never forecasts.
- `platform-policy` for every ad, paid random item, younger-player and data question. No user data to outside platforms.
- Secrets (Open Cloud keys) stay outside the repo; only the owner creates them.

## 6. Self-check before returning
- [ ] Campaign record updated: sources with read dates, asset versions, decision ids.
- [ ] Every image: `thumb_check.py` sheet + JSON with a hero mask (traced and overlay-checked, magenta pass, key or alpha; never a coarse polygon for counts or black-fill), checklist, art director note; every title: checklist with comprehension check.
- [ ] `references/image-review.md`: each stage's MR lines on every candidate and crop, the full list (MR-01..MR-33) on the recommended final, each line labelled (measured / looked / art-director / game-designer / owner-confirmed / not verified); the could-not-check list written.
- [ ] Options: warm-up labelled, 3-5 distinct roughs (shape and frame IoU recorded), one recommended with reasons, rejection reasons, closed directions recorded.
- [ ] Images generated and sheets looked at, reported against the stage budgets.
- [ ] Every test: analyst spec before start; honest label (adaptive / observational / attributed / randomized).
- [ ] Every platform number in the package has a source and a read date; logged-in-only facts are marked "owner to confirm in the form".
- [ ] Owner actions listed; nothing external done.
- [ ] Hand-back in `rules/messages.md` §3 with coverage of every item in scope.

Project overlay: if `knowledge/overlays/marketing-craft.md` exists, read it after this file; it wins for this game.
