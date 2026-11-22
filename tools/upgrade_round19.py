"""第19轮：7 条 L1→L2（4 理论 + 场所依恋 + 游线 + 排水），强去模板化。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"geometry-symmetry": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='380' y1='60' x2='380' y2='340' stroke='var(--accent)' stroke-dasharray='8 6'/><rect x='220' y='140' width='120' height='140' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='420' y='140' width='120' height='140' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='330' y='110' fill='var(--ink)'>镜像对称</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"visual-movement": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><path d='M 120 300 Q 300 160 420 240 T 650 140' fill='none' stroke='var(--accent)' stroke-width='3'/><polygon points='640,134 660,140 642,150' fill='var(--accent)'/><circle cx='120' cy='300' r='12' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='330' y='120' fill='var(--ink)'>视线由起点被引导至终点</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"leading-lines": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='90' y1='330' x2='560' y2='200' stroke='var(--accent)' stroke-width='3'/><line x1='670' y1='330' x2='560' y2='200' stroke='var(--muted)'/><circle cx='560' cy='200' r='16' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='140' y='300' fill='var(--ink)'>道路/栏杆汇聚</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"rhythm-repetition": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='100' y='160' width='40' height='100' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='200' y='160' width='40' height='100' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='300' y='160' width='40' height='100' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='400' y='160' width='40' height='100' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='500' y='160' width='40' height='100' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='260' y='130' fill='var(--ink)'>重复与间距节奏</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"place-attachment": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='380' cy='200' r='80' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='350' y='205' fill='var(--ink)'>场所</text><line x1='300' y1='140' x2='200' y2='90' stroke='var(--muted)'/><line x1='460' y1='140' x2='560' y2='90' stroke='var(--muted)'/><text x='160' y='80' fill='var(--ink)'>记忆</text><text x='540' y='80' fill='var(--ink)'>归属</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"tour-route": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><polyline points='110,300 230,220 350,280 470,180 600,230 660,160' fill='none' stroke='var(--accent)' stroke-width='3'/><circle cx='230' cy='220' r='12' fill='var(--accent-soft)' stroke='var(--accent)'/><circle cx='470' cy='180' r='12' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='120' y='150' fill='var(--ink)'>景点串联的游线</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"drainage": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='80' y1='140' x2='680' y2='140' stroke='var(--ink)' stroke-width='2'/><polyline points='300,140 380,220 460,140' fill='none' stroke='var(--muted)' stroke-width='2'/><line x1='360' y1='220' x2='400' y2='300' stroke='var(--accent)' stroke-width='3'/><text x='330' y='110' fill='var(--ink)'>坡向与集水点</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"geometry-symmetry": {
 "原理":"对称让左右或上下两部分互为镜像，带来稳定与仪式感；轻微的破对称则能避免呆板。",
 "典型手法与适用条件":"立面以中轴镜像、局部增减打破完全对称；适用于纪念性与正式空间。",
 "实例":"名称：对称立面的礼仪建筑（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"强对称会压抑变化；地形不平处硬做对称代价高。" + REG,
 "一图":"见下方示意：以中轴镜像的两半。",
 "待核实":"示例建筑的设计者与年代待核实。",
},
"visual-movement": {
 "原理":"画面借线条、明暗与形状的排列，牵引观者的视线沿一定路线移动，形成观看的“动势”。",
 "典型手法与适用条件":"用渐变的明暗或连续曲线引导由入口到重点；适合叙事性画面。",
 "实例":"名称：叙事画面的视线引导（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"引导线互相冲突会让视线迷失；动势过强则喧宾夺主。" + REG,
 "一图":"见下方示意：视线由起点被引向终点。",
 "待核实":"示例画面的作者与年代待核实。",
},
"leading-lines": {
 "原理":"现实中或隐含的线条（道路、栏杆、光影边界）可把视线拉向主体，是构图的“指路牌”。",
 "典型手法与适用条件":"利用透视汇聚或重复排列的线条指向主体；适用于风景与建筑摄影。",
 "实例":"名称：道路汇聚式引导（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"线条指向画面外会带走注意；过多线条互相竞争。" + REG,
 "一图":"见下方示意：道路与栏杆汇聚于主体。",
 "待核实":"示例照片的拍摄者与年代待核实。",
},
"rhythm-repetition": {
 "原理":"相同或相似元素的重复形成视觉节奏，间距与大小的变化则决定节奏的快慢与强弱。",
 "典型手法与适用条件":"柱列、窗格与砖缝的重复可建立秩序；以渐变间距制造韵律。",
 "实例":"名称：柱廊的重复韵律（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"机械等距会单调；重复元素过多显得拥挤。" + REG,
 "一图":"见下方示意：重复与间距形成的节奏。",
 "待核实":"示例柱廊的设计者与年代待核实。",
},
"place-attachment": {
 "原理":"场所依恋指人与特定空间长期互动后形成的情感纽带，使人产生归属、认同与留恋。",
 "典型手法与适用条件":"保留可辨识的地标与日常活动场所，支持社区记忆；适用于更新与社区设计。",
 "实例":"名称：社区公共空间的场所依恋营造（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"大拆大建会切断情感联结；符号化复制难以替代真实记忆。" + REG,
 "一图":"见下方示意：场所与记忆、归属的联结。",
 "待核实":"示例社区的研究者与年代待核实。",
},
"tour-route": {
 "原理":"游线把多个景点按时间与视线顺序串联，决定先看什么、何时转折、在哪里停留。",
 "典型手法与适用条件":"以起景—发展—高潮—收束组织路径；适用于园林与展陈参观。",
 "实例":"名称：拙政园式园林游线（类型性描述）；地点：中国苏州；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"游线过长或重复会疲劳；导向不清会使游客逆行。" + REG,
 "一图":"见下方示意：若干景点被游线串联。",
 "待核实":"具体园林游线的设计者与年代待核实。",
},
"drainage": {
 "原理":"排水依靠坡度、沟槽与集水点，把雨水迅速引离低洼与铺装，避免积水与倒灌。",
 "典型手法与适用条件":"设置找坡、明沟或暗管与雨水口；下沉空间尤需重点组织。",
 "实例":"名称：下沉广场排水组织（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"坡度不足或雨水口堵塞会积水；管径与重现期须按规范校核。" + REG,
 "一图":"见下方示意：坡向与集水点。",
 "待核实":"示例排水设计的工程参数与设计者待核实。",
},
}

SRC = {
"geometry-symmetry":["wp-symmetry","wp-composition-visual-arts"],
"visual-movement":["wp-composition-visual-arts","wp-leading-line"],
"leading-lines":["wp-leading-line","wp-composition-visual-arts"],
"rhythm-repetition":["wp-composition-visual-arts","wp-symmetry"],
"place-attachment":["wp-environmental-psychology","wp-place-attachment"],
"tour-route":["wp-chinese-garden","wp-wayfinding"],
"drainage":["wp-architecture","wp-sunken-courtyard"],
}

def main():
    n=0
    for path in sorted((ROOT/"entries").glob("*.json")):
        doc=json.loads(path.read_text(encoding="utf-8")); ch=False
        for e in doc.get("entries",[]):
            k=e["id"]
            if k not in S: continue
            e["level"]="L2"; e["sections"]=S[k]; e["svg"]=[SVG[k]]; e["sources"]=SRC[k]
            e["needs_verification"]=True; e["pending_notes"]="实例的具体名称、设计者与年代待补充独立来源。"
            n+=1; ch=True
        if ch: path.write_text(json.dumps(doc,ensure_ascii=False,indent=2),encoding="utf-8")
    print("upgraded",n)

if __name__=="__main__": main()
