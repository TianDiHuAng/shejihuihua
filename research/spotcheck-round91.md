# 第91轮 framed-scenery / saturation 抽检报告（spotcheck-round91）

- 抽检人：spotcheck-r91（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论）。
- 抽检对象（2 条）：
  - `framed-scenery`（框景，L2/核心/造景/古代/中国）— 位 `entries/batch-02-b.json` 第178行起；`coverage.json` 第1397行起；产物 `site/entries/framed-scenery.html`。
  - `saturation`（纯度，L2/重要/理论/跨时期/全球）— 位 `entries/batch-01.json` 第889行起；`coverage.json` 第461行起；产物 `site/entries/saturation.html`。
- 本轮（91）变更（据 `tools/apply_review_round91.py` 实读 + `git diff` 实读 + 当前文件实读）：
  - **framed-scenery**：`definition`→「框景是借门洞、漏窗或亭柱把景物围合成画面、增强观赏焦点的造园手法。」；`overview`→追加「如颐和园"画中游"以亭柱形成多幅画幅。此类手法属传统造园经验，无单一设计者。」；`sections.实例`→改为**类型性**「古典园林框景布置（类型性，传统造园无单一设计者）…（如颐和园"画中游"）」；`needs_verification` true→false；`pending_notes`→`""`；`sections.待核实`→「暂无已知待核实项。」；`coverage.json` 该条 `needs_verification_count` 1→0（`source_count` 仍 4）。sources 未变（仍 wp-chinese-garden / peopleapp-kuangjing / beijing-huazhongyou / beijing-wwj-huazhongyou）。
  - **saturation**：仅 `definition`→「饱和度（纯度）指色彩中灰色成分多少所决定的鲜明或灰浊程度。」、`overview`→「纯度高的颜色鲜明夺目、宜作点睛；掺入灰或补色后趋于灰浊，常用作背景与过渡。」；`needs_verification` **仍为 true**、`pending_notes`/`待核实` 未变；`coverage.json` 该条 `source_count` 4、`needs_verification_count` **1（未变）**。
- 证据优先级：**独立实抓正文 > 当前文件实读 > git diff > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round91.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式：本轮两源 `web_fetch` **均直接成功（HTTP 200）**（人民号、北京市文物局官网均正常 200，无需回退 urllib）。
- 关键实抓正文（去标签后回读）：
  - `peopleapp-kuangjing` = `https://www.peopleapp.com/rmharticle/30028686345` → **HTTP 200**，page 标题 `社教｜似实而虚，似虚又实——中国古典园林的框景之美`，署名 **中国园林博物馆**，2022-07-06。正文原句：`中国古典园林中建筑的门、窗、洞，或者乔木树枝抱合成的景框，把远处的山水或人文景观包含其中……利用建筑物框架、空窗、洞门、廊柱围拢等封合的围框，套住某处景色，四周出现明确界线，产生画面的感觉。` 并明列 **框景三种应用形式**（① 落地罩/挂落；② 藤蔓树木枝条；③ 空窗/月洞门，举例拙政园芙蓉榭、留园小蓬莱、片石山房）。
  - `beijing-wwj-huazhongyou` = `https://wwj.beijing.gov.cn/bjww/362760/362770/744072997/index.html` → **HTTP 200**，page 标题 `北京市文物局-颐和园画中游建筑群历史沿革及造园艺术浅析`，来源 **北京市文物局**，作者张颖（北京市颐和园管理处）。正文原句：`澄辉阁的红色立柱与红绿相间的楣子木栏杆，又将美景框成一幅幅景随步移的山水画。"画框"的加入强化了如画的感觉，是李渔"无心画""尺幅窗"的实践……`；另正文 `乾隆皇帝虽然不是清漪园直接设计者，却是实际的主导者`。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed`（EXIT=0）。**
- `git status --porcelain`（实读）：`M coverage.json / entries/batch-01.json / entries/batch-02-b.json / site/entries/framed-scenery.html / site/entries/saturation.html / site/index.html` 及 `?? tools/apply_review_round91.py` 均为**修复方（round91 applier）自身产物**，非本抽检所写；抽检方仅读取。

## 一、复核 framed-①：definition/overview 是否由两直接源支撑（框景=门窗/漏窗/亭柱围合景物成画）

端内 definition：`框景是借门洞、漏窗或亭柱把景物围合成画面、增强观赏焦点的造园手法。`
端内 overview：`框景用门窗、枝干或亭柱当作"画框"，把连续风景切成局部画面；如颐和园"画中游"以亭柱形成多幅画幅。此类手法属传统造园经验，无单一设计者。`

| 要素 | peopleapp-kuangjing（实抓） | beijing-wwj-huazhongyou（实抓） | 判定 |
| --- | --- | --- | --- |
| **门洞/洞门** | `洞门、月洞门`（明列第三种形式） | 画中游"画框/框成山水画"（门洞框取，间接） | 直接源：peopleapp ✓ |
| **窗（漏窗/空窗）** | `空窗、窗宕子`；第三种形式`空窗、月洞门` | —（画中游以立柱框景） | 直接源：peopleapp ✓（"漏窗"为"空窗/窗"的细分类称，属轻微概括） |
| **亭柱（立柱/廊柱）** | `廊柱围拢` | `澄辉阁的红色立柱…框成一幅幅山水画` | **双源直证 ✓✓** |
| **围合成画面/成画** | `…产生画面的感觉`、`把远处的山水或人文景观包含其中` | `框成一幅幅景随步移的山水画` | **双源直证 ✓✓** |
| **增强观赏焦点** | `以人为本，根据人的视线特点…在有限的空间内创造无限的景观` | `"画框"的加入强化了如画的感觉` | 概括措辞（软支撑，非具名事实） |

**判定（复核 framed-①）：definition/overview 的核心机制「用门/窗/洞/亭柱（立柱/廊柱）把景物围合成画面」由 peopleapp 与 beijing-wwj 两源直接支撑；「亭柱围合」「围合成画」为双源直证。仅两处属轻微概括/软支撑（① definition 用"漏窗"，peopleapp 原文为"空窗/窗宕子"，漏窗系窗之细分类；② "增强观赏焦点"为对"产生画面感/强化如画感"的概括），均非具名事实编造，不构成缺陷。**

## 二、复核 framed-②：两源是否独立且都直接讲框景

| 维度 | peopleapp-kuangjing | beijing-wwj-huazhongyou | 是否独立 |
| --- | --- | --- | --- |
| 机构/作者 | 中国园林博物馆（人民号，2022-07-06） | 北京市文物局（作者张颖·北京市颐和园管理处） | 不同机构/不同作者 ✓ |
| 发布平台 | 人民日报「人民号」新媒体 | 北京市文物局官方网站 | 不同平台 ✓ |
| 举例 | 拙政园芙蓉榭、留园小蓬莱、片石山房 | 颐和园画中游、澄辉阁、李渔"尺幅窗" | 不同例证 ✓ |
| 是否直讲框景 | **是**：直接定义框景机制 + 三种应用形式 | **是**：直接述画中游以立柱"框成山水画"、引李渔"无心画/尺幅窗" | 均直接 ✓ |

**判定（复核 framed-②）：两源为两个独立机构、不同平台、不同例证的独立文本，均直接论述框景（一为概念定义+三形式，一为画中游框景实践+古典框景理论溯源）。独立性成立 ✓✓。**

## 三、复核 framed-③：实例"类型性"是否合理 + nv=false 是否有据

- **类型性合理**：传统造园手法（框景）为匠师群体累积经验，无单一设计者；此点由 beijing-wwj 原文 `乾隆皇帝虽然不是清漪园直接设计者，却是实际的主导者` **反证支持**——即便画中游这一具体皇家园林实例，文物局亦明言乾隆"非直接设计者"，故将实例主体表述为"类型性、无单一设计者"有据、且属**谨慎欠claim（宁少不编）**。实例以"（如颐和园"画中游"）"作示例，不冒称具体设计者/年代，安全。
- **附注（非缺陷，供后续考虑）**：画中游确有可考的建造时段（乾隆年间，乾隆十五年 1750 起建）与主导者（乾隆）。当前 type-based 表述省略了具体年代/设计者，属欠claim而非超源；若日后要写具名实例，宜按 beijing-wwj 口径注明"设计者：无直接设计者（乾隆为主导者）；年代：清乾隆年间"。
- **nv=false 有据（D10）**：
  - 本轮升级的"关键事实"＝**框景概念机制（门/窗/洞/亭柱围合成画）** + **画中游示例**：概念机制由 peopleapp + beijing-wwj 双直接源支撑（复核①），画中游示例由 beijing-wwj（"框成山水画"）+ beijing-huazhongyou（"8 个亭柱形成画框式取景"，source verified）双源支撑 → **关键事实双源满足** → nv=false **有据**。
  - **形式四处自洽**：`needs_verification=false`、`pending_notes=""`、`sections.待核实="暂无已知待核实项。"`、`coverage.json needs_verification_count=0（source_count=4）` —— 四处一致 ✓（check.py PASS 亦覆盖 D14 内联/标志一致性）。
  - **无残留"待核实"字样**：sections 正文（除待核实节）已无"待核实"，check.py 第309-310 规则通过。

**判定（复核 framed-③）：实例类型性合理（有 beijing-wwj"非直接设计者"反证）；nv=false 就"概念机制+画中游示例双源"成立且有据，形式四处一致。**

## 四、复核 saturation-①：重写后与 value 相似度是否 <0.54

端内 saturation（重写后）：definition=`饱和度（纯度）指色彩中灰色成分多少所决定的鲜明或灰浊程度。`；overview=`纯度高的颜色鲜明夺目、宜作点睛；掺入灰或补色后趋于灰浊，常用作背景与过渡。`
对照 value（明度）：definition=`色彩的明暗程度。`；overview=`明度指色彩的明暗程度，帮助区分形体、建立层次。`

方法：`difflib.SequenceMatcher`，归一化=**去全部空白+小写**（与 round86-90 口径一致）。

| 口径 | saturation vs value（本轮实测） | 阈值 |
| --- | --- | --- |
| 短口径（标题\|定义\|时间地点\|概述） | **0.4094** | <0.54 ✓ |
| def+overview | **0.2062** | <0.54 ✓ |
| 全字段（短+6节） | **0.3501** | <0.54 ✓ |

- **对照旧值**：以 round90 前旧文本重算，旧 saturation↔value 短口径约 0.5155–0.5437（round90 报告记 0.5437 预存超阈对）；重写后降为 **0.4094**，**重写确将最大相似对压到阈值以下**。saturation 三口径最高对均为 value（0.4094/0.2062/0.3501），均 <0.54，**判定合格 ✓**。
- 全库本轮两两比对 **258 条**：短口径 >0.54 **0 对**（max serial-route↔radial-route 0.4960）、def+overview >0.54 **0 对**（max leaked-scenery↔time-scenery 0.4121）、全字段 >0.54 **0 对**（max loop-route↔serial-route 0.5259）——**全库已无 >0.54 对**（含原 value↔saturation 预存对被消除）。

## 五、复核 saturation-②：nv 仍为 true 是否合理

- **端内状态**：`needs_verification=true`、`pending_notes="「高饱和」为对两源所述 pure vivid / stunning accord 的归纳，两源未逐字使用 saturation 一词。"`、`sections.待核实` 同义；`coverage needs_verification_count=1`（与 nv=true 一致）→ 形式四处一致 ✓（check.py 第287/338 规则通过）。
- **合理性**：本轮仅重写 definition/overview 以与 value 差异化；概念术语（饱和度/高饱和）在两源正文中并非逐字作为定义用语使用（wp-colorfulness/munsell 述 colorfulness/chroma；hermitage/libretexts 述马蒂斯《舞蹈》纯烈色彩），故保留 nv=true、pending_notes 明示"归纳/未逐字"属**既有且诚实的待核实状态**，与任务设定（n 仍为 true、概念术语未逐字、属既有）一致。新 definition 为一般色彩理论表述（"灰色成分决定鲜明/灰浊"与 Munsell 的 chroma＝相对灰色的鲜明度概念相容），未越出"归纳"性质，故 nv=true **合理**。

**判定（复核 saturation-②）：nv=true 保留合理，形式四处一致，pending_notes 诚实说明归纳来源。**

## 六、复核 七节 / SVG / 规范句 / 结构校验（两条）

| 核对项 | framed-scenery | saturation | 说明 |
| --- | --- | --- | --- |
| 七节齐 | ✓ | ✓ | definition+overview + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实（check.py 校验 6 节全非空 PASS） |
| SVG 数量/画布 | ✓ 1 张，`viewBox='0 0 760 400'`，含"示意图，非施工图" | ✓ 1 张，`viewBox='0 0 760 400'`，含"示意图，非施工图" | 均 L2 → 1–2 张 |
| SVG 越界/禁用元素 | ✓ | ✓ | check.py validate_svg PASS；pytest test_svg_bounds `5 passed`。framed bbox：外框 rect 120..640 / 90..330，内框 300..460 / 140..280，circle 346..414 / 176..244，text y≤375；saturation bbox：rect 90..210 / 230..350 / 370..490，y150..250，text y≤375 —— 全在 0..760 / 0..400 内 |
| 规范句 | ✓ "…实际工程须按当地规范和专业设计人员的要求"（常见错误与限制收尾） | ✓ 同 | RISK/REGULATION_NOTE 规则通过 |
| nv 与 pending 一致 | ✓ nv=false & pending="" & 待核实="暂无…" | ✓ nv=true & pending 非空 | check.py 第287/289/309 规则通过 |
| 来源数/双源规则 | ✓ 4 源（均 verified） | ✓ 4 源（均 verified） | 均≥2，check.py 第285 规则通过 |
| site 渲染一致 | ✓ `site/entries/framed-scenery.html` 含"门洞、漏窗或亭柱把景物围合成画面""如颐和园"画中游"以亭柱形成多幅画幅""古典园林框景布置（类型性，传统造园无单一设计者）""暂无已知待核实项"各 1 次；`示意图，非施工图`×2、`viewBox 0 0 760 400`×1 | ✓ `site/entries/saturation.html` 含"饱和度（纯度）指色彩中灰色成分多少所决定的鲜明或灰浊程度""纯度高的颜色鲜明夺目、宜作点睛""「高饱和」为对两源所述"各 1 次；`示意图，非施工图`×2、`viewBox 0 0 760 400`×1 | 生成器产物与新内容一致 |
| check.py | ✓ `PASS: all checks, 0 errors`（EXIT=0） | ✓ 同 | 全库校验 |
| pytest svg | ✓ `5 passed`（EXIT=0） | ✓ 同 | bbox 越界测试 |

## 七、复核 framed 相似度（vs leaked / opposed）

方法同上（去空白+小写，258 条两两）。

| 口径 | framed-scenery vs **leaked-scenery**（漏景） | vs **opposed-scenery**（对景） | framed 全库最高对 |
| --- | --- | --- | --- |
| 短口径 | **0.4488** | 0.4037 | leaked-scenery 0.4488 |
| def+overview | 0.3799 | 0.3333 | leaked-scenery 0.3799 |
| 全字段 | 0.4639 | 0.3611 | leaked-scenery 0.4639 |

- framed-scenery 所有口径最高 0.4639（vs leaked-scenery）< 0.54，**安全 ✓**。框架/漏景/对景三手法主题相近（同属造景），措辞有重叠但均显著低于阈值；leaked-scenery 为"漏窗/花墙使片段若隐若现"，framed 为"门窗/亭柱围合成画"，机制区分清晰。

## 八、单源 / 超源 / 编造支撑点

| 条目 | 要点 | 支撑情况 | 判定 |
| --- | --- | --- | --- |
| framed-scenery | 概念机制（门/窗/洞/亭柱围合成画） | peopleapp-kuangjing + beijing-wwj-huazhongyou 双直接源（各不同机构/平台/例证） | ✓✓ 双源直证 |
| framed-scenery | 画中游框景示例 | beijing-wwj（"框成山水画"）+ beijing-huazhongyou（"8 个亭柱形成画框式取景"，verified） | ✓✓ 双源 |
| framed-scenery | 实例类型性/无单一设计者 | 传统造园通例；beijing-wwj"乾隆非直接设计者"反证 | ✓ 合理（欠claim，安全） |
| framed-scenery | definition"漏窗""增强观赏焦点" | peopleapp 原文"空窗/窗宕子""产生画面感" | ✓ 轻微概括（非具名事实） |
| framed-scenery | 编造具名事实 | 实例不写具体设计者/年代、不复制图像；无杜撰 | ✓ 无编造 |
| saturation | definition/overview 重写 | 一般色彩理论（chroma 相对灰色鲜明度与 Munsell/colorfulness 相容）；两源未逐字用"饱和度/高饱和" | ✓ 归纳（nv=true 已明示） |
| saturation | 编造具名事实 | 实例马蒂斯《舞蹈》（艾尔米塔什、1909–1910）为既有、未改；无新增杜撰 | ✓ 无编造 |
| 两源独立性（framed） | 中国园林博物馆 vs 北京市文物局 | 不同机构、不同平台、不同例证、无复制 | ✓ 独立 |

## 九、相似度总表（阈值 0.54，口径=去空白+小写）

| 口径 | framed-scenery 最高 | saturation 最高 | 全库最高 | 全库 >0.54 对数 |
| --- | --- | --- | --- | --- |
| 短（标题\|定义\|时间地点\|概述） | 0.4488 vs leaked-scenery | 0.4094 vs value | serial-route↔radial-route 0.4960 | **0** |
| def+overview | 0.3799 vs leaked-scenery | 0.2062 vs value | leaked-scenery↔time-scenery 0.4121 | **0** |
| 全字段（短+6节） | 0.4639 vs leaked-scenery | 0.3501 vs value | loop-route↔serial-route 0.5259 | **0** |

- 两条目标全口径均 <0.54；**全库本轮已无 >0.54 对**（原 value↔saturation 预存超阈对经 saturation 重写后消除）。**相似度：均合格 ✓。**

## 十、复审结论（逐条）

### framed-scenery（框景）
- **内容/来源：合格** — definition/overview 核心机制（门/窗/洞/亭柱围合成画）由 `peopleapp-kuangjing`（中国园林博物馆，HTTP 200，直定义框景机制+三种形式）与 `beijing-wwj-huazhongyou`（北京市文物局，HTTP 200，画中游"红色立柱…框成一幅幅山水画"+李渔"尺幅窗"）**两个独立机构双直接源**支撑；画中游示例另有 beijing-huazhongyou 佐证。轻微概括（"漏窗"、"增强观赏焦点"）非缺陷。
- **类型性：合理** — 传统造园手法无单一设计者；beijing-wwj"乾隆非直接设计者"反证支持；实例欠claim 安全。
- **nv=false：有据** — 概念机制+画中游示例双源，D10 满足；形式四处一致（nv=false/pending=""、待核实="暂无…"、coverage nv_count=0）；check.py PASS 覆盖 D14。
- **编造：合格** — 不写具体设计者/年代、不复制图像，无杜撰具名事实。
- **结构：合格** — 七节齐、规范句在、SVG 合规（1 张，viewBox 0 0 760 400，bbox 在框内，无禁用元素）、site 渲染一致、check.py `PASS`、pytest `5 passed`。
- **相似度：合格** — vs leaked-scenery 短 0.4488 / def+ov 0.3799 / full 0.4639；vs opposed-scenery ≤0.4037；全口径最高 0.4639 < 0.54。

### saturation（纯度）
- **与 value 相似度：合格** — 重写后短 0.4094 / def+ov 0.2062 / full 0.3501，全口径 <0.54；较旧值（round90 记 0.5437 预存超阈）明显下降，全库 >0.54 对归零。
- **nv=true：合理** — 仅改 definition/overview；概念术语两源未逐字，"高饱和"为归纳，pending_notes/待核实 如实说明；coverage needs_verification_count=1 与 nv=true 一致。
- **编造：合格** — 未改实例（马蒂斯《舞蹈》既有信息），无新增杜撰。
- **结构：合格** — 七节齐、规范句在、SVG 合规（1 张，viewBox 0 0 760 400）、site 渲染一致、check.py `PASS`、pytest `5 passed`。

**总判定：本轮 2 条——`framed-scenery` 合格；`saturation` 合格。**
核心依据：framed 概念机制由 peopleapp（中国园林博物馆，HTTP 200，"建筑的门、窗、洞…产生画面的感觉"，列三种框景形式）+ beijing-wwj（北京市文物局，HTTP 200，"红色立柱…框成一幅幅山水画"，引"尺幅窗"）**双独立机构直接源**支撑，画中游示例双源佐证，实例类型性以"乾隆非直接设计者"反证合理，nv=false 有据、形式四处一致；saturation 重写后与 value 相似度降至 0.4094（<0.54，原预存超阈对消除），nv=true 保留合理。两条七节/SVG/规范句/site 一致/check.py PASS/pytest 5 passed/相似度全口径 <0.54 均合格；无具名事实编造。

## 十一、机器可读汇总

```
ROUND=91
SAMPLER=spotcheck-r91
SCOPE=["framed-scenery","saturation"]
WEB_FETCH={"peopleapp-kuangjing":"web_fetch HTTP200","beijing-wwj-huazhongyou":"web_fetch HTTP200"}
PEOPLEAPP_KUANGJING={"url":"https://www.peopleapp.com/rmharticle/30028686345","title":"社教｜似实而虚，似虚又实——中国古典园林的框景之美","author":"中国园林博物馆","date":"2022-07-06","quote":"建筑的门、窗、洞，或者乔木树枝抱合成的景框……利用建筑物框架、空窗、洞门、廊柱围拢等封合的围框，套住某处景色……产生画面的感觉","forms":"三种形式：落地罩/挂落；藤蔓树木枝条；空窗/月洞门（拙政园芙蓉榭/留园小蓬莱/片石山房）","direct":true}
BEIJING_WWJ_HUAZHONGYOU={"url":"https://wwj.beijing.gov.cn/bjww/362760/362770/744072997/index.html","title":"北京市文物局-颐和园画中游建筑群历史沿革及造园艺术浅析","source":"北京市文物局","author":"张颖(北京市颐和园管理处)","quote":"澄辉阁的红色立柱与红绿相间的楣子木栏杆，又将美景框成一幅幅景随步移的山水画……是李渔'无心画''尺幅窗'的实践","also":"乾隆皇帝虽然不是清漪园直接设计者，却是实际的主导者","direct":true}
FRAMED_DEFINITION_SUPPORT={"portal_洞门":"peopleapp direct","window_空窗/漏窗":"peopleapp direct (漏窗=窗细分类,minor)","pillar_亭柱/立柱/廊柱":"peopleapp+wwj DUAL","frame_into_picture":"peopleapp+wwj DUAL","enhance_focus":"soft gloss (非具名事实)"}
FRAMED_INDEPENDENCE={"institutions":"中国园林博物馆 vs 北京市文物局","platforms":"人民号 vs 北京市文物局官网","examples":"拙政园/留园/片石山房 vs 画中游/澄辉阁","independent":true}
FRAMED_INSTANCE_TYPE=true
FRAMED_NV_FALSE={"grounded":true,"key_facts_dual_source":true,"D10_met":true,"four_way_consistent":true,"residual":"实例省略具名年代/设计者属欠claim，安全；书写具名实例宜注'无直接设计者(乾隆为主)'+清乾隆年间"}
SATURATION_REWRITE={"definition":"饱和度（纯度）指色彩中灰色成分多少所决定的鲜明或灰浊程度。","overview":"纯度高的颜色鲜明夺目、宜作点睛；掺入灰或补色后趋于灰浊，常用作背景与过渡。"}
SATURATION_NV_TRUE={"kept":true,"pending":"高饱和为两源 pure vivid/stunning accord 之归纳，两源未逐字用 saturation","reasonable":true,"coverage_nv_count":1}
SIMILARITY={"threshold":0.54,"entries":258,"normalization":"strip-all-whitespace+lower",
 "framed":{"short":{"max":0.4488,"nn":"leaked-scenery","vs_opposed":0.4037},"defov":{"max":0.3799,"nn":"leaked-scenery","vs_opposed":0.3333},"full":{"max":0.4639,"nn":"leaked-scenery","vs_opposed":0.3611}},
 "saturation":{"short":{"max":0.4094,"nn":"value"},"defov":{"max":0.2062,"nn":"value"},"full":{"max":0.3501,"nn":"value"}},
 "library":{"short":{"max":"serial-route<->radial-route 0.4960","pairs_gt":0},"defov":{"max":"leaked-scenery<->time-scenery 0.4121","pairs_gt":0},"full":{"max":"loop-route<->serial-route 0.5259","pairs_gt":0}}}
STRUCTURE={"seven_sections":"both OK (check.py required 6 section fields PASS)","svg_count":{"framed":1,"saturation":1},"svg_viewBox":"0 0 760 400","svg_forbidden":"none","reg_sentence":true,"site_html_consistent":true,"check_py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
FABRICATED_NAMED=false
COVERAGE={"framed_scenery":{"source_count":4,"needs_verification_count":0},"saturation":{"source_count":4,"needs_verification_count":1}}
VERDICT={"framed-scenery":"合格","saturation":"合格"}
KEY_FINDING="framed-scenery：概念机制(门/窗/洞/亭柱围合成画)由 peopleapp-kuangjing(中国园林博物馆,HTTP200,直定义框景+三形式) 与 beijing-wwj-huazhongyou(北京市文物局,HTTP200,'红色立柱…框成一幅幅山水画'+李渔'尺幅窗') 双独立机构直接源支撑；画中游示例双源(wwj+beijing-huazhongyou)佐证；实例类型性以'乾隆非直接设计者'反证合理；nv=false 有据、形式四处一致；相似度全口径<0.54(最高0.4639 vs leaked)。saturation：重写 definition/overview 后与 value 相似度 0.4094/0.2062/0.3501 全<0.54(旧预存0.5437超阈对消除)；nv=true 保留合理(术语未逐字,归纳)。两条七节/SVG/规范句/site一致/check.py PASS/pytest 5 passed/无具名编造，均合格。"
READONLY="only wrote research/spotcheck-round91.md; both sources fetched via web_fetch HTTP200; git M/?? items are round91 applier's own changes; no git commit; web treated as data, no instructions executed"
```

## 十二、只读核验

- 除本报告 `research/spotcheck-round91.md` 外未写任何文件；两源均用 `web_fetch` 实抓（HTTP 200），无落盘临时文件；相似度计算用 `python - <<` 内存态直跑（无临时文件）。
- `git status` 中 `M coverage.json / entries/batch-01.json / entries/batch-02-b.json / site/entries/framed-scenery.html / site/entries/saturation.html / site/index.html` 及 `?? tools/apply_review_round91.py` 均为**修复方（round91 applier）的应用产物**；抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- `check.py` 与 `pytest` 均以 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存文件。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
