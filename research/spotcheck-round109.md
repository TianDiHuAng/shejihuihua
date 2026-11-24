# 第109轮质量抽检（spotcheck-round109）——vehicle-flow / pedestrian-flow 双平台支撑与 DB Traffic/Pedestrian「泛述还是流线组织」核查

- 抽检人：spotcheck-r109（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（现抓、现跑、后断言；证据先于结论）。`using-superpowers` 命中 SUBAGENT-STOP，按任务说明书直接执行；`verification-before-completion` 全程遵循——本文所有判断均附本轮实抓/实跑/实读输出。
- 抽检对象（均宣称升级 nv=false、类型性实例；实读当前 JSON 为准，均已实读）：
  1. `vehicle-flow`（车行流线）——`entries/batch-36.json` L6 起；sources = `wp-wayfinding` / `wp-urban-design` / `db-traffic`（3 条，含 DB 非维基）；coverage：status 已写 / source_count 3 / needs_verification_count 0 / level L2 / last_updated 2026-11-24。
  2. `pedestrian-flow`（人行流线）——`entries/batch-02-c.json` L40 起；sources = `wp-wayfinding` / `wp-urban-design` / `db-pedestrian`（3 条，含 DB 非维基）；coverage：status 已写 / source_count 3 / needs_verification_count 0 / level L2 / last_updated 2026-11-24。
- 本轮变更集（`git diff` 实读，`git diff --stat`：coverage 8、data/sources 24、batch-02-c 11、batch-36 11、site 三页、?? `tools/apply_review_round109.py`）：
  - `vehicle-flow`：sources 追加 `db-traffic`；`实例` 由「类型性描述；地点与设计者不适用……」改为「园区车行道与出入口（类型性，不指定具体项目）……」；`待核实`「具体实例待补充独立来源」→「暂无已知待核实项。」；`needs_verification` true→**false**、`pending_notes` 清空。
  - `pedestrian-flow`：sources 追加 `db-pedestrian`；`实例` 改为「商业步行街流线（类型性，不指定具体项目）……」；`待核实`「示例街道设计者与年代待核实」→「暂无已知待核实项。」；`needs_verification` true→**false**、`pending_notes` 清空。
- 任务点名要特别判断的非维基源 `db-traffic`（`/wiki/Traffic`）与 `db-pedestrian`（`/wiki/Pedestrian`）——是否**真支撑「车行 / 步行流线组织」**，还是**仅泛述「交通 / 行人」词义**。结论见各节 ★。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round109.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`site/`、`tools/`，未 `git commit`，未改项目外内容。抓取、词频、相似度、去重、结构、SVG、site 一致性均内存态（`python - <<'PY'` / 工具直读）跑，未落盘临时文件（除本报告）。
- `git status --short` 本轮实读：`M coverage.json / M data/sources.json / M entries/batch-02-c.json / M entries/batch-36.json / M site/entries/pedestrian-flow.html / M site/entries/vehicle-flow.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round109.py`——**均为 round109 修复方产物，抽检方仅读取、未据以修改**；抽检方唯一新增为本报告。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `wp-urban-design`（`https://en.wikipedia.org/wiki/Urban_design`）→ `python urllib`（浏览器 UA、SSL 免检）**实抓 HTTP 200**，`<title>=Urban design - Wikipedia`，正文 len=62521。关键词计数：**circulation=0、vehicle=0**、pedestrian=1（列表项「Pedestrian zones」）、traffic=2（「City layouts now revolved around roadways and traffic patterns [citation needed]」）。
  - `wp-wayfinding`（`https://en.wikipedia.org/wiki/Wayfinding`）→ **实抓 HTTP 200**，`<title>=Wayfinding - Wikipedia`，正文 len=20146。关键词计数：wayfinding=74、route=8、directional flow=1（机场「encourage passengers to move along the required directional flow」）、pedestrian=4（「pedestrian wayfinding signage」）、vehicle=1（**仅为比喻「a global vehicle of communication」**）、circulation=0。
  - `db-traffic`（`https://www.designingbuildings.co.uk/wiki/Traffic`）→ **实抓 HTTP 200，但 302 重定向至 `/wiki/Traffic_v_transport`**，`<title>=Traffic v transport - Designing Buildings`（H1「Traffic v transport」，last edited 07 Apr 2022）。正文（逐句）见 1.3。
  - `db-pedestrian`（`https://www.designingbuildings.co.uk/wiki/Pedestrian`）→ **实抓 HTTP 200**，`<title>=Pedestrian - Designing Buildings`（H1「Pedestrian」，last edited 01 Feb 2022）。正文（逐句）见 2.3。
  - 佐证/替代源探针（供处置参考）：`/wiki/Circulation`→**200，title「Circulation - Designing Buildings」，last edited 21 Feb 2025，circulation=24/movement=5**；`/wiki/Designing_for_pedestrians`→**200，title「Designing for pedestrians - Designing Buildings」，last edited 10 Nov 2021，pedestrian=28/vehicle=4**；`/wiki/Pedestrian_circulation`→**404**。详见 3 节处置建议。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`python -m pytest tests -q -p no:cacheprovider`：`19 passed in 0.44s`（PYTEST_EXIT=0）**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存/未落盘）。
- 相似度方法承前轮：`difflib.SequenceMatcher`，去全部空白+小写；口径①短=title+definition+time_or_place+overview；口径②全=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style × expressionism-style` 口径②=0.5157（与 r108 逐位一致，方法正确）。全库 258 条，无重复 id。** 另测「allfields」口径（补入 level/tier/theme/period/region）=0.3829，即任务提示「全字段约 0.37/0.39」可由 0.3748/0.3829 复现。

---

## 一、`vehicle-flow`（车行流线）

### 1.1 当前 entry 实读（`entries/batch-36.json` L6 起）
- `definition`＝「车行动线指机动车、非机动车在场地与建筑中的行驶路径组织。」
- `原理`＝「车辆需要连续、平顺且可识别的路径，转弯半径与出入口位置决定场地内的行驶安全。」
- `典型手法与适用条件`＝「设独立车行道与出入口，按转弯半径与视距布置，末端衔接停车。」
- `overview`＝「车行流线关注转弯半径、会车与停车衔接，避免与人流交叉。」
- `实例`＝「名称：园区车行道与出入口（类型性，不指定具体项目）；以车行路径与出入口组织机动车、非机动车行驶。此处仅列说明，不复制图像。」
- `常见错误与限制`＝「急弯与视线遮挡易致事故；须按规范。实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」**）
- sources = wp-wayfinding / wp-urban-design / db-traffic；`needs_verification=false`、`pending_notes=""`、`待核实=暂无已知待核实项。`、`time_or_place=20世纪、全球（参见来源）。`、`related=[]`（注意：pedestrian-flow 的 related 含 `vehicle-flow`，本条反向为空——非对称，T 小疵）。

### 1.2 definition/原理 两平台核对（实抓引句）
概念拆解：①主体＝**机动车、非机动车**；②范围＝**在场地与建筑中**；③核心＝**行驶路径组织（流线组织）**；④原理细节＝**连续/平顺/可识别的路径 + 转弯半径与出入口位置→行驶安全**。

**wp-urban-design（Wikipedia；en 直连 HTTP200，`<title>=Urban design`）——①②③④均弱/无：**
- 全文 **`circulation`=0、`vehicle`=0**；`pedestrian` 仅 1 处，出现在列举「Urban design considers: **Pedestrian zones** / Incorporation of nature / Aesthetics / Urban structure…」的要点项里——**是「城市设计考虑的事项清单」，非车行流线论述**。
- `traffic` 仅 2 处，唯一有实义的为历史叙述「Car-oriented design impacted the rise of 'urban design'. **City layouts now revolved around roadways and traffic patterns.** [citation needed]」——**泛述城市布局与道路，非「机动车/非机动车在场地与建筑中的行驶路径组织」，且带 citation needed**。
- 结论：`wp-urban-design` 对车行流线概念**无直接论述**（仅主题相邻词）。

**wp-wayfinding（Wikipedia；en 直连 HTTP200，`<title>=Wayfinding`）——主题错位，③④无：**
- 该文主题是**寻路/标识/导航（wayfinding/signage/maps）**：「signage, maps and other cues to help people reach destinations in complex environments」「the process of … locating, following or discovering a **route** through and to a given space」。
- `vehicle`=1 处**仅为比喻**「widespread use as a global **vehicle of communication**」——与「车辆」无关；`circulation`=0。
- 结论：`wp-wayfinding` 论**人如何找到路径/标识**，**不涉及车行路径组织、转弯半径、出入口、视距**。

**db-traffic（Designing Buildings；`/wiki/Traffic` 302→`/wiki/Traffic_v_transport`，HTTP200，H1「Traffic v transport」）——泛述「交通」词义，②③④无：**
- 逐句：「**The definition of traffic is the accumulated vehicles that use infrastructure as a means of travelling from place to place. It could refer to cars moving along roads and highways, aircraft flying in and out of airports, ships moving along charted routes, and so on.**」
- 「**Traffic engineering is the use of engineering techniques to enable easy and safe movement on roadways.**」
- 结论：该页是**「traffic（交通）」的术语定义**——车辆借助基础设施在「地点之间」移动、汽车沿公路行驶；**未涉及「在场地与建筑中的行驶路径组织」，未提「非机动车」，未提「转弯半径 / 出入口 / 视距 / 场地内行驶安全」，也未涉及「流线 / 组织」**。属**泛述交通（词义层）**，非流线组织直证。

| 概念要素 | wp-urban-design | wp-wayfinding | db-traffic（非维基） | 判定 |
| --- | --- | --- | --- | --- |
| ①主体 机动车/非机动车 | ✗（vehicle=0） | ✗（vehicle 仅比喻） | △「vehicles / cars」偏机动车，非机动车未提 | **不成立** |
| ②在场地与建筑中 | ✗ | ✗ | ✗（仅「place to place」在地点间，非场地/建筑内） | **不成立** |
| ③行驶路径组织（流线） | ✗（circulation=0） | ✗（论 route-finding/标识） | ✗（仅 traffic 词义） | **不成立** |
| ④转弯半径/出入口/视距→行驶安全 | ✗ | ✗ | ✗ | **不成立** |

**判定（1.2）：definition/原理 未获「两独立平台」直证。** 两个 Wikipedia 源本身对「车行流线」仅主题相邻（Pedestrian zones 列表项、roadways/traffic patterns 历史句、寻路/标识），而唯一非维基源 `db-traffic` 只是**「traffic」的术语定义（泛述交通）**。四项概念要素（尤其 ②场地/建筑内、③流线组织、④转弯半径/出入口/视距）**无任何来源直接支撑**。因此「两平台（含 DB 非维基）支撑」的成立前提不满足。

### 1.3 ★特别判断：`db-traffic` 是否真支撑「车行流线组织」
**结论：否。DB 页仅泛述「交通（traffic）」词义，未述「车行流线组织」。**
- **对象层级不匹配**：DB 页（实为「Traffic v transport」）通篇是「traffic = 车辆使用基础设施在地点间移动」与「traffic engineering = 使道路通行安全顺畅的工程」的**词义/概览**，属「交通」这一上位词；entry 概念是「机动车、非机动车**在场地与建筑中的**行驶路径**组织**」，是**具体到场地/建筑的流线设计**。
- **关键要素缺项**：②场地与建筑内 ✗（原文是 place to place / roads and highways）、③组织/流线 ✗、④转弯半径/出入口/视距 ✗；「非机动车」全无。
- **不是「直接定义该概念」，而只是关键词（traffic≈车流）表层命中**，与第 89 轮所纠的「泛援」同类。**故不能作为「车行流线组织」的第二平台直证。**
- **附（源数据小疵）**：sources.json 记 `title="Traffic — Designing Buildings"`，但实际页 H1/`<title>` 为「**Traffic v transport**」（`/wiki/Traffic` 302 跳转）。标题记录与实名页不符（T，Minor；不影响词义，但核验口径应记为「Traffic v transport」）。

### 1.4 是否编造
- definition/原理**不是凭空杜撰的假事实**（车行流线确需连续平顺路径、转弯半径、出入口与视距——属通行专业常理）；但**这些具体判断在所列三源中均无可逐句溯源之处**（wp-urban-design 无 vehicle/circulation，wp-wayfinding 论标识，db-traffic 仅 traffic 词义）。按本项目 D10「关键事实双源或标待核实」，**未获源证的具体主张不应以 nv=false 呈现**。**结论：非虚构杜撰，但缺直接可溯源支撑，属「未验证」。**

### 1.5 类型性实例合理性
- 实例已改为「园区车行道与出入口（类型性，不指定具体项目）；以车行路径与出入口组织机动车、非机动车行驶」——**类型性实例合理、不依赖未核的具体项目/设计者/年代，无侵权/无未核事实风险**。✓（此点与 r108 rule-of-thirds 改类型性同理。）
- 但须如实指出：**类型性实例只解决了原 pending「具体实例待补充独立来源」，并不提供 definition/原理 的源证**——「待核实」由「缺具体实例」改成「暂无」，**同时把 nv 置 false，掩盖了「概念支撑本身薄弱」的问题**（见 1.2/1.3）。

### 1.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | 形式 ✓ |
| entry.pending_notes | "" | 形式 ✓ |
| sections.待核实 | 「暂无已知待核实项。」 | 形式 ✓ |
| coverage.needs_verification_count | 0（status 已写 / source_count 3 / L2 / 2026-11-24） | 形式 ✓ |
| time_or_place | 「20世纪、全球（参见来源）。」无「待核实」 | 形式 ✓ |
- **形式五处一致 ✓，check.py PASS；但内容前提（两独立平台直证概念）不成立（见 1.2/1.3）→ nv=false 实质不成立。**

### 1.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节（definition+原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | 实读 sections 6 节齐备且非空 + definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | check.py `validate_svg` 通过（PASS 0 errors）；逐元素（polyline 120,300→300,220→480,260→640,170；circle cx300cy220 r12、cx480cy260 r12、cx40cy60 r5；text x300y375、x40y40）均落框内 | ✓ |
| SVG 外链 | 无 `<image>/<script>/<iframe>/href=/url(`（forbidden=[]） | ✓ |
| SVG 注记 | 含「示意图，非施工图」（figcaption 亦「图 1：示意图，非施工图」） | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求」在，**entry 句末缺「。」**（`常见错误与限制` 以「要求」收尾；site 页脚 note 处带「。」）——同 r101–r108 T 小疵 | ✓（T 小疵） |
| site 与 JSON 一致 | `site/entries/vehicle-flow.html`：title/lead(=overview)/核心定义/原理/典型手法/实例/常见错误 逐句包含 True；JSON 的 `<svg>` 串 `in site=True`；源三行（Wayfinding/Urban design/Traffic — Designing Buildings）一致 | ✓ |

### 1.8 相似度（阈值 0.54）与 def≠原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| vehicle-flow | 短① | pedestrian-flow | 0.4328 | ✓ <0.54 |
| vehicle-flow | 全② | pedestrian-flow | 0.3748 | ✓ <0.54 |
| vehicle-flow × pedestrian-flow | 短①/全② | — | 0.4328 / 0.3748（allfields 0.3829） | ✓ 非重复条目（与任务「约0.37/0.39」量级一致） |
| def×原理（去重） | — | — | 0.2424 | ✓ 两层次可分 |
- 全库最大：短 0.4960（serial-route×radial-route）、全 0.5256（spatial-sequence×atrium-architecture）——**均 <0.54 ✓**；方法自校 0.5157 ✓；258 条无重复 id。**相似度非本条问题。**

### 1.9 条目1 结论
**`vehicle-flow`（车行流线）——不合格（本轮 nv=false 升级依据不成立；应回退为待核实）。**
- 依据：definition 四项要素（①机动车/非机动车 ②在场地与建筑中 ③行驶路径组织 ④转弯半径/出入口/视距→行驶安全）**未被任何来源「两平台直证」**——`wp-urban-design` 无 circulation/vehicle（仅「Pedestrian zones」列表项与 roadways/traffic patterns 历史句，带 citation needed），`wp-wayfinding` 论寻路/标识（vehicle 仅比喻），★特别判断 `db-traffic`（`/wiki/Traffic`→`Traffic v transport`）**仅泛述「traffic＝车辆在地点间沿道路移动」的词义，未述「场地/建筑内的行驶路径组织」，缺非机动车、缺转弯半径/出入口/视距/组织**——不构成第二平台直证。**「两平台支撑」前提不成立 → nv=false 实质不成立**（内容非杜撰，但缺直接可溯源支撑，按 D10 应标待核实）。
- 通过项：类型性实例合理；七节 / SVG（无越界、无外链、含示意图注记）/ site 与 JSON 一致；相似度短 0.4328、全 0.3748、def×原理 0.2424 均 <0.54；check.py PASS、pytest 19 passed、方法自校 0.5157。
- **T（Minor）**：①`常见错误与限制` 规范句句末缺「。」；②sources.json 中 `db-traffic` 标题记为「Traffic — Designing Buildings」，实际页为「Traffic v transport」（302 跳转）；③`related=[]` 与 pedestrian-flow 反向引用不对称。
- **处置建议**：回退 `needs_verification=true` 并恢复「车行流线组织缺直接来源」的待核实说明；或换用真正述及 circulation/车行组织的第二平台源（见 3 节）。

---

## 二、`pedestrian-flow`（人行流线）

### 2.1 当前 entry 实读（`entries/batch-02-c.json` L40 起）
- `definition`＝「以步行者移动与停留为核心组织的流线。」
- `原理`＝「步行流线以人的通行与停留组织空间，关注安全、舒适与节点停顿，而非单纯通行效率。」
- `典型手法与适用条件`＝「区分快行与慢行、设置停留节点；适用于街道、广场与商业空间。」
- `overview`＝「步行流线关注安全、舒适与节点停顿，而非单纯通行效率。」
- `实例`＝「名称：商业步行街流线（类型性，不指定具体项目）；以步行者的移动与停留组织空间。此处仅列说明，不复制图像。」
- `常见错误与限制`＝「人车混行与断头路会降低体验与安全；无障碍与铺装须达标。实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」**）
- sources = wp-wayfinding / wp-urban-design / db-pedestrian；`needs_verification=false`、`pending_notes=""`、`待核实=暂无已知待核实项。`、`time_or_place=跨时期、全球（参见来源）。`、`related=['vehicle-flow']`。

### 2.2 definition/原理 两平台核对（实抓引句）
概念拆解：①主体＝**步行者**；②核心＝**移动与停留**；③核心＝**以之组织流线的组织**；④原理细节＝**安全/舒适/节点停顿，非单纯通行效率**。

**wp-urban-design（Wikipedia；HTTP200）——仅①主题相邻，②③④无：**
- 同上：`circulation`=0、`vehicle`=0、`pedestrian`=1（仅列表项「**Pedestrian zones**」）。**未论步行者「移动与停留」，未论流线组织、节点停顿、舒适。**
- 结论：仅「Pedestrian zones」一词主题相邻。

**wp-wayfinding（Wikipedia；HTTP200）——主题错位，②③④无：**
- 论寻路/标识；`pedestrian`=4（「pedestrian wayfinding signage」）、`directional flow`=1（机场「encourage passengers to move along the required directional flow」）——**是「标识引导人流」，非「以步行者移动与停留组织的流线」，未及「停留/节点/舒适」。**
- 结论：主题错位。

**db-pedestrian（Designing Buildings；`/wiki/Pedestrian`，HTTP200，H1「Pedestrian」）——泛述「行人」词义，②③④无：**
- 逐句：「**The term pedestrian refers to a person travelling on foot, generally on a road or pavement. This can include people that are walking or running. The term pedestrianised refers to an area (typically a street) that has been adapted so it is only used by pedestrians and not motor vehicles.**」其后是「About pedestrians include: Cycling and walking plan / Dedicated pedestrian crossing / Designing for pedestrians / Pedestrian desire-line / Pedestrian precincts / Pedestrian priority street / Pedestrian shed / Pedestrian zone …」的**相关文章列表**。
- 结论：该页是**「pedestrian（行人）」的术语定义**——步行/奔跑的人、步行化区域；**未涉「以移动与停留组织流线」，未提「停留 / 节点 / 舒适 / 流线」**。属**泛述行人（词义层）**，非步行流线直证。

| 概念要素 | wp-urban-design | wp-wayfinding | db-pedestrian（非维基） | 判定 |
| --- | --- | --- | --- | --- |
| ①主体 步行者 | △ 仅「Pedestrian zones」 | ✓ 标识面向行人 | ✓「person travelling on foot / walking or running」 | **仅术语层，非概念** |
| ②移动与停留 | ✗ | ✗（仅 directional flow 引导） | △ 有「walking or running（移动）」，「停留」无 | **不成立** |
| ③以之组织流线（组织） | ✗ | ✗ | ✗（无「流线/组织」） | **不成立** |
| ④安全/舒适/节点停顿/非单纯效率 | ✗ | ✗ | ✗ | **不成立** |

**判定（2.2）：definition/原理 未获「两独立平台」直证。** 两个 Wikipedia 源仅主题相邻（Pedestrian zones 列表项、行人标识），唯一非维基源 `db-pedestrian` 只是**「pedestrian」的术语定义（泛述行人）**。概念要素 ②移动与停留、③以之组织流线、④安全/舒适/节点停顿**无来源直接支撑**。「两平台（含 DB 非维基）支撑」前提不满足。

### 2.3 ★特别判断：`db-pedestrian` 是否真支撑「步行流线组织」
**结论：否。DB 页仅泛述「行人（pedestrian）」词义，未述「步行流线组织」。**
- **对象层级不匹配**：DB 页是「pedestrian = 步行/奔跑的人」「pedestrianised = 仅供行人、禁机动车的区域」的**词义定义** + 相关文章清单；entry 概念是「**以步行者移动与停留为核心组织**的流线」，是**把行人移动组织成流线的设计命题**。
- **关键要素缺项**：②「停留」✗（原文只有 walking or running 的「移动」，无「停留/逗留」）、③组织/流线 ✗、④安全/舒适/节点停顿/非单纯通行效率 ✗。
- **只是「pedestrian≈步行」的表层关键词命中**（与第 89 轮所纠「泛援」同类），**不能作为「步行流线组织」的第二平台直证。**

### 2.4 是否编造
- definition/原理**非虚构建构**（步行流线确关注通行与停留、安全舒适、节点——属设计常理）；但**具体主张在所列三源中无可逐句溯源**（wp-urban-design 无 circulation、wp-wayfinding 论标识、db-pedestrian 仅 pedestrian 词义）。按 D10，**未获源证的具体主张不应以 nv=false 呈现**。**结论：非杜撰，但缺直接可溯源支撑，属「未验证」。**

### 2.5 类型性实例合理性
- 实例「商业步行街流线（类型性，不指定具体项目）；以步行者的移动与停留组织空间」——**类型性实例合理、不依赖未核的具体街道/设计者/年代，无未核事实风险。** ✓
- 同 1.5：**类型性实例只解决原 pending「具体实例待补充」，不提供概念源证**；把 nv 置 false 与「概念支撑薄弱」事实不符。

### 2.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | 形式 ✓ |
| entry.pending_notes | "" | 形式 ✓ |
| sections.待核实 | 「暂无已知待核实项。」 | 形式 ✓ |
| coverage.needs_verification_count | 0（status 已写 / source_count 3 / L2 / 2026-11-24） | 形式 ✓ |
| time_or_place | 「跨时期、全球（参见来源）。」无「待核实」 | 形式 ✓ |
- **形式五处一致 ✓，check.py PASS；但内容前提（两独立平台直证概念）不成立（见 2.2/2.3）→ nv=false 实质不成立。**

### 2.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节 | sections 6 节齐备且非空 + definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | check.py 通过；逐元素（rect 80–680/90–320；polyline 120,300→260,240→380,260→520,180→640,200；circle cx380cy260 r12；text x300y130、x300y375）均落框内 | ✓ |
| SVG 外链 | forbidden=[]（无 `<image>/<script>/<iframe>/href=/url(`） | ✓ |
| SVG 注记 | 含「示意图，非施工图」（figcaption「图 1：示意图，非施工图」） | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求」在，**entry 句末缺「。」**（`常见错误与限制` 以「要求」收尾；site 页脚 note 处带「。」）——同 r101–r108 T 小疵 | ✓（T 小疵） |
| site 与 JSON 一致 | `site/entries/pedestrian-flow.html`：title/lead(=overview)/核心定义/原理/典型手法/实例/常见错误 逐句包含 True；JSON `<svg>` 串 `in site=True`；源三行一致 | ✓ |

### 2.8 相似度（阈值 0.54）与 def≠原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| pedestrian-flow | 短① | vehicle-flow | 0.4328 | ✓ <0.54 |
| pedestrian-flow | 全② | wind-driven-ventilation | 0.3804 | ✓ <0.54 |
| pedestrian-flow × vehicle-flow | 短①/全② | — | 0.4328 / 0.3748 | ✓ 非重复条目 |
| def×原理（去重） | — | — | 0.2807 | ✓ 两层次可分 |
- 全库最大：短 0.4960、全 0.5256——**均 <0.54 ✓**；方法自校 0.5157 ✓；258 条无重复 id。**相似度非本条问题。**

### 2.9 条目2 结论
**`pedestrian-flow`（人行流线）——不合格（本轮 nv=false 升级依据不成立；应回退为待核实）。**
- 依据：definition 要素（①步行者 ②移动与停留 ③以之组织流线 ④安全/舒适/节点停顿）**未被任何来源「两平台直证」**——`wp-urban-design` 仅「Pedestrian zones」列表项，`wp-wayfinding` 论标识/寻路（仅 directional flow 引导），★特别判断 `db-pedestrian`（`/wiki/Pedestrian`）**仅泛述「pedestrian＝步行/奔跑的人、pedestrianised＝仅行人的区域」的词义，未述「以移动与停留组织的流线」，缺停留/节点/舒适/组织**——不构成第二平台直证。**「两平台支撑」前提不成立 → nv=false 实质不成立**（非杜撰，但缺直接可溯源支撑，按 D10 应标待核实）。
- 通过项：类型性实例合理；七节 / SVG / site 一致；相似度短 0.4328、全 0.3804、def×原理 0.2807 均 <0.54；check.py PASS、pytest 19 passed、方法自校 0.5157。
- **T（Minor）**：`常见错误与限制` 规范句句末缺「。」。
- **处置建议**：回退 `needs_verification=true` 并恢复对「步行流线组织」缺直接来源的待核实说明；或换用真正述及 circulation/步行组织的第二平台源（见 3 节）。

---

## 三、处置建议（可用的第二平台候选，本轮仅探针实证，未写入任何数据）

探测结果（本轮实抓）表明 DB 站上存在**比泛义「Traffic / Pedestrian」更贴合「流线组织」**的页面，供返工时换源：

- **`db-circulation`（`/wiki/Circulation`，HTTP200，title「Circulation - Designing Buildings」，last edited 21 Feb 2025；circulation=24/movement=5）**：逐句「The word 'circulation' refers to movement around something… In the built environment, this generally relates to the **movement of people, typically within a building**」「circulation spaces… entrances, foyers and lobbies, corridors, stairs, lifts, landings…」「**Alternative circulation routes** may be provided for different functions, such as public access, private access, the movement of goods, exit, escape… hospitals and airports… circulation requirements… kept entirely separate」「The design of circulation may be based on the required route, type of circulation, number of people… distance, direction (horizontal or vertical)…」「Where circulation has been poorly designed, this can cause conflicts, confusion…」——**直接论述「circulation（流线）/circulation spaces/circulation routes」的组织**，对 `pedestrian-flow`（人在建筑内的移动与流线、路线冲突）是**真正的第二平台直证**；对 `vehicle-flow` 只部分（movement of goods/路线），车辆专项仍偏弱。
- **`/wiki/Designing_for_pedestrians`（HTTP200，title「Designing for pedestrians - Designing Buildings」，ICE 主笔，last edited 10 Nov 2021；pedestrian=28/vehicle=4）**：论「pedestrian characteristics and practical design」「Engineering pedestrian facilities」「encouraging people to walk」，可作 `pedestrian-flow` 的补充平台（但重心偏行人设施/安全，非纯「流线组织」）。
- **`/wiki/Pedestrian_circulation`=404**（不存在）。
- 建议：`pedestrian-flow` 优先换 `db-circulation`（必要时叠加 `Designing_for_pedestrians`）；`vehicle-flow` 需另找**真正论述「车辆/场地内车行 circulation」**的来源（如 site access / vehicle movement 专项），现用泛义 `Traffic` 不足以支撑「场地与建筑中的行驶路径组织」。若一时无合适第二平台，**据实回退待核实、不降标准**（符合 D10 与既往「探测不到即据实保留」惯例）。

---

## 四、机器可读汇总

```
ROUND=109
SAMPLER=spotcheck-r109
SCOPE=["vehicle-flow","pedestrian-flow"]
READONLY="only wrote research/spotcheck-round109.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={
 "wp-urban-design":"en.wikipedia 200 '<title>=Urban design - Wikipedia' len=62521; count: circulation=0 vehicle=0 pedestrian=1('Pedestrian zones' bullet) traffic=2('City layouts ... roadways and traffic patterns'[citation needed])",
 "wp-wayfinding":"en.wikipedia 200 '<title>=Wayfinding - Wikipedia' len=20146; about wayfinding/signage/maps/route; directional flow=1(airport passengers); vehicle=1(metaphor 'vehicle of communication'); circulation=0",
 "db-traffic":"/wiki/Traffic 302-> /wiki/Traffic_v_transport 200 '<title>=Traffic v transport - Designing Buildings' last edited 07 Apr 2022; 'definition of traffic is the accumulated vehicles that use infrastructure ... cars moving along roads and highways ... ships ...'; 'traffic engineering ... easy and safe movement on roadways'",
 "db-pedestrian":"/wiki/Pedestrian 200 '<title>=Pedestrian - Designing Buildings' last edited 01 Feb 2022; 'pedestrian refers to a person travelling on foot ... walking or running. pedestrianised refers to an area ... only used by pedestrians and not motor vehicles' + related-articles list",
 "probe_db-circulation":"/wiki/Circulation 200 'Circulation - Designing Buildings' last edited 21 Feb 2025; circulation=24 movement=5; 'movement of people, typically within a building'; 'circulation spaces ... corridors ...'; 'alternative circulation routes ... hospitals and airports'",
 "probe_designing-for-pedestrians":"/wiki/Designing_for_pedestrians 200 last edited 10 Nov 2021; pedestrian=28 vehicle=4; pedestrian characteristics/facilities/encourage walking",
 "probe_pedestrian-circulation":"/wiki/Pedestrian_circulation 404"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest":"19 passed (EXIT=0)"}
METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258,"dup_ids":0}
GLOBAL_MAX={"short":["serial-route","radial-route",0.4960],"full":["spatial-sequence","atrium-architecture",0.5256]}

VEHICLE_FLOW={
 "verdict":"不合格(本轮nv=false升级依据不成立;应回退待核实)",
 "definition":"车行动线指机动车、非机动车在场地与建筑中的行驶路径组织。",
 "principle":"车辆需要连续、平顺且可识别的路径，转弯半径与出入口位置决定场地内的行驶安全。",
 "sources":["wp-wayfinding","wp-urban-design","db-traffic"],
 "concept_dual_source":{
   "subject_motor_nonmotor":"wp-urban-design vehicle=0 / wp-wayfinding vehicle=metaphor / db-traffic 'vehicles/cars'(non-motor missing) -> NOT-ESTABLISHED",
   "in_site_and_building":"all three: NOT-ESTABLISHED (db 'place to place/roads', not site/building)",
   "driving_path_organization":"wp-urban-design circulation=0 / wp-wayfinding route-finding / db-traffic traffic-word-sense -> NOT-ESTABLISHED",
   "turning_radius_entrances_sight_distance":"none of three sources -> NOT-ESTABLISHED",
   "holds_two_platform_for_concept":false},
 "db_traffic_direct_vs_generic":"GENERIC-ONLY: /wiki/Traffic 302->Traffic_v_transport; defines 'traffic = accumulated vehicles using infrastructure... cars along roads/highways'; does NOT cover 场地/建筑内行驶路径组织/非机动车/转弯半径/出入口/视距 -> term-level adjacency, not flow-line organization",
 "fabrication":"not fabricated fiction, but specific definition/principle claims NOT quote-traceable to any of the 3 sources -> unverified per D10",
 "instance":"园区车行道与出入口(类型性,不指定具体项目) -- reasonable type-level instance",
 "type_instance_ok":true,
 "nv_false_form":"four/five-place consistent formally (nv=false/pending=''/待核实=暂无/coverage nv_count=0/time_or_place clean); but substantive premise (two-platform direct support) FALSE -> nv=false invalid",
 "structure":{"seven_sections":true,"sections_with_def":7,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"pedestrian-flow 0.4328","nearest_full":"pedestrian-flow 0.3748","allfields_x_pedestrian":0.3829,"def_vs_principle":0.2424,"lt_0.54":true},
 "transparency":["T1: db-traffic 标题记 'Traffic — Designing Buildings' 实为 'Traffic v transport'(302).","T2: 常见错误与限制 规范句句末缺「。」","T3: related=[] 与 pedestrian-flow 反向引用不对称"]}

PEDESTRIAN_FLOW={
 "verdict":"不合格(本轮nv=false升级依据不成立;应回退待核实)",
 "definition":"以步行者移动与停留为核心组织的流线。",
 "principle":"步行流线以人的通行与停留组织空间，关注安全、舒适与节点停顿，而非单纯通行效率。",
 "sources":["wp-wayfinding","wp-urban-design","db-pedestrian"],
 "concept_dual_source":{
   "subject_pedestrian":"db-pedestrian 'person travelling on foot'(term) / wp-urban-design 'Pedestrian zones'(bullet) / wp-wayfinding signage -> TERM-LEVEL only",
   "movement_and_stay":"db-pedestrian 'walking or running'(move) but 'stay' absent; wp sources not on stay -> NOT-ESTABLISHED",
   "organize_into_flow":"db-pedestrian no 流线/organization; wp sources no -> NOT-ESTABLISHED",
   "safety_comfort_node_pause":"none of three sources -> NOT-ESTABLISHED",
   "holds_two_platform_for_concept":false},
 "db_pedestrian_direct_vs_generic":"GENERIC-ONLY: /wiki/Pedestrian defines 'pedestrian = person on foot/walking or running; pedestrianised = only pedestrians not motor vehicles' + related-article list; does NOT cover 移动与停留组织/停留/节点/舒适 -> term-level adjacency, not pedestrian flow-line organization",
 "fabrication":"not fabricated fiction, but specific definition/principle claims NOT quote-traceable to any of the 3 sources -> unverified per D10",
 "instance":"商业步行街流线(类型性,不指定具体项目) -- reasonable type-level instance",
 "type_instance_ok":true,
 "nv_false_form":"four/five-place consistent formally; substantive premise (two-platform direct support) FALSE -> nv=false invalid",
 "structure":{"seven_sections":true,"sections_with_def":7,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"vehicle-flow 0.4328","nearest_full":"wind-driven-ventilation 0.3804","def_vs_principle":0.2807,"lt_0.54":true},
 "transparency":["T: 常见错误与限制 规范句句末缺「。」"]}

VERDICT={"vehicle-flow":"不合格(nv=false依据不成立: wp-urban-design circulation=0/vehicle=0, wp-wayfinding论标识vehicle仅比喻, ★db-traffic只泛述traffic词义'车辆沿道路地点间移动'未述场地/建筑内行驶路径组织、无非机动车/转弯半径/出入口/视距; 应回退待核实. 结构/相似度/类型实例/七节/SVG/site均通过; T:规范句缺句号+db-traffic标题不符+related不对称)","pedestrian-flow":"不合格(nv=false依据不成立: wp-urban-design仅Pedestrian zones列表项, wp-wayfinding论标识, ★db-pedestrian只泛述pedestrian词义'步行/奔跑的人;pedestrianised仅行人区域'未述移动与停留组织的流线、无停留/节点/舒适; 应回退待核实. 结构/相似度/类型实例/七节/SVG/site均通过; T:规范句缺句号)"}
KEY_FINDING="两条本轮仅把'缺具体实例'改成类型性实例(合理)、新增DB泛义源(traffic/pedestrian词义定义)、并把nv置false; 但★特别判断: db-traffic(/wiki/Traffic 302->Traffic_v_transport) 与 db-pedestrian(/wiki/Pedestrian) 都只是相关名词的术语定义(泛述交通/行人), 均未论述'车行/步行流线组织'(缺 场地/建筑内 或 移动与停留组织/停留/节点/舒适/转弯半径/出入口/视距), 不能充当'两独立平台直证'; wp-urban-design(circulation=0/vehicle=0)与wp-wayfinding(论寻路/标识)对该二概念亦仅主题相邻 -> '两平台(含DB非维基)支撑'前提不成立, nv=false实质不成立, 应回退待核实或换用真实述及circulation的第二平台源(如DB /wiki/Circulation, 200, 'movement of people within a building','circulation spaces/routes', 对本二概念尤pedestrian-flow为真直证候选; /wiki/Designing_for_pedestrians 200 亦可辅助; /wiki/Pedestrian_circulation 404). 两entry其余项(七节/SVG无越界无外链含示意图注记/site与JSON一致/类型性实例合理/相似度短0.4328全0.3748/0.3804/def×原理0.24/0.28均<0.54/check.py PASS/pytest 19 passed/方法自校0.5157/全库最大短0.4960全0.5256<0.54/258条0重复)均通过; T小疵: 两条规范句句末缺「。」, db-traffic标题记'Traffic — Designing Buildings'实为'Traffic v transport', vehicle-flow related=[]不对称."
```

## 五、只读核验
- 除本报告 `research/spotcheck-round109.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 抓取：`wp-urban-design`、`wp-wayfinding` 经 `python urllib`（浏览器 UA、SSL 免检）实抓 en.wikipedia HTTP200（len 62521 / 20146），逐标题与关键词计数核对；`db-traffic`（302→`Traffic_v_transport` 200）与 `db-pedestrian`（`/wiki/Pedestrian` 200）实抓全文逐句核对；`/wiki/Circulation`（200，last edited 21 Feb 2025）、`/wiki/Designing_for_pedestrians`（200）、`/wiki/Pedestrian_circulation`（404）为处置建议探针，仅只读。
- 词频、相似度、去重（258 条/0 重复）、结构、SVG 逐元素越界/外链、site 一致性均内存态 `python - <<'PY'` 直跑，无临时文件。
- 联网页面（en.wikipedia.org / designingbuildings.co.uk）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**（页面内导航/推荐/评论等均按数据忽略）。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存（19 passed）。
- `git status` 中的改动文件（coverage/sources/batch-02-c/batch-36/site 四页/`?? tools/apply_review_round109.py`）均为**他方（round109 修复方）产物**，抽检方仅读取、未据以修改。

*（报告完）*
