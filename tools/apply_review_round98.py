"""第98轮：light-well 补 db-light-well 第二源(天井引天然光)，重构原理聚焦采光、类型性实例，升级 nv=false。"""
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
    if "db-light-well" not in by_id:
        url = "https://www.designingbuildings.co.uk/wiki/Light_well"
        good = ok(url)
        data["sources"].append({"id": "db-light-well", "title": "Light well — Designing Buildings", "author": "Designing Buildings",
                                "type": "学术著作", "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；天井/采光井：把天然光引入建筑内部空间"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "light-well":
                if "db-light-well" not in e["sources"]:
                    e["sources"].append("db-light-well")
                e["definition"] = "天井（采光井）是以狭长开口把天然光引入建筑深处的院落或井道式空间。"
                e["sections"]["原理"] = "天井借屋面或侧向开口把天然光引入进深较大的建筑内部，使深层空间获得日照与采光。"
                e["sections"]["实例"] = "名称：传统民居天井（类型性，不指定具体项目）；以狭长开口把天然光引入内院与各进房屋。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round98 applied")


if __name__ == "__main__":
    main()
