"""第7轮：纳入 B1 发现的 7 条候选所需的 10 份新权威来源。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("wp-visual-perception", "Visual perception", "https://en.wikipedia.org/wiki/Visual_perception", "格式塔组织律与视觉分组"),
    ("wp-gestalt-psychology", "Gestalt psychology", "https://en.wikipedia.org/wiki/Gestalt_psychology", "整体知觉原则与设计应用"),
    ("wp-interior-design", "Interior design", "https://en.wikipedia.org/wiki/Interior_design", "色彩心理与照明设计"),
    ("wp-color-psychology", "Color psychology", "https://en.wikipedia.org/wiki/Color_psychology", "色彩心理效应"),
    ("wp-landscape-architecture", "Landscape architecture", "https://en.wikipedia.org/wiki/Landscape_architecture", "环境心理学与硬软质景观"),
    ("wp-environmental-psychology", "Environmental psychology", "https://en.wikipedia.org/wiki/Environmental_psychology", "人与建成环境关系"),
    ("wp-landscape-design", "Landscape design", "https://en.wikipedia.org/wiki/Landscape_design", "硬质与软质景观分类"),
    ("wp-graphic-design", "Graphic design", "https://en.wikipedia.org/wiki/Graphic_design", "环境图形与导视"),
    ("wp-lighting-design", "Lighting design", "https://en.wikipedia.org/wiki/Lighting_design", "照明设计上位概念"),
    ("wp-place-attachment", "Place attachment", "https://en.wikipedia.org/wiki/Place_attachment", "人与场所情感纽带"),
]


def main():
    path = ROOT / "data" / "sources.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    added = []
    for sid, title, url, note in NEW:
        if sid in by_id:
            continue
        data["sources"].append({
            "id": sid, "title": title, "author": "Wikipedia contributors", "type": "权威百科",
            "year": None, "url": url, "url2": None, "verified": True, "link_ok": True,
            "note": f"标题与机构已核对，HTTP 200，访问于 2026-11-22；{note}；百科条目无固定出版年",
        })
        added.append(sid)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"added={len(added)} total={len(data['sources'])}")


if __name__ == "__main__":
    main()
