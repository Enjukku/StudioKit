> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `game-concept`. Sources: N1 §9 (rubric), §6 (taste), §4 (AI evidence A01-A13), §7 (borrowing), N2 §5.4 (do-not list); FI (fact-check of the AI numbers). Tags as in SKILL.md. Revised by J018 maker game-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (RB1, RB4, goal questions, closed directions).

# Rubric, taste log, AI evidence, borrowing

## 1. Idea rubric (ordinal, O)
Four ratings: **FAIL** (an observed contradiction or unmet requirement) · **UNKNOWN** (evidence missing) · **PLAUSIBLE** (coherent reasoning, no player observation) · **OBSERVED** (a scoped observation supports it; not proof of market success). For readiness, FAIL and UNKNOWN both block; FAIL needs a redesign, UNKNOWN needs a test (J003 addition; the paper sets no order, N1 W24).

Rules: no hidden weights, no total, no average. Policy and safety are rated apart from creative appeal and are never traded against it. Every UNKNOWN or FAIL names its cheapest test.

Anchors (J003 G2 lesson):
- **RB2:** FAIL only when the twist changes no decision or consequence compared with the reference game. A title or naming problem is a naming fix, not an RB2 FAIL.
- **RB6:** with no taste-log row about this kind of concept, RB6 stays UNKNOWN and is not used to rank. The owner's example titles show the bar for boldness, not a taste verdict on a concept.
- **RB9:** OBSERVED = dated, like-for-like evidence that the loop holds players now (a time-weighted or 7-day mean from the trend scout, or an official named mention plus a matched-window count). PLAUSIBLE = one snapshot, or an official mention without numbers. UNKNOWN = memory or undated. Never compare one off-peak snapshot with an event peak to claim growth or fade. A 7-day peak is like-for-like only with another 7-day peak; a 7-day mean is preferred. Read every number with the trend scout's labels (`market-trends`: official, third-party sampled, third-party estimate, derived).

| # | Criterion | State | Raises the rating | Reject or investigate when |
| --- | --- | --- | --- | --- |
| RB1 | Fantasy | the role, the consequential verb and the target experience | players say in their own words what they want to do | the pitch is a genre label, a list of references, or "fun" with no named experience |
| RB2 | Distinctiveness | what the twist changes: mechanism, fantasy, relationship or audience meaning | comparison with named alternatives; an independent review | no clear reason the audience would value the new fantasy or twist |
| RB3 | Hook delivery | the action the title and first image promise | a playable encounter produces it without scripted tricks | marketing shows an action the loop does not support |
| RB4 | Agency and repeatability | which choices change outcomes; what changes on repeat | observed choices, retries, strategies, reasons to return | the intended agency, expression, anticipation, comfort or social value is missing; the loop has a goal but no opposition or no real decision |
| RB5 | Feasibility | the cheapest build that keeps the decisive action | device and network risk probes; art production estimates | the small version removes the reason the concept is interesting |
| RB6 | Taste fit | the owner's relevant preferences and the deliberate novelty | the owner's explicit reasoning about this concept | an inferred preference is treated as a permanent veto |
| RB7 | Social and safety fit | how players affect each other; how abuse is handled | tests with the intended party and stranger setups | the fun needs harassment, exploitation or prohibited content; competition lacks counterplay and recovery |
| RB8 | Evidence quality | source, date, sample, scope, unknowns | independent observations; reproducible results | popularity, an AI score or a thumbnail preference is called proof of fun |
| RB9 | Loop proof (J003 addition) | the proven loop, its reference game, and dated evidence it holds players now | a trend-scout record; a dated chart or official number | "proven" rests on memory, an undated claim or a peak-day number |

## 2. Taste log (`knowledge/design/taste-log.md`, create it if missing)
Frontmatter `type: profile`, `scope: game` (or `universal` for studio-wide taste). One row per owner choice:

| date | compared concepts | owner's pick | owner's words | reason class | later reversal |
| --- | --- | --- | --- | --- | --- |

Reason class (T4 O): **fantasy** (does not want this experience) · **scope** (too big now) · **pitch** (badly explained) · **risk** (technical or production) · **market** (audience evidence) · **other**. Only a fantasy rejection says something about taste; the others say something about timing or execution.

Rules (T3-T7 O):
- Keep close-fit, adjacent and wildcard ideas in each batch; no fixed proportions.
- Ask about contrasting experiences ("tense or cosy? alone or with friends?") rather than repeating the owner's favourite words. Every question names the goal ("which feels most like breaking the sun?"), never "do you like it?".
- A closed direction (owner reason class fantasy) is logged for the job and not re-pitched without new owner words; a scope, pitch, risk or market rejection may return with the change stated.
- When the owner prefers a concept that current audience evidence does not support, show the mismatch plainly. The owner still decides.
- A proven loop with a new theme can be a strong concept when the theme changes the role, the emotional meaning, the social context or the first-image appeal (T8 O). Judge it for the owner's audience, not by how unfamiliar its rules are (T9 O).

## 3. What AI-ideation research shows (and what it does not)
Every result belongs to one named model, task and judge (S02). Most tested science, product or writing ideas, not games. "Older model" = the paper's label. Numbers: FI verdicts.

| Id | Finding (model, task) | Number | Limit |
| --- | --- | --- | --- |
| A01 | a judge-prompt change moved GPT-5.4 pairwise novelty accuracy (research ideas) | 52.6 points | one AI novelty score is unstable |
| A02 | temperature ×1.5 on four 7-8B open models | novelty +10.7 %, quality −15.4 % (relative proxies) | small models |
| A03 | role-split agents + cross-domain retrieval (IdeaScientist), 277 research problems | 77.7 vs 68.7 (Claude-4.8-Opus); 71.9 vs 69.5 (GPT-5.4), Qwen judge | proposals never built |
| A04 | optimised persona sets, Gemma-4-31B-it, Alternative Uses task | diversity +78.8 %, originality +26.1 %, creativity +13.9 %; validity flat; utility about −5 % | one model, automated judging |
| A05 | preregistered metaphor study, 644 writers, 351 evaluators | AI first ideas lowered group diversity; AI refining the writer's own idea kept it | older model; metaphors |
| A06 | personalised vs aggregate judges, product ideas (gpt-5-mini appendix) | better on need validity, worse on competitive advantage | not game demand |
| A08 | generation split from goal-constrained selection, 10 scenarios | paths 27→38/56 (GPT-5.4), 30→41/56 (Sonnet 4.6); Sonnet originality fell | small, LLM-judged |
| A09 | structured analogy transfer (Qwen3-14B, 400 science cases) | novelty win rate up, usefulness down | science, older model |
| A10 | personas widened idea coverage (GPT-4o, fitness products) | 88 → 210 category combinations (humans 206) | older model, one domain |
| A11 | fine-tuned predictor of one person's text choices | 75.8 % own choices (different target from the 67.7 % majority figure) | fine-tuned, short text |
| A12 | Verbalized Sampling (2025 models) | semantic diversity 1.6-2.1× | older models |
| A13 | 43 researchers executed LLM vs human research ideas (~103 h on average) | AI ideas lost more score after execution | Claude-3.5-Sonnet, NLP, gap not significant per idea |
(FI verdicts: all confirmed or partly; A07 "five tasks" dropped as inferred.)

What the studio takes from it (O): separate generation from criticism; use contrasting perspectives; refine seeds instead of accepting first outputs; check quality whenever novelty rises; never trust a single AI novelty score; never claim an attractive AI proposal survives execution (older-model study, A13: AI ideas lost more score after being carried out); test locally before adopting a method.

## 4. Borrowing a loop without copying (N1 §7)
- The US Copyright Office separates a game's idea and method of play from its protectable expression. US guidance only, not worldwide clearance (B1 V, L01).
- Roblox prohibits unauthorized use of others' IP under its own rules (B2 V, R18; FR).
- The L01 page itself says written rules and artwork can be protected; the paper extends this to characters, code, music, text, branding and confusingly similar presentation (B3; extension = OPINION, FI IC31). Treat all of them as off limits.
- Method (B4 O): (1) describe the borrowed functional structure; (2) name the new decision or consequence; (3) make original expression; (4) review any rights-sensitive resemblance before release.
- A loop clone, a renamed franchise or a parody is never "automatically safe" (B5 O). A licensed hit is evidence about that product, not permission to use its IP (B6 O).

## 5. Do not (N2 §5.4 O)
Declare a creativity method universally best from one narrow study · merge novelty, taste and market demand into one score · claim an AI proposal survived execution · copy a hit's expressive identity · let a novelty critic kill every unproven premise before a cheap test exists · postpone the game's identity while polishing parts · confuse a prototype, a polished demo or a good pitch with production readiness · invent durations, retention targets, weights, content counts or approvals to fill a template · promise in marketing what ordinary play cannot deliver · leave contradictory rules or unexplained values for builders to settle.
