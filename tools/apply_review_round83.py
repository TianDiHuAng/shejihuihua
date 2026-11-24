"""第83轮：sasanian-architecture 补具名实例(泰西封塔克·基斯拉) 并升级（Wikipedia + Art in Context）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "sasanian-architecture":
                e["sections"]["实例"] = "名称：塔克·基斯拉（Taq Kasra，又称“霍斯劳之伊万” Iwan of Khosrow），位于泰西封（Ctesiphon，今伊拉克）；属萨珊时期（约 3–6 世纪）。是萨珊筒拱伊万（iwan，一面敞开的拱顶大厅）的现存巨构。此处仅列名称、地点与年代信息，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "萨珊建筑以筒拱、穹顶与伊万为特征由 Wikipedia 与 Art in Context 双源直证；塔克·基斯拉（泰西封）为萨珊伊万巨构，名称/地点经 Wikipedia 直证、伊万与泰西封经 Art in Context 佐证；精确建造年代学界有出入，标约 3–6 世纪。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round83 applied")


if __name__ == "__main__":
    main()
