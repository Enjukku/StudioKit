---
type: job
scope: universal
status: active
updated: 2026-10-23
source: J021 fit study, 5 Sonnet-high read-only agents (engineering and support; visual makers A; visual makers B and sound; design and data; plumbing), 2026-10-23; lead spot-checks of 15 citations, all held
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-23

# J021 implementation map: which change goes into which agent

## 1. The four changes, as corrected by the fit study
| ID | Change (final form) | Correction from the study |
| --- | --- | --- |
| C1 | **Target experience line** = `<named kind of fun>: <what the work must make the player do or believe, one sentence, no number>`. The number stays in the success test. The goal word still comes from the kind of fun. | Do not redefine "target experience" (about 20 quote sites, G-01, `gates-and-feedback.md` §1 goal word). Never call the sentence a "verb": VFX `read-card.md:11` and sound `cue-card.md:56` already use "Verb" for the mechanic word that timing list, frame script and cue card match on. |
| C2 | **Outside source chosen from that sentence, naming the method**: the field that already makes people do or believe this; the method written as an action the expert does ("holds on the reaction"), not a topic ("horror films"). Shared guard: the role's caps, safety, truth and platform rules win; never a pressure method (scarcity, streaks, casino); borrow a method, never a voice. | The method line must be checkable (DR2, BR4, P-04, PL-08, MR-02). The D1 lead picks the field; the lead's brief never dictates it. |
| C3 | **The bar** = the role's existing book checks plus the brief's `stop` and `checks`, made explicit. `stop` has `floor:` (the Success test, quoted) and `bar:` (observable signs, no method); top-level, never under `fixed`. Hand-back `checks` gets a `BAR` row: pass = bar met (evidence); fail or not verified = floor only (reason). Floor only is a valid finish, never a blocking finding, opens no round. A specialist may raise the lead's bar, never lower it. Data roles: "cannot tell yet" or "no qualified opportunity" with evidence = bar met. | Most books already hold the bar as stop criteria or self-review lines (SR, AR, QS, DR/RD, P-lines, MR, §I). So C3 is a label, not a new step. Scope: M and L work that makes a deliverable. Fallback ("name methods and tools") only when no book covers the task type. |
| C3a | **Name, never build**: what a top professional would add that the brief does not ask for goes to `proposals`. | Duplicates rule 4 and rule 17 for most roles, and harms some (rigger, builders, scout). Goes only into the role files where the study found real value (§2). |
| C4 | **Belief check at intake, before D1** (not inside D1): the lead spawns the analyst (Sonnet medium) when T1 M/L job · T2 the owner's words claim what this game's current players do or feel and a different answer would change the direction · T3 no fresh analyst reading of it · T4 data exists (universe id, published, key set, dashboard minimum). Verdict: supported / not supported / cannot tell yet; evidence, never a decision; the owner's words stand by default. No data: "belief (untested)" + cheapest test in the G1 packet, zero cost. | No recipe or workflow has an analyst slot in D1; running beside D1 hides the result from independent proposals. The game-profile starter has no live-data field. Today no game has data, so C4 never fires yet. |

## 2. Per agent
Verdicts: **A** adopt, **a** adapt (small wording), **—** skip (covered or no fit), **X** harmful (keep out; the shared rule excludes it).

| Role | C1 | C2 | C3 bar line | C3a extras | C4 | Where (main edit) | Harm to avoid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| art-director | a | **A** (home) | a | a | — | `art-direction` step 1, step 3; `rounds.md:24` (scope to direction rounds); DR1, DR2, BR4, HB2; role step 1 | image-budget creep; a scarier-than-true look over clarity |
| film-director | a | **A** | a | a | — | `film-direction` :15, :39 step 4; `film-craft` step 3, P-04; `beat-sheet.md` rows :23, :27; role step 1 | more shots after `stage: locked`; imagery instead of mechanism (D-23) |
| modeler | — | — | a | a (high effort only) | — | `asset-record.md:45`, `read-and-form.md:22` stop row; role step 2 | triangles and passes past budget; "improving" the approved design |
| character-rigger | — | — | — (release lines already are the bar) | **X** | — | none | extra joints and controls reopen the animator's K2 sign-off |
| animator | — | a (read-carrying clips) | a | — | — | `body-and-species.md:56`; role step 1 | polish past the check-in freeze; invented "pro" timing |
| vfx-designer | — (PL-01 already quotes) | a | a | a (optional) | — | step 3(a), PL-08; `read-card.md:24` stop row | flash limits and tier caps broken by a borrowed method; more layers |
| environment-designer | a | a | a | — | — | `read-plan.md:10`, :23, :31, :33; RD1, PS5 | a borrowed method that changes routes (E-02: game-designer's) |
| ui-ux-designer | a | a (atypical option only) | a | — | — (S-07 covers) | `ui-design` step 1, step 5; S-48; role :14 bar made observable | style drift from the style book; core controls moved (D-21) |
| sound-designer | — | — (for now) | a (bar = `aim` targets) | **X** (cannot hear) | — | **no edit until the other chat commits** | more regenerate rounds; listening requests |
| marketing | a | a + truth filter | a | — | **A** (consumer) | `image-pipeline.md:10-11`, MR-02; `marketing-craft` step 3 | false urgency or scarcity; extra generations |
| game-designer | a (P-16) | a | a | — (P-21 forbids widening) | consumer | `preproduction` P-16; `game-concept` step 3, C-17; claim ledger step 3 | invented numbers in the sentence; analyst on every claim |
| progression-designer | — | **X** | a | — | consumer | `progression-design` step 1 | a metaphor replacing `sim.py` |
| live-ops-designer | — | a (atypical option) | a | — | a | `live-ops-design` step 3; `live-ops-craft` step 3 | pressure methods (L-09); promises past capacity |
| analyst | — | **X** | a + guard | — | **A** (runs it) | new `analysis-craft` §3.7 (appended); role flow line | a verdict on thin data to meet a deadline |
| trend-scout | — | **X** | — | **X** | — | none | method hunts that need scraping |
| architect | — | — (optional, rejected: exotic patterns) | a | a | — | role step 1, "Before you hand back" | plan growth (90 lines, not 400) |
| feature-builder | — | — | a (pointer: SR-01..19) | — (rule 17 covers; risky) | — | "Before you hand back" | unasked hardening |
| qa-lead | — | — | a (pointer: principle 18) | — | — | "Before you hand back"; trace step (rows past the brief are proposals) | test inflation (rule 11) |
| performance-engineer | — | — | a (pointer: budget row) | — | consume only | step 1 | extra measurement rounds; pulling player data itself |
| reviewer | — | — | guard line only | **X** | — | step 4: "a floor-only line with a reason is not a finding" | bar findings become nits and rounds (rule 18) |
| quick-builder | — | — | **X** (excluded) | **X** | — | none | an S task turned into M |
| studio-operator, researcher, doc-keeper, explore | — | — | **X** (excluded by tier) | **X** | — | none | extra captures; invented records; judgment in a scout |

## 3. Shared plumbing (all from the plumbing study; no script, schema or hook change)
1. `AGENTS.md` §4: one bullet (about 110 words) with C3 and its scope: M and L work that makes a deliverable; not S work, quick-builder, `research` or `mechanical` tiers, or reviews. AGENTS.md reaches every subagent and every saved-workflow agent (journal checked) and survives compaction. Size: 140 of 200 lines now.
2. `rules/messages.md`: `stop` = floor + bar (:87); `BAR` in the hand-back example (:102) and the evidence rule (:113); §9 check (:184).
3. Templates: `intent-brief.md` (stop block), `job-card.md` (target-experience hint, Belief check row, stop note; keep the "Status" and "Gates" names: `compact_context.py` parses them), `gate-packet.md` (belief row, BAR lines), `evidence.md` §4 (2 rows: BAR met / floor only / none; proposals raised / taken), `status-block.md`, `direction-sheet.md:19`.
4. `orchestration`: SKILL §1 step 1 (C1, C4), §3 step 3, §4 step 1 (C2), §8, §14; `gates-and-feedback.md` §2, §3, §7; `briefs-and-handoffs.md` §1 and the example brief (fix: `stop` sits under `fixed` at :86 today).
5. `knowledge/design/game-profile.md`: a "Live data (universe id, launch date; blank = no player data yet)" row.
6. Then `python tools/sync_harness.py` (check first: sound-design edits from another chat are uncommitted) and `python tools/verify.py`.

**Do not touch:** `handback.schema.json` and the inline schemas in the 7 workflows (a harness test compares them); the hooks; `CLAUDE.md`, `rules/assistants/claude.md`; `knowledge/design/decisions.md` (game scope); sound-design files; section numbers.

## 4. Open choices for the owner
| # | Choice | Recommendation |
| --- | --- | --- |
| O1 | A missed lead-set bar is never a blocking finding | Yes (otherwise repair rounds grow) |
| O2 | Add a `bar` field to `keep()` in the 7 job workflows (7 identical one-line edits + workflow tests), so the lead sees BAR lines in workflow runs | Yes: without it the effect cannot be measured on workflow-run jobs |
| O3 | Phase 2 (the per-book wording in §2) now, or after one real job on phase 1 | Now for C2 mirrors (workflow D1 agents only read their own books); per-role C3 pointers after one real job |

## 5. Found in passing (follow-ups, not in this job)
- Saved-workflow briefs carry no `stop` or `budget` key, against `rules/messages.md:87` and :184 (all 7 `brief()` functions).
- `.agents/roles/analyst.md:27` cites an analyst slot in the feature recipe's direction stage that `job-types.md` does not have.
- Skill descriptions at the 400-character cap: `rigging-craft` 400, `animation-design` 399, `architecture` 399.
