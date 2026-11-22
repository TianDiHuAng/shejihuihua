"""第12轮：用现有已核验来源把 7 个核心理论 L1 升级为 L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"linear-perspective": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='60' y1='200' x2='700' y2='200' stroke='var(--accent)' stroke-width='2'/><circle cx='380' cy='200' r='6' fill='var(--accent)'/><line x1='120' y1='360' x2='380' y2='200' stroke='var(--muted)'/><line x1='640' y1='360' x2='380' y2='200' stroke='var(--muted)'/><line x1='240' y1='280' x2='380' y2='200' stroke='var(--muted)'/><text x='80' y='188' fill='var(--ink)'>视平线</text><text x='395' y='190' fill='var(--ink)'>灭点</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"scattered-perspective": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='40' y='80' width='680' height='240' fill='none' stroke='var(--line)'/><circle cx='180' cy='200' r='40' fill='none' stroke='var(--accent)'/><circle cx='380' cy='200' r='40' fill='none' stroke='var(--accent)'/><circle cx='580' cy='200' r='40' fill='none' stroke='var(--accent)'/><line x1='220' y1='200' x2='340' y2='200' stroke='var(--muted)'/><line x1='420' y1='200' x2='540' y2='200' stroke='var(--muted)'/><text x='150' y='120' fill='var(--ink)'>视点1</text><text x='350' y='120' fill='var(--ink)'>视点2</text><text x='550' y='120' fill='var(--ink)'>视点3</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"composition": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='60' y='60' width='640' height='280' fill='none' stroke='var(--line)'/><line x1='273' y1='60' x2='273' y2='340' stroke='var(--muted)'/><line x1='486' y1='60' x2='486' y2='340' stroke='var(--muted)'/><line x1='60' y1='153' x2='700' y2='153' stroke='var(--muted)'/><line x1='60' y1='246' x2='700' y2='246' stroke='var(--muted)'/><circle cx='273' cy='153' r='14' fill='var(--accent)'/><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"balance": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='380' y1='80' x2='380' y2='320' stroke='var(--accent)' stroke-width='2'/><rect x='160' y='150' width='150' height='90' fill='var(--accent-soft)' stroke='var(--accent)'/><circle cx='560' cy='195' r='45' fill='none' stroke='var(--muted)'/><text x='190' y='130' fill='var(--ink)'>大暗块</text><text x='520' y='130' fill='var(--ink)'>小亮点</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"proportion": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='90' width='520' height='220' fill='none' stroke='var(--accent)'/><line x1='442' y1='90' x2='442' y2='310' stroke='var(--accent)' stroke-width='2'/><text x='200' y='215' fill='var(--ink)'>整体</text><text x='500' y='215' fill='var(--ink)'>|部分</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"color-theory": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='380' cy='200' r='120' fill='none' stroke='var(--accent)' stroke-width='2'/><circle cx='380' cy='80' r='26' fill='var(--accent-soft)' stroke='var(--muted)'/><circle cx='500' cy='260' r='26' fill='none' stroke='var(--muted)'/><circle cx='260' cy='260' r='26' fill='none' stroke='var(--muted)'/><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"value": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='140' width='90' height='120' fill='var(--ink)'/><rect x='250' y='140' width='90' height='120' fill='var(--muted)'/><rect x='360' y='140' width='90' height='120' fill='var(--accent-soft)'/><rect x='470' y='140' width='90' height='120' fill='var(--panel)' stroke='var(--line)'/><text x='200' y='110' fill='var(--ink)'>明度梯度</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"linear-perspective": {
 "原理":"线性透视把观察者视点固定，使相互平行的深远线条向灭点汇聚，按近大远小建立空间秩序。",
 "典型手法与适用条件":"先定视平线与主灭点，再让同组平行线指向同一灭点；适用于正对观察面的室内与街景。",
 "实例":"名称：文艺复兴线性透视绘画（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"多个不一致灭点会造成空间矛盾；画面尺寸与观看距离影响透视观感。" + REG,
 "一图":"见下方示意：视平线与单一灭点。",
 "待核实":"具体作品的设计者与年代待核实。",
},
"scattered-perspective": {
 "原理":"散点透视让视点随观看移动，把不同视点下的景物组织进同一长幅画面。",
 "典型手法与适用条件":"适用于手卷、长卷等需要连续展开的题材；以段落衔接保持空间连续。",
 "实例":"名称：中国传统长卷山水（类型性描述）；地点：中国；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"视点切换过密会造成观感混乱；装裱与展示方式影响阅读顺序。" + REG,
 "一图":"见下方示意：多个视点在长幅中并列。",
 "待核实":"具体作品的设计者与年代待核实。",
},
"composition": {
 "原理":"构图把元素按位置、比例与关系组织成有序整体，引导观看顺序与信息主次。",
 "典型手法与适用条件":"三分法、主次安排与视觉引导是常用手段；适用于绘画、摄影与界面布局。",
 "实例":"名称：通用构图实践（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"元素过多会削弱重点；构图为视觉秩序而非工程尺寸。" + REG,
 "一图":"见下方示意：三分网格与主体位置。",
 "待核实":"具体案例的设计者与年代待核实。",
},
"balance": {
 "原理":"均衡指各元素在视觉重量上的平衡；可由对称达成，也可由大小、明暗与色差动态平衡。",
 "典型手法与适用条件":"以一大暗块对一小亮点实现非对称均衡；适用于强调张力又需稳定的画面。",
 "实例":"名称：非对称均衡构图（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只追求对称会呆板；失衡会让视线滑出画面。" + REG,
 "一图":"见下方示意：大暗块与小亮点的均衡。",
 "待核实":"具体案例的设计者与年代待核实。",
},
"proportion": {
 "原理":"比例描述部分与整体、部分与部分之间的尺寸关系，影响和谐与尺度感。",
 "典型手法与适用条件":"以简单整数比或黄金比组织界面；适用于立面划分与画面分割。",
 "实例":"名称：古典立面比例（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"比例规则是经验参考而非绝对；实际尺寸与模数须按规范与功能确定。" + REG,
 "一图":"见下方示意：整体与部分之比。",
 "待核实":"具体案例的设计者与年代待核实。",
},
"color-theory": {
 "原理":"色彩理论以色相、明度与纯度的关系解释配色、对比与和谐的规律。",
 "典型手法与适用条件":"以色轮组织邻近色与互补色；适用于绘画、室内与视觉传达。",
 "实例":"名称：色轮配色实践（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只套公式会忽略光照与材质；色彩对比需兼顾可读性与无障碍。" + REG,
 "一图":"见下方示意：色轮上的色彩关系。",
 "待核实":"具体案例的设计者与年代待核实。",
},
"value": {
 "原理":"明度是色彩的明暗程度，明度关系决定画面的结构、可读性与体积感。",
 "典型手法与适用条件":"先以明度块面建立结构，再叠加色相；适用于黑白灰起稿与夜间场景。",
 "实例":"名称：明度块面练习（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只重色相而忽略明度会让画面扁平；明度对比不足影响识别。" + REG,
 "一图":"见下方示意：明度梯度。",
 "待核实":"具体案例的设计者与年代待核实。",
},
}

SRC = {
 "linear-perspective":["wp-perspective-graphical","wp-vanishing-point"],
 "scattered-perspective":["wp-chinese-painting","wp-reverse-perspective"],
 "composition":["wp-composition-visual-arts","wp-rule-of-thirds"],
 "balance":["wp-composition-visual-arts","wp-symmetry"],
 "proportion":["wp-proportion-architecture","wp-golden-ratio"],
 "color-theory":["wp-color-theory","wp-theory-of-colours"],
 "value":["wp-colorfulness","wp-color-theory"],
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
