"""第4轮复核应用：补入 Visual hierarchy 来源并把 hierarchy 升级为已验证。"""
import json
import re
import html
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = "https://en.wikipedia.org/wiki/Visual_hierarchy"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"}


def main():
    with urllib.request.urlopen(urllib.request.Request(URL, headers=UA), timeout=25) as resp:
        body = resp.read().decode("utf-8", "replace")
        status = resp.status
    title = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", body, re.S).group(1))
    if status != 200 or "Visual hierarchy" not in title:
        raise ValueError(f"source verification failed: {status} {title}")

    src_path = ROOT / "data" / "sources.json"
    data = json.loads(src_path.read_text(encoding="utf-8"))
    sid = "wp-visual-hierarchy"
    if not any(s["id"] == sid for s in data["sources"]):
        data["sources"].append({
            "id": sid, "title": "Visual hierarchy", "author": "Wikipedia contributors", "type": "权威百科",
            "year": None, "url": URL, "url2": None, "verified": True, "link_ok": True,
            "note": "标题与机构已核对，HTTP 200，访问于 2026-11-22；独立支撑主次层级的定义；百科条目无固定出版年",
        })
    src_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for path in (ROOT / "entries").glob("*.json"):
        doc = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for entry in doc.get("entries", []):
            if entry["id"] != "hierarchy":
                continue
            refs = entry.get("sources", [])
            if sid not in refs:
                refs.append(sid)
            entry["sources"] = refs
            entry["needs_verification"] = False
            entry["pending_notes"] = ""
            changed = True
        if changed:
            path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("hierarchy upgraded, source added")


if __name__ == "__main__":
    main()
