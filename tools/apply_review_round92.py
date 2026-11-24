"""第92轮：mexican-baroque 概念双直接源(NSB+DB Churrigueresque)、类型性子风格，升级 nv=false。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "mexican-baroque":
                e["definition"] = "墨西哥巴洛克（新西班牙巴洛克）是新西班牙（今墨西哥）在殖民时期发展出的巴洛克建筑与艺术，装饰繁复、色彩浓烈，典型子风格为 Churrigueresque。"
                e["overview"] = "它把欧洲巴洛克与本土工艺结合，以密集的灰泥雕刻与强烈色彩装饰教堂；作为地区子风格，不归于单一设计者。"
                e["sections"]["实例"] = "名称：新西班牙巴洛克教堂（类型性，地区子风格不归于单一设计者）；地点：墨西哥；以繁复立面与 Churrigueresque 装饰为特征。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round92 applied")


if __name__ == "__main__":
    main()
