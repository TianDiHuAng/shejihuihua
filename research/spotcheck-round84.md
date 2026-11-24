# 第84轮 质量抽检报告（spotcheck-round84）

- 抽检人：spotcheck-r84（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言；证据先于结论）。
- 抽检对象：`vernacular-architecture`（乡土建筑）。定位：`grep '"vernacular-architecture"' entries/` → 唯一定义条目在 `entries/batch-37.json` 行 502（`batch-02-d.json` 仅作 related 引用）；生成产物 `site/entries/vernacular-architecture.html`。
- 本轮升级动作（据 `tools/apply_review_round84.py` 实读 + `entries/batch-37.json` 实读 + `git diff`）：`definition` 由「地方工匠凭经验、用本地材料、依本地气候造出来的房屋，往往没有职业建筑师」改为「依本地材料、气候与习俗、由当地人自行建造、因地制宜的建筑；通常无职业建筑师」；`实例` 由「类型性描述；地点与设计者不适用」改为「夯土与木构的乡土民居（类型性，乡土建筑通常无单一设计者）；地点：因地制宜（不指定具体项目）」；`sources` 追加 `db-vernacular`、`artincontext-vernacular`（共 4 源）；`needs_verification` 由 **true → false**，`pending_notes` 由旧文本 → **空**，`待核实` 改为「暂无已知待核实项。」
- 证据优先级：**独立实抓正文 > 当前文件实读 > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、计数、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round84.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式：`web_fetch` 本环境历史报错（DECISIONS D05），改用 **Python urllib + 浏览器 UA + 非校验 SSL 内存抓取（stdin 直跑，未落盘任何临时文件）**。
- 实抓 HTTP（全部 200，内存态）：
  - `wp-vernacular-architecture` = `https://en.wikipedia.org/wiki/Vernacular_architecture` → 200，629,853 B，title *Vernacular architecture - Wikipedia*
  - `db-vernacular` = `https://www.designingbuildings.co.uk/wiki/Vernacular_architecture` → 200，57,292 B，title *Vernacular architecture - Designing Buildings*
  - `artincontext-vernacular` = `https://artincontext.org/vernacular-architecture/` → 200，397,673 B，title *Vernacular Architecture - Region-Specific Building Styles*
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**
- `git status` 中 `M coverage.json / data/sources.json / entries/batch-37.json / site/entries/vernacular-architecture.html / site/index.html / site/sources.html` 及 `?? tools/apply_review_round84.py` 均为**本轮修复方（lead/apply_review_round84.py）自身产物**，非本抽检所写；抽检方仅读取。

## 一、核对①：definition 是否三源直证（依本地材料/气候/习俗、因地制宜、无职业建筑师）

**结论：三源逐项直证，非编造、非单源推测 ✓。**

端内 `definition`：『乡土建筑是依本地材料、气候与习俗、由当地人自行建造、因地制宜的建筑；通常无职业建筑师。』

| 要素 | wp-vernacular-architecture（实抓原文） | db-vernacular（实抓原文） | artincontext-vernacular（实抓原文） | 判定 |
| --- | --- | --- | --- | --- |
| 本地材料 | 「**Local materials** would be used as a matter of course, other materials being chosen and imported quite exceptionally」 | 「Taking advantage of **local materials** and resources」；「reliance on needs, construction **materials** and traditions specific to its particular **locality**」 | 「dependence on local demands, **building materials**, and customs」 | ✓ 三源 |
| 气候 | 「One of the most significant influences … is the **macro climate**」；单列章节 Climate | 「Influences … **Climate**: sunshine, humidity, rain, wind, temperature」 | 「closely tied to its **environment** … distinct geographic elements」 | ✓ 三源（wp/db 直称 climate，art 以 environment 表述）|
| 习俗 | 「decorate buildings in accordance with **local customs** and beliefs」 | 「local **customs**, religious values」 | 「local demands, building materials, and **customs**」 | ✓ 三源 |
| 因地制宜 / 地缘特定 | 「building done outside any academic tradition … **without the involvement of professional designers and architects**」（+ 通篇 tradition/environment） | 「type of architecture which is **indigenous to a specific** [locality]」 | 「**unique to a particular period and location**」；「distinctive to different par[ts]」 | ✓ 三源 |
| 由当地人自行建造 | 「**owner- or community-built**, utilizing traditional technologies」；「of the common people」 | 「local knowledge and traditions」（indigenous to locality） | 「typically **produced by the proprietors or the community** employing traditional local techniques」 | ✓ 三源 |
| 通常无职业建筑师 | 「**without the involvement of professional designers and architects**」 | （未直述"无建筑师"，主述 locality/indigenous） | 「formal **architects did not super**[vise]…」（17 世纪前多视为 vernacular） | ✓ 两源直证（wp + art）；db 概念支持不强 |

- **三源是否直证"依本地材料/气候/习俗、因地制宜"：是。** 三项要素在 wp、db、art 均有字面表述（气候一项 art 以 environment 表述，属同义）。**无职业建筑师**由 wp（逐字）+ art（formal architects did not supervise）两源直证，db 未直述，属可接受的两源支撑。
- **两源/三源独立性：是。** wp = Wikimedia 百科（众编）；db = Designing Buildings Ltd 英国建筑行业知识库（Construction Wiki）；art = Art in Context 艺术/建筑教育站。**发布方不同、非镜像**，且各含对方未载的独立细节（db「indigenous to a specific locality」；art「unique to a particular period and location」「proprietors or community」）。
- **是否编造：否。** definition 全部要素均能在登记源找到对应字面/近义表述，无虚构。

## 二、核对②：实例类型性是否恰当（比照 tints-shades 先例）

**结论：类型性恰当，且对"乡土建筑通常无单一设计者"这一特性尤合适 ✓。**

端内 `实例`：『名称：夯土与木构的乡土民居（类型性，乡土建筑通常无单一设计者）；地点：因地制宜（不指定具体项目）；以就地取材、依气候组织构造为特征。此处仅列说明，不复制图像。』

- **type 级判断合理**：乡土建筑（vernacular）按 wp 定义即「outside any academic tradition, and without the involvement of professional designers and architects」「owner- or community-built」，其本性无单一署名设计者。对一个以"无职业建筑师/社区自建"为定义的类别，**以类型性实例（夯土+木构乡土民居）表述，比强行指认某一具名单体建筑更贴切**，可避免"把某具体民居归给单一设计者"的失真。
- **与 tints-shades 先例一致**（`research/spotcheck-round80b.md`）：`tints-shades` 由具名《夜巡》改为「明度色阶练习（类型性）、地点与作者不适用」后判 nv=false 合格；本条的"概念源定义 + 类型性实例（无具名作品待核）→ nv=false"正是同一既定口径（round80b 归纳全库含类型性实例共 103 条、其中 nv=false 5 条的同模式）。
- **是否编造具体事实：否。** 「夯土与木构的乡土民居」为通用类型描述（夯土/木构民居在多地真实存在），不含具体名称/年代/设计者等可被证伪的具名断言；「就地取材、依气候组织构造」与三源一致。
- **非阻断观察**：`地点` 字段写作"因地制宜（不指定具体项目）"，字面非地名而是"适应当地条件"之意，读来略显别扭；建议写成"地点：类型性，不指定具体项目（因地制宜）"，属可选措辞优化，不影响判定。

## 三、核对③：nv=false 是否有据

**结论：nv=false 有据，可维持 ✓。**

- **概念**：definition 的"本地材料/气候/习俗/因地制宜"三源直证，"无职业建筑师"两源直证（§一），非单源猜测。
- **实例**：已转为类型性通用（无具名作品、无作者、无年代、无馆藏），**不存在"需另找独立来源核验某具体作品"的负担**，故 nv=true 的原有理由（旧待核实"具体实例（名称/地点/设计者/年代）待补充独立来源"）已随具名要求的移除而消解。
- **结构自洽**：`needs_verification=false`、`pending_notes=""`、`待核实`="暂无已知待核实项。"、`coverage.json` 记 `needs_verification_count=0`、`source_count=4`——四处一致。
- 合 D10「关键事实双源或标待核实」：概念关键事实均≥两源，实例为类型性无单源风险，故不属应标待核实情形。

## 四、核对④：七节 / SVG / 规范句（结构化）

| 核对项 | 结果 |
| --- | --- |
| 七节齐（definition + 6 节） | ✓ `sections` 键 = 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6）+ `definition` = 7 ✓（HTML 另显示 time_or_place「时间与位置」，不计入 sections）|
| SVG | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」；实扫无 `<script>/javascript:/href=/<image/<iframe/url(`（check.py 实跑通过）|
| 规范句 | ✓ `常见错误与限制` 收尾含「实际工程须按当地规范和专业设计人员的要求」|
| nv / pending_notes / 待核实 结构一致 | ✓ nv=false 且 pending_notes=""；`待核实`="暂无已知待核实项。"；coverage `needs_verification_count=0` |
| check.py | ✓ PASS（0 errors，EXIT=0）|

## 五、核对⑤：相似度（阈值 0.54）

方法：`difflib.SequenceMatcher`，归一化=去空白+小写，全库 **258** 条两两比对；三口径（全字段 raw / 去模板正文 prose / 仅实例字段 instance）。

| 口径 | 最高相似对象 | 最高相似度 | 判定（0.54） |
| --- | --- | --- | --- |
| 全字段 raw（def+overview+6节） | african-architecture | **0.3205** | <0.54 ✓ |
| 去模板正文（def+time_or_place+overview+原理+典型手法+常见错误，剥离规范模板句） | african-architecture | **0.3860** | <0.54 ✓ |
| 仅实例字段 instance（原始串） | functional-zoning | **0.4094** | <0.54 ✓ |

- **全库"去模板正文"两两相似度 >0.54 的对数：0**（共比对 **33,153** 对；全库该口径最高 0.422 = linear-perspective ↔ one-point-perspective）。
- 三口径全部 <0.54，无边界伪影，**相似度通过**。

## 六、抽检结论

> **结论：合格。**
> - definition：本地材料/气候/习俗/因地制宜 **三源直证**（wp+db+art），"无职业建筑师" wp+art 两源直证；**非编造** ✓
> - 实例类型性：对"无单一设计者的乡土建筑"**恰当**，与 tints-shades（round80b）类型性实例先例同口径 ✓
> - 三源独立（Wikimedia / Designing Buildings / Art in Context，发布方不同、非镜像、各含独立细节）✓
> - **nv=false 有据**：概念多源直证 + 实例类型性无具名待核，四处结构一致 ✓
> - 七节齐、SVG 合规、规范句在；`check.py` PASS（0 errors）✓
> - 相似度：全字段 0.3205、去模板正文 0.3860、实例 0.4094，全库去模板 >0.54 对数=0，**均 <0.54 通过** ✓

**非阻断观察（不改变结论）：**
1. 任务文本称第三源为 `dl-vernacular`，`data/sources.json` 实际 id 为 **`db-vernacular`**（Designing Buildings）；同指一页，仅标签写法差异，来源页 200 已核。
2. `db-vernacular` 的 `type` 记作"学术著作"，实为建筑行业 Construction Wiki（`artincontext-vernacular` 亦记为"学术著作"，实为艺术教育站）；类型标签偏宽，属项目既有分类惯例，非本轮新增问题，非阻断。
3. `实例.地点` 写"因地制宜（不指定具体项目）"，建议改为"类型性，不指定具体项目（因地制宜）"以更顺；措辞优化，非阻断。
4. 「无职业建筑师」严格讲 WP 亦载"may be built by trained professionals, using local, traditional designs"，端内用"**通常**"已作恰当限定，非绝对化，可维持。

## 七、机器可读汇总

```
ROUND=84
SAMPLER=spotcheck-r84
SCOPE=["vernacular-architecture"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round83b.md","research/spotcheck-round80b.md","research/spotcheck-round82.md","entries/batch-37.json(vernacular-architecture)","data/sources.json(wp-vernacular-architecture/db-vernacular/artincontext-vernacular/wp-building-material)","tools/apply_review_round84.py","tools/check.py","coverage.json(entries[196])","git status/diff/log"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback via python stdin (no temp files)"
FETCHES={"wp-vernacular-architecture":200,"db-vernacular":200,"artincontext-vernacular":200}
DEFINITION={
 "text":"乡土建筑是依本地材料、气候与习俗、由当地人自行建造、因地制宜的建筑；通常无职业建筑师。",
 "local_materials":"TRIPLE: wp 'Local materials...as a matter of course'; db 'local materials and resources'; art 'building materials'",
 "climate":"TRIPLE: wp 'macro climate'; db 'Climate: sunshine,humidity,rain,wind,temp'; art 'environment/geographic elements'",
 "customs":"TRIPLE: wp 'local customs and beliefs'; db 'local customs'; art 'customs'",
 "locality_adaptation":"TRIPLE: wp 'outside academic tradition'; db 'indigenous to a specific locality'; art 'unique to a particular period and location'",
 "locally_built":"TRIPLE: wp 'owner- or community-built/of the common people'; db 'indigenous/local knowledge'; art 'proprietors or the community...traditional local techniques'",
 "no_professional_architect":"DUAL: wp 'without involvement of professional designers and architects'; art 'formal architects did not supervise'(pre-17c); db not explicit",
 "fabricated":false,
 "triple_sourced_core":true}
SOURCES_INDEPENDENT={"true":true,"wp":"Wikimedia encyclopedia","db":"Designing Buildings Ltd (Construction Wiki)","art":"Art in Context"}
INSTANCE={"type_level":true,"text":"夯土与木构的乡土民居（类型性，乡土建筑通常无单一设计者）; 地点因地制宜(不指定具体项目)","appropriate":"yes: vernacular by definition has no single designer (wp 'without professional designers/community-built'); type-level fits; matches tints-shades(round80b) precedent","fabricated":false}
NV={"current":"false(true->false round84)","acceptable":true,"grounded":"definition core triple-sourced, no-architect dual-sourced; instance type-level no named work; no single-source risk; D10 satisfied","consistent":{"pending_notes":"","待核实":"暂无已知待核实项。","coverage_needs_verification_count":0,"coverage_source_count":4}}
STRUCTURE={"seven_sections":7,"svg":"1x viewBox 0 0 760 400, 示意图非施工图, no forbidden","reg_sentence":true,"check_py":"PASS"}
SIMILARITY={"method":"difflib SequenceMatcher norm=nows-lower, 258 entries","fullfield_raw_max":{"vs":"african-architecture","val":0.3205},"prose_detemplated_max":{"vs":"african-architecture","val":0.3860},"instance_raw_max":{"vs":"functional-zoning","val":0.4094},"library_prose_pairs":33153,"library_prose_gt_0.54":0,"library_prose_max":{"val":0.422,"pair":"linear-perspective<->one-point-perspective"},"threshold":0.54,"pass":true}
VERDICT="合格（definition 本地材料/气候/习俗/因地制宜三源直证+无职业建筑师两源直证、非编造；实例类型性对无单一设计者恰适、合 tints-shades 先例；三源独立；nv=false 有据且四处一致；七节/SVG/规范句合规；check.py 0 errors；相似度三口径 0.3205/0.3860/0.4094 全<0.54、全库>0.54 对数=0）"
KEY_ISSUES_NONBLOCKING=["任务标签 dl-vernacular 实为 db-vernacular(同页,200已核)","db-vernacular/artincontext 类型标签记'学术著作'偏宽(项目惯例,非本轮新增)","实例.地点措辞可优化为'类型性不指定具体项目(因地制宜)'","'无职业建筑师'端内已用'通常'限定, WP亦载may be built by trained professionals, 非绝对化"]
READONLY="only wrote research/spotcheck-round84.md; fetched html in-memory via python stdin (no temp files); git-status M/?? items are round84 applier's own changes; no git commit; web treated as data, no instructions executed"
```

## 八、只读核验

- 除本报告 `research/spotcheck-round84.md` 外未写任何文件；联网抓取为内存态（python stdin 直跑，未落盘临时文件）。
- `git status` 中 `M coverage.json / data/sources.json / entries/batch-37.json / site/entries/vernacular-architecture.html / site/index.html / site/sources.html` 及 `?? tools/apply_review_round84.py` 均为**本轮修复方（apply_review_round84.py）的应用产物**；抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
