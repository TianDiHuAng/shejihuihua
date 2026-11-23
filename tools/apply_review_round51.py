"""第51轮：为 8 个条目补具名实例（16 源）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("wga-masaccio-trinity", "Trinity, Santa Maria Novella — Web Gallery of Art", "https://www.wga.hu/html/m/masaccio/trinity/index.html", "Web Gallery of Art", "学术著作", "马萨乔《圣三位一体》佛罗伦萨，1425–1428"),
    ("wp-holy-trinity-masaccio", "Holy Trinity (Masaccio) — Wikipedia", "https://en.wikipedia.org/wiki/Holy_Trinity_(Masaccio)", "Wikipedia", "权威百科", "马萨乔《圣三位一体》最早运用线性透视的纪念性作品之一"),
    ("dpm-qingming", "张择端清明上河图卷 — 故宫博物院", "https://www.dpm.org.cn/collection/paint/228226.html", "故宫博物院", "官方机构", "《清明上河图》北宋张择端，汴京景象"),
    ("columbia-handscroll", "Song Dynasty China: The Handscroll Format — Columbia", "https://afe.easia.columbia.edu/songdynasty-module/intro-handscroll.html", "Columbia University", "学术著作", "手卷可移步换景、变化视角（散点透视）"),
    ("db-quaglio", "Quaglio, Giuseppe — Deutsche Biographie", "https://www.deutsche-biographie.de/116317094.html?language=en", "Deutsche Biographie", "官方机构", "Quaglio 被同时代人称为三点透视发明者，1818 慕尼黑国家剧院"),
    ("wp-quaglio", "Giuseppe Quaglio — Wikipedia", "https://en.wikipedia.org/wiki/Giuseppe_Quaglio", "Wikipedia", "权威百科", "三点透视，Die Weihe，1818 慕尼黑国家剧院开幕"),
    ("louvre-collections-mona", "La Joconde — Louvre collections", "https://collections.louvre.fr/en/ark:/53355/cl010062370", "Musée du Louvre", "官方机构", "《蒙娜丽莎》1503–1519，德农馆711厅，地平线记载"),
    ("wp-mona-lisa", "Mona Lisa — Wikipedia", "https://en.wikipedia.org/wiki/Mona_Lisa", "Wikipedia", "权威百科", "达·芬奇将地平线置于与眼睛齐平"),
    ("gallerie-vitruvian", "Studio di proporzioni del corpo umano — Gallerie dell'Accademia", "https://www.gallerieaccademia.it/opera/studio-di-proporzioni-del-corpo-noto-come-uomo-vitruviano/", "Gallerie dell'Accademia", "官方机构", "《维特鲁威人》达·芬奇，威尼斯学院美术馆"),
    ("wga-vitruvian", "Vitruvian Man — Web Gallery of Art", "https://www.wga.hu/html_m/l/leonardo/10anatom/1vitruviu.html", "Web Gallery of Art", "学术著作", "《维特鲁威人》约1492"),
    ("artic-grande-jatte", "A Sunday on La Grande Jatte — Art Institute of Chicago", "https://api.artic.edu/api/v1/artworks/27992?fields=id,title,artist_display,artist_title,date_display,place_of_origin,medium_display,dimensions", "Art Institute of Chicago", "官方机构", "修拉《大碗岛的星期天下午》1884–86"),
    ("wga-grande-jatte", "A Sunday on La Grande Jatte — Web Gallery of Art", "https://www.wga.hu/html_m/s/seurat/figures/jatte.html", "Web Gallery of Art", "学术著作", "修拉《大碗岛》1884–86"),
    ("ng-arnolfini", "The Arnolfini Portrait — National Gallery", "https://www.nationalgallery.org.uk/paintings/jan-van-eyck-the-arnolfini-portrait", "National Gallery", "官方机构", "凡·艾克《阿尔诺菲尼肖像》1434，NG186"),
    ("wga-arnolfini", "The Arnolfini Portrait — Web Gallery of Art", "https://www.wga.hu/html/e/eyck_van/jan/15arnolf/index.html", "Web Gallery of Art", "学术著作", "凡·艾克《阿尔诺菲尼肖像》双人对像、镜居中"),
    ("rijks-nightwatch", "The Night Watch — Rijksmuseum", "https://www.rijksmuseum.nl/en/collection/SK-C-5", "Rijksmuseum", "官方机构", "伦勃朗《夜巡》1642"),
    ("wga-nightwatch", "The Night Watch — Web Gallery of Art", "https://www.wga.hu/html/r/rembrand/26group/05group.html", "Web Gallery of Art", "学术著作", "伦勃朗《夜巡》明暗对照用光"),
]
INST = {
 "linear-perspective": ("名称：《圣三位一体》（Holy Trinity）；地点：意大利佛罗伦萨新圣母玛利亚教堂；设计者：马萨乔（Masaccio）；年份：约 1425–1427 年（各家记 1425–1428 / 1425–1426）。以桶形拱券的透视表现纵深。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["wga-masaccio-trinity", "wp-holy-trinity-masaccio"], "年份各家不一，已并列；两源直证线性透视。"),
 "scattered-perspective": ("名称：《清明上河图》；地点：北宋汴京（今河南开封），原作藏北京故宫博物院；设计者：张择端；年份：12 世纪初。以手卷移步换景、视角流动体现散点透视。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["dpm-qingming", "columbia-handscroll"], ""),
 "three-point-perspective": ("名称：《Die Weihe》舞台设计；地点：德国慕尼黑国家剧院；设计者：朱塞佩·夸廖（Giuseppe Quaglio）；年份：1818 年（该剧院开幕演出）。被同时代人称为“三点透视”的发明。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["db-quaglio", "wp-quaglio"], "原拟仰视摩天楼具名照片缺双源直证，改选夸廖舞台设计；实例已双源。"),
 "horizon-line": ("名称：《蒙娜丽莎》（Mona Lisa）；地点：法国巴黎卢浮宫德农馆 711 厅；设计者：列奥纳多·达·芬奇；年份：1503–1519 年。地平线置于与眼睛齐平，连接人物与风景。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["louvre-collections-mona", "wp-mona-lisa"], ""),
 "proportion": ("名称：《维特鲁威人》（Vitruvian Man）；地点：意大利威尼斯学院美术馆；设计者：列奥纳多·达·芬奇；年份：约 1490–1492 年（馆藏页记“米兰时期”、WGA 记 1492）。以人体比例体现古典模数。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["gallerie-vitruvian", "wga-vitruvian"], "确切年份各家不一，已并列。"),
 "composition": ("名称：《大碗岛的星期天下午》（A Sunday on La Grande Jatte）；地点：美国芝加哥艺术博物馆；设计者：乔治·修拉（Georges Seurat）；年份：1884–1886 年。以点彩与几何安排组织画面构图。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["artic-grande-jatte", "wga-grande-jatte"], "两来源未逐字讨论“构图法则”，实例四要素已双源。"),
 "balance": ("名称：《阿尔诺菲尼肖像》（The Arnolfini Portrait）；地点：英国伦敦国家美术馆（NG186）；设计者：扬·凡·艾克（Jan van Eyck）；年份：1434 年。以对称与居中的镜面组织均衡。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["ng-arnolfini", "wga-arnolfini"], "两源未直书 symmetry/balance，均衡定性据镜面居中与双人对像。"),
 "value": ("名称：《夜巡》（The Night Watch）；地点：荷兰阿姆斯特丹国立博物馆（SK-C-5）；设计者：伦勃朗（Rembrandt van Rijn）；年份：1642 年。以明暗对照与用光聚焦组织明暗层次。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["rijks-nightwatch", "wga-nightwatch"], ""),
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
                inst, srcs, caveat = INST[e["id"]]
                e["sections"]["实例"] = inst
                for r in srcs:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                if caveat:
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
    print("round51 instances applied")


if __name__ == "__main__":
    main()
