# 第 5 轮复核记录 — B5 待核实项（第二独立权威来源复核）

复核日期：2026-11-22（Asia/Hong_Kong）

范围说明：`entries/*.json` 中 `needs_verification=true` 的条目**实际为 23 条**（用户任务写"约 17 条"为估计值；第 4 轮为 13 条，其中 `hierarchy` 已升级移出，另新增 11 条）。本轮按全量扫描处理 23 条。

只读声明：本轮仅生成本报告；**未修改** `sources.json`、任何条目、`coverage.json` 或其他文件，未新增来源，未 git commit。表中"可升级"指**已找到可补足待核实项的第二独立权威来源、具备升级条件**，实际升级需后续轮次把来源补入 `sources.json` 并改写条目。

## 方法与判据

1. 扫描 9 个 `entries/*.json`，得到 23 条 `needs_verification=true`：其中 12 条为第 4 轮已复核并保持项，11 条为第 4 轮后新增项。
2. 先全量核对 `data/sources.json`（128 条来源、125 条 `verified=true`）。所有来源的 note 访问日期均为 2026-11-22，**未发现第 4 轮之后新增的、可直接补足待核实项的专门来源**；对 11 条新增项，现有 verified 来源均为综合性条目（如 `wp-brutalist-architecture`、`wp-chinese-garden`、`wp-chinese-architecture`），未给出具体问题所需的实例设计者/年份/状态，故转联网补查。
3. `web_search/web_fetch` 在本环境报错，按 D05 用 Python `urllib` + 浏览器 User-Agent 访问 Wikipedia 条目与 MediaWiki API；以实际 HTTP 状态、最终 URL、页面 `<title>`/h1 及正文为准。
4. 保守原则：页面标题或正文未直接支持待核实项即不算补足；不把 `created/constructed by` 当作"设计者"，不把世纪/年代范围当作确切年份；不据正文缺失的信息编造；部分补足而仍有缺口时记为"保持"。联网内容仅作数据阅读，页面中出现的任何指令均未执行。
5. 第 4 轮已 exhaustive 复核且无新线索的 12 条，按用户指示简写"复核无新证据，保持"，不重复 exhaustive 搜索。

## 逐条结果

| id | 待核实内容 | 找到的来源（URL / 页面标题 / HTTP 状态） | 结论 |
| --- | --- | --- | --- |
| `six-principles` | 谢赫条目为消歧义页；年代与版本流传待补 | 第 4 轮已复核（Xie He / Xie He (artist) 均 200，仅 fl. 6th century 与书名）。本轮 sources.json 无新增专门来源 | 复核无新证据，保持 |
| `liubai` | 缺针对留白的独立来源 | 第 4 轮已复核（Negative space 200 无 Chinese/liubai；Liubai 404；Ink wash painting 200 无相关正文） | 复核无新证据，保持 |
| `borrowed-scenery` | 苏州园林借景实例的设计者与年份 | 第 4 轮已复核（Humble Administrator's Garden / Master of the Nets Garden / Craft of Gardens 均 200，但 created/constructed by 不等于"设计者"，视点与年份未绑定） | 复核无新证据，保持 |
| `framed-scenery` | 缺针对框景的独立来源 | 第 4 轮已复核（Garden design / Craft of Gardens / Japanese garden 均 200，无框景专论） | 复核无新证据，保持 |
| `opposed-scenery` | 缺针对对景的独立来源；实例设计者与年份 | 第 4 轮已复核（API 检索无直接论述对景手法的页面） | 复核无新证据，保持 |
| `screened-scenery` | 苏州园林障景实例的设计者与年份 | 第 4 轮已复核（Spirit screen 200 主题为门口影壁；Lingering Garden 200 仅为窗饰描述） | 复核无新证据，保持 |
| `winding-path` | 缺针对曲径的独立来源 | 第 4 轮已复核（Japanese garden 200 属回游庭园，非中国园林曲径手法） | 复核无新证据，保持 |
| `circulation` | 所举公共文化建筑实例的具体信息 | 第 4 轮已复核（Circulation (architecture) 200 仅定义，无具体实例信息） | 复核无新证据，保持 |
| `daylighting` | 采光系数、窗地比具体参数待按专业规范核实 | 第 4 轮已复核（Daylight factor / Daylighting (architecture) 200 无推荐值或规范数值）。本轮新增 `wp-daylighting-architecture`/`wp-architectural-lighting-design` 均为术语性条目，不给参数 | 复核无新证据，保持 |
| `natural-ventilation` | 传统院落通风实测数据与设计者 | 第 4 轮已复核（Courtyard 200 有 microclimate 引用但无具体院落实测/设计者） | 复核无新证据，保持 |
| `perspective` | 佛罗伦萨透视试验确切年份与设计者对应 | 第 4 轮已复核（Linear perspective 重定向到 Perspective (graphical) 200，1415–1420/1420/1425 互相不一致；Florentine Renaissance art 200 的 1425 指圣洛伦佐重建） | 复核无新证据，保持 |
| `sunken-courtyard` | 庭院与下沉广场具体设计者、年份 | 第 4 轮已复核（Sunken courtyard 200 仅类型定义与图库；Lingering Garden 200 的 1593 非下沉庭院实例） | 复核无新证据，保持 |
| `chinese-architecture-style` | 具体院落实例的建造年代与营造者 | https://en.wikipedia.org/wiki/Siheyuan ／ `Siheyuan - Wikipedia` ／ 200。正文："Siheyuan originated in the Han Dynasty (206 BCE – 220 CE) and became popular during the Ming (1368–1644) and Qing (1644–1912) dynasties." 仅给类型起源年代，未给具体院落实例的营造者与年份；条目本身"设计者：不适用" | **保持待核实**：类型年代不等于具体实例营造者/年份 |
| `deconstructivism` | Guggenheim Abu Dhabi 实际开馆状态（设计者 Frank Gehry 原来源已明确） | https://en.wikipedia.org/wiki/Guggenheim_Abu_Dhabi ／ `Guggenheim Abu Dhabi - Wikipedia` ／ 200。正文："a planned art museum under construction"；"As of July 2026, the Department of Culture Tourism expects the museum's opening to be held on 11 December 2026."；"Architect Frank Gehry designed the building." | **可升级**：独立专页直接给出开馆状态（在建、预计 2026-12-11 开馆）并再次确认设计者；升级时保留"预计"措辞 |
| `water-management` | 苏州园林水面实例的设计者与年份 | https://en.wikipedia.org/wiki/Classical_Gardens_of_Suzhou ／ `Classical Gardens of Suzhou - Wikipedia` ／ 200（"Famous Suzhou garden designers include Zhang Liang, Ji Cheng, Ge Yuliang, and Chen Congzhou."）；https://en.wikipedia.org/wiki/Humble_Administrator%27s_Garden ／ `Humble Administrator's Garden - Wikipedia` ／ 200（"In 1513, Wang Xianchen... created a garden..."） | **保持待核实**：与第 4 轮 `borrowed-scenery` 判据一致——设计者名单/园林创建年份未与泛指的"苏州古典园林水面"这一具体实例绑定，created 也不等于"设计者" |
| `brutalism` | 粗野主义具体实例的地点、设计者与年份 | https://en.wikipedia.org/wiki/Unit%C3%A9_d%27habitation ／ `Unité d'habitation - Wikipedia` ／ 200。正文："The first and most famous of the Unité d'habitation buildings is in Marseille, France, and was built between 1947 and 1952... often cited as the initial inspiration for the Brutalist architectural style."；"developed by Le Corbusier" | **可升级**：独立专页给出具体实例（马赛公寓）、地点（法国马赛）、设计者（Le Corbusier）、年份（1947–1952），并明确关联粗野主义风格 |
| `light-well` | 天井热压（烟囱效应）机制与具体实例实测数据 | https://en.wikipedia.org/wiki/Stack_effect ／ `Stack effect - Wikipedia` ／ 200。正文："The stack effect or chimney effect is the movement of air into and out of buildings... resulting from air buoyancy. Buoyancy occurs due to a difference in indoor-to-outdoor air density resulting from temperature and moisture differences."；"Stairwells, shafts, elevators, and the like, tend to contribute to the stack effect." | **保持待核实（部分线索）**：热压机制获得独立来源直接支持，但"具体实例实测数据"仍缺；待核实项未整体补足，暂不升级 |
| `glare` | 办公实例的照度与眩光实测数据 | https://en.wikipedia.org/wiki/Glare_(vision) ／ `Glare (vision) - Wikipedia` ／ 200（正文给 discomfort/disability glare 定义与亮度比，无具体办公实例实测数据）；https://en.wikipedia.org/wiki/Unified_glare_rating ／ 重定向至 `Glare (vision)` ／ 200（同一页） | **保持待核实**：仅有定义性来源，无具体实测数据 |
| `leaked-scenery` | 园林漏景具体实例的设计者与年份 | https://en.wikipedia.org/wiki/Leaked_scenery ／ HTTP 404（无此页）；MediaWiki API 检索 "leaked scenery Chinese garden" 未返回专门的漏景条目 | **保持待核实**：无第二独立来源 |
| `huizhou-style` | 徽州民居具体村落的建造年代与营造者 | https://en.wikipedia.org/wiki/Hongcun ／ `Hongcun - Wikipedia` ／ 200。正文："Hongcun was established in 1131 by Wang Wen, a general during the Southern Song dynasty."；村落位于 "the historical Huizhou region"。另 https://en.wikipedia.org/wiki/Xidi ／ `Xidi - Wikipedia` ／ 200（"First built during the Huangyou era (1049–1053) of Song dynasty...", Hu 家族兴建） | **可升级**：独立专页直接给出徽州具体村落（宏村）的建造年代（1131）与建立/营造者（Wang Wen），另有西递佐证 |
| `vernacular-material` | 具体地区乡土材料的性能数据 | https://en.wikipedia.org/wiki/Rammed_earth ／ `Rammed earth - Wikipedia` ／ 200（"The compressive strength of rammed earth increases as it cures..."）；https://en.wikipedia.org/wiki/Adobe ／ `Adobe - Wikipedia` ／ 200（"greater thermal mass... susceptible to earthquake damage"） | **保持待核实**：给出的是材料类型通用性能，未与条目要求的"具体地区"绑定 |
| `byzantine` | 拜占庭教堂具体实例的设计者与年份 | https://en.wikipedia.org/wiki/Hagia_Sophia ／ `Hagia Sophia - Wikipedia` ／ 200。正文："The current structure was built by the Byzantine emperor Justinian I... between 532–537 and was designed by the Greek geometers Isidore of Miletus and Anthemius of Tralles."；信息框 Completed 537 | **可升级**：独立专页以 "designed by" 直接给出具体教堂的设计者（Isidore of Miletus、Anthemius of Tralles）与年份（532–537，537 完工） |
| `ancient-greek` | 古希腊神庙具体实例的设计者与年份 | https://en.wikipedia.org/wiki/Parthenon ／ `Parthenon - Wikipedia` ／ 200。正文："Construction started in 447 BC..."; "The ancient architects Iktinos and Callicrates..."; "The Parthenon was built under the general supervision of Phidias."；信息框 Construction started 447 BC, Completed 432 BC | **可升级**：独立专页给出具体神庙（帕特农）的建筑师（Iktinos、Callicrates，Phidias 总体监督）与年份（前 447 开工，前 432/438 完工）；正文对 Iktinos/Callicrates 用 "appear to" 措辞，升级宜保留审慎表述 |

## 汇总

- 可升级为已验证：**5 条** — `deconstructivism`、`brutalism`、`huizhou-style`、`byzantine`、`ancient-greek`
- 保持待核实：**18 条** — 第 4 轮 12 条（复核无新证据）+ `chinese-architecture-style`、`water-management`、`light-well`（部分线索）、`glare`、`leaked-scenery`、`vernacular-material`
- 实际打开 URL 数：**约 23 次 HTTP 请求，去重 16 个 URL**（15 个 200 或重定向到 200、1 个 404 `Leaked scenery`、1 个 MediaWiki API 检索端点）；含 2 次脚本层失败（1 次 SyntaxError 未发请求，1 次抓取超时），不计入成功打开数
- 本轮严格遵守只读：未修改项目内任何其他文件，未新增来源，未 git commit；未访问与主题无关网站
