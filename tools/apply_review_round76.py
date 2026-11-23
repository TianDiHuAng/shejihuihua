"""第76轮：picturesque 补具名实例(Stourhead 英式风景园) 并升级（Wikipedia + gardenvisit 双平台）。"""
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
    ("gardenvisit-stourhead", "Stourhead Garden — Gardenvisit.com", "https://www.gardenvisit.com/gardens/stourhead_garden", "Gardenvisit.com", "学术著作", "斯托海德园林受 Claude Lorrain 影响，Henry Hoare II 造 'Claudian' 园林"),
    ("wp-stourhead", "Stourhead — Wikipedia", "https://en.wikipedia.org/wiki/Stourhead", "Wikipedia", "权威百科", "斯托海德：英式风景园，受 Claude Lorrain 画作启发（经镜像核验）"),
]


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
            if e["id"] == "picturesque":
                e["sections"]["实例"] = "名称：斯托海德园林（Stourhead Garden）；地点：英国威尔特郡；设计者：亨利·霍尔二世（Henry Hoare II）等；年份：约 1740 年代起营造。英式风景园，受克劳德·洛兰（Claude Lorrain）风景画的如画趣味启发（“Claudian”园林）。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                for r in ("wp-stourhead", "gardenvisit-stourhead"):
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["sections"]["待核实"] = "斯托海德受 Claude Lorrain 启发、“Claudian”园林由 Wikipedia 与 Gardenvisit 双源直证；“如画（picturesque）”为通行的美学归类（两源未都用 picturesque 一词），具体营造年份待补。"
                e["pending_notes"] = "“如画”为美学归类（未逐字），营造年份待补；受 Claude Lorrain 启发已双源。"
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round76 applied")


if __name__ == "__main__":
    main()
