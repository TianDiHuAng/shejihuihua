"""第16轮复核应用：six-principles 升级；perspective / sunken-courtyard 收窄。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("jfdaily-xiangshanbang", "香山帮与苏州园林营造 — 解放日报·上观新闻", "https://www.jfdaily.com/wx/detail.do?id=1027626", "解放日报", "官方机构", "记载苏州古典园林多由香山帮匠人集体营造、无具名建筑师"),
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
            k = e["id"]
            if k == "six-principles":
                e["sections"]["待核实"] = "原书名（《古今画品》/《画品》）与版本流传说解不一，已在正文并列；成书年代学界通行约公元 500 年。"
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            elif k == "perspective":
                e["sections"]["待核实"] = "学界通行定为约 1413 年（约数），原始文献年代仍存争议；正文不写死具体年份。"
                e["pending_notes"] = "透视演示年代取学界通行约数（约 1413 年），原始文献年代存争议，正文不写死。"
                ch = True
            elif k == "sunken-courtyard":
                e["sections"]["实例"] = "名称：静安寺下沉广场（上海）／拙政园（苏州）；地点：中国上海／苏州；设计者：静安寺广场由卢济威主持城市设计、顾如珍负责建筑工程；拙政园由王献臣建、文徵明参与设计（一般苏州庭院由香山帮匠人集体营造、无具名建筑师）；年份：静安寺广场 1999 年落成，拙政园明正德四年（1509 年）。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "两类实例的历史原型对应关系、以及一般苏州庭院的具体营造者归属待核实。"
                for r in ["suzhou-ylj-zhuozhengyuan", "peopleapp-zhuozhengyuan", "jfdaily-xiangshanbang"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["pending_notes"] = "两类实例的历史原型对应关系与一般苏州庭院营造者归属待核实。"
                ch = True
            else:
                continue
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added", added)


if __name__ == "__main__":
    main()
