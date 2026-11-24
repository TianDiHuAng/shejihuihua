# 第94轮 three-point-perspective 抽检报告（spotcheck-round94）

- 抽检人：spotcheck-r94（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论）。
- 抽检对象（1 条）：`three-point-perspective`（三点透视，L2/重要/理论/20世纪/欧洲）
  - 条目：`entries/batch-01.json` 第311–344行（`id` 第312行；`definition` 第319行；`sources` 第325–330行；`sections.实例` 第336行）。
  - 覆盖：`coverage.json` 第57–69行（`source_count=4`、`needs_verification_count=0`、`last_updated=2026-11-24`）。
  - 来源定义：`data/sources.json` — `db-quaglio` 第4311–4322行、`wp-quaglio` 第4323–4334行（均 `verified=true`、`link_ok=null`）。
  - 产物：`site/entries/three-point-perspective.html`（28行，与条目一致）。
- 本轮（94）变更（据 `tools/apply_review_round94.py` 实读 + `git diff` 实读 + 当前文件实读）：
  - `needs_verification`：`true`→`false`；`pending_notes`：`原拟仰视摩天楼具名照片缺双源直证，改选夸廖舞台设计；实例已双源。`→`""`。
  - `sections.待核实`：`原拟仰视摩天楼具名照片缺双源直证，改选夸廖舞台设计；实例已双源。`→`暂无已知待核实项。`。
  - `coverage.json`：该条 `needs_verification_count` 1→0；`site/index.html` 顶部统计「待核实条目」163→162。
  - 注：`definition`/`overview`/`sections.实例` 文本本轮**未改**；本轮只把 nv 置 false 并清空待核实。
- 证据优先级：**独立实抓正文 > 当前文件实读 > git diff > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round94.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式（本轮实抓）：
  - `wp-quaglio` = `https://en.wikipedia.org/wiki/Giuseppe_Quaglio` → `web_fetch` **FAIL（TypeError: fetch failed）**；改用 Python urllib + 浏览器 UA → **HTTP 200**，`len=105288`，页面标题 `Giuseppe Quaglio - Wikipedia`。
  - `db-quaglio` = `https://www.deutsche-biographie.de/116317094.html?language=en` → `web_fetch` **HTTP 200**（正文可读，Deutsche Biographie「Quaglio, Giuseppe」条目，作者 Peter Prange，NDB 21 (2003) S.30–31）。
  - 定义旁证：`wp-perspective-graphical` = `https://en.wikipedia.org/wiki/Perspective_(graphical)` → urllib **HTTP 200**，`len=417463`，含 `three-point` 3 次（「Examples of three-point perspective」小节）；`wp-curvilinear-perspective` → urllib **HTTP 200**，`len=146792`，含 `three-point perspective` 图注 1 处。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed`（EXIT=0）。**
- `git status --porcelain`（实读）：`M coverage.json / M entries/batch-01.json / M site/entries/three-point-perspective.html / M site/index.html` 及 `?? tools/apply_review_round94.py` 均为**修复方（round94 applier＋gen_site）自身产物**，非本抽检所写；抽检方仅读取。

## 一、复核 definition（三点透视＝垂直线汇聚到第三（垂直）消失点）

- 端内 `definition`：`在两点透视基础上加入垂直方向灭点的透视方法。`
- 端内 `原理`：`在左右两灭点之外再补一个垂直方向的灭点，画面便获得仰视或俯视的强透视，即三点透视。`
- 端内 `overview`：`用于仰视高层建筑或俯视深井式空间，垂直线随之收敛。`

| 核对点 | 端内表述 | 判定 |
| --- | --- | --- |
| 是否有第三个灭点 | 「再补一个垂直方向的灭点」「三条棱线分别指向三个灭点」 | ✓ 含第三灭点 |
| 该灭点方向为「垂直」 | 「垂直方向灭点」「垂直线随之收敛」 | ✓ 垂直方向 |
| 垂直棱线是否汇聚到该点 | 原理「画面获得仰视或俯视」＋overview「垂直线随之收敛」 | ✓ 语义等价「垂直线汇聚第三消失点」 |
| 定义来源 | `wp-perspective-graphical`（Wikipedia）含「three-point perspective」小节；`wp-curvilinear-perspective` 有三点透视图注 | ✓ 概念有源 |

**判定（definition）：** 端内定义与「三点透视＝垂直线汇聚到第三（垂直）消失点」**一致，非错**；措辞以「垂直方向灭点＋垂直线收敛」表达，语义等价。定义的一般性支撑来自 `wp-perspective-graphical`／`wp-curvilinear-perspective`（均 Wikipedia），**非**本轮两个 Quaglio 源；本轮 Quaglio 双源服务于 `sections.实例`，不涉及定义。

## 二、复核实例四要素（夸廖《Die Weihe》舞台设计，慕尼黑国家剧院，1818）

端内 `sections.实例`：`名称：《Die Weihe》舞台设计；地点：德国慕尼黑国家剧院；设计者：朱塞佩·夸廖（Giuseppe Quaglio）；年份：1818 年（该剧院开幕演出）。被同时代人称为“三点透视”的发明。此处仅列名称、地点、设计者与年份信息，不复制图像。`

| 四要素 | wp-quaglio（实抓 HTTP200） | db-quaglio（实抓 HTTP200） | 判定 |
| --- | --- | --- | --- |
| **名称《Die Weihe》** | `for the festival performance of Die Weihe by Friedrich Albert Klebe` | `für die Festaufführung von A. Klebes „Weihe"` | 双证 ✓（DB 作「Weihe」，WP 作「Die Weihe」；端内取 WP 全称，可） |
| **地点·慕尼黑国家剧院** | `which opened the National Theatre in Munich` | `mit der 1818 das Nationaltheater eröffnet wurde`（传主活动地 München） | 双证 ✓ |
| **设计者·朱塞佩·夸廖** | 条目即 Giuseppe Quaglio，为其所作舞台布景 | 传主 Giuseppe Quaglio，Bühnenbild | 双证 ✓ |
| **年份·1818** | `(1818)`（National Theatre 开幕） | `1818 das Nationaltheater eröffnet wurde` | 双证 ✓ |
| **「被同时代人称为三点透视的发明」** | `His contemporaries credited Giuseppe with inventing what was known as three-point perspective` | `Seinen Zeitgenossen galt Q. als Erfinder der sog. Dreipunktperspektive` | 双证（字面均直述）✓ |

**判定（实例四要素）：** 名称/地点/设计者/年份四要素在**两页面上均被直接标明**；「被同时代人称为『三点透视』的发明」一句在**两页面均有字面对应**（WP `credited ... inventing ... three-point perspective`；DB `galt ... als Erfinder der sog. Dreipunktperspektive`）。端内以「被同时代人称为…发明」表述（而非断言其人真为发明者），与两源「同时代人认为/credited」的口径一致——**四要素成立、表述不越界**。

## 三、★关键：db-quaglio 与 wp-quaglio 是否「双独立平台」——不成立（同源）

此节为本轮抽检的核心。表面上两源分属两个域名（`deutsche-biographie.de` 与 `en.wikipedia.org`），但**证据显示二者源自同一权威文本，不构成两独立源**。

**证据 A — Wikipedia 的参考文献直接列出 db-quaglio 所载的同一 NDB 文章：**
- `wp-quaglio` 参考文献（实抓尾部）：`Peter Prange (2003). "Quaglio, Giuseppe". Neue Deutsche Biographie (in German). Vol. 21. Berlin: Duncker & Humblot. pp. 30–31. (full text online).`
- `db-quaglio` 页面署名与出处（实抓）：`Author: Peter Prange`；引文 `Prange, Peter, "Quaglio, Giuseppe (Joseph)" in: Neue Deutsche Biographie 21 (2003), S. 30-31 [online version]`。
- → **完全同一篇文献**：Neue Deutsche Biographie（NDB）第21卷（2003），作者 Peter Prange，第30–31页。`db-quaglio` 就是该 NDB 文章的 Deutsche Biographie 在线版；`wp-quaglio` 把该 NDB 文章列为主要参考文献（并标注 `full text online`）。

**证据 B — Wikipedia 相关句子是 NDB 德文的近乎逐句英译：**
- DB：`Seinen Zeitgenossen galt Q. als Erfinder der sog. Dreipunktperspektive, doch war diese bereits in verschiedenen Publikationen der Galli-Bibiena ... bekannt gemacht worden.`
- WP：`His contemporaries credited Giuseppe with inventing what was known as three-point perspective; in fact he borrowed it from the Galli da Bibiena, Bolognese stage designers, pictures of whose sets had been published in a book of engravings (Augsburg, 1740)...`
- DB：`für die Festaufführung von A. Klebes „Weihe", mit der 1818 das Nationaltheater eröffnet wurde.`
- WP：`for the festival performance of Die Weihe by Friedrich Albert Klebe, which opened the National Theatre in Munich (1818).`
- → 句式、信息点、甚至「borrowed it from the Galli da Bibiena」这一转折均与 NDB 德文一一对应，属**翻译式衍生**，非独立撰写。传记段（Laino 出生、Vienna 学艺、1771 Mannheim、1778 赴 München、1801 继兄职、1823 退职）亦与 NDB 段落逐条对应。

| 维度 | 结论 |
| --- | --- |
| 是否同一域名/同一网站 | 否（deutsche-biographie.de vs en.wikipedia.org） |
| 是否同一**底层权威来源** | **是**：Neue Deutsche Biographie 21 (2003), Peter Prange, S.30–31 |
| Wikipedia 是否把该 NDB 文章列为主要参考 | **是**（`full text online`，指向 Deutsche Biographie） |
| 相关句是否为 NDB 德文的逐句英译 | **是**（措辞/信息点一一对应） |
| 是否构成「两独立平台直证」 | **否——同源衍生，不独立** |

**特别判断（关键项）：** 本轮把 nv 由 true 置为 false 的**唯一理由**是「db-quaglio 与 wp-quaglio 双独立平台均直述三点透视发明/1818」。但两源实为**同一 NDB 文章的两个载体**（Wikipedia 是 Deutsche Biographie/NDB 文章的翻译与引用），**不是两个独立来源**。因此「双独立平台」前提**不成立**。

> 与第93轮的区别（说明为何不能套用旧口径）：round93 的 Wikipedia 与 Art in Context 是**两家不同出版方、内容各自撰写**（措辞、举例均不同：WP 举 Wasit/Samarra，AIC 举 Kufa/Fustat 56×53m），故判两独立平台。本轮 Wikipedia 的对应句是 Deutsche Biographie/NDB 文章的**翻译复制**并直接引用该文，属「同一来源的再发布」，**不能**算作第二独立源。

**其余两源说明：** `sources` 另有 `wp-perspective-graphical`、`wp-curvilinear-perspective`，二者支撑的是**三点透视的一般定义/图例**（见第一节），**不涉及**「夸廖＝发明者、1818 国家剧院」这一实例命题。故针对**实例/发明命题**，独立权威来源实际只有 **1 个（NDB）**。

## 四、复核「是否编造」

- **具名事实未杜撰**：名称（Die Weihe / Weihe）、地点（慕尼黑国家剧院）、设计者（Giuseppe Quaglio）、年份（1818）均与两源实抓一致；未复制图像（正文自述「不复制图像」）。
- **一处口径正确**：端内「被同时代人称为『三点透视』的发明」与两源「同时代人认为/credited」一致；两源并补充「实为借自 Galli-Bibiena」，端内未把「发明」写成既成事实，属**诚实的归属表述**，非编造。
- **一处轻微出入（非编造）**：DB 作「A. Klebes ‚Weihe‛」，WP 作「Die Weihe by Friedrich Albert Klebe」；端内取「《Die Weihe》」与 WP 全称一致，可接受。
- **编造 = 无。**

## 五、复核七节 / SVG / 规范句 / 结构校验

| 核对项 | three-point-perspective | 说明 |
| --- | --- | --- |
| 七节齐 | ✓ | definition+overview + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实（check.py 6 节全非空 PASS） |
| SVG 数量/画布 | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」 | L2 → 1–2 张 |
| SVG 越界/禁用元素 | ✓ | path `M300 300 L300 120 L460 100 L460 270 Z`（x300–460 / y100–300）；line 到 `380,40` 与 `460,100`；text `350,30`、`300,370`——全在 0..760 / 0..400；无 `<image>`/外链；pytest `5 passed` |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」，另页脚 note 亦有 |
| 形式四处自洽 | ✓（但实质不成立，见第三/八节） | `needs_verification=false`、`pending_notes=""`、`sections.待核实="暂无已知待核实项。"`、`coverage needs_verification_count=0` 四处一致；check.py D14 一致性 PASS（**仅校形式一致，不校实质来源独立性**） |
| 来源数/双源规则 | ⚠ 页面数 4，独立权威源（对实例命题）实为 1 | check.py ≥2 规则 PASS 系按 sources 数量；实例命题的 NDB＋Wikipedia 同源（见第三节） |
| site 渲染一致 | ✓ | `site/entries/three-point-perspective.html` 含 definition/实例/规范句/「暂无已知待核实项」各 1 次；来源列 4 条（WP-perspective/WP-curvilinear/DB/WP-Quaglio）；`viewBox 0 0 760 400`×1；`示意图，非施工图`×2（SVG+figcaption） |
| 首页统计一致 | ✓ | `site/index.html`「待核实条目」163→162，与本次 nv true→false 相符 |
| check.py | ✓ | `PASS: all checks, 0 errors`（EXIT=0） |
| pytest svg | ✓ | `5 passed`（EXIT=0） |

**附加观察（口径，非本轮主因）：** 端内 `period="20世纪"`、`time_or_place="20世纪（参见来源）"`，但两 Quaglio 源显示三点透视的实践可上溯至 Galli-Bibiena（18 世纪上半叶）与 1818 年（19 世纪）——**「20世纪」的断代与所引来源不符**，属超源/断代问题，建议一并核对。

## 六、复核相似度（阈值 0.54，vs one-point / two-point perspective）

方法：`difflib.SequenceMatcher`，归一化＝**去全部空白＋小写**（与 round86–93 一致）。全库条目 **258 条**。

| 口径 | vs one-point | vs two-point | vs curvilinear | 全库最高 | 阈值 | 判定 |
| --- | --- | --- | --- | --- | --- | --- |
| 短口径（title\|definition\|time_or_place\|overview） | 0.3840 | 0.2642 | 0.3902 | 0.3902（curvilinear） | <0.54 | ✓ |
| def+overview | 0.2727 | 0.1930 | 0.2366 | 0.2727（one-point） | <0.54 | ✓ |
| 全字段（短＋6节） | 0.3711 | 0.3027 | 0.2872 | 0.3711（one-point） | <0.54 | ✓ |

- 与 one-point / two-point 三口径均显著低于 0.54（余量最小处 full vs one-point = 0.3711，距阈值 0.1713）。**相似度：合格 ✓。**
- 全库两两比对（258 条）：短口径 >0.54 **0 对**（max serial-route↔radial-route 0.4960）、def+overview >0.54 **0 对**（max leaked-scenery↔time-scenery 0.4121）、全字段 >0.54 **0 对**（max loop-route↔serial-route 0.5259）——**全库无 >0.54 对**。

## 七、单源 / 超源 / 编造支撑表

| 要点 | 支撑情况 | 判定 |
| --- | --- | --- |
| 三点透视定义（垂直线→第三灭点） | 端内表述自洽；旁证 `wp-perspective-graphical`（含 three-point 小节）/`wp-curvilinear-perspective` | 概念有源 ✓ |
| 实例四要素（名/地/设计者/年份） | WP＋DB **两页面均直述**（但同源，见下行） | 字面双证；独立性存疑 |
| 「同时代人称夸廖为三点透视发明者」 | WP `credited ... inventing ... three-point perspective`＋DB `galt ... als Erfinder der sog. Dreipunktperspektive` | 字面双证、口径诚实（均注「实借自 Galli-Bibiena」）|
| 1818 慕尼黑国家剧院开幕 | WP `opened the National Theatre in Munich (1818)`＋DB `1818 das Nationaltheater eröffnet` | 字面双证 |
| **两源独立性** | **同源**：WP 引用的正是 DB 所载 NDB 21(2003) Peter Prange S.30–31，且为德文逐句英译 | **不独立 ✗** |
| `nv=false` 依据 | 依赖「双独立平台」；实为单一 NDB 来源 | **依据不足 ✗** |
| 编造具名事实 | 名称/地点/年代未杜撰；未复制图像 | 无编造 ✓ |
| 断代 period/time_or_place | 「20世纪」与来源（18–19 世纪）不符 | 超源（附带）⚠ |

## 八、结论

### 总判定：**不合格**（本轮 `nv=false` 升级不成立）

**依据（分层）：**

1. **定义正确、实例四要素字面有据、无编造** — `definition` 与「垂直线汇聚到第三（垂直）消失点」一致；实例名/地/设计者/年份在 WP 与 DB 均被直接标明；「被同时代人称为三点透视的发明」两页均有字面对应且口径诚实（同时点明「实借自 Galli-Bibiena」）；无杜撰具名事实、未复制图像。

2. **★核心缺陷：db-quaglio 与 wp-quaglio 不独立，同源衍生** — `db-quaglio` 即 Deutsche Biographie 所载 **Neue Deutsche Biographie 21 (2003), Peter Prange, S.30–31** 一文；`wp-quaglio` 的参考文献**直接列出同一篇 NDB 文章**（`full text online`），且其对应句是该 NDB 德文的**近乎逐句英译**（见第三节证据 A/B）。故二者是「同一权威文本的两个载体」，**不构成两独立平台**。nv=false 的唯一依据「双独立平台」**不成立**。

3. **独立权威源实际为 1（NDB）** — 另两个源（`wp-perspective-graphical`、`wp-curvilinear-perspective`）只支撑三点透视的一般定义，**不支撑**「夸廖＝发明者/1818 国家剧院」这一实例命题。按 D10「关键事实双源或标待核实」，此实例命题应维持**待核实**，而非 nv=false。

4. **结构与相似度全绿（但不救 nv）** — 七节齐、SVG 1 张（`viewBox 0 0 760 400`、元素全在框内、无禁用外链）、规范句在、形式四处一致（仅形式）、site 渲染一致、首页 163→162、`check.py PASS: all checks, 0 errors`、`pytest 5 passed`、相似度 vs one-point/two-point 三口径 0.3840/0.2727/0.3711 与 0.2642/0.1930/0.3027 均 <0.54（全库 >0.54 对 = 0）。**结构合格，但这只是形式校验，不能证明实例命题的双源独立性。**

5. **附带问题：断代** — `period="20世纪"`、`time_or_place="20世纪（参见来源）"` 与两源所示「18 世纪上半叶 Galli-Bibiena 已知 / 1818 年夸廖应用」**不符**，属超源，建议一并修正。

**建议修复（供修复方参考）：**
- 将 `needs_verification` 回退为 `true`，`pending_notes`／`sections.待核实` 写明：实例「夸廖＝三点透视发明者、1818 国家剧院」现为**单一权威源（NDB 21, 2003, Peter Prange）**，Wikipedia 为其译本/再发布，非独立第二源，**待补真正独立的第二来源**（如独立的艺术史专著、博物馆/剧院官方档案）。
- 或：若坚持 nv=false，须找到**独立于 NDB/Deutsche Biographie 且独立于其维基译本**的第二来源并落实引证。
- 顺带核对并修正 `period`/`time_or_place` 的「20世纪」断代。

> 一句话：**「被同时代人称为三点透视发明者 / 1818 慕尼黑国家剧院」在两页面均有字面直述、实例四要素无编造；但 `wp-quaglio` 正是 `db-quaglio`（NDB 21, 2003, Peter Prange, S.30–31）的翻译与引用，两「源」同源衍生、并非两独立平台——故本轮 `nv=false`「双独立平台」前提不成立，判「不合格」；应回退为待核实，直至补到真正独立的第二来源。**

## 九、机器可读汇总

```
ROUND=94
SAMPLER=spotcheck-r94
SCOPE=["three-point-perspective"]
WEB_FETCH={"wp-quaglio":"web_fetch direct FAIL(fetch failed) -> urllib HTTP200 len=105288 title='Giuseppe Quaglio - Wikipedia'","db-quaglio":"web_fetch HTTP200 (Deutsche Biographie Quaglio, Giuseppe; NDB 21(2003) Peter Prange S.30-31)","wp-perspective-graphical":"urllib HTTP200 len=417463 three-point hits=3","wp-curvilinear-perspective":"urllib HTTP200 len=146792 three-point hits=1"}
DB_QUAGLIO={"url":"https://www.deutsche-biographie.de/116317094.html?language=en","article":"Neue Deutsche Biographie 21 (2003), Peter Prange, S.30-31","quotes":["Seinen Zeitgenossen galt Q. als Erfinder der sog. Dreipunktperspektive, doch war diese bereits in verschiedenen Publikationen der Galli-Bibiena ... bekannt gemacht worden.","für die Festaufführung von A. Klebes 'Weihe', mit der 1818 das Nationaltheater eröffnet wurde."],"states_three_point=true,"states_1818_nationaltheatre=true,"states_die_weihe=true}
WP_QUAGLIO={"url":"https://en.wikipedia.org/wiki/Giuseppe_Quaglio","quotes":["His contemporaries credited Giuseppe with inventing what was known as three-point perspective; in fact he borrowed it from the Galli da Bibiena ...","for the festival performance of Die Weihe by Friedrich Albert Klebe, which opened the National Theatre in Munich (1818)."],"states_three_point=true,"states_1818_nationaltheatre=true,"states_die_weihe=true,"references":["Bryan 1889","Quinzi 2016 (DBI)","Peter Prange (2003). 'Quaglio, Giuseppe'. Neue Deutsche Biographie Vol.21. Berlin: Duncker & Humblot. pp.30-31. (full text online)."]}
INDEPENDENCE={"same_underlying_source":true,"underlying":"Neue Deutsche Biographie 21 (2003), Peter Prange, S.30-31","wp_cites_db_ndb":true,"wp_is_translation_of_db":true,"two_independent_platforms":false,"distinct_authorities_for_instance_claim":1}
INSTANCE_FOUR_ELEMENTS={"name":"Die Weihe (WP) / Weihe (DB)","place":"National Theatre in Munich","designer":"Giuseppe Quaglio","year":"1818","all_directly_stated_both_pages":true}
DEFINITION={"entry":"在两点透视基础上加入垂直方向灭点的透视方法。","matches_three_point_vertical_vp":true,"supported_by":"wp-perspective-graphical + wp-curvilinear-perspective (general)"}
FABRICATED_NAMED=false
NV_FALSE_GROUNDED=false
FORM_FOUR_WAY_CONSISTENT=true
PERIOD_ISSUE="period/time_or_place='20世纪' 与来源(18-19世纪)不符 -> 超源(附带)"
STRUCTURE={"seven_sections":true,"svg_count":1,"svg_viewBox":"0 0 760 400","svg_forbidden":"none","reg_sentence":true,"site_html_consistent":true,"index_stat":"163->162","check_py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
SIMILARITY={"threshold":0.54,"entries":258,"normalization":"strip-all-whitespace+lower",
 "vs_one_point":{"short":0.3840,"defov":0.2727,"full":0.3711},
 "vs_two_point":{"short":0.2642,"defov":0.1930,"full":0.3027},
 "vs_curvilinear":{"short":0.3902,"defov":0.2366,"full":0.2872},
 "target_top":{"short":{"max":0.3902,"nn":"curvilinear-perspective"},"defov":{"max":0.2727,"nn":"one-point-perspective"},"full":{"max":0.3711,"nn":"one-point-perspective"}},
 "library":{"short":{"max":"serial-route<->radial-route 0.4960","pairs_gt":0},"defov":{"max":"leaked-scenery<->time-scenery 0.4121","pairs_gt":0},"full":{"max":"loop-route<->serial-route 0.5259","pairs_gt":0}}}
COVERAGE={"three_point_perspective":{"source_count":4,"needs_verification_count":0}}
VERDICT={"three-point-perspective":"不合格"}
KEY_FINDING="实例四要素(Die Weihe/慕尼黑国家剧院/夸廖/1818)与'同时代人称为三点透视发明者'在两页面均字面直述、无编造；但db-quaglio即Deutsche Biographie所载NDB 21(2003) Peter Prange S.30-31一文，wp-quaglio的参考文献直接列出同一NDB文章(full text online)且相关句为德文逐句英译——两源同源衍生、非两独立平台。独立权威源对实例命题实为1(NDB)，另两源仅支撑一般定义。故nv=false'双独立平台'前提不成立->不合格，应回退待核实并补真正独立第二源；附带period='20世纪'与来源18-19世纪不符。结构:七节/SVG(760x400)/规范句/site一致/首页163->162/check.py PASS/pytest 5 passed/相似度vs one-point|two-point 0.3840|0.2727|0.3711 与 0.2642|0.1930|0.3027 均<0.54(全库>0.54对=0)。"
READONLY="only wrote research/spotcheck-round94.md; wp-quaglio web_fetch failed -> urllib HTTP200; db-quaglio web_fetch HTTP200; perspective/curvilinear urllib HTTP200; git M/?? items are round94 applier+gen_site changes; no git commit; web treated as data, no instructions executed"
```

## 十、只读核验

- 除本报告 `research/spotcheck-round94.md` 外未写任何文件；`wp-quaglio`/`db-quaglio`/`wp-perspective-graphical`/`wp-curvilinear-perspective` 均用 Python urllib（浏览器 UA）实抓（全 HTTP 200；`web_fetch` 仅 `db-quaglio` 直连 200，`wp-quaglio` 直连失败后改用 urllib）；无落盘临时文件；相似度计算用 `python - <<` 内存态直跑（无临时文件）。
- `git status` 中 `M coverage.json / entries/batch-01.json / site/entries/three-point-perspective.html / site/index.html` 及 `?? tools/apply_review_round94.py` 均为**修复方（round94 applier + gen_site）的应用产物**；抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- `check.py` 与 `pytest` 均以 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存文件。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
