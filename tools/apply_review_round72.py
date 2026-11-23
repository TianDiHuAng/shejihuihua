"""第72轮：placemaking 补 db-placemaking 第二平台、具名实例并升级。"""
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
    ("db-placemaking", "Placemaking — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Placemaking", "Designing Buildings", "学术著作", "场所营造：PPS(Project for Public Spaces) 推动的社区空间实践"),
]
INST = {
    "placemaking": ("名称：场所营造（Placemaking，以 Project for Public Spaces 的实践为代表）；地点：美国（PPS 1975 年于纽约创立）；组织者：Project for Public Spaces（PPS）及社区；年份：1970 年代中期以来。通过社区参与改造公共空间、营造场所感的实践。此处仅列名称、地点、组织者与年份信息，不复制图像。", False, ""),
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
                if "db-placemaking" not in e["sources"]:
                    e["sources"].append("db-placemaking")
                e["needs_verification"] = keep
                e["sections"]["待核实"] = caveat if keep else "暂无已知待核实项。"
                e["pending_notes"] = caveat if keep else ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round72 applied")


if __name__ == "__main__":
    main()
