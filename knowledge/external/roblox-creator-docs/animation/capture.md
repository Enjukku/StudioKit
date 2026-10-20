---
title: Animation capture
description: Animation Capture in the Animation Editor allows you to generate high-quality, realistic animations for faces and bodies.
tags: [roblox, documentation, external-reference, priority-reference, animation]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [animation/capture.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/animation/capture.md). Published page: [https://create.roblox.com/docs/animation/capture](https://create.roblox.com/docs/animation/capture).

import BetaAlert from '../includes/beta-features/beta-alert.md'

You can record or upload video content to the [[external/roblox-creator-docs/animation/editor|Animation Editor]] to quickly capture movement and expressions as animation keyframes. These tools can create unique and realistic animations within minutes while providing access to the animation keyframes for additional adjustments.

The animation capture tools allow you to:

- [Record your face](#face) with a webcam to puppeteer characters with [[external/roblox-creator-docs/avatar/dynamic-heads/index|animation compatible heads]].
- [Upload full-body video content](#body) to generate high quality realistic animations for an entire character.

## Face

**Animation Capture - Face** allows you to use your webcam to puppeteer rigs with [[external/roblox-creator-docs/avatar/dynamic-heads/index|animation compatible heads]] and generate corresponding keyframes to your movement. With the ability to record up to 60‑second animations, you can quickly provide both your playable and nonplayable characters the means to realistically grin, raise their eyebrows, drop their jaw, or any other expression necessary for your game.

<BetaAlert betaName="Face Capture" leadIn="To ensure that you're able to utilize your camera to record and create facial animations, you must first enable the beta feature through " leadOut="." components={props.components} />

Before you begin to record your face, ensure that you're in a well lit room close enough to your camera so that your face is in the center of your camera's recording frame. This increases your camera's ability to distinguish you from your surroundings so that you can accurately puppeteer your avatar and create high-quality animations.

1. From the toolbar's **Avatar** tab, click **Clip Editor**. The **Animation Editor** window displays.
2. In the 3D viewport or **Explorer** window, select the rig you want your video to animate. Enter a new animation name in the dialog window and click the **Create** button.
3. Navigate to the **track list** and click the **Face Capture** button. A popup displays asking you to acknowledge that you consent to the collection of your facial movements to enable the feature and camera access.

   <img src="../assets/animation/face-recorder/Face-Recorder-Button.jpg"
   width="80%" />

4. <Chip label="OPTIONAL" size="small" variant="outlined" /> If you have multiple cameras, choose which camera you want to use to record.

5. In the controls widget in the 3D viewport, click the red circle. Your camera begins recording your facial movements.

   <img src="../assets/animation/face-recorder/Ready-Button.jpg" width="150" />

6. When you finish your recording, click either the red square or countdown timer. Keyframes that correspond to your facial movement display within the timeline.

   <img src="../assets/animation/face-recorder/Countdown-Button.jpg" width="150" />

7. <Chip label="OPTIONAL" size="small" variant="outlined" /> If you'd like to delete the recording and try again, click **Re‑Record**.

After you finish your recording, you can [[external/roblox-creator-docs/animation/editor#keyframes|fine-tune]] the keyframes, [[external/roblox-creator-docs/animation/editor#save-an-animation|save]] your animation, then [[external/roblox-creator-docs/animation/editor#export-an-animation|export]] it to use across all of your games.

## Body

The **Animation Capture - Body** allows you to quickly generate high-quality, realistic full-body animations for your [[external/roblox-creator-docs/avatar/character-bodies/specifications#rigging|R15 rigs]] by uploading videos to use to track the body's movement and generate corresponding keyframes. This significantly speeds up the manual process of creating animations, and allows you to personalize your avatars and NPCs with life-like mannerisms in a few minutes.

<BetaAlert betaName="Live Animation Creator" leadIn="To import a video for animation creation, you must first enable the beta feature through " leadOut="." components={props.components} />

Before you import a video to the **Animation Editor**, ensure the `.mp4` or `.mov` file meets the following requirements:

- It includes just one person who is well-lit and visible throughout the video.
- It only contains a continuous single shot that's less than 15 seconds from a stable camera.
- It adheres to Roblox's [Community Rules](https://en.help.roblox.com/hc/articles/203313410) and [Terms of Use](https://en.help.roblox.com/hc/articles/115004647846).

To import a video to create an animation:

1. From the toolbar's **Avatar** tab, click **Clip Editor**. The **Animation Editor** window displays.
2. In the 3D viewport or the **Explorer** window hierarchy, select the R15 rig you want your video to animate. Enter a new animation name in the dialog window and click the **Create** button.
3. Navigate to the **media and playback controls** and click the **&ctdot;** button, then navigate to **Import**&nbsp;⟩ **Live&nbsp;Animation&nbsp;Creator**.

   <img src="../assets/animation/live-animation-creator/Media-Playback-Controls.jpg"width="330" />

4. In the popup dialog, click the **Choose Video** button.
5. Select the video you want to import from your local machine, then click the **Open** button. After about a minute, keyframes that correspond to movement in your video display within the timeline.

After your import is successful, you can [[external/roblox-creator-docs/animation/editor#save-an-animation|save]] and [[external/roblox-creator-docs/animation/editor#export-an-animation|export]] your animation to use across all of your games.


## Related Files

- [[external/roblox-creator-docs/animation/editor]] - Animation Editor.
- [[external/roblox-creator-docs/animation/events]] - Animation events.
- [[external/roblox-creator-docs/animation/graph-editor]] - Animation Graph Editor.
- [[external/roblox-creator-docs/animation/index]] - Animation in Roblox.
- [[external/roblox-creator-docs/animation/curve-editor]] - Curve Editor.
- [[external/roblox-creator-docs/animation/expressions]] - Graph Editor expressions.
- [[external/roblox-creator-docs/animation/graph-editor-state-machine]] - Graph Editor state machines.
- [[external/roblox-creator-docs/animation/inverse-kinematics]] - Inverse Kinematics.
- [[external/roblox-creator-docs/animation/using]] - Use animations.
