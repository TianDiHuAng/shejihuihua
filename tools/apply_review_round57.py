"""第57轮：为 6 个动线/环境条目补具名实例（12 源）；2 条仅单源者保留披露。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("rijksmuseum-schiphol-sign", "Signage for Schiphol Airport — Rijksmuseum", "https://www.rijksmuseum.nl/en/collection/NG-C-2012-11-1", "Rijksmuseum", "官方机构", "史基浦机场导视系统，Benno Wissing，1967"),
    ("crouwel-schiphol", "Designing for everyone — Wim Crouwel Instituut", "https://wimcrouwelinstituut.nl/en/research/designing-for-everyone", "Wim Crouwel Instituut", "学术著作", "史基浦机场最早整合象形符号的机场之一"),
    ("kimbell-kahn", "The Kahn Building — Kimbell Art Museum", "https://kimbellart.org/art-architecture/architecture/kahn-building", "Kimbell Art Museum", "官方机构", "金贝尔美术馆康大楼 1972，自然光经窄缝天窗柔和进入"),
    ("sah-kimbell", "Kimbell Art Museum — SAH Archipedia", "https://sah-archipedia.org/node/84831", "Society of Architectural Historians", "学术著作", "悬挂铝反射板调节自然光"),
    ("accessboard-smithsonian", "Access Board commends Smithsonian — U.S. Access Board", "https://beta.access-board.gov/news/2021/12/16/u-s-access-board-commends-smithsonian-national-museum-of-natural-history-for-new-accessible-routes/", "U.S. Access Board", "官方机构", "史密森尼自然历史博物馆 2021 新增无障碍坡道入口"),
    ("si-nmnh-accessibility", "Inclusive innovations — Smithsonian Magazine", "https://www.airspacemag.com/blogs/national-museum-of-natural-history/2024/07/30/inclusive-innovations-an-accessible-natural-history-experience", "Smithsonian Magazine", "学术著作", "两条架空步道提升无障碍通行"),
    ("bioregional-bedzed", "BedZED — Bioregional", "https://www.bioregional.com/projects-and-services/case-studies/bedzed-the-uks-first-large-scale-eco-village", "Bioregional", "官方机构", "贝丁顿零能耗社区 1997 构想、2002 完成，英国首个大型混合功能可持续社区"),
    ("ntu-bedzed", "英國貝丁頓零碳社區 — 台大科學Online", "https://case.ntu.edu.tw/highscope/永續社區的模範生-英國貝丁頓零碳社區/index.html", "台湾大学", "学术著作", "贝丁顿零碳社区 2002，Bill Dunster 设计"),
    ("kpmb-manitoba", "Manitoba Hydro Place — KPMB", "https://www.kpmb.com/project/manitoba-hydro-place/", "KPMB Architects", "官方机构", "曼尼托巴水电大楼：热质量、双层表皮、自然通风、被动太阳能"),
    ("cbc-manitoba", "Manitoba Hydro Place wins award — CBC", "https://www.cbc.ca/news/entertainment/manitoba-hydro-place-wins-architecture-award-1.860288", "CBC News", "学术著作", "曼尼托巴水电大楼地热供暖与辐射降温"),
    ("berlin-phil", "Philharmonie — Berliner Philharmoniker", "https://www.berliner-philharmoniker.de/en/about-us/philharmonie/", "Berliner Philharmoniker", "官方机构", "柏林爱乐大厅，Hans Scharoun，1963，葡萄园式座席"),
    ("aj-berlin-phil", "Scharoun's Berlin Philharmonie — Architects' Journal", "https://www.architectsjournal.co.uk/news/scharouns-berlin-philharmonie-building-burns", "Architects' Journal", "学术著作", "柏林爱乐大厅为沙隆代表作、顶级乐团驻地"),
]
INST = {
 "wayfinding": ("名称：阿姆斯特丹史基浦机场导视系统；地点：荷兰史基浦；设计者：贝诺·维辛（Benno Wissing，1967）、保罗·迈克萨纳（Paul Mijksenaar，1990s）；年份：1967 年、1990 年代。最早整合象形符号的机场导视之一。此处仅列名称、地点、作者与年份信息，不复制图像。", ["rijksmuseum-schiphol-sign", "crouwel-schiphol"], True, "同一导视系统的不同阶段由两源分别记载，作者与年份分期列出。"),
 "visual-comfort": ("名称：金贝尔艺术博物馆·康大楼；地点：美国德州沃思堡；设计者：路易·康（Louis I. Kahn）；年份：1972 年。自然光经窄缝天窗与铝反射板柔和进入，形成舒适光照。此处仅列名称、地点、作者与年份信息，不复制图像。", ["kimbell-kahn", "sah-kimbell"], True, "“视觉舒适”为对两源所述采光机制的概念归类，非来源原话。"),
 "accessibility-design": ("名称：史密森尼国家自然历史博物馆无障碍坡道；地点：美国华盛顿国家广场；设计者：史密森尼学会（实施）、美国无障碍委员会（表彰）；年份：2021 年。新增坡道改善入口可达性。此处仅列名称、地点、责任方与年份信息，不复制图像。", ["accessboard-smithsonian", "si-nmnh-accessibility"], False, ""),
 "sustainable-design": ("名称：贝丁顿零能耗社区（BedZED）；地点：英国伦敦萨顿区哈克布里奇；设计者：比尔·邓斯特（Bill Dunster，ZEDfactory）、Bioregional／Peabody／Arup；年份：1997 年构想、2002 年建成。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["bioregional-bedzed", "ntu-bedzed"], True, "两源对住宅户数口径不同（82 vs 100），本页不写具体户数。"),
 "thermal-comfort": ("名称：曼尼托巴水电大楼（Manitoba Hydro Place）；地点：加拿大温尼伯；设计者：KPMB Architects（设计）、Architecture49／Smith Carter（执行）；年份：2008 年底启用。以双层表皮、自然通风、地热与辐射降温实现室内热环境。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["kpmb-manitoba", "cbc-manitoba"], True, "两源使用工程等价词（thermal mass/natural ventilation/geothermal），未逐字使用 thermal comfort；年份并置。"),
 "acoustic-environment": ("名称：柏林爱乐大厅（Philharmonie Berlin）；地点：德国柏林；设计者：汉斯·沙隆（Hans Scharoun，建筑）、洛塔尔·克雷默（Lothar Cremer，声学）；年份：1963 年。葡萄园式座席与顶部声学反射板，混响时间约 2 秒。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["berlin-phil", "aj-berlin-phil"], True, "声学参数仅柏林爱乐官方单机构直证（两个页面合并计一源），AJ 仅作身份佐证。"),
}


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        data["sources"].append({"id": sid, "title": title, "author": author, "type": typ,
                                "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
                                "note": f"访问于 2026-11-23，由核验子任务实抓 HTTP 200 并核对正文；{note}"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] in INST:
                inst, srcs, keep, caveat = INST[e["id"]]
                e["sections"]["实例"] = inst
                for r in srcs:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = keep
                e["sections"]["待核实"] = caveat if keep else "暂无已知待核实项。"
                e["pending_notes"] = caveat if keep else ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round57 applied")


if __name__ == "__main__":
    main()
