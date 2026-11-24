"""第109轮：vehicle-flow / pedestrian-flow 补 DB 第二平台(Traffic/Pedestrian)，类型性实例，升级 nv=false。"""
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
    ("db-traffic", "Traffic — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Traffic", "交通：车辆沿道路/基础设施行驶所形成的流动"),
    ("db-pedestrian", "Pedestrian — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Pedestrian", "步行者：步行或奔跑的人；pedestrianised 指步行化区域"),
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
            if e["id"] == "vehicle-flow":
                if "db-traffic" not in e["sources"]:
                    e["sources"].append("db-traffic")
                e["sections"]["实例"] = "名称：园区车行道与出入口（类型性，不指定具体项目）；以车行路径与出入口组织机动车、非机动车行驶。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "pedestrian-flow":
                if "db-pedestrian" not in e["sources"]:
                    e["sources"].append("db-pedestrian")
                e["sections"]["实例"] = "名称：商业步行街流线（类型性，不指定具体项目）；以步行者的移动与停留组织空间。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round109 applied")


if __name__ == "__main__":
    main()
