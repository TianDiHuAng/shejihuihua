"""第6轮抽检返工：差异化 stack-ventilation，修正 related 与 pending 一致性。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STACK_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<line x1='380' y1='50' x2='380' y2='350' stroke='var(--line)'/>"
    "<rect x='60' y='90' width='280' height='220' fill='none' stroke='var(--muted)'/>"
    "<line x1='90' y1='200' x2='320' y2='200' stroke='var(--muted)' stroke-width='2'/>"
    "<text x='100' y='130' fill='var(--ink)'>风压（对比）</text>"
    "<rect x='420' y='90' width='280' height='220' fill='none' stroke='var(--accent)'/>"
    "<line x1='460' y1='280' x2='460' y2='120' stroke='var(--accent)' stroke-width='3'/>"
    "<line x1='650' y1='120' x2='650' y2='280' stroke='var(--muted)' stroke-width='2'/>"
    "<text x='470' y='130' fill='var(--ink)'>热压（本条）</text>"
    "<text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"
)


def main():
    for path in (ROOT / "entries").glob("*.json"):
        doc = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for entry in doc.get("entries", []):
            eid = entry["id"]
            if eid == "stack-ventilation":
                entry["overview"] = "与风压通风不同，热压通风在外部风较弱时仍可依靠室内外温差工作，常与风压补风配合。"
                sec = entry.setdefault("sections", {})
                sec["原理"] = "室内外空气密度差造成压力差：暖空气上升并从高位开口排出，冷空气从低位补入。该机制由浮力驱动，与风压驱动有本质区别。"
                sec["典型手法与适用条件"] = "设置具有足够高差的进排风口、通风竖井或中庭；适用于内外温差明显、外部风资源不稳定的条件。"
                sec["实例"] = "名称：通风竖井式公共建筑；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。"
                sec["常见错误与限制"] = "进排风口高差不足或被遮挡会中断热压流；冬季过度通风会增加热损失。开口尺寸与消防安全须专门校核。实际工程须按当地规范和专业设计人员的要求。"
                sec["一图"] = "见下方对比示意：左为风压、右为热压；本条聚焦热压的浮力驱动。"
                sec["待核实"] = "竖井式实例的通风实测数据待核实。"
                entry["svg"] = [STACK_SVG]
                entry["related"] = ["natural-ventilation"]
                entry["needs_verification"] = True
                entry["pending_notes"] = "热压通风实例的通风实测数据待补充独立来源。"
                changed = True
            elif eid == "color-harmony":
                entry["related"] = ["color-theory"]
                entry["pending_notes"] = "面积比例与整体感等经验性表述待补充直接来源；实例的设计者与年份待核实。"
                changed = True
            elif eid == "axis":
                entry["related"] = ["symmetry-layout"]
                changed = True
        if changed:
            path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("reworked stack-ventilation, color-harmony, axis")


if __name__ == "__main__":
    main()
