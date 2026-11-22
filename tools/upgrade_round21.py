"""第21轮：核心 L1→L2（气韵/留白/意境/空间定义/人体尺度/空间序列）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"qi-yun": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='90' width='520' height='220' fill='none' stroke='var(--line)'/><path d='M 180 260 Q 300 140 420 230 T 600 170' fill='none' stroke='var(--accent)' stroke-width='3'/><text x='300' y='60' fill='var(--ink)'>笔势贯通而气脉生动</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"liubai": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='80' width='600' height='240' fill='none' stroke='var(--line)'/><rect x='120' y='200' width='180' height='100' fill='var(--accent-soft)' stroke='var(--accent)'/><circle cx='520' cy='150' r='60' fill='none' stroke='var(--muted)'/><text x='430' y='300' fill='var(--ink)'>大面积空白参与构图</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"yijing": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='80' y1='300' x2='680' y2='300' stroke='var(--ink)' stroke-width='2'/><path d='M 140 300 Q 240 180 340 300' fill='none' stroke='var(--accent)'/><path d='M 340 300 Q 460 150 580 300' fill='none' stroke='var(--muted)'/><circle cx='620' cy='120' r='30' fill='none' stroke='var(--muted)'/><text x='430' y='100' fill='var(--ink)'>景外之意的留白与远山</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"space-definition": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='110' width='520' height='190' fill='none' stroke='var(--accent)'/><line x1='120' y1='110' x2='120' y2='300' stroke='var(--muted)' stroke-width='6'/><line x1='640' y1='110' x2='640' y2='300' stroke='var(--muted)' stroke-width='6'/><text x='300' y='210' fill='var(--ink)'>界面限定的场所</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"human-scale": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='80' y1='310' x2='680' y2='310' stroke='var(--ink)' stroke-width='3'/><circle cx='240' cy='230' r='14' fill='var(--accent)'/><line x1='240' y1='244' x2='240' y2='310' stroke='var(--accent)' stroke-width='3'/><rect x='440' y='150' width='120' height='160' fill='none' stroke='var(--muted)'/><text x='180' y='180' fill='var(--ink)'>人体为尺</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"spatial-sequence": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='90' y='150' width='120' height='130' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='260' y='130' width='150' height='170' fill='none' stroke='var(--muted)'/><rect x='460' y='110' width='200' height='190' fill='none' stroke='var(--accent)'/><polyline points='150,210 335,210 560,200' fill='none' stroke='var(--muted)' stroke-dasharray='8 6'/><text x='250' y='90' fill='var(--ink)'>开合与尺度递进</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"qi-yun": {
 "原理":"气韵生动指作品整体气脉贯通、形象有生气，是六法之首，高于单纯的形似。",
 "典型手法与适用条件":"以用笔连贯、虚实相生与经营位置共同营造；适用于人物、山水与花鸟。",
 "实例":"名称：《古画品录》品评体系（类型性记载）；地点：古代中国；设计者：不适用；年份：约公元 500 年。此处仅列名称、地点、设计者与年份信息，不复制图像。",
 "常见错误与限制":"只求形似而失气韵则呆板；气韵依赖整体，不能靠局部堆砌。" + REG,
 "一图":"见下方示意：笔势贯通、气脉生动。",
 "待核实":"具体品评作品与作者年代待核实。",
},
"liubai": {
 "原理":"留白以未画之处承载空间、光线与想象，使主体更突出、画面更具呼吸与意境。",
 "典型手法与适用条件":"计白当黑、以虚衬实；适用于水墨、山水与简洁的版式设计。",
 "实例":"名称：中国画留白实践（类型性记载）；地点：中国；设计者：不适用；年份：不适用。此处仅列名称、地点、设计者与年份信息，不复制图像。",
 "常见错误与限制":"留白过多则空洞、过少则壅塞；须与主体比例和题意配合。" + REG,
 "一图":"见下方示意：大面积空白参与构图。",
 "待核实":"具体作品的作者与年代待核实。",
},
"yijing": {
 "原理":"意境由可见物象与留白共同引发，把观者从形似引向情景交融的联想与情绪。",
 "典型手法与适用条件":"以景寓情、虚实相生；适用于山水、园林与诗画结合的表达。",
 "实例":"名称：山水画的意境表达（类型性记载）；地点：中国；设计者：不适用；年份：不适用。此处仅列名称、地点、设计者与年份信息，不复制图像。",
 "常见错误与限制":"刻意造境会显做作；意境因人而异，难以标准化衡量。" + REG,
 "一图":"见下方示意：景外之意的留白与远山。",
 "待核实":"具体作品的作者与年代待核实。",
},
"space-definition": {
 "原理":"建筑空间由围合界面、尺度与人的活动共同限定，感知不只来自几何边界，也来自光线与材料。",
 "典型手法与适用条件":"以墙、顶、地界定领域，借光与材质强化氛围；适用于各类室内外空间。",
 "实例":"名称：由界面限定的室内空间（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只重围合而忽视光线与使用会显呆板；尺度失衡影响感受。" + REG,
 "一图":"见下方示意：界面限定的场所。",
 "待核实":"示例空间的设计者与年代待核实。",
},
"human-scale": {
 "原理":"人体尺度以人的身高、步幅与视高为参照，使门、台阶、家具与通道与身体动作相匹配。",
 "典型手法与适用条件":"以常用人体尺寸确定细部尺度，营造亲切感；公共空间可与更大尺度并置。",
 "实例":"名称：住宅的亲切尺度（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"忽视尺度会造成压迫或疏离；具体尺寸须按规范与人群差异校核。" + REG,
 "一图":"见下方示意：以人体为尺。",
 "待核实":"示例空间的实测数据与设计者待核实。",
},
"spatial-sequence": {
 "原理":"空间序列把若干空间按进入顺序组织，以开合、明暗与尺度变化控制节奏与叙事。",
 "典型手法与适用条件":"起—承—转—合组织路径；适用于院落、展馆与纪念性空间。",
 "实例":"名称：院落式空间序列（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"节奏单一会乏味、转折过多会迷失；导向与疏散须校核。" + REG,
 "一图":"见下方示意：开合与尺度递进。",
 "待核实":"示例序列的设计者与年代待核实。",
},
}

SRC = {
"qi-yun":["wp-six-principles-chinese-painting","wp-chinese-painting"],
"liubai":["cnr-liubai","rmrb-liubai","wp-chinese-painting"],
"yijing":["wp-chinese-painting","wp-shitao"],
"space-definition":["wp-architecture","wp-architectural-theory"],
"human-scale":["wp-proportion-architecture","wp-architecture"],
"spatial-sequence":["wp-architecture","wp-architectural-theory"],
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
