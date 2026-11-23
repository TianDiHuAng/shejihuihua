"""第65轮：form-follows-function 补具名实例并升级。"""
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
    ("wp-form-follows-function", "Form follows function — Wikipedia", "https://en.wikipedia.org/wiki/Form_follows_function", "Wikipedia", "权威百科", "沙利文 1896 提出“形式追随功能”；Wainwright 大楼 1891 为其箴言代表（经镜像核验）"),
    ("designingbuildings-form-function", "Form follows function — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Form_follows_function", "Designing Buildings", "学术著作", "形式追随功能源自沙利文，早期钢构高层建筑"),
]
INST = {
    "form-follows-function": ("名称：温赖特大楼（Wainwright Building）；地点：美国圣路易斯；设计者：路易斯·沙利文（Louis Sullivan）；年份：1891 年。被视为沙利文“形式追随功能”箴言的代表性建筑。此处仅列名称、地点、设计者与年份信息，不复制图像。", ["wp-form-follows-function", "designingbuildings-form-function"], False, ""),
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
    print("round65 applied")


if __name__ == "__main__":
    main()
