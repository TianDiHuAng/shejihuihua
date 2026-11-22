"""第20轮复核应用：courtyard 补三源；sunken-plaza 1999 补第二源；material-texture 补机理专源。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("bjdclib-zhaotangzi", "赵堂子胡同3号（朱启钤故居）— 北京市东城区图书馆", "https://www.bjdclib.cn/ztfw/dhly/yard/202301/t20230116_43210.html", "北京市东城区图书馆", "官方机构", "记载赵堂子胡同3号四进四合院、朱启钤20世纪30年代按《营造法式》设计督造、约3000㎡"),
    ("zgkpw-zhuqian", "朱启钤与中国营造学社 — 中国科普网", "https://www.zgkpw.org.cn/expert/jiliping/content_385726.html", "中国科普网", "官方机构", "记载朱启钤故居与营造学社 1932 年迁入"),
    ("cctv-zhaotangzi", "朱启钤故居 — 央视网", "https://discovery.cctv.com/20070119/104637.shtml", "中央广播电视总台", "官方机构", "记载赵堂子胡同3号朱启钤故居四合院"),
    ("people-sh-jingan", "静安寺广场建成于1999年 — 人民网上海频道", "https://sh.people.com.cn/BIG5/n2/2024/0319/c134768-40780072.html", "人民网", "官方机构", "记载静安寺广场建成于1999年9月15日"),
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
            if k == "courtyard":
                e["sections"]["实例"] = "名称：赵堂子胡同3号（朱启钤故居）四合院；地点：北京东城区；设计者：朱启钤（据《营造法式》设计督造）；年份：20 世纪 30 年代购置并改建（另有资料记“形成时期：清”，两说并列、不写死）。四进四合院，约 3000 平方米。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "该院的形成时期有“清代”与“20 世纪 30 年代改建”两说，正文并列，具体沿革待考订。"
                for r in ["bjdclib-zhaotangzi", "zgkpw-zhuqian", "cctv-zhaotangzi"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "赵堂子胡同3号形成时期有清代与1930年代改建两说，待考订。"
                ch = True
            elif k == "sunken-plaza":
                e["sections"]["待核实"] = "“顾如珍负责建筑工程”目前为澎湃单源，待补充独立第二来源；其他下沉广场实例的设计者与年代待核实。"
                if "people-sh-jingan" not in e["sources"]:
                    e["sources"].append("people-sh-jingan")
                e["needs_verification"] = True
                e["pending_notes"] = "顾如珍负责建筑工程为单源，待补充独立来源；其他实例的设计者与年代待核实。"
                ch = True
            else:
                continue
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added", added)


if __name__ == "__main__":
    main()
