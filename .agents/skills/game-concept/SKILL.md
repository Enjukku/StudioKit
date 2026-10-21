---
name: game-concept
description: Generate and pitch bold Roblox game concepts with a marketable fantasy - a title players read and think "I need to do that" or "what would happen if I did that?" - usually a proven, trending core loop given a new theme and one twist. Covers the fantasy line, title and first image, borrowing a loop without copying, diverge-then-select idea generation, the hook test (does ordinary play deliver what the title promises), the idea rubric, the owner's taste log, and the pitch set (3 pitches, 1 recommendation). Use when the owner says "pitch me games", "give me concepts", "what should we make next", "make this idea bigger", "is this a good concept", "reskin this loop", or before pre-production starts. Read by the game designer first; marketing and the trend scout read it for the promise and the opportunity record. Proposes; the owner picks.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J003. Evidence: owner research paper Part 1 (notes `knowledge/reference/game-design/01-ideation-hook.md` = **N1**, `02-preproduction-docs.md` = **N2**), fact-checks `fact-check-roblox.md` (**FR**) and `fact-check-industry.md` (**FI**). Tags as the paper gives them: **V** VERIFIED (published measurement or official fact, in its scope), **E** EXPERIENCE (studio account), **O** OPINION (the paper's or this kit's method). **Owner** = the owner's words, 2026-10-20 (J003).

# Game concept: a fantasy players want to try

## 1. When this skill starts
The owner wants new game ideas, wants an idea grown bigger, or wants a concept judged before pre-production. It answers: what does the player become and do, why would they click, which proven loop carries it, what is the twist, what is the smallest build that proves it, and which of 3 pitches the designer recommends. After the owner picks one, `preproduction` takes over.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The idea method step by step (intake, budget, generate, expand, dedupe, critic, test, pitch), the axes and techniques, the batch diagnosis | `references/idea-method.md` |
| The pitch card, the full pitch record (13 fields), the fantasy and loop sentence forms, how to present 3 pitches | `references/pitch-template.md` |
| Hook, first image, signature moment, title and thumbnail testing, the 10-item hook check, Roblox discovery facts | `references/hook-promise.md` |
| 15 breakout concepts read as fantasy, first image, loop + twist, smallest version, lesson (incl. 3 Roblox hits) | `references/case-library.md` |
| The idea rubric (4 ratings, 9 criteria), the owner's taste log, what AI-ideation research does and does not show, borrowing without copying | `references/rubric-taste-evidence.md` |
| Trend data: the opportunity record the trend scout returns | `preproduction/references/handoffs.md` §trend-scout |
| Making the first image as a picture (concept art) | `reference-images` skill, family `concept` |
| Anything players buy, roll, trade or watch in the concept | `platform-policy` skill |

## 3. Steps
1. **Intake.** Read `knowledge/design/game-profile.md` (if a game exists), the taste log (`knowledge/design/taste-log.md`), `tried-and-failed.md`, and any opportunity records from the trend scout. No trend data → ask for it (ticket) or mark every "why now" as `not verified`. *Check:* you can name the audience and the device mix you design for.
2. **Set the search budget** before generating: how many raw concepts, why that number. Record the real counts at every step (no invented quotas, N2 §5.1 O).
3. **Diverge.** Generate one-sentence concepts across 6 axes (action, role, setting, threat, social relationship, consequence) and from proven loops (C-03). No criticism yet (C-05).
4. **Expand and dedupe.** Vary the mechanism, not the words (C-06). Group by playable action and consequence; keep distinct fantasies even on the same loop. *Check:* the batch diagnosis in `idea-method.md` §4 finds more than one mechanism family.
5. **Critic pass, separate.** Rate each survivor with the rubric (FAIL / UNKNOWN / PLAUSIBLE / OBSERVED). No weighted total. Name the cheapest test for each open risk.
6. **Pick 3, recommend 1.** Write a pitch card + full record for each (`pitch-template.md`). If fewer than 3 are defensible, show the shortfall and ask for more exploration; never pad (S15 O). *Check:* each pitch passes the title test (C-02) and names its proven loop and its twist.
7. **Present** in one message to the owner (`ste-writing`): the 3 cards, the recommendation with its tradeoff and strongest objection, and the decision asked for. Files go to `knowledge/design/concepts/<concept-id>.md`, or the path the brief names (the brief wins).
8. **Record the owner's choice** with the owner's words in the taste log and `decisions.md`, including what was rejected and why. Then start `preproduction`.

## 4. Craft core (what separates a great pitch from a list of reskins)
| ID | Practice | Evidence |
| --- | --- | --- |
| C-01 | **Fantasy first, as a role with a consequential verb.** "As [role], I [verb] so that [change], while [pressure]." Features come after. A genre label is not a fantasy | S07, T7 field 3 O (N1, N2) |
| C-02 | **The title is the fantasy.** A short verb phrase with an outsized object or a stake that makes the reader picture the action and ask "what happens if…": *Destroy the Sun*, *Build a Dam to Save the City*, *Fly or Die*. Test: a stranger who reads only the title can say what they will do | Owner; Roblox hits use verb-object titles (*Grow a Garden*, *Steal a Brainrot*), names V, pattern O |
| C-03 | **Proven loop + new theme + one twist.** Borrow the loop's functional structure; the theme changes the role, the emotional meaning, the social context or the first-image appeal; the twist changes one decision or consequence, written as a rule: "when X, the player must choose Y, and Z follows" (not a feature noun). The twist need not be new tech | Owner; T8 O; B4 O |
| C-04 | **Search decisions and consequences, not reskins.** Two ideas with the same action, reward and escalation are one idea with two skins. Keep both only if the fantasy, role or social meaning gives the audience a different reason to care | S03 O; N1 §3 |
| C-05 | **Diverge, then select, in separate passes.** Splitting generation from selection raised goal-path discovery in one small 2026 study (GPT-5.4 27→38 of 56 paths), but originality fell for another model. Criticism before alternatives exist narrows the batch | A08 V (small, model-specific) |
| C-06 | **Expand by mechanism.** Per seed vary: what the player can do, what can go wrong, who changes the outcome, what persists. Use inversion, distant analogy, a constraint, a counterfactual, an anti-cliché pass | N2 §5.1 step 3 O |
| C-07 | **Quality next to novelty.** Turning up randomness raised novelty and cut quality in small-model tests; an AI novelty score swung 52.6 points between near-identical prompts. Never present an AI score as a fact; judge each pitch on the rubric | A02 V, A01 V (see FI) |
| C-08 | **First image.** Exactly one camera view (alternatives go on a separate variant line): readable player action, scale relationship, immediate stakes. If you cannot describe the thumbnail, the concept is not ready. When the brief allows images, render it (`reference-images`, `concept`) and label it concept art | T7 field 5 O; HC01 O |
| C-09 | **Signature moment through ordinary play.** Setup → player decision → readable consequence → payoff, reachable with normal inputs, not only in a trailer. The opening teaches the verb the title promises | H6, HC03, HC04 O |
| C-10 | **Smallest version keeps the decisive action.** Cut breadth (content, world size, modes) before the action, relationship or consequence that makes the fantasy different. Split feasibility: the defining interaction vs the production burden around it | S11 O; N1 N2-N3 O |
| C-11 | **Name the failure.** The strongest reason it may fail and the cheapest test that could show it. Keep a bold, uncertain concept alive when a cheap test can settle its risk | S05 O; T7 field 11 |
| C-12 | **Learn taste without narrowing.** Log what the owner picked, rejected and why; tell apart "wrong fantasy" from "wrong scope", "weak pitch" or "too risky". Keep close-fit, adjacent and wildcard ideas in each batch; past taste is never a permanent veto | S06, T3-T7 O |
| C-13 | **Separate measures stay separate.** Novelty, owner taste, market evidence and policy compliance are different ratings. Do not add them into one score | rubric rules O; D2 O |
| C-14 | **Evidence or nothing.** Every number in a pitch (players, growth, sales) has a source and a date; peak concurrent users are not daily users; a reach figure (visits, concurrency) never supports a design claim; a trend can be temporary. No source → write `not verified`. "Number" means a measured quantity about players, money, time or performance; names, ids and values given in the brief are not | R2 O; FR |

## 5. Rules (final check, short)
- The owner decides. You recommend exactly one concept and say its tradeoff; never claim the owner or another lead approved anything without a decision-log line.
- 3 pitches when 3 are defensible. Never pad with known weak ideas; never invent player counts, trends, retention or revenue.
- Borrow loops, never expression: no other game's characters, art, names, music, text, branding or confusingly similar look; no franchise without a licence. Roblox's IP and repetitive-content rules apply (`platform-policy`).
- Anything players buy, roll or trade in a pitch is checked against `platform-policy` before the pitch goes out. A pitch never depends on paid random items or ads to deliver its fantasy.
- Concepts for young audiences: no fantasy that needs harassment, exploitation or mature content to work.
- Numbers, names and content are PROPOSAL until the owner confirms (`knowledge/design/open-questions.md`).

## 6. Self-check before returning
- [ ] Every pitch has: title, one-line fantasy, first image, proven loop named + twist, signature moment, smallest version, why now (sourced or `not verified`), failure hypothesis + cheapest test.
- [ ] The title test passes for each title (a reader can say the action from the title alone).
- [ ] The 3 pitches are different mechanism families or different fantasies, not 3 skins of one idea.
- [ ] One recommendation, its tradeoff, its strongest objection, what evidence would change it.
- [ ] Actual counts recorded and recounted from the tables (raw, expanded, deduped, critic survivors); no weighted total; every UNKNOWN or FAIL has its cheapest test.
- [ ] Survivors not pitched are listed with the rubric reason; the reserve is named.
- [ ] Policy, rights and audience checks done or listed as blocking.
- [ ] Owner message in `ste-writing`; files in `knowledge/design/concepts/`.

Project overlay: if `knowledge/overlays/game-concept.md` exists, read it after this file; it wins for this game.
