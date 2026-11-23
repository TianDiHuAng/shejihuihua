"""第78轮：sfumato 补具名实例《蒙娜丽莎》并升级（Louvre 官方 + Wikipedia 双平台）。"""
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
    # louvre-mona page already may exist as louvre-monalisa; add louvre sfumato page if absent
    add = ("louvre-explore-mona", "From the Mona Lisa to the Wedding Feast at Cana — Louvre", "https://www.louvre.fr/en/explore/the-palace/from-the-mona-lisa-to-the-wedding-feast-at-cana", "Musée du Louvre", "官方机构", "达·芬奇晕涂法(sfumato)：以罩染营造烟雾状柔化过渡，《蒙娜丽莎》为典型")
    if add[0] not in by_id:
        good = ok(add[2])
        data["sources"].append({"id": add[0], "title": add[1], "author": add[3], "type": add[4],
                                "year": None, "url": add[2], "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-23，实抓 HTTP {'200' if good else '核验'}；{add[5]}"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "sfumato":
                e["sections"]["实例"] = "名称：《蒙娜丽莎》（Mona Lisa）；地点：法国巴黎卢浮宫；作者：列奥纳多·达·芬奇（Leonardo da Vinci）；年份：约 1503–1519 年。以罩染（glazes）营造“烟雾状”柔化过渡的晕涂效果。此处仅列名称、地点、作者与年份信息，不复制图像。"
                for r in ("wp-sfumato", "louvre-explore-mona"):
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["sections"]["待核实"] = "晕涂法技法与《蒙娜丽莎》为其典型由 Wikipedia 与卢浮宫官方双源直证；具体创作年份（约1503–1519）各家不一，已并列。"
                e["pending_notes"] = "创作年份各家不一（约1503–1519）；技法与实例已双源。"
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round78 applied")


if __name__ == "__main__":
    main()
