"""第23轮复核应用：sustainable-architecture（The Edge）、sunken-accessibility（Peavey Plaza）双源升级；vitruvian-triad 收窄。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("breeam-the-edge", "The Edge, Amsterdam — BREEAM", "https://breeam.com/web/bre-group/case-studies/the-edge-amsterdam", "BRE Group / BREEAM", "官方机构", "记载 The Edge 阿姆斯特丹、BREEAM-NL Outstanding、约98.3%"),
    ("edge-tech-the-edge", "The Edge — EDGE", "https://edge.tech/portfolio/the-edge", "EDGE Technologies", "官方机构", "记载 The Edge 由 PLP Architecture 设计、2014 完工、能源正效益、98.36%"),
    ("tclf-peavey-plaza", "Peavey Plaza — The Cultural Landscape Foundation", "https://www.tclf.org/peavey-plaza", "TCLF", "官方机构", "记载 Peavey Plaza 1975 年 M. Paul Friedberg 设计、改造增设无障碍坡道、2023 ASLA 通用设计奖"),
    ("coen-peavey-plaza", "Peavey Plaza — Coen+Partners", "https://www.coenpartners.com/project/peavey-plaza/", "Coen+Partners", "官方机构", "记载改造以 new ramps 提供无障碍通行"),
    ("wikisource-ten-books", "Ten Books on Architecture（Morris Hicky Morgan 英译，1914）— Wikisource", "https://en.wikisource.org/wiki/Ten_Books_on_Architecture", "Wikisource", "学术著作", "维特鲁威《建筑十书》Morgan 1914 英译本全文"),
    ("cove-vitruvius", "De architectura — COVE", "https://editions.covecollective.org/node/7431", "COVE", "学术著作", "记载成书约公元前 30–15 年（标注 Not Vetted）"),
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
            if k == "sustainable-architecture":
                e["sections"]["实例"] = "名称：The Edge（阿姆斯特丹）；地点：荷兰阿姆斯特丹；设计者：PLP Architecture；年份：2014 年第四季度完工。获 BREEAM-NL Outstanding，评分各源记为约 98.3%–98.36%（并列不写死）。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项（评分各源 98.3%–98.36% 已并列）。"
                for r in ["breeam-the-edge", "edge-tech-the-edge"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            elif k == "sunken-accessibility":
                e["sections"]["实例"] = "名称：Peavey Plaza（明尼阿波利斯）；地点：美国明尼阿波利斯；设计者：M. Paul Friedberg（1975 原设计）、Coen+Partners（改造增设无障碍坡道）；年份：1975 年建成，改造后获 2023 年 ASLA 通用设计荣誉奖。以新增坡道提供无障碍通行。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "坡道坡度、扶手高度等具体参数为一般性说明，须按当地规范校核。"
                for r in ["tclf-peavey-plaza", "coen-peavey-plaza"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            elif k == "vitruvian-triad":
                e["sections"]["待核实"] = "英译依据 Morris Hicky Morgan（1914）译本；成书年代约为公元前 30–15 年，仍以约数表述。"
                for r in ["wikisource-ten-books", "cove-vitruvius"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "成书年代为约数（约公元前 30–15 年），译本依据 Morgan 1914，年代细节待考订。"
                ch = True
            else:
                continue
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added", added)


if __name__ == "__main__":
    main()
