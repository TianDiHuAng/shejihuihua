"""第93轮：early-islamic-architecture 补 artincontext-islamic-architecture 第二直接源(方形平面+hypostyle), 升级 nv=false。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "early-islamic-architecture":
                if "artincontext-islamic-architecture" not in e["sources"]:
                    e["sources"].append("artincontext-islamic-architecture")
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round93 applied")


if __name__ == "__main__":
    main()
