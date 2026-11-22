"""第22轮复核应用：level-change（Rolex学习中心）、winding-path（拙政园）双源升级。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("epfl-rolex", "Rolex Learning Center — EPFL", "https://www.epfl.ch/campus/visitors/?p=198", "EPFL", "官方机构", "记载劳力士学习中心无障碍、缓坡处理各类高差"),
    ("archdaily-rolex", "Rolex Learning Center / SANAA — ArchDaily", "https://www.archdaily.com/53536/rolex-learning-center-sanaa", "ArchDaily", "学术著作", "记载洛桑、SANAA、2010 年、可达性"),
    ("mur-qutong", "江南园林的曲径通幽 — 《现代城市研究》", "http://mur.cn/journals/2002/2/MUR-2002-2-bec33483a84dbb51ab3121f2c4d9f4e6.html", "现代城市研究", "学术著作", "论述曲径通幽手法并以拙政园为例"),
    ("zhuangshi-qutong", "曲径通幽的入园模式 — 《装饰》2023(9)", "https://search.napstic.cn/literature/periodical/010zhuangshi202309018", "装饰", "学术著作", "论述曲径通幽的入园模式"),
    ("thepaper-zhuozheng", "拙政园 — 澎湃新闻", "https://www.thepaper.cn/newsDetail_forward_24383367", "澎湃新闻", "官方机构", "记述拙政园历史与造景"),
    ("taiwan-zhuozheng", "拙政园 — 中国台湾网", "https://www.taiwan.cn/zt/jlzt/jstwz/jxjs/jxjs/200911/t20091111_1138694.htm", "中国台湾网", "官方机构", "记述拙政园王献臣建园、文徵明参与设计"),
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
            if k == "level-change":
                e["sections"]["实例"] = "名称：劳力士学习中心（Rolex Learning Center）；地点：瑞士洛桑（EPFL 校园）；设计者：SANAA（妹岛和世与西泽立卫）；年份：2010 年。以缓坡与连续起伏地面处理高差，全馆无障碍可达。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "暂无已知待核实项。"
                for r in ["epfl-rolex", "archdaily-rolex"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
            elif k == "winding-path":
                e["sections"]["实例"] = "名称：拙政园；地点：中国苏州；设计者：园主王献臣（相传文徵明参与设计蓝图）；年份：始建于明正德四年（1509 年）。以曲折游径与折廊延长游程、变换视角。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                e["sections"]["待核实"] = "设计者“相传文徵明”为传说性表述，正文已注明；具体游径段落的设计与年代待考订。"
                for r in ["mur-qutong", "zhuangshi-qutong", "thepaper-zhuozheng", "suzhou-ylj-zhuozhengyuan", "taiwan-zhuozheng"]:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                e["needs_verification"] = True
                e["pending_notes"] = "文徵明参与设计为相传之说；游径具体段落设计与年代待考订。"
                ch = True
            else:
                continue
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("sources added", added)


if __name__ == "__main__":
    main()
