"""第61轮：为 6 条共用 SVG 的光影条目各绘制专属示意图。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SVGS = {
 # 投影：物体遮挡光线在承接面留下暗影
 "cast-shadow": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='120' y1='320' x2='660' y2='320' stroke='var(--ink)' stroke-width='2'/><circle cx='240' cy='110' r='28' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='262' y1='132' x2='480' y2='320' stroke='var(--muted)' stroke-dasharray='6 5'/><ellipse cx='500' cy='315' rx='90' ry='14' fill='var(--muted)' fill-opacity='0.4'/><text x='40' y='40' fill='var(--ink)'>物体—光线—投影</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
 # 高光：光滑表面反射光源的亮点
 "highlight": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><ellipse cx='380' cy='230' rx='150' ry='110' fill='var(--panel)' stroke='var(--line)'/><circle cx='330' cy='180' r='16' fill='var(--accent)'/><text x='40' y='40' fill='var(--ink)'>凸起处的高光点</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
 # 反光：暗部受环境反射光的较亮区
 "reflected-light": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='180' y='120' width='200' height='200' fill='var(--muted)' fill-opacity='0.5'/><rect x='160' y='330' width='420' height='20' fill='var(--accent-soft)' stroke='var(--accent)'/><path d='M 400 330 Q 380 250 380 200' stroke='var(--muted)' stroke-dasharray='5 5' fill='none'/><text x='40' y='40' fill='var(--ink)'>暗部靠环境一侧的反光</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
 # 明暗交界线：受光转背光的最暗带
 "core-shadow": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='240' y='130' width='220' height='160' rx='6' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='400' y='130' width='60' height='160' fill='var(--ink)' fill-opacity='0.35'/><text x='40' y='40' fill='var(--ink)'>受光—交界线—暗部</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
 # 正面光：光源与视线同向
 "front-light": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='380' cy='90' r='26' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='320' y='180' width='120' height='140' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='380' y1='120' x2='380' y2='178' stroke='var(--accent)' stroke-width='3'/><text x='40' y='40' fill='var(--ink)'>光源与视线同向（正面）</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
 # 顶光：光源自正上方
 "top-light": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='380' cy='60' r='24' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='380' y1='84' x2='380' y2='180' stroke='var(--accent)' stroke-width='3'/><ellipse cx='380' cy='250' rx='100' ry='70' fill='var(--panel)' stroke='var(--line)'/><ellipse cx='380' cy='300' rx='100' ry='16' fill='var(--ink)' fill-opacity='0.25'/><text x='40' y='40' fill='var(--ink)'>光源自上而下</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>",
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
    print("unique svgs applied", n)


if __name__ == "__main__":
    main()
