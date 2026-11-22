"""第15轮：跨主题升级 6 个重要 L1→L2（去模板化，避免相似度超阈）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"saturation": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='90' y='150' width='120' height='100' fill='var(--accent)'/><rect x='230' y='150' width='120' height='100' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='370' y='150' width='120' height='100' fill='var(--panel)' stroke='var(--line)'/><text x='150' y='120' fill='var(--ink)'>高纯度→低纯度</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"primary-colors": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='300' cy='190' r='70' fill='none' stroke='var(--accent)'/><circle cx='430' cy='190' r='70' fill='none' stroke='var(--muted)'/><circle cx='365' cy='300' r='70' fill='none' stroke='var(--muted)'/><text x='330' y='60' fill='var(--ink)'>三原色交叠</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
"warm-cool": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='150' width='280' height='100' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='400' y='150' width='280' height='100' fill='none' stroke='var(--muted)'/><text x='150' y='130' fill='var(--ink)'>暖色区</text><text x='470' y='130' fill='var(--ink)'>冷色区</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"hardscape-softscape": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='220' width='600' height='110' fill='var(--accent-soft)' stroke='var(--line)'/><circle cx='200' cy='180' r='40' fill='none' stroke='var(--accent)'/><circle cx='300' cy='160' r='28' fill='none' stroke='var(--accent)'/><text x='120' y='300' fill='var(--ink)'>铺装（硬）</text><text x='500' y='140' fill='var(--ink)'>植物（软）</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"wayfinding": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='80' width='600' height='240' fill='none' stroke='var(--line)'/><line x1='140' y1='300' x2='420' y2='300' stroke='var(--accent)' stroke-width='3'/><circle cx='420' cy='300' r='14' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='480' y='120' width='120' height='56' fill='var(--panel)' stroke='var(--muted)'/><text x='495' y='155' fill='var(--ink)'>指示牌</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"mannerism": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='200' width='480' height='120' fill='var(--accent-soft)' stroke='var(--accent)'/><path d='M 200 200 Q 230 120 260 200' fill='none' stroke='var(--muted)'/><path d='M 300 200 Q 340 110 380 200' fill='none' stroke='var(--muted)'/><path d='M 440 200 Q 490 100 540 200' fill='none' stroke='var(--muted)'/><text x='250' y='80' fill='var(--ink)'>刻意拉长与变形</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"saturation": {
 "原理":"纯度指色彩的鲜艳或灰浊程度；同一色相提高纯度会更抢眼，降低纯度则趋于安静沉稳。",
 "典型手法与适用条件":"主体用高纯度色、背景用低纯度色以拉开层次；室内大面积宜控纯度以免疲劳。",
 "实例":"名称：高纯度点缀与低纯度背景的配色（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"整面高纯度色久看易生视觉疲劳；纯度差异过小则主体难凸显。" + REG,
 "一图":"见下方示意：由高纯度到低纯度的推移。",
 "待核实":"所举配色案例的设计者与年代待核实。",
},
"primary-colors": {
 "原理":"原色是不能再由其他色混合得到、却能调配出其他色彩的基础色集合；光的三原色与颜料三原色并不相同。",
 "典型手法与适用条件":"调色与显示器分属加色与减色体系，选色前须先确认媒介。",
 "实例":"名称：加色与减色三原色对照（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"把屏幕三原色直接当作颜料配方会偏色；印刷还需考虑色域限制。" + REG,
 "一图":"见下方示意：三原色交叠区。",
 "待核实":"示例所用色卡的出处待核实。",
},
"warm-cool": {
 "原理":"人对色彩有冷暖的心理倾向：红橙偏暖、蓝青偏冷，可用于暗示光照与空间远近。",
 "典型手法与适用条件":"暖色前移、冷色后退，可用于强化纵深；也可调节室内情绪。",
 "实例":"名称：冷暖对比制造空间层次（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"冷暖判断受周围色影响而漂移；跨文化联想存在差异。" + REG,
 "一图":"见下方示意：暖色区与冷色区并置。",
 "待核实":"所举案例的设计者与年代待核实。",
},
"hardscape-softscape": {
 "原理":"景观要素可分为硬质（铺装、构筑）与软质（植物、水体）两类，其配比决定空间性格与维护方式。",
 "典型手法与适用条件":"广场以硬质承载活动、以软质柔化边界；居住区提高软质比例改善微气候。",
 "实例":"名称：城市广场硬软质配比（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"硬质过多夏季蓄热、软质过多则通行与维护成本上升；无障碍铺装须达标。" + REG,
 "一图":"见下方示意：铺装与绿化的搭配。",
 "待核实":"所举广场实例的设计者与年代待核实。",
},
"wayfinding": {
 "原理":"寻路是人在空间中依靠标识、地图与空间线索确定方位并抵达目标的过程。",
 "典型手法与适用条件":"以分级标识、连续视觉线索与节点地标支撑寻路；大型公共建筑尤需系统化导视。",
 "实例":"名称：大型文化建筑导视系统（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"标识层级混乱或信息过载会加重迷路；夜间与无障碍指引须单独考虑。" + REG,
 "一图":"见下方示意：路径、节点与指示牌。",
 "待核实":"所引导视系统的设计者与年代待核实。",
},
"mannerism": {
 "原理":"样式主义在文艺复兴的规则之内故意拉长比例、扭转姿态，以显示技巧与张力。",
 "典型手法与适用条件":"以夸张人体、非对称构图与异常色彩制造不安感；多见于晚期文艺复兴绘画与建筑细部。",
 "实例":"名称：样式主义绘画与建筑细部（类型性描述）；地点：欧洲；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"过度变形会流于做作、削弱可读性；判断其价值需结合当时的赞助与审美语境。" + REG,
 "一图":"见下方示意：刻意拉长与变形的形体。",
 "待核实":"具体作品的设计者与年代待核实。",
},
}

SRC = {
"saturation":["wp-colorfulness","wp-munsell-color-system"],
"primary-colors":["wp-primary-color","wp-color-wheel"],
"warm-cool":["wp-color-theory","wp-theory-of-colours"],
"hardscape-softscape":["wp-landscape-architecture","wp-landscape-design"],
"wayfinding":["wp-graphic-design","wp-wayfinding"],
"mannerism":["wp-mannerism","wp-list-architectural-styles"],
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
