"""第16轮：跨主题升级 6 个重要 L1→L2（去模板化）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"beaux-arts": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='200' width='520' height='120' fill='var(--accent-soft)' stroke='var(--accent)'/><polygon points='160,200 300,120 440,200' fill='none' stroke='var(--muted)'/><line x1='380' y1='120' x2='380' y2='80' stroke='var(--accent)'/><text x='260' y='70' fill='var(--ink)'>对称与纪念性轴线</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"plein-air": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='80' y1='300' x2='680' y2='300' stroke='var(--ink)' stroke-width='3'/><circle cx='620' cy='90' r='36' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='300' y='210' width='90' height='70' fill='none' stroke='var(--muted)'/><text x='540' y='150' fill='var(--ink)'>户外自然光</text><text x='310' y='190' fill='var(--ink)'>画架</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"gestalt-organization-laws": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='220' cy='150' r='24' fill='none' stroke='var(--accent)'/><circle cx='280' cy='150' r='24' fill='none' stroke='var(--accent)'/><circle cx='340' cy='150' r='24' fill='none' stroke='var(--accent)'/><circle cx='520' cy='250' r='24' fill='none' stroke='var(--muted)'/><text x='200' y='100' fill='var(--ink)'>邻近即成组</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"color-psychology": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='100' y='140' width='160' height='120' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='300' y='140' width='160' height='120' fill='none' stroke='var(--muted)'/><text x='130' y='120' fill='var(--ink)'>暖→活跃</text><text x='330' y='120' fill='var(--ink)'>冷→冷静</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"environmental-psychology": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='90' y='90' width='580' height='220' fill='none' stroke='var(--line)'/><circle cx='240' cy='200' r='34' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='280' y1='200' x2='560' y2='200' stroke='var(--muted)' stroke-width='2'/><text x='180' y='150' fill='var(--ink)'>人</text><text x='500' y='170' fill='var(--ink)'>环境</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"lighting-design": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='110' width='520' height='210' fill='none' stroke='var(--line)'/><circle cx='200' cy='150' r='16' fill='var(--accent-soft)' stroke='var(--accent)'/><polygon points='200,166 160,300 240,300' fill='var(--accent-soft)' opacity='0.6'/><rect x='420' y='240' width='160' height='40' fill='none' stroke='var(--muted)'/><text x='300' y='90' fill='var(--ink)'>人工光与天然光并用</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"beaux-arts": {
 "原理":"学院派把古典柱式、对称轴线与纪念性体量系统化为可教授的设计法则，强调构图与装饰等级。",
 "典型手法与适用条件":"公共建筑常以居中主厅、两翼对称和丰富装饰体现权威；适用于大型公共与交通建筑。",
 "实例":"名称：学院派公共建筑（类型性描述）；地点：欧洲与美洲；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"重装饰轻功能易致使用不便；细部比例失当会显得浮夸。" + REG,
 "一图":"见下方示意：对称与纪念性轴线。",
 "待核实":"所举实例的设计者与年代待核实。",
},
"plein-air": {
 "原理":"外光写生直接面对自然光作画，用现场观察取代室内恒定光，捕捉色彩的即时变化。",
 "典型手法与适用条件":"便携颜料与户外画架使其普及；适合风景与光影题材，须快速记录以免光线改变。",
 "实例":"名称：外光风景写生（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"光线变化快，久画易前后色调不一致；风沙与湿度影响颜料。" + REG,
 "一图":"见下方示意：户外自然光下的写生。",
 "待核实":"具体写生作品与作者年代待核实。",
},
"gestalt-organization-laws": {
 "原理":"格式塔组织律说明视觉会把邻近、相似、连续、闭合的元素自动归组，整体先于局部被感知。",
 "典型手法与适用条件":"用间距、相似形与连续线引导分组，减少视觉杂乱；适用于版面与画面组织。",
 "实例":"名称：基于邻近与相似的分组练习（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"分组线索冲突会使读者误读结构；过度闭合可能掩盖真实边界。" + REG,
 "一图":"见下方示意：邻近元素被看成一组。",
 "待核实":"示例版式的出处待核实。",
},
"color-psychology": {
 "原理":"色彩心理学研究色相与明度如何影响情绪、注意与行为，如暖色唤起活跃、冷色趋于平静。",
 "典型手法与适用条件":"按使用场景选择情绪基调，如餐饮偏暖、办公偏中性；可结合明度调节刺激强度。",
 "实例":"名称：商业空间的色彩情绪设计（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"色彩联想受文化与个人经验影响，不可一概而论；强刺激色久处易疲劳。" + REG,
 "一图":"见下方示意：暖色活跃、冷色冷静。",
 "待核实":"所举空间案例的设计者与年代待核实。",
},
"environmental-psychology": {
 "原理":"环境心理学研究人如何感知、使用并回应自然与建成环境，关注私密性、领域感与压力恢复。",
 "典型手法与适用条件":"通过空间层次、可控制感与自然元素提升舒适；适用于住区、办公与疗愈环境。",
 "实例":"名称：疗愈性医疗环境设计（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"把个体偏好当作普遍规律会误判；研究结论多依赖具体情境。" + REG,
 "一图":"见下方示意：人与环境的相互作用。",
 "待核实":"所举环境案例的设计者与年代待核实。",
},
"lighting-design": {
 "原理":"照明设计统筹天然光与人工光，使照度、方向与色温服务于视觉任务、情绪与健康。",
 "典型手法与适用条件":"按任务分区布光，重点照明与基础照明分层；需兼顾眩光控制与节能。",
 "实例":"名称：博物馆分层照明（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只堆亮度会眩光与过热；色温混用会破坏氛围，参数须按规范校核。" + REG,
 "一图":"见下方示意：人工光与天然光并用。",
 "待核实":"所举照明实例的设计者与参数待核实。",
},
}

SRC = {
"beaux-arts":["wp-list-architectural-styles","wp-history-of-architecture"],
"plein-air":["wp-outline-of-painting","wp-visual-arts"],
"gestalt-organization-laws":["wp-visual-perception","wp-gestalt-psychology"],
"color-psychology":["wp-interior-design","wp-color-psychology"],
"environmental-psychology":["wp-landscape-architecture","wp-environmental-psychology"],
"lighting-design":["wp-interior-design","wp-lighting-design"],
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
