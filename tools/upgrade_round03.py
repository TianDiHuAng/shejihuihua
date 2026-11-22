"""第3轮：将 5 个核心条目从 L1 升级到 L2（七节结构 + 自绘 SVG）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGULATION = "实际工程须按当地规范和专业设计人员的要求"

SIX_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<rect x='30' y='30' width='700' height='340' fill='none' stroke='var(--line)'/>"
    "<circle cx='380' cy='200' r='70' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<text x='345' y='195' fill='var(--ink)'>六法</text>"
    "<text x='335' y='220' fill='var(--muted)'>品评框架</text>"
    "<rect x='90' y='65' width='150' height='46' fill='none' stroke='var(--muted)'/><text x='105' y='95' fill='var(--ink)'>气韵生动</text>"
    "<rect x='520' y='65' width='150' height='46' fill='none' stroke='var(--muted)'/><text x='535' y='95' fill='var(--ink)'>骨法用笔</text>"
    "<rect x='90' y='290' width='150' height='46' fill='none' stroke='var(--muted)'/><text x='105' y='320' fill='var(--ink)'>应物象形</text>"
    "<rect x='520' y='290' width='150' height='46' fill='none' stroke='var(--muted)'/><text x='535' y='320' fill='var(--ink)'>随类赋彩</text>"
    "<text x='250' y='160' fill='var(--muted)'>经营位置</text><text x='470' y='160' fill='var(--muted)'>传移模写</text>"
    "<text x='265' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
)
BORROW_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<line x1='60' y1='330' x2='700' y2='330' stroke='var(--ink)' stroke-width='3'/>"
    "<rect x='160' y='170' width='24' height='160' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<rect x='330' y='210' width='18' height='120' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<polyline points='520,250 560,190 600,250 640,170 680,250' fill='none' stroke='var(--muted)' stroke-width='2'/>"
    "<line x1='210' y1='230' x2='520' y2='230' stroke='var(--accent)' stroke-width='2'/>"
    "<polygon points='512,224 526,230 512,236' fill='var(--accent)'/>"
    "<text x='95' y='210' fill='var(--ink)'>园内视点</text><text x='360' y='195' fill='var(--ink)'>洞口 / 漏窗</text>"
    "<text x='545' y='140' fill='var(--ink)'>园外山影</text><text x='280' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
)
CIRCULATION_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<rect x='40' y='60' width='680' height='280' fill='none' stroke='var(--line)'/>"
    "<circle cx='120' cy='200' r='18' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<circle cx='380' cy='200' r='18' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<circle cx='640' cy='200' r='18' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<line x1='140' y1='200' x2='360' y2='200' stroke='var(--muted)' stroke-width='3'/>"
    "<line x1='400' y1='200' x2='620' y2='200' stroke='var(--muted)' stroke-width='3'/>"
    "<line x1='380' y1='220' x2='380' y2='300' stroke='var(--muted)' stroke-width='2'/>"
    "<text x='90' y='245' fill='var(--ink)'>入口</text><text x='350' y='170' fill='var(--ink)'>节点</text>"
    "<text x='610' y='245' fill='var(--ink)'>出口</text><text x='390' y='290' fill='var(--ink)'>支线</text>"
    "<text x='280' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
)
DAYLIGHT_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<line x1='80' y1='100' x2='680' y2='100' stroke='var(--ink)' stroke-width='3'/>"
    "<line x1='80' y1='330' x2='680' y2='330' stroke='var(--ink)' stroke-width='3'/>"
    "<rect x='240' y='100' width='16' height='130' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<line x1='260' y1='130' x2='520' y2='290' stroke='var(--accent)' stroke-width='2'/>"
    "<line x1='260' y1='170' x2='470' y2='320' stroke='var(--accent)' stroke-width='2'/>"
    "<text x='180' y='150' fill='var(--ink)'>侧窗</text><text x='500' y='270' fill='var(--ink)'>工作面</text>"
    "<text x='280' y='70' fill='var(--ink)'>光线方向与室内进深</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
)
VENT_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'>"
    "<rect x='160' y='90' width='440' height='250' fill='none' stroke='var(--line)'/>"
    "<rect x='160' y='280' width='40' height='30' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<rect x='560' y='100' width='40' height='30' fill='var(--accent-soft)' stroke='var(--accent)'/>"
    "<line x1='220' y1='295' x2='400' y2='295' stroke='var(--accent)' stroke-width='2'/>"
    "<line x1='400' y1='250' x2='400' y2='130' stroke='var(--accent)' stroke-width='2'/>"
    "<line x1='400' y1='130' x2='570' y2='115' stroke='var(--accent)' stroke-width='2'/>"
    "<text x='200' y='340' fill='var(--ink)'>低位进风</text><text x='560' y='80' fill='var(--ink)'>高位排风</text>"
    "<text x='300' y='220' fill='var(--muted)'>热空气上升</text><text x='280' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>"
)

UPGRADES = {
    "six-principles": {
        "level": "L2",
        "sections": {
            "原理": "六法把绘画视为相互关联的系统：精神气韵、用笔力度、物象形态、色彩类别、位置经营与传承临摹共同决定作品品质。",
            "典型手法与适用条件": "品评时先看整体气韵，再逐一检查用笔、象形、赋彩与经营位置；创作与临摹则把传移模写作为学习路径。",
            "实例": "名称：谢赫《古画品录》相关体系；地点：古代中国；设计者：不适用；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "把六法理解为六个孤立技巧会丢失整体品评意图；以形似作为唯一标准会忽略气韵。画面尺幅与展示距离影响观看判断。" + REGULATION,
            "一图": "见下方六法关系示意图，仅表达框架关系。",
            "待核实": "《古画品录》相关体系的确切年代与版本流传待核实。",
        },
        "svg": [SIX_SVG], "needs_verification": True,
        "pending_notes": "谢赫与《古画品录》的确切年代及版本流传待补充独立来源核对。",
    },
    "borrowed-scenery": {
        "level": "L2",
        "sections": {
            "原理": "借景把园外远山、塔影或天光引入园内视线，使有限边界内的空间在感知上延伸。",
            "典型手法与适用条件": "通过洞口、漏窗、高处平台或水面反射取景；适用于园外有值得观看的景物、且视线未被建筑完全遮挡的条件。",
            "实例": "名称：苏州古典园林借景实例；地点：中国苏州；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "把无关景物强行纳入会造成视觉混乱；借景方向受季节与植被变化影响。实际工程须按当地规范和专业设计人员的要求。",
            "一图": "见下方平面示意：园内视点经洞口望向园外山影。",
            "待核实": "具体园林实例的设计者与年份待核实。",
        },
        "svg": [BORROW_SVG], "needs_verification": True,
        "pending_notes": "苏州园林借景具体实例的设计者与年份待补充独立来源。",
    },
    "circulation": {
        "level": "L2",
        "sections": {
            "原理": "动线把行为路径转译为空间序列；节点、分岔与终点共同决定人对空间的理解与效率。",
            "典型手法与适用条件": "主路径串联核心节点，次路径服务辅助功能；在人流密集处增加宽度和辨识度，避免交叉冲突。",
            "实例": "名称：公共文化建筑参观动线；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "流线交叉、标识不清或端部拥堵会削弱体验；疏散路径须单独校核。实际工程须按当地规范和专业设计人员的要求。",
            "一图": "见下方动线网络示意图，表达入口—节点—出口关系。",
            "待核实": "实例的具体名称、地点与设计者待核实。",
        },
        "svg": [CIRCULATION_SVG], "needs_verification": True,
        "pending_notes": "所举公共文化建筑实例的具体信息待补充，暂不作确定性陈述。",
    },
    "daylighting": {
        "level": "L2",
        "sections": {
            "原理": "天然光通过侧窗或天窗进入室内，形成照度梯度与方向性阴影，影响视觉识别与空间情绪。",
            "典型手法与适用条件": "侧窗适用于常规房间，天窗适用于大进深空间；需结合朝向、遮阳与反射面控制眩光和过热。",
            "实例": "名称：博物馆展厅自然采光；地点：待核实；设计者：待核实；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "只追求采光系数而忽略眩光会造成不适；画面尺寸与窗地比需按当地规范校核。实际工程须按当地规范和专业设计人员的要求。",
            "一图": "见下方侧窗采光剖面示意，表达光线方向与设计进深。",
            "待核实": "展厅实例的具体参数与设计者待核实。",
        },
        "svg": [DAYLIGHT_SVG], "needs_verification": True,
        "pending_notes": "博物馆展厅实例的照度数据与设计者待补充独立来源。",
    },
    "natural-ventilation": {
        "level": "L2",
        "sections": {
            "原理": "风压通风依靠室外压差组织穿堂风，热压通风依靠室内外温差使热空气上升并从高位排出。",
            "典型手法与适用条件": "低位进风与高位排风配合中庭或风井；适用于气候温和、外部空气质量可接受的条件，可与机械系统混合。",
            "实例": "名称：传统院落自然通风；地点：待核实；设计者：不适用；年份：待核实。此处仅列名称、地点、设计者与年份信息，不复制图像。",
            "常见错误与限制": "进排风口高差不足会削弱热压效应；开口尺寸与安全、隔声需求需平衡。实际工程须按当地规范和专业设计人员的要求。",
            "一图": "见下方热压通风剖面示意：低位进风、热空气上升、高位排风。",
            "待核实": "具体院落实例的通风实测数据待核实。",
        },
        "svg": [VENT_SVG], "needs_verification": True,
        "pending_notes": "传统院落通风的实测数据与设计者信息待补充独立来源。",
    },
}


def main():
    touched = {}
    for path in sorted((ROOT / "entries").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for entry in data.get("entries", []):
            key = entry["id"]
            if key not in UPGRADES:
                continue
            upgrade = UPGRADES[key]
            entry["level"] = upgrade["level"]
            entry["sections"] = upgrade["sections"]
            entry["svg"] = upgrade["svg"]
            entry["needs_verification"] = upgrade["needs_verification"]
            entry["pending_notes"] = upgrade["pending_notes"]
            touched[key] = path.name
            changed = True
        if changed:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"upgraded={len(touched)} files={sorted(set(touched.values()))}")


if __name__ == "__main__":
    main()
