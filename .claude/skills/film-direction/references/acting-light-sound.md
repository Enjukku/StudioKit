> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-direction`. Source rows: N1 AC-01..05, LC-01..06, SN-01..07, ED-02; N4 R-04..R-09, S-01..S-15, A-05. Values from the first game (N4) are proposals unless the row says owner decision. Revised by J018 maker film-director · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§1 performance sheet, pushed moments, eyes; §2 value plan per beat; §3 sound jobs and passes).

# Acting, light and sound: what the director decides and hands over

The director decides the intention and the observable result. The animator, environment designer, VFX and sound designer decide how (`rules/messages.md`: what and why, never how).

## 1. Acting
**Brief shape per shot (N1 AC-04, O):**
| Field | Example (original) |
| --- | --- |
| Belief before the shot | "The beacon is a prize, the statue is decoration." |
| New stimulus noticed | "The beacon goes dark just before her hand reaches it; something moves in the water behind." |
| Tactic toward another character | "None yet: she is alone with the threat." |
| Visible decision | "She stops reaching and shifts her weight away." |
| Subtext (what she wants and will not say) | "She wants the prize badly enough to hesitate before she runs." |
| End pose the next shot needs | "Weight on the back foot, head turned toward the statue, right hand still raised." |
| Framing and occlusion limits | "Medium close, eye level; the hand must stay clear of the statue's hand in frame." |

**Act it out on paper before anyone keys.** I cannot perform a scene, so I write it: a performance sheet per key shot, one row per beat with the motion and what drives it (the hips pull back, the arm follows), the time (a window or a PROPOSAL), a sound word ("hup... CRACK") and the subtext. The animator builds from it; key poses come first and tell the story, the in-betweens follow.

- **Character first.** Know who is acting (temperament, history, the two words of their tension) and ask how *this* character would do it; a generic reaction wastes the shot.
- **Adjectives become pose changes.** Give 2-4 adjectives per character in the scene and say what each changes in the pose (proud: chin up, chest open; heavy: wider, lower stance; afraid: weight back, hands near the body). Push, then pull back if the balance or the character breaks.
- **Push one or two moments past real, on a believable base.** A hero landing, the boss's first step, a jump apex with legs tucked into a V: those may exaggerate; balance (centre of gravity over the support), contacts and weight shifts stay true around them, or nothing is believed.
- **Comedy contradicts a known trait,** and the whole body plays it (the tough guard running away, looking back), never only a small face at phone size.
- **Eyes act.** Eyes close through a fast head turn, widen on a shock, look from under the brows for intent; on a phone, body and head angle carry more than the face.
- **The same key poses can tell two stories.** On the key beat, ask for two timing takes on the same poses and let the owner choose on the playable animatic.
- Give the cause as an experience, not adjectives (E, N1 AC-01): "you refuse to approach after being hurt; then someone smaller succeeds and you cannot stop watching" beats "scared, then happy" (O, AC-02).
- Ask for separate readable poses for each thought (avoid, notice, evaluate, decide) and review them as silent black-fill and grayscale stills from the shot camera before paying for effects (N1 AC-02).
- Expression size matches the shot and the style; let head and body angles carry intent where a face is small (N1 AC-03, E).
- Review the pose from the final camera, not the animator's viewport (N1 AC-04). Ask for reference alternatives (pose images or a blocking pass) before polished animation.
- A still or a cutscene key frame of a character reuses the signature move's key pose from the animation set; the animator sets it on the rig at the still's camera.
- **Cast readiness (first game):** every character needs its own face kit (mouth, eyes, brows), eyes that can look at a target, and mouth shapes before any spoken line; test each planned physical beat against the rig in a render before it locks (N4 R-04, R-05 owner corrections; R-09 owner decision; R-06 proposal). Rig requests go to the character rigger, not straight to the animator.

## 2. Light, value and colour
**Value plan per beat (one row per beat, written before boards):**
| Field | Example |
| --- | --- |
| Intensity of the beat | calm / rising / climax |
| Contrast key | narrow (calm) or wide (dramatic): deep shadows and a bright accent only where the beat is intense |
| Brightest area | on the subject (the open gate, the boss's fist), or directly behind it for a planned silhouette (the boss dark in the fire-lit gate); never a sky patch or a stray lamp elsewhere |
| Motivated source | the torch, the window, the screen glow, the sun from the game's setup |
| Light direction and meaning | from above or the side for heroes and rewards; from below *can* read as threat, used the same way every time in this game |
| Separation | subject value vs its background; a rim light where a figure meets a similar-value background |
| Depth groups | dark framing foreground, lit midground subject, quiet low-contrast background |
| What stays hidden | the dark side where a surprise waits while the eye is on the light |

- Lower the contrast everywhere else before raising the subject; a value gradient (darker toward the frame edges, brightest at the subject) leads the eye.
- Block light and shadow first: test 2-3 light variants of the key beat on the rough greybox and choose before any detail or colour (`film-craft` §3 step 6).
- Per beat, write: motivated source, subject value vs background value, brightest area, silhouette readability, what stays hidden (N1 LC-02). "Brighter" is not an instruction: name what changes in visibility and attention.
- **Sequence strip** before final lighting, one vignette per beat, built on the approved value strip: subject value, background value, dominant hue family, practical source, intended shift. Judge each vignette beside its neighbours (N1 LC-05; E: LC-03).
- Colour meanings are this sequence's conventions (warm = the family's interior, cold = the father's distance in N1 SC6), never universal psychology (N1 LC-06); once set, a convention means the same thing in every cutscene of the game.
- Plan both images of a reveal: the concealment and the revealed state (N1 LC-02).
- Light and composition are decided together, never composition locked first and lit later; say whose perspective the shot follows (E: N1 LC-04, FC-22).
- Final judgement is on the captured Roblox output on target devices, not the Blender preview (N1 LC-02; tone does not carry over unchanged).
- Mood turns that must also work live use engine tools (colour correction, atmosphere, a camera push) planned with the environment designer (N4 A-04, proposal). A placed light under a villain, or behind a figure for a rim, is a local light in the scene; the sun cannot come from below.
- Readability must survive reduced or absent expensive effects (`film-craft` runtime notes).

## 3. Sound, music and silence
**Every cue has a job.** Sound tells the player what is happening, confirms what they did, and carries the emotion of the beat; every layer (music, dialogue, effects, ambience, foley, UI) takes a part of the story point. Each cue names the emotion it carries as well as its object (the same door can open happily or terribly).

**Cue attributes (N1 SN-02, O):** job and emotion, onset, offset, narrative role, listener perspective (who hears it in the story), allowed overlap, priority against dialogue, sync type (locked to action / flexible / pending music).

- One cue sheet shared with the sound designer, keyed to shot ids and events: stimulus audible, character hears it, reaction begins, action lands, music enters and exits (N1 SN-06). The shot-list tool prints it (`film-craft`).
- A staged action gets one sound per named stage (load, charge, release, travel, impact, tail), on the same names the animator and VFX use (`references/beats-and-timing.md` §4).
- Silence = removing a named layer (music out, ambience kept), not zero audio. Environmental sound can do the score's work (E: N1 SN-01).
- At a reveal, compare three versions: warning before, exact sync, delayed sound (N1 SN-02).
- **Music and effects are planned together** and hit the beats and cuts together; they enter the animatic as temp from its first cut, mixed as we go, and decide which leads at each key beat. Temp tracks carry intent and stay labelled temp; if the final music changes a dramatic accent, reopen the animatic instead of keeping the cuts blindly (E: N1 SN-03, SN-04; O: SN-06).
- **Design and editing are two passes:** the sound designer makes the sounds; fitting them to the picture (timing, level, which layers stay) is judged against the animatic or capture with every other sound present, never on the isolated file.
- **Listen to the key event solo, then in the full mix** (on the owner's device capture at the gate; Studio MCP captures have no audio).
- A dialogue-lock boundary contains revision churn (E: Linke, as paraphrased in a Netflix-sponsored Q&A article, N1 SN-05).
- **First game (owner decisions):** plan sound and voice with the sound designer while the scenes are designed, not after (N4 S-01); brief sound with what is on screen and when, the sound designer picks the sounds (N4 S-15). Short lines, light dialogue, a voice source and a licence record were that game's choices (N4 S-02, S-05): ask the owner per game.
- Every spoken word gets a caption with the speaker where it matters; whether captions are on by default is an owner question (N4 S-09 open). A beat that play depends on also reads with sound off.
- Sound designers own mix, loudness and phone-speaker checks (`sound-design`).
