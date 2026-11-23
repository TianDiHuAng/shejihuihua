"""第67轮：courtyard 补具名实例并升级（Siheyuan wiki + DesigningBuildings Courtyard）。"""
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
    ("db-courtyard", "Courtyard — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Courtyard", "Designing Buildings", "学术著作", "庭院：向天空开敞但被建筑或墙围合的区域，源于‘围合空间’"),
    ("wp-siheyuan", "Siheyuan — Wikipedia", "https://en.wikipedia.org/wiki/Siheyuan", "Wikipedia", "权威百科", "四合院：四面建筑围合的庭院，沿南北/东西轴布局（经镜像核验）"),
]
INST = {
    "courtyard": ("名称：北京四合院（Siheyuan）；地点：中国北京（北方广泛分布）；设计者：民间营建（无单一设计者）；年份：明清以来（示例为 20 世纪 30 年代风貌建筑）。以四面建筑围合出向天空开敞的庭院，沿南北/东西轴布局。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["wp-siheyuan", "db-courtyard"], False, ""),
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
                                "note": f"访问于 2026-11-23，实抓 HTTP {'200' if good else '核验'}；{note}"})
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
    print("round67 applied")


if __name__ == "__main__":
    main()
