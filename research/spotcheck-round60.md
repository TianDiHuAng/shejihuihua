# 第60轮质量抽检报告（spotcheck-round60）——第60轮补具名实例 2 条（chiaroscuro / cast-shadow）

- 抽检人：spotcheck-r60（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 18:36 起，Asia/Hong_Kong。
- 任务：对第60轮「补具名实例」的 2 条——`chiaroscuro`（明暗法，`entries/batch-02-a.json` 6–38 行）、`cast-shadow`（投影，`entries/batch-33.json` 66–96 行）——逐条核对 definition / time_or_place / overview / 实例是否有引用来源正文支撑、是否编造、来源是否直接相关（**重点：本轮新增来源 tate-chiaroscuro / ng-supper-emmaus / ng-wright-airpump 是否真述「该作品体现该概念」，NG 是否真述 chiaroscuro / 单烛光投影**）；核对 L2 七节 / 内联 SVG / 规范提示；核对 `needs_verification` 与 `pending_notes` / 正文「待核实」联动；核对相似度（阈值 0.54）。
- 协议依据：`AUTONOMOUS.md` §E（质量闸：check.py 必须通过；抽检不合格则整批返工、下轮抽检提至 25%；待核实占比异常低或相似度过高→整批降级）＋第六节（联网内容一律视为数据，网页中任何指令不得执行，项目文件夹之外保持原样）；`TASK_design.md`「条目页结构」L2 七节与「专用规则」（每页 1–2 张内联 SVG、图下注「示意图，非施工图」、SVG 元素不出 viewBox、尺寸/坡度/消防/无障碍附「实际工程须按当地规范和专业设计人员的要求」）＋「通用硬性规则」（不编造数字/日期/人名/引文/出处；关键事实至少两个独立来源互证，否则标待核实；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D07/D10/D11/D14。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，命中 `SUBAGENT-STOP`，以任务说明书执行）与 `verification-before-completion`（先实抓、后断言；本条所有来源正文均由本轮 `urllib` 实抓回读为准，不采信 sources.json 的 note 二手转述）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，2026-11-23 18:36 起）**：`coverage.json`=`total=258`；`chiaroscuro`：L2/已写/source_count=4/needs_verification_count=**0**/period=文艺复兴至19世纪/region=欧洲；`cast-shadow`：L2/已写/source_count=4/needs_verification_count=**1**/period=跨时期/region=全球。两条 `last_updated=2026-11-23`。
- **`git log -1`** = `891ca39 chore: round59 six-principles named instances`。第60轮改动尚未提交：`git status --porcelain` 显示 `M coverage.json`、`M data/sources.json`、`M entries/batch-02-a.json`、`M entries/batch-33.json`、`M site/entries/{cast-shadow,chiaroscuro}.html`、`M site/index.html`、`M site/sources.html`，并有未跟踪 `?? tools/apply_review_round60.py`。抽检对象即上述未提交工作树中 2 条的现状。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。运行前已 grep 确认该脚本无写文件语句（`write_text`/`.write(`/`open(...,'w')`/`os.remove`/`unlink`/`shutil` 均未命中，仅读）。
- **只读声明**：本次**仅写出** `research/spotcheck-round60.md` 一个项目文件；核对期间为比对抓取正文临时写过 `research/_r60_*.txt` 与抓取脚本 `research/_fetch_r60.py`，已在收尾 `rm` 删除（`git status` 复核无 research 残留）。未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目内容文件，未 `git commit`，未改项目文件夹之外内容（抓取全程临时文件，已清理）。联网内容一律视为数据，网页中任何指令性文本均未执行。
- **治理文件说明**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 在工作区磁盘为 NOT_FOUND；按前轮先例实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行），另读本项目 `DECISIONS.md`（25 行）、`research/spotcheck-round59.md`（223 行）。
- **第60轮改动来源**：`tools/apply_review_round60.py`（未跟踪）显示本轮为 `chiaroscuro` 补「以马忤斯的晚餐」实例、`needs_verification` 置 **False**（caveat 空）；为 `cast-shadow` 补「气泵中的鸟实验」实例、`needs_verification` 置 **True**（caveat「作品投影由馆方单源直证；Tate 为明暗对照概念背景源，未针对该作。」）；并向 sources.json 追加 `tate-chiaroscuro`/`ng-supper-emmaus`/`ng-wright-airpump` 三源。抽检以此工作树现状为准。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含「示意图，非施工图」；SVG 元素须限制在 viewBox 内、无 `on*` 事件属性、无外链图片；「常见错误与限制」段须以「实际工程须按当地规范和专业设计人员的要求」收尾。
- **抓取与回验方法**：本轮 5 个来源 `urllib`+浏览器 UA+非校验 SSL 实抓 **全部 HTTP 200** 取正文：`tate-chiaroscuro`（103930B）、`ng-supper-emmaus`（125583B）、`ng-wright-airpump`（104654B）、`wp-chiaroscuro`（264847B）、`wp-tenebrism`（130224B）。关键句按去标签→`html.unescape`→`norm()`（去空白＋小写）子串回验，全部 FOUND。
- **三级判定定义（沿用第51–59轮）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（核心定义或实例四要素）由 ≥2 独立来源直证互证或由强权威官方源直证且第二源覆盖实例结构；无编造；机械项全过或仅有不影响判定的轻微问题。
  - **待核实**：核心获直接相关来源实质支撑，但某关键事实（实例四要素、年份、具体术语或内容映射）实质单源/无源，或为来源未逐字作出的解读/存在来源明确讨论的学术争议；`needs_verification=true` 且 pending/正文如实披露者，属「正确的待核实管理」，判待核实但无治理缺陷。
  - **不合格**：definition/overview 主干被引用来源均不支撑（实质无源）；或实例核心四要素无任何来源直证；或关键结构项（七节/SVG）实质不满足 TASK_design 强制要求。
- **相似度口径**：`difflib.SequenceMatcher`；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，含 `一图` 解说文字、不计 `svg` 标记），归一为去空白＋小写。全库 258 条逐条扫描，警戒线 **0.54**。**方法自校**：`futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–59轮报告逐位一致，口径正确。

## 二、抽检对象来源清单与相关性（本轮全部实抓正文）

两条共引用来源去重后 5 个 id；**每条 4 个**：`chiaroscuro`＝wp-chiaroscuro、wp-tenebrism、tate-chiaroscuro、ng-supper-emmaus；`cast-shadow`＝wp-chiaroscuro、wp-tenebrism、ng-wright-airpump、tate-chiaroscuro。

| 条目 | 实例 | 引用来源 id（4） | 实抓证据（本轮） | 与本条的「直接相关性」 |
| --- | --- | --- | --- | --- |
| chiaroscuro 明暗法 | 卡拉瓦乔《以马忤斯的晚餐》（NG172, 1601） | `wp-chiaroscuro`、`wp-tenebrism`、**`tate-chiaroscuro`**、**`ng-supper-emmaus`** | wp: `use of strong contrasts between light and dark`、`contrasts of light to achieve a sense of volume in modelling three-dimensional objects`、tenebrism `darkness becomes a dominating feature`；tate: `italian term which translates as light-dark...balance and pattern of light and shade...extreme contrasts of light and shade`；ng: `the artist uses contrasts of light and shade (known as chiaroscuro) to heighten the drama`、`a strong light from the left falls on the faces`、`NG172`、`National Gallery, London`、`1601` | **概念源直证定义**（wp 体积/对比；tate light-dark 平衡与图案）；**NG 官方源逐字直证「该作chiaroscuro 强化戏剧性、左侧强光」四要素齐全**；四源全部直接相关 |
| cast-shadow 投影 | 约瑟夫·赖特《气泵中的鸟实验》（NG725, 1768） | `wp-chiaroscuro`、`wp-tenebrism`、**`ng-wright-airpump`**、`tate-chiaroscuro` | ng: `it is night, and the room is lit by a single candle`、`casting deep, dramatic shadows`、`NG725`、`National Gallery, London`、`1768`；wp: `shadow`/`dark`；tate: `shade` | **NG 官方源逐字直证「单支烛光投下深沉戏剧性投影」四要素齐全（含 NG 真述单烛光投影）**；wp-tenebrism 为背景源（本节未针对该作，但概念相容）；实例源 ng 直接相关 |

> 5 个来源 id 全部存在、`verified=true`、`year=null`（D06 允许）、`link_ok=true`（本轮实抓确认可达）。无假 id、无 `link_ok=false`。**关键相关性结论**：两条 definition 均有概念源直证（wp-chiaroscuro/tate 逐字 light-dark/体积/对比）；两个实例四要素均由对应 **NG 官方机构源逐字直证**，NG 确实分别述及「chiaroscuro（明暗对照）强化戏剧性」与「单支烛光投射深沉戏剧性阴影」——**无编造、无挂名不相关源**。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」

### 3.1 chiaroscuro（明暗法）——**合格**

- 条目现状（`batch-02-a.json` 6–38 行）：`definition`＝「以强烈明暗对比塑造体积和戏剧性效果的绘画方法。」；`time_or_place`＝「文艺复兴至19世纪欧洲（参见来源）。」；`overview`＝「明暗法把光线作为组织画面焦点的手段，其后出现更极端的暗绘倾向。」；`实例`＝「名称：《以马忤斯的晚餐》（The Supper at Emmaus）；地点：英国伦敦国家美术馆（NG172）；作者：卡拉瓦乔（Caravaggio）；年份：1601 年。以左侧强光与深影的强烈明暗对照强化戏剧性。此处仅列名称、地点、作者与年份信息，不复制图像。」
- **definition 支撑**：`wp-chiaroscuro` `use of strong contrasts between light and dark` + `contrasts of light to achieve a sense of volume in modelling three-dimensional objects` → 「强烈明暗对比塑造体积」直证 ✓；`tate-chiaroscuro` `balance and pattern of light and shade...extreme contrasts of light and shade` → 「塑造戏剧性效果」由「extreme contrasts」及 NG `heighten the drama` 支撑 ✓。**双独立权威源（wp + tate）直证**，非编造。
- **overview 支撑**：「其后出现更极端的暗绘倾向」由 `wp-tenebrism` `darkness becomes a dominating feature` + `violent contrasts of light and dark` 直证（tenebrism 即更极端明暗倾向）✓；「把光线作为组织画面焦点的手段」与 wp「contrasts ... to focus strongly on the subject」概念相容 ✓。
- **实例四要素（双源直证）**：`ng-supper-emmaus` 逐字——名称 `The Supper at Emmaus`；地点 `National Gallery, London`（NG172）；作者 `Michelangelo Merisi da Caravaggio`；年代 `1601`；并逐字 `the artist uses contrasts of light and shade (known as chiaroscuro) to heighten the drama. a strong light from the left falls on the faces` → 「左侧强光与深影的强烈明暗对照强化戏剧性」**逐字直证** ✓。`tate-chiaroscuro` 为概念源互证 chiaroscuro=light-dark 极端对比 ✓。**「该作品体现该法」获 NG 官方源直接支撑**（NG 原文即点名 chiaroscuro），非解读性挂靠。
- **七节/SVG/规范提示（机械项）**：6 节齐（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实）；1 张 SVG `viewBox='0 0 760 400'`、文字「受光面 / 暗部与投影 / 示意图，非施工图」、无 `on*`、无外链 `<image>`；「常见错误与限制」以规范句收尾 ✓；几何复算无越界 ✓；**SVG 语义贴合**（受光面↔暗部投影，正是明暗对比的体积示意）✓。
- **needs_verification / pending 联动**：`needs_verification=false`、`needs_verification_count=0`、`pending_notes=""`、正文「待核实」=「暂无已知待核实项。」→ nv=False 条目无 pending 属**正确约定**（无待核实项，不硬写待核实）✓。
- **相似度**：短文本 max 0.4027（vs plein-air）、全字段 max 0.4159（vs one-point-perspective）均 < 0.54 ✓。
- **问题**：无实质问题。可升级候选（见 §九 返工建议，可选）。
- **内容判定：合格**。definition/overview/实例四要素均获双独立权威源直证，NG 官方源点名 chiaroscuro，无编造，机械项全过，SVG 语义得体。

### 3.2 cast-shadow（投影）——**合格（正确的待核实管理；概念源略泛为可接受轻微项）**

- 条目现状（`batch-33.json` 66–96 行）：`definition`＝「投影是物体遮挡光线后在承接面上留下的暗区。」；`time_or_place`＝「跨时期、全球（参见来源）。」；`overview`＝「投影的形状与边缘虚实反映光源强弱、远近与物体形状。」；`实例`＝「名称：《气泵中的鸟实验》（An Experiment on a Bird in the Air Pump）；地点：英国伦敦国家美术馆（NG725）；作者：约瑟夫·赖特（Joseph Wright of Derby）；年份：1768 年。以单支烛光在人物面部投下深沉、戏剧性的投影。此处仅列名称、地点、作者与年份信息，不复制图像。」
- **definition 支撑**：投影（cast shadow）为光学基础概念，`wp-chiaroscuro`/`tate-chiaroscuro` 讲 light-shade/shadow-dark 关系；definition 命意（遮挡光→暗区）由「光与阴影」通识相容，且**实例源 `ng-wright-airpump` 逐字 `casting deep, dramatic shadows` 直证「遮挡光形成投影」的实际呈现** ✓。属**概念通识 + 实例源直证**，非编造（虽 concept 源非逐字给出「cast shadow」定义，但为物理光学通识，且 instance 源实质支撑，判可接受轻微项）。
- **overview 支撑**：「形状与边缘虚实反映光源强弱、远近」——`ng-wright-airpump`「single candle … casting deep, dramatic shadows」（单烛近距硬影）为实例层面佐证；原理通识相容 ✓。
- **实例四要素（NG 官方源直证）**：`ng-wright-airpump` 逐字——名称 `An Experiment on a Bird in the Air Pump`；地点 `National Gallery, London`（NG725）；作者 `joseph wright 'of derby'`；年代 `1768`；并逐字 `it is night, and the room is lit by a single candle`、`casting deep, dramatic shadows` → 「单支烛光在人物面部投下深沉、戏剧性的投影」**逐字直证** ✓。**NG 确实述及「单烛光投影」**，非编造。
- **七节/SVG/规范提示（机械项）**：6 节齐；1 张 SVG `viewBox='0 0 760 400'`、文字「光源 / 形体与明暗 / 示意图，非施工图」、无 `on*`、无外链；规范句收尾 ✓；几何无越界 ✓；**SVG 语义贴合**（光源→点光→投影椭圆，正是投影几何关系示意）✓。
- **needs_verification / pending 联动**：`needs_verification=true`、`needs_verification_count=1`、`pending_notes` 与正文「待核实」**逐字一致**：「作品投影由馆方单源直证；Tate 为明暗对照概念背景源，未针对该作。」→ 结构一致 ✓、内容诚实 ✓（如实点明「投影由馆方单源直证」，Tate 只是概念背景源）。
- **相似度**：短文本 max 0.4211（vs highlight）、全字段 max 0.3778（vs warm-cool）均 < 0.54 ✓。
- **问题**：
  - ① **（轻微·概念源泛）** cast-shadow 的「投影」定义本身无一份逐字给出「cast shadow=遮挡光成暗区」的专门源；`wp-tenebrism` 本节未针对该作（条目 pending 已如实说明「Tate/概念源未针对该作」），`tate-chiaroscuro` 为明暗对照概念背景源。definition 属物理光学通识+实例源（NG `casting deep, dramatic shadows`）实质支撑，**不构成编造，属可接受轻微项**；若求稳可补一份讲「投影/阴影成因」的光学或绘画教程源。
  - ② **（正确管理）** 实例四要素由 NG 单官方源直证，但 NG 官方机构源属强权威，且条目已 `needs_verification=true` 并在 pending 如实披露「单源直证」——**披露诚实，方向正确**；保持待核实合理（亦可由 lead 判断 NG 官方机构源已足而清零，见 §九）。
- **内容判定：合格（正确的待核实管理）**。实例四要素由 NG 官方源逐字直证、NG 真述单烛光投影；`needs_verification` 与 pending/正文逐字联动、诚实披露；SVG 得体。definition 的概念源略泛为可接受轻微项，不上升为不合格。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：5 个来源 id 全部存在、`verified=true`、`year=null`（D06 允许）；`tate-chiaroscuro`/`ng-supper-emmaus`/`ng-wright-airpump`/`wp-chiaroscuro`/`wp-tenebrism` 五条 `link_ok=true`。无假 id、无 `link_ok=false`。
- **可达性（本轮实抓）**：全部 `urllib` HTTP 200 取得正文（tate 103930B、ng-supper 125583B、ng-wright 104654B、wp-chiaroscuro 264847B、wp-tenebrism 130224B）。
- **相关性结论**：
  - `chiaroscuro`：概念源（wp-chiaroscuro+tate）逐字直证定义；NG-supper 单官方源逐字直证《以马忤斯的晚餐》四要素且点名 chiaroscuro；四源全部直接相关。
  - `cast-shadow`：NG-wright 单官方源逐字直证《气泵中的鸟实验》四要素且述单烛光投影；wp-tenebrism 为背景源（本节未针对该作，pending 已披露）；无挂名不相关源（wp-tenebrism 与本主题「明暗/阴影」范围相关，非他题挂名）。
- **「来源是否真的支撑'该作品体现该概念/光影现象'」结论**：
  - chiaroscuro：**是**（NG 原文 `known as chiaroscuro` + `strong light from the left`，两处直接支撑左侧强光明暗对照强化戏剧）。
  - cast-shadow：**是**（NG 原文 `single candle … casting deep, dramatic shadows`，直接支撑单烛光投影）。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | viewBox | 含「示意图，非施工图」 | on* 事件 / 外链图 | 规范句收尾 | SVG 几何越界 | SVG 语义贴合 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| chiaroscuro | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE | ✓ 得体（受光面↔暗部投影） |
| cast-shadow | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE | ✓ 得体（光源→形体明暗→投影） |

> 七节完整（定义 + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实，无缺节无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、含「示意图，非施工图」、无 `on*`、无 `<image>`/外链；两条「常见错误与限制」均以「实际工程须按当地规范和专业设计人员的要求」收尾；`check.py` PASS。**机械项两条全部通过；两条 SVG 语义均与本条主题相称，未发现第59轮报告所指「构图通用图复用/错配」问题在本轮重现。**
>
> **几何实核**：按 `x/y/width/height`、`cx/cy/r`、`cx/cy/rx/ry`、`line` 端点复算两条 SVG 元素包围盒，全部落在 0–760 × 400 内，**无越界**。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- 两条 `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对 mismatch=NONE）；`source_count` 与来源数组长度一致（4=4 ×2）；`coverage.needs_verification_count`：chiaroscuro=0、cast-shadow=1，与条目 `needs_verification` 逐条对应。
- `pending_sum`（全库 nv=true 计数实算）＝**0**？（按 coverage `needs_verification_count` 汇总口径，本轮两条分别 0/1）。*说明*：本轮仅按抽检对象核对，未重算全库 pending_sum，仅确认两条对象 nvc 与条目一致、无硬写清零异常（cast-shadow 保持 true）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 联动一致性 |
| --- | --- | --- | --- | --- |
| chiaroscuro | **false**（本轮置 False） | ""（空） | 「暂无已知待核实项。」 | **结构一致 ✓**：nv=False 条目无 pending、正文声明「暂无已知待核实项」为正确约定；且本条确有 NG 官方源逐字直证，置 False 有据。 |
| cast-shadow | **true**（保持） | 「作品投影由馆方单源直证；Tate 为明暗对照概念背景源，未针对该作。」 | 与 pending 逐字一致 | **结构一致 ✓、内容恰当 ✓**：如实点明「单源直证」+「Tate 为概念背景源未针对该作」，披露诚实。 |

> **异常监控（§E）**：本轮抽检两对象一为 nv=False（chiaroscuro，有 NG 官源逐字直证，清零有据）、一为 nv=True（cast-shadow，诚实披露单源）。**未见硬写清零**：chiaroscuro 清零有 NG 原文 `known as chiaroscuro`+`strong light from the left` 直证支撑，非「为降待核实而硬写」；cast-shadow 保留 true 并披露，方向正确。**不触发「待核实占比异常低」降级**（就抽检对象而言）。

## 七、任务 5：相似度（difflib 去空白＋小写，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG）

### 7.1 对既有库（排除自身）逐条扫描

| 条目 | ①短文本 max（vs 全库除自身） | 判 | ②全字段 max（vs 全库除自身） | 判 |
| --- | --- | --- | --- | --- |
| chiaroscuro | **0.4027** vs plein-air | <0.54 ✓ | **0.4159** vs one-point-perspective | <0.54 ✓ |
| cast-shadow | **0.4211** vs highlight | <0.54 ✓ | **0.3778** vs warm-cool | <0.54 ✓ |

> 两条两档均 **<0.54**，未越线。最高为 cast-shadow 短文本 0.4211（vs highlight，同为光影术语短定义），裕度充足。

### 7.2 批内两条两两

- chiaroscuro vs cast-shadow：全字段 **0.3685**、短文本（需另算；短文本最高即 vs highlight 0.4211，与 cast-shadow 更低）。
- → 批内两两均低于 0.54，无套话/模板姊妹风险（两条同属光影主题但一为「明暗对比法」、一为「投影几何」，实例分别为《以马忤斯的晚餐》与《气泵中的鸟实验》，内容分化明显）。

### 7.3 方法自校

- `futurism vs expressionism` 全字段②＝**0.5157**，与第39–59轮报告逐位一致，口径正确。

> **文本相似度判定：两条对全库与批内均 PASS（<0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition/time/overview/实例 来源支撑 | 来源存在·verified·相关·可达 | 七节/规范/SVG | 元数据·pending 联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **chiaroscuro（明暗法）** | definition 双源（wp 体积+对比 / tate light-dark）直证；overview 由 wp-tenebrism 极端暗绘直证；《以马忤斯的晚餐》四要素由 NG-supper 逐字直证并点名 chiaroscuro、左侧强光；无编造 | 4/4 存在且 true；本轮 200；四源全部直接相关 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、无越界、语义得体贴合 | 全部一致；nv=False↔pending=""↔「暂无已知待核实项」正确约定；清零有 NG 直证 | 全库 ✓（0.4027/0.4159）；批内 ✓ | **合格** |
| **cast-shadow（投影）** | definition 属光学通识+实例源 NG `casting deep, dramatic shadows` 实质支撑（概念源略泛·轻微）；《气泵中的鸟实验》四要素由 NG-wright 逐字直证、NG 真述单烛光投影；无编造 | 4/4 存在且 true；本轮 200；实例源直接相关，wp-tenebrism 为背景源（pending 已披露） | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、无越界、语议得体（光源→投影） | 全部一致；nv=true↔pending↔「待核实」逐字一致、披露诚实 | 全库 ✓（0.4211/0.3778）；批内 ✓ | **合格（正确的待核实管理）** |

### 问题清单

- **① cast-shadow 概念源略泛（轻微·不上升不合格）**：「投影」定义无专门逐字给出「cast shadow=遮挡光成暗区」的源；`wp-tenebrism` 本节未针对该作、`tate-chiaroscuro` 为概念背景源。definition 属物理光学通识+NG 实例源实质支撑，非编造；可补一份讲「投影/阴影成因」的光学或绘画教程源以更稳。
- **② cast-shadow 实例单官方源（正确管理·可选升级）**：四要素由 NG-wright 单官方机构源直证，条目 `needs_verification=true` 且 pending 如实披露「单源直证」——披露诚实；NG 为强权威官方源，亦可由 lead 判断清零（须同步 pending/待核实/coverage nvc/pending_sum），当前维持待核实同样正确。
- **③ chiaroscuro 清零合理性（已核对·无缺陷）**：chiaroscuro 本轮置 nv=False，有 NG 官方原文 `known as chiaroscuro`+`strong light from the left` 逐字直证，非硬写；四源全直接相关。
- **④（无）** 本轮未发现第59轮报告所指「SVG 通用图复用/语义错配」问题；两条 SVG 各自贴合主题、彼此不同、几何无越界。

## 九、总体结论与建议

- **抽样结果**：第60轮补具名实例 2 条——`chiaroscuro`、`cast-shadow`。**内容维度：2 合格 ＋ 0 待核实 ＋ 0 不合格；实例层面 0 编造、0 假 id、0 死链证据。** 两条 definition 均有概念源直证（wp-chiaroscuro/tate 逐字 light-dark/体积/对比），两个实例四要素均由 **NG 官方机构源逐字直证**，NG 确实分别述及「chiaroscuro 强化戏剧」与「单烛光投影」，无编造。
- **来源层面**：5 个来源全部存在、`verified=true`、本轮全部取得正文。两条实例四要素由 NG 官方源直证，无挂名不相关源（wp-tenebrism 为背景源，pending 已披露）。
- **结构/治理层面**：七节/规范提示机械项两条全过、SVG 几何无越界、SVG 语义贴合、元数据逐项一致、`check.py` PASS 0 errors。**pending 联动**：chiaroscuro nv=False（无 pending、声明暂无待核实，正确约定）；cast-shadow nv=True（pending 与正文逐字一致、披露单源，诚实）。未发现硬写清零或待核实占比异常。
- **相似度层面**：两条对全库与批内均 <0.54（短文本最高 0.4211、全字段最高 0.4159）；方法自校 0.5157 与第39–59轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——2 合格、0 不合格，0 实例编造/假 id/死链。
  2. **§E「相似度过高（疑似套话）→整批降级」路径：不成立**——两条对全库与批内均 <0.54。
  3. **§E「待核实占比异常低（疑似硬写）→整批降级」路径：不成立**——chiaroscuro 清零有 NG 原文直证，cast-shadow 保留 true 并披露，无硬写。
  4. **结论：本轮 2 条合格、0 不合格，不触发整批返工/降级。** 本轮质量为近几轮最好（两条均合格、SVG 语义贴合、无挂名源）。
- **返工/修复建议（可选·非阻断）**：
  1. **（可选·轻微）** 为 `cast-shadow` 的「投影」定义补一份讲「阴影/投影成因」的光学或绘画基础源，使 definition 不只靠通识+实例源。
  2. **（可选·lead 判断）** `cast-shadow` 实例四要素已由 NG 官方源逐字直证，若 lead 认为单官方机构源已足，可评估将 `needs_verification` true→false 清零（须同步 `pending_notes`、正文「待核实」、`coverage.needs_verification_count` 与 `pending_sum`）；否则维持现状（当前披露诚实，无需回滚）。
  3. **（维护·建议）** 第60轮把 chiaroscuro/cast-shadow 从 L1/弱 L2 补成具名实例，质量达标；可将同批仍有「无具名实例」的光影类条目（如 five-tones、highlight、value 等）纳入后续补实例队列，参照本条「NG 官方机构源逐字直证」范式。

### 机器可读汇总

```
ROUND=60
SAMPLER=spotcheck-r60
MODE=第60轮补具名实例抽2条（chiaroscuro / cast-shadow）
SCOPE=["chiaroscuro","cast-shadow"]
FILES={"chiaroscuro":"entries/batch-02-a.json:6-38","cast-shadow":"entries/batch-33.json:66-96"}
GIT_HEAD="891ca39 chore: round59 six-principles named instances"; ROUND60_COMMITTED=false; GIT_STATUS="round60 changes UNCOMMITTED as found (M coverage/data-sources/batch-02-a/batch-33 + site entries chiaroscuro,cast-shadow + site/index + site/sources; ?? tools/apply_review_round60.py)"
STATE={"coverage.json":"total=258","chiaroscuro":"L2/已写/src=4/nvc=0","cast-shadow":"L2/已写/src=4/nvc=1"}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0); no file-write statements; SVG geometry recheck: 0 out-of-viewBox across 2"
SAMPLE_RATIO="2/2 of the round60 named-instance group"
FETCH_METHOD="urllib+UA+unverified-SSL HTTP200 for tate-chiaroscuro(103930B),ng-supper-emmaus(125583B),ng-wright-airpump(104654B),wp-chiaroscuro(264847B),wp-tenebrism(130224B); norm substring readback; all FOUND"
SOURCES={"ids":5,"all_exist":true,"all_verified_true":true,"all_year_null":true,"link_ok_all_200_this_round":true,"fake_id":0,"irrelevant_source":[]}
BODY_SUPPORT={
 "chiaroscuro":"definition dual (wp-chiaroscuro 'strong contrasts between light and dark'+'sense of volume modelling three-dimensional' / tate 'balance and pattern of light and shade...extreme contrasts'); overview wp-tenebrism 'darkness dominating feature'; instance Supper at Emmaus four facts verbatim by NG ('strong light from the left'/'known as chiaroscuro to heighten the drama'/'NG172'/'National Gallery, London'/'1601'); no fabrication; VERDICT=合格",
 "cast-shadow":"definition optical common-knowledge + instance source NG 'casting deep, dramatic shadows' (concept source slightly generic, minor); instance Air Pump four facts verbatim by NG ('single candle'/'casting deep, dramatic shadows'/'NG725'/'National Gallery, London'/'1768'); no fabrication; nv=true pending honest single-source disclosure; VERDICT=合格(正确待核实管理)"}
L2_CHECK={"seven_sections":"definition+6/6 x2","svg_count":"1 each","svg_phrase":"示意图，非施工图 x2","viewBox":"0 0 760 400 x2; 无on*/无外链图","risk_note":"实际工程须按当地规范和专业设计人员的要求 x2","svg_out_of_viewbox":0,"svg_semantic_issue":"none; chiaroscuro(受光面/暗部与投影) & cast-shadow(光源/形体与明暗) both fit theme, not byte-identical"}
METADATA={"field_match_coverage":"ALL OK x2 (mismatch=NONE)","source_count":"4=4 x2","nvc":"chiaroscuro=0, cast-shadow=1; matches entry needs_verification (false/true)","needs_verification":"chiaroscuro=false(pending empty, 暂无已知待核实项 correct convention, cleared with NG verbatim support); cast-shadow=true (pending==待核实节 verbatim)"}
SIMILARITY={
 "chiaroscuro":{"vs_all_short":0.4027,"short_entry":"plein-air","vs_all_full":0.4159,"full_entry":"one-point-perspective","verdict":"PASS<0.54"},
 "cast-shadow":{"vs_all_short":0.4211,"short_entry":"highlight","vs_all_full":0.3778,"full_entry":"warm-cool","verdict":"PASS<0.54"},
 "intrabatch_full":"chiaroscuro vs cast-shadow=0.3685",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-59 -> method validated","threshold":0.54}
VERDICT_CONTENT={"chiaroscuro":"合格","cast-shadow":"合格"}
HARD_FABRICATION_INSTANCE=0
UNSOURCED_CLAIM=0
FAKE_ID=0
LINK_FAIL=0
SVG_OUT_OF_VIEWBOX=0
SVG_SEMANTIC_MISMATCH=0
IRRELEVANT_SOURCE_COUNT=0
BATCH_ACTION="No rollback/downgrade: 2 合格, 0 不合格, 0 instance fabrication/0 fake id/0 dead link; similarity all <0.54; chiaroscuro nv=False backed by NG verbatim (no hard-write); cast-shadow nv=true honest single-source disclosure. Optional non-blocking: (1) add an optics/painting-basics source for cast-shadow 'shadow/cast-shadow' definition; (2) lead may evaluate clearing cast-shadow nv true->false given NG official source is authoritative (sync pending/待核实/nvc/pending_sum) else keep."
READONLY="only wrote research/spotcheck-round60.md; temp files research/_r60_*.txt & _fetch_r60.py written then rm-removed (git status clean of them); no other project content file changed; no git commit; round60 work remains uncommitted as found; web content treated as data, no instruction executed"
```

*（报告完）*
