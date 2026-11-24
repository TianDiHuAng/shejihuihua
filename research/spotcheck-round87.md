# 第87轮 质量抽检报告（spotcheck-round87）

- 抽检人：spotcheck-r87（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论）。
- 抽检对象（3 条，跨 3 个批次文件）：
  - `opposed-scenery`（对景，核心/造景/古代/中国）— 概念源：`wp-chinese-garden`(Wikipedia, Chinese garden) + `peopleapp-zaoyuan-2`(中国园林博物馆·人民号《造园的艺术手法（二）》)；位 `entries/batch-02-b.json`；产物 `site/entries/opposed-scenery.html`。
  - `leaked-scenery`（漏景，重要/造景/古代/中国）— 概念源：`wp-chinese-garden` + `wp-garden-design`(Wikipedia, Garden design) + `peopleapp-zaoyuan-2`；位 `entries/batch-05.json`；产物 `site/entries/leaked-scenery.html`。
  - `korean-architecture`（韩国建筑，补充/风格/跨时期/东亚）— 概念源：`wp-korean-architecture`(Wikipedia) + `koreanet-hanok-madang`(Korea.net/KOCIS) + `springer-hanok-madang`(Springer, Nexus Network Journal)；位 `entries/batch-38.json`；产物 `site/entries/korean-architecture.html`。
- 本轮升级动作（据 `tools/apply_review_round87.py` 实读 + `git -c core.pager=cat diff` 实读）：三条均改写 `definition`、`overview`、`实例`（→ 类型性/无单一设计者）；`needs_verification` **true → false**、`pending_notes` 清空、`待核实` → "暂无已知待核实项。"。**opposed 额外改 `典型手法与适用条件`（删「……对应关系待核实」句）；三条 SVG、原理、来源未改。** `coverage.json` 三条 `needs_verification_count` 1→0。
- 证据优先级：**独立实抓正文 > 当前文件实读 > git diff > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、计数、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round87.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式：`web_fetch` 本环境历史报错（DECISIONS D05），改用 **Python urllib + 浏览器 UA + 非校验 SSL（内存态 stdin 直跑，未落盘任何临时文件）**。
- 实抓 HTTP（首轮均 200，内存态）：
  - `wp-chinese-garden` = `https://en.wikipedia.org/wiki/Chinese_garden` → 200，491,127 B，正文 ~83,116 字。
  - `wp-garden-design` = `https://en.wikipedia.org/wiki/Garden_design` → 200，320,461 B（正文 ~40,829 字）。
  - `peopleapp-zaoyuan-2` = `https://www.peopleapp.com/rmharticle/30020551454` → 200，74,711 B（正文 ~1,433 字），题《造园的艺术手法（二）》·中国园林博物馆。
  - `wp-korean-architecture` = `https://en.wikipedia.org/wiki/Korean_architecture` → 200，441,575 B（正文 ~55,445 字）。
  - `koreanet-hanok-madang` = `https://www.korea.net/NewsFocus/HonoraryReporters/view?articleId=241777` → 200，96,919 B（正文 ~5,281 字）。
  - `springer-hanok-madang` = `https://link.springer.com/article/10.1007/s00004-016-0292-x` → **200，但仅 3,038 B 的 JS 挑战页**（正文 "Client Challenge … JavaScript is disabled …"，可读文本仅 305 字）。**该源正文当前无法核对。** Crossref 元数据 `10.1007/s00004-016-0292-x` 可确认文章真实存在：*Algorithmic Design Paradigm Utilizing Cellular Automata for the Han-ok*, Nexus Network Journal, 2016-07（无摘要）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** `python -m pytest tests/test_svg_bounds.py -q`：`5 passed`（EXIT=0）。
- `git status` 中 `M coverage.json / entries/batch-02-b.json / entries/batch-05.json / entries/batch-38.json / site/entries/{opposed-scenery,leaked-scenery,korean-architecture}.html / site/index.html` 及 `?? tools/apply_review_round87.py` 均为**本轮修复方（apply_review_round87.py）自身产物**，非本抽检所写；抽检方仅读取。

## 一、核对①：definition / overview 是否由所引来源正文支撑

### 1.1 opposed-scenery（对景）

端内 definition：『对景是在游线或视线的端点布置景物，使行进有明确落点、前后呼应的造园手法。』
端内 overview：『对景把远端厅堂、山石或树木定为视觉目标，令游走产生期待与收束；属传统造园经验，多由匠师群体经手、无单一设计者。』

| 要素 | peopleapp-zaoyuan-2（实抓原文） | wp-chinese-garden（实抓原文） | 判定 |
| --- | --- | --- | --- |
| 相对成景/呼应 | 「登上楼阁……转身上亭榭再观前度楼阁的感觉，大有不同……从甲到乙，与从乙到甲……亭、台、楼、阁、榭，与堂、山、桥、树木乃至花卉，都可为对景」 | **全文无「对景 / opposed / 端点 / culminate」术语**（实抓检索：对景=0、opposed=0、terminate=0） | peopleapp 直证「呼应/互对」；wiki **未直证** |
| 端点布置景物 / 行进落点 | 未见「端点 / 落点 / 布景于视线终点」的字面表述（为释义推演） | 仅泛述「a series of perfectly composed and framed glimpses … a view of a distant mountain peak or a pagoda」（属成景/框取远景，非「对景」机制） | **超源引申**，两源均无直述 |
| 视觉目标为厅堂/山石/树木 | 「堂、山、桥、树木乃至花卉，都可为对景」 | — | peopleapp 支撑要素 ✓ |
| 传统造园经验/无单一设计者 | 讲造园手法，未署具名设计者 | 未署名 | 类型性推断（见§二） |

- **判定：概念核心「相对成景、前后呼应」由 `peopleapp-zaoyuan-2` 直证；`wp-chinese-garden` 全文不出现「对景」术语，只泛述成景/框景，不能直证「对景」机制。definition 里的「视线端点布置景物、使行进有明确落点」在 peopleapp 亦无字面对应，属释义推演。→ 对景概念在引用集内实质偏单源（peopleapp），第二源未直证（详见§六）。**

### 1.2 leaked-scenery（漏景）

端内 definition：『漏景是借漏窗、花墙或稀疏枝叶让景物片段若隐若现的造园手法。』
端内 overview：『漏景不一次揭示全貌，而让景物随步移时断时续地显现，形成含蓄节奏；此类手法为传统经验、无单一设计者。』

| 要素 | peopleapp-zaoyuan-2（实抓原文） | wp-chinese-garden（实抓原文） | wp-garden-design | 判定 |
| --- | --- | --- | --- | --- |
| 漏窗 / 窗隙「漏出」 | 「漏景，常常与游廊上的漏窗相关联……设漏窗……漏窗间有窗隙，'漏出'园外、墙外的各种美景，就是漏景」 | 「windows with elaborate **lattices that broke the view into pieces**」；「small windows … to give **glimpses** of the garden or scenery」 | 无 lattice/glimpse/leak/窗框相关内容（检索命中 0） | **双源直证 ✓（peopleapp+wiki）** |
| 片段化/若隐若现 | 「漏出……各种美景」 | 「broke the view into pieces」「glimpses」 | — | 双源 ✓ |
| 传统经验/无单一设计者 | 讲造园手法，未署具名设计者 | 未署名 | — | 类型性推断（见§二） |

- **判定：definition/overview 核心（漏窗/窗隙→景物片段显现）由 `peopleapp`（字面）与 `wp-chinese-garden`（格栅把景打散、glimpse）双源直证，非编造 ✓。但 `wp-garden-design` 第三源与「漏景」无关，属冗余挂源（见§六 minor）。**

### 1.3 korean-architecture（韩国建筑）

端内 definition：『韩国传统建筑以木构架承重、温突地面采暖与顺应山势的院落布局，适应四季分明的气候。』
端内 overview：『木构使墙体轻巧、温突把地面变成采暖面、院落采光通风；此类传统民居多由地方匠人集体营建，无单一设计者。』

| 要素 | wp-korean-architecture（实抓） | koreanet-hanok-madang（实抓） | springer（实抓） | 判定 |
| --- | --- | --- | --- | --- |
| 木构架承重 | 「wooden console structure and supported on posts；walls are made of earth (adobe) or … movable wooden doors」 | 「Hanok is characterized by a **wooden structure**」 | 正文不可核对 | **双源 ✓（wiki+korea.net）** |
| 温突地面采暖 | 「**ondol (온돌), the Korean floor panel heating system**」 | 「the **ondol (underground heating)** system … distributes heat … during winter / underfloor heating」 | 不可核对 | **双源 ✓（wiki+korea.net）** |
| 院落采光通风 | 「courtyard」=0、「madang」=0（未提） | 「Central to Hanok design is the **madang (open courtyard)**, a gathering space … also provides **natural light and ventilation**」 | note 称「Chae 与 Madang 空间构成」但**不可核对** | **单源（korea.net）** |
| 顺应山势的院落布局 | 有「Terrain utilization：约 70% 山地、steep slopes、hillside constructions、retaining walls」——为**地形/现代建构泛指**，非「院落布局顺应山势」 | 无（mountain=0） | 不可核对 | **未直证（超源措辞）** |
| 适应四季分明的气候 | 「climate」=0、「season」=0（winter/summer 仅指奥运会） | 「adapting to sun and wind patterns for temperature control」+ 冬季采暖（暗示，未言「四季分明」） | 不可核对 | **未直证（超源措辞）** |
| 地方匠人集体营建/无单一设计者 | 未直言 | 未直言 | 不可核对 | 类型性推断（见§二） |

- **判定：木构架承重、温突地暖双源稳固 ✓；「院落」实为 korea.net 单源直证；「顺应山势的院落布局」「适应四季分明的气候」在所引**可核对**源的正文中均无直述，属超源措辞（非具名事实编造，但超出引用正文）；springer 正文被 JS 挑战拦截，其 note 所述内容当前无法独立复核（详见§六）。**

**小结（核对①）：** `leaked-scenery` definition/overview 由双源直证，合格；`opposed-scenery` 概念核心仅 peopleapp 直证（wiki 不载「对景」），偏单源且含超源措辞；`korean-architecture` 木构/温突双源稳，但"院落"单源、"顺应山势/四季分明"超源、springer 不可核对。

## 二、核对②：「无单一设计者、类型性实例」是否合理

**结论：三条的类型性判断本身合理 ✓，与 vernacular / tibetan / xinjiang 先例同口径；但"类型性"只解决"实例无需具名"的问题，不能替代"概念关键事实需双源"（D10），亦不能洗白超源措辞。**

- `opposed-scenery`：对景是传统造园手法（peopleapp 列为「造景方式：障景、借景、框景、夹景、漏景、对景」之一），作为手法无单一发明者，实例转「类型性，传统造园无单一设计者；地点：中国江南古典园林」，无具名作品/作者/年代，不可证伪、非编造。类型性合理 ✓。
- `leaked-scenery`：同理，漏景为传统造景手法，实例「类型性，传统造园无单一设计者；地点：中国江南古典园林」，非编造。类型性合理 ✓。
- `korean-architecture`：韩屋（传统木构院落民居）属地方匠人集体营建的乡土/民族建筑，无单一设计者，实例已收窄为「韩国传统木构院落民居（韩屋，类型性，无单一设计者）；地点：韩国」，与 `vernacular-architecture`（round84, nv=False）先例同口径。类型性合理 ✓。**唯需注意**：条目题「韩国建筑」宽于实例「韩屋民居」（宫殿/寺庙/城郭等亦有具名匠师），本轮以"传统民居"作类型性实例是收敛得当的，但题/义范围略有落差（minor，非阻断）。
- **先例一致（实读库内条目）**：`vernacular-architecture`、`tibetan-architecture`、`xinjiang-architecture` 均为「概念源定义 + 类型性实例（无具名作品）→ nv=false」的既定口径，本轮三条同一模式。
- **是否编造具体事实：否（无具名名称/年代/设计者被杜撰）。** 但 korean 的「顺应山势的院落布局/四季分明」为超出引用正文的泛化断言，属"超源"而非"编造具名事实"，仍应清理。

## 三、核对③：nv=false 是否有据

**结论：`leaked-scenery` 的 nv=false 有据；`opposed-scenery` 因概念实质单源、`korean-architecture` 因超源措辞+不可核对源，二者 nv=false 依据不足，宜回退/待核实。**

- 结构自洽（三条均）：`needs_verification=false`、`pending_notes=""`、`待核实`="暂无已知待核实项。"、`coverage.json` 记 `needs_verification_count=0`；`source_count` 分别 =2 / 3 / 3（实读覆盖条目相符）——四处一致。
- 但"验证状态"应绑定"关键事实是否双源可核"（D10）：
  - `leaked-scenery`：概念双源直证（§1.2），实例类型性无单源风险 → nv=false 成立 ✓。
  - `opposed-scenery`：概念核心仅 peopleapp 单源直证（wiki 不载对景）→ 不满足 D10「关键事实双源」，nv=false 依据不足 ✗（建议 nv 回退 true 或补第二直证源）。
  - `korean-architecture`：木构/温突双源可，但"院落"单源、"顺应山势/四季分明"超源、springer 正文不可核对 → nv=false 暂不足 ✗（建议清理超源措辞、补院落第二直证、复核 springer 后再定）。
- 合 D10：`leaked` 达标；`opposed`、`korean` 未达标（单源/超源/不可核）。

## 四、核对④：七节 / SVG / 规范句

| 核对项 | opposed-scenery | leaked-scenery | korean-architecture |
| --- | --- | --- | --- |
| 七节齐（definition + 6 节） | ✓ 7 节 | ✓ 7 节 | ✓ 7 节 |
| SVG 数量/画布 | ✓ 1 张，`viewBox 0 0 760 400`，含「示意图，非施工图」 | ✓ 同 | ✓ 同 |
| SVG 禁用元素 | ✓ 无 `<script>/javascript:/href=/<image/<iframe/url(/on*=` | ✓ 同 | ✓ 同 |
| SVG 越界（实算 bbox） | ✓ bbox x[80..680] y[150..330]，均在框内 | ✓ bbox x[60..530] y[90..310]，均在框内 | ⚠ **`<ellipse cx=171 cy=117 rx=101 ry=197>` 顶点 y=117−197=−80，越 viewBox 顶 80px（预存，本轮未改 SVG；check.py 20% 边距容忍带 y∈[−80,480] 恰容，故未报，`test_svg_bounds` 5 passed）** |
| 规范句 | ✓ 收尾含「实际工程须按当地规范和专业设计人员的要求」 | ✓ 同 | ✓ 同 |
| nv / pending / 待核实 一致 | ✓ nv=false、pending=""、待核实="暂无已知待核实项。" | ✓ 同 | ✓ 同 |
| check.py | ✓ PASS（0 errors，EXIT=0） | ✓ 同 | ✓ 同 |

- 注：`korean-architecture` SVG 的 `<ellipse>` 严格越 viewBox 顶约 80px（同类 round86 rock-garden `<rect>` 预存越界），check.py 因 20% 边距容忍未报；建议后续收拢 ry 或下移 cy，非本轮引入、非阻断。

## 五、核对⑤：相似度（阈值 0.54；重点 opposed/leaked/framed 之间、korean vs 中/日建筑）

方法：`difflib.SequenceMatcher`，归一化 = **去全部空白 + 小写**（与 round86 口径一致：该口径下短口径全库最高 `value↔saturation 0.5437`、>0.54 对数=1，与 round86 完全复现）。全库 **258** 条两两比对（33,153 对）。分「短口径(标题|定义|时间地点|概述)」「def+overview」「全字段(短+6节)」「去模板正文」多档。

### 5.1 目标与全库（当前磁盘态）

| 口径 | 全库最高对 | 全库 >0.54 对数 | opposed 最高 | leaked 最高 | korean 最高 |
| --- | --- | --- | --- | --- | --- |
| 短口径 | value↔saturation **0.5437**（预存） | **1**（仅它，预存；三目标不在列） | 0.4413 与 time-scenery | 0.4900 与 time-scenery | 0.3571 与 chinese-architecture-style |
| def+overview | leaked↔time-scenery **0.4121** | 0 | 0.3596 与 time-scenery | 0.4121 与 time-scenery | 0.2710 与 chinese-architecture-style |
| 全字段(短+6节) | loop-route↔serial-route **0.5259** | 0 | 0.4190 与 leaked-scenery | 0.4317 与 opposed-scenery | 0.3519 与 rock-garden |
| 去模板正文 | loop-route↔serial-route **0.4811** | 0 | — | — | — |

- **三目标在所有口径下最高 <0.54**；全库唯一 >0.54 的 `value↔saturation` 为**既往预存**，与本轮无关。

### 5.2 指定关注对（全部 <0.54）

| 对 | 短 | def+ov | 全字段 |
| --- | --- | --- | --- |
| opposed ↔ leaked | 0.3980 | 0.2959 | 0.4190 |
| opposed ↔ framed | 0.3195 | 0.1752 | 0.2383 |
| leaked ↔ framed | 0.3590 | 0.2097 | 0.2897 |
| korean ↔ chinese-architecture-style | 0.3571 | 0.2710 | 0.2824 |
| korean ↔ japanese-architecture | 0.3550 | 0.1860 | 0.3256 |

- **opposed/leaked/framed 三者边界清晰**（最高 0.419）：「对景=相对成景」「漏景=漏窗片段显现」「框景=洞口成画框」，机制分层，不可辨性低。
- **korean vs 中日建筑** 均 <0.40（vs 中式短 0.357、vs 日式短 0.355），不构成模板重复。
- 最接近阈值者为本轮 `leaked↔time-scenery` 短口径 **0.4900**（仍 <0.54，安全；两者一为漏窗片段、一为晨昏晴雨四时，边界可辨）。

### 5.3 结论
**相似度：合格。** 无新引入的 >0.54 对；三目标与任何条目（尤 opposed/leaked/framed、korean vs 中日）均安全。

## 六、单源 / 超源支撑点（按要求指出）

| 条目 | 要点 | 支撑情况 | 判定 |
| --- | --- | --- | --- |
| **opposed-scenery** | **概念核心（对景=相对成景/呼应/端点设景）** | **peopleapp 直证；wp-chinese-garden 全文不载「对景」** | **⚠ 概念实质单源（peopleapp）** |
| opposed-scenery | 「视线端点布置景物 / 行进落点」字面 | 两源均无直述，为释义推演 | 轻微超源措辞 |
| **leaked-scenery** | 概念核心（漏窗片段显现） | peopleapp（字面）+ wiki（lattices broke view into pieces/glimpse）双源 | ✓ 多源，无单源要害 |
| leaked-scenery | `wp-garden-design` 第三源 | 该页无 lattice/glimpse/leak 相关内容，**不支撑漏景** | minor：冗余挂源，建议剔除/替换 |
| **korean-architecture** | 「院落（madang）」 | **仅 korea.net 直证**；wiki courtyard/madang=0；springer 不可核对 | **⚠ 单源（korea.net）** |
| korean-architecture | 「顺应山势的院落布局」 | wiki 仅「Terrain utilization」泛述山地/陡坡（现代建构），非「院落布局顺应山势」 | 超源措辞 |
| korean-architecture | 「适应四季分明的气候」 | wiki climate/season=0；korea.net 无「四季分明」（仅冬季采暖/温控暗示） | 超源措辞 |
| korean-architecture | `springer-hanok-madang` | **实抓为 JS 挑战页（305 字），正文不可核对**；Crossref 仅证文题真实存在 | 不可核对源 |

- 另：`peopleapp-zaoyuan-2` 注册题《造园的艺术手法（二）— 中国园林博物馆》与页面正文（含「障景/借景/框景/夹景/漏景/对景」逐条释义）相符，verified=true 成立；`koreanet` 注册题相符、实抓可核。二者释义命名合规。

## 七、抽检结论（逐条）

### opposed-scenery（对景）
- **内容/来源：待核实（不合格项）** — 概念核心「相对成景、前后呼应」仅 `peopleapp-zaoyuan-2` 直证；`wp-chinese-garden` 全文不出现「对景 / opposed」术语，不能直证该机制；definition 的「视线端点布置景物 / 行进落点」在两源均无字面对应，属释义推演。**概念实质偏单源**。
- **类型性/nv：类型性合理 ✓，nv=false 依据不足 ✗** — 对景为传统手法、无单一设计者，类型性实例贴切、非编造；但概念单源不满足 D10，nv=false 缺第二直证源支撑，建议 nv 回退 true 或补第二直证源（如另引一部园林专著）。
- **结构：合格** — 七节齐、规范句在、check.py PASS、SVG 合规（bbox 在框内）。
- **相似度：合格** — 短口径最高 0.4413、def+ov 0.3596、全字段 0.4190，与 leaked/framed 最高 0.4190，均 <0.54。
- **综合判定：待核实**（补第二直证源，或回退 nv=true；「端点/落点」措辞宜贴合所引源）。

### leaked-scenery（漏景）
- **内容/来源：合格** — 漏窗/窗隙→景物片段显现，由 `peopleapp`（字面）+ `wp-chinese-garden`（lattices broke view into pieces / glimpses）双源直证，非编造。
- **类型性/nv：合格** — 传统造景手法、无单一设计者，类型性实例贴切；nv=false 四处结构自洽且概念双源，成立。
- **结构：合格** — 七节齐、规范句在、check.py PASS、SVG 合规（bbox 在框内）。
- **相似度：合格** — 与 time-scenery 短 0.4900（最接近但 <0.54）、与 opposed 0.3980、与 framed 0.3590，均安全。
- **综合判定：合格**（minor：`wp-garden-design` 与漏景无关，属冗余第三源，建议剔除或换专门源；source_count 虽记 3，有效直证源=2 仍满足双源）。

### korean-architecture（韩国建筑）
- **内容/来源：待核实（不合格项）** — 木构架承重（wiki+korea.net）、温突地暖（wiki+korea.net）双源稳固；但「院落（madang）」仅 korea.net 直证（单源），「顺应山势的院落布局」「适应四季分明的气候」在两源正文无直述（超源措辞）；`springer-hanok-madang` 正文被 JS 挑战拦截、当前不可核对（Crossref 仅证文题真实）。
- **类型性/nv：类型性合理 ✓，nv=false 依据不足 ✗** — 韩屋民居作类型性无单一设计者，与 vernacular 先例同口径、非编造；但存在单源/超源/不可核源，nv=false 暂不足。
- **结构：合格（1 处 minor）** — 七节齐、规范句在、check.py PASS；SVG `<ellipse ry=197 cy=117>` 顶点越 viewBox 顶约 80px（**预存，本轮未改**，20% 边距容忍未报）。
- **相似度：合格** — vs chinese-architecture-style 0.3571、vs japanese-architecture 0.3550，均 <0.54。
- **综合判定：待核实**（删除/改写"顺应山势的院落布局""四季分明的气候"，或将之换成源可直证表述；补"院落"第二直证源；复核 springer 正文后再定 nv）。

**总判定：本轮 3 条中 `leaked-scenery` 合格；`opposed-scenery`、`korean-architecture` 待核实。核心问题：对景概念偏单源（peopleapp），韩建"院落"单源+"顺应山势/四季分明"超源、springer 不可核对。相似度全口径 <0.54、结构（七节/规范句/check.py）合格；korean SVG ellipse 预存越顶 minor。**

## 八、机器可读汇总

```
ROUND=87
SAMPLER=spotcheck-r87
SCOPE=["opposed-scenery","leaked-scenery","korean-architecture"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round86.md","entries/batch-02-b.json","entries/batch-05.json","entries/batch-38.json","data/sources.json(6 srcs)","coverage.json(3 entries)","tools/apply_review_round87.py","tools/check.py","tests/test_svg_bounds.py","git diff/status/log"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
PYTEST_SVG="5 passed (EXIT=0)"
FETCH_METHOD="urllib+browserUA+unverified-SSL, in-memory via python stdin (no temp files)"
FETCHES={"wp-chinese-garden":200,"wp-garden-design":200,"peopleapp-zaoyuan-2":200,"wp-korean-architecture":200,"koreanet-hanok-madang":200,"springer-hanok-madang":"200-BUT-JS-CHALLENGE(305 chars, body NOT readable)"}
ROUND87_CHANGES={"definition":"all 3 edited","overview":"all 3 edited","实例":"all 3 edited -> 类型性/无单一设计者","needs_verification":"true->false (all 3)","pending_notes":"-> ''","待核实":"-> 暂无已知待核实项。","opposed_extra":"典型手法与适用条件 also edited (removed 待核实 clause)","svg/原理/sources":"unchanged"}
DEFINITION_SUPPORT={
 "opposed-scenery":{"相对成景/呼应":"peopleapp direct only; wiki has NO 对景/opposed term","端点/行进落点":"NOT literal in either source (释义推演,超源)","multi_source":false,"fabricated_named":false},
 "leaked-scenery":{"漏窗/窗隙片段":"DUAL(peopleapp literal + wiki 'lattices broke view into pieces'/'glimpses')","wp-garden-design":"irrelevant(no lattice/glimpse/leak)","multi_source":true,"fabricated_named":false},
 "korean-architecture":{"木构架承重":"DUAL(wiki wooden frame/posts + korea.net wooden structure)","温突地暖":"DUAL(wiki ondol + korea.net ondol underfloor)","院落madang":"SINGLE(korea.net); wiki 0; springer unverifiable","顺应山势的院落布局":"wiki only generic Terrain utilization(modern); not 院落布局顺应山势 (超源)","四季分明气候":"NOT stated(wiki climate/season=0; korea.net none) (超源)","multi_source_partial":true,"fabricated_named":false}}
INSTANCE_TYPE_LEVEL={"all":true,"rationale":"传统手法/韩屋民居类型性, no single named designer; matches vernacular(round84)/tibetan/xinjiang(round85)","fabricated":false,"korean_scope_note":"题'韩国建筑'宽于实例'韩屋民居'(minor)"}
NV_FALSE_GROUNDED={"leaked-scenery":true,"opposed-scenery":false,"korean-architecture":false,"reason":"opposed concept single-source; korean over-claim + unverifiable springer","structure_consistent":"all four-way (nv=false/pending=''/待核实/coverage nv_count=0) but nv status vs D10 fails for opposed & korean"}
STRUCTURE={"seven_sections":7,"svg_count":1,"svg_forbidden":[],"reg_sentence":true,"check_py":"PASS",
 "svg_overflow_minor":{"korean-architecture":"ellipse cx171 cy117 rx101 ry197 -> top y=-80 越viewBox顶80px (预存; 20%边距容忍 y>=-80 未报)","opposed":"none bbox y[150..330]","leaked":"none bbox y[90..310]"}}
SIMILARITY={"threshold":0.54,"entries":258,"pairs":33153,"normalization":"strip-all-whitespace+lower (reproduces round86 short max 0.5437)",
 "short":{"library_max":"value<->saturation 0.5437(预存)","pairs_gt_0.54":1,"opposed_max":0.4413,"leaked_max":0.49,"korean_max":0.3571},
 "def_overview":{"library_max":"leaked<->time-scenery 0.4121","pairs_gt_0.54":0},
 "full":{"library_max":"loop-route<->serial-route 0.5259","pairs_gt_0.54":0},
 "detempl":{"library_max":"loop-route<->serial-route 0.4811","pairs_gt_0.54":0},
 "pairs":{"opposed-leaked":[0.398,0.2959,0.419],"opposed-framed":[0.3195,0.1752,0.2383],"leaked-framed":[0.359,0.2097,0.2897],"korean-chinese-style":[0.3571,0.271,0.2824],"korean-japanese":[0.355,0.186,0.3256]),
 "new_pairs_over_threshold":0}
SINGLE_SOURCE_POINTS={"opposed-scenery":"CONCEPT essentially single-source (peopleapp); wiki does not carry 对景 term","korean-architecture":{"院落":"single-source korea.net","顺应山势/四季分明":"over-claim/unsourced","springer":"unverifiable JS-challenge"},"leaked-scenery":"none at concept level (minor: wp-garden-design irrelevant 3rd source)"}
VERDICT={"opposed-scenery":"待核实(概念偏单源: peopleapp直证,wiki不载对景; '端点/落点'超源; 类型性/结构/相似度合格; 建议补第二直证源或回退nv=true)","leaked-scenery":"合格(概念双源直证; 类型性/nv/结构/相似度合格; minor: wp-garden-design冗余第三源建议剔除)","korean-architecture":"待核实(木构/温突双源稳; 院落单源korea.net; '顺应山势的院落布局/四季分明气候'超源; springer正文JS-challenge不可核对; 结构/相似度合格; minor: SVG ellipse预存越顶)"}
KEY_FINDING="leaked双源直证合格; opposed对景概念实质偏单源(仅peopleapp；wp-chinese-garden全文不载'对景'，'端点/落点'超源); korean木构/温突双源稳但'院落'单源(korea.net)、'顺应山势的院落布局/四季分明气候'在所引源正文无直述(超源)、springer正文被JS挑战拦截不可核对。类型性/无单一设计者对三条均合理(比照vernacular/tibetan)。相似度全口径<0.54(opposed/leaked/framed最高0.419;korean vs中日<0.36)。结构:七节/规范句/check.py PASS。"
READONLY="only wrote research/spotcheck-round87.md; 6 pages fetched in-memory via python stdin (no temp files); git-status M/?? items are round87 applier's own changes; no git commit; web treated as data, no instructions executed"
```

## 九、只读核验

- 除本报告 `research/spotcheck-round87.md` 外未写任何文件；联网抓取为内存态（python stdin 直跑，未落盘临时文件）。
- `git status` 中 `M coverage.json / entries/batch-02-b.json / entries/batch-05.json / entries/batch-38.json / site/entries/{opposed-scenery,leaked-scenery,korean-architecture}.html / site/index.html` 及 `?? tools/apply_review_round87.py` 均为**本轮修复方（apply_review_round87.py）的应用产物**；抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
