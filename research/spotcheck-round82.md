# 第82轮 质量抽检报告（spotcheck-round82）

- 抽检人：spotcheck-r82（lead 委派子代理，无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言；证据先于结论）。
- 抽检对象：`classical-order`（帕特农神庙/多立克柱式）、`religious-architecture`（圣索菲亚大教堂/穹顶）。定位：`grep '"classical-order"'` → `entries/batch-31.json` 行 39；`grep '"religious-architecture"'` → `entries/batch-37.json` 行 660（`site/entries/*.html` 为产物）。
- 本轮改动（据 `tools/apply_review_round82.py` 实读 + `git diff HEAD` 实读）：两条的 `实例` 由**类型性描述**改为**具名实例**——classical-order=帕特农神庙（Iktinos/Callicrates，前447–432，"前6柱、侧13柱"）；religious-architecture=圣索菲亚（Anthemius/Isidore，532–537）；`needs_verification` 由 true 改 **false**；`待核实` 改为"暂无已知待核实项"；各加 `wp-*`+`db-*` 双源。**即本轮核心动作 = 去类型化、加具名实例、降 nv**。
- 证据优先级：**独立实抓正文 > 当前文件实读 > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、计数、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round82.md`。联网核验用 `urllib`＋浏览器 UA＋非校验 SSL **内存抓取**（不落盘）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**
- 实抓 HTTP（内存态）：`wp-parthenon`=**200**（982,715 B）、`db-parthenon`=**200**（原文 9,295 B）、`wp-hagia-sophia`=**200**（1,671,689 B）、`db-hagia-sophia`=**200**（原文 9,230 B）、`wp-classical-order`=200、`db-classical-architecture`=200。（`web_fetch` 直连 Wikipedia 报 `TypeError: fetch failed`，改用 urllib 直连均 200。）
- `git status` 中 `M coverage.json / data/sources.json / entries/batch-31.json / entries/batch-37.json / site/*` 及 `?? tools/apply_review_round82.py` 均为**本轮改动方（lead/apply_review_round82.py）自身产物**，非本抽审所写（见文末）。

## 一、核心命题核对①：definition/实例是否由两源正文支撑

### 1. `classical-order` — definition ✓ 双源；实例"多立克高峰" ✓，但"前 6 柱、侧 13 柱" ✗ 被两源同时否定

definition/overview 双源直证：
- `wp-classical-order`：三级希腊柱式 Doric / Ionic / Corinthian（Roman orders 另列 Tuscan、Composite）。
- `db-classical-architecture`（实抓）：「developed according to three basic styles, or 'orders' – **Doric, Ionic and Corinthian** – that formed the heart of classical Greek architecture. **The Romans also used these widely but added two of their own orders: Tuscan and Composite.**」→ 与 definition「希腊以多立克、爱奥尼、科林斯为主」、overview「罗马…增塔司干与复合柱式」逐项吻合 ✓。

实例"多立克柱式高峰/典范" ✓，但柱数 **✗ 事实错误**（两源同时否定"前6侧13柱"）：

| 来源（实抓原文） | 帕特农实际柱数 | "6/13"在源中的含义 |
| --- | --- | --- |
| Wikipedia《Parthenon》 | 「The Parthenon is an **octastyle** peripteral Doric temple…」；「The gable-end of the Parthenon features **eight columns instead of the traditional six** found in typical Doric temples.」；「**There are seventeen columns on the sides.**」 | 6 = 传统多立克惯例，非帕特农 |
| Designing Buildings《Parthenon》 | 「Whereas traditionally, Doric colonnades would consist of **six columns across the front and thirteen down the sides, the Parthenon was built with eight** fluted, baseless columns at the front and **seventeen** at the sides.」 | 6/13 = 传统惯例，帕特农改为 8/17 |

- 结论：帕特农为 **前 8 柱、侧 17 柱（octastyle）**；**"前 6 柱、侧 13 柱"是它所脱离的传统多立克柱数**。端内「多立克柱式的典范（前 6 柱、侧 13 柱）」把"传统惯例柱数"**误挂到帕特农头上**，构成**事实性错误/误引**（两源均不支持且直接相反）。这也正是 `db-parthenon` 来源 note 自身把源文误读为「前6后侧13柱」所致（见问题①）。

### 2. `religious-architecture` — 实例"穹顶重大创新" ✓ 双源；definition 偏泛

实例"穹顶重大创新" ✓ 双源直证：

| 来源（实抓原文） | 支撑句 |
| --- | --- |
| Wikipedia《Hagia Sophia》 | 「among the first to employ a **fully pendentive dome**…epitome of Byzantine architecture」；`pendentive` 出现 12 次 |
| Designing Buildings《Hagia Sophia》 | 「…due largely to its **dome which was a significant innovation at the time**」；「The dome rests on four pendentives - an **innovative development** for the time」 |

- definition「宗教建筑指供礼拜与仪式使用的建筑类型」为**通用型定义**（近同义反复），所引四源无一是"宗教建筑"专论页逐字给出该定义；属编辑性通识定义，**非两源正文直证**（观察项，非阻断）。`原理` 又整句重复 definition（"宗教建筑指供礼拜与仪式使用的建筑类型。"）后接 overview，内容偏薄。

## 二、核心命题核对②：是否编造（设计者 / 年份）

| 条目 | 要素 | 端内声明 | 实抓核对 | 判定 |
| --- | --- | --- | --- | --- |
| classical-order | 设计者 | 伊克蒂诺与卡利克拉底（Iktinos and Callicrates） | DB：「The architects **Ictinus and Callicrates** designed the temple…」；WP architect 字段：`Iktinos, Callicrates` | ✓ **双源**，无编造 |
| classical-order | 年份 | 公元前 447–432 年 | DB：「Work began in **447 BCE**…exterior decoration continued until **432 BCE**」；WP：Construction started **447 BC** / Completed **432 BC** | ✓ 双源，无编造 |
| religious-architecture | 设计者 | 特拉勒斯的安提莫斯与米利都的伊西多尔（Anthemius of Tralles and Isidore of Miletus） | WP architects 字段：`Isidore of Miletus / Anthemius of Tralles`（各 11/7 次）；**DB 全文 Anthemius=0、Isidore=0（未提设计者）** | △ **仅 Wikipedia 单源**（真实无编造，但非双源） |
| religious-architecture | 年份 | 公元 532–537 年 | WP：`532`(9次)/`537`(11次)；DB：「Dating back to A.D. **532**」「completed in just five years, in A.D. **537**」 | ✓ 双源，无编造 |

- 四条具名史实**均真实、无虚构**（非错位、非张冠李戴）；唯一"错误"不是"编造"，而是第一节的**柱数误引**（真数字 6/13 被错误归属到帕特农）。
- **设计者单源问题成立（针对 religious-architecture）**：圣索菲亚设计者仅在 Wikipedia 有据，Designing Buildings 未提名。

## 三、核心命题核对③：两源是否独立

- 两源为 **Wikipedia（Wikimedia）** 与 **Designing Buildings（IHBC Conservation Wiki / Designing Buildings Ltd，英国）**——不同机构、独立编纂，**独立性成立**（`wp-parthenon`↔`db-parthenon`、`wp-hagia-sophia`↔`db-hagia-sophia` 均如此）。
- 附注（历史瑕疵）：`wp-classical-order`/`designingbuildings-classical` 的 `author` 字段均写 "Wikipedia/机构"，两站却实为不同机构，字段措辞不严谨，但不影响实例侧 `wp-*`↔`db-*` 的独立性判定。

## 四、核心命题核对④：nv=false 是否有据（含"设计者仅单源是否构成问题"）

### `classical-order` — nv=false **无据/不成立**
- 端内 `待核实`="暂无已知待核实项"、`pending_notes`=""，但**实例含一处被两源否定的事实错误（前6侧13柱）**。有真实错误却标"暂无待核实"→ nv=false **不成立**，属**误披露**。

### `religious-architecture` — nv=false **部分有据，但未披露单源，宜 待核实**
- 核心命题（穹顶重大创新）＋年代（532–537）**双源成立**→ 大方向有据；
- 但**设计者 Anthemius/Isidore 仅 Wikipedia 单源**（DB 未提），按 D10「关键事实双源或标待核实」应**标注待核实或补第二源**；现 nv=false＋"暂无已知待核实项"**未披露该单源**。
- 故任务设问「若设计者仅单源是否构成问题」——**构成**：它是一处（轻微）关键事实单源，未到否定全部的程度，但按项目 D10/D14 口径，此条更宜 **nv=true / 标待核实**，而非直接 nv=false。

## 五、核心命题核对⑤：相似度（阈值 0.54）

> 口径：`difflib.SequenceMatcher`，norm=去空白小写，全库 **258** 条两两比对。**主口径=去模板正文（definition+time_or_place+overview+原理+典型手法+常见错误，剔除实例/一图/待核实，并剥离规范模板句）**；另列短文本、实例字段备查。**方法已用 `tints-shades` 复现前报告数值（0.2286 / 0.2862 / 0.3548）校准一致。**

| 条目 | 短文本(def+ov) | 去模板正文（主口径） | 实例字段 | 判定（0.54） |
| --- | --- | --- | --- | --- |
| classical-order | 0.3182 vs ancient-greek | **0.5803 vs ancient-greek** | 0.6524 vs ancient-greek | **正文 0.5803 > 0.54 ✗**（且为**全库唯一 >0.54、全库最高值**） |
| religious-architecture | 0.4000 vs imperial-architecture | **0.3515** vs imperial-architecture | 0.6231 vs byzantine | 正文 **< 0.54 ✓**；但实例与 byzantine 同例（见下） |

关键判读：
- **全库去模板正文比对：33,153 对，>0.54 者仅 1 对，恰为 `classical-order ↔ ancient-greek = 0.5803`。** 驱动因：两条 `原理` **逐字完全相同**——「柱径、柱距与檐部高度之间存在可感知的比例关系，使建筑呈现秩序与尺度感。」；且本轮又把**同一帕特农实例**（Iktinos/Callicrates、447–432）从 `ancient-greek` 复用到 `classical-order`。→ **实质性重复，超阈值**。
- 实例字段原始比对在全库有 **2,318 对 ≥0.55**（大量来自"类型性描述/此处仅列…"等**共用模板**，含多组 1.0），故**实例字段不能作严格 0.54 闸门**；但**"同名同一建筑"的针对性重合**仍须单列：`classical-order↔ancient-greek`（同为帕特农）、`religious-architecture↔byzantine`（同为圣索菲亚 532–537 同设计者）——正是 round80b 处理 tints-shades 时去具名所消除的那类"同例重合"。

## 六、七节 / SVG / 规范句（结构化）

| 核对项 | classical-order | religious-architecture |
| --- | --- | --- |
| 七节齐 | ✓ definition+6（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实）=7 | ✓ 同左=7 |
| SVG | ✓ 1 张，`viewBox='0 0 760 400'`，含"示意图，非施工图"；无 script/iframe/image/href/xlink/url()、无 `onX=` 事件 | ✓ 同左 |
| 规范句 | ✓ 常见错误与限制收尾"实际工程须按当地规范和专业设计人员的要求" | ✓ 同左 |
| 可引性 | 4 源 verified=true；`wp-parthenon`/`db-parthenon` link_ok=true（实抓 200）；`wp-classical-order`/`designingbuildings-classical` link_ok=null（历史） | 4 源 verified=true；`wp-hagia-sophia`/`db-hagia-sophia` link_ok=true（实抓 200） |
| check.py | PASS（0 errors） | PASS（0 errors） |

## 七、问题清单

1. **【阻断·事实错误】`classical-order` 实例"（前 6 柱、侧 13 柱）"不实。** 两引源（WP《Parthenon》"octastyle…eight columns instead of the traditional six…seventeen on the sides"；DB《Parthenon》"six…thirteen [traditional]…Parthenon…eight…seventeen"）**一致表明帕特农为前 8 侧 17，6/13 是它所脱离的传统柱数**。端内把传统柱数误挂帕特农。**建议**：改为"多立克柱式的典范（前 8 柱、侧 17 柱 / octastyle）"或删去柱数括注；并**同步修正 `data/sources.json` 中 `db-parthenon` 的 note**（现误作"前6后侧13柱"，系对源文的误读）。
2. **【阻断·相似度超阈】`classical-order ↔ ancient-greek`。** 去模板正文 **0.5803 > 0.54（全库唯一超阈、最高值）**；`原理` 句逐字相同，且本轮又把同一帕特农实例从 `ancient-greek` 复用过来（实例字段 0.6524）。**建议**：改写 `classical-order` 的 `原理`（与 ancient-greek 差异化），并**更换或去具名实例**（避免与 ancient-greek 同用帕特农；可回退类型性描述或改用其它柱式实例），使正文与实例双降阈下。
3. **【重要·单源未披露】`religious-architecture` 设计者 Anthemius/Isidore 仅 Wikipedia 单源**（DB 全文未提），却 nv=false＋"暂无待核实"。**建议**：补第二独立源证实设计者，或将 `待核实`/`pending_notes` 如实标注"设计者为 Wikipedia 单源、DB 未提及"，并按 D10 暂置 nv=true。
4. **【重要·同例重合】`religious-architecture ↔ byzantine` 同用圣索菲亚（532–537，同设计者）**（实例字段 0.6231）；虽去模板正文 0.3515<0.54，但"同一建筑同一实例"的针对性重合与 round80b 所修问题同类。**建议**：`religious-architecture` 改用不同具名实例，或与 `byzantine` 明确分工（一者讲建筑类型通例、一者讲拜占庭风格）。
5. **【观察·非阻断】`religious-architecture` definition 偏泛、`原理` 整句重复 definition**（"宗教建筑指供礼拜与仪式使用的建筑类型。"），内容偏薄；可补"空间/光线/象征"的独立展开。
6. **【观察·口径】实例字段全库有 2,318 对 ≥0.55（模板句共用所致），不宜作严格 0.54 闸门**；本报告以"去模板正文"为主口径，实例仅作针对性重合旁证。

## 八、总体结论

- **`classical-order`：不合格。** ①实例"（前 6 柱、侧 13 柱）"**被两条引用来源同时否定**（帕特农实为前 8 侧 17，6/13 是传统多立克柱数），属事实误引，却标 nv=false"暂无待核实"；②与 `ancient-greek` **正文相似度 0.5803（全库唯一 >0.54）**、`原理` 逐字相同、并复用同一帕特农实例（0.6524），实质重复超阈。definition/多立克高峰双源、设计者与年份双源、七节/SVG/规范句合规，但这些正面项不足以抵消上面两项阻断。
- **`religious-architecture`：待核实。** 核心命题「穹顶重大创新」**双源直证成立**（WP fully pendentive/among first/epitome；DB significant innovation/pendentives innovative）、年代 532–537 **双源**、正文相似度 0.3515<0.54、七节/SVG/规范句合规——主体可用；但①**设计者 Anthemius/Isidore 仅 Wikipedia 单源且未披露**（按 D10 宜 nv=true/待核实）；②**实例与 `byzantine` 同为圣索菲亚**（同例重合，实例字段 0.6231）。补第二源＋去重后可转合格。

- **本轮 2 条：0 合格、1 待核实（religious-architecture）、1 不合格（classical-order）。**

## 九、机器可读汇总

```
ROUND=82
SAMPLER=spotcheck-r82
SCOPE=["classical-order","religious-architecture"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round80b.md","research/spotcheck-round79.md","entries/batch-31.json(classical-order)","entries/batch-37.json(religious-architecture)","entries/batch-05.json(ancient-greek,byzantine)","data/sources.json(wp-classical-order/designingbuildings-classical/wp-parthenon/db-parthenon/wp-architectural-style/wp-gothic-architecture/wp-hagia-sophia/db-hagia-sophia)","tools/apply_review_round82.py","tools/check.py"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback (no temp files); web_fetch to Wikipedia failed(TypeError)->urllib 200"
FETCHES={"wp-parthenon":200,"db-parthenon":200,"wp-hagia-sophia":200,"db-hagia-sophia":200,"wp-classical-order":200,"db-classical-architecture":200}
CLASSICAL_ORDER={
 "definition":"dual-sourced OK (Doric/Ionic/Corinthian; Roman +Tuscan+Composite: wp-classical-order + db-classical-architecture)",
 "peak_of_doric":"OK (db:'culmination of the Doric order'; wp:'octastyle peripteral Doric temple')",
 "column_count_CLAIM":"WRONG: entry says 前6柱侧13柱; BOTH sources: Parthenon = 8 front / 17 side (octastyle); 6/13 = TRADITIONAL Doric norm it departed from (wp:'eight columns instead of the traditional six'/'seventeen on the sides'; db:'six...thirteen[traditional]...Parthenon...eight...seventeen')",
 "designers":"Iktinos/Callicrates dual-sourced (wp+db) NOT fabricated",
 "dates":"447-432 dual-sourced (wp+db) NOT fabricated",
 "nv_false_grounded":false,
 "nv_note":"待核实='暂无已知待核实项' but instance has a real error -> mis-disclosure"}
RELIGIOUS={
 "dome_innovation":"DUAL-sourced OK (wp:'fully pendentive dome'/'among the first'/epitome; db:'dome which was a significant innovation'/'pendentives innovative development')",
 "dates":"532-537 dual-sourced (wp+db) NOT fabricated",
 "designers":"Anthemius/Isidore real but WIKIPEDIA-ONLY (db Anthemius=0/Isidore=0) -> single-source",
 "definition":"generic/tautological, no dedicated source (observation)",
 "nv_false_grounded":"partial: core innovation+dates dual-sourced, but designers single-source undisclosed -> ideally nv=true/待核实"}
INDEPENDENCE={"wp":"Wikipedia","db":"Designing Buildings (IHBC/Designing Buildings Ltd)","independent":true}
SIMILARITY={"method":"difflib SequenceMatcher, norm=nows-lower, 258 entries; calibrated vs tints-shades 0.2286/0.2862/0.3548",
 "classical_order":{"short":0.3182,"prose_detemplated_max":0.5803,"prose_vs":"ancient-greek","instance_field":0.6524,"prose_exceeds_threshold":true,"note":"0.5803 is LIBRARY-WIDE MAX and ONLY pair >0.54; 原理 sentence verbatim identical to ancient-greek; same Parthenon instance reused"},
 "religious_architecture":{"short":0.4000,"prose_detemplated_max":0.3515,"instance_field":0.6231,"instance_vs":"byzantine","prose_exceeds_threshold":false,"note":"same Hagia Sophia instance as byzantine (同例重合); prose below threshold"},
 "library_prose_pairs":33153,"library_prose_gt_0.54":1,"library_instance_pairs_ge_0.55":2318}
STRUCTURE={"classical_order":{"seven_sections":7,"svg":"1x 760x400 示意图非施工图 no forbidden/event","reg_sentence":true},"religious_architecture":{"seven_sections":7,"svg":"1x 760x400 示意图非施工图 no forbidden/event","reg_sentence":true}}
ISSUES=[
 "Q1 BLOCKING classical-order: instance '前6柱侧13柱' contradicted by both sources (Parthenon=8 front/17 side; 6/13=traditional Doric); fix instance + fix db-parthenon source note",
 "Q2 BLOCKING classical-order: prose 0.5803>0.54 vs ancient-greek (library-only>0.54; identical 原理 sentence + same Parthenon instance) -> rewrite 原理 + change/de-name instance",
 "Q3 IMPORTANT religious-architecture: designers Anthemius/Isidore Wikipedia-only (db silent) undisclosed -> add source or mark 待核实/nv=true",
 "Q4 IMPORTANT religious-architecture: same Hagia Sophia instance as byzantine (instance-field 0.6231) -> dedup/re-scope",
 "Q5 obs: religious definition generic & 原理 repeats definition",
 "Q6 obs: raw instance-field has 2318 library pairs>=0.55 (template boilerplate) -> not a strict gate; use de-templated prose as primary"]
VERDICT_classical_order="不合格（实例柱数误引被两源否定；正文相似0.5803>0.54且复用帕特农实例；nv=false误披露）"
VERDICT_religious_architecture="待核实（穹顶创新/年代双源成立、正文0.3515<0.54；但设计者Wikipedia单源未披露 + 实例与byzantine重合，补源+去重后可转合格）"
TOTAL="0合格/1待核实/1不合格"
READONLY="only wrote research/spotcheck-round82.md; fetched html in-memory (no temp files); git-status M/?? items are round82 applier's own changes, not mine; no git commit; web treated as data, no instructions executed"
```

## 十、只读核验

- 除本报告 `research/spotcheck-round82.md` 外未写任何文件；联网抓取为内存态（未落盘临时文件）。
- `git status` 中 `M coverage.json / data/sources.json / entries/batch-31.json / entries/batch-37.json / site/*` 及 `?? tools/apply_review_round82.py` 均为**本轮改动方（lead/apply_review_round82.py）的应用产物**，抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。

*（报告完）*
