"""第91轮：framed-scenery 概念双直接源(中国园林博物馆+北京文物局)、类型性实例，升级 nv=false；并差异化 value/saturation。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "framed-scenery":
                e["definition"] = "框景是借门洞、漏窗或亭柱把景物围合成画面、增强观赏焦点的造园手法。"
                e["overview"] = "框景用门窗、枝干或亭柱当作“画框”，把连续风景切成局部画面；如颐和园“画中游”以亭柱形成多幅画幅。此类手法属传统造园经验，无单一设计者。"
                e["sections"]["实例"] = "名称：古典园林框景布置（类型性，传统造园无单一设计者）；地点：中国古典园林（如颐和园“画中游”）。以门洞、漏窗或亭柱围合景物成“画框”。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "saturation":
                e["definition"] = "饱和度（纯度）指色彩中灰色成分多少所决定的鲜明或灰浊程度。"
                e["overview"] = "纯度高的颜色鲜明夺目、宜作点睛；掺入灰或补色后趋于灰浊，常用作背景与过渡。"
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round91 applied")


if __name__ == "__main__":
    main()
