"""第5轮：新写 5 条重要 L2，并把 chinese-architecture-style 升级到 L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COVERAGE = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
META = {r["id"]: r for r in COVERAGE["entries"]}
ORDER = COVERAGE["entries"]
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG_LEAK = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='60' y='90' width='240' height='220' fill='none' stroke='var(--accent)'/><rect x='330' y='130' width='24' height='180' fill='var(--accent-soft)' stroke='var(--accent)'/><circle cx='460' cy='210' r='70' fill='none' stroke='var(--muted)'/><line x1='170' y1='210' x2='455' y2='210' stroke='var(--accent)' stroke-width='2'/><text x='90' y='75' fill='var(--ink)'>园内</text><text x='415' y='130' fill='var(--ink)'>园外景物</text><text x='320' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_HUIZHOU = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='80' y1='300' x2='680' y2='300' stroke='var(--ink)' stroke-width='3'/><polygon points='180,300 180,170 360,110 540,170 540,300' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='230' y='210' width='70' height='90' fill='none' stroke='var(--muted)'/><rect x='460' y='210' width='70' height='90' fill='none' stroke='var(--muted)'/><text x='315' y='80' fill='var(--ink)'>粉墙黛瓦与马头墙</text><text x='300' y='350' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_VERNAC = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='100' width='600' height='220' fill='none' stroke='var(--line)'/><rect x='120' y='140' width='160' height='180' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='320' y='120' width='120' height='200' fill='none' stroke='var(--muted)'/><rect x='480' y='160' width='160' height='160' fill='none' stroke='var(--accent)'/><text x='170' y='75' fill='var(--ink)'>地域材料与砌筑方式</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_BYZ = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='150' y='110' width='460' height='230' fill='none' stroke='var(--accent)'/><path d='M 250 340 L 250 180 Q 380 90 510 180 L 510 340' fill='var(--accent-soft)' stroke='var(--muted)'/><circle cx='380' cy='150' r='30' fill='none' stroke='var(--accent)'/><text x='280' y='80' fill='var(--ink)'>中央穹顶与集中式构图</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_GREEK = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='120' y1='300' x2='640' y2='300' stroke='var(--ink)' stroke-width='3'/><line x1='160' y1='300' x2='160' y2='140' stroke='var(--accent)' stroke-width='16'/><line x1='250' y1='300' x2='250' y2='140' stroke='var(--accent)' stroke-width='16'/><line x1='340' y1='300' x2='340' y2='140' stroke='var(--accent)' stroke-width='16'/><line x1='130' y1='130' x2='370' y2='130' stroke='var(--muted)' stroke-width='10'/><polygon points='120,130 250,70 380,130' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='440' y='180' fill='var(--ink)'>柱式与檐部秩序</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_CHINESE = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='80' y1='320' x2='680' y2='320' stroke='var(--ink)' stroke-width='3'/><rect x='130' y='180' width='130' height='140' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='315' y='140' width='130' height='180' fill='none' stroke='var(--accent)'/><rect x='500' y='180' width='130' height='140' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='220' y='150' fill='var(--ink)'>院落序列</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"

NEW = {
    "leaked-scenery": {
        "sources": ["wp-chinese-garden", "wp-garden-design"], "svg": [SVG_LEAK],
        "definition": "漏景是通过缝隙或稀疏遮挡让景物片段显现的造景手法。",
        "time_or_place": "古代中国（参见来源）。",
        "overview": "与一次性揭示不同，漏景让景物在移动中被断续看到，形成节奏。",
        "sections": {
            "原理": "视线通过花墙、枝隙或格栅被切分，景物以片段形式进入感知，激发补完联想。",
            "典型手法与适用条件": "在游线旁设置透空隔断或疏植，适用于希望保持空间连续但又避免一览无余的路径。",
            "实例": "名称：苏州古典园林漏窗；地点：中国苏州；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "缝隙过密会造成视觉噪声；遮挡构件应兼顾结构与通行安全。" + REG,
            "一图": "见下方示意：园内视线经洞口片段望向园外景物。",
            "待核实": "具体漏窗实例的设计者与年份待核实。",
        },
        "needs_verification": True, "pending_notes": "园林漏景具体实例的设计者与年份待补充独立来源。",
    },
    "huizhou-style": {
        "sources": ["wp-chinese-architecture", "wp-vernacular-architecture"], "svg": [SVG_HUIZHOU],
        "definition": "徽派建筑是流行于徽州地区、以粉墙黛瓦、马头墙与院落组合为特征的乡土建筑。",
        "time_or_place": "古代、中国（参见来源）。",
        "overview": "聚落依地形展开，白色墙面与深色屋面形成强烈对比，防火山墙成为地域标志。",
        "sections": {
            "原理": "高密度聚落中，墙体既界定院落也承担防火与防风；材料色彩回应潮湿气候。",
            "典型手法与适用条件": "以天井组织采光排水，以马头墙分隔相邻屋顶；适用于山地与紧凑村落肌理。",
            "实例": "名称：徽州传统民居；地点：中国安徽；设计者：不适用；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "马头墙构造尺寸与防火间距须依当地规范；旅游开发中的立面仿制容易丢失原本空间逻辑。" + REG,
            "一图": "见下方剖面概念图：粉墙、黛瓦与马头墙。",
            "待核实": "具体村落的建造年代与营造者待核实。",
        },
        "needs_verification": True, "pending_notes": "徽州民居具体村落年代与营造者待补充独立来源。",
    },
    "vernacular-material": {
        "sources": ["wp-building-material", "wp-vernacular-architecture"], "svg": [SVG_VERNAC],
        "definition": "乡土材料是就地取得、与当地气候和营造技艺相适应的建筑材料。",
        "time_or_place": "跨时期、全球（参见来源）。",
        "overview": "材料选择受资源、运输与工艺共同制约，因而呈现鲜明的地域差异。",
        "sections": {
            "原理": "就地取材减少运输能耗，材料的蓄热、透气与耐候性能与当地气候长期适配。",
            "典型手法与适用条件": "木、石、夯土、竹等按可获得性与结构角色组合；适用于尊重地域景观的营造。",
            "实例": "名称：地域乡土建筑；地点：待核实；设计者：不适用；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "直接移植他地材料会破坏景观协调；材料尺寸与防火性能须依规范校核。" + REG,
            "一图": "见下方材料组合示意：不同质感对应不同空间性格。",
            "待核实": "具体地区的材料性能数据待核实。",
        },
        "needs_verification": True, "pending_notes": "具体地区乡土材料的性能数据待补充独立来源。",
    },
    "byzantine": {
        "sources": ["wp-byzantine-architecture", "wp-architectural-style"], "svg": [SVG_BYZ],
        "definition": "拜占庭建筑是以中央穹顶、集中式构图和马赛克装饰为特征的东罗马建筑传统。",
        "time_or_place": "中世纪、欧洲（参见来源）。",
        "overview": "穹顶与鼓座把集中式空间推向垂直方向，光线与金色表面共同塑造神圣氛围。",
        "sections": {
            "原理": "帆拱把方形平面上的穹顶荷载传到四角柱，使集中式空间获得结构可能。",
            "典型手法与适用条件": "以穹顶为中心组织前廊与侧廊；适用于教堂与纪念性空间。",
            "实例": "名称：拜占庭教堂建筑；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "只看装饰会忽略结构逻辑；穹顶跨度与支承条件需专业设计。" + REG,
            "一图": "见下方集中式构图示意：中央穹顶与方形基座。",
            "待核实": "具体教堂的设计者与年份待核实。",
        },
        "needs_verification": True, "pending_notes": "拜占庭教堂具体实例的设计者与年份待补充独立来源。",
    },
    "ancient-greek": {
        "sources": ["wp-ancient-greek-architecture", "wp-classical-architecture"], "svg": [SVG_GREEK],
        "definition": "古希腊建筑以柱式体系、檐部比例和神庙平面秩序为基础。",
        "time_or_place": "古代、欧洲（参见来源）。",
        "overview": "多立克、爱奥尼与科林斯柱式把结构构件转化为可识别的比例语言。",
        "sections": {
            "原理": "柱径、柱距与檐部高度之间存在可感知的比例关系，使建筑呈现秩序与尺度感。",
            "典型手法与适用条件": "以柱廊围合神庙，按柱式确定细部；适用于纪念性与公共建筑的形式参考。",
            "实例": "名称：古希腊神庙；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "脱离结构比例复制柱式会沦为布景；石材尺寸与抗震须按当地规范。" + REG,
            "一图": "见下方柱式与檐部秩序示意。",
            "待核实": "具体神庙的设计者与年份待核实。",
        },
        "needs_verification": True, "pending_notes": "古希腊神庙具体实例的设计者与年份待补充独立来源。",
    },
}


def related_for(eid):
    pos = next(i for i, r in enumerate(ORDER) if r["id"] == eid)
    for nxt in ORDER[pos + 1:]:
        if nxt["theme"] == META[eid]["theme"]:
            return [nxt["id"]]
    return []


def main():
    new_entries = []
    for eid, spec in NEW.items():
        meta = META[eid]
        new_entries.append({
            "id": eid, "title": meta["title"], "level": "L2", "tier": meta["tier"],
            "theme": meta["theme"], "period": meta["period"], "region": meta["region"],
            "definition": spec["definition"], "time_or_place": spec["time_or_place"],
            "overview": spec["overview"], "related": related_for(eid),
            "sections": spec["sections"], "svg": spec["svg"], "sources": spec["sources"],
            "needs_verification": spec["needs_verification"], "pending_notes": spec["pending_notes"],
        })
    out = ROOT / "entries" / "batch-05.json"
    out.write_text(json.dumps({"unit_id": "batch-05", "title": "第5轮新写 L2", "entries": new_entries},
                              ensure_ascii=False, indent=2), encoding="utf-8")

    upgraded = 0
    for path in (ROOT / "entries").glob("*.json"):
        doc = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for entry in doc.get("entries", []):
            if entry["id"] != "chinese-architecture-style":
                continue
            entry["level"] = "L2"
            entry["sections"] = {
                "原理": "木构框架把荷载传到柱与梁，墙体不承重，因而可形成灵活的门窗与院落组织。",
                "典型手法与适用条件": "以院落串联不同等级的空间，用对称与轴线表达秩序；适用于礼制与居住建筑。",
                "实例": "名称：中国传统院落建筑；地点：中国；设计者：不适用；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
                "常见错误与限制": "木构防火与防腐须专门处理；木料尺寸与连接方式按当地规范设计。" + REG,
                "一图": "见下方院落序列示意：三个院落沿轴线组织。",
                "待核实": "具体院落实例的建造年代与营造者待核实。",
            }
            entry["svg"] = [SVG_CHINESE]
            entry["needs_verification"] = True
            entry["pending_notes"] = "具体院落实例的建造年代与营造者待补充独立来源。"
            upgraded += 1
            changed = True
        if changed:
            path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"batch-05 written={len(new_entries)} upgraded={upgraded}")


if __name__ == "__main__":
    main()
