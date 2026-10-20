"""Build the stage-1 motion blueprint page (vfx-workflow-proposal.md §2) from an effect folder.

  python tools/vfx/blueprint_page.py content/vfx/<effect-id> [out.html]

Reads <effect>/blueprint.json (required) and <effect>/layers.json (optional), fills
tools/vfx/blueprint_page.template.html, writes output/vfx/<effect-id>/blueprint.html by default.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = Path(__file__).with_name("blueprint_page.template.html")


def build(effect_dir: Path, out: Path | None = None) -> Path:
    bp = json.loads((effect_dir / "blueprint.json").read_text(encoding="utf-8"))
    layers_path = effect_dir / "layers.json"
    layers = json.loads(layers_path.read_text(encoding="utf-8")) if layers_path.exists() else []
    title = bp.get("title") or bp["id"].replace("-", " ").title() + " Blueprint"
    bp.setdefault("title", title)
    # "</" inside inline JSON would end the script tag early
    dump = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
    html = (TEMPLATE.read_text(encoding="utf-8")
            .replace("__TITLE__", title)
            .replace("__BLUEPRINT__", dump(bp))
            .replace("__LAYERS__", dump(layers)))
    out = out or ROOT / "output" / "vfx" / bp["id"] / "blueprint.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


if __name__ == "__main__":
    print(build(Path(sys.argv[1]), Path(sys.argv[2]) if len(sys.argv) > 2 else None))
