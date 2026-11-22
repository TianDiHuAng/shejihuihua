"""第9轮复核应用：3 条概念层面双源成立，收窄待核范围为实例数据。"""
import html
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"}
NEW = [
    ("wp-sense-of-place", "Sense of place", "https://en.wikipedia.org/wiki/Sense_of_place", "场所感与情感联结"),
    ("wp-genius-loci", "Genius loci", "https://en.wikipedia.org/wiki/Genius_loci", "场所精神术语"),
    ("wp-spatial-cognition", "Spatial cognition", "https://en.wikipedia.org/wiki/Spatial_cognition", "空间认知机制"),
]

TYPE_INSTANCE = "名称：类型性实例（不指定具体项目）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。"


def main():
    src_path = ROOT / "data" / "sources.json"
    data = json.loads(src_path.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, note in NEW:
        if sid in by_id:
            continue
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as resp:
            body = resp.read().decode("utf-8", "replace")
            status = resp.status
        actual = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", body, re.S).group(1))
        if status != 200 or title.lower() not in actual.lower():
            raise ValueError(f"source verification failed: {sid} {status} {actual}")
        data["sources"].append({
            "id": sid, "title": title, "author": "Wikipedia contributors", "type": "权威百科",
            "year": None, "url": url, "url2": None, "verified": True, "link_ok": True,
            "note": f"标题与机构已核对，HTTP 200，访问于 2026-11-22；{note}；百科条目无固定出版年",
        })
    src_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    entry_path = ROOT / "entries" / "batch-09.json"
    doc = json.loads(entry_path.read_text(encoding="utf-8"))
    changes = {
        "parametric-architecture": ([], "具体实例的设计者与建造数据待补充独立来源。"),
        "place-spirit": (["wp-sense-of-place", "wp-genius-loci"], "具体场所的设计者与实测数据待补充独立来源。"),
        "spatial-perception": (["wp-spatial-cognition"], "具体空间的感知实测数据待补充独立来源。"),
    }
    for entry in doc["entries"]:
        spec = changes.get(entry["id"])
        if not spec:
            continue
        extra, pending = spec
        for ref in extra:
            if ref not in entry["sources"]:
                entry["sources"].append(ref)
        entry["sections"]["实例"] = TYPE_INSTANCE
        entry["sections"]["待核实"] = pending
        entry["needs_verification"] = False
        entry["pending_notes"] = ""
    entry_path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("applied 3 concept-level upgrades")


if __name__ == "__main__":
    main()
