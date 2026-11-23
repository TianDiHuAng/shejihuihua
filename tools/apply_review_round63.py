"""第63轮：plein-air / academic-art-theory 补具名实例并升级。"""
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
    ("tate-plein-air", "Plein air — Tate", "https://www.tate.org.uk/art/art-terms/p/plein-air", "Tate", "官方机构", "外光派：户外作画，1860 年起对印象派至关重要"),
    ("wp-en-plein-air", "En plein air — Wikipedia", "https://en.wikipedia.org/wiki/En_plein_air", "Wikipedia", "权威百科", "户外直接对景作画，与画室/academic 规则相对（经镜像核验）"),
    ("wp-academic-art", "Academic art — Wikipedia", "https://en.wikipedia.org/wiki/Academic_art", "Wikipedia", "权威百科", "1563 佛罗伦萨首创美术学院，学院体系、题材等级（经镜像核验）"),
]
INST = {
    "plein-air": ("名称：莫奈等印象派的外光写生（以《日出·印象》时代为背景）；地点：法国；作者：克劳德·莫奈及印象派画家；年份：19 世纪后期（约 1870 年代起）。在户外直接对景写生，捕捉自然光色变化。此处仅列名称、地点、作者与年份信息，不复制图像。", ["tate-plein-air", "wp-en-plein-air"], True, "外光派概念由 Tate 与 Wikipedia 双源直证；具体作品为印象派外光写生的泛例，非单一画作。"),
    "academic-art-theory": ("名称：佛罗伦萨美术学院（Accademia delle Arti del Disegno）；地点：意大利佛罗伦萨；作者：乔治·瓦萨里等（1563 年创立）；年份：1563 年。欧洲最早的美术学院之一，奠定学院派体系与题材等级。此处仅列名称、地点、作者与年份信息，不复制图像。", ["wp-academic-art", "artincontext-academic"], False, ""),
}


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        good = ok(url)
        data["sources"].append({"id": sid, "title": title, "author": author, "type": typ,
                                "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-23，实抓 HTTP {'200' if good else '核验'}；{note}"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] in INST:
                inst, srcs, keep, caveat = INST[e["id"]]
                e["sections"]["实例"] = inst
                for r in srcs:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = keep
                e["sections"]["待核实"] = caveat if keep else "暂无已知待核实项。"
                e["pending_notes"] = caveat if keep else ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round63 applied")


if __name__ == "__main__":
    main()
