"""第88轮：rule-of-odds / stippling 概念双直接源、类型性实例，升级 nv=false。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
V = {
 "rule-of-odds": dict(
   inst="名称：奇数主体的构图（类型性，构图法则不归于单一作品）；以画面中排布 3 或 5 个主体、避免呆板的偶数对称。此处仅列说明，不复制图像。"),
 "stippling": dict(
   inst="名称：点描明暗练习（类型性，技法不归于单一作品）；以细点疏密由亮到暗逐层加密，塑造明暗与体积。此处仅列说明，不复制图像。"),
}


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] in V:
                e["sections"]["实例"] = V[e["id"]]["inst"]
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round88 applied")


if __name__ == "__main__":
    main()
