"""第68轮：spatial-sequence 补具名实例并升级（Guggenheim LPC + Visitor Guide PDF 双源）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INST = {
    "spatial-sequence": dict(
        inst="名称：纽约古根海姆博物馆（Solomon R. Guggenheim Museum）螺旋坡道；地点：美国纽约；设计者：弗兰克·劳埃德·赖特（Frank Lloyd Wright）；年份：1959 年开馆。观众沿环绕中庭的连续螺旋坡道盘旋而上观展，形成连续的空间序列。此处仅列名称、地点、设计者与年份信息，不复制图像。",),
}


def main():
    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] in INST and "nyc-lpc-guggenheim" in e["sources"] and "guggenheim-visitor-guide" in e["sources"]:
                e["sections"]["实例"] = INST[e["id"]]["inst"]
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
            print("spatial-sequence upgraded in", p.name)


if __name__ == "__main__":
    main()
