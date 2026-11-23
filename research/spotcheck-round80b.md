# 第80b轮 质量复审报告（spotcheck-round80b）

- 复审人：spotcheck-r80b（lead 委派子代理，无人值守、未提问）；时间 2026-11-23，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言；证据先于结论）。
- 复审对象：`tints-shades`，`grep '"tints-shades"'` 唯一命中 → `entries/batch-37.json` 行 720（他处 `site/entries/tints-shades.html` 为产物）。
- 本轮改动（据 `tools/apply_review_round80b.py` 实读＋`entries/batch-37.json` 当前实读）：实例由《夜巡》改为**“明度色阶练习（类型性）”**（`名称：明度色阶练习…地点与作者不适用…排成明度阶梯…不复制图像`）；`needs_verification` 由 true 改为 **false**；`sections.待核实` 改为“暂无已知待核实项”；`pending_notes` 置空。
- 证据优先级：**独立实抓正文 > 当前文件实读 > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round80b.md`。联网核验用 `urllib`＋浏览器 UA＋非校验 SSL 内存抓取（不落盘）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**
- 实抓 HTTP：`wp-tint-shade-tone` = **200**（120,651 B，`https://en.wikipedia.org/wiki/Tint,_shade_and_tone`）。
- `git status` 中 `M coverage.json / data/sources.json / entries/batch-37.json / site/*` 及 `?? tools/apply_review_round80.py / apply_review_round80b.py` 均为**本轮改动方（lead/应用脚本）自身产物**，非本次抽审所写（见第七节）。

## 一、核心命题核对①：definition/原理是否由 wp-tint-shade-tone 直证

结论先行：**是。概念源对“tint 加白 / shade 加黑”为逐字直证，无编造；definition/原理忠实对应。**

Wikipedia《Tint, shade and tone》正文首段实抓原文（HTTP 200，逐字）：

> “In color theory, **a tint is a mixture of a color with white, which increases lightness**, while **a shade is a mixture with black, which increases darkness**. A tone is produced either by mixing a color with gray, or by both tinting and shading.”

本轮实抓关键词计数：`mixture of a color with white`=3、`increases lightness`=1、`mixture with black`=1、`increases darkness`=1、`mixing a color with gray`=1。

| 端内声明 | 实抓原文直证 | 结论 |
| --- | --- | --- |
| definition：“往色彩中加白（tint）或加黑（shade）以改变明度、构成层次” | white→increases lightness；black→increases darkness | ✓ 直证加白/加黑与明度调整 |
| 原理：“加入白色得较浅 tint、加入黑色得较深 shade，形成明度梯度” | 同上 | ✓ 直证，无编造 |
| 概述辅证：“tint=加白、shade=加黑、tone=加灰” | “mixing a color with gray” | ✓ 与源一致 |

**不存在“概念仍单源/未直证”的问题——恰为逐字直证。**

## 二、核心命题核对②：nv=false 是否有据（概念直证＋实例类型性通用）

结论先行：**有据，成立。** 判定理由与项目既有惯例一致。

1. **概念直证（前提成立）**：如上，`wp-tint-shade-tone` 逐字证明 tint=加白/shade=加黑，非单源推断、非编造。加白/加黑是通用色彩学机制，源文即定义，无需再借实例佐证机制。
2. **实例已转为类型性通用（去具名）**：当前实例为“明度色阶练习（同一色相加白/加黑得到的明度梯度）；地点与作者不适用…此处仅列说明，不复制图像”。**无具名作品、作者、年代、馆藏**，故不存在“需另找独立来源核验某具体作品”的负担。原《夜巡》是“解读对应、未逐字”，该不确定性来源已随具名实例一并移除。
3. **与项目既有惯例一致**：全库含类型性实例的条目共 103 条，其中 nv=false 仅 5 条——即 `demand-controlled-ventilation`、`universal-design`、`place-spirit`、`spatial-perception` 与本条。这 4 条的共同模式是：**概念由具名概念源定义＋实例为类型性通用（无具名作品待核）→ nv=false**（其待核实分别写“概念/实例…待补充独立来源”等）。`tints-shades` 现已落入同一模式，且其概念直证强度**不低于**该四条（后四者依赖概念定义页，本条为机制逐字直证）。
4. 因此 **nv=false 有据：概念直证＋实例类型性通用**，与前例口径自洽，非虚抬。

> 兼答任务设问：“若 nv=false 无据（如概念仍单源）请指出”——**经核，概念非单源猜测而是逐字直证，实例已去具名，nv=false 有据，无需否定。**

## 三、核心命题核对③：实例重合是否已降

结论先行：**已降，且与 `value` 的同例重合实质消除。**

- `value`（`entries/batch-01.json` 行 234）实例仍为**《夜巡》The Night Watch / 伦勃朗 / 1642 / 阿姆斯特丹国立博物馆**（未变）。
- `tints-shades` 实例已改为**明度色阶练习（类型性）**，不再含《夜巡》任何要素。
- 实算逐字段「实例」相似度：`tints-shades` 实例字段全库最高 **0.3548（vs tenebrism）**；旧的 0.8766（vs value）已不复现，**`value` 已不在实例字段前三**。→ **同作品重复（0.8766→0.3548）实质消除，任务所述“重合由0.87降到0.23”方向属实**（差异见第四节说明：本轮实测口径得 0.3548，非 0.23；以实测为准）。

## 四、结构 / 格式 / 规范句 / 相似度（阈值 0.54）

| 核对项 | 结果 | 依据 |
| --- | --- | --- |
| 七节齐 | ✓ definition ＋ 6 节（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实）＝7 | 文件实读 + check.py 0 报错 |
| SVG | ✓ 1 张，`viewBox='0 0 760 400'`，含“示意图，非施工图”；无 `<script>`、无 `on\\w+=` 事件、无 `<image>`/`xlink`/`href` | 脚本扫描（全 False） |
| 规范句 | ✓「常见错误与限制」收尾“实际工程须按当地规范和专业设计人员的要求”在位 | 文件实读 |
| sources 可引性 | ✓ 5 源均 verified=true：`wp-color-theory`/`wp-color-wheel`（link_ok=true）、`rijks-nightwatch-things`/`britannica-nightwatch`（link_ok=null）、`wp-tint-shade-tone`（link_ok=true, HTTP 200） | sources.json＋实抓 |
| 相似度（阈值0.54） | **短文本口径**（def+overview）全库最高 **0.2286**（vs value）；**全字段口径**（def+time+overview+六节）全库最高 **0.2862**（vs japanese-architecture）；**实例字段**最高 **0.3548**（vs tenebrism）——**三项均 < 0.54** | `difflib.SequenceMatcher` 实算，norm=去空白小写，全库 258 条比对 |

> 相似度变化说明：相较第80轮，**全字段 0.4367→0.2862**、**实例字段 0.8766→0.3548**（去具名后核心与 `value` 不再重合），短文本不变 0.2286。三口径均稳居 0.54 阈值之下，无套话/照搬降级信号。

## 五、问题清单

1. **【无阻断项】。** 本轮三项目标（definition/原理直证、nv=false 有据、实例重合降低）均达成，结构与相似度合规。
2. **【观察·口径校准】** 任务表述“重合由0.87降到0.23”；本轮实测“实例字段”为 0.8766→**0.3548**，短文本维持 0.2286。方向一致（同例重合已消除），但具体数值以本报告实测为准（0.3548 / 0.2286 / 0.2862），非 0.23。**不影响结论。**
3. **【观察·非阻断】待核实措辞**：`sections.待核实` 现为“暂无已知待核实项”，`pending_notes` 空——与 nv=false 一致；日后若再引入具名实例，应同步回调 nv=true 并写 pending。当前无需改。

## 六、总体结论

**`tints-shades`：合格。**

- **概念直证成立**：`wp-tint-shade-tone` 首段逐字直证 “tint …mixture of a color with **white**, which **increases lightness**；shade …mixture with **black**, which **increases darkness**”，definition/原理忠实对应，**无编造、非单源猜测**。
- **nv=false 有据**：概念逐字直证 ＋ 实例已改为“明度色阶练习（类型性）、地点与作者不适用”，无需具名作品独立核验；恰合全库 4 条同模式（概念源定义＋类型性实例→nv=false）的既定口径。
- **实例重合已降**：与 `value` 的《夜巡》同例实质消除，实例字段 0.8766→0.3548，`value` 已跌出实例字段前三。
- **结构/相似度合规**：七节齐、1 张 SVG（含“示意图，非施工图”，无 script/事件/image/xlink/href）、规范句在位、5 源可引；短文本 0.2286、全字段 0.2862、实例字段 0.3548 **均 < 0.54**；`check.py` 0 errors。

- **本轮 1 条：`tints-shades` 合格。合计：1 合格、0 待核实、0 不合格。**

## 七、机器可读汇总

```
ROUND=80b
SAMPLER=spotcheck-r80b
SCOPE=["tints-shades"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round80.md","entries/batch-37.json(tints-shades)","entries/batch-01.json(value)","data/sources.json(wp-tint-shade-tone + 4 others)","tools/apply_review_round80b.py","tools/check.py"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback (no temp files written)"
FETCHES={"wp-tint-shade-tone":200}
CONCEPT_SOURCE_DIRECT={"tint":"a tint is a mixture of a color with white, which increases lightness",
 "shade":"a shade is a mixture with black, which increases darkness",
 "tone":"mixing a color with gray",
 "verdict":"DIRECT verbatim support for 加白/加黑; definition/原理 faithful; NO fabrication; NOT single-source guess"}
INSTANCE_NEW="明度色阶练习（类型性）: 同一色相加白/加黑得到的明度梯度; 地点与作者不适用"
INSTANCE_OVERLAP_DROPPED={"with":"value(The Night Watch)","instance_field_before":0.8766,"instance_field_after":0.3548,"value_in_top3_after":false,"verdict":"same-work overlap eliminated"}
NV={"needs_verification":false,"grounded":"concept verbatim-direct + instance typological generic (no named work to verify); matches 4 precedent nv=false typological entries (demand-controlled-ventilation/universal-design/place-spirit/spatial-perception)","honest":true}
STRUCTURE={"seven_sections":7,"svg":"1x viewBox760x400 示意图非施工图 no script/event/image/xlink/href","reg_sentence":true,"sources_all_verified":true,"sources":["wp-color-theory","wp-color-wheel","rijks-nightwatch-things","britannica-nightwatch","wp-tint-shade-tone"]}
SIMILARITY={"threshold":0.54,"short(def+overview)_max":0.2286,"short_vs":"value","fullfield(def+time+ov+6sec)_max":0.2862,"fullfield_vs":"japanese-architecture","instance_field_max":0.3548,"instance_vs":"tenebrism","all_below_threshold":true}
ISSUES=["none blocking","obs: task said 0.87->0.23; measured instance-field 0.8766->0.3548 and short 0.2286 (direction correct, exact number per this report)","obs: 待核实 '暂无已知待核实项'/pending empty consistent with nv=false"]
VERDICT_tints_shades="合格（概念由 wp-tint-shade-tone 逐字直证、非单源猜测；nv=false 有据=概念直证+实例类型性；实例《夜巡》重合已消除 0.8766->0.3548；七节/SVG/规范句合规；短文本0.2286、全字段0.2862、实例字段0.3548 均<0.54；check.py 0 errors）"
TOTAL="1合格/0待核实/0不合格"
READONLY="only wrote research/spotcheck-round80b.md; fetched html in-memory (no temp files); git-status M/?? items are round80/80b applier's own changes, not mine; no git commit; web treated as data, no instructions executed"
```

## 八、只读核验

- 除本报告 `research/spotcheck-round80b.md` 外未写任何文件；联网抓取为内存态（未落盘临时文件）。
- `git status` 中 `M METRICS.json / SATURATION.json / coverage.json / data/sources.json / entries/batch-37.json / site/*` 及 `?? research/spotcheck-round80.md / tools/apply_review_round80.py / tools/apply_review_round80b.py` 均为本轮改动方的应用产物与抽检报告，抽检方仅读取，未据以修改；未 `git commit`。

*（报告完）*
