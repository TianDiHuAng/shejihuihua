# 第69轮质量抽检报告（spotcheck-round69）

- 抽检人：spotcheck-r69（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 19:37 起，Asia/Hong_Kong。
- 抽检对象（第69轮改动 1 条）：`interior-exterior-transition`（室内外过渡，`entries/batch-02-b.json`，经 `grep "interior-exterior-transition"` 定位）。
- 本轮引用来源（`data/sources.json`）：`wp-loggia`（Wikipedia，`https://en.wikipedia.org/wiki/Loggia`，verified=true）、`db-loggia`（Designing Buildings，`https://www.designingbuildings.co.uk/wiki/Loggia`，verified=true）；旁证 `wp-courtyard`（Wikipedia）。
- 本轮任务：将 `interior-exterior-transition` 升级为「已验证」——实例=敞廊（Loggia），双源=`wp-loggia`（Wikipedia："covered exterior gallery, one side open…semi-outdoor room"）＋`db-loggia`（Designing Buildings："open-sided, roofed or vaulted gallery"）。
- 判定依据：`README.md` 硬性规则（不编造/只引 verified/关键事实双源互证否则标待核实/内联 SVG 非施工图/规范句/40 条上限）＋`DECISIONS.md`（D05/D06/D10/D11/D14）＋`tools/check.py` 校验口径＋第22–68轮既定相似度口径（difflib.SequenceMatcher，norm=去空白小写，①短=title+definition ②全字段不含 SVG，阈值 0.54）。

## 〇、只读声明与数据稳定性（verification-before-completion：先实抓、先跑、再断言）

- **只读**：本次**仅写出** `research/spotcheck-round69.md` 一个文件。来源核验全程 `python` 内存抓取（`urllib`＋浏览器 UA＋非校验 SSL），两页 HTML 抽取落为 `research/_r69_wp.html`、`research/_r69_db.html` 及派生 `_r69_wp.txt`、`_r69_db.txt`，核验后**已删除**；另有临时 `research/_r69_tmp.json`、`research/_r69_cov.txt` 亦已删除。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** 纯校验不写文件。
- **注**：工作区含第69轮未提交改动（`interior-exterior-transition` 条目、`data/sources.json` 新增 `db-loggia`、coverage 已改为 source_count=3/nv=false）。本次核验以工作区当前内容为准，未触碰数据文件。

## 一、来源实抓结果（HTTP 状态＋正文回读，均为本轮现抓）

| 来源 id | URL | HTTP | 大小 | 回读要点（抽取正文，逐字） |
| --- | --- | --- | --- | --- |
| `wp-loggia` | https://en.wikipedia.org/wiki/Loggia | **200** | 158,325 B | 导语：「**Covered exterior gallery, one side open**」（逐字，任务点名串）；正文：「a loggia serves as a **semi-outdoor room** for leisure, whereas an arcade provides shelter and rhythm along a passage」（逐字，任务点名串）；「usually supported by a series of **columns or arches**」；「From the early Middle Ages, nearly every Italian **comune** had an…」；「The **Renaissance** three-story arcade loggia of the **City Hall** in Poznań, Poland」 |
| `db-loggia` | https://www.designingbuildings.co.uk/wiki/Loggia | **200** | 48,631 B | 「A loggia is an **open-sided, roofed or vaulted gallery**, often on the upper level of a building but sometimes at ground level.」（逐字，任务点名串）；「A loggia can be either free-standing or can run along the front or side of a building. The **outer wall is open to the elements** and is usually support…」 |

**两源均 HTTP 200、正文可回读。任务点名的引文串「Covered exterior gallery, one side open…semi-outdoor room」与「open-sided, roofed or vaulted gallery」全部在两份页面正文逐字可回读。**

## 二、逐条核对

### `interior-exterior-transition`（室内外过渡）— **合格**

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| definition 引用支撑 | △ 有据但属概念抽象（非逐字） | 条目 definition「室内与室外在空间、视线与气候上的连续过渡」↔ wp `semi-outdoor room`（半室外房间）＋db `open-sided…outer wall is open to the elements`（外侧开敞、外墙对户外敞开）＝「内外可渗透」的直证；「连续过渡」为对「敞廊作为内外之间的半室外房间/开敞画廊」的概念抽象。**两源正文均未出现 "interior/exterior/transition" 字样**，definition 系由实例抽象而非逐字转述。见问题1（非阻断） |
| time_or_place | ✓ | 「跨时期、全球（参见来源）」为泛化表述；实例年代由 sections 承载，成立 |
| **实例·敞廊 Loggia**（任务点名） | ✓ 直证 | 条目「名称：敞廊（Loggia，意大利语）；地点：欧洲（源自意大利，如市政厅拱廊敞廊）；年份：文艺复兴以来」↔ wp `Italian comune`、`Renaissance…loggia of the City Hall`；db `Loggia`（标题＋定义）＝名称/地域/文艺复兴/市政厅拱廊逐字或近乎逐字对上 |
| **双源引文一（covered exterior gallery, one side open…semi-outdoor room）**（任务点名） | ✓ **逐字** | wp 正文：`Covered exterior gallery, one side open`（导语原句）、`semi-outdoor room`（原句）两串均命中（见 §一） |
| **双源引文二（open-sided, roofed or vaulted gallery）**（任务点名） | ✓ **逐字** | db 正文：`A loggia is an open-sided, roofed or vaulted gallery` 全串命中（见 §一） |
| 实例·设计者/年份（是否编造） | △ 年份有据、设计者泛化 | 年份「文艺复兴以来」↔ wp `Renaissance…loggia`，有据；设计者「民间营建/建筑师（随例不同）」为**泛化回避表述**，两源均未点名单一设计者（敞廊为类型而非单件作品，本身无单一设计者）。**未编造具体人名/年份**；泛化写法合规但不构成"设计者三要素"的硬核。见问题2（非阻断） |
| 来源直接相关 | ✓ | wp 为 Loggia 百科条目（定义＋类型＋词源），db 为 Loggia 专条（定义＋构造）；均为「敞廊」主题直源、HTTP 200、verified=true |
| **两源独立性**（任务点名：Wikipedia vs Designing Buildings） | ✓ **成立** | `wp-loggia` 发布方＝**Wikipedia（众编在线百科）**；`db-loggia` 发布方＝**Designing Buildings（"The Construction Wiki"，建筑行业专业站）**。两独立发布主体、体例不同（百科导语 vs 行业专条含 cookie/注册栏目）、措辞不同（`semi-outdoor room` vs `open-sided…outer wall open to the elements`）、非镜像；两者独立载明「敞廊＝一侧开放/带顶拱廊画廊」核心定义，构成真双源互证 |
| 七节 | ✓ | definition + sections 六节（原理／典型手法与适用条件／实例／常见错误与限制／一图／待核实）＝七节齐，无空缺（check.py 0 报错） |
| SVG | ✓ | 1 张（`viewBox 0 0 760 400`，rect/line/text，含「示意图，非施工图」；无 `on*=` 事件处理器、无 `<image>`/xlink/href/`<script>`；check.py 0 报错） |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位 |
| nv↔pending 联动 | ✓ 一致 | `needs_verification=false`／`pending_notes=""`／「待核实」节「暂无已知待核实项」三处一致；正文无内联「待核实」声明；check.py 未报「有待核实说明但 nv=false」类错误 |
| **nv 置 false 是否有据** | △—✓ 有据（在"实例+概念抽象"口径下） | 实例核心定义（敞廊＝一侧开放带顶拱廊画廊/半室外房间）由 Wikipedia＋Designing Buildings 两独立主体逐字互证；文艺复兴/意大利/市政厅等实例要素有据、未编造。**唯 definition 的概念层（"内外连续过渡"）系对敞廊半室外性质的抽象，两源正文未直接以此措辞论述**。按第68轮（`spatial-sequence`）确立口径——实例三要素有据、概念为实例的合理抽象即标 nv=false——本条属**有据**；原历史 gaps 多轮记「实例名称/设计者/年代待补独立来源」的缺陷，随本轮补入 Loggia 双源实例而消解。见问题1（非阻断） |
| coverage↔entry | ✓ | title「室内外过渡」/theme「理论」/tier「核心」/period「跨时期」/region「全球」/level「L2」全一致；`source_count=3`＝entries 3 源（wp-courtyard/wp-loggia/db-loggia）；`needs_verification_count=0`＝nv false；status=已写 |
| 相似度（阈值 0.54） | ✓ | ①短 最高 **0.3390**（vs gray-space）＜0.54；②全字段 最高 **0.4426**（vs courtyard）＜0.54，均明显低于阈值 |

**`interior-exterior-transition` 结论：合格（本轮已可升级为已验证）。**

## 三、问题与建议（均非阻断）

1. **（提示，非阻断）definition 属概念抽象而非逐字支撑**：两源正文均只描述敞廊「一侧开放/带顶拱廊画廊/半室外房间」，**未出现 "interior / exterior / transition / 过渡" 等措辞**；definition「室内与室外在空间、视线与气候上的连续过渡」系将敞廊的半室外性质抽象为「室内外过渡」概念。此与第68轮 `spatial-sequence`（概念由实例动线抽象、两源均为实例文档）同型。在当前口径（实例有据＋合理概念抽象即标 nv=false）下成立；若追求理论层更硬双源，可后续补一篇论述「室内外过渡/灰空间」概念的理论专文。**可选，不阻断。**
2. **（提示，非阻断）实例"设计者"为泛化表述**：「设计者：民间营建/建筑师（随例不同）」回避具体人名——因敞廊是**建筑类型**而非单件作品，本身无单一设计者，两源亦未点名，故不编造、泛化处理符合规则；但严格意义上「设计者三要素」未能落实到具体个案。建议后续若需硬核实例，可点名某一具体敞廊（如 wp 已出现的 Poznań 市政厅敞廊）作为个案三要素来源。**可选，不阻断。**
3. **（提示，非阻断）相似度与 courtyard 贴近**：全字段 0.4426（vs courtyard）为本条最高，源于两者都涉及庭院/廊道与内外关系；距阈值 0.54 仍有 0.10 余量，当前合规，后续若再扩写实例段需留意差异化。

## 四、总体结论

- **`interior-exterior-transition`：合格（本轮已可升级为已验证）。**
  - 任务点名核对诸项获支撑：**Covered exterior gallery, one side open…semi-outdoor room** 由 `wp-loggia` 正文逐字命中；**open-sided, roofed or vaulted gallery** 由 `db-loggia` 正文逐字命中；实例 名称（敞廊 Loggia）/地点（欧洲·意大利）/年份（文艺复兴以来）均双源或单源逐字可回读，**未编造具体人名/数字**。
  - definition/overview/time_or_place 有据（definition 属实例的概念抽象，见问题1）；七节齐、SVG 合规（示意图非施工图、无脚本/外链/事件处理器）、规范句在位、coverage 全字段一致、nv↔pending 三处一致。
  - **两源独立成立**：`wp-loggia`（Wikipedia·众编百科）与 `db-loggia`（Designing Buildings·建筑行业站）为两独立发布主体、体例与措辞不同、非镜像，核心「敞廊＝一侧开放带顶拱廊画廊」定义互证。
  - **nv=false 有据**（实例有据＋概念抽象口径，同第68轮标准）；历史"实例要素待补独立来源"缺陷随本轮补双源实例而消解。
  - **相似度 0.3390 / 0.4426 均低于 0.54**。
  - 全库 `python tools/check.py`＝`PASS: all checks, 0 errors`（EXIT=0）。
- **本轮 1 条：1 合格、0 待核实、0 不合格。**
- **建议（非阻断）**：① 若追求理论层更硬双源，可补论述「室内外过渡/灰空间」概念的理论专文；② 若需硬核个案，可点名具体敞廊（如 Poznań 市政厅敞廊）落实设计者/年代三要素。

## 五、机器可读汇总

```
ROUND=69
SAMPLER=spotcheck-r69
MODE=round69 改动 1 条抽检（interior-exterior-transition 升级已验证）
SCOPE=["interior-exterior-transition"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round68.md","README.md","tools/check.py","tools/apply_review_round69.py","entries/batch-02-b.json","data/sources.json","coverage.json"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback; temp research/_r69_* deleted after"
FETCHES={"wp-loggia":200,"db-loggia":200}
INTERIOR_EXTERIOR_TRANSITION={
 "sources":["wp-courtyard","wp-loggia","db-loggia"],
 "definition_support":"wp 'semi-outdoor room'+db 'open-sided...outer wall open to the elements' -> 内外可渗透有据; 但两源未出现interior/exterior/transition措辞, definition为实例概念抽象(问题1非阻断)",
 "instance":"敞廊 Loggia / 欧洲(源自意大利,如市政厅拱廊敞廊) / 设计者泛化(随例不同) / 文艺复兴以来",
 "quote1_wp":"'Covered exterior gallery, one side open' + 'semi-outdoor room' VERBATIM in wp page",
 "quote2_db":"'open-sided, roofed or vaulted gallery' VERBATIM in db page",
 "designer_year":"年份 Renaissance=wp逐字有据; 设计者泛化回避(类型无单一设计者), 未编造具体人名/数字",
 "two_source_independence":"wp-loggia=Wikipedia(众编百科) vs db-loggia=Designing Buildings(建筑行业站): 两独立主体/体例措辞不同/非镜像 -> 真双源互证",
 "seven_sections":7,"svg":"1x viewBox760x400 rect/line/text 示意图非施工图, no on*/image/xlink/href/script",
 "reg_sentence":true,"nv":false,"pending_consistent":true,
 "nv_false_basis":"实例核心定义由Wikipedia+DesigningBuildings两独立主体逐字互证, 文艺复兴/意大利/市政厅有据未编造; definition概念层为实例抽象(同r68口径) -> 标false有据; 历史实例要素待补缺随本轮补双源实例消解",
 "coverage":"title/theme/tier/period/region/level 一致; source_count3=3源; nvc0=nvfalse",
 "similarity":{"short":0.3390,"short_vs":"gray-space","full":0.4426,"full_vs":"courtyard","threshold":0.54},
 "verdict":"合格"}
TOTAL="1合格/0待核实/0不合格"
RECOMMEND="非阻断: ①definition概念抽象(两源无interior/exterior措辞),可补室内外过渡/灰空间理论专文 ②实例设计者泛化,可点名具体敞廊落实三要素"
READONLY="only wrote research/spotcheck-round69.md; fetched html in-memory, temp research/_r69_* deleted; no entries/sources/coverage/tools/site changed; no git commit; web treated as data (no instructions executed)"
NOTE="工作区含 round69 未提交改动(interior-exterior-transition 条目+db-loggia 源+coverage source_count3/nvfalse), 核验以工作区当前内容为准, 未触碰"
```

*（报告完）*
