# 第72轮质量抽检报告（spotcheck-round72）

- 抽检人：spotcheck-r72（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 起，Asia/Hong_Kong。
- 抽检对象（第72轮改动，本轮升级为「已验证」）：`placemaking`（场所营造），在 `entries/batch-11.json` 经 `grep "placemaking"` 定位（第 6 行条目）。
- 本轮引用来源（`data/sources.json`）：
  - `wp-placemaking`（Wikipedia，`https://en.wikipedia.org/wiki/Placemaking`，verified=true，link_ok=null）
  - `wp-urban-design`（旁证，Wikipedia）
  - `db-placemaking`（Designing Buildings，`https://www.designingbuildings.co.uk/wiki/Placemaking`，verified=true，link_ok=true，本轮新增）
- 判定依据：`README.md` 硬性规则（不编造 / 只引 verified / 关键事实双源互证否则标待核实 / 内联 SVG 非施工图 / 规范句 / 40 条上限）＋`DECISIONS.md`（D05/D06/D10/D11/D14）＋`tools/check.py` 校验口径＋第 22–71 轮既定相似度口径（`difflib.SequenceMatcher`，norm=去空白小写，①短=title+definition ②全字段不含 SVG，阈值 0.54）。

## 〇、只读声明与数据稳定性（verification-before-completion：先实抓、先跑、再断言）

- **只读**：本次**仅写出** `research/spotcheck-round72.md` 一个文件。来源核验全程 `python` 内存抓取（`urllib`＋浏览器 UA＋非校验 SSL），两页正文抽取临时落为 `research/_r72_wp.txt`、`research/_r72_db.txt` 及临时脚本 `research/_r72_fetch.py`、`research/_r72_sim.py`，核验后**已删除**（`rm -f` 已确认清除，`ls research/_r72*` 无残留）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** 纯校验不写文件。
- **`data/sources.json` / `coverage.json` 与条目一致性实查：** 条目 `sources` = `["wp-placemaking","wp-urban-design","db-placemaking"]`（3 源）；`coverage.json` 中 `placemaking` 记 `source_count=3`、`needs_verification_count=0`（=条目 nv=false）、`status=已写`，三处一致。
- 工作区含第72轮未提交改动（`placemaking` 条目实例改写、`data/sources.json` 新增 `db-placemaking`、`coverage.json`、生成的 `site/entries/placemaking.html` 等、`tools/apply_review_round72.py`）。本次核验以工作区当前内容为准，未触碰任何数据文件。

## 一、来源实抓结果（HTTP 状态＋正文回读，均为本轮现抓）

| 来源 id | URL | HTTP | 大小 | 回读要点（抽取正文，逐字） |
| --- | --- | --- | --- | --- |
| `wp-placemaking` | https://en.wikipedia.org/wiki/Placemaking | **200** | 141,487 B | 「**Placemaking is a multi-disciplinary approach to the planning, design and management of public spaces that emphasizes community engagement, human-centered design, and the creation of meaningful, functional, and attractive environments.**」「**In 1975, Fred Kent, who had collaborated with Whyte on a project studying pedestrian behavior in New York, founded the non-profit Project for Public Spaces (PPS)**, dedicated to creating public spaces though participatory design and placemaking.」（均逐字） |
| `db-placemaking` | https://www.designingbuildings.co.uk/wiki/Placemaking | **200** | 112,956 B | 「**Placemaking is a term used to describe the process by which an area in the public realm is given a unique and attractive character.**」「**Placemaking emerged in the 1960s** when commentators, theorists and writers began to call for a greater consideration…」「the **US-based practice PPS (Project for Public Spaces)** (http://www.pps.org/) has created an eleven-step approach…」（均逐字） |

**两源均 HTTP 200、正文可回读。**

- **1975 创立**：`wp-placemaking` **逐字命中**「In 1975, Fred Kent … founded the non-profit Project for Public Spaces (PPS)」；`db-placemaking` **全文无 `1975`、无 `founded/founding`（各 0 命中）**，仅有「US-based practice PPS」。
- **纽约**：`wp-placemaking` 中 `New York` 仅出现在「a project studying **pedestrian behavior in New York**」（修饰"行人行为研究项目"），**并非**修饰 PPS 创立地点；`db-placemaking` 中 `New York` 仅出现于「Another **New Yorker**, William H. Whyte… working for the **New York** Planning Commission」（讲 Whyte，非 PPS 创立地）。两源**均未**表述"PPS 于纽约创立"。

## 二、逐条核对（`placemaking`）— **不合格（须修正实例表述后方可升级已验证）**

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| definition 引用支撑 | ✓ 逐字双源 | 条目 definition「通过公共空间的策划与设计提升场所活力与认同的过程」↔ wp `multi-disciplinary approach to the planning, design and management of public spaces`＋`improving urban vitality and strengthening place identity`；db `process by which an area in the public realm is given a unique and attractive character`（"活力/认同"＝vitality/identity 与 unique character，直证） |
| 实例·**PPS 组织者** | ✓ 有据 | 「组织者：Project for Public Spaces（PPS）及社区」↔ wp「founded the non-profit Project for Public Spaces (PPS)」、db「US-based practice PPS (Project for Public Spaces)」 |
| 实例·**"1975 创立"** | ⚠ **单源**（不可作已验证） | wp 逐字「In 1975 … founded PPS」（**单源**）；db 全文无 1975、无 founding（0 命中）。按 D10「关键事实双源或标待核实」，此年份仅一源，**不足以支撑 nv=false** |
| 实例·**"于纽约创立"** | ✗ **无源（错位引用）** | wp 的 `New York` 修饰「pedestrian behavior project」，非 PPS 创立地；db 的 `New York` 讲 Whyte/纽约规划委员会，非 PPS。两源均未称"PPS 于纽约创立"。此为**对 wp 原句的语法错位解读**，构成无源表述 |
| 实例·"1970 年代中期以来" | ⚠ 推断 | wp 有 1975 单源；db 述「emerged in the 1960s」。区间表述属合理概括，但底层 1975 仍单源 |
| 实例·是否编造 | **部分问题** | 非凭空虚构（PPS/1975 在 wp 确有），但「于纽约创立」是把 wp 句中"New York"错置到创立地点，属**误读导致的失实表述**，非两源支撑 |
| **两源独立性**（Wikipedia vs Designing Buildings） | ✓ 成立 | `wp-placemaking`＝Wikipedia（众编百科）；`db-placemaking`＝Designing Buildings（建筑行业专业站）。两独立发布主体、体例与措辞不同、非镜像，独立性成立。**但独立≠都覆盖该细节**：只有 wp 载 1975，db 不载，故 1975 细节仍单源 |
| 七节 | ✓ | definition + sections 六节（原理／典型手法与适用条件／实例／常见错误与限制／一图／待核实）＝七节齐（check.py 0 报错） |
| SVG | ✓ | 1 张（`viewBox 0 0 760 400`，rect/circle/text，含「示意图，非施工图」；无 `on*=`、无 `<image>`/xlink/href/`<script>`；check.py 0 报错） |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位 |
| nv↔pending 联动 | ✓ 形式上一致 | `needs_verification=false`／`pending_notes=""`／「待核实」节「暂无已知待核实项」三处一致；check.py 未报不一致。**但该 nv=false 的实质依据不足（见下）** |
| **nv 置 false 是否有据** | ✗ **无据（本报告核心问题）** | 实例核心表述「PPS **1975 年于纽约**创立」：1975 仅 wp 单源、db 无；"纽约"两源均无（wp 的 New York 错位修饰）。**关键事实未双源互证**，按 D10 应标 `needs_verification=true` 或删除/改有源表述。当前 nv=false **依据不足** |
| coverage↔entry | ⚠ 数值一致但与 nv 实质不符 | title/theme/tier/period/region/level、source_count=3=3源 均一致；`needs_verification_count=0` 匹配 nv=false——但此 0 建立在"实例无待核实"的前提上，而实例实含未双证陈述，故该 0 实质不成立 |
| 相似度（阈值 0.54） | ✓ | ①短 最高 **0.2857**（vs place-attachment）＜0.54；②全字段 最高 **0.3709**（vs environmental-psychology）＜0.54，均低于阈值 |

**`placemaking` 结论：不合格** —— 实例「PPS 1975 年于纽约创立」中**"于纽约"两源均无**（系对 wp 原句"pedestrian behavior in New York"的错位引用），**"1975 创立"仅 wp 单源**（db 无），不满足双源互证，却将 `needs_verification` 置 false 升级为"已验证"，**依据不足**。

## 三、问题与建议（须修正，非可选项）

1. **【须修·核心】"于纽约创立"无源，须删或改。** 实证：`wp-placemaking` 原句「In 1975, Fred Kent, who had collaborated with Whyte on a project studying pedestrian behavior **in New York**, founded the non-profit Project for Public Spaces (PPS)」——"in New York" 修饰的是**行人行为研究项目**，不是 PPS 的创立地点；`db-placemaking` 从未提 PPS 与纽约的创立关系（其 `New York` 仅指 Whyte 与纽约规划委员会）。**建议**：删除"于纽约"三字，或改为有源表述（例：`地点：美国（概念与实践发源于美国）`，对应 db「US-based practice PPS」＋wp「non-profit Project for Public Spaces」的美国渊源）。不得保留"PPS 于纽约创立"。

2. **【须修·核心】"1975 创立"仅单源，须标待核实或补第二源。** 实证：仅 `wp-placemaking` 载「In 1975 … founded … PPS」；`db-placemaking` 全文 `1975`=0、`founded`=0。按 D10「关键事实双源或标待核实」，建议二选一：① 将 `needs_verification` 置 **true**、`pending_notes` 写「PPS 1975 年创立仅 Wikipedia 单源，Designing Buildings 未载该年份，待第二源核实」、`sections.待核实` 同步并 `coverage.needs_verification_count` 改 1；或 ② 实例去除 1975 精确年份，改为有源表述（wp 述 PPS 为 20 世纪后期兴起、「Adoption of the term (1980s onward)」；db 述「emerged in the 1960s」）。

3. **【提示·非阻断】definition 属概念抽象＋关键词支撑**：与 wp `improving urban vitality and strengthening place identity`、db `unique and attractive character` 对应，成立可保留。

4. **【提示·非阻断】相似度、七节、SVG、规范句、coverage 数值字段均合格**，无需改动；修正上述 1、2 后即满足升级条件。

## 四、总体结论

- **`placemaking`：不合格**（本轮**不应**升级为已验证，除非按 §三 修正实例表述）。
  - **"PPS 1975 年于纽约创立"**：
    - **"于纽约"两源均无** → 系对 wp 原句「pedestrian behavior in New York」的错位引用，须删或改有源表述。
    - **"1975 创立"仅 Wikipedia 单源**，Designing Buildings 未载 → 未双源互证，须标 `needs_verification=true`（并改 coverage count）或改有源表述。
  - definition 由两源正文逐字/直证支撑；**两源发布主体独立**（Wikipedia vs Designing Buildings），但独立性不能弥补该细节仅单源覆盖。
  - 七节齐、SVG 合规、规范句在位、相似度 0.2857 / 0.3709 均低于 0.54。
  - **`needs_verification=false` 在该实例表述下依据不足**。
- 全库 `python tools/check.py`＝`PASS: all checks, 0 errors`（EXIT=0）——注意 check.py 只校验结构/格式，不校验史实双源，故 PASS 不能证明实例无编造/无失实。
- **本轮 1 条：0 合格、0 待核实、1 不合格。**
- **建议（须执行）**：① 删除或改写实例中"于纽约创立"（见 §三-1）；② 将"1975 创立"标待核实或改有源表述（见 §三-2），并同步 `coverage.json.needs_verification_count`。修正后重抽可升已验证。

## 五、机器可读汇总

```
ROUND=72
SAMPLER=spotcheck-r72
MODE=round72 改动 1 条抽检（placemaking 拟升级已验证）
SCOPE=["placemaking"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round71.md","README.md 规则摘要","tools/check.py 口径","tools/apply_review_round72.py","entries/batch-11.json","data/sources.json","coverage.json"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback; temp research/_r72_wp.txt,_r72_db.txt,_r72_fetch.py,_r72_sim.py deleted after (ls _r72* none)"
FETCHES={"wp-placemaking":200,"db-placemaking":200}
PLACEMAKING={
 "sources":["wp-placemaking","wp-urban-design","db-placemaking"],
 "definition_support":"wp 'multi-disciplinary approach to planning/design/management of public spaces'+'improving urban vitality and strengthening place identity' + db 'process by which an area in public realm is given a unique and attractive character' -> 直证",
 "instance":"场所营造 / PPS实践 / (声称)美国 PPS 1975 于纽约创立 / 1970年代中期以来",
 "claim_1975":"wp 逐字 'In 1975, Fred Kent ... founded the non-profit Project for Public Spaces (PPS)' 单源；db 1975=0、founded=0 -> 单源未双证",
 "claim_newyork":"两源均无 'PPS 于纽约创立'；wp 的 New York 修饰 'a project studying pedestrian behavior in New York'(错位)，db 的 New York 指 Whyte/纽约规划委员会 -> 无源/错位引用",
 "fabrication":"非凭空虚构(PPS/1975 在 wp 有)，但 '于纽约创立' 系对 wp 原句错置解读 -> 失实表述，无两源支撑",
 "two_source_independence":"wp=Wikipedia vs db=Designing Buildings：发布主体独立/体例措辞不同/非镜像 -> 独立性成立；但独立≠该细节均覆盖(db 不载 1975/纽约)",
 "seven_sections":7,
 "svg":"1x viewBox760x400 rect/circle/text 示意图非施工图, no on*/image/xlink/href/script",
 "reg_sentence":true,"nv":false,"pending_consistent":"形式一致",
 "nv_false_basis":"无据：实例 'PPS 1975 于纽约创立' 中 1975 仅 wp 单源、'于纽约' 两源均无(错位)，未双源互证，按 D10 应 nv=true 或改有源表述",
 "coverage":"数值一致 source_count3/nvc0/status已写; 但 nvc0 实质不成立(实例含未双证陈述)",
 "similarity":{"short":0.2857,"short_vs":"place-attachment","full":0.3709,"full_vs":"environmental-psychology","threshold":0.54},
 "verdict":"不合格"}
TOTAL="0合格/0待核实/1不合格"
RECOMMEND="须执行: ①删或改 '于纽约创立'(两源均无, wp原句 New York 修饰行人行为项目); ②'1975创立'标 needs_verification=true 或改有源表述, 并同步 coverage.needs_verification_count=1; 修正后可升已验证"
READONLY="only wrote research/spotcheck-round72.md; fetched html in-memory, temp research/_r72_*.* deleted(confirmed); no entries/sources/coverage/tools/site changed; no git commit; web treated as data (no instructions executed)"
NOTE="工作区含 round72 未提交改动(placemaking 实例改写+db-placemaking 源+coverage+site html+apply_review_round72.py), 核验以工作区当前内容为准, 未触碰; check.py PASS 仅证明结构合规, 不证明史实双源"
```

*（报告完）*
