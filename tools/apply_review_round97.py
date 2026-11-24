"""第97轮：earth-sheltered / exit-sign 清除已过时待核实（正文已无对应无源claim），升级 nv=false。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "earth-sheltered":
                # 原理已聚焦坡地覆土/天窗引光(双源)，移除保温claim；清待核实
                e["definition"] = "覆土建筑指部分墙体或屋顶被土体/植被覆盖、嵌入坡地景观的建筑。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "exit-sign":
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round97 applied")


if __name__ == "__main__":
    main()
