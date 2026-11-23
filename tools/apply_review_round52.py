"""第52轮：为 5 条色彩理论补具名实例（双源）；另 3 条仅单源者补实例并保留待核实披露。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("royalsociety-colour-wheel", "Newton's colour wheel — Royal Society", "https://royalsociety.org/blog/2021/11/colour-wheel/", "Royal Society", "官方机构", "牛顿首个色环、七种光谱色置于不等分圆周"),
    ("mollon-colour-science", "Mollon: Colour Science — Cambridge PDF", "https://vision.psychol.cam.ac.uk/jdmollon/papers/MollonColorScience.pdf", "University of Cambridge", "学术著作", "圆周表示七主色；同色相饱和度可变"),
    ("hermitage-dance", "The Dance (Matisse) — Hermitage", "https://www.hermitagemuseum.org/digital-collection/28411?lng=en", "Hermitage Museum", "官方机构", "马蒂斯《舞蹈》1909-1910，红蓝绿强烈和声"),
    ("libretexts-fauvism", "Fauvism & Expressionism — Humanities LibreTexts", "https://human.libretexts.org/Bookshelves/Art/Art_History_and_Theory/SmartHistory_of_Art/10%3A_Modernisms_1900__1980/10.03%3A_Fauvism__Expressionism", "LibreTexts", "学术著作", "野兽派纯烈色彩与大胆笔触，《舞蹈》蓝绿背景"),
    ("louvreabudhabi-mondrian", "Mondrian — Louvre Abu Dhabi", "https://prod-cm.louvreabudhabi.ae/en/whats-online/art-from-home/mondrian", "Louvre Abu Dhabi", "官方机构", "蒙德里安用三原色（红黄蓝）与黑白"),
    ("tate-mondrian", "Piet Mondrian — Tate Kids", "https://www.tate.org.uk/kids/artists/who-piet-mondrian", "Tate", "官方机构", "蒙德里安常用三原色"),
    ("centv-liberty", "卢浮宫名画《自由引导人民》 — CETV", "https://www.centv.cn/p/462928.html", "CETV", "学术著作", "蓝白红三色旗为法国大革命象征"),
    ("artic-water-lilies", "Water Lilies — Art Institute of Chicago", "https://api.artic.edu/api/v1/artworks/16568?fields=id,title,artist_display,date_display,description,credit_line", "Art Institute of Chicago", "官方机构", "莫奈《睡莲》1906，水面映树云"),
    ("ng-water-lilies", "Water Lilies — National Gallery", "https://www.nationalgallery.org.uk/paintings/claude-monet-water-lilies", "National Gallery", "官方机构", "莫奈《睡莲》NG6343，绿赭紫黄天蓝粉"),
    # 仅单源/单机构者：补具名实例 + 披露，不升级
    ("webexhibits-vangogh-533", "Van Gogh letter 533 — Webexhibits", "http://webexhibits.org/vangogh/letter/18/533.htm", "Webexhibits", "学术著作", "梵高书信：以红绿表达激情、红绿冲突对比"),
    ("webexhibits-contrast", "Color contrast — Webexhibits", "http://webexhibits.org/colorart/contrast.html", "Webexhibits", "学术著作", "互补色同时对比最强；举梵高夜间咖啡馆红绿"),
    ("ng-temeraire", "The Fighting Temeraire — National Gallery", "https://www.nationalgallery.org.uk/paintings/joseph-mallord-william-turner-the-fighting-temeraire", "National Gallery", "官方机构", "透纳《无畏号》1839，暖橙黄到冷蓝紫粉"),
]
INST = {
 "hue": ("名称：牛顿色环图（Newton's colour wheel）；地点：英国伦敦（皇家学会藏品与研究）；设计者：艾萨克·牛顿（Isaac Newton）；年份：1704 年前后（《光学》时期）。以圆周排布七种光谱色表示色相。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["royalsociety-colour-wheel", "mollon-colour-science"], False, ""),
 "saturation": ("名称：《舞蹈》（The Dance）；地点：俄罗斯圣彼得堡艾尔米塔什博物馆；设计者：亨利·马蒂斯（Henri Matisse）；年份：1909–1910 年。以红、蓝、绿的纯烈色彩体现高饱和。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["hermitage-dance", "libretexts-fauvism"], True, "“高饱和”为对两源所述 pure vivid / stunning accord 的归纳，两源未逐字使用 saturation 一词。"),
 "primary-colors": ("名称：《蓝、红、黄、黑构成》；地点：阿布扎比卢浮宫；设计者：皮特·蒙德里安（Piet Mondrian）；年份：1922 年。以红黄蓝三原色与黑白作画。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["louvreabudhabi-mondrian", "tate-mondrian"], True, "第二源（Tate）配图为另一幅作品，仅说明蒙德里安一贯的原色用法；本幅三原色由阿布扎比卢浮宫单源直证。"),
 "color-symbolism": ("名称：《自由引导人民》（Liberty Leading the People）；地点：法国巴黎卢浮宫（RF 129）；设计者：欧仁·德拉克洛瓦（Eugène Delacroix）；年份：1830 年。画中蓝白红三色旗象征自由、平等、博爱。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["libretexts-romanticism", "centv-liberty"], False, ""),
 "color-harmony": ("名称：《睡莲》（Water Lilies）；地点：美国芝加哥艺术博物馆／英国伦敦国家美术馆；设计者：克劳德·莫奈（Claude Monet）；年份：1906 年前后。以绿、赭、紫、黄、天蓝、粉等色构成和谐画面。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["artic-water-lilies", "ng-water-lilies"], True, "两源直证各色并用，但未逐字使用 harmony 一词，和谐为基于色彩描写的解读。"),
 "complementary-colors": ("名称：《夜间咖啡馆》（The Night Café）；地点：美国纽黑文耶鲁大学美术馆；设计者：文森特·梵高（Vincent van Gogh）；年份：1888 年。梵高在书信中明言以红绿这对互补色表达激情。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["webexhibits-vangogh-533", "webexhibits-contrast"], True, "两页均属 Webexhibits 同一机构，按单一来源计；作品要素与互补色论述待补第二独立机构来源。"),
 "color-contrast": ("名称：《夜间咖啡馆》（The Night Café）；地点：美国纽黑文耶鲁大学美术馆；设计者：文森特·梵高；年份：1888 年。以“最相异的红与绿”冲突并置制造色彩对比。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["webexhibits-vangogh-533", "webexhibits-contrast"], True, "两页同属 Webexhibits 单一机构，色彩对比直证仅一机构来源，待补第二独立机构来源。"),
 "warm-cool": ("名称：《被拖去解体的战舰无畏号》（The Fighting Temeraire）；地点：英国伦敦国家美术馆（NG524）；设计者：J.M.W. 透纳（J. M. W. Turner）；年份：1839 年。夕阳下由暖色白橙黄褐渐入冷色蓝紫粉。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["ng-temeraire"], True, "暖→冷色列由馆方单源直证，待补第二独立机构来源。"),
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
    print("round52 applied")


if __name__ == "__main__":
    main()
