"""第61轮补充：为剩余共用 SVG 的中国画/色彩条目各绘制专属示意图。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
V = "viewBox='0 0 760 400'"
S = "xmlns='http://www.w3.org/2000/svg'"
CAP = "<text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text>"

SVGS = {
 "bone-method": f"<svg {S} {V}><path d='M 200 300 Q 260 120 380 200 T 560 140' fill='none' stroke='var(--accent)' stroke-width='6'/><path d='M 210 310 Q 270 140 380 215 T 550 155' fill='none' stroke='var(--muted)' stroke-width='2'/><text x='40' y='40' fill='var(--ink)'>中锋提按的笔线骨力</text>{CAP}</svg>",
 "ink-wash": f"<svg {S} {V}><rect x='260' y='120' width='60' height='160' fill='var(--ink)'/><rect x='330' y='120' width='60' height='160' fill='var(--ink)' fill-opacity='0.7'/><rect x='400' y='120' width='60' height='160' fill='var(--ink)' fill-opacity='0.45'/><rect x='470' y='120' width='60' height='160' fill='var(--ink)' fill-opacity='0.25'/><text x='40' y='40' fill='var(--ink)'>焦—浓—重—淡—清</text>{CAP}</svg>",
 "cunfa": f"<svg {S} {V}><path d='M 180 300 Q 240 160 320 250 T 520 180' fill='none' stroke='var(--accent)' stroke-width='3'/><g stroke='var(--muted)'><path d='M 260 200 Q 270 240 250 280'/><path d='M 300 190 Q 310 230 290 270'/><path d='M 340 200 Q 350 240 330 280'/></g><text x='40' y='40' fill='var(--ink)'>顺山势的皴笔</text>{CAP}</svg>",
 "gongbi": f"<svg {S} {V}><path d='M 300 260 Q 380 120 460 260' fill='none' stroke='var(--accent)' stroke-width='2'/><path d='M 320 260 Q 380 160 440 260' fill='none' stroke='var(--muted)' stroke-width='2'/><path d='M 340 260 Q 380 200 420 260' fill='none' stroke='var(--muted)' stroke-width='2'/><text x='40' y='40' fill='var(--ink)'>勾线后层层罩染</text>{CAP}</svg>",
 "landscape-painting": f"<svg {S} {V}><path d='M 120 320 L 260 160 L 380 280 L 520 140 L 660 320 Z' fill='none' stroke='var(--accent)'/><line x1='100' y1='320' x2='680' y2='320' stroke='var(--muted)'/><text x='40' y='40' fill='var(--ink)'>高远—深远—平远</text>{CAP}</svg>",
 "transmission-copy": f"<svg {S} {V}><rect x='200' y='140' width='150' height='180' fill='none' stroke='var(--accent)'/><rect x='410' y='140' width='150' height='180' fill='none' stroke='var(--muted)'/><path d='M 350 230 L 410 230' stroke='var(--muted)' stroke-width='3'/><text x='40' y='40' fill='var(--ink)'>原作—临摹（对临/背临）</text>{CAP}</svg>",
 "xu-shi": f"<svg {S} {V}><rect x='180' y='130' width='180' height='170' fill='var(--ink)' fill-opacity='0.55'/><rect x='400' y='130' width='180' height='170' fill='none' stroke='var(--muted)' stroke-dasharray='6 6'/><text x='40' y='40' fill='var(--ink)'>实处（浓墨）—虚处（留白）</text>{CAP}</svg>",
 "color-scheme": f"<svg {S} {V}><rect x='180' y='150' width='180' height='120' fill='var(--accent)'/><rect x='360' y='150' width='100' height='120' fill='var(--accent)' fill-opacity='0.5'/><rect x='460' y='150' width='60' height='120' fill='var(--muted)'/><text x='40' y='40' fill='var(--ink)'>主色—辅色—点缀（面积比）</text>{CAP}</svg>",
 "color-symbolism": f"<svg {S} {V}><circle cx='280' cy='200' r='40' fill='var(--accent)'/><circle cx='380' cy='200' r='40' fill='var(--panel)' stroke='var(--line)'/><circle cx='480' cy='200' r='40' fill='var(--muted)'/><text x='40' y='40' fill='var(--ink)'>色彩—文化联想</text>{CAP}</svg>",
}


def main():
    n = 0
    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] in SVGS:
                e["svg"] = [SVGS[e["id"]]]
                ch = True
                n += 1
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("extra unique svgs applied", n)


if __name__ == "__main__":
    main()
