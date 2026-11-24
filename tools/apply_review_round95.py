"""第95轮：parametric-architecture 补具名实例(盖达尔·阿利耶夫中心)，ArchDaily+TheArtStory 双独立源，升级 nv=false。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "parametric-architecture":
                e["sections"]["实例"] = "名称：盖达尔·阿利耶夫中心（Heydar Aliyev Center）；地点：阿塞拜疆巴库；设计者：扎哈·哈迪德建筑事务所（Zaha Hadid Architects）；年份：2007–2012 年设计建造（ArchDaily 记 2013 年）。以连续曲面体量体现参数化设计。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round95 applied")


if __name__ == "__main__":
    main()
