---
title: Character bodies
description: All Roblox users are represented by an avatar character which can be customized with body parts, accessories, and clothes from the Marketplace or within games.
tags: [roblox, documentation, external-reference, priority-reference, avatar]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [avatar/character-bodies/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/avatar/character-bodies/index.md). Published page: [https://create.roblox.com/docs/avatar/character-bodies](https://create.roblox.com/docs/avatar/character-bodies).

<iframe width="800" height="450" src="https://www.youtube-nocookie.com/embed/2My8jE47clI" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>

**Character bodies** for avatars are models with technical components that work together to create a character that can interact with objects in the 3D space and wear cosmetics, clothing, and accessories. There are four main layers of the avatar body that structure how the character looks and moves on the platform:

- **Body parts & textures** that make up the character's visual appearance.
- **Rigging armature** that determines how the character moves.
- **Facial animation data** in the character's head that expresses the character's personality and emotions.
- **Cage meshes & attachments** that determine how the character attaches accessories and wears clothing.

While you can create each of these layers manually in third-party modeling tools like [Blender](https://www.blender.org/) or [Maya](https://www.autodesk.com/products/maya/overview), some have strict configuration requirements to meet Roblox's technical [[external/roblox-creator-docs/avatar/character-bodies/specifications|character specifications]] that guarantee your avatar behaves consistently from game to game. Before you create your first custom character body, it's recommended to:

1. Understand the [essential components](#character-body-components) of an avatar's character body and how they work together on the platform.
1. Review all [resources](#resources) that Roblox provides to standardize and expedite the [creation process](#creation-process), such as Blender and Maya project files, Studio tooling, and step-by-step guides.
1. Follow the [[external/roblox-creator-docs/art/characters/creating/index|basic character creation tutorial]] that uses Roblox templates in collaboration with common Blender modeling and texturing tools.

Once you have a custom character body model, you can import it into Studio and use the Avatar Setup tool to process your creation into an avatar asset that's ready to be sold on the [[external/roblox-creator-docs/marketplace/index|Marketplace]].

## Character body components

All character bodies for avatars are made up of several fundamental components that provide users the functionality and flexibility to interact with their world. Many of these components are never made visible to the user, but they enable powerful avatar features that enhance social and environmental interactions. When creating avatar characters, all of these components are typically created first in your modeling software and then converted to their appropriate Roblox Studio instance on import.

Each avatar character is made up of the following rendered and non-rendered components:

<Tabs>
  <TabItem label="Rendered">
<GridContainer numColumns="2">
  <figure><img src="../../assets/art/avatar/Component-Body-Parts.png" />  <figcaption>15 separate body part meshes make up the shape and contours of the character.</figcaption></figure>

  <figure><img src="../../assets/art/avatar/Component-Texture-Map.png" /><figcaption>Texture image maps apply a surface color and appearance to the character's skin.</figcaption></figure>
  
</GridContainer>
  </TabItem>
  <TabItem label="Non-Rendered">
<GridContainer numColumns="2">
  <figure><img src="../../assets/art/avatar/Component-Rigging.png" />  <figcaption>A rigging armature allows the body parts to properly connect with each other, driving movement, expressions, and animations.</figcaption></figure>

  <figure><img src="../../assets/art/avatar/Component-Facial-Animation-Data.png" /> <figcaption>Facial animation data allows avatars to express virtually all types of facial expressions for chatting and socializing.</figcaption></figure>
</GridContainer>
<GridContainer numColumns="2">
  <figure><img src="../../assets/art/avatar/Component-Cage-Mesh.png" />  <figcaption>Cage meshes define the surface where layered accessories can wrap and stretch over.</figcaption></figure>

  <figure><img src="../../assets/art/avatar/Component-Attachments.png" />  <figcaption>Attachment points define where rigid accessories attach to a character.</figcaption></figure>

</GridContainer>
  </TabItem>
</Tabs>

### Body parts

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/avatar/Body-Parts-Visual.png" />  <figcaption>Each avatar character is made up of 15 separate mesh objects</figcaption></figure>

  <figure><img src="../../assets/art/avatar/Body-Parts-Data-Model.png" width="100%"/><figcaption>These meshes must follow a standard naming convention</figcaption></figure>
</GridContainer>

An avatar's physical body geometry is made up of 15 separate mesh body parts that define the shape and contours of the character:

- Head
- Upper and lower torso
- Left upper arm, lower arm, and hand
- Right upper arm, lower arm, and hand
- Left upper leg, lower leg, and foot
- Right upper leg, lower leg, and foot

In Studio, these geometries are represented as `Class.MeshPart` objects and are nested under a single `Class.Model`.

### Textures

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/avatar/Textures-Brown.png" />  <figcaption>Textures apply color and surface details to your character model.</figcaption></figure>

  <figure><img src="../../assets/art/avatar/Textures-Blue.png" /><figcaption>A texture image map's opacity can combine with the `Class.MeshPart.Color` to apply custom skin tones to characters.</figcaption></figure>
</GridContainer>

Textures are image files that define the surface appearance of your character. You can create textures using a texture painting program or 3D modeling software. In Studio, you must import textures as image files and set them to `Class.MeshPart` objects by a child `Class.SurfaceAppearance` object or the mesh's `Class.MeshPart.TextureID|TextureID` property.

<Alert severity = 'warning'>
When texturing parts of your character model's body, ensure that your character model includes a modesty layer over sensitive regions. See [Community Standards](https://en.help.roblox.com/hc/en-us/articles/203313410#safety) for more information on Roblox's policies.
</Alert>

### Rigging armature

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/avatar/Rigging-Visual.png" />  <figcaption>The rigging armature includes at least 16 bones, 1 for each body part and a root bone. Higher-fidelity rigs can include up to 37 additional bones.</figcaption></figure>

  <figure><img src="../../assets/avatar/specifications/High-Fidelity-LeftHand.png" /><figcaption>Bones must follow a specific hierarchy and naming convention</figcaption></figure>  
</GridContainer>

Inside of the avatar's physical body is a non-rendered rigging armature that allows the character to articulate its limbs. Often referred to as joints or bones, a rigging armature includes skinning data that allows connections between limbs to bend organically, such as the character's knees and elbows.

[[external/roblox-creator-docs/avatar/character-bodies/specifications#standard-r15-rigs|Standard avatar rigs]] (R15) require 15 poseable joints to articulate the character's 15 body parts. However, if you want to create higher-fidelity characters with a greater level of realism, there are up to 37 additional optional joints for [[external/roblox-creator-docs/avatar/character-bodies/specifications#advanced-r15-rigs|advanced R15 rigs]] that you can create for articulated hands, shoulders, and spine movements.

In Studio, each joint of the rigging armature is represented by `Class.Bone` objects that connect the character's body part `Class.MeshPart` objects together. `Class.Bone` objects must follow a specific hierarchy and naming convention for the avatar to function properly in Studio and on the Marketplace. For more information, see [[external/roblox-creator-docs/avatar/character-bodies/specifications#rigging|Rigging]].

### Face animation data

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/avatar/Facial-Rig-Visual.png" />  <figcaption>Each avatar character face is rigged and skinned to create various expressions</figcaption></figure>
  
 <figure><img src="../../assets/art/avatar/Facial-Properties.png" /><figcaption>Each pose is mapped to a pose name within the Custom Properties (Extra Attributes in Maya) of the Head_Geo object</figcaption></figure>
</GridContainer>

<figure><img src="../../assets/art/avatar/Facial-Animation-Timeline.png" /><figcaption>Each required face pose is saved as a keyframe in the animation timeline.</figcaption></figure>

Facial animation data from either the character's rigging armature or facial joints allow avatars to express emotions with their eyes, mouth, and teeth. Each character includes facial joints, skinning data, animation timeline data, and mapped pose data that allows these expressions. In Studio, these facial animation elements are represented by a `Class.FaceControls` instance.

### Cage meshes

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/avatar/Cage-Mesh-Visual.png" />  <figcaption>Head and Upper Torso cage mesh objects (wireframe)</figcaption></figure>

  <figure><img src="../../assets/art/avatar/Cage-Mesh-Data-Model.png" width="100%"/><figcaption>Cage objects must exist for each of the 15 body parts</figcaption></figure>
</GridContainer>

Cage meshes set the invisible outer boundary for layered accessories to stretch and fit over body parts, allowing clothes to fit over models of different shapes and sizes without you having to remodel the clothing item each time. In Studio, outer cage mesh objects are represented by a `Class.WrapTarget` instance.

If you are caging your own non-template character model, it's important to use one of Roblox's body cage [[external/roblox-creator-docs/avatar/resources#mannequin-models|project files]] to ensure you are using a Roblox standard cage mesh. Removing or adding vertices from this standard mesh can cause issues with clothing fit and import.

### Attachments

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/avatar/Attachments-Visual.png" />  <figcaption>Each character has common attachment points for equipping rigid cosmetics</figcaption></figure>

  <figure><img src="../../assets/art/avatar/Attachments-Data-Model.png" width="100%"/><figcaption>Each avatar character must include their associated 19 attachment points</figcaption></figure>
</GridContainer>

Attachment points set the specific points where rigid accessories and in-game equippable objects attach to the character's body. These are not rendered on the platform, but they are represented visually as spheres in 3D modeling software when you use Roblox's **R15 Rig and Attachments** [[external/roblox-creator-docs/avatar/resources#project-files|project file]].

When you import a rig with these visual representations, the spheres are created as `Class.Attachment` objects using standardized names.

<Alert severity = 'info'>
When users wear a layered accessory, the layered accessory isn't attached directly to the attachment, but it does reference the associated attachment point during ragdoll and dismemberment animations.
</Alert>

## Creation process

When designing a character body in [Blender](https://www.blender.org/) or [Maya](https://www.autodesk.com/products/maya/overview), you must export all of the avatar components in a single `.fbx` or `.gltf` for import into Studio. Since 3D creation isn't a linear process and always requires reiteration and testing, the process of creating an avatar character model can differ between individuals and various creation workflows.

In general, the creation process follows these typical workflows:

<GridContainer numColumns="2">
  <figure><center>**Basic Creation with Templates**</center><br />Customize a [[external/roblox-creator-docs/art/characters/creating/index|character body template]] that already includes all the necessary components.<img src="../../assets/art/avatar/Workflow-Bodies-Templates.png"/></figure>

  <figure><center>**Advanced Creation from Scratch**</center><br />Create characters from scratch, allowing full customization of the avatar character's components.<img src="../../assets/art/avatar/Workflow-Bodies-Traditional.png"/></figure>
</GridContainer>

<Alert severity = 'warning'>
Ensure that all assets you create follow Roblox's [Community Standards](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Standards) and any applicable [[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace policies]].
</Alert>

## Resources

There are a variety of resources available for creators of all backgrounds to get started with character creation. Review the following table for specific topics and resources:

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
    <td>[[external/roblox-creator-docs/art/characters/creating/index|Basic character creation tutorial]]</td>
  </tr>
  <tr>
    <td>Reference files</td>
    <td>[[external/roblox-creator-docs/avatar/character-bodies/project-files|Avatar references and project files]]<br /><br />[[external/roblox-creator-docs/art/modeling/project-files|Example mesh/model objects]]</td>
  </tr>
  <tr>
    <td>Technical specs</td>
    <td>[[external/roblox-creator-docs/avatar/character-bodies/export|.FBX export settings]]<br /><br />[[external/roblox-creator-docs/avatar/character-bodies/specifications|Avatar specifications]]<br /><br />[[external/roblox-creator-docs/art/modeling/specifications|General mesh specifications]]<br /><br />[[external/roblox-creator-docs/avatar/rigid-accessories/specifications|Accessory specifications]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace policy]]</td>
  </tr>
  <tr>
    <td>Cosmetic creation</td>
    <td>[[external/roblox-creator-docs/avatar/rigid-accessories/index|Accessories overview]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-face-accessories|Creating face accessories]]<br /><br />[[external/roblox-creator-docs/avatar/accessory-fitting-tool|Accessory Fitting Tool]]<br /><br />[[external/roblox-creator-docs/avatar/rigid-accessories/specifications|Accessory specifications]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace requirements]]</td>
  </tr>
  <tr>
    <td>Texturing</td>
    <td>[[external/roblox-creator-docs/art/modeling/texture-specifications|Texturing requirements]]<br /><br />[[external/roblox-creator-docs/art/modeling/surface-appearance|PBR textures]]</td>
  </tr>
  <tr>
    <td>Rigging and skinning</td>
    <td>[[external/roblox-creator-docs/art/modeling/rigging|Rigging and skinning overview]]<br /><br />[[external/roblox-creator-docs/avatar/character-bodies/specifications#rigging|Humanoid rig requirements]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads#rig-and-skin-the-head|Rigging facial bones]]<br /><br />[[external/roblox-creator-docs/avatar/automatic-skinning-transfer|Automatic Skinning Transfer]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads#skin-joints|Skinning facial bones]]</td>
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
    <td>[[external/roblox-creator-docs/marketplace/publish-to-marketplace|Uploading to Marketplace]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace policy]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-fees-and-commissions|Fees and commissions]]</td>
  </tr>
</tbody>
</table>


## Related Files

- [[external/roblox-creator-docs/avatar/character-bodies/test-blender]] - Blender tests for character bodies.
- [[external/roblox-creator-docs/avatar/character-bodies/project-files]] - Character body reference files.
- [[external/roblox-creator-docs/avatar/character-bodies/specifications]] - Character body specifications.
- [[external/roblox-creator-docs/avatar/character-bodies/export]] - Export character bodies.
- [[external/roblox-creator-docs/avatar/character-bodies/import]] - Import character bodies.
- [[external/roblox-creator-docs/avatar/character-bodies/test-studio]] - Studio tests for character bodies.
- [[external/roblox-creator-docs/avatar/character-bodies/test]] - Test character bodies.
