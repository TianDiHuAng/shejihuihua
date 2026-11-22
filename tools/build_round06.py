"""第6轮：按 B4 读者问题写入 6 条 L2 条目。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = {r["id"]: r for r in json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))["entries"]}
ORDER = list(META.values())
REG = "实际工程须按当地规范和专业设计人员的要求"

SVGS = {
    "color-harmony": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='320' cy='200' r='120' fill='none' stroke='var(--accent)' stroke-width='2'/><circle cx='250' cy='140' r='40' fill='var(--accent-soft)' stroke='var(--muted)'/><circle cx='390' cy='160' r='40' fill='none' stroke='var(--muted)'/><circle cx='320' cy='270' r='40' fill='none' stroke='var(--muted)'/><text x='150' y='70' fill='var(--ink)'>色相关系与明度层级</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "composition-placement": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='60' y='60' width='640' height='280' fill='none' stroke='var(--line)'/><rect x='120' y='100' width='180' height='200' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='340' y='100' width='300' height='90' fill='none' stroke='var(--muted)'/><rect x='340' y='210' width='300' height='90' fill='none' stroke='var(--muted)'/><text x='150' y='85' fill='var(--ink)'>主位</text><text x='450' y='85' fill='var(--ink)'>次位与呼应</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "axis": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='380' y1='40' x2='380' y2='360' stroke='var(--accent)' stroke-width='2'/><rect x='280' y='90' width='200' height='70' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='280' y='220' width='200' height='70' fill='none' stroke='var(--muted)'/><text x='120' y='135' fill='var(--ink)'>前序空间</text><text x='520' y='265' fill='var(--ink)'>核心空间</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "stack-ventilation": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='160' y='80' width='440' height='260' fill='none' stroke='var(--line)'/><rect x='160' y='280' width='50' height='30' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='560' y='90' width='50' height='30' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='230' y1='295' x2='400' y2='295' stroke='var(--accent)' stroke-width='2'/><line x1='400' y1='260' x2='400' y2='110' stroke='var(--accent)' stroke-width='2'/><line x1='400' y1='110' x2='570' y2='105' stroke='var(--accent)' stroke-width='2'/><text x='210' y='340' fill='var(--ink)'>低位冷风</text><text x='555' y='70' fill='var(--ink)'>高位排风</text><text x='290' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "thermal-comfort": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='90' width='600' height='240' fill='none' stroke='var(--line)'/><circle cx='230' cy='210' r='60' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='310' y1='210' x2='560' y2='210' stroke='var(--muted)' stroke-width='2'/><text x='180' y='130' fill='var(--ink)'>人体</text><text x='400' y='180' fill='var(--ink)'>空气温度 · 辐射 · 风速</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "service-route": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='60' y='70' width='640' height='260' fill='none' stroke='var(--line)'/><line x1='120' y1='200' x2='380' y2='200' stroke='var(--accent)' stroke-width='3'/><line x1='380' y1='200' x2='650' y2='200' stroke='var(--muted)' stroke-width='2' stroke-dasharray='8 6'/><circle cx='380' cy='200' r='16' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='130' y='170' fill='var(--ink)'>公众流线</text><text x='500' y='170' fill='var(--ink)'>后勤流线</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

DATA = {
    "color-harmony": {
        "sources": ["wp-color-theory", "wp-color-wheel"],
        "definition": "色彩和谐是依据色相、明度与纯度的关系组织配色，使画面或空间产生秩序感的方法。",
        "time_or_place": "跨时期、全球（参见来源）。",
        "overview": "邻近色带来统一，互补色带来张力；和谐并非固定公式，而取决于对比强度与面积比例。",
        "sections": {
            "原理": "色彩关系由色轮上的位置与明度、纯度共同决定；视觉系统倾向于把有规律的关系读成整体。",
            "典型手法与适用条件": "以单一色相的明度变化建立安静背景，以互补色小面积点缀建立焦点；适用于需要层次但避免杂乱的画面。",
            "实例": "名称：绘画与室内配色实践；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "只套用色轮公式会忽略材质与光照；色差过大可能影响可读性。实际工程须按当地规范和专业设计人员的要求。",
            "一图": "见下方色相关系示意：主色、辅助色与点缀色。",
            "待核实": "具体实例的设计者与年份待核实。",
        },
    },
    "composition-placement": {
        "sources": ["wp-six-principles-chinese-painting", "wp-composition-visual-arts"],
        "definition": "经营位置是中国画六法之一，指画面中各部分的位置安排与主次关系。",
        "time_or_place": "古代中国（参见来源）。",
        "overview": "它关注物象在画面中的占位与呼应，与西方构图理论中的布局概念可相互参照。",
        "sections": {
            "原理": "位置关系决定观看顺序：主位承担视觉重心，次位与留白共同形成节奏。",
            "典型手法与适用条件": "以主体占据关键位置，辅以题跋、印章或景物呼应；适用于立轴、手卷等长幅面经营。",
            "实例": "名称：传统中国画构图；地点：中国；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "把经营位置等同于填满画面会损害气韵；画幅比例与观看距离影响位置判断。" + REG,
            "一图": "见下方布局示意：主位与次位的呼应关系。",
            "待核实": "具体作品的设计者与年份待核实。",
        },
    },
    "axis": {
        "sources": ["wp-symmetry", "wp-chinese-architecture"],
        "definition": "轴线是组织空间序列的假想直线，建筑与院落常沿其对称或递进布置。",
        "time_or_place": "跨时期、全球（参见来源）。",
        "overview": "轴线把分散的空间连成有序序列，使行进方向与重要节点被清晰感知。",
        "sections": {
            "原理": "对称与重复强化轴线方向，节点上的体量变化形成节奏与高潮。",
            "典型手法与适用条件": "以门、殿、庭逐级递进；适用于礼制建筑与需要明确导向的公共空间。",
            "实例": "名称：中国传统院落建筑群；地点：中国；设计者：不适用；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "轴线过长而缺少节点会单调；轴线尺寸与疏散组织须按当地规范校核。" + REG,
            "一图": "见下方轴线示意：前序空间指向核心空间。",
            "待核实": "具体建筑群的设计者与年份待核实。",
        },
    },
    "stack-ventilation": {
        "sources": ["wp-natural-ventilation", "wp-ventilation-architecture"],
        "definition": "热压通风是利用室内外空气温差造成的密度差，使空气从低位进入、高位排出的自然通风方式。",
        "time_or_place": "跨时期、全球（参见来源）。",
        "overview": "它与风压通风互补，在外部风较弱时仍能依靠温差维持空气交换。",
        "sections": {
            "原理": "暖空气密度较低而上升，从高位开口排出；较冷空气由低位开口补入，形成持续流动。",
            "典型手法与适用条件": "设置低位进风口与高位排风口，配合中庭或通风竖井；适用于内外温差明显的季节与气候。",
            "实例": "名称：传统建筑自然通风；地点：待核实；设计者：不适用；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "进排风口高差不足会削弱效果；开口尺寸与安全、隔声需平衡。实际工程须按当地规范和专业设计人员的要求。",
            "一图": "见下方剖面示意：低位进风、热空气上升、高位排风。",
            "待核实": "具体建筑的通风实测数据待核实。",
        },
    },
    "thermal-comfort": {
        "sources": ["wp-thermal-comfort", "wp-passive-solar-building-design"],
        "definition": "热舒适是人对周围热环境感到满意的生理与心理状态。",
        "time_or_place": "20世纪、全球（参见来源）。",
        "overview": "它受空气温度、辐射温度、湿度与风速共同影响，不能用单一温度计读数替代。",
        "sections": {
            "原理": "人体通过辐射、对流与蒸发与环境交换热量，舒适来自产热与散热的平衡。",
            "典型手法与适用条件": "结合遮阳、保温、自然通风与朝向设计；适用于不同气候区的使用环境。",
            "实例": "名称：被动式太阳能建筑；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "只调低空调温度会忽略辐射与湿度；尺寸与设备参数须按当地规范设计。" + REG,
            "一图": "见下方关系示意：人体与温度、辐射、风速的交换。",
            "待核实": "具体建筑的热舒适实测数据待核实。",
        },
    },
    "service-route": {
        "sources": ["wp-wayfinding", "wp-architecture"],
        "definition": "服务动线是供后勤、清洁、配送等非公众活动使用的路径组织。",
        "time_or_place": "跨时期、全球（参见来源）。",
        "overview": "它与公众流线分离，既能提升运营效率，也减少干扰与安全冲突。",
        "sections": {
            "原理": "不同使用群体的路径交叉会产生冲突；分离流线让公众体验与后勤作业各自成立。",
            "典型手法与适用条件": "设置独立后勤入口、货物通道与工作节点；适用于文化、商业与医疗建筑。",
            "实例": "名称：公共建筑后勤流线；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "后勤入口离主要使用区过远会降低效率；货运尺寸与疏散要求须按当地规范校核。" + REG,
            "一图": "见下方流线示意：公众流线与服务流线分离。",
            "待核实": "具体建筑的后勤流线设计者与使用数据待核实。",
        },
    },
}


def related_for(eid):
    pos = next(i for i, r in enumerate(ORDER) if r["id"] == eid)
    for nxt in ORDER[pos + 1:]:
        if nxt["theme"] == META[eid]["theme"]:
            return [nxt["id"]]
    return []


def main():
    rows = []
    for eid, spec in DATA.items():
        meta = META[eid]
        rows.append({
            "id": eid, "title": meta["title"], "level": "L2", "tier": meta["tier"],
            "theme": meta["theme"], "period": meta["period"], "region": meta["region"],
            "definition": spec["definition"], "time_or_place": spec["time_or_place"],
            "overview": spec["overview"], "related": related_for(eid),
            "sections": spec["sections"], "svg": [SVGS[eid]], "sources": spec["sources"],
            "needs_verification": True,
            "pending_notes": "实例的具体名称、地点、设计者与年份待补充独立来源。",
        })
    out = ROOT / "entries" / "batch-06.json"
    out.write_text(json.dumps({"unit_id": "batch-06", "title": "第6轮读者问题对应 L2", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"batch-06 entries={len(rows)}")


if __name__ == "__main__":
    main()
