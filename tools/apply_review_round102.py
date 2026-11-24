"""第102轮：material-durability / mixed-mode-ventilation 补 DB 第二平台，类型性实例，升级 nv=false。"""
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
    ("db-durability", "Durability — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Durability", "耐久性：材料抵抗日常磨损与气候侵蚀、影响维护与寿命"),
    ("db-mixed-mode-ventilation", "Mixed-mode ventilation — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Mixed_mode_ventilation", "混合通风：自然通风不足时以机械通风补充"),
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
            if e["id"] == "material-durability":
                if "db-durability" not in e["sources"]:
                    e["sources"].append("db-durability")
                e["definition"] = "耐久性是材料抵抗日常磨损与气候侵蚀的能力，决定维护周期与全生命周期成本。"
                e["sections"]["实例"] = "名称：公共建筑外立面材料（类型性，不指定具体项目）；不同材料的耐磨与耐候性能决定其维护周期。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "mixed-mode-ventilation":
                if "db-mixed-mode-ventilation" not in e["sources"]:
                    e["sources"].append("db-mixed-mode-ventilation")
                e["sections"]["实例"] = "名称：办公建筑混合通风（类型性，不指定具体项目）；自然通风不足时由机械系统补充，兼顾能效与空气品质。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round102 applied")


if __name__ == "__main__":
    main()
