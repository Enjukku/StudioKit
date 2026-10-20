---
title: AlignPosition
description: The AlignPosition constraint applies force to move two attachments together, or to move one attachment to a goal position.
tags: [roblox, documentation, external-reference, priority-reference, physics]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/align-position.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/align-position.md). Published page: [https://create.roblox.com/docs/physics/constraints/align-position](https://create.roblox.com/docs/physics/constraints/align-position).

<Alert severity="info">
For an overview on creating, visualizing, and simulating mover constraints, including `Class.AlignPosition`, see [[external/roblox-creator-docs/physics/mover-constraints|mover constraints]]. Also see [[external/roblox-creator-docs/physics/units|Roblox&nbsp;units]] to understand how Roblox units compare to metric units.
</Alert>

An `Class.AlignPosition` constraint applies force to move two attachments together, or to move one attachment to a goal position. As indicated by the name, it only affects the **position** of the attachments, not their orientation (to align attachments by **orientation**, see [[external/roblox-creator-docs/physics/constraints/align-orientation|AlignOrientation]]).

<video controls src="../../assets/physics/constraints/AlignPosition-Demo.mp4"></video>

<Alert severity="warning">
By default, the constraint only applies force to `Class.Constraint.Attachment0|Attachment0`, although this behavior can be controlled through the constraint's [reactionary force](#reactionary-force).
</Alert>

## Force location

By default, force is applied to the parent of `Class.Constraint.Attachment0|Attachment0` at that attachment's location, meaning that if the parent's center of mass is not aligned with the direction of the force, torque will be applied as well as force. Alternatively, force can be applied to the parents' center of mass by toggling on `Class.AlignPosition.ApplyAtCenterOfMass|ApplyAtCenterOfMass`.

## Force magnitude

You can configure the `Class.AlignPosition` constraint to apply the maximum force that constraints allow through the `Class.AlignPosition.RigidityEnabled|RigidityEnabled` property. When `true`, the physics solver reacts as quickly as possible to complete the alignment. When `false`, the force is determined by `Class.AlignPosition.MaxForce|MaxForce`, `Class.AlignPosition.MaxVelocity|MaxVelocity`, and `Class.AlignPosition.Responsiveness|Responsiveness`.

## Reactionary force

By default, the constraint only applies force to `Class.Constraint.Attachment0|Attachment0` while `Class.Constraint.Attachment1|Attachment1` remains unaffected. If desired, force can be applied to **both** attachments in **equal and opposite directions** by enabling `Class.AlignPosition.ReactionForceEnabled|ReactionForceEnabled`.

<figure>
<video controls src="../../assets/physics/constraints/AlignPosition-ReactionForceEnabled.mp4" width="90%"></video>
</figure>

## Attachment mode

The `Class.AlignPosition.Mode|Mode` property specifies whether the constraint uses **one** or **two** attachments in calculating its goal. By default, this is `Enum.PositionAlignmentMode.TwoAttachment|TwoAttachment`, meaning that the constraint disregards `Class.AlignPosition.Position|Position` and attempts to move `Class.Constraint.Attachment0|Attachment0` to the position of `Class.Constraint.Attachment1|Attachment1`. If set to `Enum.PositionAlignmentMode.OneAttachment|OneAttachment`, the constraint disregards `Class.Constraint.Attachment1|Attachment1` and attempts to move `Class.Constraint.Attachment0|Attachment0` to `Class.AlignPosition.Position|Position`.


## Related Files

- [[external/roblox-creator-docs/physics/constraints/align-orientation]] - AlignOrientation.
- [[external/roblox-creator-docs/physics/constraints/angular-velocity]] - AngularVelocity.
- [[external/roblox-creator-docs/physics/constraints/animation]] - AnimationConstraint.
- [[external/roblox-creator-docs/physics/constraints/ball-socket]] - BallSocket.
- [[external/roblox-creator-docs/physics/constraints/cylindrical]] - Cylindrical.
- [[external/roblox-creator-docs/physics/constraints/hinge]] - Hinge.
- [[external/roblox-creator-docs/physics/constraints/linear-velocity]] - LinearVelocity.
- [[external/roblox-creator-docs/physics/constraints/line-force]] - LineForce.
- [[external/roblox-creator-docs/physics/constraints/no-collision]] - NoCollision.
- [[external/roblox-creator-docs/physics/constraints/plane]] - Plane.
- [[external/roblox-creator-docs/physics/constraints/prismatic]] - Prismatic.
- [[external/roblox-creator-docs/physics/constraints/rigid]] - Rigid.
- [[external/roblox-creator-docs/physics/constraints/rod]] - Rod.
- [[external/roblox-creator-docs/physics/constraints/rope]] - Rope.
- [[external/roblox-creator-docs/physics/constraints/spring]] - Spring.
- [[external/roblox-creator-docs/physics/constraints/torque]] - Torque.
- ...and 4 more local docs.
