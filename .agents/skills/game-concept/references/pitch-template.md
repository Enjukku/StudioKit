> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `game-concept`. Sources: N2 §5.2 (T7 concept pitch, 13 fields, O), N2 §4 (working with a creative director, O), owner 2026-10-20 (J003). The two-layer form (card + record) is a J003 addition.

# Pitch template: card for the owner, record for the studio

## 1. Two layers
| Layer | Reader | Length | Where |
| --- | --- | --- | --- |
| **Pitch card** | the owner, in chat | 8 lines, `ste-writing` | the message |
| **Pitch record** | the owner on demand; every lead later | the 13 fields below | `knowledge/design/concepts/<concept-id>.md` (frontmatter `type: reference`, `scope: game`, `status: draft`) |

## 2. Pitch card (one per pitch)
```text
### <n>. <Title>                      ← the title test: a reader can say the action from it
Fantasy: As <role>, I <verb> so that <change>, while <pressure>.
First image: <camera, the player's action, scale, the stake, in one sentence>
Loop: <proven loop, named reference game> + twist: <the one rule that changes a decision or consequence>
Signature moment: <setup → decision → consequence → payoff, with normal inputs>
Why now: <dated trend evidence, source> | not verified
Smallest version: <the build that proves the fantasy; what is cut>
Biggest risk: <failure hypothesis> → test: <cheapest test>
```

## 3. Pitch record (13 fields, N2 T7)
| # | Field | What it holds | Form |
| --- | --- | --- | --- |
| 1 | Concept ID and version | id, author, date, current decision | `C-<yyyymmdd>-<slug>` v1, proposed |
| 2 | Title candidates | 2-4 distinct titles and the promise each makes; never imply a tested winner | |
| 3 | One-line fantasy | role, consequential verb, change, pressure | "As [role], I [verb] so that [change], while [pressure or uncertainty]." |
| 4 | Hook | one surprising action or relationship; why a player wants to try it | |
| 5 | First image | camera, readable action, scale relationship, immediate stakes; labelled concept art | |
| 6 | Core loop in one sentence | | "[goal] leads to [choice and action], then [feedback and consequence], then [a changed reason to act again]." |
| 7 | Signature moment | ordinary inputs → a demonstrable consequence; the art, animation, VFX and sound it needs | |
| 8 | Why now | dated trend evidence, audience, alternative explanation, what may be temporary | |
| 9 | Familiar foundation and original contribution | named loop reference, the changed rule, own expression, rights questions | |
| 10 | Smallest buildable version | the complete promise-keeping interaction; excluded breadth; dependencies; target devices. Content counts here (zones, items, states) are allowed and labelled PROPOSAL; they are scope, not targets | |
| 11 | Failure hypothesis | the strongest reason it may fail; the cheapest test that could show it | |
| 12 | Evidence | source IDs, observed facts, untested assumptions, results and limits; rubric ratings | |
| 13 | Recommendation to owner | approve an experiment, revise, hold or reject; alternatives; cost of delay | |

Keep proposed content apart from evidence (N2 §5.2). Unknown values say `TBD`, who decides, and the test.

## 4. Presenting the set (one message)
1. One line: what you were asked, the budget, the actual counts (raw → candidates → survivors).
2. The 3 pitch cards. Different mechanism families or different fantasies; never 3 skins of one idea.
3. **Recommendation:** one pitch, the player outcome it protects, the evidence that matters, its tradeoff, the strongest objection, and the evidence that would change your view (N2 6.2 O).
4. Not pitched: one line per critic survivor you did not pitch, with the rubric reason; name the reserve.
5. The decision asked for, with a default (e.g. "Default if no answer: I start a pre-production brief for pitch 2").
6. Paths to the 3 records, and to the first-image pictures if the brief allowed images (`reference-images`, family `concept`; labelled concept art, never a promise of final look).

Do not offer a menu to avoid judgment; do not hide uncertainty to look decisive (N2 6.2 O). The owner usually knows what is fun on Roblox (owner): when the owner's pick differs from your recommendation, record why and adapt; do not argue it again without new evidence (N2 6.4 O).

## 5. Growing an owner's idea ("make this bigger")
When the owner brings an idea, keep its fantasy and test it with the same tools: write the fantasy line and the title test; name the loop it implies; offer 2-3 **escalations** (bigger stake, sharper twist, stronger first image, a social consequence), each one sentence, and recommend one. Never replace the owner's fantasy with your own without saying so.
