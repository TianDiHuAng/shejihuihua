"""第7轮：写入 B1 新增 7 个 scope 条目的 L1 骨架。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COVERAGE = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
META = {r["id"]: r for r in COVERAGE["entries"]}
ORDER = COVERAGE["entries"]

DATA = """
gestalt-organization-laws|视觉系统按邻近、相似、闭合、对称与连续等原则把局部组织为整体的规律。|20世纪、全球（参见来源）。|格式塔组织律为构图法则与图底关系提供了上位解释。|wp-visual-perception,wp-gestalt-psychology|0|
color-psychology|研究色彩对人的感受、情绪与行为影响的领域。|20世纪、全球（参见来源）。|色彩心理效应把色相与空间情绪联系起来，是室内配色的重要依据。|wp-interior-design,wp-color-psychology|0|
environmental-psychology|研究自然与建成环境如何影响人的体验与行为的领域。|20世纪、全球（参见来源）。|该领域把空间感知、场所情感与使用行为纳入统一框架。|wp-landscape-architecture,wp-environmental-psychology|0|
hardscape-softscape|景观中铺装、构筑物等硬质要素与植物、水体等软质要素的分类。|跨时期、全球（参见来源）。|两类要素的比例决定空间的围合感、维护需求与生态表现。|wp-landscape-architecture,wp-landscape-design|0|
wayfinding|人在物理空间中借助标识、地图与视觉线索定向和导航的过程与设计。|跨时期、全球（参见来源）。|导视与寻路把动线组织、空间认知和图形信息结合起来。|wp-graphic-design,wp-wayfinding|0|
lighting-design|组织天然光与人工光以支持视觉、健康和空间氛围的设计。|跨时期、全球（参见来源）。|照明设计把采光、任务照明和情绪氛围作为整体考虑。|wp-interior-design,wp-lighting-design|0|
place-attachment|人与特定场所之间形成的情感纽带。|当代、全球（参见来源）。|场所依恋解释人为何对某些空间产生归属与记忆，与场所精神互为补充。|wp-environmental-psychology,wp-place-attachment|0|
"""


def related_for(eid):
    pos = next(i for i, r in enumerate(ORDER) if r["id"] == eid)
    for nxt in ORDER[pos + 1:]:
        if nxt["theme"] == META[eid]["theme"]:
            return [nxt["id"]]
    return []


def main():
    rows = []
    for line in DATA.strip().splitlines():
        parts = line.split("|")
        if len(parts) != 7:
            raise ValueError(line[:60])
        eid, definition, time_place, overview, srcs, flag, note = parts
        meta = META[eid]
        rows.append({
            "id": eid, "title": meta["title"], "level": "L1", "tier": meta["tier"],
            "theme": meta["theme"], "period": meta["period"], "region": meta["region"],
            "definition": definition, "time_or_place": time_place, "overview": overview,
            "related": related_for(eid), "sources": [s for s in srcs.split(",") if s],
            "needs_verification": flag == "1", "pending_notes": note,
        })
    out = ROOT / "entries" / "batch-07.json"
    out.write_text(json.dumps({"unit_id": "batch-07", "title": "第7轮 B1 新增条目", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"batch-07 entries={len(rows)}")


if __name__ == "__main__":
    main()
