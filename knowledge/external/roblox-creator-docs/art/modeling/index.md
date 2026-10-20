---
title: Custom 3D assets
description: External modeling is the use of a third-party modeling software to create custom 3D assets.
tags: [roblox, documentation, external-reference, priority-reference, art, assets, index]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/modeling/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/modeling/index.md). Published page: [https://create.roblox.com/docs/art/modeling](https://create.roblox.com/docs/art/modeling).

Meshes are **custom 3D assets** that let you personalize and stylize your game's environment and characters. Unlike parts, which you can directly create in Studio, you need to use a third-party modeling application like [Blender](https://www.blender.org) or [Maya](https://www.autodesk.com/products/maya/overview) to design and model meshes, then import them into Studio. Studio represents imported meshes as `Class.MeshPart` objects, descendants of the `Class.BasePart` class.

<Alert severity = 'info'>
Many 3D assets are made up of several meshes that are parented to a single `Class.Model` object.
</Alert>

Meshes typically fall into one of three types of application in games:

- Meshes for **decorating your game's environment**, such as plants, buildings, and vehicles.
- Meshes for **individual body parts** for avatars or non-player characters (NPCs).
- Meshes for **cosmetic accessories** that characters can equip and wear, such as clothing, props, and weapons.

Each mesh type must meet specifications according to how you are going to use the mesh on the platform. For example, while all meshes must meet general mesh specifications, meshes for characters must also meet character specifications that account for rigging and skinning data. For a full list of specifications for different types of meshes, see [Resources](#resources).

In addition, if you meet certain account requirements, you can publish and sell collections of meshes that are parented to a single `Class.Model` object. For example, you can publish avatar-ready models on the Marketplace and earn a commission for each sale, or you can sell models on the Creator Store and earn 100% of net proceeds on each transaction.

<Alert severity = 'info'>
For more information on monetizing meshes, see [Monetize avatar items](../../monetize-avatar.md) and [[external/roblox-creator-docs/production/creator-store#distribute-and-sell-assets|Creator Store - Distribute and sell assets]].
</Alert>

<GridContainer numColumns="3">
  <figure>
    <img src="../../assets/modeling/meshes/Mystery-of-Duvall-Example.png" alt="A cluttered interior room with a candle in the forefront and spooky interior lighting from the Mystery of Duvall Drive game"/>
    <figcaption>Use custom meshes and models to give your environments ambiance and depth</figcaption>
  </figure>
  <figure>
    <img src="../../assets/modeling/meshes/Beyond-The-Dark-Example.png" alt="A floating alien creature in space, from the Beyond The Dark game"/>
    <figcaption>Design a custom character unique to your game</figcaption>
  </figure>
  <figure>
    <img src="../../assets/modeling/surface-appearance/Layered-Clothing-Example.png" alt="A Roblox avatar wearing a glossy puffy jacket and jeans"/>
    <figcaption>Create custom accessories, clothing, and characters that anyone can wear and use</figcaption>
  </figure>
</GridContainer>

## Supported 3D assets

Roblox supports many types of custom 3D assets, as long as they adhere to the [[external/roblox-creator-docs/art/modeling/specifications|general mesh specifications]]. A basic custom 3D asset consists of at least one `Class.MeshPart` object and one texture:

<GridContainer numColumns="3">
  <figure>
    <img src="../../assets/art/Basic-Mesh-Example.png" alt="A plain white tree mesh without a texture"/>
    <figcaption>A `Class.MeshPart` object sets the shape and geometry of the 3D asset</figcaption>
  </figure>
  <figure>
    <img src="../../assets/art/Basic-Texture-Example.png" alt="Various color maps used to apply textures to the tree bark, and inner, middle, and outer leaves"/>
    <figcaption>A texture image map applies a surface appearance and color</figcaption>
  </figure>
  <figure>
    <img src="../../assets/art/Basic-Mesh-Combined-Example.png" alt="The tree mesh and the image maps combined to create a single tree"/>
    <figcaption>The mesh and texture combine to make a unique custom 3D asset</figcaption>
  </figure>
</GridContainer>

Studio also supports custom 3D assets that include [rigging and skinning](#rigging-and-skinning) data, [PBR textures](#pbr-textures), and other [Studio-related objects](#studio-related-objects) like cage meshes and attachments. Many of these various components are required if you are creating avatar character models or accessories.

### Rigging and skinning

A **rigged mesh** is a `Class.MeshPart` object with an internal poseable skeleton rig and bone structure. Rigged meshes allow mesh surfaces to rotate and move where internal bone joints are placed within a model, such as a character's knee or elbow. Skinning a rigged mesh allows the mesh to bend organically, imitating the natural way joints would move in real life.

<GridContainer numColumns="2">
  <figure>
    <video controls src="../../assets/modeling/skinned-meshes/Head-Rigid-Example.mp4"></video>
    <figcaption>Without skinning, the entire head mesh rotates on a single axis</figcaption>
  </figure>
  <figure>
    <video controls src="../../assets/modeling/skinned-meshes/Head-Skinned-Example.mp4"></video>
    <figcaption>With skinning, the head mesh bends naturally at the neck, and the bottom of the neck stays connected to the torso</figcaption>
  </figure>
</GridContainer>

For more information on rigging and skinning, see [[external/roblox-creator-docs/art/modeling/rigging|Rigging and skinning]].

### PBR textures

**Physically-Based rendering** (PBR) textures allow you to represent realistic shading and lighting by using multiple types of texture images, or **maps**, on a single 3D asset. Combining multiple texture maps can more accurately simulate color, roughness, and reflectivity in any lighting environment, and can enhance the visual elements of your assets and environment.

<GridContainer numColumns="2">
  <img src="../../assets/modeling/surface-appearance/SurfaceAppearance-Example-1.jpg" alt="A realistic looking leafy bush with shadows and depth."/>
  <img src="../../assets/modeling/surface-appearance/SurfaceAppearance-Example-3.jpg" alt="A realistic looking rock with moss on the top." />
</GridContainer>

For more information on PBR textures, see [[external/roblox-creator-docs/art/modeling/surface-appearance|PBR textures]].

### Studio-related objects

Studio automatically converts certain types of objects found in 3D modeling files as specific workspace objects in the game. These are typically used when creating a character or accessory, and configuring these in your modeling software can sometimes be the primary way of correctly setting up these Studio objects.

The following objects are automatically created in Studio if they are detected by the 3D Importer:

- `Class.Attachment` - Created when Studio detects mesh objects that include `_Att` at the end of their name.
- `Class.WrapTarget` - Created when Studio detects mesh objects that include `_OuterCage` at the end of their name.
- `Class.WrapLayer` - Created when Studio detects a mesh object with `_InnerCage` and similarly named mesh object with `_OuterCage` at the end of their names.
- `Class.FaceControls` - Created when Studio detects an avatar character head and the appropriate facial animation data in the model.

For more information on how the `Class.WrapTarget` and `Class.WrapLayer` objects reshape and layer meshes, see [[external/roblox-creator-docs/art/modeling/cage-meshes/index|Cage meshes]].

## Resources

There are a variety of resources available for creators of all backgrounds to get started with custom 3D assets.

If you are interested in specific avatar creation topics, use the following table to find guides and resources that best match your needs:

<table>
<thead>
  <tr>
    <th>Topic</th>
    <th>Resources</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Reference files</td>
    <td>[[external/roblox-creator-docs/art/modeling/project-files|Example models, project kits, and templates]]</td>
  </tr>
  <tr>
    <td>Technical specs</td>
    <td>[[external/roblox-creator-docs/art/modeling/export-requirements|.FBX export settings]]<br /><br />[[external/roblox-creator-docs/art/modeling/specifications|General mesh specifications]]<br /><br />
    [[external/roblox-creator-docs/avatar/character-bodies/specifications|Avatar specifications]]<br /><br />[[external/roblox-creator-docs/avatar/rigid-accessories/index|Accessory specifications]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace policy]]</td>
  </tr>
  <tr>
    <td>Bodies and clothing creation</td>
    <td>[[external/roblox-creator-docs/avatar/rigid-accessories/index|Accessories overview]]<br /><br />[[external/roblox-creator-docs/avatar/character-bodies/index|Bodies overview]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-face-accessories|Face accessory creation]]<br /><br />[[external/roblox-creator-docs/avatar/accessory-fitting-tool|Accessory Fitting Tool]]<br /><br />[[external/roblox-creator-docs/avatar/rigid-accessories/specifications|Accessory specifications]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace requirements]]</td>
  </tr>
  <tr>
    <td>Texturing</td>
    <td>[[external/roblox-creator-docs/art/modeling/texture-specifications|Texture specifications]]<br /><br />[[external/roblox-creator-docs/art/modeling/surface-appearance|PBR textures]]</td>
  </tr>
  <tr>
    <td>Rigging and skinning</td>
    <td>[[external/roblox-creator-docs/art/modeling/rigging|Rigging and skinning overview]]<br /><br />[[external/roblox-creator-docs/art/modeling/rig-a-simple-mesh|Basic mesh rigging]] <br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads#rig-and-skin-the-head|Facial bone rigging]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads#skin-joints|Facial bone skinning]]<br /><br />[[external/roblox-creator-docs/avatar/character-bodies/specifications#rigging|Avatar rigging requirements]]<br /><br />[[external/roblox-creator-docs/avatar/automatic-skinning-transfer|Automatic skinning transfer]]</td>
  </tr>

  <tr>
    <td>Facial animation and live heads</td>
    <td>[[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads|Basic head creation]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-face-accessories|Face accessory creation]]<br /><br />[[external/roblox-creator-docs/avatar/dynamic-heads/facs-poses-reference|FACS pose references]]</td>
  </tr>
  <tr>
    <td>Testing and validation</td>
    <td>[[external/roblox-creator-docs/art/modeling/calisthenics-tool|Calisthenics Tool]]<br /><br />[[external/roblox-creator-docs/art/accessories/validation-tool|Clothing Validation Tool]]</td>
  </tr>
  <tr>
    <td>Publishing and Marketplace</td>
    <td>[[external/roblox-creator-docs/marketplace/publish-to-marketplace|Upload to Marketplace]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace policy]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-fees-and-commissions|Fees and commissions]]</td>
  </tr>
</tbody>
</table>


## Related Files

- [[external/roblox-creator-docs/art/modeling/gltf-export]] - 3D Export.
- [[external/roblox-creator-docs/art/modeling/assign-textures]] - Blender and Maya texture settings.
- [[external/roblox-creator-docs/art/modeling/calisthenics-tool]] - Calisthenics Tool.
- [[external/roblox-creator-docs/art/modeling/export-requirements]] - Export settings.
- [[external/roblox-creator-docs/art/modeling/specifications]] - General specifications.
- [[external/roblox-creator-docs/art/modeling/material-reference]] - Material references.
- [[external/roblox-creator-docs/art/modeling/project-files]] - Modeling project files and references.
- [[external/roblox-creator-docs/art/modeling/surface-appearance]] - PBR textures.
- [[external/roblox-creator-docs/art/modeling/reimport]] - Reimport.
- [[external/roblox-creator-docs/art/modeling/rig-a-humanoid-model]] - Rig a humanoid model.
- [[external/roblox-creator-docs/art/modeling/rig-a-simple-mesh]] - Rig a simple mesh.
- [[external/roblox-creator-docs/art/modeling/rigging]] - Rigging and skinning.
- [[external/roblox-creator-docs/art/modeling/roblox-blender-plugin]] - Roblox Blender plugin.
- [[external/roblox-creator-docs/art/modeling/skin-a-humanoid-model]] - Skin a humanoid model.
- [[external/roblox-creator-docs/art/modeling/skin-a-simple-mesh]] - Skin a simple mesh.
- [[external/roblox-creator-docs/art/modeling/texture-specifications]] - Texture specifications.
