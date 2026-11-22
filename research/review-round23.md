# 第 23 轮 B5 待核实复核记录

复核日期：2026-11-22（Asia/Hong_Kong）　｜　复核人：review-r23（lead 委派子任务，无人值守）

## 一、执行说明

- 已读取任务文档：`AUTONOMOUS.md`、`TASK_design.md`（二者位于 `D:/Users/Administrator/Desktop/`，项目内无同名文件）、`DECISIONS.md`、`research/review-round22.md`、`research/gaps-round23.md`、`PROGRESS.md`；并按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。本会话为被委派子任务，按 `using-superpowers` 的 SUBAGENT-STOP 以本任务说明为准。
- `entries/*.json` 共 14 个文件、**126 条**；用 Python 逐条枚举确认 `needs_verification=true` 为 **101 条**（与 gaps-round23 的 B5 清单一致）。本报告对 101 条全部扫描，其中 8 条为本轮重点（`sustainable-architecture`、`vitruvian-triad`、`damp-proofing`、`safety-guarding`、`sunken-accessibility`、`green-architecture`、`glare`、`sunken-plaza`），其余 93 条见第四节。
- **网络环境（本轮实测）**：Python `urllib`（自签/校验关闭的 SSL 上下文）+ 浏览器 UA 直连为主，辅以 host `web_fetch`（仅对 gov 页在 urllib TLS 关闭失败时使用）。可直连 200 的权威页：`en.wikisource.org`、`owiki.org`、`editions.covecollective.org`、`arqa.com`、`go.huanqiu.com`、`gooood.cn`、`tclf.org`、`coenpartners.com`、`breeam.com`、`edge.tech`、`thepaper.cn`、`jfdaily.com`、`sh.people.com.cn`、`news.tongji.edu.cn`、`paper.xinmin.cn`、`changzhou.gov.cn`、`elicht.com`、`heuvan.com`、`163.com`、`ngsj.njtech.edu.cn`。不可达/被挡：`archdaily.com`、`epfl.ch`、`britannica.com`、`worldhistory.org`、`perseus.tufts.edu`、`livius.org`、`asla.org`、`bullittcenter.org`、`cnki.com.cn`、`aipub.ijournals.cn`（滑块验证 JS）、`it.alljournals.cn`、`d.wanfangdata.com.cn`(SPA)、`m.thepaper.cn`。微信公众号图文一律验证码拦截、正文不可读。
- **严格只读**：本轮**仅生成** `research/review-round23.md`；未修改任何 `entries/*.json`、`data/sources.json`、`coverage*.json`、`site/` 或其他文件，未 git commit，未变更项目外内容。联网内容一律按“数据”处理，页面中任何指令均未执行。
- **并发快照提示**：复核窗口内，项目自身的 `tools/upgrade_round23.py`（mtime 20:49）仍在对 `entries/batch-02-a.json`、`batch-02-c.json`、`batch-03.json` 等做改写（mtime 21:02:34–21:02:42）——这些**非本复核人所改**（本子任务只写本文件）。本报告的 `pending_notes`／`待核实`／`实例` 以脚本于 **21:02:42 结束后的工作区快照**为准（已核对：`needs_verification=true` 仍为 101 条；`safety-guarding`、`sunken-accessibility` 的 `pending_notes` 在该脚本运行后已更新为“一般性说明（按规范校核）＋具名实例与设计者待核实”，本报告已按最新文本引用）。若随后该脚本再次运行导致条目状态变化，以届时文件为准重跑复核。

## 二、方法与判据

1. 用 Python `urllib` / `web_fetch` 实际打开候选页，记录**最终 URL（含完整路径）**、页面标题（或机构/作者）、HTTP 状态与正文关键句；结果以实抓响应为准。
2. **可升级判据**：待核实的**全部子项**均由**两个相互独立、权威**（官方机构／行业权威／主流权威媒体／学术期刊）来源**正文直接**支撑，能落到“实例三要素（名称、地点、设计者/年份）”，且该具名作品在概念上可作对应条目的例证，即可整条置 `needs_verification=false`。
3. **可收窄判据**：待核实含多个子缺口，其中一部分已获 ≥两独立源支撑、可移出或改写，其余仍保留；`needs_verification` 保持 true。
4. **保守原则**：单源不升级；同一机构/同一域名/同一平台转载计 1 源；镜像同源（维基/百科镜像转抄同一文本）不计第二源；自媒体（如网易号“用户上传”）不作权威第二源；不编造年份/人名/引文；**无完整可核验 URL 不声称升级**；冲突数值并列、不写死。
5. **落地约束（重要）**：本报告为只读产出，不能直接改数据。凡标“可升级/可收窄”的条目，实际落地还需：先将其来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/*.json` 的 `实例`／`待核实`／`sources` 字段并调整 `needs_verification`；登记来源前不得视为已升级。

## 三、重点复核（8 条）

### 3.1 `sustainable-architecture`（可持续建筑，核心/L2，风格）—— **可升级（候选实例：The Edge，阿姆斯特丹）**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”；`sections.待核实`＝“示例建筑的评价数据与设计者待核实。”。现实例＝“被动式可持续建筑（类型性描述）／不适用／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://breeam.com/web/bre-group/case-studies/the-edge-amsterdam`（原 `https://breeam.com/case-studies/offices/the-edge-amsterdam` 301 跳转） | The Edge Amsterdam — **BRE Group / BREEAM（绿色建筑认证机构官方）** | 200 | “designed for Deloitte and awarded an Outstanding rating… **BREEAM rating: Outstanding（98.3%）**… **Architect: PLP Architecture**… Client: EDGE Technologies（formerly OVG Real Estate）… BREEAM NL New Construction” |
| 2 | `https://edge.tech/portfolio/the-edge` | The Edge — **EDGE Technologies（业主/开发商官方）** | 200 | “The Edge … Gustav Mahlerlaan 2970 … **Amsterdam** … **98.36% BREEAM-NL sustainability score** … **Architect PLP Architecture** … **Completion date Q4 2014** … Gross floor area 40.000 sq m … **generate more energy than they consume** … aquifer thermal energy storage … self-generated solar energy” |

- **结论：可升级（候选）。** 实例三要素（名称＝The Edge；地点＝荷兰阿姆斯特丹 Gustav Mahlerlaan；设计者＝**PLP Architecture**；年份＝**2014（Q4 完工）**）与评价数据（**BREEAM-NL 认证 Outstanding，98.36%〔edge.tech〕/98.3%〔BREEAM〕**，能源正效益）由 **BREEAM 认证机构官方（#1）＋业主 EDGE 官方（#2）两个相互独立权威源**正文直接支撑；概念（全生命周期高能效、能源产出大于消耗、健康办公与长期资产价值）贴合“可持续建筑”三重底线。
  - **数值/年份提示（并列不写死）**：BREEAM 评分 98.36%（edge.tech）与 98.3%（BREEAM）并列；竣工 Q4 2014（edge.tech）。写入正文并列注明“BREEAM-NL Outstanding（约 98.3%–98.36%）”。
  - **落地步骤**：先将 #1、#2 登记入 `data/sources.json`（verified=true），改写 `实例` 为“The Edge（荷兰阿姆斯特丹；PLP Architecture 设计；2014 年完工；BREEAM-NL Outstanding ≈98.3%，能源正效益）”并写贴合说明，再置 `needs_verification=false`。

### 3.2 `sunken-accessibility`（下沉空间无障碍，核心/L2，下沉空间）—— **可升级（候选实例：Peavey Plaza，明尼阿波利斯）**

- **待核实内容**：`pending_notes`＝“下沉空间无障碍做法为一般性说明（按规范校核）；具名实例与设计者待核实。”；`sections.待核实`＝“下沉空间无障碍的具体做法（坡度、扶手等）为一般性说明，须按当地规范校核；具名实例与设计者待核实。”。现实例＝“下沉空间无障碍坡道（类型性描述）／不适用／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://www.tclf.org/peavey-plaza`（原 `https://www.tclf.org/landscapes/peavey-plaza` 跳转） | Peavey Plaza — **The Cultural Landscape Foundation（TCLF，权威景观机构）** | 200 | “Peavey Plaza … **Minneapolis, MN** … **the sunken plaza** which also served as a pool basin … **M. Paul Friedberg + Partners created Peavey Plaza in 1975** … now with a raised basin floor and **ramps to enhance accessibility**, reopened the following year … National Register of Historic Places 2013” |
| 2 | `https://www.coenpartners.com/project/peavey-plaza/` | Peavey Plaza — **Coen+Partners（改造设计事务所官方）** | 200 | “**Iconic sunken plaza** … In **1975**, landscape architect **M. Paul Friedberg** conceived Peavey Plaza … **new ramps provide accessibility** to the plaza's new shallow, central reflecting pool” |
| 3 | `https://www.gooood.cn/2023-asla-general-design-award-of-honor-peavey-plaza-minneapolis-minnesota-united-states-by-coenpartners.htm` | 2023 ASLA 通用设计类荣誉奖：Peavey 广场 / Coen+Partners — 谷德设计网（**转载 ASLA 内容，计 1 源**） | 200 | “2023 ASLA 通用设计类荣誉奖…Peavey 广场…设计公司 Coen+Partners…位置 美国…明尼阿波里斯…1975 年…**改善可达性/无障碍**” |

- **结论：可升级（候选）。** 实例三要素（名称＝**Peavey Plaza（Peavey 广场）**；地点＝美国明尼苏达州明尼阿波利斯；设计者/年份＝**M. Paul Friedberg 1975 年原设计；Coen+Partners 2018–2019 改造（2023 获 ASLA 通用设计荣誉奖）增设无障碍坡道**）由 **TCLF（#1）＋ Coen+Partners（#2）两个相互独立权威源**正文直接支撑；概念（**下沉广场以“new ramps provide accessibility”实现无障碍**）正文直接对应。
  - **来源独立性提示**：#3 谷德为 ASLA 内容转载，按“同平台转载计 1 源”只作佐证，主证以 #1（TCLF）＋ #2（Coen 官方）为准。
  - **坡度参数**：坡道具体坡度数值三源均未给出，正文宜注明“坡度参数按当地无障碍规范”，不写死。
  - **落地步骤**：先将 #1、#2（可并 #3）登记入 `data/sources.json`（verified=true），改写 `实例` 为“Peavey Plaza（美国明尼阿波利斯；M. Paul Friedberg 1975 原设计；Coen+Partners 改造增设无障碍坡道，2023 ASLA 通用设计荣誉奖）”，再置 `needs_verification=false`。

### 3.3 `vitruvian-triad`（维特鲁威三原则，核心/L2，理论）—— **可收窄**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”；`sections.待核实`＝“《建筑十书》成书年代与译本细节待核实。”。现实例＝“维特鲁威《建筑十书》所述三原则（类型性记载）／古罗马／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://en.wikisource.org/wiki/Ten_Books_on_Architecture` | Ten Books on Architecture — **Wikisource（维基文库，1914 年 Morris Hicky Morgan 英译本，哈佛大学出版社）** | 200 | “**Ten Books on Architecture（1914）by Vitruvius, translated by Morris Hicky Morgan**… **CAMBRIDGE HARVARD UNIVERSITY PRESS… 1914**… a treatise on architecture written by the Roman architect Vitruvius and dedicated to his patron, the emperor Caesar Augustus” |
| 2 | `https://editions.covecollective.org/node/7431` | Vitruvius's de Architectura — **COVE（Collaborative Organization for Virtual Education，学术教学版；页面标注 “Not Vetted”）** | 200 | “Roman architect and engineer, Vitruvius, wrote and published … **de Architectura**, now known as The Ten Books on Architecture, **circa 30 to 15 BCE** and dedicated it to … Caesar Augustus … three ideals of architecture, **utility, strength, and beauty**” |

- **结论：可收窄（保留 `needs_verification=true`）。**
  - **译本细节**：英译者为 **Morris Hicky Morgan，1914 年，哈佛大学出版社（Harvard University Press）**——由 Wikisource（#1，独立于维基百科）正文直接支撑，此子项可移出。
  - **成书年代**：COVE（#2）记 **circa 30 to 15 BCE**，但该页明确标注 “**Not Vetted**”（未经审校），权威度不足；Britannica（`britannica.com/technology/De-architectura` 返回 404、`/biography/Vitruvius` 握手失败）、Perseus/Tufts、worldhistory、livius 本轮均不可达，无更强的第二条权威年代源。
  - 故**仅收窄**：译本已核，成书年代仍保留待核实。**建议（下一轮）**：取 Britannica、Perseus/Tufts 或学术出版社页面确认“约公元前 30–前 15 年”后，即可整条升级。

### 3.4 `green-architecture`（绿色建筑，核心/L2，风格）—— **保持**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”；`sections.待核实`＝“示例建筑的设计者与评价数据待核实。”。现实例＝“被动式节能公共建筑（类型性描述）／不适用／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句 / 说明 |
| --- | --- | --- | --- | --- |
| 1 | `https://ngsj.njtech.edu.cn/info/1064/1954.htm` | 常州国展资产高新智汇中心 — **南京工业大学建筑设计研究院有限公司（设计机构官方）** | 200 | “项目地点：江苏省常州市新北区；建筑面积：19291 平方米；设计时间：**2018 年**；获奖：**三星级绿色建筑设计标识证书（2021 年）、三星级绿色建筑评价标识证书、2022 年度江苏绿色建筑创新示范工程一等奖、2020 年度江苏省省级高品质绿色建筑项目**” |
| 2 | `https://www.163.com/dy/article/HSBDNGGE0552ADWT.html` | 住建局：2022 年常州大力发展绿色建筑产业助力实现“双碳”目标 — **网易号（页面声明“自媒体平台网易号用户上传”，自媒体转载）** | 200 | “常州国展资产高新智汇中心项目获得 **2022 年度江苏绿色建筑创新示范工程一等奖**”——仅佐证奖项，未给设计者/年份/地点/三星级标识，**不计权威第二源** |
| 3 | `https://jsszfhcxjst.jiangsu.gov.cn/art/2022/6/6/art_49384_10472747.html` | 关于 2022 年度省级绿色建筑发展专项资金项目的公示 — **江苏省住房和城乡建设厅** | 200（`web_fetch`） | 76 个项目公示，清单在 PDF 附件；属“**专项资金项目**”，与“绿色建筑创新示范工程”为**不同评选**，且未核到本项目名 |
| 4（不可读） | 微信公众号图文×2（round22 记录） | “2022 年度江苏绿色建筑创新示范工程 常州国展资产高新智汇中心”“最佳实践案例…” | 验证码 | “环境异常·需验证”，正文不可读，**不计第二源** |

- **结论：保持（保留 `needs_verification=true`）。** 具名实例（常州国展资产高新智汇中心，江苏常州新北区；南工大设计院；设计时间 2018；三星级绿色建筑标识；2022 年度江苏绿色建筑创新示范工程一等奖）**仍仅 NJTech（#1）一个可读权威源**落实三要素与评价数据。163（#2）为自媒体转载，虽佐证“一等奖”但非权威第二源；江苏住建厅公示（#3）为“专项资金”另评选、清单在 PDF。按保守原则不升级。**建议（下一轮）**：取“江苏绿色建筑创新示范工程”主办方（国际绿色建筑联盟/江苏省绿色建筑协会）公示原件、或常州市住建局/常州日报/新华网同项目报道（须含设计者、年份、标识/奖项），即可移出。

### 3.5 `glare`（眩光，重要/L2，材料）—— **保持**

- **待核实内容**：`pending_notes`＝“照度与 UGR 数值仅单一来源，待补充独立来源；面积记载不一。”；`sections.待核实`＝“照度 475lx 与 UGR 8–19 等数值仅单一来源，待补充独立来源；建筑面积记载不一。”。现实例＝“中国人民银行西宁中心支行综合办公楼／中国西宁／设计者待核实／约 1990 年代建成、2020 年照明改造”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句 / 说明 |
| --- | --- | --- | --- | --- |
| 1 | `https://ww.iea-shc.org/Data/Sites/1/publications/CN-Peoples-Bank-of-China.pdf` | Human Centric Lighting in an office building — **IEA SHC（国际能源署太阳能供热制冷计划）** | 200（PDF） | `475 lx`／`UGR 8–19` 数值来源（沿用既有记录；PDF 内容流压缩，本轮未逐字复核） |
| 2 | `https://www.elicht.com/view/101733.html` | 国内三个绿色照明项目顺利通过（预）评价 — **云知光** | 200 | “中国人民银行西宁中心支行综合办公楼照明系统改造项目…建筑高度 73m，地上 20 层，**示范面积 1 万平米**…”——**未给 475/UGR** |
| 3 | `http://www.heuvan.com/news_details.aspx?id=54` | 恒亦明…绿色照明 — **恒亦明（设备厂商）** | 200 | “…**示范面积 1.75 万平米**…”——**未给 475/UGR** |

- **结论：保持（保留 `needs_verification=true`）。** 照度 `475 lx` 与 `UGR 8–19` 实测数值本轮仍**仅 IEA PDF（#1）单源**；云知光（#2）、恒亦明（#3）均无同组数值。面积记载 1 万（云知光）／1.75 万（恒亦明）／≈1.8 万（IEA）**并列不写死**。按保守原则不升级。**建议**：取住建/科研机构或同行评议论文载同组实测数值者，方可移出该数值子项。

### 3.6 `damp-proofing`（防潮，核心/L2，下沉空间）—— **保持**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”；`sections.待核实`＝“示例构造做法与设计者待核实。”。现实例＝“地下空间防潮构造（类型性描述）／不适用／不适用／不适用”。
- **本轮核查**：未取得可归因到具体具名建筑（设计者＋年份）且由两条独立权威源正文支撑的防潮实例；相关下沉案例（如澎湃静安寺广场文）只述“排水”，属 ` drainage` 条目，非“防潮构造”。故无以具名实例升级的完整可核验 URL。
- **结论：保持（保留 `needs_verification=true`）。** 保持类型性描述，不升级；如需具名实例，须另起“名作三要素＋双权威源”专批。

### 3.7 `safety-guarding`（安全防护，核心/L2，下沉空间）—— **保持**

- **待核实内容**：`pending_notes`＝“防护做法（栏杆高度、照度）为一般性说明（按规范校核）；具名实例与设计者待核实。”；`sections.待核实`＝“下沉与临空处防护的具体做法（栏杆高度、照度）为一般性说明，须按当地规范校核；具名实例与设计者待核实。”。现实例＝“临空处防护栏杆（类型性描述）／不适用／不适用／不适用”。
- **本轮核查**：未取得可归因到具体具名建筑（设计者＋年份）且由两条独立权威源正文支撑的“安全防护/临空栏杆”实例；防护多为规范层面。故无完整可核验 URL 支撑升级。
- **结论：保持（保留 `needs_verification=true`）。** 保持类型性描述，不升级。

### 3.8 `sunken-plaza`（下沉广场，核心/L2，下沉空间）—— **保持（候选第二源已定位，但页面不可核）**

- **待核实内容**：`pending_notes`＝“顾如珍负责建筑工程为单源，待补充独立来源；其他实例的设计者与年代待核实。”；`sections.待核实`＝“‘顾如珍负责建筑工程’目前为澎湃单源，待补充独立第二来源；其他下沉广场实例的设计者与年代待核实。”。现实例＝“静安寺下沉广场／中国上海／卢济威主持城市设计、顾如珍负责建筑工程／1999 年落成”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句 / 说明 |
| --- | --- | --- | --- | --- |
| 1 | `https://www.thepaper.cn/newsDetail_forward_2786200` | “魔都”新生：同济大学与静安寺广场和南京路步行街的修建 — **澎湃新闻·私家历史** | 200 | “卢济威的夫人——同济设计院副总建筑师**顾如珍负责了具体的建筑工程**…静安寺下沉广场于 1998 年 3 月 31 日奠基启动…**于 1999 年 9 月 15 日竣工**” |
| 2 | `https://www.jfdaily.com/wx/detail.do?id=1010081` | 卢济威教授：中国现代城市设计创始者之一，静安寺广场、北外滩……都是他作品 — **解放日报·上观新闻** | 200 | “**1995 年，卢济威主持的静安寺地区城市设计**…静安寺广场…”——**未提顾如珍** |
| 3 | `https://sh.people.com.cn/BIG5/n2/2024/0319/c134768-40780072.html` | 上海静安寺广场焕新启用 — **人民网上海频道** | 200 | “**静安寺广场建成于 1999 年 9 月 15 日**…”——**未提顾如珍** |
| 4 | `https://news.tongji.edu.cn/info/1006/79436.htm`（另 `http://paper.xinmin.cn/html/xmwb/2023-10-27/8-9/172061.html`，200） | 【同济访谈录⑤】卢济威 — **同济大学新闻网（转上观）／新民晚报** | 200 | 卢济威主持静安寺地区城市设计、做“下沉式广场”佐证；**未提顾如珍** |
| 候选 | `https://it.alljournals.cn/view_abstract.aspx?pcid=5B3AB970F71A803DEACDC0559115BFCF0A068CD97DD29835&aid=2997E78A3B8E062A` | 城市中心的生态、高效、立体公共空间——上海静安寺广场（作者：**卢济威、顾如珍、孙光临、张斌**；单位：同济大学建筑城规学院/同济大学建筑设计研究院） — **期刊界（摘要页）** | 本轮**不可直连**（urllib 握手失败；`aipub.ijournals.cn/815JQ` 为滑块验证 JS） | 检索摘要可见“顾如珍”署名，但**页面无法打开核验**，不计为已核第二源 |

- **结论：保持（保留 `needs_verification=true`）。** `卢济威主持城市设计` 与 `1999-09-15 竣工` 已由澎湃＋解放日报＋人民网＋同济/新民多源正文明证；但 **“顾如珍负责建筑工程”仍仅澎湃可读单源**。检索到期刊论文（卢济威、顾如珍、孙光临、张斌 合著《城市中心的生态、高效、立体公共空间——上海静安寺广场》）可作第二源**候选**，但 `it.alljournals.cn` 摘要页与 `aipub` 本轮均无法直连核验（验证码/滑块 JS），按“无完整可核验 URL 不声称升级/收窄”原则**不据此升级**。另“其他下沉广场实例的设计者与年代”仍待核实。**建议（下一轮）**：直连 CNKI/万方/期刊官网核对该文题录（作者含顾如珍）后，可将“顾如珍”子项移出。

## 四、其余 93 条（本轮未取得成对独立权威源正文支撑，保持 `needs_verification=true`）

> 以下条目本轮未针对性打开适用新 URL 或未取得成对的独立权威来源正文直接支撑；其待核实多为“实例的具体名称/设计者/年份(地点)”“实测/性能参数”或单一来源归属，按保守原则保持。核心/重要条目若要做具名实例，需专门的“名作三要素＋双权威源”逐条核验批次（本轮预算集中在 8 个重点条目）。

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
| 41 | `spatial-organization` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 42 | `interior-exterior-transition` | 核心/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 43 | `courtyard` | 核心/理论 | 赵堂子胡同3号形成时期有清代与1930年代改建两说，待考订。 | 保持 |
| 44 | `borrowed-scenery` | 核心/造景 | 借景北寺塔的园外距离记载不一（约 1.5–1.7 公里），具体数值待核实；正文并列、不写死。 | 保持 |
| 45 | `framed-scenery` | 核心/造景 | 古典园林框景实例的具体设计者与年代待核实。 | 保持 |
| 46 | `opposed-scenery` | 核心/造景 | 对景具体实例的设计者与年代待核实。 | 保持 |
| 47 | `screened-scenery` | 核心/造景 | 苏州园林障景具体实例的设计者与年份待补充独立来源。 | 保持 |
| 48 | `winding-path` | 核心/造景 | 文徵明参与设计为相传之说；游径具体段落设计与年代待考订。 | 保持 |
| 49 | `pedestrian-flow` | 核心/动线 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 50 | `evacuation-route` | 核心/动线 | 疏散宽度/距离为一般性说明（按当地规范校核）；具名实例设计者与参数待核实。 | 保持 |
| 51 | `drainage` | 核心/下沉空间 | 雨水排放工程参数待补充专业来源；建筑面积记载不一。 | 保持 |
| 52 | `natural-ventilation` | 核心/材料 | 翠郊吴氏大院建造年代待核实；两处实测条件不同不可直接比较。 | 保持 |
| 53 | `material-texture` | 核心/材料 | 材料质感与光反射、触感之间关系的机理待补专门来源；实例的设计者与年代待核实。 | 保持 |
| 54 | `gothic` | 核心/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 55 | `renaissance-style` | 核心/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 56 | `modernism` | 核心/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 57 | `postmodernism` | 核心/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 58 | `mannerism` | 重要/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 59 | `beaux-arts` | 重要/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 60 | `plein-air` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 61 | `chinese-architecture-style` | 核心/风格 | 具体单体建筑工匠归属（蒯祥）仅单源，待补充独立来源。 | 保持 |
| 62 | `light-well` | 重要/下沉空间 | 具体天井实例的采光与通风实测数据待补充独立来源（机制层面可参见自然通风条目）。 | 保持 |
| 63 | `leaked-scenery` | 重要/造景 | 漏景具体实例的设计者与年代待核实。 | 保持 |
| 64 | `vernacular-material` | 重要/材料 | 具体地区乡土材料的性能数据待补充独立来源。 | 保持 |
| 65 | `color-harmony` | 重要/理论 | 面积比例与整体感等经验性表述待补充直接来源；实例的设计者与年份待核实。 | 保持 |
| 66 | `composition-placement` | 重要/理论 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 67 | `axis` | 重要/理论 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 68 | `stack-ventilation` | 重要/材料 | 热压通风实例的通风实测数据待补充独立来源。 | 保持 |
| 69 | `thermal-comfort` | 重要/理论 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 70 | `service-route` | 重要/动线 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 71 | `gestalt-organization-laws` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 72 | `color-psychology` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 73 | `environmental-psychology` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 74 | `hardscape-softscape` | 重要/造景 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 75 | `wayfinding` | 重要/动线 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 76 | `lighting-design` | 重要/材料 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 77 | `place-attachment` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 78 | `daylight-factor` | 补充/材料 | 具体实例的采光系数数值与设计者待补充独立来源。 | 保持 |
| 79 | `mixed-mode-ventilation` | 重要/材料 | 混合通风实例的控制策略与能耗数据待补充独立来源。 | 保持 |
| 80 | `material-durability` | 重要/材料 | 实例寿命与维护数据待补独立来源；具体退化机制的通用列表待补专门来源。 | 保持 |
| 81 | `transparent-material` | 重要/材料 | 透明与半透明材料实例的性能参数待补充独立来源。 | 保持 |
| 82 | `functional-zoning` | 重要/理论 | Architecture 与 Interior design 未直接给出“功能分区”术语定义；核心概念与实例数据均待补独立来源。 | 保持 |
| 83 | `gray-space` | 重要/理论 | 檐下与廊道实例的设计者与年代待补独立来源。 | 保持 |
| 84 | `enclosure` | 重要/理论 | 具体院落的设计者与年代待补独立来源。 | 保持 |
| 85 | `placemaking` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 86 | `space-syntax` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 87 | `pattern-language` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 88 | `form-follows-function` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 89 | `functionalism-architecture` | 重要/风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 90 | `biophilic-design` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 91 | `defensible-space-theory` | 重要/理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 92 | `perspective` | 核心/理论 | 透视演示年代取学界通行约数（约 1413 年），原始文献年代存争议，正文不写死。 | 保持 |
| 93 | `sunken-courtyard` | 核心/下沉空间 | 两类实例的历史原型对应关系与一般苏州庭院营造者归属待核实。 | 保持 |

## 五、本轮实际打开 / 请求的 URL（去重 37 个）

**HTTP 200 且正文可读 / 可用（20 个）：**

1. `https://en.wikisource.org/wiki/Ten_Books_on_Architecture` — 200（维基文库·Ten Books on Architecture，1914 Morgan 译本）
2. `https://editions.covecollective.org/node/7431` — 200（COVE·Vitruvius's de Architectura，circa 30–15 BCE，Not Vetted）
3. `https://arqa.com/?p=250772` → `…/rolex-learning-center-in-lausanne-switzerland.html` — 200（ARQA·Rolex Learning Center / SANAA / 2010）
4. `https://go.huanqiu.com/article/9CaKrnJzT8n` — 200（环球网·瑞士劳力士学习中心，2010 落成、高能源效益）
5. `https://www.gooood.cn/2023-asla-general-design-award-of-honor-peavey-plaza-minneapolis-minnesota-united-states-by-coenpartners.htm` — 200（谷德·2023 ASLA Peavey 广场，转载 ASLA）
6. `https://www.tclf.org/peavey-plaza` — 200（TCLF·Peavey Plaza，下沉广场/坡道无障碍/Friedberg 1975）
7. `https://www.coenpartners.com/project/peavey-plaza/` — 200（Coen+Partners·Peavey Plaza，new ramps provide accessibility）
8. `https://breeam.com/web/bre-group/case-studies/the-edge-amsterdam` — 200（BRE/BREEAM·The Edge，Outstanding 98.3%/PLP Architecture）
9. `https://edge.tech/portfolio/the-edge` — 200（EDGE Technologies·The Edge，98.36%/PLP/2014/energy-positive）
10. `https://www.thepaper.cn/newsDetail_forward_2786200` — 200（澎湃·卢济威与静安寺广场，顾如珍负责建筑工程/1999-09-15 竣工）
11. `https://www.jfdaily.com/wx/detail.do?id=1010081` — 200（解放日报·卢济威，静安寺城市设计 1995，未提顾如珍）
12. `https://sh.people.com.cn/BIG5/n2/2024/0319/c134768-40780072.html` — 200（人民网·静安寺广场 1999-09-15 建成）
13. `https://news.tongji.edu.cn/info/1006/79436.htm` — 200（同济新闻网·卢济威访谈，下沉式广场）
14. `http://paper.xinmin.cn/html/xmwb/2023-10-27/8-9/172061.html` — 200（新民晚报·卢济威，静安寺地区城市设计）
15. `https://ngsj.njtech.edu.cn/info/1064/1954.htm` — 200（南工大设计院·常州国展资产高新智汇中心）
16. `https://www.163.com/dy/article/HSBDNGGE0552ADWT.html` — 200（网易号·住建局稿，常州国展获 2022 创新示范一等奖；自媒体转载）
17. `https://jsszfhcxjst.jiangsu.gov.cn/art/2022/6/6/art_49384_10472747.html` — 200（`web_fetch`；江苏省住建厅·2022 省级绿色建筑发展专项资金项目公示，76 项，清单在 PDF）
18. `https://www.elicht.com/view/101733.html` — 200（云知光·人行西宁中心支行照明改造，示范面积 1 万平米，无 475/UGR）
19. `http://www.heuvan.com/news_details.aspx?id=54` — 200（恒亦明·人行西宁中心支行照明，示范面积 1.75 万平米，无 475/UGR）
20. `https://www.changzhou.gov.cn/gi_news/804167540372241` — 200（常州市住建局 2022 工作总结，仅一般绿色建筑，未列本项目）

**HTTP 200 但不可用（3 个，不计证据）：** `https://aipub.ijournals.cn/815JQ`（200，滑块验证 JS 空壳 59B）、`https://d.wanfangdata.com.cn/periodical/…`（200，SPA 无正文）、`https://www.britannica.com/technology/De-architectura`（`web_fetch` 返回 404 页面）。

**失败 / 不可达（14 个）：** `https://www.archdaily.com/`、`https://www.epfl.ch/`（SSL 握手超时）；`https://www.britannica.com/biography/Vitruvius`、`https://www.worldhistory.org/vitruvius/`、`https://www.perseus.tufts.edu/hopper/text?…`、`https://www.livius.org/articles/person/vitruvius/`（无响应）；`https://www.asla.org/2023awards/690233.html`、`https://www.bullittcenter.org/`、`https://m.thepaper.cn/newsDetail_forward_2786200`、`https://www.changzhou.gov.cn/gi_news/828161639281792`、`https://it.alljournals.cn/view_abstract.aspx?…`、`https://www.cnki.com.cn/Article/CJFDTotal-SJZJ200003005.htm`（握手/无响应）。另 `https://owiki.org/wiki/Sustainable_architecture`、`https://owiki.org/wiki/De_architectura`、`https://en.wikipedia.org/api/rest_v1/page/summary/De_architectura` 均 200（仅作连通性/维基镜像参考，镜像同源不计第二源）。

> 另 `web_search` 工具本轮查询 4 批（Rolex/维特鲁斯/下沉实例/常州绿色/顾如珍/Edge/Bullitt/江苏公示等），正文核验以 urllib/web_fetch 实抓为准。

## 六、汇总

- **可升级（建议整条置 `needs_verification=false`；均须先登记来源入 `sources.json` 并注明概念贴合）：2 条**
  - `sustainable-architecture`：候选实例 **The Edge（荷兰阿姆斯特丹；PLP Architecture 设计；2014 年完工；BREEAM-NL Outstanding ≈98.3%）**，由 **BREEAM 认证机构官方（`https://breeam.com/web/bre-group/case-studies/the-edge-amsterdam`，200）＋ EDGE 官方（`https://edge.tech/portfolio/the-edge`，200）** 两独立权威源正文直接支撑三要素与“能源正效益/BREEAM Outstanding”评价数据；数值 98.36% 与 98.3% 并列不写死。
  - `sunken-accessibility`：候选实例 **Peavey Plaza（美国明尼阿波利斯；M. Paul Friedberg 1975 原设计；Coen+Partners 改造增设无障碍坡道，2023 ASLA 通用设计荣誉奖）**；由 **TCLF（`https://www.tclf.org/peavey-plaza`，200）＋ Coen+Partners 官方（`https://www.coenpartners.com/project/peavey-plaza/`，200）** 两独立权威源正文直接支撑三要素与“下沉广场以 new ramps provide accessibility”概念（谷德转载 ASLA 为第三佐证）。
- **可收窄（保留 `needs_verification=true`）：1 条**
  - `vitruvian-triad`：**译本细节**（英译 Morris Hicky Morgan，1914 年，哈佛大学出版社）由 Wikisource（`https://en.wikisource.org/wiki/Ten_Books_on_Architecture`，200）已核；**成书年代**（COVE 记 circa 30–15 BCE 但标注 “Not Vetted”）仍待补权威机构源（Britannica/Perseus 本轮不可达），故仅收窄、不整条升级。
- **保持待核实：98 条** ＝ 第四节 93 条 ＋ 本轮重点中保持的 5 条（`green-architecture`、`glare`、`damp-proofing`、`safety-guarding`、`sunken-plaza`）。
- **本轮实测 `needs_verification=true` 总数：101 条** ＝ 可升级 2 ＋ 可收窄 1 ＋ 保持 98。
- **打开 URL 数**：直连**去重 37 个**（HTTP 200 且可读/可用 20；200 但不可用 3；失败/不可达 14；另维基 REST/owiki 镜像 3 个仅作连通性参考、不计第二源）；`web_search` 工具查询 4 批。
- **数据更正 / 冲突提示（不写死）**：The Edge BREEAM 评分 98.36%（edge.tech）与 98.3%（BREEAM）并列；Peavey Plaza 年份 1975（原建）／2018–2019 改造／2023 ASLA 获奖并列；`vitruvian-triad` 成书年代 COVE 作 circa 30–15 BCE（未审校）、译本 1914 Morgan/Harvard UP；`glare` 面积 1 万/1.75 万/≈1.8 万并列、照度 475lx/UGR 8–19 仅 IEA 单源；`green-architecture` 奖项第二佐证为网易号自媒体转载、不计权威源；`sunken-plaza` 顾如珍第二源（期刊论文署名）页面本轮不可直连、待核。

> 保守原则声明：维基/百科镜像同源不计第二源；微信公众号图文全部被验证码拦截、不作可核验第二源；自媒体（网易号“用户上传”）不作权威第二源；同机构/同平台转载计 1 源；无完整可核验 URL 不声称升级。本报告仅给结论与证据，**未修改任何条目数据或其它文件**（本文件为唯一产出）。
