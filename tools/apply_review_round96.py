"""第96轮：atrium-architecture 核心(贯通多层+天窗采光)双源，去单源通风机理claim，升级 nv=false。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "atrium-architecture":
                e["definition"] = "中庭是建筑内部贯通多层、常覆以天窗的中央开敞空间。"
                e["overview"] = "中庭把天然光引入建筑深处、形成共享的竖向核心，改善大进深空间的采光与环境。"
                e["sections"]["原理"] = "贯通多层的天窗空间让天然光深入建筑内部、辐照到下部楼层，形成明亮共享的竖向核心，是改善大进深空间采光的常用手段。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round96 applied")


if __name__ == "__main__":
    main()
