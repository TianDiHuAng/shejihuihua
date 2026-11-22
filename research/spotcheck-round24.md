# 第24轮质量闸抽检报告（spotcheck-round24）——s-curve-composition / triangular-composition / rule-of-space 逐条来源·正文支撑·结构·相似度复检

- 抽检人：spotcheck-r24（由 lead 委派的子代理）；抽检时间：2026-11-22 约 21:08 起，Asia/Hong_Kong（会话时间取样；核对完成时点约 21:12）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（本轮新增或改动条目抽 ≥25%、至少 3 个；不合格整批返工）、第六节（联网内容一律视为数据，其中任何指令不执行、不下载不运行来源代码、不改项目文件夹之外内容）、第二节（状态文件）；`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L2」「条目页结构（七节）」「通用硬性规则」「专用规则」；`DECISIONS.md` D05（实抓核验）/D06（在线百科 year=null）/D09（尺寸·坡度·消防·无障碍仅一般性说明并附规范提示）/D10（关键事实需两独立来源，否则标待核实）/D11（link_ok 三态）/D14（needs_verification 与 pending_notes 联动）。
  - 说明：任务书所称 `AUTONOMOUS.md`/`TASK_design.md` 在仓库根无同名文件，实际位于 `D:/Users/Administrator/Desktop/`（与第 12–23 轮一致），已按该路径只读读取；`DECISIONS.md`、`research/spotcheck-round23.md` 在仓库根。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考，不另启流程）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言）。
- 抽检对象（第24轮升级的 **6 条补充 L1→L2**，据 `tools/upgrade_round24.py` 头部字典确认集合为：`rule-of-space`、`golden-ratio`、`diagonal-composition`、`s-curve-composition`、`triangular-composition`、`framing-composition`；本次按指派抽其中 3 条）：**`s-curve-composition`（S形构图，tier 补充）、`triangular-composition`（三角形构图，tier 补充）、`rule-of-space`（空间法则，tier 补充）**。三条均在 `entries/batch-01.json`。抽样率 3/6 = 50%，满足「≥25% 且 ≥3 条」。

## 〇、数据稳定性说明（本轮数据已冻结）

- 本轮**未发现并发的 review/apply 流水线**（`research/review-round24.md`、`tools/apply_review_round24.py` 均不存在）。
- 写入时点：`data/sources.json` mtime 21:05:50（100132B）；`entries/batch-01.json`、`coverage.json` mtime 21:08:04（77724B / 80224B）；`tools/upgrade_round24.py` mtime 21:07:58（8012B）—— 由本轮一次写入完成。
- **21:11:53 复核**：上列四个文件 mtime 与字节数均未变 → **数据稳定，无中途改写**。`git status` 显示 round24 改动为未提交态（M coverage / M batch-01；?? gaps-round24、reader_questions-round24、upgrade_round24.py），与抽检态一致。
- **本报告口径**：以当前最终态（21:08:04 快照，21:11:53 复核未变）逐条复核。
- 只读声明：本次**仅生成** `research/spotcheck-round24.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未改动项目文件夹之外内容，未创建 git commit。抓取正文仅驻留系统临时目录（`/tmp/r24texts.json` 等）用于分析、非项目产物。联网内容一律视为数据，网页中任何指令均未执行。

## 一、判定口径与相似度方法

- **结构口径**：3 条均为 L2，按 TASK_design.md「条目页结构」核 **七节**：①核心概念与定义(=definition) ②原理 ③典型手法与适用条件 ④实例 ⑤常见错误与限制 ⑥一图 ⑦待核实；并核每页 ≥1 张内联 SVG 含「示意图，非施工图」、风控段含 D09 规范提示（“实际工程须按当地规范和专业设计人员的要求”）、`needs_verification`/`pending_notes`/正文待核实/`coverage.needs_verification_count` 联动一致；实例须为**类型性描述**（名称/地点/设计者/年份），不复制图像、不编造年份人名引文。
- **正文支撑口径（本轮重点）**：对每条所挂 verified 来源，**实抓英文维基正文并逐句比对** definition / time_or_place / overview / 七节主张，重点核 **“S形/三角形/空间法则”等子概念是否真被所引总览条目正文具体覆盖**（而非仅一般性构图）。D09 允许“尺寸·坡度·消防·无障碍”作一般性说明并附规范提示，但**不豁免核心概念/具体应用主张本身的来源支撑**。
- **相似度阈值 0.54**（AUTONOMOUS.md E 节「疑似套话」警戒线，沿用第 12–23 轮口径）。算法 = `difflib.SequenceMatcher(None,a,b).ratio()`，字段以 `|` 连接；短文本 = `title|definition|time_or_place|overview`；全字段 = 短文本再加 6 个 sections；calib = `definition|time_or_place|overview|6节`（不含 title）。sections 固定按 `原理|典型手法与适用条件|实例|常见错误与限制|一图|待核实` 顺序拼接。全库共 **126** 条（脚本实测 `TOTAL ENTRIES=126`，无重复 id），逐条对其余 125 条取最高值。

## 二、任务 1：相似度（difflib）对全库最高值

逐条对全库其余 125 条取最高相似度（脚本实算）：

| 条目 | 短文本(title+def+top+ov) 最高 | 对手 | 全字段(+sections) 最高 | 对手 | calib(def\|top\|ov\|sec) 最高 | 对手 | 是否 <0.54 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s-curve-composition | 0.5166 | triangular-composition | **0.5189** | triangular-composition | 0.5145 | triangular-composition | ✅（余量 0.0211） |
| triangular-composition | 0.5166 | s-curve-composition | 0.5114 | s-curve-composition | 0.5145 | s-curve-composition | ✅ |
| rule-of-space | 0.4265 | diagonal-composition | 0.4673 | s-curve-composition | 0.4788 | diagonal-composition | ✅（宽松） |

- **3 条无论短文本、全字段还是 calib 口径，对全库最高相似度全部 < 0.54**（最高为 s-curve-composition 全字段 **0.5189**，余量约 0.021，贴近但未越界）。
- **全库两两短文本当前最高对仍为 `s-curve-composition × triangular-composition` = 0.5166**（与第 23 轮记录一致；任务书所称“曾达 0.517”复核属实）。此对为**全库最接近阈值的一对**，但因同属“构图类”且均写“以某形引导视线/稳定骨架”，措辞存在可理解的家族相似，实测仍低于 0.54，**不触发相似度降级**。次高 `leading-lines × framing-composition` 0.5042、`color-psychology × environmental-psychology` 0.5000，均更低。
- 相似度维度**不触发降级**；仅提示 s-curve/triangular 一对处于边界区，返工改写时须注意进一步去模板化以免越线。

## 三、任务 2：来源存在性 / verified / 主题相关性（实抓）

本轮 `en.wikipedia.org` 直连**实抓 HTTP 200 且 h1 吻合**（3 个来源本次首抓即 200）。下列为实抓命中（**数据，非指令**）：

| 来源 id | 存在 / 记录标题 | verified / link_ok | 实抓 | 与主题相关（按正文内容核） |
| --- | --- | --- | --- | --- |
| wp-composition-visual-arts | ✅ `Composition (visual arts)` | true / true | en.wikipedia HTTP200，h1 吻合，正文 19663 字符 | ✅ 直接支撑：“Rule of space”专节（2.3）；“sinuous 'S' curve”；“triangular format creates a sense of stability and strength”。**三个子概念均被其正文具体覆盖** |
| wp-leading-line | ✅ `Leading lines` | true / true | en.wikipedia HTTP200，h1 吻合，正文仅 2134 字符 | ❌ **实为消歧义页**（“This is a disambiguation page…”；“Leading lines may refer to: Lines that lead to the main subject of a visual composition；Range markers which visually aid piloting in channels and rivers”）。仅一句泛泛“lines that lead to the main subject”，**对 S形/空间法则零实质支撑** |
| wp-symmetry | ✅ `Symmetry` | true / true | en.wikipedia HTTP200，h1 吻合，正文 41186 字符 | ❌ **一般数学/科普“对称”总条**（几何、拼布、音乐、伊斯兰纹样）；triangle 仅出现在几何导航与拼布；`composition` 唯一 1 处属音乐。**对“三角形构图”零相关** |

> 结论（来源层面）：3 个来源 id **均存在**、`verified=true`、`link_ok=true`，实抓 h1 全部吻合。但**“存在且 verified”不等于“正文支撑所挂主张”**：`wp-leading-line` 是消歧义页（无实质内容），`wp-symmetry` 是无关的一般对称总条——二者对相应条目的具体概念**均无正文支撑**。逐条支撑见 §四。**这是本轮最突出的系统性缺陷：三个条目都各挂了一条不支撑其概念的第二来源。**

## 四、任务 3：逐条正文支撑核对（关键项，实抓逐句比对）

`python tools/check.py` 实跑 → **`PASS: all checks, 0 errors`（EXIT=0）**。`check.py` 只校验“每条挂有 verified 来源”，**不校验来源正文是否支撑该主张**；下表为对实抓正文逐句人工比对所得。

### 4.1 s-curve-composition（S形构图）——**“S曲线”术语确被总览条目正文覆盖；但应用阐述（道路/河流/人体曲线/延长观看路径）无来源，第二来源为消歧义页 → 待核实（须返工）**

实抓命中片段（wp-composition-visual-arts，“Curves”段）：
- “Compared to straight lines, **curves provide a greater dynamic influence in a picture.** They are also generally more aesthetically pleasing, as the viewer associates them with nature and softness.”
- **“There are two main types of curves, a simple 'C' curve as well as a more sinuous 'S' curve.”**（→“S 曲线”作为曲线类型被**明确点名**，核心术语被覆盖）

实抓关键词（wp-composition-visual-arts）：`S-curve` 0（带连字符写法 0，但正文以 `"S" curve` 出现）、`curve` 5、`curved` 1、**`river` 0、`road` 0**。wp-leading-line：`curve` 0、`space` 0、`movement` 0，`river` 1（仅“Range markers … channels and rivers”通航语境，与构图无关）。

逐项比对：
- definition「以S形曲线引导视线深入画面的构图方式」→ **半支撑**：“S形曲线”术语被来源明列；“**引导视线深入画面**”为引申，来源只说曲线“dynamic influence / aesthetically pleasing / softness”，未言“深入画面”。
- overview「S形曲线延长观看路径，常用于道路与河流题材」→ **不支撑**：“延长观看路径”为引申；**“道路与河流题材”无来源（composition 正文 road=0/river=0；leading-line 的 river 属通航消歧义）**。
- 典型手法「河流、道路、人体曲线呈S形展开；适用于风景与柔和的动态」→ **不支撑**：`河流/道路/人体曲线` 均无来源；“柔和/动态”勉强由“softness/dynamic influence”泛化（部分）。
- 实例「S 形河流的纵深构图（类型性描述）；地点/设计者/年份 不适用」→ **类型性、无编造年份人名引文**（合规）。
- **待核实联动缺口**：`sections.待核实` 仅写“示例作品与作者年代待核实”，`pending_notes` 仅写“实例的具体名称、设计者与年代待补充独立来源”，**均未披露“道路/河流题材等应用主张无来源、第二来源为消歧义页（实为单源）”**。

> **判定：待核实（须返工）**。核心术语“S 曲线”确被 wp-composition-visual-arts 正文具体覆盖（**不是**第23轮 east-west 那种“术语错配/零支撑”），故不判硬性不合格；但 overview 与典型手法中“道路与河流题材/河流·道路·人体曲线/延长观看路径”等具体主张无任何来源，第二来源 `wp-leading-line` 为消歧义页无实质内容 → 核心事实实为单源，且待核实声明未如实覆盖。**返工方向**：删除或降级为“待核实”所有无来源的应用阐述（道路/河流/人体曲线），第二来源改挂真正论述曲线/S 形构图的权威页（或补一条），并把待核实声明扩写覆盖“应用主张缺源/单源”缺口。

### 4.2 triangular-composition（三角形构图）——**“三角形=稳定/强度”被总览条目正文覆盖；但“尖端指向/倒三角动感/三人山景”无来源，第二来源无关于三角构图 → 待核实（须返工）**

实抓命中片段（wp-composition-visual-arts，“Geometry and symmetry”段）：
- **“Related to the rule of odds is the observation that triangles are an aesthetically pleasing implied shape within an image.”**
- “**Paul Cézanne successfully used triangles in his compositions of still lifes. A triangular format creates a sense of stability and strength.**”（→“三角形构图=稳定/强度”被**明确支撑**，且带 Cézanne 例证）

实抓关键词（wp-composition-visual-arts）：`triangular` 1、`triangle` 3、`pyramid` 1（几何形式，非构图）。wp-symmetry：`triangle` 2（几何导航 + 拼布中的“fabric triangles”）、`pyramid` 3（几何/建筑清单）、`composition` 1（音乐），**`triangle composition` 语义 0**。

逐项比对：
- definition「以三角形的三个顶点构成画面稳定骨架、尖端方向引导视线上升或前行的构图方式」→ **半支撑**：“稳定骨架”成立（stability/strength）；“**尖端方向引导视线上升或前行**”无来源。
- overview「底宽顶尖既有稳固的重心又能形成指向性，常见于三人构图与山景题材」→ **半支撑**：“稳固”成立；“**指向性/三人构图/山景题材**”无来源。
- 原理「三个视觉支点构成稳定骨架，底宽提供稳重、尖端形成指向与张力」→ “稳定”成立；“**底宽稳重/尖端指向张力**”无来源。
- 典型手法「三人合影、山景常呈正三角；倒三角则制造不稳定与动感」→ **不支撑**：`三人合影/山景/倒三角/动感` 均无来源。
- 实例「三角构图的群像（类型性描述）；地点/设计者/年份 不适用」→ **类型性、无编造年份人名引文**（合规；未把 Cézanne 编入实例，避免误引）。
- **待核实联动缺口**：`sections.待核实`/`pending_notes` 仅涉“示例作品与作者年代/实例名称设计者年代”，**未披露“倒三角/三人山景/尖端指向等无来源、第二来源 wp-symmetry 与三角构图无关（实为单源）”**。

> **判定：待核实（须返工）**。核心“三角形格式→稳定/强度”被 wp-composition-visual-arts 正文明确支撑（**不是**零支撑），故不判硬性不合格；但 definition/overview/典型手法含多处无来源主张（尖端指向、指向性、倒三角动感、三人山景），第二来源 `wp-symmetry` 为一般数学总条、与三角构图零相关 → 核心实为单源，待核实声明未覆盖。**返工方向**：删除或降级为待核实的无来源阐述；第二来源改挂真正论述三角/金字塔式构图或视觉稳定性的权威页，并扩写待核实声明。

### 4.3 rule-of-space（空间法则）——**核心定义与典型手法被总览条目“Rule of space”专节近乎逐句支撑；第二来源为消歧义页（minor）→ 合格**

实抓命中片段（wp-composition-visual-arts，“Rule of space”专节，目录 2.3，正文“Main article: Lead room”“Image of a racing car with lead room”）：
- **“The rule of space applies to artwork (photography, advertising, illustration) picturing objects to which the artist wants to apply the illusion of movement, or which is supposed to create a contextual bubble in the viewer's mind.”**
- **“This can be achieved, for instance, by leaving white space in the direction the eyes of a portrayed person are looking, or, when picturing a runner, adding white space in front of him rather than behind him to indicate movement.”**
- “Studies with naive participants have confirmed this preference.”

逐项比对：
- definition「在视线或运动方向前方预留画面空间的构图方法」→ **强支撑（近乎逐句）**：来源“leaving white space **in the direction the eyes … are looking**”“adding white space **in front of him rather than behind him to indicate movement**”。
- overview「预留空间能表现运动趋势与方向感，避免主体视线被画面边缘截断」→ **基本支撑**：“表现运动趋势与方向感”有来源（illusion of movement / 视线方向）；“避免主体视线被画面边缘截断”为合理引申（非逐字，属轻微外延）。
- 原理/典型手法「人物或车船朝一侧运动时，在该侧留大空白、身后留小空白；适用于动态画面」→ **强支撑**：runner“front rather than behind”、racing car“lead room”两例直接对应。
- 实例「动态主体的前向留白（类型性描述）；地点/设计者/年份 不适用」→ **类型性、无编造**（合规）。
- **子概念覆盖**：本条所依赖的“空间法则/前向留白（lead room）”在总览条目中有**独立专节“Rule of space”（2.3）**，非一般性构图泛述 → 子概念确被覆盖。

> **判定：合格（附 minor）**。definition/原理/典型手法由 wp-composition-visual-arts“Rule of space”专节近乎逐句支撑，子概念被总览条目具体覆盖，实例类型性无编造。**非阻断 minor**：(1) 第二来源 `wp-leading-line` 为**消歧义页**、对空间法则零支撑（该专节其实指向“Main article: Lead room”，更恰当的第二来源应是 `Lead room` 而非 `Leading lines`）→ 核心实为单源；(2) overview“避免视线被画面边缘截断”为引申；(3) `pending_notes`/`待核实` 仅述“实例/年代”，未提“第二来源不足/单源”。以上不影响合格判定，但建议随批修正来源。

## 五、任务 4：结构 / SVG / 规范提示 / 待核实联动（当前最终态，实测）

| 检查项 | s-curve-composition | triangular-composition | rule-of-space |
| --- | --- | --- | --- |
| 七节齐备（definition + 6 节，无缺无多） | ✅ 6/6 | ✅ 6/6 | ✅ 6/6 |
| 1 张内联 SVG，viewBox（0 0 760 400） | ✅ | ✅ | ✅ |
| SVG 元素不出界（数值核对） | ✅ 无越界 | ✅ 无越界 | ✅ 无越界 |
| SVG 图注含「示意图，非施工图」 | ✅ | ✅ | ✅ |
| 常见错误与限制含 D09 规范提示 | ✅ | ✅ | ✅ |
| 正文无编造人名/引文 | ✅ | ✅ | ✅ |
| 无编造年份（实例年份均“不适用”） | ✅ | ✅ | ✅ |
| 实例为“类型性描述” | ✅（S形河流纵深，无图像） | ✅（三角群像，无图像） | ✅（动态主体前向留白） |
| needs_verification ↔ pending_notes ↔ 待核实 ↔ coverage.nvc | ✅ 一致（T/非空/非空/1） | ✅ 一致（T/非空/非空/1） | ✅ 一致（T/非空/非空/1） |
| theme/tier/period/region 与 coverage 一致 | ✅（理论/补充/跨时期/全球） | ✅（理论/补充/跨时期/全球） | ✅（理论/补充/跨时期/全球） |
| source_count 与 sources 一致 | ✅ 2 | ✅ 2 | ✅ 2 |
| **definition/overview/七节 有已挂来源正文支撑** | ⚠️ 核心“S曲线”支撑；应用阐述（道路/河流/人体曲线）无支撑；第二源无效 | ⚠️ 核心“稳定/强度”支撑；尖端指向/倒三角/三人山景无支撑；第二源无效 | ✅ 核心与典型手法近乎逐句支撑；第二源无效（minor） |

> 三条的 `needs_verification ↔ pending_notes ↔ sections.待核实 ↔ coverage.needs_verification_count` **各自形式一致**（均 T/非空/非空/1），source_count 与 sources 数一致，theme/tier/period/region 与 coverage 对齐，SVG/规范提示/实例类型性全过；`check.py` **PASS 0 errors（EXIT=0）**。**但三处 `pending_notes` 完全相同**（“实例的具体名称、设计者与年代待补充独立来源。”）——为模板化批产痕迹；且“形式一致”不等于“待核实声明如实覆盖实际缺口”（见 §4.1、§4.2 的单源/无来源应用问题）。

## 六、逐条验收结论（当前最终态）

| 条目 | 来源/正文支撑 | 结构·SVG·规范 | 待核实联动 | 相似度(短/全/calib) | 结论 |
| --- | --- | --- | --- | --- | --- |
| **s-curve-composition（S形构图）** | “S曲线”术语被 composition 正文明列支撑；**道路/河流/人体曲线/延长观看路径无来源**；第二源 leading-line 为消歧义页→单源 | 全过 | 形式一致但未覆盖应用/单源缺口 | 0.5166 / 0.5189 / 0.5145 | **待核实（须返工：删无源阐述/换第二源/扩写待核实）** |
| **triangular-composition（三角形构图）** | “三角形=稳定/强度”+Cézanne 被 composition 正文支撑；**尖端指向/倒三角动感/三人山景无来源**；第二源 symmetry 与三角构图无关→单源 | 全过 | 形式一致但未覆盖无源/单源缺口 | 0.5166 / 0.5114 / 0.5145 | **待核实（须返工：删无源阐述/换第二源/扩写待核实）** |
| **rule-of-space（空间法则）** | definition/原理/典型手法由“Rule of space”专节**近乎逐句支撑**；子概念被覆盖；第二源 leading-line 为消歧义页（minor，实为单源） | 全过 | 形式一致（仅述实例/年代，minor） | 0.4265 / 0.4673 / 0.4788 | **合格**（minor：第二源应改挂 Lead room） |

**逐条依据与问题：**

- **rule-of-space — 合格**
  - 依据：wp-composition-visual-arts“Rule of space”专节“leaving white space in the direction the eyes … are looking”“adding white space in front of him rather than behind him to indicate movement”“racing car with lead room”——**definition/原理/典型手法近乎逐句支撑**，子概念被总览条目独立专节覆盖，实例类型性无编造。
  - 问题（非阻断 minor）：第二来源 `wp-leading-line` 为消歧义页、零实质支撑（该处本应指向 `Lead room`）；overview“避免视线被画面边缘截断”为引申；`pending_notes/待核实` 仅述实例/年代，未提单源。建议随批把第二来源改为 `Lead room` 后即可稳固合格。

- **s-curve-composition — 待核实（须返工）**
  - 依据（满足部分）：wp-composition-visual-arts“There are two main types of curves, a simple 'C' curve as well as a more sinuous 'S' curve”“curves provide a greater dynamic influence… aesthetically pleasing… softness”——**“S 曲线”术语被覆盖**。
  - 问题：overview“延长观看路径，常用于道路与河流题材”、典型手法“河流、道路、人体曲线呈 S 形展开”在**两来源均无支撑**（composition 正文 road=0/river=0；leading-line 的 river 属通航消歧义）；第二来源 `wp-leading-line` 为消歧义页 → 核心实为单源；`sections.待核实`/`pending_notes` 未覆盖此缺口。→ 待核实（返工补源/删阐述/扩写待核实后复检）。

- **triangular-composition — 待核实（须返工）**
  - 依据（满足部分）：wp-composition-visual-arts“triangles are an aesthetically pleasing implied shape… Paul Cézanne successfully used triangles… A triangular format creates a sense of stability and strength”——**核心“三角形=稳定/强度”被覆盖**。
  - 问题：definition“尖端方向引导视线上升或前行”、overview“指向性/三人构图与山景题材”、典型手法“三人合影、山景常呈正三角；倒三角则制造不稳定与动感”在**两来源均无支撑**；第二来源 `wp-symmetry` 为一般数学“对称”总条、与三角构图零相关（triangle 仅几何导航与拼布）→ 核心实为单源；`sections.待核实`/`pending_notes` 未覆盖此缺口。→ 待核实（返工补源/删阐述/扩写待核实后复检）。

## 七、总体结论与是否整批返工

- **抽检结果：3 条中 1 合格、2 待核实（须返工）、0 硬性不合格。**
  - **合格（1）**：`rule-of-space`——空间法则 definition/原理/典型手法由 Composition (visual arts)“Rule of space”专节近乎逐句支撑，子概念被总览条目具体覆盖，实例类型性无编造；仅第二来源需改挂 Lead room（minor）。
  - **待核实/须返工（2）**：`s-curve-composition`（“S曲线”术语有支撑，但道路/河流/人体曲线/延长观看路径无来源，第二源为消歧义页→单源）；`triangular-composition`（“三角形=稳定/强度”有支撑，但尖端指向/倒三角动感/三人山景无来源，第二源 wp-symmetry 无关→单源）。
- **关键区别（相对第23轮）**：本轮 3 条的**核心子概念均被 wp-composition-visual-arts 正文具体覆盖**（S curve 明列、triangular format→stability+strength、rule of space 独立专节）——**未出现第23轮 east-west/sunken 那种“核心概念零支撑、术语错配”的硬性不合格**。就“子概念是否被所引总览条目覆盖”这一本轮重点而言，三条**均被覆盖**（总览条目恰在此处够具体）。问题下沉为“**具体应用阐述缺乏来源 + 第二来源无效/误引**”。
- **系统性来源缺陷（须记入返工台账）**：`wp-leading-line` 实为**消歧义页**（无实质内容），却被 `s-curve-composition`、`rule-of-space` 及（据 upgrade_round24 SRC 字典）`diagonal-composition` 共用；`wp-symmetry` 与三角构图无关，却被 `triangular-composition` 挂靠。三者导致“两独立来源互印证”实际不成立（核心实为单源），且 `pending_notes/待核实` 仅述“实例/年代”，未如实披露单源/弱源与无来源应用阐述 → **待核实联动口径不实**（D10/D14）。
- **相似度**：3 条对全库最高（短/全/calib 任一）均 < 0.54（最大 s-curve 全字段 0.5189）；全库两两短文本最高 = `s-curve-composition × triangular-composition` 0.5166，为全库最贴阈值的一对，但未越界 → **不因相似度降级**；返工改写时须继续去模板化以免越线。
- **结构**：3 条七节完整、各 1 张 SVG 含「示意图，非施工图」、SVG 不出界、风控段含 D09 提示、实例类型性、`check.py` **PASS 0 errors（EXIT=0）**、`needs_verification↔pending↔待核实↔nvc` 形式一致 → **结构维度合格**。
- **是否建议整批返工：建议对 round-24 的 6 条“补充构图”批次做「定向返工 + 全批复检」**（内容不必整批降级重写，核心概念均有真实来源支撑、结构/相似度均过）。具体：
  1. **统一处理无效第二来源**：所有挂 `wp-leading-line` 的条目（`s-curve-composition`、`rule-of-space`、`diagonal-composition`）改用 `Lead room`（rule-of-space 的专节正文明确“Main article: Lead room”）或真正论述线条/曲线构图的实质条目；`triangular-composition` 的 `wp-symmetry` 改挂真正论述三角/金字塔式构图或视觉稳定性的权威页。
  2. **清理无来源应用阐述**：s-curve 的“道路与河流题材/河流·道路·人体曲线/延长观看路径”、triangular 的“尖端指向/指向性/倒三角动感/三人山景”，删除或降级写入“待核实”。
  3. **修正待核实联动**：把 `pending_notes/待核实` 从仅“实例/年代”扩写覆盖“具体应用缺独立来源/第二来源不足（单源）”缺口，使 `needs_verification` 声明与实际缺口一致（D10/D14）。
  4. **全批复检**：未抽的 `golden-ratio`（wp-golden-ratio/wp-golden-rectangle）、`diagonal-composition`（含 wp-leading-line）、`framing-composition`（wp-composition-visual-arts/wp-chinese-garden）须一并实抓核正文支撑后再定级，防同类“总览/消歧义来源不覆盖具体子概念”缺陷。
- **是否触发相似度/占比降级复查**：相似度未超阈、待核实占比正常（3 条 nvc 均=1、nvf 均=true，无“硬写”信号），**不因相似度降级**；但因 2 条需返工补源，按质量闸建议**定向返工 + 全批复检**。

---

### 机器可读汇总

```
ROUND=24
SAMPLER=spotcheck-r24
SCOPE=["s-curve-composition","triangular-composition","rule-of-space"]   # 抽自第24轮6条补充升级集，3/6=50%
ROUND24_UPGRADE_SET=["rule-of-space","golden-ratio","diagonal-composition","s-curve-composition","triangular-composition","framing-composition"]
FILES={"s-curve-composition":"entries/batch-01.json","triangular-composition":"entries/batch-01.json","rule-of-space":"entries/batch-01.json"}
STATE_STABLE={"sources_mtime":"21:05:50/100132B","entries_coverage_mtime":"21:08:04/77724B,80224B","recheck":"21:11:53 unchanged","concurrency":"none (no review-round24/apply_review_round24)"}
SIM_METHOD="difflib.SequenceMatcher.ratio(); join='|'; short=title|definition|time_or_place|overview; full=+6sections; calib=def|top|ov|sections"
SIM_MAX_SHORT={"s-curve-composition":[0.5166,"triangular-composition"],"triangular-composition":[0.5166,"s-curve-composition"],"rule-of-space":[0.4265,"diagonal-composition"]}
SIM_MAX_FULL={"s-curve-composition":[0.5189,"triangular-composition"],"triangular-composition":[0.5114,"s-curve-composition"],"rule-of-space":[0.4673,"s-curve-composition"]}
SIM_MAX_CALIB={"s-curve-composition":[0.5145,"triangular-composition"],"triangular-composition":[0.5145,"s-curve-composition"],"rule-of-space":[0.4788,"diagonal-composition"]}
ALL_SIM_UNDER_0.54=true ; LIBRARY_SIZE=126 ; GLOBAL_MAX_SHORT={"0.5166":"s-curve-composition x triangular-composition"}
SOURCES_ALL_EXIST_VERIFIED=true
SOURCES={"s-curve-composition":["wp-composition-visual-arts","wp-leading-line"],"triangular-composition":["wp-composition-visual-arts","wp-symmetry"],"rule-of-space":["wp-composition-visual-arts","wp-leading-line"]}
FETCH={"en.wikipedia.org":"HTTP200 h1 matched x3: Composition_(visual_arts) 19663c / Leading_lines 2134c / Symmetry 41186c"}
LINK_OK={"wp-composition-visual-arts":true,"wp-leading-line":true,"wp-symmetry":true}
SOURCE_QUALITY={"wp-composition-visual-arts":"ARTICLE ✓ covers all three sub-concepts (Rule of space §; sinuous 'S' curve; triangular format=stability+strength)","wp-leading-line":"DISAMBIGUATION PAGE ✗ no substantive content (used by s-curve, rule-of-space, diagonal-composition)","wp-symmetry":"GENERAL MATH 'Symmetry' article ✗ zero triangular-composition content"}
KW_COUNTS={
  "wp-composition-visual-arts":{"S_curve_named":true,"curve":5,"curved":1,"triangular":1,"triangle":3,"pyramid":1,"symmetry":3,"rule of space":3,"lead room":2,"river":0,"road":0,"movement":9,"direction":3},
  "wp-leading-line":{"leading line":6,"curve":0,"space":0,"movement":0,"river":1,"note":"disambiguation page"},
  "wp-symmetry":{"triangle":2,"pyramid":3,"composition":1,"note":"general math; triangle only in geometry nav & quilts"}
}
BODY_SUPPORT={
  "s-curve-composition":"PARTIAL: 'S curve' TERM supported ('sinuous S curve'); but 'roads/rivers/human-body/延长观看路径' UNSUPPORTED (road=0,river=0); 2nd source wp-leading-line=disambiguation -> effectively single-source.",
  "triangular-composition":"PARTIAL: 'triangular format = stability & strength' + Cézanne SUPPORTED; but '尖端指向/指向性/倒三角动感/三人山景' UNSUPPORTED; 2nd source wp-symmetry irrelevant -> effectively single-source.",
  "rule-of-space":"STRONG: definition/principle/technique near-verbatim supported by 'Rule of space' section (eyes direction + runner front + racing car lead room); dedicated subsection = sub-concept covered."
}
SEVEN_SECTIONS_OK=true ; SVG_COUNT=1_each ; SVG_CAPTION_OK=true ; SVG_IN_BOUNDS=true ; REGNOTE_OK=true ; INSTANCE_TYPE_LEVEL=true_each
NEEDS_VERIFICATION={"s-curve-composition":"T/nvc1","triangular-composition":"T/nvc1","rule-of-space":"T/nvc1"}  # 形式一致；但 s-curve/triangular 的待核实声明未覆盖“无来源应用/单源”缺口
PENDING_NOTES_TEMPLATEIZED=true  # 三条 pending_notes 全同：“实例的具体名称、设计者与年代待补充独立来源。”
FABRICATED="none (no fabricated year/name/quote; instance year fields '不适用')"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
VERDICT={"s-curve-composition":"待核实(须返工:'S曲线'术语有支撑;但道路/河流/人体曲线/延长观看路径无来源;2nd=消歧义页→单源;待核实未覆盖)","triangular-composition":"待核实(须返工:三角形=稳定/强度有支撑;但尖端指向/倒三角动感/三人山景无来源;2nd=wp-symmetry无关→单源;待核实未覆盖)","rule-of-space":"合格(Rule of space专节近乎逐句支撑;子概念被覆盖;minor:2nd=消歧义页应改挂Lead room)"}
OVERALL="1合格(rule-of-space)+2待核实/须返工(s-curve,triangular)+0硬性不合格;核心子概念均被wp-composition-visual-arts覆盖(优于第23轮);相似度全<0.54(s-curve全字段0.5189最高,全库最高对s-curve×triangular 0.5166);系统性缺陷=wp-leading-line消歧义页/wp-symmetry误引导致单源+无源应用阐述+待核实口径不实"
BATCH_REWORK="建议定向返工+全批复检(6条):替换无效第二来源(所有wp-leading-line→Lead room或实质条目;triangular的wp-symmetry→真正三角构图来源);清理无源应用阐述(s-curve道路河流/人体曲线,triangular尖端指向/倒三角/三人山景);扩写待核实覆盖单源/弱源缺口;全批复检golden-ratio/diagonal-composition/framing-composition。不因核心概念缺源整批降级重写(核心均有composition条支撑)"
```

*（报告完）*
