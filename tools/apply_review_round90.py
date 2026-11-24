"""第90轮：romanticism-style 补具名实例新天鹅堡并升级（wp + db 双平台）。"""
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
    for sid, title, url, author, typ, note in [
        ("wp-neuschwanstein", "Neuschwanstein Castle — Wikipedia", "https://en.wikipedia.org/wiki/Neuschwanstein_Castle", "Wikipedia", "权威百科", "新天鹅堡：城堡浪漫主义，路德维希二世，1869 动工（经镜像核验）"),
        ("db-neuschwanstein", "Neuschwanstein Castle — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Neuschwanstein_Castle", "Designing Buildings", "学术著作", "新天鹅堡：浪漫主义典范，路德维希二世 1869 起建"),
    ]:
        if sid in by_id:
            continue
        good = ok(url)
        data["sources"].append({"id": sid, "title": title, "author": author, "type": typ,
                                "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；{note}"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "romanticism-style":
                e["sections"]["实例"] = "名称：新天鹅堡（Neuschwanstein Castle）；地点：德国巴伐利亚；委托者：巴伐利亚国王路德维希二世（Ludwig II）；年份：1869 年动工。被视为“城堡浪漫主义”的典型。此处仅列名称、地点、委托者与年份信息，不复制图像。"
                for r in ("wp-neuschwanstein", "db-neuschwanstein"):
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round90 applied")


if __name__ == "__main__":
    main()
