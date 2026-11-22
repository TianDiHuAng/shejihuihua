"""第13轮：用现有已核验来源把 6 个重要 L1 升级为 L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"one-point-perspective": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='80' width='520' height='240' fill='none' stroke='var(--line)'/><line x1='60' y1='200' x2='700' y2='200' stroke='var(--accent)' stroke-width='2'/><circle cx='380' cy='200' r='6' fill='var(--accent)'/><line x1='120' y1='80' x2='380' y2='200' stroke='var(--muted)'/><line x1='120' y1='320' x2='380' y2='200' stroke='var(--muted)'/><line x1='640' y1='80' x2='380' y2='200' stroke='var(--muted)'/><line x1='640' y1='320' x2='380' y2='200' stroke='var(--muted)'/><text x='80' y='188' fill='var(--ink)'>视平线</text><text x='392' y='192' fill='var(--ink)'>主灭点</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"rule-of-thirds": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='60' y='60' width='640' height='280' fill='none' stroke='var(--line)'/><line x1='273' y1='60' x2='273' y2='340' stroke='var(--muted)'/><line x1='486' y1='60' x2='486' y2='340' stroke='var(--muted)'/><line x1='60' y1='153' x2='700' y2='153' stroke='var(--muted)'/><line x1='60' y1='246' x2='700' y2='246' stroke='var(--muted)'/><circle cx='486' cy='153' r='16' fill='var(--accent)'/><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"figure-ground": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='100' width='600' height='200' fill='var(--accent-soft)' stroke='var(--line)'/><rect x='260' y='140' width='240' height='120' fill='var(--ink)'/><text x='330' y='205' fill='var(--panel)'>图</text><text x='120' y='130' fill='var(--ink)'>底</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"negative-space": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='80' width='600' height='240' fill='none' stroke='var(--line)'/><circle cx='300' cy='200' r='60' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='260' y='200' fill='var(--ink)'>主体</text><text x='450' y='200' fill='var(--muted)'>负空间</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"hue": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='80' y1='200' x2='680' y2='200' stroke='var(--line)'/><rect x='100' y='160' width='120' height='80' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='260' y='160' width='120' height='80' fill='none' stroke='var(--muted)'/><rect x='420' y='160' width='120' height='80' fill='none' stroke='var(--muted)'/><rect x='580' y='160' width='80' height='80' fill='var(--accent)'/><text x='150' y='140' fill='var(--ink)'>色相序列</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"complementary-colors": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='380' cy='200' r='120' fill='none' stroke='var(--line)'/><circle cx='380' cy='80' r='30' fill='var(--accent-soft)' stroke='var(--accent)'/><circle cx='380' cy='320' r='30' fill='none' stroke='var(--accent)'/><line x1='380' y1='110' x2='380' y2='290' stroke='var(--muted)'/><text x='400' y='80' fill='var(--ink)'>色 A</text><text x='400' y='330' fill='var(--ink)'>对侧补色</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"one-point-perspective": {
 "原理":"一点透视把一组平行于视线的线汇聚到画面单一主灭点，正对视线的立面保持不动形。",
 "典型手法与适用条件":"以视平线与主灭点作图，适用于走廊、街景与正对观察者的室内。",
 "实例":"名称：正对式室内透视（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"偏离主灭点会造成正立面变形；画面尺寸影响透视观感。" + REG,
 "一图":"见下方示意：单一主灭点与汇聚线。",
 "待核实":"具体作品的设计者与年代待核实。",
},
"rule-of-thirds": {
 "原理":"三分法把画面横竖各三等分，主体置于交点或分割线上以获得偏离中心的均衡。",
 "典型手法与适用条件":"适用于摄影、绘画与界面布局的主体定位；可与引导线配合。",
 "实例":"名称：三分法摄影构图（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"机械套用会导致构图僵硬；主体位置应结合视线方向调整。" + REG,
 "一图":"见下方示意：三分网格与交点主体。",
 "待核实":"具体案例的设计者与年代待核实。",
},
"figure-ground": {
 "原理":"图底关系区分被注意的主体（图）与背景（底），两者边界与对比决定可读性。",
 "典型手法与适用条件":"以明度对比与轮廓清晰度强化图底分离；适用于平面与界面设计。",
 "实例":"名称：图底对比练习（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"图底对比不足会造成辨认困难；可读性需兼顾无障碍对比度。" + REG,
 "一图":"见下方示意：图与底的分离。",
 "待核实":"具体案例的设计者与年代待核实。",
},
"negative-space": {
 "原理":"负空间是主体之外的空白区域，它塑造主体轮廓并控制画面的呼吸与节奏。",
 "典型手法与适用条件":"保留大面积留白以突出主体；适用于简洁风格与东方构图。",
 "实例":"名称：留白式构图（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"留白过多会显得空洞；留白需与主体比例协调。" + REG,
 "一图":"见下方示意：主体与负空间。",
 "待核实":"具体案例的设计者与年代待核实。",
},
"hue": {
 "原理":"色相是色彩借以区分种类的属性，在色轮上按光谱顺序排列。",
 "典型手法与适用条件":"以邻近色相取得协调、以对比色相建立焦点；适用于配色与主题区分。",
 "实例":"名称：色相环配色（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只看色相忽略明度会降低可读性；色相选择需兼顾色觉差异。" + REG,
 "一图":"见下方示意：色相序列。",
 "待核实":"具体案例的设计者与年代待核实。",
},
"complementary-colors": {
 "原理":"互补色位于色轮相对位置，并置时形成强烈对比，可制造张力与焦点。",
 "典型手法与适用条件":"以互补色小面积点缀建立重点；适用于需要活力的画面与空间。",
 "实例":"名称：互补配色（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"大面积等量互补会刺眼；应调节纯度与面积比例。" + REG,
 "一图":"见下方示意：色轮对侧的互补关系。",
 "待核实":"具体案例的设计者与年代待核实。",
},
}

SRC = {
"one-point-perspective":["wp-perspective-graphical","wp-de-pictura"],
"rule-of-thirds":["wp-rule-of-thirds","wp-composition-visual-arts"],
"figure-ground":["wp-figure-ground","wp-composition-visual-arts"],
"negative-space":["wp-negative-space","wp-composition-visual-arts"],
"hue":["wp-hue","wp-color-theory"],
"complementary-colors":["wp-complementary-colors","wp-color-wheel"],
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
