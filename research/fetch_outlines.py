"""抓取权威百科/课程大纲页面，提取标题与章节结构，保存为研究笔记。"""
import urllib.request
import urllib.error
import re
import html
from pathlib import Path

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
OUT = Path(__file__).resolve().parent.parent / "research" / "outline_raw.md"

URLS = [
    ("S1", "https://en.wikipedia.org/wiki/Outline_of_architecture"),
    ("S2", "https://en.wikipedia.org/wiki/Architectural_style"),
    ("S3", "https://en.wikipedia.org/wiki/Chinese_garden"),
    ("S4", "https://en.wikipedia.org/wiki/Chinese_painting"),
    ("S5", "https://en.wikipedia.org/wiki/Perspective_(graphical)"),
    ("S6", "https://en.wikipedia.org/wiki/Composition_(visual_arts)"),
    ("S7", "https://en.wikipedia.org/wiki/Color_theory"),
    ("S8", "https://en.wikipedia.org/wiki/Circulation_(architecture)"),
    ("S9", "https://en.wikipedia.org/wiki/Architectural_lighting"),
    ("S10", "https://en.wikipedia.org/wiki/Ventilation_(architecture)"),
    ("S11", "https://en.wikipedia.org/wiki/Chinese_architecture"),
    ("S12", "https://en.wikipedia.org/wiki/Garden_design"),
]

HEAD_RE = re.compile(r"<h[23][^>]*>(.*?)</h[23]>", re.I | re.S)
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")


def clean(text):
    return html.unescape(TAG_RE.sub(" ", text)).replace("\u00a0", " ").strip()


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as resp:
        return resp.status, resp.read().decode("utf-8", "replace")


def main():
    lines = [
        "# 权威大纲抓取记录",
        "",
        "抓取日期：2026-11-22（Asia/Hong_Kong）",
        "抓取方式：Python urllib + 浏览器 User-Agent；web_search/web_fetch 工具在本环境不可用。",
        "",
    ]
    for sid, url in URLS:
        try:
            status, body = fetch(url)
            title = clean(TITLE_RE.search(body).group(1)) if TITLE_RE.search(body) else "(no title)"
            heads = [clean(h) for h in HEAD_RE.findall(body)]
            heads = [h for h in heads if h and len(h) < 90]
            seen, unique = set(), []
            for h in heads:
                key = h.lower()
                if key not in seen:
                    seen.add(key)
                    unique.append(h)
            lines += [
                f"## {sid} {title}",
                "",
                f"- URL: {url}",
                f"- HTTP: {status}",
                "- 章节标题（去重，前40）：" + "；".join(unique[:40]),
                "",
            ]
            print(f"OK {sid} {status} {url}")
        except Exception as exc:
            lines += [f"## {sid} {url}", "", f"- 抓取失败: {exc}", ""]
            print(f"FAIL {sid} {url}: {exc}")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("saved", OUT)


if __name__ == "__main__":
    main()
