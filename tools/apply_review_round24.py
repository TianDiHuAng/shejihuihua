"""第24轮复核应用：spatial-organization（萨伏伊别墅）双源升级；green-architecture 评价数据补第二源。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("fondationlc-villa-savoye", "Villa Savoye — Fondation Le Corbusier", "https://www.fondationlecorbusier.fr/en/work-architecture/achievements-villa-savoye-and-gardeners-lodge-poissy-france-1928-1931/", "Fondation Le Corbusier", "官方机构", "记载萨伏伊别墅位于普瓦西，勒·柯布西耶与皮埃尔·让纳雷，1928–1931"),
    ("villasavoye-promenade", "An Architectural Promenade — Villa Savoye (CMN)", "https://www.villa-savoye.fr/en/discover/an-architectural-promenade", "Centre des monuments nationaux", "官方机构", "记载建筑漫步、坡道与连续空间组织"),
    ("changzhou-gxzj", "高新智汇中心 — 常州市人民政府", "https://www.changzhou.gov.cn/gi_news/828161639281792", "常州市人民政府", "官方机构", "点名高新智汇中心绿色建筑三星/示范项目"),
    ("xinhua-js-green", "绿色建筑三星项目高新智汇中心 — 新华网江苏", "https://js.news.cn/20250407/5442dcc356fc4d69b0c26cf04381435d/c.html", "新华网", "官方机构", "记载高新智汇中心为绿色建筑三星项目"),
]


def main():
    path = ROOT / "data" / "sources.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    added = []
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        data["sources"].append({
            "id": sid, "title": title, "author": author, "type": typ,
            "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
            "note": f"访问于 2026-11-22，由核验子任务实抓 HTTP 200 并核对正文；{note}",
        })
        added.append(sid)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            k = e["id"]
            if k == "spatial-organization":
                e["sections"]["实例"] = "名称：萨伏伊别墅（Villa Savoye）；地点：法国普瓦西（Poissy）；设计者：勒·柯布西耶与皮埃尔·让纳雷（Le Corbusier & Pierre Jeanneret）；年份：1928–1931 年。以坡道与连续流线组织“建筑漫步”的串联式空间。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项。"
                for r in ["fondationlc-villa-savoye", "villasavoye-promenade"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            elif k == "green-architecture":
                e["sections"]["待核实"] = "设计者（南京工业大学建筑设计研究院）与 2018 年设计年代仍为单一来源，待补充；三星级/示范工程评价数据已有多源。"
                for r in ["changzhou-gxzj", "xinhua-js-green"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "设计者与 2018 设计年代仍单源，待补充；评价数据已多源。"
                ch = True
            else:
                continue
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added", added)


if __name__ == "__main__":
    main()
