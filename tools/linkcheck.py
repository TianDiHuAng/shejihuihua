"""来源链接三态核验：true=可达，blocked=反爬拒绝，false=死链，null=无链接。"""
from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
BLOCKED = (401, 403, 429, 503)


def classify(status):
    if status is None:
        return None
    if 200 <= status < 400:
        return True
    if status in BLOCKED:
        return "blocked"
    return False


def probe(url: str):
    if not url:
        return None
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return classify(response.status)
    except urllib.error.HTTPError as exc:
        return classify(exc.code)
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser(description="来源链接三态核验")
    parser.add_argument("--dry-run", action="store_true", help="只检查不写回 sources.json")
    args = parser.parse_args()
    path = ROOT / "data" / "sources.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    sources = data["sources"]

    def update(src):
        src["link_ok"] = probe(src.get("url"))
        if src.get("url2"):
            src["link_ok2"] = probe(src["url2"])

    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(update, sources))
    if not args.dry_run:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    counts = {"true": 0, "blocked": 0, "false": 0, "null": 0}
    for src in sources:
        key = src.get("link_ok")
        counts["null" if key is None else ("true" if key is True else ("false" if key is False else key))] += 1
    print(f"link_ok: {counts}" + (" (dry-run)" if args.dry_run else " (written to sources.json)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
