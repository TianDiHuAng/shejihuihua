"""第55轮：为 8 个下沉/造景/动线条目补具名实例（16 源）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("butchart-story", "Our Story — The Butchart Gardens", "https://butchartgardens.com/our-story/", "The Butchart Gardens", "官方机构", "布查特花园 Jennie Butchart 将采石坑建成下沉花园"),
    ("cib-butchart", "The Butchart Gardens — Communities in Bloom", "https://www.communitiesinbloom.ca/the-butchart-gardens-british-columbia-2026-national-special-attractions/", "Communities in Bloom", "学术著作", "布查特花园 1904 创建、位于 Brentwood Bay、含下沉花园"),
    ("louvre-pyramid-symbol", "A pyramid for a symbol — Louvre", "https://www.louvre.fr/en/explore/the-palace/a-pyramid-for-a-symbol", "Musée du Louvre", "官方机构", "贝聿铭中央地下大厅直通三翼，1989-03-29 启用"),
    ("pcf-grand-louvre", "Grand Louvre Modernization — PCF Architects", "https://pcfarchitects.com/projects/grand-louvre-modernization/", "PCF Architects", "学术著作", "拿破仑大厅与地下连廊联系三翼"),
    ("moesgaard-building", "Building and landscape — Moesgaard Museum", "https://moesgaardmuseum.dk/en/visit-us/building-and-landscape", "Moesgaard Museum", "官方机构", "莫斯高博物馆 2014 开馆，Henning Larsen 设计，错层展陈"),
    ("henning-moesgaard", "Moesgaard — Henning Larsen", "https://henninglarsen.com/projects/moesgaard", "Henning Larsen Architects", "官方机构", "坡地覆土、草皮屋顶、自然光进入地下展厅"),
    ("adjaye-sunken-house", "Sunken House — Adjaye Associates", "https://www.adjaye.com/work/sunken-house/", "Adjaye Associates", "官方机构", "伦敦 Sunken House 2007，开挖庭院、主起居层位于下沉处"),
    ("archdaily-sunken-house", "Sunken House — ArchDaily", "https://www.archdaily.com/213736/sunken-house-adjaye-associates", "ArchDaily", "学术著作", "2007 建成于伦敦 Hackney，场地挖至地下室标高形成下沉庭院"),
    ("suzhou-lion-grove", "狮子林 — 苏州市园林和绿化管理局", "https://ylj.suzhou.gov.cn/szsylj/sjyc/201905/767dcf47765b40549969f1a6989c689c.shtml", "苏州市园林和绿化管理局", "官方机构", "狮子林湖石假山群，国内尚存最大古代假山群，1342 年"),
    ("unesco-suzhou", "Classical Gardens of Suzhou — UNESCO", "https://whc.unesco.org/en/list/813/", "UNESCO", "官方机构", "狮子林列为苏州园林代表，rock formations 构成园林"),
    ("whj-kew-borders", "The Great Broad Walk Borders — World Heritage Journeys", "https://visitworldheritage.com/en/eu/the-great-broad-walk-borders/0220f1d9-1d71-47b7-8748-b0d0f9775f2e", "World Heritage Journeys", "学术著作", "邱园大花境 1840s Nesfield 设计、6 万株开花植物"),
    ("dcms-kew-pdf", "World Heritage Sites — UK DCMS PDF", "https://assets.publishing.service.gov.uk/media/5a79c52f40f0b66d161ae059/WorldHeritageSites1999.pdf", "UK DCMS", "官方机构", "邱园 1841 由 Nesfield 重新造景，步道与视廊为主轴线"),
    ("kunaicho-katsura", "Katsura Imperial Villa — Imperial Household Agency", "https://www.kunaicho.go.jp/en/learn/institution/shisetsu/kyoto/kyoto.html", "日本宫内厅", "官方机构", "桂离宫 1615 起营建、两代皇子、四季花木与变化的景色"),
    ("jnt-katsura", "桂离宫 — JNTO", "https://www.japan-travel.cn/spot/1137/", "JNTO", "官方机构", "桂离宫 17 世纪皇室建造、四季皆宜、每次景色不同"),
    ("louvre-pyramid-presse", "The Pyramid Project — Louvre Press", "https://presse.louvre.fr/the-pyramid-project/?lang=en", "Musée du Louvre", "官方机构", "贝聿铭金字塔 1989，管理参观流线、三翼入口重组"),
    ("britannica-louvre-pyramid", "Louvre Pyramid — Britannica", "https://www.britannica.com/topic/Louvre-Pyramid", "Britannica", "权威百科", "卢浮宫主入口，贝聿铭设计 1989 完成，中央地下大厅统合三翼"),
]
INST = {
 "sunken-garden": ("名称：布查特花园下沉花园（The Sunken Garden）；地点：加拿大不列颠哥伦比亚省 Brentwood Bay；设计者：珍妮·布查特（Jennie Butchart）；年份：园区 1904 年创建、采石坑花园化节点约 1912 年。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["butchart-story", "cib-butchart"], False, ""),
 "sunken-atrium": ("名称：卢浮宫金字塔与拿破仑大厅（Pyramide / Hall Napoléon）；地点：法国巴黎卢浮宫拿破仑庭院；设计者：贝聿铭（I. M. Pei）；年份：1989 年 3 月 29 日启用。中央地下大厅直通博物馆三翼。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["louvre-pyramid-symbol", "pcf-grand-louvre"], False, ""),
 "earth-sheltered": ("名称：莫斯高博物馆（Moesgaard Museum）；地点：丹麦奥胡斯南部；设计者：亨宁·拉森建筑事务所（Henning Larsen Architects）；年份：2014 年开馆（2009–2014 设计施工）。坡地覆土、草皮屋顶、自然光进入地下展厅。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["moesgaard-building", "henning-moesgaard"], False, ""),
 "semi-sunken-space": ("名称：下沉住宅（Sunken House）；地点：英国伦敦哈克尼区 De Beauvoir Town；设计者：Adjaye Associates；年份：2007 年。场地挖至地下室标高，形成下沉庭院与主起居层。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["adjaye-sunken-house", "archdaily-sunken-house"], False, ""),
 "rockery": ("名称：苏州狮子林湖石假山群；地点：中国江苏苏州园林路；设计者：天如禅师及弟子（无单一设计师）；年份：元至正二年（1342 年）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["suzhou-lion-grove", "unesco-suzhou"], False, ""),
 "planting-design": ("名称：邱园大花境（Great Broad Walk Borders）；地点：英国伦敦邱园；设计者：威廉·内斯菲尔德（原始）、理查德·威尔福德（再设计）；年份：1840 年代。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["whj-kew-borders", "dcms-kew-pdf"], False, ""),
 "seasonal-scenery": ("名称：桂离宫庭园；地点：日本京都西京区桂川西岸；设计者：智仁亲王、智忠亲王（皇室营建）；年份：1615 年起近 50 年。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["kunaicho-katsura", "jnt-katsura"], False, ""),
 "visitor-route": ("名称：卢浮宫金字塔—拿破仑大厅主入口；地点：法国巴黎卢浮宫；设计者：贝聿铭（I. M. Pei）；年份：1989 年。入口重组后管理内外参观流线并统合三翼。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["louvre-pyramid-presse", "britannica-louvre-pyramid"], False, ""),
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
    print("round55 applied")


if __name__ == "__main__":
    main()
