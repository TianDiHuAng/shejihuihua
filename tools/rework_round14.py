"""第14轮返工：透视六条去模板化，aerial 时段/地区据实修正。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"two-point-perspective": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><polygon points='260,140 480,120 480,260 260,280' fill='none' stroke='var(--accent)'/><line x1='260' y1='140' x2='60' y2='110' stroke='var(--muted)'/><line x1='260' y1='280' x2='60' y2='300' stroke='var(--muted)'/><line x1='480' y1='120' x2='690' y2='90' stroke='var(--muted)'/><line x1='480' y1='260' x2='690' y2='290' stroke='var(--muted)'/><text x='30' y='100' fill='var(--ink)'>左灭点</text><text x='600' y='80' fill='var(--ink)'>右灭点</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"three-point-perspective": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><path d='M 300 300 L 300 120 L 460 100 L 460 270 Z' fill='none' stroke='var(--accent)'/><line x1='300' y1='120' x2='380' y2='40' stroke='var(--muted)'/><line x1='460' y1='100' x2='380' y2='40' stroke='var(--muted)'/><text x='350' y='30' fill='var(--ink)'>垂直灭点</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"aerial-perspective": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='60' y='250' width='640' height='90' fill='var(--accent-soft)'/><polyline points='70,240 200,170 330,215 470,140 620,205 700,180' fill='none' stroke='var(--muted)'/><text x='120' y='110' fill='var(--ink)'>愈远愈淡、愈远愈灰蓝</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"foreshortening": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><path d='M 240 160 Q 380 120 520 160 L 520 240 Q 380 280 240 240 Z' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='240' y1='200' x2='520' y2='200' stroke='var(--muted)'/><text x='280' y='120' fill='var(--ink)'>朝向观者的一侧被压缩</text><text x='300' y='390' fill='var(--muted)'>示意图，非施工图</text></svg>",
"vanishing-point": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='80' y1='90' x2='470' y2='205' stroke='var(--muted)'/><line x1='80' y1='300' x2='470' y2='205' stroke='var(--muted)'/><line x1='690' y1='90' x2='470' y2='205' stroke='var(--muted)'/><line x1='690' y1='300' x2='470' y2='205' stroke='var(--muted)'/><circle cx='470' cy='205' r='9' fill='none' stroke='var(--accent)' stroke-width='2'/><text x='485' y='200' fill='var(--ink)'>所有斜线交于此</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"horizon-line": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='50' y1='215' x2='710' y2='215' stroke='var(--accent)' stroke-dasharray='10 6'/><rect x='150' y='250' width='120' height='110' fill='none' stroke='var(--muted)'/><circle cx='560' cy='270' r='26' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='90' y='203' fill='var(--ink)'>与眼睛齐高的基准线</text><text x='300' y='390' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"two-point-perspective": {
 "原理":"当观察者斜对一个立方体时，两组水平边线各奔一侧，形成左右两个灭点，这就是两点透视。",
 "典型手法与适用条件":"画街角建筑时先定左右灭点，竖直棱线保持垂直；适合表现斜向体块。",
 "实例":"名称：斜视角的街角楼体（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"两灭点靠得太近会使转角夸张到失真；仰头或低头时还会冒出第三个灭点，需另作处理。" + REG,
 "一图":"见下方示意：左右灭点各收一组水平边线。",
 "待核实":"街角建筑实例的建造者与年代待核实。",
},
"three-point-perspective": {
 "原理":"在左右两灭点之外再补一个垂直方向的灭点，画面便获得仰视或俯视的强透视，即三点透视。",
 "典型手法与适用条件":"高层仰拍、深井俯拍时启用；三条棱线分别指向三个灭点。",
 "实例":"名称：仰视摩天楼的透视练习（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"垂直灭点放错会让楼体像要倾倒；视距越短变形越剧烈。" + REG,
 "一图":"见下方示意：竖直棱线收向顶部灭点。",
 "待核实":"练习所参照建筑的名称与年代待核实。",
},
"aerial-perspective": {
 "原理":"空气层散射使远处景物对比减弱、颜色转淡转蓝，画家借此制造纵深，称为空气透视。",
 "典型手法与适用条件":"画远山远树时逐层降低对比、提亮并偏冷；可与线性透视叠用。",
 "实例":"名称：庞贝壁画与早期山水中的远景处理（类型性记载）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"不顾天气一味加灰雾，会让远景失去层次；雾霾与晴日的空气效果差别很大。" + REG,
 "一图":"见下方示意：愈远愈淡、愈远愈偏灰蓝。",
 "待核实":"具体作品的作者与年代待核实；空气透视的早期实例跨度较广。",
},
"foreshortening": {
 "原理":"形体正面朝向观者时，它在画面上的长度会被压缩，这种透视现象叫缩短法。",
 "典型手法与适用条件":"画伸向镜头的手臂、指向观者的器物时要按比例压缩，否则显得僵硬。",
 "实例":"名称：人物手臂前伸的短缩处理（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"压缩过头会让四肢比例怪诞；须与全身透视关系协调。" + REG,
 "一图":"见下方示意：朝向观者的一侧被压扁。",
 "待核实":"范例作品及其作者、年代待核实。",
},
"vanishing-point": {
 "原理":"一组彼此平行的纵深线，在画面上会交于同一假想点，这个点即灭点。",
 "典型手法与适用条件":"作透视线稿时先钉住灭点，再让同向线束归拢；灭点决定画面的观看方向。",
 "实例":"名称：透视草图的灭点定位（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"若同向线束各自乱跑、出现多个灭点，空间立刻矛盾；灭点出画时要延长辅助线。" + REG,
 "一图":"见下方示意：四组斜线交于一点。",
 "待核实":"示范草图的作者与出处待核实。",
},
"horizon-line": {
 "原理":"视平线就是观者眼睛所在的水平高度在画面上的投影，它统领上下所有物象的高低关系。",
 "典型手法与适用条件":"构图先定视平线，再据此安排人物头顶与建筑檐口的高度；视平线高低可强化压迫或开阔感。",
 "实例":"名称：场景构图中的视平线设定（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"视平线与实际视高脱节，会使人物与建筑比例错位；贴地或极高的视平线会扭曲空间。" + REG,
 "一图":"见下方示意：与眼睛齐高的虚线基准。",
 "待核实":"示例场景的出处与年代待核实。",
},
}

SRC = {
"two-point-perspective":["wp-perspective-graphical","wp-alberti"],
"three-point-perspective":["wp-perspective-graphical","wp-curvilinear-perspective"],
"aerial-perspective":["wp-aerial-perspective","wp-perspective-graphical"],
"foreshortening":["wp-perspective-graphical","wp-leonardo-da-vinci"],
"vanishing-point":["wp-vanishing-point","wp-perspective-graphical"],
"horizon-line":["wp-perspective-graphical","wp-vanishing-point"],
}

def main():
    n=0
    for path in sorted((ROOT/"entries").glob("*.json")):
        doc=json.loads(path.read_text(encoding="utf-8")); ch=False
        for e in doc.get("entries",[]):
            k=e["id"]
            if k not in S: continue
            e["level"]="L2"; e["sections"]=S[k]; e["svg"]=[SVG[k]]; e["sources"]=SRC[k]
            e["needs_verification"]=True
            e["pending_notes"]={"aerial-perspective":"实例的作者与年代待核实；空气透视早期实例跨度广，正文只作一般性说明。"}.get(k,"实例的具体名称、设计者与年代待补充独立来源。")
            n+=1; ch=True
        if ch: path.write_text(json.dumps(doc,ensure_ascii=False,indent=2),encoding="utf-8")
    print("reworked",n)

if __name__=="__main__": main()
