---
type: job
scope: universal
status: draft
updated: 2026-10-24
source: J023 research
supersedes: []
---
> Author: researcher (general-purpose) · claude-sonnet-5-5 · default · 2026-10-24

# J023 research: flow map of three job types (gameplay feature, UI screen, marketing art)

Goal (owner J023-D3, `knowledge/jobs/J023-flow-speed/decisions.md:17`): understand every step, who does it, what passes between agents, why it exists and what it protects. **No recommendation here.** Per step I note "what breaks if removed or merged" only with evidence, else "no evidence found".

## 0. How this was made, and limits

- Read: `orchestration/SKILL.md` (all), `references/job-types.md` (§4, §5, §7 and cross-type rules), `briefs-and-handoffs.md`, `gates-and-feedback.md`, `rules/company.md`, `rules/anti-overengineering.md`, the three scripts (`job-feature.js`, `job-ui-screen.js`, `job-marketing-art.js`, read in full), `.agents/workflows/jobs/README.md`, J016 `design.md` and `design-jobtypes.md`, J016 `design-context.md`, the capability record, J018 `g3-proposals.md` G3-P2 and G3-P3, the partner tables of the architect, feature-builder, sound-designer and ui-ux-designer role files, and `presentation-contract.md`.
- **Counts come from running the real scripts under a copy of the kit's own fake-agent harness** (`tools/workflows/wf_harness.mjs`, copied to the scratchpad and extended to log model, effort and a `plan` of planted findings; no kit file was changed). Each count is the number of `agent()` calls the script makes with fake hand-backs. Real agents may set flags differently: `crafts_not_needed`, `performance_risk`, `no_timed_actions`, `no_player_feedback`, `world_to_hud`, `hero_is_character`, `conflicts`. Base counts below fix `performance_risk=light` and all four crafts needed. The fake default would be `heavy`, which adds 1 run per review round.
- **No run data.** Searching `knowledge/` for `job-feature`, `job-ui-screen`, `job-marketing-art` finds only J016, J017, J018, J019 design and review files. No real job of these three types is on record. All "why" evidence below is design-time evidence (papers, Riot transcripts, tabletop audits, capability probes). No step has a measured defect-catch rate. The J016 design itself calls its round counts "pilot settings, not measured optima" (`DES:151`) and says no controlled study shows the hybrid beats the old process (`DES:208`).
- Not opened: the raw Riot transcripts R00-R13 and the owner papers P1/P2 (cited only through the J016 design files, which carry their line numbers).

### Evidence keys (path : line)
| Key | File |
| --- | --- |
| CAP | `knowledge/reference/studio/claude-code-capabilities.md`: K1 :49, K2 :50, K3 :51, K4 :52, K5 :53, K6 :54, K7 :55 |
| DES / DJT / DCX | `knowledge/jobs/J016-orchestration/` `design.md` / `design-jobtypes.md` / `design-context.md` (E5 :29, E7 :31, E8 :32, E9 :33, E10 :34, E12 :36) |
| JT / SK / BH / GF | `.agents/skills/orchestration/` `references/job-types.md` / `SKILL.md` / `references/briefs-and-handoffs.md` / `references/gates-and-feedback.md` |
| CO / AO / RD | `rules/company.md` / `rules/anti-overengineering.md` / `.agents/workflows/jobs/README.md` |
| G3P | `knowledge/jobs/J018-riot-craft/g3-proposals.md` (G3-P2 :74-96, G3-P3 :97-123) |
| PC | `.agents/skills/architecture/references/presentation-contract.md` |
| D23 | `knowledge/jobs/J023-flow-speed/decisions.md` (J023-D2 :16) |
| JF / JU / JM | `.agents/workflows/jobs/job-feature.js` / `job-ui-screen.js` / `job-marketing-art.js` |

Cell shorthand: `J/` = `knowledge/jobs/<job>/`. Model/effort: `o/h` Opus high, `o/m` Opus medium, `s/m` Sonnet medium. `∥` = runs in parallel with the same group; `→` = strictly after (a chain in one lane). `X` = conditional step. "Studio writer" = the one agent holding Studio.

---

## 1. Facts that hold for all three types

| Fact | Cite |
| --- | --- |
| Stages are one call each: `direction` → G1 → `proof` (L only) → G2 → `build` → G3; `repair` after G3. A workflow cannot pause, so the owner gates sit between calls. | `RD:10`, `SK:18`, `CO:56-69` |
| Gates: M = G1 + G3 (2). L = G1 + G2 + G3 (3). An extra gate only for scope, intent, rights, spend or release risk. | `CO:24-34` |
| M runs its proof inside the `build` call; `proof` refuses size M (feature, marketing). UI M runs only the contract inside `build` (no prototype). | `JF:64`, `JM:60`, `JU:67`, `JU:905-910` |
| Every `agent()` has role, model, effort and the hand-back schema; no peer ids, no messages: sideways work goes through files in a fixed order. | `RD:17`, `RD:12`, `CO:79` |
| At most 5 agents at once; one Studio driver; one Blender user; one built-in-browser user. | `RD:20`, `CO:135-136` |
| Image steps write prompts first and generate only with the browser and the owner's yes; a pending batch stops the stage as `blocked`. | `RD:11` |
| Review rounds: code findings 3 repair rounds, other findings 2, interface rounds 2, direction 1 proposal + 1 resolution. | `CO:130-132`, `AO:37-39` |
| Lead-side work outside any script: intake and job card, belief check (analyst, Sonnet medium, 0 or 1 run), image batches with the owner, gate packets, readiness, inbox drafts, close with a doc-keeper run (1) and `kb_index`. Not counted below. | `SK:13-14`, `SK:19`, `SK:82-91` |
| Artifact paths, hand-back fields (`coverage`, `checks`, `built_on`, `docs_read`, optional `lesson`) are the same in every call. | `JF:97-118` |

---

## 2. Job type A: gameplay feature (`job-feature`)

Job lead game-designer, technical lead architect (`JT:85`). Roles and effort: `JF:76-92`. Builder and reviewer go to high when `money` or a risk in {saves, remotes, trades, paid-random} is set (`JF:49,81-82`).

**Size note.** The script has no step that depends on M or L except where the proof runs and whether the owner sees G2. M and L make the **same 36 agent calls** (`DIR 8 + PROOF 15 + BUILD 13` for L; `8 + 28` for M).

### 2.1 Step table (M and L share every row; "P" rows run in the `proof` call for L and inside the `build` call for M)
| # | Stage | Who (role · model/effort · group) | Reads | Writes | Hands to | Why it exists (evidence) | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | D · D1 proposals | game-designer o/h ∥ architect o/h ∥ X progression-designer o/h (only `numbers`) | `J/job-card.md`, `game-profile.md`, `documents.md` §3 (`JF:310`). Must not open peers' files (`JF:308`) | `J/direction/proposal-<role>.md` | F2, F3 | Independent first ideas: upstream messages flipped 11.1 % of correct answers (K1, `CAP:49`; E7, `DCX:31`); stage D1 in `DES:104` | Merging into one agent loses the independence K1 measures (other task types). No feature-job measurement found |
| F2 | D · D2 exchange | same agents ∥ | the other leads' proposals (`JF:324`) | `J/exchange/r1-<role>.md` (conflicts that change production only) | F3 | One exchange, conflicts only (`DES:105`, `CO:60`) | Nothing measured. F3 also reads the proposals directly (`JF:336`), so an unlisted conflict is still visible to it |
| F3 | D · D3 synthesis | game-designer o/h | all proposals + exchange notes, `templates/jobs/direction-sheet.md` | `J/direction.md` rev 1 (behaviour in player words, options, risky claims + proof test, feedback stack, closed doors); sets `no_timed_actions`, `no_player_feedback` | F4, F5, lead (G1 packet) | One direction sheet, decisions recorded (`DES:106`, `CO:58`, `GF:46-53`) | No evidence found |
| F4 | D · consults | animator o/m ∥ sound-designer o/m; X each skipped when the flags above are set | `direction.md@rev`, `proposal-game-designer.md` (`JF:355`) | `J/direction/consult-<role>.md` (frame lengths + named markers; cue list per state change) | F5, F6, F10 | Animator and sound join at feature direction (`JT:86`; `G3P:80`, G3-P2 item 4); sounds hang on named events (`DJT:99`) | Their needs would first appear at F13, which already asks the animator for the timing list draft and sound for cue ids (`JF:453,455`). No evidence found of a defect only F4 catches |
| F5 | D · signatures | architect o/h ∥ X progression-designer o/h (the designer does not sign its own sheet; animator and sound do not sign) | `direction.md@rev` + consult notes | `J/direction/sign-<role>.md` | F6, lead | Others sign or name an incompatibility (`CO:58`) | No evidence found |
| F6 | D · X resolution | game-designer o/h; only if a sign says no or a consult lists a conflict (`JF:377`) | sheet + sign + consult notes | `direction.md` next rev | lead (G1) | The one resolution round (`CO:130`) | No evidence found |
| G1 | owner | — | behaviour in player words, risky claims, closed doors, scope, usage | — | — | `CO:30` | — |
| F10 | P · P1 contract | game-designer o/h | `direction.md`, `J/direction/*`, `contract-header.md`, `documents.md` §3-4, §6 | `J/contract-<feature>.md` rev 1: state model, stable event names, tuning keys, feedback stack with denial messages, acceptance checks (given/when/then, 5 paths); names crafts not needed and `no_visible_parts` | architect, builder, qa-lead, prog, UI, VFX, sound (`JF:406`) | Shared contract with stable ids and a Consumers table (`JT:88`, `SK:55`, E12 `DCX:36`); sounds hang on named events (`DJT:99`) | Every later step lists it as input (`JF:438,461,553,...`); no evidence found for a lighter form |
| F11 | P · X tier table | progression-designer o/h; only risk `rewards` (`JF:417`) | contract, direction | `J/progression/tier-table.md` + contract next rev | UI, VFX, sound, qa | Reward and celebration tiers before production (`JT:88`) | No evidence found |
| F12 | P · P1 trace table | qa-lead o/m | contract@rev, tiers, `player-facing.md` §3 | `J/qa/trace-table.md`: player-facing rows + the test hooks the builder must deliver | architect (copies hooks into plan), builder | Hooks delivered before any partner's first capture (`JT:143`; `G3P:100`, G3-P3 item 1) | Named captures need hooks `Reject`, `DelayMs` (`JT:151-152`): without the table the builder is not told to build them |
| F13 | P · P2 needs, round 1 | architect o/h ∥ X progression-designer o/h ∥ ui-ux-designer o/m ∥ chain **animator o/m → vfx-designer o/h → sound-designer o/m** (VFX reads the animator's note, sound reads both) | contract@rev, `direction.md`, trace table, tiers; chain: the earlier notes (`JF:458-473`) | `J/exchange/p1-<role>.md` (agree / conflict / missing per state, event, key) | F14, F15 | Owner decision: the crafts' joint needs step stays (D23, `D23:16`). One timing change cascades to animation, effects and sound (K4, `CAP:52`); I1-I3 (`DES:108`); `CO:60` | Locked by the owner (J023-D2). Defect evidence behind it: VFX and sound started on markers that did not exist yet (`G3P:87`) |
| F14 | P · X merge | game-designer o/h; only if any note holds a conflict or missing item | contract + notes | contract next rev + change-table row | F15 | Decision owner reconciles (`JT:89`, `CO:60`) | No evidence found |
| F15 | P · P2 presentation contract | architect o/h | contract, trace, all `p<r>` notes | `J/architect/presentation-contract.md`: one row per player-visible event (source, payload, runs on, per viewer, comfort, rate, information, truth, check seed) and the one marker list | builder, qa, UI, VFX, sound, animator | Where gameplay hands over to animation, VFX, sound, UI (`PC:5`; `JT:89`) | No evidence found for a lighter form; `PC:1` says it "connects the crafts' documents" |
| | | *Round 2 of F13 + F14 + F15 repeats the whole set (all needers again) only when round 1 had any conflict or missing item (`JF:478-505`).* | | | | | |
| F16 | P · P3 UI target image | ui-ux-designer o/m, browser | contract, direction, art bible | `content/ui/<f>/refs/` images or `image-prompts.md` | owner (G2, or mid-build for M), F36 | Visual work starts from an approved reference image (AGENTS.md §3.5; `JF:187`) | B4 and B5 return `blocked` with no approved image path (`JF:187`) |
| F17 | P · P3 VFX key frames | vfx-designer o/h, browser, runs after F16 (one browser user, `JF:512-533`) | contract, direction | `content/vfx/<f>/refs/` sheets | owner, F37 | same | same |
| F18 | P · P3 temp cues | sound-designer o/m; the prototype waits for it | presentation@rev, contract | `output/sound/<f>/temp/` + cue table | F19 | The skeleton plays temp cues so the play is judged with sound (`JT:90`; `G3P:81`) | No evidence found |
| F19 | P · P3 grey-box prototype | feature-builder o/m (o/h on code risk), Studio writer; ∥ F16-F17 images | contract, presentation, trace, direction, `proposal-architect.md`, temp cues | prototype in Studio (paths outside production source), `J/prototype/notes.md` | F20, F21, F30 | A playable prototype tests the risky claim and the fun (`JT:90`; `DJT:100`; K5 `CAP:53`) | Risky claims reach the real build untested (`DJT:100`). In M a pending image batch stops the stage here (`JF:564`) |
| F20 | P · P4 play | studio-operator s/m (Studio writer), rounds 0-2 | notes, contract, direction | `J/captures/proof-r<N>/` (stills, Output log) | F21 | Reviewers judge captures, never open Studio (`JF:597`); stills only (`RD:21`) | Reviewers have nothing to judge |
| F21 | P · PR proof review | game-designer o/h → architect o/h | captures, notes, contract, direction | `J/reviews/proof-r<N>-<role>.md` | lead (G2); F22 | Domain lead then architect (`CO:61`; `JT:90`); reviewers read-only (K2 `CAP:50`) | Recipe names only the game-designer (`JT:90`); the architect review is the company default (`CO:61`). No evidence found either way |
| F22 | P · X proof repair | makers (≤5 parallel) then feature-builder (prototype mode); then F20-F21 again; ≤2 rounds | review files, contract | fixed revisions | — | `CO:132` | — |
| G2 | owner (L only) | — | playable prototype, captures, UI target image, VFX key frames | — | — | `CO:31` | — |
| F30 | B · B1 plan | architect o/h | contract, presentation, trace, direction, prototype notes, proof reviews | `J/architect/plan.md`, `brief-feature-builder.md`, `test-seeds.md`; `performance_risk`, crafts needed | builder, qa, perf, UI, VFX, sound, prog | Plan before code, files owned per builder (`JT:91`, `CO:60`) | No evidence found |
| F31 | B · X plan check | reviewer o/m→h; only money or a code risk | plan, brief, presentation, contract | `J/reviews/plan-check-reviewer.md` | F32 | Money bugs were found only at merge (`G3P:111`, reviewer.md:17); `review-method.md` §7 :63 | Doc claim: money farms found late (`G3P:111`). Not measured on a real run |
| F32 | B · X plan answer | architect o/h; only if F31 has blocking findings | review file | plan next rev | F33 | The one plan-check exchange | — |
| F33 | B · B1 acceptance tests | qa-lead o/m | trace, contract, presentation, plan, `test-seeds.md` | protected acceptance tests (path in the plan) + trace table next rev | builder (runs, never edits), reviewer | Expected results come from the contract, not the code (`JT:91`, `JF:721`) | No evidence found |
| F34 | B · B2 skeleton | feature-builder o/m→h, Studio writer | brief, plan, contract, presentation, tests | source files + tests; every event fired with stand-ins | F35-F39 | Failing case first (`AGENTS.md` §4; `JT:91`) | Everything after it keys from its event ids |
| F35 | B · B3 tables | progression-designer o/h; only `numbers`; ∥ F36 ∥ F37→F38 | contract, plan, direction | `content/progression/<f>/` + traces | builder, UI | `JT:91` | No evidence found |
| F36 | B · B4 UI | ui-ux-designer o/m; only if UI needed | contract, presentation, plan, tiers, target image | `content/ui/<f>/spec.md` with Figma node ids and handoff | builder | `JT:91` | No evidence found |
| F37 | B · B5 VFX | vfx-designer o/h; only if VFX needed | contract, presentation, plan, tiers, key frames | `content/vfx/<f>/` frame scripts + `spec.json` (writes each envelope first) | F38, builder | VFX writes the envelope, sound answers (`RD:12`; TT-06 in the J016 audit) | No evidence found |
| F38 | B · B6 sound | sound-designer o/m (after F37); only if sound needed | contract, presentation, plan, `content/vfx/<f>/` | `output/sound/<f>/` cue cards keyed to event ids | builder | same | same |
| F39 | B · B7 integration | feature-builder o/m→h, Studio writer | brief, plan, contract, presentation, trace + tables, UI spec, VFX spec, sound cards | hooks + debug log, wiring, analytics events, `J/evidence.md` (candidate revision, protected list); worst-case pass; gate PASS; freeze | review chain | One integrator, one frozen candidate (`CO:16`, `CO:64`) | The gate result is the entry rule of the chain (`JF:834`) |
| F40 | B · RV capture | studio-operator s/m, Studio writer; ∥ F41 ∥ F42 | `evidence.md`, contract, `job-types.md` named captures | `J/captures/<tag>/`: acceptance cases, slow confirmation, two-client, grayscale + sound off + reduced motion, real rate + burst, lowest graphics; X rejected request (money or `server-result`); X event set | F43-F47 | Named captures, one Studio user (`JT:146-160`, `CO:135`) | Creative reviewers judge captures only |
| F41 | B · RV code review | reviewer o/m→h, ∥ F40 | code, tests, plan; runs the gate itself first | `J/reviews/<tag>-reviewer.md` | makers | Every candidate with code gets the reviewer (`CO:100`, J016-LD15) | Rule: no code ships unreviewed |
| F42 | B · RV architect | architect o/h, ∥ F40 | candidate vs plan, presentation, budgets | review file | makers | `JT:93` | No evidence found |
| F43 | B · RV qa-lead | qa-lead o/m, after F40 | protected acceptance suite, scenarios, planted-fault check | review file + owner result card | makers | `JT:93`; planted faults prove the suite can fail | — |
| F44 | B · X RV performance | performance-engineer o/h, after F43; only if the plan says `heavy` | plan peak case | review file | makers | `JT:93` | — |
| F45 | B · RV design validation | game-designer o/h, after F40 | captures incl. named captures | review file | makers | Play wins; incentives checked (`JT:93`) | — |
| F46 | B · RV art | art-director o/m, after F45; only if visible parts | captures | review file | makers | `JT:93` | — |
| F47 | B · X RV live-ops | live-ops-designer o/m, after F46; only risk `event` | event capture set | review file | makers | event review (`JT:123`; J019-LD1) | — |
| F48 | B · X repair round | non-builder makers in parallel (≤5), then feature-builder; then a **full re-run of F40-F47** | review files, contract, `evidence.md` | new revisions | review chain | Code 3 rounds, other 2 (`AO:39`, `CO:132`) | Rounds past 3 on one approach return to the architect (`JT:94`). Anthropic: first-round passes 65 → 78 %, 5+ round changes 8.9 → 1.5 %, 59 % of repeat findings were about old code (`AO:39`, source `AO:2`) |
| G3 | owner | — | game-camera captures, checks with labels, could-not-check list, owner-confirmed lines | — | — | `CO:32`, `GF:19` | — |
| R | repair stage | game-designer o/h (R1 scope) → affected makers ∥ → feature-builder → review chain F40-F47 | owner's G3 change | scope file; changed revisions | — | `JF:913-957` | — |

### 2.2 Counts (verified by harness)
| Case | Direction | Proof | Build | Total |
| --- | --- | --- | --- | --- |
| L, base (4 crafts, light perf, `[]` risks) | 8 | 15 | 13 | **36** |
| M, same | 8 | — (inside build) | 28 | **36** |
| Lean: no UI, VFX, sound, animator, no visible parts (contract says so) | 6 | 8 | 9 | 23 |
| Flag `numbers` | +3 | +1 | +1 | +5 |
| `money` or `saves`/`remotes`/`trades`/`paid-random` | 0 | 0 | +1 plan check (+1 architect answer if blocked) | +1 |
| `server-result` | 0 | 0 | 0 (adds a named capture inside F40) | 0 |
| `rewards` | 0 | +1 tier table | 0 | +1 |
| `event` | 0 | 0 | +1 per review round | +1 |
| `performance_risk=heavy` (from the plan) | 0 | 0 | +1 per review round | +1 |
| All flags on, minimum | 11 | 17 | 16 | 44 |

Maximums (all repair rounds), harness runs with planted findings:
- Interface round 2 + merge: +7 (+1 more if round 2 also has a conflict). Direction resolution: +1.
- **Single-maker path** (only feature-builder findings, every loop used: proof 2 repairs, code review 3 repairs): **74** runs (L: 9 + 31 + 34; M: 9 + 65).
- **Ceiling** (every maker has a finding, staggered so the loops run longest: 2 rounds of non-code findings, then 3 rounds of code findings = 6 review rounds, 5 repair rounds, `JF:842,897-904`): **122** with base flags, **140** with all flags and heavy perf.
- Role mix, L base: architect 8, game-designer 6, sound-designer 4, qa-lead 3, ui-ux-designer 3, vfx-designer 3, feature-builder 3, animator 2, studio-operator 2 (Sonnet), reviewer 1, art-director 1. 34 Opus + 2 Sonnet.
- Critical path (sequential agent slots, not wall time): L = 25 (5 + 11 + 9); M = 25 (5 + 20).
- Owner gates: M 2 (G1, G3), L 3. **Plus one hidden stop in M with visible UI or VFX:** `build` returns `blocked` for missing `args.images` after the 15-agent proof and the plan (16 runs, harness: M build with no images), so the lead must run the image batch with the owner and call build again (`JF:714-716`, `JF:564`). Inferred from code and confirmed by the harness; not seen in a real run.
- Exchange rounds: direction exchange 1 (+ resolution ≤ 1); consult 1; interface rounds 1-2 (each: needs notes, merge if open, presentation); plan-check exchange 1 on code risks.

---

## 3. Job type B: UI screen (`job-ui-screen`)

Job lead ui-ux-designer; the game-designer owns the player's decision (`JT:71`). Roles: `JU:79-92`. UI is high for L-with-newLook or `shop` (`JU:80`); builder and reviewer high for `shop` or `paid-random`.

### 3.1 Step table
| # | Stage | Who (role · model/effort · group) | Reads | Writes | Hands to | Why it exists (evidence) | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 | D · D1 proposals | game-designer o/h → **then** ui-ux-designer o/h (L) or o/m (M); ∥ art-director o/m ∥ feature-builder o/m→h ∥ X progression-designer o/h (shop, shop-screen, paid-random) | job card, `screen-contract.md`; the UI lead reads the designer's `information-list.md` (the one exception to independence, `JU:292,324-331`) | `J/direction/proposal-<role>.md`; designer also writes `information-list.md`; UI lead writes state list, focus map, flow sheet, 2-3 wireframes, grey value pass, 2-3 target images (browser) in `content/ui/<id>/refs/` | U2, U3 | UX flow before UI, function before polish (`DJT:84`, R00:4573-4599; `JT:72`); K1 `CAP:49` | The order design → UI is a rule (`JT:72`). No evidence found for the cost of the 2-3 target images at D1 |
| U2 | D · D2 exchange | all D1 leads ∥ | other leads' proposals | `J/exchange/r1-<role>.md` | U3 | `DES:105` | No evidence found |
| U3 | D · D3 synthesis | ui-ux-designer o/h (L) | proposals, information list, exchange notes | `J/direction.md` rev 1 (decision record, flow, wireframe pick, style targets, failed options, File owners section) | U4 | `DES:106`; `GF:46-53` | No evidence found |
| U4 | D · signatures | game-designer o/h ∥ art-director o/m ∥ feature-builder o/m ∥ X progression-designer | `direction.md@rev` | `J/direction/sign-<role>.md` | lead | `CO:58` | No evidence found |
| U5 | D · X resolution | ui-ux-designer; only if a sign says no (consults do not exist here) | sign files | direction next rev | lead | `CO:130` | — |
| G1 | owner | — | decision record, flow, wireframes, grey value pass, 2-3 style targets, recommendation | — | — | `CO:30` | — |
| U10 | P(L)/B(M) · C1 contract | ui-ux-designer o/h→m | direction | `content/ui/<id>/spec.md` rev 1 (state map, events, data fields, sizes, readiness list) | all needers | State map + spec (`JT:74`; `DJT:86`) | A state or readability failure returns here, not to styling (`JT:80`) |
| U11 | C2 needs, round 1 | feature-builder o/m ∥ game-designer o/h ∥ X progression-designer ∥ chain **vfx-designer → sound-designer** | spec@rev (+ vfx note for sound) | `J/exchange/c1-<role>.md` | U12, U13 | Consumers state needs before the producer builds (`JT:137`; `CO:60`); D23 | Locked by J023-D2 for crafts' needs. Sound and VFX on one event must agree (`JU:425`) |
| U12 | C2 X merge | ui-ux-designer; only if open items; round 2 repeats all needers (`JU:439-449`) | notes | spec next rev | U13 | `CO:60` | No evidence found |
| U13 | C3 code file owners | architect o/h | direction (File owners section), spec | `J/contract-code.md` (one row per builder, remotes and validation) | builder, reviewer, qa | Code file owners set by the architect (J016-LD10; `JT:74`) | A builder with an empty row returns `blocked` (`RD:19`) |
| U14 | X plan check | reviewer o/h; only `shop` or `paid-random`; then X ui-ux-designer and/or architect fix (one exchange) | code contract, spec | `J/reviews/plan-check-reviewer.md` | U15 | Code risks caught before the builder starts (`JT:75`; `G3P:111`) | Doc claim only |
| U15 | B0 storyboard | ui-ux-designer o/h → X vfx-designer (only `world_to_hud`) → sound-designer o/m (chain) | spec, direction, information list | `content/ui/<id>/motion/storyboard.md`, `J/exchange/storyboard-*.md` | U16 / U20 | One beat list for press, VFX, sound (`JT:75-76`; J019-LD2) | In L, G2 freezes these beats (J019-LD2). No evidence found of what is lost if sound reads the spec instead |
| U16 | P1 prototype (L only) | ui-ux-designer o/h | spec, direction, target image, beat list | Figma prototype, `figma-ids.json`, one screenshot per state | U17 | Clickable prototype of every state at phone size (`JT:75`; `DJT:87`) | G2 would have nothing playable (`CO:31`) |
| U17 | PR proof review (L only) | game-designer o/h → art-director o/m → feature-builder o/m, sequential; rounds 0-2 | prototype, screenshots | `J/reviews/prototype-rev<N>-<role>.md` | makers; lead (G2) | Decision clear → look → buildable (`JT:75`) | — |
| U18 | X proof repair | ui-ux-designer (+ progression-designer); ≤2 rounds | findings | fixed Figma/spec | U17 | `CO:132` | — |
| G2 | owner (L only) | — | clickable prototype; motion feel at normal speed on it | — | — | `CO:31`, `JT:75` | — |
| U20 | B1 Figma build + handoff | ui-ux-designer o/h→m | spec, direction, target image, beat list, prototype (L) | Figma screens, `export/`, handoff layer table, merged beat list | U21 | Build to the owner-chosen target image (`JT:76`) | Returns `blocked` if icons or item art are still prompt rows (`JU:684`) |
| U21 | B2 implement | feature-builder o/m→h, Studio writer ∥ lane [vfx-designer o/m→h → sound-designer o/m] | handoff, spec, code contract | code, tests, hooks, one capture per state; `content/vfx/<id>-ui/`; `output/sound/<id>-ui/` | U22 | Handoff checked by the receiver; effects and sounds off the VFX library (`JT:76`) | — |
| U22 | B5 integrate | feature-builder | all of the above | wired candidate + `J/evidence.md` | U23 | One integrator; hooks before captures (`JT:77`, `JT:143`) | — |
| U23 | CR code review | reviewer o/m→h; loop: rounds 0-3 | candidate, gate | `J/reviews/<tag>-reviewer.md` | fixers (ui, builder, sound, vfx, prog) | Gate PASS + reviewer first (`JT:79`); rule 20 (`AO:39`) | — |
| U24 | B6 capture | studio-operator s/m, Studio writer | evidence, spec | `J/captures/`: Device Simulator stills (smallest phone, PC), busiest-gameplay shot, press frame folders, X paid-reveal tiers, X rejected request, reduced motion, largest text, grayscale | U25 | S-33 capture rules (`JT:78`) | Reviewers judge captures only |
| U25 | RV chain | qa-lead o/m ∥ (ui-ux-designer o/h → X progression-designer → art-director o/m → game-designer o/h → X live-ops-designer); rounds 0-2; in rounds ≥ 1 a reviewer recheck runs first | captures, spec, target image | review files | fixers; lead (G3) | Review order in `JT:79`; K2 `CAP:50` | — |
| U26 | X repair round | ui-ux-designer first, then sound/vfx/prog parallel, then feature-builder (fix + integrate + refreeze), then **recapture (U24) and a full re-run of U25** | findings | new revisions | — | `CO:132` | — |
| G3 | owner | — | Studio build; motion feel; two listens | — | — | `CO:32` | — |
| R | repair | ui-ux-designer (R1 scope) → game-designer, ui (in order) → sound/vfx/prog ∥ → feature-builder → code review + capture + chain | owner's G3 change | scope file; revisions | — | `JU:860-896` | — |

M differs from L: U10-U15 and U20-U25 run inside `build`; **no U16, U17, U18, no G2** (`JU:905-910`).

### 3.2 Counts (verified by harness)
| Case | L: dir / proof / build / total | M: dir / build / total |
| --- | --- | --- |
| Base | 12 / 12 / 11 = **35** | 12 / 19 = **31** |
| `shop` or `paid-random` | 15 / 14 / 12 = 41 | 15 / 22 = 37 (+3 dir, +1 needs, +1 plan check, +1 progression review) |
| `shop-screen` | 15 / 13 / 12 = 40 | 15 / 21 = 36 |
| `server-result` | 35 (adds a rejected-request capture inside U24) | 31 |
| `event` | +1 per review round | same |
| `world_to_hud` (set by the storyboard) | +1 | +1 |
| `newLook` | 0 runs; UI and VFX effort go high; forces L | refused for M |
| All on (shop, paid-random, server-result, shop-screen, event, world_to_hud) | 15 / 15 / 13 = 43 | 15 / 24 = 39 |

Maximums: single-maker path (proof ui-only 2 repairs, code review builder-only 3 repairs, chain ui-only 2 repairs, both interface rounds, direction resolution): **L 72** (13 + 26 + 33), **M 60** (13 + 47). Ceiling, every fixer in every round: **L 86** (13 + 27 + 46), **M 74** (13 + 61) with base flags; **L 105**, **M 91** with all flags.
Critical path: L = 24 (5 + 10 + 9, +1 with a plan check), M = 20 (5 + 15).
Role mix, L base: ui-ux-designer 8, feature-builder 7, game-designer 6, art-director 5, sound-designer 3, vfx-designer 2, architect 1, reviewer 1, studio-operator 1, qa-lead 1.
Exchange rounds: D2 1 (+ resolution ≤ 1); needs rounds 1-2 (+ merge); plan-check exchange 1 (`shop`/`paid-random`); storyboard chain 1.

---

## 4. Job type C: marketing art (`job-marketing-art`)

Job lead marketing (`JT:112`). No Studio driver (`JM:26`). Roles: `JM:99-111`. `launch=true` puts marketing on high effort (0 extra runs, `JM:100`).

### 4.1 Step table
| # | Stage | Who | Reads | Writes | Hands to | Why it exists (evidence) | What breaks if removed or merged |
| --- | --- | --- | --- | --- | --- | --- | --- |
| M1 | D · D1 proposals | marketing o/m→h ∥ game-designer o/h ∥ art-director o/m ∥ X trend-scout s/m (arg `trends`); no image is made here | job card, `promise-ledger.md`, `art-bible.md`, `image-pipeline.md` §1 | `J/direction/proposal-<role>.md` (trend: `J/trend-scout/`); marketing lists slot sizes not measured | M2 | Hook, truth to play, style/identity as separate views (`JT:113`; `DJT:122`); K1 `CAP:49` | If marketing lists an unmeasured slot size the stage returns `needs-decision` (`JM:324-327`): a stop |
| M2 | D · D2 exchange | the same leads ∥ X animator o/m (hero pose, only `hero_is_character`, Blender) | other proposals; pose reads marketing's proposal | `J/exchange/r1-<role>.md`; `J/pose/` | M3 | Animator consulted when a character is the hero (`JT:113`) | Roughs would pose the hero from anchors only (`JM:334`) |
| M3 | D · D3 direction + roughs | marketing o/m→h, browser (the only image maker) | proposals, notes, pose, `thumbnail-brief.md`, `image-pipeline.md` §1 | `J/direction.md` rev 1: labelled warm-up, 3-5 roughs from different hooks with real-size sheets, colour/grey/black-fill, crop plan, failed roughs, closed doors; `J/marketing/` | M4 | G1 shows 3-5 roughs (`JT:114`; `DJT:123`, R05:144-176) | No evidence found |
| M4 | D · signatures | art-director o/m ∥ game-designer o/h (trend-scout does not sign) | `direction.md@rev`, `J/marketing/` | `J/direction/sign-<role>.md` | lead | `CO:58` | No evidence found |
| M5 | D · X resolution | marketing | sign files | direction next rev | lead | `CO:130` | — |
| G1 | owner | — | warm-up + 3-5 roughs at real slot size, recommendation | — | — | `CO:30` (3-5 roughs) | — |
| M10 | P(L)/B(M) · P1 value study | marketing o/m (edit tools only) | direction, decisions, `J/marketing/` | `J/marketing/greenlight/` silhouette + 3-value study; `campaign.md` closed doors | M11 | Cheapest pass first, grey (`JT:115`; cross-type rule `JT:139`) | No evidence found |
| M11 | P2 green light | marketing, browser | value study, direction | 2-3 light set-ups, green-light image, thumb_check sheet, real-layout mock, crop safe squares, `greenlight.md` (frozen big shapes) | M12 | After green light the big shapes stop moving (`DJT:124`, R08:656-712) | — |
| M12 | PR green-light review | art-director o/m → game-designer o/h, sequential; rounds 0-2; repair by marketing | `greenlight/`, art bible, promise ledger | `J/reviews/greenlight-r<N>-<role>.md` | lead (G2) | Default proof reviewers `CO:61`; recipe names none (`JT:115`) | — |
| G2 | owner (L only) | — | green-lit image at real size and layout | — | — | `CO:31` | — |
| M20 | B · B1 render | marketing, browser; X staged render by environment-designer o/h or modeler o/h (Blender) | green light | `J/marketing/render/` | M21 | Three render routes (`JM:553-587`; J012-D7) | — |
| M21 | B1 colour | marketing | render | `J/marketing/colour/` | M22 | render → colour → polish (`JT:116`; `DJT:125`) | — |
| M22 | B2 polish | marketing | colour | `J/marketing/final/` | M23 | same | — |
| M23 | B3 layered file | marketing | final | layered source file | M24 | Layers so crops re-lay without repainting (`JT:116`) | — |
| M24 | B4 crop family | marketing | final | `J/marketing/final/crops/` each with sheet, mock, checklist | M25 | Crop family planned at the start (`JT:116`) | — |
| M25 | RV scripts | **marketing o/m (an agent, not a script)** | candidate files | `J/evidence.md` + `J/marketing/checks/` | M26 | Scripts first (`JT:118`, `JT:14`) | Format FAIL stops the creative reviews (`JM:445`) |
| M26 | RV creative | art-director o/m → game-designer o/h → X live-ops-designer o/m; rounds 0-2; repair by marketing and renderers | images, mocks, art bible, ledger | review files | M27 | `JT:118`; K2 `CAP:50` | — |
| M27 | B6 owner package | marketing | evidence, reviews, final | `J/marketing/owner-package.md` (recommendation, rollback, owner actions) | lead (G3) | Owner does every external action (`JM:291`) | Not in the recipe; added by the script |
| G3 | owner | — | owner package | — | — | `CO:32` | — |
| R | repair | marketing (R1 scope) → X renderers → marketing → review chain M25-M27 | owner's change | revisions | — | `JM:685-718` | — |

### 4.2 Counts (verified by harness)
| Case | L: dir / proof / build / total | M: dir / build / total |
| --- | --- | --- |
| Base | 9 / 4 / 9 = **22** | 9 / 13 = **22** |
| `trends` | +2 (proposal, exchange) | +2 |
| `hero_is_character` | +1 (animator pose) | +1 |
| `event` | +1 per review round | same |
| staged render | +1 (+1 per repair round that routes to a renderer) | same |
| `launch` | 0 runs (effort only) | 0 |
| All on | 12 / 4 / 11 = 27 | 12 / 15 = 27 |

Maximums: single-maker path (marketing fixes only, both loops used, resolution used): **37** for L and M. Ceiling (renderers in every round too): **39** base, **46** with all options.
Marketing makes 12 of the 22 base runs. All 22 are Opus except an optional trend-scout. Critical path: 17 (L: 4 + 4 + 9; M: 4 + 13). Exchange rounds: D2 1 (+ resolution ≤ 1); hero-pose consult 1; **no needs round** and no interface rounds.
Owner gates: M 2, L 3. Extra stop: unmeasured slot size (`needs-decision`), image batches (the whole job is image batches).

---

## 5. Plain-English walk-through: one L gameplay feature, request to G3

You ask for a feature, for example "a daily reward chest". The lead (one chat) copies your words into a job card, sizes the job L because it needs screens, effects and sound, and checks the game profile. The game designer and the architect write their ideas apart from each other, then read each other's note once and list only the clashes. The designer writes one direction sheet, the animator and sound designer check that it is possible, and the architect signs; you see this at G1 as the behaviour in plain words, the risky parts and the cost. After your yes, the designer writes the contract (every state, every event name, the numbers' names and the tests) and a QA lead lists what each player must see and hear. Then the architect, UI designer, animator, VFX artist and sound designer each say what they need from the others, and the architect merges this into one "presentation contract". Next a builder makes a rough grey-box version in Studio, the UI and VFX designers make target pictures, sound makes placeholder cues, and a Sonnet operator plays it; the designer and the architect judge it, and you see it at G2. After your second yes, the architect writes the build plan, QA writes protected tests, and the builder builds the real logic first. UI, VFX and sound then build their parts, and the builder wires everything together and runs the gate. One frozen build goes to reviewers (code, cost and contract, QA tests, designer play-through, art), and each problem goes back to its maker, up to three rounds for code and two for the rest. The lead checks that every claim has evidence, shows you the real result in Studio at G3, and after your yes files the job into the knowledge base. A clean run is about 36 agent runs in a chain of about 25 steps in a row.

---

## 6. Where the hand-run recipe and the saved script differ

| # | Topic | Hand-run (recipe / rules) | Saved script | Cite |
| --- | --- | --- | --- | --- |
| 1 | Messages and repairs | Crafts on one interface may use `SendMessage`; repairs resume the maker by id and keep its context. | No ids, no messages; repairs are fresh calls that re-read the files. A resumed agent re-sends its whole context (105 k tokens for a small probe, J016 pilot R6). | `CO:76-79`, `SK:66`, `RD:12`, `rules/assistants/claude.md` Peer message row |
| 2 | Size M, feature | "M jobs skip proof (it runs inside build)", shown at G3. | The full proof (15 runs, 2 reviews, play) runs inside `build`: M = L in runs; M with UI/VFX stops once for images. | `JT:5`, `JF:960-973`, `JF:714` |
| 3 | Prototype vs skeleton, feature | One builder step: "feature-builder skeleton (…the G2 proof for L)". | Two builder builds: a grey-box prototype outside production source (F19), then a production skeleton from "what the plan keeps" (F34). | `JT:90-91`, `JF:549,733` |
| 4 | Animator and sound at feature direction | Listed as consulted direction leads. | Run after the draft as consults, do not sign, and are asked again for the same facts in the needs round. | `JT:86`, `JF:344-362`, `JF:453-455` |
| 5 | Feature proof reviewers | Game-designer judges the play. | Game-designer, then architect (company default). | `JT:90`, `JF:568-571`, `CO:61` |
| 6 | Review order, feature | gate → reviewer ∥ qa ∥ perf ∥ architect → game-designer → art. | Capture, reviewer, architect start together; qa and perf wait for the capture; game-designer and art wait for it and run in a row. | `JT:93`, `JF:875-886` |
| 7 | Selective recheck | "Only the failed layer and what depends on it" is rechecked. | Every review round re-runs every reviewer (feature F40-F47; UI U25 plus a reviewer recheck; marketing M25-M26). Only the brief text narrows later rounds ("review the new revision's changes"). | `CO:108`, `SK:20`, `JF:842-889`, `JU:810-856`, `JM:426-499` |
| 8 | UI review order | gate PASS + reviewer → qa → ui → prog → art → game-designer. | A separate code-review loop (3 repairs) before any capture; then chain with qa beside the creative order; a reviewer recheck leads rounds ≥ 1. | `JT:79`, `JU:743-749,772-793,822-828` |
| 9 | UI direction lead | "feature-builder or architect". | feature-builder at D1; architect only at C3. | `JT:72`, `JU:305,452` |
| 10 | UI size M | Proof is "L only". README says M runs the proof inside build. | UI M builds the contract, storyboard and Figma build; it has no prototype and no proof review. | `JT:75`, `RD:22`, `JU:905-910` |
| 11 | Marketing "scripts first" | `thumb_check.py` and `look_check.py` run first (tools). | An Opus agent (marketing) runs them each review round; the green-light review has no scripts step. | `JT:118`, `JM:431-444,537-539` |
| 12 | Marketing owner package | Not a recipe row. | One extra Opus run after a clean chain. | `JT:117-119`, `JM:667-681` |
| 13 | Risks | The lead fills the card's Risks row and updates it. | Exact tokens in `args.risks`; a missing or unknown token is `blocked`. Rows not named are skipped and listed in `skipped_slots`. | `JT:15`, `RD:36`, `JF:246` |
| 14 | Owner stops | Lead can interleave questions. | Cannot pause: image batches, unmeasured slots, `needs-decision` end the call. | `RD:10-11`, `JM:326` |
| 15 | Spawning | The lead's chat spawns every craft; scouts at depth 2. | Agents inside a workflow spawn no scouts. | `CO:95` |
| 16 | Work outside the script | Belief-check analyst, prerequisites, image batches, readiness, close (doc-keeper). | None of these is a script step. | `SK:14,19,82-91` |
| 17 | Fresh session per stage | The lead should run each stage from a fresh session. | n/a | `SK:19`, `rules/assistants/claude.md` Session size |

---

## 7. The needs and interface steps in detail

### 7.1 Feature (what each role reads, writes and hands over)
| Role | At direction | At the needs round (P2, `JF:449-456`) | At build |
| --- | --- | --- | --- |
| game-designer | D1 spec in player words, feedback stack, acceptance cases on 5 paths; D3 sheet; sets `no_timed_actions` and `no_player_feedback` (`JF:298-299,334`) | writes the contract first (F10), says which crafts are not needed (`JF:401`); merges open items (F14) | RV design validation (F45) |
| architect | D1 engine features, risky claims, probes, placement, file owners (`JF:300-301`); signs | Asked "can each behaviour be built where the plan will place it, does every event carry what consumers need?" Then merges all notes into the presentation contract (F15, `JF:492-505`) | plan + builder brief + test seeds (F30); answers the plan check; RV cost review (F42) |
| animator | consult: frame lengths and named markers per timing stage (`JF:346`) | first of the chain: timing list draft, frame lengths, named markers (`JF:453`); no clips are keyed in this job (`JF:90`) | none |
| vfx-designer | none | second in the chain: importance per viewer, caps, per-viewer and reduced variants, budget block per event, envelope on the animator's markers (`JF:454`) | key frames in the proof (F17); frame scripts + `spec.json` (F37), writing each envelope first |
| sound-designer | consult: cue list per state change or the reason for none (`JF:350`) | third: cue ids, voice cap, merge needs per event, and an answer to the VFX envelope (onset against peak) (`JF:455`) | temp cues (F18); final cue cards keyed to the VFX frame scripts (F38) |
| ui-ux-designer | none | states, denial reasons and messages, motion-table rows (`JF:452`) | target image (F16); spec + Figma + handoff (F36) |
| progression-designer | D1 numbers, tuning keys (only `numbers`) | tuning keys and the values players feel (`JF:451`) | tier table (F11); tables (F35) |
| qa-lead | none | writes the trace table before the round, so the architect copies its hooks (F12) | protected acceptance tests before code (F33); suite + planted faults in review (F43) |
| feature-builder | none (no needs note) | none; its partner table asks the architect for owned files and interface, and the others for specs "at the wiring step" (`feature-builder.md:41-52`) | prototype (F19), skeleton (F34), integration (F39), repairs (F48) |

Mechanics: the animator, vfx and sound notes run strictly in that order inside one lane (`JF:466-473`); architect, progression and UI notes run beside that lane. Each note is agree / conflict / missing. Round 2 runs only if round 1 had any conflict or missing item and re-runs **all** needers and the presentation contract (`JF:478-505`). The role files list more asks than the script implements (for example sound asks the architect for the contract rows to key to, `sound-designer.md:44-52`): in the script that exchange goes through the single `p<r>-<role>.md` note and the presentation contract.

### 7.2 UI screen
- **Order of leads at D1:** game-designer writes the information list and read rank first, then the UI lead builds the flow on it (`JU:324-331`); art-director and feature-builder write beside them.
- **C2 needs (`JU:410-433`):** feature-builder ("every data field, event and remote can be built and validated"), game-designer ("the states cover every action, failure and recovery"), sound ("which events need a UI sound, what each must say"), vfx ("which events need a UI effect from the library, and the screen budget"), progression (shop only: "every shown price, quantity, odd and limit maps to a field"). VFX writes first, sound answers on that note; the UI lead merges.
- **C3 (`JU:451-464`):** the architect writes `contract-code.md` after the needs rounds, from the builder's proposed file list.
- **Storyboard (`JU:470-506`):** UI beat list → X VFX world-to-HUD beats → sound cue list, one chain. In L it runs before the prototype so G2 freezes it.
- **Production (`JU:691-725`):** builder implements while the VFX → sound lane works from the handoff. The builder hands nothing sideways; the UI lead's handoff (layer table, 9-slice, live text fields, motion records) is its only input from the UI side.

### 7.3 Marketing art
There is **no needs round and no contract**. The interfaces are: marketing's crop plan and closed doors in `direction.md`/`campaign.md`; the animator's key pose (only when the hero is a character); the game-designer's promise-ledger claim ids; and the art-director's anchors, all consumed by marketing alone. Renderers (environment-designer, modeler) are used only when a staged Blender render is chosen (`JM:569-587`).

---

## 8. Three most surprising facts

1. **Size does not change the work in two of the three types.** Feature M and L make the same 36 calls; marketing M and L make the same 22; only G2 and the place of the proof differ (`JF:960-973`, `JM:721-733`). UI M saves 4 runs (no prototype, no proof reviews).
2. **Reviews are not selective in any script.** All three re-run every reviewer each round, although the rules say "only the failed layer and what depends on it" (`CO:108`, `SK:20`; scripts at `JF:842-889`, `JU:810-856`, `JM:426-499`). Marketing's "scripts first" step is an Opus agent run each round (`JM:433`).
3. **The same facts are asked twice, and the builder builds twice.** The feature animator and sound designer are asked for timings and cue ids at D3 consults and again at the P2 needs round (`JF:346,350` vs `JF:453,455`); the feature-builder builds a grey-box prototype and then a production skeleton (`JF:549,733`).

## 9. Could not map or verify

- No real-run data (tokens, wall time, defects per step): none on record for these three types.
- Counts depend on hand-back flags; real agents may drop crafts (`crafts_not_needed`), set `heavy`, or raise conflicts, which moves the totals between the minimums and maximums above.
- I did not read the full role files, the `templates/jobs/*` files, or `testing` and `engineering-craft` references beyond the cited lines, so the exact content of each hand-back beyond the brief text in the scripts is not mapped.
- Raw Riot and paper evidence is cited only as the J016 design files cite it.
