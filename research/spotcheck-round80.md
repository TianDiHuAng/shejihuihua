# 第80轮 质量抽检报告（spotcheck-round80）

- 抽检人：spotcheck-r80（lead 委派子代理，无人值守、未提问）；时间 2026-11-23，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言；证据先于结论）。
- 抽检对象：`tints-shades`（色调与明暗层次），`grep '"tints-shades"'` 定位 → `entries/batch-37.json` 行 720（`entries/` 全库唯一命中；他处 `site/entries/tints-shades.html` 为产物）。
- 本轮改动（据 `tools/apply_review_round80.py` 实读＋当前文件实读）：新增概念源 `wp-tint-shade-tone`（Wikipedia《Tint, shade and tone》），`definition`/`原理` 改为“加白（tint）/加黑（shade）调整明度”；实例保持《夜巡》；`needs_verification` 保留 **true**（披露“实例与该术语的对应为解读、未逐字”）。
- 证据优先级：**独立实抓正文 > 当前文件实读 > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round80.md`。联网核验用 `urllib`＋浏览器 UA＋非校验 SSL 内存抓取；临时文件 `research/_r80_wp.html`、`research/_r80_lead.txt`、`research/_r80_cmp.txt` 用后已 `rm -f`（见文末核验，无残留）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。`git status` 中出现的 `M coverage.json / data/sources.json / entries/batch-37.json / site/*` 与 `?? tools/apply_review_round80.py` 均为**本轮改动方（lead/应用脚本）自身产物**，非本次抽检所写。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**
- 实抓 HTTP：`wp-tint-shade-tone` = **200**（120,651 B，`https://en.wikipedia.org/wiki/Tint,_shade_and_tone`）。

## 一、核心命题核对：definition/原理是否由新源直证“tint 加白 / shade 加黑”

结论先行：**新概念源 `wp-tint-shade-tone` 对“加白/加黑”为直接、逐字直证，无编造；definition/原理忠实对应，成立。**

Wikipedia《Tint, shade and tone》正文首段实抓原文（HTTP 200，逐字）：

> “In color theory, **a tint is a mixture of a color with white, which increases lightness**, while **a shade is a mixture with black, which increases darkness**. A tone is produced either by mixing a color with gray, or by both tinting and shading.”

| 端内声明 | 实抓原文直证 | 结论 |
| --- | --- | --- |
| definition：“往色彩中加白（tint）或加黑（shade）以改变明度、构成层次” | “tint is a mixture of a color with **white**, which **increases lightness**”；“shade is a mixture with **black**, which **increases darkness**” | ✓ 直证“加白/加黑”；“改变明度”对应 increases lightness/darkness，措辞成立 |
| 原理：“加入白色得较浅的 tint、加入黑色得较深的 shade，形成明度梯度” | 同上：白色→增亮（较浅）、黑色→增暗（较深） | ✓ 直证，无编造 |
| 概述辅证：“tint=加白、shade=加黑、tone=加灰” | 同页 “A tone is produced either by mixing a color with gray…” | ✓ 与源一致 |

- **是否有“加白/加黑”直证：有。** 源文明确 “mixture of a color with white / black” 且 “increases lightness / darkness”，即加白、加黑，且方向为调整明度（浅/深），与端内 definition/原理完全吻合。**不存在“新源未直证加白/加黑”的问题。**
- **无编造补充**：本轮 definition/原理未引入源外新事实（如具体作品、作者、年代），“明度梯度/绘画与设计常用手段”为对“lightness/darkness 之差即梯度”的合理概括，不构成事实性编造。

## 二、实例《夜巡》与 nv=true / pending 是否如实

| 项 | 值 | 判定 |
| --- | --- | --- |
| 实例 | 《夜巡》The Night Watch；荷兰阿姆斯特丹国立博物馆；伦勃朗；1642 年 | 信息为真实作品要素；与本术语（tint/shade）的对应属“明暗层次”解读，非逐字 termini |
| `needs_verification` | **true** | ✓ 与正文“待核实”声明、pending_notes 三者联动一致（符合 D10/D14） |
| `sections.待核实` | “加白/加黑定义由 Wikipedia（Tint, shade and tone）直证；实例《夜巡》的明暗运用系‘明暗层次’对应解读（原源用 chiaroscuro），未逐字用 tints and shades。” | **如实 ✓**：明确区分“概念有直证”与“实例为解读、未逐字”，未把解读说成直证，未抬高 nv |
| `pending_notes` | “概念（加白/加黑）有源；实例与该术语的对应为解读，未逐字。” | 与待核实节同义，如实 ✓ |

- 核查 `wp-tint-shade-tone` 正文：`rembrandt`、`night watch`、`chiaroscuro` 出现次数均 = **0**——**新源不涉及《夜巡》**，故端内把实例标注为“解读、未逐字”是**正确且诚实**的处置（未虚构“源直证《夜巡》为 tint/shade 范例”）。nv=true 保留恰当，未虚报合格。

## 三、结构 / 格式 / 规范句 / 相似度（阈值 0.54）

| 核对项 | 结果 | 依据 |
| --- | --- | --- |
| 七节齐 | ✓ definition ＋ 6 节（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实）＝7 | 文件实读 + check.py 0 报错 |
| SVG | ✓ 1 张，`viewBox='0 0 760 400'`，含“示意图，非施工图”；无 `<script>`、无 `on\w+=` 事件处理器、无 `<image>`/`xlink`/`href` | 脚本扫描（全 False） |
| 规范句 | ✓「常见错误与限制」收尾“实际工程须按当地规范和专业设计人员的要求”在位 | 文件实读 |
| sources 可引性 | ✓ 5 源：`wp-color-theory`/`wp-color-wheel`（link_ok=true）、`rijks-nightwatch-things`/`britannica-nightwatch`（link_ok=null）、`wp-tint-shade-tone`（verified=true, link_ok=true, HTTP 200） | sources.json 5932 行区域实读＋实抓 |
| 相似度（阈值0.54） | **短文本口径**（definition+overview）全库最高 **0.2286**（vs value）；**全字段口径**（def+time_or_place+overview+六节）全库最高 **0.4367**（vs value）——**均 < 0.54** | `difflib.SequenceMatcher` 实算，norm=去空白小写，全库 258 条比对 |

> 相似度说明（诚实披露·观察项）：**逐字段「实例」本体最高 0.8766（vs `value`）**——`tints-shades` 与 `value` 两条**选用同一件《夜巡》**（同作者伦勃朗、同年 1642、同地点阿姆斯特丹国立博物馆）并共用“此处仅列名称…不复制图像”元数据模板，剥离模板后核心仍 0.8375（因整件作品身份重复）。这属“同作品重复选例＋元数据模板”所致的**实例字段重合**，而非正文/原理照搬：
> - 按本项目既往口径（第13/14/79 轮），0.54 闸门以**短文本（0.2286）与全字段（0.4367）**为准，二者均 < 0.54，**不触发不合格**；
> - 「实例」单字段重合在第13轮被记为“模板驱动·软信号，不构成降级”、第79轮作为披露项（0.5126）。本轮 0.8766 显著高于 0.5126，**虽不改变短/全字段结论，但作为较高观测项列出，供后续去重参考**（建议把本条或 `value` 的实例改为不同作品，或明确两条“同作品不同侧重点”的编辑取舍）。
> - `常见错误与限制` 逐字段亦受全库统一规范句模板抬升，属结构性模板，不计为抄袭。

## 四、问题清单

1. **【重要·观察，不阻断本轮概念直证】实例字段与 `value` 高度重合（0.8766 ≫ 0.54）**：`tints-shades` 与 `value` 同选《夜巡》且共用元数据模板。虽短文本 0.2286、全字段 0.4367 均 < 0.54 不构成“套话降级”，但实例字段重复度高，**建议后续把两条例的实例分化为不同作品/不同侧重点**，以消除实质同例重复。
2. **【观察·非阻断】实例为“解读”而非直证**：新源 `wp-tint-shade-tone` 不含 Rembrandt/Night Watch/chiaroscuro（均为 0）；端内已如实标注“对应解读、未逐字”，处置正确。若后续欲将实例转为“直证”，需另找把《夜巡》与 tint/shade 明度挂钩的艺术史/藏品说明来源。
3. **【观察·非阻断】来源 note 措辞**：`sources.json` 该源 note 写“tone=加灰”，源文为“mixing a color with gray”成立；“（经镜像核验）”为记录性注记，本轮实抓直连 Wikipedia 即 200，可后续修正说明为直连命中。

## 五、总体结论

**`tints-shades`：合格。**

- **核心成立**：本轮重点“definition/原理是否由新概念源直证 tint 加白 / shade 加黑”——`wp-tint-shade-tone` 正文首段逐字直证 “tint … mixture of a color with **white**, which **increases lightness**；shade … mixture with **black**, which **increases darkness**”，即**加白/加黑的明度调整**，**无编造**，definition/原理忠实对应。**不存在“新源未直证加白/加黑”的问题。**
- **诚实性成立**：`needs_verification=true` 与正文“待核实”、`pending_notes` 三者一致；明确区分“概念有直证”与“实例《夜巡》为解读、未逐字”，未把解读抬高为直证；新源确实不涉及《夜巡》（关键词计数 0），标注如实。
- **结构成立**：七节齐、1 张 SVG（含“示意图，非施工图”、无 script/事件/image/xlink/href）、规范句在位、5 源可引；`check.py` 0 errors。
- **相似度**：短文本 0.2286、全字段 0.4367，**均 < 0.54，不触发套话降级**；唯「实例」字段 0.8766 与 `value` 同作品重复，作观察项建议后续分化（不影响本轮合格判定）。

- **本轮 1 条：`tints-shades` 合格（加白/加黑由新源直证、无编造；nv/pending 如实；七节/SVG/规范句合规；短文本与全字段相似度均 <0.54；实例字段同作品重复列为观察项）。合计：1 合格、0 待核实、0 不合格。**

## 六、机器可读汇总

```
ROUND=80
SAMPLER=spotcheck-r80
SCOPE=["tints-shades"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round79.md","entries/batch-37.json(tints-shades)","data/sources.json(wp-tint-shade-tone + 4 others)","tools/apply_review_round80.py","tools/check.py"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback; temp research/_r80_* deleted(no residue)"
FETCHES={"wp-tint-shade-tone":200}
CONCEPT_SOURCE_DIRECT={"tint":"'a tint is a mixture of a color with white, which increases lightness'",
 "shade":"'a shade is a mixture with black, which increases darkness'",
 "verdict":"DIRECT verbatim support for 加白/加黑 (lightness/darkness); definition/原理 faithful, NO fabrication"}
INSTANCE="The Night Watch / 《夜巡》; Rembrandt; 1642; Rijksmuseum Amsterdam"
INSTANCE_IN_SOURCE={"rembrandt":0,"night watch":0,"chiaroscuro":0,"note":"new source does NOT cover the instance — honestly labeled as interpretation"}
NV={"needs_verification":true,"honest":"concept direct / instance=interpretation, not verbatim; not inflated","consistent_with_pending=true}
STRUCTURE={"seven_sections":7,"svg":"1x viewBox760x400 示意图非施工图 no script/event/image/xlink/href","reg_sentence":true,"sources":["wp-color-theory","wp-color-wheel","rijks-nightwatch-things","britannica-nightwatch","wp-tint-shade-tone"]}
SIMILARITY={"threshold":0.54,"short(def+overview)_max":0.2286,"short_vs":"value","fullfield(def+time+ov+6sec)_max":0.4367,"fullfield_vs":"value","instance_field_max":0.8766,"instance_vs":"value","instance_core_excl_boilerplate":0.8375,"pass_substantive":true,"note":"short & fullfield both <0.54; instance-field high because both entries pick same Night Watch + metadata template — observation only, not a gate fail"}
ISSUES=["Q1 important-observation(non-blocking): instance field 0.8766 vs value (same Night Watch + template) — suggest diversify instance later; short 0.2286 / fullfield 0.4367 <0.54 so no downgrade","Q2 obs: instance is interpretation not direct (source has 0 rembrandt/night watch/chiaroscuro); honestly labeled","Q3 obs: source note '经镜像核验' — live direct fetch returned 200"]
VERDICT_tints_shades="合格（加白/加黑由新源直证、无编造；nv/pending 如实；七节/SVG/规范句合规；短文本0.2286、全字段0.4367 均<0.54；实例字段同作品重复为观察项）"
TOTAL="1合格/0待核实/0不合格"
READONLY="only wrote research/spotcheck-round80.md; fetched html in-memory, temp research/_r80_* deleted(confirmed no residue); git-status M/?? items are round80 applier's own changes, not mine; no git commit; web treated as data, no instructions executed"
```

## 七、只读核验

- `ls research/_r80*` 现无残留（临时脚本/中间输出已删）。除本报告外未写任何文件。
- `git status` 中 `M coverage.json / data/sources.json / entries/batch-37.json / site/entries/tints-shades.html / site/index.html / site/sources.html` 及 `?? tools/apply_review_round80.py` 均为本轮改动方的应用产物，抽检方仅读取，未据以修改。

*（报告完）*
