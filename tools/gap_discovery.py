"""第2轮缺口发现：覆盖矩阵稀疏格、悬空引用、待核实清单、核心深度缺口。"""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY = "2026-11-22"


def main():
    coverage = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
    rows = coverage["entries"]
    written = {}
    for path in sorted((ROOT / "entries").glob("*.json")):
        for entry in json.loads(path.read_text(encoding="utf-8")).get("entries", []):
            written[entry["id"]] = entry
    titles = {r["title"]: r["id"] for r in rows}
    ids = {r["id"] for r in rows}

    # B2 覆盖矩阵稀疏格
    cells = Counter((r["theme"], r["period"], r["region"]) for r in rows)
    empty = sorted(k for k, c in cells.items() if c == 0)
    sparse = sorted((k, c) for k, c in cells.items() if 0 < c <= 1)

    # B3 悬空引用
    dangling = []
    for eid, entry in written.items():
        for ref in entry.get("related", []):
            if ref not in ids:
                dangling.append((eid, "related", ref))
        text = " ".join(str(v) for v in entry.get("sections", {}).values())
        for mention in re.findall(r"另见[：:]?\s*([\u4e00-\u9fffA-Za-z0-9_-]{2,20})", text):
            if mention not in titles and mention not in ids:
                dangling.append((eid, "另见", mention))

    # B5 待核实清单
    pending = [(eid, e.get("pending_notes", "")) for eid, e in written.items() if e.get("needs_verification")]

    # B7 核心条目深度缺口
    core_l1 = [r["id"] for r in rows if r["tier"] == "核心" and r.get("level") == "L1" and r["id"] not in written]
    core_written_l1 = [r["id"] for r in rows if r["tier"] == "核心" and written.get(r["id"], {}).get("level") == "L1"]
    important_unwritten = [r["id"] for r in rows if r["tier"] == "重要" and r["id"] not in written]

    lines = [
        "# 缺口发现 — 第 2 轮",
        "",
        f"日期：{TODAY}",
        "方法：B2 覆盖矩阵、B3 悬空引用、B5 待核实清单、B7 深度缺口。B1/B6 由外部子任务补充。",
        "",
        f"## B2 覆盖矩阵：空格 {len(empty)}，稀疏格（≤1 条）{len(sparse)}",
        "",
        "空格（前20）：" + "、".join("/".join(k) for k in empty[:20]),
        "",
        "稀疏格（前20）：" + "、".join("/".join(k) + f"({c})" for k, c in sparse[:20]),
        "",
        f"## B3 悬空引用：{len(dangling)}",
        "",
    ]
    lines += [f"- {a} → {b}：{c}" for a, b, c in dangling[:50]] or ["无"]
    lines += ["", f"## B5 待核实清单：{len(pending)}", ""]
    lines += [f"- {a}：{b}" for a, b in pending] or ["无"]
    lines += [
        "",
        f"## B7 深度缺口：核心未写 {len(core_l1)}，核心已写但 L1 {len(core_written_l1)}，重要未写 {len(important_unwritten)}",
        "",
        "核心未写（按 scope 序，前50）：" + "、".join(core_l1[:50]),
        "",
        "核心已写 L1（待升级）：" + "、".join(core_written_l1[:50]),
        "",
    ]
    out = ROOT / "research" / "gaps-round02.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"gaps: empty={len(empty)} sparse={len(sparse)} dangling={len(dangling)} pending={len(pending)} core_l1={len(core_l1)}")


if __name__ == "__main__":
    main()
