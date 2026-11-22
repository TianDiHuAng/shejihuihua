"""B4 读者问题清单：四类读者各 20 问，检查站内条目是否可直接回答。"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

QUESTIONS = {
    "初学者": [
        ("什么是透视法？", "perspective"), ("一点透视怎么画？", "one-point-perspective"),
        ("什么是构图法则？", "composition"), ("三分法是什么？", "rule-of-thirds"),
        ("色相和明度有什么区别？", "hue"), ("互补色怎么搭配？", "complementary-colors"),
        ("什么是明暗法？", "chiaroscuro"), ("中国画六法是哪六条？", "six-principles"),
        ("留白是什么意思？", "liubai"), ("什么是气韵生动？", "qi-yun"),
        ("哥特建筑有什么特点？", "gothic"), ("文艺复兴建筑追求什么？", "renaissance-style"),
        ("园林借景是什么？", "borrowed-scenery"), ("曲径为什么让园林更有趣？", "winding-path"),
        ("动线设计管什么？", "circulation"), ("下沉庭院如何排水？", "drainage"),
        ("自然采光怎么引入室内？", "daylighting"), ("什么是人体尺度？", "human-scale"),
        ("室内外如何过渡？", "interior-exterior-transition"), ("空间序列是什么？", "spatial-sequence"),
    ],
    "学生": [
        ("线性透视与空气透视如何互补？", "aerial-perspective"),
        ("散点透视与焦点透视差别在哪？", "east-west-perspective-compare"),
        ("图底关系如何建立？", "figure-ground"),
        ("负空间在构图中起什么作用？", "negative-space"),
        ("色彩和谐有哪些方案？", "color-harmony"),
        ("冷暖色如何影响空间感受？", "warm-cool"),
        ("六法中经营位置指什么？", "composition-placement"),
        ("意境如何生成？", "yijing"),
        ("比例与尺度如何区分？", "proportion"),
        ("轴线在空间中如何组织？", "axis"),
        ("哥特结构为何能开大窗？", "gothic"),
        ("包豪斯为何强调功能？", "bauhaus"),
        ("现代主义反对什么？", "modernism"),
        ("中国园林的借景与框景有何不同？", "framed-scenery"),
        ("游线如何制造悬念？", "tour-route"),
        ("疏散动线与参观动线如何区分？", "evacuation-route"),
        ("下沉广场与下沉庭院差别？", "sunken-plaza"),
        ("热压通风原理是什么？", "stack-ventilation"),
        ("材料质感如何影响空间？", "material-texture"),
        ("可持续建筑关注哪些指标？", "sustainable-architecture"),
    ],
    "爱好者": [
        ("为什么达芬奇作品有空间深度？", "foreshortening"),
        ("伦勃朗光是什么？", "rembrandt"),
        ("暗绘风格如何形成？", "tenebrism"),
        ("为什么中国画不画阴影也成立？", "liubai"),
        ("园林为什么要先抑后扬？", "screened-scenery"),
        ("对景如何成为视线终点？", "opposed-scenery"),
        ("漏景和框景有何区别？", "leaked-scenery"),
        ("为什么古典园林要理水？", "water-management"),
        ("哪些风格属于粗野主义？", "brutalism"),
        ("解构主义为何看起来不稳定？", "deconstructivism"),
        ("徽派建筑有哪些特征？", "huizhou-style"),
        ("天井在民居中起什么作用？", "light-well"),
        ("为什么穹顶让人感到崇高？", "byzantine"),
        ("希腊柱式如何表达秩序？", "ancient-greek"),
        ("广场如何形成城市客厅？", "plaza"),
        ("中庭如何改善采光？", "atrium-architecture"),
        ("为什么老建筑会返潮？", "damp-proofing"),
        ("玻璃幕墙为何产生眩光？", "glare"),
        ("乡土材料为何有地域感？", "vernacular-material"),
        ("普利兹克奖与中国建筑有什么关系？", "chinese-architecture-style"),
    ],
    "从业者": [
        ("屋面雨水如何组织？", "drainage"),
        ("下沉空间防潮构造注意什么？", "damp-proofing"),
        ("高差处如何做安全防护？", "safety-guarding"),
        ("无障碍路径如何避开台阶？", "sunken-accessibility"),
        ("疏散标识如何布置？", "exit-sign"),
        ("人员密集场所动线如何避免瓶颈？", "evacuation-route"),
        ("采光系数如何估算？", "daylight-factor"),
        ("眩光如何控制？", "glare"),
        ("自然通风与机械通风如何混合？", "mixed-mode-ventilation"),
        ("需求控制通风适用条件？", "demand-controlled-ventilation"),
        ("热舒适如何评价？", "thermal-comfort"),
        ("材料耐久性如何选择？", "material-durability"),
        ("透明材料的构造限制？", "transparent-material"),
        ("通用设计与无障碍如何区分？", "universal-design"),
        ("功能分区如何支持运营？", "functional-zoning"),
        ("服务动线如何避开公众流线？", "service-route"),
        ("门厅如何承担过渡与安检？", "vestibule"),
        ("灰空间在气候适应中有何价值？", "gray-space"),
        ("绿色建筑评价关注什么？", "green-architecture"),
        ("参数化设计如何辅助空间组织？", "parametric-architecture"),
    ],
}


def main():
    parser = argparse.ArgumentParser(description="读者问题缺口发现")
    parser.add_argument("--round", type=int, default=4)
    args = parser.parse_args()
    round_no = args.round
    coverage = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
    scope_ids = {r["id"] for r in coverage["entries"]}
    written = set()
    for path in sorted((ROOT / "entries").glob("*.json")):
        for e in json.loads(path.read_text(encoding="utf-8")).get("entries", []):
            written.add(e["id"])
    lines = ["# B4 读者问题清单 — 第 3 轮", "", "四类读者各 20 问；标注对应条目是否已在 scope / 已写。未写不等于缺失，只表示当前无直接答案。", ""]
    gaps = []
    for group, items in QUESTIONS.items():
        lines += [f"## {group}", "", "| 问题 | 对应条目 | scope | 已写 |", "| --- | --- | --- | --- |"]
        for question, eid in items:
            in_scope, is_written = eid in scope_ids, eid in written
            lines.append(f"| {question} | {eid} | {'是' if in_scope else '否'} | {'是' if is_written else '否'} |")
            if not is_written:
                gaps.append((group, question, eid))
        lines.append("")
    lines += [f"## 缺口汇总", "", f"- 站内暂时无法直接回答的问题：{len(gaps)} / 80。", ""]
    lines += [f"- {g}：{q}（需 {e}）" for g, q, e in gaps[:30]]
    out = ROOT / "research" / f"reader_questions-round{round_no:02d}.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"reader questions: 80 total, {len(gaps)} unanswered")


if __name__ == "__main__":
    main()
