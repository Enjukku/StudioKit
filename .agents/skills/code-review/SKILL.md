---
name: code-review
description: Review Roblox Luau changes, especially AI-written code, for what hurts players most - lost data, exploitable requests, money and policy, misleading feedback or reveals, leaks, performance, over-building - and set which tests a change needs. Use before merging, for "review this", "is this safe", "why did this break", and after a builder hands back code. Reports proven findings; never rewrites.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J001 step 6. Evidence: owner research papers (`knowledge/reference/architecture/strong-codebases-2026-10.md` A-20, A-23; `roblox-operations-2026-10.md`), the kit's engineering skills and the Roblox docs mirror. Rebuilt by J018 maker reviewer · claude-opus-5-5 · high · 2026-10-22, built also from the owner's Riot transcripts (J018): two reading passes, what each input can prove, the could-not-check list, re-review by the problem, player-facing truth in code, core principles (§7). Repair round 1 (J018 maker reviewer · claude-opus-5-5 · high · 2026-10-22): PT-18, PT-19, harm-area and fresh-eyes self-review lines, the planted-fault route, one place each for the failure sweep and the PT severities. Repair round 2 (same maker, 2026-10-22): PT-09 against the five comfort settings, one meaning for the fresh-eyes pass. Repair round 3: PT-19 checks both hook guards.

# Code review: find what would hurt players, prove it, rank it

## 1. When this skill starts
A change is ready to merge, a builder handed back code, something broke ("why did this break"), or the architect's plan for a deep change arrives before the build. I need the brief or feature plan (intent), the candidate revision and its diff, the test results, and, when players see or hear the change, the rows it implements (the architect's presentation contract, the builder's feedback stack sheet, the timing list, the odds table) and the builder's debug log of the test-hook runs. Without the intent, I ask for it: a diff alone cannot show missing behaviour.
After a compaction, re-read §3 to §7 of this file before continuing.

## 2. Read this file when
| You need | Open |
| --- | --- |
| What each input can prove; the two reading orders; how to write a finding; re-review rounds; the could-not-check list; symptom reviews; plan checks | `references/review-method.md` |
| Effects, sound, UI motion, counters, reveals, camera; presentation that must not decide gameplay; test hooks: what the code must guarantee (PT-01 to PT-19), severities, the input each row needs, screening patterns | `references/presentation.md` |
| Four reviews written out (egg hatch, sword hit, a clean change, a symptom) | `references/worked-examples.md` |
| Which tests the change needs; when a result counts; fixtures; boundary brackets | `references/testing.md` |
| Current Luau and outdated habits | `references/luau-current.md` |
| The rules each area must keep | `data-saving`, `networking-security`, `platform-policy`, `performance`, `ui-basics`, `architecture` skills |

## 3. Steps
1. **Set depth and the stop rule** (V-13): quick, standard or deep; what "done" means for this review (§3 step 9).
2. **Read the intent**: brief, invariants, acceptance cases with their failure cases, owned files, non-goals, spec rows. Write 2-4 goal questions, each naming an invariant (`references/review-method.md` §2).
3. **Look before the claims**: the diff and changed files at the candidate revision, then the builder's manifest (V-03).
4. **Check scope** (V-09, V-18): files changed vs owned; new files the plan did not name; a second way to do something the game already does.
5. **Pass 1, file order, shallow**: every changed file against all 8 harm areas (V-01, V-02); write candidates only.
6. **Pass 2, trace order**: each player path from input to cleanup, then its failure sweep (V-15); for anything players see or hear, the PT rows of `references/presentation.md`.
7. **Prove or drop** each candidate; try to make it safe first (V-06, V-14); a candidate only a run can settle becomes a ticket and a could-not-check line.
8. **Check the tests** (V-05, `references/testing.md`): lane, the brief's failure cases, can fail, limits bracketed.
9. **Write and close** (V-12, V-16): ranked findings in the `rules/messages.md` §6 fields, keep list, could-not-check list, the honest recap, the verdict. Re-reviews follow V-17.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| V-01 | **Harm order:** (1) saved data lost, corrupted or duplicated; (2) a client can gain rewards, items, permission or damage (`networking-security` N-02 validation, N-03 server-decided outcomes such as prices; presentation that decides gameplay, test hooks live outside Studio: PT-18, PT-19); (3) money, policy and player safety (receipts, odds, prices, filtering; paid reveals and counters that tell the truth; flash rates; `references/presentation.md` PT-03, PT-04, PT-10); (4) leaks, yields, lifetimes, races after waits; (5) performance at peak; (6) structure (owners, contracts, locality; presentation follows confirmed results and shared data, PT rows); (7) outdated or invented APIs; (8) over-building. Style is the tools' job | A-23 (fix by harm and blast radius) |
| V-02 | **Adversarial questions** for every change: where is authority duplicated? which callback can outlive its owner? what happens after a yield (player left, character respawned, round ended)? can a retry repeat a side effect? does a config or data change bypass validation? what does the worst client input do? what does a denied request show the player? | A-20 |
| V-03 | **Intent over diff; look before the claims.** Missing behaviour (a failure path, a cleanup, a check, a pending or denied state) is the most common defect in generated code and never shows in a diff: compare against the brief's invariants and failure cases. Read the code before the builder's hand-back; its claims are claims | A-20; `architecture` R-01; `rules/company.md` §7 |
| V-04 | **APIs must exist.** Every engine call, property and enum in the change is checked against `_api-reference/` (and its deprecation notes); invented or deprecated APIs are findings. If the mirror is missing, still report the call and mark it "unverified: no API reference available" | `AGENTS.md` §0 |
| V-05 | **Tests must be able to fail.** Expected results come from the brief, not from the code; zero or skipped tests are a fail; one test checked against a deliberately wrong version (the qa-lead's planted-fault result, else a scratch copy: `references/testing.md`); every limit has a case just inside and just outside | `references/testing.md` |
| V-06 | **Evidence or nothing.** Each finding: file:line, a concrete failure scenario (input or sequence → wrong outcome for players), severity, and the label of the input that proved it. "Might be a problem" without a scenario is not reported | ours |
| V-07 | **Concurrency is reviewed as sequences:** two servers, two players, leave mid-save, respawn mid-ability, duplicate requests, two overlapping effects on one track. Write the sequence in the finding | `data-saving` D-04, D-11; `networking-security` N-02 |
| V-08 | **Lifetimes:** every `Connect`, `task.spawn/delay`, tween, `Instance.new`, pause (`AdjustSpeed(0)`, `TimeScale = 0`) and camera change has a cleanup or restore owner, on its timer and on interruption; I name the owner or report the leak | `architecture` R-11 |
| V-09 | **Scope discipline:** changes outside the owned files, unrequested renames, new packages or layers are findings, even if they work | `rules/packages.md`; `architecture` R-09 |
| V-10 | **Report what was not checked** with the labels gate-verified / MCP-verified / owner-confirmed / not verified; the could-not-check list (V-16) carries each item | `AGENTS.md` §3 |
| V-11 | **Over-building is a finding, nitpicks are not.** Apply the reviewer checks in `rules/anti-overengineering.md` (unplanned files, one-caller abstractions, defensive code around our own code, out-of-scope edits, extra tests, stubs). A stand-in (temp asset, placeholder text, stub) the manifest does not name is a finding; a named one is a could-not-check line. "It would be cooler" is a new request, not a finding. No style or "could be nicer" items. Depth follows risk; after 3 rounds on one approach, escalate to the lead instead of another round; later rounds review only the new diff; findings in untouched code are tagged pre-existing follow-ups | `rules/anti-overengineering.md` 18-20; claude.dev/blog/solving-code-review-at-anthropic (2026-10-15) |
| V-12 | **Severity and report format.** Critical: data loss or duplication, a client gains currency, items or permission, a money or policy rule broken. High: a race, leak or yield that breaks play; performance past the game's budget at peak. Medium: structure, scope, outdated APIs, over-building. Player-facing cases (PT rows): the one severity table in `references/presentation.md` §3. Anything lower is at most a one-line non-blocking note, only with proof. **Find first, filter second:** list every candidate across the harm order, prove or drop each, then rank (asking a model to report only severe items up front can lower what it finds: Opus 5 prompting guide, `knowledge/reference/engineering/paper/factcheck-practice.md` correction 4). A clean change gets "no blocking findings", never an invented one. Each finding is one row: severity · file:line · scenario · rule broken · fix direction · protect · retest | ours; J010 |
| V-13 | **Missing intent and review depth.** No brief or plan: ask for it; if none exists, review against the intent you infer from the code and the request, and say so in the first line. Depth: quick (small change, no money, saves, remotes or security), standard (default), deep (money, saves, remotes, security, paid random, or many files). The depth sets the stop rule: quick = scope, pass 1 (areas the change cannot reach marked n/a with the reason) and the tests; standard = both passes; deep = both passes and the final harm-order pass (`references/review-method.md` §2 step 5). At every depth each kept candidate is re-read from the caller's side before it is written | `rules/anti-overengineering.md` 19 |
| V-14 | **Try to make it safe before calling it a bug.** For each candidate look for the guard elsewhere (transport rate limit, data-layer check), the engine guarantee (a docs line) or the type that rules it out; when several fixes would work, recommend the smallest with the reason | ours |
| V-15 | **Two reading orders.** Pass 1 in file order, shallow, over the whole change; pass 2 in trace order per player path, plus the failure sweep on the same path (the trace and the sweep's cases: `references/review-method.md` §2 steps 3-4). The second order finds what the first missed | `references/review-method.md` §2 |
| V-16 | **Close honestly.** Every check names its input; the review ends with the keep list, the could-not-check list (step, missing input, what closes it, who supplies it) and one line on the weakest part of the review. I never pass a check its input cannot show; feel is the owner's at the gate | `references/review-method.md` §1, §5 |
| V-17 | **Re-review by the problem.** Map every earlier finding fixed / not fixed / disputed; re-trace each finding's sequence in the new code or read its retest's log (a fix that made the suggested change but still allows the sequence is not fixed); walk the harm order on the new diff around each fix; withdraw a finding the builder disproves; ideas past the gate are follow-ups | `references/review-method.md` §4 |
| V-18 | **One house way.** The change uses the patterns the game already has (transport module, data adapter, policy module, cleanup object, motion and colour tables, settings module). A second way to do a solved thing, or a new module that duplicates one, is a finding | `networking-security` N-01; `engineering-craft` EC-15 |

## 5. Rules (final check)
- Changes touching purchases, currency, saves, trades, paid random items or client-callable methods always get this review before merge.
- A finding without a failure scenario is not reported; a check without the input that can prove it is not passed.
- The reviewer does not rewrite or edit the change; it reports, and the builder fixes. A fix sketch is at most 3 lines.
- Presentation is reviewed as code, never as taste: when it plays, for whom, from which data, and what a failed request shows.
- Binding skills win: where this book and `platform-policy`, `data-saving` or `networking-security` differ, the binding skill decides.

## 6. Self-check before returning
Inputs: B = brief, plan, spec rows, manifest · D = the candidate's diff and files, read · G = a screening pattern (`presentation.md` §5; a pointer, never proof) · T = gate or test logs on the candidate revision · S = Studio or device evidence supplied by the builder or the qa-lead (I cannot produce it: ticket) · P = a partner at the named check-in.
**Intent and scope**
- [ ] (B) Depth and stop rule recorded; goal questions written, each naming an invariant; no intent → asked, or inferred and said in line 1.
- [ ] (D) Code read at the candidate revision before the manifest; the revision recorded in the review file.
- [ ] (D) Scope: changed vs owned files; unplanned files; a duplicate of an existing module or a second way to do a solved thing (V-18).
**Both passes**
- [ ] (D) Pass 1: every changed file walked against all 8 harm areas; skipped areas named with the reason.
- [ ] (D) Pass 2 (standard and deep): each player path traced input to cleanup; each failure-sweep case has code or a finding.
- [ ] (D) Fresh eyes: each kept candidate re-read with the hand-back closed and from the caller's side; deep: one more pass over the harm order on the same frozen revision (`review-method.md` §2 step 5).
- [ ] (D) After every yield in a handler the same player, character or session is re-checked; every connection, task, tween, instance, pause and camera change has its owner (V-08).
- [ ] (D) Engine calls exist in `_api-reference/`; custom replacements of engine mechanisms carry the EC-03 answer; nothing server-only replicates.
**Harm areas 1-3** (the binding skills' rows; pointers, not copies)
- [ ] (D) Each client-callable handler: the `networking-security` N-02 order, with its idempotency key for anything that grants (its §6 checklist).
- [ ] (D) Each save write, grant or spend: through the `data-saving` D-05 update, only once the player is ready (D-04); receipts, trades and quest rewards by D-11.
- [ ] (D) Each paid random or policy-gated path asks the game's policy module (`platform-policy` P-02), never `PolicyService` directly.
- [ ] (D, G) No damage, grant, spend, save write, state change or hit area decided in a marker, track-event, tween `Completed`, effect `Touched` or client-timer handler (PT-18, S9).
- [ ] (D, G, T) Every test-hook reader behind `RunService:IsStudio()`; no hook reachable from a client request; the default project file maps no hook (PT-19, S10, SR-18 log).
**Player-facing truth** (when players see or hear the change; `presentation.md` §2)
- [ ] (D, G) Success layers only on the confirmed result; denied and unavailable results show no success; slow answers show pending (PT-01).
- [ ] (D) Outcome size from the server's result, escalation thresholds from data (PT-02).
- [ ] (D) Logic and affordability read the true balance; the display only counts up to it (PT-03).
- [ ] (D, P) Paid random: result decided on the server first; windup code takes no tier input; one odds table, effective odds; restricted gate; the S-44 frame compare requested from the UI designer (PT-04).
- [ ] (D, G) Telegraph sent when the wind-up starts, with its server time, never in the same step as the damage; shape, radius and fuse from the hit test's data; removed on the end event; every attack path fires it (PT-05, S11).
- [ ] (D, G) Camera, FOV, post effects and shake only from the local player's own events at the allowed importance; shake rotates, decays, is restored; others' effects toned only locally (PT-06, PT-07).
- [ ] (D, G) Each hit-stop pause restored on its timer and on interruption; nothing pauses the server or physics (PT-08).
- [ ] (D, G) The comfort module answers the contract's five settings (reduced motion, shake, flashes, screen effects, clarity); every tween, shake, flash, tint, FOV punch and toned effect in the change asks the setting that owns it, and each reduced path keeps the information (PT-09).
- [ ] (D, G) Code-driven pulses and blinks at most 3 Hz (1 / full period); the composite flash count is the VFX designer's, else a could-not-check line (PT-10).
- [ ] (D) Frequent effects pooled, capped, merged; low quality drops decoration only (PT-11).
- [ ] (D, G) Random only on decorative values, engine-side ranges included (PT-12).
- [ ] (D, B, G) Effects and sounds fire from the timing list's marker or the gameplay event, by the contract's names (PT-13).
- [ ] (D, G) Meaning colours, durations, asset ids, radii and tiers read from shared data (PT-14).
- [ ] (D) Denials show their reason at the control; cosmetics change no physics or stats; no sound-only state change (PT-15 to PT-17).
**Tests and evidence**
- [ ] (T) Lane fits; the brief's failure cases are tests; zero or skipped tests fail; limits bracketed.
- [ ] (T, P) Tests can fail: the qa-lead's planted-fault result read (caught x of n, false alarms y); else one fault planted in a scratch copy of the candidate, never the tree under review (`references/testing.md`); else a could-not-check line.
- [ ] (T, S) Every runtime claim (timing, replication, physics, performance, feel) carries its label; without S it is not verified and its item is not done.
**Writing and closing**
- [ ] (D) Each kept finding survived the try-to-make-it-safe step; one problem per finding with harm area, rule, file:line, sequence, severity, fix direction, protect, retest.
- [ ] (D) Ranked most harmful first; at most a few recommendations, each proven; no style or taste.
- [ ] (D, T, S) Keep list, could-not-check list (step, missing input, what closes it, who) and the weakest-part line written.
- [ ] (D, T) Re-review: every earlier finding mapped and its sequence re-traced or its retest log read; harm order walked around each fix; round 3 escalated.

Project overlay: if `knowledge/overlays/code-review.md` exists, read it after this file; it wins for this game.

## 7. Core principles for this craft
The studio's universal principles, written for code review. The master is `knowledge/reference/craft/riot/universal-principles.md`; where this section and the master seem to differ, the master wins and the difference is reported to the lead. Two principles are visual crafts I do not carry out: shape and silhouette (their code side, meaning never on one channel, is row 20) and pushing past real (its code side, the truth never exaggerated, is row 19).

| # | Principle for my work | Example (our pipeline) | Check |
| --- | --- | --- | --- |
| 1 | **Players first.** The harm order ranks by what players lose; code must never show a player a state the server did not confirm, and a threat's tell leaves the server when its wind-up starts, never with the damage | A sell handler plays the coin burst before `InvokeServer` returns; a denied sale still shows "+50"; a boss sends its slam tell in the same step as the damage, so on a slow connection the warning arrives with the hit | Each player path: what is shown equals the server's result (PT-01, PT-03); each threat's tell is sent before the wind-up wait, never beside the damage (PT-05, S11) |
| 2 | **Judge where players meet it.** A runtime claim holds only on the input that can prove it; static reading cannot prove timing, replication or phone cost | "The debounce works" is proven by a two-client run, not by reading the debounce | Every runtime claim names its input and label (`review-method.md` §1) |
| 3 | **Decide what is read first.** The verdict leads, the most harmful finding comes first, few findings; nothing small competes with a blocking finding | A Critical dupe followed by nine style notes buries the dupe: write the dupe and nothing below the bar | Findings in severity order; no style or taste items |
| 4 | **Big before small.** The whole change at the harm-area level first, then depth; owners, contracts and data flow before line details | In a 12-file shop change, pass 1 finds a second balance writer in `Inventory.luau` before any time goes into a tween | Candidates cover every changed file and all 8 areas before the first proof |
| 6 | **Less is more.** The smallest fix direction; over-building is a finding; no extra rounds, hardening or nits | A generic `EventBus` added for one signal: Medium over-building with the one-caller proof | Each fix direction touches the fewest lines; nothing asks for hardening the brief does not need |
| 7 | **One code for meaning.** Colours, motion values, cue ids and tiers live in shared data and mean one thing everywhere | Danger red typed in a VFX script and a different red in the HUD | S5 hits traced to the colour-role table (PT-14) |
| 8 | **Timing tells cause and effect.** In code the result follows its cause: outcome layers after confirmation, effects on named markers, one trigger for picture and sound | `task.wait(0.35)` before the impact burst instead of the `contact_confirmed` marker; after a retime the burst lands before the contact | PT-01, PT-13; every presentation delay traced to a marker or the timing list |
| 10 | **The change's purpose sets the weight.** What the feature does for players (buy, hatch, hit, save) decides which areas get the deepest look; all 8 are still walked | A cosmetic trail weighs per-viewer, cost and cosmetic physics; a shop weighs money and saves | The review names the feature's verb and the areas it weighed most |
| 11 | **One house way.** The change follows the game's existing patterns; a second way to do a solved thing drifts (V-18) | A feature creates its own RemoteEvent instead of registering in the transport module | For each new mechanism, the codebase searched for an existing owner |
| 12 | **Vary decoration, lock meaning.** Randomness only on decorative values | `FlipbookStartRandom = true` on a telegraph: the warning starts on a random frame | S4 hits and engine-side ranges classed decorative or semantic (PT-12) |
| 13 | **Intent before review.** Brief, invariants and failure cases come before the diff | A missing pending state is invisible in a diff and obvious against the screen contract's pending row | Goal questions written before pass 1 |
| 14 | **Other explanations before a verdict.** Look for the guard, the docs line or the type that makes a candidate safe; recommend one fix with its reason | A "missing rate limit" lives in the transport's per-method bucket: dropped | Each kept finding says what was checked to rule out the safe reading (V-14) |
| 15 | **Cheap stages first.** The plan before the code for deep changes; quick depth for small safe ones; later rounds see only the new diff | Reading a trade feature's invariant cards finds "no trade id" before 600 lines exist | Depth recorded; plan checks filed against the plan (`review-method.md` §7) |
| 16 | **Critique against the goal, one problem at a time.** Each finding names its rule, harm area, one problem and the smallest fix; re-review re-checks the problem, not the suggested change | A fix renamed the check but two requests in one frame still both pass: not fixed | Finding fields complete; each earlier sequence re-traced (V-17) |
| 17 | **Build for the next role and the engine.** The change gives the next role what it keys on (contract event names, data tables, the manifest) and uses engine features first | A hit event that lacks the `contact_confirmed` name the VFX and sound cues key to | Event names in code match the contract; EC-03 answer present for custom infrastructure |
| 18 | **Know when the review is done.** Depth sets the stop rule; done when every area is walked and every candidate proved or dropped; a round with nothing new ends the loop; round 3 escalates | A clean data change gets "no blocking findings" and a keep list (WE-3) | The hand-back states depth, areas walked, round number |
| 19 | **Feedback follows the real outcome.** The attempt cue plays at once; the big layer, counters and reveals follow the confirmed result and never claim more than it | A denied hatch still cracks the egg (WE-1 F4); a tween's `Completed` that grants the coins | PT-01 to PT-04; PT-18 (presentation never decides the outcome); a denied-request run or test, else not verified |
| 20 | **Every player can read it.** Meaning never on one channel; every intense channel has a reduced path that keeps the information; rates at most 3 Hz | A shake and FOV punch with no reduced branch; a low-health blink at 5 Hz | PT-09, PT-10, PT-15, PT-17 |

## 8. Framework games: bypass greps (J025)
In a game built on `roblox-game-framework` (blocks: `engineering-craft` → `references/framework.md`), run these greps from the game root on every review. They search `src/`, the game's own code; `Framework/`, `vendor/` and `Packages/` are copies checked by the lock. A hit is a V-18 finding (a second way to do a solved thing) unless `knowledge/design/game-profile.md` records the deviation; severity follows V-12 by what it bypasses (saves, money and remotes: High or Critical).

```sh
rg -n "DataStoreService|GetDataStore|ProcessReceipt|ProfileStore" src                                         # B1 saves outside Session
rg -n "RemoteEvent|RemoteFunction|UnreliableRemoteEvent|OnServerEvent|OnServerInvoke|InvokeClient" src -g "!**/Remotes.luau"   # B2 raw remotes outside Net
rg -n "Remotes\.[A-Za-z.]+\.On\(" src/server                                                                  # B3 every hit is the first argument of Net.on / Net.answer (or Admin.start's action)
rg -n "LoadAnimation" src                                                                                     # B4 tracks outside Anim
rg -n -i "zap|bytenet|warp|networker|rodux|reflex|fusion|vide|trove|maid|promise|goodsignal|lemonsignal|dataservice|profileservice|lapis" wally.toml   # B5 second library
python Framework/check_lock.py .                                                                              # B6 edited framework copy: must name no file
rg -n "require\(script|require\(game" src                                                                     # B7 in the framework repo only: Instance requires
rg -n "Config\.(number|string|json)\(" src/server                                                             # B8 read each key: no receipt price, no store name
rg -n "TweenInfo\.new|TweenService:Create" src                                                                # B9 tween literals outside Motion
rg -n "AnalyticsService" src                                                                                  # B10 analytics outside the block
```

| Id | Check | Allowed only in |
| --- | --- | --- |
| B1 | saved data, receipts or ProfileStore outside Session | nowhere in `src/` (Session and `vendor/ProfileStore` own them) |
| B2 | a raw remote outside Net | the generated `src/*/Remotes.luau` |
| B3 | a handler connected outside Net | as the `listen` argument of `Net.on` / `Net.answer`, or Admin's `action` |
| B4 | `LoadAnimation` outside Anim | nowhere (Anim loads once per Animator and clip) |
| B5 | a second transport, state, save, cleanup, signal or Promise library | none (`rules/packages.md` one per concern); Janitor's own typed-promise dependency is allowed |
| B6 | an edited, added or deleted file under `Framework/`, `vendor/`, `Framework-tools/` or the locked dev tools | none: fix in the framework repo, tag, install again |
| B7 | `script.Parent...` or `game:GetService(...)` requires in framework code | nowhere (`REQUIRES.md`; the framework gate's `rules` check fails them too) |
| B8 | a config key tied to money or saves | never (Config C5) |
| B9 | tween timing literals | the game's motion table through `Motion.play` |
| B10 | `AnalyticsService` direct | nowhere (Analytics block) |
| B11 | a content table without its spec | every `src/**/Content/<Name>.luau` has a sibling `<Name>.spec.luau` (ContentTests pattern step 6) |

- The greps find candidates; V-06 still applies: each hit needs its failure scenario (for example "this handler skips Net, so a NaN amount reaches the save") or it is dropped.
- The blocks are not reviewed again in a game review; a suspected framework bug is a ticket to the framework repo with the failing sequence.
