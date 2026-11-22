"""第41轮：新增 sfumato 与 trompe-l'oeil 两条，L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"
NEW = [
    ("artincontext-sfumato", "Sfumato — Art in Context", "https://artincontext.org/sfumato/", "Art in Context", "学术著作", "渐隐法柔和色彩过渡、模拟失焦"),
    ("wp-trompe-loeil", "Trompe-l'œil", "https://en.wikipedia.org/wiki/Trompe-l%27%C5%93il", "Wikipedia", "学术著作", "以二维平面临摹三维空间与物体的视错觉（经镜像核验）"),
    ("artincontext-trompe", "Trompe l'oeil — Art in Context", "https://artincontext.org/trompe-loeil/", "Art in Context", "学术著作", "错视画制造三维错觉"),
    ("designingbuildings-trompe", "Trompe l'oeil — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Trompe_l%27oeil", "Designing Buildings", "学术著作", "建筑中的错视画扩展空间错觉"),
]
SVG_S = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><ellipse cx='300' cy='200' rx='120' ry='90' fill='var(--accent-soft)' stroke='var(--accent)'/><ellipse cx='460' cy='200' rx='120' ry='90' fill='var(--panel)' stroke='var(--line)'/><path d='M 380 120 Q 380 200 380 280' stroke='var(--muted)' fill='none'/><text x='40' y='40' fill='var(--ink)'></text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_T = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='160' y='120' width='440' height='180' fill='none' stroke='var(--accent)'/><polygon points='160,120 400,60 640,120 400,180' fill='var(--accent-soft)' stroke='var(--muted)'/><text x='40' y='40' fill='var(--ink)'></text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>"

DATA = {
"sfumato": dict(defn="渐隐法（Sfumato）指以极柔和的明暗与色彩过渡、消除硬边以模拟失焦与空气感。", tp="文艺复兴至19世纪、欧洲（参见来源）。", ov="它让轮廓在明暗中消融，营造朦胧与真实感，与硬朗的明暗对比不同。",
    prin="以多层薄涂让色与形的边界逐渐消失，视觉上模拟景深失焦，使形体仿佛融入空气。", method="以极薄的透明色层反复罩染、柔化轮廓与明暗交界。",
    inst="名称：渐隐法的人物面部（类型性描述）；地点与设计者不适用。看轮廓如何在明暗中消融。", cap="见下方示意：柔和过渡消除硬边。", limit="过度柔化会失结构；需保留转折。", srcs=["wp-sfumato", "artincontext-sfumato"]),
"trompe-loeil": dict(defn="错视画（Trompe-l'œil）指以高度写实手法在平面上制造三维空间与物体假象的绘画。", tp="文艺复兴至19世纪、欧洲（参见来源）。", ov="它借透视、明暗与投影让人误以为墙面、穹顶或凹龛是真实空间。",
    prin="以精确透视、明暗与投影欺骗视觉，让二维表面呈现出三维的空间、构件或开口。", method="在墙面或穹顶以透视绘制假窗、假穹顶与假构件，配合真实光线。",
    inst="名称：穹顶错视天顶画（类型性描述）；地点与设计者不适用。看假穹顶如何被当真。", cap="见下方示意：平面临摹出的三维假象。", limit="视点偏移会穿帮；需按观看位置设计。", srcs=["wp-trompe-loeil", "artincontext-trompe", "designingbuildings-trompe"]),
}

cov = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))["entries"]
META = {r["id"]: r for r in cov}


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        data["sources"].append({
            "id": sid, "title": title, "author": author, "type": typ,
            "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
            "note": f"访问于 2026-11-23，由核验子任务实抓 HTTP 200/镜像核验并核对正文；{note}",
        })
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    rows = []
    for eid, f in DATA.items():
        m = META[eid]
        svg = (SVG_S if eid == "sfumato" else SVG_T)
        svg = svg.replace("<text x='40' y='40' fill='var(--ink)'></text>", "<text x='40' y='40' fill='var(--ink)'>" + m["title"] + "</text>")
        rows.append({
            "id": eid, "title": m["title"], "level": "L2", "tier": m["tier"],
            "theme": m["theme"], "period": m["period"], "region": m["region"],
            "definition": f["defn"], "time_or_place": f["tp"], "overview": f["ov"], "related": [],
            "sections": {"原理": f["prin"], "典型手法与适用条件": f["method"], "实例": f["inst"],
                         "常见错误与限制": f["limit"] + REG, "一图": f["cap"],
                         "待核实": "「%s」的具体实例（作品、作者、年代）待补充独立来源。" % m["title"]},
            "svg": [svg], "sources": f["srcs"], "needs_verification": True,
            "pending_notes": "「%s」的具体实例（作品、作者、年代）待补充独立来源。" % m["title"],
        })
    out = ROOT / "entries" / "batch-41.json"
    out.write_text(json.dumps({"unit_id": "batch-41", "title": "第41轮新增条目", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-41 written", len(rows))


if __name__ == "__main__":
    main()
