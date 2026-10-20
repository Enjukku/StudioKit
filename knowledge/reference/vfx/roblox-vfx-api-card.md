---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: docs agent · claude-sonnet-5-5 · medium · 2026-10-20
Source: local Creator Docs mirror (knowledge/external/roblox-creator-docs/), read 2026-10-20.

Legend: ND = not documented in the mirror (never guessed). Default col: value only if a mirror page states it; "(tut)" = stated only in a tutorial. Mirror paths are relative to `knowledge/external/roblox-creator-docs/`: API = `_api-reference/classes/<X>.yaml`, ENUM = `_api-reference/enums/`, DT = `_api-reference/datatypes/`.

## 1. Classes

### 1.1 ParticleEmitter (parent: BasePart or Attachment; Attachment gives point emission)
| Property | Type | Range/limits | Default | What it does | Gotcha |
| --- | --- | --- | --- | --- | --- |
| Enabled | bool | - | ND | Continuous emission on/off | false keeps live particles until they expire; Clear() to remove |
| Rate | float | 400/s per emitter, 100/s mobile | 20 (tut) | Particles per second while Enabled | Cap from guide; tutorial uses Rate 50000 on one emitter (conflict, see 4) |
| Lifetime | NumberRange | max 20 s (capped internally); 0 = no emission | 5-10 s (tut) | Per-particle age min..max | Changing it leaves live particles on old lifetime |
| Speed | NumberRange | negative = reverse | ND | Initial speed studs/s along EmissionDirection | Does not affect live particles |
| SpreadAngle | Vector2 | 360 on one axis = circle, both = sphere | ND | Random cone angle per axis, degrees | Applied around EmissionDirection; (180,180) = all directions |
| EmissionDirection | NormalId | enum 0-5 | Top (tut) | Parent face particles leave from | On Attachment rotate the attachment instead |
| Acceleration | Vector3 | studs/s^2, global axes | ND | Continuous force on all particles | Affects live and future particles; Speed 0 + -Y = falling drops |
| Drag | float | negative = speed grows exponentially | ND | Seconds for a particle to lose half its speed | Scales Speed and inherited velocity |
| VelocityInheritance | float | 0..1 | ND | Share of parent velocity given to particles | 1 = same speed as parent; alt to LockedToPart |
| LockedToPart | bool | - | ND | Particles move rigidly with parent | - |
| WindAffectsDrag | bool | needs Drag > 0 | ND | Follow Workspace.GlobalWind | No effect at Drag 0 |
| TimeScale | float | 0..1 | ND | Effect speed; 0 freezes | - |
| Size | NumberSequence | envelope per keypoint | ND (flat default) | World size (studs) of square sprite over life | Fill-rate cost grows with screen pixels covered |
| Squash | NumberSequence | >0 narrower+taller, <0 wider+shorter | ND | Non-uniform scale over life | Case study: Squash 20 stretched particles, Size also raised (resources/the-mystery-of-duvall-drive/develop-a-moving-world.md) |
| Transparency | NumberSequence | 0 opaque .. 1 invisible (not rendered) | flat 0 (tut) | Alpha over life | Fade in/out avoids pop; envelope randomizes per particle |
| Color | ColorSequence | RGB 0-1 per channel | white (tut) | Tint over life | With LightEmission>0, darker = more transparent |
| Texture / TextureContent | ContentId / Content | PNG w/ alpha best | white sparkle | Sprite image | TextureContent assignment updates Texture |
| LightEmission | float | 0..1 | ND | 0 normal blend, 1 additive | Does NOT light the world; grayscale w/o alpha: set 1 to hide darks |
| LightInfluence | float | 0..1, outside undefined | 1 if inserted by Studio, 0 via Instance.new | Env light on particle: 0 full bright, 1 black in darkness | Brightness only works at 0 |
| Brightness | float | ND | ND | Scales emitted light when LightInfluence = 0 | - |
| LocalTransparencyModifier | float | 0..1 | 0 | Local-client-only transparency multiplier | Does NOT replicate; 1 - (1-T)(1-LTM) |
| Orientation | ParticleOrientation | 0-3 | FacingCamera | Particle geometry facing | see 3 |
| Rotation | NumberRange | degrees, + = clockwise | ND | Start angle | New particles only; [0,360] random |
| RotSpeed | NumberRange | deg/s, - = counter-clockwise | ND | Angular speed | Very high speed aliases vs frame rate (360/frame = still) |
| ZOffset | float | studs, fractional | ND | Render depth shift toward (+) / away (-) camera, no size change | Very negative renders inside/behind parent part; layers emitters |
| Shape / ShapeStyle / ShapeInOut / ShapePartial | enums + float | see 3 | ND / Volume / Outward / ND | Emission volume | Sphere and Cylinder break on Attachment parent |
| ShapePartial | float | 0..1 | ND | Cylinder: top radius share (0 = cone). Disc: inner radius share (1 = rim only). Sphere: hemisphere angle (0.5 half dome, 0 = pole point) | Box ignores it |
| FlipbookLayout | ParticleFlipbookLayout | 0-4 | ND | Sheet grid, None = static | Custom uses FlipbookSizeX/Y |
| FlipbookSizeX / FlipbookSizeY | int | columns / rows | ND | Custom grid | Only for Custom |
| FlipbookMode | ParticleFlipbookMode | 0-3 | ND | Playback type | OneShot ignores FlipbookFramerate |
| FlipbookFramerate | NumberRange | max 30 fps | ND | Frames per second (random in range) | Ignored by OneShot |
| FlipbookStartRandom | bool | - | ND | Random first frame per particle | Framerate 0 + this = random static cell |
| FlipbookBlendFrames | bool | - | ND | Crossfade vs hard swap | - |
| FlipbookIncompatible | string | - | ND | Error text if texture unfit | "texture size must be an exact multiple of layout size" |
| VelocitySpread | float | - | ND | DEPRECATED, use SpreadAngle | - |

| Method / event | Signature | Behaviour | Gotcha |
| --- | --- | --- | --- |
| Emit | Emit(particleCount: int = 16) | Instantly emits N particles | Works when Enabled = false; emitter needs to exist >= 1 frame (not in mirror, see 5) |
| Clear | Clear() | Removes all live particles (Rate or Emit made) | Use with Enabled=false to hard stop |
Source: API ParticleEmitter.yaml; effects/particle-emitters.md; tutorials/use-case-tutorials/vfx/{basic-particle-effects,use-particles-for-explosions}.md (defaults marked tut).

### 1.2 Beam (needs Attachment0 + Attachment1, both Workspace descendants)
| Property | Type | Range/limits | Default | What it does | Gotcha |
| --- | --- | --- | --- | --- | --- |
| Attachment0 / Attachment1 | Attachment | must differ | nil | Start / end points | Remove either = beam stops rendering |
| Enabled | bool | - | ND | Visibility | - |
| Width0 / Width1 | float | studs; <0 set to 0 (Studio) | ND | Width at start / end, linear between | - |
| Segments | int | ND cap | 10 | Straight pieces forming the curve | Need >= n-1 segments for n Color/Transparency keypoints |
| Color | ColorSequence | spans length | ND | Tint along beam | Solid line if no Texture |
| Transparency | NumberSequence | 0..1 | ND | Alpha along beam (not over time) | Same n-1 segment rule |
| Texture / TextureContent | ContentId / Content | - | none = solid line | Image on beam | Invalid/unloaded id shows solid line |
| TextureMode | TextureMode | Stretch/Wrap/Static | ND | Repeat rule | Static acts as Wrap on beams |
| TextureLength | float | - | ND | Wrap/Static: repeats = beam length / TextureLength. Stretch: repeats = TextureLength times | - |
| TextureSpeed | float | negative reverses | 1 | Texture cycles per second, Attachment0 -> 1 | 0 = static |
| CurveSize0 / CurveSize1 | float | studs | ND | Bezier handle length: P1 = +X of Att0, P2 = -X of Att1 | Attachment orientation sets curve direction |
| FaceCamera | bool | - | ND | Billboard toward CurrentCamera | Off = invisible from some angles (2D plane) |
| LightEmission | float | 0..1 | ND | 0 normal blend, 1 additive | Does not light the world |
| LightInfluence | float | clamp 0..1 | ND | Env lighting effect | - |
| Brightness | float | 0..10000 | 1 | Light scale when LightInfluence < 1 | Higher LightInfluence weakens it |
| LocalTransparencyModifier | float | 0..1 | 0 | Local-only; not replicated | - |
Source: API Beam.yaml; effects/beams.md.

### 1.3 Trail (needs Attachment0 + Attachment1 on a moving part)
| Property | Type | Range/limits | Default | What it does | Gotcha |
| --- | --- | --- | --- | --- | --- |
| Attachment0 / Attachment1 | Attachment | - | nil | Edge points; gap = trail width | Changing them mid-draw deletes drawn segments |
| Enabled | bool | - | ND | Draw new segments | false leaves old segments until Lifetime; call Clear() too |
| Lifetime | float | 0.01-20 s | 2 | Seconds a segment lives | Changing it applies to existing segments immediately (older ones vanish) |
| MinLength | float | studs | ND | Min movement before new segment | Affects new segments only |
| MaxLength | float | studs | 0 = none | Max trail length, oldest erased | - |
| WidthScale | NumberSequence | 0..1 | ND | Width multiplier over life (x attachment gap) | 0.5 on 2-stud gap = 1 stud, centered |
| Color | ColorSequence | - | ND | Tint over segment life | Edits recolor old segments |
| Transparency | NumberSequence | 0..1 | ND | Alpha over segment life | - |
| Texture / TextureContent | ContentId / Content | - | none = solid plane | Image | - |
| TextureMode / TextureLength | TextureMode / float | Stretch/Wrap/Static | ND | Stretch: repeats TextureLength times over trail. Wrap/Static: TextureLength = tile length | Wrap = stationary vs attachments; Static = stamped in world (tracks, prints) |
| FaceCamera | bool | - | ND | Billboard | Applies to existing segments |
| LightEmission / LightInfluence / Brightness | float | 0..1 / clamp 0..1 / 0..10000 | Brightness 1 | Same as Beam | - |
| LocalTransparencyModifier | float | 0..1 | 0 | Local-only | Not replicated |
| Clear() | method | - | - | Remove all segments now | Alone does not stop new ones |
Source: API Trail.yaml; effects/trails.md.

### 1.4 Attachment
| Property | Type | Range/limits | Default | What it does | Gotcha |
| --- | --- | --- | --- | --- | --- |
| CFrame / Position / Orientation | CFrame / Vector3 | local to parent | Position (0,0,0) | Offset + rotation (Orientation order Z,X,Y) | Valid parent for emitters, lights, beams, trails |
| WorldCFrame / WorldPosition / WorldOrientation / WorldAxis / WorldSecondaryAxis | world space | writable | - | World-space equivalents | - |
| Axis (X) / SecondaryAxis (Y) | Vector3 | unit | (1,0,0) / (0,1,0) | Orientation basis | Setting Axis re-projects SecondaryAxis |
| Visible | bool | - | false | Green sphere in play | Debug |
| Rotation / WorldRotation | Vector3 | - | - | DEPRECATED (use Orientation / WorldOrientation) | - |
| GetAxis/SetAxis/GetSecondaryAxis/SetSecondaryAxis | methods | - | - | DEPRECATED | Use the properties |
Source: API Attachment.yaml. Beam curve/spotlight Face on attachments use attachment axes: -Z front, +X right, +Y top.

### 1.5 Lights (Light base: PointLight, SpotLight, SurfaceLight; must be direct child of BasePart or Attachment inside Workspace)
| Property | Type | Range/limits | Default | What it does | Gotcha |
| --- | --- | --- | --- | --- | --- |
| Light.Brightness | float | ND | 1 | Intensity at center | Does not enlarge Range |
| Light.Color | Color3 | - | ND | Light color | - |
| Light.Enabled | bool | - | ND | Emit on/off | - |
| Light.Shadows | bool | - | ND | Cast shadows when blocked | Costly; disable where unneeded |
| PointLight.Range | float | studs | ND | Sphere radius | Tutorials: 50-60 for big areas |
| SpotLight.Range / Angle / Face | float / float / NormalId | Angle max 180 (= half sphere) | ND | Cone length / apex angle / emitting face | On Attachment, Face picks axis |
| SurfaceLight.Range / Angle / Face | float / float / NormalId | Angle 0 = straight out, 180 = perpendicular | ND | Emits from whole face | On Attachment acts like SpotLight |
Source: API Light/PointLight/SpotLight/SurfaceLight.yaml; effects/light-sources.md; volcano tutorial (Brightness 15, Range 60, color 255,85,0 as sample only).

### 1.6 Highlight
| Property | Type | Range/limits | Default | What it does | Gotcha |
| --- | --- | --- | --- | --- | --- |
| Adornee | Instance | Model or BasePart | nil (uses parent) | Target when Highlight is not a child | May sit in Workspace, StarterPlayer, StarterGui, StarterPack, ReplicatedStorage |
| Enabled | bool | - | ND | Toggle | Disabled still holds one of 255 slots |
| FillColor / OutlineColor | Color3 | - | ND (Studio-inserted: red tint fill, white outline) | Interior / outline color | - |
| FillTransparency / OutlineTransparency | float | 0 opaque .. 1 invisible | 0 | Visibility | Invisible highlights cost nothing |
| DepthMode | HighlightDepthMode | 0 AlwaysOnTop, 1 Occluded | ND | Through-wall or hidden | - |
Source: API Highlight.yaml; effects/highlighting.md.

### 1.7 Post effects (PostEffect.Enabled bool on all; parent to Lighting = all players, to Workspace.CurrentCamera = that player only)
| Class.Property | Type | Range/limits | Default | What it does | Gotcha |
| --- | --- | --- | --- | --- | --- |
| BloomEffect.Intensity | float | ND | ND | Additive blend strength of blooming colors | Several Blooms stack |
| BloomEffect.Size | float | px radius; 0 = no bleed | ND | Bloom radius | 0 keeps color adjustment |
| BloomEffect.Threshold | float | 0 all colors bloom .. 1 only pure white | ND | Brightness needed to bloom | Volcano sample: 0.75 / 80 / 0.85 |
| ColorCorrectionEffect.Brightness | float | -1 black .. 1 white | ND | Shift pixels | Several stack |
| ColorCorrectionEffect.Contrast | float | <0 less, >0 more | ND | Dark/light separation | - |
| ColorCorrectionEffect.Saturation | float | >1 vivid, -1 full gray | ND | Color intensity | - |
| ColorCorrectionEffect.TintColor | Color3 | multiplicative | ND | Scales RGB channels | (255,0,0) zeroes G and B |
| BlurEffect.Size | float | px radius | ND | Gaussian blur of 3D view | Only one applies: greatest Size wins; GUIs unaffected |
| DepthOfFieldEffect.FocusDistance | float | studs | ND | In-focus distance | - |
| DepthOfFieldEffect.InFocusRadius | float | studs each side | ND | No-blur band around focus | - |
| DepthOfFieldEffect.NearIntensity / FarIntensity | float | ND | ND | Blur nearer / farther than the band | - |
| SunRaysEffect.Intensity / Spread | float | Spread 0..1 (outside undefined) | ND | Ray opacity / width | May not render on low-end devices |
| ColorGradingEffect.TonemapperPreset | TonemapperPreset | 0 Default, 1 Retro | ND | Tonemap look | Retro = pre-2019 |
Source: API {Bloom,ColorCorrection,Blur,DepthOfField,SunRays,ColorGrading,Post}Effect.yaml; environment/post-processing-effects.md.

### 1.8 Lighting / Atmosphere / Camera / Debris / TweenService (VFX-relevant only)
| Item | Type | Range/limits | Default | What it does | Gotcha |
| --- | --- | --- | --- | --- | --- |
| Lighting.Brightness | float | ND | ND | Sun/moon intensity | Ambient and OutdoorAmbient also change look |
| Lighting.ExposureCompensation | float | -5..5 | 0 | Exposure bias before tonemap; 1 = 2x, -1 = 1/2x | - |
| Lighting.Ambient / OutdoorAmbient | Color3 | - | (0,0,0) / (127,127,127) | Fill color indoors / outdoors | Outdoor clamped >= Ambient; GlobalShadows off = Ambient everywhere |
| Lighting.ColorShift_Top / _Bottom | Color3 | - | ND | Tint on sun-facing / opposite surfaces | - |
| Lighting.GlobalShadows | bool | voxels 4x4x4 studs | ND | Dynamic shadows | Objects under 4 studs give weak shadows |
| Lighting.ShadowSoftness | float | 0 hard .. 1 soft | ND | Shadow blur | Only when LightingStyle = Realistic |
| Lighting.LightingStyle | LightingStyle | 0 Realistic, 1 Soft | ND | Look target | Technology is DEPRECATED (superseded by LightingStyle + PrioritizeLightingQuality) |
| Lighting.PrioritizeLightingQuality | bool | - | ND | Shadow/shader quality vs view distance when quality drops | - |
| Lighting.EnvironmentDiffuseScale / EnvironmentSpecularScale | float | - | 0 / 0 | Sky-derived ambient / reflections | - |
| Atmosphere.Density/Offset/Color/Decay/Glare/Haze | float/Color3 | ND | ND | Haze, glare, fog tint | Hides Lighting fog props; Decay needs Haze+Glare > 0; Glare needs Haze > 0 |
| Camera.FieldOfView | float | 1-120 (clamped) | 70 | Vertical FOV degrees | Extremes disorient |
| Camera.CameraType | CameraType | 0 Fixed, 5 Custom, 6 Scriptable (see enum) | Custom | Camera behaviour | Scriptable stops default camera scripts |
| Debris:AddItem(item, lifetime = 10) | method | hardcoded 1000 items | - | Timed Destroy w/o yield | Over 1000: oldest destroyed instantly; lifetime is a maximum; MaxItems DEPRECATED/read-only; addItem DEPRECATED |
| TweenInfo.new(time=1, style=Quad, dir=Out, repeatCount=0, reverses=false, delay=0) | DT | repeatCount -1 = forever | shown | Tween timing | Two tweens on same property: newest wins |
| TweenService:Create(inst, info, props) / GetValue(alpha, style, dir) | methods | tweens number, bool, CFrame, Color3, UDim2, Vector2/3, EnumItem | - | Property tween / easing sample | Tween.Completed passes PlaybackState |
Source: API Lighting/Atmosphere/Camera/Debris/TweenService/TweenBase.yaml; DT TweenInfo.yaml.

## 2. Data types
| Type | Rules | Mapping |
| --- | --- | --- |
| NumberSequence | >= 2 keypoints; first time 0, last time 1; ascending time; linear interpolation; Keypoint = (Time 0-1, Value, Envelope >= 0); envelope picks random value in [Value-Env, Value+Env] per keypoint per particle at emit. Constructors: new(n), new(n0,n1), new{keypoints}. Keypoint count cap: not documented in mirror (project glossary says 2-20, source R-206) | Particle: age/Lifetime. Beam: position along length (Segments). Trail: segment age/Lifetime |
| ColorSequence | Same time rules; linear interpolation in RGB; channels 0-1; no envelope. Cap: not documented in mirror | Same mappings as above |
| NumberRange | Min <= Max; 32-bit floats; new(v) = fixed | Random per particle (Lifetime, Speed, Rotation, RotSpeed, FlipbookFramerate) |
| Evaluate | No built-in evaluator (envelopes random) | Docs give a manual lerp over Keypoints |
Source: DT NumberSequence/NumberSequenceKeypoint/ColorSequence/ColorSequenceKeypoint/NumberRange.yaml; effects/particle-emitters.md.

## 3. Enums (value = meaning)
| Enum | Values |
| --- | --- |
| ParticleOrientation | 0 FacingCamera billboard; 1 FacingCameraWorldUp (rotates only about world Y); 2 VelocityParallel (along motion); 3 VelocityPerpendicular |
| ParticleEmitterShape | 0 Box; 1 Sphere; 2 Cylinder; 3 Disc |
| ParticleEmitterShapeInOut | 0 Outward (default); 1 Inward; 2 InAndOut (random per particle) |
| ParticleEmitterShapeStyle | 0 Volume (default); 1 Surface |
| ParticleFlipbookLayout | 0 None; 1 Grid2x2 (4 frames); 2 Grid4x4 (16); 3 Grid8x8 (64); 4 Custom (SizeX x SizeY) |
| ParticleFlipbookMode | 0 Loop; 1 OneShot (frame time = Lifetime / frames); 2 PingPong; 3 Random (crossfades) |
| ParticleFlipbookTextureCompatible | 0 NotCompatible (flipbook off); 1 Compatible; 2 Unknown (initial); engine-set, read-only |
| TextureMode | 0 Stretch; 1 Wrap; 2 Static (Trail only, Beam treats as Wrap) |
| HighlightDepthMode | 0 AlwaysOnTop; 1 Occluded |
| NormalId | 0 Right; 1 Top; 2 Back; 3 Left; 4 Bottom; 5 Front |
| EasingStyle | 0 Linear; 1 Sine; 2 Back; 3 Quad; 4 Quart; 5 Quint; 6 Bounce; 7 Elastic; 8 Exponential; 9 Circular; 10 Cubic |
| EasingDirection | 0 In; 1 Out; 2 InOut |
| CameraType | 0 Fixed; 1 Attach; 2 Watch; 3 Track; 4 Follow; 5 Custom; 6 Scriptable; 7 Orbital |
| LightingStyle / TonemapperPreset | 0 Realistic, 1 Soft / 0 Default, 1 Retro |
Source: ENUM files of the same names.

## 4. Hard limits and behaviours
| Topic | Fact | File |
| --- | --- | --- |
| Particle Rate | Up to 400/s per emitter, 100/s on mobile | effects/particle-emitters.md |
| Rate vs tutorial | create-basic-visual-effects sets Rate 50000 on a huge part (dust); no doc reconciles it with the 400 cap | tutorials/curriculums/core/building/create-basic-visual-effects.md |
| Particle Lifetime | Max 20 s, higher values capped; Lifetime 0 = nothing emits | particle-emitters.md; API ParticleEmitter.yaml |
| Trail Lifetime | 0.01-20 s | API Trail.yaml |
| Flipbook texture | Playback needs a 1024x1024 texture (enum doc); guide example is 1024x1024 8x8; FlipbookIncompatible says size must be an exact multiple of layout size | ENUM ParticleFlipbookTextureCompatible; API ParticleEmitter.yaml |
| Flipbook framerate | Max 30 fps; OneShot ignores it | API ParticleEmitter.yaml |
| Flipbook frames | Leave transparent spacing between frames; mip filtering may need more | particle-emitters.md |
| Flipbook memory | Low-memory clients auto-disable flipbooks (older phones); reuse textures, fewer unique sheets, smaller resolution | particle-emitters.md; volcano tutorial |
| Texture authoring | PNG, transparent background; grayscale lets Color tint it; blur edges | particle-emitters.md; custom-particle-effects.md |
| Highlight count | 255 simultaneous per client, extras silently ignored; disabled ones keep a slot (delete instead). The 31 figure is NOT in the mirror | effects/highlighting.md; API Highlight.yaml |
| Highlight cost | Property changes are cheap; add/remove can spike (geometry rebuild); first on screen costs up to 1 ms GPU on mobile; mobile cost grows with screen coverage; invisible/disabled-visible cost none; avoid nesting Highlighted objects inside other Highlighted objects (back-to-front draw) | highlighting.md |
| Beam Segments | Default 10; need >= n-1 for n Color/Transparency keypoints; max not documented | API Beam.yaml |
| Beam Brightness / Trail Brightness | 0-10000, default 1 | API Beam.yaml, Trail.yaml |
| LightEmission | 0 normal blending, 1 additive; documented range 0-1; never lights environment (use a PointLight) | API ParticleEmitter/Beam/Trail.yaml |
| LightInfluence | 0 = unaffected by env light, 1 = fully lit like a part (black in darkness) | API ParticleEmitter.yaml |
| Brightness link | Emitter/Beam/Trail Brightness scales emitted light only when LightInfluence is below 1 (Particle: at 0); more LightInfluence reduces it | API ParticleEmitter/Beam/Trail.yaml |
| ZOffset | Studs toward camera (+) / away (-), size unchanged; very negative goes inside/behind parent | API ParticleEmitter.yaml |
| Emitter shape on Attachment | Sphere and Cylinder shapes display wrong | particle-emitters.md |
| Replication | Only LocalTransparencyModifier (Particle/Beam/Trail) is stated not to replicate; Emit/Clear/property replication not documented. Post effects: Lighting = everyone, Camera = that player | API; post-processing-effects.md |
| Quality scaling | Visuals vary by device quality; test lowest and highest Editor Quality Level. Post effects may differ or not run at low QualityLevel; SunRays may not render on low-end; Blur/Bloom/DoF render differently on low-end; shadows degrade then turn off below quality level 4; highlights pixelated on low-end | particle-emitters.md; API PostEffect/SunRays.yaml; performance-optimization/improve.md |
| Particle cost | Fill-rate (size) and overdraw (overlap); particles/decals batch poorly; ParticleEmitter property changes can cost a lot; MicroProfiler tag updateParticles: cut emitter count, rate, lifetime, emitter movement | particle-emitters.md; performance-optimization/improve.md, microprofiler/tag-table.md |
| Light cost | Many shadow-casting lights hurt; disable Light.Shadows, limit Range and Angle, fewer lights, disable far/other-room lights | performance-optimization/improve.md |
| Attachments required | Beam and Trail stop rendering without both attachments; changing Trail attachments clears drawn segments | beams.md; trails.md |
| Debris | 1000 item cap, oldest destroyed first; lifetime is a maximum | API Debris.yaml |
| Fire / Smoke objects | Pre-made, far less customizable than ParticleEmitter | basic-particle-effects.md |
| Documented defaults | Basic tutorial: default particles last 5-10 s, EmissionDirection Top, Rate 20; the API pages state no defaults | basic-particle-effects.md |

## 5. Docs say vs practitioners say
| Topic | Docs (mirror) | Project practitioner file | Action |
| --- | --- | --- | --- |
| Beam segments | Need >= n-1 for n keypoints | zonito ZO-13: keypoints + 1 (2 if opaque) | Use the docs minimum n-1; test ZO-13 in Studio |
| Highlight cap | 255 (silently ignored beyond) | brief mentions 31 | Docs and 02a/07 files say 255; 31 unsupported |
| Flipbook size | Enum doc: 1024x1024 required; field text: exact multiple of layout size | ZO-12: other textures smaller (420 max), flipbooks 1024 | Flipbook sheet = 1024x1024 |
| Rate | 400/s cap, 100/s mobile | ZO-01: engine already scales Rate on mobile; Emit() spam may bypass scaling | Docs silent on Emit scaling: Studio check |
| Emit timing | Emit(n) described as instant, no frame condition | ZO-04: emitter must exist >= 1 frame, Emit replicates before Parent, wait ~0.03 s | Not in mirror; follow ZO-04 |
| LightEmission range | 0..1 documented | building-blocks: negative values on 8% of pro emitters (-0.3, -1, -5) | Outside documented range; treat as unsupported style |
| LightInfluence | Default 1 from Studio, 0 from Instance.new | building-blocks: 0 on 979/980 emitters | Set explicitly in code (Instance.new gives 0) |
| Brightness | Beam/Trail 0-10000 | building-blocks: pros use 5-15, max 50 | Compatible; only works at low LightInfluence |
| NumberSequence keypoints | No cap in mirror | glossary: 2-20 | Keep to 20 |
| Transparency start | Fade in/out recommended | building-blocks: starts 0.00 for most jobs except smoke | Compatible |
