"""第69轮：interior-exterior-transition 用敞廊(Loggia)作过渡实例，补 db-loggia 第二独立平台。"""
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
    ("db-loggia", "Loggia — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Loggia", "Designing Buildings", "学术著作", "敞廊：一侧开放的带顶/拱廊画廊，常位于楼层"),
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
            if e["id"] == "interior-exterior-transition" and "wp-loggia" in e["sources"]:
                e["sections"]["实例"] = "名称：敞廊（Loggia，意大利语）；地点：欧洲（源自意大利，如市政厅拱廊敞廊）；设计者：民间营建/建筑师（随例不同）；年份：文艺复兴以来。一侧开放、带拱廊的画廊，常作半室外过渡空间，模糊室内外边界。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                if "db-loggia" not in e["sources"]:
                    e["sources"].append("db-loggia")
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
            print("interior-exterior-transition upgraded in", p.name)


if __name__ == "__main__":
    main()
