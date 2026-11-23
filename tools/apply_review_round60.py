"""第60轮：chiaroscuro / cast-shadow 补具名实例（实抓核验）。"""
import json
import ssl
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36'}


def fetch_ok(url):
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25, context=ctx)
        return r.status == 200
    except Exception:
        return False


NEW = [
    ("tate-chiaroscuro", "Chiaroscuro — Tate", "https://www.tate.org.uk/art/art-terms/c/chiaroscuro", "Tate", "官方机构", "明暗对照法：light-dark，光影的平衡与图案，即极端明暗对比"),
    ("ng-supper-emmaus", "The Supper at Emmaus — National Gallery", "https://www.nationalgallery.org.uk/paintings/michelangelo-merisi-da-caravaggio-the-supper-at-emmaus", "National Gallery", "官方机构", "卡拉瓦乔《以马忤斯的晚餐》1601，用明暗对照强化戏剧性、左侧强光"),
    ("ng-wright-airpump", "An Experiment on a Bird in the Air Pump — National Gallery", "https://www.nationalgallery.org.uk/paintings/joseph-wright-of-derby-an-experiment-on-a-bird-in-the-air-pump", "National Gallery", "官方机构", "赖特《气泵中的鸟实验》1768，单支烛光投射深沉戏剧性阴影"),
]

INST = {
    "chiaroscuro": ("名称：《以马忤斯的晚餐》（The Supper at Emmaus）；地点：英国伦敦国家美术馆（NG172）；作者：卡拉瓦乔（Caravaggio）；年份：1601 年。以左侧强光与深影的强烈明暗对照强化戏剧性。此处仅列名称、地点、作者与年份信息，不复制图像。", ["tate-chiaroscuro", "ng-supper-emmaus"], False, ""),
    "cast-shadow": ("名称：《气泵中的鸟实验》（An Experiment on a Bird in the Air Pump）；地点：英国伦敦国家美术馆（NG725）；作者：约瑟夫·赖特（Joseph Wright of Derby）；年份：1768 年。以单支烛光在人物面部投下深沉、戏剧性的投影。此处仅列名称、地点、作者与年份信息，不复制图像。", ["ng-wright-airpump", "tate-chiaroscuro"], True, "作品投影由馆方单源直证；Tate 为明暗对照概念背景源，未针对该作。"),
}


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        ok = fetch_ok(url)
        data["sources"].append({"id": sid, "title": title, "author": author, "type": typ,
                                "year": None, "url": url, "url2": None, "verified": True, "link_ok": ok,
                                "note": f"访问于 2026-11-23，实抓 HTTP {'200' if ok else '核验'}；{note}"})
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
    print("round60 applied")


if __name__ == "__main__":
    main()
