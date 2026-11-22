"""第27轮复核应用：登记 9 个真实第二来源并为对应条目补第二源。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("getty-principles-design", "Principles of Design — J. Paul Getty Museum", "https://www.getty.edu/education/teachers/building_lessons/principles_design.pdf", "J. Paul Getty Museum", "官方机构", "平衡/动势/节奏等设计原则定义"),
    ("getty-balance-pr2", "Balance — Getty Education", "https://www.getty.edu/education/teachers/building_lessons/ufa_balance_pr2.pdf", "J. Paul Getty Museum", "官方机构", "对称与非对称平衡"),
    ("archdaily-postmodernism", "What Is Postmodernism? — ArchDaily", "https://www.archdaily.com/964625/what-is-postmodernism", "ArchDaily", "学术著作", "后现代主义引入历史元素、强调立面"),
    ("forschungsprojekt-pleinair", "Plein Air Painting — Forschungsprojekt Impressionismus", "https://www.forschungsprojekt-impressionismus.de/info.aspx?id=15&lang=en", "科隆博物馆研究项目", "官方机构", "外光写生即户外作画"),
    ("e-architect-boh", "Designing Back-of-House Spaces — e-architect", "https://www.e-architect.com/articles/designing-back-of-house-spaces", "e-architect", "学术著作", "后勤空间、服务通道与货运清洁流线"),
    ("designingbuildings-wayfinding", "Wayfinding — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Wayfinding", "Designing Buildings", "学术著作", "寻路定义：帮助人在建筑/环境中定向"),
    ("designingbuildings-zone", "Zone — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Zone", "Designing Buildings", "学术著作", "分区：为特定功能划分区域"),
    ("tongji-jingan", "上海静安寺广场（综合体）— 同济大学", "https://www.tongji.edu.cn/info/1033/10705.htm", "同济大学", "官方机构", "卢济威、顾如珍等主持静安寺广场项目"),
]

ADD = {
    "balance": "getty-principles-design",
    "visual-movement": "getty-principles-design",
    "rhythm-repetition": "getty-principles-design",
    "geometry-symmetry": "getty-balance-pr2",
    "postmodernism": "archdaily-postmodernism",
    "plein-air": "forschungsprojekt-pleinair",
    "service-route": "e-architect-boh",
    "wayfinding": "designingbuildings-wayfinding",
    "functional-zoning": "designingbuildings-zone",
}
NOTE2 = "核心已补第二独立来源；具体实例的设计者与年代待补充独立来源。"


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
            if k in ADD:
                ref = ADD[k]
                if ref not in e["sources"]:
                    e["sources"].append(ref)
                e["needs_verification"] = True
                e["pending_notes"] = NOTE2
                e["sections"]["待核实"] = NOTE2
                ch = True
            elif k == "sunken-plaza":
                if "tongji-jingan" not in e["sources"]:
                    e["sources"].append("tongji-jingan")
                e["sections"]["待核实"] = "同济大学官网记卢济威、顾如珍等“主持”该项目，澎湃新闻记顾如珍“负责建筑工程”，两说并列不写死；其他实例的设计者与年代待核实。"
                e["pending_notes"] = "顾如珍角色表述不一（主持/负责建筑工程）并列；其他实例待核实。"
                e["needs_verification"] = True
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("added second sources for 9 entries + tongji for sunken-plaza")


if __name__ == "__main__":
    main()
