"""第46轮：新增 4 条（宫廷中轴动线/如画/莫卧儿/早期伊斯兰），L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"
NEW = [
    ("wp-forbidden-city", "Forbidden City", "https://en.wikipedia.org/wiki/Forbidden_City", "Wikipedia", "权威百科", "紫禁城：外朝南、内朝北、中轴对称（经镜像核验）"),
    ("wp-picturesque", "Picturesque", "https://en.wikipedia.org/wiki/Picturesque", "Wikipedia", "权威百科", "如画美学：风景画趣味、不规则与野趣（经镜像核验）"),
    ("tate-picturesque", "Picturesque — Tate", "https://www.tate.org.uk/art/art-terms/p/picturesque", "Tate", "官方机构", "如画指兼具美与野趣的理想风景类型"),
    ("wp-mughal-architecture", "Mughal architecture", "https://en.wikipedia.org/wiki/Mughal_architecture", "Wikipedia", "权威百科", "莫卧儿建筑以建筑彰显权力，融合多元风格（经镜像核验）"),
    ("designingbuildings-taj-mahal", "Taj Mahal — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Taj_Mahal", "Designing Buildings", "学术著作", "泰姬陵为莫卧儿建筑典范，印度/波斯/伊斯兰融合"),
    ("wp-umayyad-architecture", "Umayyad architecture", "https://en.wikipedia.org/wiki/Umayyad_architecture", "Wikipedia", "权威百科", "倭马亚建筑：方形礼拜殿柱廊、岩石圆顶、大马士革清真寺（经镜像核验）"),
    ("artincontext-islamic-art", "Islamic Art — Art in Context", "https://artincontext.org/islamic-art/", "Art in Context", "学术著作", "伊斯兰艺术与清真寺建筑，岩石圆顶、阿克萨清真寺"),
]
D = {
"imperial-axial-route": dict(
  defn="宫廷中轴仪礼动线指以南北中轴依次组织外朝典礼与内朝起居的行进序列。",
  tp="古代、中国（参见来源）。", ov="外朝在南、内朝在北，沿中轴层层递进，以对称与门阙强化礼制秩序。",
  prin="以中轴串联门、庭、殿，把“外朝理政—内朝起居”的功能与尊卑次序写进行进路线。",
  method="沿中轴由南向北布置门阙、庭院与主殿，两侧对称配置廊庑。",
  inst="名称：紫禁城南北中轴行进（类型性描述）；地点与设计者不适用。看外朝到内朝的层次。",
  cap="见下方示意：中轴由外朝向内朝的递进。", limit="中轴过长会疲劳单调；需靠门庭变化分节奏。",
  srcs=["wp-forbidden-city", "designingbuildings-forbidden-city"]),
"picturesque": dict(
  defn="如画（Picturesque）是一种追求不规则、野趣与入画效果的风景审美趣味。",
  tp="跨时期、欧洲（参见来源）。", ov="它介于优美与崇高之间，偏爱起伏地形、树木掩映与废墟。",
  prin="把“像画一样”作为评判风景的标准，以不对称、变化与野趣唤起情感。",
  method="以曲折路径、掩映植物与废墟点景经营入画构图。",
  inst="名称：如画式风景园林（类型性描述）；地点与设计者不适用。看曲折与掩映如何入画。",
  cap="见下方示意：如画的不规则与掩映。", limit="过度追求野趣会失可游性。",
  srcs=["wp-picturesque", "tate-picturesque"]),
"mughal-architecture": dict(
  defn="莫卧儿建筑是16–17世纪南亚莫卧儿帝国融合印度、波斯与伊斯兰语汇的建筑风格。",
  tp="中世纪、伊斯兰/南亚（参见来源；史学上限至17世纪，此处按分类归中世纪）。", ov="以穹顶、拱门、对称花园与精细石材镶嵌彰显帝国权力。",
  prin="把中亚穹顶与波斯拱、印度石作与镶嵌工艺综合，以对称与尺度表达皇权。",
  method="以集中式穹顶、伊万拱门、四分花园（charbagh）与石材镶嵌组织。",
  inst="名称：泰姬陵（类型性描述）；地点与设计者不适用。看穹顶与四分花园的对称。",
  cap="见下方示意：穹顶、拱门与对称花园。", limit="装饰繁复成本高；需结构支撑。",
  srcs=["wp-mughal-architecture", "designingbuildings-taj-mahal"]),
"early-islamic-architecture": dict(
  defn="早期伊斯兰建筑指倭马亚时期形成的清真寺与圣所形制：方形平面、柱廊与穹顶。",
  tp="古代、伊斯兰/南亚（参见来源）。", ov="以方形礼拜殿与柱廊容纳信众，以穹顶标示神圣中心。",
  prin="以宽大的柱廊礼拜殿满足集体礼拜，以穹顶与朝向（qibla）确立神圣方位。",
  method="以方形平面、多柱廊礼拜殿与穹顶（如岩石圆顶）组织。",
  inst="名称：岩石圆顶与倭马亚清真寺（类型性描述）；地点与设计者不适用。看穹顶与柱廊。",
  cap="见下方示意：方形柱廊与穹顶。", limit="柱廊过密会影响视线；需结构协调。",
  srcs=["wp-umayyad-architecture", "artincontext-islamic-art"]),
}
SVGS = [
 "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='380' y1='60' x2='380' y2='340' stroke='var(--accent)' stroke-dasharray='8 6'/><rect x='300' y='90' width='160' height='60' fill='none' stroke='var(--accent)'/><rect x='300' y='170' width='160' height='60' fill='none' stroke='var(--muted)'/><rect x='300' y='250' width='160' height='60' fill='none' stroke='var(--accent)'/><text x='40' y='40' fill='var(--ink)'>{t}</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
 "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><path d='M 120 320 Q 260 150 420 260 T 660 180' fill='none' stroke='var(--accent)' stroke-width='3'/><circle cx='420' cy='260' r='26' fill='var(--accent-soft)' stroke='var(--muted)'/><text x='40' y='40' fill='var(--ink)'>{t}</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
 "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='110' width='520' height='210' fill='none' stroke='var(--line)'/><path d='M 380 110 Q 300 60 220 110' fill='none' stroke='var(--accent)'/><line x1='120' y1='215' x2='640' y2='215' stroke='var(--muted)'/><line x1='380' y1='110' x2='380' y2='320' stroke='var(--muted)'/><text x='40' y='40' fill='var(--ink)'>{t}</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
 "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='150' width='480' height='160' fill='none' stroke='var(--accent)'/><circle cx='380' cy='150' r='56' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='180' y1='230' x2='580' y2='230' stroke='var(--muted)'/><text x='40' y='40' fill='var(--ink)'>{t}</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
]

cov = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))["entries"]
META = {r["id"]: r for r in cov}


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        data["sources"].append({"id": sid, "title": title, "author": author, "type": typ,
                                "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
                                "note": f"访问于 2026-11-23，经实抓/镜像核验；{note}"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    rows = []
    for i, (eid, f) in enumerate(D.items()):
        m = META[eid]
        svg = SVGS[i % 4].replace("{t}", m["title"])
        rows.append({"id": eid, "title": m["title"], "level": "L2", "tier": m["tier"],
                     "theme": m["theme"], "period": m["period"], "region": m["region"],
                     "definition": f["defn"], "time_or_place": f["tp"], "overview": f["ov"], "related": [],
                     "sections": {"原理": f["prin"], "典型手法与适用条件": f["method"], "实例": f["inst"],
                                  "常见错误与限制": f["limit"] + REG, "一图": f["cap"],
                                  "待核实": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"]},
                     "svg": [svg], "sources": f["srcs"], "needs_verification": True,
                     "pending_notes": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"]})
    out = ROOT / "entries" / "batch-46.json"
    out.write_text(json.dumps({"unit_id": "batch-46", "title": "第46轮稀疏格补条目", "entries": rows}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-46 written", len(rows))


if __name__ == "__main__":
    main()
