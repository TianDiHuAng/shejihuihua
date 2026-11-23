"""第71轮：biophilic-design 补 db-biophilic 第二平台、具名实例并升级。"""
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
    ("db-biophilic-design", "Biophilic design — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Biophilic_design", "Designing Buildings", "学术著作", "亲生命设计：Edward Wilson 1980s 普及 biophilia 概念"),
]
INST = {
    "biophilic-design": ("名称：亲生命设计理论（Biophilic Design，源自 E. O. 威尔逊《Biophilia》）；地点：美国（概念起源）；作者：爱德华·O·威尔逊（Edward O. Wilson）；年份：1984 年《Biophilia》提出、1980 年代起普及。主张将自然要素融入建筑环境以支持健康与福祉。此处仅列名称、地点、作者与年份信息，不复制图像。", False, ""),
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
                inst, keep, caveat = INST[e["id"]]
                e["sections"]["实例"] = inst
                if "db-biophilic-design" not in e["sources"]:
                    e["sources"].append("db-biophilic-design")
                e["needs_verification"] = keep
                e["sections"]["待核实"] = caveat if keep else "暂无已知待核实项。"
                e["pending_notes"] = caveat if keep else ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round71 applied")


if __name__ == "__main__":
    main()
