---
title: Emotes specifications
description: Character specification lists the specific technical requirements for custom characters created outside of Studio.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/emotes/specifications.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/emotes/specifications.md). Published page: [https://create.roblox.com/docs/art/emotes/specifications](https://create.roblox.com/docs/art/emotes/specifications).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/emotes/specifications]]. Kept locally so existing links keep working; read that page for current information.

Emotes are made up of an `Class.Animation` object with the `Class.Animation.AnimationId` property set to the asset ID of your animation sequence.

<GridContainer numColumns="2">
  <figure>
    <img src="../../assets/avatar/avatar-emotes/Animation-Explorer.png" />
    <figcaption><center>`Animation` object in the Explorer.</center></figcaption>

  </figure>
  <figure>
    <img src="../../assets/avatar/avatar-emotes/Animation-Properties.png" />
    <figcaption><center>`AnimationId` property in the Properties window.</center></figcaption>
  </figure>
</GridContainer>

Only the `Class.Animation` object is required to upload an emote to the Marketplace. Animations do not require meshes, textures, or other 3D art components.

## Animation requirements

Emotes must also meet the following requirements or may fail validation:

- Emotes must be less than 10 seconds.
- The joint root of the character can not move too far from its starting position.
- Movement speed can't exceed a certain threshold to prevent teleportation abuse (measured from a frame-by-frame basis).
- Animation data must reference an R15 rig.
- Animation must be sourced from a `CurveAnimation`. For information on converting animation data, see [[external/roblox-creator-docs/art/emotes/import#generate-asset-id|import and configure]].
- Animations must meet [[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace]] and [Community](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Standards) policies.


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/emotes/export-settings]] - Animation export settings.
- [[external/roblox-creator-docs/art/emotes/index]] - Emotes.
- [[external/roblox-creator-docs/art/emotes/import]] - Import and configure animations.
- [[external/roblox-creator-docs/marketplace/marketplace-policy]] - Marketplace policy.
