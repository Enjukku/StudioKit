> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10. Revised by J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018).

# AI sound generation prompts

Vendor facts (M-48, ElevenLabs docs read 2026-10-10; re-check before use): text-to-sound-effects endpoint, model
`eleven_text_to_sound_v2`, duration 0.5-30 s (the endpoint minimum 0.5 s beats the overview's 0.1 s),
prompt_influence 0-1 (default 0.3), `loop` on v2 only. Describe events in order.

## A. Rules

| ID | Rule | Evidence |
| --- | --- | --- |
| S-123 | One-shots 0.5-2 s; prompt_influence 0.5-0.7; 2-3 texture descriptions per layer, 4 takes each, at least 3 candidates per layer before a pick, keep 1-2; one odd variant per layer (reversed, extreme pitch, unrelated texture) (SC-14); `loop` only for beds of 10-30 s. (P settings) | practice + inference |
| S-124 | Prompt anatomy: sound type + source and material + action + size and weight + shape ("sharp transient, fast decay") + space ("dry, close-up") + style + isolation ("single one-shot, no music, no background noise") + pitch hint. One event per prompt; sequences in order. Describe the texture, not only the object ("dry palm leaves crunching slowly" for ice); add motion words ("spinning", "swirling", "passing") for magic, travel and loop layers (SC-10). | practice + inference |
| S-125 | Ask for dry, isolated sound: the designed tail and glue are added and baked in the design pass, the room comes from the zone's live reverb (SC-08). | inference |
| S-126 | Clean every clip: trim silence to the transient, fade the last 10-30 ms, remove hiss, hum and rumble, peak to −1 dBFS, loudness-match to its family, check clipping; this is step 1 of the design-pass order (`craft-process.md` §6); measure with `review.md` §4. | inference |
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
Layers: generate each layer job (body, tick, crunch, report, signature; SC-05) or transient, body and tail (S-76) as its own prompt when the mix needs control of each.
Texture-first: for one layer, write 2-3 texture descriptions that might sound like it, not only its name (ice: "dry palm leaves crunching slowly", "foil crumpling slowly", "glass bottle tink").

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
| Ice slow tail (texture, not noun) | "Dry palm leaves crunching slowly, then settling, crisp brittle texture, slowing down, dry, close-up, isolated one-shot, no music" (×4; also "foil crumpling slowly") | 1.5 s, 0.6 |
| Magic travel loop (motion inside) | "Bright glassy shimmer spinning and swirling, slow wobble, airy, no impact, dry, seamless, no music" | 10 s, 0.5, loop: true |
| Footstep set | "Single heavy boot step on wet gravel, crunchy, close-up, dry, isolated one-shot, no music" (×4 re-rolls: gravel → dirt, wood, metal) | 0.5 s, 0.6 |

Never prompt for a named film, game, brand or famous logo sound (S-197). Tag every generated asset's status as not
auditioned until the owner has heard it at a check-in on the device matrix (an agent cannot listen; S-217).
