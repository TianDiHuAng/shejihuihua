"""第38轮返工：登记 6 个真实来源并修正 acoustic/romanticism/korean。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("designingbuildings-acoustics", "Building acoustics — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Building_acoustics", "Designing Buildings", "学术著作", "混响时间、吸声降混响、隔声受质量/刚度/阻尼影响"),
    ("libretexts-room-acoustics", "Anechoic and Reverberation Rooms — Physics LibreTexts", "https://phys.libretexts.org/Bookshelves/Waves_and_Acoustics/Acoustics/03:_Applications_in_Room_Acoustics/3.01:_Anechoic_and_reverberation_rooms", "LibreTexts", "学术著作", "声音在墙面反射往复、吸声材料在宽频带吸声"),
    ("henryford-gothic-revival", "Gothic Revival — The Henry Ford", "https://www.thehenryford.org/collections/explore/articles/detail/articles/2013/10/18/gothic-revival-an-alternative-trend-for-victorian-americans", "The Henry Ford", "官方机构", "18世纪英国哥特复兴与如画浪漫主义"),
    ("libretexts-romanticism", "Romanticism (1780-1850) — Humanities LibreTexts", "https://human.libretexts.org/Courses/Gavilan_College/A_World_Perspective_of_Art_Appreciation_(Gustlin_and_Gustlin)_2.0/11:_The_Industrial_Revolution_(1800_CE__1899_CE)/11.02:_Romanticism_(1780-1850)", "LibreTexts", "学术著作", "浪漫主义反新古典理性、重情感想象与自然崇高"),
    ("koreanet-hanok-madang", "Traditional Korean architecture: madang — Korea.net (KOCIS)", "https://www.korea.net/NewsFocus/HonoraryReporters/view?articleId=241777", "Korea.net / KOCIS", "官方机构", "韩屋以 madang 院落为核心，采光通风与家庭聚集"),
    ("springer-hanok-madang", "Algorithmic Design Paradigm for the Han-ok — Nexus Network Journal", "https://link.springer.com/article/10.1007/s00004-016-0292-x", "Springer", "学术著作", "韩屋 Chae 与 Madang 的空间构成，院落为中心生活空间"),
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

    p = ROOT / "entries" / "batch-38.json"
    doc = json.loads(p.read_text(encoding="utf-8"))
    for e in doc["entries"]:
        k = e["id"]
        if k == "acoustic-environment":
            e["sources"] = ["designingbuildings-acoustics", "libretexts-room-acoustics"]
            e["definition"] = "声环境指空间中的声音条件，包括隔声、吸声与混响。"
            e["overview"] = "混响过长、隔声不足或噪声干扰都会削弱听闻清晰度与舒适。"
            e["sections"]["原理"] = "声音在硬表面反复反射形成混响，混响时间过长则听不清；吸声材料缩短混响，隔声构造阻断声音传播。"
            e["sections"]["典型手法与适用条件"] = "以隔声墙体与楼板阻断传播、以吸声材料控制混响、按用途设定混响时间。"
            e["sections"]["待核实"] = "「声环境」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
            e["pending_notes"] = "「声环境」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
        elif k == "romanticism-style":
            e["sources"] = ["henryford-gothic-revival", "libretexts-romanticism"]
            e["sections"]["原理"] = "浪漫主义以情感、想象与自然崇高对抗新古典的理性秩序，哥特复兴与如画趣味是其建筑表现。"
            e["sections"]["典型手法与适用条件"] = "以哥特母题、如画轮廓与不规则体量唤起历史与自然联想。"
            e["sections"]["待核实"] = "「浪漫主义建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
            e["pending_notes"] = "「浪漫主义建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
        elif k == "korean-architecture":
            e["sources"] = ["wp-korean-architecture", "koreanet-hanok-madang", "springer-hanok-madang"]
            e["definition"] = "韩国传统建筑以木构架、温突地面采暖与院落（마당 madang）组织生活为特征。"
            e["overview"] = "木构承重使墙体轻巧，温突把地面变成采暖面，中央院落采光通风并承载家庭活动。"
            e["sections"]["典型手法与适用条件"] = "以木构架、温突地暖与中央院落（madang）组织居住，室内外以缘侧过渡。"
            e["sections"]["待核实"] = "「韩国建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
            e["pending_notes"] = "「韩国建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round38 rework applied")


if __name__ == "__main__":
    main()
