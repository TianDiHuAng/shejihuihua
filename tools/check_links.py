"""站内链接核验：检查生成页面中所有本地 href/src 指向的文件是否存在。"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
ATTR_RE = re.compile(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']', re.I)
SKIP = ("http://", "https://", "mailto:", "data:", "tel:", "//")


def check() -> list[str]:
    broken = []
    for page in sorted(SITE.glob("**/*.html")):
        text = page.read_text(encoding="utf-8")
        for target in ATTR_RE.findall(text):
            if target.startswith(SKIP) or target.startswith("#") or not target.strip():
                continue
            rel = target.split("#", 1)[0].split("?", 1)[0]
            if not rel:
                continue
            resolved = (page.parent / rel).resolve()
            if not resolved.exists():
                broken.append(f"{page.relative_to(ROOT)} -> {target}")
    return broken


def main():
    if not SITE.exists():
        print("FAIL: site/ 未生成")
        return 1
    broken = check()
    if broken:
        print(f"FAIL: {len(broken)} broken links")
        for item in broken[:100]:
            print(" -", item)
        return 1
    print("PASS: 0 broken links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
