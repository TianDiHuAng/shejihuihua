# 第71轮质量抽检报告（spotcheck-round71）

- 抽检人：spotcheck-r71（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 起，Asia/Hong_Kong。
- 抽检对象（第71轮改动，本轮升级为「已验证」）：`biophilic-design`（亲生命性设计），在 `entries/batch-11.json` 经 `grep "biophilic-design"` 定位。
- 本轮引用来源（`data/sources.json`）：
  - `wp-biophilic-design`（Wikipedia，`https://en.wikipedia.org/wiki/Biophilic_design`，verified=true）
  - `wp-evidence-based-design`（旁证）
  - `db-biophilic-design`（Designing Buildings，`https://www.designingbuildings.co.uk/wiki/Biophilic_design`，verified=true，本轮新增）
- 判定依据：`README.md` 硬性规则（不编造/只引 verified/关键事实双源互证否则标待核实/内联 SVG 非施工图/规范句/40 条上限）＋`DECISIONS.md`（D05/D06/D10/D11/D14）＋`tools/check.py` 校验口径＋第22–70轮既定相似度口径（difflib.SequenceMatcher，norm=去空白小写，①短=title+definition ②全字段不含 SVG，阈值 0.54）。

## 〇、只读声明与数据稳定性（verification-before-completion：先实抓、先跑、再断言）

- **只读**：本次**仅写出** `research/spotcheck-round71.md` 一个文件。来源核验全程 `python` 内存抓取（`urllib`＋浏览器 UA＋非校验 SSL），两页正文抽取临时落为 `research/_r71_*.txt` 及临时脚本 `research/_r71_fetch.py`、`research/_r71_sim.py`，核验后**已删除**（`rm -f` 已确认清除）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** 纯校验不写文件。
- 工作区含第71轮未提交改动（`biophilic-design` 条目实例改写、`data/sources.json` 新增 `db-biophilic-design`、`coverage.json`、生成的 `site/*.html`、`tools/apply_review_round71.py`）。本次核验以工作区当前内容为准，未触碰任何数据文件。

## 一、来源实抓结果（HTTP 状态＋正文回读，均为本轮现抓）

| 来源 id | URL | HTTP | 大小 | 回读要点（抽取正文，逐字） |
| --- | --- | --- | --- | --- |
| `wp-biophilic-design` | https://en.wikipedia.org/wiki/Biophilic_design | **200** | 346,507 B | 「**Biophilic design seeks to increase people's connectivity to nature and nature-like design to improve their health and well-being.**」「Although the term was coined in the 20th century…」「**Edward O. Wilson's book Biophilia (1984)** …he took a biologist's approach and first coined the "biophilia hypothesis" and **popularized the notion**.」「Wilson defined biophilia as "the innate tendency to focus on life and lifelike processes"」（均逐字） |
| `db-biophilic-design` | https://www.designingbuildings.co.uk/wiki/Biophilic_design | **200** | 59,541 B | 「**Biophilic design makes use of natural materials and planting to increase wellbeing.**」「Biophilic designs therefore are those that **connect people to nature and natural processes**…」「**Edward Wilson, an American biologist, popularised the term in the 1980s.** …In his book **Biophilia**, he argued that humans have an innate and evolutionarily based affinity for nature」（均逐字，任务点名串） |

**两源均 HTTP 200、正文可回读。任务点名串「Edward Wilson / popularised / in the 1980s」在 `db-biophilic-design` 逐字命中；「Wilson / Biophilia / 1984 / popularized」在 `wp-biophilic-design` 逐字命中。**

## 二、逐条核对（`biophilic-design`）— **合格**

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| definition 引用支撑 | ✓ 逐字 | 条目 definition「把**自然要素与过程**纳入建成环境以支持**健康与福祉**的设计」↔ db `connect people to nature and **natural processes**`（自然要素与过程，逐字）＋ db `increase wellbeing` ＋ wp `improve their health and well-being`（健康与福祉，逐字）＝直证 |
| time_or_place | ✓ | 「当代、全球」↔ wp `the term was coined in the 20th century`、db `popularised the term in the 1980s`、全球范围讨论，成立 |
| **实例·亲生命设计理论（Biophilia, Wilson）**（任务点名） | ✓ 逐字 | 条目「名称：亲生命设计理论（Biophilic Design，源自 E. O. 威尔逊《Biophilia》）；地点：美国（概念起源）；作者：爱德华·O·威尔逊（Edward O. Wilson）；年份：1984 年《Biophilia》提出、1980 年代起普及」↔ wp `Edward O. Wilson's book Biophilia (1984)`、db `Edward Wilson, an American biologist…In his book Biophilia…popularised the term in the 1980s`＝名称/作者/年份逐字对上 |
| **双源引文一（Wilson, Biophilia, 1984/popularized）**（任务点名） | ✓ **逐字** | wp：`Edward O. Wilson's book Biophilia (1984) … first coined the "biophilia hypothesis" and popularized the notion`（见 §一） |
| **双源引文二（Edward Wilson popularised term in the 1980s）**（任务点名） | ✓ **逐字** | db：`Edward Wilson, an American biologist, popularised the term in the 1980s.`（见 §一，即任务指定原句） |
| 实例·是否编造 | ✓ 未编造 | 威尔逊／《Biophilia》／1984／1980 年代普及／美国生物学家，两源逐字可回读；「地点：美国（概念起源）」由 db `an American biologist`＋wp 起源叙述支撑。无虚构人名/数字 |
| 来源直接相关 | ✓ | wp 为 Biophilic design 百科条目（定义＋Wilson 源流），db 为 Biophilic design 专条（定义＋Wilson 1980s 普及）；均主题直源、HTTP 200、verified=true |
| **两源独立性**（任务点名：Wikipedia vs Designing Buildings） | ✓ **成立** | `wp-biophilic-design` 发布方＝**Wikipedia（众编在线百科）**；`db-biophilic-design` 发布方＝**Designing Buildings（"The Construction Wiki"，建筑行业专业站）**。两独立发布主体、体例不同（百科导语＋多节框架 vs 行业专条含 BRE 案例/相关文章）、措辞不同（`Wilson's book Biophilia (1984)…popularized the notion` vs `Edward Wilson…popularised the term in the 1980s`）、非镜像；两者独立载明「Wilson／Biophilia／1980 年代普及」核心史实，构成真双源互证 |
| 七节 | ✓ | definition + sections 六节（原理／典型手法与适用条件／实例／常见错误与限制／一图／待核实）＝七节齐，无空缺（check.py 0 报错） |
| SVG | ✓ | 1 张（`viewBox 0 0 760 400`，rect/circle/line/text，含「示意图，非施工图」；无 `on*=` 事件处理器、无 `<image>`/xlink/href/`<script>`；check.py 0 报错） |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位 |
| nv↔pending 联动 | ✓ 一致 | `needs_verification=false`／`pending_notes=""`／「待核实」节「暂无已知待核实项」三处一致；正文无内联「待核实」声明；check.py 未报「有待核实说明但 nv=false」类错误 |
| **nv 置 false 是否有据** | ✓ 有据 | 实例核心三要素（作者 Edward O. Wilson／书名 Biophilia／1984 提出且 1980 年代普及）由 Wikipedia 逐字回读、`Edward Wilson…popularised the term in the 1980s` 由 Designing Buildings 逐字互证，**未编造人名/数字/年份**；definition「自然要素与过程→健康与福祉」由 db `natural processes`＋wp `health and well-being` 直证。满足双源互证，标 nv=false 有据 |
| coverage↔entry | ✓ | title「亲生命性设计」/theme「理论」/tier「重要」/period「当代」/region「全球」/level「L2」全一致；`source_count=3`＝entries 3 源（wp-biophilic-design/wp-evidence-based-design/db-biophilic-design）；`needs_verification_count=0`＝nv false；status=已写 |
| 相似度（阈值 0.54） | ✓ | ①短 最高 **0.4194**（vs lighting-design）＜0.54；②全字段 最高 **0.3470**（vs international-style）＜0.54，均低于阈值 |

**`biophilic-design` 结论：合格（本轮已可升级为已验证）。**

## 三、问题与建议（均非阻断）

1. **（提示，非阻断）definition 属概念抽象＋关键词逐字混成**：「自然要素与过程」对 db `natural processes`（逐字）、「健康与福祉」对 wp `health and well-being`（逐字），其余为概念化组织。与第68–70轮既定口径（实例有据＋合理概念抽象即标 nv=false）同型，成立。
2. **（提示，非阻断）实例「地点：美国（概念起源）」为推断性地点**：db 称 Wilson 为 `an American biologist`、wp 述其为概念源头；「美国」指概念发源地而非某具体建筑，表述已标「（概念起源）」限定，未夸大。可保留。
3. **（提示，非阻断）`wp-biophilic-design` 的 note 载 canonical 直连曾因网络限制未确、经镜像核对**：本轮 canonical `en.wikipedia.org` 实抓 HTTP 200、正文可回读，标题与首句、Wilson/Biophilia/1984 均命中，等于已补正该 note 的历史状态；`link_ok` 仍为 null，与 D11 三态口径一致（不改 verified）。可选后续把 link_ok 更新为 true，不阻断。

## 四、总体结论

- **`biophilic-design`：合格（本轮已可升级为已验证）。**
  - 实例「亲生命设计理论（Biophilia, Edward O. Wilson, 1984／1980 年代普及，美国）」名称/作者/年份由 `wp-biophilic-design` 逐字回读；「Edward Wilson…popularised the term in the 1980s」由 `db-biophilic-design` 逐字互证，**未编造人名/数字/年份**。
  - **两源独立成立**：Wikipedia（众编百科）与 Designing Buildings（建筑行业站）两独立发布主体、体例与措辞不同、非镜像，核心史实互证。
  - **nv=false 有据**；七节齐、SVG 合规、规范句在位、coverage 全字段一致。
  - **相似度 0.4194 / 0.3470 均低于 0.54**。
- 全库 `python tools/check.py`＝`PASS: all checks, 0 errors`（EXIT=0）。
- **本轮 1 条：1 合格、0 待核实、0 不合格。**
- **建议（非阻断）**：① 可后续将 `wp-biophilic-design` 的 `link_ok` 由 null 更新为 true（canonical 本轮已 200）；② 其余表述无需改动。

## 五、机器可读汇总

```
ROUND=71
SAMPLER=spotcheck-r71
MODE=round71 改动 1 条抽检（biophilic-design 升级已验证）
SCOPE=["biophilic-design"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round70.md","README.md","tools/check.py","tools/apply_review_round71.py","entries/batch-11.json","data/sources.json","coverage.json"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback; temp research/_r71_*.txt + _r71_fetch.py/_r71_sim.py deleted after"
FETCHES={"wp-biophilic-design":200,"db-biophilic-design":200}
BIOPHILIC_DESIGN={
 "sources":["wp-biophilic-design","wp-evidence-based-design","db-biophilic-design"],
 "definition_support":"db 'connect people to nature and natural processes'+'increase wellbeing' + wp 'improve their health and well-being' -> 直证",
 "instance":"亲生命设计理论（Biophilia）/ 美国(概念起源) / Edward O. Wilson / 1984《Biophilia》提出且1980s普及",
 "quote_wp":"'Biophilic design seeks to increase people\"s connectivity to nature...to improve their health and well-being' + 'Edward O. Wilson\"s book Biophilia (1984)...popularized the notion' VERBATIM",
 "quote_db":"'Edward Wilson, an American biologist, popularised the term in the 1980s.' + 'Biophilic design makes use of natural materials and planting to increase wellbeing.' VERBATIM",
 "fabrication":"none; Wilson/Biophilia/1984/popularized wp逐字; Edward Wilson/popularised/1980s db逐字",
 "two_source_independence":"wp=Wikipedia(众编百科) vs db=Designing Buildings(建筑行业站): 两独立主体/体例措辞不同/非镜像 -> 真双源互证",
 "seven_sections":7,"svg":"1x viewBox760x400 rect/circle/line/text 示意图非施工图, no on*/image/xlink/href/script",
 "reg_sentence":true,"nv":false,"pending_consistent":true,
 "nv_false_basis":"作者Wilson/书名Biophilia/1984由wp逐字+Edward Wilson popularised 1980s由db逐字互证, 未编造; definition由natural processes/health-wellbeing直证 -> 有据",
 "coverage":"title/theme/tier/period/region/level 一致; source_count3=3源; nvc0=nvfalse",
 "similarity":{"short":0.4194,"short_vs":"lighting-design","full":0.3470,"full_vs":"international-style","threshold":0.54},
 "verdict":"合格"}
TOTAL="1合格/0待核实/0不合格"
RECOMMEND="非阻断: ①可将wp-biophilic-design的link_ok由null更新为true(canonical本轮200) ②其余无需改动"
READONLY="only wrote research/spotcheck-round71.md; fetched html in-memory, temp research/_r71_*.txt + _r71_fetch.py/_r71_sim.py deleted; no entries/sources/coverage/tools/site changed; no git commit; web treated as data (no instructions executed)"
NOTE="工作区含 round71 未提交改动(biophilic-design 条目实例改写+db-biophilic-design 源+coverage+site html+apply_review_round71.py), 核验以工作区当前内容为准, 未触碰"
```

*（报告完）*
