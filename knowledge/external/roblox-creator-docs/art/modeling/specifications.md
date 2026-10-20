---
title: General specifications
description: Lists the specific technical requirements for custom models created outside of Studio.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/modeling/specifications.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/modeling/specifications.md). Published page: [https://create.roblox.com/docs/art/modeling/specifications](https://create.roblox.com/docs/art/modeling/specifications).

Roblox supports a wide variety of mesh configurations created from third-party software such as [Blender](https://www.blender.org) or [Maya](https://www.autodesk.com/products/maya/overview).

Check that your model meets the following modeling specifications and guidelines before exporting to ensure Studio compatibility. Specific types of assets, like characters and accessories, have additional specifications:

<Alert severity = 'warning'>
<AlertTitle>If creating other types of 3D models:</AlertTitle>
<ul>
<li>For rigid accessories, see [[external/roblox-creator-docs/avatar/rigid-accessories/specifications|accessory specifications]] and [[external/roblox-creator-docs/avatar/rigid-accessories/export|accessory export settings]].</li> <br />
<li>For layered accessories, see [[external/roblox-creator-docs/avatar/layered-accessories/specifications|layered accessory specifications]] and [[external/roblox-creator-docs/avatar/layered-accessories/export|layered export settings]].</li> <br />
<li>For avatar characters, see [[external/roblox-creator-docs/avatar/character-bodies/specifications|avatar specifications]] and [[external/roblox-creator-docs/avatar/character-bodies/export|avatar export settings]].</li>
</ul>
</Alert>

When ready to export, see the [[external/roblox-creator-docs/art/modeling/export-requirements|export settings]] for mesh export settings for Blender and Maya.

<Alert severity='info'>
If you meet certain account requirements, you can sell your custom meshes as accessories on the Marketplace. See [[external/roblox-creator-docs/avatar/rigid-accessories/index|Rigid accessories]] for an overview on the creation process for these types of accessories.
</Alert>

## Geometry

See the following specifications for general geometry:

- **Budgets** - Individual meshes can not exceed 20,000 triangles. Avatar items have their own individual budget requirements for [[external/roblox-creator-docs/avatar/character-bodies/specifications|character bodies]], [[external/roblox-creator-docs/avatar/rigid-accessories/specifications|rigid accessories]], and [[external/roblox-creator-docs/avatar/layered-accessories/specifications|layered accessories]].
- **Watertight** - All geometry must be watertight without exposed holes or backfaces.
- **No N-gons** - Meshes must be in quads where possible.
- **Volume** - Meshes cannot be 0 thickness and must have some volume.

## Rigging and skinning

Roblox supports third-party meshes with an internal rig, or skeleton structure that can be used as additional articulation points in your model. For more information on the specific standards for R15 rigs, see [[external/roblox-creator-docs/avatar/character-bodies/specifications#rigging|Character body specifications - Rigging]].

<GridContainer numColumns="2">
  <figure>
    <img src="../../assets/animation/importing-custom-3d-rigs/Rig-Custom-Puffer-Blender.png" alt="A cartoon-ish low polygon model of a puffer fish."/>
    <figcaption>Generic rig model.</figcaption>
  </figure>
  <figure>
    <img src="../../assets/animation/importing-custom-3d-rigs/Rig-Hierarchy-Custom-Blender-Bones.png" width="75%" alt="The Outliner in Blender of the puffer fish model, showing the armature bone structure."/>
    <figcaption>Generic rig bone structure (Blender).</figcaption>
  </figure>
</GridContainer>

See the following requirements for general rigging and skinning:

- **Transformations** - All bones (Blender) or joints (Maya) must be frozen and have scale values set to `1`, `1`, `1` and rotation values set to `0`, `0`, `0`.
- **Symmetry** - When possible, maintain symmetry when applying influences to a rig
- **Root joint** - The root bone or joint should always be set to `0`, `0`, `0`.
- **Max influences** - A vertex can not be influenced by more than 4 bones or joints.
- **No Root influences** - Do not apply influences to the Root bone or joint.

## Textures

- Roblox supports basic color textures and modern [[external/roblox-creator-docs/art/modeling/surface-appearance|PBR textures]].
- For instructions on assigning texture images to natively import with your mesh, see [[external/roblox-creator-docs/art/modeling/assign-textures|Assign textures in modeling tools]].
- For technical requirements and best practices when generating individual texture images, see [[external/roblox-creator-docs/art/modeling/texture-specifications|Texture specifications]].

## Animations

An animation can be included on any `.fbx` mesh export. For information on prepping a character animation from a modeling software for export, see [[external/roblox-creator-docs/art/characters/export-avatar-animations-from-maya|Export animations from Maya]].

See the following requirements for assets with animation:

- **Single track animation** - Only a single animation track can be exported with a mesh or model. If you want to export multiple animations, you need to create separate exports for each animation you want to import.

## Inner and outer cages

Inner and Outer cages are non-rendered meshes that Roblox uses to define the inner and outer surfaces of a mesh using a `Class.WrapLayer` or `Class.WrapTarget` instance. These cages are most often used with characters and accessories, though you can use cage meshes for any mesh object.

<Alert severity="warning">
Character models must include an outer cage in order to properly equip layered accessories. For more information, see [[external/roblox-creator-docs/avatar/character-bodies/specifications|Character body specifications]].
</Alert>

For general use, see the following requirements for adding inner and outer cage meshes to your model:

- **Naming conventions** - The inner and outer cage must be named after the primary mesh object with **\_InnerCage** and **\_OuterCage** affixed.

   <img src="../../assets/accessories/lc-blender-selecting-cage-in-outlier.png" alt="The Outliner in Blender showing two mesh objects called Tshirt_InnerCage and Tshirt_OuterCage."/>

- **Outer cage** - Models, such as a playable character, that aren't expected to deform but are the target of meshes that will stretch over it, only require an outer cage.
  - For more information on applying and implementing cages on non-Humanoid targets, see [[external/roblox-creator-docs/characters/appearance#layered-accessories-on-non-r15|layered accessories on non-R15]].
- **Vertices and UV map** - Don't delete vertices or alter the UVs on the Inner or Outer Cages as this can cause errors when importing in Studio or when equipping onto a character.
- **Symmetry and consistency** - Keep each face (the space between vertices) consistently sized and retain symmetry wherever possible. Use symmetry tools in your modeling software whenever possible.


## Related Files

- [[external/roblox-creator-docs/art/modeling/gltf-export]] - 3D Export.
- [[external/roblox-creator-docs/art/modeling/assign-textures]] - Blender and Maya texture settings.
- [[external/roblox-creator-docs/art/modeling/calisthenics-tool]] - Calisthenics Tool.
- [[external/roblox-creator-docs/art/modeling/index]] - Custom 3D assets.
- [[external/roblox-creator-docs/art/modeling/export-requirements]] - Export settings.
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
