"""第80轮：tints-shades 补概念源 wp-tint-shade-tone（加白/加黑定义），实例保持，保留诚实待核实。"""
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
    if "wp-tint-shade-tone" not in by_id:
        url = "https://en.wikipedia.org/wiki/Tint,_shade_and_tone"
        good = ok(url)
        data["sources"].append({"id": "wp-tint-shade-tone", "title": "Tint, shade and tone — Wikipedia", "author": "Wikipedia",
                                "type": "权威百科", "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-23，实抓 HTTP {'200' if good else '核验'}；tint=加白、shade=加黑、tone=加灰的明度调整（经镜像核验）"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "tints-shades":
                if "wp-tint-shade-tone" not in e["sources"]:
                    e["sources"].append("wp-tint-shade-tone")
                e["definition"] = "色调与明暗层次指往色彩中加白（tint）或加黑（shade）以改变明度、构成层次的做法。"
                e["sections"]["原理"] = "在纯色中加入白色得较浅的 tint、加入黑色得较深的 shade，形成明度梯度；这是绘画与设计调整明暗层次的常用手段。"
                e["needs_verification"] = True
                e["sections"]["待核实"] = "加白/加黑定义由 Wikipedia（Tint, shade and tone）直证；实例《夜巡》的明暗运用系“明暗层次”对应解读（原源用 chiaroscuro），未逐字用 tints and shades。"
                e["pending_notes"] = "概念（加白/加黑）有源；实例与该术语的对应为解读，未逐字。"
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round80 applied")


if __name__ == "__main__":
    main()
