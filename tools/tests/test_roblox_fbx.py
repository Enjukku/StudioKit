"""Offline tests for tools/rig/roblox_fbx.py: the profiles hold Roblox's export guidance (no Blender needed)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "rig"))
import roblox_fbx as rf  # noqa: E402


class ProfileTest(unittest.TestCase):
    def test_roblox_general_rules_in_every_profile(self):
        for kind in rf.PROFILES:
            p = rf.profile(kind)
            self.assertEqual(p["apply_scale_options"], "FBX_SCALE_UNITS", kind)
            self.assertFalse(p["add_leaf_bones"], kind)
            self.assertEqual((p["path_mode"], p["embed_textures"]), ("COPY", True), kind)
            self.assertFalse(p["bake_space_transform"], kind)

    def test_rest_has_no_animation(self):
        self.assertFalse(rf.profile("rest")["bake_anim"])

    def test_clip_exports_one_action_unsimplified(self):
        p = rf.profile("clip")
        self.assertTrue(p["bake_anim"])
        self.assertFalse(p["bake_anim_use_all_actions"])
        self.assertFalse(p["bake_anim_use_nla_strips"])
        self.assertFalse(p["bake_anim_force_startend_keying"])
        self.assertEqual(p["bake_anim_simplify_factor"], 0.0)

    def test_avatar_body_keeps_custom_props(self):
        self.assertTrue(rf.profile("avatar_body")["use_custom_props"])
        self.assertFalse(rf.profile("clip")["use_custom_props"])

    def test_sockets_not_dropped(self):
        for kind in rf.PROFILES:
            self.assertFalse(rf.profile(kind)["use_armature_deform_only"], kind)

    def test_profile_is_a_copy_and_unknown_kind_fails(self):
        rf.profile("rest")["bake_anim"] = True
        self.assertFalse(rf.profile("rest")["bake_anim"])
        with self.assertRaises(KeyError):
            rf.profile("glb")


if __name__ == "__main__":
    unittest.main()
