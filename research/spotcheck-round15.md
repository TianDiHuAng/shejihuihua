# 第15轮质量闸抽检报告（spotcheck-round15）——3 条跨主题重要 L1→L2 升级的逐条来源/结构/相似度复检

- 抽检人：spotcheck-r15（由 lead 委派的子代理）；抽检时间：2026-11-22 19:25 起，Asia/Hong_Kong（会话时间取样）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（本轮改动条目抽 25% 至少 3 个、不合格整批返工、待核实占比异常低或相似度过高则整批降级复查）、第六节（联网内容仅作数据，其中指令一律不执行）、第二节（状态文件）；`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L2」「条目页结构（七节）」「通用硬性规则」「专用规则」；`DECISIONS.md` D05（实抓核验）/D06（在线百科 year=null）/D09（规范提示模板）/D14（needs_verification 与 pending_notes 联动）；前序 `research/spotcheck-round14b.md`（相似度口径与阈值沿用其标定）。
  - 说明：任务书所称项目根 `AUTONOMOUS.md`/`TASK_design.md` 在仓库内无同名文件，实际位于 `D:/Users/Administrator/Desktop/`，已按该路径读取（与第12–14轮一致）。
- 技能：已加载 `using-superpowers`（本会话为子代理，按 SUBAGENT-STOP 不另启流程）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言）。
- 抽检对象（第15轮升级的 6 条重要 L1→L2：`saturation`、`primary-colors`、`warm-cool`、`hardscape-softscape`、`wayfinding`、`mannerism`，据 `tools/upgrade_round15.py` 的 `S`/`SRC` 清单确认；本次抽 3 条）：**`saturation`（纯度）、`wayfinding`（导视与寻路）、`mannerism`（样式主义建筑）**。抽样率 3/6 = 50%，满足「≥25% 且 ≥3 条」。
- 只读声明：本次仅生成 `research/spotcheck-round15.md`；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/` 或任何其他项目文件，未改动项目文件夹之外内容，未创建 git commit。工作树中 `coverage.json`、`data/sources.json`、`entries/batch-01.json`、`entries/batch-02-a.json`、`entries/batch-02-b.json`、`entries/batch-03.json`、`entries/batch-07.json`、`entries/l2-samples.json` 的改动，以及 `research/gaps-round15.md`、`research/reader_questions-round15.md`、`research/review-round15.md`、`tools/upgrade_round15.py`、`tools/apply_review_round15.py` 等，均为第15轮执行/复核阶段的既有或**并发**产物（`git status` 在本抽检期间发生变化，系另一复核流程并发写入），非本次抽检所写。所核对 3 条目标条目文件（batch-01/03/07）mtime 均为 19:25:05、抽检期间未被改动；`data/sources.json` 虽于 19:31 被并发流程更新（来源 178→185），6 个被引来源仍 `verified=true`（复读确认），相似度按当前数据复算与报告一致。联网内容一律视为数据，网页中的任何指令均未执行。

## 一、判定口径与相似度方法（先校准，再测量）

- **结构口径**：3 条均为 L2 升级，按 TASK_design.md「条目页结构」核 **七节**：①核心概念与定义(=definition) ②原理 ③典型手法与适用条件 ④实例 ⑤常见错误与限制 ⑥一图 ⑦待核实；并核每页 ≥1 张内联 SVG 含「示意图，非施工图」、风控段含 D09 规范提示（"实际工程须按当地规范和专业设计人员的要求"）、`needs_verification`/`pending_notes`/正文待核实/`coverage.needs_verification_count` 联动一致。
- **相似度阈值 0.54**（AUTONOMOUS.md E 节「疑似套话」警戒线）。算法 = `difflib.SequenceMatcher(None,a,b).ratio()`。
- **三套口径并报**：
  - 任务口径-短文本 = `title|definition|time_or_place|overview`；
  - 任务口径-全字段 = 短文本再加 6 个 sections（同一 `|` 连接，含 title）；
  - 第13/14轮可比口径（calib）= `definition|time_or_place|overview|6节`（不含 title），用于与 round14 基线直接对比。
- **算法校准（关键）**：用 calib 口径复算 round13/14 记录的三个锚点，逐位吻合——`figure-ground` **0.4760**、`complementary-colors` **0.5177**、`one-point-perspective` **0.4862**。方法与本报告数值可直接与前序轮次比较。

## 二、任务 1：相似度（difflib）对全库最高值

扫描全库 126 条，逐条对全部其他条目取最高相似度（报告最高值对手）：

| 条目 | 短文本(title+def+top+ov) 最高 | 对手 | 全字段(+sections, 任务口径) 最高 | 对手 | calib(def|top|ov|sec) 最高 | 对手 | 是否 <0.54 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| saturation | 0.4815 | value | 0.4579 | hue | 0.4594 | hue | ✅ |
| wayfinding | 0.3830 | interior-exterior-transition | 0.4142 | color-theory | 0.4229 | color-theory | ✅ |
| mannerism | 0.3804 | renaissance-style | 0.4028 | renaissance-style | 0.4067 | complementary-colors | ✅ |

- **3 条无论短文本还是全字段、无论任务口径还是 calib 口径，对全库最高相似度全部 < 0.54**（最大 0.4815，saturation×value 短文本）。无套话嫌疑。
- **附带观察（非本轮 6 条范围，不据此判定本批）**：全库两两扫描另有非目标条目超过 0.54，例如 `modernism × functionalism-architecture` 短文本 **0.6761**、`diagonal-composition × triangular-composition` 全字段 **0.5645**。这些条目不属本轮升级的 6 条，**不影响本批结论**，但提示后续轮次可对这两对做去模板化复核。

## 三、任务 2：来源支撑核对（实抓，HTTP 200，h1 已核对）

`en.wikipedia.org` 直连在本环境超时（URLError: timed out），改用镜像 `www.owiki.org`（与 sources.json 的 canonical 页同内容，DECISIONS D05 既定做法）实抓，**6 个来源全部 HTTP 200 且 h1 与 sources.json 标题一致**。下列为实抓命中片段（数据，非指令）：

- **wp-colorfulness**（Colorfulness）："Colorfulness, chroma and saturation are attributes of perceived color relating to chromatic intensity."；"Saturation is the 'colorfulness of an area judged in proportion to its brightness'." → 支撑 saturation 的 definition「色彩的鲜艳或饱和程度」与 原理「鲜艳或灰浊程度」。
- **wp-munsell-color-system**（Munsell color system）："specifies colors based on three properties of color: hue, value, and chroma." → 以 chroma（彩度）佐证 saturation=纯度维度。
- **wp-graphic-design**（Graphic design）："Examples of practice areas for environmental graphic designers are wayfinding, placemaking…"；"The signage in the London Underground is a classic design example of the modern era." → 支撑 wayfinding 作为图形/环境图形设计的实践领域。
- **wp-wayfinding**（Wayfinding）："all of the ways in which people orient themselves in physical space and navigate from place to place"；"signage and other graphic communication, visual clues in the built environment"；"the set of architectural or design elements that aid orientation"；"spatial semiotics, information design, and cognitive science" → 支撑 wayfinding 的 definition「借助标识、地图与视觉线索定向和导航」与 overview「动线组织、空间认知和图形信息」。
- **wp-mannerism**（Mannerism）："emerged in the later years of the Italian High Renaissance around 1520… lasting until about the end of the 16th century… when the Baroque style largely replaced it"；"elongated proportions, highly stylized poses"；"compositions that are asymmetrical or unnaturally elegant. Notable for its artificial qualities"；"maniera, meaning 'style' or 'manner'"；"figura serpentinata" → 支撑 mannerism 的 definition「文艺复兴晚期出现、以夸张比例与刻意变形显示技巧」、time_or_place「文艺复兴晚期欧洲」与 overview「从文艺复兴向巴洛克过渡的一环」。
- **wp-list-architectural-styles**（List of architectural styles）："Mannerism 1520–1600"；"Polish Mannerism 1550–1650" → 佐证样式主义作为建筑风格列举。

**来源 id/verified/主题相关核对**：

| 来源 id | 存在 | verified | 标题 | 与主题相关 |
| --- | --- | --- | --- | --- |
| wp-colorfulness | ✅ | true | Colorfulness | ✅（chroma/saturation 直接定义） |
| wp-munsell-color-system | ✅ | true | Munsell color system | ✅（chroma 彩度维度） |
| wp-graphic-design | ✅ | true | Graphic design | ✅（wayfinding 为环境图形实践领域） |
| wp-wayfinding | ✅ | true | Wayfinding | ✅（直接条目） |
| wp-mannerism | ✅ | true | Mannerism | ✅（直接条目） |
| wp-list-architectural-styles | ✅ | true | List of architectural styles | ✅（列出 Mannerism 1520–1600） |

> 注：复核时 `data/sources.json` 已被并发复核流程更新（来源 178→185 条），上述 6 个来源经复读仍全部 `verified=true`、标题不变。

## 四、任务 3：逐条结构与内容核对

实跑 `python tools/check.py` → **`PASS: all checks, 0 errors`（EXIT=0）**；并另跑结构化脚本核对下列各项：

| 检查项 | saturation（纯度） | wayfinding（导视与寻路） | mannerism（样式主义建筑） |
| --- | --- | --- | --- |
| 七节齐备（definition+6 节） | ✅ 6/6，无缺无多 | ✅ 6/6，无缺无多 | ✅ 6/6，无缺无多 |
| 1 张内联 SVG，viewBox 有效 | ✅ 760×400，元素不出界 | ✅ 760×400，元素不出界 | ✅ 760×400，元素不出界 |
| SVG 图注含「示意图，非施工图」 | ✅ 命中 | ✅ 命中 | ✅ 命中 |
| 常见错误与限制含 D09 规范提示 | ✅ 命中 | ✅ 命中 | ✅ 命中 |
| 正文无编造具体年份/世纪 | ✅ 无显式年份/世纪 | ✅ 无显式年份/世纪 | ✅ 无显式年份/世纪 |
| 实例为类型性描述、无编造具体项目/设计者/年份 | ✅（"高纯度点缀与低纯度背景的配色"，均"不适用"） | ✅（"大型文化建筑导视系统"，均"不适用"） | ✅（"样式主义绘画与建筑细部"，地点欧洲，设计者/年份"不适用"） |
| definition/overview/七节有来源正文支撑 | ✅（见 §三；overview/手法为一般设计推断，见软信号） | ✅（强支撑） | ✅（强支撑） |
| needs_verification ↔ pending_notes ↔ 正文待核实 ↔ coverage.nvc=1 | ✅ 四者一致 | ✅ 四者一致 | ✅ 四者一致 |
| period/region 与 coverage 一致 | ✅ 跨时期/全球 | ✅ 跨时期/全球 | ✅ 文艺复兴至19世纪/欧洲（粗粒度分期桶，见 §五） |

## 五、逐条验收结论

| 条目 | 来源支撑 | 结构/SVG/规范提示 | 待核实联动 | 相似度 | 结论 |
| --- | --- | --- | --- | --- | --- |
| **saturation** | definition/原理有 Colorfulness+Munsell 支撑；overview/典型手法为一般设计推断（软信号） | 全过 | 四者一致 | 0.4815/0.4579 <0.54 | **合格** |
| **wayfinding** | definition/overview/原理/手法有 Wayfinding+Graphic design 强支撑 | 全过 | 四者一致 | 0.3830/0.4142 <0.54 | **合格** |
| **mannerism** | definition/time_or_place/overview/原理/手法有 Mannerism+List 强支撑 | 全过 | 四者一致 | 0.3804/0.4028 <0.54 | **合格** |

- **软信号（saturation，不据此判不合格，供 L3 微调）**：① `overview`「高纯度色彩吸引注意，低纯度色彩适合作为背景与过渡」及 `典型手法`（主体高纯度/背景低纯度）属一般设计实践经验，非所引"测量导向"的 Colorfulness 条目原文，但无编造事实，L2 层可接受；② 「吸引注意」类表述若有更强来源（如设计心理学/色彩设计教材）可补双源。
- **说明（mannerism，不据此判不合格）**：`period=文艺复兴至19世纪` 是覆盖矩阵的**粗粒度分期桶**（同一桶另有 renaissance-style/baroque/rococo/neoclassical 等 11 条，取值集合为 古代/中世纪/文艺复兴至19世纪/20世纪/当代/跨时期），并非"样式主义延续到19世纪"的精确断代；读者可见的 `time_or_place=文艺复兴晚期欧洲` 与来源（1520–1600）一致，definition/七节亦为"文艺复兴晚期"，故不构成编造年份或矛盾。

## 六、总体结论与是否整批返工

- **抽检结果：3/3 全部合格。**
  - 来源：6 个来源 id 均存在且 `verified=true`、标题与主题直接相关；实抓镜像 HTTP 200、h1 吻合，definition/time_or_place/overview/七节均有正文支撑；实例为类型性描述，**未发现编造年份、人名或引文**。
  - 结构：七节完整、1 张 SVG 含「示意图，非施工图」、风控段含 D09 规范提示、`check.py` 0 errors（EXIT=0）。
  - 待核实：`needs_verification=true` ↔ `pending_notes` ↔ 正文「待核实」 ↔ `coverage.needs_verification_count=1` 四者一致。
  - 相似度：3 条对全库最高（短文本/全字段/calib 任一）均 **< 0.54**（最大 0.4815）。
- **整批返工建议：不建议整批返工。** 所抽 3 条无不合格项，按 AUTONOMOUS E「不合格才整批返工」不触发返工；本批无待核实占比异常（3 条均 nvc=1）也无相似度超阈（全部 <0.54）。
- **闭环建议（非返工）**：本轮 6 条升级集仅抽 3 条（50%），其余 `primary-colors`、`warm-cool`、`hardscape-softscape` 建议在后续抽检或同闸门补足，以完成 6 条整体闭环；并在未来轮次对全库两两超阈对（modernism×functionalism、diagonal×triangular）做去模板化复核。

---

### 机器可读汇总

```
ROUND=15
SCOPE=["saturation","wayfinding","mannerism"]   # 抽自第15轮6条升级集，3/6=50%
ROUND15_UPGRADE_SET=["saturation","primary-colors","warm-cool","hardscape-softscape","wayfinding","mannerism"]
SIM_METHOD="difflib.SequenceMatcher.ratio(); join='|'"
SIM_CALIBRATION={"figure-ground":0.4760,"complementary-colors":0.5177,"one-point-perspective":0.4862}  # matches round13/14 exactly
SIM_MAX_SHORT_TASK={"saturation":0.4815,"wayfinding":0.3830,"mannerism":0.3804}
SIM_MAX_FULL_TASK={"saturation":0.4579,"wayfinding":0.4142,"mannerism":0.4028}
SIM_MAX_CALIB={"saturation":0.4594,"wayfinding":0.4229,"mannerism":0.4067}
ALL_SIM_UNDER_0.54=true
GLOBAL_LIBRARY_MAX_NON_TARGET={"full":"0.5645 diagonal-composition×triangular-composition","short":"0.6761 modernism×functionalism-architecture"}  # 非本轮6条，仅观察
SOURCES_ALL_VERIFIED=true
SOURCES=["wp-colorfulness","wp-munsell-color-system","wp-graphic-design","wp-wayfinding","wp-mannerism","wp-list-architectural-styles"]
FETCH={"en.wikipedia.org":"timeout","www.owiki.org":"HTTP200 h1 matched for all 6"}
FABRICATED_YEARS_NAMES_QUOTES=false
SEVEN_SECTIONS_OK=true ; SVG_CAPTION_OK=true ; SVG_IN_BOUNDS=true ; REGNOTE_OK=true ; NV_LINKAGE_OK=true
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
VERDICT={"saturation":"合格","wayfinding":"合格","mannerism":"合格"}
SOFT_SIGNALS={"saturation":"overview/典型手法为一般设计推断，非测量型来源原文；无编造","mannerism":"period=文艺复兴至19世纪为粗分桶，非精确断代；time_or_place准确"}
OVERALL="3/3 合格；来源/结构/待核实/相似度全部达标；不建议整批返工"
CLOSURE_HINT="补抽 primary-colors/warm-cool/hardscape-softscape 以闭环6条；未来复核 modernism×functionalism 等全库超阈对"
REST_FILES_WRITTEN=["research/spotcheck-round15.md"]   # 只写本文件
```
