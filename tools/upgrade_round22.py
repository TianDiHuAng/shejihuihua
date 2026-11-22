"""第22轮：核心 L1→L2（过渡空间/空间组织/室内外过渡/曲径/疏散动线/高差处理）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"transition-space": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='130' width='170' height='150' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='420' y='130' width='260' height='150' fill='none' stroke='var(--muted)'/><rect x='250' y='170' width='170' height='70' fill='none' stroke='var(--accent)' stroke-dasharray='8 5'/><text x='290' y='150' fill='var(--ink)'>过渡空间</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"spatial-organization": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='150' width='120' height='110' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='320' y='100' width='120' height='110' fill='none' stroke='var(--muted)'/><rect x='320' y='250' width='120' height='110' fill='none' stroke='var(--muted)'/><rect x='520' y='150' width='120' height='110' fill='none' stroke='var(--accent)'/><line x1='240' y1='205' x2='320' y2='155' stroke='var(--muted)'/><line x1='240' y1='205' x2='320' y2='305' stroke='var(--muted)'/><line x1='440' y1='155' x2='520' y2='205' stroke='var(--muted)'/><line x1='440' y1='305' x2='520' y2='205' stroke='var(--muted)'/><text x='300' y='70' fill='var(--ink)'>中心与群组组织</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"interior-exterior-transition": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='150' width='300' height='140' fill='none' stroke='var(--accent)'/><rect x='380' y='150' width='300' height='140' fill='none' stroke='var(--muted)' stroke-dasharray='10 6'/><line x1='380' y1='110' x2='380' y2='330' stroke='var(--muted)'/><text x='150' y='120' fill='var(--ink)'>室内</text><text x='520' y='120' fill='var(--ink)'>室外</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"winding-path": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><path d='M 120 320 Q 260 220 220 160 T 400 120 Q 560 110 620 200' fill='none' stroke='var(--accent)' stroke-width='3'/><circle cx='120' cy='320' r='10' fill='var(--accent)'/><text x='300' y='260' fill='var(--ink)'>曲折延长游程</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"evacuation-route": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='90' width='600' height='230' fill='none' stroke='var(--line)'/><line x1='160' y1='200' x2='620' y2='200' stroke='var(--accent)' stroke-width='3'/><polygon points='612,194 632,200 612,206' fill='var(--accent)'/><circle cx='160' cy='200' r='14' fill='none' stroke='var(--muted)'/><text x='300' y='170' fill='var(--ink)'>疏散方向与出口</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"level-change": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><polyline points='100,260 260,260 260,180 420,180 420,260 620,260' fill='none' stroke='var(--accent)' stroke-width='3'/><polyline points='260,260 260,240 420,240 420,260' fill='none' stroke='var(--muted)' stroke-dasharray='5 4'/><text x='330' y='130' fill='var(--ink)'>台阶与坡道转换高差</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"transition-space": {
 "原理":"过渡空间介于两处性质不同的空间之间，缓冲内外、公私或动静的突变。",
 "典型手法与适用条件":"以门厅、廊道或檐下作为缓冲；适用于由公共转入私密、由室外转入室内的场合。",
 "实例":"名称：门厅作为过渡空间（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"过渡缺失会让空间转换生硬；缓冲尺度与导向须与两侧匹配。" + REG,
 "一图":"见下方示意：夹在两室之间的过渡带。",
 "待核实":"示例空间的设计者与年代待核实。",
},
"spatial-organization": {
 "原理":"空间组织把功能、流线与空间单元组合成整体，常见串联、并列、集中与放射等方式。",
 "典型手法与适用条件":"按使用关系选择组织方式，以中心或路径统摄单元；适用于各类建筑平面。",
 "实例":"名称：集中式空间组织（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"组织方式与流线不匹配会混乱；单元尺度与出入口须校核。" + REG,
 "一图":"见下方示意：中心与群组的组织关系。",
 "待核实":"示例平面的设计者与年代待核实。",
},
"interior-exterior-transition": {
 "原理":"室内外过渡通过庭院、廊道与可开启界面，让内外在空间、视线与气候上连续。",
 "典型手法与适用条件":"以檐廊、庭院与落地窗柔化边界；适用于气候温和、强调景观的空间。",
 "实例":"名称：庭院式内外过渡（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"界面过于通透会带来眩光与能耗问题；气密与水密须达标。" + REG,
 "一图":"见下方示意：室内向室外的连续过渡。",
 "待核实":"示例空间的设计者与年代待核实。",
},
"winding-path": {
 "原理":"曲径以曲折路线延长游览、变换视角，使有限场地产生多重画面并放慢行进。",
 "典型手法与适用条件":"以折线、弧线与转折组织路径，配合障景与对景；适用于园林游线。",
 "实例":"名称：园林曲径（类型性描述）；地点：中国苏州；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"曲折过度会迷路、迂回过长令人疲惫；无障碍与排水须兼顾。" + REG,
 "一图":"见下方示意：曲折延长的游程。",
 "待核实":"曲径手法的独立专门来源与具体实例设计者、年代待核实。",
},
"evacuation-route": {
 "原理":"疏散动线在紧急情况下把人员快速引向安全出口，强调清晰标识、足够宽度与避免瓶颈。",
 "典型手法与适用条件":"设置连续疏散通道、出口与应急照明，控制疏散距离；按建筑类型与人数校核。",
 "实例":"名称：公共建筑疏散路径（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"通道堆物或出口不足会造成拥堵；疏散宽度与距离须严格按规范执行。" + REG,
 "一图":"见下方示意：疏散方向与出口。",
 "待核实":"示例建筑的疏散设计参数与设计者待核实。",
},
"level-change": {
 "原理":"高差处理用台阶、坡道与平台组织空间转换，既划分领域也制造视线变化。",
 "典型手法与适用条件":"以台阶分区、坡道保证无障碍；适用于场地高差与多层空间。",
 "实例":"名称：场地高差处理（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只设台阶会中断无障碍路径；踏步尺寸与扶手须按规范校核。" + REG,
 "一图":"见下方示意：台阶与坡道转换高差。",
 "待核实":"示例场地的高差参数与设计者待核实。",
},
}

SRC = {
"transition-space":["wp-vestibule-architecture","wp-loggia"],
"spatial-organization":["wp-architecture","wp-architectural-theory"],
"interior-exterior-transition":["wp-courtyard","wp-loggia"],
"winding-path":["wp-chinese-garden"],
"evacuation-route":["wp-exit-sign","wp-wayfinding"],
"level-change":["wp-architecture","wp-sunken-courtyard"],
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
