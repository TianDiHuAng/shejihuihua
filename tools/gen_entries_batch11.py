"""第11轮：为已实抓核验通过的 B1 候选写 L1 骨架（只写 verified 列表中的）。"""
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COVERAGE = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
META = {r["id"]: r for r in COVERAGE["entries"]}
ORDER = COVERAGE["entries"]

VERIFY = ROOT / "research" / "verify-round11.txt"
verified = set()
if VERIFY.exists():
    for line in VERIFY.read_text(encoding="utf-8").splitlines():
        if line.startswith("verified="):
            verified = set(ast.literal_eval(line.split("=", 1)[1]))

# id|定义|时间与位置|概述|来源A|来源B
DATA = {
    "placemaking": ("通过公共空间的策划与设计提升场所活力与认同的过程。", "当代、全球（参见来源）。", "场所营造把使用者的日常活动置于设计中心。", "wp-placemaking", "wp-urban-design"),
    "space-syntax": ("用拓扑与几何方法分析空间连接关系及其与行为关联的理论。", "20世纪、全球（参见来源）。", "空间句法把可达性与视线关系转化为可比较的空间指标。", "wp-space-syntax", "wp-urban-morphology"),
    "pattern-language": ("用可复用的设计模式描述建筑与城市空间问题及解法。", "20世纪、全球（参见来源）。", "模式语言把经验性设计知识组织为可组合的条目。", "wp-pattern-language", "wp-a-pattern-language"),
    "form-follows-function": ("建筑形式应由其功能目的决定的命题。", "19–20世纪、全球（参见来源）。", "该命题成为现代主义建筑的重要论证之一。", "wp-form-follows-function", "wp-functionalism-architecture"),
    "functionalism-architecture": ("以功能、结构与材料逻辑为设计出发点的建筑倾向。", "20世纪、全球（参见来源）。", "功能主义反对历史样式复制，强调使用需求与技术理性。", "wp-functionalism-architecture", "wp-form-follows-function"),
    "biophilic-design": ("把自然要素与过程纳入建成环境以支持健康与福祉的设计。", "当代、全球（参见来源）。", "亲生命性设计关注自然光、植物、水与材料质感对人的影响。", "wp-biophilic-design", "wp-evidence-based-design"),
    "defensible-space-theory": ("通过领域感、自然监视与可达性组织空间以降低犯罪机会的理论。", "20世纪、全球（参见来源）。", "该理论把空间布局与社会行为联系起来，影响住区与公共空间设计。", "wp-defensible-space-theory", "wp-cpted"),
}


def related_for(eid):
    pos = next((i for i, r in enumerate(ORDER) if r["id"] == eid), -1)
    for nxt in ORDER[pos + 1:]:
        if nxt["theme"] == META[eid]["theme"]:
            return [nxt["id"]]
    return []


def main():
    verified_local = set()
    for line in VERIFY.read_text(encoding="utf-8").splitlines():
        if line.startswith("verified="):
            import ast as _ast
            verified_local = set(_ast.literal_eval(line.split("=", 1)[1]))
    rows = []
    skipped = []
    for eid, (definition, time_place, overview, s1, s2) in DATA.items():
        if eid not in META:
            skipped.append((eid, "not-in-scope"))
            continue
        if s1 not in verified_local or s2 not in verified_local:
            skipped.append((eid, "source-unverified"))
            continue
        meta = META[eid]
        rows.append({
            "id": eid, "title": meta["title"], "level": "L1", "tier": meta["tier"],
            "theme": meta["theme"], "period": meta["period"], "region": meta["region"],
            "definition": definition, "time_or_place": time_place, "overview": overview,
            "related": related_for(eid), "sources": [s1, s2],
            "needs_verification": False, "pending_notes": "",
        })
    out = ROOT / "entries" / "batch-11.json"
    out.write_text(json.dumps({"unit_id": "batch-11", "title": "第11轮 B1 实抓核验后新增", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"batch-11 written={len(rows)} skipped={skipped}")


if __name__ == "__main__":
    main()
