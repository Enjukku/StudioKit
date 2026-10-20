---
title: Verify attachment placement
description: When creating characters in Blender, the character model requires minor attachment adjustments to be Studio-ready.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
next: /art/characters/creating/final-checks
prev: /art/characters/creating/remove-extra-bones
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/characters/creating/verify-attachments.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/characters/creating/verify-attachments.md). Published page: [https://create.roblox.com/docs/art/characters/creating/verify-attachments](https://create.roblox.com/docs/art/characters/creating/verify-attachments).

Attachment points are non-rendered objects of your avatar where rigid accessories attach to. Each template includes the required attachments at their expected locations ending with **\_Att**. Before exporting, it's important to verify the attachment position and, if necessary, adjust the location if you made any changes to the shape of your model.

<GridContainer numColumns="2">
  <figure><img src="../../../assets/art/avatar/basic-creation/Pre-Attachment.png" />  <figcaption>Original template attachment positions</figcaption></figure>

  <figure><img src="../../../assets/art/avatar/basic-creation/Post-Attachment.png" /><figcaption>Attachments after adjustment</figcaption></figure>
</GridContainer>

Center attachment points at their respective locations. Each attachment should overlap approximately halfway with the character's mesh.

This tutorial only changes the head of your model, so you only need to adjust the **Hat**, **Hair** and **FaceFront** attachments. To enable visibility and verify your head attachment point:

1. If you haven't already, enable [[external/roblox-creator-docs/art/characters/creating/index#disabled-objects|disabled objects]] in your Outliner.
1. In the Outliner, find the `Joints` parent object.
1. Hold <kbd>Shift</kbd> and click the **Hide** icon for the `Joints` object to hide everything.
1. Expand the `Joints` object's hierarchy and unhide `Head_Geo`, `Hat_Att`, `Hair_Att`, and `FaceFront_Att`.
   1. If required, disable **Disable In Viewport** <img src="../../../assets/art/blender-ui/Disabled-Icon.png" style={{marginBottom:"0px;"}} width="20px"/> next to the \_Att objects.
1. In the viewport, verify the placement of the attachments. The goblin's head is shorter than the starting template, so the attachments require minor vertical adjustment.
1. Select the attachments, then switch to **Edit** mode.
1. Using the **Grab** tool, position the attachments vertically along the y-axis until they are about halfway embedded in the head.

   <video controls muted src="../../../assets/art/avatar/basic-creation/Cleanup_02.mp4" width="100%"></video>


## Related Files

- [[external/roblox-creator-docs/art/characters/creating/blender-configurations]] - Blender configuration.
- [[external/roblox-creator-docs/art/characters/creating/caging]] - Caging character head.
- [[external/roblox-creator-docs/art/characters/creating/combine-head-geometry]] - Combine head geometry.
- [[external/roblox-creator-docs/art/characters/creating/index]] - Create with templates.
- [[external/roblox-creator-docs/art/characters/creating/export-character]] - Export character model.
- [[external/roblox-creator-docs/art/characters/creating/export-textures]] - Export textures.
- [[external/roblox-creator-docs/art/characters/creating/final-checks]] - Final checks.
- [[external/roblox-creator-docs/art/characters/creating/modeling-best-practices]] - Modeling best practices.
- [[external/roblox-creator-docs/art/characters/creating/modeling-tips]] - Modeling tips.
- [[external/roblox-creator-docs/art/characters/creating/texturing-pbr]] - PBR textures (optional).
- [[external/roblox-creator-docs/art/characters/creating/remove-extra-bones]] - Remove extra bones.
- [[external/roblox-creator-docs/art/characters/creating/sculpting]] - Sculpt the head.
- [[external/roblox-creator-docs/art/characters/creating/template-files]] - Template files.
- [[external/roblox-creator-docs/art/characters/creating/head-objects]] - Template head structure.
- [[external/roblox-creator-docs/art/characters/creating/texturing-eyes]] - Texturing eyes.
- [[external/roblox-creator-docs/art/characters/creating/texturing-face]] - Texturing face.
- ...and 1 more local docs.
