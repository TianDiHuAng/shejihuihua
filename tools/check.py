"""质量校验器：数据字段、来源核验、SVG 安全、覆盖一致性。"""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

THEMES = ("理论", "风格", "造景", "动线", "下沉空间", "材料")

ID_RE = re.compile(r"^[a-z0-9-]+$")
SVG_ALLOWED = {
    "svg", "g", "rect", "circle", "ellipse", "line", "polyline", "polygon",
    "path", "text", "tspan", "defs", "marker", "title", "desc", "use",
}
REGULATION_NOTE = "实际工程须按当地规范和专业设计人员的要求"
RISK_WORDS = ("尺寸", "坡度", "消防", "无障碍", "排水", "防潮", "高差", "安全")
REQUIRED_ENTRY_FIELDS = (
    "id", "title", "level", "tier", "theme", "period", "region",
    "definition", "time_or_place", "overview", "related", "sources",
    "needs_verification", "pending_notes",
)


def load_json(root: Path, rel: str):
    path = root / rel
    if not path.exists():
        return None
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def scope_ids(root: Path) -> set[str]:
    path = root / "scope.md"
    if not path.exists():
        return set()
    ids = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*([a-z0-9-]+)\s*\|", line)
        if m and m.group(1) not in ("id", "---"):
            ids.add(m.group(1))
    return ids


def matrix_counts(root: Path):
    path = root / "coverage-matrix.md"
    if not path.exists():
        return None
    counts = {}
    region = None
    periods = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s+地区：(.+)$", line.strip())
        if m:
            region = m.group(1).strip()
            periods = []
            continue
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0] == "主题":
            periods = cells[1:]
            continue
        if region and periods and len(cells) == len(periods) + 1 and cells[0] in THEMES:
            for period, cell in zip(periods, cells[1:]):
                num = re.match(r"^(\d+)", cell)
                counts[(cells[0], period, region)] = int(num.group(1)) if num else 0
    return counts


def validate_scope(root: Path) -> list[str]:
    errors = []
    ids = scope_ids(root)
    coverage = load_json(root, "coverage.json")
    if not ids:
        errors.append("scope.md 未找到条目表格")
    if not coverage:
        errors.append("coverage.json 缺失或无法解析")
        return errors
    cov_rows = coverage.get("entries", [])
    cov_ids = {e.get("id") for e in cov_rows}
    if ids != cov_ids:
        errors.append(f"scope/coverage id 不一致: 仅 scope={sorted(ids - cov_ids)[:5]}, 仅 coverage={sorted(cov_ids - ids)[:5]}")
    if coverage.get("total") != len(cov_rows):
        errors.append("coverage.json total 与 entries 数量不一致")
    counts = matrix_counts(root)
    if counts is None:
        errors.append("coverage-matrix.md 缺失，无法校验覆盖矩阵")
    else:
        expected = Counter((r["theme"], r["period"], r["region"]) for r in cov_rows)
        if sum(counts.values()) != len(cov_rows):
            errors.append(f"覆盖矩阵总数 {sum(counts.values())} 与 scope 条目数 {len(cov_rows)} 不一致")
        for key, n in expected.items():
            if counts.get(key, 0) != n:
                errors.append(f"覆盖矩阵格子 {key} 为 {counts.get(key, 0)}，应为 {n}")
        for key, n in counts.items():
            if expected.get(key, 0) != n:
                errors.append(f"覆盖矩阵格子 {key} 为 {n}，应为 {expected.get(key, 0)}")
    return errors


def validate_sources(root: Path) -> tuple[list[str], dict]:
    errors = []
    data = load_json(root, "data/sources.json")
    if not data or not isinstance(data.get("sources"), list):
        return ["data/sources.json 缺失或格式错误"], {}
    sources = {}
    current_year = 2026
    for src in data["sources"]:
        sid = src.get("id", "")
        if not ID_RE.match(sid):
            errors.append(f"来源 id 非法: {sid!r}")
            continue
        if sid in sources:
            errors.append(f"来源 id 重复: {sid}")
        sources[sid] = src
        for field in ("title", "author", "type", "url", "verified", "note"):
            if field not in src or src[field] in (None, ""):
                errors.append(f"来源 {sid} 缺少字段 {field}")
        year = src.get("year")
        if year is not None:
            if not isinstance(year, int) or not (-4000 <= year <= current_year + 1):
                errors.append(f"来源 {sid} 年份非法: {year!r}")
        if src.get("verified"):
            if not str(src.get("url", "")).startswith(("http://", "https://")):
                errors.append(f"来源 {sid} verified=true 但 URL 非法")
            if not str(src.get("note", "")).strip():
                errors.append(f"来源 {sid} verified=true 但缺少核验说明")
            if src.get("link_ok") is False:
                errors.append(f"来源 {sid} verified=true 但 link_ok=false（死链不得标已核验）")
    # URL 唯一性：同 URL 多登记须在 note 中显式披露"[B4]"，否则视为重复来源
    from urllib.parse import urlsplit
    by_url = {}
    for src in data["sources"]:
        url = str(src.get("url", "") or "").strip()
        if not url:
            continue
        parts = urlsplit(url)
        key = (parts.netloc, parts.path, parts.query)
        by_url.setdefault(key, []).append(src)
    for (netloc, path, query), group in by_url.items():
        if len(group) > 1 and not all("[B4]" in str(s.get("note", "")) for s in group):
            errors.append(f"重复 URL（未披露 [B4]）: {netloc}{path}?{query} -> {[s['id'] for s in group]}")
    return errors, sources


def validate_svg(svg: str) -> list[str]:
    errors = []
    if not isinstance(svg, str) or "<svg" not in svg:
        return ["SVG 内容缺失"]
    low = svg.lower()
    for forbidden in ("<script", "javascript:", "href=", "<image", "<iframe", "url("):
        if forbidden in low:
            errors.append(f"SVG 含禁止内容: {forbidden.strip()}")
    event = re.search(r"\son[a-z]+\s*=", low)
    if event:
        errors.append(f"SVG 含禁止内容: {event.group(0).strip()}")
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as exc:
        return [f"SVG XML 解析失败: {exc}"]
    if root.tag.split("}")[-1] != "svg":
        errors.append("SVG 根元素不是 svg")
    viewbox = root.attrib.get("viewBox")
    if not viewbox:
        errors.append("SVG 缺少 viewBox")
    else:
        nums = []
        for token in viewbox.replace(",", " ").split():
            try:
                nums.append(float(token))
            except ValueError:
                errors.append("SVG viewBox 数值非法")
                break
        if len(nums) == 4:
            min_x, min_y, width, height = nums
            if width <= 0 or height <= 0:
                errors.append("SVG viewBox 宽高必须为正")
            else:
                max_x, max_y = min_x + width, min_y + height
                margin_x, margin_y = width * 0.2, height * 0.2
                for el in root.iter():
                    tag = el.tag.split("}")[-1]
                    if tag not in SVG_ALLOWED:
                        errors.append(f"SVG 含非白名单元素: {tag}")
                    for attr in ("x", "y", "x1", "y1", "x2", "y2", "cx", "cy"):
                        val = el.attrib.get(attr)
                        if val is None:
                            continue
                        try:
                            num = float(val)
                        except ValueError:
                            errors.append(f"SVG {tag} 的 {attr} 非数值")
                            continue
                        if attr in ("x", "x1", "x2", "cx"):
                            if not (min_x - margin_x <= num <= max_x + margin_x):
                                errors.append(f"SVG {tag} 的 {attr}={num} 超出 viewBox")
                        elif not (min_y - margin_y <= num <= max_y + margin_y):
                            errors.append(f"SVG {tag} 的 {attr}={num} 超出 viewBox")

                    def in_x(value):
                        return min_x - margin_x <= value <= max_x + margin_x

                    def in_y(value):
                        return min_y - margin_y <= value <= max_y + margin_y

                    if "r" in el.attrib:
                        try:
                            radius = float(el.attrib["r"])
                            c_x = float(el.attrib.get("cx", 0))
                            c_y = float(el.attrib.get("cy", 0))
                            if not (in_x(c_x - radius) and in_x(c_x + radius)
                                    and in_y(c_y - radius) and in_y(c_y + radius)):
                                errors.append(f"SVG {tag} 的 r={radius} 超出 viewBox")
                        except ValueError:
                            errors.append(f"SVG {tag} 的 r 非数值")
                    if tag == "ellipse" and ("rx" in el.attrib or "ry" in el.attrib):
                        try:
                            c_x = float(el.attrib.get("cx", 0))
                            c_y = float(el.attrib.get("cy", 0))
                            rx = float(el.attrib.get("rx", 0))
                            ry = float(el.attrib.get("ry", 0))
                            if not (in_x(c_x - rx) and in_x(c_x + rx)
                                    and in_y(c_y - ry) and in_y(c_y + ry)):
                                errors.append(f"SVG ellipse 的 rx/ry 超出 viewBox")
                        except ValueError:
                            errors.append(f"SVG ellipse 的 rx/ry 非数值")
                    if tag == "rect" and ("width" in el.attrib or "height" in el.attrib):
                        try:
                            x = float(el.attrib.get("x", 0))
                            y = float(el.attrib.get("y", 0))
                            rw = float(el.attrib.get("width", 0))
                            rh = float(el.attrib.get("height", 0))
                            if not (in_x(x) and in_x(x + rw) and in_y(y) and in_y(y + rh)):
                                errors.append(f"SVG rect 的 width/height 超出 viewBox")
                        except ValueError:
                            errors.append(f"SVG rect 的 width/height 非数值")
                    if tag != "svg":
                        for attr in ("width", "height"):
                            if attr not in el.attrib:
                                continue
                            try:
                                value = float(el.attrib[attr])
                            except ValueError:
                                errors.append(f"SVG {tag} 的 {attr} 非数值")
                                continue
                            if value <= 0 or (attr == "width" and not in_x(value)) or (attr == "height" and not in_y(value)):
                                errors.append(f"SVG {tag} 的 {attr}={value} 超出 viewBox")
                    for attr in ("points", "d"):
                        if attr not in el.attrib:
                            continue
                        values = [float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", el.attrib[attr])]
                        for index, value in enumerate(values):
                            ok = in_x(value) if index % 2 == 0 else in_y(value)
                            if not ok:
                                errors.append(f"SVG {tag} 的 {attr} 超出 viewBox")
                                break
    return errors


def validate_entries(root: Path, sources: dict) -> tuple[list[str], dict]:
    errors = []
    seen = set()
    by_id = {}
    for path in sorted((root / "entries").glob("*.json")):
        with path.open(encoding="utf-8") as fh:
            unit = json.load(fh)
        if not unit.get("unit_id") or not isinstance(unit.get("entries"), list):
            errors.append(f"{path.name} 缺少 unit_id 或 entries")
            continue
        for entry in unit["entries"]:
            eid = entry.get("id", "")
            label = f"条目 {eid}"
            if not ID_RE.match(eid):
                errors.append(f"条目 id 非法: {eid!r}")
            if eid in seen:
                errors.append(f"条目 id 重复: {eid}")
            seen.add(eid)
            by_id[eid] = entry
            for field in REQUIRED_ENTRY_FIELDS:
                if field not in entry:
                    errors.append(f"{label} 缺少字段 {field}")
            if entry.get("level") not in ("L1", "L2", "L3"):
                errors.append(f"{label} level 非法")
            for field in ("title", "tier", "theme", "period", "region", "definition", "time_or_place", "overview"):
                if not str(entry.get(field, "")).strip():
                    errors.append(f"{label} 字段 {field} 为空")
            refs = entry.get("sources", [])
            if not isinstance(refs, list) or not refs:
                errors.append(f"{label} 缺少来源")
            else:
                for ref in refs:
                    if ref not in sources:
                        errors.append(f"{label} 引用未定义来源 {ref}")
                    elif not sources[ref].get("verified"):
                        errors.append(f"{label} 引用未 verified 来源 {ref}")
                if len(set(refs)) < 2 and not entry.get("needs_verification"):
                    errors.append(f"{label} 单源且未标待核实，违反双源规则")
            if entry.get("needs_verification") and not str(entry.get("pending_notes", "")).strip():
                errors.append(f"{label} needs_verification=true 但 pending_notes 为空")
            if not entry.get("needs_verification") and str(entry.get("pending_notes", "")).strip():
                errors.append(f"{label} 有待核实说明但 needs_verification=false")
            for related in entry.get("related", []):
                if related not in scope_ids(root):
                    errors.append(f"{label} related 指向 scope 外条目 {related}")
            svgs = entry.get("svg", [])
            if entry.get("level") in ("L2", "L3"):
                if not 1 <= len(svgs) <= 2:
                    errors.append(f"{label} {entry['level']} 需 1–2 张 SVG")
                if not any("示意图，非施工图" in str(s) for s in svgs):
                    errors.append(f"{label} SVG 缺少说明“示意图，非施工图”")
            for pos, diagram in enumerate(svgs):
                for err in validate_svg(diagram):
                    errors.append(f"{label} SVG#{pos + 1}: {err}")
            sections = entry.get("sections", {})
            if entry.get("level") in ("L2", "L3"):
                for field in ("原理", "典型手法与适用条件", "实例", "常见错误与限制", "一图", "待核实"):
                    if not str(sections.get(field, "")).strip():
                        errors.append(f"{label} 缺少 L2 结构节: {field}")
            inline_text = " ".join(str(v) for k, v in sections.items() if k != "待核实")
            if "待核实" in inline_text and not entry.get("needs_verification"):
                errors.append(f"{label} 正文含待核实声明但标志位为 false")
            risk_text = " ".join(str(v) for v in sections.values())
            if any(word in risk_text for word in RISK_WORDS) and REGULATION_NOTE not in risk_text:
                errors.append(f"{label} 涉及尺寸/坡度/消防/无障碍等，缺少规范提示")
    return errors, by_id


def validate_coverage(root: Path, by_id: dict) -> list[str]:
    errors = []
    coverage = load_json(root, "coverage.json")
    if not coverage:
        return ["coverage.json 缺失"]
    entries = coverage.get("entries", [])
    cov = {e.get("id"): e for e in entries}
    for eid, entry in by_id.items():
        if eid not in cov:
            errors.append(f"条目 {eid} 未登记在 coverage.json")
            continue
        row = cov[eid]
        if row.get("level") != entry.get("level"):
            errors.append(f"条目 {eid} 层级与 coverage 不一致")
        for field in ("theme", "tier", "period", "region"):
            if row.get(field) != entry.get(field):
                errors.append(f"条目 {eid} 的 {field} 与 coverage 不一致")
        if row.get("source_count") != len(entry.get("sources", [])):
            errors.append(f"条目 {eid} 来源数与 coverage 不一致")
        if row.get("title") != entry.get("title"):
            errors.append(f"条目 {eid} 名称与 coverage 不一致")
        if bool(row.get("needs_verification_count")) != bool(entry.get("needs_verification")):
            errors.append(f"条目 {eid} 待核实状态与 coverage 不一致")
    return errors


def validate_all(root: Path) -> list[str]:
    errors = validate_scope(root)
    source_errors, sources = validate_sources(root)
    errors += source_errors
    entry_errors, by_id = validate_entries(root, sources)
    errors += entry_errors
    errors += validate_coverage(root, by_id)
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description="知识库质量校验器")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    parser.add_argument("--scope-only", action="store_true")
    args = parser.parse_args(argv)
    root = Path(args.root)
    errors = validate_scope(root) if args.scope_only else validate_all(root)
    if errors:
        print(f"FAIL: {len(errors)} errors")
        for err in errors[:200]:
            print(" -", err)
        return 1
    mode = "scope-only" if args.scope_only else "all"
    print(f"PASS: {mode} checks, 0 errors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
