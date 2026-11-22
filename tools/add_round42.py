"""第42轮：新增 hatching、stippling 两条，L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"
NEW = [
    ("wp-hatching", "Hatching", "https://en.wikipedia.org/wiki/Hatching", "Wikipedia", "学术著作", "以密集平行线表现明暗（经镜像核验）"),
    ("artincontext-hatching", "Cross Hatching — Art in Context", "https://artincontext.org/cross-hatching/", "Art in Context", "学术著作", "排线与交叉排线叠加明暗"),
    ("wp-stippling", "Stippling", "https://en.wikipedia.org/wiki/Stippling", "Wikipedia", "学术著作", "以细点疏密表现明暗（经镜像核验）"),
    ("artincontext-stippling", "Stippling Art — Art in Context", "https://artincontext.org/stippling-art/", "Art in Context", "学术著作", "以点描绘制图像"),
]
SVG_H = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><g stroke='var(--accent)'><line x1='180' y1='120' x2='240' y2='280'/><line x1='210' y1='120' x2='270' y2='280'/><line x1='240' y1='120' x2='300' y2='280'/><line x1='270' y1='120' x2='330' y2='280'/></g><g stroke='var(--muted)'><line x1='420' y1='140' x2='560' y2='140'/><line x1='420' y1='180' x2='560' y2='180'/><line x1='420' y1='220' x2='560' y2='220'/></g><text x='40' y='40' fill='var(--ink)'></text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_D = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='250' cy='200' r='90' fill='none' stroke='var(--accent)' stroke-dasharray='2 10'/><circle cx='480' cy='200' r='70' fill='none' stroke='var(--muted)' stroke-dasharray='1 14'/><text x='40' y='40' fill='var(--ink)'></text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>"
DATA = {
"hatching": dict(defn="排线法（Hatching）指以密集的平行线表现明暗与质感，交叉排线则叠加多组线以加深色调。", tp="文艺复兴至19世纪、欧洲（参见来源）。", ov="线条越密越暗、越疏越亮，交叉排线可层层加深。",
   prin="线条的疏密与交叉层数决定局部明度，是版画、素描与铜版画塑造体积的常用手段。", method="以平行线铺底、交叉线加深，按形体走向安排线组方向。",
   inst="名称：铜版画的排线明暗（类型性描述）；地点与设计者不适用。看交叉线如何加深暗部。", cap="见下方示意：平行线与交叉线叠加明暗。", limit="线条杂乱会脏；方向不符会失形体。", srcs=["wp-hatching", "artincontext-hatching"]),
"stippling": dict(defn="点描法（Stippling）指以细点的疏密表现明暗与形体的绘制技法。", tp="文艺复兴至19世纪、欧洲（参见来源）。", ov="点越密越暗、越疏越亮，靠点的聚集塑造渐变。",
   prin="单位面积内点的数量决定局部明度，靠点阵密度模拟连续调子。", method="以细密点阵逐层加密表现暗部，靠疏密过渡表现亮部。",
   inst="名称：点描的生物插画（类型性描述）；地点与设计者不适用。看点密度如何塑造体积。", cap="见下方示意：点的疏密形成明暗。", limit="点过大或过匀会失层次；需耐心分层。", srcs=["wp-stippling", "artincontext-stippling"]),
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
        data["sources"].append({"id": sid, "title": title, "author": author, "type": typ,
                                "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
                                "note": f"访问于 2026-11-23，经实抓/镜像核验；{note}"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    rows = []
    for eid, f in DATA.items():
        m = META[eid]
        svg = (SVG_H if eid == "hatching" else SVG_D).replace("<text x='40' y='40' fill='var(--ink)'></text>", "<text x='40' y='40' fill='var(--ink)'>" + m["title"] + "</text>")
        rows.append({"id": eid, "title": m["title"], "level": "L2", "tier": m["tier"],
                     "theme": m["theme"], "period": m["period"], "region": m["region"],
                     "definition": f["defn"], "time_or_place": f["tp"], "overview": f["ov"], "related": [],
                     "sections": {"原理": f["prin"], "典型手法与适用条件": f["method"], "实例": f["inst"],
                                  "常见错误与限制": f["limit"] + REG, "一图": f["cap"],
                                  "待核实": "「%s」的具体实例（作品、作者、年代）待补充独立来源。" % m["title"]},
                     "svg": [svg], "sources": f["srcs"], "needs_verification": True,
                     "pending_notes": "「%s」的具体实例（作品、作者、年代）待补充独立来源。" % m["title"]})
    out = ROOT / "entries" / "batch-42.json"
    out.write_text(json.dumps({"unit_id": "batch-42", "title": "第42轮新增条目", "entries": rows}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-42 written", len(rows))


if __name__ == "__main__":
    main()
