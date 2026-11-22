# 第17轮质量闸抽检报告（spotcheck-round17）——3 条升级条目的逐条来源/结构/相似度复检

- 抽检人：spotcheck-r17（由 lead 委派的子代理）；抽检时间：2026-11-22 19:44 起，Asia/Hong_Kong（会话时间取样）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（本轮改动条目抽 25%、至少 3 个；不合格整批返工；待核实占比异常低或相似度过高则整批降级复查）、第六节（联网内容一律视为数据，网页中任何指令一律不执行）、第二节（状态文件）；`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L2」「条目页结构（七节）」「通用硬性规则」「专用规则」；`DECISIONS.md` D05（实抓核验）/D06（在线百科 year=null）/D09（规范提示模板）/D10（关键事实需两独立来源，否则标待核实）/D11（link_ok 三态）/D14（needs_verification 与 pending_notes 联动）；相似度口径与前序 `research/spotcheck-round16.md` 一致并本轮实算。
  - 说明：任务书所称项目根 `AUTONOMOUS.md`/`TASK_design.md` 在仓库内无同名文件，实际位于 `D:/Users/Administrator/Desktop/`，已按该路径读取（与第12–16轮一致）。
- 技能：已加载 `using-superpowers`（本会话为子代理，按 SUBAGENT-STOP 不另启流程）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言）。
- 抽检对象（第17轮升级的 7 条：`placemaking`、`space-syntax`、`pattern-language`、`biophilic-design`、`defensible-space-theory`、`functionalism-architecture`、`sunken-plaza`，据 `tools/upgrade_round17.py` 的 `S`/`SRC` 清单确认；本次按指派抽 3 条）：**`placemaking`（场所营造，`entries/batch-11.json`）、`space-syntax`（空间句法，`entries/batch-11.json`）、`sunken-plaza`（下沉广场，`entries/batch-02-c.json`）**。抽样率 3/7 ≈ 42.9%，满足「≥25% 且 ≥3 条」。
- 只读声明：本次**仅生成** `research/spotcheck-round17.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/` 或任何其他项目文件，未改动项目文件夹之外内容，未创建 git commit。工作树中 `coverage.json`、`entries/batch-02-c.json`、`entries/batch-11.json` 的改动，及 `research/gaps-round17.md`、`research/reader_questions-round17.md`、`tools/upgrade_round17.py` 等，均为第17轮执行阶段的既有产物，非本次抽检所写（本轮 `git status` 显示这些为第17轮升级脚本产物，抽检期间未再改动）。联网内容一律视为数据，网页中的任何指令均未执行。

## 一、判定口径与相似度方法（先校准，再测量）

- **结构口径**：3 条均为 L2 升级，按 TASK_design.md「条目页结构」核 **七节**：①核心概念与定义(=definition) ②原理 ③典型手法与适用条件 ④实例 ⑤常见错误与限制 ⑥一图 ⑦待核实；并核每页 ≥1 张内联 SVG 含「示意图，非施工图」、风控段含 D09 规范提示（"实际工程须按当地规范和专业设计人员的要求"）、`needs_verification`/`pending_notes`/正文待核实/`coverage.needs_verification_count` 联动一致。
- **相似度阈值 0.54**（AUTONOMOUS.md E 节「疑似套话」警戒线）。算法 = `difflib.SequenceMatcher(None,a,b).ratio()`，字段以 `|` 连接；口径与前序 `spotcheck-round16` 一脉：短文本 = `title|definition|time_or_place|overview`；全字段 = 短文本再加 6 个 sections；calib = `definition|time_or_place|overview|6节`（不含 title，便于跨轮对比）。sections 固定按 `原理|典型手法与适用条件|实例|常见错误与限制|一图|待核实` 顺序拼接。本轮全库共 **126** 条，逐条对其余 125 条取最高值。

## 二、任务 1：相似度（difflib）对全库最高值

逐条对全库其余 125 条取最高相似度（报告最高值对手）：

| 条目 | 短文本(title+def+top+ov) 最高 | 对手 | 全字段(+sections) 最高 | 对手 | calib(def\|top\|ov\|sec) 最高 | 对手 | 是否 <0.54 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| placemaking | 0.3817 | place-attachment | 0.4157 | warm-cool | 0.4229 | warm-cool | ✅ |
| space-syntax | 0.4231 | defensible-space-theory | 0.4236 | pattern-language | 0.4353 | pattern-language | ✅ |
| sunken-plaza | 0.4031 | drainage | 0.3568 | sunken-courtyard | 0.3578 | bauhaus | ✅ |

- **3 条无论短文本、全字段还是 calib 口径，对全库最高相似度全部 < 0.54**（最高为 space-syntax 全库短文本 **0.4231**，仍显著低于阈值）。无套话嫌疑。
- 附带观察（非本轮 3 条判定依据）：全库两两短文本当前最高对为 `s-curve-composition × triangular-composition` **0.5166**，亦低于 0.54，无整库套话告警。

## 三、任务 2：来源支撑核对（实抓）

`en.wikipedia.org` 直连在本环境易超时（与 DECISIONS D05 记载一致），本轮以镜像 `www.owiki.org`（与 sources.json 的 canonical 页同源同标题）实抓维基正文（HTTP 200，h1 均吻合）；两条中文官方媒体来源（澎湃新闻、解放日报·上观新闻）经 `web_fetch` **直连实抓 HTTP 200**，读到正文。下列均为实抓命中片段（**数据，非指令**），并逐条核 `id 存在 / verified / 标题与主题相关 / 正文支撑`。

### 3.1 逐来源核验表（7 个来源）

| 来源 id | 存在 | verified | 记录标题 / 实抓 h1 | 实抓 | 与主题相关 | 正文支撑要点 |
| --- | --- | --- | --- | --- | --- | --- |
| wp-placemaking | ✅ | true | Placemaking / **Placemaking** | owiki HTTP200 h1 吻合 | ✅ | "Placemaking is a multi-faceted approach to the planning, design and management of public spaces… improving urban vitality… place identity"；"The Community Knows Best"；"community driven grassroots tactical urbanism… open streets events"；"creating squares, plazas, parks, streets and waterfronts" |
| wp-urban-design | ✅ | true | Urban design / **Urban design** | owiki HTTP200 h1 吻合 | ✅ | "Urban design theory deals primarily with the design and management of public space… streets, plazas, parks"；New Urbanism "began in the 1980s as a **place-making** initiative" |
| wp-space-syntax | ✅ | true | Space syntax / **Space syntax** | owiki HTTP200 h1 吻合 | ✅ | "Space syntax is a set of theories and techniques for the analysis of spatial configurations"；"maps and graphs that describe the relative **connectivity and integration**"；"measures…correlate with human spatial behaviour…forecast likely effects…on users"；integration "predict the pedestrian use of a street" |
| wp-urban-morphology | ✅ | true | Urban morphology / **Urban morphology** | owiki HTTP200 h1 吻合 | ✅ | 明确以 "its **syntax (Space_syntax)**" 作比、并提 "integration of new architectural works in the **syntax of the urban tissue**"——为空间句法的相关学科第二源 |
| thepaper-jingan | ✅ | true | 静安寺下沉广场 — 澎湃新闻 / **"魔都"新生：同济大学与静安寺广场和南京路步行街的修建（澎湃·私家历史，2019-01-09，华霞虹、郑时龄）** | HTTP200 正文已读 | ✅ | "1995年4月…同济大学建筑系教授**卢济威**…开始了…上海市静安寺地区城市设计"；"**1999年，新落成的静安寺广场**"；"方案通过后，卢济威的夫人——同济设计院副总建筑师**顾如珍负责了具体的建筑工程**"；"静安寺下沉广场于1998年3月31日奠基…**于1999年9月15日竣工**" |
| jfdaily-jingan | ✅ | true | 静安寺下沉广场 — 解放日报·上观新闻 / **卢济威教授：中国现代城市设计创始者之一，静安寺广场、北外滩……都是他作品（解放日报·上观新闻，2025-11-01，李蕾）** | HTTP200 正文已读 | ✅ | "**1995年，卢济威主持的静安寺地区城市设计**"；"他和团队成员有一个创新的想法——做一个**下沉式广场**，能够把地铁站、公园以及南京西路等周边环境有机结合起来…把商业下压，并与下沉式广场相连" |
| wp-sunken-courtyard | ✅ | true | Sunken courtyard / **Sunken courtyard** | owiki HTTP200 h1 吻合 | ✅（标题相关，但正文仅一句） | "a **sunken courtyard**, sometimes called a **sunken plaza**, is a courtyard **below ground level**."——仅给出泛化定义，**不含静安寺/卢济威/顾如珍/1999 任何实例信息** |

> 7 个来源 id 均存在且 `verified=true`、标题与各自主题直接相关；实抓 HTTP200、h1 吻合。注：两条中文来源在 sources.json 的**记录标题为便于识别的缩写**（非页面 literal h1），主题仍直接相关，属可接受的轻量记法（建议后续把记录标题改为实抓 h1，见 §六）。

### 3.2 关键发现：`sunken-plaza` 实例的“两份来源支撑”并未完全成立（顾如珍 / 1999 为单源）

任务书要求特别核对 `sunken-plaza` 实例“**静安寺下沉广场 / 卢济威主持城市设计、顾如珍负责建筑工程 / 1999年落成**”是否被两份来源支撑。逐要素比对实抓文本：

| 实例要素 | thepaper-jingan（澎湃） | jfdaily-jingan（解放日报·上观） | 是否双源 |
| --- | --- | --- | --- |
| 名称＝静安寺下沉广场 | ✅ "静安寺下沉广场" | ✅ "静安寺广场…下沉式广场" | 双源 ✅ |
| 地点＝中国上海（静安寺） | ✅ "上海市静安寺地区" | ✅ "静安寺地区" | 双源 ✅ |
| 设计者①＝卢济威主持城市设计 | ✅ "卢济威…开始了…静安寺地区城市设计" | ✅ "1995年，卢济威主持的静安寺地区城市设计" | 双源 ✅ |
| 设计者②＝**顾如珍负责建筑工程** | ✅ "副总建筑师**顾如珍负责了具体的建筑工程**" | ❌ **正文未提顾如珍** | **单源** ⚠️ |
| 年份＝**1999年落成** | ✅ "1999年，新落成的静安寺广场…1999年9月15日竣工" | ❌ **正文未给竣工年份**（仅"1995年主持城市设计") | **单源** ⚠️ |

- 结论：实例的**主体（名称/地点/卢济威主持城市设计/下沉广场类型）确为双源支撑**；但任务书点名要核的 **“顾如珍负责建筑工程”“1999年落成”两项具体细节，仅 thepaper-jingan 单源明确记载**，jfdaily-jingan 未覆盖，`wp-sunken-courtyard` 为泛化条目亦不涉及该实例。**按 TASK 通用硬性规则「关键事实至少两个独立来源互相印证，否则标待核实」（D10），这两项属“单源”，尚未达双源互证。**
- **但绝无编造**：顾如珍（含其“同济设计院副总建筑师/卢济威夫人”身份）、1999 年竣工均在 thepaper 原文逐字可查；卢济威、静安寺、下沉广场亦两源可查。第15/16轮 review 所记“多源落实”中，`zgcsb.com`（中国城市网）一源实为“来源澎湃新闻”之转载，与 thepaper 同源，**不构成独立第二源**；故“顾如珍+1999”实质仍是**单一来源（澎湃系）**。此前轮次将 jfdaily 一并算作支撑，属**引证口径偏宽**，本轮据此收窄。
- 处置方向：属**可定点修复的引证厚度问题，非内容虚构**（既不改“不合格整批返工”，也无需删改实例事实），建议见 §六。

## 四、任务 3：逐条结构与内容核对

实跑 `python tools/check.py` → **`PASS: all checks, 0 errors`（EXIT=0）**；并另跑只读结构化脚本逐项核对（下为实测结果）：

| 检查项 | placemaking | space-syntax | sunken-plaza |
| --- | --- | --- | --- |
| 七节齐备（definition+6 节：原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | ✅ 6/6，无缺无多 | ✅ 6/6，无缺无多 | ✅ 6/6，无缺无多 |
| 1 张内联 SVG，viewBox 有效（0 0 760 400） | ✅ 1 张 | ✅ 1 张 | ✅ 1 张 |
| SVG 元素不出界（rect/circle/line/text 坐标实测） | ✅ 无出界 | ✅ 无出界 | ✅ 无出界 |
| SVG 图注含「示意图，非施工图」 | ✅ 命中 | ✅ 命中 | ✅ 命中 |
| 常见错误与限制含 D09 规范提示 | ✅ "实际工程须按当地规范和专业设计人员的要求" | ✅ 同 | ✅ 同 |
| definition/time_or_place/overview 有被引来源正文支撑 | ✅ 强（wp-placemaking 直接定义+urban-design 佐证） | ✅ 强（wp-space-syntax 直接定义+urban-morphology 佐证） | ⚠️ definition 强（wp-sunken-courtyard 定义吻合）；实例见 §3.2 |
| 七节正文有被引来源正文支撑 | ✅（原理/手法均有正文对应；软信号见 §五） | ✅（原理/手法/限制均有正文对应） | ⚠️ 实例 thepaper 强、jfdaily 部分；顾如珍/1999 单源（§3.2） |
| 正文无编造具体年份/人名/引文 | ✅ 无 | ✅ 无 | ✅ 无（顾如珍/1999 均 thepaper 原文可查） |
| 实例为类型性描述、无编造具名项目/设计者/年份 | ✅ "社区参与式公共空间更新（类型性描述）"，设计者/年份"不适用" | ✅ "街区可达性拓扑分析（类型性描述）"，设计者/年份"不适用" | ✅ 具名实例（静安寺下沉广场）经 thepaper 落实，非编造；见 §3.2 双源口径 |
| needs_verification ↔ pending_notes ↔ 正文待核实 ↔ coverage.nvc=1 | ✅ 四者一致 | ✅ 四者一致 | ✅ 结构一致（但实质见 §3.2：pending 仅覆盖“其他实例”，未点明本实例顾如珍/1999 单源） |
| theme/period/region 与 coverage 一致 | ✅ 理论/当代/全球 | ✅ 理论/20世纪/全球 | ✅ 下沉空间/20世纪/全球 |

> `check.py` 已覆盖：必填字段、日期数字合法、来源 verified、无重复、内部链接、SVG 不出界、跨页一致性等，本批 0 errors。

## 五、逐条验收结论

| 条目 | 来源支撑 | 结构/SVG/规范提示 | 待核实联动 | 相似度(短/全) | 结论 |
| --- | --- | --- | --- | --- | --- |
| **placemaking（场所营造）** | wp-placemaking 正文直接给定义（"planning, design and management of public spaces… improve urban vitality… place identity"）+ 手法（tactical urbanism / squares-plazas-parks-waterfronts）+ urban-design 佐证 → **强支撑** def/overview/原理/手法 | 全过 | 四者一致（实例设计者/年份） | 0.3817 / 0.4157 | **合格** |
| **space-syntax（空间句法）** | wp-space-syntax 正文直接给定义（"analysis of spatial configurations"、connectivity&integration、correlate with human spatial behaviour）+ 原理（graph/network、integration predicts pedestrian use）+ 限制（criticism：axial map bias、reliability scrutiny）+ urban-morphology 佐证 → **强支撑** | 全过 | 四者一致 | 0.4231 / 0.4236 | **合格** |
| **sunken-plaza（下沉广场）** | 实例主体 thepaper 强支撑、jfdaily 部分；**“顾如珍负责建筑工程”“1999年落成”仅 thepaper 单源**（jfdaily 未覆盖、wp-sunken-courtyard 不涉实例）；definition 由 wp-sunken-courtyard 定义吻合 | 全过 | 结构一致（实质见 §3.2） | 0.4031 / 0.3568 | **待核实** |

**逐条依据与问题：**

- **placemaking — 合格**
  - 依据：`wp-placemaking` 实抓"Placemaking is a multi-faceted approach to the planning, design and management of public spaces…improve urban vitality and promote people's health, happiness, and well-being…place identity"支撑定义「通过公共空间的策划与设计提升场所活力与认同」；"The Community Knows Best"/"First life, then spaces, then buildings"（Jan Gehl）支撑 overview「把使用者日常活动置于设计中心」；"community driven grassroots tactical urbanism…open streets events"、"creating squares, plazas, parks, streets and waterfronts"支撑典型手法「社区共创、临时活动、街区/广场/滨水」。`wp-urban-design` 以 "place-making initiative"、公共空间"设计与管理"佐证。实例为类型性描述，无具名设计者/年份。
  - 问题（软信号，不据此判不合格）：「把公共空间从'建好'推向'被使用、被认同'」的措辞为**概括性诠释**，两源未逐字出现该句；「短期活动难转化为长期活力」由"Requires Patience/ongoing process"意译而来，属一般实践表述。无编造。

- **space-syntax — 合格**
  - 依据：`wp-space-syntax` 实抓"Space syntax is a set of theories and techniques for the analysis of spatial configurations"、"maps and graphs that describe the relative connectivity and integration"、"measures…correlate with human spatial behaviour…forecast likely effects of architectural and urban space on users"、integration "predict the pedestrian use of a street"，逐句支撑定义「用拓扑与几何方法分析空间连接关系及其与行为关联」、原理「图论、节点与连接、整合度/连接度、人流可达性」、手法「可达性比较/预测人流/前期评估」、限制「模型简化、指标解释需结合现场观察」（对应 Criticism：axial map 偏向长直街、数学可靠性受审视）。`wp-urban-morphology` 以 "syntax (Space_syntax)"/"syntax of the urban tissue"作第二相关源。
  - 问题（软信号）：「遗漏实际使用与时间因素」为对 Criticism 的合理概括，非逐字；无编造。

- **sunken-plaza — 待核实（引证厚度：顾如珍/1999 单源，建议补独立第二源或正文标注单源）**
  - 依据（合格面）：definition「地坪低于周边城市地面的公共广场」与 `wp-sunken-courtyard` "a sunken courtyard, sometimes called a sunken plaza, is a courtyard below ground level"吻合；实例「静安寺下沉广场 / 中国上海 / 卢济威主持城市设计 / 顾如珍负责建筑工程 / 1999年落成」经 `thepaper-jingan` **逐字强支撑**（"卢济威…城市设计"、"顾如珍负责了具体的建筑工程"、"1999年，新落成的静安寺广场…1999年9月15日竣工"），`jfdaily-jingan` 佐证"卢济威主持城市设计 + 下沉式广场"。**无编造**。
  - 问题（待核实面）：任务书点名的 **“顾如珍负责建筑工程”“1999年落成”两项，仅 thepaper-jingan 单源明确，jfdaily-jingan 未提顾如珍、未给竣工年份，wp-sunken-courtyard 不涉该实例** → 未达「两份独立来源互相印证」（D10）。且条目 `pending_notes` / `正文待核实` 只写"**其他**下沉广场实例的设计者与年代待核实"，**未涵盖本实例这两项单源细节**，存在「正文把单源细节当既证事实、结构化待核实声明未覆盖之」的错位。→ 判 **待核实**。
  - 处置建议：属**可定点修复的引证/取源问题，非内容虚构**，不按“不合格整批返工”处理；闭环前二选一（见 §六）。

## 六、总体结论与是否整批返工

- **抽检结果：2 合格（placemaking、space-syntax）+ 1 待核实（sunken-plaza）。**
  - 来源：7 个来源 id 均存在且 `verified=true`、标题与主题直接相关；实抓（owiki 镜像 + 澎湃/上观直连）HTTP200、h1 吻合。placemaking/space-syntax 的 definition/time_or_place/overview/七节均有被引来源正文强支撑；3 条实例**均未发现编造年份、人名或引文**。sunken-plaza 因“顾如珍/1999”为澎湃单源（jfdaily 未覆盖）而“双源支撑”不完整（见 §3.2）。
  - 结构：3 条七节完整、各含 1 张 SVG 且含「示意图，非施工图」、元素不出界、风控段含 D09 规范提示、`check.py` 0 errors（EXIT=0）。
  - 待核实：3 条 `needs_verification=true` ↔ `pending_notes` ↔ 正文「待核实」 ↔ `coverage.needs_verification_count=1` **结构上四者一致**（sunken-plaza 的实质偏差见 §3.2/§五）。
  - 相似度：3 条对全库最高（短文本/全字段/calib 任一）均 **< 0.54**（最大 0.4353）；全库两两短文本最高 0.5166 亦低于阈值。
- **整批返工建议：不建议整批返工。** 无“不合格”条目，按 AUTONOMOUS E「不合格才整批返工」不触发；亦无待核实占比异常或相似度超阈。
- **闭环建议（非返工，定点修复）**：
  1. **sunken-plaza（核心闭环项）**：二选一——(a) 补一条**真正独立**且明确覆盖“顾如珍负责建筑工程 / 1999 年落成”的权威来源（如同一时期《建筑学报》/同济官方/上海地方志等非澎湃系来源），重抓核对后再视情收窄待核实；或 (b) 维持现有双源事实不变，但在 `pending_notes` 与 `sections.待核实` 明确写入「本实例“顾如珍负责建筑工程、1999年落成”现为澎湃新闻单源、待补独立第二源」，使**结构化待核实声明覆盖到这两项单源细节**，与 D10 对齐。**不建议**把 jfdaily 或 zgcsb 直接计作顾如珍/1999 的独立第二源（前者未提、后者系澎湃转载同源）。
  2. **来源记录标题（Minor）**：`thepaper-jingan`/`jfdaily-jingan` 的 sources.json 记录标题宜改为实抓 literal h1（如"“魔都”新生：同济大学与静安寺广场和南京路步行街的修建"、"卢济威教授：中国现代城市设计创始者之一…"），便于复核溯源；不影响 verified/主题相关性判定。
  3. 本轮 7 条升级集仅抽 3 条（42.9%），其余 `pattern-language`、`biophilic-design`、`defensible-space-theory`、`functionalism-architecture` 建议在后续抽检或同闸门补足，以完成 7 条整体闭环。

---

### 机器可读汇总

```
ROUND=17
SCOPE=["placemaking","space-syntax","sunken-plaza"]   # 抽自第17轮7条升级集，3/7≈42.9%
ROUND17_UPGRADE_SET=["placemaking","space-syntax","pattern-language","biophilic-design","defensible-space-theory","functionalism-architecture","sunken-plaza"]
SIM_METHOD="difflib.SequenceMatcher.ratio(); join='|'; short=title|definition|time_or_place|overview; full=+6 sections; calib=def|top|ov|sections"
SIM_MAX_SHORT={"placemaking":[0.3817,"place-attachment"],"space-syntax":[0.4231,"defensible-space-theory"],"sunken-plaza":[0.4031,"drainage"]}
SIM_MAX_FULL={"placemaking":[0.4157,"warm-cool"],"space-syntax":[0.4236,"pattern-language"],"sunken-plaza":[0.3568,"sunken-courtyard"]}
SIM_MAX_CALIB={"placemaking":[0.4229,"warm-cool"],"space-syntax":[0.4353,"pattern-language"],"sunken-plaza":[0.3578,"bauhaus"]}
ALL_SIM_UNDER_0.54=true ; LIBRARY_SIZE=126
GLOBAL_LIBRARY_MAX_SHORT={"0.5166":"s-curve-composition×triangular-composition"}  # 非本轮3条，仅观察
SOURCES_ALL_EXIST_VERIFIED_RELATED=true
SOURCES=["wp-placemaking","wp-urban-design","wp-space-syntax","wp-urban-morphology","thepaper-jingan","jfdaily-jingan","wp-sunken-courtyard"]
FETCH={"en.wikipedia.org":"timeout-prone","www.owiki.org":"HTTP200 h1 matched (wp-placemaking/urban-design/space-syntax/urban-morphology/sunken-courtyard)","m.thepaper.cn":"HTTP200 body read","www.jfdaily.com":"HTTP200 body read"}
SUNKEN_PLAZA_SOURCE_CHECK={
  "静安寺下沉广场/中国上海/卢济威主持城市设计":"DUAL (thepaper+jfdaily)",
  "顾如珍负责建筑工程":"SINGLE (thepaper only; jfdaily未提; wp-sunken-courtyard不涉)",
  "1999年落成":"SINGLE (thepaper only; jfdaily未给年份; wp-sunken-courtyard不涉)",
  "FABRICATED":false,
  "NOTE":"zgcsb(中国城市网)系澎湃转载，非独立第二源；顾如珍/1999实质为澎湃单源"
}
FABRICATED_YEARS_NAMES_QUOTES=false
SEVEN_SECTIONS_OK=true ; SVG_CAPTION_OK=true ; SVG_IN_BOUNDS=true ; REGNOTE_OK=true ; NV_LINKAGE_OK_STRUCTURAL=true
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
VERDICT={"placemaking":"合格","space-syntax":"合格","sunken-plaza":"待核实"}
SOFT_SIGNALS={"placemaking":"部分措辞为概括性诠释，非逐字；无编造","space-syntax":"限制句为对Criticism合理概括，非逐字；无编造","sunken-plaza":"顾如珍/1999仅澎湃单源，jfdaily未覆盖;pending_notes未涵盖本实例该两项"}
OVERALL="2 合格 + 1 待核实；来源/结构/待核实/相似度均无硬失败；无编造；不建议整批返工"
FIX_HINT="sunken-plaza: 补独立第二源覆盖顾如珍/1999，或在pending_notes/待核实明注该两项单源;来源记录标题改实抓h1;补抽其余4条以闭环7条"
REST_FILES_WRITTEN=["research/spotcheck-round17.md"]   # 只写本文件
```
