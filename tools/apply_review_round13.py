"""第13轮复核应用：chinese-architecture-style 与 daylighting 实例升级；daylight-factor 收窄。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("designingbuildings-forbidden-city", "Forbidden City — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Forbidden_City", "Designing Buildings Wiki", "学术著作", "记载紫禁城位于北京，始建于明永乐年间（1406–1420），由明成祖朱棣营建"),
    ("travelchinaguide-forbidden-city", "Forbidden City, Beijing — TravelChinaGuide", "https://www.travelchinaguide.com/cityguides/beijing/forbidden.htm", "TravelChinaGuide", "官方机构", "记载紫禁城北京、明成祖朱棣、1406–1420；蒯祥为单源附注不作定论"),
    ("architectuul-kimbell", "Kimbell Art Museum — Architectuul", "https://architectuul.com/architecture/kimbell-art-museum", "Architectuul", "学术著作", "记载金贝尔美术馆位于美国沃思堡，Louis I. Kahn 设计，1972 年建成，以自然光为主题"),
    ("designingbuildings-louis-kahn", "Louis Kahn — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Louis_Kahn", "Designing Buildings Wiki", "学术著作", "记载 Louis Kahn 设计金贝尔美术馆，运用自然采光"),
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
            "note": f"访问于 2026-11-22，由核验子任务实抓 HTTP 200 并核对正文；canonical 直连待复；{note}",
        })
        added.append(sid)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "chinese-architecture-style":
                e["sections"]["实例"] = "名称：北京紫禁城；地点：北京；设计者：明成祖朱棣（永乐帝）主持营建；年份：1406–1420 年。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "具体单体建筑的工匠与设计者归属（如蒯祥）目前仅单源记载，待补充独立来源。"
                for r in ["designingbuildings-forbidden-city", "travelchinaguide-forbidden-city"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "具体单体建筑工匠归属（蒯祥）仅单源，待补充独立来源。"
                ch = True
            elif e["id"] == "daylighting":
                e["sections"]["实例"] = "名称：金贝尔美术馆（Kimbell Art Museum）；地点：美国沃思堡；设计者：路易·康（Louis I. Kahn）；年份：1972 年。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "采光系数等具体数值按一般性说明，须按当地规范校核。"
                for r in ["architectuul-kimbell", "designingbuildings-louis-kahn"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "daylight-factor":
                e["sections"]["待核实"] = "均布阴天假设已由采光系数标准解释；仅具体实例的采光系数数值与设计者待补充独立来源。"
                e["pending_notes"] = "具体实例的采光系数数值与设计者待补充独立来源。"
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added", added)


if __name__ == "__main__":
    main()
