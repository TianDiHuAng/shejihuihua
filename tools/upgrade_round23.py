"""第23轮：收尾剩余 7 条核心 L1→L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"east-west-perspective-compare": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='60' y='110' width='300' height='180' fill='none' stroke='var(--muted)'/><circle cx='210' cy='200' r='6' fill='var(--accent)'/><line x1='120' y1='280' x2='210' y2='200' stroke='var(--muted)'/><line x1='300' y1='280' x2='210' y2='200' stroke='var(--muted)'/><text x='120' y='90' fill='var(--ink)'>焦点透视（单视点）</text><rect x='420' y='110' width='280' height='180' fill='none' stroke='var(--accent)'/><circle cx='480' cy='200' r='12' fill='none' stroke='var(--muted)'/><circle cx='560' cy='200' r='12' fill='none' stroke='var(--muted)'/><circle cx='640' cy='200' r='12' fill='none' stroke='var(--muted)'/><text x='460' y='90' fill='var(--ink)'>散点透视（多视点）</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"east-west-space-compare": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='60' y='110' width='300' height='180' fill='none' stroke='var(--muted)'/><rect x='120' y='160' width='180' height='80' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='110' y='90' fill='var(--ink)'>留白（以无胜有）</text><rect x='420' y='110' width='280' height='180' fill='none' stroke='var(--accent)'/><circle cx='560' cy='200' r='46' fill='none' stroke='var(--muted)'/><text x='480' y='90' fill='var(--ink)'>负空间（主体之外的底）</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"damp-proofing": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='140' width='480' height='170' fill='none' stroke='var(--line)'/><line x1='140' y1='250' x2='620' y2='250' stroke='var(--accent)' stroke-width='4'/><text x='300' y='230' fill='var(--ink)'>防潮层</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"safety-guarding": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='80' y1='260' x2='680' y2='260' stroke='var(--ink)' stroke-width='2'/><line x1='300' y1='260' x2='300' y2='170' stroke='var(--accent)' stroke-width='4'/><line x1='300' y1='170' x2='460' y2='170' stroke='var(--accent)' stroke-width='4'/><line x1='300' y1='220' x2='460' y2='220' stroke='var(--muted)' stroke-width='2'/><text x='320' y='140' fill='var(--ink)'>临空护栏与照明</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"sustainable-architecture": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='140' width='280' height='170' fill='none' stroke='var(--accent)'/><circle cx='560' cy='170' r='40' fill='none' stroke='var(--muted)'/><path d='M 540 260 Q 560 300 580 260' fill='none' stroke='var(--muted)'/><text x='150' y='110' fill='var(--ink)'>全生命周期与被动优先</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"vitruvian-triad": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><polygon points='380,80 560,320 200,320' fill='none' stroke='var(--accent)' stroke-width='2'/><text x='360' y='140' fill='var(--ink)'>坚固</text><text x='220' y='300' fill='var(--ink)'>实用</text><text x='500' y='300' fill='var(--ink)'>美观</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"sunken-accessibility": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='60' y1='150' x2='700' y2='150' stroke='var(--ink)' stroke-width='2'/><polyline points='200,150 360,300 560,300' fill='none' stroke='var(--accent)' stroke-width='3'/><text x='380' y='330' fill='var(--ink)'>缓坡代替台阶</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"east-west-perspective-compare": {
 "原理":"散点透视随视点移动组织长卷，焦点透视固定视点汇聚于灭点，二者服务不同的观看方式。",
 "典型手法与适用条件":"东方长卷用散点连续展开，西方透视用于单点凝视的深度；比较时应看观者与画面的关系。",
 "实例":"名称：中国长卷与西方焦点透视绘画的对照（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"把散点透视简单说成“错误透视”是误解；两种体系各有其空间逻辑。" + REG,
 "一图":"见下方对照：单视点与多视点。",
 "待核实":"具体对照作品的作者与年代待核实。",
},
"east-west-space-compare": {
 "原理":"留白以“无”参与意境，负空间以“底”塑造图形；两者都运用空白，但文化意图与读法不同。",
 "典型手法与适用条件":"东方留白重气韵与想象，西方负空间重图底识别；可用于跨文化构图比较。",
 "实例":"名称：水墨留白与平面负空间的对照（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"把留白等同于“没画完”会误读；负空间也非单纯空着。" + REG,
 "一图":"见下方对照：留白与负空间。",
 "待核实":"具体对照案例的出处待核实。",
},
"damp-proofing": {
 "原理":"防潮通过隔汽层、防水层与通风构造，阻止毛细水、冷凝水与地下水侵入室内。",
 "典型手法与适用条件":"地下与近地墙体设防潮层、地面设防潮垫层并组织排水；适用于潮湿气候与下沉空间。",
 "实例":"名称：地下空间防潮构造（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只做防水不做隔汽会导致冷凝；材料搭接与节点须按规范施工。" + REG,
 "一图":"见下方示意：墙体与地面的防潮层。",
 "待核实":"示例构造做法与设计者待核实。",
},
"safety-guarding": {
 "原理":"安全防护以护栏、照明与视线管理降低高差跌坠与死角风险，让人能预见边缘。",
 "典型手法与适用条件":"临空设防护栏杆、边缘加强照明与防滑铺装；适用于下沉空间、挑台与坡道。",
 "实例":"名称：临空处防护栏杆（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"护栏高度不足或有可攀爬空隙会失效；照度与防滑须达标。" + REG,
 "一图":"见下方示意：临空护栏与照明。",
 "待核实":"示例防护做法的参数与设计者待核实。",
},
"sustainable-architecture": {
 "原理":"可持续建筑兼顾生态、社会与经济的长期性，把全生命周期影响纳入设计判断。",
 "典型手法与适用条件":"被动式设计优先、材料循环利用与可再生资源并用；适用于新建与改造项目。",
 "实例":"名称：被动式可持续建筑（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只贴“绿色标签”而无实测支撑；评价须按当地标准核定。" + REG,
 "一图":"见下方示意：全生命周期与被动优先。",
 "待核实":"示例建筑的评价数据与设计者待核实。",
},
"vitruvian-triad": {
 "原理":"维特鲁威三原则把坚固（结构可靠）、实用（功能合用）与美观（比例和谐）并列为建筑的基本要求。",
 "典型手法与适用条件":"设计中同时权衡结构、功能与形式；适用于建筑评价与方案取舍。",
 "实例":"名称：维特鲁威《建筑十书》所述三原则（类型性记载）；地点：古罗马；设计者：不适用；年份：不适用。此处仅列名称、地点、设计者与年份信息，不复制图像。",
 "常见错误与限制":"三者失衡会顾此失彼；三原则是框架而非固定比例公式。" + REG,
 "一图":"见下方示意：坚固—实用—美观三角。",
 "待核实":"《建筑十书》成书年代与译本细节待核实。",
},
"sunken-accessibility": {
 "原理":"下沉空间的无障碍要求让不同行动能力者都能到达并使用，须以坡道、平台与连续扶手替代单纯台阶。",
 "典型手法与适用条件":"设置符合坡度的无障碍坡道与休息平台，避免台阶中断路径；适用于下沉庭院与广场。",
 "实例":"名称：下沉空间无障碍坡道（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只设台阶会中断无障碍路径；坡长坡度与扶手须按规范校核。" + REG,
 "一图":"见下方示意：缓坡代替台阶。",
 "待核实":"示例坡道的坡度参数与设计者待核实。",
},
}

SRC = {
"east-west-perspective-compare":["wp-perspective-graphical","wp-chinese-painting"],
"east-west-space-compare":["wp-chinese-garden","wp-negative-space"],
"damp-proofing":["wp-building-material","wp-sunken-courtyard"],
"safety-guarding":["wp-architecture","wp-exit-sign"],
"sustainable-architecture":["wp-sustainable-architecture","wp-passive-solar-building-design"],
"vitruvian-triad":["wp-architectural-theory","wp-visual-arts"],
"sunken-accessibility":["wp-architecture","wp-exit-sign"],
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
