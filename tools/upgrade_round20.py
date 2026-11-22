"""第20轮：收尾剩余重要 L1（visual-center/contrast-principle/form-follows-function）+ 3 条补充。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"visual-center": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='80' width='600' height='240' fill='none' stroke='var(--line)'/><circle cx='380' cy='200' r='26' fill='var(--accent)'/><circle cx='200' cy='140' r='14' fill='none' stroke='var(--muted)'/><circle cx='560' cy='260' r='14' fill='none' stroke='var(--muted)'/><text x='400' y='195' fill='var(--ink)'>视觉中心</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"contrast-principle": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='130' width='220' height='140' fill='var(--accent)'/><rect x='420' y='160' width='220' height='80' fill='var(--panel)' stroke='var(--line)'/><text x='180' y='110' fill='var(--ink)'>强对比</text><text x='480' y='140' fill='var(--ink)'>弱对比</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"form-follows-function": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='130' width='480' height='190' fill='none' stroke='var(--accent)'/><rect x='180' y='170' width='150' height='150' fill='var(--accent-soft)' stroke='var(--muted)'/><rect x='360' y='170' width='220' height='150' fill='none' stroke='var(--muted)'/><text x='200' y='105' fill='var(--ink)'>功能→形态</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"curvilinear-perspective": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='80' width='600' height='240' fill='none' stroke='var(--line)'/><path d='M 120 120 Q 380 60 640 120' fill='none' stroke='var(--accent)'/><path d='M 120 280 Q 380 340 640 280' fill='none' stroke='var(--accent)'/><path d='M 140 300 Q 120 200 140 100' fill='none' stroke='var(--muted)'/><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
"courtyard": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='100' width='480' height='230' fill='none' stroke='var(--accent)'/><rect x='280' y='170' width='200' height='120' fill='var(--accent-soft)' stroke='var(--muted)'/><text x='330' y='225' fill='var(--ink)'>院落</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"green-architecture": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='150' width='300' height='160' fill='none' stroke='var(--accent)'/><circle cx='560' cy='200' r='46' fill='none' stroke='var(--muted)'/><line x1='540' y1='300' x2='580' y2='300' stroke='var(--muted)'/><text x='160' y='120' fill='var(--ink)'>节能与自然要素</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"visual-center": {
 "原理":"视觉中心是画面中优先吸引注意的区域，可由位置、对比或指向线建立，未必在几何中点。",
 "典型手法与适用条件":"把主体放在三分点或对比最强处；适用于摄影、海报与界面首屏。",
 "实例":"名称：三分点式视觉中心（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"多个等强焦点会分散注意；主体贴边易被裁切。" + REG,
 "一图":"见下方示意：偏离中心的视觉焦点。",
 "待核实":"示例作品与作者年代待核实。",
},
"contrast-principle": {
 "原理":"对比借助明暗、色彩、形状与尺度的差异突出主体，但过度对比会破坏整体统一。",
 "典型手法与适用条件":"以一方强、一方弱建立主次；可在大面积柔和区放置小块高对比。",
 "实例":"名称：强弱对比的主次安排（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"处处强对比等于没有重点；低对比在弱光下不可读。" + REG,
 "一图":"见下方示意：强对比与弱对比并置。",
 "待核实":"示例版式的出处待核实。",
},
"form-follows-function": {
 "原理":"“形式追随功能”主张建筑的形态应由实际用途决定，而非先定样式再塞功能。",
 "典型手法与适用条件":"先梳理功能与流线，再生成体量与开窗；适用于强调理性的现代建筑。",
 "实例":"名称：功能主导的现代建筑（类型性描述）；地点：全球；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"把命题绝对化会导致空间机械单调；形式与意义、文脉需一并权衡。" + REG,
 "一图":"见下方示意：从功能推导形态。",
 "待核实":"示例建筑的设计者与年代待核实。",
},
"curvilinear-perspective": {
 "原理":"曲线透视用弯曲的网格表现超广角或鱼眼视野，直线在画面边缘发生弯曲。",
 "典型手法与适用条件":"用于全景、穹顶画与极端视角；可减轻直线透视在广角下的拉伸。",
 "实例":"名称：广角全景的曲线透视（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"曲率使用不当会显得扭曲失真；与直线元素混用需谨慎。" + REG,
 "一图":"见下方示意：边缘弯曲的网格。",
 "待核实":"示例作品与作者年代待核实。",
},
"courtyard": {
 "原理":"庭院由建筑或墙体围合、向天空开敞，兼具采光、通风与安静户外活动，是多文化的空间原型。",
 "典型手法与适用条件":"以院落组织采光与私密性，院内可植栽、置石或理水；适用于居住与合院式建筑。",
 "实例":"名称：合院式住宅庭院（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"院落过深会采光不足；排水与防潮需专门设计。" + REG,
 "一图":"见下方示意：被建筑围合的院落。",
 "待核实":"示例庭院的设计者与年代待核实。",
},
"green-architecture": {
 "原理":"绿色建筑以降低资源消耗与环境影响为目标，关注能耗、水、材料与室内健康。",
 "典型手法与适用条件":"被动式设计优先，辅以高效设备与可再生资源；适用于新建与改造。",
 "实例":"名称：被动式节能公共建筑（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"只堆设备而忽视被动设计会事倍功半；评价指标须按当地标准核定。" + REG,
 "一图":"见下方示意：节能与自然要素。",
 "待核实":"示例建筑的设计者与评价数据待核实。",
},
}

SRC = {
"visual-center":["wp-composition-visual-arts","wp-rule-of-thirds"],
"contrast-principle":["wp-composition-visual-arts","wp-color-theory"],
"form-follows-function":["wp-form-follows-function","wp-functionalism-architecture"],
"curvilinear-perspective":["wp-curvilinear-perspective","wp-perspective-graphical"],
"courtyard":["wp-courtyard","wp-chinese-garden"],
"green-architecture":["wp-green-building","wp-sustainable-architecture"],
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
