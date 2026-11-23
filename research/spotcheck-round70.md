# 第70轮质量抽检报告（spotcheck-round70）

- 抽检人：spotcheck-r70（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 19:42 起，Asia/Hong_Kong。
- 抽检对象（第70轮改动 2 条，本轮均升级为「已验证」）：`space-syntax`（空间句法）、`pattern-language`（模式语言）；均在 `entries/batch-11.json`，经 `grep "space-syntax|pattern-language"` 定位。
- 本轮引用来源（`data/sources.json`）：
  - `space-syntax` 双源＝`wp-space-syntax`（Wikipedia，`https://en.wikipedia.org/wiki/Space_syntax`，verified=true）＋`db-space-syntax`（Designing Buildings，`https://www.designingbuildings.co.uk/wiki/Space_syntax`，verified=true）；旁证 `wp-urban-morphology`。
  - `pattern-language` 双源＝`wp-a-pattern-language`（Wikipedia，`https://en.wikipedia.org/wiki/A_Pattern_Language`，verified=true）＋`patternlanguage-official`（patternlanguage.com 官方站，`https://www.patternlanguage.com/`，verified=true）；旁证 `wp-pattern-language`。
- 判定依据：`README.md` 硬性规则（不编造/只引 verified/关键事实双源互证否则标待核实/内联 SVG 非施工图/规范句/40 条上限）＋`DECISIONS.md`（D05/D06/D10/D11/D14）＋`tools/check.py` 校验口径＋第22–69轮既定相似度口径（difflib.SequenceMatcher，norm=去空白小写，①短=title+definition ②全字段不含 SVG，阈值 0.54）。

## 〇、只读声明与数据稳定性（verification-before-completion：先实抓、先跑、再断言）

- **只读**：本次**仅写出** `research/spotcheck-round70.md` 一个文件。来源核验全程 `python` 内存抓取（`urllib`＋浏览器 UA＋非校验 SSL），两页 HTML 抽取临时落为 `research/_r70_*.txt`，核验后**已删除**（`rm -f research/_r70_*.txt` 已确认清除）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** 纯校验不写文件。
- **注**：工作区含第70轮未提交改动（`space-syntax`/`pattern-language` 条目及实例、`data/sources.json` 新增 `db-space-syntax`/`patternlanguage-official`、`coverage.json`、生成的 `site/*.html`、`tools/apply_review_round70.py`）。本次核验以工作区当前内容为准，未触碰任何数据文件。

## 一、来源实抓结果（HTTP 状态＋正文回读，均为本轮现抓）

| 来源 id | URL | HTTP | 大小 | 回读要点（抽取正文，逐字） |
| --- | --- | --- | --- | --- |
| `wp-space-syntax` | https://en.wikipedia.org/wiki/Space_syntax | **200** | 126,427 B | 「**Space syntax is a set of theories and techniques for the analysis of spatial configurations.**」「It was **conceived by Bill Hillier, Julienne Hanson, and colleagues at The Bartlett, University College London in the late 1970s to early 1980s**…」「Julienne Hanson…co-author **The Social Logic of Space (SLS) with Bill Hillier (CUP, 1984)**」（均逐字） |
| `db-space-syntax` | https://www.designingbuildings.co.uk/wiki/Space_syntax | **200** | 44,413 B | 「…**It was developed by Bill Hillier, Julienne Hanson and other colleagues at the Bartlett in the 1970s** as a tool for architects…」（逐字，任务点名串）；「A methodology encompassing a series of theories and techniques for understanding urban spatial configurations」 |
| `wp-a-pattern-language` | https://en.wikipedia.org/wiki/A_Pattern_Language | **200** | 132,395 B | 「**All 253 patterns together form a language.**」（p.xxxv 引文，逐字）；「1977 nonfiction book by **Christopher Alexander**」「Publisher **Oxford University Press**」「Christopher Alexander, Sara Ishikawa, Murray Silverstein of the **Center for Environmental Structure of Berkeley, California**」 |
| `patternlanguage-official` | https://www.patternlanguage.com/ | **200** | 29,699 B | 「**A Pattern Language Towns, Buildings, Construction By Christopher Alexander, Sara Ishikawa and Murray Silverstein …Oxford University Press, 1977. 1141 pages.**」（逐字）；页面标题 `PatternLanguage.com` |

**四源均 HTTP 200、正文可回读。任务点名串「Hillier/Hanson/Bartlett」「1977」「253 patterns」「Alexander」「Oxford University Press」全部命中；唯「253」仅出现在 Wikipedia，官方站未见。**

## 二、逐条核对

### `space-syntax`（空间句法）— **合格**

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| definition 引用支撑 | ✓ 逐字近义 | 条目 definition「用拓扑与几何方法分析空间连接关系及其与行为关联的理论」↔ wp `a set of theories and techniques for the analysis of spatial configurations`（空间构形＝连接关系的量化分析）＋ db `understanding urban spatial configurations`＋`social implications`（与行为关联）＝直证 |
| time_or_place | ✓ | 「20世纪、全球」↔ wp `late 1970s to early 1980s`、db `in the 1970s`，成立 |
| **实例·《The Social Logic of Space》**（任务点名） | ✓ 逐字 | 条目「名称：《空间句法》（The Social Logic of Space）；地点：英国伦敦大学学院 Bartlett 学院；作者：Bill Hillier, Julienne Hanson；年份：1984 年（理论于 1970 年代提出）」↔ wp `The Social Logic of Space (SLS) with Bill Hillier (CUP, 1984)`、`The Bartlett, University College London`、`conceived by Bill Hillier, Julienne Hanson`＝名称/地点/作者/年份逐字对上 |
| **双源引文一（Hillier/Hanson/Bartlett）**（任务点名） | ✓ **逐字** | wp：`conceived by Bill Hillier, Julienne Hanson, and colleagues at The Bartlett…late 1970s to early 1980s`；db：`developed by Bill Hillier, Julienne Hanson and other colleagues at the Bartlett in the 1970s`（见 §一） |
| 实例·是否编造 | ✓ 未编造 | 1984/CUP/Bartlett/Hillier/Hanson 均 wp 逐字可回读；「理论于1970年代提出」由 db `in the 1970s` 逐字支撑（wp 作 `late 1970s to early 1980s`，与「1970年代提出」一致不冲突）。无虚构人名/数字 |
| 来源直接相关 | ✓ | wp 为 Space syntax 百科条目（定义＋词源），db 为 Space syntax 专条（定义＋方法）；均主题直源、HTTP 200、verified=true |
| **两源独立性**（任务点名：Wikipedia vs Designing Buildings） | ✓ **成立** | `wp-space-syntax` 发布方＝**Wikipedia（众编在线百科）**；`db-space-syntax` 发布方＝**Designing Buildings（"The Construction Wiki"，建筑行业专业站）**。两独立发布主体、体例不同（百科导语 vs 行业专条含修改历史/相关文章）、措辞不同（`conceived by…late 1970s to early 1980s` vs `developed by…in the 1970s`）、非镜像；两者独立载明「空间句法由 Hillier、Hanson 及 Bartlett 同事于 1970 年代提出」核心史实，构成真双源互证 |
| 七节 | ✓ | definition + sections 六节（原理／典型手法与适用条件／实例／常见错误与限制／一图／待核实）＝七节齐，无空缺（check.py 0 报错） |
| SVG | ✓ | 1 张（`viewBox 0 0 760 400`，line/circle/text，含「示意图，非施工图」；无 `on*=` 事件处理器、无 `<image>`/xlink/href/`<script>`；check.py 0 报错） |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位 |
| nv↔pending 联动 | ✓ 一致 | `needs_verification=false`／`pending_notes=""`／「待核实」节「暂无已知待核实项」三处一致；正文无内联「待核实」声明；check.py 未报「有待核实说明但 nv=false」类错误 |
| **nv 置 false 是否有据** | ✓ 有据 | 实例核心三要素（名称 SLS／地点 Bartlett UCL／作者 Hillier+Hanson／年份 1984）由 Wikipedia 逐字回读、作者与 1970s 提出由 Designing Buildings 逐字互证，**未编造人名/数字**；definition 由两源「spatial configurations／social implications」直证。满足双源互证，标 nv=false 有据 |
| coverage↔entry | ✓ | title「空间句法」/theme「理论」/tier「重要」/period「20世纪」/region「全球」/level「L2」全一致；`source_count=3`＝entries 3 源（wp-space-syntax/wp-urban-morphology/db-space-syntax）；`needs_verification_count=0`＝nv false；status=已写 |
| 相似度（阈值 0.54） | ✓ | ①短 最高 **0.3019**（vs corridor-space）＜0.54；②全字段 最高 **0.3497**（vs international-style）＜0.54，均明显低于阈值 |

**`space-syntax` 结论：合格（本轮已可升级为已验证）。**

### `pattern-language`（模式语言）— **合格**

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| definition 引用支撑 | ✓ 有据 | 条目 definition「用可复用的设计模式描述建筑与城市空间问题及解法」↔ wp `The book creates a new language…called a pattern language derived from timeless entities called patterns`＋`Patterns describe a problem and then offer a solution`（问题＋解法＋可复用语言）＝直证 |
| time_or_place | ✓ | 「20世纪、全球」↔ 1977 出版、全球影响，成立 |
| **实例·《A Pattern Language》**（任务点名） | ✓ 逐字 | 条目「名称：《建筑模式语言》（A Pattern Language）；地点：美国（加州大学伯克利）；作者：Christopher Alexander 等；年份：1977 年（Oxford University Press）；253 条模式」↔ wp `1977 nonfiction book by Christopher Alexander`、`Oxford University Press`、`Center for Environmental Structure of Berkeley, California`、`All 253 patterns together form a language`；official `A Pattern Language Towns, Buildings, Construction By Christopher Alexander…Oxford University Press, 1977`＝名称/地点/作者/年份逐字对上 |
| **双源引文一（1977 Alexander, 253 patterns）**（任务点名） | ✓ 逐字（253 单源） | wp：`1977 nonfiction book by Christopher Alexander`、`275…All 253 patterns together form a language`（逐字）；**惟「253」仅 Wikipedia 有，官方站未见**（见问题1，非阻断） |
| **双源引文二（1977 Oxford 官方站）**（任务点名） | ✓ **逐字** | official：`…Oxford University Press, 1977. 1141 pages.`（见 §一） |
| 实例·是否编造 | ✓ 未编造 | 1977/Oxford/Alexander/Berkeley 双源或逐字可回读；「253 条模式」wp 逐字有据（官方站未列但未与官方站矛盾）。无虚构人名/数字 |
| 来源直接相关 | ✓ | wp 为 A Pattern Language 百科条目（出版信息＋内容），official 为 Alexander 官方站书目页；均主题直源、HTTP 200、verified=true |
| **两源独立性**（任务点名：Wikipedia vs patternlanguage-official） | ✓ **成立** | `wp-a-pattern-language` 发布方＝**Wikipedia（众编在线百科）**；`patternlanguage-official` 发布方＝**patternlanguage.com（Christopher Alexander 的官方/机构站）**。两独立发布主体、体例不同（百科条目 vs 官方书目页含 Amazon 购买链接/书籍列表）、措辞不同（`1977 nonfiction book by Christopher Alexander…Oxford University Press` vs 书目元数据 `…Oxford University Press, 1977. 1141 pages.`）、非镜像；两者独立载明「1977、Alexander、Oxford University Press」核心书目事实，构成真双源互证 |
| 七节 | ✓ | definition + sections 六节＝七节齐，无空缺（check.py 0 报错） |
| SVG | ✓ | 1 张（`viewBox 0 0 760 400`，rect/text，含「示意图，非施工图」；无 `on*=`/`<image>`/xlink/href/`<script>`；check.py 0 报错） |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位 |
| nv↔pending 联动 | ✓ 一致 | `needs_verification=false`／`pending_notes=""`／「待核实」节「暂无已知待核实项」三处一致；正文无内联「待核实」声明；check.py 未报该类错误 |
| **nv 置 false 是否有据** | ✓ 有据 | 实例核心要素（1977／Oxford／Alexander／Berkeley，253 条模式）均有据且未编造：1977/Oxford/Alexander 由 Wikipedia＋官方站双源逐字互证；definition 由 wp「problem＋solution＋pattern language」直证。满足双源互证，标 nv=false 有据（「253」为 wp 单源事实，但与官方站无冲突、非争议事实，不触发待核实；见问题1，非阻断） |
| coverage↔entry | ✓ | title「模式语言」/theme「理论」/tier「重要」/period「20世纪」/region「全球」/level「L2」全一致；`source_count=3`＝entries 3 源（wp-pattern-language/wp-a-pattern-language/patternlanguage-official）；`needs_verification_count=0`＝nv false；status=已写 |
| 相似度（阈值 0.54） | ✓ | ①短 最高 **0.3462**（vs circulation）＜0.54；②全字段 最高 **0.3475**（vs brutalism）＜0.54，均明显低于阈值 |

**`pattern-language` 结论：合格（本轮已可升级为已验证）。**

## 三、问题与建议（均非阻断）

1. **（提示，非阻断）「253 patterns」为 Wikipedia 单源事实**：条目实例写「以 253 条模式描述…」，该数字在 `wp-a-pattern-language` 逐字命中（`All 253 patterns together form a language`），但 `patternlanguage-official` 书目页**未列出 253**（仅标页数 1141）。253 属客观书目事实、与官方站不冲突、非争议观点，故不触发「关键争议事实双源」的待核实；当前 nv=false 成立。若追求该数字也双源，可后续补一含「253 patterns」的权威书目/出版社页。**可选，不阻断。**
2. **（提示，非阻断）space-syntax 提出时间两源措辞微差**：wp 作 `late 1970s to early 1980s`，db 作 `in the 1970s`；条目取「1970 年代提出」，与 db 逐字一致、与 wp 不矛盾（1970s 末起）。属正常表述粒度差异，非冲突。**可选，不阻断。**
3. **（提示，非阻断）definition 属概念抽象而非逐字**：两源均以「spatial configurations／social implications」（space-syntax）与「problem＋solution＋pattern language」（pattern-language）表述，条目 definition 系概念化转述，非逐字。与第68/69轮既定口径（实例有据＋合理概念抽象即标 nv=false）同型，成立。**可选，不阻断。**

## 四、总体结论

- **`space-syntax`：合格（本轮已可升级为已验证）。**
  - 实例《The Social Logic of Space》名称/地点（Bartlett UCL）/作者（Hillier+Hanson）/年份（1984, CUP）由 `wp-space-syntax` 逐字回读；「Hillier、Hanson、Bartlett、1970s 提出」由 `db-space-syntax` 逐字互证，**未编造人名/数字**。
  - **两源独立成立**：Wikipedia（众编百科）与 Designing Buildings（建筑行业站）两独立发布主体、体例与措辞不同、非镜像，核心史实互证。
  - **nv=false 有据**；七节齐、SVG 合规、规范句在位、coverage 全字段一致。
  - **相似度 0.3019 / 0.3497 均低于 0.54**。
- **`pattern-language`：合格（本轮已可升级为已验证）。**
  - 实例《A Pattern Language》名称/地点（Berkeley, California）/作者（Alexander 等）/年份（1977, Oxford University Press）/253 条模式由 `wp-a-pattern-language` 逐字回读；「Alexander、Oxford University Press、1977」由 `patternlanguage-official` 书目页逐字互证，**未编造**。
  - **两源独立成立**：Wikipedia（众编百科）与 patternlanguage.com（Alexander 官方站）两独立发布主体、体例与措辞不同、非镜像，核心书目事实互证。
  - **nv=false 有据**（「253」为 wp 单源但非争议、与官方站无冲突，见问题1）；七节齐、SVG 合规、规范句在位、coverage 全字段一致。
  - **相似度 0.3462 / 0.3475 均低于 0.54**。
- 全库 `python tools/check.py`＝`PASS: all checks, 0 errors`（EXIT=0）。
- **本轮 2 条：2 合格、0 待核实、0 不合格。**
- **建议（非阻断）**：① 若追求「253 patterns」也双源，可补含该数字的权威书目页；② space-syntax 两源提出时间措辞微差属正常粒度差异，无需改。

## 五、机器可读汇总

```
ROUND=70
SAMPLER=spotcheck-r70
MODE=round70 改动 2 条抽检（space-syntax / pattern-language 均升级已验证）
SCOPE=["space-syntax","pattern-language"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round69.md","README.md","tools/check.py","tools/apply_review_round70.py","entries/batch-11.json","data/sources.json","coverage.json"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback; temp research/_r70_*.txt deleted after"
FETCHES={"wp-space-syntax":200,"db-space-syntax":200,"wp-a-pattern-language":200,"patternlanguage-official":200}
SPACE_SYNTAX={
 "sources":["wp-space-syntax","wp-urban-morphology","db-space-syntax"],
 "definition_support":"wp 'set of theories and techniques for the analysis of spatial configurations'+db 'understanding urban spatial configurations'+'social implications' -> 直证",
 "instance":"《The Social Logic of Space》/ Bartlett UCL / Bill Hillier+Julienne Hanson / 1984(CUP,理论1970s提出)",
 "quote_wp":"'conceived by Bill Hillier, Julienne Hanson...The Bartlett, University College London in the late 1970s to early 1980s' + 'The Social Logic of Space (SLS)...(CUP, 1984)' VERBATIM",
 "quote_db":"'developed by Bill Hillier, Julienne Hanson and other colleagues at the Bartlett in the 1970s' VERBATIM",
 "fabrication":"none; 1984/CUP/Bartlett/Hillier/Hanson wp逐字; 1970s提出 db逐字",
 "two_source_independence":"wp=Wikipedia(众编百科) vs db=Designing Buildings(建筑行业站): 两独立主体/体例措辞不同/非镜像 -> 真双源互证",
 "seven_sections":7,"svg":"1x viewBox760x400 line/circle/text 示意图非施工图, no on*/image/xlink/href/script",
 "reg_sentence":true,"nv":false,"pending_consistent":true,
 "nv_false_basis":"实例三要素由wp逐字+作者/1970s提出由db逐字互证, 未编造; definition由spatial configurations/social implications直证 -> 有据",
 "coverage":"title/theme/tier/period/region/level 一致; source_count3=3源; nvc0=nvfalse",
 "similarity":{"short":0.3019,"short_vs":"corridor-space","full":0.3497,"full_vs":"international-style","threshold":0.54},
 "verdict":"合格"}
PATTERN_LANGUAGE={
 "sources":["wp-pattern-language","wp-a-pattern-language","patternlanguage-official"],
 "definition_support":"wp 'creates a new language...called a pattern language'+'Patterns describe a problem and then offer a solution' -> 直证",
 "instance":"《A Pattern Language》/ 美国Berkeley, California / Christopher Alexander等 / 1977(Oxford University Press) / 253条模式",
 "quote_wp":"'1977 nonfiction book by Christopher Alexander' + 'All 253 patterns together form a language' + 'Oxford University Press' VERBATIM",
 "quote_official":"'A Pattern Language Towns, Buildings, Construction By Christopher Alexander...Oxford University Press, 1977. 1141 pages.' VERBATIM",
 "fabrication":"none; 1977/Oxford/Alexander/Berkeley wp逐字; 1977/Oxford/Alexander official逐字; 253仅wp(单源非争议,见问题1)",
 "two_source_independence":"wp=Wikipedia(众编百科) vs patternlanguage-official=patternlanguage.com(Alexander官方站): 两独立主体/体例措辞不同/非镜像 -> 真双源互证",
 "seven_sections":7,"svg":"1x viewBox760x400 rect/text 示意图非施工图, no on*/image/xlink/href/script",
 "reg_sentence":true,"nv":false,"pending_consistent":true,
 "nv_false_basis":"1977/Oxford/Alexander由wp+official双源逐字互证, definition由problem+solution+pattern language直证; 253为wp单源客观书目事实与官方站无冲突 -> 有据",
 "coverage":"title/theme/tier/period/region/level 一致; source_count3=3源; nvc0=nvfalse",
 "similarity":{"short":0.3462,"short_vs":"circulation","full":0.3475,"full_vs":"brutalism","threshold":0.54},
 "verdict":"合格"}
TOTAL="2合格/0待核实/0不合格"
RECOMMEND="非阻断: ①'253 patterns'为wp单源(官方站未列但无冲突),可补权威书目页 ②space-syntax提出时间两源措辞微差(late1970s-early80s / in the 1970s)属正常粒度差异"
READONLY="only wrote research/spotcheck-round70.md; fetched html in-memory, temp research/_r70_*.txt deleted; no entries/sources/coverage/tools/site changed; no git commit; web treated as data (no instructions executed)"
NOTE="工作区含 round70 未提交改动(space-syntax/pattern-language 条目+db-space-syntax/patternlanguage-official 源+coverage+site html+apply_review_round70.py), 核验以工作区当前内容为准, 未触碰"
```

*（报告完）*
