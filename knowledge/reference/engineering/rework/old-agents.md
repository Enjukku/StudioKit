---
type: reference
scope: universal
status: draft
updated: 2026-10-21
source: J010 rework study; DestructionSimulator old engineering agents, skills and rules (HEAD 12a1e82b4, 2026-10-20), part R half 2
supersedes: []
---
> Author: rework-extractor · claude-sonnet-5-5 · high · 2026-10-21

# Rework study part R, half 2: the old engineering agents as a baseline

Purpose. The owner wants to keep what worked and fix what did not, without assuming the old agents were bad. This file lists, one line per rule, what the five old agents and the skills and rules they load told them to do, and what the rework evidence says about each rule. I did not edit or copy whole texts; every rule below is a paraphrase.

## 0. How to read this file

**Scope.** Agents: `architect`, `feature-builder`, `quick-builder`, `reviewer`, `studio-operator` (`.claude/agents/`). Skills they load: `roblox-architecture`, `luau-code-review`, `remotes-security`, `datastores`, `performance-profiling`, `gameplay-systems`, plus `mcp-studio-workflow` (loaded by studio-operator). Rules they point to: `rules/architecture.md`, `performance.md`, `security.md`, `datastores.md`, `luau.md`, `anti-overengineering.md`, `packages.md`, `mcp-studio.md`, `content.md`, `gui.md`, `owner-profile.md`, `platform-policy.md`, `original-content.md`, and the process sections of `AGENTS.md`. None of the six skills has a `references/` folder (each is one `SKILL.md`).

**Two versions of every text.** The texts I read are the repo HEAD (2026-10-20). The game's rework mostly happened under the **baseline** text (commit `4a86dc544`, 2026-09-30 12:47, an "AI-first project scaffold" ported from the owner's earlier project `Roblox-Blocks`, `logs/2026-09-30-baseline-port.md`). Later edits: `189200157` (10-08 setup audit), `71d7dc484` and `a9582b5c8` (10-09 agent review), `3240ec883`, `4432c6307`, `c77c89842`, `4e8f86fe7` (10-10, docs-first and replication rules). Each row's **origin** cell says "baseline" or the edit date, so you can tell whether a rule could have prevented rework that happened earlier. I note when a baseline line was later removed.

**Universal / game.** `U` = applies to any Roblox game. `U-stack` = universal practice written in terms of this project's package stack (Networker, Janitor, Charm, DataService; D-041 says the stack is a default, not a mandate). `G` = tied to the brick world, stages, destruction or this game's economy.

**Evidence handles.** `A01..A26` and `B01..B27` are rows in `git-a.md` and `git-b.md` (git-a's two-round appendix is `aB01..aB10`; `EG`, `S`, `E` are those files' engine-guess and symptom tables). `R01..R07` and `rec §n` are in `records.md`. `F-nnn` is `tried-and-failed.md`; `D-nnn` is `decisions.md`. `scorecard` is `knowledge/logs/agent-review/2026-10-09.json` and `.md`. Other cites are repo paths.

**Columns.** "worked" means the evidence shows the rule (or the habit it names) prevented or ended rework. "failed or missing" means rework happened where the rule was broken, absent, stale or wrong. "no evidence" says why neither can be shown. A rule can have both.

**Run statistics (30 days to 2026-10-09, effectively the first 10 days of the project; the scorecard calls its pushback metric approximate).**

| agent | runs | finished | tool error rate | worktree-isolation refusals | re-brief rate | owner pushback (approx.) | median tokens / minutes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| feature-builder | 121 | 95.9% | 4.8% | 488 | 1.7% | 11.6% | 862k / 54 |
| reviewer | 61 | 100% | 1.4% | 9 | 26.2% | 3.3% | 150k / 8.8 |
| studio-operator | 37 | 97.3% | 4.5% | 0 | 24.3% | 8.1% | 138k / 17.6 |
| quick-builder | 13 | 92.3% | 9.3% | 36 | 7.7% | 46.2% (judged a false positive in the review) | 135k / 6.8 |
| architect | 6 | 100% | 0.7% | 0 | 0% | 33.3% (noisy) | 196k / 9.6 |

Source: scorecard JSON. These show activity, not quality. The one clear signal is that 601 builder actions were refused by the harness because they touched the main checkout; the log says about 590.

## 1. architect (`.claude/agents/architect.md`, 27 lines)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| AR1 | Read the architecture, performance and brick-system notes, the relevant design docs and the real code first; a design item is locked only if it has a ledger id (l.12) | U (read first) / G (file list) | the ledger-lock habit kept proposals apart from decisions and stopped retries (git-b §4; F-006 retried only when its condition was met) | a ledger text can hold a misread: D-109 recorded an indestructible mountain, D-110 "corrects the reading" (B12); D-122 vs D-127 same day (B10) | - | baseline; ledger rule AGENTS §0 (09-30) |
| AR2 | Mark each point as evidence (path:line or doc) or opinion, because the orchestrator decides from the answer (l.12) | U | labelled opinions were later tested and some failed: the "25x load" idea was not supported (`physics-findings.md:339`), the wake fall term was wrong (`:348`); labels let the lead discount them (lag-audit E/O/U) | - | - | `189200157` (10-08) |
| AR3 | Return placement: path, Studio parent, type, how it starts (l.15) | U-stack | - | baseline placement text put compiled stage content in ReplicatedStorage and called ServerStorage "Studio-managed" (S3, EG4, EG5, R02) | - | baseline |
| AR4 | Return a replication footprint per new or moved module: container, whether every client downloads it, bytes, why not ServerStorage (l.16) | U | - | pre-rule: 5.2 MB stage data and 1.56 MB server code reached every client (S3, EG5; `4e8f86fe7` body) | the rule is too new to show a prevented rework | `4e8f86fe7` (10-10) after the replication audit; D-133 |
| AR5 | Return authority (server owns, client owns, client requests), data (content tables, profile keys, runtime tables) and the Networker surface with its validation (l.17-19) | U-stack | no rework row traces to a wrong authority split; server authority held (engine review grade A- for bricks as data) | - | absence of failure is weak evidence | baseline |
| AR6 | Return a per-frame and instance budget (l.20) | U | consults that gave costed, ranked lists were used by builders (`astra-handoff.md` §2) | the budgets were estimates; CLI speedups ranked by them were invisible in Studio (EG9, `physics-findings.md:240`); the 8-12 player budget was never measured (rec §1 SR3) | - | baseline |
| AR7 | Return failure modes (l.21) | U | - | - | none found in the records | baseline |
| AR8 | Return the simplest version that ships and what it must not rule out on the roadmap; give a rough size in lines and say if existing code is far larger (l.22, l.25) | U | when an architect design replaced a patch chain the task ended: debris vetoes to pile sweep (B01, `1d46a48c`, F-007), mountain redesign (B26, handoff 10-10:43) | the destruction runtime grew to 45,068 lines in 100 modules against an estimate of 2.5-4k (clean-room :9); the architect ran only 6 times in the window versus 121 feature-builder runs, so most design choices were made by builders and the physics designer (A07, scorecard) | the size-of-simplest-version line (10-09) is too new | baseline; size line `a9582b5c8` (10-09, owner worry about overcomplication, D-118) |
| AR9 | List design questions for the owner; never decide design (l.23) | U | D-083 shows the right shape: "May I change that rule?" before breaking a binding rule (rec §5) | the owner often delegated instead ("you decide", D-073, D-082), so the rule and `rules/owner-profile.md` ("give one recommendation and act") pull in different directions | - | baseline; owner-profile 10-08 |
| AR10 | Read the docs mirror first and cite it; prefer an engine feature over custom Luau; for each part say which engine feature was considered and why custom code is still needed (l.25) | U | too new to show prevented rework | pre-rule: B09 (homegrown shadow system), B08, EG1-EG3; clean-room size check; lag-audit "engine features we should have used" | prevented-rework evidence missing after the rule | `3240ec883` (10-10); D-118, D-128 |
| AR11 | Audit the existing systems the design touches against the engine checklist; report misplacements outside the brief (l.27) | U | - | the replication miss sat unseen from 09-30 to 10-10 because no agent audited placement (S3, R02) | too new | `4e8f86fe7` (10-10) |
| AR12 | Advisory only (tools Read, Grep, Glob, Bash); effort medium (was high) | U | no unreviewed architect edits appear in the records | - | - | baseline; effort `189200157` (Opus 5.5 medium roughly equals Opus 5 high) |

## 2. feature-builder (`.claude/agents/feature-builder.md`, 36 lines)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| FB1 | Read the rules the task touches; run the context packet and read only the cited sections (l.16) | U / G (tool) | - | AGENTS.md was read in only 6 of 19 sessions until CLAUDE.md imported it (`logs/2026-10-08-setup-audit.md`); about 590 builder actions refused because the builder used main-checkout paths (scorecard) | context-packet effect not measured anywhere | baseline; import fix `189200157`; worktree line `71d7dc484` (10-09) |
| FB2 | Load the matching lens skill (gameplay-systems, gui-ui, remotes-security, datastores, performance-profiling, brick-builder) (l.17) | G (names) | - | - | no record shows which skill a builder loaded | baseline |
| FB3 | Read the Roblox docs for every engine system or API touched before designing; build the Roblox way; own code only if measurably better, and say why (l.18) | U | partial: B08 round 3 tested effect class names against the API mirror (`5be67384`) | before the rule: B08 invented effect class names, B09 rebuilt shadow policy, EG1-EG3, B17 | the rule has no later failure or success to compare | `3240ec883` (10-10); D-118, D-128; owner: "inventing our own stuff" (D-139) |
| FB4 | Confirm the write scope; never edit shared registries (LoadOrder, ControllerOrder, ProfileTemplate, Networkers, default.project.json); return the lines needed (l.19) | U / G (file names) | parallel lanes merged with disjoint scopes (`logs/2026-09-30-stage1-prototype.md` lanes A-E) | the ProfileTemplate path in this line went stale after D-133 and needed `f2d89feff` | no conflict row exists, which is weak evidence | baseline |
| FB5 | Put pure logic in side-effect-free shared modules with an offline suite; for a bug fix write the failing case first (l.22) | U | failing-case-first closed bugs in one more round: `8ce884ac5`, `3e971a924`, `00236dbc2`, `e8e417519`, `8af7b1f3`, `5983bee7`, `5499509a` (git-a §3.1, git-b §4); oracle and mutation tests ended A05 (`3ddcecc8b`) | the first spec covered a toy case, not the real content or the owner's scene: A05, A12, A14 (real-stage case only in `edaedb215`), A18, A19, A21, A23 (a skipped test hid the break), B05 (windmill content had every rotor part anchored), B18, B20, B21 | - | baseline |
| FB6 | Validate every client-callable method per the security rules (l.23) | U-stack | A18 (NaN blast refused), `368d56dc` (instant-credit teleport hole), A17 (movement gate) were caught by review before merge | A12: the cooldown-commit race came back in the thrown-C4 build (`cdd98eb3b`); builders had no checklist for "commit before you yield" | - | baseline text "Networker only. Validate every clientAccess method"; moved to rules 10-08 (`189200157`) |
| FB7 | UI follows the ui-style note and the brick UI kit; no default grey frames (l.24) | G | - | the look rule itself was reversed: D-054 painted art and Figma, then D-129 Blender-first; the owner called AI-drawn UI "AI slop" (A15, A16, rec §2) | - | baseline; `c77c89842` fixed the stale mock-up line (10-10) |
| FB8 | Stop and return instead of guessing when the brief needs a design choice or the work must outgrow the scope; state assumptions (l.25) | U | D-083 (asked before breaking a binding rule); R06 shows numbers kept as PROPOSAL while work went on | - | no failure traced to missing a stop | baseline; reworded `a9582b5c8` |
| FB9 | Do the work yourself; do not spawn subagents (l.26) | U | - | - | no evidence either way | `189200157` (10-08) |
| FB10 | Deliver what the brief asks; do not widen the task; list extra problems as open questions (l.27) | U | - | B09 built a per-category shadow system and changed defaults though the saving was 0.2-0.8 ms; B25 content added 377 steps; B08 invented classes | the brief's exact scope for B09 is not in the records | baseline "surgical edits" (AGENTS §3); reworded `a9582b5c8` |
| FB11 | If one symptom needs a third patch round, stop and return so the orchestrator can call a clean-room review (l.28) | U | B01 (five veto rounds, then a pile-sweep plan `1d46a48c`) and B26 (architect redesign `ecb1abe6`) ended in one design; handoff 10-10:43: "the mountain needed that" | before the rule: A02 9 rounds, A08 7, A01 6, A09 6, A14 6, A03 5, B02 6, B03 5 | the rule's own effect after 10-09 cannot be separated from the orchestrator doing the same by hand | `a9582b5c8` (10-09); owner worry; clean-room note `71d7dc484` |
| FB12 | Done = `tools/verify.ps1` prints `RESULT: PASS` in the worktree; commit with Agent/Model/Effort trailers (l.30-31) | U | the gate as a floor: every merged fix passed it; trailers made this study possible | the gate cannot see the game: it tests arithmetic not behaviour (engine review F21), ran with physics switches off while the owner played with them on (aB09), `-Fast` skips Luau suites (B24), tests tied to layout broke (S5) | - | baseline; trailers hook; `189200157` |
| FB13 | Return branch, Docs read, files, replicated bytes added, registry lines, how verified (gate / not Studio-verified), the Studio check to run, open questions (l.33-34) | U | honest labels let the lead schedule checks: 15 "Not Studio-verified" bodies in git-a §3 item 6; `logs/2026-10-05-accepted-still-live.md` | the label did not stop merging: A01 three rounds "Not Studio-verified", A16, B13 merged on CLI numbers, B23, B24 | - | baseline; Docs read and bytes `3240ec883`, `4e8f86fe7` |
| FB14 | Use relative paths in the worktree; never `cd` to or edit the main checkout; merge the base inside the worktree (l.36) | U | - | 488 refusals for this agent in the window (601 for all builders) before the line existed | later effect not recorded | `71d7dc484` (10-09), after the scorecard count |
| FB15 | Tuning numbers live in `content/` tables, never in logic (removed from this file 10-08; now `rules/content.md`, `gameplay-systems`) | G | config switches and Studio attributes made A/B runs possible (git-b §4: unified contact, B1 lanes, bigStress, D2 stayed off until measured) | 29 throttle constants in the config compensate for costs (engine review §3), so "data" became a way to hide load-dependent behaviour | - | baseline; moved by `189200157` as a duplicate |
| FB16 | Janitor owns every connection, thread, tween and temp Instance; `--!strict` on shared/server code (removed from this file 10-08; now rules) | U-stack | - | - | no rework row mentions cleanup or typing | baseline; moved `189200157` |
| FB17 | Isolation worktree; effort medium (was high) (frontmatter) | U | parallel builders did not collide in the lanes of 09-30 | the early master merge was an orchestrator dry-run in the main checkout, not a builder (`logs/2026-09-30-stage1-prototype.md` Incident) | - | baseline; effort `189200157` |

## 3. quick-builder (`.claude/agents/quick-builder.md`, 26 lines)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| QB1 | Only minor, fully specified work in a worktree; anything touching core systems, economy, persistence, remotes or brick-world logic goes to feature-builder (description, l.12) | U | - | B08 (lighting presets) and B09 (shadow cost) were quick-builder tasks (Sonnet 5.5 medium) that were measurement and design tasks, not fully specified: 3 rounds each, wrong-engine-guess and reinvented-engine-feature | routing reason for B08/B09 not in the records | baseline; D-021 (Sonnet only for minor work) |
| QB2 | Stop and return if a design choice appears, the change grows past about 200 lines, or adds about 50 KB to a replicated container (l.14) | U | - | B08/B09 grew across rounds without a stop | the 50 KB line is new | baseline; 50 KB line `4e8f86fe7` (10-10) |
| QB3 | Write only inside the briefed scope; return needed registry lines; no subagents (l.12) | U | - | - | no evidence | baseline |
| QB4 | Done = the gate prints PASS, committed with trailers (l.16) | U | the gate is a floor | B08 round 2 (`622f1116`) was gate-only and still created instances in code | - | baseline |
| QB5 | Read the Roblox docs before design; own code only if measurably better (l.18) | U | see FB3 | B08, B09 before the line | no later case | `3240ec883` (10-10), D-128 |
| QB6 | Keep working until the brief is done or blocked; do not stop midway (l.24) | U | - | - | no evidence | `a9582b5c8` (10-09) from Sonnet 5.5 guidance |
| QB7 | Before reporting a change as working, run a real check and quote the result; a file that compiles is not a check (l.26) | U | - | B08 round 2 and A16 handed in on gate or preview only | no case after the line | `a9582b5c8` (10-09) |
| QB8 | Return branch, docs read, files, replicated bytes, registry lines, verification, about 300 words (l.20) | U | - | - | no evidence | baseline; extended 10-10 |

## 4. reviewer (`.claude/agents/reviewer.md`, 27 lines)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| RV1 | Review the named diff and what it calls; mandatory before merging purchases, currency, persistence, egg rolls or client-callable methods; report findings only (description, l.14) | U | independent review found real defects before merge: A12, A17, A18, A19 (`6e31ed352`, `471780f84`); later `ed0c842f`, `776720c0`, `5489c26d`, `368d56dc`, `f92651c1`; scorecard: 61 runs, 100% finished, 3.3% owner pushback | review is bounded to the diff: B13 merges said "reviewed, no Medium+" without a Studio run; B17 "identical" (`3e81e06e`) was wrong for 158 verdicts found by a Studio probe; B05 round 1 passed review with content that could never detach | - | baseline; brick-core physics reviews came from the owner's 10-06 brief, not this rule |
| RV2 | Look hardest at what a client can fake, currency and save-data correctness (atomic check inside `update`, idempotent receipts, no double grant on retry or rejoin), economy exploits and races (l.20) | U-stack | the client-fake and race parts caught A12, A17, A18 and `368d56dc` | A12 came back at High in the thrown-C4 build; the persistence part has no case | persistence and receipts: no rework or review row; handoff 10-10:33 lists the rejoin-save Studio check as not run | baseline priorities 2-5; reworded `189200157` |
| RV3 | Flag complexity: code that redoes an engine feature, a Studio switch with no plan to remove it, a patch on a symptom already patched twice (l.18) | U | too new | before the rule: S6 11 patches, F-007, B01 | - | `a9582b5c8` (10-09); D-118 |
| RV4 | Check the Roblox way both ways: engine feature used, builder listed the docs read, flag forced engine features that measure worse (l.16) | U | too new | B08, B09 before the rule | - | `3240ec883` (10-10); D-128 |
| RV5 | Flag server-only data or logic under ReplicatedStorage, ReplicatedFirst or StarterPlayer, growth in replicated bytes, and a reliable vs unreliable mismatch (l.17) | U | too new | S3, EG4, EG5 | - | `4e8f86fe7` (10-10); D-133 |
| RV6 | Report every finding as severity, path:line, symbol, problem, exploit or failure scenario, fix, and the test that would catch it; end with what you could not verify; skip style nits (l.22-27) | U | review fixes added specs: A19 (decode bounds), A18 (`brickworld_sync`); the "could not verify" line is how unverified Studio claims were exposed | - | - | baseline format; "default effort medium" `189200157` |
| RV7 | Default effort medium; the brief raises it for purchase, persistence or brick-core code (l.14) | U | the 10-06 brief ran core-physics reviewers at high and xhigh and used adversarial verifiers; the verifiers refuted sub-claims of 26 findings (engine review Appendix) | - | no comparison of effort levels | `189200157` |
| RV8 | Read-only (tools Read, Grep, Glob, Bash) | U | - | - | no evidence | baseline |

## 5. studio-operator (`.claude/agents/studio-operator.md`, 26 lines)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| SO1 | Pre-check that Studio is connected, Rojo is synced and the expected Instances exist (l.14) | U | - | Rojo crashed and the plugin disconnected during the first sessions (`logs/2026-09-30-stage1-prototype.md`; handoff 10-04 test-map-start.md:57) | no row shows a pre-check preventing rework | baseline |
| SO2 | Never edit `.luau` through MCP; use edit-mode `execute_luau` only for read-only checks or requested setup (l.15) | U | no divergence between disk and Studio is recorded | - | absence only | baseline; `rules/mcp-studio.md` |
| SO3 | Play-test exactly the steps in the brief; capture errors and warnings, screenshots, FPS, draw calls, instance count, memory by category, `DataReceiveKbps` (l.16) | U | Studio probes overruled assumptions: `bb9471ad` (memory), `a7ce9a3b` (bounds), `ed2f45dd` (11-view review), `8b13cfec` (foreground checkpoint with a preset budget) (git-b §4) | readings were confounded: background Studio throttles (EG8), scanning the log during a run adds 140-1,800 ms (E14), 130-520 ms Heartbeat stalls with Lua at 0-2 ms (`physics-findings.md:241`), `DataReceiveKbps` reads 0 in Play Solo, one cottage recipe gave two outcomes (`:113`); the rule has no foreground, repeat-run or spread requirement | - | baseline; perf list widened 10-10 (`4e8f86fe7`) |
| SO4 | Footprint probe in edit mode: ReplicatedStorage descendant count and script bytes per folder, plus place settings (l.17) | U | - | S3 went unseen without it | too new | `4e8f86fe7` (10-10) |
| SO5 | Label each check MCP-verified or not verified; if Studio is unavailable say so and give manual steps (l.18) | U | honest labels: `logs/2026-10-05-accepted-still-live.md`, git-a §3 item 6; D-101 used "owner-confirmed" | - | - | baseline; AGENTS §2.3 |
| SO6 | Return pass/fail with evidence, deduplicated errors, screenshot paths, a perf table, and a suspected cause for each failure as a hypothesis (l.20) | U | MEASURED / HYPOTHESIS labels in the findings log kept guesses visible (`physics-findings.md:348`, `:241`) | - | - | baseline |
| SO7 | For a visible change shoot the required angles (front, side, back, high 3/4, player eye), report each problem with its screenshot, never fix (l.22) | G | `ed2f45dd` found open porch roof courses that offline checks passed (B20); the cottage and church built after an approved blueprint drew only a colour review (git-a §3 item 8) | blank back walls and odd spheres reached the owner on Stage 3 (D-192, R07); holes under the mountain were found after merge (B21); the review moved from content-builders to a post-merge Studio step (`189200157`), so it comes late | - | owner request 09-30 (`6978a3042`, awning built backwards); AGENTS §2.4; restore-camera line moved to the skill 10-08 |
| SO8 | Drive only the Studio instance named in the brief; one driver at a time (frontmatter, l.3) | U | - | B27: a two-instance plan (`18920015`) failed in practice (`9371849c`, EG7); a plan for two Studio windows had been committed on 10-08 | no case after the fix | baseline "one driver"; two instances 10-08; one instance `a301cb8af`, `9371849c` (10-09) |
| SO9 | Keep working until done; before reporting run a real check and quote it (l.24, l.26) | U | - | - | no evidence | `a9582b5c8` (10-09) |
| SO10 | Sonnet 5.5, effort medium; all Studio testing goes to Sonnet, never Opus (frontmatter; owner 10-06) | U | scorecard: 37 runs, 97% finished | 24% re-brief rate | no quality comparison with Opus | baseline; owner 10-06 (handoff 2026-10-06:81) |

## 6. Skills they load

### roblox-architecture (`.agents/skills/roblox-architecture/SKILL.md`)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| RA1 | Name the player-facing feature and check whether the ledger locks it (l.12) | U | see AR1 | see AR1 | - | baseline |
| RA2 | List trusted state and untrusted inputs; split server, client, shared (l.13-14) | U | - | - | no rework traces to this | baseline |
| RA3 | Place files in the service/controller folders and register in LoadOrder or ControllerOrder (l.15) | G | - | - | no evidence | baseline |
| RA4 | Define intent-named `clientAccess` methods, ProfileTemplate keys only for persistent data, Charm atoms only for cross-screen state, Janitor owners (l.16-19) | U-stack | - | - | no evidence | baseline |
| RA5 | For world features define data layout, chunking, render strategy, change replication, mobile render distance, per-stage delivery path and memory release (l.20) | G | the brick world as data with deltas graded A- keep by the engine review | the per-stage delivery and memory-release items were added after the miss; rested rubble followed forever on clients (engine review F7), statics replicate to clients (NET-3) | - | baseline (items 1-9); delivery path `4e8f86fe7` |
| RA6 | Placement heuristics: bootstrap Script plus ModuleScripts; trusted logic in ServerScriptService; server-only data in ServerStorage; shared only if a client requires it; type-only modules must not require runtime modules (l.29-35) | U | too new | the baseline said ServerStorage is "Studio-managed" and compiled content goes to shared: S3, EG4, EG5, R02 | - | rewritten `4e8f86fe7`, `2874c8403` (10-10), D-133 |
| RA7 | Checklist: can an exploiter fake it; what does a client download; server-only logic in replicated modules; one server and two clients; clear module names; degrade on DataStore failure; smooth on a low-end phone (l.40-46) | U | - | the phone item could not be checked: no real device (D-117), emulation only (`physics-findings.md:116`) | the two-client item: multi-client test not run (`:152`) | baseline; download items `4e8f86fe7` |

### luau-code-review (`.agents/skills/luau-code-review/SKILL.md`)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| LR1 | Review order: runtime correctness, trust boundary, `clientAccess` validation, DataService use, Charm, Janitor, typing, service shape, performance, readability (l.10-19) | U-stack | review caught runtime and trust defects first (A17 respawn baseline, A18, A12) | performance sits ninth; the perf failures (B13, B02) were not reviewable from a diff | - | baseline (never edited) |
| LR2 | Common bugs: assuming Character/HumanoidRootPart exists, infinite WaitForChild, leaked connections, trusting client positions or amounts, unchecked NaN, saving fallback data after a failed load, mutating shared config, same-table atom writes, modules over about 1,000 lines (l.23-31) | U-stack | A17 `b73d94957` (position read at CharacterAdded) and A18 (NaN) match the first and fifth items | the size item: `ChunkBodies.luau` was about 3,400 lines against a guideline of 800 (handoff 10-04:98); the runtime has 45k lines in 100 modules | cleanup, typing and DataStore items: no rework case | baseline; 800 changed to 1,000 on 10-08 |
| LR3 | Findings format with severity, problem, why it matters in Roblox, fix, verification (l.35-41) | U | see RV6 | - | - | baseline |

### remotes-security (`.agents/skills/remotes-security/SKILL.md`)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| RS1 | Every client-server call goes through Networker, which is transport and not authorization (l.8) | U-stack | no raw-remote incident recorded | the stack has no unreliable channel; the review asks for one (F14, F15) but nothing was built | no evidence either way | baseline; D-041 makes the stack a default |
| RS2 | Validation order: ready, types (finite, integer, string caps), shape, rate, ownership, distance, state, idempotency; fail silently (l.27-38) | U | A18 NaN, A17 gate, `368d56dc`; no exploit rework in range | A12: no step says "commit the cooldown before any yielding call" | - | baseline; `93d022286` (thrown C4) |
| RS3 | Contract example: the server simulates the shot and ignores client hit claims (l.12-25) | G | the design held: no client-trust incident | - | - | baseline; updated for D-051 |
| RS4 | Reliable for state, unreliable only for small replaceable streams (over 1,000 bytes drop); about 500 requests per second per client; batch per blast; Networker has no unreliable channel (l.40-45) | U | deltas at about 1 byte per brick graded A- keep (engine review §1.1); kill-list varint format came from measured bytes (aB10) | - | - | baseline; unreliable section `189200157`, `4e8f86fe7` |
| RS5 | Avoid raw remotes, generic endpoints, client-sent results, client Instance references, yielding fetch handlers, server-only logic in replicated modules (l.49-56) | U | - | the last item was added after S3, EG5 | - | baseline; last item `4e8f86fe7` |

### datastores (`.agents/skills/datastores/SKILL.md`)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| DS1 | Add keys to the template; bump the version and migrate on load for renames (l.18-22) | U-stack | - | - | no rework row; no schema change in range | baseline |
| DS2 | Write only from a server service; put validity checks inside the `update` callback (l.19-20) | U-stack | economy path reviewed four rounds (A17) | - | persistence itself has no rework row; end-to-end rejoin save is listed as not run (handoff 10-10:33) | baseline |
| DS3 | Client reads via change signals; clone before atoms (l.21) | U-stack | - | - | no evidence | baseline |
| DS4 | The brick world is never saved (l.30) | G | no rework about world saving | - | absence only | baseline; D-030 (player data incl. carried bricks) |
| DS5 | JSON-safe values, coarse checkpoints, no empty-profile fallback, idempotent receipts (l.30 and `rules/datastores.md`) | U | - | - | none | baseline |

### performance-profiling (`.agents/skills/performance-profiling/SKILL.md`)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| PP1 | First questions: which kind of problem, join size, one player or many, leak, warnings, brick Parts, render distance, phone or Studio only (l.12-18) | U | - | A01 and B02: the work started from a guess, not a measured split | - | baseline; join-size item `4e8f86fe7` |
| PP2 | Tools: MicroProfiler, Render Stats, Developer Console, ProcessPackets and worldStep scopes, Script Profiler, device emulator plus a real device for the truth (l.22-27) | U | the profiling ledger and foreground checkpoint (git-b §4, `1fa1beda`, `8b13cfec`) found the real causes | the emulator shows screens not CPU; no real device existed (D-117); nothing here warns about Play Solo sharing one process, background Studio, or log scans | - | baseline; scopes `4e8f86fe7` |
| PP3 | Common fixes: spread builds over frames, render exposed faces only, pool and anchor bricks, events not polling, move client-unused data out of ReplicatedStorage, let bodies sleep and re-anchor, default shadows, `BulkMoveTo`, Actors only after measurement (l.31-42) | G / U | client draw radius, pooling and FrameBudget graded sound by the review; shadow line corrected after F-018 | "let bodies sleep and re-anchor" is the pattern behind rest/wake churn (SR1); stage reset destroyed about 24k Parts in one frame despite the spread-over-frames line (B13, S2); the shadow advice was added then retired inside a day (D-123, D-139) | - | baseline; edits `189200157`, `3d9413ae4`, `4e8f86fe7`, `914f26654` |
| PP4 | Verify: compare before and after in play mode; check instance count and memory return to baseline; keep Output clean (l.45) | U | before/after tables produced the fixes that stuck (A01 SM2, A03 FL1, A08, B02 checkpoint) | the line does not require a baseline taken first, repeated runs, the same recipe, or reported spread (A01, B02, B13, cottage two outcomes `:113`) | - | baseline |

### gameplay-systems (`.agents/skills/gameplay-systems/SKILL.md`)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| GS1 | Locked design is the ledger; build with the documented proposal and flag it; new mechanic ideas are welcome as labelled proposals (l.8-11) | G | PROPOSAL numbers let work continue (B10, R06); the ledger kept retries out | B10 still took five rounds on PROPOSAL numbers (owner direction, not a fault) | - | baseline said "do not invent unlocked mechanics"; changed `c77c89842` (10-10) |
| GS2 | Canonical weapon flow: input, requestFire, server validate and simulate, query bricks, islands to server bodies (D-083), credit, delta, client apply (l.15-25) | G | engine review graded the data-first flow A-; weapon lane reviewed and merged (A12) | the body step was added after D-083; AGENTS.md carried the opposite rule for 8 days (R02) | - | baseline; bodies `3af9c542d` (10-02) / `4e8f86fe7` |
| GS3 | Tuning is data in `content/`, no magic numbers in services (l.29) | G | see FB15 | see FB15 | - | baseline |
| GS4 | Pure core, thin services, offline specs (l.30) | U | see FB5 | see FB5 | - | baseline |
| GS5 | Batch brick credits per player and flush on a cadence or at sell (l.31) | G | - | - | no evidence | baseline |
| GS6 | Every client call can lie: never accept hit lists, counts, impact positions or roll results (l.32) | U | see RS2 | - | - | baseline |
| GS7 | Cosmetics are client-side; the server sends facts plus a seed (l.33) | U | kill deltas at about 1 byte per brick; client debris by seed | the falling-piece smoothing layers built on this client idea were wrong (A01, E8); client-drawn falling pieces collide with the local character (engine review F19, inferred) | - | baseline |
| GS8 | New audio uses AudioPlayer, AudioEmitter, Wire; phone haptics via HapticEffect (l.34) | U | - | - | no evidence | `189200157` (10-08) |
| GS9 | Before adding custom contact queries for server bodies, evaluate Collision Summaries (`BindToCollisionSummaries`) (l.35) | U | - | the call errored "is not enabled" on 10-04 (E12); the review says contact impulses are unavailable; no re-test recorded, so the rule and the measurement conflict (rec §2 E12) | - | `3240ec883` / `4e8f86fe7` (10-10), D-128 |
| GS10 | Discovery rewards return visits; judge a loop by next-day return (l.36) | U | - | - | no evidence | `c77c89842` (10-10) |
| GS11 | Checklist: which loop it feeds; what can be faked; per-blast ms and delta bytes; container bytes; behaviour with 12 players (8 minimum) blasting one structure; one-thumb phone use (l.40-45) | G | - | the 12-player and phone items were never measured (`physics-findings.md:152`, D-117, rec R06) | - | baseline; D-058 |

### mcp-studio-workflow (`.agents/skills/mcp-studio-workflow/SKILL.md`, loaded by studio-operator)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| MS1 | After screenshots, restore the edit camera to Fixed (l.10) | U | - | the camera was left locked in the first session | no later case | `2ea53297a` (owner report 09-30) |
| MS2 | Wedges rise toward +Z at identity; awnings and roofs are easy to get backwards (l.11) | G | - | the 09-30 awning incident | no later case | `6978a3042` (09-30) |
| MS3 | `execute_luau` runs in the plugin context, so `require` returns separate copies; read prints from the log history; do not scan the log during a lab run (l.12) | U | - | E14: a log scan added 140-1,800 ms to server frames and produced false "frame max" readings | - | `189200157` (10-08) |
| MS4 | The place is Team Create; never edit scripts in Studio; restore toggled properties (l.13) | U | - | - | no evidence | baseline |
| MS5 | One Studio instance; starting a second causes idle hitches (l.14) | U | - | B27, EG7 | no case after the rule | `189200157`, `9371849c` (10-09) |
| MS6 | Rojo serves the main checkout, not worktrees; MCP can only start Play Solo; `screen_capture` can time out in Play (l.15) | U | - | multi-client test never ran (`physics-findings.md:152`) | - | `189200157` |
| MS7 | Snippets are temporary and targeted; do not delete trees, touch live DataStores or grant currency without an explicit request (l.17) | U | - | - | no evidence | baseline |
| MS8 | Done means no new console errors or warnings, expected Instances in the right services, behaviour matching server authority (l.18) | U | - | - | no evidence | baseline |

## 7. Rules the agents point to

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| RU1 | Server is authoritative for fairness and persistence; the client owns presentation; falling pieces are server-owned bodies (`rules/architecture.md:7-8`) | G | D-083 let the engine-body route in; no authority rework in range | AGENTS.md §1 said "never unanchored physics on the server" from the baseline (`4a86dc544:AGENTS.md:58`) until `c77c89842` (10-10) | - | baseline; D-083 (`3af9c542d`, 10-02) |
| RU2 | The server holds brick data, not brick Parts; exception is the invisible body colliders (`architecture.md:9`) | G | engine review grade A- keep | permanent colliders grew to 29,633 and about 5.2k replicate to clients (NET-3, lag-audit) | - | baseline; D-083, D-099 |
| RU3 | Everything is on disk (Rojo); Studio-only state is limited to place settings recorded in `place-settings.md`, created the first time one is changed (`architecture.md:31`) | U | - | Fixed stepping was set in the place and the file was never created (agent-docs-audit §2; handoff 10-04:57) | - | baseline |
| RU4 | One responsibility per module; split near about 1,000 lines; shared must not require server-only code; declare locals before use (`architecture.md:42-46`) | U | - | `ChunkBodies.luau` about 3,400 lines (handoff 10-04:98); 45k-line runtime (clean-room :9) | - | baseline; 800 to 1,000 on 10-08 |
| RU5 | Services: init does not yield, start wires, each step pcall-wrapped; controllers mirror (`architecture.md:48-55`) | U-stack | - | - | no rework row | baseline |
| RU6 | Networker only; `clientAccess` registered after all services start; intent-named methods (`architecture.md:57-63`) | U-stack | - | - | no evidence | baseline |
| RU7 | Placement and replication table; a module goes in shared only if a client requires it; server-only logic never in a replicated module; name container and bytes for every new module (`architecture.md:65-85`) | U | too new | pre-rule S3, EG4, EG5, R02 | - | `4e8f86fe7`, `2874c8403`, `99d8a3ea2` (10-10), D-133 |
| RU8 | Replicate only what clients need; send deltas not full state (`architecture.md:87-91`) | U | deltas (A-) | - | - | baseline |
| RU9 | One loop per system; no uncontrolled `while true`; no descendant scans in frame loops (`architecture.md:95-96`) | U | - | about 10 per-frame loops walked every chunk until the 10-05 index (`physics-findings.md:21`, `ChunkIndex`) | - | baseline |
| RU10 | Cleanup through Janitor (`architecture.md:100-102`) | U-stack | - | - | no rework row | baseline |
| RU11 | Engine feature or our own system: use the engine feature when it does the job at our scale; build our own when it cannot express the game; both mistakes count (`architecture.md:104-116`) | U | too new | B09, EG1-EG3, EG10 | - | `4432c6307` (10-10), D-118, D-128 |
| RU12 | Mobile is the primary user; per-frame work spread with budgets; pool Instances; set properties before parent; one Heartbeat for scale visuals (`performance.md:9-15`) | U | client FrameBudget graded sound | stage reset destroyed about 24k Parts in one frame, 404-565 ms (B13); one-frame spikes S2 | - | baseline |
| RU13 | Brick world: only exposed bricks instanced, pooled anchored CanTouch-off Parts, no per-brick scripts, default shadows, capped debris (`performance.md:17-27`) | G | draw radius and pooling kept the client sound | the shadow line was reversed twice (D-123, D-139, F-018) | - | baseline; shadows `914f26654` |
| RU14 | Content meshes declare Box or Hull CollisionFidelity (`performance.md:31`) | G | - | not settable from scripts, so the rule was marked dormant (EG6, `9d9a72176`) | - | baseline text; dormant 10-10 |
| RU15 | Effects thin out with distance and have live caps (`performance.md:35`) | G | - | - | not Studio-checked (handoff 10-10:20) | `f28e5839` (10-10) |
| RU16 | Targets: 60 FPS on mid-tier phones, no hitches, flat memory, clean Output; "initial, revise with measurement" (`performance.md:44-49`) | U | - | never measured on a phone by 10-10 (D-117, D-141); engine review budget table says the server "fails" for 8-12 players (estimate) | - | baseline |
| RU17 | Measuring: MicroProfiler, Render Stats, Developer Console; the emulator is not a device, a real low-end device is the ground truth (`performance.md:51-55`) | U | - | EG8, EG9; no device lab (SR3) | - | baseline |
| RU18 | Physics: static geometry anchored; cosmetic debris is client-created; constraints only on listed hero props; falling building pieces are server bodies up to 120 per stage (`performance.md:57-60`) | G | the 120-body cap held as a safety valve (engine review §3 item 9) | one long bullet that grew across D-083, D-099 and `266523319`; the Fixed-stepping result is not in it | - | baseline; D-083, D-099 |
| RU19 | The client can lie about everything; never let requests grant rewards directly (`security.md:5-8`) | U | no exploit rework | - | - | baseline |
| RU20 | Remote validation list (`security.md:10-20`) | U | see RS2 | A12 | - | baseline |
| RU21 | No secrets, admin data, anti-cheat thresholds, server-only logic or unreleased content in replicated locations; replicated modules can be decompiled (`security.md:24`) | U | too new | S3, EG5; the 14-stage surprise order was at risk on day one | - | baseline; expanded `4e8f86fe7`, D-133 |
| RU22 | Purchases are server-verified and idempotent; secrets live outside the repo (`security.md:28-38`) | U | - | - | no evidence | baseline |
| RU23 | DataStore rules: DataService only, template with migration, writes at coarse checkpoints, atomic checks inside `update`, no empty-profile fallback, receipts idempotent (`datastores.md`) | U-stack | - | - | no rework or review row | baseline |
| RU24 | `--!strict` on shared and server modules; typed public APIs; guard clauses; check Instance existence (`luau.md`) | U | - | - | no evidence | baseline |
| RU25 | Prefer simple; add structure when code crosses boundaries or repeats; avoid frameworks, DI containers, hand-rolled persistence, state stores, remote wrappers and cleanup helpers (`anti-overengineering.md`) | U | - | it names packages and frameworks, not homegrown copies of engine features or runtime size; the runtime reached 45k lines (clean-room :9), the owner said "overcomplicated" (D-118); closed by D-128 | - | baseline; D-041 note |
| RU26 | Package stack is a default; patch, fork or replace deliberately and document it (`packages.md`, D-041) | U-stack | - | - | no rework row | `e8666e760` (09-30), D-041 |
| RU27 | Rojo edits, MCP verifies; capture console errors after every play test; if MCP is down say so and mark checks user-confirmed (`mcp-studio.md`) | U | honest labels (see SO5) | - | - | baseline |
| RU28 | Content is data: stable ids never renamed, schema versions, generated files never hand-edited, structures go draft, review, approved, only approved ship (`content.md`) | G | the gate held generated files; the status gate kept unreviewed content out of published servers | B23: the live Stage 1 was empty because all 54 placements were still "review"; builders and the gate did not show it | - | baseline |
| RU29 | GUI: standard Instances, no React, controllers own behaviour, touch targets about 44 px, per-platform HUD sizes, test at three resolutions (`gui.md`) | G | `hud_geometry` spec at 6 screens fixed the HUD (A16) | A16: the HUD was handed in with a 1629x939 preview only | - | baseline; mock-up line `c77c89842`, `abee4acae` (D-129) |
| RU30 | Owner profile: talk about what the player sees, one recommendation, STE writing, blueprint then renders then Studio, how to work on physics (spec first, player-like cuts, measure in Studio, one passing build) (`owner-profile.md`) | G | blueprint-first drew only colour reviews (git-a §3 item 8); spec-first (git-a §3 item 1) | - | - | `189200157` (10-08) moved from the orchestrator's memory |
| RU31 | Platform policy and original content rules (paid random items, filtering, IP) | U / G | the status gate and D-156 kept names off landmarks | an early reference set was rejected for copying another game's IP (`astra-handoff.md:108`) | most rows have no case in range | baseline; D-017, D-187 |

## 8. Project process rules the agents inherit (`AGENTS.md`, harness profile, orchestration)

| id | rule (paraphrase) | U/G | worked | failed or missing | no evidence | origin |
| --- | --- | --- | --- | --- | --- | --- |
| AG1 | The gate is the source of done: `RESULT: PASS` or not done (§2.2) | U | see FB12 | see FB12 | - | baseline |
| AG2 | Label every check gate-verified, MCP-verified, owner-confirmed or not verified; never skip verification silently (§2.3) | U | see FB13, SO5 | labels did not block merging unverified perf work | - | baseline |
| AG3 | Multi-angle Studio review of anything visible before reporting (§2.4) | G | see SO7 | see SO7 | - | owner request 09-30 |
| AG4 | Plan, build, verify, log; short numbered plan with a check per step (§3) | U | - | - | no evidence | baseline |
| AG5 | Simplest thing that works; data-driven tables, no speculative frameworks (§3) | U | - | see RU25 | - | baseline |
| AG6 | Say what you assumed; push back when a rule looks wrong (§3) | U | D-083 | - | - | baseline |
| AG7 | Check what changed before reporting a state; other chats work in parallel (§3) | U | - | the 10-09 clean-room note was written from older state until the owner pointed out other chats had worked on it (clean-room :12) | - | `cabeb0e04` (10-09, crew-board mod; other chats edit the repo at the same time) |
| AG8 | Tests are the spec; a bug fix starts with a failing case (§3) | U | see FB5 | see FB5 | - | baseline |
| AG9 | Parallel builders get disjoint write scopes; shared files are merged by the orchestrator (§4, orchestration rule 2) | U | see FB4 | - | no conflict evidence | baseline |
| AG10 | One driver per Studio instance; performance runs take an exclusive lease (§4, orchestration rule 3) | U | - | EG8 (background Studio), B27; the exclusive-lease line is not in the studio-operator text | - | `a301cb8af`, `9371849c` (10-09) |
| AG11 | Verify subagent claims (paths, lines, API facts) before relying on them (§4, orchestration rule 7) | U | the setup audit caught 3 subagent errors; verifiers refuted sub-claims of 26 review findings | - | - | baseline (AGENTS §4); reinforced by owner 10-08 (orchestration rule 7) |
| AG12 | Briefs state a Docs line (exact docs pages) for builders, architect, reviewer, studio-operator (orchestration brief format) | U | too new | handoff 10-10:39: missing doc pointers caused the lighting bug (B08) | - | owner 2026-10-10; `rule-guard` mod |
| AG13 | Log: finished system gets a contract card; session log under 40 lines; decisions to the ledger; reverted approaches to the tried-and-failed register (§5) | U | the register and ledger are how this study was possible (git-b §4); F-006 retry-met | `physics-findings.md` grew to 184 KB; the briefs tell every agent to read it first, which is not practical in one context window (about 46k tokens) | whether agents read it is not recorded | baseline; register `189200157` (10-08) |

## 9. Habits that worked with no written rule

| id | habit | evidence | where it could be written |
| --- | --- | --- | --- |
| HB1 | New physics ships behind a default-off switch with byte-identical output when off, then an A/B in Studio | `3e971a924`, `4584fa60c`, `893fbca2`, `9aa7b8c9`, `c8e2668b`: no switched feature shipped as a regression | builder and reviewer |
| HB2 | Behaviour-identical changes are proved with frozen-copy differential tests and planted-bug mutants | lanes A, C, D1, E, F3, ChunkScan, GroundIndex merged with no rework (git-b §4; 28 + 4 mutants caught on 10-06) | builder |
| HB3 | Alternate arms in the same Studio session and report ratios | `ec17f46b`, `dbe88803` | studio-operator |
| HB4 | Add a profiling ledger before fixing | `1fa1beda` found debt idle and churn | performance skill |
| HB5 | Pre-set a pass budget before a foreground checkpoint | `8b13cfec`: p95 0.77 vs 23.6 ms | performance skill |
| HB6 | Studio-only repro hooks (`BrickWorldDevCut`, `DevDrop`, traces) | `e0acac123`, `17c4a2443`, `73f07339f` | builder |
| HB7 | Measure a candidate fix before it becomes the default, even when written in the same task | F-011: cache regressed 0.291 to 1.348 ms and was capped before merge (`physics-findings.md:55`) | builder |
| HB8 | Stop after 2-3 rounds and ask for an architect design | written for builders on 10-09 (FB11); in use for B01 and B26 before and after | already a rule |

## 10. Gaps: rules that were broken or missing when rework happened

| id | gap | evidence | affects |
| --- | --- | --- | --- |
| GP1 | No standing rule to measure first: take a baseline, repeat the same recipe, report spread, then change code | A01 (three smoothing layers built before the source was measured), B02 (CLI and memory work before a foreground soak), B13, B01, A03; the skill's Verify line is a post-check | builder, performance skill, studio-operator |
| GP2 | A perf, physics or feel claim may be merged "Not Studio-verified" with no stop | A01 rounds, A16, B13, B23, B24, B25; labels were honest but not binding | builder, reviewer, lead |
| GP3 | Docs-first covers what docs state, not what they leave out; no rule to write a short Studio probe for any engine behaviour the design relies on | E1, E5, E7, EG3, EG10, A25; probes overruled assumptions when they were run (git-b §4) | builder, architect |
| GP4 | Tests must use the real content, the real scale and the owner's scene | A14 (`edaedb215`), B05, B20, B21, A23, A05 | builder |
| GP5 | Measurement hygiene is not in the studio-operator text: foreground window, exclusive lease, no log scans, three or more runs | EG8, E14, `physics-findings.md:113`, `:241` | studio-operator, skill |
| GP6 | No device lab and no rule saying what to do without one | D-117, D-141, SR3, RU16, RU17 | all performance rules |
| GP7 | Rules drift from decisions: a stale rule stayed live for days | AGENTS.md §1 (`4a86dc544` to `c77c89842`), placement rule, UI mock-up line, `place-settings.md` never written, Fixed stepping not in the checklist | rules owner |
| GP8 | Rules were not delivered: AGENTS.md skipped in 13 of 19 sessions; 601 refused builder actions | setup audit, scorecard | harness, builders |
| GP9 | Repeated defect classes have a reviewer net but no builder checklist | A12 (cooldown ordering), A14 (landing), R01 (roads) | builder |
| GP10 | Routing: the architect ran 6 times against 121 builder runs; quick-builder took design-adjacent measurement tasks; the physics design role is not an agent file | scorecard; A07; B08, B09 | lead, routing rules |
| GP11 | Over-building has no size or complexity budget in the agents, only in the owner's words | clean-room :9; D-118; B09; B25 | architect, reviewer |
| GP12 | A rule says "evaluate" a feature that the project measured as unavailable | GS9, E12 | skills |

## 11. Hand-back material

**Five old rules with the strongest "it worked" evidence**

1. **FB5 / AG8: write the failing case first and keep logic in offline-tested modules.** Bugs with a spec that failed before the fix closed in one more round (git-a §3.1 five commits; git-b §4 Astra fixes), and the oracle plus mutants ended the six-round A05 (`3ddcecc8b`). The rule's gap is that the first spec must use real content and the owner's scene (GP4).
2. **RV1 / RV2: independent review before merge.** Defects found before merge in A12, A17, A18, A19 and later `ed0c842f`, `776720c0`, `5489c26d`, `368d56dc`, `f92651c1`. Reviewer runs: 61, 100% finished, 3.3% owner pushback. Limit: a diff review cannot see Studio-only or engine facts (B13, B17).
3. **AG2 / FB13 / SO5: honest verification labels.** 15 "Not Studio-verified" bodies and the lead's use of them; no false "done" claims are recorded. Limit: the label is not a stop (GP2).
4. **Blueprint first with owner approval (D-091, owner-profile review order).** Buildings made after approval needed colour reviews only, and the later village layout had 2-3 owner layout rounds but no rebuilds (git-a §3.8, git-b §4).
5. **FB11 / RV3: stop at the third patch and ask for an architect design.** B01 and B26 ended in one design after patch chains; the orchestrator calls the pattern necessary (handoff 10-10:43). Caveat: most of the evidence comes from before the rule was written (10-09), so it is practice evidence more than rule evidence.

Unwritten habit with equally strong evidence: default-off switches with identity checks and Studio A/B (HB1).

**Five biggest gaps**

1. **No measure-first rule and no measurement hygiene** (GP1, GP5): the largest source of multi-round tasks (A01, B02, B13, B01).
2. **No binding verification before "done" for perf, physics and feel** (GP2, GP4): honest labels, merged anyway.
3. **No probe rule for engine behaviour the docs do not state** (GP3): the docs-first rule of 10-10 does not close this.
4. **Rules that drift or are not delivered** (GP7, GP8): stale AGENTS.md physics line, the placement rule that sent 6.8 MB to every client, rules read in 6 of 19 sessions.
5. **Routing and ownership of design** (GP10, GP11): the architect was rarely used, quick-builder got design-adjacent tasks, nobody owned a size or complexity budget for the destruction runtime.

## 12. Coverage and questions

| part | status |
| --- | --- |
| architect, feature-builder, quick-builder, reviewer, studio-operator | done (current text and baseline) |
| roblox-architecture, luau-code-review, remotes-security, datastores, performance-profiling, gameplay-systems | done |
| mcp-studio-workflow | done (added because studio-operator loads it) |
| rules: architecture, performance, security, datastores, luau, anti-overengineering, packages, mcp-studio, content, gui, owner-profile, platform-policy, original-content | done; `character-rigs.md` not read (added 10-13, outside the agents' scope) |
| origin of each rule | baseline or commit; a decision id where the text or the commit gives one; where no reason is recorded the cell says baseline |

Questions with defaults:
1. Should the new agents be compared with the baseline text (`4a86dc544`) or the HEAD text? Default: the baseline for rework before 10-09, HEAD for what the owner would keep today. Both are in the origin column.
2. The scorecard window (30 days to 10-09) covers only the project's first 10 days; run counts are not comparable with later windows.
3. `character-rigs.md` and the craft agents (content-builder, animator, vfx-designer) are out of scope here. Default: leave them.
