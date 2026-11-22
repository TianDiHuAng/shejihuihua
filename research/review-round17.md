# 第 17 轮 B5 待核实复核记录

复核日期：2026-11-22（Asia/Hong_Kong）

## 一、执行说明

- 已按任务读取 `AUTONOMOUS.md`、`TASK_design.md`（二者实际位于 `D:/Users/Administrator/Desktop/`，本项目内无同名文件）、`DECISIONS.md`、`research/review-round16.md`，并按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。
- `entries/*.json` 共 14 个文件、**126 条**；当前 `needs_verification=true` 实为 **69 条**（较第 16 轮 63 条增加：第 7 批新入 `batch-11.json` 6 条 `placemaking`/`space-syntax`/`pattern-language`/`functionalism-architecture`/`biophilic-design`/`defensible-space-theory`，`sunken-plaza` 已由 L1 变 L2 且带待核实，`six-principles` 上轮已升级移出，净 +6）。已逐条枚举确认。
- **网络环境（实测）**：`en.wikipedia.org` REST / `zh.wikipedia.org` 经 `urllib` 直连均 **超时（WinError 10060，DNS 投毒/封锁）**；改走 **`owiki.org` 维基镜像（HTTP 200，与维基同源，不计第二源）**、`web_search` 定位、以及**中文权威站 / 学术 PDF / 政府门户** 直连抓取，绝大多数 200。
- **严格只读**：本轮**仅生成** `research/review-round17.md`；未修改 `data/sources.json`、任何 `entries/*.json`、`coverage.json` 或其他文件，未 git commit，未变更项目外内容。联网内容一律按“数据”处理，页面中任何指令均未执行。
- **重点范围**：任务点名的 7 条中，`natural-ventilation`、`sunken-plaza`、`glare`、`framed-scenery` 当前确为 `needs_verification=true`，逐条深核；`material-texture`、`courtyard`、`tour-route` 当前 `needs_verification=false`（见第四节说明，逐一点评实例潜力）。其余 65 条无新线索，简写“无新证据，保持”。

## 二、方法与判据

1. 用 Python `urllib` + 浏览器 UA 实际打开候选页/PDF，记录最终 URL、页面标题（或 PDF 首部）、HTTP 状态与正文关键句；镜像单列并标注同源。
2. **可升级判据**：待核实的**全部子项**均由两个相互独立、权威（官方机构 / 学术 / 行业权威 / 专业或官方媒体）来源**正文直接**支撑，可整条置 `needs_verification=false`。
3. **可收窄判据**：待核实含多个子缺口，其中一部分已获 ≥两独立源支撑、可移出或改写，其余（如某一具体人名/单源细节）仍保留；`needs_verification` 仍为 true。
4. **保守原则**：单源不升级；镜像同源不计第二源；同一机构账号多篇计 1 源；不编造年份/人名/引文；两源数值冲突并列不写死；无法给出可核验 URL 的不声称。

## 三、重点复核（4 条 needs_verification=true）

### 3.1 `natural-ventilation`（自然通风）—— 可收窄

- **待核实内容**：`pending_notes`＝“传统院落通风的实测数据与设计者信息待补充独立来源。”；`sections.待核实`＝“具体院落实例的通风实测数据待核实。”；实例现为“名称：传统院落自然通风；地点：待核实；设计者：不适用；年份：待核实。”

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://mdpi-res.com/d_attachment/buildings/buildings-12-00629/article_deploy/buildings-12-00629.pdf`（PDF，19 页） | Coupling CFD Simulation and Field Experiments in Summer to Prove Feng Shui Optimizes Courtyard Wind Environments: A Case Study of Prince Kung's Mansion in Beijing — **Buildings（MDPI, 2022, 12, 629）** | 200 | “**field experiments**……from **60 points in Prince Kung's Mansion** by way of CFD simulation and field experiments, were well coupled……”；“The houses were first built in **45th year of Qianlong period (1780 AD)**……” |
| `http://www.scszlxh.com/uploads/a31474cc.pdf`（PDF，8 页） | 经典著作中建筑风环境描述的科学诠释及实证 — **《制冷与空调》第32卷第5期（2020，大连理工大学建筑环境与新能源研究所 徐四维等）** | 200 | “对福建省福鼎市**翠郊村吴氏大院**（清乾隆年间）……**实测调查**……院落内各测点平均风速为 **0.2～0.3 m/s**，院落外界各测点风速为 0.6～……” |
| `https://www.pgm.org.cn/pgm/lsyg/201705/fe07519b863b4d4385473890770aee0b.shtml` | 恭王府历史沿革 — **文化和旅游部恭王府博物馆** | 200（第 16 轮已核） | “乾隆四十五年（1780 年），大学士和珅奉旨建十公主府。” |
| `https://sjfw.mct.gov.cn/site/dataservice/culdetails?curId=10&id=34785` | 5A 级景区·恭王府博物馆 — **文化和旅游部数据服务** | 200（第 16 轮已核） | “恭王府始建于清乾隆四十五年（1780），为和孝公主府（与权臣和珅共用）……” |

- **结论：可收窄。** “传统院落通风实测数据”现有 **两篇相互独立的学术现场实测**（恭王府 MDPI 2022 现场 60 测点＋CFD；翠郊吴氏大院《制冷与空调》2020 院落内 0.2～0.3 m/s）。**设计者可定为“不适用（传统工匠营建、无具名建筑师）”**。**但仍不整条升级**：若把实例具体到**恭王府**这一具名实例，其**自身**实测仍为单源（仅 MDPI，另一实测属不同院落吴氏大院），按“单源不升级”保守原则仅列收窄。
- 建议改写实例：“名称：北京恭王府（传统院落自然通风）；地点：北京；设计者：不适用（传统工匠营建）；年份：清乾隆四十五年（1780）；另见福建福鼎翠郊吴氏大院院落实测（院落内平均风速 0.2～0.3 m/s）。”据此可将“实测数据/设计者”两子项移出待核实，仅保留“具名实例自查实测量待补第二源”这一最小标注。

### 3.2 `sunken-plaza`（下沉广场）—— 可收窄

- **待核实内容**：`pending_notes`＝“‘顾如珍负责建筑工程’与‘1999 年落成’为单源（澎湃转载不计第二源），待补充独立来源；**其他实例的设计者与年代待核实**。”

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://www.zgcsb.com/news/pinDao/2023-11/24/a_482136.html` | ASSC70周年｜卢济威：上海是中外建筑师共创的杰作 — **中国城市网（中国城市报，2023-11-24）** | 200 | “**1999年**，依然是在静安寺交通枢纽，**卢济威设计建成了**核心公共空间——**静安寺下沉广场**……被视作城市设计的经典之作。” |
| `https://www.jingan.gov.cn/rmtzx/003008/003008006/20231027/1fc54614-89df-427d-b1cf-09315a285108.html` | 依旧少年｜87岁的卢济威教授仍很忙碌 — **上海市静安区人民政府** | 200 | “……还有一座**巨大的下沉式广场**……它的**设计者就是**我国著名建筑师、同济大学教授**卢济威**……” |
| `https://news.tongji.edu.cn/info/1006/92585.htm` | 【上观新闻】卢济威教授：中国现代城市设计创始者之一，静安寺广场……都是他作品 — **同济大学新闻网（转上观新闻）** | 200 | 标题与正文确认“**静安寺广场**……都是他（卢济威）作品”，并述其为“**下沉式广场**”。 |
| `https://m.thepaper.cn/newsDetail_forward_2786200` | “魔都”新生：同济大学与静安寺广场和南京路步行街的修建 — **澎湃新闻**（原有源 `thepaper-jingan`） | 前轮已核（本轮未重抓） | “**1999年**，新落成的静安寺广场……**卢济威的夫人——同济设计院副总建筑师顾如珍负责了具体的建筑工程**……” |
| `https://www.nanning.gov.cn/ywzx/bmdt/2022bmdt/t5221791.html` | 友城地铁广场启用 见证我市与国际友城深厚情谊 — **广西南宁市人民政府门户网站（来源南宁日报，2022-06-08）** | 200 | “6 月 7 日，由南宁市与意大利克雷马市共同设计建造的**南宁地铁那洪立交站双层下沉广场——友城地铁广场**正式启用……**由克雷马市进行整体装潢设计，南宁市进行施工建设**……**2022 年**实现竣工。” |
| `https://gx.chinadaily.com.cn/a/202206/08/WS62a01682a3101c3ee7ad96ff.html` | 惊艳！国内首个“友城地铁广场”亮相广西南宁 — **中国日报网（广西记者站，2022-06-08）** | 200 | “……**友城地铁广场**正式投入使用……**该项目由克雷马市设计师主创**、南宁轨道及外事单位配合深化……**2022 年实现广场竣工**。” |
| `https://gx.cri.cn/2022-06-08/c5397444-5a34-37c7-22f3-71d7d3c523d1.html` | 友城地铁广场启用（来源南宁日报）— **国际在线** | 200 | 与南宁市政府同源（均转载南宁日报），**不计独立第二源** |

- **结论：可收窄。** 三条子项进展：①**“1999 年落成”** 现由澎湃＋中国城市网（“1999 年……建成”）**双独立源**支撑；②**“卢济威主持设计”** 由澎湃＋中国城市网＋静安区政府＋同济新闻**多源**支撑；③**“其他下沉广场实例”** 由南宁 **友城地铁广场** 落实——设计者（克雷马市设计、南宁施工/克雷马设计师主创）、年份（2022 年竣工/6 月 7 日启用）由**南宁市政府门户＋中国日报**双独立权威源确认。**唯一残留**：“**顾如珍负责建筑工程**”仍仅澎湃单源（学术题录 `alljournals`/维普显示该论文作者含“卢济威、顾如珍、孙光临、张斌”，但该页为 JS 渲染、正文不可直抓，不作硬依据）。
- 建议改写实例：“静安寺下沉广场（上海静安寺，卢济威主持城市设计、1999 年落成；顾如珍负责建筑工程为单源，作补充说明）／南宁·友城地铁广场（南宁地铁那洪立交站双层下沉广场，克雷马市设计、南宁市施工，2022 年启用）。”若将“顾如珍”细节降为补充说明或改为“卢济威主持城市设计”，则整条可升级；保守起见本轮列**收窄**，`needs_verification` 保持 true。

### 3.3 `glare`（眩光）—— 保持

- **待核实内容**：`pending_notes`＝“办公实例的照度与眩光实测数据待补充独立来源。”；`sections.待核实`＝“具体办公实例的照度与眩光指数待核实。”

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://task61.iea-shc.org/Data/Sites/1/publications/CN-Peoples-Bank-of-China.pdf`（PDF，4 页） | Human Centric Lighting in an office building — **IEA SHC Task 61 案例（监测：Luo Tao，中国建筑科学研究院 CABR）** | 200 | 项目为 **Xining Central Sub-branch of the People's Bank of China（中国人民银行西宁中心支行）**，“Built in the **1990s**……20 floors”；实测表：**Illuminance on working plane (lux)** Office 475、Meeting 322/762、Hall 228、Corridor 54；Uniformity U0；**Unified glare rating UGR** R19 / M8·19 / ≤25；**Luminance (cd/m²)** 3340/1842/623 等。 |
| `https://iea-shc.org/Data/Sites/1/publications/US-NYC-Project.pdf` | Advanced lighting upgrades in daylit offices — IEA SHC Task 61 | 200 | 匿名“monitored commercial office building”，报 DGP Class A、照度 200–300 lx，但**未具名**。 |
| `https://www.iea-shc.org/Data/Sites/1/publications/US-Oakland.pdf` | Enhancing workplace quality… dual-zone shades — IEA SHC Task 61 | 200 | 匿名“LBNL test-bed”，测 discomfort glare 与 workplane illuminance 100–2000 lx，但**未具名**。 |

- **结论：无新证据（关键实例单源），保持。** 已锁定**一个具名办公实例**——“中国人民银行西宁中心支行”：**照度（办公区 475 lx 等）＋眩光指数（UGR 8–19）都有实测**，且由 IEA SHC / 中国建研院权威发布；但仅 **IEA 单一来源**。其余 IEA 案例及 Tehran Pars Tower（模拟）或**未具名**、或**非实测**，均不能凑成“同一/另一具名办公实例”的**第二独立源**。按“单源不升级”，`needs_verification` 保持 true；可作为具名线索记入 BACKLOG，待补第二独立源后可升级或收窄。

### 3.4 `framed-scenery`（框景，L1）—— 可升级

- **待核实内容**：`pending_notes`＝“仅见中国园林综合条目，待补充针对框景的独立来源。”（唯一缺口＝缺“专门针对框景”的独立来源）。

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://www.peopleapp.com/rmharticle/30028686345` | 社教｜似实而虚，似虚又实——中国古典园林的框景之美 — **中国园林博物馆（人民日报“人民号”官方账号，2022-07-06）** | 200 | 全文专论框景：“中国古典园林中建筑的**门、窗、洞**……把远处的山水或人文景观包含其中……**利用建筑物框架、空窗、洞门、廊柱围拢**……套住某处景色”；列**三种形式**并举具名实例：**拙政园“别有洞天”、拙政园东部芙蓉榭（落地罩/圆光罩）、留园“小蓬莱”**、中国园林博物馆片石山房“竹石图”；引计成《园冶》“藉以粉壁为纸、以石为绘”、李渔“尺幅窗/无心画”。 |
| `https://www.beijing.gov.cn/renwen/whrl/rdtj/202303/t20230303_2928040.html` | 颐和园“画中游”景区重开 — **北京市人民政府门户（首都之窗，来源北京晚报，2023-03-03）** | 200 | “‘画中游’景区**始建于乾隆年间**，由澄辉阁、爱山楼、借秋楼……组成……登上澄辉阁 2 层，**8 个亭柱巧妙地形成了多种画幅的‘画框’**，让游客在不同方向体验独特视角的景色……既像是真在画中游览，又像是在观赏风景画。”（框景具名实例：颐和园画中游） |
| `https://www.peopleapp.com/rmharticle/30020551454` | 园林线上课堂（91）｜苏州古典园林·造园的艺术手法（二）— **中国园林博物馆（人民号，2020-12-26）** | 200 | “**框景** 利用门洞、窗框等将一定范围内景致框住，取远处的山水美景或人文美景在内。就好似相机的取景框……”（与上一篇同机构，**计 1 源**） |

- **结论：可升级。** 唯一缺口“缺专门针对框景的独立来源”已被 **中国园林博物馆《框景之美》专文**（正文直接定义框景机制＋三种形式＋多个具名实例）补足；该文与既有 `wp-chinese-garden`（维基，综合条目）相互独立。**北京市政府（首都之窗）** 另提供具名实例 **颐和园“画中游”**（清乾隆年间，“8 个亭柱形成多种画幅的‘画框’”）。故“框景”已有 ≥2 个相互独立权威来源正文直接支撑。
- 建议：置 `needs_verification=false`；实例可写“颐和园‘画中游’（北京，清乾隆年间始建；设计者未具名/皇家园林）”或“拙政园芙蓉榭·留园小蓬莱（苏州，拙政园明正德四年 1509 王献臣建、文徵明参与）”。注意：两篇“人民号”同为**中国园林博物馆**账号，按同机构计 1 源；`人民号`系自媒体发布平台，权威性以**博物馆官方账号**论，已与**北京市政府**官媒互补。

## 四、任务点名但当前 `needs_verification=false` 的 3 条（点评实例潜力，不改数据）

> 任务曾把这三条列为“有实例潜力”，但现库中三者均为 `needs_verification=false`、L1，不属于本轮待核实条目，故不作升级/收窄判定，仅记实例潜力供 BACKLOG 的 L1→L2 参考。

- `courtyard`（庭院，L1，源 `wp-courtyard`+`wp-chinese-garden`）：L2 实例候选如**北京四合院**、徽州民居天井；需另补“名称/地点/设计者/年份”双源后再升 L2。**非待核实，保持。**
- `tour-route`（游线，L1，源 `wp-chinese-garden`+`wp-wayfinding`）：园林游线具名实例候选**拙政园**（东部兰雪堂→芙蓉榭→听雨轩→海棠春坞→中部山水一线），但现有检索到的游线来源多为旅行社/攻略（非权威），暂不足双源，建议列入 BACKLOG。**非待核实，保持。**
- `material-texture`（材料质感，L1，源 `wp-building-material`+`wp-vernacular-architecture`）：实例候选为乡土材料（夯土墙、青砖、木构）之质感，缺“具体建筑＋设计者/年份”双源，建议列入 BACKLOG。**非待核实，保持。**

## 五、其余 65 条待核实（无新证据，保持）

以下条目本轮未打开针对性 URL（按任务“其余无新线索简写保持”）；待核实项多为“实例的具体名称/设计者/年份”或“实测/性能参数”，未取得成对的独立权威来源直接支撑，按保守原则保持 `needs_verification=true`。

| # | id | 待核实内容（简） | 结论 |
| --- | --- | --- | --- |
| 1 | `linear-perspective` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 2 | `scattered-perspective` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 3 | `composition` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 4 | `balance` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 5 | `proportion` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 6 | `color-theory` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 7 | `value` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 8 | `one-point-perspective` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 9 | `two-point-perspective` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 10 | `three-point-perspective` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 11 | `aerial-perspective` | 实例的作者与年代待核实；空气透视早期实例跨度广，正文只作一般性说明。 | 无新证据，保持 |
| 12 | `foreshortening` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 13 | `vanishing-point` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 14 | `horizon-line` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 15 | `rule-of-thirds` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 16 | `figure-ground` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 17 | `negative-space` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 18 | `hue` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 19 | `saturation` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 20 | `primary-colors` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 21 | `complementary-colors` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 22 | `warm-cool` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 23 | `chiaroscuro` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 24 | `borrowed-scenery` | 借景北寺塔的园外距离记载不一（约 1.5–1.7 公里），具体数值待核实；正文并列、不写死。 | 无新证据，保持 |
| 25 | `opposed-scenery` | 中国园林条目未直接支撑“对景”的核心机制；需补充专门来源，实例的设计者与年份亦待核实。 | 无新证据，保持 |
| 26 | `screened-scenery` | 苏州园林障景具体实例的设计者与年份待补充独立来源。 | 无新证据，保持 |
| 27 | `winding-path` | 仅见中国园林综合条目，待补充针对曲径的独立来源。 | 无新证据，保持 |
| 28 | `gothic` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 29 | `renaissance-style` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 30 | `modernism` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 31 | `postmodernism` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 32 | `mannerism` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 33 | `beaux-arts` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 34 | `plein-air` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 35 | `chinese-architecture-style` | 具体单体建筑工匠归属（蒯祥）仅单源，待补充独立来源。 | 无新证据，保持 |
| 36 | `light-well` | 具体天井实例的采光与通风实测数据待补充独立来源（机制层面可参见自然通风条目）。 | 无新证据，保持 |
| 37 | `leaked-scenery` | 所引来源以机制描述支持漏景，未出现“漏景/漏窗”字面术语；实例的设计者与年份待核实。 | 无新证据，保持 |
| 38 | `vernacular-material` | 具体地区乡土材料的性能数据待补充独立来源。 | 无新证据，保持 |
| 39 | `color-harmony` | 面积比例与整体感等经验性表述待补充直接来源；实例的设计者与年份待核实。 | 无新证据，保持 |
| 40 | `composition-placement` | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 无新证据，保持 |
| 41 | `axis` | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 无新证据，保持 |
| 42 | `stack-ventilation` | 热压通风实例的通风实测数据待补充独立来源。 | 无新证据，保持 |
| 43 | `thermal-comfort` | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 无新证据，保持 |
| 44 | `service-route` | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 无新证据，保持 |
| 45 | `gestalt-organization-laws` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 46 | `color-psychology` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 47 | `environmental-psychology` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 48 | `hardscape-softscape` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 49 | `wayfinding` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 50 | `lighting-design` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 51 | `daylight-factor` | 具体实例的采光系数数值与设计者待补充独立来源。 | 无新证据，保持 |
| 52 | `mixed-mode-ventilation` | 混合通风实例的控制策略与能耗数据待补充独立来源。 | 无新证据，保持 |
| 53 | `material-durability` | 实例寿命与维护数据待补独立来源；具体退化机制的通用列表待补专门来源。 | 无新证据，保持 |
| 54 | `transparent-material` | 透明与半透明材料实例的性能参数待补充独立来源。 | 无新证据，保持 |
| 55 | `functional-zoning` | Architecture 与 Interior design 未直接给出“功能分区”术语定义；核心概念与实例数据均待补独立来源。 | 无新证据，保持 |
| 56 | `gray-space` | 檐下与廊道实例的设计者与年代待补独立来源。 | 无新证据，保持 |
| 57 | `enclosure` | 具体院落的设计者与年代待补独立来源。 | 无新证据，保持 |
| 58 | `placemaking` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 59 | `space-syntax` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 60 | `pattern-language` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 61 | `functionalism-architecture` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 62 | `biophilic-design` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 63 | `defensible-space-theory` | 实例的具体名称、设计者与年代待补充独立来源。 | 无新证据，保持 |
| 64 | `perspective` | 透视演示年代取学界通行约数（约 1413 年），原始文献年代存争议，正文不写死。 | 无新证据，保持 |
| 65 | `sunken-courtyard` | 两类实例的历史原型对应关系与一般苏州庭院营造者归属待核实。 | 无新证据，保持 |

## 六、本轮实际打开 / 请求的 URL（urllib 直连，去重）

- 有效正文/PDF（HTTP 200）：`peopleapp 30028686345`、`peopleapp 30020551454`、`nanning.gov.cn/t5221791`、`gx.chinadaily …WS62a01682…`、`gx.cri.cn …c5397444…`、`ylj.suzhou.gov.cn 造景艺术`、`task61.iea-shc CN-Peoples-Bank-of-China.pdf`、`iea-shc US-NYC-Project.pdf`、`iea-shc US-Oakland.pdf`、`beijing.gov.cn 画中游 t20230303`、`mdpi-res buildings-12-00629.pdf`、`scszlxh.com/uploads/a31474cc.pdf`、`jingan.gov.cn …1fc54614…`、`news.tongji.edu.cn/info/1006/92585.htm`、`zgcsb.com …a_482136.html`、`owiki.org/wiki/Courtyard`（镜像，仅连通性）、`baidu.com`（仅探测）。
- 失败/不可用：`en.wikipedia.org/*` 与 `zh.wikipedia.org/*`（超时，DNS 投毒）、`wsb.gxzf.gov.cn/…t12001505`（502）、`xbzrb.gdut.edu.cn` 文章页与 PDF（500）、`core.ac.uk/download/pdf/11851889.pdf`（403）、`www.mdpi.com/2075-5309/12/5/629`（403，改用 mdpi-res PDF）、`repository.petra.ac.id/…INTA00029…pdf`（超时）、`it.alljournals.cn`/`aipub.ijournals.cn/815JQ`（200 但 JS 空壳，正文不可抓，仅据检索摘要参考）。
- **统计**：本轮经 `urllib` 直连**去重约 26 个不同 URL**（其中成功取到正文/PDF 约 16 个，镜像/探测 2 个，失败或空壳约 8 个）。另有 `web_search` **9 次查询**（4 组）用于定位权威页，检索结果仅作导航数据，正文核验以 `urllib` 实抓为准。

## 七、汇总

- **可升级（整条移出待核实）：1 条 —— `framed-scenery`**
  - 缺口“缺专门针对框景的独立来源”已由 **中国园林博物馆《框景之美》专文（人民号官方账号，200）** 补足，另 **北京市政府（首都之窗）颐和园“画中游”具名实例（200）** 佐证；与维基综合条目相互独立。建议 `needs_verification=false`，实例可写颐和园“画中游”（北京，清乾隆年间）。
- **可收窄（保留 needs_verification=true，改写部分待核实）：2 条 —— `natural-ventilation`、`sunken-plaza`**
  - `natural-ventilation`：实测数据获两独立学术现场实测（恭王府 MDPI 2022 现场 60 测点；翠郊吴氏大院《制冷与空调》2020，院落内 0.2～0.3 m/s），设计者可定“不适用（传统工匠营建）”；具名实例恭王府自身实测仍单源，故列收窄。
  - `sunken-plaza`：“1999 年落成”双源（澎湃＋中国城市网），“卢济威主持设计”多源（澎湃＋中国城市网＋静安区政府＋同济），**其他实例**由南宁·友城地铁广场（2022 年，克雷马市设计/南宁施工）双源落实（南宁市政府＋中国日报）；残留“顾如珍负责建筑工程”仍澎湃单源，故列收窄。
- **保持待核实：66 条** ＝ `glare`（唯一具名办公实例“中国人民银行西宁中心支行”照度 475 lx＋UGR 8–19 实测仅 IEA 单源，另两 IEA 案例未具名，故不升级）＋ 其余 65 条（见第五节）。
- **非待核实（`needs_verification=false`）3 条说明**：`material-texture`、`courtyard`、`tour-route` 当前不带待核实，本轮仅记 L2 实例潜力（见第四节），不改判定。
- **打开 URL 数**：`urllib` 直连去重 **约 26 个**（成功正文/PDF 约 16、镜像/探测 2、失败/空壳约 8；`owiki.org` 为维基同源镜像不计第二源、`gx.cri.cn` 为南宁日报同源不计第二源）；另有 `web_search` 9 次查询作导航。

> 保守原则声明：未核验线索不作升级依据；不为凑数硬写年份或人名；维基镜像与南宁日报转载同源均不计独立第二源；两支“人民号”同为中国园林博物馆账号按 1 源计；`顾如珍`（澎湃单源）、`glare` 具名实例（IEA 单源）、借景 1.5/1.7 公里冲突均**并列/标注、不写死、不升级**。以上仅给结论与证据，**未修改任何条目数据或其它文件**（本文件为唯一产出）。
