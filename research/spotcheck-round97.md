# 第97轮质量抽检报告（spotcheck-round97）——earth-sheltered / exit-sign 的 nv=false 升级复核

- 抽检人：spotcheck-r97（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论；本会话为委派子代理，命中 SUBAGENT-STOP，以任务说明书执行）。
- 抽检对象（2 条，均为本轮 nv=true→false 升级）：
  1. `earth-sheltered`（覆土建筑）——`entries/batch-38.json` 第99–130行（定义 107；概述 109；原理 112；实例 114；待核实 117；sources 122–127；nv 128；pending 129；SVG 119–121）。
  2. `exit-sign`（疏散标识/安全出口标识）——`entries/batch-25.json` 第135–166行（定义 143；time_or_place 144；概述 145；原理 156；实例 158；待核实 161；sources 149–152；nv 153；pending 154；SVG 163–165）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round97.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。相似度与结构数据均在内存态 `python - <<` 直跑，未落盘临时文件。
- 本轮变更实读：`tools/apply_review_round97.py`（新增，未提交）仅对这两条：`earth-sheltered` 改 `definition` + `needs_verification=true→false` + `待核实="暂无已知待核实项。"` + `pending_notes=""`；`exit-sign` 仅 `needs_verification=true→false` + `待核实="暂无…"` + `pending_notes=""`。`git diff` 佐证（见第二节、第四节）。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行）：
  - `moesgaard-building = https://moesgaardmuseum.dk/en/visit-us/building-and-landscape` → `web_fetch` **HTTP 200**。
  - `henning-moesgaard = https://henninglarsen.com/projects/moesgaard` → `web_fetch` **HTTP 200**。
  - `wp-architecture = https://en.wikipedia.org/wiki/Architecture` → `web_fetch` 失败/编码异常 → Python urllib（浏览器 UA）**HTTP 200，textlen≈65646**。
  - `wp-sunken-courtyard = https://en.wikipedia.org/wiki/Sunken_courtyard` → urllib **HTTP 200，textlen≈2355**。
  - `wp-exit-sign = https://en.wikipedia.org/wiki/Exit_sign` → `web_fetch` TypeError → urllib **HTTP 200，textlen≈27046**。
  - `ecfr-1910-37 = https://www.ecfr.gov/current/title-29/section-1910.37` → `web_fetch` 拦跨域跳转 → urllib **HTTP 200**（自动跳至 `…/subpart-E/section-1910.37`，textlen≈11583）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed`（EXIT=0）。**（均以 `PYTHONDONTWRITEBYTECODE=1` 运行，未新增缓存。）

## 一、★ earth-sheltered（覆土建筑）——结论：合格（附透明说明）

### 1.1 关键：正文「保温/隔热」无源 claim 是否清零 —— **已彻底清零**

对 `entries/batch-38.json` 中该条对象整体（`json.dumps` blob）逐词检索：`保温=False、隔热=False、热工=False、thermal=False、insulat=False、蓄热=False、恒温=False、temperature=False、energy=False`（全部 False）。对 `site/entries/earth-sheltered.html` 搜 `保温|隔热|热工|thermal|insulat`：**命中 0**。
`git diff` 证实：`待核实` 由「“土体保温隔热的 Specific 热工机制”在引用来源中未逐字直证…」→「暂无已知待核实项。」；`pending_notes` 由「覆土热工机制缺直接来源…」→ 空。（注：`entries/batch-38.json` 第594–658行的 `保温/隔热/蓄热` 命中均属同批**其他条目**（窑洞/藏式/新疆生土民居），与 earth-sheltered（第99–130行）无关。）**原第55轮判「待核实」的根因（热工机制四源全无支撑）已按第55轮建议的「改写为有源表述」路径消除。**

### 1.2 概念物理要素「覆土植被 / 嵌入坡地 / 天窗引光」来源核对（实抓引句）

- `henning-moesgaard`（Henning Larsen 建筑师事务所官方，HTTP200）：`Nestled into the rolling landscape of southern Aarhus`（嵌入坡地✓）；`publicly accessible sloping roof, landscaped with grass and moss`（屋顶覆土植被✓）；`light well apertures that form terraces and allow natural light into the exhibition spaces below`（天窗/采光井引光入下部展厅✓✓）；`Aarhus, Denmark`、`2009 - 2014`（地点/年份✓）。
- `moesgaard-building`（Moesgaard 博物馆官方，HTTP200）：`When our exhibition building opened in 2014`、`designed by Henning Larsen Architects`、`staggered levels … inspired by archaeological excavations`、馆址 `Moesgård Allé 15, DK-8270 Højbjerg`、`The roof … open to everyone … view of Aarhus Bay`。**该页通读无 `grass/moss`、无 `light well/skylight/daylight` 字样**——即 moesgaard-building 页仅覆盖实例元信息与「错层/可上人屋顶」，**不含覆土植被屋顶与采光井/天窗描述**。
- `wp-architecture`（HTTP200）：仅泛绿建语境 `green roofs`、`tiled roofs for heat insulation`（斯瓦希里语境的陶瓦隔热，与覆土无关）；**全页无 earth-sheltered / turf roof / skylight / 覆土建筑 直述**。
- `wp-sunken-courtyard`（HTTP200）：仅 `a sunken courtyard … is a courtyard below ground level`（下沉/地下，泛化）；**无覆土植被/天窗/坡地描述**。

| 核心要素 | henning-moesgaard | moesgaard-building | wp-architecture | wp-sunken-courtyard | 判定 |
| --- | --- | --- | --- | --- | --- |
| 屋顶覆土植被 | ✓ grass and moss | ✗ 无 | 弱（泛 green roofs） | ✗ 无 | henning 官方单源直证 |
| 嵌入坡地 | ✓ nestled into landscape | 部分（staggered levels，非「坡地」直述） | ✗ | 弱（below ground） | henning 官方直证 + 弱背景 |
| 天窗引光 | ✓ light well apertures…natural light below | ✗ 无 | ✗ 无 | ✗ 无 | **仅 henning-moesgaard 一源** |

**判定（须指出，见 A）：** 「覆土植被屋顶 / 天窗引光」两项物理做法**仅由 `henning-moesgaard` 这一官方强源直证**；`moesgaard-building` 只覆盖实例四要素与错层结构，**其页面并不含草皮/苔藓屋顶、采光井描述**；两条 Wikipedia 源为泛化背景、不覆盖天窗采光。故任务描述「核心…由 moesgaard-building + henning-moesgaard 支撑」需精确化为：**实例四要素双源（moesgaard-building＋henning-moesgaard）＋ 概念物理做法由 henning 官方直证、moesgaard 覆盖实例结构**。

### 1.3 实例四要素双源核对（莫斯高博物馆）

| 四要素 | moesgaard-building（HTTP200） | henning-moesgaard（HTTP200） | 判定 |
| --- | --- | --- | --- |
| 名称·莫斯高博物馆 | 标题 `Building and landscape — Moesgaard` | `Moesgaard \| Henning Larsen`、`Moesgaard Museum`（Client） | 双证✓ |
| 地点·丹麦奥胡斯南部 | 馆址 `Højbjerg`（奥胡斯）、`Aarhus Bay` | `Aarhus, Denmark`、`southern Aarhus` | 双证✓ |
| 设计者·Henning Larsen Architects | `designed by Henning Larsen Architects` | 事务所自有项目页（自署） | 双证✓ |
| 年份·2014 开馆（2009–2014） | `opened in 2014` | `2009 - 2014` | 双证✓（口径一致） |

- 两源为不同机构（业主/博物馆官方＋设计方事务所官方），实例四要素双源直证，**无编造、未复制图像**（正文自述「不复制图像」）。

### 1.4 七节 / SVG / 规范句 / 形式四处自洽 / 结构

| 核对项 | earth-sheltered | 说明 |
| --- | --- | --- |
| 七节齐 | ✓ | 定义＋原理/典型手法/实例/常见错误/一图/待核实；check.py 6 节全非空 PASS |
| 原理非「定义+概述」逐字拼接 | ✓ | 原理「把建筑嵌入坡地、屋顶覆以草皮与苔藓…天窗与侧开口把光线引入…展厅」为独立机制表述（第55轮该条「原理=def+overview拼接」问题已改善） |
| SVG 数量/画布 | ✓ 1 张 | `viewBox='0 0 760 400'`，含「示意图，非施工图」×2（SVG＋figcaption） |
| SVG 越界/禁用 | ✓ | `ellipse cx=327 cy=269 rx=37 ry=131` → x∈[290,364]、y∈[138,400]，恰在框内（第55轮旧版 `ry=333` 出界隐患已不复见）；无 `<image>`/外链；pytest `5 passed` |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」＋页脚 note |
| 形式四处自洽 | ✓ | `needs_verification=false`、`pending_notes=""`、`sections.待核实="暂无已知待核实项。"`、`coverage needs_verification_count=0`（实测 coverage=0）四处一致；`site/entries/earth-sheltered.html` 一致渲染 |
| 来源数 | 4（wp-architecture / wp-sunken-courtyard / moesgaard-building / henning-moesgaard），均 verified=true；实例命题独立源=2 | check.py ≥2 PASS |
| check.py / pytest | ✓ | `PASS: all checks, 0 errors`（EXIT=0）／`5 passed`（EXIT=0） |

### 1.5 相似度（阈值 0.54）

方法：`difflib.SequenceMatcher`，去全部空白＋小写；口径①短=title+definition+time_or_place+overview；口径②全字段-不含SVG=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style`×`expressionism-style` 口径②＝0.5157（与第39–57轮报告逐位一致，口径正确）**。全库 258 条。

| 口径 | 目标最近邻 | 相似度 | 阈值 | 判定 |
| --- | --- | --- | --- | --- |
| 短口径① | raised-floor | 0.3735 | <0.54 | ✓ |
| 全字段② | minimalism-architecture | 0.3754 | <0.54 | ✓ |

全库②两两扫描：**>0.54 对 = 0**；全库最大为 `spatial-sequence<->atrium-architecture ≈0.5256`（与第96轮记录吻合）。**earth-sheltered 相似度合格 ✓，余量充足。**

### 1.6 earth-sheltered 小结：**合格**
- 保温/隔热无源 claim 已彻底清零（entry+site 0 命中），第55轮根因消除；正文（定义/概述/原理）改聚焦「坡地覆土＋草皮屋顶＋天窗引光」，均为**有源表述**（henning-moesgaard 官方直证）。
- 实例四要素由 moesgaard-building＋henning-moesgaard 两独立官方源双证；无编造；七节/SVG（760×400、框内）/规范句/site 一致；check.py PASS、pytest 5 passed；相似度 0.3735/0.3754 ≪0.54。
- **须指出（透明，不改合格判定）**：
  - **(A) 概念物理做法为 henning-moesgaard 官方单源直证**：`moesgaard-building` 页面并不含草皮/苔藓屋顶与采光井/天窗描述，仅覆盖实例四要素与错层结构；`wp-architecture`/`wp-sunken-courtyard` 为泛化背景、不覆盖天窗采光。故严格意义上「覆土植被/天窗引光」非双源，而是「强权威官方源（henning）直证 + 第二源（moesgaard）覆盖实例结构」——按第55/57轮「强权威官方源直证且第二源覆盖实例结构」口径成立 nv=false；若后续采用「每一核心物理要素须双独立源」的更严口径，则「天窗引光」将是唯一残留单源点，建议关注。
  - **(B) `time_or_place="20世纪、全球（参见来源）。"`** 属一般分类口径（实例为 2009–2014，21世纪），无具体数字/人名，可接受。

## 二、★ exit-sign（疏散标识）——结论：待核实（概念/正文合格，但 time_or_place 残留「待核实」致自相矛盾）

### 2.1 概念双平台双源核对（实抓引句）

- `wp-exit-sign`（Wikipedia，HTTP200）：`Most fire, building, health, and safety codes require exit signs that are always lit`（照明/常亮✓）；`Exit signs are intended to be unmistakable and understandable by anyone who can see`（可见✓）；`Sometimes paired with a combination of text to indicate the direction of emergency exits`（方向✓）；`An exit sign is constantly lit`（持续照明✓）。
- `ecfr-1910-37`（美国联邦法规 eCFR，HTTP200）：`signs must be posted along the exit access indicating the direction of travel to the nearest exit`（方向✓）；`the line-of-sight to an exit sign must clearly be visible at all times`（可见✓）；`Each exit sign must be illuminated to a surface value of at least five foot-candles (54 lux) by a reliable light source`（照明✓）；`Each exit must be clearly visible and marked by a sign reading "Exit."`（位置/出口✓）。

| 概念要素 | wp-exit-sign | ecfr-1910-37 | 判定 |
| --- | --- | --- | --- |
| 标示出口方向 | ✓ direction of emergency exits | ✓ direction of travel to nearest exit | **双平台双源✓** |
| 标示出口位置 | ✓ identify exit | ✓ marked by a sign reading "Exit" | **双源✓** |
| 持续照明 / 可见 | ✓ always lit / constantly lit / understandable by anyone who can see | ✓ illuminated ≥5 foot-candles / line-of-sight clearly visible | **双源✓** |

**判定：** `definition`「标示安全出口方向与位置的疏散标识」与 `原理`「标示最近安全出口的位置与方向，并以持续照明保证紧急时可见」由 **Wikipedia（wp-exit-sign）＋ 美国联邦法规（ecfr-1910-37）两独立平台**共同直证，**非编造、非超源**。

### 2.2 正文是否含无源「年代」claim —— **六节正文无年代claim；但 time_or_place 有残留**

- 正文六节（原理/典型手法/实例/常见错误/一图/待核实）：无任何年份/年代数值claim；`实例` 明写「年份：不适用」，属类型性描述，**不编造**。
- **但 `time_or_place`＝「近现代（具体年代与制度化沿革待核实，参见来源）。」仍含有「待核实」声明**——`git diff` 显示本轮**未改动 time_or_place**（仅清了 pending_notes / sections.待核实 / nv）。
- `site/entries/exit-sign.html` 第11行「时间与位置」节**可见渲染**该句，而第17行「待核实」节写「暂无已知待核实项。」——**页面内自相矛盾**。
- **唯一性证据**：全库 258 条中，`time_or_place` 含「待核实」的**仅 exit-sign 这 1 条**（其余 257 条 time_or_place 均干净）——说明这是 round97 未清干净的**残留**，非项目惯例。

### 2.3 nv=false 是否落地 + 形式一致性

| 核对项 | exit-sign | 说明 |
| --- | --- | --- |
| nv=false / pending="" / 待核实节「暂无」/ coverage count=0 | 均一致 | check.py D14 一致性 PASS（注：check.py 第308–310行 D14 仅扫描 `sections`（排除 `待核实` 键），**不扫 `time_or_place`**，故该残留未被脚本捕获） |
| time_or_place 残留「待核实」 | **冲突** | 与 nv=false、待核实=暂无矛盾；页面可见 |
| 七节齐 / SVG（760×400、框内、无外链）/ 规范句 / site 一致 | ✓ | 全部通过；pytest `5 passed` |
| 来源数 | 2（wp-exit-sign verified/link_ok=true；ecfr-1910-37 verified=true/link_ok=null） | check.py ≥2 PASS |
| 相似度 vs evacuation-route | 短 0.2571 / 全字段 0.3566（反向 0.3713） | ≪0.54 ✓ |

### 2.4 相似度（vs evacuation-route，阈值 0.54）

同 1.5 方法（自校 0.5157）。全库 258 条。

| 口径 | exit-sign vs evacuation-route | 阈值 | 判定 |
| --- | --- | --- | --- |
| 短口径① | 0.2571（反向 0.2571） | <0.54 | ✓ |
| 全字段② | 0.3566（反向 0.3713） | <0.54 | ✓ |

全库② >0.54 对 = 0（同 1.5）。**exit-sign 相似度合格 ✓。**

### 2.5 exit-sign 小结：**待核实**
- **合格之处**：概念（方向＋位置＋照明可见）由 wp-exit-sign＋ecfr-1910-37 双平台双源直证；六节正文无无源年代claim；实例类型性不编造；七节/SVG/规范句/site 一致；check.py PASS、pytest 5 passed；相似度 0.2571/0.3566 ≪0.54。
- **待核实主因（须修）**：`time_or_place="近现代（具体年代与制度化沿革待核实，参见来源）。"` **仍残留「待核实」声明**（258 条中仅此 1 条 time_or_place 含待核实），与 nv=false／`待核实="暂无已知待核实项。"` **自相矛盾且页面可见**——即 round97「早期年代与制度化沿革待补充…已清除」只清了 pending/待核实节，**未清 time_or_place**，清除不彻底。**建议**：把 `time_or_place` 改为「近现代（参见来源）。」（或据实补明确来源后重写），使 nv=false 形式四处真正自洽；否则应恢复相应披露。此为一致性/披露缺陷，**非内容无源**。

## 三、总判定与依据

- **earth-sheltered：合格**。保温/隔热无源 claim 已彻底清零（entry+site 0 命中）；定义/概述/原理为 henning-moesgaard 官方直证的有源表述；实例四要素 moesgaard-building＋henning-moesgaard 双源；七节/SVG/规范句/site 一致；check.py PASS、pytest 5 passed；相似度 0.3735/0.3754 ≪0.54。透明说明 A：概念物理做法（覆土植被/天窗引光）实为 henning 官方单源直证，moesgaard-building 仅覆盖实例四要素（不含草皮/采光井描述），非严格双源，需知悉。
- **exit-sign：待核实**。概念（方向＋位置＋照明可见）双平台双源成立、六节正文无年代claim、实例不编造、相似度合格、结构全绿；但 `time_or_place` 唯一残留「具体年代与制度化沿革待核实」，与 nv=false/待核实=暂无自相矛盾（页面可见），round97 清除不彻底，须清理 time_or_place 后 nv=false 方可视为完全合格。

## 四、机器可读汇总

```
ROUND=97
SAMPLER=spotcheck-r97
SCOPE=["earth-sheltered","exit-sign"]
READONLY="only wrote research/spotcheck-round97.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={"moesgaard-building":"web_fetch HTTP200","henning-moesgaard":"web_fetch HTTP200","wp-architecture":"web_fetch fail->urllib HTTP200 textlen~65646","wp-sunken-courtyard":"urllib HTTP200 textlen~2355","wp-exit-sign":"web_fetch TypeError->urllib HTTP200 textlen~27046","ecfr-1910-37":"web_fetch blocked redirect->urllib HTTP200 textlen~11583"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}

EARTH_SHELTERED={
 "verdict":"合格",
 "change":"definition 土体覆盖、融入坡地 -> 土体/植被覆盖、嵌入坡地；待核实 由『土体保温隔热热工机制未逐字直证』->『暂无已知待核实项』；nv true->false；pending 清空",
 "thermal_residue":{"terms":"保温|隔热|热工|thermal|insulat|蓄热|恒温|temperature|energy","entry_hits":0,"site_hits":0},
 "concept_support":{
   "屋顶覆土植被":"henning-moesgaard 'sloping roof, landscaped with grass and moss'; moesgaard-building NONE; wp-architecture 弱/泛; wp-sunken-courtyard NONE",
   "嵌入坡地":"henning-moesgaard 'nestled into the rolling landscape of southern Aarhus'; moesgaard 部分(staggered levels); wp 弱",
   "天窗引光":"henning-moesgaard 'light well apertures...allow natural light into the exhibition spaces below' ONLY; moesgaard-building NONE; wp NONE"
 },
 "instance_four_elements":{"name":"莫斯高博物馆/Moesgaard Museum","place":"丹麦奥胡斯南部","designer":"Henning Larsen Architects","year":"2014开馆(2009-2014)","dual_source":"moesgaard-building + henning-moesgaard 均直证"},
 "fabricated":false,
 "nv_false_grounded":true,
 "form_consistency":"nv=false / pending='' / 待核实=暂无 / coverage_count=0 四处一致; check.py D14 PASS",
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"reg_sentence":true,"site_consistent":true},
 "similarity":{"threshold":0.54,"short_nn":"raised-floor","short":0.3735,"full_nn":"minimalism-architecture","full":0.3754,"lt_0.54":true},
 "caveat":"概念物理做法(覆土植被/天窗引光)实为 henning-moesgaard 官方单源直证；moesgaard-building 仅覆盖实例四要素，不含草皮/采光井描述——非严格双源；按『强权威官方源直证+第二源覆盖实例结构』口径成立 nv=false"
}

EXIT_SIGN={
 "verdict":"待核实",
 "change":"仅 nv true->false / 待核实节清空 / pending 清空；time_or_place 未改（残留）",
 "concept_dual_source":{"platforms":["Wikipedia wp-exit-sign","US eCFR 29 CFR 1910.37"],
   "方向":"wp 'direction of emergency exits' + ecfr 'direction of travel to nearest exit'",
   "位置":"wp 'identify exit' + ecfr 'marked by sign reading Exit'",
   "照明/可见":"wp 'always lit/constantly lit/understandable by anyone who can see' + ecfr 'illuminated >=5 foot-candles/line-of-sight clearly visible'",
   "holds":true},
 "body_year_claim_sections":"NONE (实例年份=不适用)",
 "time_or_place_residual":{"value":"近现代（具体年代与制度化沿革待核实，参见来源）。","contains_pending":true,"unique_among_258":true,"contradicts":"nv=false & 待核实=暂无；页面『时间与位置』可见","check_py_catches":false,"note":"check.py D14 仅扫 sections，不扫 time_or_place"},
 "fabricated":false,
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"reg_sentence":true,"site_consistent":true},
 "similarity_vs_evacuation_route":{"threshold":0.54,"short":0.2571,"full":0.3566,"reverse_full":0.3713,"lt_0.54":true},
 "must_fix":"将 time_or_place 改为『近现代（参见来源）。』或据实重写，使 nv=false 与页面自洽；否则恢复披露"
}

SIMILARITY_METHOD={"lib":"difflib.SequenceMatcher","norm":"strip-all-whitespace+lower","selfcheck_futurism_expressionism":0.5157,"entries":258,"library_full_pairs_gt_0.54":0,"library_full_max":"spatial-sequence<->atrium-architecture ~0.5256"}

VERDICT={"earth-sheltered":"合格","exit-sign":"待核实"}
KEY_FINDING="earth-sheltered: 保温/隔热无源claim已彻底清零(entry+site 0命中)，实例四要素moesgaard-building+henning-moesgaard双源，结构/相似度全过；但概念物理做法『覆土植被/天窗引光』实为henning-moesgaard官方单源直证，moesgaard-building页面不含草皮/采光井描述(须指出，非严格双源)。exit-sign: 概念由wp-exit-sign+ecfr-1910-37双平台双源成立、六节正文无年代claim、实例不编造、相似度合格；但time_or_place仍残留『具体年代与制度化沿革待核实』(258条中唯一)，与nv=false/待核实=暂无自相矛盾且页面可见，round97清除不彻底(check.py D14不扫time_or_place)，须清理后方为完全合格。"
```

## 五、只读核验

- 除本报告 `research/spotcheck-round97.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 六个来源本轮均实抓回读（moesgaard-building / henning-moesgaard = web_fetch HTTP200；wp-architecture / wp-sunken-courtyard / wp-exit-sign / ecfr-1910-37 = urllib HTTP200）；相似度与结构数据用内存态 `python - <<` 直跑，无临时文件。
- 联网页面（含 `ecfr.gov` 重定向、Wikipedia）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**。
- `check.py` 与 `pytest` 均以 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存。
- `git status` 中 `M coverage.json / M entries/batch-25.json / M entries/batch-38.json / M site/entries/earth-sheltered.html / M site/entries/exit-sign.html / M site/index.html` 及 `?? tools/apply_review_round97.py` 均为**修复方（round97 applier＋gen_site）自身产物**，抽检方仅读取、未据以修改。

*（报告完）*
