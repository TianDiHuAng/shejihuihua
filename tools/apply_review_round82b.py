"""第82b轮：修正 classical-order（柱数误写/原理去重）与 religious-architecture（去单源设计者）。"""
import json
import ssl
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36'}


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    for s in data["sources"]:
        if s["id"] == "db-parthenon":
            s["note"] = "帕特农神庙为多立克柱式建筑的高峰；其八柱面（octastyle，前8柱、侧17柱）突破传统六柱式"
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "classical-order":
                # 帕特农为八柱式（octastyle），前8柱、侧17柱；非6/13
                e["sections"]["实例"] = "名称：帕特农神庙（Parthenon）；地点：希腊雅典卫城；设计者：伊克蒂诺与卡利克拉底（Iktinos and Callicrates）；年份：公元前 447–432 年。作为多立克柱式的典范，它采用八柱面（octastyle，正面 8 柱、侧翼 17 柱），突破传统的六柱式。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                # 重写原理，避免与 ancient-greek 逐字重合
                e["sections"]["原理"] = "古典柱式把柱头、柱身、檐部与基座按固定柱径倍数关系组配：多立克柱身粗壮、装饰简省，爱奥尼与科林斯渐趋修长华饰。柱式的比例秩序使立面统一并传达庄重。"
                e["sections"]["典型手法与适用条件"] = "按所选柱式的柱径确定柱高、柱距与檐部比例；多立克用于庄重庙宇，爱奥尼、科林斯用于更华丽的立面。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "religious-architecture":
                # 去掉单源设计者，保留双源核心（穹顶创新/年代/地点）
                e["sections"]["实例"] = "名称：圣索菲亚大教堂（Hagia Sophia）；地点：土耳其伊斯坦布尔；年份：公元 532–537 年。以巨大穹顶统摄的礼拜空间，是宗教建筑穹顶的重要创新。此处仅列名称、地点与年份信息，不复制图像。"
                e["sections"]["待核实"] = "圣索菲亚穹顶为重大创新、年代（532–537）与地点由 Wikipedia 与 Designing Buildings 双源直证。"
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round82b applied")


if __name__ == "__main__":
    main()
