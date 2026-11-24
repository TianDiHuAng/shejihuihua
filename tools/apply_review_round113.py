"""第1轮(新目标)：核心条目 L3 试点——为 value/balance 增加第二张分析示意图，level→L3。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VALUE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 400" role="img" aria-label="明度阶梯示意">
<rect width="760" height="400" fill="var(--panel, #f7f7f7)"/>
<text x="30" y="40" font-size="20" fill="var(--fg, #222)">明度阶梯：由黑到白的连续过渡（示意图，非施工图）</text>
<g>
""" + "".join(
    f'<rect x="{60+i*60}" y="90" width="60" height="120" fill="rgb({int(255*(i)/9)},{int(255*(i)/9)},{int(255*(i)/9)})" stroke="var(--line,#888)"/>'
    for i in range(10)
) + """
</g>
<text x="60" y="245" font-size="14" fill="var(--muted,#555)">低明度（暗）</text>
<text x="600" y="245" font-size="14" fill="var(--muted,#555)">高明度（亮）</text>
<text x="60" y="300" font-size="15" fill="var(--fg,#222)">作用：明度拉开层次可区分形体、建立空间前后与重点；层次过窄则画面扁平。</text>
<text x="60" y="330" font-size="15" fill="var(--fg,#222)">读法：相邻两格为一档，观察主体与背景应至少相差数档以形成对比。</text>
</svg>"""

BALANCE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 400" role="img" aria-label="对称与非对称均衡对比示意">
<rect width="760" height="400" fill="var(--panel, #f7f7f7)"/>
<text x="30" y="36" font-size="20" fill="var(--fg, #222)">对称均衡 vs 非对称均衡（示意图，非施工图）</text>
<line x1="380" y1="60" x2="380" y2="360" stroke="var(--line,#bbb)" stroke-dasharray="6 6"/>
<text x="90" y="70" font-size="16" fill="var(--fg,#222)">对称（天平式）</text>
<line x1="200" y1="120" x2="200" y2="300" stroke="var(--fg,#444)"/>
<polygon points="200,120 140,300 260,300" fill="var(--accent,#7aa7c7)" opacity="0.8"/>
<polygon points="200,120 260,300 140,300" fill="var(--accent,#7aa7c7)" opacity="0.4"/>
<circle cx="200" cy="200" r="26" fill="var(--fg,#444)" opacity="0.5"/>
<text x="110" y="340" font-size="13" fill="var(--muted,#555)">两侧等量、镜像，稳定庄重</text>
<text x="470" y="70" font-size="16" fill="var(--fg,#222)">非对称（杠杆式）</text>
<line x1="470" y1="190" x2="700" y2="190" stroke="var(--fg,#444)"/>
<circle cx="585" cy="190" r="6" fill="var(--fg,#444)"/>
<rect x="500" y="120" width="60" height="140" fill="var(--accent,#7aa7c7)" opacity="0.8"/>
<circle cx="680" cy="150" r="34" fill="var(--accent,#c78a7a)" opacity="0.7"/>
<text x="500" y="340" font-size="13" fill="var(--muted,#555)">大小、位置不同但视觉重量相抵，活泼而不失衡</text>
</svg>"""


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "value" and e.get("level") != "L3":
                e.setdefault("svg", []).append(VALUE_SVG)
                e["level"] = "L3"
                ch = True
            elif e["id"] == "balance" and e.get("level") != "L3":
                e.setdefault("svg", []).append(BALANCE_SVG)
                e["level"] = "L3"
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("L3 pilot applied: value, balance")


if __name__ == "__main__":
    main()
