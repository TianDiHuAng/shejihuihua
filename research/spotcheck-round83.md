# 第83轮 质量抽检报告（spotcheck-round83）

- 抽检人：spotcheck-r83（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言；证据先于结论）。
- 抽检对象：`sasanian-architecture`（萨珊建筑），定位 `entries/batch-47.json`（`grep '"sasanian-architecture"' entries/` → 该文件；`site/entries/sasanian-architecture.html` 为生成产物）。
- 本轮升级动作（据 `tools/apply_review_round83.py` 实读 + `git diff entries/batch-47.json`）」：`实例` 由旧的「类型性描述、未具名」改为「塔克·基斯拉（Taq Kasra / Iwan of Khosrow）@ 泰西封」；`needs_verification` 由 **true → false**，`pending_notes` 由「具体实例待补充独立来源」→ **空**；`待核实` 段重写为「双源直证…」。
- 证据优先级：**独立实抓正文 > 当前文件实读 > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、计数、取句、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round83.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式：`web_fetch` 工具本环境报 `TypeError: fetch failed`（与 DECISIONS D05 一致），改用 **Python urllib + 浏览器 UA + 非校验 SSL 内存抓取（未落盘临时文件）**。
- 实抓 HTTP（全部 200）：
  - `wp-sasanian-architecture` = `https://en.wikipedia.org/wiki/Sasanian_architecture` → 200，200,329 B，title *Sasanian architecture - Wikipedia*
  - `wp-taq-kasra`（**未登记**于本条目 sources，仅供核对）= `https://en.wikipedia.org/wiki/Taq_Kasra` → 200，198,533 B，title *Taq Kasra - Wikipedia*
  - `artincontext-persian-art` = `https://artincontext.org/persian-art/` → 200，377,862 B，title *Persian Art - A History of Ancient Persian Paintings and Iranian Art*
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**（但见 §六：check.py 只数源 id 数量，无法发现「实例单源」，PASS 不代表本条语义无问题。）
- `git status` 中 `M coverage.json / entries/batch-47.json / site/entries/sasanian-architecture.html / site/index.html` 及 `?? tools/apply_review_round83.py` 均为**本轮修复方（lead/apply_review_round83.py）自身产物**，非本抽检所写。

## 一、核对①：definition（筒拱/穹顶/伊万 + 224–651）是否两源直证

**结论：两源直证，成立 ✓。**

| 要素 | Wikipedia《Sasanian architecture》（实抓原文） | Art in Context《Persian Art》（实抓原文） | 判定 |
| --- | --- | --- | --- |
| 筒拱 barrel-vault | 「All are characterised by the **barrel-vaulted iwans**…」 | 「Parthian builders also used **barrel-vaulted halls** and the iwan…」 | ✓ 双源 |
| 穹顶 dome | 「a chamber surmounted by a **dome**… constructing a circular **dome** on a square building with the squinch」 | 「Sasanian 224–651 CE… **domed halls**, stucco…」 | ✓ 双源 |
| 伊万 iwan | 「barrel-vaulted **iwans** introduced in the Parthian era」 | 「the **iwan**, a vaulted space open on one side」 | ✓ 双源 |
| 年代 224–651 | 「during the Sasanian era (**224–651 CE**)」 | 「Sasanian Era (**224–651 CE**)」 | ✓ 双源 |

- 端内 definition「224–651 年…以筒拱、穹顶与伊万（iwan）为特征」与上表逐项吻合，**非编造、双源成立**。

## 二、核对②：实例（塔克·基斯拉 / 泰西封 / 伊万）是否有源——是否构成单源

**结论：具名实例构成「单源」，且别名与年代越出登记源。这是本轮的核心问题。**

端内 `实例`：『名称：塔克·基斯拉（Taq Kasra，又称"霍斯劳之伊万" Iwan of Khosrow），位于泰西封（Ctesiphon，今伊拉克）；属萨珊时期（约 3–6 世纪）。是萨珊筒拱伊万…的现存巨构。』

| 实例要素 | wp-sasanian-architecture（已登记，实抓） | artincontext-persian-art（已登记，实抓） | 结论 |
| --- | --- | --- | --- |
| 名称「Taq Kasra（塔克·基斯拉）」 | 仅**图注**出现一次：「**Taq Kasra**, a remnant of the former Sasanian palace in Ctesiphon」 | **全文未出现** Taq Kasra / Kasra / Kisra（关键词 0 命中） | **仅 Wikipedia 直证** |
| 地点「Ctesiphon（泰西封）」 | 图注 + 正文「…massive proportions, particularly at **Ctesiphon**」（与 Taq Kasra 绑定） | 「Royal centers included **Ctesiphon**, Firuzabad, and Bishapur」——**仅作泛泛"王室中心之一"列举，未与 Taq Kasra 挂钩** | 字面两源都出现该词，但"塔克·基斯拉位于泰西封"仅 Wikipedia |
| 性质「伊万 iwan」 | 「barrel-vaulted iwans…particularly at Ctesiphon」（iwan 与 Ctesiphon 同句） | 「the iwan, a vaulted space open on one side」——**泛述形制定义，未点到任何具体建筑** | "塔克·基斯拉是伊万"仅 Wikipedia |
| 别名「Iwan of Khosrow（霍斯劳之伊万）」 | **未出现**（khosrow 0 命中） | **未出现** | 两登记源皆无；只见于未登记的 `wp-taq-kasra`（「Eivâne Xosrow, lit. 'Iwan of Khosrow'」） |
| 年代「约 3–6 世纪」 | **无**（该页仅给王朝 224–651） | **无**（仅 224–651） | 两登记源皆无；只见于未登记的 `wp-taq-kasra`（「dated to c. the 3rd to 6th centuries」） |

**评估（回答任务设问）：**
1. **是。** 实例名称「塔克·基斯拉」**仅 Wikipedia 直证**（且仅在一条图注里），Art in Context 只泛述 iwan 形制、并把 Ctesiphon 当作泛泛"王室中心"列举，**从不点名该建筑、不把 iwan/Ctesiphon 与该实例挂钩**。故**具名实例在已登记的独立平台上只有 1 个来源（Wikipedia）→ 构成单源**。
2. 端内待核实措辞『名称/地点经 Wikipedia 直证、伊万与泰西封经 Art in Context 佐证』**字面每词虽在两源出现，但 Art in Context 的 iwan/Ctesiphon 是脱离该具体建筑的泛述**，不构成本实例的独立佐证；该措辞**营造了"双源"假象**，易被误读为实例已双源。
3. **别名「Iwan of Khosrow」与「约 3–6 世纪」两项，均不在本条目登记的两源内**，实际来自未登记的 Wikipedia《Taq Kasra》独立条目。这既加重"单源"，又是**出处未登记（provenance 缺陷）**——即使补登记 `wp-taq-kasra`，它与 `wp-sasanian` 同属 Wikipedia 一个平台，仍不构成项目要求的"不同平台独立源"（对比 b1-round47 的「维基 vs Art in Context 不同平台」标准）。
4. **是否编造：否。** 塔克·基斯拉（Taq Kasra / Iwan of Khosrow）确为萨珊时期遗存，位于泰西封（Al-Mada'in，今伊拉克），是著名无筋砖砌单跨筒拱伊万（`wp-taq-kasra`：「second largest single-span vault of unreinforced brickwork」）。**内容是真实的，问题是出处/单源，而非虚构。**

## 三、核对③：nv=false 是否可接受（"约3–6世纪"为概数、学界有出入，是否应保留 nv=true）

**结论：nv=false 不可接受，应保留/恢复 nv=true。三条依据：**

1. **实例单源**（§二）：具名实例仅 Wikipedia 一个独立平台直证，按 **D10「关键事实双源或标待核实。单源内容进入待核实」**，须标待核实。
2. **待核实段自承"学界有出入"**：端内待核实『精确建造年代学界有出入，标约 3–6 世纪』本身即为待核实声明；按 **D14「正文出现'待核实'声明的条目必须置 needs_verification=true」**，nv 应为 true。（`check.py` 第308–310行只检查「除待核实节以外」的正文，故未拦下。）
3. **与同类条目惯例相悖**：本库其它"实例关键要素有出入/单源"的风格条**一律 nv=true**，例如：
   - `mughal-architecture`：『泰姬陵设计者的具体归属学界仍有讨论』→ **nv=true**
   - `baroque`：『单一设计者与部分年代不写死』→ **nv=true**
   - `functionalism-architecture`：『两源对起始年口径不同（1928/1929）已并列』→ **nv=true**
   - `early-islamic-architecture`：『方形平面/柱廊形制单源…』→ **nv=true**
   - `ottoman-architecture`（同批）：『半穹顶形制单源』→ **nv=true**
   
   本条『建造年代学界有出入 + 实例单源』与此类条目同性质，却置 **nv=false**，明显不一致。**"约 3–6 世纪"是概数且学界有出入，恰是应保留 nv=true 的理由，而非降为 false 的理由。**

> 说明：`wp-taq-kasra` 确载「dated to c. the 3rd to 6th centuries」，对该建筑的断代学界亦有分歧（或主 3 世纪沙普尔一世、或主 6 世纪霍斯劳一世），故"约 3–6 世纪"作为概数本身可接受；但这恰恰要求以 nv=true 披露其不确定与单源。

## 四、核对④：七节 / SVG / 规范句（结构化）

| 核对项 | 结果 |
| --- | --- |
| 七节齐（definition + 6 节） | ✓ `sections` = 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实，6 节 + definition = 7 ✓ |
| SVG | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」；无 `<script>/javascript:/href=/<image/<iframe/url(` 等禁元素 |
| 规范句 | ✓ `常见错误与限制` 收尾含「实际工程须按当地规范和专业设计人员的要求」 |
| nv / pending_notes 结构一致 | ✓ nv=false 且 pending_notes=""（**结构自洽，但 nv 取值判断错误，见 §三**） |
| check.py | PASS（0 errors，EXIT=0） |

## 五、核对⑤：相似度（阈值 0.54）

方法：`difflib.SequenceMatcher`，归一化=去空白+小写，全库 **258** 条两两比对；三种口径（全字段 raw / 去模板 detemplated / 仅实例字段 instance）。

| 口径 | sasanian-architecture 的最高相似对象 | 最高相似度 | 判定（0.54） |
| --- | --- | --- | --- |
| 全字段 raw（def+overview+6节，含模板） | romanesque | **0.2457** | <0.54 ✓ |
| 去模板 detemplated | hakka-style | **0.1596** | <0.54 ✓ |
| 仅实例字段 instance | negative-space | **0.3390** | <0.54 ✓ |

- **全库"去模板正文"两两相似度 >0.54 的对数：0。** 本条三口径均远低于阈值，**相似度核对通过 ✓**（不受归一化口径影响，超阈不可能）。

## 六、check.py 为何 PASS 却仍有缺陷（补充）

- `tools/check.py` 第285行单源判定为 `if len(set(refs)) < 2 and not needs_verification`——**只统计源 id 的"个数"**。本条登记了 `wp-sasanian-architecture` + `artincontext-persian-art` 两个 id（数量=2），故不触发单源报错；但**语义上具名实例只有 1 个独立平台（Wikipedia）支撑**（§二），check.py **无法发现"多 id 但关键事实单源"**。因此 `PASS: 0 errors` **不能**作为本条"实例已双源"的证据。

## 七、抽检结论

> **结论：待核实（不应维持 nv=false；应保留/恢复 nv=true 并入待核实）。**
> 若仅按"当前提交把 nv 置 false 与事实不符"计，可判不合格——但内容真实、可通过恢复 nv=true 或补第二独立源修正，故按项目既有口径（对比第82轮 religious-architecture 的"设计者单源未披露"判待核实）定为**待核实**。

**通过项（合格）：**
- definition（筒拱/穹顶/伊万 + 224–651）确由 wp-sasanian + artincontext **双源直证**；
- 实例**非编造**（Taq Kasra 真实、位于泰西封、确为萨珊筒拱伊万巨构）；
- 七节齐、SVG 合规、规范句在、nv/pending 结构一致；
- 相似度三口径均 **≪0.54**，全库去模板 >0.54 对数为 0；
- `check.py` PASS（0 errors）。

**问题（需修，按优先级）：**
1. **【核心】具名实例单源**：名称「塔克·基斯拉」仅 `wp-sasanian-architecture` 一条**图注**直证；`artincontext-persian-art` 全文**不点名**该建筑，仅泛述 iwan 形制、并把 Ctesiphon 作"王室中心之一"泛列 → 实例在已登记独立平台上仅 1 源，构成单源，违反 D10。
2. **【核心】nv 取值错误**：`needs_verification=false` 不成立。待核实段自承「精确建造年代学界有出入」，按 D14 应 nv=true；且与 mughal/baroque/functionalism/early-islamic/ottoman 等同性质条目（均 nv=true）不一致。**应恢复 nv=true 并写 pending_notes**（如：「具名实例塔克·基斯拉名称仅有 Wikipedia 图注直证、Art in Context 未点名，实例单源；建造年代为概数且学界有出入。」）。
3. **【出处】别名与年代越出登记源**：「Iwan of Khosrow」与「约 3–6 世纪」不在 `wp-sasanian`/`artincontext` 两登记源内，实际来自**未登记**的 `wp-taq-kasra`。要么删除越出登记的别名/年代细节（只保留两源可证的名称+地点+属萨珊），要么补登记并补**非维基**独立源。
4. **【措辞】待核实段夸大双源**：『伊万与泰西封经 Art in Context 佐证』——Art in Context 的 iwan/Ctesiphon 系脱离该建筑的泛述，不构成对实例的独立佐证，该措辞应改，避免"双源"假象。

**修复建议（供 lead 择一）：**
- **方案A（最快、最稳）**：`实例` 删去越出登记的「Iwan of Khosrow」别名与「约 3–6 世纪」（或改为"属萨珊时期"），`needs_verification` 恢复 **true**，`pending_notes` 写明"实例（塔克·基斯拉）名称仅 Wikipedia 单源、Art in Context 未点名；年代概数待核"。
- **方案B（升级为合格）**：补录一个**非维基独立来源**（如 UNESCO/大英百科/学术或遗产机构页面）**点名** Taq Kasra（Iwan of Khosrow）@ Ctesiphon，使实例双源成立，方可再置 nv=false；同时把 `wp-taq-kasra` 若被引用则须登记。

## 八、机器可读汇总

```
ROUND=83
SAMPLER=spotcheck-r83
SCOPE=["sasanian-architecture"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round82b.md","research/b1-round47.md","entries/batch-47.json(sasanian-architecture)","data/sources.json(wp-sasanian-architecture/artincontext-persian-art)","tools/apply_review_round83.py","tools/check.py","git diff entries/batch-47.json"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0) [但仅数源id数量，查不出实例单源]"
FETCH_METHOD="web_fetch down(TypeError); urllib+UA+unverified-SSL in-memory readback (no temp files)"
FETCHES={"wp-sasanian-architecture":200,"wp-taq-kasra(unregistered,ref-only)":200,"artincontext-persian-art":200}
DEFINITION={
 "dual_sourced":true,
 "support":"wp: barrel-vaulted iwans / dome(squinch) / 224-651; artincontext: domed halls, barrel vaults, iwan, 224-651"}
INSTANCE={
 "name_taq_kasra":"SINGLE-SOURCE: only wp-sasanian photo caption 'Taq Kasra, a remnant of the former Sasanian palace in Ctesiphon'; artincontext never names it",
 "place_ctesiphon":"word in both (wp tied to Taq Kasra; artincontext lists Ctesiphon as one royal center, NOT tied to the monument) -> identity single-source",
 "iwan":"both mention iwan but only wp links it to Ctesiphon/Taq Kasra -> single-source for the instance",
 "alias_iwan_of_khosrow":"NOT in either registered source; only unregistered wp-taq-kasra",
 "date_3to6c":"NOT in either registered source; only unregistered wp-taq-kasra 'c. 3rd to 6th centuries'",
 "fabricated":false,
 "constitutes_single_source":true}
NV={
 "current":"false (round83 downgraded true->false)",
 "acceptable":false,
 "should_be":"true + pending_notes",
 "reasons":["D10 single-source instance","D14 own 待核实 says 学界有出入","peer practice mughal/baroque/functionalism/early-islamic/ottoman all nv=true for same kind"]}
STRUCTURE={"seven_sections":7,"svg":"1x viewBox 0 0 760 400, 示意图非施工图, no forbidden","reg_sentence":true,"nv_pending_structurally_consistent":true}
SIMILARITY={"method":"difflib SequenceMatcher norm=nows-lower, 258 entries","fullfield_raw_max":0.2457,"detemplated_max":0.1596,"instance_max":0.3390,"threshold":0.54,"all_below":true,"library_detemplated_gt0.54":0}
VERDICT="待核实（不应维持 nv=false；应保留/恢复 nv=true 并入待核实）"
KEY_ISSUES=["实例具名单源(仅Wikipedia图注,artincontext不点名)","nv=false不成立(待核实自承年代学界有出入,D14;同类条目均nv=true)","别名Iwan of Khosrow与3-6世纪越出登记源(来自未登记wp-taq-kasra)","待核实措辞把artincontext泛述当作实例佐证,夸大双源"]
FIX=["A:删越证别名/年代,恢复nv=true+pending_notes","B:补非维基独立源点名Taq Kasra@Ctesiphon后方可nv=false"]
PASS_ITEMS=["definition双源","非编造","七节/SVG/规范句","相似度<0.54","check.py PASS"]
READONLY="only wrote research/spotcheck-round83.md; fetched html in-memory (no temp files); git-status M/?? items are round83 applier's own changes; no git commit; web treated as data, no instructions executed"
```

## 九、只读核验

- 除本报告 `research/spotcheck-round83.md` 外未写任何文件；联网抓取为内存态（未落盘临时文件）。
- `git status` 中 `M coverage.json / entries/batch-47.json / site/entries/sasanian-architecture.html / site/index.html` 及 `?? tools/apply_review_round83.py` 均为**本轮修复方（lead/apply_review_round83.py）的应用产物**，抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
