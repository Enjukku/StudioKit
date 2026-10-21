---
name: preproduction
description: Grow a concept the owner picked into a full game design and write it as documents every agent can build from - pillars, lead reviews, feature specs, tuning tables, per-craft briefs. Use after the owner picks a concept, for "let's build this one", "plan the game", "write the GDD", "brief the team", "spec this feature", or when a decided change must reach every craft.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J003. Evidence: owner research paper Part 1 §3-§7 (notes `knowledge/reference/game-design/02-preproduction-docs.md` = **N2**); `rules/messages.md`; owner 2026-10-20 (J003). Tags: **V** VERIFIED, **E** EXPERIENCE, **O** OPINION; **Owner** = the owner's words.

# Pre-production: from a picked concept to a design everyone can build

## 1. When this skill starts
The owner picked one concept (`game-concept`), or a decided game needs its design written down or changed. It answers: in what order the design grows, who joins when, what the owner decides at each step, which documents hold the truth, and what each craft gets as exact contract vs open craft. Output: the design baseline in `knowledge/design/` and one brief per craft. Production starts only after the owner approves the baseline.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The growth steps one by one, the seven lead reviews, what the owner decides at each, the readiness checks | `references/growth-order.md` |
| Document set and paths, states, the vision record, pillar sheet, feature spec, tuning table, decision record, uncertainty register | `references/documents.md` |
| A brief to each lead (art director, architect, marketing, trend scout, UI, VFX, sound, animation, levels): what is exact, what is open, full examples | `references/handoffs.md` |
| Loops, systems, economy, social, review checklists for the design you are writing | `game-design` skill |
| World, levels, routes, encounters | `level-design` skill |
| Brief and hand-back format (binding) | `rules/messages.md` |

## 3. Steps
1. **Open the job.** L job folder `knowledge/jobs/<job-id>/` (lead's `orchestration` skill). Move the picked concept record from `knowledge/design/concepts/` into the vision record (`documents.md` §2). *Check:* the fantasy line and title are copied word for word from the approved pitch.
2. **Grow in order, one owner decision per step** (`growth-order.md` §1): fantasy and promise → pillars → style direction → key characters and moments → world → core loop → features → content. Each step adds the documents its next step needs, nothing more; untested detail stays open (N2 3.3 O).
3. **Bring leads in early** (`growth-order.md` §2): trend scout and marketing at step 1, architect from step 1 for risky claims, art director at step 3, craft leads at the first playable moment. Each early review ends with: the decision, its owner, affected files, open questions, next evidence (N2 2.3 O).
4. **Write contracts, not prose.** Exact what another craft cannot safely reinterpret (rules, states, permissions, timing relations, units, resource changes, persistence, failure recovery); leave expression, art treatment and code structure to the craft lead (N2 5.4 O). Unknown value → `TBD`, who decides, the test. *Check:* `rules/messages.md` §6 checks pass on every brief.
5. **Brief each craft** (`handoffs.md`) with the same fantasy, pillar, feature ids, state names and data revision in every brief.
6. **Readiness review** (`growth-order.md` §4): receivers restate the behaviour, compare readings, review one integrated moment, check device, network, social and policy assumptions. The owner approves the next commitment, not a promise that the game will be fun.
7. **Keep it alive.** A change goes through the change review: impact map, versioned decision, every affected brief updated in the same pass.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| P-01 | **Stage purposes, not a waterfall.** Concept clarifies the experience; a pitch asks for a decision; prototypes attack risky assumptions; pre-production joins the experience to a way of making it; a slice shows the quality can be made repeatably. Bad evidence can send work back without killing the fantasy | N2 3.2 O |
| P-02 | **Prototype whether, then how.** A prototype tests whether to make the game; pre-production also tests how. Throwaway code is fine for learning; it does not prove production architecture | S09 E (Riot, P02-P03) |
| P-03 | **Art early, cheap.** Art direction can shape the concept while prototype art stays cheap. Concept art answers 6 questions: silhouette and role, scale, readability in the real camera, key materials, character relationships, the signature moment. A paper concept that failed to read in first-person 3D changed (Blizzard) | S10 E (P04, P12); N2 3.6 O |
| P-04 | **Pillars are decisions.** Each pillar: what the player experiences, which decisions it favours, which tempting feature it rejects, and the observable sign. No optimal pillar count exists | S12 O; N2 T1 |
| P-05 | **Contracts exact, expression open.** Exact: rules, states, permissions, timing relations, units, resource changes, persistence, failure recovery. Open: art treatment, animation expression, sound character, engineering architecture | S13 O; N2 5.4 |
| P-06 | **One source for every number.** Tuning values live in one versioned data source with units, rationale, uncertainty and a test; briefs cite the key and the data revision, never a hand-copied number | S14 O; AGENTS.md §2 (content is data) |
| P-07 | **Promise ledger.** Every title, image and trailer claim maps to a playable feature or an explicitly unbuilt concept | N2 §2 marketing O |
| P-08 | **One state vocabulary for all crafts.** Agree which signals mean anticipation, commitment, success, failure, danger, recovery; review one representative interaction with all crafts together, not each craft alone | N2 §2 craft leads O |
| P-09 | **Behaviour test ≠ experience test.** A build can meet every written rule while players stay confused or bored; keep both checks in every spec | N2 5.2 O |
| P-10 | **Cut breadth, keep the decisive action.** When scope must shrink, cut content, modes and world size before the action, relationship or consequence that makes the fantasy different | S11 O |
| P-11 | **Propose with one recommendation.** One recommendation, the player outcome it protects, the evidence, the strongest objection, what would change your mind. Alternatives only when they are a real experience, cost or risk tradeoff | N2 6.2 O; owner |
| P-12 | **Sort a disagreement before arguing it.** Empirical → a test that can tell the options apart. Technical → a measured constraint and the specialist's alternatives. Taste and ambition → the owner. Scope and risk → an explicit decision. Safety, legal, platform → a constraint to explain, never a score to average | N2 6.3 O |

## 5. Rules (final check, short)
- The owner decides creative direction and resource tradeoffs; leads raise risks; you record agreement. Never invent a lead's approval; silence is not consent (N2 2.3 O).
- Locked decisions live only in `knowledge/design/decisions.md` with the owner's words; everything else is PROPOSAL and listed in `open-questions.md`.
- Every brief follows `rules/messages.md`: `<intent>` + `<spec>`, `fixed` values with a source, `open`, every rule restated in full words, skills named, runnable checks, sent whole.
- Paid random items, purchases, ads, chat, player data, mature or franchise themes: `platform-policy` at design time. Saved data: `data-saving`. Client-callable features: `networking-security` (through the architect). New player steps, currency flows, quit points: `analytics`.
- Never invent durations, retention targets, prices, content counts or scoring weights to complete a template (N2 D8 O).
- Write only in `knowledge/design/` and the job folder; code, data files and assets belong to their owners.

## 6. Self-check before returning
- [ ] Each growth step has its owner decision recorded (or pending in the digest with a default).
- [ ] Every document traces to the same fantasy line and pillars; the opening teaches the decisive verb; systems support the core loop, not genre habit (N2 §5.3).
- [ ] Every feature spec has the 15 fields, acceptance tests on 5 paths (success, boundary, interruption, denied, multiplayer disagreement) and an experience test.
- [ ] Every number is a tuning key with units and provenance, or `TBD` + owner + test.
- [ ] Every craft brief uses the same state names and data revision; every craft listed in `handoffs.md` that the game needs has a brief.
- [ ] Uncertainty register current: each open assumption has an owner and a test.

Project overlay: if `knowledge/overlays/preproduction.md` exists, read it after this file; it wins for this game.
