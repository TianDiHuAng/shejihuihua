"""第4轮：补入解构主义与 2026 建筑动态的直接来源。"""
import json
import urllib.request
import re
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"}
NEW = [
    ("wp-deconstructivism", "Deconstructivism", "https://en.wikipedia.org/wiki/Deconstructivism", "解构主义建筑直接条目，支撑风格定义与实例"),
    ("wp-2026-in-architecture", "2026 in architecture", "https://en.wikipedia.org/wiki/2026_in_architecture", "2026 年建筑动态，支撑 Guggenheim Abu Dhabi 近期实例"),
]


def verify(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as resp:
        body = resp.read().decode("utf-8", "replace")
        title = re.search(r"<title[^>]*>(.*?)</title>", body, re.S)
        return resp.status, html.unescape(title.group(1)) if title else ""


def main():
    path = ROOT / "data" / "sources.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {s["id"]: s for s in data["sources"]}
    for sid, title, url, note in NEW:
        status, actual = verify(url)
        if title.lower() not in actual.lower():
            raise ValueError(f"title mismatch: {sid} {actual}")
        if sid not in by_id:
            data["sources"].append({
                "id": sid, "title": title, "author": "Wikipedia contributors", "type": "权威百科",
                "year": None, "url": url, "url2": None, "verified": True, "link_ok": True,
                "note": f"标题与机构已核对，HTTP {status}，访问于 2026-11-22；{note}；百科条目无固定出版年",
            })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added:", [s[0] for s in NEW])


if __name__ == "__main__":
    main()
