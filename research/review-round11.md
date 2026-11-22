# 第 11 轮 B5 待核实复核记录

复核日期：2026-11-22（Asia/Hong_Kong）

## 一、执行说明

- 已读取 `AUTONOMOUS.md`（实际位于 `D:/Users/Administrator/Desktop/`）、`TASK_design.md`（同目录）、`DECISIONS.md`、`research/review-round10.md`、`research/review-round09.md`，并按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。
- `entries/*.json` 共 13 个文件；当前 `needs_verification=true` 实际为 **37 条**（与任务“约 37 条”一致）。较第 9 轮的 34 条：新增 `chiaroscuro`、`gothic`、`renaissance-style`、`modernism`、`bauhaus`、`postmodernism` 6 条风格/理论条目，且 `parametric-architecture`、`place-spirit`、`spatial-perception` 已不在待核实列。
- **网络环境（本轮关键约束）**：`en.wikipedia.org` 直连被 DNS 投毒（解析到 `2001::1`、`31.13.94.41` 等，属 Facebook IP 段）；以 `urllib` + 浏览器 UA 对其 summary/raw 共发出 10 次请求全部连接超时（错误 10060），`simple/zh/en.m.wikipedia` 亦全部 000。`web_search` 工具可用；`web_fetch` 工具 `fetch failed`。因此改用 **Wikipedia 全文镜像 `everything.explained.today`（HTTP 200）** 读取对应词条正文（该站页脚自述 “It uses material from the Wikipedia article …”，属维基同源镜像，**不作为“第二独立来源”**）。`whc.unesco.org`、`britannica.com`、`moma.org`、`archpaper.com` 等权威站返回 403；`dbpedia.org`、`grokipedia` 可及但为维基衍生/AI 生成，均不采用。
- 严格只读：本轮仅生成本报告；**未修改** `sources.json`、任何条目、`coverage.json` 或其他文件，未 git commit，未变更项目外内容。联网内容一律按“数据”处理，页面中任何指令均未执行。

## 二、方法与判据

1. 用 Python `urllib` + 浏览器 User-Agent（或镜像站 HTML）实际打开候选页面，记录最终 URL、页面标题、HTTP 状态与正文关键句。
2. 保守原则：**单源直接支撑不升级；正文只给类型/机制/综合性描述、未直接支撑待核实项中“具体实例设计者/年份/实测数据”的，不算补足；维基同源镜像不计为独立第二来源；缺第二独立来源或实例数据即不升级；不编造年份、人名、引文。**
3. 重点复核任务指定的 `sunken-courtyard`、`light-well` 两条；其余条目若历轮已反复复核且无新线索，简写“无新证据，保持”。

## 三、重点复核（2 条）

### 3.1 `sunken-courtyard`（下沉庭院）—— 保持

- **待核实内容**：实例中“苏州古典园林庭院”与“当代城市下沉广场”的具体设计者、年份待核实，待补充独立来源。
- **实际打开的来源**：

| 来源 URL | 页面标题 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://everything.explained.today/Rockefeller_Center/` | Rockefeller Center — Everything Explained.Today（Wikipedia 镜像） | 200 | “The 14 original Art Deco buildings … split by a large **sunken square** and a private street called Rockefeller Plaza.” / “the principal architect and leader of the Associated Architects was **Raymond Hood**” / “Construction … started in 1931, and the first buildings opened in 1933. The core of the complex was completed by 1939.” / “In **1936**, an ice skating rink replaced the unprofitable retail space on **the lower plaza, below ground level**.” |
| `https://everything.explained.today/Sunken_plaza/`（302 跳转）→ `…/Sunken_courtyard/` | Sunken courtyard — Everything Explained.Today（Wikipedia 镜像） | 302→200 | “a sunken courtyard, sometimes called a sunken plaza, is a courtyard below ground level.”（与现有 `wp-sunken-courtyard` 同页 stub，非独立来源） |
| `https://mooc1.chaoxing.com/mooc-ans/ztnodedetailcontroller/visitnodedetail?courseId=216136382&knowledgeId=388898290` | 超星慕课·园林实例节点页 | 200 | 该节点实为“园林/公园实例清单”（沧浪亭 969 年、狮子林 1342 年、寄畅园 1506—1521 年、拙政园 1509 年、留园 1593 年……），检索标题虽含“洛克菲勒中心广场(1936年)”，但**正文未给下沉广场的设计者**，不予采用。 |

- **结论：保持。** Rockefeller Center 页把“sunken square / recessed central plaza”作为**综合体组成部分**描述，给出的是**综合体主建筑师 Raymond Hood（Associated Architects）**与**建造年代 1931–1939（1939 完成）、1936 年地下层零售改为冰场**；**未给出“下沉广场本身”独立的设计者与年份**，属“页面正文不直接支撑待核实项”。且该页为维基同源镜像，`Sunken_plaza` 又落回同一 `Sunken courtyard` stub，**均不构成第二独立权威来源**。故不升级。

### 3.2 `light-well`（天井）—— 保持

- **待核实内容**：Lightwell 来源支持采光与一般通风，但未给出热压机制；具体实例（实测）数据待补充。
- **实际打开的来源**：

| 来源 URL | 页面标题 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://everything.explained.today/Stack_effect/` | Stack effect — Everything Explained.Today（Wikipedia 镜像） | 200 | “**Buoyancy** occurs due to a difference in indoor-to-outdoor **air density** resulting from **temperature** and moisture differences … The greater the **thermal difference and the height** of the structure, the greater the buoyancy force, and thus the stack effect.” / “The stack effect can be useful to **drive natural ventilation**…” / “Usefulness in passive cooling … openings at different heights … cool air enters low, warm air escapes through higher-level openings…” |
| `https://everything.explained.today/Lightwell/` | Lightwell — Everything Explained.Today（Wikipedia 镜像） | 200 | “a lightwell, sky-well, or air shaft is an unroofed or roofed external space … to allow **light and air** to reach … dark or unventilated areas.”（**通篇未出现 stack / thermal / buoyancy 字样**，仅“采光与空气”、罗马 impluvium/compluvium、See also：Atrium/Clerestory/Skylight/Ventilation shaft 等） |
| `https://everything.explained.today/Passive_cooling/` | Passive cooling — Everything Explained.Today（Wikipedia 镜像） | 200 | 被动降温策略（通风、夜间冲洗、蒸发冷却、热质量等），仍未给“天井”实例的实测通风数据。 |

- **结论：保持。** `Stack effect` 页**能补足“热压/烟囱效应”的机制说明**（浮力源于室内外空气密度差、温差与高度越大浮力越强、可驱动自然通风）——但这只是**概念/机制层面**，且该页与条目现有 `wp-*` 同为维基同源，**不构成独立第二来源**；`Lightwell` 页**本身不涉及热压机制**，恰好印证原待核实表述；**任何页面都未给“天井/天窗井”具体实例的实测数据**。按“正文不直接支撑/缺实例数据即不升级”，保持。建议主流程将本条的待核实收窄为“实例实测数据待补”（机制层面可引 `Stack effect` 佐证），下轮补源后再升级。

## 四、其余条目（抽查说明 + 逐条结论）

### 4.1 风格/理论类抽查（本轮新增待核实项）

对 `chiaroscuro`、`gothic`、`renaissance-style`、`modernism`、`bauhaus`、`postmodernism` 6 条，其“实例”字段均为**类型性描述**（设计者/年份标“不适用”），待核实均为“具体作品的设计者与年代待补充独立来源”。本轮 `web_search` 抽查：

- **`bauhaus` —— 候选线索（未升级，保持）**：检索到 Dessau 包豪斯校舍（Bauhaus Dessau）线索。已实际打开并读到正文：`https://bauhaus-dessau.de/en/venues/bauhaus-building/`（包豪斯德绍基金会官方站，**HTTP 200**）——“the planning and realisation of the new building was undertaken by **Walter Gropius'** private office … On **4 December 1926** … the building was opened.”；`http://www.bauhausmuseum.com/history/dessau-building.php`（**HTTP 200**）——“The Bauhaus Dessau was constructed in **1925/26** designed by **Walter Gropius**…”；`https://www.archdaily.com/87728/ad-classics-dessau-bauhaus-walter-gropius`（**HTTP 200**，标题标注 Dessau Bauhaus / Walter Gropius，但正文为 JS 渲染，未取到年份句）。**但**：UNESCO `whc.unesco.org`、Britannica、MoMA 均 **403**，无法取得第二个**独立且权威**来源；`bauhausmuseum.com` 文本疑与维基同源、独立性不能确证。按“缺第二独立来源不升级”→ **保持**，建议下轮纳入官方站并复核第二独立源后再升级。
- 其余 `chiaroscuro`/`gothic`/`renaissance-style`/`modernism`/`postmodernism`：`web_search` 仅见聚合站（百度/搜狗百科）或标题级线索（如科隆大教堂 1248、Dessau 校舍等），未取得“两独立权威来源 + 正文直接支撑”的证据；保持。

### 4.2 逐条结论表（35 条非重点项）

| id | 待核实内容（简） | 结论 |
| --- | --- | --- |
| `chiaroscuro` | 具体作品的设计者与年代待核实 | 无新证据，保持 |
| `six-principles` | 谢赫条目为消歧义页；年代与版本流传待补专门研究来源 | 无新证据，保持 |
| `liubai` | 待补针对留白的独立来源 | 无新证据，保持 |
| `borrowed-scenery` | 苏州园林借景实例的设计者与年份待补 | 无新证据，保持 |
| `framed-scenery` | 待补针对框景的独立来源 | 无新证据，保持 |
| `opposed-scenery` | 未直接支撑“对景”核心机制；实例设计者/年份待核实 | 无新证据，保持 |
| `screened-scenery` | 苏州园林障景实例的设计者与年份待补 | 无新证据，保持 |
| `winding-path` | 待补针对曲径的独立来源 | 无新证据，保持 |
| `circulation` | 公共文化建筑实例具体信息待补 | 无新证据，保持 |
| `daylighting` | 采光系数与窗地比等参数待按专业规范核实 | 无新证据，保持 |
| `natural-ventilation` | 传统院落通风实测数据与设计者待补 | 无新证据，保持 |
| `gothic` | 具体教堂的设计者与年代待核实 | 无新证据，保持 |
| `renaissance-style` | 具体建筑的设计者与年代待核实 | 无新证据，保持 |
| `modernism` | 具体建筑的设计者与年代待核实 | 无新证据，保持 |
| `bauhaus` | 具体作品的设计者与年代待核实 | 候选线索（见 4.1），暂保持 |
| `postmodernism` | 具体建筑的设计者与年代待核实 | 无新证据，保持 |
| `chinese-architecture-style` | 具体院落实例的建造年代与营造者待补 | 无新证据，保持 |
| `water-management` | 苏州园林水面实例的设计者与年份待补 | 无新证据，保持 |
| `glare` | 办公实例的照度与眩光实测数据待补 | 无新证据，保持 |
| `leaked-scenery` | 未出现“漏景/漏窗”字面术语；实例设计者/年份待核实 | 无新证据，保持 |
| `vernacular-material` | 具体地区乡土材料性能数据待补 | 无新证据，保持 |
| `color-harmony` | 面积比例等经验性表述待补直接来源；实例设计者/年份待核实 | 无新证据，保持 |
| `composition-placement` | 实例名称/地点/设计者/年份待补 | 无新证据，保持 |
| `axis` | 实例名称/地点/设计者/年份待补 | 无新证据，保持 |
| `stack-ventilation` | 热压通风实例的通风实测数据待补 | 无新证据，保持 |
| `thermal-comfort` | 实例名称/地点/设计者/年份待补 | 无新证据，保持 |
| `service-route` | 实例名称/地点/设计者/年份待补 | 无新证据，保持 |
| `daylight-factor` | 实例参数与设计者、均布阴天假设解释待补专门来源 | 无新证据，保持 |
| `mixed-mode-ventilation` | 混合通风实例控制策略与能耗数据待补 | 无新证据，保持 |
| `material-durability` | 实例寿命与维护数据、退化机制通用列表待补 | 无新证据，保持 |
| `transparent-material` | 透明/半透明材料实例性能参数待补 | 无新证据，保持 |
| `functional-zoning` | 核心概念术语与实例数据均待补独立来源 | 无新证据，保持 |
| `gray-space` | 檐下与廊道实例的设计者与年代待补 | 无新证据，保持 |
| `enclosure` | 具体院落的设计者与年代待补 | 无新证据，保持 |
| `perspective` | 佛罗伦萨透视试验确切年份与设计者对应关系待补第二独立来源 | 无新证据，保持 |

## 五、本轮实际打开的 URL 清单（可核对）

| # | URL | 标题 | HTTP |
| --- | --- | --- | --- |
| 1 | `https://everything.explained.today/Rockefeller_Center/` | Rockefeller Center（维基镜像） | 200 |
| 2 | `https://everything.explained.today/Stack_effect/` | Stack effect（维基镜像） | 200 |
| 3 | `https://everything.explained.today/Lightwell/` | Lightwell（维基镜像） | 200 |
| 4 | `https://everything.explained.today/Sunken_plaza/` → `…/Sunken_courtyard/` | Sunken courtyard（维基镜像） | 302→200 |
| 5 | `https://everything.explained.today/Lower_Plaza/` → `…/Rockefeller_Center/#Lower_Plaza` | Rockefeller Center：#Lower Plaza（维基镜像） | 200 |
| 6 | `https://everything.explained.today/Passive_cooling/` | Passive cooling（维基镜像） | 200 |
| 7 | `https://mooc1.chaoxing.com/mooc-ans/ztnodedetailcontroller/visitnodedetail?courseId=216136382&knowledgeId=388898290` | 超星慕课·园林实例节点页 | 200 |
| 8 | `https://www.archdaily.com/87728/ad-classics-dessau-bauhaus-walter-gropius` | AD Classics: Dessau Bauhaus / Walter Gropius | 200 |
| 9 | `https://bauhaus-dessau.de/en/venues/bauhaus-building/` | Bauhaus Building — Bauhaus Dessau Foundation | 200 |
| 10 | `http://www.bauhausmuseum.com/history/dessau-building.php` | The Bauhaus Dessau was constructed in 1925/26 | 200 |

> 另：对 `en.wikipedia.org` 直连 10 次请求全部超时（DNS 投毒，无响应）；`simple/zh/en.m.wikipedia` 000；`whc.unesco.org`、`britannica.com`、`moma.org`、`archpaper.com` 403；`dome.mit.edu` 404；`dbpedia.org`/`grokipedia` 200（维基衍生/AI 生成，不采用）。

## 六、汇总

- **可升级：0 条**（无任一条同时满足“第二独立权威来源 + 正文直接支撑待核实项全部缺口”）。
- **保持待核实：37 条**（当前快照全部条目）。
  - 其中 **2 条重点项**已实际核对：`sunken-courtyard`（Rockefeller Center 页给出综合体建筑师 Raymond Hood 与 1931–1939 年代、1936 冰场，但未给“下沉广场本身”的设计者/年份，且镜像同源 → 保持）、`light-well`（`Stack effect` 可补热压机制概念、`Lightwell` 页不涉及热压、均无实例实测数据 → 保持）。
  - 其中 **1 条候选（未升级）**：`bauhaus`——Dessau 校舍 / Walter Gropius / 1925–26，官方站 200 正文确认，但第二独立权威源 403、镜像同源，按保守原则暂保持，建议下轮补源后升级。
  - 其余 **34 条**：无新证据，保持（沿用第 4–10 轮结论）。
- **实际打开 URL 数：10 个去重 URL（12 次正文请求，含 2 次重定向与 1 次重复打开 Rockefeller Center）；另有对 Wikipedia 直连 10 次全部超时、多个候选权威源 403/404 的可达性探测。**

保守原则声明：未核验的线索（如 `bauhaus` 第二独立源）不作为升级依据，不为凑数硬写年份或人名；维基同源镜像不计为独立第二来源。
