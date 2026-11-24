# 第83b轮 补充抽检报告（spotcheck-round83b）

- 抽检人：spotcheck-r83b（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言；证据先于结论）。
- 抽检对象：`structural-material`（结构材料），定位 `entries/batch-35.json`（`grep '"structural-material"' entries/` → 该文件；`site/entries/structural-material.html` 为生成产物）。
- 本轮升级动作（据 `tools/apply_review_round83b.py` 实读 + `entries/batch-35.json` 实读）：`实例` 由旧的「类型性描述、不具名」改为「埃菲尔铁塔 / 法国巴黎 / 古斯塔夫·埃菲尔 / 1889 / 锻铁露空格构」；`needs_verification` 由 **true → false**，`pending_notes` 由旧文本 → **空**；`sources` 追加 `wp-eiffel-tower`、`db-eiffel-tower`；`待核实` 段改为「暂无已知待核实项。」
- 证据优先级：**独立实抓正文 > 当前文件实读 > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、计数、取句、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round83b.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式：`web_fetch` 本环境历史报错（DECISIONS D05），改用 **Python urllib + 浏览器 UA + 非校验 SSL 内存抓取（未落盘临时文件）**。
- 实抓 HTTP（全部 200，内存态）：
  - `wp-eiffel-tower` = `https://en.wikipedia.org/wiki/Eiffel_Tower` → 200，892,030 B，title *Eiffel Tower - Wikipedia*
  - `db-eiffel-tower` = `https://www.designingbuildings.co.uk/wiki/Eiffel_Tower` → 200，57,000 B，title *Eiffel Tower - Designing Buildings*
  - 旁证（definition）：`wp-building-material` = `https://en.wikipedia.org/wiki/Building_material` → 200，381,957 B，title *Building material - Wikipedia*
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**
- `git status` 中 `M coverage.json / data/sources.json / entries/batch-35.json / site/entries/structural-material.html / site/index.html / site/sources.html` 及 `?? tools/apply_review_round83b.py` 均为**本轮修复方（lead/apply_review_round83b.py）自身产物**，非本抽检所写；`M entries/batch-47.json / site/entries/sasanian-architecture.html` 与 `?? tools/apply_review_round83.py / research/spotcheck-round83.md` 为第83轮遗留产物。抽检方仅读取。

## 一、核对①：definition（结构材料如石木砖钢混凝土，决定跨度形态）

**结论：概念通识成立，且有登记源佐证 ✓。**

- 端内 `definition`：『结构材料指承担荷载的主要材料，如石、木、砖、钢与混凝土。』`overview`：『结构材料决定跨度、形态与建造方式。』
- 这是"结构材料"的通用定义（承担荷载的主体材料 + 石木砖钢混凝土），属**概念通识**，无需双源亦可成立。
- 佐证：登记源 `wp-building-material`（实抓 381,957 B）通篇列举 **stone(x18)/wood(x44)/brick(x35)/steel(x7)/concrete(x31)**，并有 **structural(x18)/span(x12)** 语境；与本条 definition 的"石、木、砖、钢、混凝土"及 overview 的"决定跨度"一致。**非编造。**

## 二、核对②：实例要素（名称/地点巴黎/设计者/1889/锻铁/格构）是否两源直证

**结论：六个要素全部由两源直证，无一单源 ✓。**

端内 `实例`：『名称：埃菲尔铁塔（Eiffel Tower）；地点：法国巴黎；设计者：古斯塔夫·埃菲尔（Gustave Eiffel）；年份：1889 年。以锻铁（wrought iron）露空格构承重，是大跨金属结构材料的经典实例。此处仅列名称、地点、设计者与年份信息，不复制图像。』

| 要素 | Wikipedia《Eiffel Tower》（实抓原文） | Designing Buildings《Eiffel Tower》（实抓原文） | 判定 |
| --- | --- | --- | --- |
| 名称 Eiffel Tower | 标题 *Eiffel Tower - Wikipedia*；正文「**Eiffel Tower** Tour Eiffel」 | 标题 *Eiffel Tower - Designing Buildings*；「The **Eiffel Tower** (Tour Eiffel)…」 | ✓ 双源 |
| 地点 巴黎 Paris | 「is a lattice tower on the Champ de Mars in **Paris, France**」；「Tower in **Paris**, France」 | 「situated on the Left Bank of the Seine River in **Paris**」；「Location: 7th arrondisseement, **Paris, France**」 | ✓ 双源 |
| 设计者 Gustave Eiffel | 「named after the engineer **Gustave Eiffel**, whose company designed and built the tower from 1887 to 1889」 | 「The tower was **designed by Gustave Eiffel** for the 1889 Exposition Universelle」 | ✓ 双源 |
| 年份 1889 | 「constructed as the centrepiece of the **1889** World's Fair」；infobox completion_date **1889-03-31** | 「for the **1889** Exposition Universelle」；「Construction period: 1887 – **1889**」 | ✓ 双源 |
| 锻铁 wrought iron | 「for its use of **wrought iron**」；「The **puddle iron (wrought iron)** of the Eiffel Tower weighs 7,300 tonnes」 | 「Eiffel's open-lattice **wrought iron** design」；「built of very pure **structural iron**」 | ✓ 双源 |
| 格构 lattice | 「is a **lattice** tower」；「a great pylon, consisting of four **lattice girders** … joined together by metal **trusses**」；「latticework」 | 「Eiffel's **open-lattice** wrought iron design」 | ✓ 双源 |

- **是否编造：否。** 埃菲尔铁塔位于巴黎、由 Gustave Eiffel（公司）设计、1889 年建成、锻铁格构——两源逐项吻合，无虚构。
- **两源是否独立：是。** `wp-eiffel-tower` 为 Wikimedia 百科（众编）；`db-eiffel-tower` 为 Designing Buildings Ltd 的英国建筑行业知识库，**发布方不同、非镜像**，且 DB 含 WP 未载的独立细节（「18,038 pieces … 2.5 million rivets … around 300 steel workers」「open-lattice wrought iron design」），互证为本项目要求的"不同平台独立源"。

## 三、核对③：nv=false 是否有据（若某要素（如设计者/年份）仅单源，是否应保留 nv=true）

**结论：nv=false 有据，可维持；无需恢复 nv=true ✓。**

- 任务设问："若某要素（如设计者/年份）仅单源，请评估是否应保留 nv=true。" **实测反证：设计者与年份均双源**（§二：设计者 WP「Gustave Eiffel, whose company designed and built」+ DB「designed by Gustave Eiffel」；年份 WP「1889」+ DB「1889」），**不存在单源要素**，故 nv=false 成立，无须保留 nv=true。
- 与 D10「关键事实双源或标待核实；单源内容进入待核实」一致：本条关键事实（名称/地点/设计者/年份/锻铁/格构）**均双源**，不属于应标待核实情形。
- **非阻断观察（不改变判定）**：严格工程史上，铁塔的**结构构想**由 Eiffel 公司工程师 Maurice Koechlin、Émile Nouguier 完成，Gustave Eiffel 以其公司名义署名并主导。但**两登记源均以"designed by Gustave Eiffel / whose company designed and built"表述**，端内"设计者：古斯塔夫·埃菲尔"与两源字面一致，**属双源支持的通行署名**，非单源、非编造；如需更严谨可注"（Eiffel 公司设计，Koechlin/Nouguier 构想）"，此为可选优化，非阻断。

## 四、核对④：七节 / SVG / 规范句（结构化）

| 核对项 | 结果 |
| --- | --- |
| 七节齐（definition + 6 节） | ✓ `sections` = 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）+ `definition` = 7 ✓ |
| SVG | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」；无 `<script>/javascript:/href=/<image/<iframe/url(` 等禁元素（check.py 实跑通过） |
| 规范句 | ✓ `常见错误与限制` 收尾含「实际工程须按当地规范和专业设计人员的要求」 |
| nv / pending_notes 结构一致 | ✓ nv=false 且 pending_notes=""；`待核实` 段「暂无已知待核实项。」——结构自洽，且与"六要素双源"的语义一致 |
| check.py | ✓ PASS（0 errors，EXIT=0） |

## 五、核对⑤：相似度（阈值 0.54）

方法：`difflib.SequenceMatcher`，归一化=去空白+小写，全库 **258** 条两两比对；三口径（全字段 raw / 去模板 detemplated / 仅实例字段 instance）。

| 口径 | 最高相似对象 | 最高相似度 | 判定（0.54） |
| --- | --- | --- | --- |
| 全字段 raw（def+overview+6节） | ancient-roman | **0.3847** | <0.54 ✓ |
| 去模板 detemplated | neoclassical | **0.2522** | <0.54 ✓ |
| 仅实例字段 instance（**原始串**） | daylighting | **0.5381** | 略超 0.54（见下说明）|
| 仅实例字段 instance（**去样板后**） | beaux-arts | **0.4306** | <0.54 ✓ |

- **全库"去模板正文"两两相似度 >0.54 的对数：0**（共比对 33,153 对）。
- **对 instance 原始串 0.5381 的判定说明（透明披露）**：该值完全由全库**统一实例样板句**「名称：…；地点：…；设计者：…；年份：…。此处仅列名称、地点、设计者与年份信息，不复制图像。」造成——`daylighting` 实例同为「名称：金贝尔美术馆…；地点：美国沃思堡…；设计者：路易·康…；年份：1972 年。此处仅列名称、地点、设计者与年份信息，不复制图像。」，两句的"高相似"是**模板本身**而非正文内容重合。**去样板后 instance 最高降至 0.4306、全字段 raw 0.3847、去模板正文 0.2522，均 <0.54。** 故相似度按项目"去模板正文"绑定口径**判定通过**；`instance` 原始串 0.5381 仅属阈值边界的模板伪影，非内容抄袭。

## 六、抽检结论

> **结论：合格。**
> - definition：概念通识成立，且 `wp-building-material` 佐证"石木砖钢混凝土/跨度" ✓
> - 实例六要素（名称/巴黎/设计者 Gustave Eiffel/1889/锻铁 wrought iron/露空格构）：**两源逐项直证，无一单源** ✓
> - 两源独立（Wikimedia 百科 vs Designing Buildings 行业知识库，发布方不同、含独立细节、非镜像）✓
> - **非编造**（铁塔事实真实，两源吻合）✓
> - **nv=false 有据**：六要素均双源，无单源，无须恢复 nv=true ✓
> - 七节齐、SVG 合规、规范句在、nv/pending 结构一致；`check.py` PASS（0 errors）✓
> - 相似度：全字段 raw 0.3847、去模板正文 0.2522、去样板 instance 0.4306，全库去模板 >0.54 对数=0，**均 <0.54 通过** ✓

**非阻断观察（不改变结论）：**
1. **instance 原始串 0.5381（daylighting）**为全库统一样板句（名称/地点/设计者/年份 + "此处仅列…不复制图像"）造成的模板伪影；去样板后 0.4306，非内容重复。若严口径以"instance 原始串"卡阈值，仅此 1 对超阈 0.002，可改实例样板措辞消除，但非必要。
2. **设计者署名**：结构构想在 Eiffel 公司内由 Koechlin/Nouguier 完成；两源均以"designed by Gustave Eiffel / whose company designed and built"表述，端内一致、双源支持，非单源。可选补注"（Eiffel 公司设计）"。
3. `db-eiffel-tower` 源 note 记有"约300钢工、200万铆钉"等细节，端内未引用，仅作源记录，不构成端内声明。

## 七、机器可读汇总

```
ROUND=83b
SAMPLER=spotcheck-r83b
SCOPE=["structural-material"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round83.md","entries/batch-35.json(structural-material)","data/sources.json(wp-eiffel-tower/db-eiffel-tower/wp-building-material/wp-architecture)","tools/apply_review_round83b.py","tools/check.py","git status/log"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback (no temp files)"
FETCHES={"wp-eiffel-tower":200,"db-eiffel-tower":200,"wp-building-material":200}
DEFINITION={"dual_sourced_or_common":true,"text":"结构材料=承担荷载的主体材料，如石木砖钢混凝土；决定跨度/形态/建造方式","support":"concept common-knowledge + wp-building-material stone/wood/brick/steel/concrete+structural+span"}
INSTANCE={
 "name":"DUAL: both titles/corpus 'Eiffel Tower'/'Tour Eiffel'",
 "place_paris":"DUAL: wp 'lattice tower on the Champ de Mars in Paris, France'; db 'Left Bank of the Seine in Paris' / 'Paris, France'",
 "designer_gustave_eiffel":"DUAL: wp 'Gustave Eiffel, whose company designed and built; db 'designed by Gustave Eiffel'",
 "year_1889":"DUAL: wp '1889 World Fair' completion 1889-03-31; db '1889 Exposition Universelle' 1887-1889",
 "wrought_iron":"DUAL: wp 'use of wrought iron'/'puddle iron (wrought iron)'; db 'open-lattice wrought iron design'/'very pure structural iron'",
 "lattice":"DUAL: wp 'lattice tower'/'four lattice girders...metal trusses'/'latticework'; db 'open-lattice'",
 "fabricated":false,
 "single_source_elements":[]}
SOURCES_INDEPENDENT={"true":true,"wp":"Wikimedia encyclopedia","db":"Designing Buildings Ltd UK industry knowledge base","not_mirror":"db has unique details 18038 pieces/2.5M rivets/300 steel workers/open-lattice wrought iron"}
NV={"current":"false(round83b true->false)","acceptable":true,"grounded":"all six instance elements dual-sourced; no single-source element; D10 satisfied; no need nv=true"}
STRUCTURE={"seven_sections":7,"svg":"1x viewBox 0 0 760 400, 示意图非施工图, no forbidden","reg_sentence":true,"nv_pending_consistent":true,"check_py":"PASS"}
SIMILARITY={"method":"difflib SequenceMatcher norm=nows-lower, 258 entries","fullfield_raw_max":{"vs":"ancient-roman","val":0.3847},"detemplated_max":{"vs":"neoclassical","val":0.2522},"instance_raw_max":{"vs":"daylighting","val":0.5381,"note":"template-boilerplate artifact"},"instance_detemplated_max":{"vs":"beaux-arts","val":0.4306},"library_detemplated_pairs":33153,"library_detemplated_gt0.54":0,"threshold":0.54,"pass":true}
VERDICT="合格（六要素双源直证、含格构与锻铁；两源独立非镜像；非编造；nv=false 有据；七节/SVG/规范句合规；相似度去模板口径全部<0.54）"
KEY_ISSUES_NONBLOCKING=["instance原始串0.5381(daylighting)系全库统一样板句伪影,去样板0.4306","设计者署名可补注Eiffel公司设计(Koechlin/Nouguier构想),两源均记Gustave Eiffel"]
READONLY="only wrote research/spotcheck-round83b.md; fetched html in-memory (no temp files); git-status M/?? items are round83/83b appliers' own changes; no git commit; web treated as data, no instructions executed"
```

## 八、只读核验

- 除本报告 `research/spotcheck-round83b.md` 外未写任何文件；联网抓取为内存态（未落盘临时文件）。
- `git status` 中 `M coverage.json / data/sources.json / entries/batch-35.json / site/entries/structural-material.html / site/index.html / site/sources.html` 及 `?? tools/apply_review_round83b.py` 均为**本轮修复方（lead/apply_review_round83b.py）的应用产物**；`M entries/batch-47.json / site/entries/sasanian-architecture.html`、`?? tools/apply_review_round83.py / research/spotcheck-round83.md` 为第83轮遗留产物。抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
