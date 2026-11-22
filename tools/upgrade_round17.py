"""第17轮：升级 6 个重要 L1 + sunken-plaza(L2)，去模板化。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"placemaking": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='220' width='600' height='110' fill='var(--accent-soft)' stroke='var(--line)'/><circle cx='200' cy='180' r='26' fill='none' stroke='var(--accent)'/><circle cx='300' cy='180' r='26' fill='none' stroke='var(--accent)'/><circle cx='400' cy='180' r='26' fill='none' stroke='var(--accent)'/><text x='150' y='130' fill='var(--ink)'>居民活动</text><text x='500' y='260' fill='var(--ink)'>公共空间</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"space-syntax": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='140' y1='200' x2='340' y2='140' stroke='var(--accent)' stroke-width='2'/><line x1='140' y1='200' x2='340' y2='260' stroke='var(--accent)' stroke-width='2'/><line x1='340' y1='140' x2='560' y2='200' stroke='var(--muted)'/><line x1='340' y1='260' x2='560' y2='200' stroke='var(--muted)'/><circle cx='140' cy='200' r='12' fill='var(--accent)'/><circle cx='340' cy='200' r='12' fill='var(--accent-soft)' stroke='var(--accent)'/><circle cx='560' cy='200' r='12' fill='var(--muted)'/><text x='120' y='150' fill='var(--ink)'>拓扑连接</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"pattern-language": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='140' width='120' height='100' fill='none' stroke='var(--accent)'/><rect x='320' y='110' width='120' height='100' fill='none' stroke='var(--muted)'/><rect x='520' y='160' width='120' height='100' fill='none' stroke='var(--muted)'/><text x='150' y='120' fill='var(--ink)'>模式 A</text><text x='350' y='90' fill='var(--ink)'>模式 B</text><text x='550' y='140' fill='var(--ink)'>组合</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"biophilic-design": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='100' y='90' width='560' height='220' fill='none' stroke='var(--line)'/><circle cx='220' cy='200' r='30' fill='none' stroke='var(--accent)'/><rect x='320' y='170' width='80' height='60' fill='var(--accent-soft)' stroke='var(--muted)'/><line x1='470' y1='140' x2='470' y2='260' stroke='var(--muted)'/><text x='180' y='150' fill='var(--ink)'>植物</text><text x='440' y='120' fill='var(--ink)'>自然光与材料</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"defensible-space-theory": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='100' y='100' width='560' height='210' fill='none' stroke='var(--line)'/><rect x='140' y='140' width='140' height='140' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='480' y='140' width='140' height='140' fill='none' stroke='var(--muted)'/><circle cx='380' cy='210' r='16' fill='none' stroke='var(--accent)'/><text x='160' y='120' fill='var(--ink)'>领域</text><text x='500' y='120' fill='var(--ink)'>自然监视</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"functionalism-architecture": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='130' width='460' height='190' fill='none' stroke='var(--accent)'/><rect x='180' y='170' width='110' height='150' fill='var(--accent-soft)' stroke='var(--muted)'/><rect x='330' y='170' width='110' height='150' fill='none' stroke='var(--muted)'/><text x='200' y='105' fill='var(--ink)'>形式服务功能</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"sunken-plaza": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='60' y1='150' x2='700' y2='150' stroke='var(--ink)' stroke-width='3'/><polyline points='60,150 220,150 220,300 540,300 540,150 700,150' fill='none' stroke='var(--muted)' stroke-width='2'/><rect x='260' y='200' width='240' height='100' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='300' y='140' fill='var(--ink)'>城市地面</text><text x='320' y='255' fill='var(--ink)'>下沉广场</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"placemaking": {
 "原理":"场所营造以使用者参与和日常活动为核心，把公共空间从“建好”推向“被使用、被认同”。",
 "典型手法与适用条件":"通过社区共创、临时活动与渐进改造激活空间；适用于街区、广场与滨水地带。",
 "实例":"名称：社区参与式公共空间更新（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"忽视在地使用者会流于“设计师自嗨”；短期活动难转化为长期活力。" + REG,
 "一图":"见下方示意：居民活动填充公共空间。",
 "待核实":"所举更新案例的设计团队与年份待核实。",
},
"space-syntax": {
 "原理":"空间句法用图论把空间抽象为节点与连接，量化整合度、连接度以分析人流与可达性。",
 "典型手法与适用条件":"用于城市与建筑平面的可达性比较、预测人流的空间分布；适合前期方案评估。",
 "实例":"名称：街区可达性拓扑分析（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"模型简化会遗漏实际使用与时间因素；指标解释需结合现场观察。" + REG,
 "一图":"见下方示意：空间的拓扑连接。",
 "待核实":"所举分析案例的研究者与年份待核实。",
},
"pattern-language": {
 "原理":"模式语言把反复出现的设计问题与解法写成可复用的“模式”，供组合使用。",
 "典型手法与适用条件":"从城市到细部逐级列举模式并互相引用；适用于参与式设计与经验传承。",
 "实例":"名称：住宅与街区模式组合（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"机械套用模式会僵化；模式需按具体语境调整。" + REG,
 "一图":"见下方示意：若干模式彼此组合。",
 "待核实":"所举模式应用的作者与年代待核实。",
},
"biophilic-design": {
 "原理":"亲生命性设计把自然要素（光、植物、水、天然材料）与自然形态引入建成环境以促进健康。",
 "典型手法与适用条件":"增设自然采光、绿视率与天然材质，营造可恢复压力的空间；适用于办公、医疗与居住。",
 "实例":"名称：引入自然要素的办公空间（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"“贴几盆绿植”不等于亲生命设计；维护与过敏、湿度问题需一并考虑。" + REG,
 "一图":"见下方示意：植物、自然光与材料并置。",
 "待核实":"所举空间案例的设计者与年份待核实。",
},
"defensible-space-theory": {
 "原理":"防御性空间理论认为领域感、自然监视与清晰的半私密层次能减少犯罪机会与不安全感。",
 "典型手法与适用条件":"以入口过渡、可视窗与照明强化“易被看见”；适用于住区与校园。",
 "实例":"名称：住区领域层次设计（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"过度封闭会削弱公共性；监控设计需平衡隐私与安全。" + REG,
 "一图":"见下方示意：领域与自然监视。",
 "待核实":"所举住区实例的设计者与年份待核实。",
},
"functionalism-architecture": {
 "原理":"功能主义主张以使用需求、结构与材料的技术可能决定形态，而非复制历史样式。",
 "典型手法与适用条件":"以流线与功能分区组织平面，用标准化构件控制造价；适用于住宅与公共建筑。",
 "实例":"名称：功能主义集合住宅（类型性描述）；地点：欧洲；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只求合用易致空间单调；采光、保温与构造须按规范校核。" + REG,
 "一图":"见下方示意：形式服务功能。",
 "待核实":"所举住宅实例的设计者与年份待核实。",
},
"sunken-plaza": {
 "原理":"下沉广场借低于地面的高差形成相对独立的城市公共空间，兼顾聚集、通行与景观。",
 "典型手法与适用条件":"以台阶或坡道连接地面，配合绿化、水景与商业界面；适用于枢纽与商业中心。",
 "实例":"名称：静安寺下沉广场；地点：中国上海；设计者：卢济威主持城市设计、顾如珍负责建筑工程；年份：1999 年落成。此处仅列名称、地点、设计者与年份信息，不复制图像。",
 "常见错误与限制":"排水、防潮、无障碍与视线盲区需专门处理；与地面人流衔接不当会形成死角。" + REG,
 "一图":"见下方剖面示意：城市地面与下沉广场的高差。",
 "待核实":"其他下沉广场实例的设计者与年代待核实。",
},
}

SRC = {
"placemaking":["wp-placemaking","wp-urban-design"],
"space-syntax":["wp-space-syntax","wp-urban-morphology"],
"pattern-language":["wp-pattern-language","wp-a-pattern-language"],
"biophilic-design":["wp-biophilic-design","wp-evidence-based-design"],
"defensible-space-theory":["wp-defensible-space-theory","wp-cpted"],
"functionalism-architecture":["wp-functionalism-architecture","wp-form-follows-function"],
"sunken-plaza":["thepaper-jingan","jfdaily-jingan","wp-sunken-courtyard"],
}

def main():
    n=0
    for path in sorted((ROOT/"entries").glob("*.json")):
        doc=json.loads(path.read_text(encoding="utf-8")); ch=False
        for e in doc.get("entries",[]):
            k=e["id"]
            if k not in S: continue
            e["level"]="L2"; e["sections"]=S[k]; e["svg"]=[SVG[k]]; e["sources"]=SRC[k]
            if k=="sunken-plaza":
                e["needs_verification"]=True; e["pending_notes"]="其他下沉广场实例的设计者与年代待核实。"
            else:
                e["needs_verification"]=True; e["pending_notes"]="实例的具体名称、设计者与年代待补充独立来源。"
            n+=1; ch=True
        if ch: path.write_text(json.dumps(doc,ensure_ascii=False,indent=2),encoding="utf-8")
    print("upgraded",n)

if __name__=="__main__": main()
