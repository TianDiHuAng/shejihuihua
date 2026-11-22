"""并发实抓核验候选来源（12s 超时，3 线程，最多约 60s）。"""
import html
import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"}
CAND = {
    "wp-placemaking": ("Placemaking", "https://en.wikipedia.org/wiki/Placemaking", "场所营造概念"),
    "wp-urban-design": ("Urban design", "https://en.wikipedia.org/wiki/Urban_design", "城市设计与公共空间"),
    "wp-space-syntax": ("Space syntax", "https://en.wikipedia.org/wiki/Space_syntax", "空间句法理论"),
    "wp-urban-morphology": ("Urban morphology", "https://en.wikipedia.org/wiki/Urban_morphology", "城市形态学"),
    "wp-pattern-language": ("Pattern language", "https://en.wikipedia.org/wiki/Pattern_language", "模式语言理论"),
    "wp-a-pattern-language": ("A Pattern Language", "https://en.wikipedia.org/wiki/A_Pattern_Language", "建筑模式语言著作"),
    "wp-form-follows-function": ("Form follows function", "https://en.wikipedia.org/wiki/Form_follows_function", "形式追随功能命题"),
    "wp-functionalism-architecture": ("Functionalism (architecture)", "https://en.wikipedia.org/wiki/Functionalism_(architecture)", "功能主义建筑"),
    "wp-biophilic-design": ("Biophilic design", "https://en.wikipedia.org/wiki/Biophilic_design", "亲生命性设计"),
    "wp-evidence-based-design": ("Evidence-based design", "https://en.wikipedia.org/wiki/Evidence-based_design", "循证设计"),
    "wp-defensible-space-theory": ("Defensible space theory", "https://en.wikipedia.org/wiki/Defensible_space_theory", "防御性空间理论"),
    "wp-cpted": ("Crime prevention through environmental design", "https://en.wikipedia.org/wiki/Crime_prevention_through_environmental_design", "环境设计预防犯罪"),
}


def probe(item):
    sid, (title, url, _) = item
    try:
        resp = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=12)
        body = resp.read().decode("utf-8", "replace")
        actual = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", body, re.S).group(1))
        ok = resp.status == 200 and title.lower() in actual.lower()
        return sid, ok, f"{resp.status} {actual[:50]}"
    except Exception as exc:
        return sid, False, type(exc).__name__


def main():
    results = {}
    with ThreadPoolExecutor(max_workers=3) as pool:
        for sid, ok, info in pool.map(probe, CAND.items()):
            results[sid] = ok
            print(("OK " if ok else "NO "), sid, info, flush=True)
    verified = [k for k, v in results.items() if v]
    failed = [k for k, v in results.items() if not v]
    (ROOT / "research" / "verify-round11.txt").write_text(
        f"verified={verified}\nfailed={failed}\n", encoding="utf-8")
    print(f"VERIFIED {len(verified)}/{len(CAND)} FAILED={failed}")


if __name__ == "__main__":
    main()
