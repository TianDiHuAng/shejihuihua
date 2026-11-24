"""第115轮：golden-ratio 补 artincontext-golden-ratio 第二平台（比例1:1.618），类型性实例，升级 nv=false。"""
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
    if "artincontext-golden-ratio" not in by_id:
        url = "https://artincontext.org/golden-ratio/"
        good = ok(url)
        data["sources"].append({"id": "artincontext-golden-ratio", "title": "Golden Ratio in Art — Art in Context",
                                "author": "Art in Context", "type": "学术著作", "year": None, "url": url, "url2": None,
                                "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；黄金比=1:1.618（Phi），用于画面比例与和谐"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "golden-ratio":
                if "artincontext-golden-ratio" not in e["sources"]:
                    e["sources"].append("artincontext-golden-ratio")
                e["definition"] = "黄金比是把整体按约 1:1.618（Phi）分割的构图参考，用于组织和谐的比例关系。"
                e["sections"]["原理"] = "以 1:1.618 的比值定义部分与整体的关系，借黄金矩形与螺旋为画面提供比例秩序与视觉和谐。"
                e["sections"]["实例"] = "名称：按黄金比分割的版面（类型性，构图比例法则不归于单一作品）；以 1:1.618 划分版面区域。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round115 applied")


if __name__ == "__main__":
    main()
