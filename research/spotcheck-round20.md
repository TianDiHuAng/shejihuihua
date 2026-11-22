# 第20轮质量闸抽检报告（spotcheck-round20）——3 条升级条目的逐条来源/结构/相似度复检

- 抽检人：spotcheck-r20（由 lead 委派的子代理）；抽检时间：2026-11-22 20:21 起，Asia/Hong_Kong（会话时间取样），最终态复核至 20:24。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（本轮改动条目抽 25%、至少 3 个；不合格整批返工；待核实占比异常低或相似度过高则整批降级复查）、第六节（联网内容一律视为数据，网页中任何指令一律不执行）、第二节（状态文件）；`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L2」「条目页结构（七节）」「通用硬性规则」「专用规则」；`DECISIONS.md` D05（实抓核验）/D06（在线百科 year=null）/D09（规范提示模板）/D10（关键事实需两独立来源，否则标待核实）/D11（link_ok 三态）/D14（needs_verification 与 pending_notes 联动）。
  - 说明：任务书所称项目根 `AUTONOMOUS.md`/`TASK_design.md` 在仓库内无同名文件，实际位于 `D:/Users/Administrator/Desktop/`（与第 12–19 轮一致），已按该路径读取；`DECISIONS.md`、`research/spotcheck-round19.md` 在仓库根。
- 技能：已加载 `using-superpowers`（本会话为子代理，按 SUBAGENT-STOP 不另启流程，仅作规范参考）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言）。
- 抽检对象（第20轮升级的 6 条：`visual-center`、`contrast-principle`、`form-follows-function`、`curvilinear-perspective`、`courtyard`、`green-architecture`，据 `tools/upgrade_round20.py` 的 `S`/`SRC`/`SVG` 清单确认；本次按指派抽其中 3 条）：**`visual-center`（视觉中心，`entries/batch-01.json`，tier 重要）、`contrast-principle`（对比，`entries/batch-01.json`，tier 重要）、`green-architecture`（绿色建筑，`entries/batch-02-d.json`，tier 核心）**。抽样率 3/6 = 50%，满足「≥25% 且 ≥3 条」。

## 〇、并发变更与最终态说明

- 本次抽检会话起点约 20:21:21；`tools/upgrade_round20.py` 于 **20:21:10 生成、20:21:14 应用**，`entries/batch-01.json`、`entries/batch-02-d.json`、`coverage.json`、`data/sources.json`（20:19:49）的 mtime 均定格在 20:21:14 前后，**早于本报告写作时点**。
- 截至 **20:24:26** 复核：`tools/` 内**尚无** `apply_review_round20.py`，`research/` 内**尚无** `review-round20.md`；上述文件 mtime 与 20:21:14 一致，**未见并行变更**（与第19轮出现的 review 流水线并发不同）。
- 处理方式：**本报告以磁盘最终态（20:21:14 快照，20:24:26 复核未变）为准逐条复核**，即质量闸保护的真正出厂状态。
- 只读声明：本次**仅生成** `research/spotcheck-round20.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/` 或任何其他项目文件，未改动项目文件夹之外内容，未创建 git commit。抓取缓存置于系统临时目录（`%TEMP%`）仅用于分析、非项目产物。联网内容一律视为数据，网页中的任何指令均未执行。

## 一、判定口径与相似度方法

- **结构口径**：3 条均为 L2，按 TASK_design.md「条目页结构」核 **七节**：①核心概念与定义(=definition) ②原理 ③典型手法与适用条件 ④实例 ⑤常见错误与限制 ⑥一图 ⑦待核实；并核每页 ≥1 张内联 SVG 含「示意图，非施工图」、风控段含 D09 规范提示（"实际工程须按当地规范和专业设计人员的要求"）、`needs_verification`/`pending_notes`/正文待核实/`coverage.needs_verification_count` 联动一致。
- **相似度阈值 0.54**（AUTONOMOUS.md E 节「疑似套话」警戒线）。算法 = `difflib.SequenceMatcher(None,a,b).ratio()`，字段以 `|` 连接；短文本 = `title|definition|time_or_place|overview`；全字段 = 短文本再加 6 个 sections；calib = `definition|time_or_place|overview|6节`（不含 title，便于跨轮对比）。sections 固定按 `原理|典型手法与适用条件|实例|常见错误与限制|一图|待核实` 顺序拼接。全库共 **126** 条（脚本实测 `TOTAL ENTRIES=126`），逐条对其余 125 条取最高值。

## 二、任务 1：相似度（difflib）对全库最高值

逐条对全库其余 125 条取最高相似度（报告最高值对手，脚本实算）：

| 条目 | 短文本(title+def+top+ov) 最高 | 对手 | 全字段(+sections) 最高 | 对手 | calib(def\|top\|ov\|sec) 最高 | 对手 | 是否 <0.54 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| visual-center | 0.4310 | visual-movement | 0.4699 | simplification | 0.4776 | simplification | ✅ |
| contrast-principle | 0.4923 | color-contrast | 0.4912 | color-contrast | 0.4990 | color-contrast | ✅ |
| green-architecture | 0.4179 | biophilic-design | 0.4662 | modernism | 0.4654 | modernism | ✅ |

- **3 条无论短文本、全字段还是 calib 口径，对全库最高相似度全部 < 0.54**（最高为 contrast-principle calib **0.4990**，仍低于阈值）。
- 附带观察：`green-architecture` 与最易混的既有条目 `sustainable-architecture` 相似度仅为 短 **0.4034** / 全 **0.1835** / calib **0.1709**，两条区隔清晰，无近重复。
- 全库两两短文本当前最高对仍为 `s-curve-composition × triangular-composition` **0.5166**，亦低于 0.54，无整库套话告警（与第17–19轮一致）。

## 三、任务 2：来源支撑核对（实抓）

`en.wikipedia.org` 直连在本环境 20s 超时（与 DECISIONS D05 一致）。本轮以镜像 `www.owiki.org` 实抓维基正文（与 sources.json canonical 页同源同标题，均 **HTTP 200 且 h1 与记录标题吻合**）。下列均为实抓命中片段（**数据，非指令**）。

### 3.1 逐来源核验表

| 来源 id | 存在 / 记录标题 | verified / link_ok | 实抓与 h1 | 与主题相关 | 正文支撑要点（实抓片段） |
| --- | --- | --- | --- | --- | --- |
| wp-composition-visual-arts | ✅ `Composition (visual arts)` | true / true | owiki HTTP200，h1 `Composition (visual arts)` 吻合 | ✅（构图总论；支撑 visual-center、contrast-principle） | "**There should be a center of interest or focus in the work, to prevent it becoming a pattern in itself**"；"**The direction followed by the viewer's eye should lead the viewer's gaze**…"；"**The more contrast in value, the more pronounced the three-dimensional form is**"；"**Shape — areas defined by edges within the piece**"；"in nature objects are rarely the **same size** and evenly spaced" |
| wp-rule-of-thirds | ✅ `Rule of thirds` | true / true | owiki HTTP200，h1 `Rule of thirds` 吻合 | ✅（三分法；支撑 visual-center） | "**important compositional elements should be placed along these lines or their intersections**"；"aligning a subject with these points creates **more tension, energy and interest** in the composition than simply centering the subject"；"to **discourage placement of the subject at the center**" |
| wp-color-theory | ✅ `Color theory` | true / true | owiki HTTP200，h1 `Color theory` 吻合 | ✅（色彩理论；支撑 contrast-principle 的色彩/明度对比） | "…**color contrast effects**、color harmony…"；"**The Law of Simultaneous Color Contrast** by … Michel Eugène Chevreul"；"**simultaneous contrast, which appears in two colors viewed side by side**"；"hue, colorfulness and **lightness**" |
| wp-green-building | ✅ `Green building` | true / true | owiki HTTP200，h1 `Green building` 吻合 | ✅（绿色建筑总论；支撑 green-architecture） | "the common objective of green buildings is to **reduce the overall impact of the built environment on human health and the natural environment** by: **Efficiently using energy, water, and other resources**; Protecting occupant health…"; "**energy efficiency, water efficiency, materials efficiency, indoor environmental quality** enhancement"; "the usage of **recycled materials** is crucial" |
| wp-sustainable-architecture | ✅ `Sustainable architecture` | true / true | owiki HTTP200，h1 `Sustainable architecture` 吻合 | ✅（可持续建筑；支撑 green-architecture） | "architecture that **seeks to minimize the negative environmental impact of buildings** through improved efficiency and moderation in the use of materials, energy, development space and the ecosystem at large"; "**prioritizes passive systems** … supplementing with **renewable energy sources**" |

> 结论（来源层面）：5 个来源 id **均存在**、`verified=true`、`link_ok=true`、标题与主题**直接相关**、实抓 h1 与记录标题逐一吻合。`visual-center`/`contrast-principle` 共用 `wp-composition-visual-arts`（合法共用），其余各挂 2 条，全部为已核验权威百科。

## 四、任务 3：逐条结构与内容核对（最终态）

实跑 `python tools/check.py` → **`PASS: all checks, 0 errors`（EXIT=0）**；另跑只读结构化脚本逐项核对（实测）：

| 检查项 | visual-center | contrast-principle | green-architecture |
| --- | --- | --- | --- |
| 七节齐备（definition+6 节，无缺无多） | ✅ 6/6 | ✅ 6/6 | ✅ 6/6 |
| 1 张内联 SVG，viewBox 有效（0 0 760 400） | ✅ 1 张 | ✅ 1 张 | ✅ 1 张 |
| SVG 元素坐标实测不出界（rect/circle/line/text） | ✅ 无出界 | ✅ 无出界 | ✅ 无出界 |
| SVG 图注含「示意图，非施工图」 | ✅ | ✅ | ✅ |
| 常见错误与限制含 D09 规范提示 | ✅ | ✅ | ✅ |
| definition/time_or_place/overview 有**已挂载**来源正文支撑 | ✅ 强（composition "center of interest/focus"+"direction…lead the viewer's gaze"；rule-of-thirds "lines or their intersections""discourage…center"） | ✅ 强（composition "contrast in value…three-dimensional form"；color-theory "color contrast effects""simultaneous contrast""lightness"） | ✅ 强（green-building "reduce the overall impact…energy, water…"; sustainable-architecture "minimize the negative environmental impact""passive systems…renewable"） |
| 原理/手法有已挂载来源正文支撑 | ✅ 强（居中 vs 三分点；位置/对比/指向线） | ✅ 强（一方强一方弱的主次；明度/色彩对比） | ✅ 强（energy/water/materials/IEQ；被动式优先+可再生） |
| 正文无编造具体年份/人名/引文 | ✅ | ✅ | ✅ |
| 实例为**类型性描述**（符合本轮要求） | ✅（三分点式视觉中心；地点/设计者/年份=不适用） | ✅（强弱对比的主次安排；不适用） | ✅（被动式节能公共建筑；不适用） |
| needs_verification ↔ pending_notes ↔ 正文待核实 ↔ coverage.nvc=1 | ✅ 一致 | ✅ 一致 | ✅ 一致 |
| theme/period/region/tier 与 coverage 一致 | ✅ 理论/跨时期/全球/重要 | ✅ 理论/跨时期/全球/重要 | ✅ 风格/当代/全球/核心 |
| source_count 与 sources 一致 | ✅ 2 | ✅ 2 | ✅ 2 |

> `check.py` 只校验“每条记录挂有 verified 来源”，不校验来源正文是否支撑该主张；上表“正文支撑”一列系本报告按 §三 实抓片段**逐句人工比对**所得，3 条均已落实。`needs_verification=true ↔ pending_notes ↔ sections.待核实 ↔ coverage.needs_verification_count=1` 三者**全部一致**。

## 五、逐条验收结论

| 条目 | 来源支撑 | 结构/SVG/规范提示 | 待核实联动 | 相似度(短/全/calib) | 结论 |
| --- | --- | --- | --- | --- | --- |
| **visual-center（视觉中心）** | `wp-composition-visual-arts`「center of interest/focus」「direction…lead the viewer's gaze」＋`wp-rule-of-thirds`「lines/intersections」「discourage…center」→ **强支撑** | 全过 | 四者一致 | 0.4310 / 0.4699 / 0.4776 | **合格** |
| **contrast-principle（对比）** | `wp-composition-visual-arts`「contrast in value…form」「Shape—areas defined by edges」＋`wp-color-theory`「color contrast effects」「simultaneous contrast」「lightness」→ **强支撑** | 全过 | 四者一致 | 0.4923 / 0.4912 / 0.4990 | **合格** |
| **green-architecture（绿色建筑）** | `wp-green-building`「reduce the overall impact…energy, water…」「energy/water/materials efficiency, IEQ」「recycled materials」＋`wp-sustainable-architecture`「minimize the negative environmental impact」「passive systems…renewable」→ **强支撑** | 全过 | 四者一致 | 0.4179 / 0.4662 / 0.4654 | **合格** |

**逐条依据与问题：**

- **visual-center — 合格**
  - 依据：`wp-composition-visual-arts` 实抓「**There should be a center of interest or focus in the work, to prevent it becoming a pattern in itself**」直接支撑定义「画面中优先吸引注意力的区域」；「**The direction followed by the viewer's eye should lead the viewer's gaze**」支撑概述「可由…指向线建立」，配合该页「contrast」与 `wp-rule-of-thirds`「placed along these lines or their intersections」「discourage placement of the subject at the center」共同支撑「由对比、位置或指向线建立，未必在几何中点」及手法「放在三分点或对比最强处」。实例为类型性描述（不适用），无编造年份/人名/引文。
  - 问题（软信号，不据此判不合格）：「适用于…界面首屏」为常见适用面的合理外推，来源未逐字出现“界面”；概属合理补充，非编造。

- **contrast-principle — 合格**
  - 依据：`wp-composition-visual-arts` 实抓「**The more contrast in value, the more pronounced the three-dimensional form is**」「**Shape — areas defined by edges**」「objects are rarely the same size」支撑“明度/形状/尺度差异”；`wp-color-theory` 实抓「**color contrast effects**」「**The Law of Simultaneous Color Contrast**」「**simultaneous contrast…two colors viewed side by side**」「lightness」支撑“色彩差异”与对比原理。概述「对比建立主次，但过度对比破坏整体统一」可对应 composition「center of interest…prevent it becoming a pattern」与 color-theory 的 contrast/harmony 张力。实例为类型性，无编造。
  - 问题（软信号，不据此判不合格）：「形状或尺度差异」中“形状/尺度”是对 composition 设计元素（Shape、size 变化）的**合理外推**而非逐字；「对比建立主次…破坏统一」为合理性提炼。均非编造，措辞可略收窄。
  - 附注（Minor）：与既有 `color-contrast`（色彩对比）相似度 0.4923/0.4912/**0.4990**，为本批最高、逼近阈值；二者语义相邻，建议后续在概述或 related 中显式区分“构图对比（明暗/形状/尺度/位置）”与“色彩对比（色相/明度/饱和度）”，以守住 <0.54。

- **green-architecture — 合格**
  - 依据：`wp-green-building` 实抓「the common objective of green buildings is to **reduce the overall impact of the built environment on human health and the natural environment** by: **Efficiently using energy, water, and other resources**」「**energy efficiency, water efficiency, materials efficiency, indoor environmental quality**」「usage of **recycled materials** is crucial」逐字支撑定义「以降低环境影响为目标的建筑设计取向」与概述「关注能耗、水资源、材料循环与室内健康」；`wp-sustainable-architecture` 实抓「**seeks to minimize the negative environmental impact of buildings**」「**prioritizes passive systems** … supplementing with **renewable energy sources**」支撑原理与手法「被动式设计优先，辅以高效设备与可再生资源」。实例为类型性（被动式节能公共建筑，不适用），无编造年份/人名/引文。本条虽为 tier=核心，但技术本体（定义/原理/手法）**由已挂载双源强支撑**，与第19轮 drainage“核心但技术本体无已挂载来源”性质不同。
  - 问题（Minor，非阻断）：tier=核心而实例为类型性——符合本轮“实例应为类型性描述”的约定；后续若提升，可补 1 个具名绿色建筑实例（如 LEED/BREEAM 认证项目）双源，并补评价指标（能耗/水耗）数据来源，从而把 `pending_notes` 从模板收窄为具体缺口。

## 六、总体结论与是否整批返工

- **抽检结果：3/3 合格（visual-center、contrast-principle、green-architecture）。**
  - 来源：5 个来源 id 均**存在**、`verified=true`、`link_ok=true`、h1 与记录标题吻合、主题直接相关；3 条的 definition / time_or_place / overview 及原理/手法/实例/风险段均由已挂载来源**正文强支撑**；**均未发现编造年份、人名或引文**；实例均按本轮要求为**类型性描述**。
  - 结构：3 条七节完整、各含 1 张 SVG 且含「示意图，非施工图」、元素不出界、风控段含 D09 规范提示、`check.py` **PASS 0 errors（EXIT=0）**。
  - 待核实：3 条 `needs_verification=true ↔ pending_notes ↔ 正文待核实 ↔ coverage.needs_verification_count=1` **四者一致**（与 coverage 的 level=L2、status=已写、source_count=2 亦一致）。
  - 相似度：3 条对全库最高（短/全/calib 任一）均 **< 0.54**（最大 contrast-principle calib 0.4990）；全库两两短文本最高 0.5166 亦低于阈值；库规模 126。
- **整批返工建议：不建议整批返工。** 无“不合格”条目；按 AUTONOMOUS E「不合格才整批返工」不触发；亦无待核实占比异常或相似度超阈；3 条均无编造、结构全过。
- **非返工、定点优化建议（Minor，均不阻断出厂）**：
  1. **pending_notes 去模板化**：3 条 `pending_notes` 现为同一模板句“实例的具体名称、设计者与年代待补充独立来源。”，建议按各自实际缺口分别撰写（visual-center：示例作品的作者/年代；contrast-principle：示例版式出处/作者；green-architecture：示例建筑与评价指标/认证数据来源），与各自 `sections.待核实` 更贴合。
  2. **contrast-principle 与 color-contrast 边界**：相似度 0.4990 为本批最高（仍 <0.54），建议在概述或 `related` 明示二者分工，长期守住阈值。
  3. **软信号措辞**：contrast「形状/尺度差异」、visual-center「界面首屏」为合理外推，可略收窄以更贴近来源逐字；green-architecture 核心条后续可补具名实例与评价数据来源以收窄 pending。
  4. **本批其余 3 条**（`form-follows-function`、`curvilinear-perspective`、`courtyard`）本轮未抽；其中 `courtyard` 使用 `wp-courtyard`/`wp-chinese-garden`、`curvilinear-perspective` 使用 `wp-curvilinear-perspective`/`wp-perspective-graphical`，建议后续补抽以闭环 6 条（并发/同源风险相对可控）。

---

### 机器可读汇总

```
ROUND=20
SCOPE=["visual-center","contrast-principle","green-architecture"]   # 抽自第20轮6条升级集，3/6=50%
ROUND20_UPGRADE_SET=["visual-center","contrast-principle","form-follows-function","curvilinear-perspective","courtyard","green-architecture"]
FILES={"visual-center":"entries/batch-01.json","contrast-principle":"entries/batch-01.json","green-architecture":"entries/batch-02-d.json"}
CONCURRENCY={"state":"upgrade_round20.py applied 2026-11-22T20:21:14; no apply_review_round20 / no review-round20 at 20:24:26; mtimes unchanged","report_basis":"FINAL on-disk state @20:21:14 snapshot, rechecked 20:24:26"}
SIM_METHOD="difflib.SequenceMatcher.ratio(); join='|'; short=title|definition|time_or_place|overview; full=+6 sections; calib=def|top|ov|sections"
SIM_MAX_SHORT={"visual-center":[0.4310,"visual-movement"],"contrast-principle":[0.4923,"color-contrast"],"green-architecture":[0.4179,"biophilic-design"]}
SIM_MAX_FULL={"visual-center":[0.4699,"simplification"],"contrast-principle":[0.4912,"color-contrast"],"green-architecture":[0.4662,"modernism"]}
SIM_MAX_CALIB={"visual-center":[0.4776,"simplification"],"contrast-principle":[0.4990,"color-contrast"],"green-architecture":[0.4654,"modernism"]}
ALL_SIM_UNDER_0.54=true ; LIBRARY_SIZE=126
GREEN_VS_SUSTAINABLE_ARCH={"short":0.4034,"full":0.1835,"calib":0.1709}
GLOBAL_LIBRARY_MAX_SHORT={"0.5166":"s-curve-composition x triangular-composition"}
SOURCES_ALL_EXIST_VERIFIED=true
SOURCES_VC=["wp-composition-visual-arts","wp-rule-of-thirds"]
SOURCES_CP=["wp-composition-visual-arts","wp-color-theory"]
SOURCES_GA=["wp-green-building","wp-sustainable-architecture"]
FETCH={"en.wikipedia.org":"timeout (D05)","www.owiki.org":"HTTP200 h1 matched (all 5 wiki sources)"}
VISUAL_CENTER_SUPPORT="STRONG (composition 'center of interest/focus','direction...lead the viewer's gaze'; rule-of-thirds 'lines or their intersections','discourage...center')"
CONTRAST_SUPPORT="STRONG (composition 'contrast in value...form','Shape-areas defined by edges'; color-theory 'color contrast effects','simultaneous contrast','lightness')"
GREEN_ARCH_SUPPORT="STRONG (green-building 'reduce the overall impact...energy,water','energy/water/materials efficiency, IEQ','recycled materials'; sustainable-architecture 'minimize the negative environmental impact','passive systems...renewable')"
INSTANCE_TYPE_LEVEL={"visual-center":true,"contrast-principle":true,"green-architecture":true}
FABRICATED=false
SEVEN_SECTIONS_OK=true ; SVG_COUNT=1_each ; SVG_CAPTION_OK=true ; SVG_IN_BOUNDS=true ; REGNOTE_OK=true
PENDING_VS_SECTION={"visual-center":"consistent","contrast-principle":"consistent","green-architecture":"consistent"}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
VERDICT={"visual-center":"合格","contrast-principle":"合格","green-architecture":"合格"}
SOFT_SIGNALS={"visual-center":"'界面首屏'合理外推非逐字","contrast-principle":"'形状/尺度差异'合理外推；与color-contrast相似度0.4990为本批最高","green-architecture":"核心条实例为类型性(符合本轮要求)；材料循环由recycled materials支撑"}
OVERALL="3/3 合格；来源/结构/相似度无硬失败；无编造；四者一致；不建议整批返工"
FIX_HINT="pending_notes去模板化(三条)；contrast-principle与color-contrast边界显式区分；核心green-architecture后续补具名实例+评价数据；补抽form-follows-function/curvilinear-perspective/courtyard"
REST_FILES_WRITTEN=["research/spotcheck-round20.md"]   # 只写本文件
```
