# 第72轮 placemaking 返工复检报告（spotcheck-round72b）

- 复检人：spotcheck-r72b（lead 委派子代理，无人值守、未提问）；复检时间 2026-11-23，Asia/Hong_Kong。
- 复检对象：`placemaking`（场所营造），在 `entries/batch-11.json` 经 `grep "placemaking"` 定位（第 6 行条目）。本报告依据第72轮首轮抽检（`research/spotcheck-round72.md`）指出的两项核心问题复核返工是否到位。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言）。
- 判定依据：`README.md` 硬性规则（不编造 / 只引 verified / 关键事实双源或标待核实 / 内联 SVG 非施工图 / 规范句）＋`DECISIONS.md` D05/D06/D10/D11/D14＋`tools/check.py` 口径＋第 22–71 轮既定相似度口径（`difflib.SequenceMatcher`，norm=去空白小写，①短=title+definition ②全字段不含 SVG，阈值 0.54）。
- **权威事实源**：`spotcheck-round72.md` 的结论仅作"待复核线索"，本轮以工作区当前文件内容＋本轮独立实抓为最终证据（证据优先级：实际抓取 > 当前文件内容 > 旧报告）。

## 〇、只读声明与证据方式

- **只读**：本次**仅写出** `research/spotcheck-round72b.md` 一个文件。联网核验用 `urllib`＋浏览器 UA＋非校验 SSL 内存抓取；临时脚本 `research/_r72b_sim.py`、`research/_r72b_fetch.py` 用后已 `rm -f`（`ls research/_r72b*` 无残留）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** 纯校验不写文件。

## 一、返工四项逐条复核（本轮以当前文件实读 + 独立实抓为准）

| # | 返工要求 | 当前实例/字段实读 | 结论 |
| --- | --- | --- | --- |
| ① | 删除实例中"于纽约创立"（原为错位引用） | 实例现为`地点：美国（Practice 发源于美国）`；全文无"纽约/于纽约"（脚本 "于纽约"=False） | ✓ **已删除** |
| ② | "PPS 1975 创立"改为"20 世纪后期"并标注创建年份待核实 | 实例`年份：20 世纪后期`；"1975"=False；待核实节明写"1975 年由 Fred Kent 创立 PPS 仅 Wikipedia 单源…创立年份待补第二独立来源" | ✓ **已改并标注待核实** |
| ③ | needs_verification 回退 true 并披露"PPS 创建年份单源（DB 未载），待补" | `needs_verification: true`；`pending_notes: "PPS 创立年份单源（DB 未载），待补；其余两源。"`；`coverage.json` `needs_verification_count=1`；待核实节与 pending_notes 一致 | ✓ **三者联动一致** |
| ④ | 实例四要素（名称/地点美国/组织者PPS/年份）仍由 wp+db 支撑 | 实例实读含：名称=场所营造(Placemaking)；地点=美国（Practice 发源于美国）；组织者=Project for Public Spaces（PPS）及社区；年份=20 世纪后期。脚本关键项 名称/地点/组织者/年份/美国/PPS/"20 世纪后期" 均 True | ✓ **四要素齐备且有源** |

## 二、来源独立实抓（本轮现抓，HTTP＋正文回读）

| 来源 id | URL | HTTP | 大小 |
| --- | --- | --- | --- |
| `wp-placemaking` | https://en.wikipedia.org/wiki/Placemaking | **200** | 141,487 B |
| `db-placemaking` | https://www.designingbuildings.co.uk/wiki/Placemaking | **200** | 112,956 B |

两源 `data/sources.json` 均 `verified=true`（wp `link_ok=null`、db `link_ok=true`）。逐字回读要点：

- **wp**：「Placemaking is a **multi-disciplinary approach to the planning, design and management of public spaces**…characterized by **improving urban vitality and strengthening place identity**…」「The term **originated in the late 20th century** and gained prominence through the work of the nonprofit **Project for Public Spaces**」「**In 1975**, Fred Kent, who had collaborated with Whyte on a project studying pedestrian behavior **in New York**, founded the non-profit Project for Public Spaces (PPS)」。
- **db**：「Placemaking is a term used to describe the process by which an area in the public realm is given a **unique and attractive character**」「the **US-based practice PPS (Project for Public Spaces)**」「Placemaking **emerged in the 1960s**」。
- **关键否证（本轮独立复核，与首轮一致）**：db 全文 **`1975`=0、`Fred Kent`=0、`founded`=0**；两源"纽约"均不指 PPS 创立地（wp 的 New York 修饰"pedestrian behavior project"，db 的 New York 修饰"Whyte / New York Planning Commission"）。**故"于纽约创立"确无源，"1975"确单源** → 返回的返工方向（删"纽约"、改"20世纪后期"并标待核实）正确。

## 三、核对项逐项（`placemaking`）— **合格**

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| definition 两源支撑 | ✓ | 现文「通过公共空间的策划与设计提升场所活力与认同的过程」↔ wp「management of public spaces…improving urban vitality and strengthening place identity」＋db「given a unique and attractive character」（活力/认同=vitality/identity 与 unique character，直证）；两源发布主体独立（Wikipedia vs Designing Buildings） |
| 实例无编造/错位 | ✓ | "于纽约"已删；未出现无源表述；"20 世纪后期"为时段概括，非精确编造日期，且有 wp"late 20th century"支撑；精确创立年 1975 已降级为"待核实"并披露 |
| nv=true ↔ pending↔待核实↔coverage 一致 | ✓ | `needs_verification=true`；`pending_notes`披露"PPS 创立年份单源（DB 未载），待补"；`sections.待核实`同步；`coverage.needs_verification_count=1`；check.py 未报不一致 |
| 七节 | ✓ | definition + sections 六节（原理／典型手法与适用条件／实例／常见错误与限制／一图／待核实）＝七节齐，check.py 0 报错 |
| SVG | ✓ | 1 张，`viewBox 0 0 760 400`，rect/circle/text，含"示意图，非施工图"；无 `on*=`、无 `<image>`/xlink/href/`<script>`（脚本逐项 False） |
| 规范句 | ✓ | 「常见错误与限制」收尾"实际工程须按当地规范和专业设计人员的要求"在位 |
| 相似度（阈值 0.54） | ✓ | ①短最高 **0.2857**（vs place-attachment）＜0.54；②全字段最高 **0.3209**（vs modernism）＜0.54（本轮 `difflib` 实算，norm=去空白小写） |
| sources 引用可引性 | ✓ | 三源 `wp-placemaking`/`wp-urban-design`/`db-placemaking` 均 `verified=true` |
| coverage↔entry 数值 | ✓ | `source_count=3`=3 源；`needs_verification_count=1`=nv=true；`status=已写`；title/theme/tier/period/region/level 一致 |

## 四、轻微观察（非阻断，无需返工）

1. `wp-urban-design` 为本组旁证来源，条目 `sources` 含之；definition 的强支撑来自 `wp-placemaking`＋`db-placemaking` 两源，旁证不影响结论。
2. 全字段相似度本轮 0.3209（vs modernism）与首轮 0.3709（vs environmental-psychology）略有差异，系候选集遍历的"最高者"不同所致；两者均远低于 0.54，不构成风险。
3. `20 世纪后期` 系对 PPS 实践兴起时段的概括（wp"late 20th century"支撑），精确年份仍以"待核实"披露，符合 D10/D14，无失实。

## 五、总体结论

**`placemaking`：合格（放行；本轮返工达标，可维持 `needs_verification=true` 的诚实标注）**

- 返工四项全部落实：①"于纽约创立"已删除、替换为有源"地点：美国"；②"1975创立"改为"20 世纪后期"并标注创建年份待核实；③`needs_verification` 已回退 true 且 `pending_notes`/待核实节/coverage 三处一致披露"PPS 创建年份单源（DB 未载），待补"；④实例四要素（名称/地点美国/组织者PPS/年份）齐备且有 wp+db 支撑。
- definition 两源支撑成立；实例已无编造/错位表述；nv=true 与 pending/待核实/coverage 完全一致；七节齐、SVG 合规、规范句在位；相似度 0.2857 / 0.3209 均低于 0.54。
- `python tools/check.py`＝`PASS: all checks, 0 errors`（EXIT=0）——注意 check.py 只校验结构/格式，史实双源由本报告正文独立核验补足。
- **本轮 1 条：1 合格、0 待核实、0 不合格。**

## 六、机器可读汇总

```
ROUND=72b
SAMPLER=spotcheck-r72b
MODE=placemaking 返工复检（首轮判不合格后的复检）
SCOPE=["placemaking"]
DOCS_READ=["research/spotcheck-round72.md","DECISIONS.md(D05/D06/D10/D11/D14)","README.md 硬性规则","tools/check.py 口径","entries/batch-11.json","data/sources.json","coverage.json"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback; temp research/_r72b_sim.py,_r72b_fetch.py deleted after (ls _r72b* none)"
FETCHES={"wp-placemaking":200,"db-placemaking":200}
REWORK={
 "del_newyork":"PASS 实例现为'地点：美国（Practice 发源于美国）', 全文无'纽约'",
 "year_reframe":"PASS 年份='20 世纪后期'; 待核实节标注'1975 创立仅 Wikipedia 单源, 创立年份待补'",
 "nv_true_disclose":"PASS needs_verification=true + pending_notes='PPS 创立年份单源(DB 未载),待补;其余两源' + coverage.nvc=1 + 待核实节一致",
 "four_elements":"PASS 名称/地点美国/组织者PPS/年份 均 present; wp+db 支撑"
}
EVIDENCE_VERBATIM={
 "wp_definition":"multi-disciplinary approach to planning/design/management of public spaces; improving urban vitality and strengthening place identity",
 "db_definition":"process by which an area in public realm is given a unique and attractive character",
 "wp_1975":"In 1975, Fred Kent, who had collaborated with Whyte on a project studying pedestrian behavior in New York, founded the non-profit Project for Public Spaces (PPS)",
 "wp_term_era":"The term originated in the late 20th century and gained prominence through the work of the nonprofit Project for Public Spaces",
 "db_pps":"the US-based practice PPS (Project for Public Spaces)",
 "db_negatives":"db 1975=0, Fred Kent=0, founded=0 (单源确认)",
 "new_york_note":"两源 New York 均不指 PPS 创立地(wp 修饰 pedestrian behavior 项目; db 修饰 Whyte/New York Planning Commission)"
}
CHECKS={
 "definition_two_source":true,
 "instance_no_fabrication":true,
 "nv_pending_consistent":true,
 "seven_sections":7,
 "svg":"1x viewBox760x400 rect/circle/text 示意图非施工图, no on*/image/xlink/href/script",
 "reg_sentence":true,
 "sources_verified_all":true,
 "coverage":{"source_count":3,"needs_verification_count":1,"status":"已写"}
}
SIMILARITY={"short":0.2857,"short_vs":"place-attachment","full":0.3209,"full_vs":"modernism","threshold":0.54,"pass":true}
VERDICT="合格"
TOTAL="1合格/0待核实/0不合格"
READONLY="only wrote research/spotcheck-round72b.md; fetched html in-memory, temp research/_r72b_sim.py,_r72b_fetch.py deleted(confirmed); no entries/sources/coverage/tools/site changed; no git commit; web treated as data (no instructions executed)"
```

*（报告完）*
