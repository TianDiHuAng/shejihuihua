"""第11轮：写入经实抓（镜像+web_search 佐证）核验的 12 份来源。"""
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = {
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
NOTE = "访问于 2026-11-22，经 Wikipedia 镜像 owiki.org 实抓核对标题与首句定义 + web_search 佐证条目存在；canonical en.wikipedia.org 直连因网络限制待复"


def main():
    verified = set()
    for line in (ROOT / "research" / "verify-round11.txt").read_text(encoding="utf-8").splitlines():
        if line.startswith("verified="):
            verified = set(ast.literal_eval(line.split("=", 1)[1]))
    path = ROOT / "data" / "sources.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    added = []
    for sid in verified:
        if sid in by_id:
            continue
        title, url, desc = META[sid]
        data["sources"].append({
            "id": sid, "title": title, "author": "Wikipedia contributors", "type": "权威百科",
            "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
            "note": f"{NOTE}；{desc}；百科条目无固定出版年",
        })
        added.append(sid)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"added={len(added)} total={len(data['sources'])}")


if __name__ == "__main__":
    main()
