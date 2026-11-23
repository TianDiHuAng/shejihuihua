"""第80b轮：tints-shades 概念已有直证，实例去具名(改类型性练习)、升级 nv=false，避免与 value 同例重合。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "tints-shades":
                e["sections"]["实例"] = "名称：明度色阶练习（同一色相加白/加黑得到的明度梯度）；地点与作者不适用。以加白得浅色 tint、加黑得深色 shade，排成明度阶梯。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round80b applied")


if __name__ == "__main__":
    main()
