"""第12轮复核应用：bauhaus 补两条独立权威来源并升级；light-well 收窄待核实表述。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("stiftung-bauhaus-dessau", "Bauhaus Building — Stiftung Bauhaus Dessau", "https://www.bauhaus-dessau.de/en/venues/bauhaus-building/", "Stiftung Bauhaus Dessau", "官方机构", "官方站记载 Bauhaus Building 由 Walter Gropius 规划与实现，1926-12-04 落成"),
    ("archdaily-bauhaus-dessau", "Bauhaus Dessau — ArchDaily", "https://www.archdaily.com/87728/ad-classics-bauhaus-dessau-walter-gropius", "ArchDaily", "学术著作", "ArchDaily 记载 Architects: Walter Gropius; Year: 1926"),
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
            "note": f"访问于 2026-11-22，由核验子任务实抓 HTTP 200 并核对标题/正文；canonical 直连待复；{note}",
        })
        added.append(sid)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "bauhaus":
                e["sections"]["实例"] = "名称：德绍包豪斯校舍；地点：德国德绍；设计者：瓦尔特·格罗皮乌斯（Walter Gropius）；年份：1925–1926 年（1926-12-04 落成）。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项。"
                for ref in ["stiftung-bauhaus-dessau", "archdaily-bauhaus-dessau"]:
                    if ref not in e["sources"]:
                        e["sources"].append(ref)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "light-well":
                e["sections"]["待核实"] = "热压机制的一般原理可参见自然通风相关条目；本条目尚缺具体天井实例的实测数据。"
                e["pending_notes"] = "具体天井实例的采光与通风实测数据待补充独立来源（机制层面可参见自然通风条目）。"
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added", added)


if __name__ == "__main__":
    main()
