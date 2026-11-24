"""第94轮：three-point-perspective 双独立源(db-quaglio+wp-quaglio)均述三点透视发明/1818，升级 nv=false。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "three-point-perspective":
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["needs_verification"] = False
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round94 applied")


if __name__ == "__main__":
    main()
