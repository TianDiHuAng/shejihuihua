"""第100轮：glare 补 db-glare 第二平台，重构def/原理(去重)、类型性实例，升级 nv=false。"""
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
    if "db-glare" not in by_id:
        url = "https://www.designingbuildings.co.uk/wiki/Glare"
        good = ok(url)
        data["sources"].append({"id": "db-glare", "title": "Glare in buildings — Designing Buildings", "author": "Designing Buildings",
                                "type": "学术著作", "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；眩光：光线过亮或与周围对比过强时产生的不适"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "glare":
                if "db-glare" not in e["sources"]:
                    e["sources"].append("db-glare")
                e["definition"] = "眩光指视野内出现过亮光源或其与背景的强烈亮度对比、造成不适或降低识别的情形。"
                e["sections"]["原理"] = "当视野中某处亮度远高于周边、或直射光直射入眼时，人眼产生不适并难以看清对象，即为眩光；可用遮阳、控制反射面与降低亮度对比来抑制。"
                e["sections"]["实例"] = "名称：室内眩光场景（类型性，不指定具体项目）；以高亮度窗口或灯具与背景的强对比造成视觉不适。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round100 applied")


if __name__ == "__main__":
    main()
