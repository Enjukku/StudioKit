---
name: ste-writing
description: Use for every message to the owner and every explanation (how a system works, what code does, why a method was chosen, status reports, explainer pages, video scripts). Write 80% toward ASD-STE100 Simplified Technical English, keep domain terms and every hedge, pick the cheapest format that is easy to check.
---

# STE Writing (80% of ASD-STE100)

> Author: orchestrator · claude-sonnet-5-5 · high · 2026-10-07. Kit skill: universal. Ported 2026-10-20 by orchestrator · claude-opus-5-5 · medium from DestructionSimulator (owner rule 2026-10-09); game examples replaced.

**Sources.** Andrej Karpathy's X post (2026): ask the LLM to explain in ASD-STE100, "80% of the way"
(read through explainx.ai and stashbase.ai summaries; the original post was not opened). Structural
rules, scan checklist and modality rule adapted from `danyuchn/asd-ste100-skill` v0.4.0 (MIT,
github.com/danyuchn/asd-ste100-skill). This is a clarity tool inspired by STE. It is not certified STE.
The official 900-word dictionary is not used.

## Why only 80%

Full STE limits the word list. Summaries of the post say the model then drops facts. So follow the
sentence rules, but **keep product names, code names and domain terms** (hitbox, cooldown, rig,
`DataService`). Define each term once, in one line, the first time.

## Sentence rules (apply fully)

| Rule | Do | Do not |
| --- | --- | --- |
| Active voice | "The server removes the item." | "The item is removed." |
| Length | Steps: max 20 words. Descriptions: max 25. | Long chained clauses |
| One instruction per sentence | "Open the file. Read line 3." | "Open the file and read line 3, then check it." |
| No phrasal verbs | "start", "remove", "contact" | "spin up", "take off", "reach out" |
| No semicolons | Two sentences | `;` |
| Noun clusters | Max 3 nouns in a row | "high pressure fuel pump inlet valve" |
| No ellipsis | Keep subject, verb, article | "Files not backed up are lost" |
| Paragraphs | One topic, max 6 sentences, main point first | Mixed topics |
| Lists | Numbered list for 3+ steps | Steps hidden in one sentence |
| Tenses | Present, past, future | Perfect tenses — unless they carry needed meaning (see below) |
| Style | Warnings first. Digits with units ("60 Hz"). No idioms, slang, contractions. | |

## Word rules (aim for them)

- One word, one meaning. One name per thing. Never rotate synonyms ("item" / "object" / "thing").
- Use the verb, not the noun made from it: "analyze the log", not "perform an analysis of the log".
- Short common words: "use", not "utilize".

## Keep the meaning (most important)

- **Keep every hedge.** "May have failed" stays "may have failed". Never turn a guess into a fact.
- **Keep needed perfect tenses.** "The job has completed" differs from "the job completed". Keep it when it carries meaning.
- **Never add a fact** the source did not state. Never drop a number, a condition or a scope.
- **Mark what you did not verify:** gate-verified, MCP-verified, owner-confirmed, not verified, not recorded.
- Simple text cannot fix empty content. If you have nothing to say, say that.
- Stop when the sentence is clear, not when it is shortest.

## Scan before sending

1. Synonym rotation: one thing, many names.
2. Hedge stacking: "may potentially help to improve". State the claim or delete it.
3. Nominalization: "provides assistance to" → "helps".
4. Marketing words: seamless, robust, powerful, blazing-fast. Delete, or give the measurement.
5. Run-ons: several ideas in one sentence.
6. Soft phrasal verbs: kick off, dive into.

## Pick the format (Karpathy's ladder)

Choose the cheapest format that makes the answer easy to check.

1. **Text** in this style. The default.
2. **Diagram** (SVG or Mermaid) for components and flows, or states and transitions. Mark uncertain labels.
3. **HTML page** when the owner must look around: tabs, tables, sliders. Best return for the effort.
4. **Narrated slideshow or video** for a full walkthrough. Use free browser speech. Use paid voice only if the owner agrees.

## Layout for a system explanation

| Part | Content |
| --- | --- |
| What it is | 1 sentence |
| What the player sees | 2-3 sentences, cause and effect |
| How it works | 3-7 numbered steps, each with the file name |
| Why this method | the alternatives, the evidence, what was rejected |
| Why it is fast or slow | what it saves, what it costs |
| What breaks first | 1-3 bullets |
| How to check | a command or an Output line |

## Do not use for

AI-only knowledge files (they keep their dense format), creative or persuasive copy, code comments.
