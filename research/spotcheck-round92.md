# 第92轮 mexican-baroque 抽检报告（spotcheck-round92）

- 抽检人：spotcheck-r92（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论）。
- 抽检对象（1 条）：`mexican-baroque`（墨西哥巴洛克／新西班牙巴洛克，L2/补充/风格/文艺复兴至19世纪/美洲）
  - 条目：`entries/batch-30.json` 第5–37行（条目内 `id` 位于第6行）。
  - 覆盖：`coverage.json` 第3151–3163行（`source_count=2`、`needs_verification_count=0`、`last_updated=2026-11-24`）。
  - 来源定义：`data/sources.json` 第3003–3014行（`wp-new-spanish-baroque`）、第3015–3026行（`designingbuildings-baroque`），两源均 `verified=true`、`link_ok=null`。
  - 产物：`site/entries/mexican-baroque.html`（27行，与条目一致）。
- 本轮（92）变更（据 `tools/apply_review_round92.py` 实读 + `git diff` 实读 + 当前文件实读）：
  - `definition`：「墨西哥巴洛克是新西班牙（今墨西哥）在殖民时期发展出的巴洛克建筑与艺术，装饰繁复、色彩浓烈。」→「墨西哥巴洛克（新西班牙巴洛克）是新西班牙（今墨西哥）在殖民时期发展出的巴洛克建筑与艺术，装饰繁复、色彩浓烈，**典型子风格为 Churrigueresque**。」
  - `overview`：「…最典型的子风格是装饰密集的 Churrigueresque。」→「它把欧洲巴洛克与本土工艺结合，以密集的灰泥雕刻与强烈色彩装饰教堂；**作为地区子风格，不归于单一设计者**。」
  - `sections.实例`：类型性表述升级为「新西班牙巴洛克教堂（类型性，地区子风格不归于单一设计者）；地点：墨西哥；以繁复立面与 Churrigueresque 装饰为特征。此处仅列说明，不复制图像。」
  - `needs_verification`：`true`→`false`；`pending_notes`：「「墨西哥巴洛克」的具体实例…待补充独立来源。」→`""`；`sections.待核实`：「具体教堂的设计者与年代待补充独立来源。」→「暂无已知待核实项。」
  - `coverage.json`：该条 `needs_verification_count` 1→0（`source_count` 仍 2）。sources 未变（仍 `wp-new-spanish-baroque` / `designingbuildings-baroque`）。
- 证据优先级：**独立实抓正文 > 当前文件实读 > git diff > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round92.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式（本轮实抓）：
  - `designingbuildings-baroque` = `https://www.designingbuildings.co.uk/wiki/Baroque_architecture` → **web_fetch HTTP 200**，页面标题 `Baroque architecture - Designing Buildings`，出版方 Designing Buildings Ltd（英国建筑知识维基），`Last edited 15 Nov 2021`。
  - `wp-new-spanish-baroque` = `https://en.wikipedia.org/wiki/New_Spanish_Baroque` → **web_fetch 直连失败（TypeError: fetch failed）**；改抓 **owiki 镜像 `https://owiki.org/wiki/New_Spanish_Baroque` → HTTP 200**，标题 `New Spanish Baroque ::: Open WIKI`，正文与条目「New Spanish Baroque / Mexican Baroque / New Spain / Churrigueresque」一致。canonical 直连待复（与 sources.json note「经 owiki 镜像/独立站点实抓核对…canonical 直连待复」一致）。
- 关键实抓原句（去标签后回读）：
  - **WP（New Spanish Baroque，owiki 200）**：
    - `New Spanish Baroque, also known as Mexican Baroque, refers to Baroque art developed in the entire territories that once formed the Viceroyalty of New Spain.`
    - `...reflect the expressiveness and the colour contrasts characteristic of New Spanish Baroque.`
    - `Two styles can be traced in the architecture of New Spain: the Salomónico, developed from the mid-17th century, and the Estípite, which began in the early 18th century.`
    - `The most emblematic substyle of Mexican Baroque architecture is Churrigueresque.`
    - 例证：`A model of the Cathedral of Puebla...`；`the Altarpiece of the Kings in the Metropolitan Cathedral of Mexico City built and hand-carved by Jerónimo de Balbas in 1736`。
  - **DB（Baroque architecture，designingbuildings 200）** 与 Churrigueresque 相关**仅一句**：
    - `The late Baroque style is often referred to as Rococo or, in Spain and Spanish America, as Churrigueresque.`
    - 另有一句泛述：`...in some regions, notably Germany and colonial South America, it lasted until the 18th century.`（提及 colonial South America，**未提墨西哥/新西班牙**）
    - 其余为通论巴洛克特征（dynamic designs、curves and twists、Rich surface treatments、Gilded statuary、Bright colours、plaster/stucco 等），**全篇无 `Mexico`/`New Spain`/`Mexican Baroque` 字样**。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed`（EXIT=0）。**
- `git status --porcelain`（实读）：`M coverage.json / M entries/batch-30.json / M site/entries/mexican-baroque.html / M site/index.html` 及 `?? tools/apply_review_round92.py` 均为**修复方（round92 applier）自身产物**，非本抽检所写；抽检方仅读取。

## 一、复核 definition/overview 是否由两源支撑（新西班牙/墨西哥殖民巴洛克、装饰繁复、Churrigueresque）

端内 definition：`墨西哥巴洛克（新西班牙巴洛克）是新西班牙（今墨西哥）在殖民时期发展出的巴洛克建筑与艺术，装饰繁复、色彩浓烈，典型子风格为 Churrigueresque。`
端内 overview：`它把欧洲巴洛克与本土工艺结合，以密集的灰泥雕刻与强烈色彩装饰教堂；作为地区子风格，不归于单一设计者。`

| 定义要素 | wp-new-spanish-baroque（实抓） | designingbuildings-baroque（实抓） | 判定 |
| --- | --- | --- | --- |
| **墨西哥巴洛克＝新西班牙巴洛克** | `New Spanish Baroque, also known as Mexican Baroque` | 未提（全篇无 Mexican/New Spain） | **仅 WP 直证** |
| **新西班牙（今墨西哥）殖民时期巴洛克** | `territories that once formed the Viceroyalty of New Spain`；`in Mexico` | 未提（仅泛提 colonial South America） | **仅 WP 直证** |
| **装饰繁复、色彩浓烈** | `expressiveness and the colour contrasts characteristic of New Spanish Baroque`（色泽对比）＋Churrigueresque 繁饰 | 通论巴洛克 `Rich surface treatments / Gilded statuary / Bright colours / plaster,stucco`（**非墨西哥专述**） | WP 直证；DB 仅泛证 |
| **典型子风格为 Churrigueresque** | `The most emblematic substyle of Mexican Baroque architecture is Churrigueresque`（**明确「子风格 substyle」＋「墨西哥」**） | `late Baroque style ... in Spain and Spanish America, as Churrigueresque`（**地区通名/同义名，非「子风格」、不含墨西哥**） | WP 直证；DB **泛化** |

**判定（复核 definition/overview）：** 定义/概述中所有「墨西哥/新西班牙专属性」要素（新西班牙＝墨西哥＝殖民巴洛克、典型子风格为 Churrigueresque）**均由 wp-new-spanish-baroque 单一来源直接支撑**；designingbuildings-baroque **未对任何墨西哥专属要素提供直接支撑**——它只有一句把「西班牙与西属美洲的晚期巴洛克」笼统称为 Churrigueresque，既不含「墨西哥/新西班牙」，也把 Churrigueresque 当作**地区同义名（late Baroque＝Churrigueresque）**而非「墨西哥巴洛克的子风格」。故「两源共同支撑 definition/overview」这一命题**仅在 WP 一源成立**，DB 属泛证/背景性旁证，不构成对墨西哥专属断言的双源直证。

## 二、复核两源是否独立

| 维度 | wp-new-spanish-baroque | designingbuildings-baroque | 是否独立 |
| --- | --- | --- | --- |
| 出版方 | Wikipedia（本轮经 owiki 镜像实抓） | Designing Buildings Ltd（英国建筑知识维基，独立站） | **不同出版方 ✓** |
| 主题层级 | 专门词条：New Spanish / Mexican Baroque | 通论词条：Baroque architecture（全球巴洛克） | 层级不同 |
| 是否讲墨西哥/新西班牙 | **是** | **否**（全篇无 Mexico/New Spain） | — |
| Churrigueresque 表述性质 | 「墨西哥巴洛克最具代表性的**子风格**」 | 「西班牙与西属美洲**晚期巴洛克的通称**」 | 性质/层级不同 |
| 例证 | 普埃布拉主教座堂、墨西哥城主座堂「列王祭坛」（Balbás,1736） | 无墨西哥例证（仅欧洲/圣彼得等） | 不同 |

**判定（复核两源独立性）：** 作为**出版物**，两源确属不同出版方、不同平台、无复制关系，**文献独立性成立 ✓**。但「独立」≠「两源都直接支撑同一墨西哥专属断言」：WP 为墨西哥专属直证，DB 为全球巴洛克通论中的泛证。独立性成立，但**作为「第二直接源」的适配度不足**（见第四节特别判断）。

## 三、复核类型性子风格是否合理 + 是否编造

- **类型性合理（有条件成立）**：把对象表述为「地区子风格（不归于单一设计者）」在方法论上成立——巴洛克地区子风格是群体/地域现象，通常不归于单一设计者。WP 亦以「子风格 substyle」称 Churrigueresque，支持「类型/风格层级」而非「单一设计者」的表述。
- **但属明显欠claim（非超源，非编造）**：WP 其实提供了**可考的具名例证**（普埃布拉主教座堂模型；墨西哥城主座堂「列王祭坛」由 Jerónimo de Balbás 1736 年建造），当前 `实例` 却只写「新西班牙巴洛克教堂（类型性…）」，未采用任何具名实例。此系「宁少不编」的欠claim，安全、不算错，但对 L2 条目而言实例偏空；若日后占用 WP 具名例证，可写「普埃布拉主教座堂／列王祭坛（Balbás, 1736）」。
- **无编造具名事实**：未杜撰设计者/年份/建筑名；未复制图像；「地区子风格不归于单一设计者」为方法论陈述，非具名事实。**编造 = 无。**
- **来源元数据小瑕（非阻断）**：两源 `author` 字段均填「Wikipedia/机构」（模板占位），对 DB（实为 Designing Buildings Ltd）不精确；属元数据粗糙，非内容编造。

## 四、特别判断：DB 的 Churrigueresque 一句是否足以支撑「墨西哥巴洛克＝Churrigueresque 子风格」，能否构成独立第二直接源，还是过泛？

**核心事实（DB 全文唯一相关句）：** `The late Baroque style is often referred to as Rococo or, in Spain and Spanish America, as Churrigueresque.`

逐条比对这句话与端内断言「墨西哥巴洛克…典型子风格为 Churrigueresque」：

| 断言成分 | DB 该句是否支撑 | 说明 |
| --- | --- | --- |
| 主语「墨西哥巴洛克 / 新西班牙巴洛克」 | **否** | DB 全篇无 Mexico / New Spain / Mexican Baroque，主语是「the late Baroque style」全球晚期巴洛克 |
| 范围「墨西哥」 | **否（过泛）** | DB 说的是「Spain and Spanish America」（全西属美洲），非墨西哥专指；对墨西哥只是「包含」而非「直指」 |
| 关系「子风格 substyle」 | **否** | DB 是「…is often referred to as … Churrigueresque」——把 Churrigueresque 当作**晚期巴洛克的地区同义名/别称**，不是「墨西哥巴洛克之下的一个子风格」这一层级关系 |
| 「装饰繁复/色彩浓烈」的墨西哥特征 | **否（泛证）** | DB 通论巴洛克「Rich surface treatments/Bright colours」，非墨西哥专述 |

**判断结论：DB 的这一句「过泛」，不构成「墨西哥巴洛克＝Churrigueresque 子风格」的独立第二直接源。理由三点：**
1. **主体与范围不符**：断言主体是「墨西哥/新西班牙」，DB 句主体是「西班牙与西属美洲的晚期巴洛克」，全篇不含 Mexico/New Spain，无法作为墨西哥专属断言的直接源，只能作全西属美洲的泛化旁证。
2. **关系性质不同**：断言要的是「典型**子风格**（墨西哥巴洛克之下）」，DB 给的是「晚期巴洛克的**地区通称/同义名**」；把「late Baroque in Spanish America = Churrigueresque」外推为「墨西哥巴洛克的子风格是 Churrigueresque」，是**由更宽泛的地区同义名向更窄的子风格层级反推**，属推断而非直证。
3. **单句孤证**：DB 支持 Churrigueresque 的仅此一句，且与墨西哥无直接绑定，不足以承担「第二直接源」之责。

**由此：本轮升级 `nv=false` 所依赖的「概念双源」不成立。** 定义/概述里的墨西哥专属关键事实（新西班牙＝墨西哥＝殖民巴洛克、典型子风格 Churrigueresque）**实际由 wp-new-spanish-baroque 单一直接源承担**；按项目规则 D10「关键事实双源或标待核实」，该关键事实**未达双源**，`nv=false` **依据不足，应回退为待核实（nv=true）**，并在 `pending_notes` 记明「需一条墨西哥/新西班牙专属的第二直接来源（明确称 Churrigueresque 为墨西哥巴洛克子风格）」。

> 备注（对照 WP 强度）：WP 单源其实很强——明确「also known as Mexican Baroque」「Viceroyalty of New Spain」「most emblematic substyle of Mexican Baroque architecture is Churrigueresque」，可**完整**支撑 definition/overview。问题不在 WP，而在把 DB 那句泛化通名当作「第二直接源」来支撑墨西哥专属断言，属**以泛充专**。

## 五、复核七节 / SVG / 规范句 / 结构校验

| 核对项 | mexican-baroque | 说明 |
| --- | --- | --- |
| 七节齐 | ✓ | definition+overview + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实（check.py 校验 6 节全非空 PASS） |
| SVG 数量/画布 | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」 | L2 → 1–2 张 |
| SVG 越界/禁用元素 | ✓ | check.py validate_svg PASS；pytest test_svg_bounds `5 passed`。bbox：外框 rect 120..640 / 120..320；两条 path 落在框内区域；text x=260 y=90、x=300 y=375；全在 0..760 / 0..400 内 |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」，RISK/REGULATION_NOTE 规则通过 |
| 形式四处自洽 | ✓（形式一致，但实质见第四节） | `needs_verification=false`、`pending_notes=""`、`sections.待核实="暂无已知待核实项。"`、`coverage needs_verification_count=0` 四处数值一致；check.py D14 一致性 PASS——**仅形式一致，nv=false 的实质依据不足** |
| 来源数/双源规则 | ✓ 2 源（均 verified） | check.py ≥2 规则通过；但「双源直证墨西哥专属断言」不成立（见第一、四节） |
| site 渲染一致 | ✓ | `site/entries/mexican-baroque.html` 含「典型子风格为 Churrigueresque」「作为地区子风格，不归于单一设计者」「新西班牙巴洛克教堂（类型性，地区子风格不归于单一设计者）」「暂无已知待核实项」各 1 次；`示意图，非施工图`×2；`viewBox 0 0 760 400`×1 |
| check.py | ✓ | `PASS: all checks, 0 errors`（EXIT=0） |
| pytest svg | ✓ | `5 passed`（EXIT=0） |

## 六、复核相似度（阈值 0.54，vs rococo/baroque）

方法：`difflib.SequenceMatcher`，归一化＝**去全部空白＋小写**（与 round86–91 口径一致）。全库条目 **258 条**。

| 口径 | mexican-baroque 全库最高 | vs **rococo** | vs **baroque** | 阈值 |
| --- | --- | --- | --- | --- |
| 短口径（title\|definition\|time_or_place\|overview） | 0.3180 vs **rococo** | **0.3180** | 0.2824 | <0.54 ✓ |
| def+overview | 0.2283 vs latin-american-colonial | 0.0565 | 0.1762 | <0.54 ✓ |
| 全字段（短＋6节） | 0.3171 vs plaza | 0.3045 | 0.2577 | <0.54 ✓ |

- mexican-baroque 所有口径最高 **0.3180**（短口径 vs rococo）< 0.54，**安全 ✓**；与 rococo（0.3180/0.0565/0.3045）、与 baroque（0.2824/0.1762/0.2577）均显著低于阈值。
- 全库两两比对（258 条）本轮：短口径 >0.54 **0 对**（max sunken-accessibility↔accessibility-design 0.5202）、def+overview >0.54 **0 对**（max leaked-scenery↔time-scenery 0.4192）、全字段 >0.54 **0 对**（max loop-route↔serial-route 0.5311）——**全库无 >0.54 对**。**相似度：合格 ✓。**

## 七、单源 / 超源 / 编造支撑表

| 要点 | 支撑情况 | 判定 |
| --- | --- | --- |
| 新西班牙（墨西哥）＝New Spanish/Mexican Baroque | wp-new-spanish-baroque 直证（`also known as Mexican Baroque`、`Viceroyalty of New Spain`）；DB 未提 | **仅单源（WP）** |
| 装饰繁复、色彩浓烈 | WP（`colour contrasts characteristic`）直证；DB 通论巴洛克泛证（非墨西哥） | WP 直证；DB 泛证 |
| 典型子风格为 Churrigueresque | WP 直证（`most emblematic substyle of Mexican Baroque`）；DB 仅泛化同义名（`in Spain and Spanish America, as Churrigueresque`，无墨西哥、无「子风格」） | **WP 直证；DB 过泛，不成第二直接源** |
| 类型性/不归于单一设计者 | 方法论通例；WP 以「substyle」层级亦称支持 | 合理（欠claim，安全） |
| 编造具名事实 | 未写具体设计者/年代；未复制图像 | 无编造 ✓ |
| 两源文献独立性 | Wikipedia(owiki 镜像) vs Designing Buildings Ltd | 独立 ✓（但非「双直接源」） |
| 来源元数据 | 两源 author 均「Wikipedia/机构」占位，DB 实为 Designing Buildings Ltd | 元数据小瑕（非阻断） |

## 八、结论

### 总判定：**待核实**

**依据（分层）：**

1. **内容事实本身：基本准确、无编造（合格层）** — `wp-new-spanish-baroque`（owiki 镜像 HTTP 200）明确「New Spanish Baroque, also known as Mexican Baroque…Viceroyalty of New Spain」「most emblematic substyle of Mexican Baroque architecture is Churrigueresque」，可**完整**支撑 definition/overview；`designingbuildings-baroque`（HTTP 200）中 Churrigueresque 仅一句「in Spain and Spanish America, as Churrigueresque」。实例未编造具名事实（欠claim，安全）；七节齐、SVG 合规（1 张、viewBox 0 0 760 400、bbox 在框内、无禁用元素）、规范句在、site 渲染一致、`check.py PASS`、`pytest 5 passed`、相似度全口径 <0.54（最高 0.3180 vs rococo，全库 >0.54 对 = 0）。

2. **判为「待核实」的决定性理由（来源层，非内容层）** — 本轮把 `nv` 由 `true` 升为 `false`，其唯一依据是「概念双源（WP＋DB）」。但经实抓核对：**DB 的 Churrigueresque 一句过泛**——主体是「西班牙与西属美洲的晚期巴洛克」，全篇**不含墨西哥/新西班牙**，且把 Churrigueresque 当作**地区同义名（late Baroque＝Churrigueresque）**而非「墨西哥巴洛克的子风格」。它**不能构成「墨西哥巴洛克＝Churrigueresque 子风格」的独立第二直接源**。于是 definition/overview 的墨西哥专属关键事实**实际由 WP 单一直接源承担**，未达 D10「关键事实双源」。**因此 `nv=false` 依据不足，应回退为待核实（nv=true）**，或在补充一条**墨西哥/新西班牙专属**的第二直接来源（明确称 Churrigueresque 为墨西哥巴洛克子风格，如艺术史专著/馆方文本）后方可再升 `nv=false`。

3. **形式一致性不等于实质充分** — 当前 `needs_verification=false / pending_notes="" / sections.待核实="暂无已知待核实项。" / coverage needs_verification_count=0` 四处**形式自洽**且 `check.py` D14 一致性通过，但这是「形式一致」，掩盖了「双源不成立」的**实质缺口**；形式合格不能替代来源达标。

> 一句话：**WP 单源把事情说清楚了，DB 只是把「西属美洲晚期巴洛克＝Churrigueresque」泛泛带过，够不上「墨西哥专属」的第二直接源。内容不假，但「已核实（nv=false）」的证据基础不成立，故判「待核实」，建议回退 nv=true 并补一条墨西哥专属直源。**

## 九、机器可读汇总

```
ROUND=92
SAMPLER=spotcheck-r92
SCOPE=["mexican-baroque"]
WEB_FETCH={"designingbuildings-baroque":"web_fetch HTTP200","wp-new-spanish-baroque":"en.wikipedia direct FAIL(fetch failed) -> owiki.org mirror HTTP200"}
WP_NSB={"url":"https://en.wikipedia.org/wiki/New_Spanish_Baroque","mirror":"https://owiki.org/wiki/New_Spanish_Baroque","title":"New Spanish Baroque","quotes":["New Spanish Baroque, also known as Mexican Baroque, refers to Baroque art developed in the entire territories that once formed the Viceroyalty of New Spain.","...reflect the expressiveness and the colour contrasts characteristic of New Spanish Baroque.","The most emblematic substyle of Mexican Baroque architecture is Churrigueresque."],"examples":["Cathedral of Puebla","Altarpiece of the Kings, Metropolitan Cathedral of Mexico City, Jeronimo de Balbas 1736"],"direct_mexico_specific":true}
DB_BAROQUE={"url":"https://www.designingbuildings.co.uk/wiki/Baroque_architecture","publisher":"Designing Buildings Ltd","churrigueresque_sentence":"The late Baroque style is often referred to as Rococo or, in Spain and Spanish America, as Churrigueresque.","mentions_mexico":false,"mentions_new_spain":false,"mentions_mexican_baroque":false,"calls_substyle":false,"generic_regional":true}
DEFINITION_SUPPORT={"mexican_equals_new_spanish_baroque":"WP only","new_spain_mexico_colonial":"WP only","ornate_color":"WP direct + DB generic","churrigueresque_substyle":"WP direct + DB over-generic","concept_dual_direct_source":false}
SOURCES_INDEPENDENT_AS_PUBLICATIONS=true
DB_AS_SECOND_DIRECT_SOURCE=false
DB_TOO_GENERIC=true
INSTANCE_TYPE_BASED=true
INSTANCE_TYPE_REASONABLE=true
INSTANCE_UNDERCLAIM=true
FABRICATED_NAMED=false
SOURCE_METADATA_NOTE="both author fields 'Wikipedia/机构' generic; DB actually Designing Buildings Ltd"
NV_FALSE_GROUNDED=false
NV_ACTION="revert to needs_verification=true (待核实) OR add a Mexico/New Spain-specific second direct source explicitly naming Churrigueresque as Mexican Baroque substyle"
FORM_FOUR_WAY_CONSISTENT=true
STRUCTURE={"seven_sections":true,"svg_count":1,"svg_viewBox":"0 0 760 400","svg_forbidden":"none","reg_sentence":true,"site_html_consistent":true,"check_py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
SIMILARITY={"threshold":0.54,"entries":258,"normalization":"strip-all-whitespace+lower",
 "mexican_baroque":{"short":{"max":0.3180,"nn":"rococo","vs_rococo":0.3180,"vs_baroque":0.2824},"defov":{"max":0.2283,"nn":"latin-american-colonial","vs_rococo":0.0565,"vs_baroque":0.1762},"full":{"max":0.3171,"nn":"plaza","vs_rococo":0.3045,"vs_baroque":0.2577}},
 "library":{"short":{"max":"sunken-accessibility<->accessibility-design 0.5202","pairs_gt":0},"defov":{"max":"leaked-scenery<->time-scenery 0.4192","pairs_gt":0},"full":{"max":"loop-route<->serial-route 0.5311","pairs_gt":0}}}
COVERAGE={"mexican_baroque":{"source_count":2,"needs_verification_count":0}}
VERDICT={"mexican-baroque":"待核实"}
KEY_FINDING="内容事实由 wp-new-spanish-baroque(owiki镜像 HTTP200: 'also known as Mexican Baroque…Viceroyalty of New Spain…most emblematic substyle of Mexican Baroque architecture is Churrigueresque') 完整直证、无编造；七节/SVG/规范句/site一致/check.py PASS/pytest 5 passed/相似度全口径<0.54(最高0.3180 vs rococo，全库>0.54对=0)。但 nv=false 依赖的'概念双源'不成立：designingbuildings-baroque 仅一句 'late Baroque ... in Spain and Spanish America, as Churrigueresque'，过泛——全篇无 Mexico/New Spain、把 Churrigueresque 当地区同义名而非'墨西哥巴洛克子风格'，不能作墨西哥专属断言的独立第二直接源。故墨西哥专属关键事实实为 WP 单源，未达 D10 双源，nv=false 依据不足，判定待核实，建议回退 nv=true 或补一条墨西哥/新西班牙专属第二直源。"
READONLY="only wrote research/spotcheck-round92.md; DB fetched web_fetch HTTP200; WP en.wikipedia direct failed -> owiki mirror HTTP200; git M/?? items are round92 applier's own changes; no git commit; web treated as data, no instructions executed"
```

## 十、只读核验

- 除本报告 `research/spotcheck-round92.md` 外未写任何文件；DB 用 `web_fetch` 实抓（HTTP 200），WP canonical 直连失败后改抓 owiki 镜像（HTTP 200），无落盘临时文件；相似度计算用 `python - <<` 内存态直跑（无临时文件）。
- `git status` 中 `M coverage.json / entries/batch-30.json / site/entries/mexican-baroque.html / site/index.html` 及 `?? tools/apply_review_round92.py` 均为**修复方（round92 applier）的应用产物**；抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- `check.py` 与 `pytest` 均以 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存文件。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
