"""第31轮：新增 2 条稀疏格条目（学院派理论/古典柱式），L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"
NEW = [
    ("wp-academic-art", "Academic art", "https://en.wikipedia.org/wiki/Academic_art", "学术著作", "欧洲学院体系下的绘画雕塑，系统化艺术教学"),
    ("artincontext-academic", "Academic Art — Art in Context", "https://artincontext.org/academic-art/", "学术著作", "学院派重视素描/解剖/构图/完成度与题材等级"),
    ("wp-classical-order", "Classical order", "https://en.wikipedia.org/wiki/Classical_order", "学术著作", "多立克/爱奥尼/科林斯三种希腊柱式"),
    ("designingbuildings-classical", "Classical architecture — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Classical_architecture", "学术著作", "希腊三柱式，罗马增塔司干与复合柱式"),
]

SVG1 = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='120' width='520' height='200' fill='none' stroke='var(--accent)'/><line x1='200' y1='160' x2='560' y2='160' stroke='var(--muted)'/><line x1='200' y1='200' x2='560' y2='200' stroke='var(--muted)'/><line x1='200' y1='240' x2='560' y2='240' stroke='var(--muted)'/><text x='250' y='90' fill='var(--ink)'>素描、比例与题材等级的学院规范</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG2 = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='140' y1='300' x2='620' y2='300' stroke='var(--ink)' stroke-width='3'/><line x1='220' y1='300' x2='220' y2='150' stroke='var(--accent)' stroke-width='14'/><line x1='330' y1='300' x2='330' y2='150' stroke='var(--accent)' stroke-width='14'/><line x1='440' y1='300' x2='440' y2='150' stroke='var(--accent)' stroke-width='14'/><line x1='180' y1='140' x2='480' y2='140' stroke='var(--muted)' stroke-width='10'/><text x='260' y='110' fill='var(--ink)'>柱式比例与檐部</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"

ENTRIES = [
    {
        "id": "academic-art-theory", "title": "学院派理论与素描教学（学院主义 / Academic art）", "level": "L2",
        "tier": "重要", "theme": "理论", "period": "文艺复兴至19世纪", "region": "全球",
        "definition": "学院派理论是欧洲美术学院体系下形成的绘画与雕塑规范，以系统化的素描教学为核心。",
        "time_or_place": "文艺复兴至19世纪、全球（参见来源）。",
        "overview": "学院以素描、解剖、构图与完成度为训练重点，并按题材等级评价作品。",
        "related": ["composition", "proportion"],
        "sections": {
            "原理": "学院把艺术教学制度化：以古典范本训练素描与解剖，用比例与构图规则统一评判标准。",
            "典型手法与适用条件": "先素描后油画、按题材等级选题；适用于学院教育与历史画创作。",
            "实例": "名称：欧洲美术学院的历史画教学（类型性描述）；地点：欧洲；设计者：不适用；年份：不适用。此处不复制图像。",
            "常见错误与限制": "过度规范会压抑个性与创新；题材等级观念带有时代偏见。" + REG,
            "一图": "见下方示意：学院规范与素描训练。",
            "待核实": "具体学院与代表作品的设计者、年代待补充独立来源。",
        },
        "svg": [SVG1],
        "sources": ["wp-academic-art", "artincontext-academic"],
        "needs_verification": True,
        "pending_notes": "「学院派理论」的具体学院与代表作品待补充独立来源。",
    },
    {
        "id": "classical-order", "title": "古典柱式（古典建筑柱式 / Classical order）", "level": "L2",
        "tier": "重要", "theme": "理论", "period": "古代", "region": "欧洲",
        "definition": "古典柱式是按既定比例组合柱、檐与基座的一套建筑规范，希腊以多立克、爱奥尼、科林斯为主。",
        "time_or_place": "古代、欧洲（参见来源）。",
        "overview": "柱式以固定比例关系统摄细部，罗马在希腊三式之外增塔司干与复合柱式。",
        "related": ["ancient-greek", "vitruvian-triad"],
        "sections": {
            "原理": "柱径、柱距与檐部高度之间存在可感知的比例关系，使建筑呈现秩序与尺度感。",
            "典型手法与适用条件": "按柱式确定柱头、檐部与基座细部；适用于神庙、公共建筑与古典复兴立面。",
            "实例": "名称：古希腊神庙柱廊（类型性描述）；地点：欧洲；设计者：不适用；年份：不适用。此处不复制图像。",
            "常见错误与限制": "脱离结构比例照搬柱式会沦为布景；石材尺寸与抗震须按当地规范校核。" + REG,
            "一图": "见下方示意：柱式比例与檐部。",
            "待核实": "具体神庙的设计者与年代待补充独立来源。",
        },
        "svg": [SVG2],
        "sources": ["wp-classical-order", "designingbuildings-classical"],
        "needs_verification": True,
        "pending_notes": "「古典柱式」的具体实例（名称、地点、设计者、年代）待补充独立来源。",
    },
]


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, typ, note in NEW:
        if sid in by_id:
            continue
        data["sources"].append({
            "id": sid, "title": title, "author": "Wikipedia/机构", "type": typ,
            "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
            "note": f"访问于 2026-11-22，经 owiki 镜像/独立站点实抓核对标题与正文，canonical 直连待复；{note}",
        })
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    out = ROOT / "entries" / "batch-31.json"
    out.write_text(json.dumps({"unit_id": "batch-31", "title": "第31轮稀疏格补条目", "entries": ENTRIES},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-31 written", len(ENTRIES))


if __name__ == "__main__":
    main()
