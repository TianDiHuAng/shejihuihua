"""第4轮：写作 deconstructivism（L2）并升级 6 个 L1 条目为 L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COVERAGE = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
META = {r["id"]: r for r in COVERAGE["entries"]}
ORDER = COVERAGE["entries"]
REG = "实际工程须按当地规范和专业设计人员的要求"

DECON_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<rect x='40' y='40' width='680' height='320' fill='none' stroke='var(--line)'/>"
    "<polygon points='120,300 260,110 330,300' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<polygon points='330,300 420,150 560,300' fill='none' stroke='var(--accent)'/>"
    "<polyline points='560,300 640,120 690,300' fill='none' stroke='var(--muted)'/>"
    "<line x1='120' y1='300' x2='690' y2='300' stroke='var(--ink)' stroke-width='2'/>"
    "<text x='150' y='80' fill='var(--ink)'>破碎几何与错位体块</text>"
    "<text x='300' y='365' fill='var(--muted)'>示意图，非施工图</text></svg>"
)
OPPOSED_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<line x1='80' y1='330' x2='680' y2='330' stroke='var(--ink)' stroke-width='3'/>"
    "<circle cx='130' cy='250' r='12' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<line x1='150' y1='245' x2='560' y2='190' stroke='var(--accent)' stroke-width='2'/>"
    "<polygon points='552,185 568,190 552,197' fill='var(--accent)'/>"
    "<rect x='560' y='150' width='90' height='80' fill='none' stroke='var(--muted)'/>"
    "<text x='90' y='290' fill='var(--ink)'>起点</text><text x='565' y='135' fill='var(--ink)'>对景终点</text>"
    "<text x='290' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
)
SCREEN_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<line x1='60' y1='330' x2='700' y2='330' stroke='var(--ink)' stroke-width='3'/>"
    "<rect x='250' y='140' width='90' height='190' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<circle cx='130' cy='250' r='12' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<line x1='150' y1='245' x2='245' y2='245' stroke='var(--muted)' stroke-width='2'/>"
    "<line x1='345' y1='245' x2='620' y2='200' stroke='var(--accent)' stroke-width='2'/>"
    "<text x='250' y='120' fill='var(--ink)'>障景墙体</text><text x='590' y='180' fill='var(--ink)'>揭示</text>"
    "<text x='290' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
)
WATER_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<rect x='60' y='200' width='640' height='130' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<polyline points='120,200 200,170 300,200 420,160 540,200 640,175' fill='none' stroke='var(--muted)'/>"
    "<circle cx='250' cy='260' r='26' fill='none' stroke='var(--accent)'/>"
    "<text x='90' y='370' fill='var(--ink)'>水面</text><text x='90' y='150' fill='var(--muted)'>岸线与池岛</text>"
    "<text x='300' y='45' fill='var(--muted)'>示意图，非施工图</text></svg>"
)
BRUT_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<rect x='120' y='120' width='520' height='220' fill='none' stroke='var(--accent)' stroke-width='3'/>"
    "<rect x='180' y='180' width='150' height='160' fill='var(--accent-soft)' stroke='var(--muted)'/>"
    "<rect x='380' y='150' width='190' height='190' fill='none' stroke='var(--muted)'/>"
    "<text x='160' y='90' fill='var(--ink)'>粗野混凝土体量</text>"
    "<text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
)
WELL_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<line x1='80' y1='90' x2='680' y2='90' stroke='var(--ink)' stroke-width='3'/>"
    "<rect x='300' y='90' width='160' height='230' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<line x1='380' y1='100' x2='380' y2='260' stroke='var(--accent)' stroke-width='2'/>"
    "<text x='100' y='70' fill='var(--ink)'>屋面</text><text x='325' y='345' fill='var(--ink)'>天井</text>"
    "<text x='300' y='380' fill='var(--muted)'>示意图，非施工图</text></svg>"
)
GLARE_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<rect x='100' y='90' width='560' height='250' fill='none' stroke='var(--line)'/>"
    "<rect x='140' y='120' width='120' height='160' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<line x1='270' y1='150' x2='560' y2='300' stroke='var(--accent)' stroke-width='3'/>"
    "<circle cx='570' cy='305' r='18' fill='none' stroke='var(--accent)'/>"
    "<text x='150' y='100' fill='var(--ink)'>窗</text><text x='580' y='280' fill='var(--ink)'>视线</text>"
    "<text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
)

UPGRADES = {
    "opposed-scenery": {
        "sections": {
            "原理": "对景把视线终点安排在路径或视线的端点，使空间具有明确的目的地与视觉落点。",
            "典型手法与适用条件": "在廊道尽头、院落轴线或转折处设置山石、建筑或树木；适用于视线可贯通且端点景物有辨识度的场景。",
            "实例": "名称：苏州古典园林对景实例；地点：中国苏州；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "端点景物过多会分散焦点；对景与动线方向不一致会造成观看混乱。" + REG,
            "一图": "见下方视线示意：起点经路径指向对景终点。",
            "待核实": "具体实例的设计者与年份待核实。",
        },
        "svg": [OPPOSED_SVG], "needs_verification": True,
        "pending_notes": "苏州园林对景具体实例的设计者与年份待补充独立来源。",
    },
    "screened-scenery": {
        "sections": {
            "原理": "障景以墙体或植物暂时遮挡视线，再通过转折揭示景物，形成先抑后扬的体验。",
            "典型手法与适用条件": "在入口或路径转折处设置影壁、山石或树丛；适用于希望控制揭示节奏、避免一览无余的空间。",
            "实例": "名称：苏州古典园林障景实例；地点：中国苏州；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "遮挡过度会使空间显得闭塞；通行宽度不足会影响安全与无障碍。" + REG,
            "一图": "见下方平面示意：障景墙体遮挡后于转折处揭示景物。",
            "待核实": "具体实例的设计者与年份待核实。",
        },
        "svg": [SCREEN_SVG], "needs_verification": True,
        "pending_notes": "苏州园林障景具体实例的设计者与年份待补充独立来源。",
    },
    "water-management": {
        "sections": {
            "原理": "理水通过水面形状、岸线曲折与池岛布置组织视线、声音和微气候。",
            "典型手法与适用条件": "集中水面适合形成静观中心，曲折水道适合延长游线；需结合排水与水源条件。",
            "实例": "名称：苏州古典园林水面；地点：中国苏州；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "水面封闭或补水不足会水质恶化；池岸高差与防滑需要专门处理。" + REG,
            "一图": "见下方水面与岸线示意，仅表达构图关系。",
            "待核实": "具体水面实例的设计者与年份待核实。",
        },
        "svg": [WATER_SVG], "needs_verification": True,
        "pending_notes": "苏州园林水面实例的设计者与年份待补充独立来源。",
    },
    "brutalism": {
        "sections": {
            "原理": "粗野主义以暴露的混凝土结构和大体量表达材料的真实性与社会性。",
            "典型手法与适用条件": "适用于公共建筑与纪念性项目；需要以结构清晰、体量组合明确为前提。",
            "实例": "名称：粗野主义公共建筑；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "混凝土表面维护不足会显得破旧；尺度过大可能压迫街道空间。" + REG,
            "一图": "见下方体量示意图，表达结构暴露与组合关系。",
            "待核实": "具体实例名称、地点与设计者待核实。",
        },
        "svg": [BRUT_SVG], "needs_verification": True,
        "pending_notes": "粗野主义具体实例的地点、设计者与年份待补充独立来源。",
    },
    "light-well": {
        "sections": {
            "原理": "天井以狭长开口把天然光引入建筑深处，并通过热压促进空气流动。",
            "典型手法与适用条件": "适用于进深大、外墙开窗受限的民居或公共建筑；需结合当地气候与朝向。",
            "实例": "名称：传统民居天井；地点：待核实；设计者：不适用；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "开口尺寸过小会采光不足；雨水倒灌与高空坠物需防护。" + REG,
            "一图": "见下方剖面示意：屋面开口把光引入内部。",
            "待核实": "具体民居实例的采光实测数据待核实。",
        },
        "svg": [WELL_SVG], "needs_verification": True,
        "pending_notes": "天井实例的采光与通风实测数据待补充独立来源。",
    },
    "glare": {
        "sections": {
            "原理": "眩光来自视野内过亮的表面或直射光，降低视觉舒适度与识别能力。",
            "典型手法与适用条件": "通过遮阳、反射面控制与工位朝向避开高亮度光源；适用于长时间停留的室内空间。",
            "实例": "名称：办公空间侧窗眩光控制；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "只降低整体照度会牺牲任务可见度；窗面尺寸与遮阳构造需综合判断。" + REG,
            "一图": "见下方视线示意：窗与工作位之间需避免直射。",
            "待核实": "具体办公实例的照度与眩光指数待核实。",
        },
        "svg": [GLARE_SVG], "needs_verification": True,
        "pending_notes": "办公实例的照度与眩光实测数据待补充独立来源。",
    },
}


NEW_L2_SOURCES = {
    "water-management": ["wp-chinese-garden", "wp-garden-design"],
    "brutalism": ["wp-brutalist-architecture", "wp-architectural-style"],
    "light-well": ["wp-atrium-architecture", "wp-chinese-architecture"],
    "glare": ["wp-daylighting-architecture", "wp-architectural-lighting-design"],
}


def related_for(eid):
    meta = META[eid]
    pos = next(i for i, r in enumerate(ORDER) if r["id"] == eid)
    for nxt in ORDER[pos + 1:]:
        if nxt["theme"] == meta["theme"]:
            return [nxt["id"]]
    return []


def main():
    meta = META["deconstructivism"]
    decon = {
        "id": "deconstructivism", "title": meta["title"], "level": "L2",
        "tier": meta["tier"], "theme": meta["theme"], "period": meta["period"], "region": meta["region"],
        "definition": "以破碎几何、错位体块与结构不确定性挑战传统秩序的建筑倾向。",
        "time_or_place": "20世纪后期、全球（参见来源）。",
        "overview": "解构主义通过非直线、非对称的形式制造张力，近年仍有代表性文化建筑项目推进。",
        "related": related_for("deconstructivism"),
        "sections": {
            "原理": "解构主义把建筑形式从秩序与轴线中释放，利用错位、倾斜与片段化表达不稳定感。",
            "典型手法与适用条件": "以几何分解、体块穿插和结构外显形成视觉张力；适合文化展示类建筑，对施工精度要求较高。",
            "实例": "名称：Guggenheim Abu Dhabi；地点：阿布扎比；设计者：Frank Gehry；年份：预计 2026 年 12 月开馆（来源页面表述）。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "形式碎片化可能损害使用效率与导向；结构尺寸与施工可行性须专门论证。" + REG,
            "一图": "见下方示意：破碎几何与错位体块。",
            "待核实": "实例开馆时间为来源页面预计表述，实际状态待核实。",
        },
        "svg": [DECON_SVG],
        "sources": ["wp-deconstructivism", "wp-2026-in-architecture", "wp-postmodern-architecture"],
        "needs_verification": True,
        "pending_notes": "Guggenheim Abu Dhabi 的实际开馆时间与作品归属待后续核对。",
    }
    existing_ids = set()
    for p in (ROOT / "entries").glob("*.json"):
        for e in json.loads(p.read_text(encoding="utf-8")).get("entries", []):
            existing_ids.add(e["id"])
    new_l2 = []
    for eid, up in UPGRADES.items():
        if eid in existing_ids:
            continue
        meta = META[eid]
        new_l2.append({
            "id": eid, "title": meta["title"], "level": "L2", "tier": meta["tier"],
            "theme": meta["theme"], "period": meta["period"], "region": meta["region"],
            "definition": up["sections"]["原理"].split("。")[0] + "。",
            "time_or_place": f"{meta['period']}、{meta['region']}（参见来源）。",
            "overview": up["sections"]["典型手法与适用条件"],
            "related": related_for(eid), "sections": up["sections"], "svg": up["svg"],
            "sources": NEW_L2_SOURCES[eid], "needs_verification": up["needs_verification"],
            "pending_notes": up["pending_notes"],
        })
    out = ROOT / "entries" / "batch-04.json"
    out.write_text(json.dumps({"unit_id": "batch-04", "title": "第4轮新写条目", "entries": [decon] + new_l2},
                              ensure_ascii=False, indent=2), encoding="utf-8")

    upgraded = []
    for path in sorted((ROOT / "entries").glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for entry in doc.get("entries", []):
            if entry["id"] not in UPGRADES:
                continue
            up = UPGRADES[entry["id"]]
            entry["level"] = "L2"
            entry["sections"] = up["sections"]
            entry["svg"] = up["svg"]
            entry["needs_verification"] = up["needs_verification"]
            entry["pending_notes"] = up["pending_notes"]
            upgraded.append(entry["id"])
            changed = True
        if changed:
            path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"batch-04 written={1 + len(new_l2)} upgraded={len(upgraded)}")


if __name__ == "__main__":
    main()
