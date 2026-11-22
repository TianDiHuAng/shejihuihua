"""第19轮复核应用：tour-route 升级；drainage/glare 实例补双源（参数仍待核实）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("gdkcsj-sysu-gym", "中山大学珠海校区体育馆 — 广东省工程勘察设计行业协会", "https://www.gdkcsj.com/m/caseInfo.aspx?id=1487", "广东省工程勘察设计行业协会", "官方机构", "记载设计单位北京市建筑设计研究院、2014–2015设计、2017投用"),
    ("sysu-gym-news", "中山大学珠海校区体育馆 — 中山大学新闻网", "https://www.sysu.edu.cn/news/info/2171/587221.htm", "中山大学", "官方机构", "记载体育馆建设与投用信息（转南都）"),
    ("iea-pbc-xining", "Retrofit of office lighting, People's Bank of China Xining — IEA SHC Task 61", "https://ww.iea-shc.org/Data/Sites/1/publications/CN-Peoples-Bank-of-China.pdf", "IEA SHC", "学术著作", "记载西宁中支办公楼照明改造，照度475lx、UGR 8–19"),
    ("elicht-pbc-xining", "中国人民银行西宁中心支行照明改造 — 云知光", "https://www.elicht.com/view/101733.html", "云知光", "官方机构", "记载该办公楼照明改造案例"),
    ("heuvan-pbc-xining", "中国人民银行西宁中心支行照明案例 — 恒亦明", "http://www.heuvan.com/news_details.aspx?id=54", "恒亦明", "官方机构", "记载该办公楼照明案例"),
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
            "note": f"访问于 2026-11-22，由核验子任务实抓 HTTP 200 并核对正文；{note}",
        })
        added.append(sid)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            k = e["id"]
            if k == "tour-route":
                e["sections"]["实例"] = "名称：拙政园；地点：中国苏州（东北街）；设计者：王献臣（文徵明参与设计，据传）；年份：明正德四年（1509 年）；全园分东、中、西三部分逐区展开游线。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项（面积等数据各源记载不一，正文不写死）。"
                for r in ["suzhou-ylj-zhuozhengyuan", "peopleapp-zhuozhengyuan"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            elif k == "drainage":
                e["sections"]["实例"] = "名称：中山大学珠海校区体育馆；地点：中国珠海；设计者：北京市建筑设计研究院股份有限公司；年份：2014–2015 年设计、2017 年投用。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "雨水排放的工程参数（集水坑尺寸、重现期等）待补充专业来源；建筑面积各源记载不一。"
                for r in ["gdkcsj-sysu-gym", "sysu-gym-news"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "雨水排放工程参数待补充专业来源；建筑面积记载不一。"
                ch = True
            elif k == "glare":
                e["sections"]["实例"] = "名称：中国人民银行西宁中心支行综合办公楼；地点：中国西宁；设计者：待核实；年份：约 1990 年代建成，2020 年照明改造。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "照度 475lx 与 UGR 8–19 等数值仅单一来源，待补充独立来源；建筑面积记载不一。"
                for r in ["iea-pbc-xining", "elicht-pbc-xining", "heuvan-pbc-xining"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "照度与 UGR 数值仅单一来源，待补充独立来源；面积记载不一。"
                ch = True
            else:
                continue
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added", added)


if __name__ == "__main__":
    main()
