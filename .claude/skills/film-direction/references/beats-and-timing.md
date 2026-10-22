> Author: J018 maker film-director · claude-opus-5-5 · high · 2026-10-22. Reference for `film-direction`: built also from the owner's Riot transcripts (J018); the length and cut rules in §1 come from the J015 book (research paper rows N1 SU, ED and N3 DN). Numbers marked PROPOSAL are starting values a check may change.

# Beats and timing: cause and effect the player can follow

## 1. Lengths, setups and the causal chain
- **Length is event-bounded until the animatic measures it.** Write "until the player recognises the blocked exit", not a number. No source gives an ideal cutscene length, shot length per mood, skip delay or cuts per minute; lengths come from our own animatic and are labelled design choices. In the animatic, cuts sit on events; what geometry decides is measured (contact, arrival, line of sight); acting durations inside a shot stay PROPOSALS until the owner directs timing.
- **A setup earns its place by changing a later meaning,** and a payoff the player must use is actionable, not only surprising. Write the causal chain in verbs: wants, tries, meets resistance, notices, chooses, changes. A montage compresses time but keeps the choice that explains the next action. Show through behaviour where it reads; use a line of dialogue or UI where silent staging would hide essential information.

## 2. The beat grammar: tell, build, beat, peak, result
Every beat is a short story the player reads from order and timing.

| Part | In a cinematic | Fails when |
| --- | --- | --- |
| Tell | the player learns something is coming: a sound, a glance, a light change, the ground shaking | the event arrives with no warning, so it reads as random |
| Build | intensity rises: closer framing or a slow push, light narrowing, sound rising in pitch or level, motion converging on the focus | the build is flat, or so long nothing develops |
| Beat | a short held moment before the release: a breath of silence, a still frame, the camera settled | the peak lands on the end of the build with no gap, and loses weight |
| Peak | one clear frame where picture, effect flash and sound transient meet on one marker | several competing peaks blur which one mattered |
| Result | the consequence starts after its cause, never with it; the old spot calms and the eye moves to the result | the result plays together with its cause, so cause and effect merge |

- Tune the gaps in tenths of a second (3-frame steps at 30 fps). A small delay between cause and result reads as consequence.
- Big things move slowly: a giant gets slower steps, longer holds and slower camera moves than a person; a giant at human speed reads small.
- One peak per beat. A boss entrance with a roar, a flash and a camera shake on three different frames has no peak.

## 3. Rhythm and the climax
- **Uneven on purpose.** The gaps between beats and the shot lengths are not all equal; each difference has a reason (a quick cut on surprise, a long hold on a decision). An even cadence reads as a metronome and lowers attention.
- **Hold only while something develops.** A hold with nothing developing is delay, not suspense. Rhythm is the spread of new information, not the cut count.
- **Quiet before the big beat.** Lower the contrast in time as well as in the frame: dim or stop competing motion and sound just before the peak so it has a calm baseline to beat.
- **One climax.** The intensity line (framing, light contrast, sound layers, motion) rises across the sequence toward one climax beat; a flat finish wastes the ending. After the climax, the release is short and lands on play.
- **A visual contract earns its break.** Hold a repeated framing until the turn, then break it; if the camera already moves all the time, the turn has no contrast.

## 4. The marker list is the timing contract
- **One marker at every cut and every synced event** (contact, release, impact, reveal, a line's first word). The shot list holds the cuts (`shot:<id>`) and the cue events (`cues[].id`, dotted names such as `sfx.gate.burst`); a character's pose-linked events come from the animator's timing list by its own names (for example `contact_candidate`), with the same stage names VFX and sound use (load, charge, release, travel, impact, tail). VFX frame scripts and sound cue cards key from these names; no craft keeps its own rounded frame list.
- **Sync rule.** Picture punch and sound transient start from one trigger event. The sound onset lands on the picture event or up to about 40 ms after it, never more than one frame (16.7 ms at 60 fps) before it; a steady small delay beats a jittering one. Studio MCP captures are stills, so audible sync is "not verified" unless captured on a device with audio; the playback log shows scheduled times. This rule is the one the animator, VFX and sound books use; the other film lines point here.
- **A retime is a contract change.** It bumps the shot-list revision and reaches the animator, VFX, sound, UI and engineering in the same hand-back, with the affected cue ids (`shotlist.py diff` shows the shots whose windows moved).
- **Feedback follows the real outcome.** A victory, reward or defeat sequence starts on the server-confirmed result, never on a client guess; its size matches the result; it can be skipped. A rejected or failed attempt never shows the success layer. A cinematic around a paid random result (an egg, a crate) follows the game-designer's reveal rules and `platform-policy`: the same windup for every result, no near-miss, no tier hint before the result frame.

## 5. Big before small: the order of decisions
1. Beats and blocking (who stands where, who moves where, what each beat changes).
2. Camera (size, angle, lens, move) on the approved blocking.
3. Value and light: the grayscale read of every key frame; the light's direction and the brightest area.
4. Colour on the approved values (a colour strip, one vignette per beat).
5. Effects, particles, post effects and polish, added to a clean frame that already passes composition and value.

Each level is approved cheaply before the next is spent; a change to an earlier level reopens the levels after it. The stages that do this work are in `film-craft` §3.
