---
title: Effects
description: Learn how to add visual effects to your games.
tags: [roblox, documentation, external-reference, priority-reference, effects, vfx, index]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [effects/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/effects/index.md). Published page: [https://create.roblox.com/docs/effects](https://create.roblox.com/docs/effects).

You can create special effects by parenting special effect objects to other
objects or attachments.

## Light sources

Light sources let you attach lighting effects to objects or attachments. There
are three types of light sources:

- A `Class.PointLight`
  emits light spherically from a single point. This object is ideal for
  non-directional lights like bulbs, torches, and fireballs.
- A `Class.SpotLight`
  emits light in the shape of a cone with a spherical base. This object is ideal
  for directional lights like street lamps, flashlights, and headlights.
- A `Class.SurfaceLight` emits light from the face of a BasePart. This object is
  ideal for lighting from TV or computer screens, billboards, and fluorescent
  panels.

<GridContainer numColumns="3">
  <figure>
    <img src="../assets/lighting-and-effects/light-sources/PointLight-Range-8.jpg" alt="" />
    <figcaption>Point lights</figcaption>
  </figure>
  <figure>
    <img src="../assets/lighting-and-effects/light-sources/SpotLight-Face-Bottom.jpg" alt="" />
    <figcaption>Spotlights</figcaption>
  </figure>
  <figure>
    <img src="../assets/lighting-and-effects/light-sources/SurfaceLight-Angle-0.jpg" alt="" />
    <figcaption>Surface lights</figcaption>
  </figure>
</GridContainer>

## Particle emitters

A [[external/roblox-creator-docs/effects/particle-emitters|particle emitter]] is an object that emits customizable 2D images (particles) into the world, useful for simulating special effects like fire, smoke, and sparks.

<video src="../assets/lighting-and-effects/particle-emitter/Showcase.mp4"
controls width="100%"></video>

## Beams

A [[external/roblox-creator-docs/effects/beams|beam]] is an object that renders a texture between two
`Class.Attachment` objects `Class.Beam.Attachment0` and
`Class.Beam.Attachment1`. By setting beam properties, you can:

- Add a [[external/roblox-creator-docs/effects/beams#texture|texture]] and [[external/roblox-creator-docs/effects/beams#color|color gradient]] to create interesting visuals like waterfalls and force fields.
- Modify a beam's [transparency](/effects/beams#transparency) so that it fades over time.
- Warp its shape by changing the [[external/roblox-creator-docs/effects/beams#width|width]] or [[external/roblox-creator-docs/effects/beams#curve|curve]] of each attachment point.

<video src="../assets/lighting-and-effects/beam/Showcase.mp4" controls
width="100%"></video>

## Trails

A [[external/roblox-creator-docs/effects/trails|trail]] is an object that creates a trail between and behind two `Class.Attachment` objects as they move through space. Trails can help players visualize movement, such as a sword slashing through the air, projectiles flying to their target, or footprints walking away.

By setting trail properties, you can:

- Add a [[external/roblox-creator-docs/effects/trails#texture|texture]] to create interesting visuals.
- Set a constant or gradient [[external/roblox-creator-docs/effects/trails#color|color]].
- Modify a trail's [[external/roblox-creator-docs/effects/trails#lifetime|lifetime]].

<video src="../assets/lighting-and-effects/trail/Showcase.mp4" controls
width="100%"></video>

## Highlighting

`Class.Highlight` is a visual effect which you can use to call attention to a specific object within a game, such as to provide visual feedback that the object is important and/or interactable. See [[external/roblox-creator-docs/effects/highlighting|Highlighting Objects]] for details.

<GridContainer numColumns="3">
  <figure>
    <img src="../assets/ui/highlighting-objects/OutlineTransparency-1.jpg" alt="A tree mesh against a grey background." />
    <figcaption>Base object</figcaption>
  </figure>
  <figure>
    <img src="../assets/ui/highlighting-objects/Adding-Highlight.jpg" alt="The same tree mesh with a white outline and a red highlight interior." />
    <figcaption>White outline, 50% red interior</figcaption>
  </figure>
  <figure>
    <img src="../assets/ui/highlighting-objects/Overview-Yellow-Outline.jpg" alt="The same tree mesh with a yellow outline and a black highlight interior." />
    <figcaption>Yellow outline, black interior</figcaption>
  </figure>
</GridContainer>


## Related Files

- [[external/roblox-creator-docs/effects/beams]] - Beams.
- [[external/roblox-creator-docs/effects/highlighting]] - Highlighting objects.
- [[external/roblox-creator-docs/effects/light-sources]] - Light sources.
- [[external/roblox-creator-docs/effects/particle-emitters]] - Particle emitters.
- [[external/roblox-creator-docs/effects/trails]] - Trails.
