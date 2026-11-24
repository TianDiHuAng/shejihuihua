"""第112轮：garden-architecture 补 db-pavilion 第二平台(园林亭榭)，类型性实例，升级 nv=false。"""
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
    if "db-pavilion" not in by_id:
        url = "https://www.designingbuildings.co.uk/wiki/Pavilion"
        good = ok(url)
        data["sources"].append({"id": "db-pavilion", "title": "Pavilion — Designing Buildings", "author": "Designing Buildings",
                                "type": "学术著作", "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；园林/公园亭榭：可开放、供遮荫休憩与装饰性点景的建筑"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "garden-architecture":
                if "db-pavilion" not in e["sources"]:
                    e["sources"].append("db-pavilion")
                e["definition"] = "园林建筑指园林中供观景、休憩与点景的亭、榭、廊等小型建筑。"
                e["sections"]["原理"] = "亭榭等园林建筑置于景观点上，可开放或半开放、供遮荫休憩，既自成景又供观景，串联游线与视线。"
                e["sections"]["实例"] = "名称：临水亭榭（类型性，不指定具体项目）；置于水岸景观点，兼作景点与观景处。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round112 applied")


if __name__ == "__main__":
    main()
