"""第24轮：收尾 6 条补充 L1→L2（构图类，强去模板化）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"rule-of-space": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='90' width='600' height='220' fill='none' stroke='var(--line)'/><circle cx='230' cy='200' r='26' fill='var(--accent)'/><line x1='256' y1='200' x2='620' y2='200' stroke='var(--muted)" + "' stroke-dasharray='8 6'/><text x='380' y='180' fill='var(--ink)'>主体前方的留白</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"golden-ratio": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='110' width='372' height='230' fill='none' stroke='var(--accent)'/><line x1='492' y1='110' x2='492' y2='340' stroke='var(--muted)'/><text x='150' y='90' fill='var(--ink)'>约 1 : 1.618 的分割</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"diagonal-composition": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='100' y1='320' x2='660' y2='90' stroke='var(--accent)' stroke-width='3'/><circle cx='180' cy='295' r='16' fill='var(--accent-soft)' stroke='var(--accent)'/><circle cx='560' cy='125' r='16' fill='none' stroke='var(--muted)'/><text x='330' y='200' fill='var(--ink)'>对角动势</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"s-curve-composition": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><path d='M 140 330 C 260 300 220 190 380 170 C 540 150 520 90 640 80' fill='none' stroke='var(--accent)' stroke-width='3'/><circle cx='140' cy='330' r='10' fill='var(--accent)'/><text x='330' y='230' fill='var(--ink)'>S 形引导深入</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"triangular-composition": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><polygon points='380,80 620,320 140,320' fill='none' stroke='var(--accent)' stroke-width='2'/><circle cx='380' cy='80' r='14' fill='var(--accent-soft)' stroke='var(--accent)'/><circle cx='140' cy='320' r='14' fill='none' stroke='var(--muted)'/><circle cx='620' cy='320' r='14' fill='none' stroke='var(--muted)'/><text x='340' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"framing-composition": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='80' width='600' height='240' fill='none' stroke='var(--line)'/><rect x='120' y='120' width='120' height='160' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='540' y='120' width='100' height='160' fill='none' stroke='var(--muted)'/><circle cx='390' cy='200' r='60' fill='none' stroke='var(--muted)'/><text x='330' y='60' fill='var(--ink)'>前景围合主体</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"rule-of-space": {
 "原理":"空间法则指在主体视线或运动方向的前方预留更多空白，让动势有去处、画面不憋闷。",
 "典型手法与适用条件":"人物或车船朝一侧运动时，在该侧留大空白、身后留小空白；适用于动态画面。",
 "实例":"名称：动态主体的前向留白（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"主体顶边或被身后空间挤压会显得局促；留白方向须与动势一致。" + REG,
 "一图":"见下方示意：主体趋向前方的空白。",
 "待核实":"示例作品与作者年代待核实。",
},
"golden-ratio": {
 "原理":"黄金比约为 1∶1.618，被用作分割画面与界面以求协调的经验参考，而非硬性规则。",
 "典型手法与适用条件":"按黄金比安排主次区或版面横竖分割；常用于版式与立面划分的参考。",
 "实例":"名称：按黄金比分割的版面（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"机械套用会僵化，且比例美感受直觉与文化影响；不必强求精确数值。" + REG,
 "一图":"见下方示意：约 1∶1.618 的分割。",
 "待核实":"示例版式与作者年代待核实。",
},
"diagonal-composition": {
 "原理":"对角线构图让主体沿画面斜向展开，制造比水平线更强的运动感与方向冲突。",
 "典型手法与适用条件":"人物、道路或光影沿对角线布置；适用于表现动势、冲突与纵深。",
 "实例":"名称：沿对角展开的动态场景（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"对角线过多会造成画面不稳；需以次要元素平衡。" + REG,
 "一图":"见下方示意：对角动势。",
 "待核实":"示例作品与作者年代待核实。",
},
"s-curve-composition": {
 "原理":"S 形构图以蜿蜒曲线引导视线由近及远深入画面，延长观看路径、增添柔美与纵深。",
 "典型手法与适用条件":"河流、道路、人体曲线呈 S 形展开；适用于风景与柔和的动态。",
 "实例":"名称：S 形河流的纵深构图（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"S 形过于对称会呆板；曲线断裂会打断引导。" + REG,
 "一图":"见下方示意：S 形曲线引向远处。",
 "待核实":"示例作品与作者年代待核实。",
},
"triangular-composition": {
 "原理":"三角形构图以三个视觉支点构成稳定骨架，底宽提供稳重、尖端形成指向与张力。",
 "典型手法与适用条件":"三人合影、山景常呈正三角；倒三角则制造不稳定与动感。",
 "实例":"名称：三角构图的群像（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"三角形过扁会丧失张力；顶点偏离会削弱稳定。" + REG,
 "一图":"见下方示意：三角形骨架。",
 "待核实":"示例作品与作者年代待核实。",
},
"framing-composition": {
 "原理":"框架式构图用前景元素（门窗、枝叶、拱券）围合主体，形成“画中画”、增强纵深与聚焦。",
 "典型手法与适用条件":"以门洞、窗框或拱券框住远景主体；适用于建筑摄影与园林取景。",
 "实例":"名称：门窗取景的框架构图（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"前景过重会喧宾夺主；框架与主体比例失衡会削弱画面。" + REG,
 "一图":"见下方示意：前景围合主体。",
 "待核实":"示例作品与作者年代待核实。",
},
}

SRC = {
"rule-of-space":["wp-composition-visual-arts","wp-leading-line"],
"golden-ratio":["wp-golden-ratio","wp-golden-rectangle"],
"diagonal-composition":["wp-composition-visual-arts","wp-leading-line"],
"s-curve-composition":["wp-composition-visual-arts","wp-leading-line"],
"triangular-composition":["wp-composition-visual-arts","wp-symmetry"],
"framing-composition":["wp-composition-visual-arts","wp-chinese-garden"],
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
