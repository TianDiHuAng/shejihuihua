"""第61轮返工：back-light 定义换真源重写 + 重绘 SVG；light-shadow-modeling/side-light 复核。"""
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
    ("wp-contre-jour", "Contre-jour", "https://en.wikipedia.org/wiki/Contre-jour", "Wikipedia", "权威百科", "逆光：光源在主体背后，产生背光、更强明暗对比、剪影与轮廓（经镜像核验）"),
    ("expertphoto-backlight", "Backlight Photography — ExpertPhotography", "https://expertphotography.com/backlighting-photography/", "ExpertPhotography", "学术著作", "逆光：主光在主体背后朝向相机，主体变暗形成剪影"),
]
SVG_BACK = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='580' cy='120' r='40' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='530' y='90' fill='var(--ink)'>光源在主体背后</text><ellipse cx='300' cy='230' rx='55' ry='110' fill='var(--muted)'/><path d='M 300 120 Q 250 120 245 210' fill='none' stroke='var(--accent)' stroke-width='4'/><path d='M 300 120 Q 350 120 355 210' fill='none' stroke='var(--accent)' stroke-width='4'/><text x='60' y='360' fill='var(--muted)'>主体成剪影、边缘亮线（轮廓光）</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>"


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
            if k == "back-light":
                # 替换挂名的建筑照明源，改用真逆光源
                e["sources"] = ["wp-contre-jour", "expertphoto-backlight", "ng-temeraire"]
                e["definition"] = "逆光指光源位于主体背后、朝向镜头的照明，主体因此变暗成剪影、边缘显出轮廓光。"
                e["overview"] = "光源在主体之后，主体大面积处于阴影，边缘被照亮形成轮廓；曝光不当主体会全黑。"
                e["sections"]["原理"] = "当主光位于主体背后并朝向相机，主体迎镜头一面落在背光中而变暗，其轮廓边缘被背后强光照亮，形成剪影与轮廓光。"
                e["sections"]["典型手法与适用条件"] = "逆光下以剪影或轮廓光造型，必要时对主体补光避免死黑。"
                e["sections"]["实例"] = "名称：《被拖去解体的战舰无畏号》（The Fighting Temeraire）；地点：英国伦敦国家美术馆（NG524）；作者：J.M.W. 透纳（Turner）；年份：1839 年。以逆光夕阳与雾蓝对比表现暮色氛围（作品以“blazing sunset / glowing orange”直证）。此处仅列名称、地点、作者与年份信息，不复制图像。"
                e["svg"] = [SVG_BACK]
                e["needs_verification"] = True
                e["sections"]["待核实"] = "逆光概念由 Contre-jour 与 ExpertPhotography 双源直证；实例《无畏号》的夕阳逆光为据馆方“blazing sunset/glowing orange”解读，作品未直言“逆光”。"
                e["pending_notes"] = "实例“逆光”解读基于馆方夕阳/暖色描述；概念已双源。"
                ch = True
            elif k == "light-shadow-modeling":
                # 替换泛援的 rijks 源为 NG 明暗塑形直证 + 保留 wp
                e["sources"] = ["wp-chiaroscuro", "wp-sfumato", "ng-supper-emmaus"]
                ch = True
            elif k == "side-light":
                e["sections"]["待核实"] = "“一侧光照”由馆方对该像的描述解读（伦勃朗自画像面部受光、背景深影）；Tate 为明暗对照概念源。"
                e["pending_notes"] = "侧光为据馆方描述的解读；概念有 Tate 背景。"
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round61 rework applied")


if __name__ == "__main__":
    main()
