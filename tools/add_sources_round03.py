"""第3轮：纳入 B1 新核验来源；已存在的 id 只更新 note，不重复添加。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("wp-list-architectural-styles", "List of architectural styles", "https://en.wikipedia.org/wiki/List_of_architectural_styles", "建筑风格分类清单，用于样式主义与学院派风格归属核对"),
    ("wp-outline-of-painting", "Outline of painting", "https://en.wikipedia.org/wiki/Outline_of_painting", "绘画大纲，用于外光写生与样式主义归属核对"),
    ("wp-history-of-architecture", "History of architecture", "https://en.wikipedia.org/wiki/History_of_architecture", "建筑史大纲，已核验页面；用于风格序列比对"),
    ("wp-architectural-theory", "Architectural theory", "https://en.wikipedia.org/wiki/Architectural_theory", "建筑理论大纲，已核验页面；用于维特鲁威三原则核对"),
    ("wp-visual-arts", "Visual arts", "https://en.wikipedia.org/wiki/Visual_arts", "视觉艺术总览，用于建筑理论与外光写生核对"),
]


def main():
    path = ROOT / "data" / "sources.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {s["id"]: s for s in data["sources"]}
    added, updated = [], []
    for sid, title, url, note in NEW:
        if sid in by_id:
            src = by_id[sid]
            src["note"] += f"；第3轮复核：2026-11-22 HTTP 200，用于{note}"
            src.setdefault("link_ok", True)
            updated.append(sid)
        else:
            data["sources"].append({
                "id": sid, "title": title, "author": "Wikipedia contributors",
                "type": "权威百科", "year": None, "url": url, "url2": None,
                "verified": True, "link_ok": True,
                "note": f"标题与机构已核对，访问于 2026-11-22；{note}；百科条目无固定出版年",
            })
            added.append(sid)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"sources added={added} updated={updated} total={len(data['sources'])}")


if __name__ == "__main__":
    main()
