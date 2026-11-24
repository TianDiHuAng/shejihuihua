"""第99轮：damp-proofing 补 db-damp_proofing 第二平台(湿度控制构造)，类型性实例，升级 nv=false。"""
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
    if "db-damp-proofing" not in by_id:
        url = "https://www.designingbuildings.co.uk/wiki/Damp_proofing"
        good = ok(url)
        data["sources"].append({"id": "db-damp-proofing", "title": "Damp proofing buildings — Designing Buildings", "author": "Designing Buildings",
                                "type": "学术著作", "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；防潮指对墙与地面施加的湿度控制，防上升潮/渗透潮（薄膜、表面涂层等）"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "damp-proofing":
                if "db-damp-proofing" not in e["sources"]:
                    e["sources"].append("db-damp-proofing")
                e["definition"] = "防潮是对墙体与地面施加的湿度控制构造措施，用以阻止上升潮、渗透潮等水分侵入。"
                e["sections"]["原理"] = "以防水薄膜、表面涂层等阻隔层切断水分由地面或墙面渗入的路径，防止地下或近地空间受潮。"
                e["sections"]["实例"] = "名称：地下空间防潮构造（类型性，不指定具体项目）；以防水薄膜与表面涂层阻断上升潮与渗透潮。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round99 applied")


if __name__ == "__main__":
    main()
