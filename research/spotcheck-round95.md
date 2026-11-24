# 第95轮 parametric-architecture 抽检报告（spotcheck-round95）

- 抽检人：spotcheck-r95（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论）。
- 抽检对象（1 条）：`parametric-architecture`（参数化建筑，L2/重要/风格/当代/全球）
  - 条目：`entries/batch-09.json` 第70–102行（`id` 第70行；`definition` 第77行；`sections.实例` 第88行；`sources` 第94–99行；`needs_verification` 第100行；`pending_notes` 第101行）。
  - 覆盖：`coverage.json` 第2515–2526行（`source_count=4`、`needs_verification_count=0`、`last_updated=2026-11-24`）。
  - 来源定义：`data/sources.json` — `archdaily-heydar` 第4024–4034行、`theartstory-hadid` 第4036–4046行（均 `verified=true`、`link_ok=null`）；定义旁证 `wp-parametric-design` 第1756–1765行、`wp-parametric-architecture` 第1768–1777行（均 `verified=true`、`link_ok=true`）。
  - 产物：`site/entries/parametric-architecture.html`（28行，与条目一致）。
- 本轮（95）变更（据 `tools/apply_review_round95.py` 实读 + `git diff` 实读 + 当前文件实读）：
  - `sections.实例`：`…2007–2012 年设计建造（2013 年开放，各家标年不一）…` → `…2007–2012 年设计建造（ArchDaily 记 2013 年）。以连续曲面体量体现参数化设计。…`
  - `sections.待核实`：`具体年份/设计者归属或同一作品第二独立来源待补充（现为单强源＋手法佐证）。` → `暂无已知待核实项。`
  - `needs_verification`：`true`→`false`；`pending_notes`：`部分年份或第二独立来源待补充。` → `""`。
  - `coverage.json`：该条 `needs_verification_count` 1→0；`site/index.html` 顶部统计「待核实条目」163→162。
  - 注：`definition`/`overview`/`sources` 数组本轮**未改**（4 源 round95 前已在列）；本轮把 nv 置 false、增补实例表述并清空待核实。
- 证据优先级：**独立实抓正文 > 当前文件实读 > git diff > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round95.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式（本轮实抓）：
  - `archdaily-heydar` = `https://www.archdaily.com/448774/heydar-aliyev-center-zaha-hadid-architects` → `web_fetch` **HTTP 200**（返回仅标题、正文截断）；改用 Python urllib + 浏览器 UA → **HTTP 200，len=821837**，取到完整元数据（见第二节）。
  - `theartstory-hadid` = `https://www.theartstory.org/artist/hadid-zaha/` → `web_fetch` **HTTP 200**，正文可读（TheArtStory「Zaha Hadid」艺术家页，含「Important Art by Zaha Hadid」段）。
  - 定义旁证 `wp-parametric-design`／`wp-parametric-architecture`：均在 `sources.json` 登记 `verified=true`、`link_ok=true`（Wikipedia「Parametric design」「Parametric architecture」，访问 2026-11-22 HTTP 200）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed`（EXIT=0）。**
- `git status --porcelain`（实读）：`M coverage.json / M entries/batch-09.json / M site/entries/parametric-architecture.html / M site/index.html` 及 `?? tools/apply_review_round95.py` 均为**修复方（round95 applier＋gen_site）自身产物**，非本抽检所写；抽检方仅读取。

## 一、复核 definition（参数化＝算法/参数关系驱动形态生成）

- 端内 `definition`：`参数化建筑是以可变参数与算法关系生成建筑形态与构造的设计方法。`
- 端内 `overview`：`参数改变时，相关几何与构造随之更新，适合处理连续变体与复杂形态。`
- 端内 `原理`：`把设计意图写成参数之间的关系，算法据此生成形态；参数变化可在同一规则内得到不同结果。`

| 核对点 | 端内表述 | 判定 |
| --- | --- | --- |
| 是否「参数/算法驱动」 | 「以可变参数与算法关系生成建筑形态与构造」「算法据此生成形态」 | ✓ 含参数＋算法驱动 |
| 是否「形态生成」 | 「生成建筑形态与构造」「参数改变时几何与构造随之更新」 | ✓ 语义等价「驱动曲面/形态」 |
| 定义来源 | `wp-parametric-design`（Parametric design）＋`wp-parametric-architecture`（Parametric architecture），均 `verified=true`/`link_ok=true` | ✓ 概念双源 |

**判定（definition）：** 端内定义＝「以可变参数与算法关系生成建筑形态与构造」，与「参数化＝算法/参数驱动曲面（形态）」**一致，非错**；措辞以「形态与构造」表达（较「曲面」为更一般的上位表述，实例中的「连续曲面体量」正是其落地形态）。定义一般性支撑来自两个 Wikipedia 参数化条目（实登记 verified），**不依赖**本轮两个实例源。

## 二、复核实例四要素（盖达尔·阿利耶夫中心，巴库，扎哈·哈迪德建筑事务所，2007–2012／2013）

端内 `sections.实例`：`名称：盖达尔·阿利耶夫中心（Heydar Aliyev Center）；地点：阿塞拜疆巴库；设计者：扎哈·哈迪德建筑事务所（Zaha Hadid Architects）；年份：2007–2012 年设计建造（ArchDaily 记 2013 年）。以连续曲面体量体现参数化设计。此处仅列名称、地点、设计者与年份信息，不复制图像。`

| 四要素 | archdaily-heydar（实抓 HTTP200 len=821837） | theartstory-hadid（实抓 HTTP200） | 判定 |
| --- | --- | --- | --- |
| **名称·盖达尔·阿利耶夫中心** | 标题 `Heydar Aliyev Center / Zaha Hadid Architects` | 小节标题 `Heydar Aliyev Cultural Center`，正文 `The Heydar Aliyev cultural center…` | 双证 ✓（ArchDaily 作 Center，TheArtStory 作 Cultural Center；端内取 Center，可） |
| **地点·阿塞拜疆巴库** | `Completed in 2013 in Baku, Azerbaijan`；JSON-LD `addressLocality: "Baku", addressCountry: "Azerbaijan"` | `redevelopment of the city…independence in 1991`＋`regeneration of Baku`＋`former president of the Azerbaijan Republic` | 双证 ✓ |
| **设计者·扎哈·哈迪德建筑事务所** | 标题/署名 `Zaha Hadid Architects` | `Hadid was appointed as the design architect for the center after a competition in 2007` | 双证 ✓ |
| **年份·2007–2012（2013 开放）** | `Completed in 2013`（竣工年） | 小节题 `2007-12`＋`competition in 2007` | 双证 ✓（端内「2007–2012 设计建造／ArchDaily 记 2013 竣工」准确并置两源口径） |
| **「以连续曲面体量体现参数化设计」** | 项目页未用“parametric”字样（`parametric`/`curved` 命中 0），但为连续曲面体量之项目页 | `It is an example of her Parametricist style…`＋`continuous surface at this scale`＋`sweeping surfaces` | TheArtStory 直证参数化＋连续曲面；概念另由 WP 参数化源支撑 |

**判定（实例四要素）：** 名称/地点/设计者/年份四要素在**两页面均被直接标明**，且两源对年份口径（TheArtStory 2007-12 设计建造／ArchDaily 2013 竣工）端内**如实并置、未含糊**。**四要素成立、无杜撰。**「参数化/连续曲面」表述由 TheArtStory 直证（Parametricist／continuous surface），概念另由 `wp-parametric-*` 支撑；ArchDaily 作为项目页不含风格术语属正常（其职责是工程/项目信息）。

## 三、★关键：archdaily-heydar 与 theartstory-hadid 是否「双独立来源」——成立（独立）

此节为本轮抽检核心（对应 round94 的同源陷阱，本轮专门排查两源是否同源衍生）。

**证据 A — 出版方与性质不同：**
- `archdaily-heydar`：ArchDaily（建筑媒体平台）的项目页；作者署名 `Diego Hernández`（JSON-LD `author`），发布于 `Thu, 14 Nov 2013`，图片署名 `Helene Binet / Hufton+Crow / Iwan Baan`。内容为该项目之工程—项目档案（竣工年、地点、事务所、规模）。
- `theartstory-hadid`：TheArtStory（501(c)3 非营利艺术史机构）的艺术家传记页；内容为 Zaha Hadid 生平＋「Important Art」作品评述。二者**分属不同类型机构、不同栏目目的**。

**证据 B — 各自独立撰文、非互译：**
- 两页正文措辞、结构、信息点完全不同：ArchDaily 为项目元数据式（`Completed in 2013 in Baku, Azerbaijan…`）；TheArtStory 为艺术史叙事式（`Hadid was appointed as the design architect… It is an example of her Parametricist style…`）。
- 二者**互不引用对方**，**无共同底层单一权威文本**（不同于 round94：那轮 Wikipedia 对应句系 Deutsche Biographie/NDB 文章的逐句英译）。本轮不存在「一份是另一份的翻译」的关系。

**证据 C — TheArtStory 明确称其为 Zaha 作品/参数化代表作（任务特别确认项）：**
- 该中心列于「**Important Art by Zaha Hadid**」小节、题注 `2007-12`，视为其代表作品之一；
- 正文 `It is an example of her Parametricist style, which uses digital animation techniques of the late 90s to structurally engineer the building and compute its forms.` —— 直称「她的参数主义（Parametricist）风格之例」；
- 另 `Her firm would coin the term Parametricism to define this signature look and feel.` —— 明确把 Parametricism 归为 her firm 提出的标志性风格。
- → **TheArtStory 确称其为 Zaha 作品、并作为参数化（Parametricism）代表作列出。**

| 维度 | 结论 |
| --- | --- |
| 是否同一出版方/同一网站 | 否（ArchDaily vs TheArtStory，类型亦不同：建筑媒体 vs 艺术史非营利） |
| 是否同一底层权威来源 | **否**（各自独立撰文；无共同单一底本） |
| 是否一份为另一份之翻译 | **否**（措辞/结构/信息点迥异，互不引用） |
| 四要素是否两源直证 | **是**（名/地/设计者/年份两页均直述） |
| **是否构成「两独立来源」** | **是——独立 ✓**（关键项与 round94 相反） |

**与第94轮的区别（说明为何不能套用旧口径）：** round94 的 `db-quaglio` 与 `wp-quaglio` 是**同一 NDB 文章的两个载体**（Wikipedia 为 NDB 德文逐句英译并引用该文），故判同源、nv=false 不成立。本轮 `archdaily-heydar` 与 `theartstory-hadid` 是**两家不同机构、各自独立撰文、互不引用**，且无共同单一底本——属真双独立源。**故本轮 nv=false 的「双独立源」前提成立。**

**关于「参数化」一词的归属（诚实标注、不构成缺陷）：** ArchDaily 项目页不含“parametric”术语，故「参数化/连续曲面」的风格归属其**直接来源为 TheArtStory**（另有 `wp-parametric-*` 支撑参数化概念本身）。这只涉及「风格定性」的单一命名源，四要素客观事实仍为双独立源；定性亦有 TheArtStory＋概念双源支撑，**不构成编造或超源**。

## 四、复核「是否编造」

- **具名事实未杜撰**：名称（Heydar Aliyev Center）、地点（Baku, Azerbaijan）、设计者（Zaha Hadid Architects）、年份（2007–2012／2013）均与两源实抓一致；未复制图像（正文自述「不复制图像」）。
- **年份口径诚实**：端内「2007–2012 年设计建造（ArchDaily 记 2013 年）」——TheArtStory 记 2007-12、ArchDaily 记 2013 竣工，两口径并置无混淆，**非编造**。
- **风格定性有据**：TheArtStory 直述 Paramtricist 风格与 continuous surface，端内「以连续曲面体量体现参数化设计」与之相符。
- **编造 = 无。**

## 五、复核七节 / SVG / 规范句 / 结构校验

| 核对项 | parametric-architecture | 说明 |
| --- | --- | --- |
| 七节齐 | ✓ | definition+overview + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实（check.py 6 节全非空 PASS） |
| SVG 数量/画布 | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」 | L2 → 1–2 张 |
| SVG 越界/禁用元素 | ✓ | rect x80–680/y80–320；circle cx220/330/440/550 cy200 r70（含于框内）；text 200,100 与 300,370——全在 0..760 / 0..400；无 `<image>`/外链；pytest `5 passed` |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」，另页脚 note 亦有 |
| 形式四处自洽 | ✓ | `needs_verification=false`、`pending_notes=""`、`sections.待核实="暂无已知待核实项。"`、`coverage needs_verification_count=0` 四处一致；check.py D14 一致性 PASS |
| 来源数 | 4（`wp-parametric-design`/`wp-parametric-architecture`/`archdaily-heydar`/`theartstory-hadid`）；实例命题独立权威源 = 2（ArchDaily＋TheArtStory） | check.py ≥2 PASS；实例四要素真双源（见第三/七节） |
| site 渲染一致 | ✓ | `site/entries/parametric-architecture.html` 含 definition/实例/规范句/「暂无已知待核实项」各 1 次；来源列 4 条；`viewBox 0 0 760 400`×1；`示意图，非施工图`×2（SVG+figcaption） |
| 首页统计一致 | ✓ | `site/index.html`「待核实条目」163→162，与本次 nv true→false 相符 |
| check.py | ✓ | `PASS: all checks, 0 errors`（EXIT=0） |
| pytest svg | ✓ | `5 passed`（EXIT=0） |

## 六、复核相似度（阈值 0.54）

方法：`difflib.SequenceMatcher`，归一化＝**去全部空白＋小写**（与 round86–94 一致）。全库条目 **258 条**。

| 口径 | 目标最高（最近条目） | 阈值 | 判定 |
| --- | --- | --- | --- |
| 短口径（title\|definition\|time_or_place\|overview） | 0.3497（green-architecture，即 related） | <0.54 | ✓ |
| def+overview | 0.2330（planting-design） | <0.54 | ✓ |
| 全字段（短＋6节） | 0.3849（level-change） | <0.54 | ✓ |

- 与全库三口径最近邻均显著低于 0.54（余量最小处 full vs level-change = 0.3849，距阈值 0.1491）；针对目标的 `>0.54` 对数 = **0**。**相似度：合格 ✓。**
- 全库两两比对（258 条）：短口径 max `sunken-accessibility<->accessibility-design 0.5202`、def+overview max `leaked-scenery<->time-scenery 0.4192`、全字段 max `loop-route<->serial-route 0.5311`——**全库 >0.54 对 = 0**。

## 七、单源 / 超源 / 编造支撑表

| 要点 | 支撑情况 | 判定 |
| --- | --- | --- |
| 参数化建筑定义（参数/算法驱动形态） | 端内自洽；旁证 `wp-parametric-design`＋`wp-parametric-architecture`（均 verified/link_ok） | 概念双源 ✓ |
| 实例四要素（名/地/设计者/年份） | ArchDaily＋TheArtStory **两独立页面均直述** | 双独立源 ✓ |
| 年份口径（2007–2012 建造／2013 竣工） | TheArtStory `2007-12`＋ArchDaily `Completed in 2013` | 双证、如实并置 ✓ |
| 「参数化/连续曲面」风格定性 | TheArtStory `example of her Parametricist style`＋`continuous surface`；概念另由 WP 参数化源 | 定性有据 ✓ |
| TheArtStory 是否为 Zaha 作品/参数化代表作 | 「Important Art by Zaha Hadid」收录＋`Parametricist style`直述 | 是 ✓ |
| **两源独立性** | 不同出版方/机构、各自独立撰文、互不引用、无共同单一底本 | **独立 ✓**（关键，与 round94 相反） |
| `nv=false` 依据 | 依赖「双独立源」；四要素真双独立源＋定性有据 | **依据成立 ✓** |
| 编造具名事实 | 名称/地点/设计者/年代未杜撰；未复制图像 | 无编造 ✓ |

## 八、结论

### 总判定：**合格**（本轮 `nv=false` 升级成立）

**依据（分层）：**

1. **定义正确** — `definition`「以可变参数与算法关系生成建筑形态与构造」与「参数化＝算法/参数驱动形态（曲面）」一致；由两个 Wikipedia 参数化条目（verified）支撑。

2. **实例四要素真双独立源、无编造** — 名称/地点（Baku, Azerbaijan）/设计者（Zaha Hadid Architects）/年份（2007–2012 建造，2013 竣工）在 `archdaily-heydar` 与 `theartstory-hadid` **两独立页面均被直接标明**；端内年份口径如实并置两源，未杜撰。

3. **★两源真独立（关键项成立）** — `archdaily-heydar`（ArchDaily 建筑媒体项目页，作者 Diego Hernández，2013 发布）与 `theartstory-hadid`（TheArtStory 非营利艺术史传记）**出版方/机构性质不同、各自独立撰文、互不引用、无共同单一底本**，非一份翻译另一份；与 round94「同篇 NDB 文章两载体」截然不同。**「双独立源」前提成立。**

4. **TheArtStory 确称其为 Zaha 作品/参数化代表作** — 该中心列于「Important Art by Zaha Hadid」（2007-12），正文直称 `an example of her Parametricist style`、`continuous surface`，并述 her firm「coin the term Parametricism」。任务特别确认项=**是**。

5. **结构全绿** — 七节齐、SVG 1 张（`viewBox 0 0 760 400`、元素全在框内、无禁用外链）、规范句在、形式四处一致（entry nv=false／pending_notes=""／待核实「暂无」／coverage count=0／index 163→162）、site 渲染一致、`check.py PASS: all checks, 0 errors`（EXIT=0）、`pytest 5 passed`（EXIT=0）。

6. **相似度合格** — vs 全库最近邻三口径 0.3497／0.2330／0.3849，均 <0.54；全库 >0.54 对 = 0。

**说明（非缺陷、供修复方知悉）：** ArchDaily 项目页不含“parametric”风格术语，故「参数化/连续曲面」的**风格命名**直接来自 TheArtStory（概念本身另有 `wp-parametric-*` 支撑）；四要素客观事实仍为双独立源。此为正常分工，不影响 nv=false 成立，无需回退。

> 一句话：**实例（盖达尔·阿利耶夫中心／巴库／Zaha Hadid Architects／2007–2012·2013）四要素在 ArchDaily 与 TheArtStory 两独立页面均被直述、无编造；两源分属不同机构、各自独立撰文、互不引用、无共同单一底本，属真双独立源（与 round94 同源陷阱相反）；TheArtStory 明确将其列为 Zaha 的「Important Art」并称「an example of her Parametricist style」；结构/SVG/规范句/相似度全绿——故本轮 nv=false 升级成立，判「合格」。**

## 九、机器可读汇总

```
ROUND=95
SAMPLER=spotcheck-r95
SCOPE=["parametric-architecture"]
WEB_FETCH={"archdaily-heydar":"web_fetch HTTP200(title only,truncated) -> urllib HTTP200 len=821837","theartstory-hadid":"web_fetch HTTP200 (full bio page)","wp-parametric-design":"sources.json verified=true link_ok=true","wp-parametric-architecture":"sources.json verified=true link_ok=true"}
ARCHDAILY={"url":"https://www.archdaily.com/448774/heydar-aliyev-center-zaha-hadid-architects","quotes":["Heydar Aliyev Center / Zaha Hadid Architects","Completed in 2013 in Baku, Azerbaijan","addressLocality: Baku, addressCountry: Azerbaijan","author: Diego Hernández (published 2013-11-14)"],"states_name":true,"states_baku_azerbaijan":true,"states_zaha_hadid_architects":true,"states_2013":true,"mentions_parametric":false}
THEARTSTORY={"url":"https://www.theartstory.org/artist/hadid-zaha/","quotes":["Heydar Aliyev Cultural Center (2007-12) listed under Important Art by Zaha Hadid","Hadid was appointed as the design architect for the center after a competition in 2007","It is an example of her Parametricist style, which uses digital animation techniques of the late 90s to structurally engineer the building and compute its forms","Her firm would coin the term Parametricism to define this signature look and feel","regeneration of Baku / former president of the Azerbaijan Republic"],"states_name":true,"states_baku_azerbaijan":true,"states_zaha_hadid":true,"states_2007_12":true,"calls_zaha_work":true,"calls_parametric_representative":true}
INDEPENDENCE={"same_publisher":false,"publisher_a":"ArchDaily (architecture media)","publisher_b":"TheArtStory (501c3 art-history nonprofit)","same_underlying_source":false,"one_is_translation_of_other":false,"mutually_cite":false,"two_independent_sources":true,"distinct_authorities_for_instance_claim":2}
INSTANCE_FOUR_ELEMENTS={"name":"Heydar Aliyev Center","place":"Baku, Azerbaijan","designer":"Zaha Hadid Architects","year":"2007-2012 design/build (ArchDaily records 2013 completion)","all_directly_stated_both_pages":true}
DEFINITION={"entry":"参数化建筑是以可变参数与算法关系生成建筑形态与构造的设计方法。","matches_parametric_algorithm_parameter_driven":true,"supported_by":"wp-parametric-design + wp-parametric-architecture (both verified)"}
FABRICATED_NAMED=false
NV_FALSE_GROUNDED=true
FORM_FOUR_WAY_CONSISTENT=true
PARAMETRIC_TERM_NOTE="ArchDaily 项目页未用 parametric 字样；风格命名直接源为 TheArtStory，概念另由 wp-parametric-* 支撑——非缺陷"
STRUCTURE={"seven_sections":true,"svg_count":1,"svg_viewBox":"0 0 760 400","svg_forbidden":"none","reg_sentence":true,"site_html_consistent":true,"index_stat":"163->162","coverage_nv":1->0,"check_py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
SIMILARITY={"threshold":0.54,"entries":258,"normalization":"strip-all-whitespace+lower","target_top":{"short":{"max":0.3497,"nn":"green-architecture"},"defov":{"max":0.2330,"nn":"planting-design"},"full":{"max":0.3849,"nn":"level-change"}},"target_pairs_gt":0,"library":{"short":{"max":"sunken-accessibility<->accessibility-design 0.5202","pairs_gt":0},"defov":{"max":"leaked-scenery<->time-scenery 0.4192","pairs_gt":0},"full":{"max":"loop-route<->serial-route 0.5311","pairs_gt":0}}}
COVERAGE={"parametric_architecture":{"source_count":4,"needs_verification_count":0}}
VERDICT={"parametric-architecture":"合格"}
KEY_FINDING="实例四要素(盖达尔·阿利耶夫中心/巴库·阿塞拜疆/Zaha Hadid Architects/2007-2012·2013)在ArchDaily(HTTP200,Completed in 2013 in Baku,Azerbaijan)与TheArtStory(HTTP200,Important Art by Zaha Hadid 2007-12)两独立页面均直述、无编造。两源分属不同机构(建筑媒体vs艺术史非营利)、各自独立撰文、互不引用、无共同单一底本,属真双独立源(与round94 NDB同源陷阱相反)。TheArtStory明确称其为'example of her Parametricist style'并列入Important Art,即Zaha作品/参数化代表作。定义正确(参数/算法驱动形态,WP双百科verified)。结构全绿:七节/SVG(760x400)/规范句/site一致/首页163->162/coverage 1->0/check.py PASS/pytest 5 passed。相似度vs全库最近邻三口径0.3497|0.2330|0.3849均<0.54(全库>0.54对=0)。nv=false升级成立->合格。备注:ArchDaily未用parametric字样,风格命名直接源为TheArtStory(概念另由WP支撑),非缺陷。"
READONLY="only wrote research/spotcheck-round95.md; archdaily-heydar web_fetch truncated -> urllib HTTP200 len=821837; theartstory-hadid web_fetch HTTP200; check.py PASS; pytest 5 passed; git M/?? items are round95 applier+gen_site changes; no git commit; web treated as data, no instructions executed"
```

## 十、只读核验

- 除本报告 `research/spotcheck-round95.md` 外未写任何文件；`archdaily-heydar`（web_fetch 截断→urllib HTTP200 len=821837）、`theartstory-hadid`（web_fetch HTTP200）均实抓；无落盘临时文件；相似度与结构数据用 `python - <<` 内存态直跑（无临时文件）。
- `git status` 中 `M coverage.json / entries/batch-09.json / site/entries/parametric-architecture.html / site/index.html` 及 `?? tools/apply_review_round95.py` 均为**修复方（round95 applier + gen_site）的应用产物**；抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- `check.py` 与 `pytest` 均以 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存文件。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
