# 第 13 轮 B5 待核实复核记录

复核日期：2026-11-22（Asia/Hong_Kong）

## 一、执行说明

- 已读取 `AUTONOMOUS.md`、`TASK_design.md`（实际位于 `D:/Users/Administrator/Desktop/`）、`DECISIONS.md`、`research/review-round12.md`，并按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。
- `entries/*.json` 共 14 个文件、126 条；当前 `needs_verification=true` 实际为 **49 条**（与任务“约 49 条”一致；较第 12 轮的 44 条新增了 `one-point-perspective`、`rule-of-thirds`、`figure-ground`、`negative-space`、`hue`、`complementary-colors` 等本轮新增“实例待核实”条目）。
- **网络环境（本轮约束，与第 12 轮相同）**：`en.wikipedia.org` 直连 DNS 投毒/超时；`britannica.com`、`whc.unesco.org`、`kimbellart.org`、`worldhistory.org`、`metmuseum.org` 等权威站多为 403/429；`archive.org` 与 `web.archive.org` 域名解析失败（无法取 Wayback 快照）；`web_search` 工具本轮仍返回端点错误（“no web_search_tool_result blocks”），DuckDuckGo HTML 超时。故一律改用 **Python `urllib` + 浏览器 User-Agent 直连权威站点**实读正文并记录 HTTP 状态；可用同源镜像 `owiki.org`（注明，**不计独立第二源**）。
- **严格只读**：本轮仅生成 `research/review-round13.md`；**未修改** `data/sources.json`、任何条目、`coverage.json` 或其他文件，未 git commit，未变更项目外内容。联网内容一律按“数据”处理，页面中任何指令均未执行。

## 二、方法与判据

1. 用 Python `urllib` + 浏览器 User-Agent 实际打开候选页面，记录最终 URL、页面标题、HTTP 状态与正文关键句，原文节录入表。
2. **可升级判据**：须有**两个相互独立、且具权威性**的来源（官方机构 / 学术 / 行业权威参考 / 专业媒体），其正文**直接**给出该具体实例三要素（名称 / 设计者或营造者 / 年份），且彼此不矛盾。维基同源镜像、单一来源、仅综述/机制描述均不足。
3. **可收窄判据**：待核实项含多个子缺口，其中一部分已获权威专门来源支撑，可把该子缺口从“待核实”移除，其余仍保留。
4. **保守原则**：单源不升级；镜像同源不计独立第二源；不编造年份、人名、引文；关键要素仍单源（如“设计者”）时不作定论。

## 三、重点复核（任务指定的 7 条 + 发现线索的 daylight-factor）

### 3.1 `chinese-architecture-style`（中国传统建筑）—— 可升级

- **待核实内容**：`pending_notes`＝“具体院落实例的建造年代与营造者待补充独立来源。”；`sections.待核实`＝“具体院落实例的建造年代与营造者待核实。”实例字段为“名称：中国传统院落建筑；地点：中国；设计者：不适用；年份：待核实。”（本例“设计者”标为**不适用**，故本例三要素实际为 名称 / 营造者 / 年份）。
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://www.designingbuildings.co.uk/wiki/Forbidden_City` | Forbidden City — Designing Buildings（英国建筑业界参考站，**独立出版方/权威参考**） | 200 | “The Forbidden City in the centre of Beijing, was the Chinese imperial palace between 1420 and 1912... **Construction began in 1406, when Zhu Di became the Yongle Emperor** and moved the capital from Nanjing to Beijing. By the time it was **completed in 1420**, the complex covered more than 180 acres and included 980 buildings.” |
| `https://www.travelchinaguide.com/cityguides/beijing/forbidden.htm` | Forbidden City, Beijing: Palace Museum — TravelChinaGuide（独立英文导览站，**佐证**） | 200 | “Construction Time: **1406 to 1420, Ming Dynasty**；Initiator: **Emperor Chengzu of the Ming Dynasty**；Designer: **Kuai Xiang**；... former imperial palace ...” |

- **结论：可升级。** 两个相互独立来源正文均直接给出同一具体实例的 **名称＝北京紫禁城（Forbidden City）**、**地点＝北京**、**年代＝1406–1420（明永乐朝始建、1420 建成）**、**营造者/营建发起者＝明成祖朱棣（永乐帝，Zhu Di / Emperor Chengzu）**。其中 Designing Buildings 为权威建筑行业参考，TravelChinaGuide 为独立导览佐证，二者在“年代 + 营建发起者”上完全一致，未发现矛盾。
  - 附带线索（**不作定论**）：“设计者＝蒯祥（Kuai Xiang）”目前**仅见 TravelChinaGuide 单一来源**，故在报告与建议中仅列为单源附注，不以之作为升级依据。
  - 建议主流程（本报告仅结论，不改数据）：将 `实例` 改为“名称：北京紫禁城（Forbidden City）；地点：北京；营造者：明成祖朱棣（永乐帝）；年份：1406–1420”；据上述两源在 `data/sources.json` 新增 verified=true 来源后清除 `needs_verification`；若要写“设计者蒯祥”须再补第二权威来源。

### 3.2 `daylighting`（自然采光）—— 可升级（实例三要素；数值参数仍作一般性说明）

- **待核实内容**：`pending_notes`＝“采光系数与窗地比等具体参数待按专业规范核实，正文仅作一般性说明。”；`sections.待核实`＝“展厅实例的具体参数与设计者待核实。”实例字段“名称：博物馆展厅自然采光；地点/设计者/年份：待核实”。
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://architectuul.com/architecture/kimbell-art-museum` | Kimbell Art Museum — Architectuul（独立建筑数据库/百科） | 200 | “The Kimbell Art Museum's original building, **designed by Louis Kahn** and **opened to the public for the first time in 1972**, has become a mecca of modern architecture... Kahn designed a building in which **‘light is the theme.’** Kahn's innovative use of **natural light** and subtle articulation of space and materials greatly enhance the experience of the art.” |
| `https://www.designingbuildings.co.uk/wiki/Louis_Kahn` | Louis Kahn — Designing Buildings（英国建筑业界参考站，**独立出版方/权威参考**） | 200 | “Louis Kahn (1901-74) is regarded as one of America's greatest architects... **Kimbell Art Museum, Fort Worth (1972)**... geometric forms revealed through the action of **light**.” |

- **结论：可升级（就实例三要素而言）。** 两个相互独立来源均直接支撑同一展厅实例的三要素：**名称＝金贝尔美术馆（Kimbell Art Museum）**、**地点＝美国德州沃思堡（Fort Worth）**、**设计者＝路易·康（Louis I. Kahn）**、**年份＝1972**，且均有“以自然光为主题”的表述，正是“博物馆展厅自然采光”的典型实例。
  - **范围界定（诚实声明）**：本升级仅覆盖“实例的名称/地点/设计者/年份”；**采光系数、窗地比等具体数值参数本轮仍未取得专门规范来源**，按 TASK_design D09 继续作一般性说明，不作数值定论。若要求“具体参数”也须落实，则本条至多“可收窄”为“仅数值参数待补”。

### 3.3 `daylight-factor`（采光系数）—— 可收窄

- **待核实内容**：`pending_notes`＝“实例参数与设计者待补独立来源；均布阴天假设下的解释性概括待补专门来源。”
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://www.designingbuildings.co.uk/wiki/Daylight_factor` | The daylight factor — Designing Buildings（英国建筑业界参考站，**专门来源/权威参考**） | 200 | “This is expressed as a percentage of the simultaneous outdoor illuminance on a horizontal plane under an unobstructed **CIE Standard Overcast Sky**.” Ref Commission Internationale de L'Éclairage（国际照明委员会），**CIE Standard 011/E:2003**；并给出 point daylight factor 等定义。 |

- **结论：可收窄。** “均布阴天假设（CIE 标准全阴天）下的解释性概括”这一子缺口已由 **专门来源** Designing Buildings《The daylight factor》（明确引 CIE Standard Overcast Sky / CIE 011/E:2003）支撑，可从待核实中移除。剩余子缺口“具体实例的采光系数数值与设计者”仍未获，保留。建议 `pending_notes` 改写为“具体实例的采光系数数值与设计者待补独立来源（均布阴天假设已由 CIE 标准与 Designing Buildings 专门来源说明）”。

### 3.4 `six-principles`（中国画六法）—— 保持

- **待核实内容**：“谢赫条目为消歧义页；年代与版本流传待补充专门研究来源。”
- **核对**：仅 `https://owiki.org/wiki/Xie_He`（Open WIKI，**维基同源镜像**，HTTP 200）可读，属同一维基来源，**不计独立第二来源**；`britannica.com/biography/Xie-He`（403）、`metmuseum.org`（429）均被阻塞；未取得独立权威艺术史专门来源直接支撑“谢赫与《古画品录》确切年代及版本流传”。
- **结论：无新证据，保持。**（该条待核实的“版本流传”本身需专门文献学研究，非单页可解决。）

### 3.5 `circulation`（动线设计）—— 保持

- **待核实内容**：“所举公共文化建筑实例的具体信息待补充，暂不作确定性陈述。”
- **核对**：所举为“公共文化建筑参观动线”泛化实例，未确定唯一具体建筑；本轮未获可锁定“名称/地点/设计者/年份”的成对独立来源。
- **结论：无新证据，保持。**

### 3.6 `natural-ventilation`（自然通风）—— 保持

- **待核实内容**：“传统院落通风的实测数据与设计者信息待补充独立来源。”
- **核对**：`https://www.designingbuildings.co.uk/wiki/Natural_ventilation`（Natural ventilation of buildings，HTTP 200）可作**机制/原理**参考，但**不含传统院落的通风实测数据**，故不能补足“实测数据”子缺口。
- **结论：无新证据，保持**（机制层面有来源，实测数据仍缺）。

### 3.7 `water-management`（理水）—— 保持

- **待核实内容**：“苏州园林水面实例的设计者与年份待补充独立来源。”
- **核对**：`data/sources.json` 已有 `unesco-suzhou-gardens`（whc.unesco.org/en/list/813，verified）与 `wp-humble-administrators-garden`（维基）等来源，可证“苏州古典园林”整体，但**未直接给出某一水面实例（如拙政园）的设计者与年份**；本轮 `whc.unesco.org/en/list/813`（403）、`britannica.com/place/Humble-Administrators-Garden`（403）均阻塞，`chinahighlights`/`travelchinaguide` 的拙政园专页为 JS 空壳或 404，未取到“设计者（如文徵明）+ 年份（如 1509）”的正文证据，更无第二权威来源。
- **结论：无新证据，保持。**

### 3.8 `glare`（眩光）—— 保持

- **待核实内容**：“办公实例的照度与眩光实测数据待补充独立来源。”
- **核对**：`https://www.designingbuildings.co.uk/wiki/Glare`（Glare in buildings，HTTP 200）给出眩光定义（引 BSRIA《Illustrated Guide to Electrical Building Services》BG 31/2017）与成因，属**定义/机理**来源；但**不含具体办公实例的照度与眩光指数（如 UGR）实测数据**，故不能补足本待核实项。
- **结论：无新证据，保持**（定义有来源，办公实例实测数据仍缺）。

## 四、其余 41 条（无新证据，保持）

以下条目待核实项为“实例具体名称/设计者/年份”或“实测/性能参数”，本轮未取得成对的独立权威来源直接支撑，按保守原则保持。`light-well` 沿用第 12 轮结论（机制已双源收窄，仅实例实测数据待补）。第 12 轮已复核的 `sunken-courtyard`、`perspective` 等本轮无新证据。

| id | 待核实内容（简） | 结论 |
| --- | --- | --- |
| `linear-perspective` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `scattered-perspective` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `composition` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `balance` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `proportion` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `color-theory` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `value` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `one-point-perspective` | 实例的具体名称、设计者与年代待补充独立来源（本轮新增） | 无新证据，保持 |
| `rule-of-thirds` | 实例的具体名称、设计者与年代待补充独立来源（本轮新增） | 无新证据，保持 |
| `figure-ground` | 实例的具体名称、设计者与年代待补充独立来源（本轮新增） | 无新证据，保持 |
| `negative-space` | 实例的具体名称、设计者与年代待补充独立来源（本轮新增） | 无新证据，保持 |
| `hue` | 实例的具体名称、设计者与年代待补充独立来源（本轮新增） | 无新证据，保持 |
| `complementary-colors` | 实例的具体名称、设计者与年代待补充独立来源（本轮新增） | 无新证据，保持 |
| `chiaroscuro` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `liubai` | 待补针对留白的独立来源 | 无新证据，保持 |
| `borrowed-scenery` | 苏州园林借景具体实例的设计者与年份待补充独立来源 | 无新证据，保持 |
| `framed-scenery` | 待补针对框景的独立来源 | 无新证据，保持 |
| `opposed-scenery` | 未直接支撑“对景”核心机制；实例设计者/年份待核实 | 无新证据，保持 |
| `screened-scenery` | 苏州园林障景具体实例的设计者与年份待补充独立来源 | 无新证据，保持 |
| `winding-path` | 待补针对曲径的独立来源 | 无新证据，保持 |
| `gothic` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `renaissance-style` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `modernism` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `postmodernism` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `light-well` | 具体天井实例的采光与通风实测数据待补充（机制已参见自然通风） | 无新证据，保持（沿用第 12 轮：仅实例实测数据待补） |
| `leaked-scenery` | 未出现“漏景/漏窗”字面术语；实例设计者/年份待核实 | 无新证据，保持 |
| `vernacular-material` | 具体地区乡土材料的性能数据待补充独立来源 | 无新证据，保持 |
| `color-harmony` | 面积比例等经验性表述待补直接来源；实例设计者/年份待核实 | 无新证据，保持 |
| `composition-placement` | 实例的具体名称、地点、设计者与年份待补充独立来源 | 无新证据，保持 |
| `axis` | 实例的具体名称、地点、设计者与年份待补充独立来源 | 无新证据，保持 |
| `stack-ventilation` | 热压通风实例的通风实测数据待补充独立来源 | 无新证据，保持 |
| `thermal-comfort` | 实例的具体名称、地点、设计者与年份待补充独立来源 | 无新证据，保持 |
| `service-route` | 实例的具体名称、地点、设计者与年份待补充独立来源 | 无新证据，保持 |
| `mixed-mode-ventilation` | 混合通风实例的控制策略与能耗数据待补充独立来源 | 无新证据，保持 |
| `material-durability` | 实例寿命与维护数据、退化机制通用列表待补充独立来源 | 无新证据，保持 |
| `transparent-material` | 透明与半透明材料实例的性能参数待补充独立来源 | 无新证据，保持 |
| `functional-zoning` | “功能分区”术语定义与实例数据均待补独立来源 | 无新证据，保持 |
| `gray-space` | 檐下与廊道实例的设计者与年代待补独立来源 | 无新证据，保持 |
| `enclosure` | 具体院落的设计者与年代待补独立来源 | 无新证据，保持 |
| `perspective` | 佛罗伦萨透视试验确切年份与设计者对应关系待补第二独立来源 | 无新证据，保持 |
| `sunken-courtyard` | 中庭院与下沉广场的具体设计者、年份待核实 | 无新证据，保持（沿用第 11–12 轮） |

## 五、本轮实际打开的 URL 清单（关键证据页 + 阻塞项）

| # | URL | 标题 / 机构 | HTTP | 用途 |
| --- | --- | --- | --- | --- |
| 1 | `https://www.designingbuildings.co.uk/wiki/Forbidden_City` | Forbidden City — Designing Buildings | 200 | `chinese-architecture-style` 主证（1406–1420、永乐帝） |
| 2 | `https://www.travelchinaguide.com/cityguides/beijing/forbidden.htm` | Forbidden City, Beijing — TravelChinaGuide | 200 | `chinese-architecture-style` 独立佐证（1406–1420、Chengzu、Kuai Xiang） |
| 3 | `https://architectuul.com/architecture/kimbell-art-museum` | Kimbell Art Museum — Architectuul | 200 | `daylighting` 主证（Kahn、1972、自然光） |
| 4 | `https://www.designingbuildings.co.uk/wiki/Louis_Kahn` | Louis Kahn — Designing Buildings | 200 | `daylighting` 第二独立源（Kimbell, Fort Worth (1972)） |
| 5 | `https://www.designingbuildings.co.uk/wiki/Daylight_factor` | The daylight factor — Designing Buildings | 200 | `daylight-factor` 专门来源（CIE 全阴天假设） |
| 6 | `https://www.designingbuildings.co.uk/wiki/Daylight` | Natural light — Designing Buildings | 200 | `daylighting` 概念参考（查阅） |
| 7 | `https://www.designingbuildings.co.uk/wiki/Glare` | Glare in buildings — Designing Buildings | 200 | `glare` 定义来源（无实例数据） |
| 8 | `https://www.designingbuildings.co.uk/wiki/Natural_ventilation` | Natural ventilation of buildings — Designing Buildings | 200 | `natural-ventilation` 机制参考（无实测数据） |
| 9 | `https://owiki.org/wiki/Xie_He` | Xie He — Open WIKI（维基同源镜像，注明，不计独立第二源） | 200 | `six-principles` 查阅（镜像） |

> **可达性探测（未取到可用正文，非证据）**：`en.wikipedia.org`（直连超时/DNS 投毒）；`britannica.com`〔Kimbell / Forbidden City / Humble-Administrators-Garden / Chinese-garden / biography/Xie-He〕403；`whc.unesco.org/en/list/813`、`/439` 403；`kimbellart.org` 403；`archive.org`、`web.archive.org` 域名解析失败（无法取 Wayback）；`metmuseum.org` 429；`worldhistory.org` 403；`thoughtco.com` 402；`history.com` 406；`arch2o.com` 403；`archeyes.com` 502；`baike.baidu.com` 403；`en.wikiarquitectura.com` 403；`oxfordreference.com` 302 重定向；`theartstory.org/artist/xie-he`、`travelchinaguide/...humble-administrator(s)`、`chinahighlights/.../forbidden-city`、`designingbuildings/.../Humble_Administrator's_Garden`、`/Chinese_garden` 等 404；`archdaily.com` 具体 Kimbell 文章（63929/19064/909090 均 404 或重定向至他文，搜索页为 JS 空壳）；`suzhou.gov.cn`、`english.suzhou.gov.cn`、`chinadaily.com.cn` 首页可达但未见拙政园设计者/年份正文；`chinahighlights` 拙政园页正文为 JS 空壳（无 1509/王献臣字句）。

## 六、汇总

- **可升级：2 条 —— `chinese-architecture-style`、`daylighting`**
  - `chinese-architecture-style`：Designing Buildings《Forbidden City》+ TravelChinaGuide《Forbidden City, Beijing》两独立来源均证 **紫禁城 / 北京 / 1406–1420 / 营造者=明成祖朱棣（永乐帝）**（设计者蒯祥仅单源，附注不作定论）。
  - `daylighting`：Architectuul《Kimbell Art Museum》+ Designing Buildings《Louis Kahn》两独立来源均证 **金贝尔美术馆 / 沃思堡 / 路易·康（Louis I. Kahn）/ 1972 / 自然光为主题**（采光系数数值参数仍作一般性说明）。
- **可收窄：1 条 —— `daylight-factor`**（“均布阴天假设（CIE 标准全阴天）”已有 Designing Buildings 专门来源支撑，剩余“具体实例采光系数数值与设计者”仍待补）。
- **保持待核实：46 条**（49 − 2 − 1；含 `six-principles`、`circulation`、`natural-ventilation`、`water-management`、`glare`、`light-well`、`perspective`、`sunken-courtyard` 等，多数沿用第 4–12 轮结论）。
- **打开 URL 数**：本轮实际向约 **60 个不同 URL**（去重，含反复探测、REST/首页探测与阻塞项）发起请求；其中取到 HTTP 200 正文并用作证据/查阅的关键页见第五节第 1–9 项。

> 保守原则声明：未核验线索不作为升级依据；不为凑数硬写年份或人名；维基同源镜像（`owiki.org`）不计独立第二源；`daylighting`、`chinese-architecture-style` 仅在“实例三要素（名称/设计者或营造者/年份）”层面升级，未把仍属单源的“设计者蒯祥”“采光系数数值”等硬写成定论。
