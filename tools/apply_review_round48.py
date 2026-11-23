"""第48轮：5 条补具名实例（10 源）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("flw-guggenheim", "Solomon R. Guggenheim Museum — Frank Lloyd Wright Foundation", "https://franklloydwright.org/site/solomon-r-guggenheim-museum/", "Frank Lloyd Wright Foundation", "官方机构", "古根海姆美术馆 1943 委托、螺旋坡道与玻璃顶"),
    ("theartstory-wright", "Frank Lloyd Wright — TheArtStory", "https://www.theartstory.org/artist/wright-frank-lloyd/", "TheArtStory", "学术著作", "古根海姆 1943–59，螺旋坡道环绕顶部采光中庭"),
    ("archdaily-heydar", "Heydar Aliyev Center — ArchDaily", "https://www.archdaily.com/448774/heydar-aliyev-center-zaha-hadid-architects", "ArchDaily", "学术著作", "盖达尔·阿利耶夫中心，巴库，Zaha Hadid，2013"),
    ("theartstory-hadid", "Zaha Hadid — TheArtStory", "https://www.theartstory.org/artist/hadid-zaha/", "TheArtStory", "学术著作", "Heydar Aliyev Center 2007–12，Parametricism"),
    ("guggenheim-bilbao-building", "The Building — Guggenheim Bilbao", "https://www.guggenheim-bilbao.eus/en/the-building", "Guggenheim Bilbao", "官方机构", "毕尔巴鄂古根海姆，Frank Gehry，钛/玻璃/石灰岩，围绕中庭"),
    ("theartstory-deconstructivism", "Deconstructivism — TheArtStory", "https://www.theartstory.org/movement/deconstructivism/", "TheArtStory", "学术著作", "解构主义，Guggenheim Bilbao 1997"),
    ("flc-unite", "Unité d'habitation, Marseille — Fondation Le Corbusier", "https://www.fondationlecorbusier.fr/en/work-architecture/achievements-unite-dhabitation-marseille-france-1945-1952/", "Fondation Le Corbusier", "官方机构", "马赛公寓 1945–1952，清水混凝土 béton brut"),
    ("theartstory-brutalism", "Brutalism — TheArtStory", "https://www.theartstory.org/movement/brutalism/", "TheArtStory", "学术著作", "粗野主义，Unité d'habitation 1952，béton brut"),
    ("thyssen-canaletto", "Piazza San Marco, Venice — Museo Thyssen-Bornemisza", "https://www.museothyssen.org/en/collection/artists/canaletto/piazza-san-marco-venice", "Museo Thyssen-Bornemisza", "官方机构", "卡纳莱托《圣马可广场》约1723–24，明确使用两个消失点"),
    ("theartstory-canaletto", "Canaletto — TheArtStory", "https://www.theartstory.org/artist/canaletto/", "TheArtStory", "学术著作", "卡纳莱托精湛的透视，angolo 斜角透视"),
]
INST = {
    "atrium-architecture": ("名称：纽约古根海姆美术馆（Solomon R. Guggenheim Museum）；地点：美国纽约；设计者：弗兰克·劳埃德·赖特（Frank Lloyd Wright）；年份：1943 年委托、1959 年开馆。以螺旋坡道环绕顶部采光中庭。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["flw-guggenheim", "theartstory-wright"], False),
    "parametric-architecture": ("名称：盖达尔·阿利耶夫中心（Heydar Aliyev Center）；地点：阿塞拜疆巴库；设计者：扎哈·哈迪德建筑事务所（Zaha Hadid Architects）；年份：2007–2012 年设计建造（2013 年开放，各家标年不一）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["archdaily-heydar", "theartstory-hadid"], True),
    "deconstructivism": ("名称：毕尔巴鄂古根海姆美术馆（Guggenheim Museum Bilbao）；地点：西班牙毕尔巴鄂；设计者：弗兰克·盖里（Frank Gehry）；年份：1997 年建成开放（约 1991 年起设计）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["guggenheim-bilbao-building", "theartstory-deconstructivism"], True),
    "brutalism": ("名称：马赛公寓（Unité d'habitation）；地点：法国马赛；设计者：勒·柯布西耶（Le Corbusier）；年份：1947–1952 年。以清水混凝土（béton brut）著称。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["flc-unite", "theartstory-brutalism"], False),
    "two-point-perspective": ("名称：《圣马可广场威尼斯景》（Piazza San Marco, Venice）；地点：西班牙马德里提森-博内米萨国立博物馆藏；设计者：卡纳莱托（Canaletto）；年份：约 1723–1724 年。画面在两个等距消失点间组织透视。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["thyssen-canaletto", "theartstory-canaletto"], True),
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
                inst, srcs, keep_nv = INST[e["id"]]
                e["sections"]["实例"] = inst
                for r in srcs:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                if keep_nv:
                    e["needs_verification"] = True
                    e["sections"]["待核实"] = "具体年份/设计者归属或同一作品第二独立来源待补充（现为单强源＋手法佐证）。"
                    e["pending_notes"] = "部分年份或第二独立来源待补充。"
                else:
                    e["needs_verification"] = False
                    e["sections"]["待核实"] = "暂无已知待核实项。"
                    e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round48 instances applied")


if __name__ == "__main__":
    main()
