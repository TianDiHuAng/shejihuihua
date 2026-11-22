"""第8轮：升级 6 个从业者问题相关 L1 条目到 L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
    "daylight-factor": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='80' width='600' height='240' fill='none' stroke='var(--line)'/><rect x='120' y='120' width='140' height='160' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='270' y1='160' x2='560' y2='260' stroke='var(--accent)' stroke-width='2'/><rect x='520' y='240' width='100' height='20' fill='none' stroke='var(--muted)'/><text x='130' y='105' fill='var(--ink)'>窗洞口</text><text x='500' y='230' fill='var(--ink)'>工作面</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "mixed-mode-ventilation": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='90' y='90' width='580' height='240' fill='none' stroke='var(--line)'/><line x1='130' y1='210' x2='360' y2='210' stroke='var(--muted)' stroke-width='3'/><rect x='380' y='160' width='120' height='100' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='510' y1='210' x2='640' y2='210' stroke='var(--accent)' stroke-width='2'/><text x='140' y='180' fill='var(--ink)'>可开启窗（自然）</text><text x='390' y='140' fill='var(--ink)'>风机（机械）</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "demand-controlled-ventilation": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='100' y='100' width='560' height='220' fill='none' stroke='var(--line)'/><circle cx='230' cy='210' r='40' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='280' y1='210' x2='460' y2='210' stroke='var(--accent)' stroke-width='2'/><rect x='470' y='170' width='120' height='80' fill='none' stroke='var(--muted)'/><text x='190' y='280' fill='var(--ink)'>传感器</text><text x='480' y='150' fill='var(--ink)'>风量调节</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "material-durability": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='90' width='600' height='240' fill='none' stroke='var(--line)'/><rect x='130' y='140' width='140' height='190' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='330' y='140' width='140' height='190' fill='none' stroke='var(--muted)'/><rect x='530' y='140' width='140' height='190' fill='none' stroke='var(--accent)'/><text x='140' y='120' fill='var(--ink)'>耐候</text><text x='340' y='120' fill='var(--ink)'>耐磨</text><text x='540' y='120' fill='var(--ink)'>可维护</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "transparent-material": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='100' y='90' width='560' height='240' fill='none' stroke='var(--line)'/><rect x='160' y='130' width='180' height='160' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='420' y='130' width='180' height='160' fill='none' stroke='var(--accent)' stroke-dasharray='8 5'/><text x='180' y='110' fill='var(--ink)'>透明：视线穿透</text><text x='430' y='110' fill='var(--ink)'>半透明：透光不透视</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "universal-design": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='80' width='600' height='260' fill='none' stroke='var(--line)'/><line x1='180' y1='300' x2='580' y2='300' stroke='var(--muted)' stroke-width='3'/><circle cx='250' cy='220' r='30' fill='var(--accent-soft)' stroke='var(--accent)'/><circle cx='500' cy='220' r='30' fill='none' stroke='var(--accent)'/><text x='200' y='160' fill='var(--ink)'>不同使用者</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

UPGRADES = {
    "daylight-factor": {
        "sources": ["wp-daylighting-architecture", "wp-architectural-lighting-design"],
        "sections": {
            "原理": "采光系数把室内某点的天然光照度与同期室外无遮挡水平照度相比，用于剥离天气波动比较采光潜力。",
            "典型手法与适用条件": "用于方案阶段评估窗洞口与进深的关系；数值结果受遮挡、反射与朝向影响，不能替代现场实测。",
            "实例": "名称：办公空间侧窗采光评估；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "把系数当作照度绝对值会误判；眩光与过热需另行检查。窗地比等具体尺寸按当地规范校核。" + REG,
            "一图": "见下方示意：窗洞口与工作面的照度关系。",
            "待核实": "实例的具体采光系数与设计者待核实。",
        },
        "pending": True, "note": "实例的具体参数与设计者待补充独立来源。",
    },
    "mixed-mode-ventilation": {
        "sources": ["wp-ventilation-architecture", "wp-natural-ventilation"],
        "sections": {
            "原理": "混合通风在可开启窗与自然驱动可用时优先自然通风，在条件不足时由机械系统补充。",
            "典型手法与适用条件": "设置可开启窗、风机与控制策略；适用于气候温和但室外空气质量或风况不稳定的建筑。",
            "实例": "名称：办公建筑混合通风；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "自然与机械模式切换逻辑不清会造成能耗增加；开口尺寸与安全按当地规范校核。" + REG,
            "一图": "见下方示意：自然路径与机械路径并行。",
            "待核实": "实例的控制策略与能耗数据待核实。",
        },
        "pending": True, "note": "混合通风实例的控制策略与能耗数据待补充独立来源。",
    },
    "demand-controlled-ventilation": {
        "sources": ["wp-ventilation-architecture"],
        "sections": {
            "原理": "按需控制通风用传感器监测二氧化碳或人员存在，按实际需求调节新风量而非恒定运行。",
            "典型手法与适用条件": "在人员密度波动大的空间设置传感器与变频风机；需与室内空气质量目标联动。",
            "实例": "名称：会议室按需通风；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "传感器布置不当会误判 occupancy；通风量下限须按当地规范执行。" + REG,
            "一图": "见下方示意：传感器—控制器—风量的反馈链。",
            "待核实": "该条目仅一份直接来源，控制阈值与实例数据待补第二独立来源。",
        },
        "pending": True, "note": "按需控制通风缺第二独立来源；实例阈值与数据待补。",
    },
    "material-durability": {
        "sources": ["wp-building-material", "wp-vernacular-architecture"],
        "sections": {
            "原理": "耐久性来自材料抵抗磨损、腐蚀、冻融与紫外老化的能力，决定维护周期与全生命周期成本。",
            "典型手法与适用条件": "按暴露环境与使用强度选材，兼顾可替换性；潮湿或盐雾环境需专门防护。",
            "实例": "名称：公共建筑外立面材料；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "只看初始价格会忽略更换成本；材料尺寸与防火等级按当地规范校核。" + REG,
            "一图": "见下方示意：耐候、耐磨与可维护三种维度。",
            "待核实": "实例材料的实测寿命数据待核实。",
        },
        "pending": True, "note": "材料实例的实测寿命与维护数据待补充独立来源。",
    },
    "transparent-material": {
        "sources": ["wp-building-material", "wp-architectural-lighting-design"],
        "sections": {
            "原理": "透明材料让视线穿透并传递光，半透明材料传递光但模糊影像；两者改变空间边界的视觉重量。",
            "典型手法与适用条件": "玻璃、聚碳酸酯与薄膜用于采光顶面、隔断与幕墙；需结合遮阳与热工性能。",
            "实例": "名称：建筑玻璃隔断；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "透明并不等于节能；眩光与结露需专门处理，构造尺寸按当地规范校核。" + REG,
            "一图": "见下方示意：透明与半透明的视觉差异。",
            "待核实": "实例材料的具体性能参数待核实。",
        },
        "pending": True, "note": "透明与半透明材料实例的性能参数待补充独立来源。",
    },
    "universal-design": {
        "sources": ["wp-architecture"],
        "sections": {
            "原理": "通用设计力求让绝大多数人在不使用专门适配的情况下也能使用同一空间与产品。",
            "典型手法与适用条件": "宽通道、连续扶手、可调节台面与清晰标识；适用于公共建筑与可变使用场景。",
            "实例": "名称：公共建筑通用设计实践；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "通用设计与无障碍规范目标相近但范围更广；具体尺寸须按当地规范执行。" + REG,
            "一图": "见下方示意：不同使用者共享同一路径。",
            "待核实": "该条目仅一份直接来源；通用设计与无障碍的边界定义待补第二独立来源。",
        },
        "pending": True, "note": "通用设计缺第二独立来源；实例的设计者与年份待补。",
    },
}


COVERAGE = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
META = {r["id"]: r for r in COVERAGE["entries"]}
ORDER = COVERAGE["entries"]


def related_for(eid):
    pos = next((i for i, r in enumerate(ORDER) if r["id"] == eid), -1)
    for nxt in ORDER[pos + 1:]:
        if nxt["theme"] == META[eid]["theme"]:
            return [nxt["id"]]
    return []


def main():
    rows = []
    for eid, spec in UPGRADES.items():
        meta = META[eid]
        rows.append({
            "id": eid, "title": meta["title"], "level": "L2", "tier": meta["tier"],
            "theme": meta["theme"], "period": meta["period"], "region": meta["region"],
            "definition": spec["sections"]["原理"].split("。")[0] + "。",
            "time_or_place": f"{meta['period']}、{meta['region']}（参见来源）。",
            "overview": spec["sections"]["典型手法与适用条件"],
            "related": related_for(eid), "sections": spec["sections"],
            "svg": [SVG[eid]], "sources": spec["sources"],
            "needs_verification": spec["pending"], "pending_notes": spec["note"],
        })
    out = ROOT / "entries" / "batch-08.json"
    out.write_text(json.dumps({"unit_id": "batch-08", "title": "第8轮从业者问题对应 L2", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"batch-08 written={len(rows)}")


if __name__ == "__main__":
    main()
