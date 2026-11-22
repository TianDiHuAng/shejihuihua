"""第14轮：用现有已核验来源把 6 个重要理论 L1 升级为 L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"two-point-perspective": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='100' width='240' height='200' fill='none' stroke='var(--accent)'/><line x1='360' y1='140' x2='640' y2='180' stroke='var(--muted)'/><line x1='360' y1='260' x2='640' y2='220' stroke='var(--muted)'/><line x1='120' y1='140' x2='60' y2='180' stroke='var(--muted)'/><line x1='120' y1='260' x2='60' y2='220' stroke='var(--muted)'/><circle cx='640' cy='200' r='6' fill='var(--accent)'/><circle cx='60' cy='200' r='6' fill='var(--accent)'/><text x='600' y='185' fill='var(--ink)'>灭点R</text><text x='20' y='185' fill='var(--ink)'>灭点L</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"three-point-perspective": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><polygon points='300,120 460,120 460,280 300,280' fill='none' stroke='var(--accent)'/><line x1='300' y1='120' x2='380' y2='60' stroke='var(--muted)'/><line x1='460' y1='120' x2='380' y2='60' stroke='var(--muted)'/><line x1='300' y1='280' x2='220' y2='340' stroke='var(--muted)'/><line x1='460' y1='280' x2='540' y2='340' stroke='var(--muted)'/><circle cx='380' cy='60' r='6' fill='var(--accent)'/><circle cx='380' cy='345' r='6' fill='var(--accent)'/><text x='330' y='45' fill='var(--ink)'>上灭点</text><text x='330' y='380' fill='var(--muted)'>示意图，非施工图</text></svg>",
"aerial-perspective": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='60' y='270' width='640' height='70' fill='var(--accent-soft)' stroke='var(--line)'/><polyline points='80,260 220,190 360,230 520,150 700,210' fill='none' stroke='var(--muted)' stroke-width='2'/><text x='160' y='120' fill='var(--ink)'>远景对比降低、偏冷灰</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"foreshortening": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><ellipse cx='380' cy='200' rx='180' ry='60' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='200' y1='200' x2='560' y2='200' stroke='var(--muted)'/><text x='300' y='140' fill='var(--ink)'>正对视线缩短</text><text x='300' y='390' fill='var(--muted)'>示意图，非施工图</text></svg>",
"vanishing-point": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='60' y1='120' x2='500' y2='200' stroke='var(--muted)'/><line x1='60' y1='280' x2='500' y2='200' stroke='var(--muted)'/><line x1='660' y1='120' x2='500' y2='200' stroke='var(--muted)'/><line x1='660' y1='280' x2='500' y2='200' stroke='var(--muted)'/><circle cx='500' cy='200' r='8' fill='var(--accent)'/><text x='515' y='195' fill='var(--ink)'>灭点</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"horizon-line": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='60' y1='200' x2='700' y2='200' stroke='var(--accent)' stroke-width='2'/><polygon points='80,330 260,330 170,210' fill='var(--accent-soft)' stroke='var(--muted)'/><circle cx='520' cy='250' r='30' fill='none' stroke='var(--muted)'/><text x='90' y='188' fill='var(--ink)'>视平线</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"two-point-perspective": {
 "原理":"两点透视让两组水平平行线分别汇聚到左右两个灭点，用于表现建筑转角与斜向观察的体块。",
 "典型手法与适用条件":"以两个灭点确定转角立面，垂直线保持竖直；适用于斜看的立方体与街角建筑。",
 "实例":"名称：建筑转角透视（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"两灭点过近会造成剧烈变形；视距与画面尺寸影响观感。" + REG,
 "一图":"见下方示意：左右两个灭点。",
 "待核实":"具体作品的设计者与年代待核实。",
},
"three-point-perspective": {
 "原理":"三点透视在两点透视基础上加入垂直方向灭点，表现仰视或俯视的强烈透视。",
 "典型手法与适用条件":"用于仰视高层或俯视深井式空间；垂直线随视角收敛。",
 "实例":"名称：高层仰视透视（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"垂直灭点使用不当会造成倾斜失真；画面尺寸影响透视强度。" + REG,
 "一图":"见下方示意：垂直线向上灭点收敛。",
 "待核实":"具体作品的设计者与年代待核实。",
},
"aerial-perspective": {
 "原理":"空气透视利用远处物象对比降低、明度提高并偏冷灰的现象表达深度。",
 "典型手法与适用条件":"以远近色彩与清晰度差异补充线性透视；适用于风景与远景。",
 "实例":"名称：风景画空气透视（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"把远景一律处理成灰雾会丢失材质；空气条件随天气变化。" + REG,
 "一图":"见下方示意：远景对比降低、偏冷灰。",
 "待核实":"具体作品的设计者与年代待核实。",
},
"foreshortening": {
 "原理":"缩短法指物体朝向观察者时视觉长度缩短，是透视在三维形体上的体现。",
 "典型手法与适用条件":"处理朝向镜头的肢体与器皿时按透视压缩比例；适用于人物与静物。",
 "实例":"名称：人物缩短法（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"压缩比例失真会造成形体扭曲；需与整体透视一致。" + REG,
 "一图":"见下方示意：正对视线的体块缩短。",
 "待核实":"具体作品的设计者与年代待核实。",
},
"vanishing-point": {
 "原理":"灭点是画面中相互平行的深远线汇聚的假想点，决定观看方向与空间稳定。",
 "典型手法与适用条件":"以灭点统一同组平行线；适用于画面透视控制。",
 "实例":"名称：透视灭点作图（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"多个不一致灭点造成空间矛盾；灭点位置影响画面张力。" + REG,
 "一图":"见下方示意：平行线汇聚的灭点。",
 "待核实":"具体作品的设计者与年代待核实。",
},
"horizon-line": {
 "原理":"视平线与观察者眼睛等高，在画面中表现为水平基准线，统一管理各组平行线。",
 "典型手法与适用条件":"先定视平线再定人物与建筑高度关系；适用于场景构图。",
 "实例":"名称：场景视平线控制（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"视平线位置与视高不一致会造成比例错乱；画面尺寸影响观感。" + REG,
 "一图":"见下方示意：视平线与其上下物象。",
 "待核实":"具体作品的设计者与年代待核实。",
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
            e["needs_verification"]=True; e["pending_notes"]="实例的具体名称、设计者与年代待补充独立来源。"
            n+=1; ch=True
        if ch: path.write_text(json.dumps(doc,ensure_ascii=False,indent=2),encoding="utf-8")
    print("upgraded",n)

if __name__=="__main__": main()
