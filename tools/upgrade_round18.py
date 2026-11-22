"""第18轮：跨主题升级 6 个 L1→L2（混合重要/补充，去模板化）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"simplification": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='100' y='120' width='240' height='160' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='420' y='180' width='120' height='80' fill='none' stroke='var(--muted)'/><text x='150' y='100' fill='var(--ink)'>繁复</text><text x='440' y='160' fill='var(--ink)'>简化后</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"hierarchy": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='150' y='110' width='220' height='70' fill='var(--accent)'/><rect x='400' y='150' width='150' height='50' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='400' y='220' width='120' height='40' fill='none' stroke='var(--muted)'/><text x='170' y='100' fill='var(--ink)'>主</text><text x='470' y='180' fill='var(--ink)'>次</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"color-contrast": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='130' width='200' height='120' fill='var(--ink)'/><rect x='420' y='130' width='200' height='120' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='200' y='110' fill='var(--ink)'>高明度对比</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"framed-scenery": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='90' width='520' height='240' fill='none' stroke='var(--line)'/><rect x='300' y='140' width='160' height='140' fill='none' stroke='var(--accent)' stroke-width='3'/><circle cx='380' cy='210' r='34' fill='var(--accent-soft)' stroke='var(--muted)'/><text x='330' y='120' fill='var(--ink)'>洞口成画框</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"pedestrian-flow": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='90' width='600' height='230' fill='none' stroke='var(--line)'/><polyline points='120,300 260,240 380,260 520,180 640,200' fill='none' stroke='var(--accent)' stroke-width='3'/><circle cx='380' cy='260' r='12' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='300' y='130' fill='var(--ink)'>步行路径与停留点</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"material-texture": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='120' width='160' height='170' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='320' y='120' width='160' height='170' fill='var(--panel)' stroke='var(--line)'/><rect x='520' y='120' width='120' height='170' fill='none' stroke='var(--muted)' stroke-dasharray='6 4'/><text x='160' y='100' fill='var(--ink)'>粗糙</text><text x='360' y='100' fill='var(--ink)'>光滑</text><text x='540' y='100' fill='var(--ink)'>透明</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"simplification": {
 "原理":"简化是删去次要信息、保留结构要点的手法，它让主体更易被识别而不是让画面变空。",
 "典型手法与适用条件":"合并相近色块、压缩多余细节；适用于信息密集的画面与界面。",
 "实例":"名称：繁复场景的简化处理（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"过度简化会丢失必要信息；简化不等于省略功能。" + REG,
 "一图":"见下方示意：繁复到简化的取舍。",
 "待核实":"示例作品与作者年代待核实。",
},
"hierarchy": {
 "原理":"层级通过大小、位置、明度与色彩的差异，建立“先看什么、后看什么”的次序。",
 "典型手法与适用条件":"用对比把主信息推到最前、次信息退后；适用于海报、页面与展陈。",
 "实例":"名称：海报主次层级（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"层级过多会相互打架；全靠放大易致杂乱。" + REG,
 "一图":"见下方示意：主、次、辅三级。",
 "待核实":"示例海报的设计者与年代待核实。",
},
"color-contrast": {
 "原理":"色彩对比来自明度、色相与纯度的差异，对比度决定可读性与视觉冲击。",
 "典型手法与适用条件":"文字与背景保足明度差、重点用对比色提亮；须满足无障碍对比要求。",
 "实例":"名称：图文高对比排版（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"低对比在弱光下难以辨认；大面积极端对比易刺眼。" + REG,
 "一图":"见下方示意：高明度差的文字与底色。",
 "待核实":"示例版式的出处待核实。",
},
"framed-scenery": {
 "原理":"框景用门洞、窗框或枝干把连续风景裁成一幅画，强化焦点与层次。",
 "典型手法与适用条件":"在游线上设置取景洞口，控制画幅比例与对景内容；适用于园林与取景式建筑。",
 "实例":"名称：园林门洞取景（类型性描述）；地点：中国苏州；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"框洞过多会使视线碎片化；画幅比例失当会削弱画面感。" + REG,
 "一图":"见下方示意：洞口把景物框成画面。",
 "待核实":"框景手法的独立专门来源与具体实例设计者、年代待核实。",
},
"pedestrian-flow": {
 "原理":"步行流线以人的通行与停留组织空间，关注安全、舒适与节点停顿，而非单纯通行效率。",
 "典型手法与适用条件":"区分快行与慢行、设置停留节点；适用于街道、广场与商业空间。",
 "实例":"名称：商业步行街流线（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"人车混行与断头路会降低体验与安全；无障碍与铺装须达标。" + REG,
 "一图":"见下方示意：步行路径与停留点。",
 "待核实":"示例街道的设计者与年代待核实。",
},
"material-texture": {
 "原理":"材料质感通过粗糙、光滑、透明与吸光等表面属性，影响光线反射、触感与空间心理温度。",
 "典型手法与适用条件":"以质感对比划分界面、以天然材质传递温暖；适用于室内外界面设计。",
 "实例":"名称：质感对比的室内界面（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只看效果图会低估维护与清洁成本；防滑与防火须按规范校核。" + REG,
 "一图":"见下方示意：粗糙、光滑与透明三种质感。",
 "待核实":"示例空间的设计者与年代待核实。",
},
}

SRC = {
"simplification":["wp-composition-visual-arts","wp-negative-space"],
"hierarchy":["wp-composition-visual-arts","wp-visual-hierarchy"],
"color-contrast":["wp-color-theory","wp-complementary-colors"],
"framed-scenery":["wp-chinese-garden"],
"pedestrian-flow":["wp-wayfinding","wp-plaza"],
"material-texture":["wp-building-material","wp-vernacular-architecture"],
}

def main():
    n=0
    for path in sorted((ROOT/"entries").glob("*.json")):
        doc=json.loads(path.read_text(encoding="utf-8")); ch=False
        for e in doc.get("entries",[]):
            k=e["id"]
            if k not in S: continue
            e["level"]="L2"; e["sections"]=S[k]; e["svg"]=[SVG[k]]; e["sources"]=SRC[k]
            if k=="framed-scenery":
                e["needs_verification"]=True; e["pending_notes"]="框景的独立专门来源与具体实例设计者、年代待核实。"
            else:
                e["needs_verification"]=True; e["pending_notes"]="实例的具体名称、设计者与年代待补充独立来源。"
            n+=1; ch=True
        if ch: path.write_text(json.dumps(doc,ensure_ascii=False,indent=2),encoding="utf-8")
    print("upgraded",n)

if __name__=="__main__": main()
