"""第87轮：opposed-scenery / leaked-scenery / korean-architecture 传统/类型性无单设计者，概念多源，升级 nv=false。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
V = {
 "opposed-scenery": dict(
   defn="对景是在游线或视线的端点布置景物，使行进有明确落点、前后呼应的造园手法。",
   ov="对景把远端厅堂、山石或树木定为视觉目标，令游走产生期待与收束；属传统造园经验，多由匠师群体经手、无单一设计者。",
   inst="名称：古典园林的对景布置（类型性，传统造园无单一设计者）；地点：中国江南古典园林。以门洞框取的远处厅堂或山石作视线落点。此处仅列说明，不复制图像。"),
 "leaked-scenery": dict(
   defn="漏景是借漏窗、花墙或稀疏枝叶让景物片段若隐若现的造园手法。",
   ov="漏景不一次揭示全貌，而让景物随步移时断时续地显现，形成含蓄节奏；此类手法为传统经验、无单一设计者。",
   inst="名称：古典园林的漏窗漏景（类型性，传统造园无单一设计者）；地点：中国江南古典园林。透过漏窗花纹隐约得见园景。此处仅列说明，不复制图像。"),
 "korean-architecture": dict(
   defn="韩国传统建筑以木构架承重、温突地面采暖与顺应山势的院落布局，适应四季分明的气候。",
   ov="木构使墙体轻巧、温突把地面变成采暖面、院落采光通风；此类传统民居多由地方匠人集体营建，无单一设计者。",
   inst="名称：韩国传统木构院落民居（韩屋，类型性，无单一设计者）；地点：韩国。以木构架、温突地暖与院落组织生活。此处仅列说明，不复制图像。"),
}


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] in V:
                f = V[e["id"]]
                e["definition"] = f["defn"]
                e["overview"] = f["ov"]
                e["sections"]["实例"] = f["inst"]
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round87 applied")


if __name__ == "__main__":
    main()
