"""第47轮：为 mannerism/beaux-arts/one-point-perspective/foreshortening 补具名实例（8 源）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("palazzote-official", "Palazzo Te — Centro Palazzo Te", "https://www.centropalazzote.it/", "Centro Palazzo Te", "官方机构", "得特宫 1525–1535，Federico II Gonzaga 委托，Giulio Romano"),
    ("theartstory-mannerism", "Mannerism — TheArtStory", "https://www.theartstory.org/movement/mannerism/", "TheArtStory", "学术著作", "样式主义，Palazzo del Te 1524–1534"),
    ("pop-garnier", "Palais Garnier — POP/Mérimée PA00089004", "https://pop.culture.gouv.fr/notice/merimee/PA00089004", "法国文化部", "官方机构", "巴黎歌剧院，Charles Garnier，1862/1875"),
    ("operadeparis-garnier", "Palais Garnier — Opéra national de Paris", "https://www.operadeparis.fr/en/visits/palais-garnier", "Opéra national de Paris", "官方机构", "加尼叶宫（巴黎歌剧院）"),
    ("cenacolo-history", "History — Cenacolo Vinciano", "https://cenacolovinciano.org/en/history/", "Cenacolo Vinciano", "官方机构", "最后的晚餐，米兰圣玛利亚感恩修道院餐厅"),
    ("italia-lastsupper", "The Last Supper — Italia.it", "https://www.italia.it/en/lombardy/milan/da-vinci-last-supper-museum", "Italia.it", "官方机构", "达·芬奇《最后的晚餐》米兰"),
    ("pinacotecabrera-christ", "Cristo morto — Pinacoteca di Brera", "https://pinacotecabrera.org/en/collezioni/collezione-on-line/cristo-morto/", "Pinacoteca di Brera", "官方机构", "曼特尼亚《哀悼基督》，米兰布雷拉，约1483"),
    ("artchive-mantegna", "The Lamentation over the Dead Christ — Artchive", "https://www.artchive.com/artwork/the-lamentation-over-the-dead-christ-andrea-mantegna-c-1490/", "Artchive", "学术著作", "曼特尼亚《哀悼基督》，强烈透视缩短"),
]
INST = {
    "mannerism": ("名称：得特宫（Palazzo del Te）；地点：意大利曼图亚；设计者：朱利奥·罗马诺（Giulio Romano）；年份：约 1524–1535 年（各家标年 1524–1534 / 1525–1535 并列）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["palazzote-official", "theartstory-mannerism"]),
    "beaux-arts": ("名称：巴黎歌剧院（Palais Garnier）；地点：法国巴黎第九区；设计者：夏尔·加尼叶（Charles Garnier）；年份：1861–1875 年（1862 动工、1875 启用）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["pop-garnier", "operadeparis-garnier"]),
    "one-point-perspective": ("名称：《最后的晚餐》（The Last Supper）；地点：意大利米兰圣玛利亚感恩修道院餐厅；设计者：列奥纳多·达·芬奇（Leonardo da Vinci）；年份：约 1495–1498 年。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["cenacolo-history", "italia-lastsupper"]),
    "foreshortening": ("名称：《哀悼基督》（Lamentation over the Dead Christ）；地点：意大利米兰布雷拉美术馆；设计者：安德烈亚·曼特尼亚（Andrea Mantegna）；年份：约 1480–1490 年（各家标年 1480/1483/1490 并列）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["pinacotecabrera-christ", "artchive-mantegna"]),
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
                inst, srcs = INST[e["id"]]
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
    print("round47 instances applied")


if __name__ == "__main__":
    main()
