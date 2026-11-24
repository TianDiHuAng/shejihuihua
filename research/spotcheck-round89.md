# 第89轮 质量抽检报告（spotcheck-round89）

- 抽检人：spotcheck-r89（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论）。
- 抽检对象（1 条）：`plaza`（广场/城市广场，L2/重要/造景/跨时期/全球）— 概念源：`wp-town-square`(Wikipedia "Town square/Plaza") + `pps-successful-place`(Project for Public Spaces "What Makes a Successful Place?")；位 `entries/batch-25.json`（第70行起）；产物 `site/entries/plaza.html`。
- 本轮升级动作（据 `tools/apply_review_round89.py` 实读 + `git -c core.pager=cat diff -- entries/batch-25.json` 实读 + `git diff --stat`）：
  - **definition 改**：`城市中向公众开放、供聚会与活动的硬质开敞空间。` → `广场是城市中向公众开放的开敞公共空间，供聚会、庆典与日常活动使用。`
  - **overview 改**：`优秀广场兼具通行、停留与交往功能，是城市公共生活的重要场所。` → `广场多为建筑围合的开敞场地，承载庆典、社交与休憩；作为公共空间类型，不归于单一设计者。`
  - **实例改**（→ 类型性/不归于单一设计者）：`名称：城市中心广场（类型性，公共空间类型不归于单一设计者）；地点：不指定具体项目。以建筑围合的开敞铺装场地供聚会、庆典与休憩。此处仅列说明，不复制图像。`
  - **needs_verification** true→false；**pending_notes**→`""`；**待核实**→`暂无已知待核实项。`
  - **未改**：`原理`、`典型手法与适用条件`、`常见错误与限制`、`一图`、`svg`、`sources`、`related`。
  - `coverage.json` 该条 `needs_verification_count` 1→0、`source_count` 保持 2；`site/entries/plaza.html`、`site/index.html` 为本轮 applier 重新生成（`git diff --stat`：4 文件 12 增 12 删）。
- 证据优先级：**独立实抓正文 > 当前文件实读 > git diff > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、计数、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round89.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式：`web_fetch` 本环境历史报错（DECISIONS D05），改用 **Python urllib + 浏览器 UA + 非校验 SSL（内存态 stdin 直跑，未落盘任何临时文件）**。
- 实抓 HTTP（两条均 200，内存态；正文去标签后字符数）：
  - `wp-town-square` = `https://en.wikipedia.org/wiki/Plaza` → **200，319,276 B（正文 ~28,721 字）**，标题 `Town square - Wikipedia`；计数 `plaza`×48、`public space`×5、`public square`×14、`town square`×21、`gather/gathering`×1、`community`×3、`open space`×4、**`celebrat`×0、`social`×0**。
  - `pps-successful-place` = `https://www.pps.org/article/grplacefeat` → **200，41,561 B（正文 ~9,721 字）**，标题 `What Makes a Successful Place?`；计数 **`plaza`×0、`public square`×0、`town square`×0、`open space`×0、`civic`×0**、`public space`×9、`celebrat`×1、`social`×4、`community`×4、`gather`×1、`market`×9。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** `python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed`（EXIT=0）。
- `git status --porcelain`（实读）：`M coverage.json / entries/batch-25.json / site/entries/plaza.html / site/index.html` 及 `?? tools/apply_review_round89.py` 均为**本轮修复方（apply_review_round89.py）自身产物**，非本抽检所写；抽检方仅读取（另：`.pytest_cache` mtime 10:34:20，早于本会话 10:52，非本轮产生）。

## 一、核对①：definition/overview 是否由两源正文直接支撑（公开开敞空间/聚会庆典社交）

端内 definition：`广场是城市中向公众开放的开敞公共空间，供聚会、庆典与日常活动使用。`
端内 overview：`广场多为建筑围合的开敞场地，承载庆典、社交与休憩；作为公共空间类型，不归于单一设计者。`

**两源关键原文（实抓）**
- `wp-town-square` 定义句：**「A town square (or public square, urban square, city square or simply square), also called a plaza or piazza, is an open public space commonly found in the heart of a traditional town or city, and which may sometimes be used for community gatherings.」**
  另有：`the plaza remains a center of community life that is only equaled by the market-place.`；`Most squares are hardscapes suitable for open markets, concerts, political rallies, and other events...`；`town squares are often surrounded by small shops...`；`It is often surrounded by governmental buildings, churches, and other structures...`
- `pps-successful-place` 关键句：**「Great public spaces are those places where celebrations are held, social and economic exchanges occur, friends run into each other, and cultures mix.」**（全篇是「成功公共场所四要素：可达 / 有活动 / 舒适 / 社交」的通用框架，举例为图书馆、市场等一切公共空间）

| definition / overview 要素 | wp-town-square（实抓） | pps-successful-place（实抓） | 判定 |
| --- | --- | --- | --- |
| **广场 = 城市中向公众开放的「开敞公共空间」** | **「…also called a plaza… is an open public space commonly found in the heart of a traditional town or city」** | **无**：全篇无 `plaza/public square/town square/open space`（count 均 0），仅泛称 `public spaces` | **仅 wp 单源直证；pps 不支撑** |
| 供**聚会** | 「may sometimes be used for **community gatherings**」 | — | wp 直证 |
| 供**庆典** | 无（`celebrat`×0） | 「Great public spaces… **celebrations are held**」（泛称，非指广场） | pps 仅泛证 |
| 供**社交** | 无（`social`×0）；「center of community life」 | 「**social** and economic exchanges occur」（泛称） | pps 泛证 |
| 供**日常活动** | 「concerts, political rallies, and other events」 | 「people are engaged in **activities** there」 | 泛证 |
| overview：**建筑围合的开敞场地** | 「open public space」+「often **surrounded by** … **buildings**/shops」 | 无 | **wp 支撑** |
| overview：**承载庆典、社交与休憩** | 活动/社区生活 | 庆典/社交/舒适(sit, comfortable) | 庆典社交 pps 泛证、休憩 pps |

**判定（核对①）：definition 的核心「广场 = 城市中向公众开放的开敞公共空间」由 `wp-town-square` 单独直证；pps 全篇不含 `plaza/public square/town square/open space`，只提供泛化的「成功公共空间=有庆典/社交」通性。即：所谓「概念双源」只在极泛的『公共空间 + 庆典社交』层面成立，对「广场」这一命名的核心定义实为 wp 单源。**

### 1.1 特别判断：PPS 页是否构成对「广场」定义的第二独立直接源？

- **该页题为 `What Makes a Successful Place?`**，正文是「成功公共空间四要素」的**通用成功框架**（accessible / activities / comfortable / sociable），覆盖面是**一切公共空间**（公园、图书馆、市场等；文中即以 All Access Library、Market Cities 为例），**不是广场专属页，也不定义广场**。
- **客观计数铁证**：`plaza`×0、`public square`×0、`town square`×0、`open space`×0、`civic`×0；它仅为「Great public spaces… celebrations are held, social… exchanges occur」——描述的是**「great public spaces」的通性**，而非「广场」。
- **结论：PPS 仅泛论公共空间（成功公共场所），不构成对「广场」定义的第二独立直接源。** 依任务指令「若偏泛/单源请判待核实」——**判待核实**。

## 二、核对②：两源是否独立

- `wp-town-square`（Wikipedia，权威百科，en.wikipedia.org）与 `pps-successful-place`（Project for Public Spaces，官方机构，pps.org）为**不同独立平台/机构**，独立性成立 ✓。
- **但：独立 ≠ 直接。** pps 虽独立，却是**泛化的成功公共空间通性页**，不能补足「广场=开敞公共空间」这一命名性定义，见 §1.1。

## 三、核对③：类型性实例是否合理 / 是否编造

**结论：类型性处理合理 ✓；无编造具体事实 ✓（但庆典/休憩的落点偏 pps 泛证）。**
- 端内实例：`名称：城市中心广场（类型性，公共空间类型不归于单一设计者）；地点：不指定具体项目。以建筑围合的开敞铺装场地供聚会、庆典与休憩。此处仅列说明，不复制图像。`
- 「广场」是**公共空间类型**，不归于单一设计者；地点不指定具体项目——**类型性合理**，与 `tints-shades`（batch-37，nv=false，技法/练习作类型性、地点作者不适用）先例同口径 ✓。
- **无编造**：无具名作品/作者/年代被杜撰。
- 细节可溯：`建筑围合`→wp「often surrounded by … buildings/shops」✓；`开敞`→wp「open public space」✓；`硬质铺装`（原理）→wp「Most squares are hardscapes」✓；`聚会`→wp「community gatherings」✓；`庆典`→pps（泛）；`休憩`→pps comfort。均无超源臆造。
- **先例一致（实读库内条目）**：`tints-shades` 亦把「技法/练习」作类型性、地点作者不适用并 nv=false——本轮 plaza 的类型性与之同一路数 ✓。

## 四、核对④：nv=false 是否有据

**结论：结构自洽（形式）✓，但 D10 双源支撑（实质）不足 → nv=false 依据不足。**
- **形式自洽（四处一致）**：`needs_verification=false`、`pending_notes=""`、`待核实="暂无已知待核实项。"`、`coverage.json` `needs_verification_count=0`、`source_count=2`——四处一致 ✓。
- **实质不足**：DECISIONS D10 要求「关键事实双源或标待核实」。**核心定义「广场=开敞公共空间」仅 wp 单源直证，pps 为泛论「成功公共空间」的通性页、非广场专属直接源**（§1.1）。**双源要求未满足 → 不应置 nv=false。**
- 与 round87 对照：round87 的 `opposed-scenery`（概念实质单源）、`korean-architecture`（单源+超源）被判待核实；**本轮 plaza 属同一类问题——定义核心单源（wp），pps 偏泛不能补足** → 应维持待核实（needs_verification=true）。
- 遂：**本轮 nv=false 升级不成立；正确状态应为 `needs_verification=true`**，pending/待核实 写明：「广场『开放公共空间』核心单源（wp-town-square），pps（What Makes a Successful Place?）为泛论成功公共空间、非广场专属直接源，待补第二直接源」。

## 五、核对⑤：七节 / SVG / 规范句 / 结构校验

| 核对项 | plaza | 说明 |
| --- | --- | --- |
| 七节齐 | ✓ | definition+overview + 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实 = 7 |
| SVG 数量/画布 | ✓ | 1 张，`viewBox 0 0 760 400`，含「示意图，非施工图」 |
| SVG 禁用元素 | ✓ | 无 `<script>/javascript:/href=/<image/<iframe/url(/onload/onclick/onerror` |
| SVG 越界（实算 bbox） | ✓ | 实算 bbox `x[80..680] y[90..375]`，在 0..760 / 0..400 内（rect x80 y110 w600 h190；circle cx240/380/520 cy205 r20；text x300 y90、x300 y375） |
| 规范句 | ✓ | 常见错误与限制收尾含「实际工程须按当地规范和专业设计人员的要求」 |
| nv / pending / 待核实 一致 | ✓（形式） | nv=false、pending=""、待核实="暂无已知待核实项。"（但实质依据不足，见 §四） |
| check.py | ✓ | `PASS: all checks, 0 errors`（EXIT=0） |
| pytest test_svg_bounds | ✓ | `5 passed`（EXIT=0） |

- 注：本轮 SVG **未改**（diff 只动 definition/overview/实例/nv），bbox 在框内，无越界。结构层面全部合规。

## 六、核对⑥：相似度（阈值 0.54）

方法：`difflib.SequenceMatcher`，归一化=**去全部空白+小写**（与 round86/87/88 口径一致；复现全库短口径最高 `value↔saturation 0.5437`）。全库 **258** 条两两比对（短口径 33,153 对）。

| 口径 | plaza 最高相似对 | 全库最高对 | 全库 >0.54 对数 |
| --- | --- | --- | --- |
| 短口径（标题\|定义\|时间地点\|概述） | **0.3711** vs rock-garden | value↔saturation **0.5437**（预存） | **1**（仅它，预存；plaza 不在列） |
| def+overview | **0.2745** vs rock-garden | leaked-scenery↔time-scenery 0.4192 | 0 |
| 全字段（短+6节） | **0.3876** vs rock-garden | loop-route↔serial-route 0.5311 | 0 |

- **plaza 所有口径最高 0.3876 < 0.54，安全 ✓。** 全库唯一 >0.54 的 `value↔saturation`（0.5437）为既往预存，与本轮无关；plaza 无新增 >0.54 对。
- plaza 近邻（short）：rock-garden 0.3711、urban-planning-style 0.3625、openness 0.3484、courtyard 0.3314、placemaking 0.3293——均低，边界清晰。
- **相似度：合格。**

## 七、单源 / 超源 / 编造支撑点（按要求指出）

| 条目 | 要点 | 支撑情况 | 判定 |
| --- | --- | --- | --- |
| **plaza** | **定义核心「广场=城市中向公众开放的开敞公共空间」** | **仅 wp-town-square 单源直证**（"also called a plaza… is an open public space… in the heart of a traditional town or city"）；**pps 不含 plaza/square/open space（count=0）**，非直接源 | **单源要害（定义核心）** |
| plaza | 「供聚会」 | wp「community gatherings」 | wp 单源 |
| plaza | 「供庆典 / 社交」 | 仅 pps 泛证（"Great public spaces… celebrations are held, social… exchanges"），非广场专属 | **泛证（非直接）** |
| plaza | 「建筑围合 / 开敞 / 硬质铺装」 | wp（surrounded by buildings / open public space / hardscapes） | ✓ 有据 |
| plaza | 类型性实例（不归于单一设计者） | 类型性，与 tints-shades 先例同口径 | ✓ 合理，无编造 |
| 两源独立性 | wp(Wikipedia) vs pps(Project for Public Spaces) | 不同独立平台 | ✓ 独立（但 pps 偏泛，非直接源） |
| 编造具名事实 | 实例类型性、不指定具体项目、不复制图像 | 无具名作品/作者/年代杜撰 | ✓ 无编造 |

- **核心问题：定义核心（开敞公共空间）单源（wp）；pps 是泛论成功公共空间的通性页，不构成「广场」定义的第二独立直接源。** 其余细节与实例均有据、无编造。

## 八、抽检结论（逐条）

### plaza（广场/城市广场）
- **内容/来源：待核实** — 定义核心「广场=城市中向公众开放的开敞公共空间」**仅 `wp-town-square` 单源直证**；`pps-successful-place`（题 `What Makes a Successful Place?`）通篇不含 `plaza/public square/town square/open space`（count 全 0），只是泛论「成功公共空间」的通性（celebrations/social exchange），**不构成对「广场」定义的第二独立直接源**。属偏泛、核心单源。
- **类型性/编造：合格** — 实例类型性（公共空间类型不归于单一设计者）、无具名作品/作者/年代杜撰；建筑围合/开敞/硬质铺装均可由 wp 溯源。
- **结构：合格** — 七节齐、规范句在、SVG 合规（1 张，viewBox 0 0 760 400，bbox x[80..680] y[90..375] 在框内，无禁用元素）、check.py `PASS`、pytest 5 passed。
- **相似度：合格** — 全口径最高 0.3876 < 0.54；全库唯一 >0.54 的 value↔saturation 0.5437 为预存，与本轮无关。
- **nv=false：不合格（依据不足）** — 形式四处自洽，但 D10 双源实质未满足（定义核心单源 wp，pps 偏泛），nv=false 不应成立；应回置 `needs_verification=true`。
- **综合判定：待核实**（问题：pps 非广场专属直接源、定义核心单源 → nv=false 升级依据不足）。

**总判定：本轮 1 条（`plaza`）——待核实。**
核心依据：`wp-town-square` 确证「广场=open public space + community gatherings」；但 `pps-successful-place` 是题为 *What Makes a Successful Place?* 的**成功公共空间通性页**，全篇无 `plaza/square/open space`，只泛述「great public spaces 有庆典/社交」。所谓「概念双源」仅在极泛「公共空间+庆典社交」层面成立，**「广场=开敞公共空间」的命名性定义实为 wp 单源**。因此本轮将 `needs_verification` 置 false 的**依据不足**（违反 D10「关键事实双源或标待核实」），应维持 `needs_verification=true` 并写明单源待补。其余维度（类型性实例合理、无编造、七节/SVG/规范句/check.py PASS/pytest 5 passed、相似度全口径 <0.54）均合格。

## 九、机器可读汇总

```
ROUND=89
SAMPLER=spotcheck-r89
SCOPE=["plaza"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round88.md","entries/batch-25.json(plaza)","data/sources.json(2 srcs)","coverage.json(plaza)","tools/apply_review_round89.py","git diff/stat/status","2 live pages"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
PYTEST_SVG="5 passed (EXIT=0)"
FETCH_METHOD="urllib+browserUA+unverified-SSL, in-memory via python stdin (no temp files)"
FETCHES={"wp-town-square":200,"pps-successful-place":200}
WP_COUNTS={"plaza":48,"public space":5,"public square":14,"town square":21,"gather":1,"community":3,"open space":4,"celebrat":0,"social":0}
PPS_COUNTS={"plaza":0,"public square":0,"town square":0,"open space":0,"civic":0,"public space":9,"celebrat":1,"social":4,"community":4}
ROUND89_CHANGES={"definition":"rewritten","overview":"rewritten","实例":"-> 类型性/不归于单一设计者","needs_verification":"true->false","pending_notes":"-> ''","待核实":"-> 暂无已知待核实项。","原理/典型手法/常见错误/一图/svg/sources":"unchanged","coverage.nv_count":"1->0","applier":"tools/apply_review_round89.py"}
DEFINITION_DUAL_DIRECT={
 "plaza":{"open_public_space":"wp 'also called a plaza... is an open public space... in the heart of a traditional town or city' ONLY; pps has NO plaza/square/open space (count 0)","gathering":"wp 'community gatherings'","celebration":"pps 'Great public spaces... celebrations are held' (GENERIC, not plaza)","social":"pps 'social and economic exchanges occur' (GENERIC)","dual_source":false,"note":"dual holds only at generic 'public space + celebration/social' level; plaza-specific core is single-source wp","fabricated_named":false}}
PPS_SPECIAL_JUDGMENT={"title":"What Makes a Successful Place?","contains_plaza_word":false,"contains_square_word":false,"contains_open_space":false,"nature":"GENERIC successful-public-space framework (accessible/activities/comfortable/sociable), covers parks/libraries/markets","second_independent_direct_source_for_plaza":false,"verdict":"偏泛/单源 -> 待核实"}
INDEPENDENCE={"wp(Wikipedia) vs pps(Project for Public Spaces)":"independent platforms YES","but_independent_ne_direct":true}
INSTANCE_TYPE_LEVEL={"type_level":true,"single_designer":false,"fabricated":false,"detail_traceable":{"建筑围合":"wp surrounded by buildings(shops)","开敞":"wp open public space","硬质铺装":"wp hardscapes","聚会":"wp community gatherings","庆典":"pps(generic)","休憩":"pps comfort"}}
NV_FALSE_GROUNDED={"plaza":false,"reason":"definition core 'open public space' SINGLE-SOURCE wp; pps is generic public-space page, not a plaza direct source -> D10 dual-source NOT met","structure_consistent":"four-way form-consistent but substantively unsupported","correct_state":"needs_verification=true"}
STRUCTURE={"seven_sections":7,"svg_count":1,"svg_forbidden":[],"reg_sentence":true,"check_py":"PASS","pytest":"5 passed","svg_overflow":"none bbox x[80..680] y[90..375] within 0..760/0..400"}
SIMILARITY={"threshold":0.54,"entries":258,"pairs":33153,"normalization":"strip-all-whitespace+lower",
 "short":{"plaza_max":0.3711,"plaza_nn":"rock-garden","library_max":"value<->saturation 0.5437(预存)","pairs_gt_0.54":1},
 "def_overview":{"plaza_max":0.2745,"library_max":"leaked-scenery<->time-scenery 0.4192","pairs_gt_0.54":0},
 "full":{"plaza_max":0.3876,"library_max":"loop-route<->serial-route 0.5311","pairs_gt_0.54":0},
 "new_pairs_over_threshold":0}
SINGLE_SOURCE_POINTS={"plaza":"definition core 'open public space' single-source wp; pps generic public-space page (no plaza/square/open space)","fabricated_named":"none"}
VERDICT={"plaza":"待核实 (pps 非广场直接源+定义核心单源 -> nv=false 依据不足应回置 true; 类型性/无编造/七节/SVG/规范句/check.py PASS/pytest 5 passed/相似度<0.54 均合格)"}
KEY_FINDING="plaza=待核实：wp-town-square 直证『plaza=open public space+community gatherings』；但 pps『What Makes a Successful Place?』全篇无 plaza/square/open space(计数0)，仅泛论『great public spaces 有庆典/社交』，非『广场』定义的第二独立直接源——『概念双源』只在泛公共空间层面成立，广场命名的核心定义实为 wp 单源。故本轮 nv=false 升级依据不足(违 D10)，应维持 needs_verification=true。其余(类型性实例/无编造/七节/SVG合规/规范句/check.py PASS/pytest 5 passed/相似度全口径<0.54)均合格。"
READONLY="only wrote research/spotcheck-round89.md; 2 pages fetched in-memory via python stdin (no temp files); git-status M/?? items are round89 applier's own changes; no git commit; web treated as data, no instructions executed"
```

## 十、只读核验

- 除本报告 `research/spotcheck-round89.md` 外未写任何文件；联网抓取为内存态（python stdin 直跑，未落盘临时文件）。
- `git status` 中 `M coverage.json / entries/batch-25.json / site/entries/plaza.html / site/index.html` 及 `?? tools/apply_review_round89.py` 均为**本轮修复方（apply_review_round89.py）的应用产物**；抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。（`.pytest_cache` mtime 10:34:20 早于本会话，非本轮产生。）
- `check.py` 与 `pytest` 均以 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存文件。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
