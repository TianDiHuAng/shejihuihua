"""确定性生成首批 L1 骨架条目（38 条），与 2 条 L2 样板合计 40 条/轮。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# id|名称|层级|主题|时期|地区|定义|时间或位置|概述|来源(逗号分隔)|待核实(0/1)|待核实说明
DATA = """
linear-perspective|线性透视|重要|理论|文艺复兴至19世纪|欧洲|以几何投影和灭点组织画面深度的透视体系。|文艺复兴时期意大利（参见来源）。|它把观察者视点固定，使平行线按规律汇聚，是焦点透视的基础。|wp-perspective-graphical,wp-vanishing-point|0|
one-point-perspective|一点透视|重要|理论|文艺复兴至19世纪|欧洲|平行线向画面中单一主灭点汇聚的透视方法。|文艺复兴至19世纪欧洲（参见来源）。|适合表现正对观察者的立面、走廊与室内空间。|wp-perspective-graphical,wp-de-pictura|0|
two-point-perspective|两点透视|重要|理论|文艺复兴至19世纪|欧洲|两组水平平行线分别汇聚于左右两个灭点的透视方法。|文艺复兴至19世纪欧洲（参见来源）。|常用于表现建筑转角与斜向观看的立方体。|wp-perspective-graphical,wp-alberti|0|
three-point-perspective|三点透视|重要|理论|20世纪|欧洲|在两点透视基础上加入垂直方向灭点的透视方法。|20世纪（参见来源）。|用于仰视高层建筑或俯视深井式空间，垂直线随之收敛。|wp-perspective-graphical,wp-curvilinear-perspective|0|
curvilinear-perspective|曲线透视|补充|理论|20世纪|全球|用曲线网格表现超广角或鱼眼视野的透视方法。|20世纪（参见来源）。|直线在画面边缘弯曲，适合表现极端视角与空间包裹感。|wp-curvilinear-perspective,wp-perspective-graphical|0|
aerial-perspective|空气透视|重要|理论|文艺复兴至19世纪|欧洲|以远处物象明度降低、对比减弱并偏冷灰表现深度的方法。|文艺复兴至19世纪欧洲（参见来源）。|它补充线性透视，使远景在色彩与清晰度上退后。|wp-aerial-perspective,wp-perspective-graphical|0|
foreshortening|缩短法|重要|理论|文艺复兴至19世纪|欧洲|物体朝向观察者时视觉长度缩短的现象与画法。|文艺复兴至19世纪欧洲（参见来源）。|正确处理缩短关系能让肢体与器皿在透视中保持可信体积。|wp-perspective-graphical,wp-leonardo-da-vinci|0|
vanishing-point|灭点|重要|理论|文艺复兴至19世纪|欧洲|画面中相互平行的深远线汇聚的假想点。|文艺复兴时期（参见来源）。|灭点位置决定观看方向与空间稳定性，是透视作图的核心。|wp-vanishing-point,wp-perspective-graphical|0|
horizon-line|视平线|重要|理论|文艺复兴至19世纪|欧洲|与观察者眼睛等高、在画面中表现为水平的基准线。|文艺复兴至19世纪欧洲（参见来源）。|视平线统一管理各组平行线，决定画面中人物与建筑的相对高度。|wp-perspective-graphical,wp-vanishing-point|0|
scattered-perspective|散点透视|核心|理论|古代|中国|中国画中视点移动、多视点组合的空间表现方法。|古代中国（参见来源）。|它使长卷能够连续展开不同视点下的景物，与焦点透视形成对照。|wp-chinese-painting,wp-reverse-perspective|0|
composition|构图法则|核心|理论|跨时期|全球|对画面元素的位置、比例与关系进行组织以形成秩序和重点的方法。|跨时期、全球（参见来源）。|构图决定观看路径与信息主次，是绘画与视觉设计共通的骨架。|wp-composition-visual-arts,wp-rule-of-thirds|0|
rule-of-thirds|三分法|重要|理论|跨时期|全球|将画面横竖各三等分并把主体置于交点或分割线上的构图方法。|跨时期、全球（参见来源）。|它让主体偏离几何中心，产生更自然的视觉平衡。|wp-rule-of-thirds,wp-composition-visual-arts|0|
rule-of-space|空间法则|补充|理论|跨时期|全球|在视线或运动方向前方预留画面空间的构图方法。|跨时期、全球（参见来源）。|预留空间能表现运动趋势与方向感，避免主体视线被画面边缘截断。|wp-composition-visual-arts,wp-leading-line|0|
simplification|简化|重要|理论|跨时期|全球|删减次要细节以突出主体的构图方法。|跨时期、全球（参见来源）。|简化不是信息缺失，而是通过取舍建立清晰的视觉层次。|wp-composition-visual-arts,wp-negative-space|0|
geometry-symmetry|几何与对称|重要|理论|跨时期|全球|以基本几何形状和对称关系组织画面的方法。|跨时期、全球（参见来源）。|对称带来稳定与仪式感，轻微破对称可增加张力。|wp-symmetry,wp-composition-visual-arts|0|
visual-movement|视觉动势|重要|理论|跨时期|全球|通过线条、形状与明暗引导视线在画面中移动的方法。|跨时期、全球（参见来源）。|动势控制观看顺序，使构图从入口走向重点。|wp-composition-visual-arts,wp-leading-line|0|
leading-lines|引导线|重要|理论|跨时期|全球|利用实际或隐含线条把视线引向主体的构图手法。|跨时期、全球（参见来源）。|道路、栏杆、光影边界都可以成为引导线。|wp-leading-line,wp-composition-visual-arts|0|
figure-ground|图底关系|重要|理论|20世纪|全球|区分主体图形与背景底面的视觉组织关系。|20世纪视觉心理学研究（参见来源）。|图底互换会造成有趣的歧义，稳定图底则保证信息清晰。|wp-figure-ground,wp-composition-visual-arts|0|
negative-space|负空间|重要|理论|20世纪|全球|主体之外的空白区域参与构图的方法。|20世纪（参见来源）；中国画留白传统另见相关条目。|负空间塑造主体轮廓并控制画面呼吸感。|wp-negative-space,wp-composition-visual-arts|0|
visual-center|视觉中心|重要|理论|跨时期|全球|画面中优先吸引注意力的区域。|跨时期、全球（参见来源）。|视觉中心可由对比、位置或指向线建立。|wp-composition-visual-arts,wp-rule-of-thirds|0|
balance|均衡|核心|理论|跨时期|全球|画面各元素在视觉重量上的均衡关系。|跨时期、全球（参见来源）。|均衡不等于对称，大小与色彩差异都能改变视觉重量。|wp-composition-visual-arts,wp-symmetry|0|
contrast-principle|对比|重要|理论|跨时期|全球|通过明度、色彩、形状或尺度差异突出主体的构图方法。|跨时期、全球（参见来源）。|对比建立主次，但过度对比会破坏整体统一。|wp-composition-visual-arts,wp-color-theory|0|
rhythm-repetition|节奏与重复|重要|理论|跨时期|全球|元素重复出现并形成视觉节奏的构图方法。|跨时期、全球（参见来源）。|重复建立秩序，节奏变化则防止单调。|wp-composition-visual-arts,wp-symmetry|0|
hierarchy|主次层级|重要|理论|跨时期|全球|通过大小、位置、明度等差异建立信息主次次序的方法。|跨时期、全球（参见来源）。|层级帮助观看者按重要性顺序读取画面信息。|wp-composition-visual-arts|1|仅见构图条目关于主次的讨论，待补充第二独立来源。
proportion|比例|核心|理论|跨时期|全球|部分与整体之间、或各部分之间的尺寸关系。|跨时期、全球；建筑理论中亦有专门讨论（参见来源）。|比例决定和谐感与尺度感，是构图和空间设计的共同语言。|wp-proportion-architecture,wp-golden-ratio|0|
golden-ratio|黄金分割|补充|理论|跨时期|欧洲|以约一比一点六一八的比例分割整体的构图参考。|跨时期、欧洲（参见来源）。|它被用作经验性的和谐参考，而非强制规则。|wp-golden-ratio,wp-golden-rectangle|0|
diagonal-composition|对角线构图|补充|理论|跨时期|全球|以对角线方向组织主体形成动势的构图方式。|跨时期、全球（参见来源）。|对角线比水平线更具运动感，适合表现方向与冲突。|wp-composition-visual-arts,wp-leading-line|0|
s-curve-composition|S形构图|补充|理论|跨时期|全球|以S形曲线引导视线深入画面的构图方式。|跨时期、全球（参见来源）。|S形曲线延长观看路径，常用于道路与河流题材。|wp-composition-visual-arts,wp-leading-line|0|
triangular-composition|三角形构图|补充|理论|跨时期|全球|以三角形结构稳定画面的构图方式。|跨时期、全球（参见来源）。|三角形底边提供稳定感，尖端提供指向与张力。|wp-composition-visual-arts,wp-symmetry|0|
framing-composition|框架式构图|补充|理论|跨时期|全球|利用前景元素围合主体的构图方式。|跨时期、全球（参见来源）。|门窗、枝叶与拱券都可成为框架，增加画面层次。|wp-composition-visual-arts,wp-chinese-garden|0|
color-theory|色彩理论|核心|理论|跨时期|全球|研究色彩混合、对比与和谐规律的理论体系。|跨时期、全球（参见来源）。|色彩理论连接物理光学、视觉感知与审美经验。|wp-color-theory,wp-theory-of-colours|0|
hue|色相|重要|理论|跨时期|全球|色彩借以区分种类的属性。|跨时期、全球（参见来源）。|色相是色彩循环秩序的基础，与明度、纯度共同描述颜色。|wp-hue,wp-color-theory|0|
value|明度|核心|理论|跨时期|全球|色彩的明暗程度。|跨时期、全球（参见来源）。|明度关系决定画面的结构与可读性，先于色相被视觉系统捕捉。|wp-colorfulness,wp-color-theory|0|
saturation|纯度|重要|理论|跨时期|全球|色彩的鲜艳或饱和程度。|跨时期、全球（参见来源）。|高纯度色彩吸引注意，低纯度色彩适合作为背景与过渡。|wp-colorfulness,wp-munsell-color-system|0|
primary-colors|三原色|重要|理论|跨时期|全球|可混合生成其他色彩的基础色集合。|跨时期、全球（参见来源）。|不同色彩模型采用不同原色集合，需区分光色与颜料色。|wp-primary-color,wp-color-wheel|0|
complementary-colors|互补色|重要|理论|跨时期|全球|色轮上相对、并置时形成强烈对比的色彩。|跨时期、全球（参见来源）。|互补配色能制造张力，降低一方纯度可获得更稳定的效果。|wp-complementary-colors,wp-color-wheel|0|
color-contrast|色彩对比|重要|理论|跨时期|全球|色彩之间在明度、色相、冷暖或纯度上的差异。|跨时期、全球（参见来源）。|对比度影响可读性与情绪，是无障碍视觉设计的重要变量。|wp-color-theory,wp-complementary-colors|0|
warm-cool|冷暖色|重要|理论|跨时期|全球|色彩给人的冷暖心理感受与倾向。|跨时期、全球（参见来源）。|冷暖关系常用于组织空间前后层次与画面情绪。|wp-color-theory,wp-theory-of-colours|0|
"""


def main():
    rows = []
    for line in DATA.strip().splitlines():
        parts = line.split("|")
        if len(parts) != 12:
            raise ValueError(f"bad row: {line[:80]}")
        eid, title, tier, theme, period, region, definition, time_place, overview, srcs, flag, note = parts
        rows.append({
            "id": eid, "title": title, "level": "L1", "tier": tier,
            "theme": theme, "period": period, "region": region,
            "definition": definition, "time_or_place": time_place, "overview": overview,
            "related": [],
            "sources": [s for s in srcs.split(",") if s],
            "needs_verification": flag == "1",
            "pending_notes": note,
        })
    # 同主题相邻条目作为相关条目，保证 related 指向 scope 内真实 id
    themes = list(dict.fromkeys(r["theme"] for r in rows))
    for theme in themes:
        group = [r for r in rows if r["theme"] == theme]
        for i, r in enumerate(group):
            if i + 1 < len(group):
                r["related"] = [group[i + 1]["id"]]
    out = ROOT / "entries" / "batch-01.json"
    out.write_text(json.dumps({"unit_id": "batch-01", "title": "首批 L1 骨架条目", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"batch-01 entries={len(rows)}")


if __name__ == "__main__":
    main()
