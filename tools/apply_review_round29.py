"""第29轮复核应用：gothic 补第二源；postmodernism/bauhaus 具名实例；新增 baroque 条目。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"
NEW = [
    ("libretexts-gothic-vault", "7.3: The Vaulted Arch — Humanities LibreTexts", "https://human.libretexts.org/Courses/Gavilan_College/A_World_Perspective_of_Art_Appreciation_(Gustlin_and_Gustlin)_2.0/07:_The_Sacred_Buildings_of_Civilizations_(200_CE__1400_CE)/7.03:_The_Vaulted_Arch", "LibreTexts", "学术著作", "尖拱/肋拱/飞扶壁用于哥特建筑"),
    ("pcad-piazza", "Piazza d'Italia — PCAD (University of Washington)", "https://pcad.lib.washington.edu/building/16410", "PCAD", "学术著作", "Piazza d'Italia，Charles Willard Moore，1978–1979，新奥尔良"),
    ("docomomo-piazza", "Piazza d'Italia — Docomomo US", "https://nocache.docomomo-us.org/register/piazza-d-italia", "Docomomo US", "官方机构", "Charles Moore 后现代主义转向、Piazza d'Italia 1978"),
    ("basilicasanpietro", "Basilica di San Pietro — Fabbrica di San Pietro", "https://www.basilicasanpietro.va/en/san-pietro", "Fabbrica di San Pietro", "官方机构", "1506 奠基；贝尼尼广场 1667 建成"),
    ("turismoroma-sanpietro", "Piazza San Pietro — Turismo Roma", "https://turismoroma.it/en/node/710", "Turismo Roma", "官方机构", "马代尔诺 17 世纪立面、贝尼尼巴洛克广场"),
]
SVG_BAROQUE = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><ellipse cx='380' cy='230' rx='200' ry='70' fill='none' stroke='var(--muted)'/><path d='M 200 230 Q 380 60 560 230' fill='none' stroke='var(--accent)' stroke-width='3'/><line x1='380' y1='90' x2='380' y2='300' stroke='var(--accent)'/><text x='250' y='60' fill='var(--ink)'>曲线立面与圆形广场</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        data["sources"].append({
            "id": sid, "title": title, "author": author, "type": typ,
            "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
            "note": f"访问于 2026-11-22，由核验子任务实抓 HTTP 200 并核对正文；{note}",
        })
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            k = e["id"]
            if k == "gothic":
                if "libretexts-gothic-vault" not in e["sources"]:
                    e["sources"].append("libretexts-gothic-vault")
                e["sections"]["待核实"] = "暂无已知待核实项（实例建筑师佚名；苏利为主教发起者）。"
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            elif k == "postmodernism":
                e["sections"]["实例"] = "名称：意大利广场（Piazza d'Italia）；地点：美国新奥尔良；设计者：查尔斯·威拉德·摩尔（Charles Willard Moore）；年份：1978–1979 年。以历史母题拼贴体现后现代主义。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项。"
                for r in ["pcad-piazza", "docomomo-piazza"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            elif k == "bauhaus":
                e["sections"]["实例"] = "名称：包豪斯德绍校舍（Bauhaus Dessau）；地点：德国德绍-罗斯劳；设计者：瓦尔特·格罗皮乌斯（Walter Gropius）；年份：1925–1926 年（1926-12-04 启用）。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项。"
                for r in ["stiftung-bauhaus-dessau", "archdaily-bauhaus-dessau"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")

    # 新增 baroque 条目
    meta = {r["id"]: r for r in json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))["entries"]}
    bar = {
        "id": "baroque", "title": meta["baroque"]["title"], "level": "L2",
        "tier": meta["baroque"]["tier"], "theme": meta["baroque"]["theme"],
        "period": meta["baroque"]["period"], "region": meta["baroque"]["region"],
        "definition": "巴洛克建筑以动感曲线、戏剧化光影与宏大尺度表达情感与权力。",
        "time_or_place": "文艺复兴至19世纪、欧洲（参见来源）。",
        "overview": "巴洛克打破文艺复兴的静态对称，以椭圆平面、曲面立面和强烈明暗制造运动感。",
        "related": ["renaissance-style", "rococo"],
        "sections": {
            "原理": "以曲线、起伏立面与集中式椭圆平面制造运动与张力，并借强烈明暗与装饰强调中心。",
            "典型手法与适用条件": "用曲面柱廊、穹顶与椭圆广场组织戏剧性空间；适用于教堂、宫殿与城市广场。",
            "实例": "名称：圣彼得大教堂及广场（St. Peter's Basilica）；地点：梵蒂冈/罗马；设计者：布拉曼特、米开朗基罗、马代尔诺（立面）、贝尼尼（广场柱廊）；年份：1506 年奠基，17 世纪立面，广场 1667 年建成。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "装饰过度会喧闹、尺度失衡会压抑；结构与防火须按当地规范校核。" + REG,
            "一图": "见下方示意：曲线立面与圆形广场。",
            "待核实": "该建筑为多建筑师跨时段作品，单一设计者与部分年代不写死；其余细节待核实。",
        },
        "svg": [SVG_BAROQUE],
        "sources": ["wp-baroque-architecture", "basilicasanpietro", "turismoroma-sanpietro"],
        "needs_verification": True,
        "pending_notes": "圣彼得大教堂为多建筑师跨时段作品，单一设计者与部分年代不写死。",
    }
    out = ROOT / "entries" / "batch-29.json"
    data2 = {"unit_id": "batch-29", "title": "第29轮条目", "entries": [bar]}
    if out.exists():
        data2 = json.loads(out.read_text(encoding="utf-8"))
        if not any(x["id"] == "baroque" for x in data2["entries"]):
            data2["entries"].append(bar)
    out.write_text(json.dumps(data2, ensure_ascii=False, indent=2), encoding="utf-8")
    print("applied round29 incl baroque")


if __name__ == "__main__":
    main()
