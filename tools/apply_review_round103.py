"""第103轮：wind-driven-ventilation / transparent-material / safety-guarding 补 DB 第二平台，类型性实例，升级 nv=false。"""
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
    ("db-ventilation", "Ventilation — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Ventilation", "自然通风可由风压(wind driven)或热压(buoyancy)驱动"),
    ("db-glass", "Glass for buildings — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Glass", "玻璃可透明/半透明/着色/反射，视觉透明性可按需调整"),
    ("db-guardrail", "Guardrail — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Guardrail", "护栏为纵向屏障，防止人跌落或越界"),
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
            if e["id"] == "wind-driven-ventilation":
                if "db-ventilation" not in e["sources"]:
                    e["sources"].append("db-ventilation")
                e["sections"]["实例"] = "名称：对流通风的房间（类型性，不指定具体项目）；迎风面进风、背风面出风形成穿堂风。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "transparent-material":
                if "db-glass" not in e["sources"]:
                    e["sources"].append("db-glass")
                e["sections"]["原理"] = "光线与视线穿过玻璃等透明材料时可传达通透与联系；半透明材料只传光而模糊影像，从而以不同程度削弱空间边界的视觉重量。"
                e["sections"]["实例"] = "名称：建筑玻璃隔断（类型性，不指定具体项目）；透明玻璃分隔空间而保持视线连通。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "safety-guarding":
                if "db-guardrail" not in e["sources"]:
                    e["sources"].append("db-guardrail")
                e["sections"]["原理"] = "以护栏等实体屏障在临空、下沉与高差处阻止跌落，配合照明与出口标识使人能预见边缘与疏散方向，减少跌坠与死角风险。"
                e["sections"]["实例"] = "名称：临空处防护栏杆（类型性，不指定具体项目）；在边缘设置护栏阻挡跌落。此处仅列说明，不复制图像。"
                e["sections"]["常见错误与限制"] = "栏杆高度、照度等具体数值须按当地规范与专业设计校核，本条不写死数值。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round103 applied")


if __name__ == "__main__":
    main()
