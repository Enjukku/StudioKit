---
title: Testing characters
comments:
description: Verify the important aspects of your character model in Blender and in Studio.
tags: [roblox, documentation, external-reference, priority-reference, art, assets, index]
next: /art/characters/testing/blender
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/characters/testing/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/characters/testing/index.md). Published page: [https://create.roblox.com/docs/art/characters/testing](https://create.roblox.com/docs/art/characters/testing).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/character-bodies/test]]. Kept locally so existing links keep working; read that page for current information.

It's important to constantly test your models during and after the creation process to ensure that your character can interact with various social and environmental elements in any experience.

Whether you are using a template character, or your own custom assets, use the information provided in [[external/roblox-creator-docs/art/characters/testing/blender|Test in Blender]] and [[external/roblox-creator-docs/art/characters/testing/studio|Test in Studio]] throughout your workflow to comprehensively test your assets and quality check your models.

Use the following table as an overview of common tests and resources to verify each component of your character model.

<Tabs>
  <TabItem label="Blender">
  <Alert severity = 'info'>
  You can apply the following workflows with any modeling software, though certain interfaces and instructions may differ between platforms. See [[external/roblox-creator-docs/art/characters/testing/blender|Testing in Blender]] for additional information.
  </Alert>
<table>
<thead>
  <tr>
    <th style={{width:"25%"}}>Component</th>
    <th>Testing recommendations</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><img src="../../../assets/art/avatar/Component-Body-Parts.png" /> <br /><center>**Body Parts**</center></td>
    <td>When modeling, confirm that your geometry follows [[external/roblox-creator-docs/art/characters/specifications#geometry|avatar geometry specifications]].</td>
  </tr>
  <tr>
    <td><img src="../../../assets/art/avatar/Component-Texture-Map.png" /> <br /><center>**Textures**</center></td>
    <td>When texturing, confirm that your geometry follows [[external/roblox-creator-docs/art/characters/specifications#textures|avatar texture specifications]]. </td>
  </tr>
  <tr>
    <td><img src="../../../assets/art/avatar/Component-Rigging.png" /> <br /><center>**Rigging**</center></td>
    <td>Use [[external/roblox-creator-docs/art/characters/testing/blender#body-skinning|Blender's posing tools]] to check the rigging and skinning quality of your asset.<br /></td>
  </tr>
  <tr>
    <td><img src="../../../assets/art/avatar/Component-Facial-Animation-Data.png" /> <br /><center>**Face Animation**</center></td>
    <td>Confirm that [[external/roblox-creator-docs/art/characters/testing/blender#facial-animation-data|your FACS data]] is present and correctly configured.</td>
  </tr>
  <tr>
    <td><img src="../../../assets/art/avatar/Component-Cage-Mesh.png" /> <br /><center>**Cage Mesh**</center></td>
    <td>Manually verify that your cage mesh completely and tightly covers your character model and follows [[external/roblox-creator-docs/art/characters/specifications#outer-cages|avatar outer cage specifications]].</td>
  </tr>
  <tr>
    <td><img src="../../../assets/art/avatar/Component-Attachments.png" /> <br /><center>**Attachments**</center></td>
    <td>Manually verify that your attachment points are correctly positioned and follow [[external/roblox-creator-docs/art/characters/specifications#attachments|avatar attachment specifications]].</td>
  </tr>
</tbody>
</table>
  </TabItem>
  <TabItem label="Studio">

  <Alert severity = 'info'>
  Roblox provides an uncopylocked testing place that includes quick access to various environments and testing features. See [[external/roblox-creator-docs/art/characters/testing/studio|Testing in Studio]] for additional information.
  </Alert>
<table>
<thead>
  <tr>
    <th style={{width:"25%"}}>Component</th>
    <th>Testing recommendations</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><img src="../../../assets/art/avatar/basic-creation/Testing-Emotes.png" /> <br /><center>**Body Parts**</center></td>
    <td>Verify your character's geometry while in [[external/roblox-creator-docs/art/characters/testing/studio#movement-and-animation|movement and animation]].</td>
  </tr>
  <tr>
    <td><img src="../../../assets/art/avatar/basic-creation/Testing-Skin-Tone.png" /> <br /><center>**Textures**</center></td>
    <td>Test your character in [[external/roblox-creator-docs/art/characters/testing/studio#lighting-and-color|various lighting environments and skin tone colors]].</td>

  </tr>
  <tr>
    <td><img src="../../../assets/art/avatar/basic-creation/Testing-Outdoor-Environment.png" /> <br /><center>**Rigging**</center></td>
    <td>Use [[external/roblox-creator-docs/art/characters/testing/studio#movement-and-animation|animations and testing environments]] to verify your character's rigging, skinning, and movement.</td>

  </tr>
  <tr>
    <td><img src="../../../assets/art/avatar/basic-creation/Testing-Face-Animation.png" /> <br /><center>**Face Animation**</center></td>
    <td>[[external/roblox-creator-docs/art/characters/testing/studio#movement-and-animation|Cycle through various facial animations]] to ensure your character can express common expressions.</td>
  </tr>
  <tr>
    <td><img src="../../../assets/art/avatar/basic-creation/Testing-Clothing-Try-On.png" /> <br /><center>**Cage Mesh**</center></td>
    <td>[[external/roblox-creator-docs/art/characters/testing/studio#clothing-and-accessories|Equip various clothing items]] to check for fit and for any unexpected cosmetic issues.</td>
  </tr>
  <tr>
    <td><img src="../../../assets/art/avatar/basic-creation/Testing-Clothing.png" /> <br /><center>**Attachments**</center></td>
    <td>[[external/roblox-creator-docs/art/characters/testing/studio#clothing-and-accessories|Equip various accessory items]] to verify rigid accessory placement and orientation.</td>
  </tr>
</tbody>
</table>
</TabItem>
</Tabs>


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/characters/index]] - Avatar characters.
- [[external/roblox-creator-docs/art/characters/specifications]] - Character specifications.
- [[external/roblox-creator-docs/art/characters/testing/blender]] - Test in Blender.
- [[external/roblox-creator-docs/art/characters/testing/studio]] - Test in Studio.
