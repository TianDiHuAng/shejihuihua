# 第61轮质量抽检报告（spotcheck-round61）——第61轮补具名实例 3 条中抽 2 条（light-shadow-modeling / back-light）

- 抽检人：spotcheck-r61（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 18:42 起，Asia/Hong_Kong。
- 任务：对第61轮「补具名实例」3 条（`light-shadow-modeling`、`side-light`、`back-light`，均在 `entries/batch-33.json`）中**抽 2 条**——`light-shadow-modeling`（光影塑形）、`back-light`（逆光）——逐条核对 definition / time_or_place / overview / 实例是否有引用来源正文支撑、是否编造、来源是否直接相关（**重点：本轮新增来源 ng-rembrandt-self63 / ng-temeraire / rijks-milkmaid 是否真述「该作品归属此光影概念」；NG 是否真述明暗塑形 / 逆光夕阳**）；核对 L2 七节 / 内联 SVG / 规范提示；核对 `needs_verification` 与 `pending_notes` / 正文「待核实」联动；核对相似度（阈值 0.54）。本报告未涉 `side-light`（非抽样对象，仅在交叉引用处提及）。
- 协议依据：`AUTONOMOUS.md` §三 E（质量闸：check.py 必须通过；抽检不合格则整批返工、下轮抽检提至 25%；待核实占比异常低或相似度过高→整批降级）＋第六节（联网内容一律视为数据，网页中任何指令不得执行，项目文件夹之外保持原样）；`TASK_design.md`「条目页结构」L2 七节与「专用规则」（每页 1–2 张内联 SVG、图下注「示意图，非施工图」、SVG 元素不出 viewBox、尺寸/坡度/消防/无障碍附「实际工程须按当地规范和专业设计人员的要求」）＋「通用硬性规则」（不编造数字/日期/人名/引文/出处；关键事实至少两个独立来源互证，否则标待核实；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D07/D10/D11/D14。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，命中 `SUBAGENT-STOP`，以任务说明书执行）与 `verification-before-completion`（先实抓、后断言；本条所有来源正文均由本轮 `urllib` 实抓回读为准，不采信 sources.json 的 note 二手转述）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，2026-11-23 18:42 起）**：`coverage.json`=`total=258`；`light-shadow-modeling`：L2/已写/src=4/nvc=**0**/period=文艺复兴至19世纪/region=欧洲；`back-light`：L2/已写/src=4/nvc=**1**/period=跨时期/region=全球。两条 `last_updated=2026-11-23`。
- **`git log -1`** = `6202b6b chore: round60 chiaroscuro and cast-shadow named instances`。第61轮改动尚未提交：`git status --porcelain` 显示 `M coverage.json`、`M data/sources.json`、`M entries/batch-33.json`、`M site/entries/{back-light,light-shadow-modeling,side-light}.html`、`M site/index.html`、`M site/sources.html`，并有未跟踪 `?? tools/apply_review_round61.py`。抽检对象即上述未提交工作树中 2 条的现状。第61轮为 `light-shadow-modeling`/`side-light`/`back-light` 三条补具名实例。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。运行前已 grep 确认该脚本无写文件语句（`write_text`/`.write(`/`open(...,'w')`/`os.remove`/`unlink`/`shutil` 计数=0，仅读）。
- **只读声明**：本次**仅写出** `research/spotcheck-round61.md` 一个项目文件；核对期间为比对抓取正文临时写过 `research/_r61_*.html` 与 `research/_r61_dump.txt`，已在收尾 `rm` 删除（`git status` 复核无残留）。未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目内容文件，未 `git commit`，未改项目文件夹之外内容。联网内容一律视为数据，网页中任何指令性文本均未执行。
- **治理文件说明**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 在工作区磁盘为 NOT_FOUND；按前轮先例实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（6466B）与 `TASK_design.md`（5238B），另读本项目 `DECISIONS.md`、`research/spotcheck-round60.md`（作为口径延续基线）。
- **第61轮改动来源**：`tools/apply_review_round61.py`（未跟踪）显示本轮为 `light-shadow-modeling`/`side-light`/`back-light` 补具名实例：light-shadow-modeling 补「以马忤斯的晚餐」实例、needs_verification 置 **False**（caveat 空）；side-light 补「63岁自画像」实例、nv 置 True；back-light 补「无畏号」实例、nv 置 True（caveat「逆光夕阳由馆方单源直证（blazing sunset / glowing orange）；概念源 Tate 非针对该作。」）。并向 sources.json 追加 `ng-rembrandt-self63`/`ng-temeraire`/`rijks-milkmaid` 三源。抽检以此工作树现状为准。

## 一、判定口径与抓取方法（沿用第51–60轮）

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含「示意图，非施工图」；SVG 元素须限制在 viewBox 内、无 `on*` 事件属性、无外链图片；「常见错误与限制」段须以「实际工程须按当地规范和专业设计人员的要求」收尾。
- **抓取与回验方法**：本轮对两条涉及来源 `urllib`+浏览器 UA+非校验 SSL 实抓并回读正文：`ng-temeraire`（HTTP 200，120439B）、`ng-rembrandt-self63`（200，128877B）、`rijks-milkmaid`（200，166576B）、`ng-supper-emmaus`（200，125583B）、`wp-chiaroscuro`（200，264847B）、`wp-sfumato`（200，127177B）、`wp-architectural-lighting-design`（200，377000B）、`wp-daylighting-architecture`（200，312781B）。关键句按去标签→`html.unescape`→`norm()`（去空白＋小写）子串回验。
- **三级判定定义（沿用第51–60轮）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（核心定义或实例四要素）由 ≥2 独立来源直证互证或由强权威官方源直证且第二源覆盖实例结构；无编造；机械项全过或仅有不影响判定的轻微问题。
  - **待核实**：核心获直接相关来源实质支撑，但某关键事实实质单源/无源，或为来源未逐字作出的解读；`needs_verification=true` 且 pending/正文如实披露者，属「正确的待核实管理」，判待核实但无治理缺陷。**注：若 definition 主干被所引来源均不支撑（实质无源），则依第60轮口径上升为「不合格」。**
  - **不合格**：definition/overview 主干被引用来源均不支撑（实质无源）；或实例核心四要素无任何来源直证；或关键结构项（七节/SVG）实质不满足 TASK_design 强制要求（含 SVG 语义与主题错配）。
- **相似度口径**：`difflib.SequenceMatcher`；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview`+六节正文，含「一图」解说、不计 `svg` 标记），归一为去空白＋小写。全库 258 条逐条扫描，警戒线 **0.54**。**方法自校**：`futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–60轮报告逐位一致，口径正确。

## 二、抽检对象来源清单与相关性（本轮全部实抓正文）

| 条目 | 实例 | 引用来源 id（4） | 实抓证据（本轮） | 与本条的「直接相关性」 |
| --- | --- | --- | --- | --- |
| light-shadow-modeling 光影塑形 | 卡拉瓦乔《以马忤斯的晚餐》（NG172, 1601） | `wp-chiaroscuro`、`wp-sfumato`、**`ng-supper-emmaus`**、`rijks-milkmaid` | wp-chiaroscuro: `use of contrasts of light to achieve a sense of volume in modelling three-dimensional objects and figures`、`strong contrasts between light and dark`；wp-sfumato: `a painting technique for softening the transition between colours`；ng-supper: `The artist uses contrasts of light and shade (known as chiaroscuro) to heighten the drama. A strong light from the left falls on the faces...It casts a shadow...`、`NG172`、`1601`、`Caravaggio`；rijks: `light by means of hundreds of colourful dots plays over the surface of objects`、`SK-A-2344` | 定义由 wp-chiaroscuro（体积/modelling）+ wp-sfumato（过渡）**双源直证**；实例四要素由 **NG 官方源逐字直证**且点名 chiaroscuro；rijks 只讲「光以彩点落在表面」——**与「体积/塑形」间接、偏泛（轻微）** |
| back-light 逆光 | 透纳《被拖去解体的战舰无畏号》（NG524, 1839） | `wp-architectural-lighting-design`、`wp-daylighting-architecture`、**`ng-temeraire`**、`tate-chiaroscuro` | ng-temeraire: `Set against a blazing sunset`、`The colour scheme leans heavily on misty blue and glowing orange`、`The whole scene is bathed in colour as the sun sets – whites, oranges, yellows...`、`NG524`、`1839`、`Turner`；wp-archlight / wp-daylight: **全文无** `backlight/back-light/backlit/against the light/contre-jour/silhouette/rim light`（逐一 MISSING，len 分别 40524/42681） | 实例四要素由 NG 直证、含「blazing sunset / glowing orange / misty blue」（**NG 未用逆光/backlit/silhouette 字样**，属「夕阳为背景」可核而「逆光机制」为推断）；**两个定义导向源完全不含逆光/剪影/轮廓光术语 → 定义主干无源**；tate 为概念背景源 |

> 5 个来源 id 全部存在、`verified=true`、`year=null`（D06 允许）。`ng-temeraire` 的 `link_ok=null`（apply 脚本未记 true），但本轮实抓 **HTTP 200** 可达，非死链。`ng-rembrandt-self63`/`rijks-milkmaid` 为侧光/塑形旁支来源，已实抓可达。**关键相关性结论**：light-shadow-modeling 的定义/实例均有直接来源支撑、rijks 偏泛为轻微项；**back-light 的定义主干（逆光机制）被所引两个定义导向源完全不含相关术语、tate 仅为概念背景 → 定义实质无源；实例仅「夕阳+雾蓝」可核，「逆光」为推断。**

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」

### 3.1 light-shadow-modeling（光影塑形）——**合格（含轻微项）**

- 条目现状（`batch-33.json` 1–21 行）：`definition`＝「光影塑形指用受光与背光的明暗过渡表现物体的体积与转折。」；`time_or_place`＝「文艺复兴至19世纪、欧洲（参见来源）。」；`overview`＝「光线落在形体上形成亮部、暗部与过渡，体积因明暗梯度而被感知。」；`实例`＝《以马忤斯的晚餐》NG172 / 1601 / 卡拉瓦乔，「以强烈的明暗对比塑造人物与静物的体积。此处仅列名称、地点、作者与年份信息，不复制图像。」
- **definition 支撑**：`wp-chiaroscuro` `sense of volume in modelling three-dimensional objects and figures` → 「表现物体的体积」直证 ✓；`wp-sfumato` `softening the transition between colours` → 「明暗过渡」直证 ✓。**双独立权威源（wp-chiaroscuro + wp-sfumato）直证**，非编造。
- **overview 支撑**：「体积因明暗梯度而被感知」由 wp-chiaroscuro「volume in modelling」概念直证 ✓；「亮部、暗部与过渡」为同源与 sfumato 过渡的相容表述 ✓。
- **实例四要素（NG 直证）**：`ng-supper-emmaus` 逐字 `The Supper at Emmaus`、`National Gallery, London`（NG172）、`Michelangelo Merisi da Caravaggio`、`1601` ✓；且逐字 `contrasts of light and shade (known as chiaroscuro) to heighten the drama`、`A strong light from the left falls on the faces...` ✓。**「该作品体现明暗对比」获 NG 官方源直接支撑（点名 chiaroscuro、左侧强光）**，非解读性挂靠。
  - **轻微项**：实例句「塑造人物与静物的**体积**」——NG 原文用 `heighten the drama`（强化戏剧性），**并未出现 `volume`**（实抓 MISSING）。「体积」来自 wp-chiaroscuro 的概念层，非该作官网对该画所下的判断，属「以概念源补描述」的可接受轻微解读，不上升为编造。
  - **轻微项**：`rijks-milkmaid`（第4源）只述「光以数百彩点落在物体表面」，**不涉及体积/塑形/明暗过渡**，与本条定义支撑较弱、偏泛；属挂靠偏松的额外源，建议后续以「体积塑形」专述源替换或降为旁证。
- **七节/SVG/规范提示（机械项）**：6 节齐（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实）；1 张 SVG `viewBox='0 0 760 400'`、文字「光源 / 形体与明暗 / 示意图，非施工图」、无 `on*`、无外链 `<image>`/`href`；「常见错误与限制」以规范句收尾 ✓；几何复算全落 viewBox 内、无越界 ✓；**SVG 语义尚可**（光源→目标形体，标「形体与明暗」贴合体积/明暗主题）✓。**但该 SVG 与 back-light 的 SVG 字节完全相同（见 §五）**。
- **needs_verification / pending 联动**：`needs_verification=false`、nvc=0、`pending_notes=""`、正文「待核实」=「暂无已知待核实项。」→ nv=False 条目无 pending、声明「暂无」属**正确约定**（且本条定义/实例确有 wp+NG 直证，置 False 有据）✓。
- **相似度**：短文本 max 0.3810（vs core-shadow）、全字段 max **0.5233（vs chiaroscuro）**——均 <0.54，但全字段 0.5233 为本条最接近阈值者（裕度仅 0.0167），系因与 chiaroscuro **共用同一实例《以马忤斯的晚餐》且体积定义同族**（见 §六）。
- **内容判定：合格**。definition/overview 由 wp-chiaroscuro+wp-sfumato 双源直证、实例四要素由 NG 官方源直证并点名 chiaroscuro，无编造，机械项全过；两处轻微项（实例「体积」为概念层补述、rijks 偏泛）不影响合格定性。

### 3.2 back-light（逆光）——**不合格（定义主干无源；SVG 与主题错配且复用）**

- 条目现状（`batch-33.json` 43–63 行）：`definition`＝「逆光让光源躲在主体背后直射镜头，主体大半成影，边缘却镶出一条亮廓。」；`time_or_place`＝「跨时期、全球（参见来源）。」；`overview`＝「轮廓光与剪影感强烈，氛围突出，曝光控制不好主体易全黑。」；`实例`＝《被拖去解体的战舰无畏号》NG524 / 1839 / 透纳，「以逆光的发光夕阳与雾蓝对比表现暮色。此处仅列名称、地点、作者与年份信息，不复制图像。」
- **definition 支撑（致命项）**：定义核心是「光源在主体背后 / 主体成影 / 边缘亮廓（轮廓光/剪影）」。所引两个定义导向源——`wp-architectural-lighting-design`（建筑照明）、`wp-daylighting-architecture`（建筑采光）——本轮实抓正文**全文逐词检索 `backlight/back-light/backlit/against the light/contre-jour/silhouette/rim light/rim lighting` 全部 MISSING**（len 40524 / 42681）；`tate-chiaroscuro` 为明暗对照概念背景源，不述逆光；`ng-temeraire` 只述「blazing sunset / glowing orange / misty blue」（夕阳色彩），**未出现 `backlit`/`silhouette`/`against the light`（实抓 MISSING）**。→ **定义主干无任何所引来源直接支撑，属「实质无源」**，仅靠摄影通识，且两定义导向源实为「建筑照明/采光」而非「摄影逆光」——**来源与本条概念错配（挂名不相关源）**。依第60轮判定口径「definition 主干被所引来源均不支撑（实质无源）」→ 不合格。
- **overview 支撑**：「轮廓光与剪影感强烈」同样落空——`silhouette`/`rim light` 在两建筑源与 tate 中均 MISSING；仅 NG「Temeraire rendered stark and white almost like a ghost ship」（近剪影观感）为间接旁证，不构成对「轮廓光/剪影」机制的直证。
- **实例四要素（NG 直证）**：`ng-temeraire` 逐字 `The Fighting Temeraire`、`National Gallery, London`（NG524）、`Joseph Mallord William Turner`、`1839` ✓；`blazing sunset`、`misty blue and glowing orange` ✓ → 「发光夕阳 + 雾蓝对比」直证 ✓。但「**逆光**」一词 NG 未用（`backlit` MISSING），系由 `Set against a blazing sunset`（船相对于夕阳为背景）作出的推断，属「来源未逐字作出的解读」。→ 实例四要素本身可核，但「逆光」定性为推断而非直证。
- **七节/SVG/规范提示（机械项·含实质缺陷）**：6 节齐、规范句收尾 ✓、几何无越界 ✓、无 `on*`/无外链 ✓。**但 SVG 语义与主题错配**：本条 SVG **与 light-shadow-modeling 字节完全相同**（`circle cx=150 cy=90` 光源 + 虚线射线 + `ellipse cx=480 cy=250` 目标 + 文字「光源 / 形体与明暗」），图示为「**光源在左上前方 → 目标形体**」的**正面/侧向照明**，**并非逆光（光源在主体背后、主体成影、边缘亮廓）**；而本条「一图」文字却写「光源在主体背后」——**图文不一致、图示未表达逆光机制**。此即第59轮报告所指「SVG 通用图复用/语义错配」缺陷在本轮重现，且属 TASK_design 强制「图示自绘、须表达本条设计意图」的实质不满足。
- **needs_verification / pending 联动**：`nv=true`、nvc=1、`pending_notes` 与正文「待核实」**逐字一致**：「逆光夕阳由馆方单源直证（blazing sunset / glowing orange）；概念源 Tate 非针对该作。」→ 结构一致 ✓、就「实例单源」披露诚实 ✓；**但 pending 未披露「定义主干无源 / 两建筑照明源不含逆光术语」这一更根本的缺口**，且未提示 SVG 与主题错配 → 披露不完整。
- **相似度**：短文本 max 0.3750（vs highlight）、全字段 max 0.4735（vs warm-cool），均 <0.54 ✓。
- **内容判定：不合格**。定义主干（逆光机制）被所引来源实质无源、两定义导向源与「摄影逆光」概念错配；SVG 与 light-shadow-modeling 复用同一张「正面照明」图、未表达逆光且与「一图」文字自相矛盾。实例四要素可核、pending 结构已联动，但不能抵消定义无源与 SVG 错配两项强制缺陷。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified**：涉及 5 个来源 id（两条去重：wp-chiaroscuro、wp-sfumato、ng-supper-emmaus、rijks-milkmaid、wp-architectural-lighting-design、wp-daylighting-architecture、ng-temeraire、tate-chiaroscuro）全部存在、`verified=true`、`year=null`（D06 允许）。无假 id。
- **可达性（本轮实抓）**：全部 `urllib` HTTP 200 取得正文（ng-temeraire 120439B、ng-rembrandt-self63 128877B、rijks-milkmaid 166576B、ng-supper-emmaus 125583B、wp-chiaroscuro 264847B、wp-sfumato 127177B、wp-archlight 377000B、wp-daylight 312781B）。`ng-temeraire` 的 `link_ok` 字段为 `null`（apply 未记 true），但本轮实抓 200 可达，非死链——**建议补记 link_ok=true**。
- **相关性结论**：
  - `light-shadow-modeling`：wp-chiaroscuro（体积 modelling）+ wp-sfumato（过渡）双源直证定义；NG-supper 单官方源逐字直证《以马忤斯的晚餐》四要素且点名 chiaroscuro；**rijks-milkmaid 偏泛（仅述彩点落表面，不涉体积/塑形）——轻微**。
  - `back-light`：**wp-architectural-lighting-design / wp-daylighting-architecture 为「建筑照明/采光」，全文不含逆光/剪影/轮廓光术语——定义导向源与本概念错配（挂名不相关）**；tate 为概念背景源；ng-temeraire 单官方源直证实例四要素与「夕阳/雾蓝」，但未用「逆光」字样。
- **「来源是否真的支撑'该作品体现该概念/光影现象'」结论**：
  - light-shadow-modeling：**是**（NG 原文 `contrasts of light and shade (known as chiaroscuro)` + `strong light from the left`，直接支撑明暗对比塑形/戏剧）。
  - back-light：**部分**——NG 原文支撑「夕阳为背景、雾蓝/发光橙」，但**未直述「逆光/剪影/轮廓光」**；定义机制层面**无源**。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | viewBox | 含「示意图，非施工图」 | on* 事件 / 外链图 | 规范句收尾 | SVG 几何越界 | SVG 语义贴合 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| light-shadow-modeling | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE | ✓ 尚可（光源→形体，标「形体与明暗」） |
| back-light | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE | **✗ 错配（图示为正面/侧向照明，非逆光；与「一图」文字「光源在主体背后」矛盾）** |

> 七节完整（定义 + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实，无缺节无多余节）；两条各 1 张内联 SVG、`viewBox='0 0 760 400'`、含「示意图，非施工图」、无 `on*`、无 `<image>`/外链；两条「常见错误与限制」均以「实际工程须按当地规范和专业设计人员的要求」收尾；`check.py` PASS。**机械容器项两条通过；但 SVG 语义维度：back-light 与 light-shadow-modeling 的 SVG 字节完全相同（`circle cx=150/ellipse cx=480` 同一图），back-light 的图未表达逆光且与其「一图」文字矛盾——语义错配，判定不满足。**
>
> **几何实核**：按 `x/y/width/height`、`cx/cy/r`、`cx/cy/rx/ry`、`line` 端点复算两条 SVG 元素包围盒，全部落在 0–760 × 400 内，**无越界**。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实 + 相似度

- 两条 `title/theme/tier/period/region/level/status` 与 `coverage.json` 逐字段**一致**（程序化比对 mismatch=NONE）；`source_count` 与来源数组长度一致（4=4 ×2）；`coverage.needs_verification_count`：light-shadow-modeling=0、back-light=1，与条目 `needs_verification`（False/True）逐条对应。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 联动一致性 |
| --- | --- | --- | --- | --- |
| light-shadow-modeling | **false** | ""（空） | 「暂无已知待核实项。」 | **结构一致 ✓**：nv=False 无 pending、声明「暂无」为正确约定；且本条确有 wp+NG 直证，置 False 有据。 |
| back-light | **true** | 「逆光夕阳由馆方单源直证（blazing sunset / glowing orange）；概念源 Tate 非针对该作。」 | 与 pending 逐字一致 | **结构一致 ✓、但披露不完整**：如实点明实例「单源直证」+「Tate 非针对该作」，然**未披露「定义主干无源 / 两建筑照明源不含逆光术语 / SVG 与主题错配」**——该三项属更根本缺陷，未进入待核实说明。 |

> **异常监控（§E）**：light-shadow-modeling 置 nv=False 有 wp-chiaroscuro+NG 逐字直证支撑，非硬写；back-light nv=True 而披露不完整（漏报定义无源与 SVG 错配）。**就抽检对象而言，back-light 的 nv=True 并非「待核实占比异常低」，而是「待核实披露不全」，属内容缺陷而非硬写清零。**

### 相似度（difflib 去空白＋小写，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG）

| 条目 | ①短文本 max（vs 全库除自身） | 判 | ②全字段 max（vs 全库除自身） | 判 |
| --- | --- | --- | --- | --- |
| light-shadow-modeling | 0.3810 vs core-shadow | <0.54 ✓ | **0.5233 vs chiaroscuro** | <0.54 ✓（裕度仅 0.0167） |
| back-light | 0.3750 vs highlight | <0.54 ✓ | 0.4735 vs warm-cool | <0.54 ✓ |

- **批内两两（抽检两条）**：全字段 0.3406、短文本 0.1806，均远低于 0.54 ✓。
- **light-shadow-modeling vs chiaroscuro = 0.5233（最高）**：主因两条**共用同一实例《以马忤斯的晚餐》（NG172，同 4 字段）**且「体积塑造」定义同族；未越 0.54 但已逼近阈值，属共享实例带来的中度相似，需关注（非降级，因 <0.54）。
- **方法自校**：`futurism vs expressionism` 全字段②＝**0.5157**，与第39–60轮一致，口径正确。
- **文本相似度判定：两条对全库与批内均 PASS（<0.54）；不触发相似度降级，但 light-shadow-modeling↔chiaroscuro 的 0.5233 贴近阈值需记录。**

## 七、逐条验收结论

| 条目 | definition/time/overview/实例 来源支撑 | 来源存在·verified·相关·可达 | 七节/规范/SVG | 元数据·pending 联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **light-shadow-modeling（光影塑形）** | definition 双源（wp-chiaroscuro 体积 modelling / wp-sfumato 过渡）直证；overview 同源；《以马忤斯的晚餐》四要素由 NG-supper 逐字直证并点名 chiaroscuro、左侧强光；「体积」为概念层补述（轻微）；rijks 偏泛（轻微）；无编造 | 4/4 存在且 true；本轮 200；定义/实例源直接相关，rijks 偏泛 | 七节齐、规范句✓；1 SVG「示意图，非施工图」、无越界、语义尚可（但与 back-light 复用同图） | 全部一致；nv=False↔pending=""↔「暂无」正确约定；清零有 wp+NG 直证 | 全库 ✓（0.3810/0.5233）；批内 ✓ | **合格（含轻微项）** |
| **back-light（逆光）** | **definition 主干（逆光机制）被所引来源实质无源**：两建筑照明/采光源全文无 backlight/silhouette/轮廓光；tate 概念背景；NG 仅述夕阳色彩、未用逆光字样 → **定义实质无源**；实例四要素由 NG 直证、「逆光」为推断；无编造四要素 | 4/4 存在且 true；本轮 200；**两定义导向源与摄影逆光概念错配（挂名不相关）**；ng-temeraire 直接相关但仅支撑夕阳 | 七节齐、规范句✓；1 SVG 无越界；**SVG 与 light-shadow-modeling 字节相同、图示为正面照明非逆光、与「一图」文字矛盾（语义错配）** | 结构一致；nv=True↔pending↔「待核实」逐字一致，**但披露漏报定义无源+SVG 错配（不完整）** | 全库 ✓（0.3750/0.4735）；批内 ✓ | **不合格** |

### 问题清单

- **① back-light 定义主干无源（严重·强制项）**：definition/overview 的「光源在主体背后、主体成影、边缘亮廓（轮廓光/剪影）」被所引 `wp-architectural-lighting-design`、`wp-daylighting-architecture`（建筑照明/采光，全文无逆光/剪影/轮廓光术语）与 `tate-chiaroscuro`（概念背景）均不支撑，属「定义实质无源」；两定义导向源与「摄影逆光」概念错配。→ 依第60轮口径应判**不合格**。
- **② back-light SVG 语义错配 + 通用图复用（严重·强制项）**：其 SVG 与 light-shadow-modeling **字节完全相同**，图示为「光源左上前方→目标形体」的正面/侧向照明，**未表达逆光**，且与本条「一图」文字「光源在主体背后」**自相矛盾**；属第59轮已指出的「SVG 通用图复用/语义错配」缺陷重现，违反 TASK_design「图示自绘且表达本条设计意图」。
- **③ back-light pending 披露不完整（治理·中等）**：nv=True 但 pending/正文仅披露「实例单源 + Tate 非针对该作」，**未披露定义主干无源与 SVG 错配**，待核实说明不完整。
- **④ light-shadow-modeling 实例「体积」为概念层补述（轻微）**：NG 原文用 `heighten the drama`，未出现 `volume`；「塑造人物与静物的体积」为 wp-chiaroscuro 概念层补述，非该作官网判断——可接受轻微，非编造。
- **⑤ light-shadow-modeling 第4源 rijks-milkmaid 偏泛（轻微）**：仅述「光以彩点落在表面」，不涉体积/塑形/明暗过渡，与本条定义支撑弱，建议换用「体积塑形」专述源或降为旁证。
- **⑥ light-shadow-modeling↔chiaroscuro 相似度 0.5233 贴近阈值（关注·非降级）**：因共用同一实例与体积定义同族；仍在 0.54 内（裕度 0.0167），记录关注。
- **⑦ ng-temeraire link_ok=null（维护·轻微）**：字段未记 true（本轮实抓 200 可达），建议补记 `link_ok=true`。

## 八、总体结论与返工建议

- **抽样结果**：第61轮补具名实例 3 条中抽 2 条——`light-shadow-modeling`、`back-light`。**内容维度：1 合格 + 0 待核实 + 1 不合格。**
  - `light-shadow-modeling`：**合格**（定义双源直证、实例 NG 直证点名 chiaroscuro；两处轻微项）。
  - `back-light`：**不合格**（定义主干无源 + 两定义导向源概念错配 + SVG 与 light-shadow-modeling 复用同图且未表达逆光、图文矛盾）。
- **来源层面**：5 个来源全部存在、`verified=true`、本轮全部取得正文；无假 id、无死链（ng-temeraire 实抓 200，仅 link_ok 未记）。**但 back-light 的两个定义导向源（建筑照明/采光）与「摄影逆光」概念错配，属挂名不相关源。**
- **结构/治理层面**：七节/规范提示机械项两条全过、SVG 几何无越界、元数据逐项一致、`check.py` PASS 0 errors。**SVG 语义维度：back-light 与 light-shadow-modeling 复用同一张正面照明图，back-light 未表达逆光且与「一图」文字矛盾（语义错配）。** pending 联动：light-shadow-modeling nv=False（正确约定，有据）；back-light nv=True（结构一致但披露漏报定义无源与 SVG 错配）。
- **相似度层面**：两条对全库与批内均 <0.54（短文本最高 0.3810、全字段最高 0.5233）；方法自校 0.5157 一致。light-shadow-modeling↔chiaroscuro 0.5233 贴近阈值需关注（非降级）。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：成立（1 条不合格）**——`back-light` 判不合格（定义实质无源 + SVG 语义错配/通用图复用）。按 §E，本轮 3 条（light-shadow-modeling / side-light / back-light）应**整批返工**，且**下一轮抽检比例提高至 25%**。注：3 条中仅抽 2 条，`side-light` 未抽检，但 `side-light` 与本轮同批且实例亦为「单官方源直证+推断」（其「一侧光照」措辞在 NG 该画页面未逐字出现，实抓 `lit dramatically from one side` 实指向另一馆藏画作 A Seated Man with a Stick），返工时宜一并复核。
  2. **§E「相似度过高→整批降级」路径：不成立**——两条均 <0.54。
  3. **§E「待核实占比异常低→整批降级」路径：不成立**（针对被抽两条）——light-shadow-modeling 清零有据、back-light 保留 true（但披露不全）。
  4. **结论：`back-light` 不合格，触发 §E 整批返工（同批 light-shadow-modeling/side-light/back-light）＋下轮抽检提至 25%。**
- **返工/修复建议（阻断项优先）**：
  1. **（阻断·back-light 定义无源）** 为 `back-light` 补引**直接讲「逆光/backlight/contre-jour/剪影/轮廓光」的权威源**（如摄影用光、绘画逆光专述的百科/教材/馆方说明），替换或补充当前两份「建筑照明/采光」错配源；或在无法取得直述源时，将定义改写为可被现有源支撑的、并如实标注「逆光机制部分为通识、来源未直述」入 pending。
  2. **（阻断·back-light SVG 错配复用）** 为 `back-light` 重绘独立 SVG，须真正表达「光源在主体背后、主体成剪影、边缘镶亮廓」的逆光几何（如：光源画在主体后方/镜头对向，主体呈暗剪影+边缘亮线），并与「一图」文字一致；不得再与 light-shadow-modeling 共用同一张正面照明图。
  3. **（治理·back-light pending 完整化）** 重绘并补源后，`pending_notes`/正文「待核实」须如实反映「定义来源强度」「实例单源」等真实状态；若补到直述源则评估 nv 是否需要调整（同步 coverage nvc）。
  4. **（轻微·light-shadow-modeling）** 示例「塑造体积」宜以 NG 原文「强化戏剧性」为准或补一句「（体积判断参见明暗法/光影塑形原理源）」，避免把概念层补述当作该作官网判断；第4源 rijks-milkmaid 若不能支撑「体积/塑形」，建议换为「体积塑形」专述源或降为旁证。
  5. **（维护）** 补记 `ng-temeraire.link_ok=true`（本轮实抓 200）；关注 light-shadow-modeling↔chiaroscuro 共享实例导致的相似度 0.5233，后续修改实例或定义时留意勿越 0.54。

### 机器可读汇总

```
ROUND=61
SAMPLER=spotcheck-r61
MODE=第61轮补具名实例3条抽2条（light-shadow-modeling / back-light）
SCOPE=["light-shadow-modeling","back-light"]
GROUP_NOT_SAMPLED=["side-light"]
FILES={"light-shadow-modeling":"entries/batch-33.json:1-21","back-light":"entries/batch-33.json:43-63"}
GIT_HEAD="6202b6b chore: round60 chiaroscuro and cast-shadow named instances"; ROUND61_COMMITTED=false; GIT_STATUS="round61 UNCOMMITTED (M coverage/data-sources/batch-33 + site entries back-light,light-shadow-modeling,side-light + site/index + site/sources; ?? tools/apply_review_round61.py)"
STATE={"coverage.json":"total=258","light-shadow-modeling":"L2/已写/src=4/nvc=0","back-light":"L2/已写/src=4/nvc=1"}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0); no file-write statements (grep count=0); SVG geometry recheck: 0 out-of-viewBox across 2"
FETCH_METHOD="urllib+UA+unverified-SSL HTTP200: ng-temeraire(120439B),ng-rembrandt-self63(128877B),rijks-milkmaid(166576B),ng-supper-emmaus(125583B),wp-chiaroscuro(264847B),wp-sfumato(127177B),wp-archlight(377000B),wp-daylight(312781B); norm substring readback"
SOURCES={"ids_involved":8,"all_exist":true,"all_verified_true":true,"all_year_null":true,"reachable_200_this_round":true,"fake_id":0,"ng_temeraire_link_ok_field":null,"irrelevant_source":["wp-architectural-lighting-design (back-light: no backlight/silhouette terms)","wp-daylighting-architecture (back-light: no backlight/silhouette terms)"]}
BODY_SUPPORT={
 "light-shadow-modeling":"definition dual DIRECT (wp-chiaroscuro 'sense of volume modelling three-dimensional objects' + wp-sfumato 'softening the transition between colours'); overview same; instance Supper at Emmaus four facts verbatim by NG + 'known as chiaroscuro' + 'strong light from the left'; minor: 'volume' not on NG page (heighten the drama) = concept-layer bridge; rijks-milkmaid generic(light as colourful dots, no volume); no fabrication; VERDICT=合格(含轻微项)",
 "back-light":"definition backbone (source behind subject/silhouette/rim) NOT supported by any cited source: wp-archlight & wp-daylight contain NO backlight/back-light/backlit/against the light/contre-jour/silhouette/rim light (all MISSING, len 40524/42681); tate concept-background only; ng-temeraire only 'blazing sunset/misty blue/glowing orange', backlit MISSING; DEFINITION ESSENTIALLY UNSOURCED + two definition-oriented sources mismatch(建筑照明/采光 vs photographic backlight); instance four facts verbatim by NG but '逆光' is inference; SVG identical to light-shadow-modeling & shows FRONT/side lighting not back-light, contradicts 一图 text '光源在主体背后'; VERDICT=不合格"}
L2_CHECK={"seven_sections":"definition+6/6 x2","svg_count":"1 each","svg_phrase":"示意图，非施工图 x2","viewBox":"0 0 760 400 x2; 无on*/无外链","risk_note":"实际工程须按当地规范和专业设计人员的要求 x2","svg_out_of_viewbox":0,"svg_semantic":{"light-shadow-modeling":"acceptable (光源/形体与明暗)","back-light":"MISMATCH: byte-identical SVG to light-shadow-modeling; depicts front/side lighting, not back-light; contradicts 一图 text; identical-graph reuse (round59 defect recurred)"}}
METADATA={"field_match_coverage":"ALL OK x2","source_count":"4=4 x2","nvc":"light-shadow-modeling=0, back-light=1; matches needs_verification (false/true)","needs_verification":"light-shadow-modeling=false(pending empty, 暂无 correct, cleared with wp+NG support); back-light=true (pending==待核实 verbatim BUT omits definition-unsourced + SVG-mismatch disclosure)"}
SIMILARITY={
 "light-shadow-modeling":{"vs_all_short":0.3810,"short_entry":"core-shadow","vs_all_full":0.5233,"full_entry":"chiaroscuro","note":"near threshold margin 0.0167, shared instance Supper at Emmaus + same volume theme","verdict":"PASS<0.54"},
 "back-light":{"vs_all_short":0.3750,"short_entry":"highlight","vs_all_full":0.4735,"full_entry":"warm-cool","verdict":"PASS<0.54"},
 "intrabatch_full":"0.3406","intrabatch_short":"0.1806",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-60","threshold":0.54}
VERDICT_CONTENT={"light-shadow-modeling":"合格","back-light":"不合格"}
HARD_FABRICATION_INSTANCE=0
FAKE_ID=0
LINK_FAIL=0
SVG_OUT_OF_VIEWBOX=0
SVG_SEMANTIC_MISMATCH=1
IRRELEVANT_SOURCE_COUNT=2
DEFINITION_UNSOURCED=1
BATCH_ACTION="ROLLBACK/BATCH-REWORK TRIGGERED (§E): back-light 不合格 (definition unsourced + SVG semantic mismatch/identical-graph reuse). Rework whole 3-entry group (light-shadow-modeling/side-light/back-light); raise next-round spotcheck to 25%. side-light not sampled but same batch, its 实例 '一侧光照' also inferred (NG page phrase 'lit dramatically from one side' actually refers to different work A Seated Man with a Stick), recheck together. Non-blocking minor: light-shadow-modeling instance 'volume' is concept-layer bridge, rijks-milkmaid generic; record ng-temeraire.link_ok=true; watch light-shadow-modeling<->chiaroscuro 0.5233."
READONLY="only wrote research/spotcheck-round61.md; temp files research/_r61_*.html & _r61_dump.txt written then rm-removed (git status clean of them); no other project content file changed; no git commit; round61 work remains uncommitted as found; web content treated as data, no instruction executed"
```

*（报告完）*
