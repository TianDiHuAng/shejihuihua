"""第9轮抽检返工：参数化建筑补直接来源；两条定向保守化。"""
import html
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"}
NEW = [
    ("wp-parametric-design", "Parametric design", "https://en.wikipedia.org/wiki/Parametric_design", "参数化设计概念与算法驱动"),
    ("wp-parametric-architecture", "Parametric architecture", "https://en.wikipedia.org/wiki/Parametric_architecture", "参数化建筑直接条目"),
]


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
    for entry in doc["entries"]:
        if entry["id"] == "parametric-architecture":
            entry["sources"] = ["wp-parametric-design", "wp-parametric-architecture"]
            entry["definition"] = "参数化建筑是以可变参数与算法关系生成建筑形态与构造的设计方法。"
            entry["overview"] = "参数改变时，相关几何与构造随之更新，适合处理连续变体与复杂形态。"
            sec = entry["sections"]
            sec["原理"] = "把设计意图写成参数之间的关系，算法据此生成形态；参数变化可在同一规则内得到不同结果。"
            sec["典型手法与适用条件"] = "以脚本或可视化编程驱动表皮、结构与布局；适用于需要批量变体与复杂几何的设计任务。"
            sec["待核实"] = "具体实例的设计者、年份与建造数据待核实。"
            entry["needs_verification"] = True
            entry["pending_notes"] = "参数化建筑实例的设计者、年份与建造数据待补充独立来源。"
        elif entry["id"] == "functional-zoning":
            entry["definition"] = "把使用需求相近的空间集中组织的功能布局方法（术语定义待补直接来源）。"
            entry["pending_notes"] = "Architecture 与 Interior design 未直接给出“功能分区”术语定义；核心概念与实例数据均待补独立来源。"
        elif entry["id"] == "place-spirit":
            entry["pending_notes"] = "现有来源支撑场所依恋，但未直接给出“场所精神/genius loci”及欧洲语境定义；核心术语与实例数据待补独立来源。"
    entry_path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("reworked parametric-architecture and two pending entries")


if __name__ == "__main__":
    main()
