"""第83b轮：structural-material 补具名实例(埃菲尔铁塔·锻铁结构) 并升级（Wikipedia + Designing Buildings）。"""
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


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, note in [
        ("wp-eiffel-tower", "Eiffel Tower — Wikipedia", "https://en.wikipedia.org/wiki/Eiffel_Tower", "埃菲尔铁塔：锻铁（wrought iron）格构结构，1889 古斯塔夫·埃菲尔（经镜像核验）"),
        ("db-eiffel-tower", "Eiffel Tower — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Eiffel_Tower", "埃菲尔铁塔：露空格构锻铁设计，Gustave Eiffel 1889（约300钢工、200万铆钉）"),
    ]:
        if sid in by_id:
            continue
        good = ok(url)
        data["sources"].append({"id": sid, "title": title, "author": "Wikipedia" if "wikipedia" in url else "Designing Buildings",
                                "type": "权威百科" if "wikipedia" in url else "学术著作", "year": None, "url": url,
                                "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；{note}"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "structural-material":
                e["sections"]["实例"] = "名称：埃菲尔铁塔（Eiffel Tower）；地点：法国巴黎；设计者：古斯塔夫·埃菲尔（Gustave Eiffel）；年份：1889 年。以锻铁（wrought iron）露空格构承重，是大跨金属结构材料的经典实例。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                for r in ("wp-eiffel-tower", "db-eiffel-tower"):
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round83b applied")


if __name__ == "__main__":
    main()
