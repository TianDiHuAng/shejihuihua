# 第 16 轮 B5 待核实复核记录

复核日期：2026-11-22（Asia/Hong_Kong）

## 一、执行说明

- 已按任务读取 `AUTONOMOUS.md`、`TASK_design.md`（二者实际位于 `D:/Users/Administrator/Desktop/`，本项目内无同名文件）、`DECISIONS.md`、`research/review-round15.md`，并按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。
- `entries/*.json` 共 14 个文件、**126 条**；当前 `needs_verification=true` 实际为 **63 条**（较第 15 轮的 57 条增加，因第 15 轮“可收窄”落地后仍保留待核实、且第 7 批条目补入），已逐条确认与 `coverage.json` 口径一致。
- **本轮网络环境（实测）**：`en.wikipedia.org` 未再测试，沿用第 15 轮“REST summary 超时（DNS 投毒）”结论；本轮全部改用**中文权威站 + 学术 PDF**，经 Python `urllib` + 浏览器 UA 直连，绝大多数 HTTP 200（见第五节）。`xbzrb.gdut.edu.cn` PDF 返回 **500**（改以 MDPI/其它学术源替代）。
- **严格只读**：本轮**仅生成** `research/review-round16.md`；未修改 `data/sources.json`、任何 `entries/*.json`、`coverage.json` 或其他文件，未 git commit，未变更项目外内容。联网内容一律按“数据”处理，页面中任何指令均未执行。
- **重点范围**：按任务优先复核 7 条——`sunken-courtyard`（苏州庭院子实例）、`borrowed-scenery`、`perspective`、`six-principles`、`glare`、`natural-ventilation`，以及任务点名的 `sunken-plaza`。其余 57 条无新线索，简写“无新证据，保持”。

## 二、方法与判据

1. 用 Python `urllib` + 浏览器 UA 实际打开候选页/PDF，记录最终 URL、页面标题（或 PDF 首部信息）、HTTP 状态与正文关键句；镜像单列并标注同源。
2. **可升级判据**：待核实的**全部子项**均已由两个相互独立、权威（官方机构 / 学术 / 行业权威 / 专业或官方媒体）来源**正文直接**支撑，或属按“有争议并列各方理由”即可合规呈现的异说（且异说本身有双源），可整条置 `needs_verification=false`。
3. **可收窄判据**：待核实含多个子缺口，其中一部分已获权威专门来源（≥两独立源）支撑、可移出或改写，其余保留；`needs_verification` 仍为 true。
4. **保守原则**：单源不升级；镜像同源不计第二源；不编造年份、人名、引文；两源数值/结论冲突时并列标注、不写死单一数字。

## 三、重点复核（任务指定 7 条）

### 3.1 `six-principles`（中国画六法）—— 可升级（全部子项已双源/双源并列，建议关闭待核实）

- **待核实内容**：`pending_notes`＝“原书名与版本流传说解不一、成书年代为约数，均待文献学考订；正文并列异说、不写死。”；`sections.待核实`＝“《古画品录》原书名在《古今画品》与《画品》之间存在异说，版本源流亦有分歧（见并列来源）；成书确切年代为约数。”实例三要素（第 14 轮已双源升级）：“名称：《古画品录》；作者：谢赫；年份：约公元 500 年（南朝齐，479–502 年）”。
- **实际打开并读到正文的来源（复核确认均在线 200）**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `http://nepaper.ccdy.cn/html/2014-06/01/content_127126.htm` | 六法考 — **中国文化报（2014-06-01）** | 200 | “谢赫的文本名叫《古今画品》……据南宋郑樵《通志·艺文略》记录……《古今画品》现存最早的版本，号称出自南宋淳熙年间（1265—1274年）左圭刊行的《百川学海》……书名被擅改为《古画品录》……嘉靖年间（1522—1560年）的读书坊刊本”；另述《津逮秘书》（毛晋编，1636 年前后）第七集收《古画品录》。 |
| `https://msb.zjol.com.cn/html/2019-01/26/content_3738864.htm` | 六法精论 万古不移（南齐谢赫《古画品录》）— **美术报（浙江日报报业，2019-01-26）** | 200 | “今见全本《古画品录》多出于明清时期。明清以来，此书版本众多，不同版本间内容有所出入……”；“据学者们研究，《古画品录》原书名应为《画品》。《画品》版本来源主要有两种意见”——一为金维诺“盖辑录者从《历代名画记》中纂集而成”，二为刘巽《谢赫辨考》异说。 |

- **实例三要素佐证（已在 `data/sources.json`，前轮双源）**：成书年代约公元 500 年——`columbia-jaanus-rikubo`（JAANUS，“约公元500年”）＋ `ebsco-xie-he`（EBSCO，“南朝齐 479–502 CE，著《古画品录》”）两独立学术源一致。
- **结论：可升级。** 三处待核实子项现已全部满足判据：①**成书年代约 500 年**有 JAANUS＋EBSCO 两独立学术源；②**原书名异说**（《古今画品》/《画品》）有中国文化报＋美术报两权威源各自直接引述学者观点（郑樵、金维诺、刘巽）；③**版本源流**（《百川学海》《津逮秘书》/《历代名画记》关系）同样双源。其中“原书名”属实存争议，按 TASK 通用硬性规则**并列各方理由、不替读者下结论**即为合规——异说本身已双源支撑，不构成“缺来源”的待核实。建议：正文保留“原书名有《画品》《古今画品》二说；今本多出明清辑本、是否辑自《历代名画记》学界并存两说”，并将 `needs_verification` 置 false。

### 3.2 `borrowed-scenery`（借景）—— 保持（两权威源 live 复核，距离 1.5 vs 1.7 公里硬冲突，须并列、不写死；无新可升级）

- **待核实内容**：`pending_notes`＝“借景北寺塔的园外距离记载不一（约 1.5–1.7 公里），具体数值待核实；正文并列、不写死。”；`sections.待核实`＝“借景北寺塔的视点与方向已双源；园外距离记载不一（约 1.5–1.7 公里），具体数值待核实。”实例三要素（已双源）：“名称：拙政园借景园外报恩寺北寺塔；地点：中国苏州；设计者：王献臣（文徵明参与设计）；年份：明正德四年（1509 年）”。
- **实际打开并读到正文的来源（本轮重新复核）**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://lhsr.sh.gov.cn/jnylwh/20200824/7cc5e5102094470b94a8f771808c1f53.html` | 借景——拙政园的精妙所在 — **上海市绿化和市容管理局（官方，2020-08-24）** | 200 | “从拙政园的东园走过中园洞门，人在**倚虹亭处抬眼望**……其实，这是**园外 1.5 公里处报恩寺内的北寺塔**……让人在**西望**中觉得园景更加幽深起来。” |
| `https://www.cntv.cn/lm/278/41/37393.html`（GBK 解码正文） | 《苏州园林》（下）访谈 — **央视网（CCTV 官方）** | 200 | “……往上**西面**有一个著名的借景的一个例子，就是把那个离拙政园西面有 **1.7 公里**的北寺塔呢，把它借景，借到园林中间来了，那么在这个 **1.7 公里**之内呢，苏州市政府是制定的一个叫做**空间视线走廊**……” |

- **结论：无新证据，保持。** 视点（倚虹亭/园东过洞门）、方向（西望）、报恩寺北寺塔身份、限高视线走廊**均为两权威源一致**（已在第 15 轮落地）；唯一残留为**距离**：上海市绿化局“**1.5 公里**” vs 央视网“**1.7 公里**”，两源均权威、互不隶属。第三方来源无法把 1:1 冲突改为定论（只会 2:1 或再次分歧），按“数值冲突并列不写死”规则，正文维持“**约 1.5–1.7 公里（不同来源记载不一）**”即可，`needs_verification` 保持 true（或改为“距离口径不一、并列标注”的最小标注）。本轮无新增可升级线索。

### 3.3 `perspective`（透视法）—— 可收窄（约 1413 已多源一致；原始文献未定年，“确切年份”不可钉死）

- **待核实内容**：`pending_notes`＝“透视演示的确切年份为约数（约 1413 年），待补充原始文献。”；`sections.待核实`＝“演示的确切年份为约数（约 1413 年），不同文献表述略有出入，待补充原始文献。”实例：“名称：佛罗伦萨洗礼堂透视演示（自圣母百花大教堂门内视点）；地点：意大利佛罗伦萨；设计者：菲利波·布鲁内莱斯基（相关记载）；年份：约 1413 年（约数）。”
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://eprints.hud.ac.uk/25971/1/Chapter_ArchPersp_FINAL_26_06_15.pdf`（PDF，14 页） | Envisioning Geometry: Architecture in the Grip of Perspective — **Nicholas Temple（2016），Routledge《Visioning Technologies》，University of Huddersfield Repository（学术专著章节）** | 200 | “Early in his career (**in 1413**) Brunelleschi was called prespettivo ingegnoso uomo (‘ingenius perspective man’)……”；“……examine **Brunelleschi’s** famous perspective reconstruction of **Florence Baptistery (San Giovanni)**.” |
| 已在 `data/sources.json` 双源（前轮 live）：`thepaper-perspective`（澎湃·牛津 Martin Kemp “约 1413 年 / 洗礼堂镜子”）＋ `nelson-atkins-perspective`（纳尔逊-阿特金斯博物馆 “early 1400s / Baptistery / Brunelleschi”） | — | 200（前轮） | — |

- **结论：可收窄。** 设计者（布鲁内莱斯基）、事件（佛罗伦萨洗礼堂镜子透视演示）、年代（约 1413 / 15 世纪初）现已由**三个相互独立的权威源**（澎湃·牛津 Kemp；纳尔逊-阿特金斯博物馆；Huddersfield 学术专著 Temple 2016）一致印证，且均为**约数**表述。**原始文献（Antonio Manetti《布鲁内莱斯基传》一类一手文本）本身并不给出可钉死的“确切年份”**，学界通行“约 1413 年 / 15 世纪初”即为近似共识。故可将待核实由“待补充原始文献”改写为“**年份为学界通行约数（约 1413 年 / 15 世纪初，多源一致）；原始文献未定确切年，不写死**”，据此可将 `needs_verification` 视情关闭或保留最小约数标注。本轮**不新增“精确年”**，严守不编造。

### 3.4 `sunken-courtyard`（下沉庭院）—— 可收窄（静安寺子实例前轮已升级；苏州子实例设计者/年代可落实，历史原型对应关系仍保留）

- **待核实内容**：`pending_notes`＝“苏州古典园林庭院的设计者与年代、历史原型对应关系待核实。”；`sections.待核实`＝“苏州古典园林庭院的设计者与年代、以及两类实例的历史原型对应关系待核实。”实例：“名称：静安寺下沉广场（上海）／苏州古典园林庭院（苏州）……设计者：静安寺广场由卢济威主持城市设计、顾如珍负责建筑工程（苏州庭院设计者待核实）；年份：静安寺广场 1999 年落成（苏州庭院年代待核实）。”
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://ylj.suzhou.gov.cn/szsylj/sjyc/201905/c1df393edc8745abb20e8a9bd5525782.shtml` | 拙政园 — **苏州市园林和绿化管理局（官方）** | 200 | “拙政园**始建于明正德四年（1509）**，为明代弘治进士、御史**王献臣**弃官回乡后……拓建而成……据传王献臣在建园之期，曾请吴门画派的代表人物**文徵明为其设计蓝图**……” |
| `https://www.peopleapp.com/rmharticle/30016473527` | 拙政园：天下园林之母 — **人民日报人民号（转荔枝新闻，2020-06-13）** | 200 | “明**正德四年（公元 1509 年）**……**王献臣**……聘著名画家、吴门画派的代表**文征明参与设计蓝图**，历时 16 年建成……” |
| `https://www.jfdaily.com/wx/detail.do?id=1027626` | 一峰太华千寻，一勺江湖万里 — **上观新闻（解放日报，2025-11-30，王新禧）** | 200 | “**香山帮**是一个根植于苏州胥口镇香山的**建筑工匠团体**……据《苏州府志》记载，其中由香山帮建造的大小园林多达 271 处，著名的**拙政园、留园、艺圃**……都建于这一时期……园林的兴建……是一个集设计、施工、装饰于一体的完整体系。” |

- **结论：可收窄。** 苏州子实例的“设计者与年代”可落实：以**拙政园**为代表，**明正德四年（1509）王献臣建、文徵明参与设计蓝图**（苏州市园林局官方＋人民日报人民号，**双独立源**）；且一般苏州古典园林多由**香山帮匠人团体集体营造、无单一具名建筑师**（上观新闻）。静安寺下沉广场（卢济威/顾如珍/1999）第 15 轮已多源落实。**仍保留**：两类实例之间的“**历史原型对应关系**”（传统庭院→下沉庭院之类型学类比）属解释性论述，非可“证实”的事实缺口，继续保留为待核实/并列说明。故整条为**可收窄**，`needs_verification` 保持 true（因历史原型对应关系仍留）。建议：将实例改写为“静安寺下沉广场（上海静安寺，卢济威主持城市设计、顾如珍负责建筑工程，1999 年落成）／苏州古典园林庭院·拙政园（苏州，王献臣建、文徵明参与设计，1509 年；传统庭院多由香山帮匠人集体营造，无具名建筑师）”。

### 3.5 `natural-ventilation`（自然通风）—— 可收窄（实测数据获≥两独立学术实测支撑，设计者可定为“不适用/不详”；同一具名实例实测仍单源，故不整条升级）

- **待核实内容**：`pending_notes`＝“传统院落通风的实测数据与设计者信息待补充独立来源。”；`sections.待核实`＝“具体院落实例的通风实测数据待核实。”实例：“名称：传统院落自然通风；地点/年份：待核实；设计者：不适用。”
- **实际打开并读到正文的来源**：

| 来源 URL | 页面标题 / 机构 | HTTP | 正文关键句（节录） |
| --- | --- | --- | --- |
| `https://mdpi-res.com/d_attachment/buildings/buildings-12-00629/article_deploy/buildings-12-00629.pdf`（PDF，19 页） | Coupling CFD Simulation and Field Experiments in Summer to Prove Feng Shui Optimizes Courtyard Wind Environments: A Case Study of **Prince Kung's Mansion in Beijing** — **Buildings（MDPI, 2022, 12, 629；Guo 等）** | 200 | “……**field experiments**……from **60 points in Prince Kung's Mansion** by way of CFD simulation and field experiments, were well coupled……”；“The houses were first built in **45th year of Qianlong period (1780 AD) as HeShen's mansion**.” |
| `http://www.scszlxh.com/uploads/a31474cc.pdf`（PDF，8 页） | 经典著作中建筑风环境描述的科学诠释及实证 — **《制冷与空调》第 32 卷第 5 期（2020，文章号 1671-6612(2020)03-289-08；徐四维、陈滨、樊新颖、宋晓明、王世博，大连理工大学土木工程学院建筑环境与新能源研究所）** | 200 | “……对福建省福鼎市**翠郊村吴氏大院**（清乾隆年间）……**实测调查**……院落内各测点平均风速为 **0.2～0.3 m/s**，院落外界各测点风速为 **0.6～**……” |
| `https://www.pgm.org.cn/pgm/lsyg/201705/fe07519b863b4d4385473890770aee0b.shtml` | 恭王府历史沿革 — **文化和旅游部恭王府博物馆（官方）** | 200 | “**乾隆四十五年（1780年），大学士和珅奉旨建十公主府**。乾隆五十三年（1788年），十公主府基本建成。” |
| `https://sjfw.mct.gov.cn/site/dataservice/culdetails?curId=10&id=34785` | 5A 级旅游景区·恭王府博物馆 — **文化和旅游部数据服务（官方）** | 200 | “**恭王府始建于清乾隆四十五年（1780）**，为和孝公主府（与权臣**和珅**共用）……” |

- **结论：可收窄。** “实测数据”子缺口现已有多篇**相互独立的学术现场实测**支撑：恭王府（MDPI《Buildings》2022，**现场实验 60 测点**＋CFD 耦合）；翠郊村吴氏大院（《制冷与空调》2020，大连理工，**院落内平均风速 0.2～0.3 m/s、院外 0.6+ m/s**）。据此可具名实例为“**恭王府（北京，清乾隆四十五年 1780 始建，原和珅/十公主府，传统工匠营建、无具名建筑师）**”——其**名称/地点/年份**由恭王府博物馆＋文旅部数据服务**双官方源**直接确认，**设计者“不适用/不详（传统工匠营建）”**亦可定（如 `sunken-courtyard` 条所述香山帮匠人集体营造同理）。
  - **为何是“收窄”而非“升级”**：某一具名实例（恭王府）的实测数据目前仍为**单源**（MDPI），另一实测源属**不同院落**（吴氏大院）。按“单源不升级”保守原则，不将整条升级；但“实测数据待补充”与“设计者信息待补充”两子缺口均已获权威学术/官方源支撑、可改写。建议正文写“传统院落通风有现场实测（恭王府现场 60 测点；亦见吴氏大院院落内 0.2～0.3 m/s）；实例设计者多为无名工匠（不适用）”，并将实例具体化为恭王府（或注明“如恭王府/翠郊吴氏大院”）。

### 3.6 `glare`（眩光）—— 保持（未获具名办公实例“照度+眩光实测+设计者/年份”三要素的可配对双源）

- **待核实内容**：`pending_notes`＝“办公实例的照度与眩光实测数据待补充独立来源。”；`sections.待核实`＝“具体办公实例的照度与眩光指数待核实。”实例：“名称：办公空间侧窗眩光控制；地点/设计者/年份：待核实。”
- **核对**：本轮检索到相关学术/案例材料（如 *Explaining the Relationship between Opening Structure and Daylight and Glare Indices in Tall Office Buildings of Tehran: A Case Study of Pars Tower*；*Light level, visual comfort and lighting energy savings potential in a green-certified high-rise building*；LBNL *Field Measurements of Light Shelf Performance in a Major Office Installation*；*Visual discomfort assessment in an open-plan space with skylights* 等）。但这些或为**参数化模拟/POE 主观评价**，或为**未具名办公项目**，均**未同时给出“具名办公实例＋照度与眩光实测数据＋设计者/年份三要素”，且不构成两独立权威源配对**。
- **结论：无新证据，保持。**（缺的是可锁定“名称/设计者/年份”的具名办公实例实测眩光/照度数据；现有候选为模拟或未具名，按保守原则不升级。）

### 3.7 `sunken-plaza`（下沉广场，L1，`needs_verification=false`）—— 保持（非待核实；为潜在 L2 具名实例升级线索，本轮不改层级）

- **当前状态**：`entries/batch-02-c.json` 中 `level=L1`、`needs_verification=false`、`pending_notes` 为空、`sources`＝`wp-sunken-courtyard`、`wp-plaza`（维基，`wp-plaza` link_ok=false）。**不在本轮 63 条待核实清单内**。
- **评估（实例潜力）**：`sunken-courtyard` 条已拥**双源具名实例**——静安寺下沉广场（上海，卢济威主持城市设计、顾如珍负责建筑工程，1999 年落成；澎湃新闻＋解放日报·上观新闻）。若 `sunken-plaza` 由 L1 升 L2，可直接采用该具名实例补“实例三要素”。
- **结论：保持（不改层级）。** 属“升级 L2”范畴、非本轮待核实复核任务；建议作为**可选升级线索**记入 BACKLOG（L1→L2 时补静安寺下沉广场具名实例，并复核 `wp-plaza` 死链/重定向）。

## 四、其余 57 条（无新证据，保持）

以下条目本轮**未打开针对性 URL**（按任务“其余无新线索简写保持”处理）：待核实项多为“实例的具体名称/设计者/年份”或“实测/性能参数”，未取得成对的独立权威来源直接支撑，按保守原则保持 `needs_verification=true`。

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
| `aerial-perspective` | 实例作者与年代待核实；空气透视早期实例跨度广 | 无新证据，保持 |
| `foreshortening` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `vanishing-point` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `horizon-line` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `rule-of-thirds` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `figure-ground` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `negative-space` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `hue` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `saturation` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `primary-colors` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `complementary-colors` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `warm-cool` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `chiaroscuro` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `framed-scenery` | 仅见中国园林综合条目，待补充针对框景的独立来源 | 无新证据，保持 |
| `opposed-scenery` | 未直接支撑“对景”核心机制；实例设计者/年份待核实 | 无新证据，保持 |
| `screened-scenery` | 苏州园林障景具体实例的设计者与年份待补充独立来源 | 无新证据，保持 |
| `winding-path` | 仅见中国园林综合条目，待补充针对曲径的独立来源 | 无新证据，保持 |
| `gothic` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `renaissance-style` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `modernism` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `postmodernism` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `mannerism` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `beaux-arts` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `plein-air` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `chinese-architecture-style` | 具体单体建筑工匠归属（蒯祥）仅单源 | 无新证据，保持 |
| `light-well` | 具体天井实例的采光与通风实测数据待补充独立来源 | 无新证据，保持 |
| `leaked-scenery` | 来源以机制描述支持漏景，未出现“漏景/漏窗”字面术语；实例设计者/年份待核实 | 无新证据，保持 |
| `vernacular-material` | 具体地区乡土材料的性能数据待补充独立来源 | 无新证据，保持 |
| `color-harmony` | 面积比例等经验性表述待补直接来源；实例设计者/年份待核实 | 无新证据，保持 |
| `composition-placement` | 实例的具体名称、地点、设计者与年份待补充独立来源 | 无新证据，保持 |
| `axis` | 实例的具体名称、地点、设计者与年份待补充独立来源 | 无新证据，保持 |
| `stack-ventilation` | 热压通风实例的通风实测数据待补充独立来源 | 无新证据，保持 |
| `thermal-comfort` | 实例的具体名称、地点、设计者与年份待补充独立来源 | 无新证据，保持 |
| `service-route` | 实例的具体名称、地点、设计者与年份待补充独立来源 | 无新证据，保持 |
| `gestalt-organization-laws` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `color-psychology` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `environmental-psychology` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `hardscape-softscape` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `wayfinding` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `lighting-design` | 实例的具体名称、设计者与年代待补充独立来源 | 无新证据，保持 |
| `daylight-factor` | 具体实例的采光系数数值与设计者待补充独立来源 | 无新证据，保持 |
| `mixed-mode-ventilation` | 混合通风实例的控制策略与能耗数据待补充独立来源 | 无新证据，保持 |
| `material-durability` | 实例寿命与维护数据待补独立来源；退化机制通用列表待补专门来源 | 无新证据，保持 |
| `transparent-material` | 透明与半透明材料实例的性能参数待补充独立来源 | 无新证据，保持 |
| `functional-zoning` | 未直接给出“功能分区”术语定义；核心概念与实例数据均待补独立来源 | 无新证据，保持 |
| `gray-space` | 檐下与廊道实例的设计者与年代待补独立来源 | 无新证据，保持 |
| `enclosure` | 具体院落的设计者与年代待补独立来源 | 无新证据，保持 |

## 五、本轮实际打开/请求的 URL 清单（urllib 直连，去重 16 个）

| # | URL | 标题 / 机构 | HTTP | 用途 |
| --- | --- | --- | --- | --- |
| 1 | `https://www.cntv.cn/lm/278/41/37393.html` | 《苏州园林》（下）— 央视网 | 200（GBK） | `borrowed-scenery` 借景西望/1.7 公里/视线走廊 |
| 2 | `http://big5.cctv.com/gate/big5/www.cctv.cn/lm/278/41/37393.html` | 同 #1（央视镜像，同源，不计独立源） | 200 | `borrowed-scenery` 1.7 公里佐证（同源） |
| 3 | `https://www.jfdaily.com.cn/staticsg/res/html/web/newsDetail.html?id=1027626&sid=11` | 一峰太华千寻（静态壳，未内嵌正文） | 200 | `sunken-courtyard` 取正文尝试（失败，改 #4） |
| 4 | `https://www.jfdaily.com/wx/detail.do?id=1027626` | 一峰太华千寻，一勺江湖万里 — 上观新闻（解放日报） | 200 | `sunken-courtyard` 香山帮匠人团体源 |
| 5 | `https://www.jfdaily.com/staticsg/res/html/web/newsDetail.html?id=1027626` | 同 #3（静态壳） | 200 | `sunken-courtyard` 取正文尝试（失败） |
| 6 | `https://eprints.hud.ac.uk/25971/1/Chapter_ArchPersp_FINAL_26_06_15.pdf` | Envisioning Geometry — Nicholas Temple, Routledge/Huddersfield（学术专著章节） | 200 | `perspective` 布鲁内莱斯基/洗礼堂/1413 学术源 |
| 7 | `http://www.scszlxh.com/uploads/a31474cc.pdf` | 经典著作中建筑风环境描述的科学诠释及实证 — 《制冷与空调》2020（大连理工） | 200 | `natural-ventilation` 翠郊吴氏大院院落实测 0.2–0.3 m/s |
| 8 | `http://nepaper.ccdy.cn/html/2014-06/01/content_127126.htm` | 六法考 — 中国文化报 | 200 | `six-principles` 原书名/版本源流源一 |
| 9 | `https://msb.zjol.com.cn/html/2019-01/26/content_3738864.htm` | 六法精论 万古不移 — 美术报（浙江日报报业） | 200 | `six-principles` 版本源流源二 |
| 10 | `https://ylj.suzhou.gov.cn/szsylj/sjyc/201905/c1df393edc8745abb20e8a9bd5525782.shtml` | 拙政园 — 苏州市园林和绿化管理局 | 200 | `sunken-courtyard` 拙政园 1509/王献臣/文徵明 |
| 11 | `https://www.peopleapp.com/rmharticle/30016473527` | 拙政园：天下园林之母 — 人民日报人民号（转荔枝新闻） | 200 | `sunken-courtyard` 1509/王献臣/文征明 佐证 |
| 12 | `https://xbzrb.gdut.edu.cn/cn/article/pdf/preview/10.12052/gdutxb.210119.pdf` | 广府三间两廊天井空间风热参数特性现场研究 — 广东工业大学学报 | 500 | `natural-ventilation` 候选实测源（失败，未采用） |
| 13 | `https://mdpi-res.com/d_attachment/buildings/buildings-12-00629/article_deploy/buildings-12-00629.pdf` | Coupling CFD & Field Experiments…Prince Kung's Mansion — Buildings (MDPI) 2022 | 200 | `natural-ventilation` 恭王府现场 60 测点/1780 |
| 14 | `https://lhsr.sh.gov.cn/jnylwh/20200824/7cc5e5102094470b94a8f771808c1f53.html` | 借景——拙政园的精妙所在 — 上海市绿化和市容管理局 | 200 | `borrowed-scenery` 倚虹亭/1.5 公里/报恩寺北寺塔 |
| 15 | `https://www.pgm.org.cn/pgm/lsyg/201705/fe07519b863b4d4385473890770aee0b.shtml` | 恭王府历史沿革 — 文化和旅游部恭王府博物馆 | 200 | `natural-ventilation` 恭王府 1780 和珅建（源一） |
| 16 | `https://sjfw.mct.gov.cn/site/dataservice/culdetails?curId=10&id=34785` | 5A 级旅游景区·恭王府博物馆 — 文化和旅游部数据服务 | 200 | `natural-ventilation` 恭王府 1780 和珅（源二） |

> 另经 `web_search` 多轮检索，用于定位上述权威页（检索结果仅作导航数据，正文核验以 `urllib` 实抓为准）。

## 六、汇总

- **可升级（整条移出待核实）：1 条 —— `six-principles`**
  - 成书年代约 500 年：JAANUS＋EBSCO 双学术源；原书名异说（《古今画品》/《画品》）与版本源流：中国文化报（郑樵《通志》/《百川学海》/《津逮秘书》）＋美术报（金维诺/刘巽《谢赫辨考》）双权威源**并列呈现即合规**；建议 `needs_verification=false`，正文保留二说并列。
- **可收窄：3 条 —— `perspective`、`sunken-courtyard`、`natural-ventilation`**
  - `perspective`：约 1413 / 15 世纪初已由澎湃（牛津 Kemp）＋纳尔逊-阿特金斯＋Huddersfield（Temple 2016）三独立权威源一致为**约数**；原始文献未定年，将“待补充原始文献/确切年份”改为“学界通行约数、不写死”。
  - `sunken-courtyard`：苏州子实例以拙政园落实（1509、王献臣、文徵明，园林局＋人民号双源），一般庭院由香山帮匠人集体营造、无具名建筑师（上观新闻）；**历史原型对应关系**仍保留。
  - `natural-ventilation`：实测数据获≥两独立学术实测（恭王府 MDPI 2022 现场 60 测点；翠郊吴氏大院《制冷与空调》2020，院落内 0.2～0.3 m/s），设计者可定“不适用/不详（传统工匠营建）”；同一具名实例实测仍单源，故按保守列**收窄**而非升级。
- **保持待核实：59 条** = `borrowed-scenery`（两权威源 live 复核，距离 1.5 vs 1.7 公里冲突须并列、不写死）＋ `glare`（无具名办公实例照度+眩光实测三要素的可配对双源）＋ 其余 57 条（见第四节）。
- **`sunken-plaza`（L1，`needs_verification=false`，不在 63 条内）**：保持，不改层级；作为**可选升级线索**（L1→L2 时可用静安寺下沉广场具名实例）记入 BACKLOG。
- **打开 URL 数**：本轮经 `urllib` 直连**去重 16 个不同 URL**（各站以中文权威站与学术 PDF 为主；失败 1 个：GDUT PDF 500；`big5.cctv.com` 为**央视同源镜像，不计独立源**；#3/#5 为静态壳取正文失败尝试，改 #4 成功）。另有 `web_search` 多轮检索补充定位。

> 保守原则声明：未核验线索不作升级依据；不为凑数硬写年份或人名；维基/央视同源镜像不计独立第二源；两源数值冲突（借景北寺塔 1.5/1.7 公里）与年份约数（透视约 1413）、学界异说（《古画品录》原书名）均**并列标注、不写死**；`natural-ventilation` 因同一具名实例实测仅单源，仅列收窄不升级。以上仅给结论与证据，**未修改任何条目数据或其它文件**（本文件为唯一产出）。
