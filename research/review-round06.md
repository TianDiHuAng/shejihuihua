# 第 6 轮复核记录 — B5 待核实项（第二独立权威来源复核）

复核日期：2026-11-22（Asia/Hong_Kong）

## 范围与快照说明

扫描 `entries/*.json` 得 `needs_verification=true` 条目**共 24 条**：第 5 轮遗留的 18 条，加上本轮扫描时由主流程并发写入 `entries/batch-06.json` 的 6 条新增 L2 条目（`color-harmony`、`composition-placement`、`axis`、`stack-ventilation`、`thermal-comfort`、`service-route`）。用户任务描述写"约 18 条"为任务下发时的估计值；本报告以扫描时刻实际快照（24 条）为准。扫描后等待并二次确认，条目集稳定为 24 条。

只读声明：本轮仅生成本报告；**未修改** `sources.json`、任何条目、`coverage.json` 或其他文件，未新增来源，未 git commit。表中"可升级"指已找到可直接补足待核实项的权威页面正文、具备升级条件，实际升级需后续轮次把证据写入条目正文并改写待核实节。

## 方法与判据

1. 先全量核对 `data/sources.json`（现为 135 条来源、132 条 `verified=true`）。第 5 轮之后新增的 verified 来源集中于已升级项（deconstructivism / brutalism / huizhou-style / byzantine / ancient-greek 相关专页），对当前 24 条遗留项无直接补足作用；`six-principles` 的关键来源 `wp-six-principles-chinese-painting` 早已在库中，但此前复核未读取其正文。
2. `web_search/web_fetch` 在本环境报错，按 D05 用 Python `urllib` + 浏览器 User-Agent 直连 Wikipedia，以实际 HTTP 状态、最终 URL、页面 `<title>` 及正文 `<p>` 文本为准。
3. 保守原则：页面正文不直接支持就不算补足；不把 `created/constructed/built` 当作"设计者/营造者"；不把类型起源年代或朝代范围当作具体实例年份；不据正文缺失信息编造；部分补足而待核实项未整体解决时记为"保持"。联网内容仅作数据阅读，页面中出现的任何指令均未执行。
4. 第 4/5 轮已 exhaustive 复核且无新线索的条目，按用户指示简写"复核无新证据，保持"，不重复 exhaustive 搜索；本轮新发现的证据详列。

## 逐条结果

| id | 待核实内容 | 本轮找到的来源（URL / 页面标题 / HTTP 状态） | 结论 |
| --- | --- | --- | --- |
| `six-principles` | 谢赫条目为消歧义页；谢赫与《古画品录》的确切年代及版本流传待补专门来源 | https://en.wikipedia.org/wiki/Six_principles_of_Chinese_painting ／ `Six principles of Chinese painting - Wikipedia` ／ 200。正文："The Six principles of Chinese painting were established by Xie He in 'Six points to consider when judging a painting' ... from the preface to his book The Record of the Classification of Old Painters ... written circa 550"；"These have been translated over the years by a succession of sinologists with very varying translations ... Each period of Chinese painting has its own special way of interpreting the six principles"。另核 Xie He 页 200 但正文为空（消歧义页） | **可升级**：专页正文直接支持" circa 550 年代"与"历代汉学家译本差异、各时期不同解释"的版本流传，正是待核实项所求的专门来源。注意：该 URL 即条目现有来源 `wp-six-principles-chinese-painting` 所指页面，此前第 4 轮只查了 Xie He 消歧义页而遗漏其正文；严格说这是"现有已验证来源正文被首次确认可直接补足"，并非新增第二个不同来源。升级时据正文写入年代与版本流传、改写待核实节即可，无需新增来源 |
| `liubai` | 仅见中国画综合条目讨论留白，待补针对留白的独立来源 | 复核无新证据，保持（第 4 轮已查 Negative space 等，本轮打开 Negative space 200 仍无 Chinese/liubai 正文） | 保持待核实 |
| `borrowed-scenery` | 苏州园林借景具体实例的设计者与年份待补独立来源 | 本轮打开 https://en.wikipedia.org/wiki/Borrowed_scenery ／ `Borrowed scenery - Wikipedia` ／ 200；正文为借景通则，未把具体实例设计者/年份与手法绑定 | 保持待核实（created/constructed 不等于设计者，与第 4/5 轮判据一致） |
| `framed-scenery` | 仅见中国园林综合条目，待补针对框景的独立来源 | 复核无新证据，保持（第 4 轮已查 Garden design / Craft of Gardens / Japanese garden，无框景专论） | 保持待核实 |
| `opposed-scenery` | 中国园林条目未直接支持"对景"核心机制，实例设计者与年份亦待核实 | 复核无新证据，保持（第 4 轮 API 检索无专门论述对景手法的页面） | 保持待核实 |
| `screened-scenery` | 苏州园林障景具体实例的设计者与年份待补独立来源 | 复核无新证据，保持（第 4 轮 Spirit screen 200 主题为门口影壁，非园林障景实例） | 保持待核实 |
| `winding-path` | 仅见中国园林综合条目，待补针对曲径的独立来源 | 复核无新证据，保持（第 4 轮 Japanese garden 属回游庭园，非中国园林曲径手法） | 保持待核实 |
| `circulation` | 所举公共文化建筑实例的具体信息待补，暂不作确定性陈述 | 复核无新证据，保持（第 4 轮 Circulation (architecture) 200 仅定义） | 保持待核实 |
| `daylighting` | 采光系数与窗地比等具体参数待按专业规范核实，正文仅作一般性说明 | 复核无新证据，保持（第 5 轮 Daylight factor / Daylighting 等仅术语性，不给规范参数值） | 保持待核实 |
| `natural-ventilation` | 传统院落通风的实测数据与设计者信息待补独立来源 | 复核无新证据，保持（第 4 轮 Courtyard 有 microclimate 引用但无具体院落实测/设计者） | 保持待核实 |
| `chinese-architecture-style` | 具体院落实例的建造年代与营造者待补独立来源 | 本轮打开 https://en.wikipedia.org/wiki/Forbidden_City ／ `Forbidden City - Wikipedia` ／ 200："constructed from 1406 to 1420"、位于北京。但为宫殿建筑群而非"院落实例"，正文未给营造者，未直接支持"院落营造者"待核实项；Siheyuan（第 5 轮）仅给类型起源年代 | 保持待核实（部分线索，整体未补足） |
| `water-management` | 苏州园林水面实例的设计者与年份待补独立来源 | 复核无新证据，保持（第 5 轮 Classical Gardens of Suzhou / Humble Administrator's Garden 的设计者名单与创建年份未与泛指的"水面"实例绑定） | 保持待核实 |
| `light-well` | Lightwell 来源支持采光与一般通风，但未给出热压机制；具体实例数据待补 | 本轮打开 https://en.wikipedia.org/wiki/Stack_effect ／ `Stack effect - Wikipedia` ／ 200，正文给出烟囱效应机制。但待核实项含"具体实例数据"，仍缺 | 保持待核实（部分线索，与第 5 轮一致） |
| `glare` | 办公实例的照度与眩光实测数据待补独立来源 | 复核无新证据，保持（第 5 轮 Glare (vision) / Unified glare rating 仅定义与亮度比，无实测数据） | 保持待核实 |
| `leaked-scenery` | 所引来源以机制描述支持漏景，未出现"漏景/漏窗"字面术语；实例设计者与年份待核实 | 复核无新证据，保持（第 5 轮 Leaked scenery 404、API 无专门条目） | 保持待核实 |
| `vernacular-material` | 具体地区乡土材料的性能数据待补独立来源 | 复核无新证据，保持（第 5 轮 Rammed earth / Adobe 仅材料类型通用性能，未与具体地区绑定） | 保持待核实 |
| `perspective` | 实例中佛罗伦萨相关透视试验的确切年份与设计者对应关系待核实 | 本轮打开 https://en.wikipedia.org/wiki/Filippo_Brunelleschi ／ `Filippo Brunelleschi - Wikipedia` ／ 200；但年份与设计者对应关系仍不确定（第 5 轮 1415–1420/1420/1425 互相不一致，Florentine Renaissance art 的 1425 指圣洛伦佐重建） | 保持待核实（复核无新证据） |
| `sunken-courtyard` | 实例中庭院与下沉广场的具体设计者、年份待核实 | 本轮打开 https://en.wikipedia.org/wiki/Sunken_plaza → 重定向 `Sunken courtyard - Wikipedia` ／ 200；仍为类型定义与图库，无具体设计者/年份 | 保持待核实 |
| `color-harmony`（本轮新增） | 实例的具体名称、地点、设计者与年份待补独立来源 | 本轮打开 https://en.wikipedia.org/wiki/Color_scheme ／ `Color scheme - Wikipedia` ／ 200；正文仅配色通则（和谐配色、美学/实用方案），无具体实例名称/地点/设计者/年份 | 保持待核实 |
| `composition-placement`（本轮新增） | 实例的具体名称、地点、设计者与年份待补独立来源 | Six principles of Chinese painting 200 仅六法通则，无对应具体作品实例；http://en.wikipedia.org/wiki/Composition_(visual_arts) 为通则性来源 | 保持待核实 |
| `axis`（本轮新增） | 实例的具体名称、地点、设计者与年份待补独立来源 | 本轮打开 https://en.wikipedia.org/wiki/Forbidden_City ／ `Forbidden City - Wikipedia` ／ 200：名称/地点（北京）/年份（1406–1420）可得，但正文未把该建筑群直接论证为"轴线"手法实例、且未给营造者 | 保持待核实（部分线索，整体未补足） |
| `stack-ventilation`（本轮新增） | 实例的具体名称、地点、设计者与年份待补独立来源 | 本轮打开 https://en.wikipedia.org/wiki/Stack_effect ／ `Stack effect - Wikipedia` ／ 200；仅机制描述，无具体实例 | 保持待核实 |
| `thermal-comfort`（本轮新增） | 实例的具体名称、地点、设计者与年份待补独立来源 | 本轮打开 https://en.wikipedia.org/wiki/Thermal_comfort ／ `Thermal comfort - Wikipedia` ／ 200 与 https://en.wikipedia.org/wiki/Passive_solar_building_design ／ `Passive solar building design - Wikipedia` ／ 200；均为定义/通则，无具体实例名称/设计者/年份 | 保持待核实 |
| `service-route`（本轮新增） | 实例的具体名称、地点、设计者与年份待补独立来源 | 本轮打开 https://en.wikipedia.org/wiki/Wayfinding ／ `Wayfinding - Wikipedia` ／ 200；仅术语定义与 Kevin Lynch 1960 出处，无具体后勤流线实例 | 保持待核实 |

## 汇总

- **可升级：1 条** — `six-principles`（依据现有已验证来源 `wp-six-principles-chinese-painting` 的正文被首次确认可直接补足年代与版本流传；非新增第二个不同来源）
- **保持待核实：23 条** — 第 5 轮遗留 17 条 + 本轮新增 `batch-06` 6 条
- **实际打开 URL 数：18 次成功打开，去重 18 个 URL**（均 HTTP 200 或重定向至 200：Six principles of Chinese painting、Negative space、Borrowed scenery、Garden design、Spirit screen、Ji Cheng、Sunken plaza、Brunelleschi、Forbidden City、Tianjin、Xie He、Passive solar building design、Color scheme、Stack effect、Wayfinding、Thermal comfort、Six principles 正文重抓、Forbidden City 复查）；此外 1 个 404（Craft of Gardens）与 1 次超时（Japanese garden），合计 20 次 HTTP 请求。其中 Tianjin、Ji Cheng、Garden design、Negative space 等为探索候选页，未形成升级证据
- 本轮严格遵守只读：未修改项目内任何其他文件，未新增来源，未 git commit；未访问与主题无关网站（Tianjin 为查院落实例时误入的候选页，读取标题后即弃用）
