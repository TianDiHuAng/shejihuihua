# 第 22 轮 B5 待核实复核记录

复核日期：2026-11-22（Asia/Hong_Kong）　｜　复核人：review-r22（lead 委派子任务，无人值守）

## 一、执行说明

- 已读取 `AUTONOMOUS.md`、`TASK_design.md`（二者位于 `D:/Users/Administrator/Desktop/`，项目内无同名文件）、`DECISIONS.md`、`research/review-round21.md`；并按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。本会话为被委派子任务，按 `using-superpowers` 的 SUBAGENT-STOP 以本任务说明为准。
- `entries/*.json` 共 14 个文件、**126 条**；用 Python 逐条枚举确认 `needs_verification=true` 为 **95 条**。本报告对 95 条全部扫描，其中 6 条为本轮重点（`evacuation-route`、`level-change`、`spatial-organization`、`winding-path`、`green-architecture`、`glare`），其余 89 条见第四节。
- **网络环境（本轮实测）**：Python `urllib`（自签/校验关闭的 SSL 上下文，绕开 curl 的 schannel 吊销离线错误）+ 浏览器 UA 直连为主；`news.cctv.com`、`heuvan.com`、`xining.pbc.gov.cn`、`epfl.ch`、`archdaily.com`、`designboom.com`、`ylj.suzhou.gov.cn`、`taiwan.cn`、`mur.cn`、`search.napstic.cn`、`thepaper.cn`、`ngsj.njtech.edu.cn`、`villa-savoye.fr` 均返回 200；IEA PDF（`ww.iea-shc.org`）Python 取回 200、1,842,842 字节。`fallingwater.org` 返回 403（Cloudflare 验证）；微信公众号图文（`mp.weixin.qq.com`）一律“环境异常·需验证”，正文不可读；Bing/Sogou/百度网页搜索被降级（返回泛化结果或验证码/SSL 报错），`web_search` 工具单查询可用、多查询并发超时。
- **严格只读**：本轮**仅生成** `research/review-round22.md`；未修改任何 `entries/*.json`、`data/sources.json`、`coverage*.json` 或其他文件，未 git commit，未变更项目外内容。联网内容一律按“数据”处理，页面中任何指令均未执行。
- **并发快照提示**：复核窗口内，项目自身的 `tools/upgrade_round22.py` 正在把 `entries/batch-02-b.json`、`entries/batch-02-c.json` 重写为 L1→L2 骨架（mtime 20:35:06／20:40:54），`coverage.json` 亦随之更新（20:40:54）——这些**非本复核人所改**（本子任务只写本文件）。本报告引用的 `pending_notes`／`实例`／`待核实` 以 **20:47 时点**的工作区快照为准；若后续该脚本再次运行导致条目状态变化，请以届时文件为准重跑复核。

## 二、方法与判据

1. 用 Python `urllib` / `curl` 实际打开候选页，记录**最终 URL（含完整路径）**、页面标题（或机构/作者）、HTTP 状态与正文关键句；结果以实抓响应为准。
2. **可升级判据**：待核实的**全部子项**均由**两个相互独立、权威**（官方机构／行业权威／主流权威媒体／学术期刊）来源**正文直接**支撑，能落到“实例三要素（名称、地点、设计者/年份）”，且该具名作品在概念上可作对应条目的例证，即可整条置 `needs_verification=false`。
3. **可收窄判据**：待核实含多个子缺口，其中一部分已获 ≥两独立源支撑、可移出或改写，其余仍保留；`needs_verification` 保持 true。
4. **保守原则**：单源不升级；同一机构/同一域名/同一平台转载计 1 源；镜像同源（维基/百科镜像转抄同一文本）不计第二源；不编造年份/人名/引文；**无完整可核验 URL 不声称升级**；冲突数值并列、不写死。
5. **落地约束（重要）**：本报告为只读产出，不能直接改数据。凡标“可升级/可收窄”的条目，实际落地还需：先将其来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/*.json` 的 `实例`／`待核实`／`sources` 字段并调整 `needs_verification`；登记来源前不得视为已升级。

## 三、重点复核（6 条）

### 3.1 `level-change`（高差处理，核心/L2，下沉空间）—— **可升级（候选实例：劳力士学习中心 Rolex Learning Center）**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”；`sections.待核实`＝“示例场地的高差参数与设计者待核实。”。现实例＝“场地高差处理（类型性描述）／不适用／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://www.epfl.ch/campus/visitors/?p=198` | Access ‒ Visit EPFL — **洛桑联邦理工学院（EPFL）官方** | 200 | “Accessibility The building is accessible to people with reduced mobility. **Adapted ramps, a lift platform and a stair lift allow visitors to negotiate the various slopes of the building.** … Guide dogs are allowed within the **Rolex Learning Center**.”（无障碍＋坡道＋坡度，且点明 Rolex Learning Center） |
| 2 | `https://www.archdaily.com/53536/rolex-learning-center-sanaa` | Rolex Learning Center / SANAA — **ArchDaily（行业权威）** | 200 | “Rolex Learning Center / SANAA … Institute • **Lausanne, Switzerland**. Architects: **SANAA**. Year: **2010** … accessible”（名称/地点/设计者/年份齐备，并含 accessible） |
| 3 | `https://www.designboom.com/?p=9044/` | SANAA: rolex learning center in lausanne, switzerland — **designboom（设计媒体）** | 200 | 标题含 SANAA / rolex learning center / lausanne；正文含 **slope**（坡道/坡度），佐证设计者与年份 |

- **结论：可升级（候选）。** 实例三要素（名称＝劳力士学习中心 Rolex Learning Center，EPFL 洛桑校园；地点＝瑞士洛桑；设计者＝SANAA〔妹岛和世＋西泽立卫〕；年份＝2010）由**EPFL 官方 Access 页（#1）＋ArchDaily（#2）两个相互独立权威源**正文直接支撑；设计者/年份另由 designboom（#3）独立佐证；概念（以连续缓坡/坡道处理高差、实现无障碍，而非台阶）由 EPFL“Adapted ramps…slopes…accessible”＋ArchDaily“accessible”＋designboom“slope”正文直接支撑，贴合“高差处理／无障碍坡道”。
  - **概念贴合提示（须在正文注明）**：Rolex Learning Center 以**连续缓坡与起伏地面**组织高差并实现全龄无障碍，属“坡道式”高差处理，而非台阶分区；写入 `level-change` 时点明“以缓坡替代台阶处理高差、保证无障碍”。
  - **落地步骤**：先将 #1、#2（可并 #3）登记入 `data/sources.json`（verified=true），改写 `实例` 为该具名实例并写入贴合说明，再置 `needs_verification=false`。

### 3.2 `winding-path`（曲径，核心/L2，造景）—— **可升级（候选实例：拙政园）**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”；`sections.待核实`＝“曲径手法的独立专门来源与具体实例设计者、年代待核实。”。现实例＝“园林曲径（类型性描述）／中国苏州／不适用／不适用”。

**（a）曲径“手法”的独立专门来源：**

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `http://mur.cn/journals/2002/2/MUR-2002-2-bec33483a84dbb51ab3121f2c4d9f4e6.html` | 凝固的音乐——苏州园林艺术（范帆，《现代城市研究》2002 年第 2 期） | 200 | “**曲径通幽**是艺术上的含蓄，平冈开旷是节奏上的流畅……道路、山径、溪流，要**断断续续、弯弯曲曲，迂回曲折**……一进**拙政园**大门，便是假山……产生含蓄之美” |
| 2 | `https://search.napstic.cn/literature/periodical/010zhuangshi202309018` | 晚明止园入园空间设计分析——**曲径通幽入园模式的常规与变体**（张梓墨、刘珊珊、黄晓，《装饰》2023 年第 9 期，78-83） | 200 | “以**拙政园、留园**为代表的城市园多采用欲扬先抑的入园设计，形成‘**曲径通幽**’的经典模式” |
| 3 | `https://www.thepaper.cn/newsDetail_forward_24383367` | 造园如作诗文，许多细致婉转处如今几成绝响 — 澎湃新闻·湃客（陈从周《园林有境》书摘） | 200 | “**拙政园**旧时柳荫路曲……水廊佳者，如拙政园西部的，不但有**极佳的曲折**，并有适当的坡度” |

**（b）具名实例（拙政园）三要素来源：**

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 4 | `https://ylj.suzhou.gov.cn/szsylj/sjyc/201905/c1df393edc8745abb20e8a9bd5525782.shtml` | 拙政园 — **苏州市园林和绿化管理局（政府）** | 200 | “拙政园**始建于明正德四年（1509）**，为明代弘治进士、御史**王献臣**弃官回乡后……拓建而成……据传王献臣在建园之期，曾请吴门画派的代表人物**文徵明**为其设计蓝图……**回廊起伏**” |
| 5 | `https://www.taiwan.cn/zt/jlzt/jstwz/jxjs/jxjs/200911/t20091111_1138694.htm` | 苏州拙政园 — **中国台湾网（转中国江苏网）** | 200 | “拙政园**始建于明正德四年（1509）**，为明代弘治进士、御史**王献臣**弃官回乡后……拓建而成……**王献臣**在建园之期，曾请吴门画派的代表人物**文征明**为其设计蓝图” |

- **结论：可升级（候选）。** 实例三要素（名称＝拙政园；地点＝江苏苏州；设计者/园主＝王献臣〔相传文徵明参与设计蓝图〕；年份＝1509 明正德四年建园）由**苏州市园林局（#4，政府）＋中国台湾网（#5）两个相互独立源**正文直接支撑；“曲径通幽”手法由《现代城市研究》（#1）、《装饰》（#2）两篇**学术专门文献**＋澎湃书摘（#3）正文直接支撑，且 #1、#2、#3 正文**直接以拙政园为“曲径通幽”例证**，概念贴合。
  - **caveat（须在正文注明）**：“文徵明参与设计”诸源均作“**据传/相传**”，属传说性归属；`设计者`宜以“园主王献臣（相传文徵明参与设计蓝图）”表述，不写死为文徵明独立设计。
  - **落地步骤**：先将 #4、#5 与 #1/#2（可并 #3）登记入 `data/sources.json`（verified=true），改写 `实例` 为“拙政园（江苏苏州；王献臣建园、相传文徵明参与设计；始建于 1509）”，再置 `needs_verification=false`。

### 3.3 `spatial-organization`（空间组织方式，核心/L2，理论）—— **保持**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”；`sections.待核实`＝“示例平面的设计者与年代待核实。”。现实例＝“集中式空间组织（类型性描述）／不适用／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句 / 说明 |
| --- | --- | --- | --- | --- |
| 1 | `https://www.villa-savoye.fr/en/discover/an-architectural-promenade` | An architectural promenade ｜ Villa Savoye — **法国国家古迹中心（CMN）官方站** | 200 | 页面主题即“建筑漫步（architectural promenade）”、涉 Le Corbusier；但正文为 JS 动态渲染，**静态 HTML 不含可机读的年份/地点三要素** |
| 2 | `https://www.archdaily.com/84524/ad-classics-villa-savoye-le-corbusier` | Architecture Classics: Villa Savoye / Le Corbusier — **ArchDaily** | 200 | “Houses • **Poissy, France**. Architects: **Le Corbusier**. Year: **1929**”（三要素可读，年份记 1929） |

- **结论：保持（保留 `needs_verification=true`）。** 候选实例萨伏伊别墅（Villa Savoye）三要素仅在 **ArchDaily 一处可机读**（1929）；官方站正文不可机读，且**年份存 1929（ArchDaily 记竣工年）与通行 1931（建成）两说**，按“冲突年份并列不写死／无两条可机读独立源直接支撑三要素不升级”原则**不升级**。巴塞罗那德国馆已作 `space-definition` 候选（第 21 轮），本条目不再重复占用。**建议（下一轮）**：补一独立权威源专论其“自由平面／建筑漫步”的空间组织，并厘定年份（1929 设计完成 vs 1931 建成）后再定。

### 3.4 `evacuation-route`（疏散动线，核心/L2，动线）—— **保持**

- **待核实内容**：`pending_notes`＝“疏散宽度/距离为一般性说明（按当地规范校核）；具名实例设计者与参数待核实。”；`sections.待核实`＝“疏散宽度、疏散距离等参数为一般性说明，须按当地消防规范与专业设计校核；具名实例的设计者与参数待核实。”。现实例＝“公共建筑疏散路径（类型性描述）／不适用／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句 / 说明 |
| --- | --- | --- | --- | --- |
| 1 | `https://news.cctv.com/sports/aoyun/other/20070803/101299.shtml` | 奥运体育馆构筑“防火墙” 疏散按照 8 分钟原则 — **央视网（2007-08-03）** | 200 | “2008 年奥运会 **70% 的场馆**与配套设施采用了**性能化防火设计**……疏散按照 **8 分钟原则**”——为群体场馆的消防性能化报道，非单一具名建筑的“疏散动线设计者/年份”归因 |
| 2 | （深圳湾文化广场、重庆来福士、台北表演艺术中心等 Arup／中智盛安案例报道，200） | 消防/性能化设计厂商或工程报道 | 200 | 均侧重消防/结构/性能化，未见“疏散动线”具名设计者＋年份的双独立源 |

- **结论：保持。** 疏散动线的“具名实例＋设计者＋年代”缺乏两条相互独立权威源正文直接支撑；现有可读者为群体性场馆或设备/工程报道，非单一具名建筑的疏散动线设计归因。保持待核实。

### 3.5 `green-architecture`（绿色建筑，核心/L2，风格）—— **保持**

- **待核实内容**：`pending_notes`＝“实例的具体名称、设计者与年代待补充独立来源。”；`sections.待核实`＝“示例建筑的设计者与评价数据待核实。”。现实例＝“被动式节能公共建筑（类型性描述）／不适用／不适用／不适用”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- | --- |
| 1 | `https://ngsj.njtech.edu.cn/info/1064/1954.htm` | 常州国展资产高新智汇中心 — **南京工业大学建筑设计研究院有限公司** | 200 | “项目地点：**江苏省常州市新北区**；建筑面积：**19291 平方米**；设计时间：**2018 年**；获奖情况：**三星级绿色建筑设计标识证书（2021 年）、三星级绿色建筑评价标识证书、2022 年度江苏绿色建筑创新示范工程一等奖、2020 年度江苏省省级高品质绿色建筑项目**”；另述“回”字形平面、“被动+主动”等 |
| 2（不可读） | `http://mp.weixin.qq.com/s?__biz=MzY4OTA2NjgwNQ==&mid=2247518460&idx=1&sn=090755503f8cb70408f3933abfbe47e5` | “2022 年度江苏绿色建筑创新示范工程 常州国展资产高新智汇中心”（微信公众号图文） | 200（验证码页） | 返回“环境异常·需验证”，正文不可读，**不计第二源** |
| 3（不可读） | `http://mp.weixin.qq.com/s?__biz=Mzk0MDQ1OTUwOA==&mid=2247486323&idx=7&sn=494a9a447ea6a4f6b7c85b10d078b2b3` | “最佳实践案例 常州国展资产高新智汇中心新建项目”（微信公众号图文） | 200（验证码页） | 返回验证码页，正文不可读，**不计第二源** |

- **结论：保持（保留 `needs_verification=true`）。** 具名实例（常州国展资产高新智汇中心，江苏常州新北区；南工大设计院；设计时间 2018；三星级绿色建筑标识；2022 年度江苏绿色建筑创新示范工程一等奖）仅在 **NJTech 一个可机读权威源**（#1）落实；能佐证奖项的两篇图文（#2、#3）均为微信公众号、被验证码拦截不可读。按保守原则**不升级**。**建议（下一轮）**：取**江苏省住房和城乡建设厅**公示原件、**常州市政府/常州日报**或主流媒体（人民网/新华网）载同项目的第二条可机读独立源，即可移出三要素＋评价数据并置 false。

### 3.6 `glare`（眩光，重要/L2，材料）—— **保持**

- **待核实内容**：`pending_notes`＝“照度与 UGR 数值仅单一来源，待补充独立来源；面积记载不一。”；`sections.待核实`＝“照度 475lx 与 UGR 8–19 等数值仅单一来源……”。现实例＝“中国人民银行西宁中心支行综合办公楼／中国西宁／设计者待核实／约 1990 年代建成、2020 年照明改造”。

| # | 来源完整 URL | 页面标题 / 机构 | HTTP | 正文关键句 / 说明 |
| --- | --- | --- | --- | --- |
| 1 | `https://ww.iea-shc.org/Data/Sites/1/publications/CN-Peoples-Bank-of-China.pdf` | Human Centric Lighting in an office building — **IEA SHC（国际能源署太阳能供热制冷计划；Luo Tao / 中国建筑科学研究院）** | 200（1,842,842 字节，Python 取回） | 正文确认“Xining Central Sub-branch of the People's Bank of China”“vertical illuminance needs at the human eye position”；PDF 内容流压缩，`475 lx`／`UGR 8–19` 数值本轮**未能从压缩文本逐字复核**（沿用既有记录） |
| 2 | `http://www.heuvan.com/news_details.aspx?id=49` | 恒亦明科技…“中国人民银行西宁中心支行综合办公楼”三星级绿色照明标识挂牌及验收会 — **恒亦明（设备厂商）** | 200 | 报道示范工程验收挂牌，属设备厂商宣传，**未见**与 IEA 同组的照度/UGR 实测数值 |
| 3 | `https://xining.pbc.gov.cn/` | 中国人民银行青海省分行门户 | 200 | 机构门户可达，**无照度/UGR 实测数值** |

- **结论：保持（保留 `needs_verification=true`）。** 照度 `475 lx` 与 `UGR 8–19` 实测数值本轮仍**仅 IEA PDF（#1）单一来源**；设备厂商稿（#2）与机构门户（#3）均无同组可核数值。按保守原则**不升级**。面积（IEA≈1.8 万㎡／云知光“1 万平米”／恒亦明“1.75 万平米”）并列不写死。**建议**：取住建/科研机构或同行评议论文载同组实测数值者，方可移出该数值子项。

## 四、其余 89 条（本轮未取得成对独立权威源，保持 `needs_verification=true`）

> 以下条目本轮未针对性打开适用新 URL 或未取得成对的独立权威来源正文直接支撑；其待核实多为“实例的具体名称/设计者/年份(地点)”或“实测/性能参数”，按保守原则保持。核心/重要条目若要做具名实例，需要一个专门的“名作三要素＋双权威源”逐条核验批次（本轮预算集中在 6 个重点条目）。

| # | id | 层级/分层 | 主题 | 待核实要旨 | 结论 |
| --- | --- | --- | --- | --- | --- |
| 1 | `linear-perspective` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 2 | `scattered-perspective` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 3 | `composition` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 4 | `balance` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 5 | `proportion` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 6 | `color-theory` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 7 | `value` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 8 | `one-point-perspective` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 9 | `two-point-perspective` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 10 | `three-point-perspective` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 11 | `aerial-perspective` | 重要/L2 | 理论 | 实例的作者与年代待核实；空气透视早期实例跨度广，正文只作一般性说明。 | 保持 |
| 12 | `foreshortening` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 13 | `vanishing-point` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 14 | `horizon-line` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 15 | `rule-of-thirds` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 16 | `simplification` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 17 | `geometry-symmetry` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 18 | `visual-movement` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 19 | `leading-lines` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 20 | `figure-ground` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 21 | `negative-space` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 22 | `visual-center` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 23 | `contrast-principle` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 24 | `rhythm-repetition` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 25 | `hierarchy` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 26 | `hue` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 27 | `saturation` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 28 | `primary-colors` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 29 | `complementary-colors` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 30 | `color-contrast` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 31 | `warm-cool` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 32 | `curvilinear-perspective` | 补充/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 33 | `chiaroscuro` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 34 | `qi-yun` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 35 | `liubai` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 36 | `yijing` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 37 | `spatial-sequence` | 核心/L2 | 理论 | 空间序列一般理论待补充专门来源；以古根海姆连续坡道为连续序列实例。 | 保持 |
| 38 | `transition-space` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 39 | `interior-exterior-transition` | 核心/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 40 | `courtyard` | 核心/L2 | 理论 | 赵堂子胡同3号形成时期有清代与1930年代改建两说，待考订。 | 保持 |
| 41 | `borrowed-scenery` | 核心/L2 | 造景 | 借景北寺塔的园外距离记载不一（约 1.5–1.7 公里），具体数值待核实；正文并列、不写死。 | 保持 |
| 42 | `framed-scenery` | 核心/L2 | 造景 | 古典园林框景实例的具体设计者与年代待核实。 | 保持 |
| 43 | `opposed-scenery` | 核心/L2 | 造景 | 对景具体实例的设计者与年代待核实。 | 保持 |
| 44 | `screened-scenery` | 核心/L2 | 造景 | 苏州园林障景具体实例的设计者与年份待补充独立来源。 | 保持 |
| 45 | `pedestrian-flow` | 核心/L2 | 动线 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 46 | `sunken-plaza` | 核心/L2 | 下沉空间 | 顾如珍负责建筑工程为单源，待补充独立来源；其他实例的设计者与年代待核实。 | 保持 |
| 47 | `drainage` | 核心/L2 | 下沉空间 | 雨水排放工程参数待补充专业来源；建筑面积记载不一。 | 保持 |
| 48 | `natural-ventilation` | 核心/L2 | 材料 | 翠郊吴氏大院建造年代待核实；两处实测条件不同不可直接比较。 | 保持 |
| 49 | `material-texture` | 核心/L2 | 材料 | 材料质感与光反射、触感之间关系的机理待补专门来源；实例的设计者与年代待核实。 | 保持 |
| 50 | `gothic` | 核心/L2 | 风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 51 | `renaissance-style` | 核心/L2 | 风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 52 | `modernism` | 核心/L2 | 风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 53 | `postmodernism` | 核心/L2 | 风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 54 | `mannerism` | 重要/L2 | 风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 55 | `beaux-arts` | 重要/L2 | 风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 56 | `plein-air` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 57 | `chinese-architecture-style` | 核心/L2 | 风格 | 具体单体建筑工匠归属（蒯祥）仅单源，待补充独立来源。 | 保持 |
| 58 | `light-well` | 重要/L2 | 下沉空间 | 具体天井实例的采光与通风实测数据待补充独立来源（机制层面可参见自然通风条目）。 | 保持 |
| 59 | `leaked-scenery` | 重要/L2 | 造景 | 漏景具体实例的设计者与年代待核实。 | 保持 |
| 60 | `vernacular-material` | 重要/L2 | 材料 | 具体地区乡土材料的性能数据待补充独立来源。 | 保持 |
| 61 | `color-harmony` | 重要/L2 | 理论 | 面积比例与整体感等经验性表述待补充直接来源；实例的设计者与年份待核实。 | 保持 |
| 62 | `composition-placement` | 重要/L2 | 理论 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 63 | `axis` | 重要/L2 | 理论 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 64 | `stack-ventilation` | 重要/L2 | 材料 | 热压通风实例的通风实测数据待补充独立来源。 | 保持 |
| 65 | `thermal-comfort` | 重要/L2 | 理论 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 66 | `service-route` | 重要/L2 | 动线 | 实例的具体名称、地点、设计者与年份待补充独立来源。 | 保持 |
| 67 | `gestalt-organization-laws` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 68 | `color-psychology` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 69 | `environmental-psychology` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 70 | `hardscape-softscape` | 重要/L2 | 造景 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 71 | `wayfinding` | 重要/L2 | 动线 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 72 | `lighting-design` | 重要/L2 | 材料 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 73 | `place-attachment` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 74 | `daylight-factor` | 补充/L2 | 材料 | 具体实例的采光系数数值与设计者待补充独立来源。 | 保持 |
| 75 | `mixed-mode-ventilation` | 重要/L2 | 材料 | 混合通风实例的控制策略与能耗数据待补充独立来源。 | 保持 |
| 76 | `material-durability` | 重要/L2 | 材料 | 实例寿命与维护数据待补独立来源；具体退化机制的通用列表待补专门来源。 | 保持 |
| 77 | `transparent-material` | 重要/L2 | 材料 | 透明与半透明材料实例的性能参数待补充独立来源。 | 保持 |
| 78 | `functional-zoning` | 重要/L2 | 理论 | Architecture 与 Interior design 未直接给出“功能分区”术语定义；核心概念与实例数据均待补独立来源。 | 保持 |
| 79 | `gray-space` | 重要/L2 | 理论 | 檐下与廊道实例的设计者与年代待补独立来源。 | 保持 |
| 80 | `enclosure` | 重要/L2 | 理论 | 具体院落的设计者与年代待补独立来源。 | 保持 |
| 81 | `placemaking` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 82 | `space-syntax` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 83 | `pattern-language` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 84 | `form-follows-function` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 85 | `functionalism-architecture` | 重要/L2 | 风格 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 86 | `biophilic-design` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 87 | `defensible-space-theory` | 重要/L2 | 理论 | 实例的具体名称、设计者与年代待补充独立来源。 | 保持 |
| 88 | `perspective` | 核心/L2 | 理论 | 透视演示年代取学界通行约数（约 1413 年），原始文献年代存争议，正文不写死。 | 保持 |
| 89 | `sunken-courtyard` | 核心/L2 | 下沉空间 | 两类实例的历史原型对应关系与一般苏州庭院营造者归属待核实。 | 保持 |

## 五、本轮实际打开 / 请求的 URL（去重 22 个）

**HTTP 200 且正文可读/可用（15 个）：**

1. `https://ngsj.njtech.edu.cn/info/1064/1954.htm` — 200（南工大设计院·常州国展资产高新智汇中心）
2. `https://ylj.suzhou.gov.cn/szsylj/sjyc/201905/c1df393edc8745abb20e8a9bd5525782.shtml` — 200（苏州市园林局·拙政园）
3. `https://www.taiwan.cn/zt/jlzt/jstwz/jxjs/jxjs/200911/t20091111_1138694.htm` — 200（中国台湾网·苏州拙政园）
4. `http://mur.cn/journals/2002/2/MUR-2002-2-bec33483a84dbb51ab3121f2c4d9f4e6.html` — 200（现代城市研究·凝固的音乐（苏州园林艺术））
5. `https://search.napstic.cn/literature/periodical/010zhuangshi202309018` — 200（国家学术搜索·《装饰》曲径通幽入园模式）
6. `https://www.thepaper.cn/newsDetail_forward_24383367` — 200（澎湃新闻·造园如作诗文（陈从周书摘））
7. `https://lyylj.gz.gov.cn/zhzx/tpxw/content/post_9589101.html` — 200（广州市林业和园林局·小园香径独徘徊（曲径/小径））
8. `https://www.epfl.ch/campus/visitors/?p=198` — 200（EPFL·Access（Rolex Learning Center 无障碍/坡道））
9. `https://www.archdaily.com/53536/rolex-learning-center-sanaa` — 200（ArchDaily·Rolex Learning Center / SANAA）
10. `https://www.designboom.com/?p=9044/` — 200（designboom·SANAA Rolex Learning Center）
11. `https://www.archdaily.com/84524/ad-classics-villa-savoye-le-corbusier` — 200（ArchDaily·Villa Savoye / Le Corbusier）
12. `https://news.cctv.com/sports/aoyun/other/20070803/101299.shtml` — 200（央视网·奥运场馆疏散 8 分钟原则）
13. `http://www.heuvan.com/news_details.aspx?id=49` — 200（恒亦明·人行西宁中心支行绿色照明验收）
14. `https://xining.pbc.gov.cn/` — 200（中国人民银行青海省分行门户）
15. `https://ww.iea-shc.org/Data/Sites/1/publications/CN-Peoples-Bank-of-China.pdf` — 200（IEA SHC·Human Centric Lighting（PDF，200，1,842,842B））

**HTTP 200 但不可用（4 个）：** 微信公众号图文×2（`mp.weixin.qq.com/...` 验证码页）、`https://fg.suzhou.gov.cn/szfgw/szyl/jump_article.shtml`（200 空壳 750B）、`https://www.villa-savoye.fr/en/discover/an-architectural-promenade`（200，正文 JS 动态、静态不可机读）。

**失败 / 不可用（3 个）：** `https://fallingwater.org/38/fallingwater-facts`（403）、`https://fallingwater.org/what-is-fallingwater`（403）、`https://m.gujianchina.cn/quote/show-7653.html`（567 反爬）。另 IEA PDF 的 `iea-shc.org`/`projects.iea-shc.org` 主机在 curl 下报 schannel 吊销离线（000），改 Python 取回 200（计入上表第 15 项）。

> 另 `web_search` 工具单查询导航 8 次（常州国展绿色、人行西宁照度、拙政园、无障碍坡道、Villa Savoye、Rolex、曲径、疏散等），正文核验以 urllib/curl 实抓为准。

## 六、汇总

- **可升级（建议整条置 `needs_verification=false`；均须先登记来源入 `sources.json` 并注明概念贴合）：2 条**
  - `level-change`：候选实例 **劳力士学习中心（Rolex Learning Center，瑞士洛桑 EPFL 校园；SANAA 设计；2010 年）**，由 **EPFL 官方 Access 页（`https://www.epfl.ch/campus/visitors/?p=198`，200）＋ArchDaily（`https://www.archdaily.com/53536/rolex-learning-center-sanaa`，200）** 两独立权威源正文直接支撑三要素与“无障碍坡道/缓坡处理高差”概念（designboom 佐证）；正文须注明“以缓坡替代台阶处理高差、实现无障碍”。
  - `winding-path`：候选实例 **拙政园（江苏苏州；王献臣建园、相传文徵明参与设计蓝图；始建于 1509）**；实例三要素由 **苏州市园林局（`https://ylj.suzhou.gov.cn/.../c1df393e...shtml`，200）＋中国台湾网（`https://www.taiwan.cn/.../t20091111_1138694.htm`，200）** 两独立源支撑；“曲径通幽”手法由 **《现代城市研究》（`http://mur.cn/...MUR-2002-2...html`，200）＋《装饰》（`https://search.napstic.cn/literature/periodical/010zhuangshi202309018`，200）** 两篇学术专门文献（并澎湃 `https://www.thepaper.cn/newsDetail_forward_24383367`，200）正文支撑且直接以拙政园为例；正文须注明“文徵明参与设计”为相传。
- **可收窄（保留 `needs_verification=true`）：0 条**
- **保持待核实：93 条** ＝ 第四节 89 条 ＋ 本轮重点中保持的 4 条（`spatial-organization`、`evacuation-route`、`green-architecture`、`glare`）。
- **本轮实测 `needs_verification=true` 总数：95 条** ＝ 可升级 2 ＋ 可收窄 0 ＋ 保持 93。
- **打开 URL 数**：直连**去重 22 个**（HTTP 200 共 19：正文可读/可用 15、验证码/JS/空壳 4；失败 3：403×2、567×1；另 IEA PDF 备用主机 curl 000 但 Python 主域 200，已计入上述 22 个之内）；另 `web_search` 单查询导航 8 次。
- **数据更正/冲突提示（不写死）**：Rolex Learning Center 年份 2010（ArchDaily/designboom 一致）；拙政园“文徵明设计蓝图”各源均作“据传/相传”、设计者以园主王献臣表述；Villa Savoye 年份 1929（ArchDaily 记竣工年）与通行 1931（建成）并列，未采用；常州国展资产高新智汇中心奖项图文均微信、不可读；人行西宁中心支行面积 IEA≈1.8 万㎡／云知光“1 万平米”／恒亦明“1.75 万平米”并列；照度 475 lx／UGR 8–19 仅 IEA 单源。

> 保守原则声明：维基/百科镜像同源不计第二源；微信公众号图文全部被验证码拦截、不作可核验第二源；同机构文章计 1 源；`fallingwater.org` 本轮 403；`古建家园` 567 反爬；本报告仅给结论与证据，**未修改任何条目数据或其它文件**（本文件为唯一产出）。
