---
title: Texturing face
description: Use Blender to apply a custom surface appearance on your character's face.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
next: /art/characters/creating/texturing-pbr
prev: /art/characters/creating/texturing-eyes
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/characters/creating/texturing-face.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/characters/creating/texturing-face.md). Published page: [https://create.roblox.com/docs/art/characters/creating/texturing-face](https://create.roblox.com/docs/art/characters/creating/texturing-face).

After texturing the eyes, you can begin texturing the face. The concepts are similar to texturing the eyes, though you only use an opaque texture to ensure that the custom skin tone can remain visible.

To texture the face:

1. In the **Texture Paint** tab, [[external/roblox-creator-docs/art/characters/creating/texturing-setup#set-texture-resolution|resize your texture resolution]] to **2048** or **4096**:
1. Update your brush settings in the tool sidebar for the facial features.

   1. In **Brush Settings**:

      1. Set **Radius** to **5px**.
      1. Set **Strength** to **0.300**.

   1. In **Symmetry**, enable **X-Axis Mirroring**.

         <img src="../../../assets/art/avatar/basic-creation/Texture-Symmetry-Tool-Setting.png" />

   1. In **Color Picker**, set **Color** to a neutral dark shade for the shadows.

1. Apply texture to your character's face features, such as the nostrils, wrinkles, ears, and chin. Keep in mind that the painted textures will look softer and blended with the surface once the texture resolution is resized.

   <video controls src="../../../assets/art/avatar/basic-creation/Texturing_10.mp4" width="100%"></video>

1. When complete, resize your texture resolution back to **1024 x 1024**.

   <video controls src="../../../assets/art/avatar/basic-creation/Texturing_11.mp4" width="100%"></video>

Your final result should include various facial textures that help accentuate the features of your character and work well with any custom skin tone. Try exploring various amounts of texturing and the types of surfaces you could expect on skin, such as wrinkles, scars, or dirt/grunge. You should also verify your textures between several skin tones to ensure that your texturing looks acceptable with various skin types.

<GridContainer numColumns="3">
  <figure><img src="../../../assets/art/avatar/basic-creation/Post-Texturing-A.png" />  <figcaption>Default Green</figcaption></figure>

  <figure><img src="../../../assets/art/avatar/basic-creation/Post-Texturing-B.png" /><figcaption>Pink</figcaption></figure>

<figure><img src="../../../assets/art/avatar/basic-creation/Post-Texturing-C.png" /><figcaption>Blue</figcaption></figure>

</GridContainer>

<Alert severity = 'success'>
For a comparison reference, you can download [this version of the tutorial project with texturing completed](../../../assets/art/reference-files/checkpoint/2_Goblin-textured.blend).
</Alert>


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
- [[external/roblox-creator-docs/art/characters/creating/texturing-setup]] - Texturing setup.
- ...and 1 more local docs.
