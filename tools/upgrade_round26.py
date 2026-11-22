"""第26轮：5 条新增 L1→L2 + pending_notes 去模板化。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
"rembrandt": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><ellipse cx='380' cy='200' rx='120' ry='150' fill='var(--accent-soft)' stroke='var(--accent)'/><polygon points='330,240 430,240 380,190' fill='var(--panel)' stroke='var(--muted)'/><text x='300' y='90' fill='var(--ink)'>面部三角亮区</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
"tenebrism": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='80' width='600' height='240' fill='var(--ink)'/><ellipse cx='380' cy='210' rx='90' ry='120' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='300' y='60' fill='var(--panel)'>背景极暗、聚光突出主体</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"plaza": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='110' width='600' height='190' fill='var(--accent-soft)' stroke='var(--line)'/><circle cx='240' cy='205' r='20' fill='none' stroke='var(--accent)'/><circle cx='380' cy='205' r='20' fill='none' stroke='var(--accent)'/><circle cx='520' cy='205' r='20' fill='none' stroke='var(--accent)'/><text x='300' y='90' fill='var(--ink)'>硬质开敞、聚会停留</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"atrium-architecture": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='100' y1='80' x2='660' y2='80' stroke='var(--ink)' stroke-width='3'/><rect x='280' y='80' width='200' height='250' fill='none' stroke='var(--accent)'/><line x1='380' y1='90' x2='380' y2='250' stroke='var(--muted)' stroke-dasharray='6 5'/><rect x='120' y='150' width='160' height='180' fill='none' stroke='var(--muted)'/><rect x='480' y='150' width='160' height='180' fill='none' stroke='var(--muted)'/><text x='320' y='60' fill='var(--ink)'>天窗采光的中庭</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"exit-sign": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='90' width='600' height='230' fill='none' stroke='var(--line)'/><rect x='300' y='140' width='160' height='60' fill='var(--accent-soft)' stroke='var(--accent)'/><polygon points='430,155 470,170 430,185' fill='var(--accent)'/><circle cx='160' cy='250' r='10' fill='var(--accent)'/><line x1='170' y1='250' x2='300' y2='200' stroke='var(--muted)' stroke-dasharray='6 5'/><text x='330' y='130' fill='var(--ink)'>出口标识</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

S = {
"rembrandt": {
 "原理":"伦勃朗光以单侧主光在面部受光侧的眼下方形成倒三角亮区，另一侧深暗，突出体积与情绪。",
 "典型手法与适用条件":"主光约 45° 侧上方、辅光很弱，适用于肖像摄影与人物绘画。",
 "实例":"名称：伦勃朗式肖像布光（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"辅光过强会使三角消失；面部转向不当会破坏受光比例。" + REG,
 "一图":"见下方示意：面部三角亮区与暗侧。",
 "待核实":"具体作品/照片的拍摄者与年代待核实。",
},
"tenebrism": {
 "原理":"暗绘风格把背景压到极暗，用一束强光突出主体，是明暗法的极端化，营造神秘与戏剧。",
 "典型手法与适用条件":"大面积深色配集中高光；适用于宗教画与戏剧性题材。",
 "实例":"名称：暗色调绘画（类型性描述）；地点：欧洲；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"过暗会丢失暗部细节；强光单点易使画面失衡。" + REG,
 "一图":"见下方示意：极暗背景与聚光主体。",
 "待核实":"具体作品与作者年代待核实。",
},
"plaza": {
 "原理":"广场是城市中向公众开放、以硬质铺装为主的聚集空间，兼具通行、停留与交往功能。",
 "典型手法与适用条件":"以可达性、活动、舒适与社交四要素组织；适用于城市中心与社区。",
 "实例":"名称：城市中心广场（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"尺度失衡或缺少遮阴会让人不愿停留；无障碍与排水须达标。" + REG,
 "一图":"见下方示意：硬质开敞的公共广场。",
 "待核实":"具体广场的设计者与年代待核实。",
},
"atrium-architecture": {
 "原理":"中庭贯通多层并常覆天窗，把天然光引入建筑深处，同时组织交通与社交。",
 "典型手法与适用条件":"以天窗或侧高窗采光，结合楼梯与连廊；适用于大进深公共建筑。",
 "实例":"名称：带天窗中庭的公共建筑（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"玻璃顶易致眩光与过热；排烟与防火分隔须按规范设计。" + REG,
 "一图":"见下方示意：天窗采光的中庭。",
 "待核实":"具体建筑的设计者与年代待核实。",
},
"exit-sign": {
 "原理":"疏散标识标示最近安全出口的位置与方向，并以持续照明保证紧急时可见。",
 "典型手法与适用条件":"出口与疏散路径设发光标识，视线连续可见；照度按规范校核。",
 "实例":"名称：公共建筑出口标识系统（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
 "常见错误与限制":"标识被遮挡或照度不足会延误疏散；布置间距须按当地规范。" + REG,
 "一图":"见下方示意：出口标识与视线。",
 "待核实":"出口标识的早期年代与制度化沿革待补充专门来源。",
},
}

SRC = {
"rembrandt":["wp-rembrandt-lighting","rijksmuseum-rembrandt"],
"tenebrism":["wp-tenebrism","dailyart-tenebrism"],
"plaza":["wp-town-square","pps-successful-place"],
"atrium-architecture":["wp-atrium-architecture","designingbuildings-atrium"],
"exit-sign":["wp-exit-sign","ecfr-1910-37"],
}

TEMPLATE = "实例的具体名称、设计者与年代待补充独立来源。"

def main():
    n=0
    for path in sorted((ROOT/"entries").glob("*.json")):
        doc=json.loads(path.read_text(encoding="utf-8")); ch=False
        for e in doc.get("entries",[]):
            k=e["id"]
            if k in S:
                e["level"]="L2"; e["sections"]=S[k]; e["svg"]=[SVG[k]]; e["sources"]=SRC[k]
                e["needs_verification"]=True
                e["pending_notes"]="「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % e["title"]
                n+=1; ch=True
            elif e.get("pending_notes")==TEMPLATE:
                e["pending_notes"]="「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % e["title"]
                ch=True
        if ch: path.write_text(json.dumps(doc,ensure_ascii=False,indent=2),encoding="utf-8")
    print("upgraded",n)

if __name__=="__main__": main()
