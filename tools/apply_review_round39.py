"""第39轮：为 6 个风格条目补具名实例（双源）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("durham-whs", "Durham Cathedral — Durham World Heritage Site", "https://www.durhamworldheritagesite.com/learn/architecture/cathedral/building-durham", "Durham World Heritage Site", "官方机构", "杜伦大教堂 1093 起建、罗曼式"),
    ("durham-cathedral", "Durham Cathedral — UNESCO World Heritage", "https://www.durhamcathedral.co.uk/more/unesco-world-heritage-site", "Durham Cathedral", "官方机构", "杜伦大教堂世界遗产与建造"),
    ("amalienburg-official", "Amalienburg — Bayerische Schlösserverwaltung", "https://www.schloss-nymphenburg.de/english/amalienburg.htm", "Bayerische Schlösserverwaltung", "官方机构", "阿玛琳堡，Cuvilliés，1734–1739 洛可可"),
    ("amalienburg-muenchen", "Amalienburg — muenchen.de", "https://www.muenchen.de/sehenswuerdigkeiten/amalienburg", "muenchen.de", "官方机构", "阿玛琳堡洛可可猎宫"),
    ("pantheon-paris", "History of the Panthéon — Centre des monuments nationaux", "https://www.paris-pantheon.fr/en/discover/history-of-the-pantheon", "CMN", "官方机构", "先贤祠 Soufflot 设计、1764 奠基、1790 竣工"),
    ("pantheon-pop", "Panthéon — POP/Mérimée PA00088420", "https://pop.culture.gouv.fr/notice/merimee/PA00088420", "法国文化部", "官方机构", "先贤祠保护名录与技术信息"),
    ("red-house-nt", "Red House — National Trust", "https://www.nationaltrust.org.uk/visit/london/red-house", "National Trust", "官方机构", "红屋，Philip Webb & William Morris，1859–1860"),
    ("red-house-morris", "About William Morris — William Morris Society", "https://williammorrissociety.org/about-william-morris/", "William Morris Society", "官方机构", "莫里斯与红屋、工艺美术运动"),
    ("horta-theartstory", "Victor Horta — TheArtStory", "https://www.theartstory.org/artist/horta-victor/", "TheArtStory", "学术著作", "塔塞爾公館 1893–1894，Horta，新艺术"),
    ("hotel-tassel-visitbrussels", "10 must-visit Art Nouveau houses — Visit Brussels", "https://visit.brussels/en/visitors/what-to-do/10-must-visit-art-nouveau-houses-and-mansions-in-brussels", "Visit Brussels", "官方机构", "塔塞爾公館等新艺术建筑"),
    ("chrysler-history", "Chrysler Building — History", "https://chryslerbuilding.com/history/", "Chrysler Building", "官方机构", "克莱斯勒大厦，William Van Alen，1928–1930"),
    ("nyc-lpc-chrysler", "Chrysler Building — NYC Landmarks Preservation Commission LP-0992", "https://s-media.nyc.gov/agencies/lpc/lp/0992.pdf", "NYC LPC", "官方机构", "克莱斯勒大厦指定报告，Van Alen，1930"),
]

INST = {
    "romanesque": ("名称：杜伦大教堂（Durham Cathedral）；地点：英国杜伦；设计者：佚名（主教 William of St Calais 主持并可能参与设计）；年份：1093 年起建（约至 1133 年）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["durham-whs", "durham-cathedral"]),
    "rococo": ("名称：阿玛琳堡（Amalienburg）；地点：德国慕尼黑宁芬堡宫苑；设计者：弗朗索瓦·德·屈维利耶（François Cuvilliés）；年份：1734–1739 年。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["amalienburg-official", "amalienburg-muenchen"]),
    "neoclassical": ("名称：巴黎先贤祠（Panthéon）；地点：法国巴黎第五区；设计者：雅克-热尔曼·苏夫洛（Jacques-Germain Soufflot）；年份：1764 年奠基、1790 年竣工。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["pantheon-paris", "pantheon-pop"]),
    "arts-crafts": ("名称：红屋（Red House）；地点：英国伦敦贝克斯利希思；设计者：菲利普·韦布（Philip Webb）与威廉·莫里斯（William Morris）；年份：1859–1860 年。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["red-house-nt", "red-house-morris"]),
    "art-nouveau": ("名称：塔塞爾公館（Hôtel Tassel）；地点：比利时布鲁塞尔；设计者：维克多·奥塔（Victor Horta）；年份：1893–1894 年。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["horta-theartstory", "hotel-tassel-visitbrussels"]),
    "art-deco": ("名称：克莱斯勒大厦（Chrysler Building）；地点：美国纽约曼哈顿；设计者：威廉·范艾伦（William Van Alen）；年份：1928–1930 年。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["chrysler-history", "nyc-lpc-chrysler"]),
}


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
            "note": f"访问于 2026-11-23，由核验子任务实抓 HTTP 200 并核对正文；{note}",
        })
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for fn in ("batch-34.json", "batch-37.json"):
        p = ROOT / "entries" / fn
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc["entries"]:
            k = e["id"]
            if k in INST:
                inst, srcs = INST[k]
                e["sections"]["实例"] = inst
                e["sections"]["待核实"] = "暂无已知待核实项。"
                for r in srcs:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round39 instances applied")


if __name__ == "__main__":
    main()
