"""第47轮：新增 3 条填满稀疏格（地坑院/萨珊/奥斯曼），L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"
NEW = [
    ("smx-shanzhou-dikengyuan", "陕州地坑院 — 三门峡市人民政府", "https://www.smx.gov.cn/4138/614864448/732660.html", "三门峡市人民政府", "官方机构", "地坑院：地平线下古村落、国家级非遗营造技艺"),
    ("wp-sasanian-architecture", "Sasanian architecture", "https://en.wikipedia.org/wiki/Sasanian_architecture", "Wikipedia", "权威百科", "萨珊波斯建筑 224–651，筒拱伊万，被伊斯兰建筑吸收（经镜像核验）"),
    ("artincontext-persian-art", "Persian Art — Art in Context", "https://artincontext.org/persian-art/", "Art in Context", "学术著作", "萨珊建筑：穹顶厅、筒拱、伊万、宫殿与火庙"),
    ("wp-ottoman-architecture", "Ottoman architecture", "https://en.wikipedia.org/wiki/Ottoman_architecture", "Wikipedia", "权威百科", "古典奥斯曼 16–17 世纪，中央大穹顶＋半穹顶（经镜像核验）"),
    ("artincontext-islamic-architecture", "Islamic Architecture — Art in Context", "https://artincontext.org/islamic-architecture/", "Art in Context", "学术著作", "奥斯曼：中央穹顶、集中式平面、Sinan"),
]
D = {
"dikengyuan": dict(
  defn="地坑院（下沉式窑院）是在黄土塬面向下挖方形坑、再沿四壁横向挖窑而成的地下四合院。",
  tp="古代、中国（参见来源）。", ov="院落地平线以下，以坑为院、四壁为窑，形成“进村不见房”的地下聚落。",
  prin="黄土直立性强，可先向下挖坑作院，再沿四壁横向挖拱形窑洞，借土体保温隔热。",
  method="在平坦塬面下挖方形天井作院，沿四壁挖窑并设通道与排水。",
  inst="名称：陕州地坑院（类型性描述）；地点与设计者不适用。看坑院与四壁窑洞的关系。",
  cap="见下方示意：下沉坑院与四壁窑洞剖面。", limit="排水与防塌是关键；须按规范加固。",
  srcs=["wp-yaodong", "smx-shanzhou-dikengyuan"]),
"sasanian-architecture": dict(
  defn="萨珊建筑是 224–651 年波斯萨珊王朝的建筑，以筒拱、穹顶与伊万（iwan）为特征。",
  tp="古代、伊斯兰/南亚（前伊斯兰波斯，iwan 源头；参见来源）。", ov="其伊万与穹顶形制被伊斯兰建筑广泛吸收。",
  prin="以筒拱与穹顶覆盖大空间，以三面围合、一面敞开的伊万作为入口与厅堂。",
  method="以砖石筒拱、穹顶与伊万组织宫殿与火庙。",
  inst="名称：萨珊宫殿与火庙（类型性描述）；地点与设计者不适用。看伊万与筒拱。",
  cap="见下方示意：伊万与筒拱。", limit="拱顶推力需厚墙平衡；按规范。",
  srcs=["wp-sasanian-architecture", "artincontext-persian-art"]),
"ottoman-architecture": dict(
  defn="奥斯曼建筑是奥斯曼帝国的建筑，古典期（16–17 世纪）以中央大穹顶加半穹顶的集中式清真寺为标志。",
  tp="文艺复兴至19世纪、伊斯兰/南亚（参见来源）。", ov="以层层递落的穹顶体系覆盖宽阔礼拜空间，由建筑师锡南推向成熟。",
  prin="以中央大穹顶统摄、四周半穹顶与拱券传递推力，形成开阔而集中的礼拜空间。",
  method="以中央穹顶＋半穹顶、铅皮覆盖与光窗组织清真寺。",
  inst="名称：古典奥斯曼集中式清真寺（类型性描述）；地点与设计者不适用。看中央穹顶与半穹顶。",
  cap="见下方示意：中央穹顶与半穹顶体系。", limit="穹顶推力的扶壁处理是关键；按规范。",
  srcs=["wp-ottoman-architecture", "artincontext-islamic-architecture"]),
}
SVGS = [
 "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='80' y1='180' x2='680' y2='180' stroke='var(--ink)' stroke-width='2'/><rect x='240' y='180' width='280' height='140' fill='none' stroke='var(--accent)'/><rect x='270' y='210' width='60' height='80' fill='var(--panel)' stroke='var(--muted)'/><rect x='430' y='210' width='60' height='80' fill='var(--panel)' stroke='var(--muted)'/><text x='40' y='40' fill='var(--ink)'>{t}</text><text x='300' y='380' fill='var(--muted)'>示意图，非施工图</text></svg>",
 "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><path d='M 200 300 L 200 170 Q 300 90 400 170 L 400 300' fill='none' stroke='var(--accent)'/><rect x='430' y='180' width='200' height='120' fill='none' stroke='var(--muted)'/><line x1='430' y1='180' x2='630' y2='180' stroke='var(--muted)'/><text x='40' y='40' fill='var(--ink)'>{t}</text><text x='300' y='380' fill='var(--muted)'>示意图，非施工图</text></svg>",
 "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><path d='M 380 120 Q 300 120 300 180 L 300 300' fill='none' stroke='var(--accent)'/><path d='M 380 120 Q 460 120 460 180 L 460 300' fill='none' stroke='var(--accent)'/><path d='M 380 120 Q 240 140 220 220 L 220 300' fill='none' stroke='var(--muted)'/><path d='M 380 120 Q 520 140 540 220 L 540 300' fill='none' stroke='var(--muted)'/><line x1='180' y1='300' x2='580' y2='300' stroke='var(--ink)' stroke-width='2'/><text x='40' y='40' fill='var(--ink)'>{t}</text><text x='300' y='380' fill='var(--muted)'>示意图，非施工图</text></svg>",
]

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
    for i, (eid, f) in enumerate(D.items()):
        m = META[eid]
        rows.append({"id": eid, "title": m["title"], "level": "L2", "tier": m["tier"],
                     "theme": m["theme"], "period": m["period"], "region": m["region"],
                     "definition": f["defn"], "time_or_place": f["tp"], "overview": f["ov"], "related": [],
                     "sections": {"原理": f["prin"], "典型手法与适用条件": f["method"], "实例": f["inst"],
                                  "常见错误与限制": f["limit"] + REG, "一图": f["cap"],
                                  "待核实": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"]},
                     "svg": [SVGS[i % 3].replace("{t}", m["title"])], "sources": f["srcs"], "needs_verification": True,
                     "pending_notes": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"]})
    out = ROOT / "entries" / "batch-47.json"
    out.write_text(json.dumps({"unit_id": "batch-47", "title": "第47轮稀疏格补条目", "entries": rows}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-47 written", len(rows))


if __name__ == "__main__":
    main()
