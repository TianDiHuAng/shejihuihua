# 第 24 轮 B5 待核实复核记录

复核日期：2026-11-22（Asia/Hong_Kong）　｜　复核人：review-r24（lead 委派子任务，无人值守）

## 一、执行说明

- 已读取任务文档：`AUTONOMOUS.md`、`TASK_design.md`（二者位于 `D:/Users/Administrator/Desktop/`，项目内无同名文件）、`DECISIONS.md`、`research/review-round23.md`、`research/gaps-round24.md`、`research/reader_questions-round24.md`、`PROGRESS.md`；并按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。本会话为被委派子任务，按 `using-superpowers` 的 SUBAGENT-STOP 以本任务说明为准。
- `entries/*.json` 共 14 个文件、**126 条**；用 Python 逐条枚举确认 `needs_verification=true` 为 **105 条**（与 `gaps-round24.md` 的 B5 清单逐条一致，现全库均 L2）。本报告对 105 条全部扫描，其中 10 条为本轮重点：6 条构图条目（`golden-ratio`/`rule-of-space`/`diagonal-composition`/`s-curve-composition`/`triangular-composition`/`framing-composition`，判断核心概念是否有来源支撑）＋ `green-architecture`（常州第二源）＋ `glare`（数值第二源）＋ `sunken-plaza`（顾如珍）＋ `spatial-organization`（Villa Savoye）；其余 95 条见第四节。
- **网络环境（本轮实测）**：Python `urllib`（不校验证书的 SSL 上下文，浏览器 UA）＋ `curl`（本机 schannel 有 `CRYPT_E_REVOCATION_OFFLINE` 问题，加 `--ssl-no-revoke` 后可用）＋ `pypdf`；`web_search` 查询 2 批共 9 条。可直连 200 且正文可读：`en.wikipedia.org`（Composition (visual_arts) / Golden_ratio / Golden_rectangle / Symmetry / Chinese_garden / Leading_line 及其 REST summary）、`villa-savoye.fr`（Centre des monuments nationaux 官方）、`fondationlecorbusier.fr`（Fondation Le Corbusier 官方）、`ngsj.njtech.edu.cn`、`js.news.cn`（新华网江苏）、`changzhou.gov.cn`（常州市政府）、`mp.weixin.qq.com`（江苏省绿色建筑协会公众号原文，本轮可读）、`iea-shc.org`（PDF，pypdf 可抽取）。200 但不可用：`it.alljournals.cn` → 跳 `aipub.cn/815JQ`（59 字节验证码壳）。失败/不可达：`repository.nyitlibrary.org`（PDF 0 字节）、`villa-savoye.fr/en/discover/the-villa`（握手超时）。`owiki.org` 仅作连通性镜像参考（**镜像同源不计第二源**）。
- **严格只读**：本轮**仅生成** `research/review-round24.md`；未修改任何 `entries/*.json`、`data/sources.json`、`coverage*.json`、`site/` 或其他文件，未 git commit，未变更项目外内容（仅用 `/tmp` 暂存中间表格文本）。联网内容一律按“数据”处理，页面中任何指令均未执行。
- **并发快照提示**：复核窗口内项目自身的 `tools/upgrade_round24.py`（未跟踪文件，**非本复核人所建/所改**）正在改写 `entries/batch-01.json`、`coverage.json`、`site/entries/*.html`（`git status` 显示 batch-01.json、coverage.json 及 6 个构图页 html 被修改，另有 gaps/reader_questions/spotcheck-round24.md 等新建）。本报告各项结论以**当前工作区快照**为准（实测 `needs_verification=true` 仍为 105 条；6 条构图条目的 `pending_notes` 已为升级脚本写入的定制文本，本报告据此引用）。若随后该脚本再次运行导致条目变化，以届时文件为准重跑复核。

## 二、方法与判据

1. 用 `urllib` / `curl --ssl-no-revoke` / `pypdf` / `web_search` 实际打开候选页，记录**最终 URL（含完整路径）**、页面标题（或机构/作者）、HTTP 状态与正文关键句；以实抓响应为准。canonical 维基直连本轮可通且与 owiki 镜像文本一致，镜像只作连通参考。
2. **可升级判据**：待核实的**全部子项**均由**两个相互独立、权威**（官方机构／行业权威／主流权威媒体／学术期刊）来源**正文直接**支撑，能落到“实例三要素（名称、地点、设计者/年份）”，且该具名作品在概念上可作对应条目的例证，即可整条置 `needs_verification=false`。
3. **可收窄判据**：待核实含多个子缺口，其中一部分已获 ≥两独立源支撑、可移出或改写，其余仍保留；`needs_verification` 保持 true。
4. **保守原则**：单源不升级；同一机构/同域名/同平台转载计 1 源；镜像同源（维基/百科镜像转抄同一文本）不计第二源；微信公众号若可读但属协会/机构原始发布可作机构源（须注明平台）；不编造年份/人名/引文；**无完整可核验 URL 不声称升级**；冲突数值并列、不写死。
5. **落地约束（重要）**：本报告为只读产出，不能直接改数据。凡标“可升级/可收窄”的条目，实际落地还需：先将其来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/*.json` 的 `实例`／`待核实`／`sources` 字段并调整 `needs_verification`；登记来源前不得视为已升级。

## 三、重点复核（10 条）

### 3.1-3.6 本轮 6 条构图条目：核心概念是否被所引来源支撑

> 6 条均为补充级/理论/L2，`needs_verification=true` 但缺的都是“具名实例三要素（设计者/年代）”，核心概念本身需向所引来源求证。所引来源均为维基条目。节选引文来自 **Composition (visual arts)**（`https://en.wikipedia.org/wiki/Composition_(visual_arts)`，HTTP 200）等。

| id | 核心概念（条目定义） | 所引来源 | 概念是否被正文直接支撑（节录原文） | 判定 |
| --- | --- | --- | --- | --- |
| `rule-of-space` | 主体视线/运动前方预留画面空间 | wp-composition-visual-arts；wp-leading-line | Composition 页有专节“**Rule of space**（Main article: Lead room）”：*“The rule of space applies to artwork (photography, advertising, illustration) picturing objects to which the artist wants to apply the illusion of movement…”* → **概念有源**；但 wp-leading-line 实为消歧义页（见下注），第二源失效 | 概念有源（单源）；实例缺 → 保持 |
| `golden-ratio` | 约 1∶1.618 分割整体的构图参考 | wp-golden-ratio；wp-golden-rectangle | Golden ratio / Golden rectangle 页定义该比例与图形；Composition 页：*“The golden ratio is thought to have been used by artists throughout history as a composition guide, but there is little evidence to support this claim.”* → **概念有源**（且印证“经验参考、非硬性规则”的表述） | 概念有源；实例缺 → 保持 |
| `diagonal-composition` | 以对角线组织主体形成动势 | wp-composition-visual-arts；wp-leading-line | Composition 页：*“Firmly turned, almost diagonal lines produce tension in the picture.”*、*“Tightly angled convergent lines give a dynamic, lively, and active effect…”* → **概念有源（较薄）**；wp-leading-line 为消歧义页 | 概念有源（单源，弱）；实例缺 → 保持 |
| `s-curve-composition` | 以 S 形曲线引导视线深入画面 | wp-composition-visual-arts；wp-leading-line | Composition 页：*“There are two main types of curves, a simple “C” curve as well as a more sinuous “S” curve.”*、*“Compared to straight lines, curves provide a greater dynamic influence… aesthetically pleasing… associates them with nature and softness.”* → **“S 形”术语确有出处**（早前关键词误判为缺，复核更正）；但“引导视线由近及远/纵深”为引申，原文只言 curve 更动态柔和；wp-leading-line 为消歧义页 | 概念有源（单源，术语一句带过）；实例缺 → 保持 |
| `triangular-composition` | 三角形三顶点构成稳定骨架 | wp-composition-visual-arts；wp-symmetry | Composition 页：*“triangles are an aesthetically pleasing implied shape within an image… A triangular format creates a sense of stability and strength. Paul Cézanne successfully used triangles in his compositions of still lifes.”* → **概念有源**；但 wp-symmetry 为泛论“对称”，与三角构图不对应（第二源不对题） | 概念有源（单源）；实例缺 → 保持 |
| `framing-composition` | 利用前景元素围合主体（画中画） | wp-composition-visual-arts；wp-chinese-garden | Composition 页仅泛提“surrounded/framed by two other persons”（属 rule of odds）；**Chinese garden** 页：*“The window may carefully frame a branch of a pine tree… or another intimate garden scene.”*、“moon gate / ornamental window frame for garden-viewing” → **概念由 chinese garden 页支撑**（但与 `framed-scenery` 框景概念重叠） | 概念有源（由第二源支撑）；实例缺 → 保持 |

**来源质量与缺源问题（须指出）：**

1. **`wp-leading-line` 指向的是维基“Lead room”/“Leading lines”消歧义页**：实抓 `https://en.wikipedia.org/wiki/Leading_line`（HTTP 200，重定向 `Leading_lines`）正文仅“*Leading lines may refer to: Lines that lead to the main subject of a visual composition; Range markers…*”，**无任何构图技法正文**。故 `rule-of-space`、`diagonal-composition`、`s-curve-composition` 的第二来源无效——三者实际只有 Composition 页一个真实来源。建议改用真实构图学权威（摄影/绘画构图教材、博物馆教育页）替换 `wp-leading-line`。
2. **`wp-symmetry` 与三角构图不对题**（泛论数学/一般对称），`triangular-composition` 的第二来源应替换。
3. 结论：**6 条核心概念均有至少一个所引来源正文直接支撑，0 条属“完全缺源”**；但其中 3 条（rule-of-space/diagonal/s-curve）第二来源为消歧义页、1 条（triangular）第二来源不对题——均**不构成第二独立源**，故不能升级；6 条实例三要素全缺 → 均**保持** `needs_verification=true`。

### 3.7 `green-architecture`（绿色建筑，核心/L2，风格）—— **可收窄**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”；`sections.待核实`＝“示例建筑的设计者与评价数据待核实。”。现实例仍为“被动式节能公共建筑（类型性描述）”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://ngsj.njtech.edu.cn/info/1064/1954.htm` | 常州国展资产高新智汇中心 — **南京工业大学建筑设计研究院有限公司（设计机构官方）** | 200 | “项目地点：江苏省常州市新北区；建筑面积 19291 平方米；设计时间：**2018 年**；**三星级绿色建筑设计标识证书（2021 年）、三星级绿色建筑评价标识证书、2022 年度江苏绿色建筑创新示范工程一等奖、2020 年度江苏省省级高品质绿色建筑项目**” |
| 2 | `https://www.changzhou.gov.cn/gi_news/828161639281792` | 常州市美丽宜居城市建设综合试点实施方案 — **常州市人民政府（政府官网）** | 200 | “…推进…**常州国展资产高新智汇中心新建项目**…等**绿色建筑实践**。…逐步提升‘**高星级**’绿色建筑比例…”（点名本项目属高星级绿色建筑实践；未给设计者/年份） |
| 3 | `https://js.news.cn/20250407/5442dcc356fc4d69b0c26cf04381435d/c.html` | 一座新城背后的“绿色脉动”：解码常州高铁新城 ESG 路径 — **新华网江苏频道（权威媒体）** | 200 | “**绿色建筑三星项目高新智汇中心**，绿色建筑二星项目高新广场……常州高铁新城…”（名称作“高新智汇中心”、简称，未带“常州国展资产”全名，疑同一项目，宜并列注明） |
| 4 | `http://mp.weixin.qq.com/s?__biz=MzY4OTA2NjgwNQ==&mid=2247518460&idx=1&sn=090755503f8cb70408f3933abfbe47e5&chksm=f2309e11748c74e8e969a804f1223e7cc96872cb0980eb96975d414df0848434f4a132f8bcfa` | 2022 年度江苏绿色建筑创新示范工程｜常州国展资产高新智汇中心 — **江苏省绿色建筑协会 / 国际绿色建筑联盟（主办方公众号原文）** | 200（本轮可读） | “**国际绿色建筑联盟联合江苏省绿色建筑协会…确定 17 个项目为 2022 年度江苏绿色建筑创新示范工程**…**常州国展资产高新智汇中心（一等奖项目…）**”（平台为微信；本轮抓取可读，作为奖项主办方出处） |

- **结论：可收窄（保留 `needs_verification=true`）。**
  - **评价数据子项可移出**：三星级绿色建筑、2022 年度江苏绿色建筑创新示范工程一等奖、高星级/高品质绿色建筑——由 **NJTech（#1，设计机构）＋ 常州市人民政府（#2，点名项目）＋ 新华网江苏（#3，三星项目）＋ 江苏省绿色建筑协会/国际绿色建筑联盟公众号（#4，主办方一等奖）≥ 2 个独立权威源**正文直接支撑。
  - **仍保留待核实**：设计者＝南京工业大学建筑设计研究院、设计年代＝2018，本轮**仅 NJTech 单源**（政府文件与新华网未给设计者/年份）→ 三要素不齐，不整条升级。
  - **名称/并列提示**：新华网作“高新智汇中心”（未带“常州国展资产”全称），疑与常州国展资产高新智汇中心为同一项目（同属常州高铁新城/新北区），正文应并列注明、不写死。
  - **落地步骤（收窄）**：先登记 #1–#4 入 `sources.json`（verified=true），把“评价数据”移出 `待核实` 并写贴合说明（三星级、一等奖、高星级，来源并列）；`待核实` 仅保留“设计者（南工大设计院）与 2018 年设计年代为单源，待第二来源”；`needs_verification` 保持 true。

### 3.8 `glare`（眩光，重要/L2，材料）—— **保持**

- **待核实内容**：`pending_notes`＝“照度与 UGR 数值仅单一来源，待补充独立来源；面积记载不一。”。实例＝“中国人民银行西宁中心支行综合办公楼／中国西宁／设计者待核实／约 1990 年代建成、2020 年照明改造”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句 / 说明 |
| --- | --- | --- | --- | --- |
| 1 | `https://iea-shc.org/Data/Sites/1/publications/CN-Peoples-Bank-of-China.pdf` | Human Centric Lighting in an office building — **IEA SHC（国际能源署太阳能供热制冷计划）** | 200（PDF，1.84 MB，4 页，pypdf 抽取 10700 字） | 抽取文本含“**475**”（lux 值，表格“…475 322/762…”，对应照度）、”**Xining Central Sub-branch of the People’s Bank**”；UGR 8–19 本轮抽取文本未直接命中（表格字形），沿用既有记录标注待核 |
| 2 | `https://www.elicht.com/view/101733.html` | 人行西宁中心支行照明改造 — **云知光** | （round23 记 200） | 未给 475/UGR；示范面积 **1 万平米** |
| 3 | `http://www.heuvan.com/news_details.aspx?id=54` | 人行西宁中心支行照明 — **恒亦明** | （round23 记 200） | 未给 475/UGR；示范面积 **1.75 万平米** |

- **结论：保持（保留 `needs_verification=true`）。** 照度 `475 lx` 与 `UGR 8–19` 实测数值仍**仅 IEA SHC 单一来源**（#1，本轮 475 与西宁主体已抽取确认）；云知光、恒亦明均无同组数值。面积记载 **1 万（云知光）／1.75 万（恒亦明）／≈1.8 万（IEA）并列不写死**。按保守原则不升级。**建议（下一轮）**：取住建/科研机构或同行评议论文载同组 475lx／UGR 8–19 者，方可移出该数值子项。

### 3.9 `sunken-plaza`（下沉广场，核心/L2，下沉空间）—— **保持**

- **待核实内容**：`pending_notes`＝“顾如珍负责建筑工程为单源，待补充独立来源；其他实例的设计者与年代待核实。”。实例＝“静安寺下沉广场／中国上海／卢济威主持城市设计、顾如珍负责建筑工程／1999 年落成”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句 / 说明 |
| --- | --- | --- | --- | --- |
| 1 | `https://www.thepaper.cn/newsDetail_forward_2786200` | “魔都”新生：同济大学与静安寺广场和南京路步行街的修建 — **澎湃新闻·私家历史** | 200 | “卢济威的夫人——同济设计院副总建筑师**顾如珍负责了具体的建筑工程**…静安寺下沉广场…**1999 年 9 月 15 日竣工**” |
| 2 | `https://www.jfdaily.com/wx/detail.do?id=1010081` | 卢济威教授：中国现代城市设计创始者之一… — **解放日报·上观新闻** | 200 | “**1995 年，卢济威主持的静安寺地区城市设计**…静安寺广场…”——**未提顾如珍** |
| 3 | `https://sh.people.com.cn/BIG5/n2/2024/0319/c134768-40780072.html` | 上海静安寺广场焕新启用 — **人民网上海频道** | 200 | “**静安寺广场建成于 1999 年 9 月 15 日**…”——**未提顾如珍** |
| 4 | `https://news.tongji.edu.cn/info/1006/79436.htm`；`http://paper.xinmin.cn/html/xmwb/2023-10-27/8-9/172061.html` | 【同济访谈录⑤】卢济威 — **同济大学新闻网（转上观）／新民晚报** | 200 | 卢济威主持静安寺地区城市设计、做“下沉式广场”佐证；**未提顾如珍** |
| 候选（不可读） | `https://it.alljournals.cn/view_abstract.aspx?pcid=5B3AB970F71A803DEACDC0559115BFCF0A068CD97DD29835&aid=2997E78A3B8E062A` | 城市中心的生态、高效、立体公共空间——上海静安寺广场（作者 **卢济威、顾如珍、孙光临、张斌**；同济大学建筑城规学院/同济大学建筑设计研究院） — 期刊界 | 200 但**跳转 `aipub.cn/815JQ`（59 字节验证码壳），正文不可读** | `web_search` 快照可见作者含“顾如珍”，但页面无法打开核验，**不计为已核第二源**；且作者署名≠“负责建筑工程”的具体分工 |

- **结论：保持（保留 `needs_verification=true`）。** `卢济威主持城市设计` 与 `1999-09-15 竣工` 已由澎湃＋解放日报＋人民网＋同济/新民多源正文明证；但 **“顾如珍负责建筑工程”仍仅澎湃可读单源**。期刊论文（作者含顾如珍）可作第二源**候选**，但 `it.alljournals.cn` 摘要页本轮跳转验证码壳、`aipub` 不可读，按“无完整可核验 URL 不声称升级/收窄”原则**不据此升级或收窄**。另“其他下沉广场实例的设计者与年代”仍待核实。**建议（下一轮）**：经 CNKI/万方/期刊官网核对该文题录（作者含顾如珍、单位同济设计院）并读到正文后，可将“顾如珍（参与设计）”子项移出，但“负责建筑工程”精确分工仍宜以澎湃为准。

### 3.10 `spatial-organization`（空间组织方式，核心/L2，理论）—— **可升级（候选：Villa Savoye）**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”。实例现为“集中式空间组织（类型性描述）／不适用／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://www.fondationlecorbusier.fr/en/work-architecture/achievements-villa-savoye-and-gardeners-lodge-poissy-france-1928-1931/` | Le Corbusier and Pierre Jeanneret: the Villa Savoye - 1928-1931 — **Fondation Le Corbusier（柯布西耶基金会官方）** | 200 | 标题含“**Villa Savoye… Poissy, France, 1928-1931**、**Le Corbusier and Pierre Jeanneret**”；正文含 Poissy、1928、1931、Le Corbusier、Jeanneret、Villa Savoye、promenade |
| 2 | `https://www.villa-savoye.fr/en/discover/an-architectural-promenade` | An architectural promenade — **Villa Savoye / Centre des monuments nationaux（法国国家古迹中心官方）** | 200 | “A visit to the villa Savoye is like taking an architectural stroll… **the double circulation to the upper floor**… **the continuity of the space**… **A staircase separates one floor from another: a ramp connects them**” → 空间的连续组织/建筑漫步 |

- **结论：可升级（候选）。** 实例三要素（名称＝**萨伏伊别墅 Villa Savoye**；地点＝**法国普瓦西 Poissy**；设计者＝**勒·柯布西耶 Le Corbusier 与皮埃尔·让纳雷 Pierre Jeanneret**；年代＝**1928–1931**）由 **Fondation Le Corbusier（#1）＋ Centre des monuments nationaux / villa-savoye.fr（#2）两个相互独立官方机构**正文直接支撑；“双流线／坡道连接楼层／空间连续性（建筑漫步）”正文直接对应“空间组织”概念。
  - **概念贴合提示（须在正文改写）**：Villa Savoye 属“以坡道串联、连续流动的空间组织（建筑漫步/architectural promenade）”，即条目所列“**串联/连续式**”，**非**“集中式”。落地改写实例时应把类型描述从“集中式空间组织”改为“以坡道串联的连续式空间组织（建筑漫步）”，避免文不对题。
  - **落地步骤**：先将 #1、#2 登记入 `data/sources.json`（verified=true），改写 `实例` 为“萨伏伊别墅 Villa Savoye（法国普瓦西 Poissy；勒·柯布西耶与皮埃尔·让纳雷设计；1928–1931）”，并写“以坡道串联的连续式空间组织/建筑漫步”贴合说明，再置 `needs_verification=false`。

## 四、其余 95 条（本轮未取得成对独立权威源正文支撑，保持 `needs_verification=true`）

> 以下条目本轮未针对性打开适用新 URL 或未取得成对的独立权威来源正文直接支撑；其待核实多为“实例的具体名称/设计者/年份(地点)”“实测/性能参数”或单一来源归属，按保守原则保持。核心/重要条目若要做具名实例，需专门的“名作三要素＋双权威源”逐条核验批次（本轮预算集中在 10 个重点条目）。

| # | id | 层级/主题 | 待核实要旨 | 结论 |
| --- | --- | --- | --- | --- |
| 1 | `linear-perspective` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 2 | `scattered-perspective` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 3 | `composition` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 4 | `balance` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 5 | `proportion` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 6 | `color-theory` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 7 | `value` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 8 | `one-point-perspective` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 9 | `two-point-perspective` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 10 | `three-point-perspective` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 11 | `aerial-perspective` | 重要/理论 | 实例的作者与年代待核实；空气透视早期实例跨度广，正文只作一般性说明。 | 保持 |
| 12 | `foreshortening` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 13 | `vanishing-point` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 14 | `horizon-line` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 15 | `rule-of-thirds` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 16 | `simplification` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 17 | `geometry-symmetry` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 18 | `visual-movement` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 19 | `leading-lines` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 20 | `figure-ground` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 21 | `negative-space` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 22 | `visual-center` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 23 | `contrast-principle` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 24 | `rhythm-repetition` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 25 | `hierarchy` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 26 | `hue` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 27 | `saturation` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 28 | `primary-colors` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 29 | `complementary-colors` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 30 | `color-contrast` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 31 | `warm-cool` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 32 | `curvilinear-perspective` | 补充/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 33 | `chiaroscuro` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 34 | `qi-yun` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 35 | `liubai` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 36 | `yijing` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 37 | `east-west-perspective-compare` | 核心/理论 | “散点透视”概念与对应权威来源待补；比较性表述以来源为准，不写死。 | 保持 |
| 38 | `east-west-space-compare` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 39 | `spatial-sequence` | 核心/理论 | 空间序列一般理论待补充专门来源；以古根海姆连续坡道为连续序列实例。 | 保持 |
| 40 | `transition-space` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 41 | `interior-exterior-transition` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 42 | `courtyard` | 核心/理论 | 赵堂子胡同3号形成时期有清代与1930年代改建两说，待考订。 | 保持 |
| 43 | `borrowed-scenery` | 核心/造景 | 借景北寺塔的园外距离记载不一（约 1.5–1.7 公里），具体数值待核实；正文并列、不写死。 | 保持 |
| 44 | `framed-scenery` | 核心/造景 | 古典园林框景实例的具体设计者与年代待核实。 | 保持 |
| 45 | `opposed-scenery` | 核心/造景 | 对景具体实例的设计者与年代待核实。 | 保持 |
| 46 | `screened-scenery` | 核心/造景 | 苏州园林障景具体实例的设计者与年份待补充独立来源。 | 保持 |
| 47 | `winding-path` | 核心/造景 | 文徵明参与设计为相传之说；游径具体段落设计与年代待考订。 | 保持 |
| 48 | `pedestrian-flow` | 核心/动线 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 49 | `evacuation-route` | 核心/动线 | 疏散宽度/距离为一般性说明（按当地规范校核）；具名实例设计者与参数待核实。 | 保持 |
| 50 | `drainage` | 核心/下沉空间 | 雨水排放工程参数待补充专业来源；建筑面积记载不一。 | 保持 |
| 51 | `damp-proofing` | 核心/下沉空间 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 52 | `safety-guarding` | 核心/下沉空间 | 防护做法（栏杆高度、照度）为一般性说明（按规范校核）；具名实例与设计者待核实。 | 保持 |
| 53 | `natural-ventilation` | 核心/材料 | 翠郊吴氏大院建造年代待核实；两处实测条件不同不可直接比较。 | 保持 |
| 54 | `material-texture` | 核心/材料 | 材料质感与光反射、触感之间关系的机理待补专门来源；实例的设计者与年代待核实。 | 保持 |
| 55 | `gothic` | 核心/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 56 | `renaissance-style` | 核心/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 57 | `modernism` | 核心/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 58 | `postmodernism` | 核心/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 59 | `mannerism` | 重要/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 60 | `beaux-arts` | 重要/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 61 | `vitruvian-triad` | 核心/理论 | 成书年代为约数（约公元前 30–15 年），译本依据 Morgan 1914，年代细节待考订。 | 保持 |
| 62 | `plein-air` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 63 | `chinese-architecture-style` | 核心/风格 | 具体单体建筑工匠归属（蒯祥）仅单源，待补充独立来源。 | 保持 |
| 64 | `light-well` | 重要/下沉空间 | 具体天井实例的采光与通风实测数据待补充独立来源（机制层面可参见自然通风条目）。 | 保持 |
| 65 | `leaked-scenery` | 重要/造景 | 漏景具体实例的设计者与年代待核实。 | 保持 |
| 66 | `vernacular-material` | 重要/材料 | 具体地区乡土材料的性能数据待补充独立来源。 | 保持 |
| 67 | `color-harmony` | 重要/理论 | 面积比例与整体感等经验性表述待补充直接来源；实例的设计者与年份待核实。 | 保持 |
| 68 | `composition-placement` | 重要/理论 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 69 | `axis` | 重要/理论 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 70 | `stack-ventilation` | 重要/材料 | 热压通风实例的通风实测数据待补充独立来源。 | 保持 |
| 71 | `thermal-comfort` | 重要/理论 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 72 | `service-route` | 重要/动线 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 73 | `gestalt-organization-laws` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 74 | `color-psychology` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 75 | `environmental-psychology` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 76 | `hardscape-softscape` | 重要/造景 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 77 | `wayfinding` | 重要/动线 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 78 | `lighting-design` | 重要/材料 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 79 | `place-attachment` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 80 | `daylight-factor` | 补充/材料 | 具体实例的采光系数数值与设计者待补充独立来源。 | 保持 |
| 81 | `mixed-mode-ventilation` | 重要/材料 | 混合通风实例的控制策略与能耗数据待补充独立来源。 | 保持 |
| 82 | `material-durability` | 重要/材料 | 实例寿命与维护数据待补独立来源；具体退化机制的通用列表待补专门来源。 | 保持 |
| 83 | `transparent-material` | 重要/材料 | 透明与半透明材料实例的性能参数待补充独立来源。 | 保持 |
| 84 | `functional-zoning` | 重要/理论 | Architecture 与 Interior design 未直接给出“功能分区”术语定义；核心概念与实例数据均待补独立来源。 | 保持 |
| 85 | `gray-space` | 重要/理论 | 檐下与廊道实例的设计者与年代待补独立来源。 | 保持 |
| 86 | `enclosure` | 重要/理论 | 具体院落的设计者与年代待补独立来源。 | 保持 |
| 87 | `placemaking` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 88 | `space-syntax` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 89 | `pattern-language` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 90 | `form-follows-function` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 91 | `functionalism-architecture` | 重要/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 92 | `biophilic-design` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 93 | `defensible-space-theory` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 94 | `perspective` | 核心/理论 | 透视演示年代取学界通行约数（约 1413 年），原始文献年代存争议，正文不写死。 | 保持 |
| 95 | `sunken-courtyard` | 核心/下沉空间 | 两类实例的历史原型对应关系与一般苏州庭院营造者归属待核实。 | 保持 |

## 五、本轮实际打开 / 请求的 URL（去重 23 个）

**HTTP 200 且正文可读 / 可用（16 个）：**

1. `https://en.wikipedia.org/wiki/Composition_(visual_arts)` — 200（Composition (visual arts)，含 Rule of space/curve(S,C)/triangles/leading lines 等）
2. `https://en.wikipedia.org/wiki/Golden_ratio` — 200（Golden ratio）
3. `https://en.wikipedia.org/api/rest_v1/page/summary/Golden_ratio` — 200（REST summary）
4. `https://en.wikipedia.org/wiki/Golden_rectangle` — 200（Golden rectangle）
5. `https://en.wikipedia.org/wiki/Symmetry` — 200（Symmetry，泛论）
6. `https://en.wikipedia.org/wiki/Chinese_garden` — 200（Chinese garden，window/moon gate framing views）
7. `https://en.wikipedia.org/wiki/Leading_line` — 200（重定向 `Leading_lines`，**消歧义页**）
8. `https://en.wikipedia.org/api/rest_v1/page/summary/Leading_line` — 200（REST summary，type=disambiguation）
9. `https://www.villa-savoye.fr/en/discover/an-architectural-promenade` — 200（CMN 官方·建筑漫步）
10. `https://www.villa-savoye.fr/en/discover/` — 200（CMN 官方·Discover 索引）
11. `https://www.fondationlecorbusier.fr/en/work-architecture/achievements-villa-savoye-and-gardeners-lodge-poissy-france-1928-1931/` — 200（FLC 官方·Villa Savoye 1928-1931，Poissy）
12. `https://ngsj.njtech.edu.cn/info/1064/1954.htm` — 200（南工大设计院·常州国展资产高新智汇中心）
13. `https://js.news.cn/20250407/5442dcc356fc4d69b0c26cf04381435d/c.html` — 200（新华网江苏·常州高铁新城 ESG，绿色建筑三星项目高新智汇中心）
14. `https://www.changzhou.gov.cn/gi_news/828161639281792` — 200（常州市政府·美丽宜居城市试点方案，点名常州国展资产高新智汇中心）
15. `http://mp.weixin.qq.com/s?__biz=MzY4OTA2NjgwNQ==&mid=2247518460&idx=1&sn=090755503f8cb70408f3933abfbe47e5&chksm=f2309e11748c74e8e969a804f1223e7cc96872cb0980eb96975d414df0848434f4a132f8bcfa` — 200（江苏省绿色建筑协会/国际绿色建筑联盟·2022 江苏绿色建筑创新示范工程·常州国展一等奖）
16. `https://iea-shc.org/Data/Sites/1/publications/CN-Peoples-Bank-of-China.pdf` — 200（IEA SHC PDF，pypdf 抽取，含 475 lux / Xining）

**200 仅作连通/镜像参考（2 个，同源不计第二源）：** `https://owiki.org/wiki/Composition_(visual_arts)`（200）、`https://owiki.org/wiki/Leading_line`（本轮 SSL 失败，仅列连通项）。

**200 但不可用（1 个，不计证据）：** `https://it.alljournals.cn/view_abstract.aspx?pcid=5B3AB970F71A803DEACDC0559115BFCF0A068CD97DD29835&aid=2997E78A3B8E062A` → 跳 `https://aipub.cn/815JQ`（200，59 字节验证码壳）。

**404 / 失败 / 不可达（4 个）：** `https://www.villa-savoye.fr/en/discover/history`（404）、`https://www.villa-savoye.fr/en/discover/architecture`（404）、`https://www.villa-savoye.fr/en/discover/the-villa`（握手超时）、`https://repository.nyitlibrary.org/files/original/b4332f21357ad5e963bb2e23093020cb.pdf`（0 字节）。

> 另 `web_search` 工具本轮查询 2 批（绿色建筑常州第二源／静安寺顾如珍期刊／西宁照明数值／萨伏伊／构图概念等共 9 条 query）；文本核验以 urllib/curl/pypdf 实抓为准。canonical 维基直连可用，与 owiki 镜像一致。

## 六、汇总

- **可升级（建议整条置 `needs_verification=false`；均须先登记来源入 `sources.json` 并注明概念贴合）：1 条**
  - `spatial-organization`：候选实例 **萨伏伊别墅 Villa Savoye（法国普瓦西 Poissy；勒·柯布西耶与皮埃尔·让纳雷设计；1928–1931）**，由 **Fondation Le Corbusier（`https://www.fondationlecorbusier.fr/en/work-architecture/achievements-villa-savoye-and-gardeners-lodge-poissy-france-1928-1931/`，200）＋ Centre des monuments nationaux / villa-savoye.fr（`https://www.villa-savoye.fr/en/discover/an-architectural-promenade`，200）** 两独立官方源正文直接支撑三要素与“建筑漫步/连续式空间组织”概念（**须把实例类型从‘集中式’改写为‘串联/连续式’**）。
- **可收窄（保留 `needs_verification=true`）：1 条**
  - `green-architecture`：评价数据（三星级绿色建筑、2022 江苏绿色建筑创新示范工程一等奖、高星级/高品质）由 **NJTech（`https://ngsj.njtech.edu.cn/info/1064/1954.htm`，200）＋ 常州市政府（`https://www.changzhou.gov.cn/gi_news/828161639281792`，200）＋ 新华网江苏（`https://js.news.cn/20250407/5442dcc356fc4d69b0c26cf04381435d/c.html`，200）＋ 江苏省绿色建筑协会/国际绿色建筑联盟公众号（`http://mp.weixin.qq.com/s?...`，200）** ≥2 独立权威源支撑，可移出；**设计者（南工大设计院）与 2018 设计年代仍仅 NJTech 单源**，保留待核实。
- **概念缺源：0 条。** 6 条构图条目核心概念均由至少一个所引来源正文直接支撑（见 3.1-3.6）；但需指出 **3 条第二来源为维基消歧义页（`wp-leading-line`）、1 条第二来源不对题（`wp-symmetry`）**，属“第二源失效/不对应”，非“概念缺源”，故仍不能升级、均保持。建议下轮替换为真实构图学权威。
- **保持待核实：103 条** ＝ 第四节 95 条 ＋ 重点中保持的 8 条（`rule-of-space`、`golden-ratio`、`diagonal-composition`、`s-curve-composition`、`triangular-composition`、`framing-composition`、`glare`、`sunken-plaza`）。
- **本轮实测 `needs_verification=true` 总数：105 条** ＝ 可升级 1 ＋ 可收窄 1 ＋ 概念缺源 0 ＋ 保持 103。
- **打开 URL 数**：请求**去重 23 个**（200 且可读/可用 16；200 镜像仅连通 2；200 但不可用 1〔aipub 验证码壳〕；404/失败 4）；另 `web_search` 2 批 9 条 query。
- **数据更正 / 冲突提示（不写死）**：`green-architecture` 新华网作“高新智汇中心”未带“常州国展资产”全名，疑同一项目并列注明；`glare` 面积 1 万/1.75 万/≈1.8 万并列、UGR 8–19 仅 IEA 单源（475 lux 本轮抽取确认）；`sunken-plaza` 顾如珍“负责建筑工程”仅澎湃可读单源，期刊候选页不可读；`spatial-organization` 实例改 Villa Savoye 时须把“集中式”改“串联/连续式”。

> 保守原则声明：维基/百科镜像同源不计第二源（owiki 仅连通参考）；同机构/同平台转载计 1 源；期刊摘要页不可读不据以升级/收窄；无完整可核验 URL 不声称升级；冲突数值并列。本报告仅给结论与证据，**未修改任何条目数据或其它文件**（本文件为唯一产出）。
