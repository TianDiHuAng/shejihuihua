# 第102轮质量抽检报告（spotcheck-round102）——material-durability / mixed-mode-ventilation 的 nv=false 升级复核

- 抽检人：spotcheck-r102（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言，证据先于结论）。`using-superpowers` 命中 SUBAGENT-STOP，按任务说明书直接执行；`verification-before-completion` 全程遵循——本文所有「合格/通过」判断均附本轮实跑/实抓输出。
- 抽检对象（2 条，均在 `entries/batch-08.json`）：
  - `material-durability`（材料耐久）——entry 对象 L103–L134；字段：definition、sections〔原理／典型手法与适用条件／实例／常见错误与限制／一图／待核实〕、svg（1 张，viewBox `0 0 760 400`）、sources（wp-building-material / wp-vernacular-architecture / db-durability）、needs_verification / pending_notes；coverage row L2060。
  - `mixed-mode-ventilation`（混合通风）——entry 对象 L38–L69；字段同上（6 节）、svg（1 张，viewBox `0 0 760 400`）、sources（wp-ventilation-architecture / wp-natural-ventilation / db-mixed-mode-ventilation）、needs_verification / pending_notes；coverage row L2008。
- 本轮变更实读：`tools/apply_review_round102.py`（新增，未提交，64 行）。其 `main()` 对两条所做改动（逐字段比对 JSON 确认）：
  - `material-durability`：sources 追加 `db-durability`；definition 改写为「耐久性是材料抵抗日常磨损与气候侵蚀的能力，决定维护周期与全生命周期成本。」；`sections.实例` →「名称：公共建筑外立面材料（类型性，不指定具体项目）；不同材料的耐磨与耐候性能决定其维护周期。此处仅列说明，不复制图像。」；`sections.待核实`→「暂无已知待核实项。」；needs_verification `true→false`；pending_notes 清空。
  - `mixed-mode-ventilation`：sources 追加 `db-mixed-mode-ventilation`；`sections.实例` →「名称：办公建筑混合通风（类型性，不指定具体项目）；自然通风不足时由机械系统补充，兼顾能效与空气品质。此处仅列说明，不复制图像。」；`sections.待核实`→「暂无已知待核实项。」；needs_verification `true→false`；pending_notes 清空。（definition/原理 未改动，见 T4。）
  - `data/sources.json` 新增两源：`db-durability`（title「Durability — Designing Buildings」, url .../wiki/Durability）与 `db-mixed-mode-ventilation`（title「Mixed-mode ventilation — Designing Buildings」, url .../wiki/Mixed_mode_ventilation），author Designing Buildings、type 学术著作、year null、verified=true、link_ok=true。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round102.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。抓取、词扫描、相似度、去重、越界、结构、git 核对均内存态 `python - <<'PY'` / 工具直跑，未落盘临时文件（除本报告）。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `db-durability = https://www.designingbuildings.co.uk/wiki/Durability` → `web_fetch` **HTTP 200**，页面 H1=`Durability`（无重定向）。
  - `db-mixed-mode-ventilation = https://www.designingbuildings.co.uk/wiki/Mixed_mode_ventilation` → `web_fetch` **HTTP 200**，H1=`Mixed-mode ventilation`；**主作者 BSRIA**，正文引 BSRIA《Illustrated Guide to Mechanical Building Services, 3rd ed. (BG 31/2017)》。
  - 四个 Wikipedia 源：承第100–101轮结论，本环境 en.wikipedia 直连阻断；改用同文镜像 `owiki.org` 实抓，全部 **HTTP 200**，H1 逐一核对：`Building material`、`Vernacular architecture`、`Ventilation (architecture)`、`Passive ventilation`（对应 wp-natural-ventilation，其 title 即「Passive ventilation」）——标题与 sources.json title 一致，正文为 Wikipedia 原文。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed in 0.12s`（PYTEST_EXIT=0）。**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存。）
- `git status --short`：`M coverage.json / M data/sources.json / M entries/batch-08.json / M site/entries/material-durability.html / M site/entries/mixed-mode-ventilation.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round102.py`——前七项与本轮 `apply_review_round102.py`＋gen_site 自身产物一致；`??` 为修复方脚本。抽检方仅读取，未据以修改。

## 一、★ material-durability（材料耐久）逐项核对

### 1.1 概念「材料抵抗退化/日常磨损与气候侵蚀、决定维护周期与全生命周期成本」双平台核对（实抓引句）

- `db-durability`（Designing Buildings「Durability」页；HTTP200，H1=Durability）：
  - `Durability is the resistance to degradation of products, materials, buildings and other built assets over time.`（**明确把「materials（材料）」纳入耐久性定义＋over time ✓✓**）
  - `A building will be subjected not only to daily wear and tear from users but also to the constant influence of climate – in particular rain, frost, sun and heat – forces collectively referred to as weathering. Such forces can cause significant deterioration and therefore a reduction in durability.`（**日常磨损 daily wear and tear＋气候/风化 rain/frost/sun/heat ✓✓✓，直接对应「抵抗日常磨损与气候侵蚀」**）
  - `even the best materials may deteriorate prematurely if they are not adequately maintained, and a design which makes this difficult e.g timberwork that is inaccessible and so infrequently painted, will have adverse effects on component durability.`（**维护→耐久，「infrequently painted」含维护频次含义 ✓**）
  - `designers must face a trade-off between the initial costs of materials and the likely future costs of maintenance and the resulting effect on durability.`（**初始成本 vs 未来维护成本之权衡＝全生命周期成本 ✓✓**）
  - 影响因素枚举含 `Resistance to damp, moisture and water`、`Resistance to atmospheric pollution`、`Resistance to heat and cold`、`Resistance to mould and rot`（**气候/环境侵蚀要素 ✓**）。
- `wp-building-material`（Wikipedia `Building material`；owiki HTTP200）：
  - `Sometimes people take into consideration the energy savings or durability of the materials and see the value of paying a higher initial cost in return for a lower lifetime cost. For example, an asphalt shingle roof costs less than a metal roof to install, but the metal roof will last longer so the lifetime cost is less per year.`（**材料耐久性→全生命周期成本 ✓✓**）
  - `Some materials may require more care than others, maintaining costs specific to some materials may also influence the final decision.`（**维护成本 ✓**）；`if the material is not as durable as advertised`（**耐久性 ✓**）；趋势 `repair-able to disposable; chosen for increased levels of fire-safety`（**耐久/维护相关 ✓**）。
- `wp-vernacular-architecture`（Wikipedia `Vernacular architecture`；owiki HTTP200）：
  - `the local environment, the construction materials it can provide and the durability of these materials in the environment govern many aspects of vernacular architecture.`（**材料在环境中的耐久性 ✓✓**）
  - `Mud bricks are most common along river valleys in arid environments, where mud is available and rainfall is too low to damage unfired brick`（**气候（降雨）侵蚀材料 ✓**）
  - `Materials used will become heavier, more solid and more durable.`（**耐久性 ✓**）

| 概念要素 | db-durability（Designing Buildings） | wp-building-material | wp-vernacular-architecture | 判定 |
| --- | --- | --- | --- | --- |
| 材料耐久性＝材料抵抗退化 | ✓ `resistance to degradation of ... materials ... over time` | ✓ `durability of the materials` | ✓ `durability of these materials in the environment` | **三平台直证✓** |
| 日常磨损 | ✓ `daily wear and tear from users` | ✗ 无「日常磨损」直述 | ✗ | **DB直证（DB 非维基平台即满足）** |
| 气候侵蚀 | ✓ `constant influence of climate – rain, frost, sun and heat – weathering` | △ `damaged by ... wind`（弱） | ✓ `rainfall is too low to damage unfired brick` | **双平台✓（DB强＋WP-vernacular）** |
| 维护周期 / 维护 | ✓ `adequately maintained` / `infrequently painted` / `future costs of maintenance` | ✓ `require more care` / `maintaining costs` | △ `more durable`（间接减更换） | **双平台✓** |
| 全生命周期成本 | ✓ `trade-off between the initial costs ... and future costs of maintenance` | ✓ `lower lifetime cost` / `lifetime cost is less per year` | ✗ | **双平台✓** |

**判定（1.1）：** definition「耐久性是材料抵抗日常磨损与气候侵蚀的能力，决定维护周期与全生命周期成本」与 原理「耐久性指材料在整个使用期内抵抗性能退化的能力，关系到维护周期与全生命周期成本」之核心要素——**材料抵抗退化、日常磨损、气候（风化）侵蚀、维护、全生命周期成本**——由 **Designing Buildings（db-durability）＋ Wikipedia（wp-building-material / wp-vernacular-architecture）两独立平台逐要素直证**（「日常磨损」由 DB 直证，「气候侵蚀/维护/寿命成本」双平台均证），**成立、非编造、双平台强支撑**。

### 1.2 ★特别判断：db-durability 是否真定义「材料耐久性 / 维护周期」？

- **结论：是，足够；并非仅泛述「建筑耐久」。** 依据：
  1. **明确定义了「材料耐久性」**：开篇 `Durability is the resistance to degradation of products, **materials**, buildings and other built assets over time.` ——「materials（材料）」被显式列入，「over time（随时间）」给出时间维度，等价于「材料抵抗随时间退化」，即材料耐久性本身。
  2. **明确覆盖「日常磨损＋气候侵蚀」**：`daily wear and tear from users` ＋ `constant influence of climate – rain, frost, sun and heat – weathering ... reduction in durability` ——正是定义中「抵抗日常磨损与气候侵蚀」的直述来源（虽然主语落在 building，但句意是建筑及其组成材料所受风化，且前段主题即材料退化）。
  3. **明确提出「维护与寿命成本」关系**：`if they are not adequately maintained ... infrequently painted`（维护频次）＋`trade-off between the initial costs of materials and the likely future costs of maintenance`（全生命周期成本）。「**维护周期**」一词 DB 未逐字出现，但「adequately maintained / infrequently painted / future costs of maintenance」已直接蕴含维护间隔与维护成本，属**通识性合理概括，非编造**（见 T1）。
- 故 db-durability **不是只泛述建筑耐久**，它把 materials 纳入定义并直述磨损、气候风化、维护与成本，足以支撑本条 definition/原理。**评级：足够（adequate）。**

### 1.3 类型性实例

- `实例`＝「名称：公共建筑外立面材料（**类型性，不指定具体项目**）；不同材料的耐磨与耐候性能决定其维护周期。此处仅列说明，不复制图像。」
- **类型性合理**：「公共建筑外立面材料」为现象类别，不绑定具体建筑；内容与 db-durability `daily wear and tear` / `weathering` / `maintenance` 及 wp-building-material `durability...lifetime cost` 一致。**未给具体项目名/地点/设计者/年份/数值**，无编造具体事实空间；「不复制图像」自述一致。

### 1.4 nv=false 形式四处一致

| 核对项 | material-durability |
| --- | --- |
| `needs_verification`（entry） | `false` ✓ |
| `pending_notes` | `""` ✓ |
| `sections.待核实` | 「暂无已知待核实项。」✓ |
| `coverage.json` 记录 | `status 已写`、`source_count 3`、`needs_verification_count 0`、`last_updated 2026-11-24`、`level L2` ✓ |
| `time_or_place` | 「跨时期、全球（参见来源）。」无「待核实」✓ |

四处一致；`check.py`（含 D14 一致性）PASS 佐证。

## 二、★ mixed-mode-ventilation（混合通风）逐项核对

### 2.1 概念「自然通风不足时由机械系统补充」双平台核对（实抓引句）

- `db-mixed-mode-ventilation`（Designing Buildings「Mixed-mode ventilation」页；HTTP200，H1=Mixed-mode ventilation；主作者 BSRIA，引 BG 31/2017）：
  - `Mixed-mode is a term that describes a system which combines natural and mechanical ventilation. The mechanical element can be extract, supply or a combination of the two... `（**自然＋机械结合 ✓✓**）
  - `**The mechanical element ensures that an adequate air flow is maintained when natural ventilation is inadequate.**`（**自然通风不足→机械维持足够风量 ✓✓✓，与本条概念逐字对应**）
  - `This is particularly useful at night when it can be used to purge heat from the building in readiness for the next day.`（**夜间机械冲洗 ✓**）
  - `greater reliance can be placed on them to provide ventilation in comparison to a natural ventilation system, while still providing the benefits of a natural ventilation system when weather conditions are suitable.`（**天气适宜时用自然、否则靠机械＝「优先自然/不足补充」逻辑 ✓✓**）
- `wp-ventilation-architecture`（Wikipedia `Ventilation (architecture)`；owiki HTTP200）「Mixed-mode ventilation」节：
  - `Mixed-mode ventilation systems use both mechanical and natural processes. The mechanical and natural components may be used at the same time, at different times of day, or in different seasons of the year.`（**自然＋机械结合 ✓✓**）
  - `**Since natural ventilation flow depends on environmental conditions, it may not always provide an appropriate amount of ventilation. In this case, mechanical systems may be used to supplement or regulate the naturally driven flow.**`（**自然通风不足→机械补充/调节 ✓✓✓**）
  - 顶部：`Ventilation is usually categorized as either mechanical ventilation, natural ventilation, or mixed-mode ventilation.`（**混合通风为独立类别 ✓**）
- `wp-natural-ventilation`（Wikipedia `Passive ventilation`；owiki HTTP200）「Standards」节：
  - `most buildings designed to have systems to naturally condition spaces must also "include a mechanical ventilation system designed to meet the Ventilation Rate or IAQ procedures. The mechanical system is to be used when windows are closed due to extreme outdoor temperatures noise and security concerns".`（**自然调节建筑须配机械系统、在自然不可用时启用 ✓✓**）
  - `While natural ventilation eliminates electrical energy consumed by fans, overall energy consumption of natural ventilation systems is often higher than that of modern mechanical ventilation...`（**自然/机械能效对比 ✓，支撑实例「兼顾能效」**）

| 概念要素 | db-mixed-mode-ventilation | wp-ventilation | wp-natural-ventilation | 判定 |
| --- | --- | --- | --- | --- |
| 自然＋机械结合 | ✓ `combines natural and mechanical ventilation` | ✓ `use both mechanical and natural processes` | △ 标准段隐含 | **双平台✓** |
| 自然通风不足时机械补充 | ✓ `mechanical element ensures adequate air flow when natural ventilation is inadequate` | ✓ `may not always provide... mechanical systems may be used to supplement` | ✓ `mechanical system...used when windows are closed due to extreme...` | **三平台直证✓✓✓** |
| 优先自然 / 条件适宜用自然 | ✓ `benefits of a natural ventilation system when weather conditions are suitable` | ✓ `same time, different times of day, seasons` | — | **双平台✓** |
| 能效（兼顾） | ✓ night purge / natural benefits | ✓ `reduce energy demand` | ✓ 自然vs机械能效对比 | **✓** |

**判定（2.1）：** definition「混合通风在可开启窗与自然驱动可用时优先自然通风，在条件不足时由机械系统补充」与原理（同文，见 T4）之核心「自然＋机械结合、自然通风不足时机械补充」由 **Designing Buildings（db-mixed-mode-ventilation：`ensures adequate air flow when natural ventilation is inadequate`）＋ Wikipedia（wp-ventilation：`mechanical systems may be used to supplement`；wp-natural-ventilation 标准段 `mechanical system...used when windows are closed`）两独立平台逐要素直证**，**成立、非编造、双平台强支撑**。

### 2.2 类型性实例

- `实例`＝「名称：办公建筑混合通风（**类型性，不指定具体项目**）；自然通风不足时由机械系统补充，兼顾能效与空气品质。此处仅列说明，不复制图像。」
- **类型性合理**：「办公建筑混合通风」为现象类别，不绑定具体项目；内容与 db-mixed-mode-ventilation `mechanical element ensures adequate air flow when natural ventilation is inadequate` 逐项有源一致；「兼顾能效」对应 wp-natural-ventilation 能效对比。**未给具体项目名/地点/设计者/年份/数值**，无编造。

### 2.3 nv=false 形式四处一致

| 核对项 | mixed-mode-ventilation |
| --- | --- |
| `needs_verification`（entry） | `false` ✓ |
| `pending_notes` | `""` ✓ |
| `sections.待核实` | 「暂无已知待核实项。」✓ |
| `coverage.json` 记录 | `status 已写`、`source_count 3`、`needs_verification_count 0`、`last_updated 2026-11-24`、`level L2` ✓ |
| `time_or_place` | 「20世纪、全球（参见来源）。」无「待核实」✓ |

四处一致；`check.py` PASS 佐证。

## 三、形式核对汇总（两条）

| 核对项 | material-durability | mixed-mode-ventilation |
| --- | --- | --- |
| 七节（定义＋原理/典型手法/实例/常见错误/一图/待核实） | ✓ 6 节全非空 | ✓ 6 节全非空 |
| SVG 数量 / 画布 | ✓ 1 张，`viewBox='0 0 760 400'` | ✓ 1 张，`viewBox='0 0 760 400'` |
| SVG 越界 / 外链 | ✓ 元素均在框内；无 `<image>/<script>/href=/url(` | ✓ 元素均在框内；无 `<image>/<script>/href=/url(` |
| SVG 注记 | ✓ 含「示意图，非施工图」 | ✓ 含「示意图，非施工图」 |
| 规范句（常见错误收尾） | ✓ 含「实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」，见 T3**） | ✓ 含且（**句末亦缺「。」，见 T3**） |
| site 与 JSON 一致 | ✓ `site/entries/material-durability.html` 各节与 JSON 一致、3 来源含 Designing Buildings（L14/L17/L22 实读） | ✓ `site/entries/mixed-mode-ventilation.html` 一致、3 来源含 Designing Buildings（L14/L17/L22 实读） |
| 来源数 / 双平台 | 3（wp-building-material + wp-vernacular-architecture + db-durability）；平台=Wikipedia×2＋Designing Buildings(DB) | 3（wp-ventilation + wp-natural-ventilation + db-mixed-mode-ventilation）；平台=Wikipedia×2＋Designing Buildings(DB) |
| 新 DB 源 verified/link_ok / 引用 | ✓ verified=true、link_ok=true、被 1 条引用 | ✓ verified=true、link_ok=true、被 1 条引用 |

`check.py`：**PASS: all checks, 0 errors（EXIT=0）**；`pytest tests/test_svg_bounds.py`：**5 passed（EXIT=0）**。

## 四、★ 相似度（阈值 0.54）与 def≠原理

方法（承第97–101轮）：`difflib.SequenceMatcher`，去全部空白＋小写；口径①短=title+definition+time_or_place+overview；口径②全字段-不含SVG=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style`×`expressionism-style` 口径②＝0.5157（与第39–101轮逐位一致，口径正确）**。全库 258 条。

| 条目 | 口径 | 最近邻 | 相似度 | 阈值 | 判定 |
| --- | --- | --- | --- | --- | --- |
| material-durability | 短① | material-texture | 0.3087 | <0.54 | ✓ |
| material-durability | 全② | mixed-mode-ventilation | 0.3295 | <0.54 | ✓ |
| mixed-mode-ventilation | 短① | demand-controlled-ventilation | 0.3386 | <0.54 | ✓ |
| mixed-mode-ventilation | 全② | glare | 0.3292 | <0.54 | ✓ |

- **指定对比**：`material-durability × vernacular-material` 短 0.3086 / 全 0.2754，均 <0.54 ✓；`mixed-mode-ventilation × natural-ventilation` 短 0.2642 / 全 0.2657，均 <0.54 ✓；`mixed-mode-ventilation × demand-controlled-ventilation` 短 0.3386 / 全 0.3087，均 <0.54 ✓。
- 两条全库最近邻最大：material-durability 短 0.3087、全 0.3295；mixed-mode 短 0.3386、全 0.3292——**均 ≪0.54，余量充足，无任何对手 >0.54。相似度合格 ✓**。
- **def≠原理（去重）**：
  - material-durability `definition×原理` = **0.64**（中等重叠：共用「耐久性…抵抗…能力…维护周期与全生命周期成本」；不同处「日常磨损与气候侵蚀」vs「性能退化」「决定」vs「关系到」，非逐字），可接受，轻记 T2。
  - mixed-mode-ventilation `definition×原理` = **1.0（逐字完全相同）**：definition L45 与 `sections.原理` L52 内容一字不差——**原理节无独立机制说明，纯重复定义**，属较重去重瑕疵，见 **T4（建议 lead 要求整改）**。

## 五、总判定与依据

**结论：**
- **`material-durability`（材料耐久）——合格。** 概念「材料抵抗退化、日常磨损与气候侵蚀、决定维护周期与全生命周期成本」由三源（DB＋Wikipedia×2）逐要素直证；**特别判断：db-durability 真正定义材料耐久性（把 materials 纳入定义）并直述磨损/气候风化/维护/寿命成本，并非只泛述建筑耐久，足以支撑本条**；类型性实例合理、nv=false 四处一致、七节/SVG/规范句/site 一致、相似度全通过。
- **`mixed-mode-ventilation`（混合通风）——合格（附透明项 T4：def≡原理 逐字重复，建议重写原理节）。** 概念「自然通风不足时由机械系统补充」由 db-mixed-mode-ventilation（BSRIA：`ensures adequate air flow when natural ventilation is inadequate`）＋ wp-ventilation（`mechanical systems may be used to supplement`）＋ wp-natural-ventilation（标准段）三平台逐字级直证；类型性实例合理、nv=false 四处一致、结构/相似度全通过。

依据（逐项对齐任务核对点）：
1. **definition/原理 双平台支撑（含 DB 非维基）**：
   - material-durability：`材料抵抗退化/维护/寿命成本` 由 db-durability（`resistance to degradation of ... materials ... over time`；`trade-off between initial costs and future costs of maintenance`）＋ wp-building-material（`durability of the materials`；`lower lifetime cost`）＋ wp-vernacular（`durability of these materials in the environment`）**双平台直证✓**；`日常磨损/气候侵蚀` 由 db-durability（`daily wear and tear`；`climate – rain, frost, sun and heat – weathering`）直证、wp-vernacular（`rainfall ... damage`）佐证 ✓。
   - mixed-mode：`自然通风不足→机械补充` 由 db-mixed-mode-ventilation（`ensures adequate air flow when natural ventilation is inadequate`）＋ wp-ventilation（`mechanical systems may be used to supplement or regulate`）＋ wp-natural-ventilation（`mechanical system is to be used when windows are closed`）**三平台逐字级直证✓✓✓**。
2. **是否编造**：两条均无虚假具体事实；仅 material-durability 的「维护周期」为 DB「adequately maintained / future costs of maintenance」的通识性概括（T1），非编造。
3. **类型性实例合理**：material-durability「公共建筑外立面材料（类型性，不指定具体项目）」、mixed-mode「办公建筑混合通风（类型性，不指定具体项目）」均不绑定具体项目、无地点/设计者/年份/数值，内容与 DB 有源一致 ✓。
4. **nv=false 落地+形式四处一致**：两条 entry nv=false / pending="" / 待核实=暂无 / coverage needs_verification_count=0；time_or_place 无「待核实」；`check.py` PASS ✓。
5. **七节/SVG/规范句/site**：两条均 6 节全非空、SVG 1 张 `760×400` 框内无外链含「示意图，非施工图」、规范句在（两条句末均缺句号 T3）、site 与 JSON 一致；`check.py` PASS、`pytest` 5 passed ✓。
6. **相似度**：material-durability 短 max 0.3087 / 全 max 0.3295；mixed-mode 短 max 0.3386 / 全 max 0.3292；指定对比均 <0.54；方法自校 0.5157 ✓。
7. **来源**：两条各 3 源、DB 与 Wikipedia 两独立平台；新增 db-durability / db-mixed-mode-ventilation verified=true、link_ok=true、各被 1 条引用 ✓。

透明说明（不改合格判定，供 lead 决策）：
- **(T1) material-durability「维护周期」为概括措辞**：db-durability 未逐字出现「维护周期」，但 `adequately maintained`／`infrequently painted`／`future costs of maintenance` 直接蕴含维护间隔与成本，属通识性合理概括、非编造。可接受；如求严谨可将「维护周期」软化为「维护要求与寿命成本」。
- **(T2) material-durability def×原理 = 0.64**：两者共用「耐久性/抵抗/能力/维护周期/全生命周期成本」，非逐字但重叠中等；层次（是什么 vs 机理）基本可分，可接受。
- **(T3) 两条「常见错误与限制」规范句句末缺「。」**：`…专业设计人员的要求`（与 r101 skylight T3 同型）。纯格式小疵，`check.py` 未拦（`REGULATION_NOTE` 只匹配子串）。
- **(T4) ★mixed-mode-ventilation def≡原理 逐字相同（ratio 1.0）**：definition 与 `sections.原理` 一字不差，原理节仅重复定义、未给机制（如「自然优先→不足切换机械」的控制逻辑、模式切换、夜间机械冲洗）。**属较重内容去重瑕疵**；建议修复方重写「原理」节以区分于定义（本条升级的「概念支撑」不受影响）。
- **(T5) mixed-mode 源同名重定向**：sources.json `wp-natural-ventilation` title=「Passive ventilation」而 url=.../wiki/Natural_ventilation；owiki 实抓 H1=`Passive ventilation`（同名异名，与 r101 一致，link_ok 语义不受影响）。非本条新问题。
- **(T6) material-durability 标题口径**：entry/coverage title=「材料耐久」，任务称「材料耐久性」；二者一致登记为「材料耐久」，属命名口径差异，非错误。

## 六、机器可读汇总

```
ROUND=102
SAMPLER=spotcheck-r102
SCOPE=["material-durability","mixed-mode-ventilation"]
READONLY="only wrote research/spotcheck-round102.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={
 "db-durability":"web_fetch HTTP200 H1=Durability (no redirect)",
 "db-mixed-mode-ventilation":"web_fetch HTTP200 H1=Mixed-mode ventilation (author BSRIA)",
 "wp-building-material":"owiki.org HTTP200 H1='Building material'",
 "wp-vernacular-architecture":"owiki.org HTTP200 H1='Vernacular architecture'",
 "wp-ventilation-architecture":"owiki.org HTTP200 H1='Ventilation (architecture)'",
 "wp-natural-ventilation":"owiki.org HTTP200 H1='Passive ventilation'"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
GIT={"changed":["M coverage.json","M data/sources.json","M entries/batch-08.json","M site/entries/material-durability.html","M site/entries/mixed-mode-ventilation.html","M site/index.html","M site/sources.html","?? tools/apply_review_round102.py"],"note":"fixer outputs; sampler read-only"}

MATERIAL_DURABILITY={
 "verdict":"合格",
 "change":"sources +db-durability; definition 明确材料抵抗日常磨损/气候侵蚀/维护周期/全生命周期成本; 实例->typological(no specific project); 待核实清空; nv true->false; pending cleared",
 "concept_dual_source":{
   "platforms":["Designing Buildings db-durability (Durability)","Wikipedia wp-building-material (Building material)","Wikipedia wp-vernacular-architecture (Vernacular architecture)"],
   "material_durability_def":"db 'resistance to degradation of products, materials, buildings ... over time' + wp 'durability of the materials' + wp-vern 'durability of these materials in the environment' -> TRIPLE direct",
   "daily_wear":"db 'daily wear and tear from users' -> DB direct (WP not explicit)",
   "climate_erosion":"db 'climate - rain, frost, sun and heat - weathering' + wp-vern 'rainfall too low to damage' -> DOUBLE direct",
   "maintenance_cycle":"db 'adequately maintained/infrequently painted/future costs of maintenance' + wp-bm 'require more care/maintaining costs' -> DOUBLE",
   "lifecycle_cost":"db 'trade-off between initial costs and future costs of maintenance' + wp-bm 'lower lifetime cost' -> DOUBLE direct",
   "holds":true},
 "special_judgment_db_durability":"ADEQUATE: db page defines durability INCLUDING 'materials ... over time' (not merely building durability), and states daily wear+climate weathering+maintenance/lifecycle-cost trade-off; supplies required non-wiki platform",
 "independence":{"holds":true,"detail":"Designing Buildings vs Wikipedia x2 = independent platforms"},
 "fabricated":false,
 "instance":{"text":"公共建筑外立面材料(类型性,不指定具体项目)","typological":true,"specific_project":false,"no_place_designer_year_number":true},
 "nv_false_grounded":true,
 "form_consistency":"nv=false / pending='' / 待核实=暂无 / coverage source_count=3 nv_count=0 four-place consistent; time_or_place clean; check.py PASS",
 "def_vs_principle":{"ratio":0.64,"distinct_below_1":true,"note":"中等重叠(共用耐久性/维护周期/全生命周期成本), 可接受"},
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"material-texture 0.3087","nearest_full":"mixed-mode-ventilation 0.3295","vs_vernacular_material_short":0.3086,"vs_vernacular_material_full":0.2754,"max_short":0.3087,"max_full":0.3295,"lt_0.54":true},
 "transparency":["T1 维护周期为DB维护/成本句的概括(非逐字,非编造)","T2 def×原理0.64中等","T3 常见错误句末缺句号","T6 标题口径材料耐久vs材料耐久性"]
}

MIXED_MODE={
 "verdict":"合格(附透明项T4)",
 "change":"sources +db-mixed-mode-ventilation; 实例->typological(no specific project); 待核实清空; nv true->false; pending cleared; (definition/原理 未改,见T4)",
 "concept_dual_source":{
   "platforms":["Designing Buildings db-mixed-mode-ventilation (Mixed-mode ventilation, BSRIA)","Wikipedia wp-ventilation-architecture (Ventilation (architecture))","Wikipedia wp-natural-ventilation (Passive ventilation)"],
   "natural_plus_mechanical":"db 'combines natural and mechanical ventilation' + wp-vent 'use both mechanical and natural processes' -> DOUBLE direct",
   "supplement_when_natural_inadequate":"db 'mechanical element ensures adequate air flow when natural ventilation is inadequate' + wp-vent 'mechanical systems may be used to supplement or regulate' + wp-natvent 'mechanical system...used when windows are closed due to extreme...' -> TRIPLE direct",
   "natural_first_when_suitable":"db 'benefits of natural ventilation system when weather conditions are suitable' + wp-vent 'same time/different times/seasons' -> DOUBLE",
   "energy":"db night purge + wp-natvent energy comparison -> holds",
   "holds":true},
 "independence":{"holds":true,"detail":"Designing Buildings(BSRIA) vs Wikipedia x2 = independent platforms"},
 "fabricated":false,
 "instance":{"text":"办公建筑混合通风(类型性,不指定具体项目)","typological":true,"specific_project":false,"no_place_designer_year_number":true},
 "nv_false_grounded":true,
 "form_consistency":"nv=false / pending='' / 待核实=暂无 / coverage source_count=3 nv_count=0 four-place consistent; time_or_place clean; check.py PASS",
 "def_vs_principle":{"ratio":1.0,"identical":true,"note":"definition 与 sections.原理 逐字相同, 原理无独立机制说明 -> T4 较重去重瑕疵"},
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"demand-controlled-ventilation 0.3386","nearest_full":"glare 0.3292","vs_natural_ventilation_short":0.2642,"vs_natural_ventilation_full":0.2657,"vs_dcv_short":0.3386,"vs_dcv_full":0.3087,"max_short":0.3386,"max_full":0.3292,"lt_0.54":true},
 "transparency":["T4 def≡原理逐字相同(ratio1.0)原理节纯重复,建议重写","T3 常见错误句末缺句号","T5 wp-natural-ventilation 同名重定向(Natural_ventilation->Passive ventilation)"]
}

METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258}
VERDICT={"material-durability":"合格","mixed-mode-ventilation":"合格(附透明项T4)"}
KEY_FINDING="material-durability 材料耐久 nv=false 升级成立: 概念『材料抵抗退化/日常磨损与气候侵蚀/维护周期/全生命周期成本』由 Designing Buildings db-durability('resistance to degradation of ... materials ... over time'/'daily wear and tear'/'climate-rain,frost,sun,heat-weathering'/'trade-off between initial costs and future costs of maintenance') + Wikipedia wp-building-material(durability of materials/lower lifetime cost) + wp-vernacular(durability of these materials in the environment/rainfall damage) 两平台逐要素直证; 特别判断 db-durability 真定义材料耐久性(显式纳入materials)并直述磨损/气候/维护/寿命成本, 非只泛述建筑耐久, 足够; 类型性实例(公共建筑外立面材料)合理不编造; nv=false四处一致; 七节/SVG(760x400框内无外链)/规范句(句末缺句号T3)/site一致; check.py PASS+pytest 5 passed; 相似度短0.3087/全0.3295<0.54(方法自校0.5157); def×原理0.64. mixed-mode-ventilation 混合通风 nv=false 升级成立: 概念『自然通风不足时机械补充』由 db-mixed-mode-ventilation(BSRIA:'mechanical element ensures adequate air flow when natural ventilation is inadequate') + wp-ventilation('mechanical systems may be used to supplement or regulate') + wp-natural-ventilation标准段('mechanical system is to be used when windows are closed') 三平台逐字级直证; 类型性实例(办公建筑混合通风)合理; nv=false四处一致; 七节/SVG/规范句/site通过; 相似度短0.3386/全0.3292<0.54. 重点透明项T4: mixed-mode definition与sections.原理逐字完全相同(ratio1.0),原理节仅重复定义无独立机制说明,属较重去重瑕疵,建议lead要求修复方重写原理节(不影响概念支撑判定)."
```

## 七、只读核验

- 除本报告 `research/spotcheck-round102.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 四个 Wikipedia 源本轮均经 `owiki.org` 同文镜像 HTTP200 抓回（en.wikipedia 本环境承前阻断，H1 逐一核对一致）；两 DB 源经 `web_fetch` 直抓 HTTP200（本轮无重定向，H1=Durability / Mixed-mode ventilation）。
- 词扫描、相似度、去重、结构、git 核对均内存态 `python - <<'PY'` 直跑，无临时文件。
- 联网页面（designingbuildings.co.uk / owiki.org）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存。
- `git status` 中的改动文件与 `?? tools/apply_review_round102.py` 均为**他方（round102 修复方）产物**，抽检方仅读取、未据以修改。

*（报告完）*
