"""第35轮：写 12 条条目（造景组/下沉空间/材料），L2、去模板化、SVG 加标题。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

D = {
"added-scenery": dict(defn="添景是在主景之外补置树木、山石或建筑以丰富画面层次的手法。", tp="古代、中国（参见来源）。", ov="它让主体不孤立，以前后层次的补景增强纵深。",
 prin="在主景周围补入次要景物，借前后遮挡与远近对比增加层次，使画面更完整。", method="于前景或侧旁添置树石、亭台，控制主次与疏密。",
 inst="名称：园林主景旁的添景树石（类型性描述）；地点与设计者不适用。看补景如何托出主景。", cap="见下方示意：主景与添景的前后层次。", limit="添景过多会夺主；需控制体量与位置。", srcs=["wp-chinese-garden", "wp-garden-design"]),
"side-scenery": dict(defn="夹景是在视线两侧布置景物、把视线夹向远处主景的手法。", tp="古代、中国（参见来源）。", ov="两侧景物的夹峙把视线收束，突出尽端的主体。",
 prin="两侧景物形成视觉边界，收窄视线通道，把注意力引向尽端主景。", method="沿路径两侧列植树石或墙体，形成透视走廊。",
 inst="名称：游径两侧的夹景树列（类型性描述）；地点与设计者不适用。看两侧景物如何收束视线。", cap="见下方示意：两侧夹景形成视线通道。", limit="夹景过密会压抑；需留出通透。", srcs=["wp-chinese-garden", "wp-garden-design"]),
"suppressed-scenery": dict(defn="抑景是先用遮挡压抑视线、再放开以突出主景的造景手法。", tp="古代、中国（参见来源）。", ov="它以先抑后扬制造期待与惊喜。",
 prin="通过入口的遮挡与转折压低预期，进入后豁然开朗，使主景更动人。", method="在入口设障景或狭道，转折后再现主景。",
 inst="名称：园林入口的先抑后扬（类型性描述）；地点与设计者不适用。看转折前后视野的对比。", cap="见下方示意：遮挡—转折—放开。", limit="压抑过久会疲惫；转折需自然。", srcs=["wp-chinese-garden", "wp-garden-design"]),
"rockery": dict(defn="叠石是以假山石堆叠模拟自然山峦的造园手法。", tp="古代、中国（参见来源）。", ov="叠石以石形与堆法营造峰、峦、洞、壑。",
 prin="依石的瘦、透、漏、皱选石，按山势堆叠，模拟自然山岳的起伏与洞穴。", method="选石、立意、堆叠，结合植物与水形成山景。",
 inst="名称：园林假山（类型性描述）；地点与设计者不适用。看石形与堆法如何造出峰壑。", cap="见下方示意：石峰与洞壑的堆叠。", limit="堆叠失当会松散危险；需结构安全。", srcs=["wp-chinese-garden", "wp-garden-design"]),
"planting-design": dict(defn="植物配置是按生态与观赏需求选配植物的设计工作。", tp="跨时期、全球（参见来源）。", ov="它兼顾季相、色彩、层次与养护。",
 prin="按植物的高度、色相、花期与习性分层配置，形成四季可观的群落。", method="以上中下三层搭配乔灌草，考虑季相与维护。",
 inst="名称：园林乔灌草分层配置（类型性描述）；地点与设计者不适用。看季相与层次的搭配。", cap="见下方示意：乔木、灌木、地被的分层。", limit="忽视习性与养护会导致成活率低；需专业选种。", srcs=["wp-garden-design", "wp-landscape-architecture"]),
"garden-architecture": dict(defn="园林建筑指园林中的亭、台、楼、榭等点景与观景建筑。", tp="古代、中国（参见来源）。", ov="园林建筑既是景点也是观景点，组织游线与视线。",
 prin="亭榭等建筑置于景观点，既成景又供观景，串联游线与视线。", method="依景设亭、临水建榭，控制体量与样式以融于自然。",
 inst="名称：临水亭榭（类型性描述）；地点与设计者不适用。看亭榭如何兼作景点与观景处。", cap="见下方示意：亭榭与水面、游线的关系。", limit="体量过大将压景；需与山水协调。", srcs=["wp-chinese-garden", "wp-garden-design"]),
"seasonal-scenery": dict(defn="四季造景指借助植物与景物的季相变化营造四时不同的景致。", tp="古代、中国（参见来源）。", ov="它以花木荣枯与气象变化使园林四季可观。",
 prin="不同植物在不同季节呈现花、叶、果的变化，配合雨雪晴晦形成四时景致。", method="按季相选配花木，设观景点题名以点景。",
 inst="名称：四季花木的季相配置（类型性描述）；地点与设计者不适用。看春夏秋冬的景色变化。", cap="见下方示意：四时花木的季相更替。", limit="季相集中会他季萧条；需均衡配置。", srcs=["wp-chinese-garden", "wp-garden-design"]),
"sunken-garden": dict(defn="下沉花园是低于周边地坪、以高差围合的下沉式绿化庭院。", tp="20世纪、全球（参见来源）。", ov="它以高差形成安静绿岛，改善采光与微气候。",
 prin="下沉形成内聚空间，植物与水面调节温湿，挡土与排水是关键构造。", method="以台阶/坡道连接地面，结合挡土墙、种植与排水组织。",
 inst="名称：城市下沉花园（类型性描述）；地点与设计者不适用。看高差、绿化与排水的组合。", cap="见下方示意：下沉花园的剖面与排水。", limit="排水与防潮不当会积水返潮；需按规范。", srcs=["wp-sunken-courtyard", "wp-garden-design"]),
"semi-sunken-space": dict(defn="半下沉空间指部分低于地面、部分仍接地的空间。", tp="20世纪、全球（参见来源）。", ov="它折中采光与围合，常见于半地下住宅与公共空间。",
 prin="一侧下沉获得安静与私密，另一侧仍可开窗采光，兼顾两者。", method="沿坡地或错层布置，下沉侧设采光井，接地侧开窗。",
 inst="名称：坡地半下沉住宅（类型性描述）；地点与设计者不适用。看两侧采光与私密的平衡。", cap="见下方示意：半下沉空间的错层剖面。", limit="防潮与通风须专门处理；需按规范。", srcs=["wp-architecture", "wp-sunken-courtyard"]),
"sunken-atrium": dict(defn="地下中庭指位于地下或半地下、贯通多层并引入天然光的核心空间。", tp="20世纪、全球（参见来源）。", ov="它以天窗采光组织地下空间的交通与公共活动。",
 prin="中庭贯通地下多层并通过天窗或下沉庭院引入天然光，改善地下环境。", method="以天窗/下沉庭院采光，围绕中庭布置交通与公共功能。",
 inst="名称：地下商业中庭（类型性描述）；地点与设计者不适用。看天窗如何把光引入地下。", cap="见下方示意：地下中庭与天窗采光。", limit="采光不足会阴暗；排烟与疏散须按规范。", srcs=["wp-atrium-architecture", "wp-sunken-courtyard"]),
"material-color": dict(defn="材料色彩指材料本身的固有色及其对空间氛围的影响。", tp="跨时期、全球（参见来源）。", ov="材料色与涂层色不同，受纹理与光照影响。",
 prin="材料的固有颜色与表面纹理共同决定其呈现色，粗糙面色彩更沉、光面更亮。", method="依空间基调选材色，以材质本色减少涂装、控制色差。",
 inst="名称：清水混凝土的灰色基调（类型性描述）；地点与设计者不适用。看材质本色如何定调。", cap="见下方示意：不同材料的固有色与质感。", limit="忽略光照会色差失衡；需样板比对。", srcs=["wp-color-theory", "wp-building-material"]),
"structural-material": dict(defn="结构材料指承担荷载的主要材料，如石、木、砖、钢与混凝土。", tp="跨时期、全球（参见来源）。", ov="结构材料决定跨度、形态与建造方式。",
 prin="不同结构材料的强度与受力方式不同，决定可实现的跨度与形态。", method="按跨度与受力选材，木石受压、钢混可大跨。",
 inst="名称：混凝土框架结构（类型性描述）；地点与设计者不适用。看材料如何决定柱网与跨度。", cap="见下方示意：不同结构材料的受力方式。", limit="选材不当影响安全与造价；须按规范。", srcs=["wp-building-material", "wp-architecture"]),
}

SVG_A = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='90' width='600' height='230' fill='none' stroke='var(--line)'/><circle cx='240' cy='200' r='34' fill='var(--accent-soft)' stroke='var(--accent)'/><path d='M 360 260 Q 460 160 600 250' fill='none' stroke='var(--muted)'/><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_B = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='60' y1='150' x2='700' y2='150' stroke='var(--ink)' stroke-width='2'/><polyline points='160,150 320,300 540,300 540,150' fill='none' stroke='var(--accent)'/><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_C = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='130' width='220' height='140' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='400' y='130' width='220' height='140' fill='none' stroke='var(--muted)'/><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG = {}
for k in D:
    SVG[k] = SVG_B if k in ("sunken-garden", "semi-sunken-space", "sunken-atrium") else (SVG_C if k in ("material-color", "structural-material") else SVG_A)

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
    out = ROOT / "entries" / "batch-35.json"
    out.write_text(json.dumps({"unit_id": "batch-35", "title": "第35轮造景/下沉/材料条目", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-35 written", len(rows))


if __name__ == "__main__":
    main()
