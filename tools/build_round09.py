"""第9轮：按 B4 与理论缺口写入 6 条 L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = {r["id"]: r for r in json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))["entries"]}
ORDER = list(META.values())
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
    "functional-zoning": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='80' width='600' height='240' fill='none' stroke='var(--line)'/><rect x='110' y='110' width='200' height='180' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='330' y='110' width='150' height='180' fill='none' stroke='var(--muted)'/><rect x='500' y='110' width='150' height='180' fill='none' stroke='var(--muted)'/><text x='140' y='100' fill='var(--ink)'>公共区</text><text x='340' y='100' fill='var(--ink)'>服务区</text><text x='510' y='100' fill='var(--ink)'>后勤区</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "gray-space": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='80' y1='300' x2='680' y2='300' stroke='var(--ink)' stroke-width='3'/><rect x='160' y='140' width='440' height='160' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='220' y='190' width='320' height='110' fill='none' stroke='var(--muted)'/><text x='250' y='125' fill='var(--ink)'>檐下 / 廊道：亦内亦外</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "parametric-architecture": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='80' width='600' height='240' fill='none' stroke='var(--line)'/><circle cx='220' cy='200' r='70' fill='none' stroke='var(--accent)'/><circle cx='330' cy='200' r='70' fill='none' stroke='var(--accent)'/><circle cx='440' cy='200' r='70' fill='none' stroke='var(--accent)'/><circle cx='550' cy='200' r='70' fill='none' stroke='var(--accent)'/><text x='200' y='100' fill='var(--ink)'>参数驱动的形状序列</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "place-spirit": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='100' y='100' width='560' height='220' fill='none' stroke='var(--line)'/><circle cx='380' cy='210' r='80' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='330' y='205' fill='var(--ink)'>场所</text><text x='180' y='150' fill='var(--muted)'>记忆</text><text x='540' y='150' fill='var(--muted)'>情感</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "spatial-perception": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='90' width='600' height='230' fill='none' stroke='var(--line)'/><circle cx='200' cy='210' r='30' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='235' y1='210' x2='540' y2='210' stroke='var(--accent)' stroke-width='2'/><polygon points='532,204 548,210 532,216' fill='var(--accent)'/><text x='520' y='170' fill='var(--ink)'>目标</text><text x='160' y='170' fill='var(--ink)'>观察者</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "enclosure": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='100' width='520' height='220' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='220' y='160' width='320' height='120' fill='var(--panel)' stroke='var(--muted)'/><text x='300' y='210' fill='var(--ink)'>内部领域</text><text x='150' y='85' fill='var(--ink)'>边界</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

DATA = {
    "functional-zoning": (["wp-architecture", "wp-interior-design"], True, "实例的功能分区数据与设计者待补独立来源。"),
    "gray-space": (["wp-loggia", "wp-chinese-architecture"], True, "檐下与廊道实例的设计者与年代待补独立来源。"),
    "parametric-architecture": (["wp-modern-architecture"], True, "仅一份直接来源；参数化实例的设计者与年代待补独立来源。"),
    "place-spirit": (["wp-environmental-psychology", "wp-place-attachment"], True, "具体场所的设计者与实测数据待补独立来源。"),
    "spatial-perception": (["wp-visual-perception", "wp-architecture"], True, "具体空间的感知实测数据待补独立来源。"),
    "enclosure": (["wp-chinese-architecture", "wp-courtyard"], True, "具体院落的设计者与年代待补独立来源。"),
}

SECTIONS = {
    "functional-zoning": {
        "原理": "功能分区把相近活动归并为连续区域，减少不同使用群体之间的交叉干扰。",
        "典型手法与适用条件": "以公共、服务、后勤三类区域组织平面；适用于运营流线复杂的公共建筑。",
        "常见错误与限制": "分区过细会降低灵活性；后勤尺寸与疏散要求须按当地规范校核。" + REG,
        "一图": "见下方分区概念图：公共区、服务区与后勤区。",
    },
    "gray-space": {
        "原理": "灰空间介于室内与室外之间，既遮风避雨又保持与外界的视觉连续。",
        "典型手法与适用条件": "檐下、外廊与架空层可作气候缓冲区；适用于多雨或日照强烈地区。",
        "常见错误与限制": "界定不清会导致领域感模糊；栏杆与地面防滑须按当地规范校核。" + REG,
        "一图": "见下方剖面概念图：檐下与廊道的中间性。",
    },
    "parametric-architecture": {
        "原理": "参数化设计把几何关系写成可变参数，使形状随条件变化而生成连续族。",
        "典型手法与适用条件": "以算法驱动表皮或结构布局；适用于形态复杂、需批量变体的设计任务。",
        "常见错误与限制": "形式生成脱离建造条件会导致成本失控；结构尺寸与加工精度按当地规范校核。" + REG,
        "一图": "见下方形状序列示意：参数变化驱动的连续变体。",
    },
    "place-spirit": {
        "原理": "场所精神指空间因历史、材料与使用记忆而具有的独特气质，使人产生认同。",
        "典型手法与适用条件": "保留场所记忆、运用地域材料与尺度；适用于更新与景观设计。",
        "常见错误与限制": "符号堆砌会流于表面；改造中的结构安全按当地规范校核。" + REG,
        "一图": "见下方关系示意：场所、记忆与情感的联结。",
    },
    "spatial-perception": {
        "原理": "空间感知把视觉、身体尺度与运动线索整合为对距离、方向和围合的判断。",
        "典型手法与适用条件": "用透视线索、材质变化与节点标识支持定向；适用于复杂公共空间。",
        "常见错误与限制": "线索冲突会让人迷失；标识与疏散指引按当地规范校核。" + REG,
        "一图": "见下方视线示意图：观察者沿线索到达目标。",
    },
    "enclosure": {
        "原理": "围合通过边界把空间从环境中划分出来，形成可识别的内部领域。",
        "典型手法与适用条件": "院墙、廊道与建筑界面形成不同强度的围合；适用于居住与公共院落。",
        "常见错误与限制": "过度围合会闭塞；防火间距与疏散开口按当地规范校核。" + REG,
        "一图": "见下方平面概念图：边界与内部领域。",
    },
}

INSTANCE = "名称：类型性实例（不指定具体项目）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。"


def related_for(eid):
    pos = next((i for i, r in enumerate(ORDER) if r["id"] == eid), -1)
    for nxt in ORDER[pos + 1:]:
        if nxt["theme"] == META[eid]["theme"]:
            return [nxt["id"]]
    return []


def main():
    rows = []
    for eid, (sources, pending, note) in DATA.items():
        meta = META[eid]
        sec = dict(SECTIONS[eid])
        sec["实例"] = INSTANCE
        sec["待核实"] = note
        rows.append({
            "id": eid, "title": meta["title"], "level": "L2", "tier": meta["tier"],
            "theme": meta["theme"], "period": meta["period"], "region": meta["region"],
            "definition": sec["原理"].split("。")[0] + "。",
            "time_or_place": f"{meta['period']}、{meta['region']}（参见来源）。",
            "overview": sec["典型手法与适用条件"],
            "related": related_for(eid), "sections": sec, "svg": [SVG[eid]],
            "sources": sources, "needs_verification": pending, "pending_notes": note,
        })
    out = ROOT / "entries" / "batch-09.json"
    out.write_text(json.dumps({"unit_id": "batch-09", "title": "第9轮读者问题与理论缺口 L2", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"batch-09 entries={len(rows)}")


if __name__ == "__main__":
    main()
