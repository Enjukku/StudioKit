---
title: Lighting and effects
description: Create more immersive environments through lighting, atmospheres, and special effects.
tags: [roblox, documentation, external-reference, priority-reference, environment, index]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [environment/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/environment/index.md). Published page: [https://create.roblox.com/docs/environment](https://create.roblox.com/docs/environment).

The `Class.Lighting` container services let you control and customize a game's environment such as [lighting](#global-lighting), [atmosphere](#atmospheric-effects), and [clouds](#clouds-and-skies). You can also apply [post-processing effects](#post-processing-effects) to adjust how the game appears on the screen.

## Global lighting

The `Class.Lighting` service contains properties that you can adjust to update the global lighting in a game, such as the `Class.Lighting.ClockTime|ClockTime` and `Class.Lighting.Brightness|Brightness`.

<Tabs>
<TabItem label="ClockTime = 0">
<img src="../assets/lighting-and-effects/lighting-properties/TimeOfDay-0.jpg" width="800" height="450" alt="Lighting with ClockTime of 0 (TimeOfDay of 00:00:00)" />
</TabItem>
<TabItem label="ClockTime = 6.3">
<img src="../assets/lighting-and-effects/lighting-properties/TimeOfDay-6.3.jpg" width="800" height="450" alt="Lighting with ClockTime of 6.3 (TimeOfDay of 06:18:00)" />
</TabItem>
<TabItem label="Brightness = 0.5">
<img src="../assets/lighting-and-effects/lighting-properties/Brightness-0.5.jpg" width="800" height="450" alt="Lighting with Brightness property of 0.5" />
</TabItem>
<TabItem label="Brightness = 3.75">
<img src="../assets/lighting-and-effects/lighting-properties/Brightness-3.75.jpg" width="800" height="450" alt="Lighting with Brightness property of 3.75" />
</TabItem>
</Tabs>

<Alert severity="info">
In addition to global lighting, you can create and attach [[external/roblox-creator-docs/effects/light-sources|light sources]] to parts or attachments to simulate objects like lamps, torches, spotlights, or TV screens.
</Alert>

## Atmospheric effects

[[external/roblox-creator-docs/environment/atmosphere|Atmospheric effects]] simulate realistic environments by scattering sunlight in unique ways. Using the `Class.Atmosphere` object in the `Class.Lighting` service, you can control air particle [[external/roblox-creator-docs/environment/atmosphere#density|density]], simulate [[external/roblox-creator-docs/environment/atmosphere#haze|haze]] or [[external/roblox-creator-docs/environment/atmosphere#glare|glare]], set an atmosphere's [[external/roblox-creator-docs/environment/atmosphere#color|color]], and more.

<figure>
<img src="../assets/lighting-and-effects/atmosphere/Showcase.jpg" width="800" alt="Atmospheric effects used to render a brilliant sunset scene" />
<figcaption>Atmospheric effects used to render a brilliant sunset scene</figcaption>
</figure>

## Clouds and skies

By default, the `Class.Sky` object forms a [[external/roblox-creator-docs/environment/skybox|skybox]] with celestial bodies such as a sun, moon, and stars. In addition, you can adjust the cloud cover, density, and color properties of the `Class.Clouds` object to render realistic, [[external/roblox-creator-docs/environment/clouds|dynamic clouds]] that drift slowly across the sky through [[external/roblox-creator-docs/environment/global-wind|global wind]].

<figure>
<video src="../assets/lighting-and-effects/clouds/Showcase.mp4" controls width="800" alt="Video of wind blowing dynamic clouds across the sky"></video>
<figcaption>Wind blowing dynamic clouds across the sky</figcaption>
</figure>

## Post-processing effects

**Post-processing effects** are customizable filters that allow you to quickly
enrich the visuals of your game. Using the post-processing effect objects
in the `Class.Lighting` service or `Class.Camera`, you can:

- Simulate a camera viewing a bright light and exaggerate its glow.
- Apply a Gaussian blur to the entirety of your game or add a blur to parts of your game that aren't in focus.
- Enhance an environment's appearance to create a specific mood through hue.
- Render a halo of light that moves with the sun.

<figure>
<img src="../assets/lighting-and-effects/post-processing/DepthOfFieldEffect-With.jpg" width="800" alt="Landscape with depth-of-field effect applied, simulating distance blur" />
<figcaption>Landscape with depth-of-field effect applied, simulating distance blur</figcaption>
</figure>


## Related Files

- [[external/roblox-creator-docs/environment/atmosphere]] - Atmospheric effects.
- [[external/roblox-creator-docs/environment/clouds]] - Dynamic clouds.
- [[external/roblox-creator-docs/environment/lighting]] - Global lighting.
- [[external/roblox-creator-docs/environment/global-wind]] - Global wind.
- [[external/roblox-creator-docs/environment/post-processing-effects]] - Post-processing effects.
- [[external/roblox-creator-docs/environment/skybox]] - Skyboxes.
