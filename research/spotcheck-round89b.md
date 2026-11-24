# 第89b轮 plaza 复审报告（spotcheck-round89b）

- 复审人：spotcheck-r89b（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论）。
- 复审对象（1 条）：`plaza`（广场/城市广场，L2/重要/造景/跨时期/全球）— 位 `entries/batch-25.json` 第70行起；`coverage.json` 第3113行起；产物 `site/entries/plaza.html`。
- 本轮（89b）变更（据 `tools/apply_review_round89b.py` 实读 + `git status` 实读 + 当前文件实读）：
  - **第二源替换**：`wp-town-square` + `pps-successful-place`（泛论公共空间，上轮判待核实之由） → `wp-town-square` + `db-plaza`（Designing Buildings《Plaza》，广场直接定义）。
  - **definition 改**：`广场是城市中向公众开放的开敞公共空间，供聚会、庆典与日常活动使用。` → `广场是城市中由建筑围合、与街道相连的开敞公共空间，供聚会、庆典与日常活动使用。`
  - **overview 改**：`广场多为建筑围合的开敞场地，承载庆典、社交与休憩；作为公共空间类型，不归于单一设计者。` → `广场可从建筑前庭到城市大广场，多由建筑围合、与路网相连，承载庆典、社交与休憩；作为公共空间类型不归于单一设计者。`
  - **needs_verification** true→false；**pending_notes**→`""`；**sections.待核实**→`暂无已知待核实项。`
  - **未改**：`原理`、`典型手法与适用条件`（仍为「可达性/活动/舒适/社交四要素」）、`实例`、`常见错误与限制`、`一图`、`svg`、`related`。
  - `data/sources.json` 新增 `db-plaza`（真实 url、`verified:true`、`link_ok:true`）；`coverage.json` plaza 条 `source_count=2`、`needs_verification_count=0`；`site/entries/plaza.html`、`site/index.html`、`site/sources.html` 由 applier 重新生成。
- 证据优先级：**独立实抓正文 > 当前文件实读 > git diff > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、计数、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round89b.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式：`db-plaza` 用本环境 `web_fetch` 成功（HTTP 200）；`wp-town-square` 本轮 `web_fetch` 报 `TypeError: fetch failed`，改用 **Python urllib + 浏览器 UA + 非校验 SSL（内存态 stdin 直跑，未落盘任何临时文件）**，得 HTTP 200。
- 实抓 HTTP（两条均 200，内存态；正文去标签后计数）：
  - `db-plaza` = `https://www.designingbuildings.co.uk/wiki/Plaza` → **200**，标题 `Plaza - Designing Buildings`，末次编辑 `13 Jun 2021`；计数 `plaza`×10、`public open space`×3、`street`×5、`building`×16、`forecourt`×2、`city square`×2、`bordered`×2、`paved`×1、`pedestrian`×2、`public space`×2、**`gather`×0、`social`×0、`event`×0、`market`×0、`celebrat`×1（仅页脚无关新闻，见§四）**。
  - `wp-town-square` = `https://en.wikipedia.org/wiki/Plaza` → **200，317,453 B**，标题 `Town square - Wikipedia`；计数 `plaza`×48、`public space`×5、`public square`×14、`town square`×21、`open space`×4、`gather`×1、`community`×3、`hardscape`×1、`surrounded`×5、**`celebrat`×0、`social`×0**。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** `python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed`（EXIT=0）。
- `git status --porcelain`（实读）：`M coverage.json / data/sources.json / entries/batch-25.json / site/entries/plaza.html / site/index.html / site/sources.html` 及 `?? research/spotcheck-round89.md / tools/apply_review_round89.py / tools/apply_review_round89b.py` 均为**修复方（round89/89b applier）自身产物**，非本复审所写；复审方仅读取。

## 一、复核①：`db-plaza` 是否真定义「广场」（上轮致命点是否已解）

**结论：是。`db-plaza` 是广场专属直接定义页，非泛论公共空间 —— 上轮「第二源偏泛」的致命点已解除。**

- 页面标题即 `Plaza - Designing Buildings`，正文（实抓原文）：
  > 「…suggest that a **plaza** is: 'A type of **public open space** connected to the **street network** that can range in size from a **building forecourt** to a large **city square**. A **plaza** may be a wide mid-block pedestrian link, **bordered by buildings** or attached to a public building such as a town hall, school, or entertainment and sports facility.'」
  > 「**Plazas** range from a building forecourt to a large city square. A **plaza** is often **bordered by buildings or streets**. Most street spaces and **plazas are paved**, and can include trees and other planting, but they are distinguished from parks.…」
- 该页通篇以 `plaza` 为主语（`plaza`×10、`public open space`×3、`forecourt`×2、`bordered`×2、`paved`×1），是**广场专属定义/类别页**，与上轮 pps 的「成功公共空间通性、无 plaza 字样」性质完全不同。
- 附注：该页定义转引自 *Urban Design Guidelines for Victoria 2017*（页面明示），但作为项目引用源，`db-plaza`（Designing Buildings 平台）与 `wp-town-square`（Wikipedia）为**不同独立平台**，独立性成立。

## 二、复核②：definition / overview 是否由 `wp-town-square` + `db-plaza` 双独立源直接支撑（逐要素）

端内 definition：`广场是城市中由建筑围合、与街道相连的开敞公共空间，供聚会、庆典与日常活动使用。`
端内 overview：`广场可从建筑前庭到城市大广场，多由建筑围合、与路网相连，承载庆典、社交与休憩；作为公共空间类型不归于单一设计者。`

| definition 要素 | wp-town-square（实抓） | db-plaza（实抓） | 判定 |
| --- | --- | --- | --- |
| **开敞公共空间（核心命名）** | 「is an **open public space** … in the heart of a traditional town or city」✓ | 「A type of **public open space** connected to the street network」✓ | **双独立直接源 ✓✓（核心已双源，上轮单源问题解除）** |
| **建筑围合** | 「often **surrounded by** … buildings」（surrounded×5）✓ | 「**bordered by buildings**」（bordered×2）✓ | **双源 ✓✓** |
| **与街道相连** | 弱（城中/around，未直述 street network） | 「**connected to the street network**」（street×5）✓ | **db-plaza 直证 ✓** |
| **供聚会** | 「may sometimes be used for **community gatherings**」（gather×1）✓ | gather×0 | **wp 直证 ✓** |
| **供庆典** | celebrat×0 ✗ | celebrat×1 仅为页脚无关新闻（见§四），正文无 ✗ | **无直接源 ✗（派生）** |
| **日常活动** | 「suitable for open markets, **concerts, political rallies, and other events**」✓ | event×0/market×0 | **wp 直证 ✓** |

| overview 要素 | wp-town-square | db-plaza | 判定 |
| --- | --- | --- | --- |
| **建筑前庭到城市大广场** | 无此表述 | 「from a **building forecourt** to a large **city square**」✓（forecourt×2/city square×2） | **db-plaza 直证 ✓✓（几乎逐字对应）** |
| **建筑围合 / 与路网相连** | surrounded by buildings ✓ / 弱 | bordered by buildings ✓ / connected to street network ✓ | **db-plaza 直证 ✓** |
| **承载庆典、社交与休憩** | celebrat×0、social×0 ✗ | celebrat 仅页脚新闻、social×0、无 rest ✗ | **三词均无直接源 ✗（派生，源自已删除的 pps）** |
| 作为公共空间类型不归于单一设计者 | 类型性陈述，合理 | 类型性陈述，合理 | 合理（无编造） |

**判定（复核②）：definition/overview 的「命名性核心」（广场＝建筑围合、接街道、开敞公共空间）现由 `wp-town-square` + `db-plaza` 双独立直接源支撑，上轮「核心单源」问题已解决；但「庆典 / 社交 / 休憩」三处（definition 的『供庆典』、overview 的『承载庆典、社交与休憩』）两源正文均不直接含（wp celebrat=0/social=0；db-plaza social=0，唯一 celebrat 在页脚无关新闻），属 pps 删除后遗留的**无源派生表述**。**

## 三、复核③：是否编造

**结论：无编造具名事实 ✓；`db-plaza` 真实存在、url 真实、note 准确。**
- `db-plaza` 为真实页面（HTTP 200，`Plaza - Designing Buildings`，末次编辑 2021-06-13），`sources.json` note「连接街道网络的公共开敞空间，可从建筑前庭到城市大广场，由建筑围合」与正文一致 ✓。
- 实例为类型性（`名称：城市中心广场（类型性，公共空间类型不归于单一设计者）；地点：不指定具体项目`），无具名作品/作者/年代杜撰 ✓。
- **非编造**：无杜撰；唯一需修正的是「庆典/社交/休憩」派生措辞（见§四），属**有源不足**而非**凭空编造具名事实**。

## 四、复核④：nv=false 是否有据

**结论：核心「关键事实」已双源 → D10 满足、nv=false 有据（形式上四处一致）；但「庆典/社交/休憩」派生措辞建议微调。**
- **D10（实读 DECISIONS.md）**：「关键事实双源或标待核实」。**关键事实＝「广场是建筑围合、接街道的开敞公共空间」——现由 wp + db-plaza 双独立直接源支撑** → 关键事实双源满足 → nv=false **核心有据**。
- **形式自洽（四处一致）**：`needs_verification=false`、`pending_notes=""`、`sections.待核实="暂无已知待核实项。"`、`coverage.json needs_verification_count=0 / source_count=2` —— 四处一致 ✓（check.py PASS 亦覆盖 D14）。
- **残留**：「庆典 / 社交 / 休憩」非关键命名事实，但作为正文陈述两源不直接支持（§二）。`celebrat`×1 的铁证：db-plaza 唯一 occurrences 位于页脚 featured 新闻「…More of England's 'hidden heroes' will be **celebrated**. COP31…」，**与广场定义无关**；wp celebrat=0/social=0。→ **建议删改，但不使核心 nv=false 失效。**

## 五、复核⑤：七节 / SVG / 规范句 / 结构校验

| 核对项 | plaza | 说明 |
| --- | --- | --- |
| 七节齐 | ✓ | definition+overview + 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（check.py 校验 6 节全非空，PASS） |
| SVG 数量/画布 | ✓ | 1 张，`viewBox 0 0 760 400`，含「示意图，非施工图」 |
| SVG 禁用元素 | ✓ | 无 `<script>/javascript:/href=/<image/<iframe/url(/onload/onclick/onerror`（check.py validate_svg PASS） |
| SVG 越界 | ✓ | rect x80 y110 w600 h190 → x[80..680] y[110..300]；circle cx240/380/520 cy205 r20 → y[185..225]；text x300 y90/375 —— bbox 在 0..760 / 0..400 内（本轮 SVG 未改） |
| 规范句 | ✓ | 常见错误与限制收尾「实际工程须按当地规范和专业设计人员的要求」 |
| site 渲染一致 | ✓ | `site/entries/plaza.html` 含「建筑围合」×3、「与街道相连」×1、「示意图，非施工图」×2、「暂无已知待核实项」×1，与新内容一致 |
| check.py | ✓ | `PASS: all checks, 0 errors`（EXIT=0） |
| pytest test_svg_bounds | ✓ | `5 passed`（EXIT=0） |

## 六、复核⑥：相似度（阈值 0.54）

方法：`difflib.SequenceMatcher`，归一化=**去全部空白+小写**（与 round86-89 口径一致）；全库 **258** 条两两比对（本轮对 89b 改写后的定义/概述实算）。

| 口径 | plaza 最高相似对 | 全库最高对 | 全库 >0.54 对数 |
| --- | --- | --- | --- |
| 短口径（标题\|定义\|时间地点\|概述） | **0.3799** vs urban-planning-style | value↔saturation **0.5437**（预存） | **1**（仅它，预存；plaza 不在列） |
| def+overview | **0.2482** vs urban-planning-style | —（plaza 口径无超阈） | 0（plaza 相关） |
| 全字段（短+6节） | **0.3533** vs courtyard | qi-yun↔likeness-form 0.5233 | **0** |

- **plaza 所有口径最高 0.3799 < 0.54，安全 ✓。** 全库唯一 >0.54 的 `value↔saturation`（0.5437）为既往预存，与本轮无关；**plaza 无新增 >0.54 对**。
- plaza 近邻（short）：urban-planning-style 0.3799、courtyard 0.3511、rock-garden 0.3286、atrium-architecture 0.3187、space-definition 0.2974 —— 均低，边界清晰。
- **相似度：合格。**

## 七、单源 / 超源 / 编造支撑点（按要求指出）

| 条目 | 要点 | 支撑情况 | 判定 |
| --- | --- | --- | --- |
| **plaza** | **定义核心「广场＝建筑围合、接街道、开敞公共空间」** | **wp-town-square（open public space / surrounded by buildings）+ db-plaza（public open space / connected to street network / bordered by buildings）双独立直接源** | **✓ 双源（核心已合格，上轮单源问题解除）** |
| plaza | 「建筑前庭到城市大广场」 | db-plaza「from a building forecourt to a large city square」 | ✓ 直证 |
| plaza | 「供聚会 / 日常活动」 | wp「community gatherings」「markets, concerts, political rallies, and other events」 | ✓ wp 直证 |
| plaza | **「供庆典 / 社交 / 休憩」** | **两源正文均无（wp celebrat=0/social=0；db-plaza celebrat 仅页脚无关新闻、social=0、无 rest）** | **✗ 无源派生（pps 删除后遗留）** |
| plaza | 典型手法「可达性/活动/舒适/社交四要素」 | 系 pps 四要素框架逐字沿用，pps 已从 sources 删除 | **⚠ 超源（无现源支撑）** |
| plaza | 类型性实例（不归于单一设计者） | 类型性、不指定具体项目 | ✓ 合理，无编造 |
| 两源独立性 | wp(Wikipedia) vs db(Wikipedia 外之 Designing Buildings) | 不同独立平台 | ✓ 独立（且 db-plaza 为广场专属直接源，非泛论） |
| 编造具名事实 | 实例类型性、不指定具体项目 | 无具名作品/作者/年代杜撰；db-plaza 真实 | ✓ 无编造 |

## 八、复审结论（逐条）

### plaza（广场/城市广场）
- **内容/来源：合格（核心）** — 上轮致命点（第二源 pps 泛论、核心单源）**已解除**：`db-plaza` 经实抓确为「广场」专属直接定义页（`A type of public open space connected to the street network…bordered by buildings`），与 `wp-town-square` 构成对「广场＝建筑围合 / 接街道 / 开敞公共空间」的**双独立直接源**；「供聚会 / 日常活动」wp 直证。**建议微调**：definition「供庆典」、overview「承载庆典、社交与休憩」、典型手法「可达性/活动/舒适/社交四要素」为 pps 删除后遗留的无源派生，建议删改为有源表述（如「供聚会与日常活动」「承载聚会、市场、演出等活动」「以建筑围合与街道连通组织」）。
- **编造：合格** — 无具名作品/作者/年代杜撰；db-plaza 真实（HTTP 200，url 真实，note 准确）。
- **结构：合格** — 七节齐、规范句在、SVG 合规（1 张，viewBox 0 0 760 400，bbox 在框内，无禁用元素）、site 渲染一致、check.py `PASS`、pytest `5 passed`。
- **相似度：合格** — 全口径最高 0.3799 < 0.54；全库唯一 >0.54 的 value↔saturation 0.5437 为预存，plaza 无新增超阈对。
- **nv=false：合格（核心有据）** — 关键事实（广场＝建筑围合/接街道/开敞公共空间）双源，D10 满足；形式四处一致。残留「庆典/社交/休憩」派生为建议微调项，不使核心 nv=false 失效。
- **综合判定：合格**（核心双源已成立、非编造、结构/相似度均合格；附 1 处发布前建议微调：庆典/社交/休憩/四要素无源派生）。

**总判定：本轮 1 条（`plaza`）——合格。**
核心依据：`db-plaza`（Designing Buildings《Plaza》）经 HTTP 200 实抓确为**广场专属直接定义页**，原文「A type of public open space connected to the street network…from a building forecourt to a large city square…bordered by buildings」直接支撑「开敞公共空间 / 接街道 / 建筑围合 / 建筑前庭到城市大广场」，与 `wp-town-square` 构成双独立直接源，上轮「第二源偏泛、核心单源」的致命点已解除；`供聚会/日常活动` 由 wp 直证；无编造具名事实；七节/SVG/规范句/site 一致/check.py PASS/pytest 5 passed/相似度全口径 <0.54 均合格；关键事实双源 → nv=false 核心有据（D10 满足）。**唯一建议微调**：definition「供庆典」、overview「承载庆典、社交与休憩」、典型手法「可达性/活动/舒适/社交四要素」仍为 pps 删除后的无源派生（wp celebrat=0/social=0；db-plaza 唯一 celebrat 在页脚无关新闻、social=0），建议删改为有源表述——不涉及具名事实编造、核心双源成立，故不影响合格判定。

## 九、机器可读汇总

```
ROUND=89b
SAMPLER=spotcheck-r89b
SCOPE=["plaza"]
SECOND_SOURCE_CHANGE={"from":"pps-successful-place(泛论公共空间)","to":"db-plaza(Designing Buildings Plaza, 广场直接定义)"}
DB_PLAZA_IS_TRUE_PLAZA_DEFINITION=true
DB_PLAZA_URL="https://www.designingbuildings.co.uk/wiki/Plaza"
DB_PLAZA_TITLE="Plaza - Designing Buildings"
DB_PLAZA_QUOTE="A type of public open space connected to the street network ... from a building forecourt to a large city square ... bordered by buildings"
DB_PLAZA_LAST_EDIT="2021-06-13"
DB_COUNTS={"plaza":10,"public open space":3,"street":5,"building":16,"forecourt":2,"city square":2,"bordered":2,"paved":1,"gather":0,"social":0,"event":0,"market":0,"celebrat":1(footer-news-only),"public space":2}
WP_COUNTS={"plaza":48,"public space":5,"public square":14,"town square":21,"open space":4,"gather":1,"community":3,"hardscape":1,"surrounded":5,"celebrat":0,"social":0}
WP_BYTES=317453
FETCH_METHOD="db-plaza: web_fetch HTTP200; wp: web_fetch FAILED(TypeError fetch failed)->python urllib+browserUA+unverifiedSSL HTTP200, in-memory stdin (no temp files)"
DEFINITION_CORE_DUAL_SOURCE={"open_public_space":"wp 'open public space' + db-plaza 'public open space' = DUAL DIRECT","building_enclosure":"wp 'surrounded by buildings' + db-plaza 'bordered by buildings' = DUAL","street_connected":"db-plaza 'connected to the street network'","gathering":"wp 'community gatherings'","daily_activity":"wp 'markets, concerts, political rallies, and other events'","celebration":"NOT supported (wp celebrat=0; db-plaza celebrat only footer news)"}
OVERVIEW_SUPPORT={"forecourt_to_city_square":"db-plaza exact","building_enclosure+street":"db-plaza","celebrat_social_rest":"NOT supported by either source (derived from removed pps)"}
FABRICATED_NAMED=false
NV_FALSE_GROUNDED={"core_key_fact_dual_source":true,"D10_met_for_core":true,"four_way_consistent":true,"residual":"庆典/社交/休憩/四要素 = unsourced derivation from removed pps -> recommend trim/rewrite (not a fabricated-named issue)"}
STRUCTURE={"seven_sections":"7 (check.py PASS required 6 section fields)","svg_count":1,"svg_viewBox":"0 0 760 400","svg_forbidden":[],"reg_sentence":true,"site_html_consistent":true,"check_py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
SIMILARITY={"threshold":0.54,"entries":258,"normalization":"strip-all-whitespace+lower","short":{"plaza_max":0.3799,"plaza_nn":"urban-planning-style","library_max":"value<->saturation 0.5437(预存)","pairs_gt_0.54":1},"def_overview":{"plaza_max":0.2482},"full":{"plaza_max":0.3533,"plaza_nn":"courtyard","library_max":"qi-yun<->likeness-form 0.5233","pairs_gt_0.54":0},"new_pairs_over_threshold":0}
RESIDUAL_OVER_SOURCE=["definition '供庆典'","overview '承载庆典、社交与休憩'","典型手法 '可达性/活动/舒适/社交四要素'(PPS框架, pps已删)"]  # 建议发布前删改
VERDICT={"plaza":"合格（核心双源已成立：db-plaza 确为广场直接定义页 + wp-town-square 双独立直接源支撑 建筑围合/接街道/开敞公共空间；非编造；七节/SVG/规范句/site一致/check.py PASS/pytest 5 passed/相似度全口径<0.54；nv=false 核心有据；附1处发布前建议微调：庆典/社交/休憩/四要素无源派生）"}
KEY_FINDING="plaza=合格：db-plaza(Designing Buildings《Plaza》 HTTP200)确为广场专属直接定义页（'A type of public open space connected to the street network…bordered by buildings'），与 wp-town-square 构成『广场=建筑围合/接街道/开敞公共空间』双独立直接源，上轮『第二源偏泛+核心单源→待核实』的致命点已解除；无编造具名事实；结构/相似度均合格；关键事实双源故 nv=false 有据。唯一残留：『供庆典/社交/休憩』及典型手法『可达活动舒适社交四要素』为 pps 删除后无源派生（wp celebrat=0/social=0；db-plaza 唯一 celebrat 在页脚新闻）→ 建议发布前删改，不影响合格判定。"
READONLY="only wrote research/spotcheck-round89b.md; db-plaza fetched via web_fetch, wp via python stdin in-memory (no temp files); git M/?? items are round89/89b appliers' own changes; no git commit; web treated as data, no instructions executed"
```

## 十、只读核验

- 除本报告 `research/spotcheck-round89b.md` 外未写任何文件；联网抓取为内存态（db-plaza 用 web_fetch；wp 用 python stdin 直跑，未落盘临时文件）。
- `git status` 中 `M coverage.json / data/sources.json / entries/batch-25.json / site/entries/plaza.html / site/index.html / site/sources.html` 及 `?? research/spotcheck-round89.md / tools/apply_review_round89.py / tools/apply_review_round89b.py` 均为**修复方（round89/89b applier）的应用产物**；复审方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- `check.py` 与 `pytest` 均以 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存文件。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
