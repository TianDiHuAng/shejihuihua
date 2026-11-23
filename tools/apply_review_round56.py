"""第56轮：为 8 个理论/尺度条目补具名实例（16 源）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("nba-rubin-vase", "Rubin's vase — Niels Bohr Archive", "https://nba-old.nbi.dk/files/sem/12feb2015.html", "Niels Bohr Archive", "学术著作", "鲁宾花瓶，Edgar Rubin 1915，图底问题"),
    ("britannica-gestalt", "Gestalt principles of perceptual organization — Britannica", "https://www.britannica.com/topic/perception/Primary-tendencies-in-perceptual-organization", "Britannica", "权威百科", "格式塔知觉组织原则"),
    ("uhbw-hospital-mural", "Children's hospital mural — University Hospitals Bristol", "https://www.uhbw.nhs.uk/p/latest-news/wildlife-presenter-kate-humble-unveils-childrens-hospital-mural", "UHBW NHS", "官方机构", "儿童医院采血室彩色壁画，鲜艳色彩转移焦虑"),
    ("pmc-color-rooms", "Colored patient rooms RCT — PMC", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8921019/", "PMC", "学术著作", "病房色彩的随机对照研究，改善福祉"),
    ("pps-whyte-plazas", "What Holly Whyte's social life film teaches — PPS", "https://www.pps.org/article/what-holly-whytes-social-life-film-can-teach-us-today", "Project for Public Spaces", "学术著作", "Whyte 观察西格拉姆广场等 12 处，人坐可坐之处"),
    ("mas-whyte-plazas", "The Social Life of Small Urban Spaces — Municipal Art Society", "https://www.mas.org/events/the-social-life-of-small-urban-spaces/", "Municipal Art Society NY", "学术著作", "1980 Street Life Project 研究纽约广场的实际行为"),
    ("dpm-qianli", "千里江山图 — 故宫博物院", "https://www.dpm.org.cn/subject_rivsmounts/qljs/245996.html", "故宫博物院", "官方机构", "王希孟《千里江山图》北宋 1113，青绿设色变化"),
    ("britannica-impression-sunrise", "Impression, Sunrise — Britannica", "https://www.britannica.com/topic/Impression-Sunrise", "Britannica", "权威百科", "莫奈 1872《日出·印象》，色彩理论与同等明度"),
    ("nps-washington-monument", "Washington Monument — NPS", "https://www.nps.gov/places/000/washington-monument.htm", "National Park Service", "官方机构", "华盛顿纪念碑 555 英尺，1848 动工、1884 建成"),
    ("britannica-washington-monument", "Washington Monument — Britannica", "https://www.britannica.com/topic/Washington-Monument-Washington-DC", "Britannica", "权威百科", "华盛顿纪念碑 Robert Mills 设计，1884 世界最高人造物"),
    ("omotesenke-taian", "待庵茶室 — 表千家不審菴", "https://www.omotesenke.jp/english/chanoyu/glossary/3_2_3_win03.html", "表千家不審菴", "官方机构", "千利休唯一留存茶室，二帖、躙口，天正10年（1582）"),
    ("kyoto-taian", "待庵 — 京都府官方旅游站", "https://www.kyototourism.org/zh-hant/sightseeing/13533/", "京都府", "官方机构", "千利休唯一现存茶室，二帖榻榻米、躙口"),
    ("rijks-nightwatch-things", "10 things about The Night Watch — Rijksmuseum", "https://www.rijksmuseum.nl/en/stories/10-things/story/10-things-about-rembrandt-s-night-watch", "Rijksmuseum", "官方机构", "伦勃朗《夜巡》1642，船长手的投影"),
    ("britannica-nightwatch", "The Night Watch — Britannica", "https://www.britannica.com/topic/The-Night-Watch", "Britannica", "权威百科", "《夜巡》1642，明暗对照 masterful chiaroscuro"),
    ("kroller-cafe-terrace", "Terrace of a Café at Night — Kröller-Müller", "https://www.krollermuller.nl/en/collection/vincent-van-gogh-terrace-of-a-caf-at-night-place-du-forum-km-108-565", "Kröller-Müller Museum", "官方机构", "梵高《夜间露天咖啡座》1888，暖黄橙绿与深蓝对比"),
    ("vangogh-colours", "Vincent's colours — Van Gogh Museum", "https://www.vangoghmuseum.nl/en/art-and-stories/stories/vincents-colours", "Van Gogh Museum", "官方机构", "梵高研究色彩理论，互补色相互增强"),
]
INST = {
 "gestalt-organization-laws": ("名称：鲁宾花瓶（Rubin's vase）；地点：丹麦哥本哈根；设计者：埃德加·鲁宾（Edgar Rubin）；年份：1915 年。图与底可互换，是格式塔组织律的经典图例。此处仅列名称、地点、作者与年份信息，不复制图像。", ["nba-rubin-vase", "britannica-gestalt"], True, "鲁宾花瓶由 Niels Bohr Archive 单源直证；Britannica 为格式塔组织原则概念背景源，非该图专页。"),
 "color-psychology": ("名称：布里斯托尔皇家儿童医院采血室彩色壁画；地点：英国布里斯托尔；设计者：亚历克斯·雷（Alex Ray）；年份：2020 年。鲜艳色彩转移儿童对采血的焦虑。此处仅列名称、地点、作者与年份信息，不复制图像。", ["uhbw-hospital-mural", "pmc-color-rooms"], True, "该壁画报道为医院官方单源；PMC 随机对照研究为“色彩影响福祉”的机制证据，非该壁画专页。"),
 "environmental-psychology": ("名称：西格拉姆大厦广场／Whyte 街头生活项目；地点：美国纽约；设计者：威廉·H·怀特（William H. Whyte）；年份：1970 年代观察、1980 年发布。通过实地观察研究人在城市广场的行为。此处仅列名称、地点、作者与年份信息，不复制图像。", ["pps-whyte-plazas", "mas-whyte-plazas"], False, ""),
 "east-west-color-compare": ("名称：《千里江山图》（王希孟，1113，北京故宫）与《日出·印象》（莫奈，1872，勒阿弗尔）；地点：中国／法国；设计者：王希孟、克劳德·莫奈；年份：1113 / 1872。前者在青绿中求变化，后者关注光色与色彩理论。此处仅列名称、地点、作者与年份信息，不复制图像。", ["dpm-qianli", "britannica-impression-sunrise"], False, ""),
 "monumental-scale": ("名称：华盛顿纪念碑（Washington Monument）；地点：美国华盛顿特区国家广场；设计者：罗伯特·米尔斯（Robert Mills）；年份：1848 年动工、1884 年建成。此处仅列名称、地点、作者与年份信息，不复制图像。", ["nps-washington-monument", "britannica-washington-monument"], True, "高度两源不同（NPS 555 英尺、Britannica 554 英尺 7 英寸，2014 重算），设计者仅 Britannica 直证。"),
 "intimate-scale": ("名称：待庵茶室；地点：日本京都府大山崎町妙喜庵内；设计者：相传为千利休；年份：天正 10 年（1582 年）。二帖榻榻米、设躙口，尺度极小。此处仅列名称、地点、作者与年份信息，不复制图像。", ["omotesenke-taian", "kyoto-taian"], True, "设计者与年份为“相传”（表千家官方用 It is said），待补确证来源。"),
 "tints-shades": ("名称：《夜巡》（The Night Watch）；地点：荷兰阿姆斯特丹国立博物馆；设计者：伦勃朗（Rembrandt van Rijn）；年份：1642 年。以明暗层次塑造体积与焦点。此处仅列名称、地点、作者与年份信息，不复制图像。", ["rijks-nightwatch-things", "britannica-nightwatch"], True, "两源用 chiaroscuro/投影，非逐字 tints and shades；概念对应为解读。"),
 "split-primary": ("名称：《夜间露天咖啡座》（Terrace of a Café at Night）；地点：荷兰奥特洛 Kröller-Müller 博物馆藏（绘于阿尔勒）；设计者：文森特·梵高；年份：1888 年 9 月。暖黄橙绿与深蓝对比。此处仅列名称、地点、作者与年份信息，不复制图像。", ["kroller-cafe-terrace", "vangogh-colours"], True, "两源未用 split-complementary 字面术语，该配色结构归类为概念解读。"),
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
    print("round56 applied")


if __name__ == "__main__":
    main()
