"""第54轮：为 8 个风格条目补具名实例（16 源）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("britannica-florence-dome", "Who designed the dome of the Florence Cathedral — Britannica", "https://www.britannica.com/question/Who-designed-the-famous-dome-of-the-Florence-Cathedral", "Britannica", "权威百科", "布鲁内莱斯基设计佛罗伦萨大教堂穹顶，1436 完成"),
    ("firenze-heritage", "Florence World Heritage — Firenze Patrimonio Mondiale", "https://www.firenzepatrimoniomondiale.it/en/florence-world-heritage-office/", "Firenze Patrimonio Mondiale", "官方机构", "佛罗伦萨为文艺复兴象征，布鲁内莱斯基奠定艺术原则"),
    ("shanxi-wwj-foguang", "五台山佛光寺东大殿 — 山西省文物局", "https://wwj.shanxi.gov.cn/gzdt/szdt/202109/t20210908_1992987.shtml", "山西省文物局", "官方机构", "佛光寺东大殿，唐大中十一年（857），中国建筑高峰"),
    ("cctv-foguang", "佛光寺东大殿 — 央视网", "https://m.news.cctv.com/2020/09/11/ARTI18AyhYpt6j83mQRG1D0x200911.shtml", "央视网", "官方机构", "佛光寺东大殿建于唐代（857），保持唐代风貌"),
    ("britannica-dome-rock", "Dome of the Rock: Historical context — Britannica", "https://www.britannica.com/topic/Dome-of-the-Rock/Historical-context-and-construction", "Britannica", "权威百科", "倭马亚哈里发阿卜杜勒-马利克敕建，691–692"),
    ("islam-museum-dome", "Dome of the Rock inscription — Islam Museum", "https://islam.museum/en/object/dome-of-the-rock-inscription/", "Islam Museum", "官方机构", "岩石圆顶铭文，72 AH（691–692 CE）"),
    ("incredibleindia-brihadisvara", "Brihadeeswarar Temple — Incredible India", "https://www.incredibleindia.gov.in/en/tamil-nadu/thanjavur/brihadeeswarar-temple", "Incredible India", "官方机构", "朱罗时期德拉维达建筑，约1010年由拉贾拉贾一世建"),
    ("unesco-chola-temples", "Chola temples — UNESCO Multimedia Archives", "https://www.unesco.org/archives/multimedia/document-1022", "UNESCO", "官方机构", "坦贾武尔布里哈迪斯瓦拉神庙，朱罗建筑成就"),
    ("horyuji-official", "Hōryū-ji — 法隆寺官方", "https://horyuji.or.jp/en/garan", "Hōryū-ji", "官方机构", "法隆寺 607 创建，世界现存最古木构"),
    ("britannica-horyu", "Hōryū Temple — Britannica", "https://www.britannica.com/topic/Horyu-Temple", "Britannica", "权威百科", "法隆寺建于 601–607，670 火灾后重建"),
    ("versailles-official", "History of Versailles — Château de Versailles", "https://en.chateauversailles.fr/discover/history", "Château de Versailles", "官方机构", "路易十四 1661 起扩建，1699–1710 皇家礼拜堂"),
    ("britannica-versailles", "Palace of Versailles: History — Britannica", "https://www.britannica.com/topic/Palace-of-Versailles/History", "Britannica", "权威百科", "1682 定为王室驻地，路易十四 1715 殁后一度废弃"),
    ("tate-tatlin", "Tatlin's Monument to the Third International — Tate Papers", "https://www.tate.org.uk/research/tate-papers/08/model-of-vladimir-tatlins-monument-to-the-third-international-reconstruction-as-instrument-of-research-and-states-of-knowledge", "Tate", "官方机构", "塔特林第三国际纪念碑 1919–20 模型，未建成，400 米玻璃钢构"),
    ("libretexts-constructivism", "Early 20th Century in Europe — Humanities LibreTexts", "https://human.libretexts.org/Courses/Irvine_Valley_College/Grimm_Art_Appreciation_(IVC_ARTH_20)/15%3A_18th-_and_19th-Century_Art-_Realism_to_Impressionism/15.08%3A_Early_20th_Century_in_Europe", "LibreTexts", "学术著作", "构成主义经典作为塔特林第三国际纪念碑（1919）"),
    ("flc-villasavoye", "Villa Savoye — Fondation Le Corbusier", "https://www.fondationlecorbusier.fr/en?p=15437", "Fondation Le Corbusier", "官方机构", "萨伏伊别墅 1928–1931，现代建筑五点之宣言"),
    ("britannica-villasavoye", "Villa Savoye — Britannica", "https://www.britannica.com/place/Villa-Savoye", "Britannica", "权威百科", "萨伏伊别墅位于普瓦西，柯布西耶设计，1929–1931"),
]
INST = {
 "renaissance-style": ("名称：佛罗伦萨大教堂穹顶（Santa Maria del Fiore）；地点：意大利佛罗伦萨；设计者：菲利波·布鲁内莱斯基（Filippo Brunelleschi）；年份：1420 年提出方案、1436 年完成。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["britannica-florence-dome", "firenze-heritage"], False, ""),
 "chinese-architecture-style": ("名称：佛光寺东大殿；地点：中国山西五台山；设计者：史料未具名；年份：唐大中十一年（857 年）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["shanxi-wwj-foguang", "cctv-foguang"], False, ""),
 "islamic-architecture": ("名称：岩石圆顶（Dome of the Rock）；地点：耶路撒冷；设计者：个人建筑师未具名，倭马亚哈里发阿卜杜勒-马利克敕建；年份：伊斯兰历 72 年（691–692 年）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["britannica-dome-rock", "islam-museum-dome"], False, ""),
 "indian-architecture": ("名称：布里哈迪斯瓦拉神庙（Brihadeeswarar Temple）；地点：印度泰米尔纳德邦坦贾武尔；设计者：个人建筑师未具名，拉贾拉贾·朱罗一世主持；年份：约 1010 年。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["incredibleindia-brihadisvara", "unesco-chola-temples"], False, ""),
 "japanese-architecture": ("名称：法隆寺（Hōryū-ji）；地点：日本奈良县斑鸠町；设计者：推古天皇与圣德太子发愿、无单一建筑师；年份：607 年创建、670 年火灾后重建。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["horyuji-official", "britannica-horyu"], False, ""),
 "imperial-architecture": ("名称：凡尔赛宫（Palace of Versailles）；地点：法国凡尔赛；设计者：路易十四主持、历代续建，无单一建筑师；年份：1661 年起扩建、1682 年成为王室驻地、1699–1710 年收尾。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["versailles-official", "britannica-versailles"], False, ""),
 "constructivism": ("名称：第三国际纪念碑（塔特林塔，Monument to the Third International）；地点：俄罗斯（原方案置于彼得格勒）；设计者：弗拉基米尔·塔特林（Vladimir Tatlin）；年份：1919–1920 年设计（方案与模型，未建成）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["tate-tatlin", "libretexts-constructivism"], False, ""),
 "functionalism-architecture": ("名称：萨伏伊别墅（Villa Savoye）；地点：法国普瓦西；设计者：勒·柯布西耶与皮埃尔·让纳雷（Le Corbusier & Pierre Jeanneret）；年份：1928–1931 年（1929–1931 为施工口径，并列）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["flc-villasavoye", "britannica-villasavoye"], True, "两源对起始年口径不同（1928 设计／1929 施工），已并列；Britannica 快览摘要自述 AI 生成，实例据其编辑正文。"),
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
                if keep:
                    e["needs_verification"] = True
                    e["sections"]["待核实"] = caveat
                    e["pending_notes"] = caveat
                else:
                    e["needs_verification"] = False
                    e["sections"]["待核实"] = "暂无已知待核实项。"
                    e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round54 applied")


if __name__ == "__main__":
    main()
