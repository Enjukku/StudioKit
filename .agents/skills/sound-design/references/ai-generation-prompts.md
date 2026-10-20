> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10

# AI sound generation prompts

Vendor facts (M-48, ElevenLabs docs read 2026-10-10; re-check before use): text-to-sound-effects endpoint, model
`eleven_text_to_sound_v2`, duration 0.5-30 s (the endpoint minimum 0.5 s beats the overview's 0.1 s),
prompt_influence 0-1 (default 0.3), `loop` on v2 only. Describe events in order.

## A. Rules

| ID | Rule | Evidence |
| --- | --- | --- |
| S-123 | One-shots 0.5-2 s; prompt_influence 0.5-0.7; 4 candidates per prompt, keep 1-2; `loop` only for beds of 10-30 s. (P settings) | practice + inference |
| S-124 | Prompt anatomy: sound type + source and material + action + size and weight + shape ("sharp transient, fast decay") + space ("dry, close-up") + style + isolation ("single one-shot, no music, no background noise") + pitch hint. One event per prompt; sequences in order. | practice + inference |
| S-125 | Ask for dry, isolated sound; add space with the engine reverb. | inference |
| S-126 | Clean every clip: trim silence, fade the last 10-30 ms, peak to −1 dBFS, loudness-match to its family, check clipping. | inference |
| S-127 | Detune-check pitched clips against the music key; shift to the nearest scale note (±50 cents or less). | inference |
| S-128 | Other tools (leads only): Stable Audio Open guidance about 7.0, about 100 steps; AudioGen about 10 s at 16 kHz (upsample). Read model cards first. | lead |
| S-216 | Every AI clip carries a rights manifest: provider, model, date, plan or contract evidence, input provenance, allowed use, attribution. Check commercial eligibility at generation time (free plans may be non-commercial). | lead |

## B. Template

```
[sound type], [source and material] [action], [size and weight], [shape: attack, decay, length],
[space: dry, close-up], [style], [pitch hint], single isolated one-shot, no music, no background noise
duration: <s>   prompt_influence: <0-1>   candidates: 4   loop: false
```

Variants: re-roll with one word changed (material adjective, size, action verb), not by raising influence.
Layers: generate transient, body and tail as separate prompts when the mix needs control of each (S-76).

## C. Examples (all settings P)

| Cue | Prompt | Settings |
| --- | --- | --- |
| Wooden crate break, small | "Single small wooden crate splintering apart on a stone floor, sharp dry crack, short wood rattle, very short, dry, close-up, isolated one-shot, no music" | 0.7 s, 0.6 |
| Wooden crate break, large | "Large stack of wooden crates collapsing, deep thud under a sharp splintering crack, many planks clattering, short dry tail, isolated one-shot, no music" | 2 s, 0.5 |
| UI tap (transient layer) | "Soft tiny plastic button tick, very short sharp click, no reverb, dry, close-up, isolated, no music" | 0.5 s (trim to <80 ms), 0.6 |
| Pickup sparkle (top layer) | "Tiny bright glass chime sparkle, single short high note, clean fast decay, no ring, dry, isolated one-shot, no music" | 0.5 s (trim), 0.6 |
| Honest no-gain cue | "Soft low muted descending synth tone, one smooth downward glide about an octave, warm, not harsh, short, dry, isolated, no music" | 1.5 s, 0.5 |
| Dread bed (loop) | "Distant low industrial hum with slow uneven metallic groans far away, dark empty concrete building, no melody, no music, seamless" | 20 s, 0.4, loop: true |
| Scare stab | "Sudden harsh unrecognisable metallic screech with a deep boom underneath, very fast attack, chaotic noisy texture, 3 second decaying tail, isolated, no music" | 3 s, 0.6 |
| Footstep set | "Single heavy boot step on wet gravel, crunchy, close-up, dry, isolated one-shot, no music" (×4 re-rolls: gravel → dirt, wood, metal) | 0.5 s, 0.6 |

Never prompt for a named film, game, brand or famous logo sound (S-197). Tag every generated asset's status as not
auditioned until a human or agent has listened on the device matrix (S-217).
