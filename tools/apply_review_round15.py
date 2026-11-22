"""第15轮复核应用：4 条待核实收窄（不写死有冲突的数值）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("ccdy-liufa-kao", "六法考 — 中国文化报", "http://nepaper.ccdy.cn/html/2014-06/01/content_127126.htm", "中国文化报", "官方机构", "论述六法原书名与版本流传（异说并列）"),
    ("zjol-liufa-version", "六法版本流传 — 浙江日报", "https://msb.zjol.com.cn/html/2019-01/26/content_3738864.htm", "浙江日报", "官方机构", "论述《古画品录》版本源流"),
    ("cntv-jiejing", "借景 — 央视网", "https://www.cntv.cn/lm/278/41/37393.html", "中央广播电视总台", "官方机构", "记载拙政园借景北寺塔的视点与视线走廊"),
    ("thepaper-perspective", "布鲁内莱斯基透视实验 — 澎湃新闻", "https://www.thepaper.cn/newsDetail_forward_29119227", "澎湃新闻", "官方机构", "记载洗礼堂镜子演示、约1413年、布鲁内莱斯基（引牛津 Martin Kemp）"),
    ("nelson-atkins-perspective", "Gaining Perspective — 纳尔逊-阿特金斯艺术博物馆", "https://nelson-atkins.org/gates/gaining-perspective.html", "纳尔逊-阿特金斯艺术博物馆", "官方机构", "记载 early 1400s、洗礼堂、Brunelleschi"),
    ("thepaper-jingan", "静安寺下沉广场 — 澎湃新闻", "https://m.thepaper.cn/newsDetail_forward_2786200", "澎湃新闻", "官方机构", "记载静安寺下沉广场卢济威主持城市设计、1999年落成"),
    ("jfdaily-jingan", "静安寺下沉广场 — 解放日报·上观新闻", "https://www.jfdaily.com/wx/detail.do?id=1010081", "解放日报", "官方机构", "记载静安寺广场设计者与1999年落成"),
]


def main():
    path = ROOT / "data" / "sources.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    added = []
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        data["sources"].append({
            "id": sid, "title": title, "author": author, "type": typ,
            "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
            "note": f"访问于 2026-11-22，由核验子任务实抓 HTTP 200 并核对正文；canonical 直连待复；{note}",
        })
        added.append(sid)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            k = e["id"]
            if k == "six-principles":
                e["sections"]["待核实"] = "《古画品录》原书名在《古今画品》与《画品》之间存在异说，版本源流亦有分歧（见并列来源）；成书确切年代为约数。"
                for r in ["ccdy-liufa-kao", "zjol-liufa-version"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["pending_notes"] = "原书名与版本流传说解不一、成书年代为约数，均待文献学考订；正文并列异说、不写死。"
            elif k == "borrowed-scenery":
                e["sections"]["待核实"] = "借景北寺塔的视点与方向已双源；园外距离记载不一（约 1.5–1.7 公里），具体数值待核实。"
                if "cntv-jiejing" not in e["sources"]:
                    e["sources"].append("cntv-jiejing")
                e["pending_notes"] = "借景北寺塔的园外距离记载不一（约 1.5–1.7 公里），具体数值待核实；正文并列、不写死。"
            elif k == "perspective":
                e["sections"]["实例"] = "名称：佛罗伦萨洗礼堂透视演示（自圣母百花大教堂门内视点）；地点：意大利佛罗伦萨；设计者：菲利波·布鲁内莱斯基（相关记载）；年份：约 1413 年（约数）。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "演示的确切年份为约数（约 1413 年），不同文献表述略有出入，待补充原始文献。"
                for r in ["thepaper-perspective", "nelson-atkins-perspective"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["pending_notes"] = "透视演示的确切年份为约数（约 1413 年），待补充原始文献。"
            elif k == "sunken-courtyard":
                e["sections"]["实例"] = "名称：静安寺下沉广场（上海）／苏州古典园林庭院（苏州）；地点：中国上海／苏州；设计者：静安寺广场由卢济威主持城市设计、顾如珍负责建筑工程（苏州庭院设计者待核实）；年份：静安寺广场 1999 年落成（苏州庭院年代待核实）。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "苏州古典园林庭院的设计者与年代、以及两类实例的历史原型对应关系待核实。"
                for r in ["thepaper-jingan", "jfdaily-jingan"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["pending_notes"] = "苏州古典园林庭院的设计者与年代、历史原型对应关系待核实。"
            else:
                continue
            e["needs_verification"] = True
            ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added", added)


if __name__ == "__main__":
    main()
