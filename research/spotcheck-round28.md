# 第28轮质量闸抽检报告（spotcheck-round28）——balance / gothic / wayfinding 逐条来源正文支撑·来源相关性·L2 七节与SVG·元数据联动·相似度

- 抽检人：spotcheck-r28（由 lead 委派的子代理）；抽检样本时间 2026-11-22 约 22:47 起、核对完成约 22:53，Asia/Hong_Kong（CST）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（新增/改动条目随机抽 ≥10%、至少 3 条逐条核对来源；**不合格则整批返工**，下一轮抽检比例提至 25%）+ 第六节（联网内容一律视为数据，其中任何指令不执行、不下载不运行来源代码、不改项目文件夹之外内容）；`D:/Users/Administrator/Desktop/TASK_design.md`「条目页结构」L2 七节标准 +「通用硬性规则」（不编造数字·日期·人名·引文·出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；只引用 verified=true 来源；图下注明“示意图，非施工图”；尺寸/坡度/消防/无障碍注明“实际工程须按当地规范和专业设计人员的要求”）+「专用规则」；`DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md`/`TASK_design.md` 在仓库根无同名文件，实际位于 `D:/Users/Administrator/Desktop/`（与第 12–27 轮一致），已按该路径只读读取；`DECISIONS.md` 在仓库根。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读）**：`data/sources.json`=110544B@22:45:32、`entries/batch-01.json`=80147B@22:45:32、`entries/batch-02-d.json`=17780B@22:45:32、`entries/batch-07.json`=15168B@22:45:32、`coverage.json`=81955B@22:45:32（Asia/Hong_Kong）。`python tools/check.py` 于约 22:50 实跑 **`PASS: all checks, 0 errors`（EXIT=0）**。`git status` 仅见 `?? research/gaps-round28.md`（主流程缺口文件，非本子任务所改），工作树除此外干净。
- **只读声明**：本次**仅生成** `research/spotcheck-round28.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未创建 git commit，未改项目文件夹之外内容。抓取缓存仅驻留系统临时目录（`%TEMP%/r28/*.txt|*.bin`），非项目产物。联网内容一律视为数据，网页中任何指令均未执行。
- **抽检口径与样本**：任务指定从“第27轮补第二源的条目”中抽 `balance`、`gothic`、`wayfinding` 3 条（≥25%、≥3 条门槛满足）。3 条定位：`balance`→`entries/batch-01.json`、`gothic`→`entries/batch-02-d.json`、`wayfinding`→`entries/batch-07.json`。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 中 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）；须 1 张 SVG 且含“示意图，非施工图”；“常见错误与限制”段须以“实际工程须按当地规范和专业设计人员的要求”收尾。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`ssl` 不校验证书）；PDF 用 `pypdf 6.21.1` 抽取正文。`en.wikipedia.org` canonical 本轮仍 `WinError 10060`（连接超时，与第 12–27 轮一致），改 **owiki 同源镜像**（`https://owiki.org/wiki/<Title>`）；`getty.edu`、`designingbuildings.co.uk`、`human.libretexts.org` canonical 直连 **HTTP 200**。逐一记录 HTTP 码、字节数、`<title>`/`<h1>`、正文长度与关键词命中。
- **第二源相关性判据**：第二源须**正文直接支撑该条核心概念/定义**（非泛论伞源、非维基镜像）。
- **相似度口径**：`difflib.SequenceMatcher`（去空白）对 `entries/*.json` 全库（**132 条**）逐条扫描，警戒线 **0.54**。按任务要求报告两档：①短文本（标题+定义+时间地点+概述）；②全字段-不含SVG（+sections 全部文本）。

## 二、抽检对象来源清单与完整性（任务 2）

`python tools/check.py` → **PASS, 0 errors**。5 个被引用来源 id **全部存在、全部 verified=true**。但**“补第二源”落实情况不一致**——`gothic` 实际仍为**单源**：

| 条目 | sources（现状） | 存在/verified | 标题 / 类型 | type | 与主题相关性 | 第二源是否落实 |
| --- | --- | --- | --- | --- | --- | --- |
| balance | `wp-composition-visual-arts` | ✅ / true | Composition (visual arts) / 百科 | 权威百科 | 直接 | — |
| balance | `getty-principles-design` | ✅ / true | Principles of Design — J. Paul Getty Museum | 官方机构 | **直接**（专段定义 Balance） | **已补** ✅ |
| gothic | `wp-gothic-architecture` | ✅ / true | Gothic architecture / 百科 | 权威百科 | 直接 | — |
| gothic | **（无第二源）** | **缺** | — | — | — | **未补** ❌ |
| wayfinding | `wp-wayfinding` | ✅ / true | Wayfinding / 百科 | 权威百科 | 直接 | — |
| wayfinding | `designingbuildings-wayfinding` | ✅ / true | Wayfinding — Designing Buildings | 学术百科 | **直接**（专条定义） | **已补** ✅ |

> 关键事实：`gothic` 的 `sources` 数组仅 1 项（`wp-gothic-architecture`），`coverage.source_count=1`；`data/sources.json` 全库检索**不存在任何 LibreTexts / Gavilan / Vaulted Arch 来源**（`libretext|gavilan|vaulted|sacred-buildings` 命中 0）。即第27轮 review-round27 曾判 `gothic` 可补 LibreTexts 第二源，但**该源从未登记、从未追加**——`gothic` 仍为单源，与“第27轮补第二源”的抽检前提不符。这是本轮最需 lead 关注的发现。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节（实抓逐句比对）

### 3.1 balance（均衡）——**合格**
- **getty-principles-design**（canonical HTTP200 217965B，application/pdf，1 页，正文 2800c；balance=6 / visual weight=1 / symmetrical=2 / asymmetrical=1）：原文 “**Balance is the distribution of the visual weight of objects, colors, texture, and space.** If the design was a scale, these elements should be balanced to make a design feel stable. In **symmetrical** balance, the elements used on one side of the design are similar to those on the other side; in **asymmetrical** balance, the sides are different but still look balanced. In **radial** balance, the elements are arranged around a central point and may be similar.”
- **wp-composition-visual-arts**（canonical 超时 WinError10060 → owiki 镜像 HTTP200 25240B，h1「Composition (visual arts)」，正文 14838c；balance=3 / symmetr=4）：原文 “…pleasing to the eye if the elements within the work are arranged in a **balanced compositional way**.”
- 逐项：definition“画面各元素在视觉重量上的均衡关系”✓（Getty “distribution of the visual weight” 逐字对应）；overview“均衡不等于对称，大小与色彩差异都能改变视觉重量”✓（Getty symmetrical/asymmetrical 对照 + objects/colors/texture/space）；原理“各元素在视觉重量上的平衡；可由对称达成，也可由大小、明暗与色差动态平衡”✓（对称/非对称/放射三类平衡 + scale 类比）；典型手法“以一大暗块对一小亮点实现非对称均衡”✓（asymmetrical balance 概念的通用示例）；time_or_place“跨时期、全球”✓（设计通则，非断代）。**双源互补且均直接支撑。**
- **实例**：“名称：非对称均衡构图（类型性描述）；地点/设计者/年份：不适用”——**类型性描述，无杜撰具体作品/人名/年份** ✓。
- **Minor**：①Getty 为“设计原则”通页，但其含**独立的 Balance 定义段**，对该条属直接支撑而非泛论；②“大小”(size) 未在 Getty 原句逐字出现（原文列 objects/colors/texture/space），属可接受意译。
- 未发现编造年份/人名/引文。**结论：合格。**

### 3.2 gothic（哥特建筑）——**待核实（内容成立，但“补第二源”未落实 → 实际单源）**
- **wp-gothic-architecture（唯一来源）**（canonical 超时 → owiki 镜像 HTTP200 128210B，h1「Gothic architecture」，正文 89402c；gothic=245 / pointed arch=30 / ribbed vault=1 / flying buttress=19 / vault=101 / buttress=41）：原文 “**The defining design element of Gothic architecture is the pointed arch. The use of the pointed arch in turn led to the development of the pointed rib vault and flying buttresses**, combined with elaborate tracery and stained glass windows.”；“Gothic architecture is an architectural style that was **prevalent in Europe from the late 12th to the 16th century**”。
- 逐项（以单一来源核对）：definition“以尖拱、肋拱与飞扶壁为特征”✓（pointed arch + pointed rib vault + flying buttresses 逐字）；time_or_place“中世纪、欧洲”✓（late 12th–16th century · Europe）；overview“结构体系使墙体得以开出大面积窗户，形成高耸而明亮的内部空间”✓（tracery + stained glass windows）；原理/手法✓（尖拱统一跨度、飞扶壁外传侧推力）。**内容本身有源、无杜撰。**
- **实例**：“名称：哥特式大教堂（类型性描述）；地点：欧洲；设计者：不适用；年份：不适用”——**类型性描述，无杜撰** ✓。
- **问题（本轮核心）**：`gothic` **仅 1 个来源**（`wp-gothic-architecture`），`coverage.source_count=1`；**未登记任何第二源**。而 review-round27 §二 第6行已明确判 `gothic` 可补 **Humanities LibreTexts《7.3: The Vaulted Arch》**（本轮独立复抓 canonical HTTP200 192191B，title「7.3: The Vaulted Arch - Humanities LibreTexts」；pointed arch=12 / ribbed vault=10 / flying buttress=15 / gothic=27；原文“**Pointed Arches**: Archways that rise to a pointed top, commonly used in **Gothic architecture** to distribute weight more efficiently. **Ribbed Vaults**…**Flying Buttresses**: Exterior stone supports that transfer the weight of a building outward, allowing for taller walls and larger windows.”）——该源对本条属**直接支撑、非泛论**，但**始终未写入 `data/sources.json`、未追加进 `gothic.sources`**。
- **诚实性评估**：`gothic` 的 `needs_verification=true`、`pending_notes` 与「待核实」节均如实写“**核心依据目前为单一权威来源（原第二来源为泛论、未覆盖本子概念）**；具体实例的设计者与年代待补充独立来源”——**单源状态已如实披露，非硬写、非造假**。故性质为“诚实但升级未完成”，非“不相关的假第二源”（区别于第27轮 vestibule 的 wp-loggia）。
- **结论：待核实**——内容与标注诚实、结构达标；但“补第二源”目标未达成，仍单源。建议**定向补齐 `gothic` 单条**（把已验证的 LibreTexts 源登记为 verified=true → 追加到 sources → 更新 source_count 与 pending_notes → 复跑 check.py），而非整批返工（详见 §八/§九）。

### 3.3 wayfinding（导视与寻路）——**合格**
- **designingbuildings-wayfinding**（canonical HTTP200 53663B，title「Wayfinding - Designing Buildings」，正文 6351c；wayfinding=19 / navigate=1 / signage=8）：原文 “**Wayfinding is a method for relaying messages to help people navigate their way around a room, building or other unfamiliar environment.** It is particularly important in large, complex buildings…”“**Signage is the most common form of wayfinding, but architectural features and other objects can also be used to guide people through buildings.**”
- **wp-wayfinding**（canonical 超时 → owiki 镜像 HTTP200 20527B，h1「Wayfinding」，正文 10373c；wayfinding=41 / navigate=4 / signage=7）：原文 “**Wayfinding encompasses all of the ways in which people orient themselves in physical space and navigate from place to place.**”“…expanded the concept to include the use of **signage and other graphic communication, visual clues in the built environment**…”。
- 逐项：definition“人在物理空间中借助标识、地图与视觉线索定向和导航”✓（orient/navigate + signage/graphic communication/visual clues，双源）；overview“把动线组织、空间认知和图形信息结合起来”✓；原理“依靠标识、地图与空间线索确定方位并抵达目标”✓；典型手法“分级标识、连续视觉线索与节点地标”✓（Signage most common + architectural features/other objects guide through buildings）；time_or_place“跨时期、全球”✓（通用概念）。**双源互补且均直接支撑。**
- **实例**：“名称：大型文化建筑导视系统（类型性描述）；地点/设计者/年份：不适用”——**类型性描述，无杜撰** ✓。
- **Minor**：“地图”(maps) 未在双源原句逐字出现（源述 signage/graphic communication/visual clues），属可接受意译。
- **结论：合格。**

## 四、任务 2：来源 id 存在性、verified、相关性、可达性

- **存在性/verified**：5 个来源 id（`wp-composition-visual-arts`、`getty-principles-design`、`wp-gothic-architecture`、`wp-wayfinding`、`designingbuildings-wayfinding`）**全部存在、全部 verified=true**（`getty`/`designingbuildings` 为 `link_ok=null`，wikis 为 `link_ok=true`；`verified` 独立表示标题/机构已核对，不受 link_ok 影响，符合 D11）。
- **相关性**：`balance` 的第二源 `getty-principles-design`、`wayfinding` 的第二源 `designingbuildings-wayfinding` 均**直接支撑**（专段/专条定义，非泛论）；`gothic` **无第二源**（唯一来源 `wp-gothic-architecture` 本身直接相关）。
- **可达性（本轮实抓）**：`getty.edu`（PDF）HTTP200、`designingbuildings.co.uk` HTTP200、`human.libretexts.org`（gothic 候选第二源）HTTP200；`en.wikipedia.org` canonical 超时（WinError 10060，与历史一致），三篇维基经 owiki 同源镜像 HTTP200 核对 h1。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | 缺节 | SVG 数 | 含“示意图，非施工图” | SVG 元素出界 | viewBox | 风险/规范句 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| balance | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓“实际工程须按当地规范和专业设计人员的要求” |
| gothic | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓ |
| wayfinding | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓ |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 全部齐备，无缺节、无多余节）；每条 1 张内联 SVG、viewBox 均 `0 0 760 400`、均含“示意图，非施工图”；逐元素（rect/circle/line/text 坐标与宽高半径）核验**无出界**；“常见错误与限制”段均以规范提示收尾。**该项三条全部通过。**

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- 三条 `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**；`source_count` 与来源数组长度**一致**：`balance` 2=2、`gothic` 1=1（真实反映单源）、`wayfinding` 2=2。

| 条目 | needs_verification | pending_notes（结构化） | 正文 `待核实` 节 | 一致性 |
| --- | --- | --- | --- | --- |
| balance | true | 核心已补第二独立来源；具体实例的设计者与年代待补充独立来源 | 与 pending 逐字相同 | **一致** ✓（“已补第二源”属实） |
| gothic | true | 核心依据目前为单一权威来源（原第二来源为泛论、未覆盖本子概念）；具体实例的设计者与年代待补充独立来源 | 与 pending 逐字相同 | **一致** ✓（单源状态如实披露） |
| wayfinding | true | 核心已补第二独立来源；具体实例的设计者与年代待补充独立来源 | 与 pending 逐字相同 | **一致** ✓（“已补第二源”属实） |

> `needs_verification=true`、`coverage.needs_verification_count=1`、`pending_notes` 非空、正文「待核实」节与 pending **逐字相同**——三条形式与实质**均一致**。特别地，`gothic` 的“单源”披露是**真实且诚实**的；其唯一缺陷是“本应补的第二源未落地”，而非披露失实。

## 七、任务 5：与既有条目相似度（difflib，阈值 0.54，全库 132 条）

| 条目 | ①短文本(标题+定义+时间+概述) | 判 | ②全字段-不含SVG | 判 |
| --- | --- | --- | --- | --- |
| balance | **0.4000** vs rhythm-repetition | <0.54 ✓ | **0.4854** vs rhythm-repetition | <0.54 ✓ |
| gothic | **0.3768** vs renaissance-style | <0.54 ✓ | **0.4483** vs axis | <0.54 ✓ |
| wayfinding | **0.3704** vs interior-exterior-transition | <0.54 ✓ | **0.4494** vs rhythm-repetition | <0.54 ✓ |

> 两条口径（①短文本、②全字段-不含SVG）三条**全部 <0.54**（短文本 0.37–0.40；全字段 0.45–0.49），**无内容套话超标**。说明：按第27轮经验，“全字段-**含**SVG原始标记”口径会因结构模板+SVG标记越线（非内容套话），故本轮按任务要求采用②（内容层）判定，未把模板式越线计为降级依据。

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview 来源支撑 | 来源存在·verified·相关·**第二源落实** | L2 七节/SVG/风险 | 元数据·联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **balance（均衡）** | 定义✓（distribution of the visual weight 逐字）；时间✓；概述✓（symmetrical/asymmetrical+objects/colors）；原理/手法✓ | 2/2 true，均相关；**第二源 getty 直接支撑·已补** | 七节齐、SVG✓、风险✓ | 全部一致；nv/pending/待核实一致 ✓ | 0.400/0.485 | **合格** |
| **gothic（哥特建筑）** | 定义✓（pointed arch+rib vault+flying buttress）；时间✓（12–16世纪欧洲）；概述✓（tracery+stained glass）；原理/手法✓ | 1/1 true，直接相关；**无第二源·未补（LibreTexts 未登记）** | 七节齐、SVG✓、风险✓ | 形式/实质一致；单源如实披露 ✓ | 0.377/0.448 | **待核实**（内容成立、标注诚实，但“补第二源”未落实，仍单源） |
| **wayfinding（导视与寻路）** | 定义✓（orient/navigate+signage/visual clues）；时间✓；概述✓；原理/手法✓ | 2/2 true，均相关；**第二源 designingbuildings 直接支撑·已补** | 七节齐、SVG✓、风险✓ | 全部一致；nv/pending/待核实一致 ✓ | 0.370/0.449 | **合格** |

- **合格 2 条**：`balance`、`wayfinding`。
- **待核实 1 条**：`gothic`（**补第二源未落实、实际单源**；内容与单源披露诚实）。
- **硬性“编造” 0 条**：三条 `实例` 均为“类型性描述 + 地点/设计者/年份 不适用（或地点欧洲）”，未发现编造人名、引文、出处或具体年份/作品。

## 九、总体结论与是否整批返工

- **抽样结果**：3 条中 **2 合格（balance、wayfinding）+ 1 待核实（gothic）+ 0 编造 + 0 硬不合格（无假第二源/无造假）**。
- **来源层面**：5 个引用来源 id 全部存在、verified=true；`balance` 的 getty、`wayfinding` 的 designingbuildings 两个第二源**均直接支撑、非泛论**；**`gothic` 的第二源根本未补——`data/sources.json` 无任何 LibreTexts/Vaulted Arch 来源，`gothic` 仍单源（source_count=1）**。这是本轮唯一实质缺陷。
- **结构层面**：三条 L2 七节完整、各 1 张 SVG 均含“示意图，非施工图”、元素无出界、风险/规范句齐备；`check.py` **PASS 0 errors**。
- **数据治理**：元数据逐项一致；`needs_verification↔pending↔待核实↔nvc` 三条**形式与实质均一致**（`gothic` 单源已如实披露）。
- **相似度**：①②两条口径三条**全部 <0.54**（0.37–0.49），无套话降级。
- **批次层面附带观察（供 lead 参考）**：第27轮 review-round27 列出的 12 条“可补第二源”目标中，**实际仅 9 条落地补入**（balance、geometry-symmetry、visual-movement、rhythm-repetition、postmodernism、plein-air、service-route、wayfinding、functional-zoning），**`leading-lines`、`gothic`、`axis` 三条仍为单源**（未落地）。本次抽中的 `gothic` 即属未落地之列。
- **是否建议整批返工**：**不建议对第27轮批次整批返工。** 依据：①无任何编造或“假第二源”造假；②`balance`、`wayfinding` 来源/七节/相似度/元数据全部合格，无需返工；③`gothic` 缺陷是**单条、单一动作**（一个已验证的源未登记追加），不涉及正文重写或来源相关性问题，影响面隔离。
  - **定向修正清单（仅 `gothic` 单条）**：①将 Humanity LibreTexts《7.3: The Vaulted Arch》（本轮复抓 HTTP200 192191B，正文直述 Pointed Arches/Ribbed Vaults/Flying Buttresses 用于 Gothic architecture，直接支撑、非泛论）以 `verified=true` 登记进 `data/sources.json`；②在 `gothic.sources` 追加该源，`coverage.source_count` 改 2；③`pending_notes`/「待核实」改为“核心已补第二独立来源；具体实例的设计者与年代待补充独立来源”；④复跑 `check.py` 复检。
  - **口径备选**：若质量闸采用宽松口径（“内容真实有源、单源已如实标待核实即不判硬不合格”），则 `gothic` 维持“待核实/需补源”定性、仅定向补齐单条即可，完全不触发整批返工。若采用严格口径（“每个补源条目必须实含 2 源”），则 `gothic` 记为单条不合格，**返工范围亦仅限 `gothic` 单条**，不牵连其余 11 条及整批。**两种口径下均不应对整批返工。**

---

### 机器可读汇总

```
ROUND=28
SAMPLER=spotcheck-r28
SCOPE=["balance","gothic","wayfinding"]   # 皆声称“第27轮补第二源”条目；grep 定位
FILES={"balance":"entries/batch-01.json","gothic":"entries/batch-02-d.json","wayfinding":"entries/batch-07.json"}
STATE={"sources.json":"110544B@22:45:32","batch-01.json":"80147B@22:45:32","batch-02-d.json":"17780B@22:45:32","batch-07.json":"15168B@22:45:32","coverage.json":"81955B@22:45:32"}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0) @~22:50"
FETCH_METHOD="urllib+ChromeUA; en.wikipedia canonical WinError10060 TIMEOUT -> owiki.org mirror; getty.edu/designingbuildings.co.uk/human.libretexts.org canonical HTTP200"
FETCH={
 "getty-principles-design":"CANONICAL 200 217965B PDF(1p) textlen2800; 'Balance is the distribution of the visual weight of objects, colors, texture, and space'; symmetrical/asymmetrical/radial; balance=6 visual weight=1",
 "designingbuildings-wayfinding":"CANONICAL 200 53663B title='Wayfinding - Designing Buildings' 6351c; 'Wayfinding is a method for relaying messages to help people navigate their way around a room, building or other unfamiliar environment'; 'Signage is the most common form of wayfinding...architectural features and other objects'; wayfinding=19 navigate=1 signage=8",
 "wp-composition-visual-arts":"OWIKI 200 25240B h1='Composition (visual arts)' 14838c; 'arranged in a balanced compositional way'; balance=3 symmetr=4",
 "wp-gothic-architecture":"OWIKI 200 128210B h1='Gothic architecture' 89402c; 'defining design element...pointed arch...pointed rib vault and flying buttresses'; 'prevalent in Europe from the late 12th to the 16th century'; gothic=245 pointed arch=30 ribbed vault=1 flying buttress=19",
 "wp-wayfinding":"OWIKI 200 20527B h1='Wayfinding' 10373c; 'orient themselves in physical space and navigate from place to place'; 'signage and other graphic communication, visual clues'; wayfinding=41 navigate=4 signage=7",
 "libretexts-gothic-CANDIDATE-NOT-REGISTERED":"CANONICAL 200 192191B title='7.3: The Vaulted Arch - Humanities LibreTexts'; 'Pointed Arches...commonly used in Gothic architecture...Ribbed Vaults...Flying Buttresses'; pointed arch=12 ribbed vault=10 flying buttress=15 gothic=27 -> 可作直接第二源但未写入sources.json"
}
SOURCES={"count_distinct":5,"all_verified_true":true,"wp-composition-visual-arts":{"verified":true,"link_ok":true},"getty-principles-design":{"verified":true,"link_ok":null,"type":"官方机构"},"wp-gothic-architecture":{"verified":true,"link_ok":true},"wp-wayfinding":{"verified":true,"link_ok":true},"designingbuildings-wayfinding":{"verified":true,"link_ok":null,"type":"学术百科"}}
SECOND_SOURCE={"balance":"getty-principles-design DIRECT(已补)","wayfinding":"designingbuildings-wayfinding DIRECT(已补)","gothic":"MISSING 未补(sources.json无LibreTexts源; gothic.sources仅1; coverage.source_count=1)"}
BODY_SUPPORT={
 "balance":"STRONG def(distribution of visual weight verbatim)+overview(symmetrical/asymmetrical)+原理/手法; 2 rel src; minor '大小' paraphrase",
 "gothic":"STRONG from SINGLE source(def pointed arch+rib vault+flying buttress; time 12-16c Europe; overview tracery+stained glass); NO 2nd source; gap honestly disclosed",
 "wayfinding":"STRONG def(orient/navigate+signage/visual clues)+overview+原理/手法; 2 rel src; minor '地图' paraphrase"
}
L2_CHECK={"seven_sections":"6/6 x3 + definition顶层, no missing/extra","svg":"1 each, all '示意图，非施工图'","svg_bounds":"no overflow (760x400)","risk_note":"'实际工程须按当地规范和专业设计人员的要求' x3"}
METADATA_CONSISTENCY={"title/theme/tier/period/region/level":"ALL OK x3","source_count matches actual":"balance 2=2, gothic 1=1, wayfinding 2=2","needs_verification=true & nvc=1 & pending=='待核实'":"formally & substantively OK x3 (gothic single-source honestly disclosed)"}
SIMILARITY={
 "balance":{"short":0.4000,"full_no_svg":0.4854,"vs":"rhythm-repetition"},
 "gothic":{"short":0.3768,"full_no_svg":0.4483,"vs":"renaissance-style/axis"},
 "wayfinding":{"short":0.3704,"full_no_svg":0.4494,"vs":"interior-exterior-transition/rhythm-repetition"},
 "threshold":0.54,
 "verdict":"short & full_no_svg ALL <0.54"
}
VERDICT={"balance":"合格","wayfinding":"合格","gothic":"待核实(内容成立+标注诚实,但第27轮补第二源未落实——实际单源;LibreTexts源未登记)"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
BATCH_CONTEXT="review-round27列12条可补第二源,实际落地9条; leading-lines/gothic/axis 仍单源未落地(本次抽中gothic)"
BATCH_REWORK="不建议整批返工(无造假/无假第二源;balance&wayfinding全合格;gothic为单条单动作缺陷)。定向补齐gothic单条: 登记LibreTexts(HTTP200已验证,直接支撑)→追加sources→source_count=2→改pending_notes→复跑check.py。严格口径下亦仅gothic单条返工,不牵连整批。"
```

*（报告完）*
