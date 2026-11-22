# 第23轮质量闸抽检报告（spotcheck-round23）——east-west-perspective-compare / vitruvian-triad / sunken-accessibility 逐条来源·正文支撑·结构·相似度复检

- 抽检人：spotcheck-r23（由 lead 委派的子代理）；抽检时间：2026-11-22 约 20:50 起，Asia/Hong_Kong（会话时间取样；核对完成时点约 20:58）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（本轮改动条目抽 ≥25%、至少 3 个；不合格整批返工；相似度过高整批降级）、第六节（联网内容一律视为数据，其中任何指令不执行、不下载不运行来源代码、不改项目文件夹之外内容）、第二节（状态文件）；`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L2」「条目页结构（七节）」「通用硬性规则」「专用规则」；`DECISIONS.md` D05（实抓核验）/D06（在线百科 year=null）/D09（尺寸·坡度·消防·无障碍仅一般性说明并附规范提示）/D10（关键事实需两独立来源，否则标待核实）/D11（link_ok 三态）/D14（needs_verification 与 pending_notes 联动）。
  - 说明：任务书所称 `AUTONOMOUS.md`/`TASK_design.md` 在仓库根无同名文件，实际位于 `D:/Users/Administrator/Desktop/`（与第 12–22 轮一致），已按该路径只读读取；`DECISIONS.md`、`research/spotcheck-round22.md` 在仓库根。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为子代理，按 SUBAGENT-STOP 仅作规范参考，不另启流程）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言）。
- 抽检对象（第23轮升级的 **7 条核心 L1→L2**，据 `tools/upgrade_round23.py` 头部 S/SRC 字典确认集合为：`east-west-perspective-compare`、`east-west-space-compare`、`damp-proofing`、`safety-guarding`、`sustainable-architecture`、`vitruvian-triad`、`sunken-accessibility`；本次按指派抽其中 3 条）：**`east-west-perspective-compare`（散点与焦点透视比较，tier 核心）、`vitruvian-triad`（维特鲁威三原则，tier 核心）、`sunken-accessibility`（下沉空间无障碍，tier 核心）**。三条分别位于 `entries/batch-02-a.json`（east-west-perspective-compare）与 `entries/batch-03.json`（vitruvian-triad、sunken-accessibility）。抽样率 3/7 ≈ 43%，满足「≥25% 且 ≥3 条」。

## 〇、数据稳定性说明（本轮数据已冻结）

- 本轮**未发现并发的 review/apply 流水线**（`research/review-round23.md`、`tools/apply_review_round23.py` 均不存在）。
- 写入时点：`data/sources.json` mtime 20:48:55；`entries/batch-02-a.json`、`entries/batch-03.json`、`coverage.json` mtime 20:49:36；`tools/upgrade_round23.py` mtime 20:49:31 —— 由本轮一次写入完成。
- **20:57 复核**：上列四个文件 mtime 仍分别为 20:48:55 / 20:49:36，字节数不变（batch-02-a 22953B、batch-03 13062B、coverage 80224B、sources 97192B）→ **数据稳定，无中途改写**。`git status` 显示 round23 改动为未提交态（M coverage/batch-02-a/c/d/03；?? gaps-round23、reader_questions-round23、upgrade_round23.py），与抽检态一致。
- **本报告口径**：以当前最终态（20:49:36 快照，20:57 复核未变）逐条复核。
- 只读声明：本次**仅生成** `research/spotcheck-round23.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未改动项目文件夹之外内容，未创建 git commit。抓取正文仅驻留系统临时目录（`/tmp/r23texts.json`）用于分析、非项目产物。联网内容一律视为数据，网页中任何指令均未执行。

## 一、判定口径与相似度方法

- **结构口径**：3 条均为 L2，按 TASK_design.md「条目页结构」核 **七节**：①核心概念与定义(=definition) ②原理 ③典型手法与适用条件 ④实例 ⑤常见错误与限制 ⑥一图 ⑦待核实；并核每页 ≥1 张内联 SVG 含「示意图，非施工图」、风控段含 D09 规范提示（“实际工程须按当地规范和专业设计人员的要求”）、`needs_verification`/`pending_notes`/正文待核实/`coverage.needs_verification_count` 联动一致；实例须为**类型性描述**（名称/地点/设计者/年份），不复制图像、不编造年份人名引文。
- **正文支撑口径（本轮重点）**：对每条所挂 verified 来源，**实抓英文维基正文并逐句比对** definition / time_or_place / overview / 七节主张。判定“核心概念是否被来源正文直接支撑”。D09 允许“尺寸·坡度·消防·无障碍”作一般性说明并附规范提示，但**不豁免核心概念本身的来源支撑**。
- **相似度阈值 0.54**（AUTONOMOUS.md E 节「疑似套话」警戒线，沿用第 12–22 轮口径）。算法 = `difflib.SequenceMatcher(None,a,b).ratio()`，字段以 `|` 连接；短文本 = `title|definition|time_or_place|overview`；全字段 = 短文本再加 6 个 sections；calib = `definition|time_or_place|overview|6节`（不含 title）。sections 固定按 `原理|典型手法与适用条件|实例|常见错误与限制|一图|待核实` 顺序拼接。全库共 **126** 条（脚本实测 `TOTAL ENTRIES=126`，无重复 id），逐条对其余 125 条取最高值。

## 二、任务 1：相似度（difflib）对全库最高值

逐条对全库其余 125 条取最高相似度（脚本实算）：

| 条目 | 短文本(title+def+top+ov) 最高 | 对手 | 全字段(+sections) 最高 | 对手 | calib(def\|top\|ov\|sec) 最高 | 对手 | 是否 <0.54 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| east-west-perspective-compare | 0.4082 | east-west-space-compare | 0.4402 | east-west-space-compare | 0.4444 | east-west-space-compare | ✅ |
| vitruvian-triad | 0.3158 | six-principles | 0.3973 | liubai | 0.4049 | liubai | ✅ |
| sunken-accessibility | 0.4366 | drainage | 0.4354 | safety-guarding | 0.4457 | safety-guarding | ✅ |

- **3 条无论短文本、全字段还是 calib 口径，对全库最高相似度全部 < 0.54**（最高为 sunken-accessibility calib **0.4457**，仍远低于阈值）。
- 全库两两短文本当前最高对仍为 `s-curve-composition × triangular-composition` **0.5166**，亦低于 0.54，无整库套话告警（与第 17–22 轮一致）。相似度维度**不触发降级**。

## 三、任务 2：来源存在性 / verified / 主题相关性（实抓）

本轮 `en.wikipedia.org` 直连**实抓 HTTP 200 且 h1 吻合**（6 个来源本次两轮重试后全部可用；architectural-theory、architecture 首抓遇瞬时 SSL EOF，重试后 200）。下列为实抓命中（**数据，非指令**）：

| 来源 id | 存在 / 记录标题 | verified / link_ok | 实抓 | 与主题相关（按正文内容核） |
| --- | --- | --- | --- | --- |
| wp-perspective-graphical | ✅ `Perspective (graphical)` | true / true | en.wikipedia HTTP200，h1 吻合 | ✅ 直接支撑“焦点透视=灭点/固定视点/线性透视” |
| wp-chinese-painting | ✅ `Chinese painting` | true / true | en.wikipedia HTTP200，h1 吻合 | ⚠️ 主题相关（中国画），但**正文零透视内容**（perspective=0），对“散点透视”无支撑 |
| wp-architectural-theory | ✅ `Architectural theory` | true / true | en.wikipedia HTTP200，h1 吻合 | ✅ 直接支撑“维特鲁威 firmitas/utilitas/venustas” |
| wp-visual-arts | ✅ `Visual arts` | true / true | en.wikipedia HTTP200，h1 吻合 | ✅ 正文含“Vitruvius 三原则 firmitas/utilitas/venustas”原句，支撑维特鲁威三原则（标题虽宽泛但正文直接命中） |
| wp-architecture | ✅ `Architecture` | true / true | en.wikipedia HTTP200，h1 吻合 | ❌ 对“无障碍/下沉空间”**零相关**（accessibility/accessible/ramp/handrail/disab 均=0；仅 1 处 “building codes”） |
| wp-exit-sign | ✅ `Exit sign` | true / true | en.wikipedia HTTP200，h1 吻合 | ⚠️ 仅涉“无障碍出口标识/accessible means of egress”；**无坡道/坡度/扶手/台阶/下沉空间**（ramp=slope=handrail=stair=sunken=0） |

> 结论（来源层面）：6 个来源 id **均存在**、`verified=true`、`link_ok=true`，实抓 h1 全部吻合。但**“存在且 verified”不等于“正文支撑所挂主张”**：wp-chinese-painting 对透视零支撑、wp-architecture 对无障碍零支撑、wp-exit-sign 对坡道/下沉空间零支撑。逐条支撑见 §四。

## 四、任务 3：逐条正文支撑核对（关键项，实抓逐句比对）

`python tools/check.py` 实跑 → **`PASS: all checks, 0 errors`（EXIT=0）**。`check.py` 只校验“每条挂有 verified 来源”，**不校验来源正文是否支撑该主张**；下表为对实抓正文逐句人工比对所得。

### 4.1 east-west-perspective-compare（散点与焦点透视比较）——**焦点透视侧强支撑；东方“散点透视/移动视点”核心无来源支撑，且术语与来源不符 → 不合格**

实抓命中片段（wp-perspective-graphical）：
- “Vanishing points … located at the left and right of the plane … a central vanishing point can be used … to indicate frontal (foreshortened) depth.”；“The most characteristic features of linear perspective are that objects appear smaller as their distance from the observer increases …”（→ 支撑“焦点透视=固定视点、汇聚于灭点、线性透视”）
- **“Whereas Roman and subsequent European visual art effectively had multiple and incoherent vanishing points, Asian art usually lacked any vanishing point, but aligned recession in parallel.”**
- **“Chinese artists made use of oblique projection from the first or second century until the 18th century.”**
- “An important factor here is the use of **long scrolls**, which even now make fully coherent perspective projection unsuitable.”

实抓命中片段（wp-chinese-painting）：
- 关键词实测：**perspective 0、viewpoint 0、scattered 0、shifting 0、three-dimensional 0、spatial 0**；handscroll 1（仅“可装裱为手卷”的装裱介质表述）、depth 2（“The artists began to show space and depth … mountain mass, distanced hills and clouds”——佛教山水语境，非透视法）。→ **中国画来源正文对“散点透视/移动视点”无任何论述**。

逐项比对：
- definition「散点透视与焦点透视在视点组织上的对照」→ **半支撑**：焦点透视一侧强支撑；**“散点透视”一侧无来源**——wp-perspective-graphical 明确把中国/亚洲绘画表述为 **oblique projection（斜投影）/ parallel recession（平行退行）/ lacked any vanishing point（无灭点）**，与“散点透视（多视点/移动视点）”属**不同概念**；wp-chinese-painting 无透视内容。
- overview「前者移动视点展开长卷，后者固定视点汇聚于灭点」→ “后者固定视点汇聚灭点”强支撑；“**前者移动视点展开长卷**”中“长卷”（long scrolls）有来源，但“**随视点移动/多点**”无来源，来源实际用“平行退行/无灭点/斜投影”表述。
- 典型手法「东方长卷用散点连续展开，西方透视用于单点凝视」→ 东方侧“散点”无来源；西方侧成立。
- 实例「中国长卷与西方焦点透视绘画的对照（类型性描述）；地点/设计者/年份 不适用」→ **类型性、无编造**（未编年份人名引文）。
- **待核实联动缺口**：`sections.待核实` 仅写“具体对照作品的作者与年代待核实”，**未披露“东方侧散点透视概念缺直接来源/单源”这一实质缺口**。

> **判定：不合格（正文支撑不足）**。西式焦点透视侧与“东西方透视差异”总体有 wp-perspective-graphical 部分支撑，可作返工基础；但核心东方术语“散点透视/移动视点”无来源直接支撑、与所引来源的 oblique projection 表述不一致，且 wp-chinese-painting 对透视零贡献（透视主张实为单源）。**返工方向**：改用来源原表述（oblique projection/parallel recession/长卷不宜一致透视）或补一条专门论述“散点透视/中国画透视”的权威来源，并同步修正待核实声明。

### 4.2 vitruvian-triad（维特鲁威三原则）——**双源逐句支撑三原则，无编造 → 合格**

实抓命中片段（wp-architectural-theory）：
- “It also proposes **the three fundamental laws that architecture must obey** … **firmitas, utilitas, venustas**, translated in the 17th century by Sir Henry Wotton into the English slogan **firmness, commodity, and delight (meaning structural adequacy, functional adequacy, and beauty)**.”
- “with the work of **Vitruvius** … Vitruvius was a Roman writer, architect, and engineer active in the 1st century BC.”；“From Alberti, good architecture is validated through the **Vitruvian triad**”；“De Architectura Libri Decem (The Ten Books on Architecture) by Marcus Vitruvius Pollio”。

实抓命中片段（wp-visual-arts）：
- “The earliest surviving written work on architecture is **De architectura**, by the Roman architect **Vitruvius** … According to Vitruvius, a good building should satisfy three principles: **firmitas, utilitas, venustas, translated as firmness, commodity, and delight**.”

逐项比对：
- definition「维特鲁威提出的坚固、实用与美观三项建筑原则」→ **强支撑**（两源均逐字列 firmitas/utilitas/venustas = firmness/commodity/delight = 结构/功能/美观）。
- overview「三原则把结构、功能与审美并列，成为后世建筑理论反复引用的基本框架」→ **强支撑**（“three fundamental laws”“Vitruvian triad”反复引用）。
- 原理「坚固（结构可靠）、实用（功能合用）、美观（比例和谐）」→ **强支撑**（structural adequacy / functional adequacy / beauty）。
- 实例「维特鲁威《建筑十书》所述三原则（类型性记载）；地点：古罗马；设计者/年份 不适用」→ **类型性、无编造**（Vitruvius 罗马人、De architectura=《建筑十书》均来源支持；未编年份）。
- **无编造年份/人名/引文**；`sections.待核实`「《建筑十书》成书年代与译本细节待核实」表述审慎、合理。

> **判定：合格**。三原则由 wp-architectural-theory + wp-visual-arts **两独立来源逐句印证**，满足 D10；无编造；结构全过。
> **非阻断小问题**：`related=['plein-air']`（外光写生，绘画户外写生法）与本条（建筑理论三原则）**主题错配**，系 L1 期继承字段（upgrade_round23 未改写 related），建议改为建筑理论类相关条目（如 architectural-theory / classicism 等）。此问题不影响本轮来源与结构判定，记为 minor。

### 4.3 sunken-accessibility（下沉空间无障碍）——**核心“无障碍坡道/平台/扶手/下沉空间”两源均零正文支撑 → 不合格**

实抓关键词精确实测：

| 关键词 | wp-architecture | wp-exit-sign |
| --- | --- | --- |
| accessibility / accessible | **0 / 0** | 3 / 19 |
| ramp（坡道） | **0** | **0** |
| slope（坡度） | **0** | **0** |
| handrail（扶手） | **0** | **0** |
| stair（台阶） | **0** | **0** |
| sunken（下沉） | **0** | **0** |
| disabled / disability / wheelchair | **0/0/0** | 3 / 0 / 3 |
| universal design | **0** | （未计，正文仅 generic） |
| means of egress / egress | **0 / 0** | 7 / 7 |
| building code | 1（仅“residential … adhering to building codes”） | — |

实抓命中片段：
- wp-architecture：**无任何无障碍/坡道/扶手/下沉空间论述**；`access` 仅出现 2 次且均为引文“accessed/Accessed”日期，非 accessibility。
- wp-exit-sign：全部围绕“**Accessible designs**（出口标识的通用设计）”“**accessible means of egress**”“wheelchair symbol on signs”——即“无障碍**出口标识**的可达性设计”，**不涉及坡道、坡度、扶手、台阶、下沉空间**（ramp=slope=handrail=stair=sunken=0）。

逐项比对：
- definition「使低处空间对不同行动能力者均可到达并使用的设计」→ “不同行动能力者/无障碍”仅能从 wp-exit-sign 的 “accessible… people with disabilities”**泛化**得到间接印证；“**低处空间/下沉空间**”无来源。
- overview「下沉空间若只设台阶会中断路径，坡道、平台与连续扶手是常见的应对方式」→ **坡道/平台/连续扶手/台阶 在两源中全部为 0，无任何正文支撑**。
- 原理/典型手法「坡道、休息平台、坡度、连续扶手…适用于下沉庭院与广场」→ **坡道/坡度/扶手/平台/下沉庭院/广场 全部无来源支撑**。
- 实例「下沉空间无障碍坡道（类型性描述）；地点/设计者/年份 不适用」→ 类型性、无编造年份人名引文（这一点合规）。
- **待核实联动缺口**：`sections.待核实` 只写“示例坡道的坡度参数与设计者待核实”，把问题收窄为“坡度参数”，**未披露“整个无障碍坡道/扶手/下沉空间概念本身无可直接支撑来源”**。

> **判定：不合格（核心主张缺乏来源正文支撑）**。wp-architecture 与“无障碍”零相关（仅 1 处 building codes），wp-exit-sign 只涉“无障碍出口标识/疏散标识”，两者均**不含坡道·坡度·扶手·下沉空间**任何内容。本条不同于第22轮 evacuation-route（该条定义“紧急疏散/出口标识”由 exit-sign 直接支撑，仅次要工程参数属 D09 一般说明）；本条连**核心概念（下沉空间无障碍坡道）都无来源背书**，D09 只豁免“尺寸/坡度数据”的一般性表述、不豁免核心概念缺源。**返工方向**：补“无障碍设计/建筑无障碍规范（如 ADA/无障碍设计标准、坡道坡度）”类权威来源，或补“下沉庭院/下沉广场”条目支撑“下沉空间”，并把待核实声明扩展到“核心概念尚无直接来源”。

## 五、任务 4：结构 / SVG / 规范提示 / 待核实联动（当前最终态，实测）

| 检查项 | east-west-perspective-compare | vitruvian-triad | sunken-accessibility |
| --- | --- | --- | --- |
| 七节齐备（definition + 6 节，无缺无多） | ✅ 6/6 | ✅ 6/6 | ✅ 6/6 |
| 1 张内联 SVG，viewBox（0 0 760 400） | ✅ | ✅ | ✅ |
| SVG 图注含「示意图，非施工图」 | ✅ | ✅ | ✅ |
| 常见错误与限制含 D09 规范提示 | ✅ | ✅ | ✅ |
| 正文无编造人名/引文 | ✅ | ✅ | ✅ |
| 无编造年份（实例年份均“不适用”） | ✅ | ✅ | ✅ |
| 实例为“类型性描述” | ✅（对照，无图像） | ✅（《建筑十书》三原则） | ✅（无障碍坡道） |
| needs_verification ↔ pending_notes ↔ 待核实 ↔ coverage.nvc | ✅ 一致（T/非空/非空/1） | ✅ 一致（T/非空/非空/1） | ✅ 一致（T/非空/非空/1） |
| theme/tier/period/region 与 coverage 一致 | ✅（理论/核心/跨时期/全球） | ✅（理论/核心/古代/欧洲） | ✅（下沉空间/核心/20世纪/全球） |
| source_count 与 sources 一致 | ✅ 2 | ✅ 2 | ✅ 2 |
| **definition/overview/七节 有已挂来源正文支撑** | ❌ 东方“散点透视/移动视点”无支撑（西式焦点透视侧支撑） | ✅ 强支撑（双源） | ❌ 无障碍坡道/扶手/下沉空间零支撑 |

> 三条的 `needs_verification ↔ pending_notes ↔ sections.待核实 ↔ coverage.needs_verification_count` **各自形式一致**（均 T/非空/非空/1），source_count 与 sources 数一致，theme/tier/period/region 与 coverage 对齐。**但三处 `pending_notes` 完全相同**（“实例的具体名称、设计者与年代待补充独立来源。”）——为模板化批产痕迹；且上述“形式一致”并不等于“待核实声明如实覆盖了实际缺口”（见 §4.1、§4.3）。`check.py` **PASS 0 errors（EXIT=0）**。

## 六、逐条验收结论（当前最终态）

| 条目 | 来源/正文支撑 | 结构·SVG·规范 | 待核实联动 | 相似度(短/全/calib) | 结论 |
| --- | --- | --- | --- | --- | --- |
| **east-west-perspective-compare（散点与焦点透视比较）** | 焦点透视侧强支撑；**东方“散点透视/移动视点”无来源，与来源 oblique projection/parallel 表述不符；wp-chinese-painting 零透视 → 单源** | 全过 | 形式一致但声明未覆盖概念缺口 | 0.4082 / 0.4402 / 0.4444 | **不合格（核心东方术语/概念无来源支撑）** |
| **vitruvian-triad（维特鲁威三原则）** | firmitas/utilitas/venustas 由 architectural-theory + visual-arts **双源逐句支撑**；无编造 | 全过 | 一致（nvc1） | 0.3158 / 0.3973 / 0.4049 | **合格**（minor：related=plein-air 错链） |
| **sunken-accessibility（下沉空间无障碍）** | 核心坡道/平台/扶手/下沉空间**两源零支撑**；wp-architecture 无障碍=0，wp-exit-sign 仅“无障碍出口标识” | 全过 | 形式一致但声明仅提及坡度参数 | 0.4366 / 0.4354 / 0.4457 | **不合格（核心概念缺乏来源正文支撑）** |

**逐条依据与问题：**

- **east-west-perspective-compare — 不合格**
  - 依据（满足部分）：wp-perspective-graphical “vanishing point … central vanishing point … linear perspective”，“Asian art usually lacked any vanishing point, but aligned recession in parallel”，“Chinese artists made use of oblique projection”，“long scrolls … make fully coherent perspective projection unsuitable”——支撑“焦点透视=灭点/固定视点”及“东西方透视组织不同”。
  - 问题（阻断）：definition/overview/原理的核心“**散点透视/随视点移动**”无来源直接支撑；来源实际用 **oblique projection / parallel recession / 无灭点** 表述，与“散点（多点/移动视点）”是**不同概念**；wp-chinese-painting 对透视零贡献（perspective=0），透视主张实为**单源**；`sections.待核实`未披露此缺口。→ 判定不合格（可按返工方向修正后复检）。

- **vitruvian-triad — 合格**
  - 依据：wp-architectural-theory “the three fundamental laws … firmitas, utilitas, venustas … firmness, commodity, and delight (structural adequacy, functional adequacy, and beauty)”“Vitruvian triad”“De Architectura Libri Decem … Vitruvius”；wp-visual-arts “According to Vitruvius … firmitas, utilitas, venustas … firmness, commodity, and delight”。**双独立来源逐句支撑三原则**，满足 D10，无编造。
  - 问题（非阻断）：`related=['plein-air']`（外光写生）与本条主题错配，建议更换为建筑理论类相关条目；`pending_notes` 为模板化通用句。均不影响合格判定。

- **sunken-accessibility — 不合格**
  - 依据（合规部分）：实例为类型性描述、无编造年份/人名/引文；七节/SVG/规范提示/D09 齐备。
  - 问题（阻断）：核心主张“无障碍坡道、平台、坡度、连续扶手，适用于下沉庭院/广场”在 **wp-architecture（无障碍词全 0，仅 1 处 building codes）与 wp-exit-sign（仅无障碍出口标识，ramp/slope/handrail/stair/sunken 全 0）中均无任何正文支撑**；“无障碍”仅能从 exit-sign 的“accessible…disabilities（出口标识设计）”泛化间接得到，且“下沉空间”完全无源。D09 仅豁免坡度/尺寸等一般性说明，不豁免核心概念本身缺源。`sections.待核实`仅收窄到“坡度参数待核实”，未如实反映“核心概念缺来源”。

## 七、总体结论与是否整批返工

- **抽检结果：3 条中 1 合格、2 不合格。**
  - **合格（1）**：`vitruvian-triad`——维特鲁威 firmitas/utilitas/venustas 由两条 Wikipedia 来源逐句支撑，无编造，结构全过。
  - **不合格（2）**：`east-west-perspective-compare`（东方“散点透视/移动视点”核心无来源、术语与来源不符、wp-chinese-painting 零透视→单源）；`sunken-accessibility`（核心“无障碍坡道/平台/扶手/下沉空间”两源均零支撑，wp-architecture 与无障碍零相关）。
- **相似度**：3 条对全库最高（短/全/calib 任一）均 < 0.54（最大 sunken-accessibility calib 0.4457）；全库两两短文本最高 0.5166；库规模 126 → **无套话/近重复告警，不因相似度降级**。
- **结构**：3 条七节完整、各 1 张 SVG 含「示意图，非施工图」、风控段含 D09 提示、实例均为类型性描述、`check.py` **PASS 0 errors（EXIT=0）**；`needs_verification↔pending↔待核实↔nvc` 三条**形式**各自一致。→ **结构维度合格**。
- **来源**：6 个来源 id 均存在、`verified=true`、`link_ok=true`，实抓 HTTP200 且 h1 吻合；**但 3 条来源的“正文支撑”不达标（2 条核心概念无来源支撑）**——这正是 check.py 无法覆盖、必须人工实抓比对的部分。
- **是否建议整批返工：建议整批返工（本轮 7 条升级批次）。** 依据 AUTONOMOUS.md 第三节 E「抽检……不合格则整批返工」，本轮已出现 **2 条不合格**（`east-west-perspective-compare`、`sunken-accessibility`），触发整批返工条件。具体：
  1. **必须定向返工（补源/改术语）**：`sunken-accessibility` 补“无障碍设计/坡道坡度/下沉庭院”类权威来源，并把待核实声明扩展到核心概念；`east-west-perspective-compare` 改用来源原表述（oblique projection / parallel recession / 长卷不宜一致透视）或补专门“散点透视/中国画透视”来源，并修正待核实声明。
  2. **全批复检**：其余 4 条（`east-west-space-compare`、`damp-proofing`、`safety-guarding`、`sustainable-architecture`）虽本轮未抽，但同属 `upgrade_round23` 模板化批产（实例普遍“不适用”、`pending_notes` 同句），**尤其 `safety-guarding` 与 `sunken-accessibility` 使用完全相同的 `wp-architecture + wp-exit-sign` 组合，存在同类“核心概念无来源支撑”高风险**，须一并实抓复检来源正文后再定级。
  3. **共性缺陷**：本轮 7 条普遍采用“权威百科总览级来源”挂靠具体概念，而总览条目往往不覆盖具体子概念（如 Architecture 不含 accessibility、Chinese painting 不含 perspective）——建议返工时逐条核对“来源正文是否真覆盖该条核心概念”，不要仅凭“标题相关 + verified”判定支撑。
- **是否触发相似度/占比降级复查**：相似度未超阈、待核实占比正常（3 条 nvc 均=1、nvf 均=true，无“硬写”信号），**不因相似度降级**；但因 2 条不合格，**按协议整批返工**。

---

### 机器可读汇总

```
ROUND=23
SAMPLER=spotcheck-r23
SCOPE=["east-west-perspective-compare","vitruvian-triad","sunken-accessibility"]   # 抽自第23轮7条核心升级集，3/7≈43%
ROUND23_UPGRADE_SET=["east-west-perspective-compare","east-west-space-compare","damp-proofing","safety-guarding","sustainable-architecture","vitruvian-triad","sunken-accessibility"]
FILES={"east-west-perspective-compare":"entries/batch-02-a.json","vitruvian-triad":"entries/batch-03.json","sunken-accessibility":"entries/batch-03.json"}
STATE_STABLE={"sources_mtime":"20:48:55","entries_coverage_mtime":"20:49:36","recheck":"20:57 unchanged","concurrency":"none (no review-round23/apply_review_round23)"}
SIM_METHOD="difflib.SequenceMatcher.ratio(); join='|'; short=title|definition|time_or_place|overview; full=+6sections; calib=def|top|ov|sections"
SIM_MAX_SHORT={"east-west-perspective-compare":[0.4082,"east-west-space-compare"],"vitruvian-triad":[0.3158,"six-principles"],"sunken-accessibility":[0.4366,"drainage"]}
SIM_MAX_FULL={"east-west-perspective-compare":[0.4402,"east-west-space-compare"],"vitruvian-triad":[0.3973,"liubai"],"sunken-accessibility":[0.4354,"safety-guarding"]}
SIM_MAX_CALIB={"east-west-perspective-compare":[0.4444,"east-west-space-compare"],"vitruvian-triad":[0.4049,"liubai"],"sunken-accessibility":[0.4457,"safety-guarding"]}
ALL_SIM_UNDER_0.54=true ; LIBRARY_SIZE=126 ; GLOBAL_MAX_SHORT={"0.5166":"s-curve-composition x triangular-composition"}
SOURCES_ALL_EXIST_VERIFIED=true
SOURCES={"east-west-perspective-compare":["wp-perspective-graphical","wp-chinese-painting"],"vitruvian-triad":["wp-architectural-theory","wp-visual-arts"],"sunken-accessibility":["wp-architecture","wp-exit-sign"]}
FETCH={"en.wikipedia.org":"HTTP200 h1 matched x6 (retry 2 on SSL EOF): perspective_graphical/chinese_painting/architectural_theory/visual_arts/architecture/exit_sign"}
LINK_OK={"wp-perspective-graphical":true,"wp-chinese-painting":true,"wp-architectural-theory":true,"wp-visual-arts":true,"wp-architecture":true,"wp-exit-sign":true}
BODY_SUPPORT={
  "east-west-perspective-compare":"PARTIAL: focal-perspective STRONG (vanishing point/linear); EAST 'scattered/散点透视/移动视点' UNSUPPORTED -- source says 'Asian art lacked any vanishing point, aligned recession in parallel','Chinese artists made use of oblique projection','long scrolls make coherent perspective unsuitable'; wp-chinese-painting perspective=0 -> single-source. NOT a valid '散点透视' support.",
  "vitruvian-triad":"STRONG double-source: architectural_theory + visual_arts both state 'firmitas, utilitas, venustas = firmness, commodity, delight (structural/functional/beauty)' by Vitruvius, De architectura. No fabrication.",
  "sunken-accessibility":"UNSUPPORTED CORE: '无障碍坡道/平台/扶手/坡度/下沉空间' -- wp-architecture accessibility/accessible/ramp/handrail/slope/stair/disab=0 (only building codes=1); wp-exit-sign accessible=19 but about accessible EXIT SIGN design & 'accessible means of egress', ramp=slope=handrail=stair=sunken=0. Core concept has NO body support."
}
KW_COUNTS={
  "wp-perspective-graphical":{"perspective":104,"vanishing point":12,"linear perspective":12,"one-point":10,"Chinese":9,"oblique":9,"scattered":0,"shifting":0,"multiple perspectives":0},
  "wp-chinese-painting":{"perspective":0,"viewpoint":0,"scattered":0,"shifting":0,"three-dimensional":0,"handscroll":1,"depth":2},
  "wp-architectural-theory":{"vitruvius":7,"firmitas":1,"utilitas":1,"venustas":1,"firmness":1,"beauty":1,"commodity":1,"delight":1},
  "wp-visual-arts":{"vitruvius":3,"firmitas":1,"architecture":12},
  "wp-architecture":{"accessibility":0,"accessible":0,"ramp":0,"handrail":0,"slope":0,"stair":0,"disab":0,"wheelchair":0,"egress":0,"building code":1},
  "wp-exit-sign":{"accessible":19,"accessibility":3,"wheelchair":3,"disab":3,"means of egress":7,"egress":7,"ramp":0,"slope":0,"handrail":0,"stair":0,"sunken":0}
}
SEVEN_SECTIONS_OK=true ; SVG_COUNT=1_each ; SVG_CAPTION_OK=true ; REGNOTE_OK=true ; INSTANCE_TYPE_LEVEL=true_each
NEEDS_VERIFICATION={"east-west-perspective-compare":"T/nvc1","vitruvian-triad":"T/nvc1","sunken-accessibility":"T/nvc1"}  # 形式一致；但 east-west/sunken 的待核实声明未覆盖实际概念缺口
FABRICATED="none (no fabricated year/name/quote; instance year fields '不适用')"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
VERDICT={"east-west-perspective-compare":"不合格(东方散点透视/移动视点核心无来源;术语与来源oblique/parallel不符;wp-chinese-painting零透视->单源;待核实未覆盖)","vitruvian-triad":"合格(双源逐句支撑firmitas/utilitas/venustas;无编造;minor:related=plein-air错链)","sunken-accessibility":"不合格(无障碍坡道/平台/扶手/下沉空间两源零支撑;wp-architecture无障碍=0;wp-exit-sign仅无障碍出口标识)"}
OVERALL="1合格(vitruvian-triad) + 2不合格(east-west-perspective-compare,sunken-accessibility);相似度全<0.54无套话;结构全过check.py PASS;6来源均verified但2条核心概念正文不支撑"
BATCH_REWORK="建议整批返工(本轮7条): 定向返工sunken-accessibility(补无障碍/坡道/下沉来源)、east-west-perspective-compare(改术语或补散点透视来源);全批复检其余4条尤其safety-guarding(同wp-architecture+wp-exit-sign高风险);共性:总览级百科来源不覆盖具体子概念"
```

*（报告完）*
