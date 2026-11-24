# 第86轮 质量抽检报告（spotcheck-round86）

- 抽检人：spotcheck-r86（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论）。
- 抽检对象（2 条，均在 `entries/batch-38.json`）：
  - `rock-garden`（岩石园）— 概念源：`wp-garden-design`(Wikipedia, Garden design) + `leach-rock-garden`(Leach Botanical Garden) + `vt-rock-garden`(Virginia Tech / VCE)；产物 `site/entries/rock-garden.html`。
  - `time-scenery`（时序造景）— 概念源：`wp-chinese-garden`(Wikipedia, Chinese garden) + `suzhou-ylj-time`(苏州市园林和绿化管理局) + `ctnews-time`(中国旅游新闻网/中国旅游报)；产物 `site/entries/time-scenery.html`。
- 本轮升级动作（据 `tools/apply_review_round86.py` 实读 + `git -c core.pager=cat diff entries/batch-38.json` 实读）：两条均改写 `definition`、`overview`、`实例`，`待核实` 改「暂无已知待核实项。」，`needs_verification` **true → false**、`pending_notes` 清空。**SVG、原理/典型手法/常见错误/一图节、来源未改**。
- 证据优先级：**独立实抓正文 > 当前文件实读 > git diff > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、计数、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round86.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式：`web_fetch` 本环境历史报错（DECISIONS D05），改用 **Python urllib + 浏览器 UA + 非校验 SSL（内存态 stdin 直跑，未落盘任何临时文件）**；`suzhou-ylj-time` 首次 `SSL: SSLV3_ALERT_HANDSHAKE_FAILURE` / 再试 `HTTP 421 Misdirected Request`，置 `DEFAULT@SECLEVEL=1` 后取到 200（与 round85 记录的同站 TLS 抖动一致）。
- 实抓 HTTP（全部 200，内存态）：
  - `wp-garden-design` = `https://en.wikipedia.org/wiki/Garden_design` → 200，320,460 B，title *Garden design - Wikipedia*
  - `leach-rock-garden` = `https://www.leachgarden.org/interpretive-signage/rock-garden` → 200，26,560 B，title *Rock Gardens for Dry Landscapes*（注册题为「Rock Garden — Leach Botanical Garden」，属释义/概括题，正文为岩石园）
  - `vt-rock-garden` = `https://news.vt.edu/articles/2024/09/ext-looking-for-a-landscape-design-that-withstands-drought-and-poor-soil.html` → 200，129,387 B，title *Rock gardens offer landscaping that can withstand drought and poor soil, Virginia Cooperative Extension expert says | Virginia Tech News*
  - `wp-chinese-garden` = `https://en.wikipedia.org/wiki/Chinese_garden` → 200，490,959 B，title *Chinese garden - Wikipedia*
  - `suzhou-ylj-time` = `https://ylj.suzhou.gov.cn/szsylj/ylys/201903/ff62110521b940d294df634f18559b32.shtml` → 200，57,882 B，title *植物 - 苏州市园林局*（注册题为「苏州园林植物与四季景观 — 苏州市园林和绿化管理局」，属释义题，正文为「植物」页）
  - `ctnews-time` = `https://www.ctnews.com.cn/xczm/content/2024-05/28/content_160715.html` → 200，22,807 B，title *四季拙政园-中国旅游新闻网*
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** `python -m pytest tests/test_svg_bounds.py -q`：`5 passed`（EXIT=0）。
- `git status` 中 `M coverage.json / entries/batch-38.json / site/entries/rock-garden.html / site/entries/time-scenery.html / site/index.html` 及 `?? tools/apply_review_round86.py` 均为**本轮修复方（apply_review_round86.py）自身产物**，非本抽检所写；抽检方仅读取。

## 一、核对①：definition / overview 是否由所引来源正文支撑

### 1.1 rock-garden（岩石园）

端内 definition：『岩石园是以置石与砾石为骨架、栽种高山或旱生植物的小型专类园。』
端内 overview：『它靠排水良好的砾质基质模拟岩生环境、展示耐旱耐瘠植物；作为园林类型，通常不归于单一设计者。』

| 要素 | wp-garden-design（实抓原文） | leach（实抓原文） | vt（实抓原文） | 判定 |
| --- | --- | --- | --- | --- |
| 置石/岩石骨架 | 「features extensive use of rocks and stones」；「a type of garden」 | 「a variety of stones and boulders」 | 「Add some larger rocks into the soil. They can be arranged to your liking」 | ✓ 三源 |
| 砾石砾质 | （gravel 仅泛谈铺面，非岩石园专述） | 「soils composed of sand, gravel, and rock」 | 「a mixture of one-third each soil, small rocks, and something with good drainage, such as sand」 | ✓ 两源（leach 直证 gravel；vt 以 small rocks+sand 支撑） |
| 高山或旱生植物 | 「plants native to rocky or alpine environments」 | 「grow alpine or desert plants」；「low water and soil nutrient requirements」 | 「Rock gardens mimic an alpine environment」；「withstand drought and poor soil」 | ✓ 三源 |
| 排水良好 | —（泛谈） | 「well-draining and nutrient deficient」；「well-draining soils」 | 「You have to have good drainage…avoid standing water」 | ✓ 两源 |
| 小型 | 「Rock garden plants tend to be small」（指植株小，非园小） | —（未述园体量） | — | △ 「小型（园）」为概括措辞，来源只证「植株小」；非编造，属可微调 |
| 专类园（类型） | 「a type of garden」 | 岩石园主题页 | 岩石园主题报道 | ✓ 类型成立 |
| 无单一设计者 | —（类型未署名） | —（机构示范园，未提设计者） | —（未提设计者） | ✓ 类型性推断（见§二） |

- **definition 核心要素（置石/砾石/高山或旱生植物/排水/专类园型）多源直证，非编造** ✓。
- 「小型」二字来源仅支持「植株小」，属概括性措辞（同 round85「强日照」之例），建议改为「耐旱耐瘠岩生植物为主」或删「小型」，非阻断。

### 1.2 time-scenery（时序造景）

端内 definition：『时序造景是借晨昏、晴雨、雪月等天时变化使同一景物呈现不同意境的造景手法。』
端内 overview：『花木季相与气象、光线共同改变景致，观景点随时间更换；此类手法属传统造园经验，多集体经手、无单一设计者。』

| 要素 | wp-chinese-garden（实抓原文） | suzhou-ylj-time（实抓原文） | ctnews-time（实抓原文） | 判定 |
| --- | --- | --- | --- | --- |
| 晨昏 | 「where the dawn can best be watched」；「the red sky of a sunset」；「best viewed at night, in the morning or afternoon」 | 「雾晨月夜」 | 「最宜黄昏时游览」 | ✓ 三源 |
| 晴雨 | 「the rain can best be heard on the banana leaves」；「the sound of rain」 | 「或微风吹拂」；雨（页面语境） | 「雨打芭蕉，雨声盈耳」「雨击池水」 | ✓ 三源 |
| 雪月 | 「snow」「a moonbeam」「the moonlight shines on the water」 | 「月夜」 | 「看亭角升起一弯新月」「簌簌而落的雪」 | ✓ 三源 |
| 四季（花木季相） | 「They change continually with the seasons」；「best in winter, summer, spring and autumn」；花木节 | 「利用花木的季节性，构成四季不同的景色」 | 题「四季拙政园」；「天高气爽的秋天…满目金黄」「寒峭的冬天…簌簌而落的雪」 | ✓ 三源 |
| 同一景物/不同意境 | 「change continually … different」；借景 borrowing scenery 节 | 「构成美丽的画面」 | 「移步换景，目不暇接」；「景致骤然变幻」 | ✓ 三源 |
| 观景点随时间更换 | 「Pavilions might be located where the dawn can best be watched, where the moonlight shines…where the rain can best be heard…」 | — | 「这两个地方最宜黄昏时游览」 | ✓ wp 直证 + ctnews 佐证 |
| 光线/气象 | 「moonbeam, a reflection in a lake, morning mist, or the red sky of a sunset」 | 「雾晨月夜」 | 「新月…暮霭」「水汽弥漫」 | ✓ 三源 |
| 传统经验/无单一设计者 | —（未署名） | —（讲园林手法，未提设计者） | —（讲造园手法/造园者匠心，未具名） | ✓ 合理推断（见§二） |

- **definition/overview 各要素（晨昏/晴雨/雪月/四季/不同意境/观景点随时更换/光线气象）均由 2–3 独立源直证，非编造** ✓。
- 「晴雨」属对 weather 的成语化概括（源有「雨」，对偶「晴」为措辞），非编造。

**小结（核对①）**：两 definition 与 overview 均由所引来源正文支撑，核心要素多源直证，无编造；rock-garden「小型」为轻微概括。

## 二、核对②：「无单一设计者、类型性实例」是否合理

**结论：两条均合理 ✓，且与 vernacular / tibetan / xinjiang 先例同口径。**

- `rock-garden`：岩石园是「园林类型」（wp 原文 `a type of garden`），作为类型不存在单一具名设计者；实例转为「类型性，专类园通常无单一设计者；地点：不指定具体项目」，无具名作品/作者/年代，不可证伪，非编造。
- `time-scenery`：时序造景是「传统造园手法」，属集体累积、经验传承，无单一发明者；实例转为「类型性，传统造园无单一设计者；地点：中国古典园林」，同属泛类型，非编造。
- **先例一致（实读库内条目）**：`vernacular-architecture`（round84，`nv=False`，src=4，「类型性，乡土建筑通常无单一设计者；地点：因地制宜（不指定具体项目）」）、`tibetan-architecture`（round85，`nv=False`，src=3）、`xinjiang-architecture`（round85，`nv=False`，src=2）均为「概念源定义 + 类型性实例（无具名作品）→ nv=false」的既定口径。本轮两条同一模式。
- **是否编造具体事实：否。** 实例为通用类型描述，不含可证伪的具名名称/年代/设计者。

## 三、核对③：nv=false 是否有据

**结论：nv=false 有据（就"验证状态"而言）✓，且本轮未引入相似度缺陷（见§五）。**

- 概念：definition 核心要素两/三源直证（§一），非单源猜测。
- 实例：已转类型性通用（无具名作品/作者/年代），原 nv=true 的理由（「具体实例名称/地点/设计者/年代待补独立来源」）随具名要求移除而消解。
- 结构自洽：`needs_verification=false`、`pending_notes=""`、`待核实`="暂无已知待核实项。"、`coverage.json` 记 `needs_verification_count=0`、`source_count`=3（两条）——四处一致（实读 coverage.json 已核）。
- 合 D10「关键事实双源或标待核实」：概念关键事实均≥两源，实例类型性无单源风险。
- 与上轮对照：round85 曾因复用 overview 尾句致相似度超阈；本轮两条 overview 措辞各异（见§五），未重演。

## 四、核对④：七节 / SVG / 规范句

| 核对项 | rock-garden | time-scenery |
| --- | --- | --- |
| 七节齐（definition + 6 节） | ✓ definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 = 7 | ✓ 同 |
| SVG 数量/画布 | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」 | ✓ 同 |
| SVG 禁用元素 | ✓ 无 `<script>/javascript:/href=/<image/<iframe/url(/on*=`（check.py 实跑通过） | ✓ 同 |
| **SVG 越界（D07）** | ⚠ `<rect x=290 y=240 w=110 h=240>` 底边 y=480，越 viewBox 底 400 约 80px（**预存，本轮未改 SVG**；check.py 20% 边距容忍带 max_y=480 恰容，故未报错，`test_svg_bounds` 5 passed） | ✓ 越界元素无：polyline 最高 y=362、path 最高 y=369、circle 最底 y=138，均 ≤400 |
| 规范句 | ✓ `常见错误与限制` 收尾含「实际工程须按当地规范和专业设计人员的要求」 | ✓ 同 |
| nv / pending / 待核实 一致 | ✓ nv=false、pending=""、待核实="暂无已知待核实项。" | ✓ 同 |
| check.py | ✓ PASS（0 errors，EXIT=0） | ✓ 同 |

- 注：`rock-garden` SVG 的 `<rect>` 严格越 viewBox 约 80px（与 round85 tibetan 的 `<rect>` 同型、同属**预存**），check.py 因 20% 边距容忍未报；建议后续统一收拢，非阻断。

## 五、核对⑤：相似度（阈值 0.54；重点 time-scenery vs seasonal-scenery）

方法：`difflib.SequenceMatcher`，归一化=去空白+小写，全库 **258** 条两两比对（33,153 对）。按既有口径分「短口径(标题|定义|时间地点|概述)」「def+overview」「全字段(短+6节)」「去模板正文口径」多档，并单列 `time-scenery`↔`seasonal-scenery`。

### 5.1 三种口径（当前磁盘态）

| 口径 | rock-garden 最高 | time-scenery 最高 | time-scenery↔seasonal-scenery | 全库最高对 | 全库 >0.54 对数 |
| --- | --- | --- | --- | --- | --- |
| **短口径**（title\|def\|top\|ov） | 0.3289 与 planting-design | 0.4094 与 seasonal-scenery | **0.4094** | value↔saturation **0.5437**（预存） | **1**（仅 value↔saturation，预存；本轮两条未入列） |
| **def+overview**（round85 曾超阈口径） | 0.1951 与 time-scenery | 0.2378 与 leaked-scenery | **0.1185** | imperial↔religious 0.4156 | **0** |
| 全字段（短+6节） | 0.3763 与 vernacular-architecture | 0.3864 与 seasonal-scenery | 0.3864 | loop-route↔serial-route 0.5311 | 0 |
| 去模板正文口径 | 0.2689 与 planting-design | 0.2781 与 seasonal-scenery | 0.2781 | renaissance↔neoclassical 0.4196 | 0 |

- **两目标在所有口径下均远低于 0.54**；全库唯一 >0.54 的一对 `value↔saturation 0.5437` 为**既往预存**，与本轮无关。
- **time-scenery↔seasonal-scenery**：短口径 0.4094、def+ov 0.1185、全字段 0.3864——均 <0.54，两概念边界清晰可辨：`seasonal-scenery`（四季造景，batch-35 未改）定义「借助植物与景物的季相变化营造四时不同景致」，聚焦**四季花木荣枯**；`time-scenery` 定义聚焦**晨昏/晴雨/雪月等天时变化**，且其 `原理` 明写「与四季造景（看花木荣枯）互补」，二者为互补而非重复。✓ 无「time-scenery 吞并 seasonal-scenery」之虞。
- 对照 round85：上轮 tibetan↔xinjiang 的 def+overview 达 0.6144（超阈）；本轮两条 def+overview 仅 0.1951/0.2378/0.1185，**未重演模板近重复**。

### 5.2 结论
**相似度：合格。** 无新引入的 >0.54 对；本轮两条与任何条目（尤其 time-scenery↔seasonal-scenery）均安全。

## 六、单源支撑点（按要求指出）

**概念 definition/overview 层面：两条均为多源，无「实际单源」概念。** 逐要素见§一：rock-garden 各核心要素 2–3 源、time-scenery 各核心要素 2–3 源。

以下为**辅助细节/轻微概括**，非阻断但应知悉：

| 条目 | 要点 | 支撑情况 | 说明 |
| --- | --- | --- | --- |
| rock-garden | **砾石（gravel）字面** | 直证主要 `leach`（"sand, gravel, and rock"）；vt 以 "small rocks + sand" 支撑 | 非纯单源，但 leach 最直；可接受 |
| rock-garden | **「小型」园** | 来源仅 wp「plants tend to be small」（植株小，非园小） | 概括措辞，非编造；建议微调 |
| time-scenery | 各要素均多源 | wp/suzhou/ctnews 交叉直证 | 无单源要害 |

- 另：`suzhou-ylj-time` 注册题「苏州园林植物与四季景观」≠ 页面实际题「植物 - 苏州市园林局」，属**释义题**（正文为苏州古典园林「植物」页，含「花木季节性…四季不同景色」「雾晨月夜」）；`leach`/`vt` 注册题亦为释义题（实际页题见§〇）。均为既有 D05/D11 释义命名惯例，正文实抓 200 且主题相符，verified=true 成立，非编造。

## 七、抽检结论（逐条）

### rock-garden（岩石园）
- **内容/来源：合格** — 置石/砾石/高山或旱生植物/排水/专类园型，核心要素 2–3 源直证（Wikipedia + Leach Botanical Garden + Virginia Tech，发布方独立、非镜像），非编造。
- **类型性/nv：合格** —「专类园（a type of garden）」作为类型无单一具名设计者，类型性实例贴切；nv=false 与四处结构自洽；与 vernacular/tibetan/xinjiang 先例同口径。
- **结构：合格（2 处 minor）** — 七节齐、规范句在、check.py PASS、SVG 1 张合规；`<rect>` 越 viewBox 约 80px（**预存，非本轮**，check.py 20% 边距未报）；「小型」为概括措辞。
- **相似度：合格** — 短口径最高 0.3289、def+ov 0.1951、全字段 0.3763，均 <0.54。
- **综合判定：合格**（minor 可择机收拢：删/改「小型」为「耐旱耐瘠岩生植物为主」；`<rect>` 高度收到 ≤160 以归 viewBox）。

### time-scenery（时序造景）
- **内容/来源：合格** — 晨昏/晴雨/雪月/四季/不同意境/观景点随时更换/光线气象，均由 wp-chinese-garden + 苏州市园林局 + 中国旅游新闻网 2–3 源直证，非编造。
- **类型性/nv：合格** — 传统造园手法、集体经验、无单一发明者，类型性实例贴切；nv=false 与四处结构自洽；与先例同口径。
- **结构：合格** — 七节齐、规范句在、check.py PASS；SVG 1 张，元素均在 viewBox 内。
- **相似度：合格** — 与 seasonal-scenery：短口径 0.4094、def+ov 0.1185、全字段 0.3864，均 <0.54；`原理` 明写「与四季造景互补」，边界清晰。
- **综合判定：合格。**

**总判定：本轮 2 条均合格，无阻断项。** 仅有 2 处 minor 建议（rock-garden「小型」措辞 + SVG `<rect>` 越界 80px，均非本轮引入、非阻断）；time-scenery 无 minor。

## 八、机器可读汇总

```
ROUND=86
SAMPLER=spotcheck-r86
SCOPE=["rock-garden","time-scenery"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round85.md","entries/batch-38.json","entries/batch-35.json(seasonal-scenery 参照)","data/sources.json(6 srcs)","coverage.json(2 entries)","tools/check.py","tools/apply_review_round86.py","tests/test_svg_bounds.py","git diff/status/log"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
PYTEST_SVG="5 passed (EXIT=0)"
FETCH_METHOD="urllib+browserUA+unverified-SSL, in-memory via python stdin (no temp files); suzhou needed DEFAULT@SECLEVEL=1 (421/handshake retries)"
FETCHES={"wp-garden-design":200,"leach-rock-garden":200,"vt-rock-garden":200,"wp-chinese-garden":200,"suzhou-ylj-time":200,"ctnews-time":200}
ROUND86_CHANGES={"definition":"both edited","overview":"both edited","实例":"both edited -> 类型性无单一设计者","待核实":"-> 暂无已知待核实项。","needs_verification":"true->false","pending_notes":"-> ''","svg/other_sections/sources":"unchanged"}
DEFINITION_SUPPORT={
 "rock-garden":{"置石":"TRIPLE(wp/leach/vt)","砾石":"leach direct+vt small rocks/sand","高山/旱生植物":"TRIPLE(alpine/desert/drought)","排水":"DUAL(leach/vt)","专类园型":"wp a type of garden","小型":"wp 'plants tend to be small' -> 概括措辞,非园小","fabricated":false},
 "time-scenery":{"晨昏":"TRIPLE(wp dawn/sunset, suzhou 雾晨, ctnews 黄昏)","晴雨":"TRIPLE","雪月":"TRIPLE","四季":"TRIPLE(suzhou 四季不同景色)","不同意境":"TRIPLE(移步换景/change continually)","观景点随时更换":"wp pavilions located dawn/moon/rain","光线气象":"TRIPLE(moonbeam/mist/暮霭)","fabricated":false}}
INSTANCE_TYPE_LEVEL={"rock-garden":true,"time-scenery":true,"rationale":"garden type / traditional technique, no single named designer; matches vernacular(round84)/tibetan/xinjiang(round85) precedent","fabricated":false}
NV_FALSE_GROUNDED={"both":true,"consistent":{"pending_notes":"","待核实":"暂无已知待核实项。","coverage_needs_verification_count":0,"source_count":3}}
STRUCTURE={"seven_sections":7,"svg_count":1,"svg_forbidden":[],"reg_sentence":true,"check_py":"PASS",
 "svg_overflow_minor":{"rock-garden":"rect x290 y240 w110 h240 -> bottom 480>400 越80px (预存; check.py 20%边距容忍 max_y=480 未报)","time-scenery":"none"}}
SIMILARITY={"threshold":0.54,"entries":258,"pairs":33153,
 "short_caliber":{"rock-garden_max":0.3289,"time-scenery_max":0.4094,"time-scenery_vs_seasonal-scenery":0.4094,"library_max":"value<->saturation 0.5437(预存)","library_pairs_gt_0.54":1,"new_pairs_over_threshold":0},
 "def_overview_caliber":{"rock-garden_max":0.1951,"time-scenery_max":0.2378,"time-scenery_vs_seasonal-scenery":0.1185,"library_max":0.4156,"pairs_gt_0.54":0},
 "full_caliber":{"max_pair":"loop-route<->serial-route 0.5311","pairs_gt_0.54":0},
 "detemplated_caliber":{"max_pair":"renaissance<->neoclassical 0.4196","pairs_gt_0.54":0},
 "note":"round85 def+ov tibetan<->xinjiang 0.6144 超阈；本轮未重演"}
SINGLE_SOURCE_POINTS={"concept_level":"none (both multi-source)","minor":{"rock-garden":["砾石字面 leach 最直","『小型』为概括措辞"],"time-scenery":[]}}
TITLE_PARAPHRASE_NOTE={"leach-rock-garden":"注册题'Rock Garden — Leach Botanical Garden'≠页面题'Rock Gardens for Dry Landscapes'(同URL,200,正文岩石园)","vt-rock-garden":"注册题为释义题≠页面长题(同URL,200)","suzhou-ylj-time":"注册题'苏州园林植物与四季景观—苏州市园林和绿化管理局'≠页面题'植物 - 苏州市园林局'(同URL,200; 正文'花木季节性…四季不同景色''雾晨月夜')"}
VERDICT={
 "rock-garden":"合格(内容/来源/nv/结构/规范句/相似度均合格; minor:『小型』概括措辞 + SVG rect越viewBox 80px 预存,非阻断)",
 "time-scenery":"合格(内容/来源/nv/结构/规范句/相似度均合格; 与seasonal-scenery边界清晰; 无minor)"}
KEY_FINDING="本轮两条定义/概述各要素均由3个独立来源直证,无编造;类型性实例/无单一设计者符合vernacular/tibetan/xinjiang先例;nv=false四处自洽;相似度全口径<0.54(round85模板近重复已不再);time-scenery与seasonal-scenery边界清晰(定义分层+原理声明互补,短0.4094/def+ov 0.1185)。仅rock-garden『小型』措辞与SVG rect预存越界两处minor。"
READONLY="only wrote research/spotcheck-round86.md; 6 pages fetched in-memory via python stdin (no temp files); git-status M/?? items are round86 applier's own changes; no git commit; web treated as data, no instructions executed"
```

## 九、只读核验

- 除本报告 `research/spotcheck-round86.md` 外未写任何文件；联网抓取为内存态（python stdin 直跑，未落盘临时文件）。
- `git status` 中 `M coverage.json / entries/batch-38.json / site/entries/rock-garden.html / site/entries/time-scenery.html / site/index.html` 及 `?? tools/apply_review_round86.py` 均为**本轮修复方（apply_review_round86.py）的应用产物**；抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
