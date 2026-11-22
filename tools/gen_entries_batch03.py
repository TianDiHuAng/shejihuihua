"""第3轮：新增 scope 条目的 L1 与核心 L1 收尾。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COVERAGE = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
META = {r["id"]: r for r in COVERAGE["entries"]}
ORDER = COVERAGE["entries"]

# id|定义|时间与位置|概述|来源|待核实(0/1)|说明
DATA = """
mannerism|文艺复兴晚期出现、以夸张比例与刻意变形显示技巧的建筑风格。|文艺复兴至19世纪欧洲（参见来源）。|样式主义在古典规则内制造张力，常被视为从文艺复兴向巴洛克过渡的一环。|wp-list-architectural-styles,wp-history-of-architecture|0|
beaux-arts|19 世纪学院体系下形成的建筑风格，强调古典对称、轴线与纪念性。|文艺复兴至19世纪、全球（参见来源）。|学院派把古典范式系统化为可教授的设计方法，影响了公共建筑与城市轴线。|wp-list-architectural-styles,wp-history-of-architecture|0|
vitruvian-triad|维特鲁威提出的坚固、实用与美观三项建筑原则。|古代欧洲（参见来源）。|三原则把结构、功能与审美并列，成为后世建筑理论反复引用的基本框架。|wp-architectural-theory,wp-visual-arts|0|
plein-air|在户外直接面对自然光进行写生的绘画方法。|文艺复兴至19世纪欧洲（参见来源）。|外光写生让色彩与明暗取自现场观察，成为色彩与光影理论的实践基础。|wp-outline-of-painting,wp-visual-arts|0|
sunken-accessibility|使低处空间对不同行动能力者均可到达并使用的设计。|20世纪、全球（参见来源）。|下沉空间若只设台阶会中断路径，坡道、平台与连续扶手是常见的应对方式。|wp-architecture,wp-exit-sign|0|
chinese-architecture-style|中国传统建筑以木构框架、对称布局与院落组织为主要特征。|古代、中国（参见来源）。|木构体系与院落序列共同塑造了空间等级与礼制秩序，并因地域材料而呈现多样形态。|wp-chinese-architecture,wp-architectural-style|0|
"""


def main():
    rows = []
    for line in DATA.strip().splitlines():
        parts = line.split("|")
        if len(parts) != 7:
            raise ValueError(f"bad row: {line[:60]}")
        eid, definition, time_place, overview, srcs, flag, note = parts
        meta = META[eid]
        pos = next(i for i, r in enumerate(ORDER) if r["id"] == eid)
        related = []
        for nxt in ORDER[pos + 1:]:
            if nxt["theme"] == meta["theme"]:
                related = [nxt["id"]]
                break
        rows.append({
            "id": eid, "title": meta["title"], "level": "L1", "tier": meta["tier"],
            "theme": meta["theme"], "period": meta["period"], "region": meta["region"],
            "definition": definition, "time_or_place": time_place, "overview": overview,
            "related": related, "sources": [s for s in srcs.split(",") if s],
            "needs_verification": flag == "1", "pending_notes": note,
        })
    out = ROOT / "entries" / "batch-03.json"
    out.write_text(json.dumps({"unit_id": "batch-03", "title": "第3轮 L1 条目", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"batch-03 entries={len(rows)}")


if __name__ == "__main__":
    main()
