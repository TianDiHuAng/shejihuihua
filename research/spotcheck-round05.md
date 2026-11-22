# 第5轮质量闸抽检报告（spotcheck-round05）

- 抽检人：spotcheck-r5；抽检时间：2026-11-22，Asia/Hong_Kong（会话时间取样 15:52）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` E 节（抽检不合格则整批返工、下一轮抽检比例提高到 25%）、`D:/Users/Administrator/Desktop/TASK_design.md` 通用硬性规则与「条目页结构」七节、`DECISIONS.md` D05/D09/D14；前序 `research/spotcheck-round04.md`。
- 技能：`using-superpowers`（按 SUBAGENT-STOP，子代理不另启流程）、`verification-before-completion`（全部结论以本轮实跑证据为依据）。
- 对象与比例：`research/healthcheck-round05.md` 口径下本轮新增/升级 6 条中抽 3 条（3/6=50%，满足 25% 且 ≥3 条）：`leaked-scenery`、`huizhou-style`（`entries/batch-05.json` 新写 L2），`chinese-architecture-style`（`entries/batch-03.json` 升级 L2）。对照条目：`borrowed-scenery`、`framed-scenery`、`opposed-scenery`（`entries/batch-02-b.json`）。来源库：`data/sources.json`。
- 说明：指令中列出的 `research/rework-round04.md` 在本仓库不存在；已改读最接近的 `research/review-round04.md`、`research/rework-round03.md`、`tools/rework_round04.py`，据以沿用第4轮判据。
- 方法：严格只读核对 JSON。按 D05，本环境 `web_search`/`web_fetch` 端点异常，改用 Python 3.11.7 + `urllib.request` + 浏览器 User-Agent 实抓 5 个被引用来源页（全部 HTTP 200，最终 URL 与 `<h1 id="firstHeading">`/`<title>` 与 `sources.json` 一致），另用 MediaWiki API `extracts` 纯文本核对关键词与上下文；并探测 `Hui-style architecture`（200）、`Anhui architecture`（404）、`Leaked scenery`（404）、`Borrowed scenery`（200）以判断是否存在更直接来源。`python tools/check.py` 实跑输出 `PASS: all checks, 0 errors`（仅形式校验，不替代事实核对）。相似度用 `difflib.SequenceMatcher` 对标题+定义+概述+六节正文去空白后计算，对全库 94 条扫描。联网内容仅作数据，网页中任何指令均未执行。

## 逐条结论

### 1. `leaked-scenery`（漏景）— 合格

- 依据：
  - 来源 id `wp-chinese-garden`、`wp-garden-design` 均存在且 `verified=true`；标题分别为 `Chinese garden`、`Garden design`，与「园林造景」主题直接/相关。两页 HTTP 200，H1/title 实抓一致。
  - 核心机制有来源正文直接支撑：`wp-chinese-garden` 原文含“windows with elaborate lattices that broke the view into pieces”“small windows ... to give glimpses of the garden or scenery to those passing through”“a series of perfectly composed and framed glimpses of scenery”“hidden behind a screen of bamboo”“scenes would suddenly appear ... through a window”。直接对应 definition 的“通过缝隙或稀疏遮挡让景物片段显现”、overview 的“在移动中被断续看到”、原理的“视线通过……格栅被切分，景物以片段形式进入感知”。`wp-garden-design` 的“to screen unattractive structures or views, and to create an element of surprise”为弱补充。
  - 未发现编造年份、人名或引文；实例段「名称：苏州古典园林漏窗……设计者：待核实；年份：待核实」全部置待核实，未伪造具体对象。
  - L2 结构：definition + overview + 六节（原理、典型手法与适用条件、实例、常见错误与限制、一图、待核实），按项目口径七节齐全；1 张 SVG，含“示意图，非施工图”；风险词段含“实际工程须按当地规范和专业设计人员的要求”。
  - 待核实联动：`needs_verification=true`，`pending_notes`「园林漏景具体实例的设计者与年份待补充独立来源」与正文「具体漏窗实例的设计者与年份待核实」一致。
  - 相似度：全库最高 `screened-scenery` 0.484、`opposed-scenery` 0.450、`borrowed-scenery` 0.444，主要为 L2 模板句与「视线经洞口望向园外」SVG 版式重合，原理段措辞不同；未达第4轮 `opposed-scenery` 0.54 的套话警戒线。
- 问题：来源正文未字面出现“leaked scenery / 漏景 / 漏窗”术语（英文页 `Leaked scenery` 为 404），定义靠机制描述支撑而非专条；`wp-garden-design` 仅为泛化补充。未构成事实错误，但建议返工时若有中文园林权威来源，补一条直接论及「漏景／漏窗」的 independent 来源以免长期依赖机制推断。

### 2. `huizhou-style`（徽派建筑）— 不合格

- 依据：
  - 来源 id `wp-chinese-architecture`、`wp-vernacular-architecture` 均存在且 `verified=true`，标题 `Chinese architecture`、`Vernacular architecture`；两页 HTTP 200，H1/title 实抓一致。但两者均非「徽派建筑」专条：前者是宽泛中国建筑综述，后者是 generalizes 的乡土建筑条目。
  - 核心定义事实缺来源支撑：`wp-chinese-architecture` 全文 “Huizhou” 0 次、“white wall” 0 次、“black tile” 0 次；`wp-vernacular-architecture` 全文 “Huizhou” 0 次、“China” 0 次、“Chinese” 仅 1 次。definition「流行于徽州地区、以粉墙黛瓦……为特征」中的“徽州地区”“粉墙黛瓦”在所引两来源中均无直接支撑；“马头墙”仅在 `wp-chinese-architecture` 以一般中国建筑特征出现一次（“matouqiang (horse-head walls), which served as a fire deterrent from drifting embers”），并非徽派标志的直接论述。time_or_place「古代、中国」仅由宽泛来源弱支撑。
  - **存在更直接来源却未引用**：实抓 `https://en.wikipedia.org/wiki/Hui-style_architecture` 得 H1 `Hui Style architecture`、HTTP 200，正文含“prevailed mostly in the historical Huizhou prefecture of Anhui”“black tiles, and white walls”“White Walls and Black Tiles”专节、“Horse-Head Wall”专节、“courtyard type”“patio ... lighting ... drainage”，可逐条覆盖本条 definition/overview/原理/典型手法。该来源不在 `sources.json`（全库 grep `Hui|徽|huizhou` 无命中），属「引用相邻/宽泛页面充当直接来源」——与第4轮 `light-well` 失败模式一致。
  - 未发现编造年份、人名或引文；实例段地点“中国安徽”、设计者“不适用”、年份“待核实”，处理保守。
  - L2 结构齐全，1 张 SVG 含“示意图，非施工图”，风险词段含规范提示；`needs_verification=true`、`pending_notes`「徽州民居具体村落年代与营造者待补充独立来源」与正文一致。
  - 相似度：全库最高 `chinese-architecture-style` 0.407，未见实质内容照搬，问题不在套话而在引用链。
- 问题：真正 unsupported 的是「徽派＝徽州地区＋粉墙黛瓦＋马头墙组合」这一核心定义，而 `pending_notes` 只写村落年代与营造者，未覆盖该来源缺口。判不合格：需新增并核验 `wp-hui-style-architecture`（Hui Style architecture，HTTP 200）为直接来源，替换或补足现有两条宽泛来源，并据原文重写 definition/overview/典型手法后再复核。

### 3. `chinese-architecture-style`（中国传统建筑）— 合格

- 依据：
  - 来源 id `wp-chinese-architecture`、`wp-architectural-style` 均存在且 `verified=true`，标题 `Chinese architecture`、`Architectural style`；两页 HTTP 200，H1/title 实抓一致。前者即本条主题的专条来源，后者为风格史语境来源。
  - 核心事实均由直接来源正文支撑：`wp-chinese-architecture` 原文含“Chinese architecture is characterized by bilateral symmetry, use of enclosed open spaces, feng shui (e.g. directional hierarchies)”（支撑 definition「对称布局与院落组织」、overview「空间等级与礼制秩序」）；“Timber frames are typically constructed with joinery and dowelling”“The bearing structure is a wooden beam”“structural timbers are prominently displayed”（支撑「木构框架」）；“Courtyard (院): Open courtyards are a common feature in many projects ... Siheyuan”“buildings or building complexes surround open spaces”（支撑「院落组织」）；“Vernacular Chinese architecture shows variations related to local terrain and climate”（支撑「因地域材料而呈现多样形态」）。`timber`/`wood`/`symmetr`/`courtyard` 命中分别为 10/26/11/23。原理「荷载传到柱与梁、墙体不承重」与来源「load-bearing walls in non-governmental ... construction」的对照表述相容。
  - 未发现编造年份、人名或引文；实例段「名称：中国传统院落建筑……设计者：不适用；年份：待核实」保守，未伪造具体建筑。
  - L2 结构齐全（definition + overview + 六节），1 张 SVG 含“示意图，非施工图”，风险词段含规范提示。
  - 待核实联动：`needs_verification=true`，`pending_notes`「具体院落实例的建造年代与营造者待补充独立来源」与正文「具体院落实例的建造年代与营造者待核实」一致。
  - 相似度：全库最高 `ancient-greek` 0.370、`vernacular-material` 0.367、`byzantine` 0.364，无高模板重合，未见与来源英文文本大段照搬。
- 问题：无事实性问题。三例中来源质量最高、事实支撑最完整；`设计者：不适用` 用于风格级条目属合理处理，无需返工。

## 总体结论

- 结果：合格 2 条（`leaked-scenery`、`chinese-architecture-style`），不合格 1 条（`huizhou-style`），待核实 0 条。
- 是否建议整批返工：**建议是**。按 `AUTONOMOUS.md` E 节「不合格则整批返工」，`huizhou-style` 1 条不合格已触发条件；本轮抽检 3/6=50%，比例满足要求。实操上建议以「引用链—正文事实—待核实声明」一致性对 6 条全批复核，重点修复 `huizhou-style`（补入并核验 `Hui Style architecture` 直接来源，重写定义与概述后再核）；`leaked-scenery` 保留机制支撑结论，返工时若有条件可补一条直接论及「漏景／漏窗」的来源；`chinese-architecture-style` 保持不动。
- 来源核验：5 个唯一被引用 id 全部存在且 `verified=true`，5/5 来源页 HTTP 200 且 H1/title 与来源库一致。问题集中在「来源本身不直接支撑条目核心事实」，而非来源 id 缺失或伪造——与第4轮结论同类。另确认 `Hui-style architecture`（200，专条）与 `Leaked scenery`（404）的实际存在性，为返工提供可操作目标。
- 结构与一致性：3 条 L2 的七节口径、1 张 SVG/“示意图，非施工图”、风险词规范提示全部通过；3 条 `needs_verification=true` 且 `pending_notes` 非空、正文均有「待核实」节。但 `huizhou-style` 的 pending 未覆盖真正的核心来源缺口，与第4轮 `light-well`/`opposed-scenery` 同一缺陷模式。
- 待核实占比：3/3 均为 `needs_verification=true`，不属于异常低，未见通过压低待核实来硬写的迹象。
- 套话与重合：模板句（“此处仅列名称、地点、设计者与年份信息，不复制图像”“实际工程须按当地规范和专业设计人员的要求”“具体实例的设计者与年份待核实”）在 L2 条目中高度重复；本组造景条目相似度 0.44–0.48，低于第4轮 `opposed-scenery` 0.54 的警戒线，`leaked-scenery` 的「视线经洞口望向园外」SVG 与 `borrowed-scenery` 版式接近但可接受。未见与来源文本大段字面重合。
- 只读声明：本次仅生成 `research/spotcheck-round05.md`，未修改项目其他文件，未修改项目文件夹之外内容，未创建 git commit。
