> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `game-concept`. Sources: N1 §3-§7, N2 §5.1 (owner research paper Part 1). All steps are **O** (a configurable studio procedure, not a proven optimum); evidence rows keep their tags.

# Idea method: from opportunities to 3 pitches

## 1. The funnel and its counts
Record the **actual** count and budget at every step, recounted from the step's own table before you report it. The N values are placeholders, never targets. The only fixed count is the owner's: 3 final pitches, then 1 chosen concept (N2 §5.1, owner).

| Step | Do | Record | Count |
| --- | --- | --- | --- |
| 1 Intake | Take opportunity records from the trend scout (fields in §2). Reject unsupported trend claims, **not** unusual fantasies | usable records | N1 ≤ N0 |
| 2 Budget | Set the raw-concept budget from review capacity and time **before** generating; write who set it and why | budget, reason | N2 |
| 3 Diverge | One-sentence concepts across the 6 axes (§3) and the proven-loop table (§5). Unranked. No criticism | raw list | N2 |
| 4 Expand | Per promising seed vary the 4 mechanism axes (§3) with the 5 techniques. Expand mechanisms, not synonyms | candidates, mechanism families | N3, F3 (measured) |
| 5 Dedupe | Group by playable action + reward + escalation. Merge true duplicates; keep distinct fantasies on one loop; keep an odd candidate whose risk is cheap to test | distinct candidates | N4 ≤ N3 |
| 6 Critic | Separate pass (a fresh context, not the generator's thread): rate every candidate on the rubric (`rubric-taste-evidence.md` §1). Name the evidence gap and the cheapest test | ratings, gaps, tests | N5 |
| 7 Owner / tests | When taste or risk tolerance decides the ranking, ask the owner or ask for a test. Report test sample, build, variant, measures, negative results. Never call an untested candidate validated | tested or explicitly untested | N6 |
| 8 Pitch | Exactly 3 pitches if 3 are defensible; else show the shortfall. One recommendation with its tradeoff; keep a materially different alternative when evidence cannot decide | 3 pitch cards + records | 3 |
| 9 After the pick | Replace the funnel with an uncertainty register and start `preproduction` | register | 1 |

"Independent critic" (step 6): this kit defines it as a separate subagent or a fresh pass that sees only the candidate list and the rubric, not the generation reasoning (J003 addition; the paper leaves it undefined, N2 W09). Put every fact the critic needs into `candidates.md` (trend numbers with sources, the owner's existing games, rights notes); the critic reads nothing else. If you cannot start a subagent (the game-designer role has no Agent tool), write the candidates to `candidates.md` first, then rate them in a separate pass that reads only that file and the rubric, and state the limit in the pitch set; the lead may re-run the critic in a fresh context. A critic must not kill an unproven premise only because it is uncertain (D5 O, A08 V).

## 2. Opportunity record (from the trend scout)
The trend scout's weekly report (`templates/trends/weekly-report.md`, skills `market-trends` and `trend-scan`, built in J004) carries these records and its top 3 opportunities; read it first when it exists.

7 fields per record: observation date · the rising player behaviour · audience · evidence (source, metric, date) · comparison period · outside trigger (event, season, meme, update) · alternative explanation (N2 §5.1 step 1 O). Add for this studio: the **proven loop** the behaviour runs on, and whether the signal looks lasting or temporary (J003 addition). A trend claim without a dated source is rejected; an unusual fantasy is not.

## 3. Axes and techniques
| Generate across (6) | Expand each seed by (4) | Techniques (5) |
| --- | --- | --- |
| action · role · setting · threat · social relationship · consequence | what the player can do · what can go wrong · who changes the outcome · what persists | inversion (reverse role, information, reward or failure) · distant analogy (map an outside mechanism to a player action) · constraint (remove a default action or resource) · counterfactual ("what if the sun could be destroyed?") · anti-cliché pass (ban the familiar mechanism for one round) |

Human methods and their failure signs (N1 §5):
| Method | Use | Failure to watch for | Tag |
| --- | --- | --- | --- |
| Generate broadly, then cut | a set budget, then a separate selection | near-duplicates posing as breadth | E (Nintendo, Double Fine) |
| Combine distant ideas | map an outside mechanism to a player action and consequence | a list of unrelated theme nouns | V (science-analogy studies; game transfer untested) |
| Constraints | remove a default action or resource, trace the result | a constraint that removes the central fantasy | E |
| What-if / inversion | reverse roles, information, rewards or failure, then model it | surprise with no playable cause and effect | O |
| Borrow trends and real events | borrow the human behaviour or tension | short attention mistaken for lasting play | V observation / O inference |
| Name clichés to avoid | ban familiar mechanisms for a round | incoherence rewarded for being unusual | O |
| Separate generator and critic | keep alternatives, then inspect | a critic that rejects novelty for being uncertain | V (A08, small) |

## 4. Diagnose a batch before you trust it
1. Group the batch by **action**, **information**, **resource**, **relationship** and **consequence** (N1 §3 O).
2. Groups nearly identical → ask if the fantasy, role or social meaning still gives the audience a different reason to care. Cosmetic change proves neither value nor worthlessness.
3. Likely causes of sameness (O, not shown for current models): the same familiar references in the prompt; rewarding polished averages; critique before alternatives; novelty defined only by vocabulary; typicality bias in the model (A12 V attributes part of convergence to it).
4. Fixes that have some evidence: contrasting player perspectives or personas when generating (A04 V, one model; A10 V, older model, raised idea coverage); refining a human seed rather than accepting the first AI idea (A05 V, older model: first AI ideas compressed group diversity). Re-test locally before adopting any method (§6).

## 5. Proven loops: where the loop comes from
A loop counts as **proven** when dated evidence shows it holds players now (trend-scout record, Roblox charts with date, a named current hit). Name the reference game and the loop in one sentence, then the change.

| Loop family (examples, not a whitelist) | Reference shape | Twist questions |
| --- | --- | --- |
| Grow / tend / harvest, change between visits | *Grow a Garden* (FR) | What grows that nobody expects? What does tending protect or destroy? |
| Collect, show off, risk losing it to others | *Steal a Brainrot* (FR) | What is contested? Who can take it, and how do I get it back? |
| Prepare by day, survive the night with friends | *99 Nights in the Forest* (FR) | What is the threat? What does preparation look like in this theme? |
| Gather → upgrade → bigger target (simulator) | many Roblox simulators | What is the outsized target (the sun, a city, a mountain)? |
| Obby / route to the top | many Roblox obbies | What makes falling or flying the fantasy (Fly or Die)? |
| Build to withstand an event | tycoon and disaster games | What disaster, and what does the build protect (a dam saves the city)? |

The table is a starting set. The trend scout's records replace it with dated evidence; never cite a player count from memory.

## 6. Reusing an AI-ideation result (N1 §4 O)
- Reproduce the method with the reported model setup before adopting it; a 2026 paper does not make its model current.
- Hold the brief, model version, budget and evaluation format constant; compare against a competent baseline; keep the rejected ideas.
- Judge mechanism-family spread, owner preference and prototype survival as three separate results.
- What the 13 AI studies show and their limits: `rubric-taste-evidence.md` §3.
