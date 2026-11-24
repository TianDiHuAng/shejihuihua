# 第82b轮 复审报告（spotcheck-round82b）

- 复审人：spotcheck-r82b（lead 委派子代理，无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言；证据先于结论）。
- 复审对象：`classical-order`（`entries/batch-31.json`）、`religious-architecture`（`entries/batch-37.json`）。定位：`grep '"classical-order"|"religious-architecture"' entries/` → 上述两文件（`site/entries/*.html` 为生成产物）。
- 复核对标（第82轮结论）：classical-order 判不合格（帕特农柱数误写“前6柱侧13柱”、原理与 ancient-greek 逐字重合、正文相似度 0.5803>0.54、nv=false 误披露）；religious-architecture 判待核实（设计者 Anthemius/Isidore 仅 Wikipedia 单源未披露）。
- 本轮已修（据 `tools/apply_review_round82b.py` 实读 + 当前文件实读）：classical-order 柱数改为八柱面 octastyle（正 8/侧 17）、重写原理与手法、`db-parthenon` note 同步、nv=false；religious-architecture 实例删去单源设计者、保留穹顶创新/532–537/伊斯坦布尔双源核心、nv=false。
- 证据优先级：**独立实抓正文 > 当前文件实读 > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、计数、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round82b.md`。联网核验用 `urllib`＋浏览器 UA＋非校验 SSL **内存抓取**（未落盘临时文件）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**
- 实抓 HTTP（内存态，全部 200）：`wp-parthenon`=200（987,311 B）、`db-parthenon`=200（53,931 B）、`wp-hagia-sophia`=200（1,679,307 B）、`db-hagia-sophia`=200（54,912 B）。
- `git status` 中 `M coverage.json / data/sources.json / entries/batch-31.json / entries/batch-37.json / site/*` 及 `?? tools/apply_review_round82b.py` 等均为**本轮修复方（lead/apply_review_round82b.py）自身产物**，非本复审所写（见文末）。

## 一、核对①：柱数是否与源一致（要求 Parthenon = octastyle 8/17）

**结论：一致 ✓。** 端内实例现为“八柱面（octastyle，正面 8 柱、侧翼 17 柱），突破传统的六柱式”，与两源实抓原文逐项吻合；已不再出现“侧13柱”误引。

| 来源（本轮实抓原文） | 支撑句 | 与端内对照 |
| --- | --- | --- |
| Wikipedia《Parthenon》 | 「The Parthenon is an **octastyle** peripteral Doric temple…」；「…features **eight columns instead of the traditional six** found in typical Doric temples.」；「There are **seventeen columns on the sides.**」 | 正 8、侧 17、octastyle、突破传统六 → 全中 |
| Designing Buildings《Parthenon》 | 「Whereas traditionally, Doric colonnades would consist of **six columns across the front and thirteen down the sides, the Parthenon was built with eight** fluted, baseless columns at the front and **seventeen** at the sides.」 | 传统 6/13 → 帕特农改 8/17；端内“突破传统的六柱式”正确 |

- 端内不再含“13 柱”字样（复核脚本 `has13column?=False`）；`db-parthenon` 源 note 已同步为「其八柱面（octastyle，前8柱、侧17柱）突破传统六柱式」（`data/sources.json` 实读），与实抓一致。

## 二、核对②：原理是否已不逐字重合、全字段相似度是否 <0.54

**结论：已不逐字重合，全字段相似度全部 <0.54 ✓。**

- 端内 `原理`（classical-order）：『古典柱式把柱头、柱身、檐部与基座按固定柱径倍数关系组配：多立克柱身粗壮、装饰简省，爱奥尼与科林斯渐趋修长华饰。柱式的比例秩序使立面统一并传达庄重。』
- ancient-greek `原理`：『柱径、柱距与檐部高度之间存在可感知的比例关系，使建筑呈现秩序与尺度感。』
- 两句已**完全不同**，不再逐字重合（第82轮为逐字相同，是 0.5803 超阈主驱动因）。

相似度（`difflib.SequenceMatcher`，norm=去空白小写，全库 **258** 条两两比对；并列三种口径以求稳健）：

| 条目 | 最高相似对象 | 去模板正文 | 原始正文(不剥模板) | 全字段拼接 | 实例字段 | 短文本 | 判定(0.54) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| classical-order | ancient-greek | **0.3769** | **0.4439** | **0.4403** | 0.4789 | 0.3182 | 全口径 **<0.54 ✓** |
| religious-architecture | imperial-architecture / byzantine | **0.3290** | **0.4444** | **0.3429** | 0.4324 | 0.4000 | 全口径 **<0.54 ✓** |

- **全库去模板正文 >0.54 的对数：0**（第82轮为 1，即 classical-order↔ancient-greek=0.5803）。该唯一阻断对已消除。
- 说明：本轮绝对数值（0.38 量级）与第82轮报告 0.5803 的差异源于模板归一化口径不同；但**在“去模板/不剥模板/全字段”三种口径下均 <0.54**，结论稳健（超标已不可能）。
- 附注（**越界观察，非本轮判定**）：仅在“全字段拼接”最严口径下，全库另有 3 对 >0.54，均为**本轮范围外**条目（revival-gothic↔revival-renaissance 0.5792、gongbi↔xieyi 0.5597、revival-gothic↔eclecticism 0.5511），不涉及本轮两条，供 lead 另行安排。

## 三、核对③：设计者单源问题是否已消除（religious-architecture）

**结论：已消除 ✓。**

- 端内 `实例` 现为「名称：圣索菲亚大教堂（Hagia Sophia）；地点：土耳其伊斯坦布尔；年份：公元 532–537 年。以巨大穹顶统摄的礼拜空间，是宗教建筑穹顶的重要创新。…」——**已完全删去 “Anthemius of Tralles / Isidore of Miletus” 设计者**，全字段（definition/原理/手法/实例/常见错误/一图/待核实）均无设计者字样。
- 第82轮的阻断点正是“设计者仅 Wikipedia 单源（DB 全文未提）却未披露”。设计者已是**端内非承载信息**，单源未披露问题随之消失，nv=false 不再因此存疑。
- 注（不影响判定）：`data/sources.json` 的 `wp-hagia-sophia` note 仍记有设计者、`db-hagia-sophia` 未提设计者——此为**源记录历史文本**，端内既未引用该要素，就不构成端内单源声明。

## 四、核对④：穹顶创新 / 532–537 是否仍双源

**结论：仍双源直证 ✓（穹顶创新、年代、地点三项均双源）。**

| 要素 | Wikipedia《Hagia Sophia》（实抓） | Designing Buildings《Hagia Sophia》（实抓） | 判定 |
| --- | --- | --- | --- |
| 穹顶为重大创新 | 「among the first to employ a **fully pendentive dome**」；「epitome of Byzantine architecture」 | 「its **dome which was a significant innovation** at the time」；「dome rests on four **pendentives — an innovative development**」 | ✓ 双源 |
| 年代 532–537 | 532（current structure）/537（completed/537 establishments） | 「Dating back to A.D. **532**」；「completed … in A.D. **537**」 | ✓ 双源 |
| 地点 伊斯坦布尔 | 分类含 Istanbul / Hagia Sophia… | 「located in **Istanbul, Turkey**」 | ✓ 双源 |

- 端内 `待核实` 现表述为「圣索菲亚穹顶为重大创新、年代（532–537）与地点由 Wikipedia 与 Designing Buildings 双源直证」——与上述实抓一致，nv=false 有据。

## 五、核对⑤：七节 / SVG / 规范句（结构化）

| 核对项 | classical-order | religious-architecture |
| --- | --- | --- |
| 七节齐（definition+6 节） | ✓ 6 节：原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 | ✓ 同左 6 节 |
| SVG | ✓ 1 张，`viewBox='0 0 760 400'`，含“示意图，非施工图”；无 `<script>/<iframe>/<image>/href/xlink/url()/onX=` | ✓ 同左 |
| 规范句 | ✓ 常见错误与限制收尾“实际工程须按当地规范和专业设计人员的要求” | ✓ 同左 |
| nv / pending_notes | nv=false，pending_notes="" | nv=false，pending_notes="" |
| check.py | PASS（0 errors） | PASS（0 errors） |

## 六、复审结论（逐条）

- **`classical-order`：合格。**
  - ①柱数：“八柱面 octastyle，正 8 / 侧 17，突破传统六柱式”与两源实抓逐项吻合，原“侧13柱”误引已消除；
  - ②原理已重写、与 ancient-greek 不再逐字重合，全字段相似度最高 0.4403（多口径均 <0.54），全库去模板正文 >0.54 对数归零；
  - ③设计者 Iktinos/Callicrates、年代 447–432 双源；④七节/SVG/规范句合规；nv=false 有据。
  - **非阻断观察**：实例仍与 `ancient-greek` 同用帕特农神庙（同例重合），但实例字段相似度 0.4789<0.54、正文亦已去重；如需彻底消除“同例”，可后续换用其它多立克实例或回退类型性描述（非本轮阻断项）。

- **`religious-architecture`：合格。**
  - ①设计者单源问题已消除（端内已删 Anthemius/Isidore，全字段无设计者）；
  - ②穹顶重大创新、年代 532–537、地点伊斯坦布尔均双源直证；全字段相似度最高 0.3429（各口径 <0.54）；七节/SVG/规范句合规；nv=false 有据。
  - **非阻断观察**：①实例仍与 `byzantine` 同用圣索菲亚（同例重合，实例字段 0.4324<0.54，已知分工：本条讲“宗教建筑穹顶创新”、byzantine 讲“拜占庭风格”，可接受）；②`原理` 仍整句复述 definition（“宗教建筑指供礼拜与仪式使用的建筑类型。”），内容偏薄，可后续补“空间/光线/象征”的独立展开（观察项，非阻断）。

- **本轮 2 条：2 合格、0 待核实、0 不合格。**（均附非阻断观察）

## 七、机器可读汇总

```
ROUND=82b
SAMPLER=spotcheck-r82b
SCOPE=["classical-order","religious-architecture"]
DOCS_READ=["research/spotcheck-round82.md","entries/batch-31.json(classical-order)","entries/batch-37.json(religious-architecture)","data/sources.json(wp-classical-order/designingbuildings-classical/wp-parthenon/db-parthenon/wp-hagia-sophia/db-hagia-sophia/wp-architectural-style/wp-gothic-architecture)","tools/apply_review_round82b.py","tools/check.py"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback (no temp files)"
FETCHES={"wp-parthenon":200,"db-parthenon":200,"wp-hagia-sophia":200,"db-hagia-sophia":200}
CLASSICAL_ORDER={
 "column_count":"FIXED & SOURCE-CONSISTENT: 八柱面octastyle 正8/侧17 (wp:'octastyle...eight instead of the traditional six'/'seventeen on the sides'; db:'six...thirteen[traditional]...eight...seventeen'); 侧13柱 已移除; db-parthenon note 已同步",
 "principle_dedup":"原理 已重写，与 ancient-greek 不再逐字相同",
 "similarity":{"detemplated":0.3769,"raw":0.4439,"fullfield":0.4403,"instance":0.4789,"short":0.3182,"vs":"ancient-greek","all_below_0.54":true},
 "designers":"Iktinos/Callicrates 双源","dates":"447-432 双源","nv_false_grounded":true,
 "residual_obs":"仍与 ancient-greek 同用帕特农(同例重合)，实例0.4789<0.54 非阻断"}
RELIGIOUS={
 "designer_single_source":"ELIMINATED: 端内已删 Anthemius/Isidore，全字段无设计者",
 "dome_innovation":"DUAL-sourced (wp fully pendentive dome/among first/epitome; db significant innovation/pendentives innovative development)",
 "dates":"532-537 DUAL-sourced (wp 532/537; db A.D.532/A.D.537)",
 "location":"Istanbul DUAL-sourced (wp categories Istanbul; db located in Istanbul, Turkey)",
 "similarity":{"detemplated":0.3290,"raw":0.4444,"fullfield":0.3429,"instance":0.4324,"short":0.4000,"vs":"imperial-architecture/byzantine","all_below_0.54":true},
 "nv_false_grounded":true,
 "residual_obs":["仍与 byzantine 同用圣索菲亚(同例重合，实例0.4324<0.54，可接受分工)","原理仍复述 definition(偏薄，观察项)"]}
SIMILARITY={"method":"difflib SequenceMatcher, norm=nows-lower, 258 entries; three metrics(detemplated/raw/fullfield)",
 "library_prose_detemplated_pairs":33153,"library_prose_detemplated_gt0.54":0,
 "note":"round82 sole blocking pair classical-order<->ancient-greek 0.5803 resolved",
 "out_of_scope_fullfield_gt0.54":[["revival-gothic","revival-renaissance",0.5792],["gongbi","xieyi",0.5597],["revival-gothic","eclecticism",0.5511]]}
STRUCTURE={"classical_order":{"seven_sections":7,"svg":"1x 760x400 示意图非施工图 no forbidden/event","reg_sentence":true,"nv":"false"},"religious_architecture":{"seven_sections":7,"svg":"1x 760x400 示意图非施工图 no forbidden/event","reg_sentence":true,"nv":"false"}}
VERDICT_classical_order="合格（柱数8/17与源一致、原理去重、全字段相似<0.54、双源齐；附非阻断观察：仍与ancient-greek同用帕特农）"
VERDICT_religious_architecture="合格（设计者单源已消除、穹顶创新/532-537/地点双源、全字段相似<0.54；附非阻断观察：仍与byzantine同用圣索菲亚、原理复述definition）"
TOTAL="2合格/0待核实/0不合格"
READONLY="only wrote research/spotcheck-round82b.md; fetched html in-memory (no temp files); git-status M/?? items are round82b applier's own changes, not mine; no git commit; web treated as data, no instructions executed"
```

## 八、只读核验

- 除本报告 `research/spotcheck-round82b.md` 外未写任何文件；联网抓取为内存态（未落盘临时文件）。
- `git status` 中 `M coverage.json / data/sources.json / entries/batch-31.json / entries/batch-37.json / site/*` 及 `?? tools/apply_review_round82b.py` 均为**本轮修复方（lead/apply_review_round82b.py）的应用产物**，复审方仅读取、未据以修改；未 `git commit`；未改项目外内容。

*（报告完）*
