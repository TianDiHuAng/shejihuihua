"""第36轮：写 12 条（动线组/采光通风/视觉舒适/无障碍），L2、去模板、SVG 加标题。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

D = {
"vehicle-flow": dict(defn="车行动线指机动车、非机动车在场地与建筑中的行驶路径组织。", tp="20世纪、全球（参见来源）。", ov="车行流线关注转弯半径、会车与停车衔接，避免与人流交叉。",
 prin="车辆需要连续、平顺且可识别的路径，转弯半径与出入口位置决定场地内的行驶安全。", method="设独立车行道与出入口，按转弯半径与视距布置，末端衔接停车。",
 inst="名称：园区车行道与出入口（类型性描述）；地点与设计者不适用。看转弯半径与视距如何保障行驶。", cap="见下方示意：车行道与出入口衔接。", limit="急弯与视线遮挡易致事故；须按规范。", srcs=["wp-wayfinding", "wp-urban-design"]),
"people-vehicle-separation": dict(defn="人车分流指以高差、绿化或独立路径把人流与车流分开的组织方式。", tp="20世纪、全球（参见来源）。", ov="它减少冲突点，提升步行安全与车行效率。",
 prin="人流与车流分置不同路径或标高，消除交叉冲突，提升安全与通行效率。", method="以绿化带、高差或独立出入口分离人车，节点处设过街控制。",
 inst="名称：住区人车分流（类型性描述）；地点与设计者不适用。看人与车如何各走其道。", cap="见下方示意：人车分行与过街节点。", limit="分流过度会绕行不便；需平衡。", srcs=["wp-urban-design", "wp-wayfinding"]),
"visitor-route": dict(defn="参观动线指为参观者组织、串联展项与节点的观赏路径。", tp="跨时期、全球（参见来源）。", ov="它兼顾观赏顺序、停留与疏散，常与叙事结合。",
 prin="参观路径按展陈逻辑串联节点，控制节奏与停留，使观展成为连续叙事。", method="以入口—序厅—重点—结束组织，设停留点与分流支线。",
 inst="名称：美术馆参观动线（类型性描述）；地点与设计者不适用。看展项如何被依次串联。", cap="见下方示意：参观路径串联展项。", limit="动线逆流与拥堵影响体验；需与疏散协调。", srcs=["wp-wayfinding", "guggenheim-visitor-guide"]),
"loop-route": dict(defn="回游式动线指路径首尾相接、可循环游览的组织方式。", tp="古代、中国（参见来源）。", ov="它让游客不走回头路，连续观赏并循环回到起点。",
 prin="路径闭合成环，各景点沿环布置，游客单向或双向循环而不重复。", method="以环形主路串联景点，支线深入局部后回到主环。",
 inst="名称：园林回游式主路（类型性描述）；地点与设计者不适用。看路径如何闭环。", cap="见下方示意：环形主路与支线。", limit="环路过长会疲劳；需设休憩点。", srcs=["wp-chinese-garden", "wp-wayfinding"]),
"serial-route": dict(defn="串联式动线指各空间依次相接、线性展开的组织方式。", tp="跨时期、全球（参见来源）。", ov="它顺序清晰，适合线性叙事与紧凑用地。",
 prin="空间沿一条主线依次串联，前一空间的出口即后一空间的入口。", method="沿单一主线顺序布置功能，控制节奏与转折。",
 inst="名称：串联式展廊（类型性描述）；地点与设计者不适用。看空间如何首尾相接。", cap="见下方示意：线性串联的空间序列。", limit="长度过大易疲劳且疏散单一；需设旁路。", srcs=["wp-architecture", "wp-wayfinding"]),
"radial-route": dict(defn="放射式动线指以一个中心向四周发散、由中心统摄的组织方式。", tp="跨时期、全球（参见来源）。", ov="它以中心节点汇聚与分配人流，方向清晰。",
 prin="以中心节点为枢纽向多个方向发散，人流在中心汇聚再分配。", method="设中心大厅或广场，放射出多条支路连接各区。",
 inst="名称：放射式大厅（类型性描述）；地点与设计者不适用。看中心如何分配人流。", cap="见下方示意：由中心放射的支路。", limit="中心节点易拥堵；需扩容与分流。", srcs=["wp-architecture", "wp-urban-design"]),
"side-window-daylight": dict(defn="侧窗采光指通过外墙侧向开窗引入天然采光的方式。", tp="跨时期、全球（参见来源）。", ov="侧窗决定光线方向与室内进深，是最常见的采光形式。",
 prin="光线从侧墙窗口进入，靠近窗口照度高、随进深衰减，形成方向性明暗。", method="按窗地比与朝向设侧窗，结合遮阳控制眩光与过热。",
 inst="名称：教室侧窗采光（类型性描述）；地点与设计者不适用。看光线如何由窗向室内衰减。", cap="见下方示意：侧窗与室内进深。", limit="进深过大处采光不足；需按规范核算。", srcs=["wp-daylighting-architecture", "wp-architectural-lighting-design"]),
"skylight": dict(defn="天窗采光指通过屋顶开口自上而下引入天然采光的方式。", tp="跨时期、全球（参见来源）。", ov="天窗适合大进深空间，可均匀引入顶光。",
 prin="光线从屋顶开口自上而下进入，照度分布较均匀，适合大进深与中庭。", method="按空间比例设天窗，结合遮阳与排烟构造。",
 inst="名称：展厅顶部天窗（类型性描述）；地点与设计者不适用。看顶光如何均匀铺开。", cap="见下方示意：屋顶天窗引入顶光。", limit="玻璃顶易眩光与过热；需遮阳排烟。", srcs=["wp-daylighting-architecture", "wp-atrium-architecture"]),
"wind-driven-ventilation": dict(defn="风压通风指依靠室外风在建筑迎风面与背风面形成压差驱动的自然通风。", tp="跨时期、全球（参见来源）。", ov="它利用迎背风压差组织穿堂风，受朝向与开口影响。",
 prin="风吹到建筑，迎风面正压、背风面负压，空气由进风口流向排风口。", method="在迎风与背风面分设进排风口，顺应主导风向组织穿堂风。",
 inst="名称：对流通风的房间（类型性描述）；地点与设计者不适用。看进排风口与风向的关系。", cap="见下方示意：迎风正压与背风负压。", limit="开口位置不当会短路；需按气候校核。", srcs=["wp-natural-ventilation", "wp-ventilation-architecture"]),
"atrium-ventilation": dict(defn="中庭通风指借中庭的竖向空间组织热压或风压通风的方式。", tp="20世纪、全球（参见来源）。", ov="中庭作为通风竖井，把热空气从高位排出。",
 prin="中庭贯通多层形成竖向通道，热空气上升从顶部排出，低位补入新风。", method="中庭顶部设排风口、底部设进风口，结合可开启天窗。",
 inst="名称：中庭热压通风（类型性描述）；地点与设计者不适用。看气流如何由下而上。", cap="见下方示意：中庭竖向气流。", limit="排烟与防火分隔须与通风协调；按规范。", srcs=["wp-atrium-architecture", "wp-ventilation-architecture"]),
"visual-comfort": dict(defn="视觉舒适指人在空间中看东西不费力、不刺眼且清晰可辨的状态。", tp="20世纪、全球（参见来源）。", ov="它兼顾照度、眩光控制与对比度，是照明设计的核心目标。",
 prin="照度充足、眩光受控、对比适度时视觉最舒适；过亮过暗或直射光都会引起疲劳。", method="按任务设定照度，控制眩光与亮度比，结合天然光与人工光。",
 inst="名称：办公空间的视觉舒适照明（类型性描述）；地点与设计者不适用。看亮度比与眩光如何被控制。", cap="见下方示意：照度、眩光与对比的平衡。", limit="只提亮度会眩光；参数须按规范。", srcs=["wp-architectural-lighting-design", "wp-daylighting-architecture"]),
"accessibility-design": dict(defn="无障碍设计指使不同行动能力者都能安全、便利地使用环境的设计。", tp="20世纪、全球（参见来源）。", ov="它以坡道、扶手、标识与尺度保障平等使用。",
 prin="通过消除高差、提供连续扶手与清晰指引，让不同能力者都能独立使用空间。", method="设无障碍坡道、扶手、触觉标识与足够通行宽度。",
 inst="名称：公共建筑无障碍入口（类型性描述）；地点与设计者不适用。看坡道与扶手如何保障通行。", cap="见下方示意：无障碍坡道与扶手。", limit="只设台阶会中断路径；尺寸须按规范。", srcs=["wp-universal-design", "wp-exit-sign"]),
}

SVG_R = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><polyline points='120,300 300,220 480,260 640,170' fill='none' stroke='var(--accent)' stroke-width='3'/><circle cx='300' cy='220' r='12' fill='var(--accent-soft)' stroke='var(--accent)'/><circle cx='480' cy='260' r='12' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_L = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='80' y1='100' x2='680' y2='100' stroke='var(--ink)' stroke-width='3'/><line x1='80' y1='320' x2='680' y2='320' stroke='var(--ink)' stroke-width='3'/><rect x='240' y='100' width='18' height='120' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='258' y1='130' x2='520' y2='300' stroke='var(--accent)' stroke-width='2'/><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_RT = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='380' cy='200' r='16' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='380' y1='200' x2='200' y2='120' stroke='var(--muted)'/><line x1='380' y1='200' x2='560' y2='120' stroke='var(--muted)'/><line x1='380' y1='200' x2='200' y2='290' stroke='var(--muted)'/><line x1='380' y1='200' x2='560' y2='290' stroke='var(--muted)'/><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG = {}
for k in D:
    if k in ("side-window-daylight", "skylight", "wind-driven-ventilation", "atrium-ventilation", "visual-comfort", "accessibility-design"):
        SVG[k] = SVG_L
    elif k == "radial-route":
        SVG[k] = SVG_RT
    else:
        SVG[k] = SVG_R

cov = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))["entries"]
META = {r["id"]: r for r in cov}


def main():
    rows = []
    for eid, f in D.items():
        m = META[eid]
        svg = SVG[eid].replace("</svg>", "<text x='40' y='40' fill='var(--ink)'>" + m["title"] + "</text></svg>")
        rows.append({
            "id": eid, "title": m["title"], "level": "L2", "tier": m["tier"],
            "theme": m["theme"], "period": m["period"], "region": m["region"],
            "definition": f["defn"], "time_or_place": f["tp"], "overview": f["ov"], "related": [],
            "sections": {"原理": f["prin"], "典型手法与适用条件": f["method"], "实例": f["inst"],
                         "常见错误与限制": f["limit"] + REG, "一图": f["cap"],
                         "待核实": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"]},
            "svg": [svg], "sources": f["srcs"], "needs_verification": True,
            "pending_notes": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"],
        })
    out = ROOT / "entries" / "batch-36.json"
    out.write_text(json.dumps({"unit_id": "batch-36", "title": "第36轮动线与物理环境条目", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-36 written", len(rows))


if __name__ == "__main__":
    main()
