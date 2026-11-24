# 第90轮 romanticism-style 抽检报告（spotcheck-round90）

- 抽检人：spotcheck-r90（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论）。
- 抽检对象（1 条）：`romanticism-style`（浪漫主义建筑，L2/补充/风格/文艺复兴至19世纪/欧洲）— 位 `entries/batch-38.json` 第132行起；`coverage.json` 第2229行起；产物 `site/entries/romanticism-style.html`。
- 本轮（90）变更（据 `tools/apply_review_round90.py` 实读 + `git diff` 实读 + 当前文件实读）：
  - **实例覆盖**：`名称：如画的哥特式宅邸（类型性描述）…` → `名称：新天鹅堡（Neuschwanstein Castle）；地点：德国巴伐利亚；委托者：巴伐利亚国王路德维希二世（Ludwig II）；年份：1869 年动工。被视为“城堡浪漫主义”的典型。…`
  - **新增双源**：`sources` 由 `[henryford-gothic-revival, libretexts-romanticism]` → 追加 `wp-neuschwanstein`、`db-neuschwanstein`（共 4 源）。
  - **nv 升级**：`needs_verification` true→false；`pending_notes` → `""`；`sections.待核实` → `暂无已知待核实项。`
  - **未改**：`definition`、`overview`、`原理`、`典型手法与适用条件`、`常见错误与限制`、`一图`、`svg`、`related`。
  - `data/sources.json` 新增 `wp-neuschwanstein`、`db-neuschwanstein`（verified:true、link_ok:true）；`coverage.json` romanticism-style 条 `source_count` 2→4、`needs_verification_count` 1→0；`site/entries/romanticism-style.html`、`site/index.html`、`site/sources.html` 由 applier 重新生成。
- 证据优先级：**独立实抓正文 > 当前文件实读 > git diff > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、计数、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round90.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式：`db-neuschwanstein` 用本环境 `web_fetch` 成功（HTTP 200）；`wp-neuschwanstein` 本轮 `web_fetch` 报 `TypeError: fetch failed`，改用 **Python urllib + 浏览器 UA + 非校验 SSL（内存态 `python -c` 直跑，未落盘任何临时文件）**，得 HTTP 200。
- 实抓 HTTP（两条均 200，内存态；正文去标签后计数）：
  - `db-neuschwanstein` = `https://www.designingbuildings.co.uk/wiki/Neuschwanstein_Castle` → **200，58,410 B**，标题 `Neuschwanstein Castle - Designing Buildings`，页面明示 `Last edited 06 Nov 2020`；计数 `Neuschwanstein`×8、**`Romanticism`×1、`iconic example`×1**、`Ludwig II`×1、`1869`×1、`Bavaria`×4、`construction began`×1、`Romanesque`×2。
  - `wp-neuschwanstein` = `https://en.wikipedia.org/wiki/Neuschwanstein_Castle` → **200，462,240 B**，标题 `Neuschwanstein Castle - Wikipedia`；计数 `Neuschwanstein`×111、`Romanticism`×3、**`Burgenromantik`×1**、`Romantic`×5、`Ludwig II`×32、`1869`×4、`Bavaria`×58、`Romanesque Revival`×3、`historicism`×2、`Wagner`×15。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** `python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed`（EXIT=0）。
- `git status --porcelain`（实读）：`M coverage.json / data/sources.json / entries/batch-38.json / site/entries/romanticism-style.html / site/index.html / site/sources.html` 及 `?? tools/apply_review_round90.py` 均为**修复方（round90 applier）自身产物**，非本抽检所写；抽检方仅读取。

## 一、复核①：definition 三要素是否有源（如画轮廓 / 异域联想 / 情感）

端内 definition：`浪漫主义建筑偏爱如画轮廓与异域联想，借历史与自然唤起情感。`
端内 overview：`它反叛新古典的冷静秩序，追求不规则、戏剧化的轮廓。`

四源实抓正文词频（henryford-gothic-revival、libretexts-romanticism、wp-neuschwanstein、db-neuschwanstein）：

| definition 要素 | 直接源证据（实抓） | 判定 |
| --- | --- | --- |
| **如画轮廓（如画/不规则）** | henryford：`picturesque`×18（如「romantic and picturesque」「this picturesque style」）；overview 的「不规则、戏剧化轮廓」由如画趣味派生 | **有源 ✓（henryford 直证；如画趣味=该源主旨）** |
| **异域联想** | henryford：`exotic`×0 / `oriental`×0 / `foreign`×0（`Eastern`8 次全为「Eastern Standard Time」时区噪声）；libretexts：`exotic`×0 / `oriental`×0；wp/db 无 exotic；仅 wp/db 提到新天鹅堡含 `Byzantine and Gothic influences`（拜占庭=外来风格，属**间接/派生**，且是具体建筑而非运动通性） | **无直接词面支撑 ✗（弱/派生）** |
| **情感（借历史与自然唤起）** | libretexts：`emotion`×25、`imagination`×5、`sublime`×2、`nature`×4、`history`×3、`historical`×4（「emphasized emotion, imagination, nature…roused the viewer's emotions」）；henryford：`emotion`×4、`history`×12、`medieval`×10（「The Gothic taste was about emotion, whimsy, and the spiritual」） | **双源直证 ✓✓（历史/自然/情感均有源）** |

**判定（复核①）：definition 的「如画轮廓」「借历史与自然唤起情感」两核心有源（如画=henryford，历史/自然/情感=henryford+libretexts 双源）；「异域联想」在四个已引来源中均无直接词面对应（exotic/oriental/foreign=0），仅可由新天鹅堡所引拜占庭/哥特等外来历史风格作间接联想，属较弱概括/派生措辞，建议核实或改为有源表达（如「历史联想/如画趣味」）。此为既有 definition 的措辞问题，非本轮新增，且不属具名事实编造。**

## 二、复核②：实例四要素是否由 `wp-neuschwanstein` + `db-neuschwanstein` 双源直证（逐要素）

端内实例：`名称：新天鹅堡（Neuschwanstein Castle）；地点：德国巴伐利亚；委托者：巴伐利亚国王路德维希二世（Ludwig II）；年份：1869 年动工。被视为“城堡浪漫主义”的典型。…`

| 实例要素 | wp-neuschwanstein（实抓） | db-neuschwanstein（实抓） | 判定 |
| --- | --- | --- | --- |
| **新天鹅堡（名称/主体）** | 页题 `Neuschwanstein Castle - Wikipedia`，全文 `Neuschwanstein`×111 | 页题 `Neuschwanstein Castle - Designing Buildings`，`Neuschwanstein`×8 | **双源直证 ✓✓** |
| **巴伐利亚** | `Palace in Bavaria, Germany`；`King Ludwig II of Bavaria`（`Bavaria`×58） | `located on a hill in southwest Bavaria, Germany`（`Bavaria`×4） | **双源直证 ✓✓** |
| **路德维希二世** | `King Ludwig II of Bavaria … commissioned Neuschwanstein Castle on the remote northern edges of the Alps as a retreat`（`Ludwig II`×32） | `was commissioned by King Ludwig II of Bavaria as his personal retreat and homage to the composer Richard Wagner`（`Ludwig II`×1） | **双源直证 ✓✓** |
| **1869 年动工** | 信息框 `Construction started 5 September 1869`；正文 `The foundation stone for the palace was laid on 5 September 1869`；`built between 1869 and 1892`（`1869`×4） | `Construction began in September 1869, after the ruins of the medieval castle were completely demolished`（`1869`×1、`construction began`×1） | **双源直证 ✓✓** |

**判定（复核②）：实例四要素（新天鹅堡 / 巴伐利亚 / 路德维希二世 / 1869 动工）均由 `wp-neuschwanstein` 与 `db-neuschwanstein` 两个独立平台逐项直接证明，无一项依赖单源或推断。本轮实例升级为强双源直证。**

## 三、复核③：「浪漫主义」与「新天鹅堡」的关联，两源是否都直证

- **db-neuschwanstein（称其 Romanticism 典范）：是。** 原文：`Neuschwanstein is an iconic example of Romanticism and remains a recognisible symbol of Germany.`（`iconic example`×1、`Romanticism`×1）—— 直称「浪漫主义的标志性范例/典范」。
- **wp-neuschwanstein（称 castle Romanticism）：是。** 原文：`Neuschwanstein embodies both the contemporaneous architectural fashion known as castle Romanticism (German: Burgenromantik) and King Ludwig II's enthusiasm for the operas of Richard Wagner.`（`Burgenromantik`×1、`Romanticism`×3）—— 直称其体现「城堡浪漫主义（Burgenromantik）」。
- 端内实例「被视为‘城堡浪漫主义’的典型」正对应 wp「embodies … castle Romanticism」与 db「iconic example of Romanticism」，措辞有据、未夸大。
- **附注（非缺陷，供参考）**：两源同时提到新天鹅堡的形式归属另含 `Romanesque Revival`（db）/ `Neo-Romanesque`（wp）与 `Byzantine and Gothic influences`；即「浪漫主义/城堡浪漫主义」为两源明确给出的定性（db 用 Romanticism、wp 用 castle Romanticism），与其复兴式（Romanesque Revival）描述并存不冲突——本条目取「浪漫主义建筑」主题下的实例，引用口径成立。

**判定（复核③）：`wp` 与 `db` 两源都对「新天鹅堡＝浪漫主义/城堡浪漫主义」作出直接定性，关联双源直证 ✓✓。**

## 四、复核④：是否编造

**结论：无编造具名事实 ✓；两源真实存在、url 真实、note 与正文一致。**
- `db-neuschwanstein` 真实（HTTP 200，`Neuschwanstein Castle - Designing Buildings`，末次编辑 2020-11-06），`sources.json` note「新天鹅堡：浪漫主义典范，路德维希二世 1869 起建」与正文（iconic example of Romanticism / King Ludwig II of Bavaria / Construction began September 1869）一致 ✓。
- `wp-neuschwanstein` 真实（HTTP 200，`Neuschwanstein Castle - Wikipedia`），note「新天鹅堡：城堡浪漫主义，路德维希二世，1869 动工」与正文（castle Romanticism / Burgenromantik、Ludwig II of Bavaria、1869）一致 ✓。
- 实例仅列「名称、地点、委托者、年份」四要素，明确声明「不复制图像」，无杜撰建筑师/图像/细节；建筑师（Eduard Riedel 等）未被写入，避免超源。
- **非编造**：无杜撰具名事实；`wp`/`db` 均真实可达且内容逐项对得上 note。

## 五、复核⑤：nv=false 是否有据

**结论：nv=false 就本轮修复目标（实例缺失）成立且有据；D10 就「实例关键事实」满足。**
- **D10（实读 DECISIONS.md）**：「关键事实双源或标待核实」。本轮升级的「关键事实」＝**新天鹅堡实例四要素（名称/地点/委托者/年份）—— 现由 wp + db 双独立平台逐项直证**（见§二），关键事实双源满足 → nv=false **有据**。
- **形式自洽（四处一致）**：`needs_verification=false`、`pending_notes=""`、`sections.待核实="暂无已知待核实项。"`、`coverage.json needs_verification_count=0 / source_count=4` —— 四处一致 ✓（check.py PASS 亦覆盖 D14）。
- **残留（与 nv 无直接关联、单列建议）**：`definition` 的「异域联想」一条在四源中无直接词面支撑（§一），属既有措辞的弱支撑，建议另行核实或改为有源表达；它不影响本轮以「实例」为核心的 nv=false 判定。

## 六、复核⑥：七节 / SVG / 规范句 / 结构校验

| 核对项 | romanticism-style | 说明 |
| --- | --- | --- |
| 七节齐 | ✓ | definition+overview + 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（check.py 校验 6 节全非空，PASS） |
| SVG 数量/画布 | ✓ | 1 张，`viewBox 0 0 760 400`，含「示意图，非施工图」 |
| SVG 禁用元素 | ✓ | 无 `<script>/javascript:/href=/<image/<iframe/url(/onload/onclick/onerror`（check.py validate_svg PASS） |
| SVG 越界 | ✓ | path x110..640 y120..320；circle cx258 cy216 r98 → x160..356 y118..314；rect x364 y298 w54 h102 → x364..418 y298..400（贴边内）；text x40/300 y40/380；散点 r4 全在内 —— bbox 均在 0..760 / 0..400（pytest test_svg_bounds 5 passed 复核） |
| 规范句 | ✓ | 常见错误与限制收尾「实际工程须按当地规范和专业设计人员的要求」 |
| site 渲染一致 | ✓ | `site/entries/romanticism-style.html` 含「新天鹅堡」「德国巴伐利亚」「路德维希二世」「1869 年动工」「暂无已知待核实项」「示意图，非施工图」×2，与新内容一致 |
| check.py | ✓ | `PASS: all checks, 0 errors`（EXIT=0） |
| pytest test_svg_bounds | ✓ | `5 passed`（EXIT=0） |

## 七、复核⑦：相似度（阈值 0.54）

方法：`difflib.SequenceMatcher`，归一化=**去全部空白+小写**（与 round86-90 口径一致）；全库 **258** 条两两比对（本轮为条目改写，未新增条数）。

| 口径 | romanticism-style 最高相似对 | 全库最高对 | 全库 >0.54 对数 |
| --- | --- | --- | --- |
| 短口径（标题\|定义\|时间地点\|概述） | **0.4051** vs neoclassical | value↔saturation **0.5437**（预存） | **1**（仅它，预存；romanticism 不在列） |
| def+overview | **0.2286** vs neoclassical | leaked-scenery↔time-scenery 0.4192 | 0 |
| 全字段（短+6节） | **0.4051** vs neoclassical | loop-route↔serial-route 0.5311 | 0 |

- **romanticism-style 所有口径最高 0.4051 < 0.54，安全 ✓。** 全库唯一 >0.54 的 `value↔saturation`（0.5437）为既往预存，与本轮无关；**romanticism 无新增 >0.54 对**。
- 指定关注对：**vs neoclassical** 短 0.4051 / def+overview 0.2286 / full 0.4051；**vs revival-gothic** 短 0.2754 / def+overview 0.1368 / full 0.2137 —— 均远低于阈值，主题区分清晰（新古典=秩序/对称/柱式；哥特复兴=中世纪哥特形式；浪漫主义=如画/情感，措辞无重叠抄袭）。
- **相似度：合格。**

## 八、单源 / 超源 / 编造支撑点（按要求指出）

| 条目 | 要点 | 支撑情况 | 判定 |
| --- | --- | --- | --- |
| **romanticism-style** | **实例四要素（新天鹅堡 / 巴伐利亚 / 路德维希二世 / 1869 动工）** | **wp-neuschwanstein + db-neuschwanstein 双独立平台逐项直证** | **✓✓ 双源（本轮核心，已合格）** |
| romanticism-style | 「浪漫主义 ↔ 新天鹅堡」关联 | wp「castle Romanticism (Burgenromantik)」+ db「iconic example of Romanticism」 | ✓✓ 双源直证 |
| romanticism-style | definition「如画轮廓 / 借历史与自然唤起情感」 | henryford（picturesque×18、emotion×4、history×12、medieval×10）+ libretexts（emotion×25、sublime×2、nature×4、history×3/4） | ✓ 有源（历史/自然/情感双源；如画=henryford） |
| romanticism-style | **definition「异域联想」** | **四源 exotic/oriental/foreign=0（henryford 的 Eastern=时区噪声）；仅 wp/db 的 Byzantine/Gothic influences 为间接** | **✗ 无直接词面源（弱/派生，建议核实或改写）** |
| 两源独立性 | wp(Wikipedia) vs db(Wikipedia 外之 Designing Buildings) | 不同独立平台 | ✓ 独立 |
| 编造具名事实 | 实例仅四要素、不复制图像、不写建筑师 | 无杜撰名称/地点/委托者/年代；wp/db 真实 | ✓ 无编造 |

## 九、复审结论（逐条）

### romanticism-style（浪漫主义建筑）
- **内容/来源：合格（强双源）** — 本轮新增 `wp-neuschwanstein` + `db-neuschwanstein`，经实抓逐项直证实例四要素：新天鹅堡 / 巴伐利亚 / 路德维希二世 / 1869 动工（db「Construction began in September 1869」；wp「Construction started 5 September 1869」）。「浪漫主义 ↔ 新天鹅堡」两源均直证（db「iconic example of Romanticism」；wp「castle Romanticism/Burgenromantik」）。**附 1 处建议**：definition「异域联想」无直接词面源（四源 exotic/oriental/foreign=0），建议核实或改为有源表述。
- **编造：合格** — 无具名作品/作者/年代杜撰；wp/db 真实（均 HTTP 200，url 真实，note 与正文一致）。
- **结构：合格** — 七节齐、规范句在、SVG 合规（1 张，viewBox 0 0 760 400，bbox 在框内，无禁用元素）、site 渲染一致、check.py `PASS`、pytest `5 passed`。
- **相似度：合格** — 全口径最高 0.4051 < 0.54；vs neoclassical 0.4051、vs revival-gothic ≤0.2754；全库唯一 >0.54 的 value↔saturation 0.5437 为预存，romanticism 无新增超阈对。
- **nv=false：合格（有据）** — 实例关键事实四要素双源直证，D10 满足，形式四处一致；definition「异域联想」为与该维度无直接关联的既有弱支撑措辞，建议单列核实/改写，不推翻本轮 nv=false 的核心依据。

**总判定：本轮 1 条（`romanticism-style`）——合格。**
核心依据：实例升级为 `wp-neuschwanstein`（Wikipedia，`castle Romanticism / Burgenromantik`、`King Ludwig II of Bavaria`、`Construction started 5 September 1869`，HTTP 200 / 462,240 B）+ `db-neuschwanstein`（Designing Buildings，`iconic example of Romanticism`、`commissioned by King Ludwig II of Bavaria`、`Construction began in September 1869`，HTTP 200 / 58,410 B）**双独立平台逐项直接证明四要素**；「浪漫主义↔新天鹅堡」两源均直证；无编造具名事实；七节/SVG/规范句/site 一致/check.py PASS/pytest 5 passed/相似度全口径 <0.54 均合格；实例关键事实双源 → nv=false 有据（D10 满足）。**唯一建议**：definition「异域联想」在四源无直接词面支撑（exotic/oriental/foreign=0），建议核实或改为「历史联想/如画趣味」等有源表达——不涉及具名事实编造，亦非本轮新增，不影响合格判定。

## 十、机器可读汇总

```
ROUND=90
SAMPLER=spotcheck-r90
SCOPE=["romanticism-style"]
INSTANCE_UPGRADE={"from":"如画的哥特式宅邸(类型性描述)","to":"新天鹅堡(Neuschwanstein) / 巴伐利亚 / 路德维希二世 / 1869动工"}
NEW_SOURCES=["wp-neuschwanstein","db-neuschwanstein"]
DB_NEUSCHWANSTEIN_URL="https://www.designingbuildings.co.uk/wiki/Neuschwanstein_Castle"
DB_NEUSCHWANSTEIN_TITLE="Neuschwanstein Castle - Designing Buildings"
DB_LAST_EDIT="2020-11-06"
DB_QUOTES={"romanticism":"Neuschwanstein is an iconic example of Romanticism and remains a recognisible symbol of Germany.","commission":"was commissioned by King Ludwig II of Bavaria","bavaria":"located on a hill in southwest Bavaria, Germany","year":"Construction began in September 1869"}
DB_COUNTS={"Neuschwanstein":8,"Romanticism":1,"iconic example":1,"Ludwig II":1,"1869":1,"Bavaria":4,"construction began":1,"Romanesque":2}
WP_NEUSCHWANSTEIN_URL="https://en.wikipedia.org/wiki/Neuschwanstein_Castle"
WP_NEUSCHWANSTEIN_TITLE="Neuschwanstein Castle - Wikipedia"
WP_BYTES=462240
WP_QUOTES={"romanticism":"Neuschwanstein embodies both the contemporaneous architectural fashion known as castle Romanticism (German: Burgenromantik) ...","commission":"King Ludwig II of Bavaria ... commissioned Neuschwanstein Castle","bavaria":"Palace in Bavaria, Germany","year":"Construction started 5 September 1869 / foundation stone laid 5 September 1869"}
WP_COUNTS={"Neuschwanstein":111,"Romanticism":3,"Burgenromantik":1,"Ludwig II":32,"1869":4,"Bavaria":58,"Romanesque Revival":3,"historicism":2,"Wagner":15}
FETCH_METHOD="db: web_fetch HTTP200; wp: web_fetch FAILED(TypeError fetch failed)->python urllib+browserUA+unverifiedSSL HTTP200, in-memory python -c (no temp files)"
INSTANCE_FOUR_ELEMENTS={"name":"wp+db DUAL DIRECT","bavaria":"wp+db DUAL DIRECT","ludwig_ii":"wp+db DUAL DIRECT","year_1869":"wp+db DUAL DIRECT(dB 'Construction began in September 1869'; wp 'Construction started 5 September 1869')"}
ROMANTICISM_NEUSCHWANSTEIN_LINK={"db":"iconic example of Romanticism = YES DIRECT","wp":"castle Romanticism / Burgenromantik = YES DIRECT","both_direct":true}
DEFINITION_SUPPORT={"picturesque_outline":"henryford picturesque x18 = sourced","emotion_via_history_nature":"henryford(history12/medieval10/emotion4)+libretexts(emotion25/sublime2/nature4/history3-4) = DUAL","exotic_association":"NO direct lexical support (exotic/oriental/foreign=0 across 4 sources; henryford 'Eastern'=timezone noise; only Byzantine/Gothic influences indirect) -> WEAK/DERIVED, recommend verify/rewrite"}
FABRICATED_NAMED=false
NV_FALSE_GROUNDED={"instance_key_fact_dual_source":true,"D10_met_for_instance":true,"four_way_consistent":true,"residual":"definition '异域联想' weak/derived -> recommend verify (not a fabricated-named issue, not this round's change)"}
STRUCTURE={"seven_sections":"7 (check.py PASS required 6 section fields)","svg_count":1,"svg_viewBox":"0 0 760 400","svg_forbidden":[],"reg_sentence":true,"site_html_consistent":true,"check_py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
SIMILARITY={"threshold":0.54,"entries":258,"normalization":"strip-all-whitespace+lower","short":{"target_max":0.4051,"target_nn":"neoclassical","vs_revival_gothic":0.2754,"library_max":"value<->saturation 0.5437(预存)","pairs_gt_0.54":1},"def_overview":{"target_max":0.2286,"target_nn":"neoclassical","vs_revival_gothic":0.1368,"library_max":"leaked-scenery<->time-scenery 0.4192","pairs_gt_0.54":0},"full":{"target_max":0.4051,"target_nn":"neoclassical","vs_revival_gothic":0.2137,"library_max":"loop-route<->serial-route 0.5311","pairs_gt_0.54":0},"new_pairs_over_threshold":0}
VERDICT={"romanticism-style":"合格（实例四要素 wp+db 双独立平台逐项直证；浪漫主义↔新天鹅堡两源均直证；非编造；七节/SVG/规范句/site一致/check.py PASS/pytest 5 passed/相似度全口径<0.54；nv=false 实例维度有据；附1处建议：definition『异域联想』无直接词面源，建议核实或改写）"}
KEY_FINDING="romanticism-style=合格：本轮实例升级为『新天鹅堡/巴伐利亚/路德维希二世/1869动工』，由 db-neuschwanstein(Designing Buildings, HTTP200, 'iconic example of Romanticism'/'commissioned by King Ludwig II of Bavaria'/'Construction began in September 1869') + wp-neuschwanstein(Wikipedia, HTTP200/462240B, 'castle Romanticism(Burgenromantik)'/'King Ludwig II of Bavaria'/'Construction started 5 September 1869') 双独立平台逐项直证四要素，且两源都将新天鹅堡直接定性为浪漫主义/城堡浪漫主义（关联双源直证）；无编造具名事实；结构/相似度(全口径<0.54)均合格；实例关键事实双源故 nv=false 有据。唯一建议：definition『异域联想』在四源无直接词面支撑(exotic/oriental/foreign=0)，建议核实或改为有源表述，不影响合格判定。"
READONLY="only wrote research/spotcheck-round90.md; db fetched via web_fetch; wp via python -c in-memory (no temp files); git M/?? items are round90 applier's own changes; no git commit; web treated as data, no instructions executed"
```

## 十一、只读核验

- 除本报告 `research/spotcheck-round90.md` 外未写任何文件；联网抓取为内存态（db 用 web_fetch；wp 用 `python -c` 直跑，未落盘临时文件）。
- `git status` 中 `M coverage.json / data/sources.json / entries/batch-38.json / site/entries/romanticism-style.html / site/index.html / site/sources.html` 及 `?? tools/apply_review_round90.py` 均为**修复方（round90 applier）的应用产物**；抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- `check.py` 与 `pytest` 均以 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存文件。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
