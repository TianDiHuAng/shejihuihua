"""第5轮：应用复核升级与抽检返工（5 条可升级 + 1 条来源返工）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW_SOURCES = [
    ("wp-guggenheim-abu-dhabi", "Guggenheim Abu Dhabi", "https://en.wikipedia.org/wiki/Guggenheim_Abu_Dhabi", "预计 2026-12-11 开馆，Frank Gehry 设计"),
    ("wp-unite-d-habitation", "Unité d'habitation", "https://en.wikipedia.org/wiki/Unit%C3%A9_d%27habitation", "马赛公寓，Le Corbusier，1947–1952，粗野主义灵感来源"),
    ("wp-hui-style-architecture", "Hui Style architecture", "https://en.wikipedia.org/wiki/Hui_Style_architecture", "徽派建筑专条，支撑粉墙黛瓦、马头墙与院落天井"),
    ("wp-hongcun", "Hongcun", "https://en.wikipedia.org/wiki/Hongcun", "宏村，1131 年由 Wang Wen 建立，位于历史徽州地区"),
    ("wp-xidi", "Xidi", "https://en.wikipedia.org/wiki/Xidi", "西递，宋代皇祐年间始建，徽州村落佐证"),
    ("wp-hagia-sophia", "Hagia Sophia", "https://en.wikipedia.org/wiki/Hagia_Sophia", "圣索菲亚大教堂，532–537 年，Isidore of Miletus 与 Anthemius of Tralles 设计"),
    ("wp-parthenon", "Parthenon", "https://en.wikipedia.org/wiki/Parthenon", "帕特农神庙，前 447–前 432 年，Iktinos 与 Callicrates"),
]

PENDING_NONE = "暂无已知待核实项。"


def main():
    src_path = ROOT / "data" / "sources.json"
    data = json.loads(src_path.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, note in NEW_SOURCES:
        if sid not in by_id:
            data["sources"].append({
                "id": sid, "title": title, "author": "Wikipedia contributors", "type": "权威百科",
                "year": None, "url": url, "url2": None, "verified": True, "link_ok": True,
                "note": f"标题与机构已核对，HTTP 200，访问于 2026-11-22；{note}；百科条目无固定出版年",
            })
    src_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    changes = {
        "huizhou-style": {
            "definition": "徽派建筑是流行于历史徽州地区、以粉墙黛瓦、马头墙和院落天井为特征的建筑传统。",
            "overview": "白色墙面与深色屋面形成鲜明对比，高起的马头墙既防火又成为聚落天际线的标志。",
            "instance": "名称：宏村；地点：中国安徽（历史徽州地区）；设计者：Wang Wen（建立者）；年份：1131 年。西递（宋代皇祐年间始建）可作佐证。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "sources": ["wp-hui-style-architecture", "wp-hongcun", "wp-xidi"],
            "pending": False,
        },
        "deconstructivism": {
            "instance": "名称：Guggenheim Abu Dhabi；地点：阿布扎比；设计者：Frank Gehry；年份：来源页面称截至 2026-07 预计 2026-12-11 开馆，仍为在建状态。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "extra_sources": ["wp-guggenheim-abu-dhabi"], "pending": False,
        },
        "brutalism": {
            "instance": "名称：马赛公寓（Unité d'habitation）；地点：法国马赛；设计者：Le Corbusier；年份：1947–1952。来源页面称其常被视为粗野主义风格的最初灵感。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "extra_sources": ["wp-unite-d-habitation"], "pending": False,
        },
        "byzantine": {
            "instance": "名称：圣索菲亚大教堂；地点：伊斯坦布尔；设计者：Isidore of Miletus 与 Anthemius of Tralles；年份：532–537 年。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "extra_sources": ["wp-hagia-sophia"], "pending": False,
        },
        "ancient-greek": {
            "instance": "名称：帕特农神庙；地点：雅典；设计者：Iktinos 与 Callicrates（来源用“似乎”表述），Phidias 总体监督；年份：前 447 年开工、前 432 年完工。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "extra_sources": ["wp-parthenon"], "pending": False,
        },
        "leaked-scenery": {
            "pending": True,
            "pending_notes": "所引来源以机制描述支持漏景，未出现“漏景/漏窗”字面术语；实例的设计者与年份待核实。",
        },
    }

    applied = []
    for path in (ROOT / "entries").glob("*.json"):
        doc = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for entry in doc.get("entries", []):
            spec = changes.get(entry["id"])
            if not spec:
                continue
            sec = entry.setdefault("sections", {})
            if "definition" in spec:
                entry["definition"] = spec["definition"]
                entry["overview"] = spec["overview"]
            if "instance" in spec:
                sec["实例"] = spec["instance"]
            if "sources" in spec:
                entry["sources"] = spec["sources"]
            for ref in spec.get("extra_sources", []):
                if ref not in entry["sources"]:
                    entry["sources"].append(ref)
            entry["needs_verification"] = spec["pending"]
            if "pending_notes" in spec:
                entry["pending_notes"] = spec["pending_notes"]
            elif not spec["pending"]:
                entry["pending_notes"] = ""
                sec["待核实"] = PENDING_NONE
            applied.append(entry["id"])
            changed = True
        if changed:
            path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"sources added={len(NEW_SOURCES)} entries applied={len(applied)}: {applied}")


if __name__ == "__main__":
    main()
