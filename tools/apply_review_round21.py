"""第21轮复核应用：space-definition（巴塞罗那德国馆）、human-scale（帕伊米奥疗养院）双源升级。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("miesbcn-barcelona-pavilion", "The Pavilion — Fundació Mies van der Rohe", "https://miesbcn.com/the-pavilion/", "Fundació Mies van der Rohe", "官方机构", "记载巴塞罗那德国馆由密斯与莉莉·赖希设计，1929 年巴塞罗那世博会"),
    ("archdaily-barcelona-pavilion", "AD Classics: Barcelona Pavilion — ArchDaily", "https://www.archdaily.com/109135/ad-classics-barcelona-pavilion-mies-van-der-rohe", "ArchDaily", "学术著作", "记载 1929 年建成、密斯与莉莉·赖希设计"),
    ("xinhua-paimio", "Paimio Sanatorium — Xinhua", "https://english.news.cn/20260805/2f2673e5085d4c72aa0efda6b8b087a5/c.html", "新华网", "官方机构", "记载帕伊米奥疗养院属阿尔托作品、1933 年建成"),
    ("paimio-official", "The Architecture of Empathy — Paimio Sanatorium", "https://paimiosanatorium.com/the-architecture-of-empathy/", "Paimio Sanatorium", "官方机构", "记载阿尔瓦与艾诺·阿尔托 1933 年杰作、1929 年委托"),
]


def main():
    path = ROOT / "data" / "sources.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    added = []
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        data["sources"].append({
            "id": sid, "title": title, "author": author, "type": typ,
            "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
            "note": f"访问于 2026-11-22，由核验子任务实抓 HTTP 200 并核对正文；{note}",
        })
        added.append(sid)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            k = e["id"]
            if k == "space-definition":
                e["sections"]["实例"] = "名称：巴塞罗那德国馆（Barcelona Pavilion）；地点：西班牙巴塞罗那蒙特惠奇山；设计者：密斯·凡·德·罗与莉莉·赖希（Ludwig Mies van der Rohe & Lilly Reich）；年份：1929 年。以独立界面与自由平面界定空间（注：为通透展亭，非封闭室内）。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项。"
                for r in ["miesbcn-barcelona-pavilion", "archdaily-barcelona-pavilion"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            elif k == "human-scale":
                e["sections"]["实例"] = "名称：帕伊米奥结核病疗养院（Paimio Sanatorium）；地点：芬兰图尔库附近；设计者：阿尔瓦·阿尔托与艾诺·阿尔托（Alvar & Aino Aalto）；年份：1933 年建成（1929 年委托）。以病人的身体姿态与使用感受确定细部尺度。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项。"
                for r in ["xinhua-paimio", "paimio-official"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            else:
                continue
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added", added)


if __name__ == "__main__":
    main()
