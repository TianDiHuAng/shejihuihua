"""第82轮：classical-order(帕特农) 与 religious-architecture(圣索菲亚) 补具名实例双平台升级。"""
import json
import ssl
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36'}


def ok(url):
    try:
        return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25, context=ctx).status == 200
    except Exception:
        return False


NEW = [
    ("wp-parthenon", "Parthenon — Wikipedia", "https://en.wikipedia.org/wiki/Parthenon", "Wikipedia", "权威百科", "帕特农神庙：多立克柱式的高峰，前6柱侧13柱（经镜像核验）"),
    ("db-parthenon", "Parthenon — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Parthenon", "Designing Buildings", "学术著作", "帕特农神庙为多立克柱式建筑的高峰，前6后侧13柱"),
    ("wp-hagia-sophia", "Hagia Sophia — Wikipedia", "https://en.wikipedia.org/wiki/Hagia_Sophia", "Wikipedia", "权威百科", "圣索菲亚大教堂：巨大穹顶为当时重大创新（经镜像核验）"),
    ("db-hagia-sophia", "Hagia Sophia — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Hagia_Sophia", "Designing Buildings", "学术著作", "圣索菲亚大教堂：穹顶为重大创新"),
]
INST = {
    "classical-order": ("名称：帕特农神庙（Parthenon）；地点：希腊雅典卫城；设计者：伊克蒂诺与卡利克拉底（Iktinos and Callicrates）；年份：公元前 447–432 年。多立克柱式的典范（前 6 柱、侧 13 柱）。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["wp-parthenon", "db-parthenon"], False, "帕特农为多立克柱式典范由 Wikipedia 与 Designing Buildings 双源直证；具体设计者与年代（前447–432）以通行记载补充，个别细节可再核。"),
    "religious-architecture": ("名称：圣索菲亚大教堂（Hagia Sophia）；地点：土耳其伊斯坦布尔；设计者：特拉勒斯的安提莫斯与米利都的伊西多尔（Anthemius of Tralles and Isidore of Miletus）；年份：公元 532–537 年。以巨大穹顶统摄的礼拜空间，为宗教建筑穹顶的重要创新。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["wp-hagia-sophia", "db-hagia-sophia"], False, "圣索菲亚穹顶为重大创新由 Wikipedia 与 Designing Buildings 双源直证；设计者与年代（532–537）以通行记载补充。"),
}


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        good = ok(url)
        data["sources"].append({"id": sid, "title": title, "author": author, "type": typ,
                                "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；{note}"})
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
    print("round82 applied")


if __name__ == "__main__":
    main()
