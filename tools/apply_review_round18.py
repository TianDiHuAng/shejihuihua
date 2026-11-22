"""第18轮复核应用：framed-scenery/natural-ventilation 实例补双源；opposed/leaked 补专门来源。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("peopleapp-kuangjing", "框景之美 — 中国园林博物馆（人民号）", "https://www.peopleapp.com/rmharticle/30028686345", "中国园林博物馆", "官方机构", "定义框景机制与三种形式，并举例拙政园、留园、片石山房"),
    ("beijing-huazhongyou", "颐和园“画中游”景区重开 — 北京市人民政府", "https://www.beijing.gov.cn/renwen/whrl/rdtj/202303/t20230303_2928040.html", "北京市人民政府", "官方机构", "记载颐和园画中游以 8 个亭柱形成画框式取景"),
    ("beijing-wwj-huazhongyou", "颐和园画中游 — 北京市文物局", "https://wwj.beijing.gov.cn/bjww/362760/362770/744072997/index.html", "北京市文物局", "官方机构", "记载画中游始建于清乾隆年间、框成山水画、引李渔“尺幅窗”"),
    ("mdpi-gongwangfu-vent", "Field measurement study of Prince Gong's Mansion — Buildings 2022, 12, 629", "https://mdpi-res.com/d_attachment/buildings/buildings-12-00629/article_deploy/buildings-12-00629.pdf", "MDPI Buildings", "学术著作", "恭王府现场 60 测点实测与 CFD，建于 1780 年"),
    ("scszlxh-cuijiao-vent", "翠郊吴氏大院自然通风实测 — 《制冷与空调》2020 年第34卷第3期", "http://www.scszlxh.com/uploads/a31474cc.pdf", "制冷与空调", "学术著作", "2016 年夏现场实测，院落内平均风速约 0.2–0.3 m/s"),
    ("peopleapp-zaoyuan-2", "造园的艺术手法（二）— 中国园林博物馆（人民号）", "https://www.peopleapp.com/rmharticle/30020551454", "中国园林博物馆", "官方机构", "描述对景机制，并明确出现“漏景/漏窗”术语与定义"),
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
            if k == "framed-scenery":
                e["sections"]["实例"] = "名称：颐和园“画中游”（框景实例）；拙政园芙蓉榭、留园小蓬莱（经典框景）；地点：中国北京／苏州；设计者：不适用（皇家园林与古典园林）；年份：颐和园画中游始建于清乾隆年间（约 1750 年，记载不一），古典园林实例年代待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "古典园林框景实例的具体设计者与年代待核实。"
                for r in ["peopleapp-kuangjing", "beijing-huazhongyou", "beijing-wwj-huazhongyou"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "古典园林框景实例的具体设计者与年代待核实。"
                ch = True
            elif k == "natural-ventilation":
                e["sections"]["实例"] = "名称：恭王府／翠郊吴氏大院；地点：中国北京／福建福鼎；设计者：不适用（传统工匠营建）；年份：恭王府约 1780 年，翠郊吴氏大院年代待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "翠郊吴氏大院的建造年代待核实；两处院落实测条件不同，数据不可直接比较。"
                for r in ["mdpi-gongwangfu-vent", "scszlxh-cuijiao-vent"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "翠郊吴氏大院建造年代待核实；两处实测条件不同不可直接比较。"
                ch = True
            elif k == "opposed-scenery":
                e["sections"]["待核实"] = "对景机制的专门来源已补；具体实例的设计者与年代待核实。"
                if "peopleapp-zaoyuan-2" not in e["sources"]:
                    e["sources"].append("peopleapp-zaoyuan-2")
                e["needs_verification"] = True
                e["pending_notes"] = "对景具体实例的设计者与年代待核实。"
                ch = True
            elif k == "leaked-scenery":
                e["sections"]["待核实"] = "漏景术语与机制已有专门来源；具体实例的设计者与年代待核实。"
                if "peopleapp-zaoyuan-2" not in e["sources"]:
                    e["sources"].append("peopleapp-zaoyuan-2")
                e["needs_verification"] = True
                e["pending_notes"] = "漏景具体实例的设计者与年代待核实。"
                ch = True
            else:
                continue
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added", added)


if __name__ == "__main__":
    main()
