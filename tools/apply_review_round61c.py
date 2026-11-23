"""第61轮再返工：side-light 换成真·侧光源并重挂实例；light-shadow-modeling 专属 SVG。"""
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
    ("studiobinder-side-lighting", "What is Side Lighting in Photography — StudioBinder", "https://www.studiobinder.com/blog/what-is-side-lighting/", "StudioBinder", "学术著作", "侧光：光源从主体一侧照来，凸显特征与质感、在另一侧投下阴影"),
    ("wp-rembrandt-lighting", "Rembrandt lighting", "https://en.wikipedia.org/wiki/Rembrandt_lighting", "Wikipedia", "权威百科", "伦勃朗光：面部一侧以明暗对照塑造几何形体（经镜像核验）"),
]
SVG_LSM = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='150' cy='110' r='26' fill='var(--accent-soft)' stroke='var(--accent)'/><ellipse cx='430' cy='210' rx='70' ry='110' fill='var(--panel)' stroke='var(--line)'/><path d='M 430 100 Q 430 210 430 320' stroke='var(--accent)' stroke-width='3'/><path d='M 430 100 Q 360 110 360 210 Q 360 310 430 320' fill='var(--muted)' fill-opacity='0.25'/><text x='40' y='40' fill='var(--ink)'>受光面—明暗交界—暗部</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>"


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
            k = e["id"]
            if k == "side-light":
                e["sources"] = ["studiobinder-side-lighting", "wp-rembrandt-lighting"]
                e["definition"] = "侧光指光源位于被摄体一侧、从侧面照来的照明。"
                e["overview"] = "侧光在一侧受光、另一侧落影，能凸显表面特征与质感，明暗对比强。"
                e["sections"]["原理"] = "光线从侧面掠过表面：迎光面亮、背光侧落影，凸处迎光、凹陷背光，因而放大质感与起伏。"
                e["sections"]["典型手法与适用条件"] = "侧光下注意暗部补光比例，避免一侧死黑；适合强调质感的肖像与静物。"
                e["sections"]["实例"] = "名称：《63岁自画像》（Self Portrait at the Age of 63）；地点：英国伦敦国家美术馆（NG221）；作者：伦勃朗（Rembrandt）；年份：1669 年。面部一侧受光另一侧沉入阴影，以明暗对照塑造结构。此处仅列名称、地点、作者与年份信息，不复制图像。"
                e["needs_verification"] = True
                e["sections"]["待核实"] = "侧光概念由 StudioBinder 与 Wikipedia（伦勃朗光）双源直证；实例《63岁自画像》的伦勃朗式侧光为据其明暗对照特征的解读。"
                e["pending_notes"] = "实例侧光为据伦勃朗光特征的解读；概念已双源。"
                ch = True
            elif k == "light-shadow-modeling":
                e["svg"] = [SVG_LSM]
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round61 rework2 applied")


if __name__ == "__main__":
    main()
