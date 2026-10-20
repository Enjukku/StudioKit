---
title: Rigid accessories
description: Rigid accessories are basic 3D cosmetics users can equip and wear on their avatar character.
tags: [roblox, documentation, external-reference, priority-reference, art, assets, index]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/index.md). Published page: [https://create.roblox.com/docs/art/accessories](https://create.roblox.com/docs/art/accessories).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/rigid-accessories/index]]. Kept locally so existing links keep working; read that page for current information.

<Grid container spacing={2} style={{ marginBottom: 24, width: '100%' }}>
<Grid item xs={6} style={{ padding: 16 }}>
<Grid item container wrap="nowrap" direction="column" style={{ gap: 8, flex: 1 }}>

<div
className="container"
style={{ position: "relative", paddingBottom: "56.25%", height: 0, marginBottom: 12 }} >
<iframe
src="https://www.youtube-nocookie.com/embed/tzPn6QvU8Bo"
title="YouTube video player"
frameBorder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
allowFullScreen
style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%" }} ></iframe>
</div>
<Typography variant="body1">
A high-level overview of accessories on Roblox.
</Typography>

</Grid>
</Grid>

<Grid item xs={6} style={{ padding: 16 }}>
<Grid item container wrap="nowrap" direction="column" style={{ gap: 8, flex: 1 }}>

<div
className="container"
style={{ position: "relative", paddingBottom: "56.25%", height: 0, marginBottom: 12 }} >
<iframe
src="https://www.youtube-nocookie.com/embed/Eed29gV0hLA"
title="YouTube video player"
frameBorder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
allowFullScreen
style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%" }} ></iframe>
</div>
<Typography variant="body1">
Create and sell your first basic accessory.
</Typography>
</Grid>
</Grid>
</Grid>

Rigid accessories are the most basic 3D cosmetic items that users can equip and wear on their avatar character, such props, weapons, hats, and more. Unlike [[external/roblox-creator-docs/art/accessories/layered-clothing|clothing accessories]] that stretch and fit over a character body, rigid accessories attach to a specific point on an avatar character and don't deform or wrap over a target.

To create a custom Roblox accessory for your own experience or to sell on the Marketplace, it's important to start with the following:

- A basic background with 3D modeling tools such as [Blender](https://www.blender.org/) or [Maya](https://www.autodesk.com/products/maya/overview).
- An understanding of the [components that make up a rigid accessory](#components-of-a-rigid-accessory).
- An understanding of the general [accessory creation process](#creation-process).
- Review Roblox's official tutorials to create your own accessories:
  - [[external/roblox-creator-docs/art/accessories/creating-rigid/index|Rigid accessory creation tutorial]] - covers each process required for converting a 3D model to a rigid accessory and publishing it to the Marketplace.
  - [[external/roblox-creator-docs/art/accessories/creating/index|Clothing creation tutorial]] - a step-by-step process of creating your own avatar-ready clothing from scratch in Blender.
- [Additional tools, resources, and guides](#resources) provided by Roblox to standardize and expedite the creation process.

## Components of a rigid accessory

All accessory models are made up of the same base components of a [mesh object](#mesh-part), [textures](#textures), and [attachment](#attachments).

When [creating accessories](#creation-process), most of these components are created first in your modeling software, then converted to their appropriate Roblox Studio instance on import.

### Mesh part

<GridContainer numColumns="2">
<figure><img src="../../assets/art/accessories/Mesh-Bow-Example.png" /><figcaption>Bow rigid accessory mesh object</figcaption></figure>

<figure><img src="../../assets/art/accessories/Mesh-Example.png"/>  <figcaption>T-shirt layered clothing mesh object</figcaption></figure>
</GridContainer>

<Alert severity = 'warning'>
Clothing, such as the t-shirt, require [[external/roblox-creator-docs/art/accessories/layered-clothing|additional clothing components]] to apply the layerable effect to the 3D object.
</Alert>

All accessories require a single mesh object that represents the geometry of the accessory object. In Studio, this mesh object is represented as a `Class.MeshPart` nested under a single `Class.Model`.

### Textures

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/accessories/Texture-Example.png" />  <figcaption>2D texture map for the t-shirt model</figcaption></figure>

  <figure><img src="../../assets/art/accessories/Texture-Applied-Example.png" /><figcaption>T-shirt model with texture applied</figcaption></figure>
</GridContainer>

Textures are 2D image files that define the surface appearance of your 3D object. You can create textures within a texture painting program or a 3D modeling software.

In Studio, textures images are imported as image assets and are set to `Class.MeshPart` objects by a child `Class.SurfaceAppearance` object or a `Class.MeshPart.TextureID` property.

### Attachments

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/accessories/Attachment-Example.png" />  <figcaption>Attachment geometry defines where the attachment connects with the character</figcaption></figure>

  <figure><img src="../../assets/art/accessories/Attachment-Data-Model-Example.png" width="80%"/><figcaption>Geometry with the "_Att" suffix automatically convert to `Class.Attachment` objects in Studio</figcaption></figure>
</GridContainer>

Attachment points define where accessories attach to a character's body. In Studio, attachments are represented by `Class.Attachment` objects.

## Creation process

Custom accessories are first created in 3D modeling programs, such as [Blender](https://www.blender.org/) or [Maya](https://www.autodesk.com/products/maya/overview), before importing the `.fbx` or `.gltf` model into Studio.
To get started creating your first avatar asset, see the [[external/roblox-creator-docs/avatar/tutorials|avatar tutorials]].

Depending on the type of asset you are creating, the creation process follows these high-level workflows:

<GridContainer numColumns="2">

  <figure>  <figcaption><center>Rigid Accessory Workflow</center></figcaption><img src="../../assets/art/accessories/Workflow-Rigid.png" /></figure>

  <figure><figcaption><center>Layered Accessory Workflow</center></figcaption><img src="../../assets/art/accessories/Workflow-Layered.png" /></figure>
</GridContainer>

<Alert severity = 'info'>
Since 3D creation isn't a linear process and always requires reiteration and testing, the process of creating an accessory can differ between individuals and various creation workflows.
</Alert>

## Resources

There are a variety of resources available for creators of all backgrounds to get started with accessory creation.

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
    <td>Tutorials</td>
    <td>[[external/roblox-creator-docs/art/accessories/creating-rigid/index|Rigid accessory creation]] <br /><br />[[external/roblox-creator-docs/art/accessories/creating/index|Basic clothing creation]]</td>
  </tr>
  <tr>
    <td>Reference files</td>
    <td>[[external/roblox-creator-docs/art/modeling/project-files|Accessory and clothing reference files]]</td>
  </tr>
  <tr>
    <td>Technical specs</td>
    <td>[[external/roblox-creator-docs/art/modeling/export-requirements|.FBX export settings]]<br /><br />[[external/roblox-creator-docs/art/modeling/specifications|General mesh specifications]]<br /><br />[[external/roblox-creator-docs/art/accessories/specifications|Accessory specifications]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace policy]]</td>
  </tr>
  <tr>
    <td>Cosmetic creation</td>
    <td>[[external/roblox-creator-docs/art/accessories/specifications|Accessories overview]]<br /><br />[[external/roblox-creator-docs/art/accessories/layered-clothing|Layered clothing overview]]<br /><br /><br />[[external/roblox-creator-docs/art/accessories/accessory-fitting-tool|Accessory Fitting Tool]]<br /><br />[[external/roblox-creator-docs/art/accessories/specifications|Accessory specifications]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace requirements]]</td>
  </tr>
  <tr>
    <td>Texturing</td>
    <td>[[external/roblox-creator-docs/art/modeling/texture-specifications|Texturing requirements]]<br /><br />[[external/roblox-creator-docs/art/modeling/surface-appearance|PBR textures]]</td>
  </tr>
  <tr>
    <td>Rigging and skinning</td>
    <td>[[external/roblox-creator-docs/art/modeling/rigging|Rigging and skinning overview]]<br /><br />[[external/roblox-creator-docs/art/characters/specifications#rigging|Humanoid rig requirements]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads#rigging|Rig facial bones]]<br /><br />[[external/roblox-creator-docs/art/accessories/automatic-skinning-transfer|Automatic Skin Transfer]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads#skin-face-bones|Skin facial bones]]</td>
  </tr>
  <tr>
    <td>Publishing and Marketplace</td>
    <td>[[external/roblox-creator-docs/marketplace/publish-to-marketplace|Uploading to Marketplace]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace Policy]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-fees-and-commissions|Fees and commissions]]</td>
  </tr>
</tbody>
</table>


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/accessories/from-existing]] - Accessories from an existing model.
- [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool]] - Accessory Fitting Tool.
- [[external/roblox-creator-docs/art/accessories/project-files]] - Accessory project files and references.
- [[external/roblox-creator-docs/art/accessories/automatic-skinning-transfer]] - Automatic Skinning Transfer.
- [[external/roblox-creator-docs/art/accessories/creating/index]] - Basic clothing creation.
- [[external/roblox-creator-docs/art/accessories/body-scale]] - Body scale and proportions.
- [[external/roblox-creator-docs/art/accessories/caging-best-practices]] - Caging best practices.
- [[external/roblox-creator-docs/art/characters/specifications]] - Character specifications.
- [[external/roblox-creator-docs/art/accessories/clothing-specifications]] - Clothing specifications.
- [[external/roblox-creator-docs/art/accessories/validation-tool]] - Clothing Validation Tool.
- [[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads]] - Create basic heads.
- [[external/roblox-creator-docs/art/modeling/export-requirements]] - Export settings.
- [[external/roblox-creator-docs/art/modeling/specifications]] - General specifications.
- [[external/roblox-creator-docs/art/accessories/import-clothing]] - Import clothing accessories.
- [[external/roblox-creator-docs/art/accessories/importing]] - Import rigid accessories.
- [[external/roblox-creator-docs/art/accessories/layered-clothing]] - Layered clothing.
- [[external/roblox-creator-docs/art/accessories/clothing-export-settings]] - Layered clothing export settings.
- [[external/roblox-creator-docs/marketplace/marketplace-fees-and-commissions]] - Marketplace fees and commissions.
- [[external/roblox-creator-docs/marketplace/marketplace-policy]] - Marketplace policy.
- ...and 11 more local docs.
