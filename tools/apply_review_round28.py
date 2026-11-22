"""第28轮复核应用：leading-lines/axis 补第二源；gothic/modernism/color-theory 去骨架化具名实例。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("libretexts-leading-lines", "4.4 Leading Lines — LibreTexts", "https://k12.libretexts.org/Bookshelves/Photography/Book:_Digital_Photography_Basics_(Politzer)/04:_Movement_and_Direction/4.04:_Leading_Lines", "LibreTexts", "学术著作", "专节定义引导线：直/曲/平行/对角引导视线"),
    ("bjaxis-official", "北京中轴线官网", "https://bjaxiscloud.com.cn/", "北京中轴线申遗保护工作办公室", "官方机构", "北京中轴线统领老城格局、对称布局与景观序列"),
    ("getty-cona-notredame", "Notre-Dame de Paris — Getty CONA", "https://www.getty.edu/cona/CONAFullSubject.aspx?subid=700009599", "Getty Research Institute", "官方机构", "巴黎圣母院，Maurice de Sully 发起主持，1163–1250"),
    ("natgeo-notredame", "Notre-Dame de Paris — National Geographic", "https://www.nationalgeographic.com/history/history-magazine/article/notre-dame-de-paris", "National Geographic", "学术著作", "1163 年奠基、Île de la Cité、Maurice de Sully"),
    ("rit-munsell", "Munsell Color Science Laboratory — RIT", "https://www.rit.edu/science/munsell-color-lab", "Rochester Institute of Technology", "官方机构", "Albert H. Munsell 创 Munsell 色彩体系，1905《A Color Notation》，生于波士顿"),
    ("sciencehistory-munsell", "A Colorful Life — Science History Institute", "https://www.sciencehistory.org/stories/magazine/a-colorful-life/", "Science History Institute", "官方机构", "Munsell 1858–1918、波士顿、1905 A Color Notation、hue/value/chroma"),
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
            "note": f"访问于 2026-11-22，由核验子任务实抓 HTTP 200 并核对正文；{note}",
        })
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            k = e["id"]
            if k == "leading-lines":
                if "libretexts-leading-lines" not in e["sources"]:
                    e["sources"].append("libretexts-leading-lines")
                e["sections"]["待核实"] = "核心已补第二独立来源；具体实例的拍摄者与年代待核实。"
                e["pending_notes"] = "核心已双源；具体实例的拍摄者与年代待核实。"
                e["needs_verification"] = True
                ch = True
            elif k == "axis":
                if "bjaxis-official" not in e["sources"]:
                    e["sources"].append("bjaxis-official")
                e["sections"]["待核实"] = "北京中轴线作为具名实例已有官方来源；轴线组织的通用定义以原有来源为主，具体案例的设计者与年代待核实。"
                e["pending_notes"] = "通用定义单源；具名实例（北京中轴线）有官方来源；具体设计者与年代待核实。"
                e["needs_verification"] = True
                ch = True
            elif k == "gothic":
                e["sections"]["实例"] = "名称：巴黎圣母院（Notre-Dame de Paris）；地点：法国巴黎西岱岛（Île de la Cité）；设计者：建筑师佚名，巴黎主教莫里斯·德·苏利（Maurice de Sully）发起并主持；年份：1163 年奠基，主体约至 1250 年。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "哥特风格的核心特征依据单一权威来源；实例（巴黎圣母院）三要素已双源；建筑师佚名。"
                for r in ["getty-cona-notredame", "natgeo-notredame"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "风格核心依据单一权威来源；实例三要素已双源；建筑师佚名。"
                ch = True
            elif k == "modernism":
                e["sections"]["实例"] = "名称：包豪斯德绍校舍（Bauhaus Dessau）；地点：德国德绍-罗斯劳；设计者：瓦尔特·格罗皮乌斯（Walter Gropius）；年份：1925–1926 年（1926-12-04 启用）。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "现代主义风格定义依据单一权威来源；实例（包豪斯德绍校舍）三要素已双源。"
                for r in ["stiftung-bauhaus-dessau", "archdaily-bauhaus-dessau"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "风格定义单源；实例三要素已双源。"
                ch = True
            elif k == "color-theory":
                e["sections"]["实例"] = "名称：蒙塞尔色彩体系（Munsell Color Order System）；地点：美国波士顿；设计者：阿尔伯特·H·蒙塞尔（Albert H. Munsell，1858–1918）；年份：1905 年《A Color Notation》提出。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项。"
                for r in ["rit-munsell", "sciencehistory-munsell"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("applied round28")


if __name__ == "__main__":
    main()
