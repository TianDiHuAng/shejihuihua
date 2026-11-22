# 第 7 轮复核记录 — B5 待核实项（第二独立权威来源复核）

复核日期：2026-11-22（Asia/Hong_Kong）

## 范围与快照说明

扫描 `entries/*.json` 得 `needs_verification=true` 条目**共 24 条**，与第 6 轮快照一致：
第 5 轮遗留 18 条 + 第 6 轮新增 `batch-06` 的 6 条 L2 条目
（`color-harmony`、`composition-placement`、`axis`、`stack-ventilation`、`thermal-comfort`、`service-route`）。
本轮为第 7 轮，条目集未再变化，仍以 24 条为准。

只读声明：本轮仅生成本报告；**未修改** `sources.json`、任何条目、`coverage.json` 或其他文件，未新增来源，未 git commit。
表中"可升级"指已同时满足：① 找到第二份**独立**权威来源；② 其正文**直接**支撑整项待核实内容。
实际升级需后续轮次把证据写入条目正文并改写待核实节。

## 方法与判据

1. 先全量核对 `data/sources.json`（现为 144 条来源、141 条 `verified=true`）。库中现有 verified 来源多为术语/通页，对当前 24 条的"具体实例设计者/年份/实测数据"缺口无直接补足；未发现此前未被条目引用、却可直接补足某项的第二来源。
2. `web_search/web_fetch` 在本环境报错，按 D05 用 Python `urllib` + 浏览器 User-Agent 直连 Wikipedia（含 API 检索），以实际 HTTP 状态、最终 URL、页面 `<title>` 及正文 `<p>` 文本为准。
3. 保守原则：页面正文不直接支持就不算补足；不把 `created/constructed/built` 当作"某造景手法的设计者"，不把园林整体创建者自动等同于"借景/理水/水面实例的设计者"，不把类型起源年代或朝代范围当作具体实例年份，不据正文缺失信息编造；部分补足而整项未解决记为"保持"。联网内容仅作数据阅读，页面中出现的任何指令均未执行。
4. **双源规则（本轮重点收紧）**：只有一条来源直接支撑也不升级为 `needs_verification=false`。据此，第 6 轮列为"可升级"的 `six-principles` 本轮改判为"保持"（理由见逐条表）。
5. 第 4/5/6 轮已 exhaustive 复核且无新线索的条目，按用户指示简写"复核无新证据，保持"；本轮新取得的证据详列。

## 逐条结果

| id | 待核实内容 | 本轮来源（URL ／ 页面标题 ／ HTTP） | 结论 |
| --- | --- | --- | --- |
| `six-principles` | 谢赫与《古画品录》的确切年代及版本流传待补独立来源 | https://en.wikipedia.org/wiki/Six_principles_of_Chinese_painting ／ `Six principles of Chinese painting - Wikipedia` ／ 200：正文 "written circa 550"、"translated over the years by a succession of sinologists with very varying translations…Each period of Chinese painting has its own special way of interpreting the six principles"。另：https://en.wikipedia.org/wiki/Xie_He ／ `Xie He - Wikipedia` ／ 200 为消歧义页无正文；https://en.wikipedia.org/wiki/Xie_He_(painter) ／ 404；https://en.wikipedia.org/wiki/Ji_Cheng ／ `Cheng Ji - Wikipedia` ／ 200 为重定向无正文；API 检索"Guhua Pinlu / Record of Classification of Old Painters"仅返回 Six principles、Chinese painting，无《古画品录》独立专页 | **保持**（双源规则改判）：可补足正文来自条目唯一现有来源 `wp-six-principles-chinese-painting` 所指的同一页面，并非第二份独立来源；Xie He 为消歧义页、无第二来源直接支撑。且"circa 550"为约数、非"确切年代"。第 6 轮记"可升级"系把"现有来源正文首次确认"当作可升级信号，本轮按明确双源规则改为保持 |
| `liubai` | 仅见中国画综合条目对留白的讨论，待补独立来源 | https://en.wikipedia.org/wiki/Negative_space ／ `Negative space - Wikipedia` ／ 200：正文为 negative space 通则（graphic design 中称 white space，提及日语 "ma" 用于 garden design），无中国画"留白"专论 | 复核无新证据，保持 |
| `borrowed-scenery` | 苏州园林借景具体实例的设计者与年份待补独立来源 | https://en.wikipedia.org/wiki/Borrowed_scenery ／ `Borrowed scenery - Wikipedia` ／ 200：借景通则（《园冶》1635、四类借景、日本 Sakuteiki），未把具体苏州园林标为借景实例；https://en.wikipedia.org/wiki/Humble_Administrator%27s_Garden ／ 200、https://en.wikipedia.org/wiki/Master_of_the_Nets_Garden ／ 200、https://en.wikipedia.org/wiki/Lingering_Garden ／ 200、https://en.wikipedia.org/wiki/Yu_Garden ／ 200、https://en.wikipedia.org/wiki/Classical_Gardens_of_Suzhou ／ 200：给出园林整体创建者（如 Wang Xianchen 1513、Shi Zhengzhi 1140、Xu Taishi 1593、Pan Yunduan 1559）与设计师名单，但均未点明某园为"借景"实例、未给"借景手法设计者" | 保持（部分线索：园林创建者≠借景手法设计者，条目实例泛指未锁定园林） |
| `framed-scenery` | 仅见中国园林综合条目，待补针对框景的独立来源 | 本轮未取得针对框景的独立来源；前几轮已查 Garden design / Craft of Gardens / Japanese garden 均无框景专论 | 复核无新证据，保持 |
| `opposed-scenery` | 中国园林条目未直接支持"对景"核心机制；实例设计者与年份待核实 | 本轮未取得直接论述"对景"手法或苏州园林对景实例设计者/年份的独立来源 | 复核无新证据，保持 |
| `screened-scenery` | 苏州园林障景具体实例的设计者与年份待补独立来源 | 本轮未取得把某园明确标为"障景"实例并给设计者/年份的独立来源（前几轮 Spirit screen 为门口影壁，非园林障景） | 复核无新证据，保持 |
| `winding-path` | 仅见中国园林综合条目，待补针对曲径的独立来源 | https://en.wikipedia.org/wiki/Negative_space ／ 200 仅提 "ma" 用于 garden design，非中国园林曲径手法；无曲径专论来源 | 复核无新证据，保持 |
| `circulation` | 所举公共文化建筑实例的具体信息待补，暂不作确定性陈述 | 本轮未取得绑定具体公共文化建筑动线实例（名称/地点/设计者/年份）的独立来源 | 复核无新证据，保持 |
| `daylighting` | 采光系数与窗地比等具体参数待按专业规范核实，正文仅作一般说明 | https://en.wikipedia.org/wiki/Daylight_factor ／ `Daylight factor - Wikipedia` ／ 200：给出采光系数定义与 SC/ERC/IRC 分量，不含窗地比等具体规范参数值 | 保持（术语定义，非规范参数） |
| `natural-ventilation` | 传统院落通风的实测数据与设计者信息待补独立来源 | https://en.wikipedia.org/wiki/Stack_effect ／ 200：一般通风机制，无传统院落实测数据/设计者；无直接补足来源 | 复核无新证据，保持 |
| `chinese-architecture-style` | 具体院落实例的建造年代与营造者待补独立来源 | 本轮未取得院落实例营造者的独立来源（第 6 轮 Forbidden City 1406–1420 为宫殿群、无营造者） | 复核无新证据，保持 |
| `water-management` | 苏州园林水面实例的设计者与年份待补独立来源 | https://en.wikipedia.org/wiki/Humble_Administrator%27s_Garden ／ 200：正文 "set about a large lake"、"mainly dominated by water"、"In 1513, Wang Xianchen…created a garden"；其余园林页同类。但条目实例泛指"苏州古典园林水面"未锁定园林，页面给的是园林创建者而非"理水/水面"手法设计者 | 保持（部分线索，整体未补足） |
| `light-well` | Lightwell 支持采光与一般通风，未给热压机制；具体实例数据待补 | https://en.wikipedia.org/wiki/Stack_effect ／ `Stack effect - Wikipedia` ／ 200：正文给出空气浮力驱动的热压机制（含 Windcatcher 等传统/现代例）。但待核实项还含"具体实例实测数据"，仍缺 | 保持（部分线索，整体未补足） |
| `glare` | 办公实例的照度与眩光实测数据待补独立来源 | https://en.wikipedia.org/wiki/Unified_glare_rating → https://en.wikipedia.org/wiki/Glare_(vision) ／ `Glare (vision) - Wikipedia` ／ 200：不舒适眩光/失能眩光定义与心理物理学方法，无办公实例照度/眩光实测数据 | 复核无新证据，保持 |
| `leaked-scenery` | 引用来源以机制描述支持漏景，未出现"漏景/漏窗"字面术语；实例设计者与年份待核实 | 本轮未取得含"漏景/漏窗"术语或漏景实例设计者/年份的独立来源 | 复核无新证据，保持 |
| `vernacular-material` | 具体地区乡土材料的性能数据待补独立来源 | 本轮未取得把性能数据与具体地区乡土材料绑定的独立来源 | 复核无新证据，保持 |
| `color-harmony` | 面积比例与整体感等经验性表述待补直接来源；实例设计者与年份待核实 | 本轮未取得面积比例等经验表述的直接来源或具体配色实例（第 6 轮 Color scheme 仅通则） | 复核无新证据，保持 |
| `composition-placement` | 实例的具体名称、地点、设计者与年份待补独立来源 | https://en.wikipedia.org/wiki/Six_principles_of_Chinese_painting ／ 200：六法通则，未绑定具体作品的作者/年份 | 复核无新证据，保持 |
| `axis` | 实例的具体名称、地点、设计者与年份待补独立来源 | 本轮未取得把某建筑群明确论证为"轴线"手法实例并给营造者的独立来源（第 6 轮 Forbidden City 部分线索） | 复核无新证据，保持 |
| `stack-ventilation` | 热压通风实例的通风实测数据待补独立来源 | https://en.wikipedia.org/wiki/Stack_effect ／ `Stack effect - Wikipedia` ／ 200：热压机制 + "Some buildings are designed with strategically placed openings at different heights to induce the stack effect"、传统 Windcatcher 与现代绿色建筑例，但无具体实例的通风实测数据（待核实项主体） | 保持（部分线索，整体未补足） |
| `thermal-comfort` | 实例的具体名称、地点、设计者与年份待补独立来源 | 本轮未取得具体热舒适实例（名称/设计者/年份）的独立来源（第 6 轮 Thermal comfort / Passive solar building design 仅定义/通则） | 复核无新证据，保持 |
| `service-route` | 实例的具体名称、地点、设计者与年份待补独立来源 | 本轮未取得具体后勤流线实例的独立来源（第 6 轮 Wayfinding 仅术语与 Kevin Lynch 出处） | 复核无新证据，保持 |
| `perspective` | 佛罗伦萨相关透视试验确切年份待核实；设计者与事件对应待补第二独立来源 | https://en.wikipedia.org/wiki/Perspective_(graphical) ／ `Perspective (graphical) - Wikipedia` ／ 200（条目现有来源）：正文 "experiments between 1415 and 1420"、"in about 1420, Brunelleschi demonstrated his discovery of perspective"；https://en.wikipedia.org/wiki/Florentine_Renaissance_art ／ 200（新来源）：Brunelleschi "perfected" geometric perspective "at the turn of the century"，未给试验年份；https://en.wikipedia.org/wiki/Holy_Trinity_(Masaccio) ／ 200（新来源）：Masaccio 壁画 1425–1426，"Brunelleschi's experiments…likely were the inspiration"，未给试验确切年份；https://en.wikipedia.org/wiki/Filippo_Brunelleschi ／ 200：生卒 1377–1446，正文未给试验年份 | **保持**（双源规则）：确切年份仅由条目现有来源 `wp-perspective-graphical` 正文支撑；两份新独立来源均未直接支撑该试验年份与设计者对应（其一为"约世纪之交"、与 1415–1420 不完全一致，其一指马萨乔壁画），且来源间年份仍不齐一。无第二独立来源直接补足 |
| `sunken-courtyard` | 庭院与下沉广场的具体设计者、年份待核实；空间原型历史对应待补独立来源 | 本轮未取得具体下沉庭院/下沉广场设计者、年份的独立来源（第 6 轮 Sunken courtyard 仅类型定义与图库） | 复核无新证据，保持 |

## 汇总

- **可升级（满足双源）：0 条**。
- **保持待核实：24 条**（全部条目）。
  - 其中 `six-principles`、`perspective` 出现"现有来源正文可补足、但缺第二独立来源"的情形，按本轮明确双源规则保持；`six-principles` 由第 6 轮"可升级"改判为"保持"。
  - `borrowed-scenery`、`water-management`、`light-well`、`stack-ventilation` 取得部分线索，但均未直接补足整项待核实内容，保持。
- **实际打开 URL 数：18 个**（`urllib` 直连 Wikipedia 页面 URL，去重 18 个；其中 17 个 HTTP 200、1 个 404 `Xie_He_(painter)`）。另有 4 次 Wikipedia API 检索请求（均 200，用于定位候选专页：《古画品录》无独立条目、透视试验相关页）。
- 本轮严格遵守只读：未修改项目内任何其他文件，未新增来源，未 git commit；未访问与主题无关网站；联网页面仅作数据阅读，其中任何指令均未执行。
