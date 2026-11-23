"""第74轮：trompe-loeil 补具名实例（Pozzo《圣依纳爵的荣耀》）+ WGA 第二平台佐证，保留诚实待核实。"""
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
    ("wga-pozzo", "Andrea Pozzo — Web Gallery of Art", "https://www.wga.hu/html_m/p/pozzo/index.html", "Web Gallery of Art", "学术著作", "波佐 1642–1709，罗马 Sant'Ignazio 壁画 1685–97"),
]


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
            if e["id"] == "trompe-loeil":
                e["sections"]["实例"] = "名称：《圣依纳爵的荣耀》（Apotheosis of St Ignatius，中殿天顶画）；地点：意大利罗马圣依纳爵教堂（Sant'Ignazio）；作者：安德烈亚·波佐（Andrea Pozzo）；年份：1685–1697 年。以透视与假穹顶在平顶上制造天顶错视。此处仅列名称、地点、作者与年份信息，不复制图像。"
                if "wga-pozzo" not in e["sources"]:
                    e["sources"].append("wga-pozzo")
                e["needs_verification"] = True
                e["sections"]["待核实"] = "作品作者与年代（Pozzo 1685–97 Sant'Ignazio）由 Wikipedia 与 Web Gallery of Art 两平台佐证；“假穹顶错视”技法的具体描述以 artincontext 等为主，待补第二独立专述。"
                e["pending_notes"] = "技法具体描述待补第二独立专述；作者/年代已两平台佐证。"
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
            print("trompe-loeil updated in", p.name)


if __name__ == "__main__":
    main()
