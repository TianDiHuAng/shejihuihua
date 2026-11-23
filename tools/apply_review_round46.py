"""第46轮：为 6 个条目补具名实例（12 源，双独立）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("turismoroma-pantheon", "Pantheon — Turismo Roma", "https://www.turismoroma.it/en/places/pantheon", "Roma Capitale", "官方机构", "万神殿：哈德良 118–125 重建，Agrippa 27BC 始建"),
    ("history-pantheon", "Pantheon — HISTORY", "https://www.history.com/topics/ancient-rome/pantheon", "HISTORY", "学术著作", "约126–128 哈德良时期完成，建筑师佚名"),
    ("flw-fallingwater", "Fallingwater — Frank Lloyd Wright Foundation", "https://franklloydwright.org/site/fallingwater/", "Frank Lloyd Wright Foundation", "官方机构", "流水别墅 1935 建，有机建筑代表"),
    ("tclf-fallingwater", "Fallingwater — TCLF", "https://www.tclf.org/landscapes/fallingwater", "The Cultural Landscape Foundation", "学术著作", "1935 设计、1936–1939 施工"),
    ("centrepompidou-who", "Who are we — Centre Pompidou", "https://www.centrepompidou.fr/en/centre-pompidou/who-are-we", "Centre Pompidou", "官方机构", "1972 动工（Piano & Rogers），1977-01-31 开幕"),
    ("nwe-pompidou", "Georges Pompidou — New World Encyclopedia", "https://www.newworldencyclopedia.org/entry/Georges_Pompidou", "New World Encyclopedia", "学术著作", "高技派、Rogers & Piano，1977-01-31 开放"),
    ("nyclpc-seagram", "Seagram Building — NYC LPC LP-1664", "https://s-media.nyc.gov/agencies/lpc/lp/1664.pdf", "NYC Landmarks Preservation Commission", "官方机构", "西格拉姆大厦，Mies & Philip Johnson，1956–58"),
    ("docomomo-seagram", "Seagram Building — Docomomo US", "https://www.docomomo-us.org/register/seagram-building", "Docomomo US", "官方机构", "1956–58 建成，Mies，Park Avenue"),
    ("rietveld-house", "Rietveld Schröder House", "https://www.rietveldschroderhuis.nl/en", "Rietveld Schröder House", "官方机构", "施罗德住宅 1924，Rietveld & Truus Schröder，乌得勒支"),
    ("iconichouses-rietveld", "Rietveld Schröder House — Iconic Houses", "https://www.iconichouses.org/houses/rietveld-schroder-house", "Iconic Houses", "官方机构", "1924，Prins Hendriklaan 50, Utrecht"),
    ("smb-neue", "Neue Nationalgalerie — Staatliche Museen zu Berlin", "https://www.smb.museum/museen-einrichtungen/neue-nationalgalerie/ueber-uns/", "Staatliche Museen zu Berlin", "官方机构", "1962 委托 Mies，1965 奠基，1968 开馆"),
    ("visitberlin-neue", "Neue Nationalgalerie — visitBerlin", "https://www.visitberlin.de/en/neue-nationalgalerie", "visitBerlin", "官方机构", "1968 开馆，Mies 最后独立作品"),
]
INST = {
    "ancient-roman": ("名称：万神殿（Pantheon）；地点：意大利罗马；设计者：建筑师佚名（哈德良时期重建）；年份：约 118–128 年（阿格里帕公元前 27 年始建）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["turismoroma-pantheon", "history-pantheon"]),
    "organic-architecture": ("名称：流水别墅（Fallingwater）；地点：美国宾夕法尼亚州熊奔溪；设计者：弗兰克·劳埃德·赖特（Frank Lloyd Wright）；年份：1935 年设计、1936–1939 年建成。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["flw-fallingwater", "tclf-fallingwater"]),
    "high-tech": ("名称：蓬皮杜中心（Centre Pompidou）；地点：法国巴黎；设计者：伦佐·皮亚诺与理查德·罗杰斯（Renzo Piano & Richard Rogers）；年份：1972 年动工、1977 年 1 月 31 日开幕。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["centrepompidou-who", "nwe-pompidou"]),
    "international-style": ("名称：西格拉姆大厦（Seagram Building）；地点：美国纽约帕克大道 375 号；设计者：密斯·凡·德·罗与菲利普·约翰逊（Mies van der Rohe & Philip Johnson）；年份：1956–1958 年建成。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["nyclpc-seagram", "docomomo-seagram"]),
    "de-stijl": ("名称：施罗德住宅（Rietveld Schröder House）；地点：荷兰乌得勒支；设计者：赫里特·里特费尔德与特鲁斯·施罗德（Gerrit Rietveld & Truus Schröder）；年份：1924 年。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["rietveld-house", "iconichouses-rietveld"]),
    "minimalism-architecture": ("名称：新国家美术馆（Neue Nationalgalerie）；地点：德国柏林；设计者：密斯·凡·德·罗（Mies van der Rohe）；年份：1962 年委托、1965 年奠基、1968 年开馆。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["smb-neue", "visitberlin-neue"]),
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

    targets = {"ancient-roman", "organic-architecture", "high-tech", "international-style", "de-stijl", "minimalism-architecture"}
    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            k = e["id"]
            if k in targets:
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
    print("round46 instances applied")


if __name__ == "__main__":
    main()
