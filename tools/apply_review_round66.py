"""第66轮：axis 补具名实例并升级（北京中轴线 wp+官方双源）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INST = {
    "axis": dict(
        inst="名称：北京中轴线（Beijing Central Axis）；地点：中国北京老城；规划者：历代规划营建（无单一设计者）；年份：始建于元、明清成形（13–16 世纪）。纵贯老城南北、采用对称布局并蕴含比例模数与景观序列。此处仅列名称、地点、设计者与年份信息，不复制图像。",
        keep=False, caveat=""),
}


def main():
    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] in INST and "wp-chinese-architecture" in e["sources"] and "bjaxis-official" in e["sources"]:
                f = INST[e["id"]]
                e["sections"]["实例"] = f["inst"]
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
            print("axis upgraded in", p.name)


if __name__ == "__main__":
    main()
