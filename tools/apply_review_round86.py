"""第86轮：rock-garden / time-scenery 专类园/传统造园手法，概念多源、类型性实例(无单一设计者)，升级 nv=false。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
V = {
 "rock-garden": dict(
   defn="岩石园是以置石与砾石为骨架、栽种高山或旱生植物的小型专类园。",
   ov="它靠排水良好的砾质基质模拟岩生环境、展示耐旱耐瘠植物；作为园林类型，通常不归于单一设计者。",
   inst="名称：岩石园（类型性，专类园通常无单一设计者）；地点：不指定具体项目。以粗砾排水层、置石与岩生植物组成。此处仅列说明，不复制图像。"),
 "time-scenery": dict(
   defn="时序造景是借晨昏、晴雨、雪月等天时变化使同一景物呈现不同意境的造景手法。",
   ov="花木季相与气象、光线共同改变景致，观景点随时间更换；此类手法属传统造园经验，多集体经手、无单一设计者。",
   inst="名称：园林时序造景（类型性，传统造园无单一设计者）；地点：中国古典园林。借雾晨月夜、雨雪四季造不同景致。此处仅列说明，不复制图像。"),
}


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] in V:
                f = V[e["id"]]
                e["definition"] = f["defn"]
                e["overview"] = f["ov"]
                e["sections"]["实例"] = f["inst"]
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round86 applied")


if __name__ == "__main__":
    main()
