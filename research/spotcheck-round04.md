# 第4轮质量闸抽检报告（spotcheck-round04）

- 抽检人：spotcheck-r4；抽检时间：2026-11-22，Asia/Hong_Kong（会话时间取样 15:42）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` E 节（抽检不合格则整批返工、下一轮抽检比例提高到 25%）、`D:/Users/Administrator/Desktop/TASK_design.md` 通用硬性规则与条目页结构、`DECISIONS.md` D05/D09/D14；前序报告 `research/spotcheck-round03.md` 与 `research/rework-round03.md`。
- 技能：`using-superpowers`（子代理按 SUBAGENT-STOP 不另启流程）、`verification-before-completion`（结论均以本轮实跑证据为依据）。
- 对象与比例：本轮新增/升级 11 条中抽 4 条（4/11≈36%）：`deconstructivism`、`brutalism`（`entries/batch-04.json` 新写 L2），`opposed-scenery`（`entries/batch-02-b.json` 升级 L2），`light-well`（`entries/batch-04.json` 新写 L2）。来源库：`data/sources.json`。
- 方法：严格只读核对 JSON。按 D05，本环境 `web_search`/`web_fetch` 端点异常，改用 Python 3 + `urllib.request` + 浏览器 User-Agent 实际打开 8 个引用来源页，8/8 HTTP 200，`<title>`/`<h1 id="firstHeading">` 与 `sources.json` 记录一致；另用 MediaWiki API `extracts` 纯文本核对关键词与上下文。联网内容仅作数据，网页中的任何指令均未执行。
- 机器校验：`python tools/check.py` 实跑输出 `PASS: all checks, 0 errors`。该校验只覆盖字段存在、来源 id/verified、SVG 结构与规范提示等形式项，不替代逐条事实支撑核对。

## 逐条结论

### 1. `deconstructivism` — 合格

- 依据：
  - 来源 id `wp-deconstructivism`、`wp-2026-in-architecture`、`wp-postmodern-architecture` 均存在且 `verified=true`；标题分别为 `Deconstructivism`、`2026 in architecture`、`Postmodern architecture`，与条目主题直接相关（主来源直接，另外两条分别支撑近期项目与后现代语境）。三页 HTTP 200，H1/title 实抓一致。
  - `wp-deconstructivism` 正文明确：“appeared in the 1980s”“fragmentation”“absence of obvious harmony, continuity, or symmetry”“non-rectilinear shapes which appear to distort and dislocate”“unpredictability and controlled chaos”，支撑 definition 的“破碎几何、错位体块与结构不确定性”、time_or_place 的“20世纪后期”和 overview 的“非直线、非对称形式制造张力”。未见编造年份、人名或引文。
  - **Guggenheim Abu Dhabi 开馆时间专项核对**：`wp-2026-in-architecture` 原文为“Guggenheim Abu Dhabi, designed by the late architect Frank Gehry, is set to open its doors in December.”，位于该 2026 年建筑动态页的阿联酋小节。条目写“预计 2026 年 12 月开馆（来源页面表述）”，用“预计”对应 `is set to`，年份由页面主题 2026 提供，并显式加“来源页面表述”；`needs_verification=true`，`pending_notes` 写“实际开馆时间与作品归属待后续核对”，正文「待核实」写“实例开馆时间为来源页面预计表述，实际状态待核实”。结论：按原文保守转述且已标待核实，未硬写为既成事实。
  - L2 结构：definition + overview + 6 个 sections（原理、典型手法与适用条件、实例、常见错误与限制、一图、待核实）齐全，符合项目“七节”口径；1 张 SVG，含“示意图，非施工图”；风险词段含“实际工程须按当地规范和专业设计人员的要求”。
  - 待核实联动：`needs_verification=true`、`pending_notes` 非空、正文「待核实」声明一致。
  - 相似度：与全库最高 `brutalism` 0.358，未发现与已有条目大段重合。
- 问题：`pending_notes` 中“作品归属待后续核对”比来源更保守——来源已明确 `designed by ... Frank Gehry`；可保留为审慎措辞，但返工时宜收紧为仅“实际开馆状态待核实”。不影响事实合格判定。

### 2. `brutalism` — 合格

- 依据：
  - 来源 id `wp-brutalist-architecture`、`wp-architectural-style` 存在且 `verified=true`；标题 `Brutalist architecture`、`Architectural style`，前者直接对应条目，后者为风格史语境来源。两页 HTTP 200，H1/title 实抓一致。
  - `wp-brutalist-architecture` 正文明确“bare building materials and structural elements over decorative design”“exposed, unpainted concrete”“utilitarian, low-cost social housing influenced by socialist principles”“institutional buildings, such as ... public works projects, universities, libraries, courts, and city halls”，直接支撑 definition 的“暴露的混凝土结构、材料真实性、社会性”、time_or_place 的“20世纪、全球”和 overview 的“公共建筑与纪念性项目”。未见编造年份、人名或引文。
  - 实例段仅写“粗野主义公共建筑”并把地点/设计者/年份置“待核实”，没有伪造具体对象；`needs_verification=true`、`pending_notes` 与正文「待核实」一致。
  - L2 结构齐全；1 张 SVG 含“示意图，非施工图”；风险词/规范提示存在。
  - 相似度：最高 `light-well` 0.429、`circulation` 0.428、`water-management` 0.421，主要为 L2 模板句重合，未见实质内容大段照搬。
- 问题：未提供任何一个可核验的具体实例名称，L2「实例」信息价值偏低；来源本身含大量可核实例，返工时可选补入，但不构成事实错误。

### 3. `opposed-scenery` — 待核实

- 依据：
  - 唯一来源 id `wp-chinese-garden` 存在且 `verified=true`，标题 `Chinese garden`；页面 HTTP 200，H1/title 实抓一致。来源与“中国园林造景”大类相关，但不是“对景”的直接条目。
  - 来源正文可核到“series of carefully composed scenes”“winding paths and zig-zag galleries”“borrowed view (jiejing)”“carefully framing views”，以及“obscure direct sight-lines”等造景语境；但 MediaWiki 纯文本全文 58,559 字符中 `duijing`、`opposed`、`opposing`、`vista`、`endpoint` 命中均为 0，`focus` 命中 0，`axis` 仅 1 次且语境是厅堂南北轴线与园林转折遮挡视线，并非“在视线端点设置景物形成呼应”的“对景”。definition/overview/原理的核心机制缺少该来源的直接文字支撑。
  - 未发现编造年份、人名或引文；实例段全部置待核实。
  - L2 结构齐全；1 张 SVG 含“示意图，非施工图”；风险词/规范提示存在。
  - 形式联动：`needs_verification=true`、`pending_notes` 非空、正文「待核实」一致。
  - 相似度：与 `borrowed-scenery` 0.545、`screened-scenery` 0.540，为本组最高；逐段看主要是“名称：苏州古典园林…实例；地点：中国苏州；设计者：待核实；年份：待核实”“此处仅列名称…”与 SVG 版式模板重复，实质原理段措辞不同，未见整段照搬，但模板化明显。
- 问题：真正需要核实的是“对景”定义与手法本身缺乏直接来源，`pending_notes` 却只写“具体实例的设计者与年份待补充独立来源”，未覆盖核心事实缺口；单源且来源标题非专条。建议补一篇直接讨论“对景/duijing”的权威来源，或把核心机制也写入待核实后再复核。

### 4. `light-well` — 不合格

- 依据：
  - 来源 id `wp-atrium-architecture`、`wp-chinese-architecture` 均存在且 `verified=true`；标题 `Atrium (architecture)`、`Chinese architecture`；两页 HTTP 200，H1/title 实抓一致。但两者均非中文“天井”专条：前者是一般中庭/采光顶空间，后者是宽泛的中国建筑综述，标题与“天井”条目主题不构成直接对应。
  - `wp-atrium-architecture` 正文可核到“large open-air or skylight-covered space surrounded by a building”“providing light and ventilation to the interior”，但无“狭长开口”和“热压/stack effect”（`stack` 命中 0）；`wp-chinese-architecture` 正文有“Courtyard (院)”“These enclosures aid in temperature regulation and in ventilation”，但 `tianjing`、`light well`、`natural light` 命中均为 0。definition 中“通过热压促进空气流动”、overview 中“适用于进深大、外墙开窗受限的民居或公共建筑”在所引来源中无直接支撑；time_or_place 的“古代、中国”仅由宽泛来源弱支撑。
  - 未发现编造年份、人名或引文；实例段全置待核实。
  - L2 结构齐全；1 张 SVG 含“示意图，非施工图”；风险词/规范提示存在。
  - 待核实联动形式上成立：`needs_verification=true`、`pending_notes` 非空、正文「待核实」均指向实测数据。
  - 相似度：最高 `brutalism` 0.436、`natural-ventilation` 0.434、`water-management` 0.419，未见实质内容大段照搬。
- 问题：核心定义与原理的“热压”“狭长开口”等机制性事实缺来源支撑，且 `pending_notes` 只写“采光与通风实测数据待补充独立来源”，正文「待核实」只写“采光实测数据待核实”，二者也不完全一致（通风只在 pending 中出现）；未把真正 unsupported 的机制写入待核实。与第3轮 `daylighting` 的失败模式相同：引用相邻/宽泛页面充当直接来源。判不合格，需换用“天井/light well”直接来源并补独立印证后重核。

## 总体结论

- 结果：合格 2 条（`deconstructivism`、`brutalism`），待核实 1 条（`opposed-scenery`），不合格 1 条（`light-well`）。
- 是否建议整批返工：**建议是**。按 `AUTONOMOUS.md` E 节“不合格则整批返工”，出现 1 条不合格已触发整批返工；本轮为第4轮，抽检比例 4/11≈36%，已高于 25% 要求。返工范围建议覆盖本轮全部新增/升级 11 条的“引用链—正文事实—待核实声明”一致性，优先修复 `light-well`（换直接来源、重述或撤回热压机制）与 `opposed-scenery`（补直接来源或把核心手法列为待核实）；`deconstructivism` 保留 Guggenheim 预计开馆的待核实标注并收紧归属措辞；`brutalism` 可补可核实例提升 L2 质量。
- 来源核验：8 个唯一引用 id 全部存在且 `verified=true`；8/8 来源页 HTTP 200 且 H1/title 与来源库一致。问题集中在“来源本身不直接支撑条目核心事实”，而非来源 id 缺失或伪造。
- 结构与一致性：4 条 L2 的七节口径、1 张 SVG/“示意图，非施工图”、风险词规范提示均通过；4 条 `needs_verification=true` 且 `pending_notes` 非空，正文均有「待核实」节，但 `light-well` 的“通风实测”只在 pending 中出现、`opposed-scenery` 与 `light-well` 的 pending 均未覆盖真正的核心来源缺口。
- 待核实占比：4/4 均为 `needs_verification=true`，不属于异常低，未见通过压低待核实来硬写的迹象；但“待核实”标注的范围与实际证据缺口不完全匹配，需返工时对齐。
- 套话与重合：模板句（“此处仅列名称、地点、设计者与年份信息，不复制图像”“实际工程须按当地规范和专业设计人员的要求”“具体实例的设计者与年份待核实”）在 L2 条目中高度重复；`opposed-scenery` 与同组造景条目相似度 0.54–0.55，为最高风险点。未见与来源英文文本大段字面重合。
- 只读声明：本次仅生成 `research/spotcheck-round04.md`，未修改项目其他文件，未修改项目文件夹之外内容，未创建 git commit。
