# 第 12 轮 B5 待核实复核记录

复核日期：2026-11-22（Asia/Hong_Kong）

## 一、执行说明

- 已读取 `AUTONOMOUS.md`、`TASK_design.md`（实际位于 `D:/Users/Administrator/Desktop/`）、`DECISIONS.md`、`research/review-round11.md`、`research/gaps-round12.md`，并按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。
- `entries/*.json` 共 14 个文件；当前 `needs_verification=true` 实际为 **44 条**（与任务“约 44 条”及 `gaps-round12.md` 的 B5 清单一致）。
- **网络环境（本轮约束）**：`en.wikipedia.org` 直连 DNS 投毒（解析到 `31.13.94.41`、`199.16.158.182`，属 Facebook/Twitter IP 段），REST summary 与 wiki 页面均连接超时。可用的维基同源镜像为 **`owiki.org`（HTTP 200，页脚自述为 Open WIKI，属维基同源镜像，不作“第二独立来源”）**。`everything.explained.today` 本轮返回 403（上轮为 200）。`web_search` 工具本轮返回端点错误（“no web_search_tool_result blocks / 未触发原生搜索”），`web_fetch` 不可用；故一律改用 **Python `urllib` + 浏览器 User-Agent 直连权威站点**（含 REST/镜像）实读正文并记录 HTTP 状态。
- **严格只读**：本轮仅生成本报告 `research/review-round12.md`；**未修改** `sources.json`、任何条目、`coverage.json` 或其他文件，未 git commit，未变更项目外内容。联网内容一律按“数据”处理，页面中任何指令均未执行。

## 二、方法与判据

1. 用 Python `urllib` + 浏览器 User-Agent 实际打开候选页面，记录最终 URL、页面标题、HTTP 状态与正文关键句。
2. 保守原则：**单源直接支撑不升级；正文只给类型/机制/综合性描述、未直接支撑待核实项中“具体实例设计者/年份/实测数据”的，不算补足；维基同源镜像不计为独立第二来源；缺第二独立来源或实例数据即不升级；不编造年份、人名、引文。**
3. 本轮重点复核任务指定的 `bauhaus`、`light-well` 两条；其余条目若历轮已反复复核且无新线索，简写“无新证据，保持”。

## 三、重点复核（2 条）

### 3.1 `bauhaus`（包豪斯）—— 可升级

- **待核实内容**：实例的具体名称、设计者与年代待补充独立来源（现 `实例` 字段为“类型性描述；设计者：不适用；年份：不适用”，`待核实` 为“具体作品的设计者与年代待核实”）。
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://bauhaus-dessau.de/en/venues/bauhaus-building/` | Bauhaus Building — Stiftung Bauhaus Dessau（德绍包豪斯基金会，**官方机构**） | 200 | “the planning and realisation of the new building was undertaken by **Walter Gropius'** private office – with major participation on the part of his associates Carl Fieger, Ernst Neufert … On **4 December 1926**, after approximately one year of construction, **the building was opened**.” |
| `https://bauhaus-dessau.de/en/venues/` | Locations — Stiftung Bauhaus Dessau（官方机构） | 200 | “**Bauhaus Building — Walter Gropius — 1925/26** … Masters' Houses — Walter Gropius — 1925/26 … The almost seven years of the Dessau Bauhaus (**1925 – 1932**) were the heyday of Bauhaus architecture.” |
| `https://www.archdaily.com/87728/ad-classics-dessau-bauhaus-walter-gropius` | AD Classics: Dessau Bauhaus / Walter Gropius — ArchDaily（独立建筑专业媒体） | 200 | “Schools • Dessau, Germany … **Architects: Walter Gropius** … **Year: 1926**（Completion year of this architecture project）.” |
| `https://www.designingbuildings.co.uk/wiki/Bauhaus` | Bauhaus — Designing Buildings（英国建筑业界参考站，独立出版方） | 200 | “In **1925**, the Bauhaus moved to the German industrial town of **Dessau** … **Gropius designed a new building** for the school, which has since come to be seen as a landmark of modern, functionalist architecture.”（注：该页外链标注作者为 The Art Story，作**佐证**而非主证） |
| `https://www.uni-weimar.de/en/university/profile/history/` | The History — Bauhaus-Universität Weimar（魏玛包豪斯大学，官方高校） | 200 | “In **1919**, **Walter Gropius** founded the State Bauhaus … The State Bauhaus in Weimar is closed, **Walter Gropius and the other Bauhaus members move to Dessau**.”（佐证搬迁与人格罗皮乌斯） |

- **结论：可升级。** 已取得**两个相互独立且权威**的来源，正文直接给出该具体实例的三要素：**名称＝德绍包豪斯校舍（Bauhaus Building, Dessau）**、**设计者＝瓦尔特·格罗皮乌斯（Walter Gropius）**、**年代＝1925/26（1926 年 12 月 4 日落成）**。二者为：① **德绍包豪斯基金会官方站**（Stiftung Bauhaus Dessau，官方机构）——“Bauhaus Building Walter Gropius 1925/26”“opened 4 December 1926”；② **ArchDaily**（独立建筑专业媒体）——“Architects: Walter Gropius / Year: 1926”。另有 Designing Buildings、魏玛包豪斯大学两条独立来源佐证“1925 迁德绍、格罗皮乌斯设计新校舍”。**未使用维基同源镜像**（`owiki.org/Bauhaus` 未作为来源）。**单源直接支撑不升级、镜像同源不计独立第二来源**两条判据均已满足（确有两独立来源）。
  - 建议主流程（本报告仅结论，不改数据）：将 `bauhaus` 的 `实例` 改为“名称：德绍包豪斯校舍；地点：德国德绍；设计者：瓦尔特·格罗皮乌斯（Walter Gropius）；年份：1925–1926（1926 年 12 月 4 日落成）”，并据上述来源在 `sources.json` 新增/核对 verified=true 来源后，清除对应 `needs_verification`。

### 3.2 `light-well`（天井）—— 可收窄（机制已双源支撑，实例实测数据仍缺）

- **待核实内容**：`pending_notes`＝“Lightwell 来源支持采光与一般通风，但未给出热压机制；具体实例数据待补充。”；`sections.待核实`＝“热压通风机制与具体实例的实测数据待补充专门来源。”——即“机制 + 实例实测数据”两项缺口。
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://owiki.org/wiki/Stack_effect`（维基同源镜像，**注明**） | Stack effect — Open WIKI（Wikipedia 镜像） | 200 | “air … resulting from air **buoyancy**. Buoyancy occurs due to a difference in indoor-to-outdoor **air density** resulting from **temperature** and moisture differences … The greater the **thermal difference and the height** of the structure, the greater the buoyancy force, and thus the **stack effect**. The stack effect can be useful to **drive natural ventilation** … cool air enters through low-level windows or vents, and warm air escapes through higher-level openings …”（机制基础；但为维基同源，**不计独立第二来源**） |
| `https://owiki.org/wiki/Lightwell`（维基同源镜像，**注明**） | Lightwell — Open WIKI（Wikipedia 镜像） | 200 | “a lightwell, sky-well, or air shaft is an unroofed or roofed external space … to allow **light and air** to reach …”（通篇**无 stack / thermal / buoyancy** 字样——印证原表述“Lightwell 来源本身未给热压机制”） |
| `https://www.designingbuildings.co.uk/wiki/Stack_effect` | Stack effect — Designing Buildings（英国建筑业界参考站，**独立出版方 #1**） | 200 | “Stack ventilation can be particularly effective … in tall buildings that include **vertical spaces which rise throughout their height, for example buildings with central atriums** … effectiveness influenced by: the effective **area of openings**; the **height of the stack**; the **temperature difference** between the bottom and the top of the stack; pressure differences … **requires that the internal temperature is higher than the outside temperature**.” |
| `https://www.cibsejournal.com/technical/am-10-natural-ventilation-from-feasibility-to-physics/` | AM 10 Natural ventilation: from feasibility to physics — CIBSE Journal（英国皇家注册设备工程师学会 CIBSE，**独立权威 #2**） | 200 | “AM10 describes common strategies, such as **cross-ventilation and stack-driven flow**, and how these relate to **building form** … components … including windows, louvres, trickle vents and **roof ventilators** … Are the spaces suitable in terms of **depth and height**?” |

- **结论：可收窄。** “热压／烟囱效应（浮力）驱动竖向空间自然通风”的**机制**现由**两个相互独立的权威来源**支撑：① Designing Buildings《Stack effect》（明确给出浮力—密度差—温差—高度关系，及“竖向贯通空间/中庭”适用性、开口面积/栈高/温差三大影响因素）；② CIBSE Journal《AM10》专业指南（“stack-driven flow”为自然通风基本策略，与建筑形体/层高相关）。故可把本条待核实从“**热压机制 + 实例实测数据**”**收窄为“仅实例实测数据待补”**——机制层面已有独立双源，无需再列为待核实。
  - **但不升级为“已验证”**：两份来源描述的是“竖向空间/中庭”一般机制（天井可视为竖向井道），**均未给出“天井/light-well 具体实例的实测通风数据”**；原 `Lightwell` 页（含其维基镜像）确实不含热压字句，仍支持原判断。建议主流程将 `pending_notes` 改写为“热压机制由 Stack effect 权威来源支撑；具体天井实例的实测通风数据待补充”。

## 四、其余条目（42 条）

以下条目历轮（第 4–11 轮）已反复复核，本轮未获新的、可核验的独立线索，按保守原则保持。`sunken-courtyard` 上轮（第 11 轮）重点复核结论为保持，本轮无新证据。

| id | 待核实内容（简） | 结论 |
| --- | --- | --- |
| `linear-perspective` | 实例的具体名称、设计者与年代待补 | 无新证据，保持 |
| `scattered-perspective` | 实例的具体名称、设计者与年代待补 | 无新证据，保持 |
| `composition` | 实例的具体名称、设计者与年代待补 | 无新证据，保持 |
| `balance` | 实例的具体名称、设计者与年代待补 | 无新证据，保持 |
| `proportion` | 实例的具体名称、设计者与年代待补 | 无新证据，保持 |
| `color-theory` | 实例的具体名称、设计者与年代待补 | 无新证据，保持 |
| `value` | 实例的具体名称、设计者与年代待补 | 无新证据，保持 |
| `chiaroscuro` | 实例的具体名称、设计者与年代待补 | 无新证据，保持 |
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
| `gothic` | 实例的具体名称、设计者与年代待补 | 无新证据，保持 |
| `renaissance-style` | 实例的具体名称、设计者与年代待补 | 无新证据，保持 |
| `modernism` | 实例的具体名称、设计者与年代待补 | 无新证据，保持 |
| `postmodernism` | 实例的具体名称、设计者与年代待补 | 无新证据，保持 |
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
| `sunken-courtyard` | 实例中庭院与下沉广场的具体设计者、年份待核实 | 无新证据，保持（沿用第 11 轮：Rockefeller 页仅给综合体建筑师与年代，未给“下沉广场本身”设计者/年份，且为维基镜像） |

## 五、本轮实际打开的 URL 清单（可核对，节录关键项）

| # | URL | 标题 / 机构 | HTTP |
| --- | --- | --- | --- |
| 1 | `https://bauhaus-dessau.de/en/venues/bauhaus-building/` | Bauhaus Building — Stiftung Bauhaus Dessau（官方） | 200 |
| 2 | `https://bauhaus-dessau.de/en/venues/` | Locations — Stiftung Bauhaus Dessau（官方） | 200 |
| 3 | `https://www.archdaily.com/87728/ad-classics-dessau-bauhaus-walter-gropius` | AD Classics: Dessau Bauhaus / Walter Gropius — ArchDaily | 200 |
| 4 | `https://www.designingbuildings.co.uk/wiki/Bauhaus` | Bauhaus — Designing Buildings | 200 |
| 5 | `https://www.uni-weimar.de/en/university/profile/history/` | The History — Bauhaus-Universität Weimar | 200 |
| 6 | `https://www.designingbuildings.co.uk/wiki/Stack_effect` | Stack effect — Designing Buildings | 200 |
| 7 | `https://www.cibsejournal.com/technical/am-10-natural-ventilation-from-feasibility-to-physics/` | AM 10 Natural ventilation — CIBSE Journal | 200 |
| 8 | `https://owiki.org/wiki/Stack_effect` | Stack effect — Open WIKI（维基同源镜像，注明） | 200 |
| 9 | `https://owiki.org/wiki/Lightwell` | Lightwell — Open WIKI（维基同源镜像，注明） | 200 |
| 10 | `https://www.theartstory.org/movement/bauhaus/` | Bauhaus Movement Overview — TheArtStory（查阅，未作主证） | 200 |
| 11 | `https://www.bauhaus.de/en/about-us/history/` | Our history — Das Bauhaus-Archiv（查阅，未直接给德绍校舍年月） | 200 |
| 12 | `https://everything.explained.today/Stack_effect/`、`…/Lightwell/` | Everything Explained.Today（维基镜像，本轮 403） | 403 |
| 13 | `https://www.britannica.com/topic/Bauhaus`、`/art/Bauhaus` | Britannica（阻塞） | 403 |
| 14 | `https://whc.unesco.org/en/list/161/` | UNESCO 世界遗产（阻塞） | 403 |

> **可达性探测（未取到正文）**：`en.wikipedia.org` REST/wiki 直连超时（DNS 投毒）；`owiki.org/Light_well`（无 `/wiki/`）404；`wikiwand.com` 超时；`tate.org.uk`、`nrel.gov`、`bauhaus100.de` DNS 失败；`metmuseum.org` 429/超时；`smarthistory.org`、`nachi.org`、`mdpi.com`、`sciencedirect.com` 403；`energy.gov/energysaver/*`、`buildingscience.com/…`、`unesco.de/*bauhaus*` 404；`wbdg.org/resources/natural-ventilation` 200 但正文为 JS 空壳（无语料）；`yourhome.gov.au/…` 超时；`extension.psu.edu` 405；`getty.edu`、`riba.org`、`bregroup.com`、`bsria.com`、`cibsejournal.com`、`nps.gov`、`gsa.gov`、`bpb.de`、`unesco.de`、`klassik-stiftung.de`、`hs-anhalt.de` 首页可达但未取得针对性数据。

## 六、汇总

- **可升级：1 条 —— `bauhaus`**（德绍包豪斯基金会官方站 + ArchDaily 两独立权威来源直接给出“德绍包豪斯校舍 / Walter Gropius / 1925/26（1926-12-04 落成）”，另 Designing Buildings、魏玛包豪斯大学佐证；未用维基镜像）。
- **可收窄：1 条 —— `light-well`**（热压／烟囱效应机制已由 Designing Buildings 与 CIBSE AM10 两独立权威来源支撑，可把待核实从“机制 + 实例实测数据”收窄为“仅实例实测数据待补”；因缺天井具体实例实测数据，不升级）。
- **保持待核实：42 条**（44 − 1 − 1；含 `sunken-courtyard` 等，沿用第 4–11 轮结论）。
- **打开 URL 数**：本轮共请求 **74 个不同 URL（去重，含 REST/API 端点与可达性探测）**；其中取到 HTTP 正文并用作证据/查阅的权威页见第五节第 1–11 项，另有若干阻塞/超时探测。

保守原则声明：未核验的线索不作为升级依据，不为凑数硬写年份或人名；维基同源镜像（`owiki.org`）不计为独立第二来源；`light-well` 仅在“机制”层面收窄，实例实测数据仍未获，故不升级。
