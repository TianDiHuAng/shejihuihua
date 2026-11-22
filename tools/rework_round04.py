"""第4轮抽检返工：修正 light-well 与 opposed-scenery 的引用与声明。"""
import json
import re
import html
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = "https://en.wikipedia.org/wiki/Light_well"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"}


def main():
    with urllib.request.urlopen(urllib.request.Request(URL, headers=UA), timeout=25) as resp:
        body = resp.read().decode("utf-8", "replace")
        status = resp.status
    title = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", body, re.S).group(1))
    if status != 200 or "Lightwell" not in title:
        raise ValueError(f"source verification failed: {status} {title}")
    src_path = ROOT / "data" / "sources.json"
    data = json.loads(src_path.read_text(encoding="utf-8"))
    if not any(s["id"] == "wp-lightwell" for s in data["sources"]):
        data["sources"].append({
            "id": "wp-lightwell", "title": "Lightwell", "author": "Wikipedia contributors",
            "type": "权威百科", "year": None, "url": URL, "url2": None,
            "verified": True, "link_ok": True,
            "note": "标题与机构已核对，HTTP 200，访问于 2026-11-22；支撑采光与一般通风；百科条目无固定出版年",
        })
    src_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for path in (ROOT / "entries").glob("*.json"):
        doc = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for entry in doc.get("entries", []):
            eid = entry["id"]
            if eid == "light-well":
                entry["definition"] = "天井是以狭长开口把天然光引入建筑深处的院落式空间。"
                entry["overview"] = "天井通过屋面开口改善内部采光与空气流动，是多种传统民居的空间原型。"
                sec = entry.setdefault("sections", {})
                sec["原理"] = "天井以屋面开口把天然光引入进深较大的建筑，并借助开口促进空气流动；热压机制的具体贡献待核实。"
                sec["典型手法与适用条件"] = "开口位置、比例与朝向决定光线分布，需结合当地气候与使用需求；构造做法因地域而异。"
                sec["待核实"] = "热压通风机制与具体实例的实测数据待补充专门来源。"
                entry["sources"] = ["wp-lightwell", "wp-courtyard"]
                entry["needs_verification"] = True
                entry["pending_notes"] = "Lightwell 来源支持采光与一般通风，但未给出热压机制；具体实例数据待补充。"
                changed = True
            elif eid == "opposed-scenery":
                sec = entry.setdefault("sections", {})
                sec["原理"] = "对景把路径或视线的终点处理为可识别的景物，使空间获得明确的方向感。"
                sec["典型手法与适用条件"] = "在轴线尽端、廊道转折或院落出口设置山石、建筑或树木；具体术语与历史实例的对应关系待核实。"
                entry["needs_verification"] = True
                entry["pending_notes"] = "中国园林条目未直接支撑“对景”的核心机制；需补充专门来源，实例的设计者与年份亦待核实。"
                changed = True
            elif eid == "deconstructivism":
                entry["pending_notes"] = "Guggenheim Abu Dhabi 的实际开馆状态待后续核对；来源页面已明确设计者为 Frank Gehry。"
                changed = True
        if changed:
            path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("reworked light-well, opposed-scenery, deconstructivism")


if __name__ == "__main__":
    main()
