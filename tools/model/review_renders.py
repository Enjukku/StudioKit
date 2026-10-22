"""Render the one standard review set for a model collection, the same way every time.

Kit tool: universal (Studio Kit). The owner's light-check rule (modeling-design/references/review.md §1, owner
J005-D8, J007-D7): one review render set per hand-off; more images only when a number from model_audit.py fails.
Pure part (camera placement from a bounding box) uses the standard library only and is tested offline. The
Blender layer (`render_set`, `main`) imports `bpy` lazily:
  blender -b model.blend --python tools/model/review_renders.py -- --collection Export \
      --out content/models/<id>/review --resolution 1024x1024 --player-height 5 --game-cam 12,6,70
or from the Blender MCP: `import review_renders; review_renders.render_set("Export", "<out>")`.

Views (names follow Blender's numpad views; the model faces -Y, 1 Blender unit = 1 stud, MR36):
  front (camera at -Y), back (+Y), left (-X), right (+X), top (+Z, image up = +Y): orthographic, framed on the
  bounding box with --margin; three_quarter: perspective from front-right, 45° azimuth, 20° elevation, 40° vertical
  FOV, framed on the bounding sphere; scale: front orthographic with a plain 2 x 1 x --player-height stud block
  1 stud to the model's +X side, standing on the model's lowest point (only its height is meant as a reference;
  default 5 studs is the brief's default, not a Roblox rule); game (only with --game-cam distance,height,fov):
  perspective from -Y, `distance` studs from the box centre horizontally, `height` studs above the model's lowest
  point, looking at the box centre, `fov` = vertical FOV in degrees (Roblox Camera.FieldOfView is vertical).
Look: Workbench, studio light, flat colour or texture, no outline, cavity or shadow, Standard view transform,
flat grey background (sRGB 0.5). These are fixed choices so sets compare across hand-offs; they are not a
judgement of the model's final look (that is the Studio render).
Scene safety: temporary camera, dummy and world live in a temp collection and are removed; render settings,
scene camera, world and every object's hide_render are restored in `finally`. Writes only into --out.
Output: review_<view>.png and review_renders.json (files, bytes, camera per view) in --out.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ORTHO_VIEWS = {  # view: (direction from target to camera, world up for the image)
    "front": ((0.0, -1.0, 0.0), (0.0, 0.0, 1.0)),
    "back": ((0.0, 1.0, 0.0), (0.0, 0.0, 1.0)),
    "left": ((-1.0, 0.0, 0.0), (0.0, 0.0, 1.0)),
    "right": ((1.0, 0.0, 0.0), (0.0, 0.0, 1.0)),
    "top": ((0.0, 0.0, 1.0), (0.0, 1.0, 0.0)),
}
THREE_QUARTER = {"azimuth_deg": 45.0, "elevation_deg": 20.0, "fov_deg": 40.0}
DUMMY_FOOTPRINT = (2.0, 1.0)  # x, y studs of the plain player block; only its height is a reference
DUMMY_GAP = 1.0  # studs between the model's box and the block
GREY_LINEAR = 0.2140  # linear value that displays as sRGB 0.5 under the Standard view transform
RENDERABLE = ("MESH", "CURVE", "SURFACE", "FONT", "META")


# ---------------------------------------------------------------- pure camera placement

def _norm(v):
    n = math.sqrt(sum(x * x for x in v))
    return tuple(x / n for x in v)


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def look_at(eye, target, up) -> list[list[float]]:
    """3x3 camera rotation (rows) whose -Z axis points from eye to target and +Y is as close to `up` as possible."""
    f = _norm(tuple(t - e for t, e in zip(target, eye)))
    r = _norm(_cross(f, up))
    u = _cross(r, f)
    return [[r[i], u[i], -f[i]] for i in range(3)]


def ortho_scale(width: float, height: float, res_x: int, res_y: int, margin: float = 1.1) -> float:
    """Blender ortho_scale (sensor fit AUTO spans the longer image side) that shows width x height with margin."""
    if res_x >= res_y:
        return max(width, height * res_x / res_y) * margin
    return max(height, width * res_y / res_x) * margin


def fit_distance(radius: float, fov_v_deg: float, res_x: int, res_y: int, margin: float = 1.1) -> float:
    """Camera distance that shows a sphere of `radius` inside a vertical FOV (and the matching horizontal one)."""
    half_v = math.radians(fov_v_deg) / 2
    half_h = math.atan(math.tan(half_v) * res_x / res_y)
    return radius * margin / math.sin(min(half_v, half_h))


def dummy_box(bmin, bmax, height: float) -> dict:
    """Plain player block beside the model on its +X side, feet on the model's lowest point."""
    w, d = DUMMY_FOOTPRINT
    cx = bmax[0] + DUMMY_GAP + w / 2
    cy = (bmin[1] + bmax[1]) / 2
    return {"center": (cx, cy, bmin[2] + height / 2), "size": (w, d, height),
            "min": (cx - w / 2, cy - d / 2, bmin[2]), "max": (cx + w / 2, cy + d / 2, bmin[2] + height)}


def _ortho(view, bmin, bmax, res, margin, up_override=None):
    direction, up = ORTHO_VIEWS[view]
    up = up_override or up
    center = tuple((a + b) / 2 for a, b in zip(bmin, bmax))
    size = tuple(b - a for a, b in zip(bmin, bmax))
    radius = max(0.5 * math.sqrt(sum(s * s for s in size)), 0.01)
    eye = tuple(c + d * (2 * radius + 1) for c, d in zip(center, direction))
    rot = look_at(eye, center, up)
    right, cam_up = [row[0] for row in rot], [row[1] for row in rot]
    w = sum(abs(r) * s for r, s in zip(right, size))
    h = sum(abs(u) * s for u, s in zip(cam_up, size))
    return {"type": "ORTHO", "eye": eye, "target": center, "rotation": rot,
            "ortho_scale": max(ortho_scale(w, h, res[0], res[1], margin), 0.01), "clip_end": 4 * radius + 2}


def _persp(eye, target, fov, radius, res):
    dist = math.dist(eye, target)
    return {"type": "PERSP", "eye": eye, "target": target, "rotation": look_at(eye, target, (0.0, 0.0, 1.0)),
            "fov_deg": fov, "clip_end": dist + 4 * radius + 2}


def plan_views(bmin, bmax, res=(1024, 1024), margin: float = 1.1, player_height: float = 5.0,
               game_cam=None) -> dict:
    """Camera for every review view from the model's world bounding box (studs). game_cam = (distance, height, fov)."""
    views = {v: _ortho(v, bmin, bmax, res, margin) for v in ORTHO_VIEWS}
    center = tuple((a + b) / 2 for a, b in zip(bmin, bmax))
    radius = max(0.5 * math.dist(bmin, bmax), 0.01)
    az, el = math.radians(THREE_QUARTER["azimuth_deg"]), math.radians(THREE_QUARTER["elevation_deg"])
    d = (math.cos(el) * math.sin(az), -math.cos(el) * math.cos(az), math.sin(el))
    dist = fit_distance(radius, THREE_QUARTER["fov_deg"], res[0], res[1], margin)
    views["three_quarter"] = _persp(tuple(c + x * dist for c, x in zip(center, d)), center,
                                    THREE_QUARTER["fov_deg"], radius, res)
    dummy = dummy_box(bmin, bmax, player_height)
    umin = tuple(min(a, b) for a, b in zip(bmin, dummy["min"]))
    umax = tuple(max(a, b) for a, b in zip(bmax, dummy["max"]))
    views["scale"] = {**_ortho("front", umin, umax, res, margin), "dummy": dummy}
    if game_cam is not None:
        distance, height, fov = game_cam
        eye = (center[0], center[1] - distance, bmin[2] + height)
        views["game"] = _persp(eye, center, fov, radius, res)
        # third person behind and above: the view players see most of their own character (J018 G3-P8)
        back = (center[0], center[1] + distance, bmin[2] + height)
        views["game_back"] = _persp(back, center, fov, radius, res)
    return views


# ---------------------------------------------------------------- Blender layer (bpy, lazy)

def _model_bbox(objs, dg):
    from mathutils import Vector  # noqa: PLC0415

    pts = []
    for o in objs:
        ev = o.evaluated_get(dg)
        pts += [ev.matrix_world @ Vector(c) for c in ev.bound_box]
    if not pts:
        raise ValueError("no renderable objects in the collection")
    return (tuple(min(p[i] for p in pts) for i in range(3)), tuple(max(p[i] for p in pts) for i in range(3)))


def render_set(collection: str, out_dir: str, resolution=(1024, 1024), player_height: float = 5.0,
               game_cam=None, margin: float = 1.1) -> dict:
    import bpy  # noqa: PLC0415
    from mathutils import Matrix, Vector  # noqa: PLC0415

    scene = bpy.context.scene
    coll = bpy.data.collections.get(collection)
    if coll is None:
        raise KeyError(f"collection {collection!r} not found")
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    model = [o for o in coll.all_objects if o.type in RENDERABLE]
    bpy.context.view_layer.update()
    bmin, bmax = _model_bbox(model, bpy.context.evaluated_depsgraph_get())
    views = plan_views(bmin, bmax, resolution, margin, player_height, game_cam)

    r, sh, vs = scene.render, scene.display.shading, scene.view_settings
    saved = [(r, "engine"), (r, "resolution_x"), (r, "resolution_y"), (r, "resolution_percentage"),
             (r, "filepath"), (r, "film_transparent"), (r.image_settings, "file_format"),
             (r.image_settings, "color_mode"), (scene, "camera"), (scene, "world"), (vs, "view_transform"),
             (vs, "look"), (vs, "exposure"), (vs, "gamma"), (sh, "light"), (sh, "color_type"),
             (sh, "show_cavity"), (sh, "show_object_outline"), (sh, "show_shadows")]
    saved = [(o, a, getattr(o, a)) for o, a in saved]
    hide = {o.name: o.hide_render for o in scene.objects}
    keep = {o.name for o in model}
    tmp = bpy.data.collections.new("_review_tmp")
    cam_data = bpy.data.cameras.new("_review_cam")
    cam = bpy.data.objects.new("_review_cam", cam_data)
    d = views["scale"]["dummy"]
    hx, hy = d["size"][0] / 2, d["size"][1] / 2
    dmesh = bpy.data.meshes.new("_review_dummy")
    dmesh.from_pydata([(x * hx, y * hy, z * d["size"][2]) for z in (-0.5, 0.5) for y in (-1, 1) for x in (-1, 1)],
                      [], [(0, 2, 3, 1), (4, 5, 7, 6), (0, 1, 5, 4), (1, 3, 7, 5), (3, 2, 6, 7), (2, 0, 4, 6)])
    dummy = bpy.data.objects.new("_review_dummy", dmesh)
    dummy.location = d["center"]
    world = bpy.data.worlds.new("_review_world")
    world.color = (GREY_LINEAR,) * 3
    files = []
    try:
        scene.collection.children.link(tmp)
        tmp.objects.link(cam)
        tmp.objects.link(dummy)
        for o in scene.objects:
            o.hide_render = o.name not in keep
        cam.hide_render = False
        r.engine = "BLENDER_WORKBENCH"
        r.resolution_x, r.resolution_y = resolution
        r.resolution_percentage = 100
        r.film_transparent = False
        r.image_settings.file_format, r.image_settings.color_mode = "PNG", "RGB"
        vs.view_transform, vs.look, vs.exposure, vs.gamma = "Standard", "None", 0.0, 1.0
        sh.light, sh.color_type = "STUDIO", "TEXTURE"
        sh.show_cavity = sh.show_object_outline = sh.show_shadows = False
        scene.world, scene.camera = world, cam
        for name, v in views.items():
            dummy.hide_render = name != "scale"
            rot = Matrix(v["rotation"])
            cam.matrix_world = Matrix.Translation(Vector(v["eye"])) @ rot.to_4x4()
            cam_data.clip_start, cam_data.clip_end = 0.01, v["clip_end"]
            if v["type"] == "ORTHO":
                cam_data.type, cam_data.ortho_scale, cam_data.sensor_fit = "ORTHO", v["ortho_scale"], "AUTO"
            else:
                cam_data.type, cam_data.sensor_fit = "PERSP", "VERTICAL"
                cam_data.angle_y = math.radians(v["fov_deg"])
            path = out / f"review_{name}.png"
            r.filepath = str(path)
            bpy.ops.render.render(write_still=True)
            files.append({"view": name, "file": path.name, "bytes": path.stat().st_size,
                          "width": resolution[0], "height": resolution[1]})
    finally:
        for o, a, val in saved:
            setattr(o, a, val)
        for o in scene.objects:
            if o.name in hide:
                o.hide_render = hide[o.name]
        bpy.data.objects.remove(cam)
        bpy.data.objects.remove(dummy)
        bpy.data.cameras.remove(cam_data)
        bpy.data.meshes.remove(dmesh)
        bpy.data.worlds.remove(world)
        bpy.data.collections.remove(tmp)
    report = {"tool": "tools/model/review_renders.py", "blender": bpy.app.version_string, "collection": collection,
              "bbox_min": bmin, "bbox_max": bmax, "resolution": list(resolution), "player_height": player_height,
              "game_cam": game_cam, "files": files,
              "views": {k: {kk: vv for kk, vv in v.items() if kk != "rotation"} for k, v in views.items()}}
    (out / "review_renders.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


MAGENTA = (1.0, 0.0, 1.0)  # black-fill backdrop: displays as #FF00FF under Standard, keyed by look_check


def render_frames(camera: str, frames: list[int], out_dir: str, resolution=(1170, 540), blackfill: bool = True,
                  shaded: bool = True, prefix: str = "frame") -> dict:
    """Render chosen frames from a named scene camera (the game camera), shaded and black-fill (J018 G3-P8).

    The shared recipe of animation-craft blender-keying section 7 (animator, rigger, film director, modeler): Workbench,
    Standard view; shaded = STUDIO light and TEXTURE colour; black-fill = FLAT light, SINGLE colour black on a
    magenta world. Every setting, the scene camera, the world and the current frame are restored in `finally`.
    Writes <prefix>_<frame>.png and <prefix>_<frame>.blackfill.png into out_dir."""
    import bpy  # noqa: PLC0415

    scene = bpy.context.scene
    cam = bpy.data.objects.get(camera)
    if cam is None or cam.type != "CAMERA":
        raise KeyError(f"camera {camera!r} not found")
    if not frames:
        raise ValueError("give at least one frame")
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    r, sh, vs = scene.render, scene.display.shading, scene.view_settings
    saved = [(r, "engine"), (r, "resolution_x"), (r, "resolution_y"), (r, "resolution_percentage"), (r, "filepath"),
             (r, "film_transparent"), (r.image_settings, "file_format"), (r.image_settings, "color_mode"),
             (scene, "camera"), (scene, "world"), (scene, "frame_current"), (vs, "view_transform"), (vs, "look"),
             (vs, "exposure"), (vs, "gamma"), (sh, "light"), (sh, "color_type"), (sh, "single_color"),
             (sh, "show_cavity"), (sh, "show_object_outline"), (sh, "show_shadows")]
    saved = [(o, a, tuple(getattr(o, a)) if a == "single_color" else getattr(o, a)) for o, a in saved]
    world = bpy.data.worlds.new("_frames_world")
    world.color = MAGENTA
    files = []
    try:
        r.engine = "BLENDER_WORKBENCH"
        r.resolution_x, r.resolution_y = resolution
        r.resolution_percentage = 100
        r.film_transparent = False
        r.image_settings.file_format, r.image_settings.color_mode = "PNG", "RGB"
        vs.view_transform, vs.look, vs.exposure, vs.gamma = "Standard", "None", 0.0, 1.0
        sh.show_cavity = sh.show_object_outline = sh.show_shadows = False
        scene.camera = cam
        for f in frames:
            scene.frame_set(int(f))
            if shaded:
                sh.light, sh.color_type = "STUDIO", "TEXTURE"
                scene.world = saved[9][2] if saved[9][2] is not None else world
                p = out / f"{prefix}_{int(f):04d}.png"
                r.filepath = str(p)
                bpy.ops.render.render(write_still=True)
                files.append({"frame": int(f), "kind": "shaded", "file": p.name})
            if blackfill:
                sh.light, sh.color_type, sh.single_color = "FLAT", "SINGLE", (0.0, 0.0, 0.0)
                scene.world = world
                p = out / f"{prefix}_{int(f):04d}.blackfill.png"
                r.filepath = str(p)
                bpy.ops.render.render(write_still=True)
                files.append({"frame": int(f), "kind": "blackfill", "file": p.name})
    finally:
        for o, a, val in saved:
            setattr(o, a, val)
        bpy.data.worlds.remove(world)
    report = {"tool": "tools/model/review_renders.py render_frames", "blender": bpy.app.version_string,
              "camera": camera, "resolution": list(resolution), "files": files}
    (out / f"{prefix}_frames.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def main(argv: list[str]) -> int:
    import argparse  # noqa: PLC0415

    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--collection", required=True)
    p.add_argument("--out", required=True, help="folder for review_<view>.png and review_renders.json")
    p.add_argument("--resolution", default="1024x1024", type=lambda s: tuple(int(x) for x in s.lower().split("x")))
    p.add_argument("--player-height", type=float, default=5.0, help="player block height in studs (default 5)")
    p.add_argument("--game-cam", type=lambda s: tuple(float(x) for x in s.split(",")),
                   help="distance,height,fov (studs, studs, vertical degrees) from the game profile")
    p.add_argument("--margin", type=float, default=1.1, help="framing margin (1.1 = 10%% space around the model)")
    a = p.parse_args(argv)
    rep = render_set(a.collection, a.out, a.resolution, a.player_height, a.game_cam, a.margin)
    print(f"RENDERED {len(rep['files'])} views -> {Path(a.out) / 'review_renders.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]))
