"""第79轮：hatching 实例具体化为 Dürer《Melencolia I》版画（单源具名，保留待核实）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "hatching":
                e["sections"]["实例"] = "名称：《忧郁 I》（Melencolia I，铜版画）；地点：原版 1514 年于纽伦堡；作者：阿尔布雷希特·丢勒（Albrecht Dürer）；年份：1514 年。以密集交叉排线塑造明暗与体积，是排线法的版画典范。此处仅列名称、地点、作者与年份信息，不复制图像。"
                e["needs_verification"] = True
                e["sections"]["待核实"] = "以排列线表现明暗的技法概念由 Wikipedia 与 Art in Context 双源直证；具体实例《忧郁 I》（丢勒，1514）目前仅 Wikipedia 单一平台直证，待补第二独立平台。"
                e["pending_notes"] = "实例《忧郁 I》仅单平台直证，待补第二独立来源；技法概念已双源。"
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round79 applied")


if __name__ == "__main__":
    main()
