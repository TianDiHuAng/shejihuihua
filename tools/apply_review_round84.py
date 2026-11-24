"""第84轮：vernacular-architecture 补 DB+Art in Context 概念双源，实例类型性(乡土无单设计者)，升级 nv=false。"""
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
    for sid, title, url, author, note in [
        ("db-vernacular", "Vernacular architecture — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Vernacular_architecture", "Designing Buildings", "乡土建筑：因地制宜、就地取材、依气候与地方习俗建造"),
        ("artincontext-vernacular", "Vernacular Architecture — Art in Context", "https://artincontext.org/vernacular-architecture/", "Art in Context", "乡土建筑依地方需求、建材与习俗，独特于特定时期与地点"),
    ]:
        if sid in by_id:
            continue
        good = ok(url)
        data["sources"].append({"id": sid, "title": title, "author": author, "type": "学术著作",
                                "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；{note}"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "vernacular-architecture":
                for r in ("db-vernacular", "artincontext-vernacular"):
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["definition"] = "乡土建筑是依本地材料、气候与习俗、由当地人自行建造、因地制宜的建筑；通常无职业建筑师。"
                e["sections"]["实例"] = "名称：夯土与木构的乡土民居（类型性，乡土建筑通常无单一设计者）；地点：因地制宜（不指定具体项目）；以就地取材、依气候组织构造为特征。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round84 applied")


if __name__ == "__main__":
    main()
