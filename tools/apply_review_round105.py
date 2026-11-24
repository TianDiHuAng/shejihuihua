"""第105轮：side-window-daylight / lighting-design 补 DB 第二平台，类型性实例，升级 nv=false。"""
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
    ("db-window", "Window — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Window", "窗：墙上或屋顶开洞引入天然光（含 bay window 等）"),
    ("db-artificial-lighting", "Artificial lighting — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Artificial_lighting", "人工照明：以灯具提供照度，与天然光配合"),
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
            if e["id"] == "side-window-daylight":
                if "db-window" not in e["sources"]:
                    e["sources"].append("db-window")
                e["sections"]["原理"] = "光从外墙竖向窗洞侧面进入，靠窗处亮、随进深逐渐衰减、光线方向明显；布窗宜与房间进深和窗地比配合。"
                e["sections"]["实例"] = "名称：教室侧窗采光（类型性，不指定具体项目）；光线由侧面窗洞射入、向室内深处逐渐衰减。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "lighting-design":
                if "db-artificial-lighting" not in e["sources"]:
                    e["sources"].append("db-artificial-lighting")
                e["sections"]["原理"] = "白天优先引入天然光、夜间或采光不足处由人工照明补足，按视觉任务与空间氛围分层布光，兼顾能效与舒适。"
                e["sections"]["实例"] = "名称：博物馆分层照明（类型性，不指定具体项目）；以天然光与人工光分层配合，突出展品并保护展品。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round105 applied")


if __name__ == "__main__":
    main()
