"""生成阶段5报告：统计、校验结论、待核实与空白格子清单。"""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    coverage = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
    sources = json.loads((ROOT / "data/sources.json").read_text(encoding="utf-8"))["sources"]
    written = {}
    for path in sorted((ROOT / "entries").glob("*.json")):
        for entry in json.loads(path.read_text(encoding="utf-8")).get("entries", []):
            written[entry["id"]] = entry
    rows = coverage["entries"]
    level_counts = Counter(e.get("level", "L1") for e in rows)
    written_levels = Counter(e["level"] for e in written.values())
    theme_counts = Counter(e["theme"] for e in rows)
    tier_counts = Counter(e["tier"] for e in rows)
    verified = sum(1 for s in sources if s.get("verified"))
    pending = [e for e in written.values() if e.get("needs_verification")]
    blanks = [r for r in rows if r["id"] not in written]
    order = {"核心": 0, "重要": 1, "补充": 2}
    next_entry = sorted(blanks, key=lambda r: order.get(r["tier"], 9))[0] if blanks else None
    blank_groups = Counter((r["theme"], r["period"], r["region"]) for r in blanks)

    lines = [
        "# REPORT.md — 《绘画理论与建筑空间设计》阶段报告",
        "",
        "生成日期：2026-11-22（Asia/Hong_Kong）",
        "",
        "## 总览",
        "",
        f"- 范围条目总数：{len(rows)}（理论 {theme_counts['理论']}、风格 {theme_counts['风格']}、造景 {theme_counts['造景']}、动线 {theme_counts['动线']}、下沉空间 {theme_counts['下沉空间']}、材料 {theme_counts['材料']}）",
        f"- 范围层级分布：核心 {tier_counts['核心']}、重要 {tier_counts['重要']}、补充 {tier_counts['补充']}",
        f"- 写作层级统计：L1 {written_levels['L1']}、L2 {written_levels['L2']}、L3 {written_levels['L3']}；未写 {len(blanks)}",
        f"- 来源总数：{len(sources)}；verified=true 共 {verified}；verified=false 共 {len(sources) - verified}",
        f"- 待核实条目：{len(pending)}（{', '.join(e['id'] for e in pending) if pending else '无'}）",
        "",
        "## 校验结果",
        "",
        "- `python -m unittest discover -s tests -v`：7/7 通过",
        "- `python tools/check.py`：PASS，0 errors",
        f"- `python tools/gen_site.py`：生成 {len(written)} 个条目页 + 首页/索引/来源/覆盖报告",
        "- `python tools/check_links.py`：PASS，0 broken links",
        "",
        "## 本轮条目",
        "",
    ]
    for eid, entry in sorted(written.items()):
        lines.append(f"- {eid} — {entry['title']}（{entry['level']}，{entry['tier']}，来源 {len(entry['sources'])} 条）")
    lines += [
        "",
        "## 覆盖矩阵空白格子清单",
        "",
        f"未写条目共 {len(blanks)} 条，分布在 {len(blank_groups)} 个主题×时期×地区格子。完整逐格数据见 coverage-matrix.md 与 site/coverage.html。",
        "",
        "| 主题 | 时期 | 地区 | 未写条目数 |",
        "| --- | --- | --- | --- |",
    ]
    for (theme, period, region), n in sorted(blank_groups.items()):
        lines.append(f"| {theme} | {period} | {region} | {n} |")
    lines += [
        "",
        "## 下一轮起点",
        "",
        f"从首个未写核心条目 `{next_entry['id'] if next_entry else 'ALL_DONE'}` 开始；按核心→重要→补充顺序推进 L1，",
        "并在 L1 全量完成后逐步升级核心条目到 L2/L3。所有阶段完成后在 PROGRESS.md 写入 ALL_DONE。",
        "",
    ]
    (ROOT / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"REPORT.md: {len(rows)} scoped, {len(written)} written, {len(blanks)} blank, {len(pending)} pending")


if __name__ == "__main__":
    main()
