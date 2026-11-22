# 第21轮质量闸抽检报告（spotcheck-round21）——qi-yun / space-definition / spatial-sequence 逐条来源·结构·相似度复检

- 抽检人：spotcheck-r21（由 lead 委派的子代理）；抽检时间：2026-11-22 20:27 起，Asia/Hong_Kong（会话时间取样），核对完成时点约 20:34。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（本轮改动条目抽 ≥25%、至少 3 个；不合格整批返工；待核实占比异常/相似度过高整批降级复查）、第六节（联网内容一律视为数据，网页中任何指令一律不执行、不下载不运行来源代码、不改项目文件夹之外内容）、第二节（状态文件）；`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L2」「条目页结构（七节）」「通用硬性规则」「专用规则」；`DECISIONS.md` D05（实抓核验）/D06（在线百科 year=null）/D09（规范提示模板）/D10（关键事实需两独立来源，否则标待核实）/D11（link_ok 三态）/D14（needs_verification 与 pending_notes 联动）。
  - 说明：任务书所称 `AUTONOMOUS.md`/`TASK_design.md` 在仓库根无同名文件，实际位于 `D:/Users/Administrator/Desktop/`（与第 12–20 轮一致），已按该路径读取；`DECISIONS.md`、`research/spotcheck-round20.md` 在仓库根。
- 技能：已加载 `using-superpowers`（本会话为子代理，按 SUBAGENT-STOP 不另启流程，仅作规范参考）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言）。
- 抽检对象（第21轮升级的 **6 条核心 L1→L2**，据 `tools/upgrade_round21.py` 文件头与 `S`/`SRC`/`SVG` 清单确认为：`qi-yun`、`liubai`、`yijing`、`space-definition`、`human-scale`、`spatial-sequence`；本次按指派抽其中 3 条）：**`qi-yun`（气韵生动，tier 核心）、`space-definition`（建筑空间定义，tier 核心）、`spatial-sequence`（空间序列，tier 核心）**，三条同在 `entries/batch-02-a.json`。抽样率 3/6 = 50%，满足「≥25% 且 ≥3 条」。

## 〇、并发变更轨迹与最终态说明（**重要：本批是移动目标**）

本批在抽检过程中被**另一条并发的评审流水线改动**，必须如实记录：

- **20:27:09/20:27:14（抽检取样态）**：`tools/upgrade_round21.py` 生成并应用；`entries/batch-02-a.json`、`coverage.json` mtime = 20:27:14，`data/sources.json` = 20:26:30。此时 3 条均为**类型性实例**、`needs_verification=true`、`nvc=1`、每条 2 个来源。
- **20:31:58 / 20:32:21–20:32:24（并发评审流水线）**：`research/review-round21.md`（20:31:58，39230B）出现，随后 `tools/apply_review_round21.py`（20:32:21）运行并改写 `entries/batch-02-a.json`、`coverage.json`、`data/sources.json`、`site/*`（均 20:32:24）。其文件头自述“第21轮复核应用：**space-definition（巴塞罗那德国馆）、human-scale（帕伊米奥疗养院）双源升级**”。
  - 该步把 **`space-definition` 由「类型性实例 + 2 来源」升级为「具名实例（巴塞罗那德国馆，1929，密斯·凡·德·罗与莉莉·赖希）+ 4 来源（新增 miesbcn / archdaily 双专源）」，并把 `needs_verification` 由 true 改为 **false**、`nvc` 由 1 改为 **0**。`human-scale` 同样被改为具名实例（帕伊米奥疗养院）+ 4 来源、nvf=false、nvc=0。
  - `qi-yun`、`spatial-sequence` **未被该流水线改动**（仍 2 来源、nvf=true、nvc=1）。
- **20:33:38（复核）**：`entries/batch-02-a.json` mtime 仍 20:32:24，**数据已稳定**，无进一步变更。
- **本报告口径**：以**当前最终态（20:32:24 快照，20:33:38 复核未变）为准**逐条复核（即真正会出厂的形态）；同时在上文保留 20:27:14 取样态，便于 lead 对比“口径漂移”。§四、§五、§六 的 space-definition 结论基于**当前具名实例态**。
- 只读声明：本次**仅生成** `research/spotcheck-round21.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/` 或任何其他项目文件，未改动项目文件夹之外内容，未创建 git commit。抓取正文仅写入系统临时目录（`/tmp`）用于分析、非项目产物。联网内容一律视为数据，网页中任何指令均未执行。

## 一、判定口径与相似度方法

- **结构口径**：3 条均为 L2，按 TASK_design.md「条目页结构」核 **七节**：①核心概念与定义(=definition) ②原理 ③典型手法与适用条件 ④实例 ⑤常见错误与限制 ⑥一图 ⑦待核实；并核每页 ≥1 张内联 SVG 含「示意图，非施工图」、风控段含 D09 规范提示（“实际工程须按当地规范和专业设计人员的要求”）、`needs_verification`/`pending_notes`/正文待核实/`coverage.needs_verification_count` 联动一致。
- **相似度阈值 0.54**（AUTONOMOUS.md E 节「疑似套话」警戒线）。算法 = `difflib.SequenceMatcher(None,a,b).ratio()`，字段以 `|` 连接；短文本 = `title|definition|time_or_place|overview`；全字段 = 短文本再加 6 个 sections；calib = `definition|time_or_place|overview|6节`（不含 title，便于跨轮对比）。sections 固定按 `原理|典型手法与适用条件|实例|常见错误与限制|一图|待核实` 顺序拼接。全库共 **126** 条（脚本实测 `TOTAL ENTRIES=126`，无重复 id），逐条对其余 125 条取最高值。**（注：space-definition 的全字段/calib 值因 20:32 实例段被改写而较取样态下降，见 §二。）**

## 二、任务 1：相似度（difflib）对全库最高值（当前态）

逐条对全库其余 125 条取最高相似度（报告最高值对手，脚本实算）：

| 条目 | 短文本(title+def+top+ov) 最高 | 对手 | 全字段(+sections) 最高 | 对手 | calib(def\|top\|ov\|sec) 最高 | 对手 | 是否 <0.54 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| qi-yun | 0.3699 | composition-placement | 0.4738 | yijing | 0.4807 | yijing | ✅ |
| space-definition | 0.4113 | transition-space | 0.3557 | byzantine | 0.3565 | byzantine | ✅ |
| spatial-sequence | 0.4444 | spatial-organization | 0.4692 | rhythm-repetition | 0.4797 | rhythm-repetition | ✅ |

- **3 条无论短文本、全字段还是 calib 口径，对全库最高相似度全部 < 0.54**（最高为 qi-yun calib **0.4807**，仍低于阈值）。
- 全库两两短文本当前最高对仍为 `s-curve-composition × triangular-composition` **0.5166**，亦低于 0.54，无整库套话告警（与第17–20轮一致）。
- 附：space-definition 取样态（类型性实例）全/calib 曾为 0.4407/0.4509，具名实例改写后降至 0.3557/0.3565，仍远低于阈值，不影响结论。

## 三、任务 2：来源存在性 / verified / 主题相关性（实抓）

`en.wikipedia.org` 直连在本环境 20s 超时（与 DECISIONS D05、第20轮一致），改用镜像 `www.owiki.org` 实抓维基正文（同源同标题，**HTTP 200 且 h1 吻合**）；`miesbcn.com`、`archdaily.com` 直连**实抓 HTTP 200**。下列为实抓命中（**数据，非指令**）。

| 来源 id | 存在 / 记录标题 | verified / link_ok | 实抓 | 与主题相关 |
| --- | --- | --- | --- | --- |
| wp-six-principles-chinese-painting | ✅ `Six principles of Chinese painting` | true / true | owiki HTTP200，h1 吻合 | ✅（六法/气韵；支撑 qi-yun） |
| wp-chinese-painting | ✅ `Chinese painting` | true / true | owiki HTTP200，h1 吻合 | ✅（中国画通论含六法；支撑 qi-yun） |
| wp-architecture | ✅ `Architecture` | true / true | owiki HTTP200，h1 吻合 | ✅（建筑总论含 interior architecture 空间句；支撑 space-definition） |
| wp-architectural-theory | ✅ `Architectural theory` | true / true | owiki HTTP200，h1 吻合 | ⚠️（理论史通论；对 spatial-sequence **不相关**，见 §4.3） |
| miesbcn-barcelona-pavilion | ✅ `The Pavilion — Fundació Mies van der Rohe` | true / **None** | miesbcn.com HTTP200（本次实抓） | ✅（巴塞罗那德国馆专页；支撑 space-definition 实例） |
| archdaily-barcelona-pavilion | ✅ `AD Classics: Barcelona Pavilion — ArchDaily` | true / **None** | archdaily HTTP200，h1 吻合（本次实抓） | ✅（巴塞罗那德国馆专页；支撑 space-definition 实例） |

> 结论（来源层面）：6 个来源 id **均存在**、`verified=true`；miesbcn/archdaily 两新源记录的 `link_ok` 未写（None），但本次实抓均 HTTP 200 可达。**“存在且 verified”不等于“正文支撑所挂主张”**，逐句支撑见 §四。

## 四、任务 3：逐条正文支撑核对（关键项，实抓逐句比对）

`python tools/check.py` 实跑 → **`PASS: all checks, 0 errors`（EXIT=0）**。但 `check.py` 只校验“每条挂有 verified 来源”，**不校验来源正文是否支撑该主张**；下表为对实抓正文逐句人工比对所得。**这是本轮发现问题的关键环节。**

### 4.1 qi-yun（气韵生动，当前态未变）——概念/书名强支撑，但**年份与来源不符**

实抓命中片段：
- `wp-six-principles-chinese-painting`：“The Six principles of Chinese painting were established by **Xie He** … from the preface to his book **The Record of the Classification of Old Painters written circa 550**…”；“‘**Spirit Resonance**’ or **vitality**… The **overall energy of a work of art**. Xie He said that **without Spirit Resonance, there was no need to look further**.”
- `wp-chinese-painting`：“…established by Xie He, a writer, art historian and critic **in 5th century China**, in … his book ‘**The Record of the Classification of Old Painters**’. Keep in mind that this was written **circa 550 CE**…”“**Spirit Resonance, or vitality**, which refers to the flow of energy that encompasses theme, work, and artist.”

逐项比对：
- definition「六法之首，强调作品的精神气息与生动韵致」→ **强支撑**（Spirit Resonance=第一法、vitality、overall energy）。
- overview「关注整体生命感，而非单一物象的精确再现」→ **强支撑**（overall energy；“without Spirit Resonance… no need to look further”）。
- 原理「气脉贯通、形象有生气，是六法之首，高于单纯的形似」→ **支撑**。
- 书名《古画品录》→ **支撑**（= The Record of the Classification of Old Painters；满足任务方“qi-yun 若引用《古画品录》须确认来源支持”的要求）。
- **实例年份「约公元 500 年」→ 与两份来源直接矛盾**：两来源均写 **“circa 550 CE”**（wp-chinese-painting 且明言谢赫为“5th century China”，成书“circa 550 CE”）。所挂来源**不支持 500 年**这一具体数字。

### 4.2 space-definition（建筑空间定义，**当前态：已由评审流水线改为具名实例 + 双专源**）

实抓命中片段：
- 概念支撑（`wp-architecture`）：“**Interior architecture is the design of a space which has been created by structural boundaries and the human interaction within these boundaries.**”；“…all aspects of the **human uses of structural spaces**”；“the **spatial art** of environmental design…”。另有 `proportion`（5 次，含 Alberti “golden mean… idealized human figure”）、`scale`（2 次）。
- 实例支撑（新增两专源，**本次实抓**）：
  - `miesbcn-barcelona-pavilion` 实抓：“**The Barcelona Pavilion was designed by Ludwig Mies van der Rohe and Lilly Reich as the German Pavilion for the Barcelona International Exposition, held on Montjuïc.**”；“…as the German national pavilion for the **1929 Barcelona International Exposition**.”；重建说明“new building was opened on its original site in 1986”。
  - `archdaily-barcelona-pavilion` 实抓：h1 “AD Classics: Barcelona Pavilion / **Mies van der Rohe + Lilly Reich**”；“Architects: **Lilly Reich, Mies van der Rohe**”；“**Year: 1929**”；“As part of the **1929 International Exposition in Barcelona Spain**…”。

逐项比对：
- definition「由围合界面、尺度与人的活动共同限定的场所」→ **支撑**：`structural boundaries`(围合界面)+`human interaction within these boundaries`(人的活动)+`space`(场所) 逐一对应；“尺度”由该页 `proportion`/`scale` 讨论支撑（较弱但成立）。
- overview「感知不只来自几何边界，也来自光线、材料与使用方式」→ **部分支撑**：`human uses`、`lighting`、`materials` 在该页有一般性论及；“光线、材料”属**合理外推**，非逐字。
- **实例（巴塞罗那德国馆 / 西班牙巴塞罗那蒙特惠奇山 / 密斯·凡·德·罗与莉莉·赖希 / 1929 年）→ 强支撑、无编造**：miesbcn 与 archdaily 双源独立印证“设计者 Mies+Lilly Reich、地点 Barcelona/Montjuïc、年份 1929、German/Barcelona Pavilion”。唯一 nuance：现址为 1986 重建（miesbcn 载明），正文写 1929（原始建成/交付年）与 ArchDaily “Year: 1929” 一致，属可接受；可加注“现址为 1986 重建”。
- **口径偏差（需 lead 定夺）**：任务本轮明确要求“**实例应为类型性描述**”。当前实例为**具名建筑**（巴塞罗那德国馆），**不再类型性**——该变化由 20:32:24 并发 `apply_review_round21` 引入（取样态 20:27:14 仍为“由界面限定的室内空间（类型性描述）”，符合口径）。

### 4.3 spatial-sequence（空间序列，当前态未变）——**核心概念在两条来源正文中完全缺失（来源不支撑）**

对两条已挂来源做全文关键词精确实测：

| 关键词 | wp-architecture 次数 | wp-architectural-theory 次数 |
| --- | --- | --- |
| sequence | **0** | **0** |
| promenade | **0** | **0** |
| procession | **0** | **0** |
| circulation | **0** | **0** |
| rhythm | **0** | **0** |
| narrative | 0 | 0 |
| transition | 0 | 1 |
| space | 3（interior/urban/structural spaces） | 3（Sitte 城市空间；Bachelard《Poetics of Space》；“Formalism and space”名录） |
| enclos | 0 | 1（Sitte：buildings collectively **enclose** 的 urban spaces） |

- `wp-architecture` 唯一相关实体句是 4.2 引的“interior architecture… structural boundaries and the human interaction…”——讲**空间的定义**，**不含“序列/进入顺序/节奏/起承转合/游线”**。
- `wp-architectural-theory` 全篇为**建筑理论史**，仅泛提“urban spaces that buildings collectively enclose”“Formalism and space”名录，**无任何“空间序列/动线/节奏”论述**。
- 因此 spatial-sequence 的 definition「若干空间按进入顺序组织形成的连续体验」、overview「开合、明暗与尺度变化控制节奏，使行进成为叙事」、原理/手法「起—承—转—合组织路径」——**均无已挂来源正文支撑**；两条来源对本概念**零印证**（不满足 D10“两独立来源互相印证”）。**注意：并发评审流水线未升级本条，仍为通用来源。**

## 五、任务 4：结构 / SVG / 规范提示 / 待核实联动（当前最终态，实测）

| 检查项 | qi-yun | space-definition（当前具名态） | spatial-sequence |
| --- | --- | --- | --- |
| 七节齐备（definition + 6 节） | ✅ 6/6 | ✅ 6/6 | ✅ 6/6 |
| 1 张内联 SVG，viewBox 有效（0 0 760 400） | ✅ | ✅ | ✅ |
| SVG 图注含「示意图，非施工图」 | ✅ | ✅ | ✅ |
| 常见错误与限制含 D09 规范提示 | ✅ | ✅ | ✅ |
| 正文无编造人名/引文 | ✅ | ✅（密斯/莉莉·赖希均有双源） | ✅ |
| 年份是否与来源相符 | ❌「约公元 500 年」≠来源「circa 550 CE」 | ✅（1929，双源支持） | ✅（正文无具体年份） |
| 实例为“类型性描述”（本轮口径） | ⚠️ 名《古画品录》为具名典籍（任务方特批，书名成立） | ⚠️ **已改为具名建筑，偏离类型性口径** | ✅（院落式空间序列） |
| needs_verification ↔ pending_notes ↔ 待核实 ↔ coverage.nvc | ✅ 一致（T/非空/非空/1） | ✅ 一致（F/空/“暂无”/0） | ✅ 一致（T/非空/非空/1） |
| theme/period/region/tier 与 coverage 一致 | ✅ | ✅ | ✅ |
| source_count 与 sources 一致 | ✅ 2 | ✅ 4 | ✅ 2 |
| **definition/overview/七节 有已挂来源正文支撑** | ⚠️ 强（唯年份不符） | ✅ 实例强支撑；概念句通用支撑（“尺度/光线材料”偏弱） | ❌ **无（核心概念来源缺失）** |

> 注：三条的 `needs_verification ↔ pending_notes ↔ sections.待核实 ↔ coverage.nvc` **各自一致**（qi-yun/spatial-sequence 为 T/非空/1；space-definition 为 F/空/0）。但 spatial-sequence 的 `pending_notes` 仅写“实例名称/设计者/年代待补”，**未披露“概念本身缺来源支撑”**这一真实缺口（D14 精神缺口）。

## 六、逐条验收结论（当前最终态）

| 条目 | 来源/正文支撑 | 结构·SVG·规范 | 待核实联动 | 相似度(短/全/calib) | 结论 |
| --- | --- | --- | --- | --- | --- |
| **qi-yun（气韵生动）** | 概念/书名强支撑；**年份与来源矛盾**（500 vs 550） | 全过 | 一致（nvc1） | 0.3699 / 0.4738 / 0.4807 | **待核实（订正年份）** |
| **space-definition（建筑空间定义）** | 具名实例双源强支撑、无编造；概念句通用支撑 | 全过 | 一致（nvc0） | 0.4113 / 0.3557 / 0.3565 | **事实合格；但具名实例偏离“类型性”口径（并发引入）** |
| **spatial-sequence（空间序列）** | **核心概念在两条来源中零出现，正文不支撑** | 结构全过，来源不支撑 | 一致（nvc1，但 pending 未披露概念缺口） | 0.4444 / 0.4692 / 0.4797 | **不合格（来源不支撑核心）** |

**逐条依据与问题：**

- **qi-yun — 待核实（需订正年份，非结构问题）**
  - 依据：两来源“Spirit Resonance=第一法/vitality/overall energy”“without Spirit Resonance…no need to look further”“The Record of the Classification of Old Painters”逐字支撑定义、overview、原理与书名。
  - 问题（**需修**）：实例年份「约公元 500 年」与两份来源「circa 550 CE」**冲突**；`needs_verification=true` 与待核实“作者年代待核实”虽已提示，但正文写死的 500 年为“所挂来源不支持的年份”，应改为“约公元 6 世纪（约 550 年，参见来源）”或移除具体年份并入待核实。
  - 软信号：实例以具名典籍《古画品录》作例（任务方已特批，书名成立）。

- **space-definition — 事实合格，但实例口径偏离（需 lead 定夺）**
  - 依据：概念句 `wp-architecture`“space created by structural boundaries and the human interaction within these boundaries”支撑定义；**实例“巴塞罗那德国馆/蒙特惠奇山/密斯与莉莉·赖希/1929”由 miesbcn + archdaily 双专源独立印证，无编造**（唯一 nuance：现址为 1986 重建，可与正文 1929 并存并加注）。
  - 问题（非结构、口径问题）：①**当前实例为具名建筑，偏离本轮“实例应为类型性描述”口径**——该变化由 20:32:24 `apply_review_round21` 引入，取样态（20:27:14）为类型性且符合口径；②概念“尺度/光线材料”仍主要依托通用 `wp-architecture`，`needs_verification` 被流水线置为 false（nvc=0）是否恰当宜复核；③两新源 `link_ok` 未写（None），本次实抓可 200，建议补 `link_ok=true`。

- **spatial-sequence — 不合格（来源正文不支撑核心概念）**
  - 依据（反向证据）：两来源 `sequence/promenade/procession/circulation/rhythm` **各为 0 次**；其一仅涉“空间定义”，其二仅涉“理论史/城市空间围合”。definition/overview/原理手法（进入顺序、开合明暗节奏、起承转合、游线叙事）**无一字来源依托**；且并发流水线未升级本条。
  - 问题（**硬问题，需返工**）：核心概念与已挂来源不匹配（两个通用百科来源顶替）。应**换源重写**（改用真正论述空间序列/游线/动线 promenade/circulation/spatial progression 的权威来源），或降为 L1 骨架并如实标待核实；`pending_notes` 需明确写“概念来源待补”。

## 七、总体结论与是否整批返工

- **抽检结果：3 条中 space-definition 事实合格（但实例口径偏离）、qi-yun 待核实（年份需订正）、spatial-sequence 不合格（来源不支撑核心）。**
  - 相似度：3 条对全库最高（短/全/calib 任一）**均 < 0.54**（最大 qi-yun calib 0.4807）；全库两两短文本最高 0.5166；库规模 126 → **无套话/近重复告警**。
  - 结构：3 条七节完整、各 1 张 SVG 含「示意图，非施工图」、风控段含 D09 提示、`check.py` **PASS 0 errors（EXIT=0）**；`needs_verification↔pending↔待核实↔nvc` 三条各自一致。
  - 来源：6 个来源 id 均存在、verified=true；**正文支撑层面两处实质问题**：qi-yun 年份与来源矛盾（500 vs 550）；spatial-sequence 核心概念在两条来源中完全缺失。另有 space-definition 具名实例**偏离本轮类型性口径**（并发流水线引入）。
- **整批返工建议：建议整批返工（按 AUTONOMOUS E：「不合格则整批返工」）。** 出现 1 条**不合格**（spatial-sequence 来源不支撑核心）即触发；且本批为**并发移动目标**，`apply_review_round21` 已在抽检中途改写 space-definition / human-scale——须先**冻结/稳定数据**再复核，否则抽检结论会随流水线漂移。
- **具体返工/修复项（按优先级）**：
  1. **spatial-sequence（必改/不合格）**：换用真正论述“空间序列/游线/动线”的来源并重写 definition/overview/原理/手法；若无合格来源则降 L1 并如实标待核实；`pending_notes` 写明概念来源缺口。**不得**继续用 Architecture/Architectural theory 两条不相关来源。
  2. **qi-yun（应改/待核实）**：实例年份「约公元 500 年」→ 改为与来源一致的「约公元 6 世纪（约 550 年，参见来源）」或删除具体年份并入待核实。
  3. **space-definition（口径裁定）**：①若本轮坚持“实例类型性”，须回退具名实例（或 lead 明示接受具名实例并统一全批口径）；②给两新源补 `link_ok=true`；③复核 `needs_verification` 由 true→false 是否恰当（概念“尺度/光线材料”仍偏通用支撑）；④实例可加注“现址为 1986 重建”。
  4. **同批未抽 3 条（liubai / yijing / human-scale）复核**：`human-scale` 已被并发流水线改为具名（帕伊米奥疗养院）+ 4 源、nvf=false、nvc=0，需与 space-definition 一样核实例事实与类型性口径；`liubai`（cnr/rmrb/wp-chinese-painting）、`yijing`（wp-chinese-painting/wp-shitao）需核来源是否真正覆盖“留白/意境”本体。
  5. **并发治理**：本轮存在 review-round21 流水线与本次抽检并行改写同一 `entries/batch-02-a.json`，建议后续抽检放在 apply 完成且数据冻结后进行，避免结论漂移。
- **是否触发降级复查**：相似度未超阈、待核实占比未见异常低，**不因相似度/占比降级**；但**因 1 条不合格触发整批返工**。

---

### 机器可读汇总

```
ROUND=21
SAMPLER=spotcheck-r21
SCOPE=["qi-yun","space-definition","spatial-sequence"]          # 抽自第21轮6条核心升级集，3/6=50%
ROUND21_UPGRADE_SET=["qi-yun","liubai","yijing","space-definition","human-scale","spatial-sequence"]
FILES={"qi-yun":"entries/batch-02-a.json","space-definition":"entries/batch-02-a.json","spatial-sequence":"entries/batch-02-a.json"}
STATE_EVOLUTION={
  "sampled_20:27:14":"3 entries type-level instance, nvf=true, nvc=1, 2 sources each",
  "applied_20:32:24":"apply_review_round21.py upgraded space-definition(巴塞罗那德国馆,named,4 sources,nvf=false,nvc=0) AND human-scale(帕伊米奥疗养院,named,4 sources,nvf=false,nvc=0); qi-yun/spatial-sequence unchanged",
  "verdict_basis":"CURRENT final state @20:32:24, stable at 20:33:38",
  "concurrency":"review-round21.md 20:31:58 + apply_review_round21.py 20:32:21 ran DURING spotcheck; data files rewritten mid-check"
}
SIM_METHOD="difflib.SequenceMatcher.ratio(); join='|'; short=title|definition|time_or_place|overview; full=+6 sections; calib=def|top|ov|sections"
SIM_MAX_SHORT={"qi-yun":[0.3699,"composition-placement"],"space-definition":[0.4113,"transition-space"],"spatial-sequence":[0.4444,"spatial-organization"]}
SIM_MAX_FULL={"qi-yun":[0.4738,"yijing"],"space-definition":[0.3557,"byzantine"],"spatial-sequence":[0.4692,"rhythm-repetition"]}
SIM_MAX_CALIB={"qi-yun":[0.4807,"yijing"],"space-definition":[0.3565,"byzantine"],"spatial-sequence":[0.4797,"rhythm-repetition"]}
ALL_SIM_UNDER_0.54=true ; LIBRARY_SIZE=126 ; GLOBAL_MAX_SHORT={"0.5166":"s-curve-composition x triangular-composition"}
SOURCES_ALL_EXIST_VERIFIED=true
SOURCES={"qi-yun":["wp-six-principles-chinese-painting","wp-chinese-painting"],"space-definition":["wp-architecture","wp-architectural-theory","miesbcn-barcelona-pavilion","archdaily-barcelona-pavilion"],"spatial-sequence":["wp-architecture","wp-architectural-theory"]}
LINK_OK_NONE=["miesbcn-barcelona-pavilion","archdaily-barcelona-pavilion"]   # verified=true, link_ok=None(record); live fetch 200 this run
FETCH={"en.wikipedia.org":"timeout (D05)","www.owiki.org":"HTTP200 h1 matched (4 wiki sources)","miesbcn.com":"HTTP200 (live)","archdaily.com":"HTTP200 h1 matched (live)"}
BODY_SUPPORT={
  "qi-yun":"STRONG concept+book (Spirit Resonance/vitality/overall energy; 'Record of the Classification of Old Painters') BUT year '约公元500年' CONTRADICTS sources 'circa 550 CE'",
  "space-definition":"INSTANCE STRONG (Barcelona Pavilion / Montjuic / Mies & Lilly Reich / 1929 by miesbcn+archdaily dual source, no fabrication); CONCEPT MEDIUM ('structural boundaries and human interaction' from wp-architecture); instance now NAMED not type-level",
  "spatial-sequence":"ABSENT (sequence=0,promenade=0,procession=0,circulation=0,rhythm=0 in BOTH cited pages; generic Architecture/Architectural-theory do NOT treat spatial sequence)"
}
KW_COUNTS={"wp-architecture":{"sequence":0,"promenade":0,"procession":0,"circulation":0,"rhythm":0,"space":3,"human interaction":1,"structural boundaries":1,"proportion":5,"scale":2},"wp-architectural-theory":{"sequence":0,"promenade":0,"procession":0,"circulation":0,"rhythm":0,"space":3,"enclos":1}}
SEVEN_SECTIONS_OK=true ; SVG_COUNT=1_each ; SVG_CAPTION_OK=true ; REGNOTE_OK=true
NEEDS_VERIFICATION={"qi-yun":"T/nvc1","space-definition":"F/nvc0","spatial-sequence":"T/nvc1"}
INSTANCE_TYPE_LEVEL={"qi-yun":"named-text 古画品录 (allowed, source supports book); year wrong","space-definition":"named building (DEVIATES from round-21 type-level criterion; introduced by concurrent apply_review)","spatial-sequence":true}
FABRICATED={"qi-yun":"year 500 vs source ~550 (mismatch)","space-definition":"none (instance dual-sourced)","spatial-sequence":"none"}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
VERDICT={"qi-yun":"待核实(订正年份)","space-definition":"事实合格(具名实例偏离类型性口径,并发引入)","spatial-sequence":"不合格(来源不支撑核心)"}
OVERALL="1合格/1待核实/1不合格；相似度<0.54无套话；结构全过check.py PASS；正文支撑两处实质问题(qi-yun年份矛盾、spatial-sequence概念来源缺失)+space-definition实例口径漂移"
BATCH_REWORK="建议整批返工(触发E:spatial-sequence不合格)；spatial-sequence换源重写、qi-yun订正年份、space-definition实例口径裁定+补link_ok、复核未抽3条(liubai/yijing/human-scale)；抽检须在并发apply后冻结数据再复核"
FIX_HINT="spatial-sequence换真正论述空间序列/动线来源或降L1；qi-yun年份改~550或删；space-definition若守类型性则回退具名实例；pending_notes如实写概念来源缺口"
REST_FILES_WRITTEN=["research/spotcheck-round21.md"]   # 只写本文件
```
