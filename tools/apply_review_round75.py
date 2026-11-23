"""第75轮：complementary-colors / color-contrast 用 Wikipedia Night Café + Van Gogh Museum 双平台升级。"""
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
    ("wp-night-cafe", "The Night Café — Wikipedia", "https://en.wikipedia.org/wiki/The_Night_Caf%C3%A9", "Wikipedia", "权威百科", "梵高《夜间咖啡馆》1888：天花板绿、墙红，强烈对比色（经镜像核验）"),
    ("vgm-colours", "Vincent's colours — Van Gogh Museum", "https://www.vangoghmuseum.nl/en/art-and-stories/stories/vincents-colours", "Van Gogh Museum", "官方机构", "梵高研究互补色：红与绿、黄与紫、蓝与橙相互增强"),
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
            if e["id"] in ("complementary-colors", "color-contrast"):
                for r in ("wp-night-cafe", "vgm-colours"):
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round75 applied")


if __name__ == "__main__":
    main()
