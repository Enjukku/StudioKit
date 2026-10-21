"""Export FBX for Roblox from Blender with every option set by name.

Kit tool: universal (Studio Kit). Why: Blender's FBX defaults are the opposite of Roblox's guidance
(leaf bones on, bake animation on, NLA strips and All Actions on, simplify 1.0, scale option NONE),
so a call that relies on defaults exports the wrong thing (fact-check-blender.md rule 4, RB23/RB31/RB47/RB48/RB53).

Sources for the values:
  Roblox general export   knowledge/external/roblox-creator-docs/art/modeling/export-requirements.md:25-47
                          (Path Mode Copy + Embed Textures; Apply Scalings = FBX Units Scale; Add Leaf Bones off;
                          Bake Animation off unless the file carries animation)
  Roblox avatar bodies    avatar/character-bodies/export.md:62-72 (Custom Properties on; NLA Strips, All Actions,
                          Force Start/End Keying off; Simplify 0.0)  -- fact-check-roblox.md RR18, RR19
  Blender operator        bpy.ops.export_scene.fbx (io_scene_fbx add-on), names checked in the 5.2.2 source (RB rows)
Axes: Roblox gives no axis setting. The profile keeps the exporter's documented default pair and records it;
verify with a labelled-reference round trip before trusting it (rigging paper RP:386).

Usage inside Blender (MCP or `blender -b ... --python`):
  import sys; sys.path.append("<kit>/tools/rig"); import roblox_fbx
  missing = roblox_fbx.check_exporter()          # [] means every option name exists in this Blender
  roblox_fbx.export("out/rest.fbx", kind="rest")
  roblox_fbx.export("out/T03_upper_envelope.fbx", kind="clip")   # assign the Action + slot and frame range first
"""

from __future__ import annotations

COMMON = {
    "use_selection": True,
    "path_mode": "COPY",
    "embed_textures": True,
    "global_scale": 1.0,
    "apply_unit_scale": True,
    "apply_scale_options": "FBX_SCALE_UNITS",
    "axis_forward": "-Z",
    "axis_up": "Y",
    "bake_space_transform": False,  # experimental for armatures (animation paper AP:686)
    "object_types": {"ARMATURE", "MESH", "EMPTY"},
    "use_mesh_modifiers": True,  # skips Armature modifiers, evaluates at rest (RB24)
    "add_leaf_bones": False,
    "use_armature_deform_only": False,  # True would drop non-deforming sockets (RB26); use an allowlist instead
    "use_custom_props": False,
}

REST = {**COMMON, "bake_anim": False}

CLIP = {
    **COMMON,
    "bake_anim": True,
    "bake_anim_use_all_bones": True,
    "bake_anim_use_nla_strips": False,
    "bake_anim_use_all_actions": False,  # True exports every resolvable Action as an extra clip (RB52)
    "bake_anim_force_startend_keying": False,
    "bake_anim_step": 1.0,  # frames, not fps
    "bake_anim_simplify_factor": 0.0,  # baseline; reduce later only against a tolerance
}

AVATAR_BODY = {**CLIP, "use_custom_props": True}  # avatar-body export page; FACS data rides on custom props

PROFILES = {"rest": REST, "clip": CLIP, "avatar_body": AVATAR_BODY}


def profile(kind: str) -> dict:
    if kind not in PROFILES:
        raise KeyError(f"unknown profile {kind!r}; use one of {sorted(PROFILES)}")
    return dict(PROFILES[kind])


def check_exporter() -> list[str]:
    """Option names in our profiles that the installed exporter does not have (run inside Blender)."""
    import bpy  # noqa: PLC0415

    props = {p.identifier for p in bpy.ops.export_scene.fbx.get_rna_type().properties}
    names = set().union(*PROFILES.values())
    return sorted(names - props)


def export(filepath: str, kind: str = "rest") -> dict:
    """Export the current selection with the named profile. Returns the options used (for the build manifest)."""
    import bpy  # noqa: PLC0415

    missing = check_exporter()
    if missing:
        raise RuntimeError(f"FBX exporter lacks options {missing}; record the Blender version and stop")
    opts = profile(kind)
    bpy.ops.export_scene.fbx(filepath=filepath, **opts)
    fbx_ver = None
    import addon_utils  # noqa: PLC0415

    for mod in addon_utils.modules():
        if mod.__name__ == "io_scene_fbx":
            fbx_ver = ".".join(map(str, mod.bl_info.get("version", ())))
    return {
        "file": filepath,
        "profile": kind,
        "blender": bpy.app.version_string,
        "fbx_addon": fbx_ver,
        "options": {k: sorted(v) if isinstance(v, set) else v for k, v in opts.items()},
    }
