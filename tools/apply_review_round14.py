"""第14轮复核应用：4 条实例升级 + liubai 补源。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("columbia-jaanus-rikubo", "rikuhō (六法) — JAANUS", "https://projects.mcah.columbia.edu/jaanus/node/1757", "哥伦比亚大学 JAANUS", "学术著作", "记载六法由南朝齐谢赫在《古画品录》提出，约公元500年"),
    ("ebsco-xie-he", "Xie He — EBSCO Research Starters", "https://www.ebsco.com/es/node/158137", "EBSCO", "学术著作", "记载谢赫属南朝齐 479–502 CE，著《古画品录》"),
    ("nyc-lpc-guggenheim", "Solomon R. Guggenheim Museum — NYC Landmarks Preservation Commission", "http://s-media.nyc.gov/agencies/lpc/lp/1774.pdf", "纽约市地标保护委员会", "官方机构", "记载古根海姆美术馆由 Frank Lloyd Wright 设计，1956–59 建成，含连续螺旋坡道"),
    ("guggenheim-visitor-guide", "Guggenheim Visitor Guide", "https://www.guggenheim.org/wp-content/uploads/2025/07/250715_VE_VisitorGuide_v02.pdf", "Solomon R. Guggenheim Foundation", "官方机构", "记载螺旋坡道与 1959 年开放、Frank Lloyd Wright"),
    ("suzhou-ylj-zhuozhengyuan", "拙政园 — 苏州市园林和绿化管理局", "https://ylj.suzhou.gov.cn/szsylj/sjyc/201905/c1df393edc8745abb20e8a9bd5525782.shtml", "苏州市园林和绿化管理局", "官方机构", "记载拙政园始建于明正德四年(1509)，王献臣请文徵明参与设计，以水为主"),
    ("peopleapp-zhuozhengyuan", "拙政园：天下园林之母 — 人民日报人民号", "https://www.peopleapp.com/rmharticle/30016473527", "人民日报", "官方机构", "记载 1509 年、王献臣、文征明参与设计、以水为心"),
    ("shanghai-lhsr-jiejing", "借景——拙政园的精妙所在 — 上海市绿化和市容管理局", "https://lhsr.sh.gov.cn/jnylwh/20200824/7cc5e5102094470b94a8f771808c1f53.html", "上海市绿化和市容管理局", "官方机构", "记载拙政园借景园外报恩寺北寺塔"),
    ("cnr-liubai", "留白，留的是什么？ — 央广网", "https://www.cnr.cn/ent/zx/20201228/t20201228_525375797.shtml", "中央广播电视总台", "官方机构", "专门讨论中国画留白手法"),
    ("rmrb-liubai", "在留白中邂逅万千气象 — 人民日报", "https://paper.people.com.cn/rmrb/pc/content/202611/01/content_30188752.html", "人民日报", "官方机构", "专门讨论留白的审美与空间营造"),
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
                e["sections"]["实例"] = "名称：《古画品录》；作者：谢赫；年份：约公元 500 年（南朝齐，479–502 年）。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "《古画品录》各版本流传与辑佚的文献学细节待补充专门来源。"
                for r in ["columbia-jaanus-rikubo", "ebsco-xie-he"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "《古画品录》版本流传等文献学细节待补充独立来源。"
            elif k == "circulation":
                e["sections"]["实例"] = "名称：所罗门·R·古根海姆美术馆；地点：美国纽约；设计者：弗兰克·劳埃德·赖特（Frank Lloyd Wright）；年份：1956–1959 年（1959 年开放）。连续螺旋坡道组织参观动线。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项。"
                for r in ["nyc-lpc-guggenheim", "guggenheim-visitor-guide"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
            elif k == "water-management":
                e["sections"]["实例"] = "名称：拙政园水面；地点：中国苏州；设计者：王献臣（文徵明参与设计）；年份：明正德四年（1509 年）。以水为中心组织全园。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项。"
                for r in ["suzhou-ylj-zhuozhengyuan", "peopleapp-zhuozhengyuan"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
            elif k == "borrowed-scenery":
                e["sections"]["实例"] = "名称：拙政园借景园外报恩寺北寺塔；地点：中国苏州；设计者：王献臣（文徵明参与设计）；年份：明正德四年（1509 年）。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "“借景北寺塔”的具体视线距离与观景视点目前为单源记载，待补充独立来源。"
                for r in ["shanghai-lhsr-jiejing", "suzhou-ylj-zhuozhengyuan", "peopleapp-zhuozhengyuan"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "借景北寺塔的视线距离与视点细节为单源，待补充独立来源。"
            elif k == "liubai":
                for r in ["cnr-liubai", "rmrb-liubai"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
            else:
                continue
            ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added", added)


if __name__ == "__main__":
    main()
