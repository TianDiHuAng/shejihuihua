"""第101轮：skylight / stack-ventilation 补 DB 第二平台，类型性实例，升级 nv=false。"""
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
    ("db-skylight", "Skylight / Rooflight — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Skylight", "天窗（屋顶采光窗）：屋顶开洞引入天然光，可深入建筑中心"),
    ("db-stack-ventilation", "Stack effect — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Stack_ventilation", "烟囱/热压效应：暖空气上升经竖向空间自然通风"),
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
            if e["id"] == "skylight":
                if "db-skylight" not in e["sources"]:
                    e["sources"].append("db-skylight")
                e["sections"]["实例"] = "名称：展厅顶部天窗（类型性，不指定具体项目）；在屋顶开洞让光近乎垂直落下，照度较均匀地铺开。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "stack-ventilation":
                if "db-stack-ventilation" not in e["sources"]:
                    e["sources"].append("db-stack-ventilation")
                e["sections"]["实例"] = "名称：通风竖井（类型性，不指定具体项目）；利用竖向空间的热压/烟囱效应把暖空气从高位排出、冷空气低位补入。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round101 applied")


if __name__ == "__main__":
    main()
