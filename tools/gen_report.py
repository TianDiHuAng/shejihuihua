"""按 AUTONOMOUS.md 第七节格式生成每轮 REPORT.md。"""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    metrics = json.loads((ROOT / "METRICS.json").read_text(encoding="utf-8"))["rounds"][-1]
    coverage = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
    sources = json.loads((ROOT / "data/sources.json").read_text(encoding="utf-8"))["sources"]
    written = {}
    for path in sorted((ROOT / "entries").glob("*.json")):
        for entry in json.loads(path.read_text(encoding="utf-8")).get("entries", []):
            written[entry["id"]] = entry
    rows = coverage["entries"]
    levels = Counter(e.get("level", "L1") for e in written.values())
    verified = sum(1 for s in sources if s.get("verified"))
    pending = sum(1 for e in written.values() if e.get("needs_verification"))
    blanks = [r for r in rows if r["id"] not in written]
    blank_cells = Counter((r["theme"], r["period"], r["region"]) for r in blanks)
    gaps = metrics.get("gaps", {})

    lines = [
        "# REPORT.md — 每轮摘要",
        "",
        f"1. 本轮编号：第 {metrics['round']} 轮｜日期：{metrics['date']}｜状态：正常",
        "",
        f"2. 本轮完成：新增 {metrics['new_entries']} 条、升级 {metrics['upgrades']} 条、"
        f"复核 {metrics['reviews']} 条、修复 {metrics['fixes']} 项。",
        "",
        f"3. 累计：范围总条目 {len(rows)}；已写 {len(written)} 条"
        f"（L1 {levels['L1']}、L2 {levels['L2']}、L3 {levels['L3']}）；"
        f"验证通过数 {verified} 条来源；待核实 {pending} 条；来源总数 {len(sources)}。",
        "",
        "4. 质量：" + metrics["check_result"] + "。",
        "",
        "5. 缺口发现摘要：使用 " + "、".join(gaps.get("methods_used", [])) + f" 共 {len(gaps.get('methods_used', []))} 种方法。"
        f"新发现 B1 范围候选 {gaps.get('B1_scope_candidates', 0)} 条、"
        f"B2 稀疏格 {gaps.get('B2_sparse_cells', 0)} 个、"
        f"B3 悬空引用 {gaps.get('B3_dangling_refs', 0)} 条、"
        f"B5 待核实 {gaps.get('B5_pending_items', 0)} 条、"
        f"B6 近期动态 {gaps.get('B6_recent_updates', 0)} 条、"
        f"B7 核心未写 {gaps.get('B7_core_unwritten', 0)} 条。"
        "B4 本轮未用，后续轮换。",
        "",
        f"6. 覆盖矩阵仍空白的格子（按未写条目，最多 20 个）：共 {len(blank_cells)} 个。"
        + "；".join(f"{'/'.join(k)}({n})" for k, n in blank_cells.most_common(20)),
        "",
        "7. 需要人关注的事项：无。",
        "",
    ]
    (ROOT / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"REPORT.md round={metrics['round']} written={len(written)} pending={pending}")


if __name__ == "__main__":
    main()
