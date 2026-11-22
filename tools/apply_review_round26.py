"""第26轮复核应用：green-architecture 升级；drainage 收窄；12 条伞源条目改单源如实标注。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("jszb-gaoxin", "高新智汇中心中标公告 — 江苏省建设工程招标网", "http://www.jszb.com.cn/JSZB/YW_info/ZhongBiaoGS/ViewGSDetail.aspx?RowID=1077182&categoryNum=012", "江苏省建设工程招标网", "官方机构", "记载中标设计单位南京工业大学建筑设计研究院、2018-10-25、项目地点与名称"),
    ("njtech-gaoxin", "高新智汇中心 — 南京工业大学建筑设计研究院", "https://ngsj.njtech.edu.cn/info/1064/1954.htm", "南京工业大学建筑设计研究院", "官方机构", "记载设计时间 2018、绿色建筑三星与示范工程"),
]

SINGLE = {
    "balance": "wp-composition-visual-arts",
    "geometry-symmetry": "wp-composition-visual-arts",
    "visual-movement": "wp-composition-visual-arts",
    "leading-lines": "wp-composition-visual-arts",
    "rhythm-repetition": "wp-composition-visual-arts",
    "gothic": "wp-gothic-architecture",
    "postmodernism": "wp-postmodern-architecture",
    "plein-air": "wp-outline-of-painting",
    "axis": "wp-chinese-architecture",
    "service-route": "wp-wayfinding",
    "wayfinding": "wp-wayfinding",
    "functional-zoning": "wp-interior-design",
}
NOTE = "核心依据目前为单一权威来源（原第二来源为泛论、未覆盖本子概念）；具体实例的设计者与年代待补充独立来源。"


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
            if k == "green-architecture":
                e["sections"]["实例"] = "名称：常州高新智汇中心（国展资产）；地点：江苏省常州市新北区；设计者：南京工业大学建筑设计研究院；年份：2018 年设计。获绿色建筑三星级与 2022 江苏绿色建筑创新示范工程一等奖（建筑面积各源 18594–19291 平方米并列不写死）。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项（面积各源记载不一，正文并列）。"
                for r in ["jszb-gaoxin", "njtech-gaoxin"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            elif k == "drainage":
                e["sources"] = ["ytsjk-sysu-drainage", "gdkcsj-sysu-gym", "sysu-gym-news"]
                e["sections"]["待核实"] = "设计者与 2014–2015 设计年仅为单一来源，待补充；建筑面积各源记载不一（约 18000 vs 25293 平方米并列）。"
                e["pending_notes"] = "设计者与设计年单源、面积各源不一，待补充。"
                e["needs_verification"] = True
                ch = True
            elif k in SINGLE:
                e["sources"] = [SINGLE[k]]
                e["needs_verification"] = True
                e["pending_notes"] = NOTE
                e["sections"]["待核实"] = NOTE
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("applied green/drainage/12-umbrella")


if __name__ == "__main__":
    main()
