---
title: Test character bodies
description: Verify the important aspects of your character model in Blender and in Studio.
tags: [roblox, documentation, external-reference, priority-reference, avatar]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [avatar/character-bodies/test.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/avatar/character-bodies/test.md). Published page: [https://create.roblox.com/docs/avatar/character-bodies/test](https://create.roblox.com/docs/avatar/character-bodies/test).

To ensure your character bodies for avatars can move, interact with objects in the 3D space, and wear cosmetics, clothing, and accessories, it's important to periodically test their components in both your third-party modeling tool and in Studio as you iterate on their design. By testing often, you can save yourself a lot of time in having to rework time-intensive processes like rigging, skinning, and caging.

Whether you are using a [[external/roblox-creator-docs/avatar/resources#templates|template character]] or [[external/roblox-creator-docs/avatar/resources#project-files|project file]] as a basis for your character body, reference the following tables for common tests and resources you can use throughout the creation process to comprehensively quality check each component of your character models.

<Tabs>
  <TabItem label="Blender Tests">

  <Alert severity = 'info'>
  You can apply the following workflows with any 3D modeling software, though certain interfaces and instructions may differ between platforms. For more information, see [[external/roblox-creator-docs/avatar/character-bodies/test-blender|Test character bodies in Blender]].
  </Alert>

<table>
<thead>
  <tr>
    <th style={{width:"40%"}}>Component</th>
    <th>Testing recommendations</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><img src="../../assets/art/avatar/Component-Body-Parts.png" /> <br /><center>**Body Parts**</center></td>
    <td>When modeling, confirm that your character's geometry follows Roblox's [[external/roblox-creator-docs/avatar/character-bodies/specifications#geometry|geometry specifications]].</td>
  </tr>
  <tr>
    <td><img src="../../assets/art/avatar/Component-Texture-Map.png" /> <br /><center>**Textures**</center></td>
    <td>When texturing, confirm that your character's textures follow Roblox's [[external/roblox-creator-docs/avatar/character-bodies/specifications#textures|texture specifications]]. </td>
  </tr>
  <tr>
    <td><img src="../../assets/art/avatar/Component-Rigging.png" /> <br /><center>**Rigging**</center></td>
    <td>Use Blender's [[external/roblox-creator-docs/avatar/character-bodies/test-blender#skinning-data|posing tools]] to check the rigging and skinning quality of your character's body.<br /></td>
  </tr>
  <tr>
    <td><img src="../../assets/art/avatar/Component-Facial-Animation-Data.png" /> <br /><center>**Face Animation**</center></td>
    <td>Confirm that your character's [[external/roblox-creator-docs/avatar/character-bodies/test-blender#facial-animation-data|FACS data]] is present and correctly configured.</td>
  </tr>
  <tr>
    <td><img src="../../assets/art/avatar/Component-Cage-Mesh.png" /> <br /><center>**Cage Mesh**</center></td>
    <td>Manually verify that your cage meshes completely and tightly cover your character model and follow Roblox's [[external/roblox-creator-docs/avatar/character-bodies/specifications#outer-cages|outer cage specifications]].</td>
  </tr>
  <tr>
    <td><img src="../../assets/art/avatar/Component-Attachments.png" /> <br /><center>**Attachments**</center></td>
    <td>Manually verify that your attachment points are correctly positioned and follow Roblox's [[external/roblox-creator-docs/avatar/character-bodies/specifications#attachments|attachment specifications]].</td>
  </tr>
</tbody>
</table>
  </TabItem>
  <TabItem label="Studio Tests">

  <Alert severity = 'info'>
  Roblox provides an uncopylocked testing place file that includes quick access to various environments and testing features. For more information, see [[external/roblox-creator-docs/avatar/character-bodies/test-studio|Test character bodies in Studio]].
  </Alert>

<table>
<thead>
  <tr>
    <th style={{width:"40%"}}>Component</th>
    <th>Testing recommendations</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><img src="../../assets/art/avatar/basic-creation/Testing-Emotes.png" /> <br /><center>**Body Parts**</center></td>
    <td>Test how your character's body parts [[external/roblox-creator-docs/avatar/character-bodies/test-studio#movement-and-animation|move and animate]] in the 3D space.</td>
  </tr>
  <tr>
    <td><img src="../../assets/art/avatar/basic-creation/Testing-Skin-Tone.png" /> <br /><center>**Textures**</center></td>
    <td>Test how your character looks in [[external/roblox-creator-docs/avatar/character-bodies/test-studio#lighting-and-color|various lighting environments and skin tone colors]].</td>
  </tr>
  <tr>
    <td><img src="../../assets/art/avatar/basic-creation/Testing-Outdoor-Environment.png" /> <br /><center>**Rigging**</center></td>
    <td>Use [[external/roblox-creator-docs/avatar/character-bodies/test-studio#movement-and-animation|animations and testing environments]] to verify your character's rigging, skinning, and movement quality.</td>
  </tr>
  <tr>
    <td><img src="../../assets/art/avatar/basic-creation/Testing-Face-Animation.png" /> <br /><center>**Face Animation**</center></td>
    <td>[[external/roblox-creator-docs/avatar/character-bodies/test-studio#movement-and-animation|Cycle through various facial animations]] to ensure your character can perform common expressions.</td>
  </tr>
  <tr>
    <td><img src="../../assets/art/avatar/basic-creation/Testing-Clothing-Try-On.png" /> <br /><center>**Cage Mesh**</center></td>
    <td>[[external/roblox-creator-docs/avatar/character-bodies/test-studio#clothing-and-accessories|Equip various clothing items]] to check for fit and for any unexpected cosmetic issues.</td>
  </tr>
  <tr>
    <td><img src="../../assets/art/avatar/basic-creation/Testing-Clothing.png" /> <br /><center>**Attachments**</center></td>
    <td>[[external/roblox-creator-docs/avatar/character-bodies/test-studio#clothing-and-accessories|Equip various accessory items]] to verify rigid accessory placement and orientation.</td>
  </tr>
</tbody>
</table>
</TabItem>
</Tabs>


## Related Files

- [[external/roblox-creator-docs/avatar/character-bodies/test-blender]] - Blender tests for character bodies.
- [[external/roblox-creator-docs/avatar/character-bodies/index]] - Character bodies.
- [[external/roblox-creator-docs/avatar/character-bodies/project-files]] - Character body reference files.
- [[external/roblox-creator-docs/avatar/character-bodies/specifications]] - Character body specifications.
- [[external/roblox-creator-docs/avatar/character-bodies/export]] - Export character bodies.
- [[external/roblox-creator-docs/avatar/character-bodies/import]] - Import character bodies.
- [[external/roblox-creator-docs/avatar/character-bodies/test-studio]] - Studio tests for character bodies.
