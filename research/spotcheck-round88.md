# 第88轮 质量抽检报告（spotcheck-round88）

- 抽检人：spotcheck-r88（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论）。
- 抽检对象（2 条，跨 2 个批次文件）：
  - `rule-of-odds`（奇数法则，L2/补充/理论/跨时期/全球）— 概念源：`dps-rule-of-odds`(Digital Photography School) + `expertphoto-rule-of-odds`(ExpertPhotography)；位 `entries/batch-37.json`；产物 `site/entries/rule-of-odds.html`。
  - `stippling`（点描法，L2/补充/理论/文艺复兴至19世纪/欧洲）— 概念源：`wp-stippling`(Wikipedia) + `artincontext-stippling`(Art in Context)；位 `entries/batch-42.json`；产物 `site/entries/stippling.html`。
- 本轮升级动作（据 `tools/apply_review_round88.py` 实读 + `git -c core.pager=cat diff` 实读 + `git diff --stat`）：
  - 仅改 **`实例`**（→ 类型性 / 不归于单一作品）、**`needs_verification` true→false**、**`pending_notes`→""**、**`待核实`→"暂无已知待核实项。"**。
  - **definition / overview / 原理 / 典型手法与适用条件 / SVG / sources 均未改**（`git diff --stat`：`entries/batch-37.json` 8 行、`entries/batch-42.json` 8 行，唯一逻辑字段是 `实例` 与 nv/pending/待核实）。
  - `coverage.json` 两条 `needs_verification_count` 1→0（实读 diff：第181、3236 行附近），`source_count` 各 2。
  - `site/entries/{rule-of-odds,stippling}.html`、`site/index.html` 为本轮 applier 重新生成的产物（`git diff --stat` 各 4/4/2 行）。
- 证据优先级：**独立实抓正文 > 当前文件实读 > git diff > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、计数、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round88.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式：`web_fetch` 本环境历史报错（DECISIONS D05），改用 **Python urllib + 浏览器 UA + 非校验 SSL（内存态 stdin 直跑，未落盘任何临时文件）**。
- 实抓 HTTP（四条均 200，内存态；正文去标签后字符数）：
  - `dps-rule-of-odds` = `https://digital-photography-school.com/the-rule-of-odds-in-photography-an-easy-trick-for-better-compositions/` → **200，198,510 B（正文 ~13,777 字）**；`odd`×61、`three`×22、`five`×10、`even`×11、`composition`×26。
  - `expertphoto-rule-of-odds` = `https://expertphotography.com/rule-of-odds-photography` → **200，101,725 B（正文 ~11,448 字）**；`odd`×21、`three`×17、`five`×5、`subjects`×16、`even`×6。
  - `wp-stippling` = `https://en.wikipedia.org/wiki/Stippling` → **200，91,865 B（正文 ~5,684 字）**；`dot`×6、`stipple`×10、`shading`×2，含定义句。
  - `artincontext-stippling` = `https://artincontext.org/stippling-art/` → **200，379,622 B（正文 ~24,117 字）**；`dot`×55、`shading`×17、`light`×21、`dark`×11、`tone`×8。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** `python -m pytest tests/test_svg_bounds.py -q`：`5 passed`（EXIT=0）。
- `git status --porcelain`（实读）：`M coverage.json / entries/batch-37.json / entries/batch-42.json / site/entries/rule-of-odds.html / site/entries/stippling.html / site/index.html` 及 `?? tools/apply_review_round88.py` 均为**本轮修复方（apply_review_round88.py）自身产物**，非本抽检所写；抽检方仅读取。

## 一、核对①：definition 是否由两独立源直接定义

### 1.1 rule-of-odds（奇数法则 = 奇数主体更生动）

端内 definition：『奇数法则指画面中主体数量取奇数更易形成生动均衡的构图经验。』
端内 overview：『奇数群体有中心与两侧，视觉更自然。』

| 要素 | dps-rule-of-odds（实抓原文） | expertphoto-rule-of-odds（实抓原文） | 判定 |
| --- | --- | --- | --- |
| 主体取奇数 / 非偶数 | 「The rule of odds states that, whenever possible, a composition should have an **odd number of objects, not an even number of objects**.」 | 「a composition guideline that suggests using an **odd number of main subjects, often three or five**.」 | **双源直证 ✓** |
| 奇数更生动/悦目 | 「arranging your subjects in odd numbers to craft compositions that are **naturally more pleasing to the eye**」「**aesthetically pleasing and impressively compelling**」「the viewer will look longer… moving between the individual elements」 | 「composition guideline」（正向构图法则）；「often three or five」 | **双源直证 ✓（dps 字面直述；expert 以 guideline + 三/五主体定义）** |
| 三或五个主体 | 「**Three** repeating shapes play to the rule of odds」「**Five** objects also adhere to the rule of odds!」 | 「often **three or five**」 | **双源直证 ✓** |
| 中心与两侧/一主两辅（视觉更自然） | 「With an odd number of objects, **one may become dominant**」「a group that can't be easily organized」 | 「one dominant subject with two supporting objects」 | **双源支撑 ✓（"dominated/一主两辅" 可对应 overview）** |
| 「均衡」字面 | 原文无 "balance"（该词仅出现在导航 "White Balance" 菜单） | 原文无 "balance"（仅相关文章标题 "Balance in Photography"） | **"均衡" 属释义性措辞（轻微引申）** |

- **判定：概念核心「主体取奇数、奇数更生动悦目、常取三或五」由 `dps-rule-of-odds` 与 `expertphoto-rule-of-odds` 两独立平台直接定义，非编造 ✓。唯一轻微措辞："均衡（balance）"两源正文均未直述（仅"pleasing / one dominant / look longer"语义），属可接受的释义性概括，非具名事实编造。**
- 附证（对本轮相似度/概念区分关键）：expert 原文直言 **「Unlike the rule of thirds, which guides where you place subjects in the frame, the rule of odds concerns how many subjects or distinct groups you include.」** ——两源分属独立摄影教育平台，且明确把「奇数法则=数量」与「三分法=位置」区分开。

### 1.2 stippling（点描 = 小点疏密表现明暗）

端内 definition：『点描法（Stippling）是以细点疏密表现明暗与形体的绘制技法。』
端内 overview：『点越密越暗、越疏越亮，靠点阵聚集塑造渐变。』

| 要素 | wp-stippling（实抓原文） | artincontext-stippling（实抓原文） | 判定 |
| --- | --- | --- | --- |
| 以细小点绘制 | 「the dots are made of pigment of a single colour, applied with a **pen or brush**」（点描主体即细点） | 「stippling art is a **drawing technique** that creates images and shapes on paper by making **small dots**」；「using small dots… ink, pencil, pen, even digital」 | **双源直证 ✓** |
| 点疏密决定明暗 | 「**the denser the dots, the darker the apparent shade**—or lighter, if the pigment is lighter than the surface.」 | 「When the dots are **further apart, it creates highlights**, or when **closer together, it creates shadows**.」 | **双源直证 ✓** |
| 塑造形体/体积 | （明暗 → 形体可推） | 「This will **form contours of a particular shape and give the image realism and depth**」 | **artin 直证 "shape/contour/depth" ✓** |
| 绘制技法（非单一作品） | 定义为技法（printmaking/drawing 中的 stipple technique） | 「**drawing technique**… create textures, shadows, and shading」 | **双源直证 ✓** |

- **判定：概念核心「细点 + 疏密→明暗 + 形体」由 `wp-stippling`（denser→darker shade）与 `artincontext-stippling`（closer→shadows / further→highlights；small dots 成形体体积）两独立平台直接定义，非编造 ✓。**

**小结（核对①）：两条 definition 的核心概念均由两独立平台直接定义：奇数法则=奇数主体更生动（dps+expert），点描法=小点疏密表现明暗（wp+artin）。均无具名事实编造。rule-of-odds 的"均衡"为轻微释义性措辞（两源正文无 "balance"），不构成超源事实主张。**

## 二、核对②：「类型性实例（不强行指认单一作品）」是否合理

**结论：两条的类型性处理均合理 ✓，与 `tints-shades` 先例同口径；且本轮对象本质是"构图法则/绘制技法"，比 round87 的传统造园手法更不适合归属于单一具名作品，类型化尤为贴切。**

- `rule-of-odds`：端内实例=『名称：奇数主体的构图（类型性，构图法则不归于单一作品）；以画面中排布 3 或 5 个主体、避免呆板的偶数对称。』
  - 两源均把其作为**通用构图法则/guideline**（dps「rule」、expert「composition guideline」）陈述，非某一具体作品的专有属性；dps 举的灯笼/手套/镐三元素、花卉小群等仅为**说明性照片**，非需署名的canonical作品。强行指认单一作品反而不当。**类型性合理 ✓**。
- `stippling`：端内实例=『名称：点描明暗练习（类型性，技法不归于单一作品）；以细点疏密由亮到暗逐层加密，塑造明暗与体积。』
  - 两源均定义为 **drawing technique**（技法）；虽提到历史人物（Campagnola、stipple engraving ~1510），但技法本身不隶属于某一作品。**类型性合理 ✓**。
- **先例一致（实读库内条目）**：`tints-shades`（batch-37，nv=false）实例=『名称：明度色阶练习（同一色相加白/加黑得到的明度梯度）；地点与作者不适用。』——同样把"技法/练习"作**类型性、地点作者不适用**处理并 nv=false。本轮两条与之一脉相承 ✓。
- **是否编造具体事实：否（无具名作品/作者/年代被杜撰）。** 两条实例都明确标注"类型性…不归于单一作品 / 此处仅列说明，不复制图像"，无杜撰。

## 三、核对③：nv=false 是否有据

**结论：两条 nv=false 均有据 ✓。**

- 结构自洽（两条均）：`needs_verification=false`、`pending_notes=""`、`待核实`="暂无已知待核实项。"；`coverage.json` 记 `needs_verification_count=0`、`source_count=2`（实读覆盖条目相符）——四处一致。
- "验证状态"绑定"关键概念是否双源可核"（DECISIONS D10）：
  - `rule-of-odds`：概念双源直证（§1.1）→ 满足 D10 双源；实例类型性、无单一作品可核风险 → **nv=false 成立 ✓**。
  - `stippling`：概念双源直证（§1.2）→ 满足 D10 双源；实例为技法类型性、无单一作品可核风险 → **nv=false 成立 ✓**。
- 与 round87 对照：round87 的 `opposed-scenery`（概念实质单源 peopleapp）、`korean-architecture`（院落单源+超源+springer 不可核）因 D10 不足被判待核实；**本轮两条不存在该问题——概念均双源直证、无超源具名事实、来源全部实抓 200 可核**，故升级 nv=false 依据充分。
- 既有的旧 pending（"具体实例（作品名称、作者、年代）待补充独立来源"）对"通用法则/技法"属过度要求；本轮改为类型性并清除该 pending，逻辑自洽。

## 四、核对④：七节 / SVG / 规范句 / 结构校验

| 核对项 | rule-of-odds | stippling |
| --- | --- | --- |
| 七节齐（definition+overview + 6 节：原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | ✓ 7 节 | ✓ 7 节 |
| SVG 数量/画布 | ✓ 1 张，`viewBox 0 0 760 400`，含「示意图，非施工图」 | ✓ 同 |
| SVG 禁用元素 | ✓ 无 `<script>/javascript:/href=/<image/<iframe/url(/on*=` | ✓ 同 |
| SVG 越界（实算 bbox） | ✓ polygon x[202..558] y[122..300]、line x[140..620] y=300、text x40 y40、尾注 x300 y375，均在 0..760 / 0..400 内 | ✓ circle1 cx250 cy200 r90 → x[160..340] y[110..290]；circle2 cx480 cy200 r70 → x[410..550] y[130..270]；text x40 y40、尾注 x300 y385，均在框内 |
| 规范句 | ✓ 常见错误与限制收尾含「实际工程须按当地规范和专业设计人员的要求」 | ✓ 同 |
| nv / pending / 待核实 一致 | ✓ nv=false、pending=""、待核实="暂无已知待核实项。" | ✓ 同 |
| check.py | ✓ PASS（0 errors，EXIT=0） | ✓ 同 |
| pytest test_svg_bounds | ✓ 5 passed（EXIT=0） | ✓ 同 |

- 注：本轮 SVG 均**未改**（diff 只动实例/nv），两条 bbox 均在 viewBox 内，无 round87 那类 ellipse 越顶预存问题。

## 五、核对⑤：相似度（阈值 0.54；重点 rule-of-odds vs rule-of-thirds）

方法：`difflib.SequenceMatcher`，归一化=**去全部空白+小写**（与 round86/87 口径一致；该口径下全库最高 `value↔saturation 0.5437`、>0.54 对数=1，与 round86/87 完全复现）。全库 **258** 条两两比对（33,153 对）。分「短口径(标题|定义|时间地点|概述)」「def+overview」「全字段(短+6节)」「去模板正文」多档。

### 5.1 全库与目标（当前磁盘态）

| 口径 | 全库最高对 | 全库 >0.54 对数 | rule-of-odds 最高 | stippling 最高 |
| --- | --- | --- | --- | --- |
| 短口径 | value↔saturation **0.5437**（预存） | **1**（仅它，预存；两目标不在列） | 0.4889 与 rule-of-thirds | 0.4062 与 hatching |
| def+overview | leaked-scenery↔time-scenery 0.4192 | 0 | 0.3469 与 rule-of-thirds | 0.3529 与 hatching |
| 全字段(短+6节) | loop-route↔serial-route 0.5311 | 0 | 0.3536 与 stippling | 0.3536 与 rule-of-odds |
| 去模板正文 | loop-route↔serial-route 0.4793 | 0 | 0.2206 与 yaodong | 0.1797 与 rule-of-odds |

- **两目标在所有口径下最高均 <0.54**；全库唯一 >0.54 的 `value↔saturation`（0.5437）为**既往预存**，与本轮无关。

### 5.2 指定关注对（全部 <0.54）

| 对 | 短 | def+ov | 全字段 | 去模板 |
| --- | --- | --- | --- | --- |
| **rule-of-odds ↔ rule-of-thirds** | **0.4889** | 0.3469 | 0.2809 | 0.1843 |
| rule-of-odds ↔ tints-shades | 0.2331 | 0.0820 | 0.3090 | 0.1653 |
| rule-of-odds ↔ stippling | 0.2166 | 0.1373 | 0.3536 | 0.1797 |
| stippling ↔ hatching | 0.4062 | 0.3529 | — | — |

- **rule-of-odds ↔ rule-of-thirds 全口径最高 0.4889（短口径）仍 <0.54，安全。** 且二者概念本质不同：rule-of-thirds=**主体放置位置（三分网格/交点）**，rule-of-odds=**主体数量（奇数 3/5）**——expert 源原文直证二者是不同法则（§1.1）。0.4889 的偏高主要来自标题/时间地点/概述的公共措辞（"构图/视觉/主体"），非机制重复，边界可辨。
- **stippling 最接近为 hatching 短口径 0.4062（<0.54）**：一为小点疏密、一为排线叠加，机制分层，可辨。
- rule-of-odds 与 tints-shades（先例条目）相似度均 <0.32，无模板耦合。

### 5.3 结论
**相似度：合格。** 无新引入的 >0.54 对；两目标与任何条目均安全；rule-of-odds 与其近邻 rule-of-thirds 最高 0.4889 <0.54 且概念可分（位置 vs 数量，源可直证）。

## 六、单源 / 超源 / 编造支撑点（按要求指出）

| 条目 | 要点 | 支撑情况 | 判定 |
| --- | --- | --- | --- |
| **rule-of-odds** | **概念核心（奇数主体更生动、常取三或五、非偶数）** | **dps + expert 双独立源直证**（"odd number… not even" / "odd number of main subjects, often three or five" / "naturally more pleasing"） | ✓ 双源，无单源要害 |
| rule-of-odds | 「均衡（balance）」字面 | 两源正文无 "balance"（仅导航/相关文章标题出现）；语义近 "pleasing/one dominant/look longer" | 轻微释义性措辞（可保留，非具名事实编造） |
| **stippling** | **概念核心（细点 + 疏密→明暗 + 形体）** | **wp + artin 双独立源直证**（"denser the dots, the darker the apparent shade" / "closer together, it creates shadows… further apart… highlights"） | ✓ 双源，无单源要害 |
| stippling | 时间地点「1510 年前后起源于意大利」 | wp 载 "The Young Shepherd… by Giulio Campagnola, around 1510"；artin 亦述 Campagnola | ✓ 有据（非本轮改动项，仅核不虚） |
| 两源独立性 | dps(Digital Photography School) vs expert(ExpertPhotography)；wp(Wikipedia) vs artin(Art in Context) | 均为**不同独立平台** | ✓ 满足"两独立平台" |
| 编造具名事实 | 两条实例均"类型性…不归于单一作品…仅列说明，不复制图像" | 无具名作品/作者/年代杜撰 | ✓ 无编造 |

- 未发现单源概念或超源具名事实；唯一可记的措辞点是 rule-of-odds 的"均衡"为释义性词汇（不影响双源判定）。
- 参考建议（非阻断，可选）：`rule-of-odds` 的 `related` 现为空 `[]`，而 `rule-of-thirds` 与其概念最近（同为构图法则，相似度全库对其最高）；可在后续将其列入 `related` 互链以提升站内导览（纯编辑优化，不影响本轮合格判定）。

## 七、抽检结论（逐条）

### rule-of-odds（奇数法则）
- **内容/来源：合格** — 概念核心「主体取奇数、奇数更生动悦目、常取三或五」由 `dps-rule-of-odds`（"odd number… not an even number"、"naturally more pleasing to the eye"、"Three/Five objects"）与 `expertphoto-rule-of-odds`（"odd number of main subjects, often three or five"）两独立平台直接定义，非编造。
- **类型性/nv：合格** — 奇数法则为通用构图法则（非单一作品属性），类型性实例贴切、非编造，与 `tints-shades` 先例同口径；nv=false 四处结构自洽且概念双源，成立。
- **结构：合格** — 七节齐、规范句在、SVG 合规（bbox 在框内）、check.py PASS、pytest 5 passed。
- **相似度：合格** — vs rule-of-thirds 最高 0.4889 <0.54（概念"数量"vs"位置"可辨），其余口径更低。
- **综合判定：合格**（minor：definition/overview 的"均衡"为两源正文未直述的释义性措辞，可保留；可选把 rule-of-thirds 列入 `related` 互链）。

### stippling（点描法）
- **内容/来源：合格** — 概念核心「细点 + 疏密→明暗 + 形体」由 `wp-stippling`（"the denser the dots, the darker the apparent shade"）与 `artincontext-stippling`（"small dots"、"closer together, it creates shadows… further apart… highlights"、"form contours… realism and depth"）两独立平台直接定义，非编造。
- **类型性/nv：合格** — 点描为绘制技法（非单一作品），类型性实例贴切、非编造，与 `tints-shades` 先例同口径；nv=false 四处结构自洽且概念双源，成立。
- **结构：合格** — 七节齐、规范句在、SVG 合规（bbox 在框内）、check.py PASS、pytest 5 passed。
- **相似度：合格** — vs hatching 最高 0.4062 <0.54，与 rule-of-odds 最高 0.3536，均安全。
- **综合判定：合格**（无实质缺陷）。

**总判定：本轮 2 条（`rule-of-odds`、`stippling`）均合格。** 核心：两条 definition 均由两独立平台直接定义（奇数法则=奇数主体更生动，dps+expert；点描=小点疏密表现明暗，wp+artin），无单源概念、无超源具名事实、无编造；实例类型性处理合理（构图法则/绘制技法不归于单一作品），与 `tints-shades` 先例同口径；nv=false 依据充分。结构（七节/SVG/规范句/check.py PASS/ pytest 5 passed）合规；相似度全口径 <0.54、rule-of-odds vs rule-of-thirds 最高 0.4889 <0.54 且概念可分。唯一轻微点：rule-of-odds 的"均衡"为释义性措辞（两源正文无 "balance"），不影响合格。

## 八、机器可读汇总

```
ROUND=88
SAMPLER=spotcheck-r88
SCOPE=["rule-of-odds","stippling"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round87.md","entries/batch-37.json","entries/batch-42.json","entries/batch-01.json(rule-of-thirds)","data/sources.json(4 srcs)","coverage.json(2 entries)","tools/apply_review_round88.py","git diff/stat/status/log","4 live pages"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
PYTEST_SVG="5 passed (EXIT=0)"
FETCH_METHOD="urllib+browserUA+unverified-SSL, in-memory via python stdin (no temp files)"
FETCHES={"dps-rule-of-odds":200,"expertphoto-rule-of-odds":200,"wp-stippling":200,"artincontext-stippling":200}
ROUND88_CHANGES={"实例":"both edited -> 类型性/不归于单一作品","needs_verification":"true->false (both)","pending_notes":"-> ''","待核实":"-> 暂无已知待核实项。","definition/overview/原理/典型手法/svg/sources":"unchanged","coverage.nv_count":"1->0 (both)","applier":"tools/apply_review_round88.py"}
DEFINITION_DUAL_DIRECT={
 "rule-of-odds":{"odd_not_even":"dps 'odd number of objects, not an even number' + expert 'odd number of main subjects, often three or five'","more_vivid":"dps 'naturally more pleasing to the eye'/'aesthetically pleasing'","three_or_five":"dps 'Three/Five objects' + expert 'often three or five'","balance_word":"NOT literal in either source body (nav/related only) -> light gloss","dual_source":true,"fabricated_named":false},
 "stippling":{"small_dots":"wp 'dots applied with pen or brush' + artin 'drawing technique... small dots'","density_to_shade":"wp 'the denser the dots, the darker the apparent shade' + artin 'closer together->shadows, further apart->highlights'","form_volume":"artin 'form contours... realism and depth'","dual_source":true,"fabricated_named":false}}
INSTANCE_TYPE_LEVEL={"all":true,"rationale":"构图法则/绘制技法, no single work; matches tints-shades(batch-37,nv=false) precedent exactly","fabricated":false}
NV_FALSE_GROUNDED={"rule-of-odds":true,"stippling":true,"reason":"both concept dual-direct + type-level instance + all sources HTTP200 verifiable (contrast round87 opposed/korean)","structure_consistent":"four-way (nv=false/pending=''/待核实/coverage nv_count=0/source_count=2)"}
STRUCTURE={"seven_sections":7,"svg_count":1,"svg_forbidden":[],"reg_sentence":true,"check_py":"PASS","pytest":"5 passed","svg_overflow":{"rule-of-odds":"none bbox x[40..620] y[40..375]","stippling":"none bbox circle1 x[160..340]y[110..290], circle2 x[410..550]y[130..270]"}}
SIMILARITY={"threshold":0.54,"entries":258,"pairs":33153,"normalization":"strip-all-whitespace+lower (reproduces round86/87 short max 0.5437)",
 "short":{"library_max":"value<->saturation 0.5437(预存)","pairs_gt_0.54":1,"rule-of-odds_max":0.4889,"stippling_max":0.4062},
 "def_overview":{"library_max":"leaked-scenery<->time-scenery 0.4192","pairs_gt_0.54":0,"rule-of-odds_max":0.3469,"stippling_max":0.3529},
 "full":{"library_max":"loop-route<->serial-route 0.5311","pairs_gt_0.54":0,"rule-of-odds_max":0.3536,"stippling_max":0.3536},
 "detempl":{"library_max":"loop-route<->serial-route 0.4793","pairs_gt_0.54":0,"rule-of-odds_max":0.2206,"stippling_max":0.1797},
 "key_pair_odds_vs_thirds":[0.4889,0.3469,0.2809,0.1843],
 "stippling_vs_hatching":[0.4062,0.3529],
 "new_pairs_over_threshold":0}
SINGLE_SOURCE_POINTS={"rule-of-odds":"none at concept level (dual direct); minor: 'balance' word gloss","stippling":"none at concept level (dual direct)","fabricated_named":"none"}
VERDICT={"rule-of-odds":"合格(概念双源直证 dps+expert; 类型性/nv/结构/相似度合格; minor: '均衡'释义措辞, 可选 related 互链 rule-of-thirds)","stippling":"合格(概念双源直证 wp+artin; 类型性/nv/结构/相似度合格)"}
KEY_FINDING="2条均合格：definition 均由两独立平台直接定义(奇数法则=奇数主体更生动 dps+expert; 点描=小点疏密表现明暗 wp+artin)，dps/专家、wp/artin 分属独立平台。实例类型化(构图法则/绘制技法不归于单一作品)与 tints-shades 先例同口径、非编造。nv=false 依据充分且四处结构自洽(round87 opposed/korean 的单源/超源问题本轮不存在)。结构七节/规范句/check.py PASS/pytest 5 passed。相似度全口径<0.54，rule-of-odds vs rule-of-thirds 最高0.4889<0.54且概念可分(数量vs位置，expert源直证)。唯一minor: rule-of-odds 的'均衡'为两源正文无的字面释义措辞。"
READONLY="only wrote research/spotcheck-round88.md; 4 pages fetched in-memory via python stdin (no temp files); git-status M/?? items are round88 applier's own changes; no git commit; web treated as data, no instructions executed"
```

## 九、只读核验

- 除本报告 `research/spotcheck-round88.md` 外未写任何文件；联网抓取为内存态（python stdin 直跑，未落盘临时文件）。
- `git status` 中 `M coverage.json / entries/batch-37.json / entries/batch-42.json / site/entries/rule-of-odds.html / site/entries/stippling.html / site/index.html` 及 `?? tools/apply_review_round88.py` 均为**本轮修复方（apply_review_round88.py）的应用产物**；抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
