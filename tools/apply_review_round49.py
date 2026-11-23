"""第49轮：6 条补具名实例（12 源）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("vatican-segnatura", "Stanza della Segnatura — Musei Vaticani", "https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/stanze-di-raffaello/stanza-della-segnatura.html", "Musei Vaticani", "官方机构", "拉斐尔《雅典学院》梵蒂冈签字厅 1509–1511"),
    ("theartstory-raphael", "Raphael — TheArtStory", "https://www.theartstory.org/artist/raphael/", "TheArtStory", "学术著作", "《雅典学院》1509-11，透视构图"),
    ("louvre-monalisa", "From the Mona Lisa to the Wedding Feast at Cana — Musée du Louvre", "https://www.louvre.fr/en/explore/the-palace/from-the-mona-lisa-to-the-wedding-feast-at-cana", "Musée du Louvre", "官方机构", "《蒙娜丽莎》卢浮宫 711 厅，远景空气透视"),
    ("wga-monalisa", "Mona Lisa — Web Gallery of Art", "https://www.wga.hu/html_m/l/leonardo/04/1monali.html", "Web Gallery of Art", "学术著作", "《蒙娜丽莎》1503-5 木板油画，卢浮宫"),
    ("uchicago-colosseum", "The Colosseum — Encyclopaedia Romana (Univ. of Chicago)", "https://penelope.uchicago.edu/~grout/encyclopaedia_romana/romanurbs/colosseum.html", "University of Chicago", "学术著作", "斗兽场四层拱廊，前三层各八十拱，多立克/爱奥尼/科林斯"),
    ("uw-colosseum", "Il Colosseo — University of Washington", "https://depts.washington.edu/hrome/Authors/jimkuo2/IlColosseo/pub_zbarticle_view_printable.html", "University of Washington", "学术著作", "三层各八十拱的重复拱廊"),
    ("theartstory-lecorbusier", "Le Corbusier — TheArtStory", "https://www.theartstory.org/artist/le-corbusier/", "TheArtStory", "学术著作", "朗香教堂 1950–1955"),
    ("wikiarquitectura-ronchamp", "Notre-Dame du Haut — WikiArquitectura", "https://en.wikiarquitectura.com/building/notre-dame-du-haut/", "WikiArquitectura", "学术著作", "朗香教堂，Le Corbusier，1950–1955"),
    ("villalarotonda-official", "Villa La Rotonda — official", "https://www.villalarotonda.it/en/villa/", "Villa La Rotonda", "官方机构", "圆厅别墅：方形平面内接圆形、四面门廊，Palladio 1567 起"),
    ("wikiarquitectura-rotonda", "Villa Rotonda — WikiArquitectura", "https://en.wikiarquitectura.com/building/villa-rotonda/", "WikiArquitectura", "学术著作", "圆厅别墅：圆内接方、双向对称"),
    ("ryoanji-official", "Ryōan-ji — official", "http://www.ryoanji.jp/smph/eng/", "Ryōan-ji", "官方机构", "龙安寺石庭（枯山水）"),
    ("japanguide-ryoanji", "Ryōan-ji — Japan Guide", "https://www.japan-guide.com/e/e3909.html", "Japan Guide", "学术著作", "日本最著名石庭，1450 改为禅寺"),
]
INST = {
    "vanishing-point": ("名称：《雅典学院》（The School of Athens）；地点：梵蒂冈博物馆签字厅；设计者：拉斐尔（Raphael）；年份：1509–1511 年。以透视汇聚表现纵深。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["vatican-segnatura", "theartstory-raphael"], True, "两主源未逐字直书“消失点”一词（属透视通识定性）；实例四要素已双源。"),
    "aerial-perspective": ("名称：《蒙娜丽莎》（Mona Lisa）；地点：法国巴黎卢浮宫（711 厅）；设计者：列奥纳多·达·芬奇（Leonardo da Vinci）；年份：约 1503–1519 年（各家标年 1503–1505 / 1503–1519 并列）。人物背后以空气透视表现远景。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["louvre-monalisa", "wga-monalisa"], True, "年份各家不一，已并列；实例四要素已双源。"),
    "rhythm-repetition": ("名称：罗马斗兽场（Colosseum）；地点：意大利罗马；设计者：韦斯巴芗始建、提图斯落成（建筑师不详）；年份：约 70–80 年。以三层各八十拱的重复拱廊形成韵律。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["uchicago-colosseum", "uw-colosseum"], False, ""),
    "contrast-principle": ("名称：朗香教堂（Notre-Dame du Haut）；地点：法国朗香；设计者：勒·柯布西耶（Le Corbusier）；年份：1950–1955 年。以厚重曲面墙体与明暗窗洞形成强烈对比。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["theartstory-lecorbusier", "wikiarquitectura-ronchamp"], True, "无官方一级来源（两家为艺术史/建筑数据库），权威级中等。"),
    "geometry-symmetry": ("名称：圆厅别墅（Villa La Rotonda）；地点：意大利维琴察；设计者：安德烈亚·帕拉第奥（Andrea Palladio）；年份：1567 年起建（约 1567–1570）。方形平面内接圆形、四面门廊，双向对称。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["villalarotonda-official", "wikiarquitectura-rotonda"], False, ""),
    "negative-space": ("名称：龙安寺方丈庭石庭（Ryōan-ji rock garden）；地点：日本京都；设计者：不详；年份：约 15 世纪（1450 年前后）。以白砂与置石留白组织“负空间”。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["ryoanji-official", "japanguide-ryoanji"], True, "设计者不详；第二源为旅行指南（权威级中等）；“negative space”术语源未直书。"),
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
                inst, srcs, keep, note = INST[e["id"]]
                e["sections"]["实例"] = inst
                for r in srcs:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                if keep:
                    e["needs_verification"] = True
                    e["sections"]["待核实"] = note
                    e["pending_notes"] = note
                else:
                    e["needs_verification"] = False
                    e["sections"]["待核实"] = "暂无已知待核实项。"
                    e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round49 instances applied")


if __name__ == "__main__":
    main()
