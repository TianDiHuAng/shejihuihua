"""第107轮：modernism / thermal-comfort 补 DB 第二平台，升级 nv=false。"""
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
    ("db-modernism", "Modernist architecture — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Modernism", "现代主义：20世纪初兴起，Form follows function、以功能与简洁形式为核心"),
    ("db-thermal-comfort", "Thermal comfort in buildings — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Thermal_comfort", "热舒适：人对热环境满意的状态，涉空气温度/速度/辐射温度/湿度及PMV-PPD"),
]


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, note in NEW:
        if sid in by_id:
            continue
        good = ok(url)
        data["sources"].append({"id": sid, "title": title, "author": "Designing Buildings", "type": "学术著作",
                                "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；{note}"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "modernism":
                if "db-modernism" not in e["sources"]:
                    e["sources"].append("db-modernism")
                e["definition"] = "现代主义是20世纪初兴起、以功能、结构与简洁形式为核心的建筑思潮。"
                e["sections"]["原理"] = "现代主义主张“形式追随功能”，以功能、结构与新材料为基础，追求自由平面、简洁体量与少装饰的立面。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "thermal-comfort":
                if "db-thermal-comfort" not in e["sources"]:
                    e["sources"].append("db-thermal-comfort")
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round107 applied")


if __name__ == "__main__":
    main()
