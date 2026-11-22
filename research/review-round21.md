# 第 21 轮 B5 待核实复核记录

复核日期：2026-11-22（Asia/Hong_Kong）

## 一、执行说明

- 已按任务读取 `AUTONOMOUS.md`、`TASK_design.md`（二者位于 `D:/Users/Administrator/Desktop/`，本项目内无同名文件）、`DECISIONS.md`、`research/review-round20.md`、`research/gaps-round21.md`；并按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能（本会话为被委派子任务，按 `using-superpowers` 的 SUBAGENT-STOP 以本任务说明为准）。
- `entries/*.json` 共 14 个文件、**126 条**；本轮用 Python 逐条枚举确认 `needs_verification=true` 为 **92 条**（第 20 轮记 86 条；差异来自 `qi-yun`、`liubai`、`yijing`、`space-definition`、`human-scale`、`spatial-sequence` 等新增 L2 条目）。本报告对 92 条全部扫描，其中 10 条为本轮重点（`green-architecture`、`glare`、`sunken-plaza`、`space-definition`、`human-scale`、`spatial-sequence`、`material-texture`、`courtyard`、`curvilinear-perspective`；`east-west-space-compare` 另行说明），其余 83 条见第四节。
- **网络环境（本轮实测）**：`urllib` + 浏览器 UA 直连；`ngsj.njtech.edu.cn`、`m.thepaper.cn`、`sh.people.com.cn`、`jfdaily.com`、`ww.iea-shc.org`（PDF）、`miesbcn.com`、`archdaily.com`、`guggenheim.org`、`xining.pbc.gov.cn`、`bjdclib.cn`、`zgkpw.org.cn`、`discovery.cctv.com`、`inds.cnki.net`、`xueshu.qikan.com.cn`、`english.news.cn`、`paimiosanatorium.com` 均返回 200。`www.britannica.com` 返回 403；微信公众号图文（`mp.weixin.qq.com`）仍一律“环境异常·需验证”，正文不可读、不计第二源。
- **严格只读**：本轮**仅生成** `research/review-round21.md`；未修改 `data/sources.json`、任何 `entries/*.json`、`coverage*.json` 或其他文件，未 git commit，未变更项目外内容。联网内容一律按“数据”处理，页面中任何指令均未执行。

## 二、方法与判据

1. 用 Python `urllib` + 浏览器 UA 实际打开候选页，记录**最终 URL（含完整路径）**、页面标题（或机构/作者）、HTTP 状态与正文关键句；结果以实抓响应为准。
2. **可升级判据**：待核实的**全部子项**均由**两个相互独立、权威**（官方机构／行业权威／主流权威媒体）来源**正文直接**支撑，能落到“实例三要素（名称、地点、设计者/年份）”，且该具名作品在概念上可作对应条目的例证，即可整条置 `needs_verification=false`。
3. **可收窄判据**：待核实含多个子缺口，其中一部分已获 ≥两独立源支撑、可移出或改写，其余仍保留；`needs_verification` 保持 true。
4. **保守原则**：单源不升级；同一机构/同一域名/同一平台转载计 1 源；镜像同源（维基/百科镜像转抄同一文本）不计第二源；不编造年份/人名/引文；**无完整可核验 URL 不声称升级**；冲突数值并列、不写死。
5. **落地约束（重要）**：本报告为只读产出，不能直接改数据。凡标“可升级/可收窄”的条目，实际落地还需：先将其来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/*.json` 的 `实例`／`待核实`／`sources` 字段并调整 `needs_verification`；登记来源前不得视为已升级。

## 三、重点复核（9 条待核实 + 1 条相关条目说明）

### 3.1 `green-architecture`（绿色建筑，L2 核心）—— **保持**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”；`sections.待核实`＝“示例建筑的设计者与评价数据待核实。”。现实例＝“被动式节能公共建筑（类型性描述）／不适用／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://ngsj.njtech.edu.cn/info/1064/1954.htm` | 常州国展资产高新智汇中心 — **南京工业大学建筑设计研究院有限公司** | 200 | “项目地点：**江苏省常州市新北区**；建筑面积：**19291 平方米**；设计时间：**2018 年**；获奖情况：**三星级绿色建筑设计标识证书（2021 年）、三星级绿色建筑评价标识证书、2022 年度江苏绿色建筑创新示范工程一等奖、2020 年度江苏省省级高品质绿色建筑项目**”。 |
| 2 | `https://ngsj.njtech.edu.cn/info/1013/1007.htm` | 我院中标常州国展资产高新智汇中心工程总承包项目 — **南京工业大学建筑设计研究院有限公司** | 200 | 同院 EPC 中标通告（2018-10 中标、约 1.25 亿元）；**与 #1 同机构，按“同机构计 1 源”不算第二源**。 |
| 3（不可读） | `http://mp.weixin.qq.com/s?...`（“2022 年度江苏绿色建筑创新示范工程 常州国展资产高新智汇中心”“最佳实践案例 常州国展资产高新智汇中心新建项目”等） | 微信公众号图文 | 200（验证码页） | 返回“环境异常·需验证”，正文不可读，**不计第二源**。 |

- **结论：保持（保留 `needs_verification=true`）。**
  - 具名实例“常州国展资产高新智汇中心（江苏常州新北区；南工大设计院；设计时间 2018 年；三星级绿色建筑设计/评价标识；2022 年度江苏绿色建筑创新示范工程一等奖）”仅在 **NJTech 一个可机读权威源**（#1）落实；#2 为同院另一文，计 1 源；能佐证的奖项图文均为微信公众号（#3）被封，不可核验。按保守原则**不升级**。
  - **建议（下一轮）**：优先取得第二条可机读的独立权威源——如**江苏省住房和城乡建设厅公示原件**、常州高新区（新北区）住建部门或主流媒体（人民网/新华网/常州日报等），即可将实例三要素＋评价数据移出、置 `needs_verification=false`。

### 3.2 `glare`（眩光，L2 重要）—— **保持**

- **待核实内容**：`pending_notes`＝“照度与 UGR 数值仅单一来源，待补充独立来源；面积记载不一。”。现实例＝“中国人民银行西宁中心支行综合办公楼／中国西宁／设计者待核实／约 1990 年代建成、2020 年照明改造”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句 / 说明 |
| --- | --- | --- | --- | --- |
| 1 | `https://ww.iea-shc.org/Data/Sites/1/publications/CN-Peoples-Bank-of-China.pdf`（PDF，1,842,842 字节） | Human Centric Lighting in an office building — **IEA SHC（国际能源署太阳能供热制冷计划）** | 200 | 主源；实测表载照度 `475 lx`、`UGR 8 / 19–18` 等（PDF 内容流压缩，本轮仅确认 HTTP 200 与文件字节数；数值以既有记录为准）。 |
| 2 | `http://mp.weixin.qq.com/s?...`（“十三五”国家重点研发计划示范工程“中国人民银行西宁中心支行综合办公楼”三星级绿色照明标识挂牌及验收） | 微信公众号图文 | 200（验证码页） | “环境异常·需验证”，正文不可读，**不计第二源**。 |
| 3 | `https://xining.pbc.gov.cn/` | 中国人民银行西宁中心支行（青海省分行）门户 | 200 | 机构门户可达，但**无照度/UGR 实测数值**。 |

- **结论：保持（保留 `needs_verification=true`）。**
  - 具名实例（人行西宁中心支行综合办公楼，青海西宁）已由 IEA＋云知光＋恒亦明多源确认为此前轮结论，本轮不作为主项。当前唯一残留为“**照度 475 lx 与 UGR 8–19 的实测数值**”。
  - 该组数值本轮仍**仅 IEA PDF（#1）单源**：机构门户（#3）无数据、微信验收报道（#2）被封；以“罗涛 中国人民银行西宁中心支行 照度 UGR”等检索未获含同组实测数值的独立可核来源。数值子项保持单源，整条维持 true；面积（IEA≈1.8 万㎡ / 云知光“1 万平米”/ 恒亦明“1.75 万平米”）并列不写死。
  - **建议**：待取得住建/科研机构或同行评议论文中载同组实测数值者，方可移出该数值子项。

### 3.3 `sunken-plaza`（下沉广场，L2 核心）—— **保持**

- **待核实内容**：`pending_notes`＝“顾如珍负责建筑工程为单源，待补充独立来源；其他实例的设计者与年代待核实。”。现实例＝“静安寺下沉广场／中国上海／卢济威主持城市设计、顾如珍负责建筑工程／1999 年落成”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://m.thepaper.cn/newsDetail_forward_2786200` | “魔都”新生：同济大学与静安寺广场和南京路步行街的修建 — **澎湃新闻（私家历史）** | 200 | “方案通过后，卢济威的夫人——**同济设计院副总建筑师顾如珍负责了具体的建筑工程**”；“静安寺下沉广场于 1998 年 3 月 31 日奠基启动……**于 1999 年 9 月 15 日竣工**”。 |
| 2 | `https://www.jfdaily.com/wx/detail.do?id=1010081` | 卢济威教授：中国现代城市设计创始者之一，静安寺广场、北外滩……都是他作品 — **上观新闻/解放日报（2025-11-01）** | 200 | “1995 年，卢济威主持的静安寺地区城市设计……做一个**下沉式广场**”；全文**只提卢济威主持，未提顾如珍**。 |
| 3 | `https://sh.people.com.cn/BIG5/n2/2024/0319/c134768-40780072.html` | 上海靜安寺廣場煥新啟用，“八瓣妙蓮，亦靜亦鬧”，成為新的文化商業空間 — **人民网·上海频道（2024-03-19）** | 200 | “**靜安寺廣場建成於 1999 年 9 月 15 日**”；“曾是上世紀 90 年代末上海浦西地區最大的、功能齊全的休閑娛樂廣場”。 |

- **结论：保持（保留 `needs_verification=true`）。**
  - 子项“**1999 年落成**”已由澎湃（#1）＋人民网上海（#3）双源支撑，已成为正文事实、不在 pending 内。
  - 子项“**顾如珍负责建筑工程**”本轮仍**仅澎湃（#1）单源**：上观/解放日报（#2）虽为独立权威媒体的卢济威专稿，但**只字未提顾如珍**，不能补该子项；故该子项保留待核实。
  - 子项“其他下沉广场实例的设计者与年代”本轮未新增具名双源，保留。整条维持 true。

### 3.4 `space-definition`（建筑空间定义，L2 核心）—— **可升级（候选实例：巴塞罗那德国馆；需先登记来源并注明概念贴合）**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”；`sections.待核实`＝“示例空间的设计者与年代待核实。”。现实例＝“由界面限定的室内空间（类型性描述）／不适用／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://miesbcn.com/the-pavilion/` | The Pavilion — **Fundació Mies van der Rohe（密斯·凡·德·罗基金会，官方）** | 200 | “The **Barcelona Pavilion** was designed by **Ludwig Mies van der Rohe and Lilly Reich** as the German national pavilion for the **1929 Barcelona International Exposition**.”（名称/设计者/年份/地点齐备） |
| 2 | `https://www.archdaily.com/109135/ad-classics-barcelona-pavilion-mies-van-der-rohe` | AD Classics: Barcelona Pavilion / Mies van der Rohe + Lilly Reich — **ArchDaily（行业权威）** | 200 | “**Completed in 1929 in Spain.** As part of the **1929 International Exposition in Barcelona Spain, the Barcelona Pavilion, designed by [Mies van der Rohe + Lilly Reich]**”。 |

- **结论：可升级（候选）。** 实例三要素（名称＝巴塞罗那德国馆；地点＝西班牙巴塞罗那 Montjuïc；设计者＝密斯·凡·德·罗与莉莉·赖希；年份＝1929）由**密斯基金会官网（#1）＋ArchDaily（#2）两个相互独立权威源**正文直接支撑，满足“第二条独立权威来源＋正文直接支撑实例三要素”。
  - **概念贴合提示（须在正文注明）**：巴塞罗那德国馆以**独立界面／自由平面**而非“封闭围合”界定空间，属“流动空间”典型；若作 `space-definition` 实例，正文应写明“以独立界面与人的游走界定空间，非封闭室内”，以免与条目“围合界面”表述冲突。
  - **落地步骤**：先将 #1、#2 登记入 `data/sources.json`（verified=true），改写 `实例` 为上述具名实例并写入贴合说明，再置 `needs_verification=false`。

### 3.5 `human-scale`（人体尺度，L2 核心）—— **可升级（候选实例：帕伊米奥结核病疗养院；需先登记来源并注明概念贴合）**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”；`sections.待核实`＝“示例空间的实测数据与设计者待核实。”。现实例＝“住宅的亲切尺度（类型性描述）／不适用／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://english.news.cn/20260805/2f2673e5085d4c72aa0efda6b8b087a5/c.html` | Feature: The Finnish architect who gives modernism a human touch — **新华网英文网（Xinhua，官方媒体）** | 200 | “**Paimio Sanatorium**, one of the Aalto Works, **near Turku, Finland**… **Completed in 1933**, the sanatorium is among 13 buildings and complexes designed by renowned [Finnish architect **Alvar Aalto**]…”（名称/地点/设计者/年份齐备，主题即“人性化/人体尺度”） |
| 2 | `https://paimiosanatorium.com/the-architecture-of-empathy/` | The Architecture of Empathy — **Paimio Sanatorium（疗养院官方站点）** | 200 | “**Alvar and Aino Aaltos' masterpiece from 1933**”；1929 年为肺结核病人康复而委托设计（“a space where tuberculosis patients could recover”）。 |

- **结论：可升级（候选）。** 实例三要素（名称＝帕伊米奥结核病疗养院 Paimio Sanatorium；地点＝芬兰图尔库近郊；设计者＝阿尔瓦·阿尔托与艾诺·阿尔托；年份＝1933 年建成）由**新华网（#1，官方媒体）＋疗养院官方站点（#2）两个相互独立权威源**正文直接支撑。
  - **概念贴合提示**：该例最能体现“**以使用者的身体感受/人体为尺度**”的人性化设计（病床视角、采光、家具尺度）；写入 `human-scale` 时正文点明“按病人身体姿态与使用感受确定尺度”，与“人体尺度”定义对接。
  - **落地步骤**：先将 #1、#2 登记入 `data/sources.json`（verified=true），改写 `实例` 为该具名实例，再置 `needs_verification=false`。

### 3.6 `spatial-sequence`（空间序列，L2 核心）—— **保持**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”。现实例＝“院落式空间序列（类型性描述）／不适用／不适用／不适用”。候选：纽约古根海姆美术馆（赖特，连续螺旋坡道）。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句 / 说明 |
| --- | --- | --- | --- | --- |
| 1 | `https://www.guggenheim.org/about-us/history` | History — **The Guggenheim Museums and Foundation（古根海姆官方）** | 200 | “in 1943 renowned architect **Frank Lloyd Wright** gained the commission to design a museum in **New York City**… The **Solomon R. Guggenheim Museum opened on October 21, 1959**.”（名称/设计者/年份/地点齐备，但**未描述“螺旋/连续序列”**）。 |
| 2（未达标的候选） | `https://eonpedia.com/...`、`illustrarch.com`、`designedbyai.io` 等 | 内容聚合/自媒体 | — | 有“single continuous spiral ramp”等序列描述，但**权威性不足**，不计独立权威第二源。 |

- **结论：保持（保留 `needs_verification=true`）。** 古根海姆仅**一个权威源（#1）**给出三要素；描述“空间序列／连续螺旋”的第二源均为内容站/自媒体，权威性不达标。按保守原则不升级。**建议**：如需以古根海姆为例，需补一独立权威源（如建筑学教材/学术论文/博物馆学术页）直接论述其连续坡道序列。

### 3.7 `material-texture`（材料质感，L2 核心）—— **可收窄（保留 `needs_verification=true`）**

- **待核实内容**：`pending_notes`＝“材料质感与光反射、触感之间关系的机理待补专门来源；实例的设计者与年代待核实。”。现实例＝“质感对比的室内界面（类型性描述）／不适用／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://inds.cnki.net/kcms/detail?v=qZ0U0cwnOEoH8CAqV0OlZmTO3KwiBCLcUQoj0pgA9ZjnEB3dghUf9X6iu1zdb%2b8JB/wRRh1JVReAJQ8kopwmDRRZfvxGVEKeuIKsdXKwEQo=` | 材料质感对空间尺度认知影响的实验研究 — **大连理工大学博士学位论文（CNKI）** | 200 | “……本文**以材料质感作为建筑空间中身体知觉体验的载体**……验证使用者的**身体知觉体验与空间认知**……影响空间尺度认知”。 |
| 2 | `http://xueshu.qikan.com.cn/preview/1/322/5803617` | 建筑光影与材质在空间设计中的应用 — **龙源期刊网（收录文章）** | 200 | “……**触觉信息开始发挥作用**，光滑、粗糙、柔软、坚硬等**触感**深化了空间体验层次。**材质对光的反射与吸收特性也影响视觉表现**，高反射材质映照周围环境使空间显得开阔……”。 |
| 3 | `http://xueshu.qikan.com.cn/preview/1/322/5314473` | 建筑材料的知觉体验研究 — **龙源期刊网（收录文章）** | 200 | “……建筑师开始关注**材料表面的温度、纹理精细度与人体舒适度的关联**……”。 |

- **结论：可收窄（保留 true）。**
  - 子项“**质感→身体知觉/触感/光反射→空间感受**的机理”现由权威专门源（#1，大连理工 2021 博士论文）＋两篇龙源专门文章（#2 触觉+光反射、#3 温度/舒适）正文直接支撑，可从待核实移出。**谨慎声明**：龙源 #2/#3 为普及/行业文章、权威性有限，仅作“专门来源”补足，**不据此把整条升级**。
  - 子项“**实例的设计者与年代**”仍无具名、可双源核实的实例，**保留待核实**，整条 `needs_verification` 维持 true。

### 3.8 `courtyard`（庭院，L2 核心）—— **保持（具名实例已三源，仅朝代两说待考订）**

- **待核实内容**：`pending_notes`＝“赵堂子胡同3号形成时期有清代与1930年代改建两说，待考订。”。现实例已含“赵堂子胡同3号（朱启钤故居）四合院／北京东城区／朱启钤（据《营造法式》设计督造）／20 世纪 30 年代购置并改建（另有资料记‘形成时期：清’，两说并列）”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://www.bjdclib.cn/ztfw/dhly/yard/202301/t20230116_43210.html` | 赵堂子胡同3号 — **北京市东城区图书馆（地方文献·四合院）** | 200 | “保护级别：**区级文物保护单位**；**形成时期：清**；别称：**朱启钤宅**；位于**赵堂子胡同 3 号**……所属街道：建国门街道”。 |
| 2 | `https://www.zgkpw.org.cn/expert/jiliping/content_385726.html` | 营造学社：胡同里的中国古建研究摇篮 — **中国科普网/《科普时报》（嵇立平，2025-08-15）** | 200 | “**1932 年，朱启钤将营造学社迁至自家购置的赵堂子胡同 3 号院**。这是一座占地近 **3000 平方米的四进四合院**，由**朱启钤按照宋代《营造法式》，亲自设计、督造**”。 |
| 3 | `https://discovery.cctv.com/20070119/104637.shtml` | 淡出岁月的古宅——访朱启钤故居 — **CCTV.com 央视网（2007-01-19）** | 200（正文本轮解码乱码，标题与前轮记录为准） | 前轮记录：“赵堂子胡同 3 号：朱启钤故居……占地约 3000 平方米……20 世纪 30 年代购置……后由他亲自设计督造。” |

- **结论：保持（保留 `needs_verification=true`，但已极度接近可升级）。** 具名实例三要素（名称/地点/设计者/年份）由 #1、#2（并 #3 佐证）正文直接支撑；**唯一残留**为“形成时期：清”与“20 世纪 30 年代朱启钤设计督造改建”的**两说并存**。按“冲突年份/朝代并列不写死”原则保留 true。
  - **落地建议**：若确认“清”指宅址沿革、“现存院落主体为 1930 年代改建”，正文并列表述后可考虑置 false；否则维持两说。CCTV 本轮正文解码乱码，建议下一轮补一次 UTF-8 重抓再定稿。

### 3.9 `curvilinear-perspective`（曲线透视，L2 补充）—— **保持**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”。现实例＝“广角全景的曲线透视（类型性描述）／不适用／不适用／不适用”。
- 本轮未新增可机读独立权威具名实例（第 20 轮结论）：Dick Termes 六点透视球面画仅**艺术家本人官网自述**（一手源，非独立第二源）；Tyler《The Vault of Perception》PDF 上轮 403 不可读；维基及镜像同源不计。**结论：保持**，实例三要素仍无成对独立权威源支撑。

### 3.10 `east-west-space-compare`（留白与负空间比较，L1 核心）—— **不在 92 条待核实；维持现状**

- 该条当前 `needs_verification=false`、`level=L1`，仅有定义/时间地点/概述/相关条目（L1 骨架），**无“实例”段落、无 pending_notes**。任务将其列入“实例”关注，但当前无实例可核。**结论：无需复核（保持）**；若后续升级 L2，需补具名实例（如中西各一具体作品的三要素＋双源）。

## 四、其余 83 条（本轮未取得成对独立权威源，保持 `needs_verification=true`）

> 以下条目本轮未针对性打开适用 URL 或未取得成对的独立权威来源正文直接支撑；其待核实多为“实例的具体名称/设计者/年份(地点)”或“实测/性能参数”，按保守原则保持。核心/重要条目若要做具名实例，需要一个专门的“名作三要素＋双权威源”逐条核验批次（本轮预算集中在 10 个重点条目）。

| # | id | 层级/分层 | 待核实要旨 | 结论 |
| --- | --- | --- | --- | --- |
| 1 | `linear-perspective` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 2 | `scattered-perspective` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 3 | `composition` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 4 | `balance` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 5 | `proportion` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 6 | `color-theory` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 7 | `value` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 8 | `one-point-perspective` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 9 | `two-point-perspective` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 10 | `three-point-perspective` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 11 | `aerial-perspective` | 重要/L2 | 实例的作者与年代待核实；空气透视早期实例跨度广，正文只作一般性说明。 | 保持 |
| 12 | `foreshortening` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 13 | `vanishing-point` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 14 | `horizon-line` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 15 | `rule-of-thirds` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 16 | `simplification` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 17 | `geometry-symmetry` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 18 | `visual-movement` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 19 | `leading-lines` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 20 | `figure-ground` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 21 | `negative-space` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 22 | `visual-center` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 23 | `contrast-principle` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 24 | `rhythm-repetition` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 25 | `hierarchy` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 26 | `hue` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 27 | `saturation` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 28 | `primary-colors` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 29 | `complementary-colors` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 30 | `color-contrast` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 31 | `warm-cool` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 32 | `chiaroscuro` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 33 | `qi-yun` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 34 | `liubai` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 35 | `yijing` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 36 | `borrowed-scenery` | 核心/L2 | 借景北寺塔的园外距离记载不一（约 1.5–1.7 公里），具体数值待核实；正文并列、不写死。 | 保持 |
| 37 | `framed-scenery` | 核心/L2 | 古典园林框景实例的具体设计者与年代待核实。 | 保持 |
| 38 | `opposed-scenery` | 核心/L2 | 对景具体实例的设计者与年代待核实。 | 保持 |
| 39 | `screened-scenery` | 核心/L2 | 苏州园林障景具体实例的设计者与年份待补充独立来源。 | 保持 |
| 40 | `winding-path` | 核心/L1 | 仅见中国园林综合条目，待补充针对曲径的独立来源。 | 保持 |
| 41 | `pedestrian-flow` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 42 | `drainage` | 核心/L2 | 雨水排放工程参数待补充专业来源；建筑面积记载不一。 | 保持 |
| 43 | `natural-ventilation` | 核心/L2 | 翠郊吴氏大院建造年代待核实；两处实测条件不同不可直接比较。 | 保持 |
| 44 | `gothic` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 45 | `renaissance-style` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 46 | `modernism` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 47 | `postmodernism` | 核心/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 48 | `mannerism` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 49 | `beaux-arts` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 50 | `plein-air` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 51 | `chinese-architecture-style` | 核心/L2 | 具体单体建筑工匠归属（蒯祥）仅单源，待补充独立来源。 | 保持 |
| 52 | `light-well` | 重要/L2 | 具体天井实例的采光与通风实测数据待补充独立来源（机制层面可参见自然通风条目）。 | 保持 |
| 53 | `leaked-scenery` | 重要/L2 | 漏景具体实例的设计者与年代待核实。 | 保持 |
| 54 | `vernacular-material` | 重要/L2 | 具体地区乡土材料的性能数据待补充独立来源。 | 保持 |
| 55 | `color-harmony` | 重要/L2 | 面积比例与整体感等经验性表述待补充直接来源；实例的设计者与年份待核实。 | 保持 |
| 56 | `composition-placement` | 重要/L2 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 57 | `axis` | 重要/L2 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 58 | `stack-ventilation` | 重要/L2 | 热压通风实例的通风实测数据待补充独立来源。 | 保持 |
| 59 | `thermal-comfort` | 重要/L2 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 60 | `service-route` | 重要/L2 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 61 | `gestalt-organization-laws` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 62 | `color-psychology` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 63 | `environmental-psychology` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 64 | `hardscape-softscape` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 65 | `wayfinding` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 66 | `lighting-design` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 67 | `place-attachment` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 68 | `daylight-factor` | 补充/L2 | 具体实例的采光系数数值与设计者待补充独立来源。 | 保持 |
| 69 | `mixed-mode-ventilation` | 重要/L2 | 混合通风实例的控制策略与能耗数据待补充独立来源。 | 保持 |
| 70 | `material-durability` | 重要/L2 | 实例寿命与维护数据待补独立来源；具体退化机制的通用列表待补专门来源。 | 保持 |
| 71 | `transparent-material` | 重要/L2 | 透明与半透明材料实例的性能参数待补充独立来源。 | 保持 |
| 72 | `functional-zoning` | 重要/L2 | Architecture 与 Interior design 未直接给出“功能分区”术语定义；核心概念与实例数据均待补独立来源。 | 保持 |
| 73 | `gray-space` | 重要/L2 | 檐下与廊道实例的设计者与年代待补独立来源。 | 保持 |
| 74 | `enclosure` | 重要/L2 | 具体院落的设计者与年代待补独立来源。 | 保持 |
| 75 | `placemaking` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 76 | `space-syntax` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 77 | `pattern-language` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 78 | `form-follows-function` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 79 | `functionalism-architecture` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 80 | `biophilic-design` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 81 | `defensible-space-theory` | 重要/L2 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 82 | `perspective` | 核心/L2 | 透视演示年代取学界通行约数（约 1413 年），原始文献年代存争议，正文不写死。 | 保持 |
| 83 | `sunken-courtyard` | 核心/L2 | 两类实例的历史原型对应关系与一般苏州庭院营造者归属待核实。 | 保持 |

## 五、本轮实际打开 / 请求的 URL（urllib + 浏览器 UA，去重 24 个）

**HTTP 200 且正文可读、用于核验的来源（19 个）：**

1. `https://ngsj.njtech.edu.cn/info/1064/1954.htm` — 200（南工大设计院·常州国展资产高新智汇中心）
2. `https://ngsj.njtech.edu.cn/info/1013/1007.htm` — 200（南工大设计院·常州国展 EPC 中标，同机构）
3. `https://m.thepaper.cn/newsDetail_forward_2786200` — 200（澎湃·静安寺广场）
4. `https://sh.people.com.cn/BIG5/n2/2024/0319/c134768-40780072.html` — 200（人民网上海·静安寺广场建成 1999-09-15）
5. `https://www.jfdaily.com/wx/detail.do?id=1010081` — 200（上观/解放日报·卢济威专稿，未提顾如珍）
6. `https://ww.iea-shc.org/Data/Sites/1/publications/CN-Peoples-Bank-of-China.pdf` — 200（IEA SHC·1,842,842 字节）
7. `https://www.miesbcn.com/en/the-pavilion/` — 200（密斯基金会·巴塞罗那德国馆）
8. `https://miesbcn.com/the-pavilion/` — 200（同上，重定向后正式页）
9. `https://www.archdaily.com/109135/ad-classics-barcelona-pavilion-mies-van-der-rohe` — 200（ArchDaily·巴塞罗那德国馆）
10. `https://www.guggenheim.org/about-us/history` — 200（古根海姆官方·历史/赖特/1959）
11. `https://xining.pbc.gov.cn/` — 200（人行西宁中心支行门户，无实测数值）
12. `https://www.bjdclib.cn/ztfw/dhly/yard/202301/t20230116_43210.html` — 200（东城区图书馆·赵堂子胡同3号）
13. `https://www.zgkpw.org.cn/expert/jiliping/content_385726.html` — 200（中国科普网·营造学社/赵堂子胡同3号）
14. `https://discovery.cctv.com/20070119/104637.shtml` — 200（央视网·朱启钤故居；本轮正文解码乱码）
15. `https://inds.cnki.net/kcms/detail?v=qZ0U...XKwEQo=` — 200（CNKI·材料质感博士论文）
16. `http://xueshu.qikan.com.cn/preview/1/322/5803617` — 200（龙源·建筑光影与材质）
17. `http://xueshu.qikan.com.cn/preview/1/322/5314473` — 200（龙源·建筑材料的知觉体验）
18. `https://english.news.cn/20260805/2f2673e5085d4c72aa0efda6b8b087a5/c.html` — 200（新华网英文·帕伊米奥疗养院/阿尔托）
19. `https://paimiosanatorium.com/the-architecture-of-empathy/` — 200（帕伊米奥疗养院官方·1933）

**失败 / 不可用（5 个）：** `https://www.britannica.com/topic/Barcelona-Pavilion`（403）、`https://www.britannica.com/topic/Guggenheim-Museum-New-York-City`（403）、`https://www.archdaily.com/27593/...`（404）、`https://www.archdaily.com/262218/...`（404）、`https://it.alljournals.cn/view_abstract.aspx?...`（200 但跳转 `aipub.cn/815JQ`，59 字节空壳，正文不可读）。另有微信公众号图文多篇返回验证码页，不计源。

> 另 `web_search` 3 次（约 12 组查询）仅作导航，正文核验以 urllib 实抓为准。合计：urllib 直连**去重 24 个 URL**（HTTP 200 共 20 个，其中正文可读 19、空壳 1；失败 4：403×2、404×2）。

## 六、汇总

- **可升级（建议整条置 `needs_verification=false`；均须先登记来源入 `sources.json` 并注明概念贴合）：2 条**
  - `space-definition`：候选实例 **巴塞罗那德国馆（Barcelona Pavilion，西班牙巴塞罗那 Montjuïc；密斯·凡·德·罗与莉莉·赖希设计；1929 年国际博览会建成）**，由 **密斯基金会官网（`https://miesbcn.com/the-pavilion/`，200）＋ArchDaily（`https://www.archdaily.com/109135/...`，200）** 两个独立权威源正文直接支撑三要素；正文须注明“以独立界面/自由平面界定空间，非封闭室内”。
  - `human-scale`：候选实例 **帕伊米奥结核病疗养院（Paimio Sanatorium，芬兰图尔库近郊；阿尔瓦·阿尔托与艾诺·阿尔托设计；1933 年建成）**，由 **新华网英文网（`https://english.news.cn/20260805/.../c.html`，200）＋疗养院官方站点（`https://paimiosanatorium.com/the-architecture-of-empathy/`，200）** 两个独立权威源正文直接支撑三要素；正文须点明“按病人身体姿态与使用感受定尺度（人体尺度）”。
- **可收窄（保留 `needs_verification=true`）：1 条**
  - `material-texture`：**质感→身体知觉/触感/光反射→空间感受**的机理由大连理工 2021 博士论文（CNKI，200）＋两篇龙源专门文章（200×2）正文直接支撑、可移出；**实例设计者/年代仍无具名双源**，保留（龙源权威性有限，仅作专门来源补足、不据此升级整条）。
- **保持待核实：89 条** ＝ 第四节 83 条 ＋ 本轮重点中保持的 6 条（`green-architecture`、`glare`、`sunken-plaza`、`spatial-sequence`、`courtyard`、`curvilinear-perspective`）。
- **本轮实测 `needs_verification=true` 总数：92 条** ＝ 可升级 2 ＋ 可收窄 1 ＋ 保持 89。
- **相关条目说明（不计入 92）：** `east-west-space-compare` 当前 `needs_verification=false`、L1 骨架、无实例段落，无需复核；若升级 L2 需补具名实例。
- **打开 URL 数**：`urllib` 直连**去重 24 个**（HTTP 200 共 20 个：正文可读 19、空壳 1；失败 4：403×2、404×2）；另 `web_search` 3 次（约 12 组查询）作导航。
- **数据更正/冲突提示（不写死）**：常州国展资产高新智汇中心 建筑面积 19291㎡（NJTech 作品页）vs 18897㎡（NJTech 开工文，同院/较早期），且佐证奖项图文均为微信、不可读；人行西宁中心支行 面积 IEA≈1.8 万㎡ / 云知光“1 万平米”/ 恒亦明“1.75 万平米”并列；赵堂子胡同3号“形成时期：清”与“20 世纪 30 年代朱启钤改建”并列；静安寺广场“1999 年 9 月 15 日竣工/建成”澎湃与人民网一致，顾如珍仅澎湃单源。

> 保守原则声明：维基/百科镜像同源不计第二源；微信公众号图文全部被验证码拦截、不作可核验第二源；同机构文章（NJTech 两文）计 1 源；Britannica 本轮 403；ArchDaily 两条猜测 URL 404；巴塞罗那德国馆与帕伊米奥疗养院虽已具备双权威源，但概念贴合需正文注明、且必须先把来源登记入 `sources.json` 方可落地升级。以上仅给结论与证据，**未修改任何条目数据或其它文件**（本文件为唯一产出）。
