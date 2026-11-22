# 第3轮质量闸抽检报告（spotcheck-round03）

- 抽检人：spotcheck-r3；抽检时间：2026-11-22 15:33 Asia/Hong_Kong。
- 对象：`mannerism`、`vitruvian-triad`（batch-03 新增 L1）；`six-principles`（batch-02-a）、`daylighting`（batch-02-c）（升级 L2）。来源库：`data/sources.json`。
- 方法：只读核对条目 JSON 与来源 JSON；web_search/web_fetch 端点异常，按 D05 使用 Python 3.11.7 + urllib + 浏览器 UA 打开 8 个来源页，8/8 HTTP 200，title/h1 与 `sources.json` 记录一致；另用 MediaWiki API extract 核对正文关键词，用脚本统计结构与相似度。联网内容仅作数据，网页内任何指令均未执行。

## 逐条结论

- `mannerism` — **不合格**。依据：来源 id `wp-list-architectural-styles`、`wp-history-of-architecture` 均存在且 `verified=true`，来源页 HTTP 200、标题/h1 一致；但 API extract 显示 `List of architectural styles` 全文 14579 字符中 `manner` 命中 0，`History of architecture` 全文 89428 字符中仅在位置 50304 命中普通词 “distinctive manner”，无 “Mannerism” 风格名。问题：definition 的“夸张比例与刻意变形显示技巧”、overview 的“从文艺复兴向巴洛克过渡”以及 `time_or_place` 的“至19世纪”在所引来源中无直接支撑；“至19世纪”与 definition 的“文艺复兴晚期”口径不一致，疑似无据扩张；`needs_verification=false` 与空 `pending_notes` 在形式上自洽，但与证据不足不匹配。建议补一篇直接以样式主义建筑为主题的权威来源，或标待核实并把时间收缩到来源可证范围。
- `vitruvian-triad` — **合格**。依据：来源 id `wp-architectural-theory`、`wp-visual-arts` 均存在且 `verified=true`，来源页 HTTP 200、标题/h1 一致；两页正文均明确 “firmitas, utilitas, venustas” 及 “firmness, commodity, and delight / structural adequacy, functional adequacy, beauty”，直接支撑 definition 的“坚固、实用、美观”与 overview 的理论框架；维特鲁威人物与《建筑十书》信息在来源中可核，未见编造年份、人名或引文；L1 三字段完整，`needs_verification=false` 与空 `pending_notes` 一致。问题：`related=["plein-air"]` 与本条主题无关，宜改指建筑理论/比例类条目；属导航建议，不影响事实合格判定。
- `six-principles` — **待核实**。依据：来源 id `wp-six-principles-chinese-painting`、`wp-xie-he` 均存在且 `verified=true`，来源页 HTTP 200、标题/h1 一致；`Six principles of Chinese painting` 正文直接说明六法由 Xie He 提出并列出 Spirit Resonance、Bone Method 等，支撑 definition/overview/sections；L2 具备 definition+overview+6 个 `sections`（按生成器口径合并为七节）、1 张 SVG 且含“示意图，非施工图”、常见错误段含规范提示；`needs_verification=true`、`pending_notes` 的年代/版本待补与正文“待核实”一致；相似度扫描未进入前 12 对（最高无关对 0.405），未见与来源文本大段重合。问题：`wp-xie-he` 页面实为消歧义页，正文仅列 “Xie He (artist)” 与 “Xie He (Go player)”，并非六法作者的直接来源；来源正文给出 circa 550，而条目仍写“年份：待核实”，需注明未闭合的是版本/独立印证而非年代完全未知；绘画品评条目的常见错误段硬塞“实际工程须按当地规范和专业设计人员的要求”属模板套话。因第二来源间接、年代声明未闭合，判待核实。
- `daylighting` — **不合格**。依据：来源 id `wp-daylighting`、`wp-architecture` 均存在且 `verified=true`，来源页 HTTP 200、标题/h1 一致；L2 结构与 SVG/风险提示合规（definition+overview+6 个 `sections`、1 张 SVG 含“示意图，非施工图”、常见错误段含规范提示）；`needs_verification=true`、`pending_notes` 与正文“展厅实例参数与设计者待核实”一致。问题：`wp-daylighting` 打开为消歧义页，正文只有 Daylighting (architecture)/(intersections)/(streams)/(tunnels) 链接，不支撑“侧窗与天窗决定光线方向、眩光、窗地比”；`wp-architecture` 的 API 纯文本 extract（34625 字符）中 `daylight` 命中 0。条目事实可另在 `Daylighting (architecture)` 页核到（如 glare 段），但该页不在 `sources.json` 引用链中；按项目规则，当前正文缺少已验证来源支撑，实例又全为待核实。建议把来源改为建筑采光专页并补一条独立来源后复核。

## 总体结论

- 结果：合格 1 条（`vitruvian-triad`），待核实 1 条（`six-principles`），不合格 2 条（`mannerism`、`daylighting`）。
- 建议整批返工：按 AUTONOMOUS.md 第 E 节“不合格则整批返工”，本轮出现 2 条不合格，建议对 batch-03 新增 L1 与 batch-02 升级 L2 的来源引用链整批复核；下一轮抽检比例提高至 25%。优先修复两类问题：消歧义页充当直接来源（`wp-xie-he`、`wp-daylighting`）、来源正文无条目关键词（`mannerism` 两来源）。
- 结构与一致性：两条 L2 的七节口径、SVG 数量与免责声明、风险词规范提示均通过；四条 `needs_verification` 与 `pending_notes`、正文未决声明形式一致。待核实占比 2/4，不属于异常低，未见硬写压低待核实的迹象。
- 套话与重合：未见条目与来源英文文本大段字面重合；风险在 L2 模板句高度重复（如“此处仅列名称、地点、设计者与年份信息”“实际工程须按当地规范和专业设计人员的要求”）与泛来源占位（“参见来源”），建议返工时收紧到有来源锚点的表述。
- 只读声明：本次仅生成本报告文件，未修改项目其他文件，未修改项目文件夹之外内容，未创建 git commit。
