---
title: Rigid accessories
description: Rigid accessories are 3D assets that attach to an avatar according to the attachment points around the character's body.
tags: [roblox, documentation, external-reference, priority-reference, avatar]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [avatar/rigid-accessories/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/avatar/rigid-accessories/index.md). Published page: [https://create.roblox.com/docs/avatar/rigid-accessories](https://create.roblox.com/docs/avatar/rigid-accessories).

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
A high-level overview of rigid accessories on Roblox.
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
Create and sell your first basic rigid accessory.
</Typography>
</Grid>
</Grid>
</Grid>

**Rigid accessories** are 3D objects that attach to attachment points around an avatar character's body. When users purchase rigid accessories on the [Marketplace](https://www.roblox.com/catalog), such as props, weapons, and hats, they can adjust the position and rotation of the item away from the attachment point according to their avatar's body type.

There are two main layers of a rigid accessory that structure how the accessory looks and works on the platform:

- **Mesh & textures** that make up the rigid accessory's visual appearance.
- **Attachments** that determine how the accessory attaches to the character's body.

While you can create the first of these layers manually in third-party modeling tools like [Blender](https://www.blender.org/) or [Maya](https://www.autodesk.com/products/maya/overview), attachments have strict configuration requirements to meet Roblox's technical [[external/roblox-creator-docs/avatar/rigid-accessories/specifications|rigid accessory specifications]] that guarantee your rigid accessories behave consistently from game to game. Before you create your first custom rigid accessory, it's recommended to:

1. Understand the [essential components](#rigid-accessory-components) of a rigid accessory and how they work together.
1. Review all [resources](#resources) that Roblox provides to standardize and expedite the [creation process](#creation-process), such as Blender and Maya project files, Studio tooling, and step-by-step guides.
1. Follow the [[external/roblox-creator-docs/art/accessories/creating-rigid/index|basic rigid accessory creation tutorial]] that covers how to convert a simple 3D model into a rigid accessory.

Once you have a custom rigid accessory, you can import it into Studio and use the Avatar Setup tool to process your creation into an avatar asset that's ready to be sold on the [[external/roblox-creator-docs/marketplace/index|Marketplace]].

<Alert severity = 'info'>
Unlike rigid accessories that don't deform when they attach to a specific point on the avatar, layered accessories stretch and wrap over a target until it fits over the character's body. For more information, see [[external/roblox-creator-docs/avatar/layered-accessories/index|Layered accessories]].
</Alert>

## Rigid accessory components

All rigid accessories are made up of the same fundamental components that allow users to equip 3D items with consistent behavior **according** to the character's [[external/roblox-creator-docs/avatar/rigid-accessories/specifications#body-scale|body type]].

<Alert severity = 'warning'>
Layered accessories require [[external/roblox-creator-docs/avatar/layered-accessories/index|additional components]] to apply the layerable effect to the 3D item.
</Alert>

### Mesh part

<GridContainer numColumns="2">
<figure><img src="../../assets/art/accessories/Mesh-Bow-Example.png" /><figcaption>Bow rigid accessory mesh object.</figcaption></figure>
<figure><img src="../../assets/art/accessories/Mesh-Hair-Example.png" /><figcaption>Hair rigid accessory mesh object.</figcaption></figure>
</GridContainer>

All rigid accessories require a single mesh object that represents the accessory's geometry. In Studio, this mesh object is represented as a `Class.MeshPart` nested under a single `Class.Model`.

### Textures

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/accessories/Texture-Bow-Example.png" />  <figcaption>2D texture map for the bow rigid accessory.</figcaption></figure>
  <figure><img src="../../assets/art/accessories/Texture-Hair-Example.png" />  <figcaption>2D texture map for the hair rigid accessory.</figcaption></figure>
</GridContainer>

Textures are image files that define the surface appearance of your rigid accessory. You can create textures within a texture painting program or 3D modeling software.

In Studio, you must import textures as image files and set them to `Class.MeshPart` objects by a child `Class.SurfaceAppearance` object or the mesh's `Class.MeshPart.TextureID|TextureID` property.

### Attachments

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/accessories/Attachment-Bow-Example.png" />  <figcaption>The bow's attachment point enables the bow to connect to a character's back.</figcaption></figure>
  <figure><img src="../../assets/art/accessories/Attachment-Hair-Example.png" />  <figcaption>The hair's attachment point enables the hair to connect to a character's head.</figcaption></figure>
</GridContainer>

Attachment points define where accessories attach to a character's body. In Studio, attachment points are represented by `Class.Attachment` objects.

<Alert severity = 'info'>
You can automatically generate attachment points for your rigid accessories using the [[external/roblox-creator-docs/avatar/accessory-fitting-tool|Accessory Fitting Tool]].
</Alert>

## Creation process

When designing a rigid accessory in [Blender](https://www.blender.org/) or [Maya](https://www.autodesk.com/products/maya/overview), you must export all of the avatar components in a single `.fbx` or `.gltf` for import into Studio. Since 3D creation isn't a linear process and always requires reiteration and testing, the process of creating a rigid accessory can differ between individuals and various creation workflows.

In general, the creation process follows the following workflow:

<figure><figcaption><center>Rigid Accessory Workflow</center></figcaption><center><img src="../../assets/art/accessories/Workflow-Rigid.png" width="50%"/></center></figure>

## Resources

There are a variety of resources available for creators of all backgrounds to get started with rigid accessory creation. Review the following table for specific topics and resources:

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
    <td>[[external/roblox-creator-docs/art/accessories/creating-rigid/index|Rigid accessory creation]]</td>
  </tr>
  <tr>
    <td>Reference files</td>
    <td>[[external/roblox-creator-docs/art/modeling/project-files|Accessory and clothing reference files]]</td>
  </tr>
  <tr>
    <td>Technical specs</td>
    <td>[[external/roblox-creator-docs/art/modeling/export-requirements|.FBX export settings]]<br /><br />[[external/roblox-creator-docs/art/modeling/specifications|General mesh specifications]]<br /><br />[[external/roblox-creator-docs/avatar/rigid-accessories/specifications|Rigid accessory specifications]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace policy]]</td>
  </tr>
  <tr>
    <td>Cosmetic creation</td>
    <td>[[external/roblox-creator-docs/avatar/rigid-accessories/index|Rigid accessories overview]]<br /><br />[[external/roblox-creator-docs/avatar/layered-accessories/index|Layered clothing overview]]<br /><br /><br />[[external/roblox-creator-docs/avatar/accessory-fitting-tool|Accessory Fitting Tool]]<br /><br />[[external/roblox-creator-docs/avatar/rigid-accessories/specifications|Rigid accessory specifications]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace requirements]]</td>
  </tr>
  <tr>
    <td>Texturing</td>
    <td>[[external/roblox-creator-docs/art/modeling/texture-specifications|Texturing requirements]]<br /><br />[[external/roblox-creator-docs/art/modeling/surface-appearance|PBR textures]]</td>
  </tr>
  <tr>
    <td>Rigging and skinning</td>
    <td>[[external/roblox-creator-docs/art/modeling/rigging|Rigging and skinning overview]]<br /><br />[[external/roblox-creator-docs/avatar/character-bodies/specifications#rigging|Humanoid rig requirements]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads#rig-and-skin-the-head|Rig facial bones]]<br /><br />[[external/roblox-creator-docs/avatar/automatic-skinning-transfer|Automatic Skin Transfer]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads#skin-joints|Skin facial bones]]</td>
  </tr>
  <tr>
    <td>Publishing and Marketplace</td>
    <td>[[external/roblox-creator-docs/marketplace/publish-to-marketplace|Uploading to Marketplace]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace Policy]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-fees-and-commissions|Fees and commissions]]</td>
  </tr>
</tbody>
</table>


## Related Files

- [[external/roblox-creator-docs/avatar/rigid-accessories/export]] - Export rigid accessories.
- [[external/roblox-creator-docs/avatar/rigid-accessories/import]] - Import rigid accessories.
- [[external/roblox-creator-docs/avatar/rigid-accessories/specifications]] - Rigid accessory specifications.
