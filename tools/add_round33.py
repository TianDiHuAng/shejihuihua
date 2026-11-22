"""第33轮：写 12 条未写条目（光影/照明组 + 配色/象征），直接 L2、去模板化。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

D = {
"light-shadow-modeling": dict(
 defn="光影塑形指用受光与背光的明暗过渡表现物体的体积与转折。",
 tp="文艺复兴至19世纪、欧洲（参见来源）。",
 ov="光线落在形体上形成亮部、暗部与过渡，体积因明暗梯度而被感知。",
 prin="物体朝向光源的一面亮、背向的一面暗，中间以渐变过渡，视觉据此推断起伏。",
 method="先定主光方向，再铺大块明暗，最后在明暗交界处压实、向亮部渐淡。",
 inst="名称：单光源石膏像的明暗写生（类型性描述）；地点与作者不适用。看暗部如何随形体转折而变。",
 cap="见下方示意图：光向、受光面与暗部的分布。",
 limit="光向不清会显得平；暗部一味加深会丢失转折。",
 srcs=["wp-chiaroscuro", "wp-sfumato"]),
"five-tones": dict(
 defn="明暗五调子指高光、亮部、明暗交界线、反光与投影五个明暗层次。",
 tp="文艺复兴至19世纪、欧洲（参见来源）。",
 ov="把连续明暗归纳为五档，便于观察与表现立体。",
 prin="五调子是对连续明暗的简化分区，帮助稳定地判断亮暗关系而非逐点描摹。",
 method="依次找出高光与投影，再定交界线，最后补亮部与反光，形成完整循环。",
 inst="名称：球体五调子练习（类型性描述）；地点与作者不适用。观察交界线最实处与反光的最亮处。",
 cap="见下方示意图：由高光到投影的五档。",
 limit="机械分档会板滞；五调子需服从整体光感。",
 srcs=["wp-chiaroscuro", "wp-rembrandt-lighting"]),
"cast-shadow": dict(
 defn="投影是物体遮挡光线后在承接面上留下的暗区。",
 tp="跨时期、全球（参见来源）。",
 ov="投影的形状与边缘虚实反映光源强弱、远近与物体形状。",
 prin="光沿直线传播，被物体遮挡处形成阴影；光源越远越接近平行光，投影边缘越硬。",
 method="依据光源方向确定投影落点，近处边缘实、远处边缘虚。",
 inst="名称：静物在桌面上的投影（类型性描述）；地点与作者不适用。看投影如何暗示桌面与光源。",
 cap="见下方示意图：光源—物体—投影的几何关系。",
 limit="投影方向与主光不一致会穿帮；投影过黑会失透明感。",
 srcs=["wp-chiaroscuro", "wp-tenebrism"]),
"highlight": dict(
 defn="高光是物体表面反射光源最亮的部位。",
 tp="跨时期、全球（参见来源）。",
 ov="高光提示材质与光源，位置随视点与光向移动。",
 prin="光滑表面把光源近乎镜面地反射入眼，形成小而亮的高光；粗糙表面高光更弥散。",
 method="按材质决定高光的锐利与大小，点在受光且朝向光源的凸起处。",
 inst="名称：瓷器表面的点状高光（类型性描述）；地点与作者不适用。观察高光如何体现釉面。",
 cap="见下方示意图：受光凸起处的高光点。",
 limit="高光过多会显得油腻；位置错误会误导光源。",
 srcs=["wp-chiaroscuro", "wp-rembrandt-lighting"]),
"reflected-light": dict(
 defn="反光是暗部受环境反射光影响而出现的较亮区域。",
 tp="跨时期、全球（参见来源）。",
 ov="反光让暗部透气，避免死黑，并暗示周边环境。",
 prin="光线被邻近物体或地面反射后进入暗部，使最暗处之外仍有一层微亮。",
 method="在暗部靠近反光面的一侧提亮一点，保留交界线仍为最暗。",
 inst="名称：衬布反射下的暗部（类型性描述）；地点与作者不适用。看暗部边缘的一线亮。",
 cap="见下方示意图：暗部靠环境一侧的反光。",
 limit="反光亮过亮部会颠倒明暗；没有反光则暗部板结。",
 srcs=["wp-chiaroscuro", "wp-sfumato"]),
"core-shadow": dict(
 defn="明暗交界线是受光面转向背光面时最暗的一条带。",
 tp="文艺复兴至19世纪、全球（参见来源）。",
 ov="交界线是体积转折的关键，常比投影更暗更实。",
 prin="形体在此处法线近乎垂直于光线，受光最少，因而最暗，是塑造体积的着力点。",
 method="沿形体转折压实交界线，再向两端过渡，使体积立起来。",
 inst="名称：圆柱体的交界线（类型性描述）；地点与作者不适用。看交界线随柱面如何纵向延伸。",
 cap="见下方示意图：受光面向暗部转折的最暗带。",
 limit="交界线位置画错会改变形体；过硬会显得生硬。",
 srcs=["wp-chiaroscuro", "wp-tenebrism"]),
"front-light": dict(
 defn="正面光指光源位于被摄体正前方、与视线同向的照明。",
 tp="跨时期、全球（参见来源）。",
 ov="正面光平铺明亮但压低立体感，适合记录与柔和人像。",
 prin="光源与相机同向时阴影被推到背后，形体起伏被削弱，画面平整。",
 method="用于需要清晰记录的场合；若要立体感可稍作侧移或加侧光。",
 inst="名称：正面补光的证件照式人像（类型性描述）；地点与作者不适用。看鼻影几乎消失。",
 cap="见下方示意图：光源与视线同向。",
 limit="全正面光会扁平呆板；易在背景留下硬影。",
 srcs=["wp-architectural-lighting-design", "wp-daylighting-architecture"]),
"side-light": dict(
 defn="侧面光指光源位于被摄体一侧约九十度方向的照明。",
 tp="跨时期、全球（参见来源）。",
 ov="侧光强调纹理与体积，明暗各半、戏剧性强。",
 prin="光线横向掠过表面，凸起迎光、凹陷背光，质感与起伏被放大。",
 method="侧光下注意暗部补光比例，避免一半死黑。",
 inst="名称：侧光下的砖墙质感（类型性描述）；地点与作者不适用。看灰缝的凹凸被拉出。",
 cap="见下方示意图：光源来自一侧、明暗各半。",
 limit="暗部过重会失细节；需控制补光。",
 srcs=["wp-architectural-lighting-design", "wp-daylighting-architecture"]),
"back-light": dict(
 defn="逆光指光源位于被摄体背后、朝向镜头的照明。",
 tp="跨时期、全球（参见来源）。",
 ov="逆光勾勒轮廓、制造剪影与透光感，氛围强烈。",
 prin="光源在主体之后，主体大面积处于阴影，边缘被照亮形成轮廓光。",
 method="逆光下以剪影或轮廓光造型，必要时对主体补光避免死黑。",
 inst="名称：逆光的窗边人物剪影（类型性描述）；地点与作者不适用。看发丝与肩线的亮边。",
 cap="见下方示意图：光源在主体背后。",
 limit="曝光不当会主体全黑；眩光需控制。",
 srcs=["wp-architectural-lighting-design", "wp-daylighting-architecture"]),
"top-light": dict(
 defn="顶光指光源位于被摄体正上方自上而下的照明。",
 tp="跨时期、全球（参见来源）。",
 ov="顶光在眼窝、鼻下与下颌形成阴影，气氛肃穆或压抑。",
 prin="光源自上而下，凸出部位受光、凹处落影，形成由上而下的明暗秩序。",
 method="顶光适合展厅与戏剧性场景，人像需谨慎补光修饰眼窝阴影。",
 inst="名称：天窗下的展厅顶光（类型性描述）；地点与作者不适用。看展台由上而下的照度梯度。",
 cap="见下方示意图：光源自上而下。",
 limit="人像顶光易显憔悴；需补光。",
 srcs=["wp-architectural-lighting-design", "wp-daylighting-architecture"]),
"color-scheme": dict(
 defn="配色方案指按一定关系选定的主色、辅色与点缀色的组合。",
 tp="跨时期、全球（参见来源）。",
 ov="配色方案决定画面的统一与重点，可按单色、类比或互补组织。",
 prin="以主色定基调、辅色做过渡、点缀色提亮，色相与明度的关系决定整体气质。",
 method="先定主色与明度骨架，再加一两个辅色与少量点缀，控制总面积比例。",
 inst="名称：以蓝为主色的室内配色（类型性描述）；地点与作者不适用。看主辅色的面积搭配。",
 cap="见下方示意图：主色、辅色与点缀的配比。",
 limit="色相过多会杂乱；比例失衡会喧宾夺主。",
 srcs=["wp-color-theory", "wp-color-wheel"]),
"color-symbolism": dict(
 defn="色彩象征指特定色彩在文化中被赋予的联想与含义。",
 tp="跨时期、全球（参见来源）。",
 ov="同一色彩在不同文化中含义不同，需结合语境理解。",
 prin="色彩意义来自长期的文化约定与经验联想，具有地域与时代差异。",
 method="依题材与文化语境选色，避免跨文化误读。",
 inst="名称：红在中国语境中的喜庆含义（类型性描述）；地点与作者不适用。对比其他文化中的红色联想。",
 cap="见下方示意图：色彩—文化联想的对应。",
 limit="脱离语境谈象征会牵强；跨文化易误读。",
 srcs=["wp-color-theory", "wp-theory-of-colours"]),
}

SVG_L = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='150' cy='90' r='26' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='176' y1='108' x2='480' y2='250' stroke='var(--muted)' stroke-dasharray='6 5'/><ellipse cx='480' cy='250' rx='70' ry='50' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='120' y='60' fill='var(--ink)'>光源</text><text x='430' y='330' fill='var(--ink)'>形体与明暗</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_C = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='380' cy='200' r='120' fill='none' stroke='var(--accent)'/><circle cx='380' cy='80' r='28' fill='var(--accent-soft)' stroke='var(--muted)'/><circle cx='500' cy='260' r='28' fill='none' stroke='var(--muted)'/><circle cx='260' cy='260' r='28' fill='none' stroke='var(--muted)'/><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"

cov = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))["entries"]
META = {r["id"]: r for r in cov}


def main():
    rows = []
    for eid, f in D.items():
        m = META[eid]
        svg = SVG_C if m["theme"] == "理论" and eid in ("color-scheme", "color-symbolism") else SVG_L
        rows.append({
            "id": eid, "title": m["title"], "level": "L2", "tier": m["tier"],
            "theme": m["theme"], "period": m["period"], "region": m["region"],
            "definition": f["defn"], "time_or_place": f["tp"], "overview": f["ov"],
            "related": [],
            "sections": {
                "原理": f["prin"],
                "典型手法与适用条件": f["method"],
                "实例": f["inst"],
                "常见错误与限制": f["limit"] + REG,
                "一图": f["cap"],
                "待核实": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"],
            },
            "svg": [svg],
            "sources": f["srcs"],
            "needs_verification": True,
            "pending_notes": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"],
        })
    out = ROOT / "entries" / "batch-33.json"
    out.write_text(json.dumps({"unit_id": "batch-33", "title": "第33轮光影与配色条目", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-33 written", len(rows))


if __name__ == "__main__":
    main()
