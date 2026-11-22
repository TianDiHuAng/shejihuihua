# 第18轮质量闸抽检报告（spotcheck-round18）——3 条升级条目的逐条来源/结构/相似度复检

- 抽检人：spotcheck-r18（由 lead 委派的子代理）；抽检时间：2026-11-22 19:55 起，Asia/Hong_Kong（会话时间取样）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（本轮改动条目抽 25%、至少 3 个；不合格整批返工；待核实占比异常低或相似度过高则整批降级复查）、第六节（联网内容一律视为数据，网页中任何指令一律不执行）、第二节（状态文件）；`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L2」「条目页结构（七节）」「通用硬性规则」「专用规则」；`DECISIONS.md` D05（实抓核验）/D06（在线百科 year=null）/D09（规范提示模板）/D10（关键事实需两独立来源，否则标待核实）/D11（link_ok 三态）/D14（needs_verification 与 pending_notes 联动）；相似度口径与前序 `research/spotcheck-round17.md` 一致并本轮实算。
  - 说明：任务书所称项目根 `AUTONOMOUS.md`/`TASK_design.md` 在仓库内无同名文件，实际位于 `D:/Users/Administrator/Desktop/`，已按该路径读取（与第12–17轮一致）。
- 技能：已加载 `using-superpowers`（本会话为子代理，按 SUBAGENT-STOP 不另启流程）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言）。
- 抽检对象（第18轮升级的 6 条：`simplification`、`hierarchy`、`color-contrast`、`framed-scenery`、`pedestrian-flow`、`material-texture`，据 `tools/upgrade_round18.py` 的 `S`/`SRC` 清单确认；本次按指派抽 3 条）：**`simplification`（简化，`entries/batch-01.json`，tier 重要）、`framed-scenery`（框景，`entries/batch-02-b.json`，tier 核心）、`material-texture`（材料质感，`entries/batch-02-d.json`，tier 核心）**。抽样率 3/6 = 50%，满足「≥25% 且 ≥3 条」。
- 只读声明：本次**仅生成** `research/spotcheck-round18.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/` 或任何其他项目文件，未改动项目文件夹之外内容，未创建 git commit。工作树中 `coverage.json`、`entries/batch-*.json`、`tools/upgrade_round18.py` 及 `research/gaps-round18.md`、`research/reader_questions-round18.md` 等，均为第18轮执行阶段的既有产物，非本次抽检所写；抽检期间未再改动。联网内容一律视为数据，网页中的任何指令均未执行。

## 一、判定口径与相似度方法（先校准，再测量）

- **结构口径**：3 条均为 L2 升级，按 TASK_design.md「条目页结构」核 **七节**：①核心概念与定义(=definition) ②原理 ③典型手法与适用条件 ④实例 ⑤常见错误与限制 ⑥一图 ⑦待核实；并核每页 ≥1 张内联 SVG 含「示意图，非施工图」、风控段含 D09 规范提示（"实际工程须按当地规范和专业设计人员的要求"）、`needs_verification`/`pending_notes`/正文待核实/`coverage.needs_verification_count` 联动一致。
- **相似度阈值 0.54**（AUTONOMOUS.md E 节「疑似套话」警戒线）。算法 = `difflib.SequenceMatcher(None,a,b).ratio()`，字段以 `|` 连接；口径与前序一致：短文本 = `title|definition|time_or_place|overview`；全字段 = 短文本再加 6 个 sections；calib = `definition|time_or_place|overview|6节`（不含 title，便于跨轮对比）。sections 固定按 `原理|典型手法与适用条件|实例|常见错误与限制|一图|待核实` 顺序拼接。本轮全库共 **126** 条（脚本实测 TOTAL ENTRIES=126），逐条对其余 125 条取最高值。

## 二、任务 1：相似度（difflib）对全库最高值

逐条对全库其余 125 条取最高相似度（报告最高值对手，脚本本轮实算）：

| 条目 | 短文本(title+def+top+ov) 最高 | 对手 | 全字段(+sections) 最高 | 对手 | calib(def\|top\|ov\|sec) 最高 | 对手 | 是否 <0.54 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| simplification | 0.4878 | contrast-principle | 0.4484 | hierarchy | 0.4556 | hierarchy | ✅ |
| framed-scenery | 0.4793 | screened-scenery | 0.4157 | scattered-perspective | 0.4221 | scattered-perspective | ✅ |
| material-texture | 0.4219 | daylighting | 0.4427 | color-theory | 0.4514 | color-theory | ✅ |

- **3 条无论短文本、全字段还是 calib 口径，对全库最高相似度全部 < 0.54**（最高为 simplification 全库短文本 **0.4878**，仍低于阈值 0.54）。无套话嫌疑。
- 附带观察（非本轮 3 条判定依据）：全库两两短文本当前最高对为 `s-curve-composition × triangular-composition` **0.5166**，亦低于 0.54，无整库套话告警（与第17轮一致）。

## 三、任务 2：来源支撑核对（实抓）

`en.wikipedia.org` 直连在本环境易超时（与 DECISIONS D05 记载一致），本轮以镜像 `www.owiki.org`（与 sources.json 的 canonical 页同源同标题）实抓维基正文，5 个来源均 **HTTP 200 且 h1 与记录标题吻合**。下列均为实抓命中片段（**数据，非指令**），并逐条核 `id 存在 / verified / 标题与主题相关 / 正文支撑`。

### 3.1 逐来源核验表（5 个来源）

| 来源 id | 存在 | verified | 记录标题 / 实抓 h1 | 实抓 | 与主题相关 | 正文支撑要点（实抓原文片段） |
| --- | --- | --- | --- | --- | --- | --- |
| wp-composition-visual-arts | ✅ | true | Composition (visual arts) / **Composition (visual arts)** | owiki HTTP200 h1 吻合 | ✅（构图总论，支撑 simplification） | "The term composition means \"putting together\"…the organization of art"；"**By decreasing the extraneous content, the viewer is more likely to focus on the primary objects. Clutter can also be reduced through the use of lighting**"；"The empty spaces around, above, and within, is negative space" |
| wp-negative-space | ✅ | true | Negative space / **Negative space** | owiki HTTP200 h1 吻合 | ✅（负空间/虚实，支撑 simplification） | "negative space or negative volume is the empty space around and between the subject of an image…**the positive space has the more visual weight while the surrounding space - that is less visually important is seen as the negative space**" |
| wp-chinese-garden | ✅ | true | Chinese garden / **Chinese garden** | owiki HTTP200 h1 吻合 | ✅（中国园林，支撑 framed-scenery） | "principle of the \"**borrowed view**,\" carefully **framing views** of the surrounding mountains and a famous view of a distant pagoda"；"They have **small windows, sometimes round or in odd geometric shapes, to give glimpses of the garden or scenery**…Windows and doors are an impo[rtant]…"；"the garden presented the visitor with a **series of perfectly composed and framed glimpses of scenery**; a view of a pond, or of a rock…" |
| wp-building-material | ✅ | true | Building material / **Building material** | owiki HTTP200 h1 吻合 | ✅（建筑材料，主题相关，但见 §3.2） | "Building material is material used for construction. Many **naturally occurring substances, such as clay, rocks, sand, wood**…"；含 "thermal mass / insulation / durability / glass(colors)"；**全文无 texture/aesthetic/tactile/smooth/transparen/reflect/psychological 任何一处** |
| wp-vernacular-architecture | ✅ | true | Vernacular architecture / **Vernacular architecture** | owiki HTTP200 h1 吻合 | ✅（乡土建筑，主题相关，但见 §3.2） | "**Local materials would be used as a matter of course**…"；"Buildings in cold climates invariably have **high thermal mass or significant amounts of insulation**…"；"aesthetic considerations, though present to some small degree, being quite minimal"；**全文无 texture/tactile/光线反射/心理温度任何一处** |

> 5 个来源 id 均存在且 `verified=true`、标题与各自主题直接相关；实抓 HTTP200、h1 吻合。`link_ok` 均为 true。`year=null` 符合 D06（在线百科记 null）。

### 3.2 关键发现：`material-texture` 的定义/原理缺被引来源正文支撑（两条来源均不涉“质感—感知”）

任务书要求核对 `material-texture` 的 definition/overview/七节是否被 `wp-building-material`、`wp-vernacular-architecture` 正文支撑。逐句比对实抓文本：

| 条目主张 | wp-building-material 实抓 | wp-vernacular-architecture 实抓 | 是否被支撑 |
| --- | --- | --- | --- |
| 定义：**材料表面质感对视觉与触觉感受的作用** | ❌ 全文无 texture/tactile/触感/视觉感知，仅列材料类型与热工/耐久 | ❌ 全文无 texture/tactile；且明言 aesthetic "quite minimal" | **未见支撑** ⚠️ |
| 原理：**粗糙/光滑/透明/吸光…影响光线反射、触感与空间心理温度** | ❌ 无 smooth/transparen/reflect/psychological；“surface”仅指"external surface covering"（金属屋面） | ❌ 无 | **未见支撑** ⚠️ |
| 手法：**以质感对比划分界面、以天然材质传递温暖** | 部分：支持“天然材料(natural substances/clay/wood)” | 部分：支持“本地材料(local materials)”与热工 | 部分支撑 |
| 常见错误：**维护/清洁成本、防滑与防火按规范校核** | 部分：支持 durability / 寿命成本 | — | 部分 + D09 规范提示 |

- 结论：`wp-building-material` 是“建筑材料类型与性能”总论（黏土/石/砂/木/金属/玻璃，热工、耐久），`wp-vernacular-architecture` 是“气候与本地材料驱动的乡土建造”，**两源均未涉及“表面质感→视觉/触觉/光线反射/心理温度”这一核心论点**。即：来源虽 `verified=true` 且主题相关，但**正文不能支撑本条目 definition/原理的核心表述**（不是“编造来源”，而是“引证与正文主张不匹配”）。
- 与之对照，`simplification`、`framed-scenery` 的核心表述在实际抓取正文中有直接对应（见 §五），不属此问题。

## 四、任务 3：逐条结构与内容核对

实跑 `python tools/check.py` → **`PASS: all checks, 0 errors`（EXIT=0）**；并另跑只读结构化脚本逐项核对（下为实测结果）：

| 检查项 | simplification | framed-scenery | material-texture |
| --- | --- | --- | --- |
| 七节齐备（definition+6 节：原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | ✅ 6/6，无缺无多 | ✅ 6/6，无缺无多 | ✅ 6/6，无缺无多 |
| 1 张内联 SVG，viewBox 有效（0 0 760 400） | ✅ 1 张 | ✅ 1 张 | ✅ 1 张 |
| SVG 元素不出界（rect/circle/line/text 坐标实测，check.py 亦校验） | ✅ 无出界 | ✅ 无出界 | ✅ 无出界 |
| SVG 图注含「示意图，非施工图」 | ✅ 命中 | ✅ 命中 | ✅ 命中 |
| 常见错误与限制含 D09 规范提示 | ✅ "实际工程须按当地规范和专业设计人员的要求" | ✅ 同 | ✅ 同 |
| definition/time_or_place/overview 有被引来源正文支撑 | ✅ 强（composition "decreasing extraneous content→focus"；negative-space 虚实权重） | ✅（wp-chinese-garden "framing views"/"framed glimpses"/门窗取景） | ⚠️ **definition/原理 未见支撑（§3.2）** |
| 七节正文有被引来源正文支撑 | ✅（原理/手法有对应；软信号见 §五） | ✅（原理/手法/一图均有对应；软信号见 §五） | ⚠️ 手法/限制部分；原理未见 |
| 正文无编造具体年份/人名/引文 | ✅ 无 | ✅ 无 | ✅ 无 |
| 实例为类型性描述、无编造具名项目/设计者/年份 | ✅ “繁复场景的简化处理（类型性描述）”，设计者/年份“不适用” | ✅ “园林门洞取景（类型性描述）”，地点中国苏州，设计者/年份“不适用” | ✅ “质感对比的室内界面（类型性描述）”，设计者/年份“不适用” |
| needs_verification ↔ pending_notes ↔ 正文待核实 ↔ coverage.nvc=1 | ✅ 四者一致（均指实例/作者/年代） | ✅ 四者一致 | ⚠️ 结构一致（但 pending/待核实仅覆盖“实例设计者年代”，未覆盖 §3.2 的定义支撑缺口） |
| theme/period/region 与 coverage 一致 | ✅ 理论/跨时期/全球 | ✅ 造景/古代/中国 | ✅ 材料/跨时期/全球 |
| source_count 与 sources 一致 | ✅ 2 | ✅ 1（单源） | ✅ 2 |

> `check.py` 已覆盖：必填字段、日期数字合法、来源 verified、无重复、内部链接、SVG 不出界、跨页一致性等，本批 0 errors。

## 五、逐条验收结论

| 条目 | 来源支撑 | 结构/SVG/规范提示 | 待核实联动 | 相似度(短/全/calib) | 结论 |
| --- | --- | --- | --- | --- | --- |
| **simplification（简化）** | wp-composition-visual-arts 正文"decreasing the extraneous content→focus on primary objects"直接支撑定义与原理；negative-space 虚实权重佐证 overview → **强支撑** | 全过 | 四者一致 | 0.4878 / 0.4484 / 0.4556 | **合格** |
| **framed-scenery（框景）** | wp-chinese-garden 正文"carefully framing views"、"small windows…to give glimpses of scenery"、"series of perfectly composed and framed glimpses of scenery"直接支撑定义/原理/手法 → **单源强支撑** | 全过 | 四者一致 | 0.4793 / 0.4157 / 0.4221 | **合格（单源，needs_verification=true 正确）** |
| **material-texture（材料质感）** | 两源主题相关但**正文均不涉及“质感→视觉/触觉/光线反射/心理温度”**；仅部分支撑“天然/本地材料、热工、耐久” → **核心定义/原理未见支撑（§3.2）** | 全过 | 结构一致但实质偏差（pending 未覆盖定义缺口） | 0.4219 / 0.4427 / 0.4514 | **待核实** |

**逐条依据与问题：**

- **simplification — 合格**
  - 依据：`wp-composition-visual-arts` 实抓"By decreasing the extraneous content, the viewer is more likely to focus on the primary objects. Clutter can also be reduced through the use of lighting"逐句支撑定义「删减次要细节以突出主体的构图方法」与原理「删去次要信息、保留结构要点…让主体更易被识别」；"The empty spaces around, above, and within, is negative space"与 `wp-negative-space`"positive space has the more visual weight while the surrounding space…is seen as the negative space"共同支撑 overview「通过取舍建立清晰的视觉层次」。实例为类型性描述（设计者/年份“不适用”），无编造。
  - 问题（软信号，不据此判不合格）：典型手法「合并相近色块」与「信息密集的画面与界面」为对构图总论（"clutter reduced"、"elements of design"）的合理外推，非逐字；无编造。

- **framed-scenery — 合格（单源，已按 D10 标待核实）**
  - 依据：`wp-chinese-garden` 实抓"principle of the 'borrowed view,' carefully framing views of the surrounding mountains"、"They have small windows, sometimes round or in odd geometric shapes, to give glimpses of the garden or scenery…Windows and doors are an impo[rtant]"、"the garden presented the visitor with a series of perfectly composed and framed glimpses of scenery"逐句支撑定义「以门窗、洞口或枝干围合景物形成画面」、原理「用门洞、窗框…把连续风景裁成一幅画，强化焦点与层次」与手法「在游线上设置取景洞口，控制画幅比例与对景内容」；"evolved over three thousand years"支撑 time_or_place「古代中国」。实例为类型性描述（地点中国苏州，设计者/年份“不适用”），无编造。
  - 单源确认：`sources` 仅 `["wp-chinese-garden"]`（`source_count=1`），**`needs_verification=true` 属实且正确**（D10：关键事实未达双独立源→标待核实）；`pending_notes`="框景的独立专门来源与具体实例设计者、年代待核实。"与 `sections.待核实` 同义、与 `coverage.needs_verification_count=1` 一致。
  - 问题（软信号）：「枝干」取景为对园林取景手法的合理补充，原文以门窗/借景为主，非逐字；单源已如实标注待核实，无编造。

- **material-texture — 待核实（定义/原理缺被引来源正文支撑，且结构化待核实未覆盖该缺口）**
  - 依据（合格面）：结构/ SVG / D09 规范提示全过；实例为类型性描述、无编造年份/人名/引文；def/原理措辞为通识性表述，`check.py` 0 errors。
  - 问题（待核实面）：见 §3.2——`wp-building-material`（材料类型/热工/耐久）与 `wp-vernacular-architecture`（气候/本地材料/热工）**正文均未涉及“表面质感→视觉/触觉/光线反射/心理温度”**，故 definition 与 原理 的核心表述**没有可核对的被引正文支撑**（来源已 verified，但内容不匹配）；同时 `pending_notes`/`sections.待核实` 仅写“实例的具体名称、设计者与年代待补充独立来源”，**未涵盖定义/原理的支撑缺口**，属“结构与正文待核实错位”（与第17轮 sunken-plaza 同类）。→ 判 **待核实**。
  - 处置建议：属**取源/表述可定点修复问题，非内容虚构**（不按“不合格整批返工”处理）；闭环二选一——(a) 补一条真正直接支撑“材料表面质感/触感/光反射/心理温度”的权威来源（如材料与感知、surface/texture in architecture 类词条或教材）；或 (b) 将 definition/原理 收窄至现两源可支撑范围（材料类型、天然/本地材料、热工与耐久），并在 `pending_notes` 与 `sections.待核实` 明写“质感—感知相关表述待补来源”。

## 六、总体结论与是否整批返工

- **抽检结果：2 合格（simplification、framed-scenery）+ 1 待核实（material-texture）。**
  - 来源：5 个来源 id 均存在且 `verified=true`、标题与主题直接相关；实抓（owiki 镜像）HTTP200、h1 吻合；`framed-scenery` 确为单源且 `needs_verification=true` 正确。simplification/framed-scenery 的 definition/time_or_place/overview/七节均有被引来源正文支撑；3 条实例**均未发现编造年份、人名或引文**。material-texture 因两源均不涉“质感—感知”而核心定义/原理缺支撑（§3.2）。
  - 结构：3 条七节完整、各含 1 张 SVG 且含「示意图，非施工图」、元素不出界、风控段含 D09 规范提示、`check.py` 0 errors（EXIT=0）。
  - 待核实：3 条 `needs_verification=true` ↔ `pending_notes` ↔ 正文「待核实」 ↔ `coverage.needs_verification_count=1` **结构上四者一致**（material-texture 的实质偏差见 §3.2/§五）。
  - 相似度：3 条对全库最高（短文本/全字段/calib 任一）均 **< 0.54**（最大 0.4878）；全库两两短文本最高 0.5166 亦低于阈值。
- **整批返工建议：不建议整批返工。** 无“不合格”条目，按 AUTONOMOUS E「不合格才整批返工」不触发；亦无待核实占比异常或相似度超阈；3 条均无编造。
- **闭环建议（非返工，定点修复）**：
  1. **material-texture（核心闭环项）**：二选一——(a) 补一条**直接支撑“材料表面质感/触感/光反射/心理温度”**的权威来源并重抓核对后收窄待核实；或 (b) 维持两源事实，把 definition/原理 收窄至“材料类型/天然与本地材料/热工与耐久”，并在 `pending_notes` 与 `sections.待核实` 明注“质感—感知表述待补来源”，使结构化待核实声明覆盖真实缺口（对齐 D10）。
  2. **pending_notes 去模板化（Minor）**：`simplification`/`material-texture` 的 `pending_notes` 现为同一模板句“实例的具体名称、设计者与年代待补充独立来源”；建议按各自实际缺口（simplification：实例作品与作者年代；material-texture：定义支撑+实例）分别撰写，避免“四者一致”仅停留形式。
  3. 本轮 6 条升级集仅抽 3 条（50%），其余 `hierarchy`、`color-contrast`、`pedestrian-flow` 建议在后续抽检或同闸门补足，以完成 6 条整体闭环。

---

### 机器可读汇总

```
ROUND=18
SCOPE=["simplification","framed-scenery","material-texture"]   # 抽自第18轮6条升级集，3/6=50%
ROUND18_UPGRADE_SET=["simplification","hierarchy","color-contrast","framed-scenery","pedestrian-flow","material-texture"]
FILES={"simplification":"entries/batch-01.json","framed-scenery":"entries/batch-02-b.json","material-texture":"entries/batch-02-d.json"}
SIM_METHOD="difflib.SequenceMatcher.ratio(); join='|'; short=title|definition|time_or_place|overview; full=+6 sections; calib=def|top|ov|sections"
SIM_MAX_SHORT={"simplification":[0.4878,"contrast-principle"],"framed-scenery":[0.4793,"screened-scenery"],"material-texture":[0.4219,"daylighting"]}
SIM_MAX_FULL={"simplification":[0.4484,"hierarchy"],"framed-scenery":[0.4157,"scattered-perspective"],"material-texture":[0.4427,"color-theory"]}
SIM_MAX_CALIB={"simplification":[0.4556,"hierarchy"],"framed-scenery":[0.4221,"scattered-perspective"],"material-texture":[0.4514,"color-theory"]}
ALL_SIM_UNDER_0.54=true ; LIBRARY_SIZE=126
GLOBAL_LIBRARY_MAX_SHORT={"0.5166":"s-curve-composition×triangular-composition"}  # 非本轮3条，仅观察
SOURCES_ALL_EXIST_VERIFIED_RELATED=true
SOURCES=["wp-composition-visual-arts","wp-negative-space","wp-chinese-garden","wp-building-material","wp-vernacular-architecture"]
FRAMED_SCENERY_SINGLE_SOURCE=true ; NEEDS_VERIFICATION_TRUE=true
FETCH={"en.wikipedia.org":"timeout-prone","www.owiki.org":"HTTP200 h1 matched (all 5 sources)"}
MATERIAL_TEXTURE_SUPPORT={
  "definition(质感→视觉触觉)":"UNSUPPORTED by either cited body (building-material: no texture/tactile/aesthetic; vernacular: no texture/tactile, aesthetic 'quite minimal')",
  "原理(粗糙/光滑/透明/吸光→光反射/触感/心理温度)":"UNSUPPORTED by either cited body",
  "手法(天然材质/质感对比)":"PARTIAL (natural/local materials, thermal)",
  "FABRICATED":false,
  "PENDING_COVERS_GAP":false
}
SIMPLIFICATION_SUPPORT="STRONG (composition: 'decreasing the extraneous content -> focus on primary objects'; negative-space: visual weight)"
FRAMED_SCENERY_SUPPORT="STRONG single-source (chinese-garden: 'carefully framing views', 'small windows...glimpses of scenery', 'series of perfectly composed and framed glimpses')"
FABRICATED_YEARS_NAMES_QUOTES=false
SEVEN_SECTIONS_OK=true ; SVG_CAPTION_OK=true ; SVG_IN_BOUNDS=true ; REGNOTE_OK=true
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
VERDICT={"simplification":"合格","framed-scenery":"合格","material-texture":"待核实"}
SOFT_SIGNALS={"simplification":"手法'合并相近色块/信息密集界面'为合理外推非逐字；无编造","framed-scenery":"'枝干'取景为合理补充非逐字；单源已如实标待核实；无编造","material-texture":"定义/原理缺被引正文支撑；pending仅覆盖实例、未覆盖定义缺口"}
OVERALL="2 合格 + 1 待核实；来源/结构/相似度无硬失败；无编造；不建议整批返工"
FIX_HINT="material-texture: 补直接支撑'质感-感知'的第二/替来源或收窄定义至材料类型/热工，并在pending_notes/待核实明注;pending_notes去模板化;补抽hierarchy/color-contrast/pedestrian-flow以闭环6条"
REST_FILES_WRITTEN=["research/spotcheck-round18.md"]   # 只写本文件
```
