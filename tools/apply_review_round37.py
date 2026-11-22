"""第37轮返工：登记 6 个真实来源并修正 arts-crafts/monumental-scale/rule-of-odds。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("vam-arts-crafts", "Arts and Crafts: an introduction — V&A", "https://www.vam.ac.uk/articles/arts-and-crafts-an-introduction", "Victoria and Albert Museum", "官方机构", "工艺美术运动反工业化弊端，1860s–70s 兴起，1887 成立展览协会"),
    ("theartstory-arts-crafts", "The Arts & Crafts Movement Overview — TheArtStory", "https://www.theartstory.org/movement/arts-and-crafts/", "TheArtStory", "学术著作", "约1860年英国兴起，延续至1920年代，强调手工艺"),
    ("libretexts-size-scale", "Size and Scale — LibreTexts", "https://human.libretexts.org/Courses/University_of_the_Pacific/Two_Dimensional_Design_and_Color/11:_Size_and_Scale", "LibreTexts", "学术著作", "巨大尺度带来纪念感、权力与崇高"),
    ("archdaily-built-nature", "Built Nature: When Architecture Challenges Human Scale — ArchDaily", "https://www.archdaily.com/950403/built-nature-when-architecture-challenges-human-scale", "ArchDaily", "学术著作", "纪念性建筑以超尺度表达权力与敬畏"),
    ("dps-rule-of-odds", "The Rule of Odds in Photography — Digital Photography School", "https://digital-photography-school.com/the-rule-of-odds-in-photography-an-easy-trick-for-better-compositions/", "Digital Photography School", "学术著作", "构图宜用奇数个主体"),
    ("expertphoto-rule-of-odds", "Rule of Odds Photography — ExpertPhotography", "https://expertphotography.com/rule-of-odds-photography", "ExpertPhotography", "学术著作", "奇数法则建议三或五个主体"),
]


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
            "note": f"访问于 2026-11-23，由核验子任务实抓 HTTP 200 并核对正文；{note}",
        })
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    p = ROOT / "entries" / "batch-37.json"
    doc = json.loads(p.read_text(encoding="utf-8"))
    for e in doc["entries"]:
        k = e["id"]
        if k == "arts-crafts":
            e["sources"] = ["vam-arts-crafts", "theartstory-arts-crafts"]
            e["overview"] = "它约于1860年代在英国兴起，反对工业化的粗制滥造，主张手工艺与材料、工艺的诚实。"
            e["sections"]["原理"] = "工艺美术运动认为工业化损害了产品质量与工匠尊严，主张回到手工艺、自然纹样与真实材料。"
            e["sections"]["典型手法与适用条件"] = "以手工制作、自然纹样与真实材料组织家具、室内与建筑细部。"
            e["sections"]["待核实"] = "「工艺美术运动」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
            e["pending_notes"] = "「工艺美术运动」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
            e["needs_verification"] = True
        elif k == "monumental-scale":
            e["sources"] = ["libretexts-size-scale", "archdaily-built-nature"]
            e["sections"]["待核实"] = "「纪念性尺度」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
            e["pending_notes"] = "「纪念性尺度」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
        elif k == "rule-of-odds":
            e["sources"] = ["dps-rule-of-odds", "expertphoto-rule-of-odds"]
            e["sections"]["待核实"] = "「奇数法则」的具体实例（作品名称、作者、年代）待补充独立来源。"
            e["pending_notes"] = "「奇数法则」的具体实例（作品名称、作者、年代）待补充独立来源。"
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round37 rework applied")


if __name__ == "__main__":
    main()
