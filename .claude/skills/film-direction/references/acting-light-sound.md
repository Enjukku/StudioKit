> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-direction`. Source rows: N1 AC-01..05, LC-01..06, SN-01..07, ED-02; N4 R-04..R-09, S-01..S-15, A-05. Values from the first game (N4) are proposals unless the row says owner decision.

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
| End pose the next shot needs | "Weight on the back foot, head turned toward the statue, right hand still raised." |
| Framing and occlusion limits | "Medium close, eye level; the hand must stay clear of the statue's hand in frame." |

- Give the cause as an experience, not adjectives. Barillaro briefed Piper's animators with a child who fell off a swing, then watches a smaller child fall and not mind (E, N1 AC-01). Our wording, for example "you refuse to approach after being hurt; then someone smaller succeeds and you cannot stop watching", beats "scared, then happy" (O, AC-02).
- Ask for separate readable poses for each thought (avoid, notice, evaluate, decide); test them as silent grayscale thumbnails from the shot camera before paying for effects (N1 AC-02).
- Expression size matches the shot and the style; one Arcane animator (Wanneroy, Season 1) toned down his own exaggerated faces and let head and body angles carry intent (N1 AC-03, E). On a phone, body and head angle carry more than the face.
- Review the pose from the final camera, not the animator's viewport (N1 AC-04).
- Request reference alternatives before polished animation.
- **Cast readiness (first game):** every character needs its own face kit (mouth, eyes, brows), eyes that can look at a target, and mouth shapes before any spoken line; test each planned physical beat against the rig in a render before it locks (N4 R-04, R-05 owner corrections; R-09 owner decision; R-06 proposal). Rig requests go to the character rigger, not straight to the animator.

## 2. Light and colour
- Per beat, write: motivated source, subject value vs background value, brightest area, silhouette readability, what stays hidden (N1 LC-02).
- **Sequence strip** before final lighting, one vignette per beat: subject value, background value, dominant hue family, practical source, intended shift. Judge each vignette beside its neighbours (N1 LC-05; E: Fortiche makes at least one colorscript vignette per sequence, LC-03).
- Colour meanings are this sequence's conventions (warm = the family's interior, cold = the father's distance in N1 SC6), never universal psychology (N1 LC-06).
- Plan both images of a reveal: the concealment and the revealed state (N1 LC-02).
- Light and composition are decided together; DeBlois found it strange that layout fixed compositions before their light was known, and Deakins asked whose perspective a shot follows (E: N1 LC-04, FC-22).
- Final judgement is on the captured Roblox output on target devices, not the Blender preview (N1 LC-02; tone does not carry over unchanged).
- Mood turns that must also work live use engine tools (colour correction, atmosphere, a camera push) planned with the environment designer (N4 A-04, proposal).
- Readability must survive reduced or absent expensive effects (`film-craft` runtime notes).

## 3. Sound, music and silence
**Cue attributes (N1 SN-02, O):** onset, offset, narrative role, listener perspective (who hears it in the story), allowed overlap, priority against dialogue, sync type (locked to action / flexible / pending music).

- One cue sheet shared with the sound designer, keyed to shot ids and events: stimulus audible, character hears it, reaction begins, action lands, music enters and exits (N1 SN-06). The shot-list tool prints it (`film-craft`).
- Silence = removing a named layer (music out, ambience kept), not zero audio. Environmental sound can do the score's work (E: the train before the restaurant killing, N1 SN-01).
- At a reveal, compare three versions: warning before, exact sync, delayed sound (N1 SN-02).
- Bring the composer or sound designer in before pictures are final; temp tracks carry intent and stay labelled temp; if the final music changes a dramatic accent, reopen the animatic instead of keeping the cuts blindly (E: N1 SN-03, SN-04; O: SN-06).
- A dialogue-lock boundary contains revision churn (E: Linke, as paraphrased in a Netflix-sponsored Q&A article, N1 SN-05).
- **First game (owner decisions):** plan sound and voice with the sound designer while the scenes are designed, not after (N4 S-01); brief sound with what is on screen and when, the sound designer picks the sounds (N4 S-15). Short lines, light dialogue, a voice source and a licence record were that game's choices (N4 S-02, S-05): ask the owner per game.
- Every spoken word gets a caption with the speaker where it matters; whether captions are on by default is an owner question (N4 S-09 open).
- Sound designers own mix, loudness and phone-speaker checks (`sound-design`).
