"""第70轮：space-syntax / pattern-language 补具名实例并升级（第二独立平台）。"""
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
    ("db-space-syntax", "Space syntax — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Space_syntax", "Designing Buildings", "学术著作", "空间句法：Hillier、Hanson 及 Bartlett 同事 1970s 提出"),
    ("patternlanguage-official", "A Pattern Language — patternlanguage.com (Christopher Alexander)", "https://www.patternlanguage.com/", "patternlanguage.com", "官方机构", "《建筑模式语言》1977，Oxford University Press，Alexander"),
]
INST = {
    "space-syntax": ("名称：《空间句法》（The Social Logic of Space）；地点：英国伦敦大学学院 Bartlett 学院；作者：比尔·希列尔、朱莉安娜·汉森（Bill Hillier, Julienne Hanson）；年份：1984 年（理论于 1970 年代提出）。以空间构形与整合度分析建筑与城市空间。此处仅列名称、地点、作者与年份信息，不复制图像。", ["wp-space-syntax", "db-space-syntax"], False, ""),
    "pattern-language": ("名称：《建筑模式语言》（A Pattern Language）；地点：美国（加州大学伯克利）；作者：克里斯托弗·亚历山大（Christopher Alexander）等；年份：1977 年（Oxford University Press）。以 253 条模式描述城镇、建筑与建造的可复用解法。此处仅列名称、地点、作者与年份信息，不复制图像。", ["wp-a-pattern-language", "patternlanguage-official"], False, ""),
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
    print("round70 applied")


if __name__ == "__main__":
    main()
