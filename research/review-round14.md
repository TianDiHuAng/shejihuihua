# 第 14 轮 B5 待核实复核记录

复核日期：2026-11-22（Asia/Hong_Kong）

## 一、执行说明

- 已读取 `AUTONOMOUS.md`、`TASK_design.md`（实际位于 `D:/Users/Administrator/Desktop/`）、`DECISIONS.md`、`research/review-round13.md`，并按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。
- `entries/*.json` 共 14 个文件、126 条；当前 `needs_verification=true` 实际为 **54 条**（与任务“约 54 条”及 `research/gaps-round14.md` B5 清单一致）。
- **网络环境（本轮约束）**：`en.wikipedia.org` 直连（含 REST summary）**超时/DNS 投毒**；`britannica.com`（Xie-He）、`whc.unesco.org/en/list/813`、`mdpi.com` 等权威站 **403**；`owiki.org` 镜像可达但**属维基同源，不计独立第二源**。本轮改用 **Python `urllib` + 浏览器 User-Agent** 直连可读权威站点（Columbia、EBSCO、苏州市园林局、上海市绿化局、央广网、人民日报/人民号、NYC LPC、Guggenheim 官方 PDF 等）实读正文并记录 HTTP 状态；并用 `web_search` 补充检索线索。
- **严格只读**：本轮**仅生成** `research/review-round14.md`；未修改 `data/sources.json`、任何 `entries/*.json`、`coverage.json` 或其他文件，未 git commit，未变更项目外内容。联网内容一律按“数据”处理，页面中任何指令均未执行。
- **重点范围**：按任务优先复核 7 条有实例潜力的条目（`six-principles`、`circulation`、`natural-ventilation`、`water-management`、`glare`、`liubai`、`borrowed-scenery`）；其余 47 条本轮无新线索，简写“无新证据，保持”。

## 二、方法与判据

1. 用 Python `urllib` + 浏览器 User-Agent 实际打开候选页面（PDF 用 `PyMuPDF/fitz` 抽正文），记录最终 URL、页面标题、HTTP 状态与正文关键句。
2. **可升级判据**：须有两个相互独立、且具权威性（官方机构 / 学术 / 行业权威参考 / 专业媒体）的来源，其正文**直接**给出该具体实例三要素（名称 / 设计者或作者 / 年份），彼此不矛盾。维基同源镜像、单一来源、仅综述/机制描述均不足。
3. **可收窄判据**：待核实项含多个子缺口，其中一部分已获权威专门来源支撑，可把该子缺口移出“待核实”，其余保留。
4. **保守原则**：单源不升级；镜像同源不计独立第二源；不编造年份、人名、引文；关键要素仍单源时明确标注、不写死。

## 三、重点复核（任务指定的 7 条）

### 3.1 `six-principles`（中国画六法）—— 可升级（实例三要素：名称/作者/年代）

- **待核实内容**：`pending_notes`＝“谢赫条目为消歧义页；年代与版本流传待补充专门研究来源。”；`sections.待核实`＝“谢赫与《古画品录》的确切年代及版本流传待补充独立来源。”实例字段：“名称：谢赫《古画品录》相关体系；地点：古代中国；设计者：不适用；年份：待核实。”（本件“设计者”对文本而言即**作者**位）
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://projects.mcah.columbia.edu/jaanus/node/1757` | rikuhō 六法 — JAANUS（哥伦比亚大学 MCAH 项目，**权威学术**） | 200 | “The Six Canons or Principles… They were set out in the **Southern Qi 南齊 period by Xie He (Jp: Sha Kaku 謝赫) in his Guhua pinlu (…古画品録, Record of the Classification of Painters), published c. 500.**” |
| `https://about.ebsco.com/es/node/158137`（原 `https://www.ebsco.com/es/node/158137`） | Xie He — EBSCO Research Starters（**独立学术参考数据库**） | 200 | “Xie He was a prominent painter and art critic during the **Southern Qi period of the Southern Dynasties, specifically from 479 to 502 CE**… His most notable contribution is the **‘Ku Hua Ping Lu,’ a record detailing the fundamentals of Chinese painting**…” |

- **结论：可升级（就实例三要素而言）。** 两个相互独立且具权威性的来源均直接给出同一实例的三要素：**名称＝《古画品录》（Guhua pinlu / Ku Hua Ping Lu，又名《画品》）**、**作者/“设计者”位＝谢赫（Xie He）**、**年代＝约公元 500 年 / 南朝齐（479–502 CE）**，二者一致、无矛盾。
  - 附带说明：`owiki.org/wiki/Xie_He` 本轮亦可达（HTTP 200），但属**维基同源镜像，不计第二源**，未作证据。
  - **范围界定（诚实声明）**：“版本流传（版本学）”子项本轮未取得专门的文献学研究来源，仍保留待补；本升级只落实到“名称/作者/年代”。
  - 建议主流程（本报告仅结论，不改数据）：将 `实例` 年份改为“约公元 500 年（南朝齐，479–502）”，名称/作者沿用；据上述两源在 `data/sources.json` 新增 verified=true 来源后，可从待核实中移除“年代”子项，`版本流传` 保留。

### 3.2 `circulation`（动线设计）—— 可升级（实例三要素：名称/设计者/年份 + 动线特征）

- **待核实内容**：`pending_notes`＝“所举公共文化建筑实例的具体信息待补充，暂不作确定性陈述。”；`sections.待核实`＝“实例的具体名称、地点与设计者待核实。”实例字段：“名称：公共文化建筑参观动线；地点/设计者/年份：待核实。”
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `http://s-media.nyc.gov/agencies/lpc/lp/1774.pdf` | LP-1774 The Solomon R. Guggenheim Museum, 1071 Fifth Avenue, Manhattan. Frank Lloyd Wright, Architect. Built 1956-59 — **纽约市地标保护委员会（LPC，官方政府）** | 200 | “THE SOLOMON R. GUGGENHEIM MUSEUM… **Frank Lloyd Wright, Architect. Built 1956-59**… its most prominent section taking on the form of a nautilus. The spiraling expanse…”;“rooms spin out in an **endless spiral**”;“**The spiral ramp**, described as ‘logarithmic’…” |
| `https://www.guggenheim.org/wp-content/uploads/2025/07/250715_VE_VisitorGuide_v02.pdf` | GUGGENHEIM NEW YORK Visitor Guide — **古根海姆博物馆官方** | 200 | “**The rotunda’s spiral ramp is a quarter mile long and climbs steadily at a three-degree incline**… Since it **opened to the public in 1959**, the rotunda has served as a catalyst…”；“commissioned **Frank Lloyd Wright** to design ‘a temple of spirit’…” |

- **结论：可升级。** 两个相互独立且权威（政府地标委员会 + 博物馆官方）的来源均直接给出：**名称＝所罗门·R·古根海姆美术馆（纽约）**、**设计者＝弗兰克·劳埃德·赖特（Frank Lloyd Wright）**、**年份＝1959 年开馆（1956–1959 建成）**，且均描述其**连续螺旋坡道（quarter-mile spiral ramp）环绕中庭**的参观动线——正是“公共文化建筑参观动线”的经典实例。

### 3.3 `natural-ventilation`（自然通风）—— 保持

- **待核实内容**：`pending_notes`＝“传统院落通风的实测数据与设计者信息待补充独立来源。”实例：“名称：传统院落自然通风；地点/年份：待核实；设计者：不适用。”
- **核对**：
  - `https://www.designingbuildings.co.uk/wiki/Natural_ventilation`（Natural ventilation of buildings，HTTP 200）仅提供**机制/原理**，不含传统院落实测数据。
  - 检索另获现代被动通风实例东阁中心（Eastgate Centre, Harare，Mick Pearce，1996）：`https://www.ipsnews.net/1996/06/architecture-zimbabwe-termites-inspire-new-office-complex/`（Inter Press Service，HTTP 200）与 `https://superscout.co/innovation/eastgate-centre-passive-cooling`（HTTP 200）均可证“1996 / Mick Pearce / 哈拉雷 / 白蚁丘启发的自然通风”。但该实例是**现代办公楼**，并非本条所指“**传统院落**”，且非“传统院落通风实测数据”，概念不匹配。
- **结论：无新证据，保持。**（传统院落多为无名工匠、无具名设计者与实测数据；现代实例不能替换本条实例概念。）

### 3.4 `water-management`（理水）—— 可升级（实例三要素：名称/设计者/年份 + 以水为主）

- **待核实内容**：`pending_notes`＝“苏州园林水面实例的设计者与年份待补充独立来源。”`sections.待核实`＝“具体水面实例的设计者与年份待核实。”实例：“名称：苏州古典园林水面；地点：中国苏州；设计者/年份：待核实。”
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://ylj.suzhou.gov.cn/szsylj/sjyc/201905/c1df393edc8745abb20e8a9bd5525782.shtml` | 拙政园 — **苏州市园林和绿化管理局（官方政府）** | 200 | “拙政园**始建于明正德四年（1509）**，为明代弘治进士、御史**王献臣**弃官回乡后……拓建而成……据传王献臣在建园之期，曾请吴门画派的代表人物**文徵明**为其设计蓝图，**形成以水为主**、疏朗平淡、近乎自然风景的园林。” |
| `https://www.peopleapp.com/rmharticle/30016473527` | 「苏州古典园林品鉴」拙政园：天下园林之母 — **人民日报·人民号（来源荔枝新闻）** | 200 | “明正德四年（公元**1509 年**）……**王献臣**仕途失意，归隐苏州后将其买下，聘著名画家、吴门画派的代表**文征明参与设计蓝图**，历时 16 年建成……其特点是**以水为主，水面广阔**……它以**池水为中心**……” |

- **结论：可升级。** 两个相互独立且权威（苏州市园林局 + 人民日报/人民号）的来源均直接支撑：**名称＝拙政园（水面/以水为主）**、**设计者＝王献臣（并聘文徵明参与设计蓝图）**、**年份＝1509 年（明正德四年）**，且均强调“以水为主、池水为中心”，正是“苏州园林理水”的核心实例。

### 3.5 `glare`（眩光）—— 保持

- **待核实内容**：`pending_notes`＝“办公实例的照度与眩光实测数据待补充独立来源。”实例：“名称：办公空间侧窗眩光控制；地点/设计者/年份：待核实。”
- **核对**：检索到 MDPI 论文《Subjective and Simulation-Based Analysis of Discomfort Glare Metrics in Office Buildings with Light Shelf Systems》（`https://www.mdpi.com/2071-1050/15/15/11885/htm`），但该站对 urllib 返回 **HTTP 403**（未能读正文）；且其性质为**参数化模拟/主观评价研究**，并非某一具体具名办公实例的“照度与眩光实测数据”，亦无设计者/年份。
- **结论：无新证据，保持。**（定义/机理来源已有；缺的是具体办公实例的实测数据与三要素，未获双源。）

### 3.6 `liubai`（留白）—— 可收窄（专门独立来源已双源落实；L1 无实例）

- **待核实内容**：`pending_notes`＝“仅见中国画综合条目对留白的讨论，待补充针对留白的独立来源。”（`liubai` 为 L1，`实例`/`待核实` 字段为空）
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://www.cnr.cn/ent/zx/20201228/t20201228_525375797.shtml`（跳转 `https://ent.cnr.cn/zx/20201228/t20201228_525375797.shtml`） | 留白，留的是什么？ — **央广网（gb18030 编码）** | 200 | 全篇专论“留白”，正文出现“留白”31 次；论及中国画“空白”的空间联想与虚实关系。 |
| `https://paper.people.com.cn/rmrb/pc/content/202611/01/content_30188752.html` | 在留白中邂逅万千气象 — **人民日报（副刊）** | 200 | “**留白，即对空白的利用，是传统中国画构图的一大特点**……在中国哲学里，黑与白、实与虚辩证存在……‘无画处皆成妙境’”；围绕广州艺术博物院“留白：从传统意境到当代表达”展展开（配 南宋佚名《云山图》）。 |

- **结论：可收窄。** “待补充针对留白的独立来源”这一子缺口已由**两篇独立的专门文章**（央广网、人民日报）支撑，可从待核实移除。因 `liubai` 为 **L1、无实例三要素**，不涉“实例三要素升级”；若要补具名实例（如南宋 马远《寒江独钓图》），需另取得可锁定作者/年代的权威来源，本轮两篇专文未给出该画作信息。

### 3.7 `borrowed-scenery`（借景）—— 可升级（实例三要素：名称/设计者/年份；借景细节单源附注）

- **待核实内容**：`pending_notes`＝“苏州园林借景具体实例的设计者与年份待补充独立来源。”`sections.待核实`＝“具体园林实例的设计者与年份待核实。”实例：“名称：苏州古典园林借景实例；地点：中国苏州；设计者/年份：待核实。”
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://lhsr.sh.gov.cn/jnylwh/20200824/7cc5e5102094470b94a8f771808c1f53.html` | 借景——拙政园的精妙所在 — **上海市绿化和市容管理局（官方政府）** | 200 | “《园冶》里讲‘借景，林园之最要者也’……**拙政园借景北寺塔的巍峨雄伟，园内水池中倒影着塔影**……这璀璨之塔，倒映池中……这是园外 1.5 公里处报恩寺内的**北寺塔**……有着近 500 年园龄的拙政园，当年造园借用此景……” |
| `https://ylj.suzhou.gov.cn/szsylj/sjyc/201905/c1df393edc8745abb20e8a9bd5525782.shtml` | 拙政园 — **苏州市园林和绿化管理局（官方政府）** | 200 | “拙政园**始建于明正德四年（1509）**……**王献臣**……**文徵明**为其设计蓝图……” |
| `https://www.peopleapp.com/rmharticle/30016473527` | 「苏州古典园林品鉴」拙政园：天下园林之母 — **人民日报·人民号** | 200 | “明正德四年（公元**1509 年**）……**王献臣**……聘……**文征明参与设计蓝图**……” |

- **结论：可升级。** 名称（拙政园）、**设计者＝王献臣（聘文徵明参与设计蓝图）**、**年份＝1509 年（明正德四年）** 三项由苏州市园林局 + 人民日报两独立权威来源直接双源支撑；借景实例“**拙政园借景（园外报恩寺）北寺塔**”的细节由上海市绿化局官方专文直接给出。
  - **保守标注**：“借景北寺塔”这一**细节**目前仅为上海市绿化局**单一权威政府来源**（另有园名/设计者/年份为双源）；建议主流程在写入时对该细节标注为“据上海市绿化和市容管理局”，或再补一独立来源，再视情写死。

## 四、其余 47 条（无新证据，保持）

以下条目本轮**未打开针对性 URL**（按任务“其余无新线索简写保持”处理），待核实项多为“实例具体名称/设计者/年份”或“实测/性能参数”，本轮未取得成对的独立权威来源直接支撑，按保守原则保持。`chinese-architecture-style` 仅余“蒯祥工匠归属单源”、`daylight-factor` 仅余“具体实例数值与设计者”等窄口子，本轮无新证据，一并保持。

| id | 待核实内容（简） | 结论 |
| --- | --- | --- |
| `linear-perspective` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `scattered-perspective` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `composition` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `balance` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `proportion` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `color-theory` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `value` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `one-point-perspective` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `two-point-perspective` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `three-point-perspective` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `aerial-perspective` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `foreshortening` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `vanishing-point` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `horizon-line` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `rule-of-thirds` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `figure-ground` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `negative-space` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `hue` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `complementary-colors` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `chiaroscuro` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `framed-scenery` | 仅见中国园林综合条目，待补充针对框景的独立来源 | 无新证据，保持 |
| `opposed-scenery` | 未直接支撑“对景”核心机制；实例设计者/年份待核实 | 无新证据，保持 |
| `screened-scenery` | 苏州园林障景具体实例的设计者与年份待补充独立来源 | 无新证据，保持 |
| `winding-path` | 仅见中国园林综合条目，待补充针对曲径的独立来源 | 无新证据，保持 |
| `gothic` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `renaissance-style` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `modernism` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `postmodernism` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `chinese-architecture-style` | 具体单体建筑工匠归属（蒯祥）仅单源，待补充独立来源 | 无新证据，保持 |
| `light-well` | 具体天井实例的采光与通风实测数据待补充独立来源 | 无新证据，保持 |
| `leaked-scenery` | 未出现“漏景/漏窗”字面术语；实例设计者/年份待核实 | 无新证据，保持 |
| `vernacular-material` | 具体地区乡土材料的性能数据待补充独立来源 | 无新证据，保持 |
| `color-harmony` | 面积比例等经验性表述待补直接来源；实例设计者/年份待核实 | 无新证据，保持 |
| `composition-placement` | 实例的具体名称、地点、设计者与年份待补充独立来源 | 无新证据，保持 |
| `axis` | 实例的具体名称、地点、设计者与年份待补充独立来源 | 无新证据，保持 |
| `stack-ventilation` | 热压通风实例的通风实测数据待补充独立来源 | 无新证据，保持 |
| `thermal-comfort` | 实例的具体名称、地点、设计者与年份待补充独立来源 | 无新证据，保持 |
| `service-route` | 实例的具体名称、地点、设计者与年份待补充独立来源 | 无新证据，保持 |
| `daylight-factor` | 具体实例的采光系数数值与设计者待补充独立来源 | 无新证据，保持 |
| `mixed-mode-ventilation` | 混合通风实例的控制策略与能耗数据待补充独立来源 | 无新证据，保持 |
| `material-durability` | 实例寿命与维护数据、退化机制通用列表待补充独立来源 | 无新证据，保持 |
| `transparent-material` | 透明与半透明材料实例的性能参数待补充独立来源 | 无新证据，保持 |
| `functional-zoning` | “功能分区”术语定义与实例数据均待补独立来源 | 无新证据，保持 |
| `gray-space` | 檐下与廊道实例的设计者与年代待补独立来源 | 无新证据，保持 |
| `enclosure` | 具体院落的设计者与年代待补独立来源 | 无新证据，保持 |
| `perspective` | 佛罗伦萨透视试验确切年份与设计者对应关系待补第二独立来源 | 无新证据，保持 |
| `sunken-courtyard` | 中庭院与下沉广场的具体设计者、年份待核实 | 无新证据，保持 |

## 五、本轮实际打开/请求的 URL 清单（去重 17 个，urllib 直连）

| # | URL | 标题 / 机构 | HTTP | 用途 |
| --- | --- | --- | --- | --- |
| 1 | `https://projects.mcah.columbia.edu/jaanus/node/1757` | rikuhō 六法 — JAANUS（哥伦比亚大学） | 200 | `six-principles` 主证（谢赫/古画品录/约500年/南朝齐） |
| 2 | `https://about.ebsco.com/es/node/158137` | Xie He — EBSCO Research Starters | 200 | `six-principles` 第二独立源（南朝齐 479–502、Ku Hua Ping Lu） |
| 3 | `https://owiki.org/wiki/Xie_He` | Xie He — Open WIKI（维基同源镜像，**不计第二源**） | 200 | `six-principles` 查阅（镜像，未作证据） |
| 4 | `https://www.designingbuildings.co.uk/wiki/Natural_ventilation` | Natural ventilation of buildings — Designing Buildings | 200 | `natural-ventilation` 机制参考（无传统院落实测数据） |
| 5 | `https://www.ipsnews.net/1996/06/architecture-zimbabwe-termites-inspire-new-office-complex/` | Termites Inspire New Office Complex — Inter Press Service | 200 | 现代实例 Eastgate（概念不匹配，未采用） |
| 6 | `https://superscout.co/innovation/eastgate-centre-passive-cooling` | Eastgate Centre passive cooling — Superscout | 200 | 同上（1996/Mick Pearce，未采用） |
| 7 | `https://ylj.suzhou.gov.cn/szsylj/sjyc/201905/c1df393edc8745abb20e8a9bd5525782.shtml` | 拙政园 — 苏州市园林和绿化管理局 | 200 | `water-management`/`borrowed-scenery` 主证（王献臣/文徵明/1509/以水为主） |
| 8 | `https://www.peopleapp.com/rmharticle/30016473527` | 拙政园：天下园林之母 — 人民日报·人民号 | 200 | `water-management` 第二独立源（王献臣/文征明/1509/以水为主） |
| 9 | `https://lhsr.sh.gov.cn/jnylwh/20200824/7cc5e5102094470b94a8f771808c1f53.html` | 借景——拙政园的精妙所在 — 上海市绿化和市容管理局 | 200 | `borrowed-scenery` 借景北寺塔细节（政府专文） |
| 10 | `https://www.cnr.cn/ent/zx/20201228/t20201228_525375797.shtml` | 留白，留的是什么？ — 央广网 | 200 | `liubai` 专门来源一（gb18030） |
| 11 | `https://paper.people.com.cn/rmrb/pc/content/202611/01/content_30188752.html` | 在留白中邂逅万千气象 — 人民日报 | 200 | `liubai` 专门来源二 |
| 12 | `http://s-media.nyc.gov/agencies/lpc/lp/1774.pdf` | LP-1774 Solomon R. Guggenheim Museum（Frank Lloyd Wright, Built 1956-59）— 纽约市地标保护委员会 | 200 | `circulation` 主证（名称/Wright/1959/螺旋坡道） |
| 13 | `https://www.guggenheim.org/wp-content/uploads/2025/07/250715_VE_VisitorGuide_v02.pdf` | GUGGENHEIM NEW YORK Visitor Guide — 古根海姆官方 | 200 | `circulation` 第二独立源（spiral ramp/1959/Wright） |
| 14 | `https://www.mdpi.com/2071-1050/15/15/11885/htm` | Discomfort Glare Metrics in Office Buildings — MDPI | 403 | `glare`（未能读正文；参数化研究，非实例实测） |
| 15 | `https://en.wikipedia.org/api/rest_v1/page/summary/Xie_He` | Wikipedia REST summary | 超时 | `six-principles` 直连失败（DNS 投毒） |
| 16 | `https://www.britannica.com/biography/Xie-He` | Xie He — Britannica | 403 | `six-principles` 阻塞 |
| 17 | `https://whc.unesco.org/en/list/813` | Classical Gardens of Suzhou — UNESCO | 403 | `water-management`/`borrowed-scenery` 阻塞 |

> 另经 `web_search` 做多轮检索以定位上述权威页（含 Columbia/EBSCO/LPC/Guggenheim/苏州/上海政府/央广/人民日报等）。

## 六、汇总

- **可升级：4 条 —— `six-principles`、`circulation`、`water-management`、`borrowed-scenery`**
  - `six-principles`：Columbia JAANUS + EBSCO 两独立权威源均证 **《古画品录》/ 谢赫 / 约公元 500 年·南朝齐（479–502）**（“版本流传”仍待补）。
  - `circulation`：纽约市 LPC + 古根海姆官方两独立权威源均证 **所罗门·R·古根海姆美术馆（纽约）/ 弗兰克·劳埃德·赖特 / 1959 年 / 连续螺旋坡道动线**。
  - `water-management`：苏州市园林局 + 人民日报两独立权威源均证 **拙政园水面 / 王献臣（文徵明参与设计）/ 1509 年 / 以水为主·池水为中心**。
  - `borrowed-scenery`：苏州市园林局 + 人民日报双源证 **拙政园 / 王献臣（文徵明参与设计）/ 1509 年**；**借景北寺塔**细节由上海市绿化局官方专文（单源，已标注）。
- **可收窄：1 条 —— `liubai`**（“针对留白的独立专门来源”已由央广网、人民日报两篇专文落实，可移出待核实；`liubai` 为 L1 无实例，不涉实例三要素升级）。
- **保持待核实：49 条**（54 − 4 − 1；含 `natural-ventilation`、`glare` 及其余 47 条，本轮无新证据）。
- **打开 URL 数**：本轮经 `urllib` 直连**去重 17 个不同 URL**（其中 13 个返回 HTTP 200 正文并用作证据/查阅，2 个 403、1 个超时、1 个镜像不计源），另以 `web_search` 多轮检索补充来源。

> 保守原则声明：未核验线索不作升级依据；不为凑数硬写年份或人名；维基同源镜像（`owiki.org`）不计独立第二源；`six-principles`、`circulation`、`water-management`、`borrowed-scenery` 仅在“实例三要素（名称/设计者或作者/年份）”层面升级，仍属单源或文献学的子项（如“版本流传”“借景北寺塔细节”）已明确标注、不写死。
