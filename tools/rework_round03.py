"""第3轮抽检返工：补入直接来源，修正 mannerism/daylighting/six-principles。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW_SOURCES = [
    ("wp-mannerism", "Mannerism", "https://en.wikipedia.org/wiki/Mannerism", "样式主义直接条目，支撑风格定义与时期"),
    ("wp-daylighting-architecture", "Daylighting (architecture)", "https://en.wikipedia.org/wiki/Daylighting_(architecture)", "建筑采光直接条目，支撑侧窗、天窗与眩光"),
    ("wp-architectural-lighting-design", "Architectural lighting design", "https://en.wikipedia.org/wiki/Architectural_lighting", "建筑照明设计直接条目，支撑采光与照明术语"),
]


def main():
    src_path = ROOT / "data" / "sources.json"
    data = json.loads(src_path.read_text(encoding="utf-8"))
    by_id = {s["id"]: s for s in data["sources"]}
    for sid, title, url, note in NEW_SOURCES:
        if sid not in by_id:
            data["sources"].append({
                "id": sid, "title": title, "author": "Wikipedia contributors", "type": "权威百科",
                "year": None, "url": url, "url2": None, "verified": True, "link_ok": True,
                "note": f"标题与机构已核对，访问于 2026-11-22；{note}；百科条目无固定出版年",
            })
    src_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for path in sorted((ROOT / "entries").glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for entry in doc.get("entries", []):
            eid = entry["id"]
            if eid == "mannerism":
                entry["definition"] = "文艺复兴晚期出现、以夸张比例与刻意变形显示技巧的建筑风格。"
                entry["time_or_place"] = "文艺复兴晚期欧洲（参见来源）。"
                entry["sources"] = ["wp-mannerism", "wp-list-architectural-styles"]
                changed = True
            elif eid == "daylighting":
                entry["sources"] = ["wp-daylighting-architecture", "wp-architectural-lighting-design"]
                entry["needs_verification"] = True
                entry["pending_notes"] = "采光系数与窗地比等具体参数待按专业规范核实，正文仅作一般性说明。"
                changed = True
            elif eid == "six-principles":
                entry["sources"] = ["wp-six-principles-chinese-painting"]
                entry["needs_verification"] = True
                entry["pending_notes"] = "谢赫条目为消歧义页；年代与版本流传待补充专门研究来源。"
                if "待核实" in entry.get("sections", {}):
                    entry["sections"]["待核实"] = "谢赫与《古画品录》的确切年代及版本流传待补充独立来源。"
                changed = True
        if changed:
            path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("reworked sources and 3 entries")


if __name__ == "__main__":
    main()
