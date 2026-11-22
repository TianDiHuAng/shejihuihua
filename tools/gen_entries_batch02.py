"""第2轮：生成 39 条核心 L1 条目，分 4 批（10/10/10/9）写入。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COVERAGE = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
META = {r["id"]: r for r in COVERAGE["entries"]}
THEME_ORDER = [r["id"] for r in COVERAGE["entries"]]

# id|定义|时间与位置|概述|来源(逗号)|待核实(0/1)|待核实说明
DATA = """
chiaroscuro|以强烈明暗对比塑造体积和戏剧性效果的绘画方法。|文艺复兴至19世纪欧洲（参见来源）。|明暗法把光线作为组织画面焦点的手段，其后出现更极端的暗绘倾向。|wp-chiaroscuro,wp-tenebrism|0|
six-principles|中国画品评与创作的六条准则，传统上归于谢赫。|古代中国（参见来源）。|六法把气韵、用笔、象形、赋彩、位置与传移并列，构成传统绘画的评价框架。|wp-six-principles-chinese-painting,wp-xie-he|0|
qi-yun|六法之首，强调作品的精神气息与生动韵致。|古代中国（参见来源）。|气韵生动关注整体生命感，而非单一物象的精确再现。|wp-six-principles-chinese-painting,wp-chinese-painting|0|
liubai|以空白参与画面结构和意境营造的方法。|古代中国（参见来源）。|留白让未画之处承担空间、光线与想象的功能，是东方构图的重要语言。|wp-chinese-painting|1|仅见中国画综合条目对留白的讨论，待补充针对留白的独立来源。
yijing|作品通过物象与留白引发的情景交融之意。|古代中国（参见来源）。|意境把观看者从可见物象引向不可尽言的情绪与想象。|wp-chinese-painting,wp-shitao|0|
east-west-perspective-compare|散点透视与焦点透视在视点组织上的对照。|跨时期、全球（参见来源）。|前者移动视点展开长卷，后者固定视点汇聚于灭点，二者服务于不同的观看方式。|wp-perspective-graphical,wp-chinese-painting|0|
east-west-space-compare|留白与负空间在画面组织中的对照。|跨时期、全球（参见来源）。|两者都利用空白塑造主体，但文化语境与意图表达各有侧重。|wp-chinese-garden,wp-negative-space|0|
space-definition|建筑空间是由围合界面、尺度与人的活动共同限定的场所。|跨时期、全球（参见来源）。|空间的感知不只来自几何边界，也来自光线、材料与使用方式。|wp-architecture,wp-architectural-theory|0|
human-scale|以人体尺寸和使用感受为参照的空间尺度。|跨时期、全球（参见来源）。|人体尺度让门、台阶、家具与通道与身体动作相匹配。|wp-proportion-architecture,wp-architecture|0|
spatial-sequence|若干空间按进入顺序组织形成的连续体验。|跨时期、全球（参见来源）。|序列通过开合、明暗与尺度变化控制节奏，使行进成为叙事。|wp-architecture,wp-architectural-theory|0|
transition-space|连接两个不同性质空间的中间地带。|跨时期、全球（参见来源）。|过渡空间缓冲内外、公私或动静的突变，常见于门厅、廊与檐下。|wp-vestibule-architecture,wp-loggia|0|
spatial-organization|把功能、流线与空间单元组织成整体的方式。|跨时期、全球（参见来源）。|常见组织方式包括串联、并列、集中与放射，各有适用条件。|wp-architecture,wp-architectural-theory|0|
interior-exterior-transition|室内与室外在空间、视线与气候上的连续过渡。|跨时期、全球（参见来源）。|庭院、廊道与可开启界面让内外界线变得可渗透。|wp-courtyard,wp-loggia|0|
courtyard|由建筑或墙体围合、向天空开敞的院落空间。|跨时期、全球（参见来源）。|庭院提供采光、通风与安静的户外活动场所，是多种文化的共同原型。|wp-courtyard,wp-chinese-garden|0|
borrowed-scenery|把园外景物纳入园内视线的造景手法。|古代中国（参见来源）。|借景突破边界，使远景、山形或塔影成为园中画面的一部分。|wp-borrowed-scenery,wp-chinese-garden|0|
framed-scenery|以门窗、洞口或枝干围合景物形成画面的手法。|古代中国（参见来源）。|框景把连续风景切成局部画面，强化观看的焦点与层次。|wp-chinese-garden|1|仅见中国园林综合条目，待补充针对框景的独立来源。
opposed-scenery|在视线端点设置景物以形成呼应的造景手法。|古代中国（参见来源）。|对景让行进终点成为视觉落点，组织游线的高潮。|wp-chinese-garden|1|仅见中国园林综合条目，待补充针对对景的独立来源。
screened-scenery|以墙体、山石或植物遮挡视线后再揭示景物的手法。|古代中国（参见来源）。|障景通过先抑后扬制造悬念，控制观看节奏。|wp-chinese-garden|1|仅见中国园林综合条目，待补充针对障景的独立来源。
winding-path|以曲折路线延长游览并变化视角的造景手法。|古代中国（参见来源）。|曲径使有限场地产生多重画面，也让行进速度放缓。|wp-chinese-garden|1|仅见中国园林综合条目，待补充针对曲径的独立来源。
tour-route|把景点按时间与视线关系串联的游线组织。|古代中国（参见来源）。|游线决定先看什么、何时转折与在哪里停留，是园林叙事的骨架。|wp-chinese-garden,wp-wayfinding|0|
circulation|建筑与城市中人流、车流及服务流线的组织。|跨时期、全球（参见来源）。|动线设计把行为路径转化为空间秩序，影响效率与体验。|wp-architecture,wp-wayfinding|0|
pedestrian-flow|以步行者移动与停留为核心组织的流线。|跨时期、全球（参见来源）。|步行流线关注安全、舒适与节点停顿，而非单纯通行效率。|wp-wayfinding,wp-plaza|0|
evacuation-route|供紧急情况下人员疏散的路径组织。|20世纪、全球（参见来源）。|疏散动线强调清晰标识、足够宽度与避免瓶颈，设计须依当地规范。|wp-exit-sign,wp-wayfinding|0|
sunken-plaza|地坪低于周边城市地面的公共广场。|20世纪、全球（参见来源）。|下沉广场借高差形成相对安静的聚集空间，同时带来排水与可达性要求。|wp-sunken-courtyard,wp-plaza|0|
level-change|通过台阶、坡道或高差组织空间转换的手法。|跨时期、全球（参见来源）。|高差既划分领域也制造视线变化，需要兼顾安全与无障碍。|wp-architecture,wp-sunken-courtyard|0|
drainage|引导雨水离开低处空间与铺装的组织方式。|20世纪、全球（参见来源）。|下沉空间尤其依赖坡度、沟槽与集水点避免积水。|wp-architecture,wp-sunken-courtyard|0|
damp-proofing|防止地下或近地空间受潮的构造措施。|20世纪、全球（参见来源）。|防潮关注毛细水、冷凝与地下水压力对材料和室内环境的影响。|wp-building-material,wp-sunken-courtyard|0|
safety-guarding|通过护栏、照明与视线管理降低高差风险的措施。|20世纪、全球（参见来源）。|低处空间需让人能预见边缘与台阶，避免跌坠和死角。|wp-architecture,wp-exit-sign|0|
daylighting|利用天然光满足视觉与空间感受的设计。|跨时期、全球（参见来源）。|侧窗与天窗决定光线方向，采光与眩光需要一并考虑。|wp-daylighting,wp-architecture|0|
natural-ventilation|依靠风压与热压实现室内外空气交换的方式。|跨时期、全球（参见来源）。|自然通风受开口位置、朝向与气候影响，可与机械系统互补。|wp-natural-ventilation,wp-ventilation-architecture|0|
material-texture|材料表面质感对视觉与触觉感受的作用。|跨时期、全球（参见来源）。|粗糙、光滑、透明与吸光材料改变空间的光线反射和心理温度。|wp-building-material,wp-vernacular-architecture|0|
gothic|以尖拱、肋拱与飞扶壁为特征的欧洲中世纪建筑风格。|中世纪、欧洲（参见来源）。|结构体系使墙体得以开出大面积窗户，形成高耸而明亮的内部空间。|wp-gothic-architecture,wp-architectural-style|0|
renaissance-style|复兴古典比例与秩序的欧洲建筑风格。|文艺复兴至19世纪、欧洲（参见来源）。|对称、柱式与几何比例成为表达理性与和谐的主要手段。|wp-renaissance-architecture,wp-alberti|0|
modernism|以功能、结构与简洁形式为核心的建筑思潮。|20世纪、全球（参见来源）。|现代主义反对历史样式复制，强调新材料、新结构与空间自由。|wp-modern-architecture,wp-le-corbusier|0|
bauhaus|把艺术、工艺与工业生产结合的设计学派。|20世纪、欧洲（参见来源）。|包豪斯影响了建筑与设计的教育方法，强调形式服从功能。|wp-bauhaus,wp-modern-architecture|0|
postmodernism|对现代主义单一理性提出反思、重视历史符号与装饰的建筑倾向。|20世纪、全球（参见来源）。|后现代建筑常以戏谑、折衷与隐喻回应地方和历史语境。|wp-postmodern-architecture,wp-architectural-style|0|
green-architecture|以降低环境影响为目标的建筑设计取向。|当代、全球（参见来源）。|绿色建筑关注能耗、水资源、材料循环与室内健康。|wp-green-building,wp-sustainable-architecture|0|
sustainable-architecture|兼顾生态、社会与经济长期性的建筑实践。|当代、全球（参见来源）。|可持续建筑把全生命周期影响纳入设计判断。|wp-sustainable-architecture,wp-passive-solar-building-design|0|
"""


def parse():
    rows = []
    for line in DATA.strip().splitlines():
        parts = line.split("|")
        if len(parts) != 7:
            raise ValueError(f"bad row: {line[:60]}")
        eid, definition, time_place, overview, srcs, flag, note = parts
        if eid not in META:
            raise ValueError(f"unknown id: {eid}")
        meta = META[eid]
        related = []
        pos = next((i for i, r in enumerate(COVERAGE["entries"]) if r["id"] == eid), -1)
        for nxt in COVERAGE["entries"][pos + 1:]:
            if nxt["theme"] == meta["theme"]:
                related = [nxt["id"]]
                break
        rows.append({
            "id": eid, "title": meta["title"], "level": "L1", "tier": meta["tier"],
            "theme": meta["theme"], "period": meta["period"], "region": meta["region"],
            "definition": definition, "time_or_place": time_place, "overview": overview,
            "related": related, "sources": [s for s in srcs.split(",") if s],
            "needs_verification": flag == "1", "pending_notes": note,
        })
    return rows


def main():
    rows = parse()
    size = 10
    for i in range(0, len(rows), size):
        batch = rows[i:i + size]
        name = f"batch-02-{chr(97 + i // size)}"
        out = ROOT / "entries" / f"{name}.json"
        out.write_text(json.dumps({"unit_id": name, "title": f"第2轮核心 L1（{i // size + 1}/4）", "entries": batch},
                                  ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{name}: {len(batch)} entries")
    print("total", len(rows))


if __name__ == "__main__":
    main()
