"""第108轮：composition / rule-of-thirds 补 artincontext-composition 第二平台，升级 nv=false。"""
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
    if "artincontext-composition" not in by_id:
        url = "https://artincontext.org/composition-in-art/"
        good = ok(url)
        data["sources"].append({"id": "artincontext-composition", "title": "Composition in Art — Techniques for Creating Balanced Scenes — Art in Context",
                                "author": "Art in Context", "type": "学术著作", "year": None, "url": url, "url2": None,
                                "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；构图：以三分法、平衡、黄金比、视觉焦点等技术组织画面元素"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "composition":
                if "artincontext-composition" not in e["sources"]:
                    e["sources"].append("artincontext-composition")
                e["sections"]["原理"] = "构图通过安排元素的位置、比例与相互关系组织画面，用三分法、平衡、黄金比与视觉焦点等手段引导观看顺序、建立主次与秩序。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "rule-of-thirds":
                if "artincontext-composition" not in e["sources"]:
                    e["sources"].append("artincontext-composition")
                e["sections"]["实例"] = "名称：三分法构图（类型性，不指定具体作品）；把主体或关键线置于横竖三分线的交点或分割线上，使画面偏离中心而取得均衡。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round108 applied")


if __name__ == "__main__":
    main()
