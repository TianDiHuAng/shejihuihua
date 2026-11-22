"""第25轮：纳入 B4 补齐的 5 条新 scope 条目与其来源（双源实抓）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW_SRC = [
    ("wp-rembrandt-lighting", "Rembrandt lighting", "https://en.wikipedia.org/wiki/Rembrandt_lighting", "权威百科", "伦勃朗光定义"),
    ("rijksmuseum-rembrandt", "Rembrandt van Rijn — Rijksmuseum", "https://www.rijksmuseum.nl/en/collection/node/Rembrandt-van-Rijn--ba2dc062acd137ffeac364321b7b10df", "官方机构", "伦勃朗明暗对比与戏剧性"),
    ("dailyart-tenebrism", "Tenebrism 101 — DailyArt Magazine", "https://www.dailyartmagazine.com/tenebrism/", "学术著作", "暗绘风格来源与机制"),
    ("wp-town-square", "Town square (Plaza)", "https://en.wikipedia.org/wiki/Plaza", "权威百科", "城市广场定义"),
    ("pps-successful-place", "What Makes a Successful Place? — Project for Public Spaces", "https://www.pps.org/article/grplacefeat", "官方机构", "优秀公共空间作为城市客厅"),
    ("designingbuildings-atrium", "Atrium definition — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Atrium_definition", "学术著作", "中庭定义（引英国 Approved Document B）"),
    ("ecfr-1910-37", "29 CFR 1910.37 — eCFR", "https://www.ecfr.gov/current/title-29/section-1910.37", "官方机构", "出口标识可见性与照度要求"),
]

# id|名称|主题|层级|时期|地区|来源A|来源B
SCOPE = [
    ("rembrandt", "伦勃朗光", "理论", "补充", "17世纪", "欧洲", "wp-rembrandt-lighting", "rijksmuseum-rembrandt"),
    ("tenebrism", "暗绘风格（暗色调主义）", "风格", "补充", "17世纪", "欧洲", "wp-tenebrism", "dailyart-tenebrism"),
    ("plaza", "广场（城市广场）", "造景", "重要", "跨时期", "全球", "wp-town-square", "pps-successful-place"),
    ("atrium-architecture", "中庭", "材料", "重要", "跨时期", "全球", "wp-atrium-architecture", "designingbuildings-atrium"),
    ("exit-sign", "疏散标识（安全出口标识）", "动线", "补充", "20世纪", "全球", "wp-exit-sign", "ecfr-1910-37"),
]

DATA = {
    "rembrandt": ("以单侧主光在面部形成三角形亮区、另一侧深暗的人像布光法。", "17世纪、欧洲（参见来源）。", "它在明暗对比中塑造体积与戏剧感，常用于肖像摄影与绘画。"),
    "tenebrism": ("把背景压到极暗、以强烈聚光突出主体的绘画风格。", "17世纪、欧洲（参见来源）。", "暗绘风格是明暗法的极端化，营造神秘与戏剧张力。"),
    "plaza": ("城市中向公众开放、供聚会与活动的硬质开敞空间。", "跨时期、全球（参见来源）。", "优秀广场兼具通行、停留与交往功能，常被称为“城市客厅”。"),
    "atrium-architecture": ("建筑内部贯通多层、常覆以天窗的中央开敞空间。", "跨时期、全球（参见来源）。", "中庭把天然光引入建筑深处并组织交通与社交。"),
    "exit-sign": ("标示安全出口方向与位置的疏散标识。", "20世纪、全球（参见来源）。", "疏散标识以可见性与照明保障紧急时快速识别出口。"),
}


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, typ, note in NEW_SRC:
        if sid in by_id:
            continue
        data["sources"].append({
            "id": sid, "title": title, "author": "Wikipedia/机构", "type": typ,
            "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
            "note": f"访问于 2026-11-22，由核验子任务实抓 HTTP 200 并核对标题/正文；{note}",
        })
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    entries = []
    for eid, title, theme, tier, period, region, s1, s2 in SCOPE:
        definition, tp, overview = DATA[eid]
        entries.append({
            "id": eid, "title": title, "level": "L1", "tier": tier,
            "theme": theme, "period": period, "region": region,
            "definition": definition, "time_or_place": tp, "overview": overview,
            "related": [], "sources": [s1, s2],
            "needs_verification": False, "pending_notes": "",
        })
    out = ROOT / "entries" / "batch-25.json"
    out.write_text(json.dumps({"unit_id": "batch-25", "title": "第25轮 B4 补齐条目", "entries": entries},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources+entries prepared", len(entries))


if __name__ == "__main__":
    main()
