> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10. Revised by J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Revised by J020 step 8 sound-designer · claude-opus-5-5 · high · 2026-10-23: takes per round (J020-D9), regenerate rounds (J020-D7), ElevenLabs facts (2026-10-23). Revised by J020 step 8 follow-up sound-designer · claude-opus-5-5 · high · 2026-10-24: ElevenLabs facts measured 2026-10-24, `generate` built.

# AI sound generation prompts

**Note (J020):** the prompt rules below will be rebuilt from a sound-prompting source the owner approves; until then only the takes rule, the vendor facts and the page's prompt rules below changed. (The owner's conversational-agents prompting guide covers LLM system prompts, not sound prompts.)

Vendor facts (ElevenLabs; re-check when the plan or the model changes; `soundbench generate` logs the real values
from each response in the take's sidecar: `credits`, `format_used`, `requested_ms`, and intake's received length):
- Sound-effects API (`/v1/sound-generation`, API reference read 2026-10-23, `editor-design.md` §8): models `eleven_text_to_sound_v2` (default) and `eleven_text_to_sound_v3` (which gives better game sounds is tested on the first real cue set); `prompt_influence` 0-1 (default 0.3); `loop`; `output_format` defaults to `mp3_44100_128`; "MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM and WAV formats with 44.1kHz sample rate requires you to be subscribed to Pro tier or above" (not enforced on this kit's Creator account: measured rows below). `generate` asks for WAV 44.1 kHz first, then falls back to `mp3_44100_192`, then `mp3_44100_128`, and logs the format it got. Billing is in the `character-cost` response header.
- Capabilities page "Sound effects" (read 2026-10-23, https://elevenlabs.io/docs/overview/capabilities/sound-effects): `prompt_influence` high gives a literal reading, low a creative reading with more variety; `loop` gives seamless repeat playback.
- **Measured facts (2026-10-24, J020 step 7, this kit's Creator-tier key; replaces the "conflicting facts, unchecked" table).** 330 credits were spent and the account's credit counter matched the sum of the `character-cost` headers (lead's J020 step 8 follow-up brief, 2026-10-24); the other rows: `tools/audio/soundbench/README.md` "Generating takes" and `generate.py` constants.

| Fact | Measured (M) | Use it so |
| --- | --- | --- |
| Duration | `duration_seconds` minimum 0.5 s, maximum 30 s; 0.1 s is refused with HTTP 400 `invalid_generation_settings`. A 0.5 s request returns 480 ms (WAV and MP3 alike; intake logs it as a warning, never a refusal) | ask 0.5 s or more; a sound shorter than 0.5 s is generated at 0.5 s and cut in the edit pass (`cut`, `trim`) |
| Cost | with `duration_seconds` set: ceil(11 × seconds) credits (0.5 s = 6, 1 s = 11, 2 s = 22, 5 s = 55); without a duration: 55 flat | **always set `duration_s`** in `prompts.json`: a 0.5 s take without it costs 55 instead of 6. Plan a round with `generate --dry-run` (`predicted_credits`) |
| Formats | this Creator account gets WAV at 44.1 and 48 kHz (also for loops), PCM, and MP3; the API page's "Pro tier" note for WAV and PCM is not enforced on it. `generate` asks `wav_44100` first; the MP3 fallback has never run against a real refusal | a WAV take needs no MP3 decode; if another account is refused, `generate` falls back to MP3 192 then 128 kbps and logs it |
| Loops | a 1.0 s looping request returned 1.5 s | do not plan a loop's length from the request: measure the take (`measure`), and set `loop_bed` / `loop_music` points from the measured file |
| Models | `eleven_text_to_sound_v2` and `eleven_text_to_sound_v3` cost the same | which one sounds better for game sounds is **not judged yet** (no one has listened; the owner's play-test of the first real cue set decides). Name the model in every round's `note` |

- **Wrong for this endpoint:** the capabilities page "Sound effects" (read 2026-10-23, https://elevenlabs.io/docs/overview/capabilities/sound-effects) says durations from 0.1 s and "40 credits per second" when the duration is set. Both are wrong for `/v1/sound-generation` on this account: 0.1 s is refused (400) and the measured cost is 11 credits per second (rows above). Trust the measured rows and the sidecars, not that page.

**Prompt rules from the capabilities page** (kept short; no template is built on them until the source is approved):
- A simple effect gets a clear, short description: "Glass shattering on concrete".
- A sequence is described in order: "Footsteps on gravel, then a metallic door opens".
- Musical parts give tempo and key: "90s hip-hop drum loop, 90 BPM", "Vintage brass stabs in F minor".
- Audio terms the model understands: impact, whoosh, ambience, one-shot, loop, stem, braam, glitch, drone.

## A. Rules

| ID | Rule | Evidence |
| --- | --- | --- |
| S-123 | One-shots 0.5-2 s; prompt_influence 0.5-0.7; 2-3 texture descriptions per layer. **Takes per round by the card's tier (J020-D9, replaces "4 takes per texture"):** minor 3, frequent 4 (kept as the variant set), important 6, spread across the texture descriptions; the layers of an important sound generated separately, one prompt each; one take of the round an odd variant (reversed, extreme pitch, unrelated texture) (SC-14). Rank against the card's targets (`craft-process.md` §5); no take passes after its fixable steps → change the prompt and regenerate, never pile on edits; at most 3 rounds per cue, then the cue goes to the owner with its numbers (J020-D7). Good unpicked takes go to the game library. `loop` only for beds of 10-30 s. (P settings) | practice + inference + J020 |
| S-124 | Prompt anatomy: sound type + source and material + action + size and weight + shape ("sharp transient, fast decay") + space ("dry, close-up") + style + isolation ("single one-shot, no music, no background noise") + pitch hint. One event per prompt; sequences in order. Describe the texture, not only the object ("dry palm leaves crunching slowly" for ice); add motion words ("spinning", "swirling", "passing") for magic, travel and loop layers (SC-10). | practice + inference |
| S-125 | Ask for dry, isolated sound: the designed tail and glue are added and baked in the design pass (`soundbench`), the room comes from the zone reverb in Roblox (SC-08, J020-D10). | inference |
| S-126 | Clean every clip: trim silence to the transient, fade the last 10-30 ms, remove hiss, hum and rumble, peak to −1 dBFS, loudness-match to its family, check clipping; this is the clean step of the recipe's design pass and its edit pass (`craft-process.md` §6), rendered by `soundbench render`; measure with `review.md` §4. | inference |
| S-127 | Detune-check pitched clips against the music key; shift to the nearest scale note (±50 cents or less). | inference |
| S-128 | Other tools (leads only): Stable Audio Open guidance about 7.0, about 100 steps; AudioGen about 10 s at 16 kHz (upsample). Read model cards first. | lead |
| S-216 | Every AI clip carries a rights manifest: provider, model, date, plan or contract evidence, input provenance, allowed use, attribution. Check commercial eligibility at generation time (free plans may be non-commercial). | lead |

## B. Template

```
[sound type], [source and material] [action], [size and weight], [shape: attack, decay, length],
[space: dry, close-up], [style], [pitch hint], single isolated one-shot, no music, no background noise
duration: <s>   prompt_influence: <0-1>   takes this round: 3 | 4 | 6 (minor | frequent | important)   loop: false
```

Variants: a frequent cue's round of 4 is its variant set; a new round changes one word (material adjective, size, action verb), not the influence alone.
Layers: an important sound's layer jobs (body, tick, crunch, report, signature; SC-05, or transient, body and tail, S-76) are always generated separately, one prompt each (J020-D9), then mixed with `layers` and `align`.
Texture-first: for one layer, write 2-3 texture descriptions that might sound like it, not only its name (ice: "dry palm leaves crunching slowly", "foil crumpling slowly", "glass bottle tink").
In the cue folder the template becomes `prompts.json` (fields and the run: `craft-process.md` §5): the descriptions go in `prompts` (or per layer in `layers[].prompts`), `duration_s` always set (cost: the measured rows above), `prompt_influence`, `loop`, `model`, and a `note` with what this round changed and which rank misses it must fix.

```json
{"cue": "SFX-COIN-PICKUP", "prompts": ["tiny bright glass chime sparkle, single short high note, clean fast decay, dry, isolated one-shot, no music",
 "small brass coin tink on stone, sharp short ring, dry, isolated one-shot, no music"],
 "duration_s": 0.5, "prompt_influence": 0.6, "loop": false, "model": "eleven_text_to_sound_v2",
 "note": "round 2: round 1 missed band_500_5k (all 4 takes too dark); brighter material words"}
```

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
| Ice slow tail (texture, not noun) | "Dry palm leaves crunching slowly, then settling, crisp brittle texture, slowing down, dry, close-up, isolated one-shot, no music" (important layer: 6 takes across this and "foil crumpling slowly") | 1.5 s, 0.6 |
| Magic travel loop (motion inside) | "Bright glassy shimmer spinning and swirling, slow wobble, airy, no impact, dry, seamless, no music" | 10 s, 0.5, loop: true |
| Footstep set | "Single heavy boot step on wet gravel, crunchy, close-up, dry, isolated one-shot, no music" (frequent: 4 takes per material, kept as its variant set; one prompt per material: gravel, dirt, wood, metal) | 0.5 s, 0.6 |

Never prompt for a named film, game, brand or famous logo sound (S-197). Tag every generated asset's status as not
auditioned until the owner has played it in a play-test (an agent cannot listen; S-217; J020-D3).
