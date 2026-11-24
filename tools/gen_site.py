"""从 JSON 数据确定性渲染静态站点：首页、条目页、索引、来源页、覆盖报告。"""
from __future__ import annotations

import html
import json
import check
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
THEMES = ["理论", "风格", "造景", "动线", "下沉空间", "材料"]
PERIODS = ["古代", "中世纪", "文艺复兴至19世纪", "20世纪", "当代", "跨时期"]

CSS = """\
:root {
  --paper: #f4f1ea; --ink: #23201c; --muted: #6b645b; --line: #c9c1b4;
  --accent: #8a4b32; --accent-soft: #e8d9cd; --panel: #fffdf8; --shadow: 0 2px 10px rgba(40,30,20,.08);
}
@media (prefers-color-scheme: dark) {
  :root {
    --paper: #171614; --ink: #ece6dc; --muted: #a79f93; --line: #443f38;
    --accent: #d49372; --accent-soft: #3a2b23; --panel: #201e1b; --shadow: 0 2px 12px rgba(0,0,0,.35);
  }
}
* { box-sizing: border-box; }
body { margin:0; background:var(--paper); color:var(--ink); font-family:"Noto Serif SC","Songti SC",Georgia,serif; line-height:1.7; }
a { color:var(--accent); text-decoration:none; }
a:hover { text-decoration:underline; }
.wrap { max-width:1080px; margin:0 auto; padding:0 24px 64px; }
header.top { border-bottom:1px solid var(--line); background:var(--panel); }
header.top .wrap { padding-top:18px; padding-bottom:18px; display:flex; flex-wrap:wrap; gap:16px; align-items:baseline; justify-content:space-between; }
.brand { font-size:22px; font-weight:700; letter-spacing:.04em; }
nav a { margin-right:16px; font-size:14px; color:var(--muted); }
h1 { font-size:clamp(28px,4vw,44px); line-height:1.25; margin:40px 0 12px; }
h2 { font-size:24px; margin:36px 0 12px; border-left:4px solid var(--accent); padding-left:12px; }
h3 { font-size:18px; margin:24px 0 8px; }
p { text-wrap:pretty; }
.lead { color:var(--muted); font-size:18px; max-width:760px; }
.cards { display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:16px; margin:28px 0; }
.card { background:var(--panel); border:1px solid var(--line); border-radius:10px; padding:18px; box-shadow:var(--shadow); }
.card .num { font-size:32px; font-weight:700; color:var(--accent); }
.card .label { color:var(--muted); font-size:14px; }
table { width:100%; border-collapse:collapse; margin:16px 0; font-size:14px; }
th,td { border:1px solid var(--line); padding:8px 10px; text-align:left; vertical-align:top; }
th { background:var(--accent-soft); font-weight:600; }
.tag { display:inline-block; border:1px solid var(--line); border-radius:99px; padding:1px 9px; font-size:12px; color:var(--muted); margin-right:6px; }
figure { margin:20px 0; padding:14px; background:var(--panel); border:1px solid var(--line); border-radius:10px; }
figure svg { width:100%; max-width:760px; height:auto; display:block; margin:auto; }
figcaption { text-align:center; color:var(--muted); font-size:13px; margin-top:8px; }
.note { color:var(--muted); font-size:13px; border-top:1px dashed var(--line); padding-top:12px; margin-top:28px; }
.badge-ok { color:#3d7a4d; } .badge-no { color:#b0513a; }
.toc { columns:2; list-style:none; padding:0; }
.toc li { margin:4px 0; break-inside:avoid; }
@media (max-width:640px) { .toc { columns:1; } nav a { font-size:13px; margin-right:10px; } }
"""


def load_json(rel):
    with (ROOT / rel).open(encoding="utf-8") as fh:
        return json.load(fh)


def load_entries():
    items = []
    for path in sorted((ROOT / "entries").glob("*.json")):
        with path.open(encoding="utf-8") as fh:
            items.extend(json.load(fh).get("entries", []))
    return items


def esc(text):
    return html.escape(str(text), quote=True)


def nav(depth=0):
    prefix = "../" * depth
    links = [
        (f"{prefix}index.html", "首页"),
        (f"{prefix}indexes.html", "索引"),
        (f"{prefix}sources.html", "来源"),
        (f"{prefix}coverage.html", "覆盖报告"),
        (f"{prefix}timeline.html", "时间线"),
    ]
    return "<nav>" + "".join(f'<a href="{h}">{t}</a>' for h, t in links) + "</nav>"


def shell(title, body, depth=0):
    return f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} — 绘画理论与建筑空间设计</title>
<link rel="stylesheet" href="{'../' * depth}assets/site.css"></head>
<body><header class="top"><div class="wrap"><span class="brand">绘画理论与建筑空间设计</span>{nav(depth)}</div></header>
<main class="wrap">{body}</main></body></html>
"""


def write_page(rel, content):
    path = SITE / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def render_home(coverage, sources, entries):
    total = coverage["total"]
    written = len(entries)
    written_levels = Counter(e.get("level", "L1") for e in entries)
    target_levels = Counter(e.get("level", "L1") for e in coverage["entries"])
    verified = sum(1 for s in sources if s.get("verified"))
    pending = sum(1 for e in entries if e.get("needs_verification"))
    theme_counts = Counter(e["theme"] for e in coverage["entries"])
    cards = [
        (total, "范围条目"), (written, "已写条目"),
        (written_levels["L1"], "已写 L1"), (written_levels["L2"], "已写 L2"),
        (verified, "已核验来源"), (pending, "待核实条目"),
    ]
    body = [
        "<h1>绘画理论与建筑空间设计</h1>",
        '<p class="lead">一个可离线浏览、可机器校验的知识脉络库。数据来自结构化 JSON，每条内容可追溯到已核验来源；查不到的事实一律标记为待核实。</p>',
        '<div class="cards">' + "".join(
            f'<div class="card"><div class="num">{n}</div><div class="label">{esc(label)}</div></div>' for n, label in cards
        ) + "</div>",
        "<h2>按主题进入</h2><ul class=\"toc\">",
    ]
    for theme in THEMES:
        body.append(f'<li><a href="indexes.html#{theme}">{theme}</a> <span class="tag">{theme_counts[theme]} 条</span></li>')
    body += [
        "</ul>",
        f'<p class="note">范围目标层级：L1 {target_levels["L1"]}、L2 {target_levels["L2"]}、L3 {target_levels["L3"]}。上方卡片统计的是已写条目。</p>',
        "<h2>阅读约定</h2>",
        "<p>图示均为自绘内联 SVG，仅用于说明空间或构图关系，非施工图。涉及尺寸、坡度、消防、无障碍的数据只作一般性说明；实际工程须按当地规范和专业设计人员的要求。</p>",
        '<p class="note">生成物由 tools/gen_site.py 确定性输出，请勿手工修改 site/ 下的 HTML。</p>',
    ]
    write_page("index.html", shell("首页", "\n".join(body)))


def render_entry(entry, sources_by_id, written_ids, titles):
    eid = entry["id"]
    body = [f'<h1>{esc(entry["title"])}</h1>']
    body.append(
        '<p>' + "".join(
            f'<span class="tag">{esc(t)}</span>' for t in
            (entry.get("level", ""), entry.get("tier", ""), entry.get("theme", ""),
             entry.get("period", ""), entry.get("region", ""))
        ) + "</p>"
    )
    body.append(f'<p class="lead">{esc(entry.get("overview", ""))}</p>')
    sections = [
        ("核心概念与定义", entry.get("definition", "")),
        ("时间与位置", entry.get("time_or_place", "")),
    ]
    for name in ("原理", "典型手法与适用条件", "实例", "常见错误与限制", "一图", "待核实"):
        if name in entry.get("sections", {}):
            sections.append((name, entry["sections"][name]))
    for heading, text in sections:
        if text:
            body.append(f"<h2>{esc(heading)}</h2><p>{esc(text)}</p>")
    for pos, diagram in enumerate(entry.get("svg", []), 1):
        body.append(f'<figure>{diagram}<figcaption>图 {pos}：示意图，非施工图</figcaption></figure>')
    refs = entry.get("sources", [])
    if refs:
        body.append("<h2>来源</h2><ul>")
        for ref in refs:
            src = sources_by_id.get(ref, {})
            url = src.get("url")
            title = esc(src.get("title", ref))
            body.append(f'<li>{f"<a href={chr(34)}{esc(url)}{chr(34)}>{title}</a>" if url else title} <span class="tag">{esc(src.get("type", ""))}</span></li>')
        body.append("</ul>")
    related = entry.get("related", [])
    if related:
        body.append("<h2>相关条目</h2><ul>")
        for r in related:
            label = esc(titles.get(r, r))
            body.append(f'<li><a href="{esc(r)}.html">{label}</a></li>' if r in written_ids else f'<li>{label}（待写）</li>')
        body.append("</ul>")
    if entry.get("needs_verification") and "待核实" not in entry.get("sections", {}):
        body.append(f'<h2>待核实</h2><p>{esc(entry.get("pending_notes", ""))}</p>')
    body.append('<p class="note">涉及尺寸、坡度、消防、无障碍等内容仅为一般性说明；实际工程须按当地规范和专业设计人员的要求。</p>')
    write_page(f"entries/{eid}.html", shell(entry["title"], "\n".join(body), depth=1))


def render_indexes(coverage, entries):
    by_id = {e["id"]: e for e in entries}
    body = ["<h1>全站条目索引</h1>", '<p class="lead">按主题分组；未写条目显示“待写”，点击已写条目进入详情。</p>']
    for theme in THEMES:
        rows = [r for r in coverage["entries"] if r["theme"] == theme]
        body.append(f'<h2 id="{theme}">{theme}（{len(rows)}）</h2><table><tr><th>名称</th><th>层级</th><th>层级深度</th><th>时期</th><th>地区</th><th>状态</th></tr>')
        for r in rows:
            link = f'<a href="entries/{r["id"]}.html">{esc(r["title"])}</a>' if r["id"] in by_id else esc(r["title"])
            status = esc(by_id[r["id"]].get("level", "已写")) if r["id"] in by_id else "待写"
            body.append(
                f'<tr><td>{link}</td><td>{esc(r["tier"])}</td><td>{esc(r.get("level", "L1"))}</td>'
                f'<td>{esc(r["period"])}</td><td>{esc(r["region"])}</td><td>{status}</td></tr>'
            )
        body.append("</table>")
    write_page("indexes.html", shell("索引", "\n".join(body)))


def render_sources(sources):
    body = ["<h1>来源库</h1>", '<p class="lead">只有 verified=true 的来源可供条目引用；链接状态由 tools/linkcheck.py 记录。</p>']
    body.append("<table><tr><th>标题</th><th>作者/机构</th><th>类型</th><th>年份</th><th>核验</th><th>链接</th><th>说明</th></tr>")
    for src in sources:
        title = esc(src.get("title", ""))
        url = src.get("url")
        if url:
            title = f'<a href="{esc(url)}">{title}</a>'
        ok = '<span class="badge-ok">已核验</span>' if src.get("verified") else '<span class="badge-no">待核验</span>'
        link = src.get("link_ok", None)
        link_text = "可达" if link is True else "反爬拒绝" if link == "blocked" else "死链" if link is False else "无链接"
        body.append(
            f'<tr><td>{title}</td><td>{esc(src.get("author", ""))}</td><td>{esc(src.get("type", ""))}</td>'
            f'<td>{esc(src.get("year") if src.get("year") is not None else "动态/未标注")}</td><td>{ok}</td>'
            f'<td>{link_text}</td><td>{esc(src.get("note", ""))}</td></tr>'
        )
    body.append("</table>")
    write_page("sources.html", shell("来源", "\n".join(body)))


def render_coverage(coverage, entries):
    rows = coverage["entries"]
    done = {e["id"] for e in entries}
    body = ["<h1>覆盖报告</h1>", f'<p class="lead">范围共 {len(rows)} 条，已写 {len(done)} 条。下表按主题与时期统计范围条目数。</p>']
    body.append("<table><tr><th>主题</th>" + "".join(f"<th>{p}</th>" for p in PERIODS) + "<th>合计</th></tr>")
    for theme in THEMES:
        cells = []
        for period in PERIODS:
            n = sum(1 for r in rows if r["theme"] == theme and r["period"] == period)
            cells.append(str(n) if n else "—")
        total = sum(1 for r in rows if r["theme"] == theme)
        body.append(f"<tr><td>{theme}</td>" + "".join(f"<td>{c}</td>" for c in cells) + f"<td>{total}</td></tr>")
    body.append("</table>")
    blanks = [r for r in rows if r["id"] not in done]
    groups = Counter((r["theme"], r["period"], r["region"]) for r in blanks)
    body.append(f'<h2>未写条目（{len(blanks)}，{len(groups)} 个格子）</h2>')
    body.append('<table><tr><th>主题</th><th>时期</th><th>地区</th><th>未写数</th></tr>')
    for (theme, period, region), n in sorted(groups.items()):
        body.append(f'<tr><td>{esc(theme)}</td><td>{esc(period)}</td><td>{esc(region)}</td><td>{n}</td></tr>')
    body.append('</table>')
    write_page("coverage.html", shell("覆盖报告", "\n".join(body)))


def render_timeline(coverage, entries):
    order = ["古代", "中世纪", "文艺复兴至19世纪", "20世纪", "当代", "跨时期"]
    by_id = {e["id"]: e for e in entries}
    rows = coverage["entries"]
    grouped = {p: [] for p in order}
    for r in rows:
        per = r.get("period", "跨时期")
        grouped.setdefault(per, []).append(r)
    body = ["<h1>时间线</h1>", '<p class="lead">按时期浏览条目（时期为大类，同一条目可能跨时期）。</p>']
    for per in order + [p for p in grouped if p not in order]:
        items = grouped.get(per, [])
        if not items:
            continue
        body.append(f'<h2>{esc(per)}</h2><ul>')
        for r in sorted(items, key=lambda x: x["id"]):
            e = by_id.get(r["id"])
            if e and r["id"] in by_id:
                body.append(f'<li><a href="entries/{esc(r["id"])}.html">{esc(r["title"])}</a> <span class="tag">{esc(r.get("theme",""))}</span> <span class="tag">{esc(r.get("region",""))}</span></li>')
            else:
                body.append(f'<li>{esc(r["title"])}（待写）</li>')
        body.append("</ul>")
    write_page("timeline.html", shell("时间线", "\n".join(body)))


def main():
    coverage = load_json("coverage.json")
    sources = load_json("data/sources.json")["sources"]
    entries = load_entries()
    sources_by_id = {s["id"]: s for s in sources}
    titles = {r["id"]: r["title"] for r in coverage["entries"]}
    written_ids = {e["id"] for e in entries}
    for entry in entries:
        for diagram in entry.get("svg", []):
            errors = check.validate_svg(diagram)
            if errors:
                raise ValueError(f"SVG {entry['id']}: {errors}")
    SITE.mkdir(exist_ok=True)
    (SITE / "assets").mkdir(exist_ok=True)
    (SITE / "assets" / "site.css").write_text(CSS, encoding="utf-8")
    render_home(coverage, sources, entries)
    for entry in entries:
        render_entry(entry, sources_by_id, written_ids, titles)
    render_indexes(coverage, entries)
    render_sources(sources)
    render_coverage(coverage, entries)
    render_timeline(coverage, entries)
    print(f"generated site/: {len(entries)} entries, {len(sources)} sources")


if __name__ == "__main__":
    main()
