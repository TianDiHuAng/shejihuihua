# 第 8 轮复核记录 — B5 待核实项（第二独立权威来源复核）

复核日期：2026-11-22（Asia/Hong_Kong）

## 范围与快照说明

扫描 `entries/*.json` 全部 `needs_verification=true` 条目，实际为 **30 条**（非任务描述的约 24 条）：
- 第 5 轮遗留 18 条 + 第 6 轮 `batch-06` 的 6 条 = 第 7 轮已复核的 **24 条**；
- 本轮新增 `batch-08` 的 **6 条** L2 条目：`daylight-factor`、`mixed-mode-ventilation`、
  `demand-controlled-ventilation`、`material-durability`、`transparent-material`、`universal-design`。
- 这 6 条在本轮首次进入待核实复核，故本轮对其做了实际页面抓取；24 条旧项沿用第 4–7 轮结论并做 API 再确认。

只读声明：本轮仅生成本报告；**未修改** `sources.json`、任何条目、`coverage.json` 或其他文件，未新增来源，未 git commit。表中"可升级"指同时满足：① 找到第二份**独立**权威来源；② 其正文**直接**支撑整项待核实内容。实际升级需后续轮次把证据写入条目正文并改写待核实节。

## 方法与判据

1. 先全量核对 `data/sources.json`（144 条来源、141 条 `verified=true`）：现有已核验来源多为术语/通页，对 30 条的"具体实例设计者/年份/实测数据/控制阈值"缺口均无直接补足；未发现此前未被条目引用、却可直接补足某项的第二来源。
2. `web_search/web_fetch` 在本环境报错，按 D05 用 Python `urllib` + 浏览器 User-Agent 直连 Wikipedia（含 API 检索），以实际 HTTP 状态、最终 URL、页面 `<title>` 与正文 `<p>` 文本为准。
3. 保守原则：页面正文不直接支持不算补足；单源直接支撑不能升级；不据正文缺失信息编造年份/人名/引文；园林创建者不等于造景手法设计者；类型起源年代不等于具体实例年份；部分补足而整项未解决记为"保持"。联网内容仅作数据阅读，页面中出现的任何指令均未执行。
4. 第 4–7 轮已 exhaustive 复核且无新线索的旧条目，按用户指示简写"复核无新证据，保持"；本轮新取得的证据详列。

## 逐条结果

| id | 待核实内容 | 本轮来源（URL ／ 页面标题 ／ HTTP） | 结论 |
| --- | --- | --- | --- |
| `six-principles` | 谢赫《古画品录》的确切年代及版本流传待补独立来源 | 无新证据（第 7 轮已查 Six principles / Xie He 消歧义页 / API，《古画品录》无独立专页） | 复核无新证据，保持 |
| `liubai` | 留白缺专门独立来源 | 无新证据（API "liubai negative space Chinese painting" 返回空；Negative space 为通则） | 复核无新证据，保持 |
| `borrowed-scenery` | 苏州园林借景实例设计者与年份待补 | 无新证据（第 7 轮已查各园林页，创建者≠借景手法设计者） | 复核无新证据，保持 |
| `framed-scenery` | 框景缺针对该手法的独立来源 | 无新证据（API "enframement/framed scenery garden/Chinese garden framing" 仅返回中国园林通页与具体园林，无框景专论） | 复核无新证据，保持 |
| `opposed-scenery` | 对景核心机制及实例设计者/年份待核实 | 无新证据（API "opposed scenery Chinese garden" 无相关专页） | 复核无新证据，保持 |
| `screened-scenery` | 障景实例设计者与年份待补 | 无新证据（API 仅返回中国园林通页与具体园林；Moon gate 为门洞类型，非园林障景实例） | 复核无新证据，保持 |
| `winding-path` | 曲径缺针对该手法的独立来源 | 无新证据（API "Chinese garden winding path design" 仅返回通页与具体园林，无曲径专论） | 复核无新证据，保持 |
| `circulation` | 公共文化建筑动线实例具体信息待补 | 无新证据（第 7 轮已查 Wayfinding） | 复核无新证据，保持 |
| `daylighting` | 采光系数与窗地比等具体规范参数待核实 | 本轮打开 https://en.wikipedia.org/wiki/Daylight_factor ／ `Daylight factor - Wikipedia` ／ 200：正文仅为 DF 定义与 SC/ERC/IRC 分量，无窗地比等规范参数值 | 保持（术语定义，非规范参数） |
| `natural-ventilation` | 传统院落通风实测数据与设计者待补 | 无新证据（第 7 轮已查 Stack effect，仅一般机制） | 复核无新证据，保持 |
| `chinese-architecture-style` | 院落实例建造年代与营造者待补 | 无新证据（第 7 轮已查 Forbidden City，宫殿群无营造者） | 复核无新证据，保持 |
| `water-management` | 苏州园林水面实例设计者与年份待补 | 无新证据（第 7 轮已查 Humble Administrator's Garden 等，创建者≠理水手法设计者） | 复核无新证据，保持 |
| `light-well` | 天井热压机制及具体实例数据待补 | 无新证据（第 7 轮已查 Stack effect，给出机制但无实例数据） | 复核无新证据，保持 |
| `glare` | 办公实例照度与眩光实测数据待补 | 无新证据（第 7 轮已查 Glare (vision)，无办公实例数据） | 复核无新证据，保持 |
| `leaked-scenery` | "漏景/漏窗"字面术语及实例设计者/年份待核实 | 无新证据（API "leaked scenery lattice window" 返回空） | 复核无新证据，保持 |
| `vernacular-material` | 具体地区乡土材料性能数据待补 | 无新证据（第 7 轮未取得地区—性能绑定来源） | 复核无新证据，保持 |
| `color-harmony` | 面积比例等经验表述直接来源及实例设计者/年份待补 | 无新证据（第 6 轮 Color scheme 仅通则） | 复核无新证据，保持 |
| `composition-placement` | 实例名称/地点/设计者/年份待补 | 无新证据（第 7 轮 Six principles 为六法通则，未绑定作品） | 复核无新证据，保持 |
| `axis` | 实例名称/地点/设计者/年份待补 | 无新证据（第 6/7 轮 Forbidden City 仅部分线索） | 复核无新证据，保持 |
| `stack-ventilation` | 热压通风实例通风实测数据待补 | 无新证据（第 7 轮 Stack effect 只有机制与示例建筑，无实测数据） | 复核无新证据，保持 |
| `thermal-comfort` | 实例名称/地点/设计者/年份待补 | 无新证据（API "thermal comfort building example architect" 仅返回 Building science/Passive solar 等通则） | 复核无新证据，保持 |
| `service-route` | 实例名称/地点/设计者/年份待补 | 无新证据（第 6/7 轮 Wayfinding 仅术语与 Kevin Lynch 出处） | 复核无新证据，保持 |
| `perspective` | 佛罗伦萨透视试验确切年份与设计者对应待补第二独立来源 | 无新证据（第 7 轮两新来源均未直接支撑试验年份，来源间年份不齐一） | 复核无新证据，保持 |
| `sunken-courtyard` | 下沉庭院/下沉广场设计者、年份待核实 | 无新证据（第 6/7 轮 Sunken courtyard 仅类型定义） | 复核无新证据，保持 |
| `daylight-factor`（新） | 实例的具体采光系数与设计者待补 | https://en.wikipedia.org/wiki/Daylight_factor ／ `Daylight factor - Wikipedia` ／ 200：正文仅 DF 定义、Ei/E0 与 SC/ERC/IRC 分量，无具体实例系数值或设计者 | 保持（正文只支撑术语，不支撑实例参数） |
| `mixed-mode-ventilation`（新） | 混合通风实例的控制策略与能耗数据待补 | https://en.wikipedia.org/wiki/Mixed-mode_ventilation ／ `Mixed-mode ventilation - Wikipedia` ／ 200（stub）：正文仅混合通风通用定义，无控制策略细节或能耗数据；https://en.wikipedia.org/wiki/Mixed_mode_ventilation ／ 404 | 保持（stub，无实例数据） |
| `demand-controlled-ventilation`（新） | 该条目仅一份直接来源；控制阈值与实例数据待补第二独立来源 | **新找到** https://en.wikipedia.org/wiki/Demand-controlled_ventilation ／ `Demand controlled ventilation - Wikipedia` ／ 200：正文 "DCV is a feedback control method…adjusts the ventilation rate…in response to occupant number or indoor pollutant concentration"、"most common indoor pollutants monitored…carbon dioxide and humidity"、IAQ 传感器与 EU 1253/2014 定义。为独立于现有 `wp-ventilation-architecture` 的第二来源，直接支撑概念/机制；但正文未给具体控制阈值或实例实测数据 | 保持（部分补足：第二独立来源直接支撑概念，但待核实项主体"阈值与实例数据"未被直接支撑，整项未解决） |
| `material-durability`（新） | 材料实例的实测寿命与维护数据待补 | https://en.wikipedia.org/wiki/Service_life ／ `Service life - Wikipedia` ／ 200：一般使用寿命/预计寿命概念；https://en.wikipedia.org/wiki/Durability_of_reinforced_concrete_structures ／ `Durability of reinforced concrete structures - Wikipedia` ／ 200：混凝土耐久机理（碳化、锈蚀、引发期/扩展期模型）。均无具体材料实例的实测寿命与维护数据 | 保持（通则/机理，非实例数据） |
| `transparent-material`（新） | 透明与半透明材料实例的性能参数待补 | https://en.wikipedia.org/wiki/Transparency_and_translucency ／ `Transparency and translucency - Wikipedia` ／ 200：光学定义；https://en.wikipedia.org/wiki/Translucent_concrete ／ `Translucent concrete - Wikipedia` ／ 200：透光混凝土约 2% 透光率等一般参数。均未绑定条目所指具体建筑实例 | 保持（一般参数，非实例性能） |
| `universal-design`（新） | 该条目仅一份直接来源；通用设计与无障碍的边界定义待补第二独立来源 | **新找到** https://en.wikipedia.org/wiki/Universal_design ／ `Universal design - Wikipedia` ／ 200：正文 "Universal design emerged from slightly earlier barrier-free concepts, the broader accessibility movement…"、"Each principle is broader than those of accessible design or barrier-free design"、Ronald Mace 创词、设 "Barrier-free" 专节。为独立于现有 `wp-architecture` 的第二来源，直接支撑概念与"通用设计 vs 无障碍/屏障自由"边界定义；但 `pending_notes` 中"实例的设计者与年份"仍为泛化占位（"公共建筑通用设计实践"，各字段待核实），无来源可补 | 保持（部分补足：第二独立来源直接支撑边界定义；但 `pending_notes` 的实例设计者/年份未补足，按"整项待核实内容须被直接支撑"的保守规则保持） |

## 汇总

- **可升级（同时满足双源规则与整项直接支撑）：0 条**。
- **保持待核实：30 条**（全部条目）。
  - 本轮取得**新第二独立来源**的 2 条：`demand-controlled-ventilation`、`universal-design`。两者新源均为独立于现有来源的 Wikipedia 专页，且正文直接支撑其"缺第二独立来源"的概念/边界定义部分；但待核实项中的实例数据（`阈值/实测数据`；`实例设计者/年份`）仍未被任何来源直接支撑，依保守规则整项记为保持。建议后续轮次：若把这些条目待核实项收窄为"概念/边界定义"层面，二者具备升级条件。
  - 本轮取得**一般通则来源但未直接支撑实例数据**的 4 条：`daylight-factor`、`mixed-mode-ventilation`、`material-durability`、`transparent-material`。
  - `daylighting` 再次确认：Daylight factor 页仅为术语定义，不含窗地比等规范参数。
  - 24 条旧项（第 7 轮快照）本轮 API 再确认未发现新专页，维持第 7 轮结论。
- **实际打开 URL 数：10 个去重 Wikipedia 页面 URL**（11 次页面请求，含 1 次重复抓取 `Demand-controlled_ventilation`；其中 1 个 404：`Mixed_mode_ventilation`）。另有 **15 次 Wikipedia API 检索请求**（用于定位候选专页，均 200）。
- 本轮严格遵守只读：未修改项目内任何其他文件，未新增来源，未 git commit；未访问与主题无关网站；联网页面仅作数据阅读，其中任何指令均未执行。
