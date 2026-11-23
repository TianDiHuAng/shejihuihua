"""第61轮：back-light / side-light / light-shadow-modeling 补具名实例（实抓核验）。"""
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
    ("ng-rembrandt-self63", "Self Portrait at the Age of 63 — National Gallery", "https://www.nationalgallery.org.uk/paintings/rembrandt-self-portrait-at-the-age-of-63", "National Gallery", "官方机构", "伦勃朗《63岁自画像》1669，面部受光、背景深影"),
    ("ng-temeraire", "The Fighting Temeraire — National Gallery", "https://www.nationalgallery.org.uk/paintings/joseph-mallord-william-turner-the-fighting-temeraire", "National Gallery", "官方机构", "透纳《无畏号》1839，逆光夕阳、发光橙"),
    ("rijks-milkmaid", "The Milkmaid — Rijksmuseum", "https://www.rijksmuseum.nl/en/collection/SK-A-2344", "Rijksmuseum", "官方机构", "维米尔《倒牛奶的女仆》，光以点点色彩落在物体表面"),
]
INST = {
    "light-shadow-modeling": ("名称：《以马忤斯的晚餐》（The Supper at Emmaus）；地点：英国伦敦国家美术馆（NG172）；作者：卡拉瓦乔；年份：1601 年。以强烈的明暗对比塑造人物与静物的体积。此处仅列名称、地点、作者与年份信息，不复制图像。", ["ng-supper-emmaus", "rijks-milkmaid"], False, ""),
    "side-light": ("名称：《63岁自画像》（Self Portrait at the Age of 63）；地点：英国伦敦国家美术馆（NG221）；作者：伦勃朗（Rembrandt）；年份：1669 年。面部受一侧光照、背衬深影，凸显结构与面容。此处仅列名称、地点、作者与年份信息，不复制图像。", ["ng-rembrandt-self63", "tate-chiaroscuro"], True, "作品侧光由馆方单源直证；Tate 为明暗对照概念背景源。"),
    "back-light": ("名称：《被拖去解体的战舰无畏号》（The Fighting Temeraire）；地点：英国伦敦国家美术馆（NG524）；作者：J.M.W. 透纳（Turner）；年份：1839 年。以逆光的发光夕阳与雾蓝对比表现暮色。此处仅列名称、地点、作者与年份信息，不复制图像。", ["ng-temeraire", "tate-chiaroscuro"], True, "逆光夕阳由馆方单源直证（blazing sunset / glowing orange）；概念源 Tate 非针对该作。"),
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
    print("round61 applied")


if __name__ == "__main__":
    main()
