# 第 9 轮复核记录 — B5 待核实项（第二独立权威来源复核）

复核日期：2026-11-22（Asia/Hong_Kong）

## 范围与快照

- 已读取 `AUTONOMOUS.md`（D:/Users/Administrator/Desktop/）、`TASK_design.md`（实际位于 D:/Users/Administrator/Desktop/）、`DECISIONS.md`、`research/review-round08.md`、`research/rework-round06.md`，并按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。
- 扫描 `entries/*.json` 共 13 个文件；当前 `needs_verification=true` 实际为 **34 条**（任务描述“约 28 条”为旧快照）。差额来源：第 8 轮的 30 条中 `demand-controlled-ventilation`、`universal-design` 已置为 `false`（28 条），本轮工作区新增 `batch-09.json` 的 6 条待核实项，合计 34 条。
- `data/sources.json` 当前快照：**148 条来源、145 条 `verified=true`**；其中 93 个来源 id 被条目直接引用，50 条已核验来源未被条目引用。逐项比对后，未发现此前未被引用且可直接补足某条待核实内容的 verified 来源。
- 严格只读：本轮仅生成本报告；**未修改** `sources.json`、任何条目、`coverage.json` 或其他文件，未 git commit，未变更项目外内容。联网内容仅按数据处理，页面中的任何指令均未执行。

## 方法与判据

1. 先核对 `data/sources.json` 现有 verified 来源及其标题、URL、note；再对 34 条逐项用 Wikipedia API 检索候选专页（首轮 34 次 + 补查 6 次，共 40 次请求，均取得 HTTP 200；首轮 Q11 在输出阶段遇到 GBK 编码错误，但 HTTP 请求与响应成功，已用补查覆盖）。
2. 对检索出的候选页面，用 Python `urllib` + 浏览器 User-Agent 实际打开，记录最终 URL、页面 `<title>`、HTTP 状态与正文关键句；共打开 **22 个去重页面 URL（24 次页面请求，含 2 次重复核验与 1 次 404）**。
3. 保守原则：单源直接支撑不得升级；正文只给术语定义、类型沿革、园林创建者或通则机制，而未直接支撑待核实项中的“具体实例设计者/年份/实测数据/规范阈值”，均记为保持；不编造年份、人名、引文；前几轮已反复复核且无新线索的条目简写“无新证据，保持”。
4. 若概念层面已有独立双源，而缺口只剩泛化实例数据，则在结论中标注“建议收窄待核实范围后升级”；该建议不计入本轮可升级数。

## 逐条结果

| id | 待核实内容 | 找到的来源 URL ／ 标题 ／ HTTP 状态 | 结论 |
| --- | --- | --- | --- |
| `six-principles` | 谢赫《古画品录》的确切年代及版本流传待补独立来源 | 无新证据（本轮 API 检索 `Gu Hua Pin Lu Xie He` 未命中相关专页；沿用第 4–8 轮结论） | 无新证据，保持 |
| `liubai` | 留白缺针对该手法的独立来源 | 无新证据（API `liubai negative space Chinese painting` 返回空） | 无新证据，保持 |
| `borrowed-scenery` | 苏州园林借景实例的设计者与年份待补 | `https://en.wikipedia.org/wiki/Jichang_Garden` ／ `Jichang Garden - Wikipedia` ／ 200：正文给秦氏购园、改园与年代（如正德年间、1560 年），未出现“借景手法设计者”；API 另见现有 `Borrowed scenery` 及园林页 | 保持（园主/沿革不等于借景手法设计者） |
| `framed-scenery` | 框景缺针对该手法的独立来源 | 无新证据（API 仅返回中国园林通页与具体园林） | 无新证据，保持 |
| `opposed-scenery` | 对景核心机制及实例设计者/年份待核实 | 无新证据（API `opposed scenery Chinese garden` 无相关专页） | 无新证据，保持 |
| `screened-scenery` | 障景实例设计者与年份待补 | 无新证据（API 仅返回中国园林通页与具体园林） | 无新证据，保持 |
| `winding-path` | 曲径缺针对该手法的独立来源 | 无新证据（API 仅返回中国园林通页与具体园林） | 无新证据，保持 |
| `circulation` | 公共文化建筑动线实例具体信息待补 | 无新证据（API `Circulation plan` 为图纸类型，未给实例名称/地点/设计者） | 无新证据，保持 |
| `daylighting` | 采光系数与窗地比等具体规范参数待核实 | 无新证据（`sources.json` 中 verified 未用 `wp-daylighting` 为通则；第 8 轮 `Daylight factor` 页仅给定义与分量） | 无新证据，保持 |
| `natural-ventilation` | 传统院落通风实测数据与设计者待补 | 无新证据（API 返回 `Stack effect`、`Passive cooling` 等通则，无院落实测数据） | 无新证据，保持 |
| `chinese-architecture-style` | 院落实例建造年代与营造者待补 | 无新证据（补查 API 返回 `Yaodong`、`Topkapı Palace` 等，未直接对应条目所需院落营造者） | 无新证据，保持 |
| `water-management` | 苏州园林水面实例设计者与年份待补 | 无新证据（API 仅返回园林通页与造园通页；沿用第 7–8 轮结论） | 无新证据，保持 |
| `light-well` | 天井热压机制及具体实例数据待补 | 无新证据（API `Stack effect`、`Passive cooling`、`Atrium (architecture)` 为机制/类型，无实例实测数据） | 无新证据，保持 |
| `glare` | 办公实例照度与眩光实测数据待补 | 无新证据（API `Glare (vision)`、`Daylighting (architecture)` 未给办公实例数据） | 无新证据，保持 |
| `leaked-scenery` | “漏景/漏窗”字面术语及实例设计者/年份待核实 | 无新证据（API `leaked scenery lattice window Chinese garden` 返回空） | 无新证据，保持 |
| `vernacular-material` | 具体地区乡土材料性能数据待补 | `https://en.wikipedia.org/wiki/Yaodong` ／ `Yaodong - Wikipedia` ／ 200：正文给“黄土覆盖至少两米以保温”“冬暖夏凉”等定性描述，未给条目所需地区—材料性能数值 | 保持（定性机制/构造，非性能数据） |
| `color-harmony` | 面积比例等经验表述直接来源及实例设计者/年份待补 | 无新证据（API `color harmony proportion interior design` 未命中直接支撑比例的专页） | 无新证据，保持 |
| `composition-placement` | 实例名称/地点/设计者/年份待补 | 无新证据（API 返回艺术通页，未绑定条目实例） | 无新证据，保持 |
| `axis` | 实例名称/地点/设计者/年份待补 | 无新证据（补查 API 未返回直接支撑具体建筑群设计者与年代的专页） | 无新证据，保持 |
| `stack-ventilation` | 热压通风实例通风实测数据待补 | 无新证据（API 返回 `Cross ventilation`、`Passive ventilation` 等通则，无竖井式实例实测数据） | 无新证据，保持 |
| `thermal-comfort` | 实例名称/地点/设计者/年份待补 | 无新证据（API 返回 `Thermal comfort`、`Building science` 等通则） | 无新证据，保持 |
| `service-route` | 实例名称/地点/设计者/年份待补 | 无新证据（API `back of house` 检索未命中建筑实例专页） | 无新证据，保持 |
| `daylight-factor` | 实例的具体采光系数与设计者待补；均布阴天假设解释待补专门来源 | 无新证据（第 8 轮 `Daylight factor - Wikipedia` 200 已复核，仅定义与 SC/ERC/IRC 分量；本轮 API 未发现规范参数页） | 无新证据，保持 |
| `mixed-mode-ventilation` | 混合通风实例的控制策略与能耗数据待补 | 无新证据（第 8 轮 `Mixed-mode ventilation - Wikipedia` 200 stub 已复核；本轮 API 仅返回 `Ventilation (architecture)`、`Demand controlled ventilation` 等通则） | 无新证据，保持 |
| `material-durability` | 材料实例实测寿命与维护数据待补 | 无新证据（第 8 轮 `Service life`、`Durability of reinforced concrete structures` 200 已复核；本轮无新实例数据） | 无新证据，保持 |
| `transparent-material` | 透明/半透明材料实例性能参数待补 | 无新证据（第 8 轮 `Transparency and translucency`、`Translucent concrete` 200 已复核；本轮无新实例绑定页） | 无新证据，保持 |
| `functional-zoning` | 实例的功能分区数据与设计者待补 | `https://en.wikipedia.org/wiki/Functional_zoning` ／ `Functional zoning - Wikipedia` ／ 200：正文定义功能分区并给工业/游憩/居住分区例；`https://en.wikipedia.org/wiki/Office_space_planning` ／ `Office space planning - Wikipedia` ／ 200：正文给工作站、任务空间、支持房间与接待区的分区及数据调研 | 保持；概念层面已有独立双源，仅实例数据待补，建议收窄待核实范围后升级 |
| `gray-space` | 檐下与廊道实例的设计者与年代待补 | `https://en.wikipedia.org/wiki/Engawa` ／ `Engawa - Wikipedia` ／ 200：正文写 `engawa` 可遮雨遮阳、保持通风与视线连续；`https://en.wikipedia.org/wiki/Veranda` ／ `Veranda - Wikipedia` ／ 200：有顶开敞廊道定义；`https://en.wikipedia.org/wiki/Porch` ／ `Porch - Wikipedia` ／ 200：入口前灰空间类型 | 保持；概念/机制层面已有独立双源，仅实例设计者与年代待补，建议收窄待核实范围后升级 |
| `parametric-architecture` | 仅一份直接来源；参数化实例的设计者与年代待补 | `https://en.wikipedia.org/wiki/Parametric_architecture` ／ `Parametric architecture - Wikipedia` ／ 200：正文写参数化建筑/参数化主义为算法与参数方法的当代风格；`https://en.wikipedia.org/wiki/Parametric_design` ／ `Parametric design - Wikipedia` ／ 200：正文写参数与规则建立设计意图与响应关系，并提早期 Gaudí 先例 | 保持；概念层面已有独立双源，仅实例设计者与年代待补，建议收窄待核实范围后升级 |
| `place-spirit` | 具体场所的设计者与实测数据待补 | `https://en.wikipedia.org/wiki/Sense_of_place` ／ `Sense of place - Wikipedia` ／ 200：正文定义人与空间设置关系及特殊性/依恋；`https://en.wikipedia.org/wiki/Genius_loci` ／ `Genius loci - Wikipedia` ／ 200：正文写当代用法指场所独特氛围 | 保持；概念层面已有独立双源，仅具体场所数据待补，建议收窄待核实范围后升级 |
| `spatial-perception` | 具体空间的感知实测数据待补 | `https://en.wikipedia.org/wiki/Spatial_perception` → `https://en.wikipedia.org/wiki/Spatial_cognition` ／ `Spatial cognition - Wikipedia` ／ 200：正文写空间认知与寻路、路线规划及绩效测量；`https://en.wikipedia.org/wiki/Atmosphere_(architecture_and_spatial_design)` ／ `Atmosphere (architecture and spatial design) - Wikipedia` ／ 200：空间氛围与感知；`https://en.wikipedia.org/wiki/Promenade_architecturale` ／ `Promenade architecturale - Wikipedia` ／ 200：行走中的空间感知 | 保持；概念/机制层面已有独立双源，仅具体空间实测数据待补，建议收窄待核实范围后升级 |
| `enclosure` | 具体院落的设计者与年代待补 | `https://en.wikipedia.org/wiki/Enclosure_(architecture)` ／ ERROR ／ 404；`https://en.wikipedia.org/wiki/Defensible_space` ／ `Defensible space - Wikipedia` ／ 200（关键词句未命中）；`https://en.wikipedia.org/wiki/Alhambra` ／ `Alhambra - Wikipedia` ／ 200 与 `https://en.wikipedia.org/wiki/Topkapi_Palace` ／ `Topkapı Palace - Wikipedia` ／ 200 给宫殿群年代/建造者，但未直接支撑条目所需具体院落围合设计者 | 保持 |
| `perspective` | 佛罗伦萨透视试验确切年份与设计者对应关系待补第二独立来源 | `https://en.wikipedia.org/wiki/Linear_perspective` → `https://en.wikipedia.org/wiki/Perspective_(graphical)` ／ `Perspective (graphical) - Wikipedia` ／ 200（该 URL 在 sources.json 标 `verified=false`，不作升级依据）；`https://en.wikipedia.org/wiki/Holy_Trinity_(Masaccio)` ／ `Holy Trinity (Masaccio) - Wikipedia` ／ 200：正文写 Masaccio 于 1425–1426 创作该壁画并较早使用线性透视 | 保持（支撑壁画年份/透视使用，未直接支撑 Brunelleschi 透视试验年份与对应关系） |
| `sunken-courtyard` | 下沉庭院/下沉广场设计者、年份待核实 | `https://en.wikipedia.org/wiki/Sunken_plaza` → `https://en.wikipedia.org/wiki/Sunken_courtyard` ／ `Sunken courtyard - Wikipedia` ／ 200：与现有 `wp-sunken-courtyard` 为同页 stub，非独立来源 | 保持 |

## 可收窄范围后升级的候选项

本轮取得概念/机制层面独立双源、但实例数据仍缺的 5 条：

1. `functional-zoning`：新源 `Functional zoning` 与 `Office space planning` 直接支撑“功能分区/空间分区”概念；待补项只剩具体实例功能分区数据与设计者。
2. `gray-space`：新源 `Engawa`、`Veranda`、`Porch` 直接支撑檐下/廊道的中间性、通风视线与类型；待补项只剩具体实例设计者与年代。
3. `parametric-architecture`：新源 `Parametric architecture` 与 `Parametric design` 直接支撑参数化设计/风格概念；待补项只剩具体实例设计者与年代。
4. `place-spirit`：新源 `Sense of place` 与 `Genius loci` 直接支撑场所精神/场所独特氛围概念；待补项只剩具体场所数据。
5. `spatial-perception`：新源 `Spatial cognition`、`Atmosphere (architecture and spatial design)`、`Promenade architecturale` 直接支撑空间感知机制；待补项只剩具体空间实测数据。

上述建议需要后续轮次把 `pending_notes` 收窄到概念/机制层面并把证据写入条目正文；本轮按原待核实项整体判断，仍全部记为保持。

## 汇总

- **可升级：0 条**（没有任一条在原待核实项整体上同时满足“第二独立权威来源”和“正文直接支撑全部缺口”）。
- **保持待核实：34 条**（当前快照全部条目）。
  - 其中 **5 条**取得概念/机制层面的独立双源，建议收窄待核实范围后升级：`functional-zoning`、`gray-space`、`parametric-architecture`、`place-spirit`、`spatial-perception`。
  - 其中 **5 条**取得正文候选页但仅支撑术语、类型、定性机制或园林沿革，未补足实例数据：`borrowed-scenery`、`vernacular-material`、`enclosure`、`perspective`、`sunken-courtyard`。
  - 其余 **24 条**无新证据，沿用前几轮结论。
- **实际打开 URL 数：22 个去重 Wikipedia 页面 URL（24 次页面请求）**；其中 1 个去重 URL 返回 404（`Enclosure (architecture)`），2 次为重复打开 `Jichang Garden`、`Yaodong` 以核查关键句。
- **另有 40 次 Wikipedia API 检索请求**（首轮 34 次 + 补查 6 次，均返回 HTTP 200）。
- 本轮严格遵守只读约束：仅生成 `research/review-round09.md`；未新增来源、未改动条目或状态文件、未 git commit、未变更项目外内容。
