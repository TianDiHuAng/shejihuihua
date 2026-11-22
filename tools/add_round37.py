"""第37轮：写 24 条（空间组/风格史/地域风格等），L2。先生成再按相似度补差异。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

D = {
"east-west-color-compare": ("中西色彩观比较对照中国画“随类赋彩”与西方条件色体系。", "跨时期、全球（参见来源）。", "东方重类别与意象设色，西方重光源下的条件色变化。", "比较时看设色依据：一类归色，一随光变色。", "以一方标准评判另一方会失真。", ["wp-chinese-painting", "wp-color-theory"]),
"monumental-scale": ("纪念性尺度指以超大尺度营造崇高与权威感的空间处理。", "跨时期、全球（参见来源）。", "它放大构件与体量，使人在其中显得渺小。", "以超常层高、巨柱与宽阔台阶强化崇高感。", "尺度失衡会压抑或空洞。", ["wp-proportion-architecture", "wp-architecture"]),
"intimate-scale": ("亲切尺度指以接近人体与日常活动的尺寸营造亲近感。", "跨时期、全球（参见来源）。", "它以小尺度细部与柔和光线让人放松。", "以低层高、小开间与温暖材料拉近距离。", "过小会局促；需与功能匹配。", ["wp-proportion-architecture", "wp-architecture"]),
"boundary": ("边界指划分空间领域的界面，可为实墙、绿化或标高等软硬形式。", "跨时期、全球（参见来源）。", "边界界定内外与公私，决定空间的围合程度。", "以墙、绿篱、高差或铺装变化形成不同强度的边界。", "边界过实会封闭；过虚则领域模糊。", ["wp-architecture", "wp-courtyard"]),
"node-path": ("节点与路径指由停留节点与连接路径共同构成的空间结构。", "跨时期、全球（参见来源）。", "节点承载活动，路径串联节点并组织行进。", "在路径交汇处设节点广场或厅，形成节奏。", "节点过密会分散；过疏则单调。", ["wp-wayfinding", "wp-architecture"]),
"corridor-space": ("廊道空间指狭长、连接两处的通行空间。", "跨时期、全球（参见来源）。", "廊道以连续界面引导行进，可兼作展廊与过渡。", "以连续侧界面与韵律开窗组织行进视线。", "过长无变化会单调；宽度须满足疏散。", ["wp-loggia", "wp-architecture"]),
"eaves-space": ("檐下空间指屋檐出挑形成的半室外过渡空间。", "古代、中国（参见来源）。", "檐下遮阳避雨，是室内外的缓冲带。", "以出挑屋檐与柱廊形成灰空间，兼作交往。", "出挑过大会影响采光；需结构支撑。", ["wp-chinese-architecture", "wp-courtyard"]),
"opening-interface": ("门窗洞口指界面上供通行与采光、通风的开口。", "跨时期、全球（参见来源）。", "洞口决定内外联系、采光与视线。", "按功能与朝向设洞口大小与位置，兼顾采光通风。", "洞口不当会眩光或私密性差。", ["wp-architecture", "wp-courtyard"]),
"interface-permeability": ("界面渗透指界面在视觉或通行上允许内外连通的程度。", "20世纪、全球（参见来源）。", "高渗透界面使内外连续，低渗透则强调围合。", "以玻璃、格栅与可开启界面调节渗透程度。", "过透会失私密与能耗；按需调节。", ["wp-loggia", "wp-architecture"]),
"view-corridor": ("视线通廊指为观景保留的连续视觉通道。", "跨时期、全球（参见来源）。", "它把远景纳入空间体验，组织对景与借景。", "沿轴线或路径保留无遮挡视线，尽端设对景。", "遮挡会破坏通廊；需控制建设高度。", ["wp-chinese-garden", "wp-wayfinding"]),
"sustainable-design": ("可持续设计指在设计中兼顾生态、社会与经济长期性的方法。", "20世纪、全球（参见来源）。", "它把全生命周期影响纳入决策，被动优先。", "以被动式策略、材料循环与可再生资源并用。", "只贴标签而无实测不算可持续。", ["wp-sustainable-architecture", "wp-green-building"]),
"arts-crafts": ("工艺美术运动主张回归手工艺、反对工业粗制，强调材料与工艺的诚实。", "20世纪、欧洲（参见来源）。", "它重视手作与装饰的整体性，影响后续设计。", "以手工、自然纹样与真实材料组织家具与建筑细部。", "手作成本高；难大规模推广。", ["wp-architectural-style", "wp-history-of-architecture"]),
"constructivism": ("构成主义以几何体块与结构暴露表达革命的动态与理性。", "20世纪、欧洲（参见来源）。", "它以悬浮体块与红色几何塑造新社会的形象。", "用简洁几何体块、暴露结构与动态构图。", "形式激进易忽视使用；需落地调整。", ["wp-architectural-style", "wp-modern-architecture"]),
"high-tech": ("高技派以暴露结构、设备与工业化构件为特征。", "20世纪、全球（参见来源）。", "它把技术本身作为美学表达。", "以外露钢构、管线与预制构件展示技术。", "设备暴露维护成本高；需协调。", ["wp-modern-architecture", "wp-architectural-style"]),
"minimalism-architecture": ("极简主义建筑以最少元素、纯净体量与精致细部为特征。", "20世纪、全球（参见来源）。", "它去除装饰，强调比例、光线与材料本身。", "以大面积素面、精确节点与自然光组织空间。", "过度简省会冷硬或功能不足。", ["wp-modern-architecture", "wp-architectural-style"]),
"critical-regionalism": ("批判地域主义主张在现代性与地方性之间保持张力。", "20世纪、全球（参见来源）。", "它用现代技术回应地方气候、材料与文化。", "以现代构造结合地域材料与空间原型。", "流于符号拼贴会失批判性。", ["wp-vernacular-architecture", "wp-architectural-style"]),
"vernacular-architecture": ("乡土建筑指就地取材、依地方气候与技艺建造的建筑。", "跨时期、全球（参见来源）。", "它由使用者与工匠按经验建造，地域差异鲜明。", "以本土材料与适应气候的构造组织。", "直接移植会破坏地域协调。", ["wp-vernacular-architecture", "wp-building-material"]),
"japanese-architecture": ("日本建筑以木构、榻榻米尺度与室内外连续为特征。", "跨时期、东亚（参见来源）。", "它强调轻盈木构、深远出檐与借景。", "以木框架、推拉门与缘侧组织内外连续。", "忽视气候与维护会失当。", ["wp-japanese-architecture", "wp-architectural-style"]),
"islamic-architecture": ("伊斯兰建筑以穹顶、拱廊、庭院与几何装饰为特征。", "中世纪、伊斯兰/南亚（参见来源）。", "它用几何、书法与庭院组织宗教与世俗空间。", "以伊万、穹顶、穆克纳斯与庭院组织。", "装饰套用会失结构逻辑。", ["wp-islamic-architecture", "wp-architectural-style"]),
"indian-architecture": ("印度建筑以石构神庙、雕刻与曼陀罗平面为特征。", "古代、伊斯兰/南亚（参见来源）。", "它以宇宙图式的平面与繁复雕刻表达信仰。", "按曼陀罗平面布置塔与龛，配雕刻装饰。", "雕刻过密会失整体；需结构支撑。", ["wp-indian-architecture", "wp-architectural-style"]),
"imperial-architecture": ("宫殿建筑指供帝王居住与理政的高等级建筑群。", "古代、中国（参见来源）。", "它以轴线、院落与等级化屋顶体现礼制。", "以中轴院落层层递进，屋顶等级区分主次。", "等级僭越与尺度失当会失序。", ["wp-chinese-architecture", "wp-chinese-garden"]),
"religious-architecture": ("宗教建筑指供礼拜与仪式使用的建筑类型。", "跨时期、全球（参见来源）。", "它以空间、光线与象征组织神圣体验。", "以轴线、穹顶或高塔与光线营造神圣感。", "只重形式忽略仪式需求会失当。", ["wp-architectural-style", "wp-gothic-architecture"]),
"rule-of-odds": ("奇数法则指画面中主体数量取奇数更易形成生动均衡的构图经验。", "跨时期、全球（参见来源）。", "奇数群体有中心与两侧，视觉更自然。", "以三或五个主体组织，避免僵硬的对称双数。", "机械套用会牵强；需看内容。", ["wp-composition-visual-arts", "wp-rule-of-thirds"]),
"tints-shades": ("色调与明暗层次指以加白或加黑改变色彩明度的做法。", "跨时期、全球（参见来源）。", "加白得浅色（tint）、加黑得暗色（shade），构成层次。", "以同一色相加白/加黑建立明度梯度。", "过度加白会失饱和、加黑会失通透。", ["wp-color-theory", "wp-color-wheel"]),
}

SVG_A = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='120' width='520' height='180' fill='none' stroke='var(--accent)'/><line x1='380' y1='120' x2='380' y2='300' stroke='var(--muted)'/><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_B = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='380' cy='200' r='110' fill='none' stroke='var(--accent)'/><line x1='120' y1='200' x2='270' y2='200' stroke='var(--muted)'/><line x1='490' y1='200' x2='640' y2='200' stroke='var(--muted)'/><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"

cov = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))["entries"]
META = {r["id"]: r for r in cov}


def main():
    rows = []
    for i, (eid, (defn, tp, ov, method, limit, srcs)) in enumerate(D.items()):
        m = META[eid]
        base = SVG_A if i % 2 == 0 else SVG_B
        svg = base.replace("</svg>", "<text x='40' y='40' fill='var(--ink)'>" + m["title"] + "</text></svg>")
        rows.append({
            "id": eid, "title": m["title"], "level": "L2", "tier": m["tier"],
            "theme": m["theme"], "period": m["period"], "region": m["region"],
            "definition": defn, "time_or_place": tp, "overview": ov, "related": [],
            "sections": {"原理": defn + ov, "典型手法与适用条件": method,
                         "实例": "名称：%s的典型场景（类型性描述）；地点与设计者不适用。" % m["title"],
                         "常见错误与限制": limit + REG,
                         "一图": "见下方示意：%s的关系。" % m["title"],
                         "待核实": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"]},
            "svg": [svg], "sources": srcs, "needs_verification": True,
            "pending_notes": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"],
        })
    out = ROOT / "entries" / "batch-37.json"
    out.write_text(json.dumps({"unit_id": "batch-37", "title": "第37轮条目（24条）", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-37 written", len(rows))


if __name__ == "__main__":
    main()
