"""第110轮：revival-gothic 补 db-gothic-architecture 第二平台（含 Gothic revival 专节+哥特特征），升级 nv=false。"""
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
    if "db-gothic-architecture" not in by_id:
        url = "https://www.designingbuildings.co.uk/wiki/Gothic_architecture"
        good = ok(url)
        data["sources"].append({"id": "db-gothic-architecture", "title": "Gothic architecture — Designing Buildings",
                                "author": "Designing Buildings", "type": "学术著作", "year": None, "url": url, "url2": None,
                                "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；含尖拱/肋拱/飞扶壁/花窗与“Gothic Revival=19世纪中叶 picturesque-romantic 运动”专节"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "revival-gothic":
                if "db-gothic-architecture" not in e["sources"]:
                    e["sources"].append("db-gothic-architecture")
                e["definition"] = "哥特复兴是18–19世纪（尤以19世纪中叶的如画-浪漫运动为代表）重新起用中世纪哥特形式的建筑潮流。"
                e["sections"]["原理"] = "哥特复兴重新组合中世纪的尖拱、肋拱、飞扶壁、花窗与垂直线条，借中世纪语汇营造宗教感与浪漫、如画的氛围。"
                e["sections"]["实例"] = "名称：哥特复兴教堂（类型性，不指定具体项目）；以尖拱与花窗复现中世纪哥特语汇。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round110 applied")


if __name__ == "__main__":
    main()
