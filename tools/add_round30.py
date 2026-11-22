"""第30轮：新增 2 条稀疏格条目（墨西哥巴洛克/新陈代谢派），L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"
NEW = [
    ("wp-new-spanish-baroque", "New Spanish Baroque", "https://en.wikipedia.org/wiki/New_Spanish_Baroque", "学术著作", "墨西哥（新西班牙）巴洛克，代表子风格 Churrigueresque"),
    ("designingbuildings-baroque", "Baroque architecture — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Baroque_architecture", "学术著作", "西班牙与西属美洲晚期巴洛克称 Churrigueresque"),
    ("wp-metabolism-architecture", "Metabolism (architecture)", "https://en.wikipedia.org/wiki/Metabolism_(architecture)", "学术著作", "日本战后新陈代谢派，巨型结构与有机生长，槙文彦/黑川纪章等"),
    ("designingbuildings-metabolism", "Metabolism in architecture — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Metabolism", "学术著作", "可响应、可替换、有机生长的城市；中银胶囊塔"),
]

SVG1 = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='120' width='520' height='200' fill='none' stroke='var(--accent)'/><path d='M 160 200 Q 260 120 360 200 T 560 200' fill='none' stroke='var(--muted)'/><path d='M 160 260 Q 260 180 360 260 T 560 260' fill='none' stroke='var(--muted)'/><text x='260' y='90' fill='var(--ink)'>繁复装饰与曲面立面</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG2 = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='300' y='80' width='160' height='260' fill='none' stroke='var(--accent)'/><rect x='320' y='100' width='120' height='40' fill='var(--accent-soft)' stroke='var(--muted)'/><rect x='320' y='150' width='120' height='40' fill='var(--accent-soft)' stroke='var(--muted)'/><rect x='320' y='200' width='120' height='40' fill='var(--accent-soft)' stroke='var(--muted)'/><text x='240' y='60' fill='var(--ink)'>可生长的巨型结构</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"

ENTRIES = [
    {
        "id": "mexican-baroque", "title": "墨西哥巴洛克（新西班牙巴洛克）", "level": "L2",
        "tier": "补充", "theme": "风格", "period": "文艺复兴至19世纪", "region": "美洲",
        "definition": "墨西哥巴洛克是新西班牙（今墨西哥）在殖民时期发展出的巴洛克建筑与艺术，装饰繁复、色彩浓烈。",
        "time_or_place": "文艺复兴至19世纪、美洲（参见来源）。",
        "overview": "它把欧洲巴洛克与本土工艺结合，最典型的子风格是装饰密集的 Churrigueresque。",
        "related": ["baroque", "latin-american-colonial"],
        "sections": {
            "原理": "在巴洛克曲面与动势之上叠加密集的灰泥、雕刻与色彩，强化宗教空间的感染力。",
            "典型手法与适用条件": "以繁复立面、金饰与曲面塔楼装饰教堂；适用于殖民时期的宗教建筑。",
            "实例": "名称：新西班牙巴洛克教堂（类型性描述）；地点：墨西哥；设计者：不适用；年份：不适用。此处不复制图像。",
            "常见错误与限制": "装饰过度易杂乱、材料维护成本高；结构与防火按当地规范校核。" + REG,
            "一图": "见下方示意：繁复装饰与曲面立面。",
            "待核实": "具体教堂的设计者与年代待补充独立来源。",
        },
        "svg": [SVG1],
        "sources": ["wp-new-spanish-baroque", "designingbuildings-baroque"],
        "needs_verification": True,
        "pending_notes": "「墨西哥巴洛克」的具体实例（名称、地点、设计者、年代）待补充独立来源。",
    },
    {
        "id": "metabolism", "title": "新陈代谢派（Metabolism）", "level": "L2",
        "tier": "重要", "theme": "理论", "period": "20世纪", "region": "东亚",
        "definition": "新陈代谢派是战后日本以巨型结构＋可替换单元主张城市有机生长的建筑运动。",
        "time_or_place": "20世纪、东亚（参见来源）。",
        "overview": "它把建筑比作可生长、可替换的生物体，代表人物有菊竹清训、黑川纪章、槙文彦等。",
        "related": ["modernism", "japanese-architecture"],
        "sections": {
            "原理": "以固定的巨型骨架承载可更换的居住/功能单元，使城市能随时间生长与更新。",
            "典型手法与适用条件": "巨型结构＋插入式胶囊单元（如中银胶囊塔）；适用于高密度、快速变化的城市设想。",
            "实例": "名称：中银胶囊塔（Nakagin Capsule Tower）；地点：日本东京；设计者：黑川纪章（Kisho Kurokawa）；年份：1972 年。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "单元更换与维护成本高、结构寿命难匹配；实际建造须按规范校核。" + REG,
            "一图": "见下方示意：可生长的巨型结构。",
            "待核实": "中银胶囊塔的具体年代与保存现状待补充独立来源；其余实例待核实。",
        },
        "svg": [SVG2],
        "sources": ["wp-metabolism-architecture", "designingbuildings-metabolism"],
        "needs_verification": True,
        "pending_notes": "中银胶囊塔的年代与现状、以及其他实例待补充独立来源。",
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

    out = ROOT / "entries" / "batch-30.json"
    payload = {"unit_id": "batch-30", "title": "第30轮稀疏格补条目", "entries": ENTRIES}
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-30 written", len(ENTRIES))


if __name__ == "__main__":
    main()
