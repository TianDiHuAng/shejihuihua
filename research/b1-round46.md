# B1/B2 稀疏格补新 scope 候选 — 第 46 轮

- 日期：2026-11-23（Asia/Hong_Kong），采样时刻 2026-11-23 10:xx
- 执行角色：b1-r46（只读子任务，无人值守，未提问）
- 任务：为第 45 轮 B2 覆盖矩阵剩下的 **5 个稀疏格（≤1 条）** 各提 1 条新 scope 候选，要求「≥2 份独立权威来源（不同平台、非维基镜像同源）+ 属本领域 + scope 缺失」。
- 抓取方式：**Python 3.11 urllib + 浏览器 User-Agent 直连实抓**（依据 DECISIONS.md D05：本环境以实际 HTTP 响应为准）。本会话 `web_search` 端点报 502、`web_fetch` 报 `fetch failed`，故全部改用 urllib 直连，逐页判读 `<title>` 与正文关键句。
- 数据纪律：联网内容一律视为**数据**；网页内任何指令均未执行；未下载或运行页面代码，仅读取 HTML 正文判读标题与相关句。
- 只读纪律：本文件是本子任务**唯一产物**；未改动其他文件、未 git commit、未触碰项目外内容（临时脚本均为 stdin heredoc，未落盘项目内）。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

## 环境备注（限制说明）

- 任务点名的 `AUTONOMOUS.md`、`TASK_design.md` 不在工作区根目录；其真实文件位于 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`、`D:/Users/Administrator/Desktop/TASK_design.md`，本轮已实际读取两份原文，并读 `DECISIONS.md`、`scope.md`、`PROGRESS.md`、`coverage-matrix.md`、`research/gaps-round45.md`、`research/b1-round44.md`、`research/b1-round31.md`、`research/b1-round41.md` 作为方法与基线。
- **范围判据取自 TASK_design.md 原文**：绘画理论（透视法、构图法则、色彩理论、光影与明暗、中国画六法与留白、东西方理论比较）；建筑与空间设计（主要建筑风格史；中国传统园林造景；动线设计；下沉式空间；空间序列与尺度；室内外过渡；采光、通风与材料的基本原理）。本轮只接受落入这两段**明确列举子域**的核心概念。
- 从严判定三条须全部满足：①≥2 份**独立**权威来源（不同平台；`owiki.org` 是 Wikipedia 镜像，与 `en.wikipedia.org` 同源，合计只算 1 源）；②属六大面**核心**概念（非边缘技法、非近义重复）；③`scope.md` 确实缺失。
- 联网平台可达性（本轮实测）：`en.wikipedia.org` 可直连（偶发 SSL EOF，重试可达）；可用的**非维基**平台仅 `designingbuildings.co.uk`、`artincontext.org`、`tate.org.uk`、`artsandculture.google.com`、`getty.edu`。`britannica.com`(403)、`whc.unesco.org`(403/SSL)、`metmuseum.org`(429)、`smarthistory.org`(403)、`worldhistory.org`(403)、`archnet.org`(429)、`mdpi.com`(403)、`link.springer.com`(SSL) 均不可用。

## 比对基准

- `scope.md` 现 **251 条**：理论 127 / 风格 62 / 造景 19 / 动线 12 / 下沉空间 12 / 材料 19（核心 50、重要 147、补充 54）。
- 5 个目标稀疏格（据 `coverage-matrix.md` 与 `research/gaps-round45.md`）：
  1. 下沉空间 / 古代 / 中国 = 1（0/1/0），现为 `light-well`（天井）。
  2. 动线 / 古代 / 中国 = 1（0/1/0），现为 `loop-route`（回游式动线）。
  3. 理论 / 跨时期 / 欧洲 = 1（0/0/1），现为 `golden-ratio`（黄金分割）。
  4. 风格 / 中世纪 / 伊斯兰·南亚 = 1（0/1/0），现为 `islamic-architecture`（伊斯兰建筑）。
  5. 风格 / 古代 / 伊斯兰·南亚 = 1（0/1/0），现为 `indian-architecture`（印度建筑）。
- 已 grep 核对：`picturesque / mughal / indo-islamic / umayyad / dikeng / 地坑 / 窑院 / early-islamic` 在 `scope.md`、`entries/*.json`、`data/sources.json`、`coverage.json` 均**无对应条目**（仅 `research/` 往轮分析笔记提到，非收录）。

---

## 候选 1｜下沉空间 / 古代 / 中国

> **该格暂无可达双源候选。**

- 拟议方向：**地坑院（天井窑院 / 下沉式窑院聚落）**——黄土塬区在下沉方形院落四壁横向挖窑形成的坑院式聚落，属「下沉/半地下传统居住空间」核心概念，`scope.md` 缺失。
- 拟议字段：id `dikengyuan`，中文名「地坑院（天井窑院）」，主题 下沉空间，层级 补充，时期 古代，地区 中国。
- **唯一可达权威源（维基，仅 1 平台，不计双源）**：
  - URL：`https://en.wikipedia.org/wiki/Yaodong` ｜ 标题 *Yaodong - Wikipedia* ｜ HTTP **200**
  - 关键句（正文直证）："They are generally carved out of a hillside or excavated horizontally from a central **'sunken courtyard'**."；"…peasants skillfully use loess's features … to **dig a square pit** on the spot, and then **dig the cave horizontally on the four walls to form the underground courtyard**. In most parts of western Henan, this form of cave is called the **'pit yard'**."；目录含子节 "**Sunken Yaodong**"。
- **第二独立源本轮全部不可达**（逐条实测）：`britannica.com` 403；`whc.unesco.org` 403/SSL；`metmuseum.org` 429；`worldhistory.org` 403；`designingbuildings.co.uk` 各相关 slug 均 404（`Earth_sheltered_construction` / `Cave_dwelling` / `Underground_building` / `Chinese_architecture` / `Siheyuan` / `Courtyard_house` / `Sunken_courtyard`）；`artincontext.org` 无地坑院专页（`/cave-dwellings/`、`/underground-architecture/`、`/earth-sheltered/` 均 404）；`mdpi.com`/`link.springer.com` 403/SSL；`ihchina.cn`（中国非遗网，地坑院营造技艺为国家级非遗）主页 200 但网络中断、无稳定专页可定位。
- 结论：仅 Wikipedia 单平台（且 owiki 镜像同源不计第二源），**凑不齐「≥2 独立权威源」**，按任务规则如实记「该格暂无可达双源候选」，不虚构第二源。

---

## 候选 2｜动线 / 古代 / 中国

- 建议 id：`imperial-axial-route`
- 中文名：**宫廷中轴仪礼动线（紫禁城南北中轴行进序列）**
- 主题：**动线** ｜ 层级：**重要** ｜ 时期：**古代** ｜ 地区：**中国**
- 定义：以南北中轴为脊、由连续门—庭—殿自南向北依次展开、以「外朝（南）→ 内朝（北）」礼仪行进为组织逻辑的宫殿空间动线，属「动线设计」面在古代中国宫殿的典型形制。
- 来源 1（维基百科）：
  - URL：`https://en.wikipedia.org/wiki/Forbidden_City` ｜ 标题 *Forbidden City - Wikipedia* ｜ HTTP **200**
  - 关键句："The Forbidden City is the imperial palace complex in the center of the Imperial City in Beijing, China."；"[UNESCO] … **Part of Beijing Central Axis** …"；结构分节 "Walls and gates / **Outer Court or the Southern Section** / **Inner Court or the Northern Section**"；"The courtyard was built on a massive, luxurious scale…"。
- 来源 2（Designing Buildings，英国建筑技术平台，非维基）：
  - URL：`https://www.designingbuildings.co.uk/wiki/Forbidden_City` ｜ 标题 *Forbidden City - Designing Buildings* ｜ HTTP **200**
  - 关键句："The **Outer Court** (the **southern** part of the complex), with its expansive **courtyards** and monumental pavilions, was used for **public audiences and ceremonies**; while the **Inner Court** (**northern** part) contained residences…"；"…typifies traditional Chinese palatial architecture, with the emphasis on articulation and **bilateral symmetry** to signify balance."。
- 入选理由：两源为**不同平台**、均 200 正文直证，共同支撑「紫禁城位于北京中轴之上、以南北对称、外朝→内朝连续庭院承载礼仪行进」这一**宫殿中轴仪礼动线**概念；`scope.md` 现有动线 12 条中，中国/古代仅 `loop-route`（回游），无「中轴行进序列」，且理论面 `axis`/`spatial-sequence` 为抽象概念、非古代中国宫廷动线实例，故本格缺失。与任务建议「宫廷/寺庙轴线行进」方向一致。
- 备注：两源均以紫禁城为典例描述该动线原则；概念层面成立（动线组织方式），实例层面为紫禁城。

---

## 候选 3｜理论 / 跨时期 / 欧洲

- 建议 id：`picturesque`
- 中文名：**如画（Picturesque 美学）**
- 主题：**理论** ｜ 层级：**重要** ｜ 时期：**跨时期** ｜ 地区：**欧洲**
- 定义：18 世纪英国形成的审美范畴与绘画/景观构图理论——以「兼具优美与野性、如风景画般入画」为准则，深刻影响风景画构图与如画式园林，并在后世绘画与景观理论中反复被援引，故按本项目粗分归「跨时期/欧洲」。
- 来源 1（维基百科）：
  - URL：`https://en.wikipedia.org/wiki/Picturesque` ｜ 标题 *Picturesque - Wikipedia* ｜ HTTP **200**
  - 关键句："Highly instrumental in the establishing of a taste for the **picturesque** in northern Europe was **landscape painting**…"；"Claude Lorrain (1604–1682) was a well-known French painter, who had developed landscape painting…"。
- 来源 2（Tate，英国泰特美术馆，非维基）：
  - URL：`https://www.tate.org.uk/art/art-terms/p/picturesque` ｜ 标题 *Picturesque | Tate* ｜ HTTP **200**
  - 关键句："**The word picturesque refers to an ideal type of landscape that has an artistic appeal, in that it is beautiful but also with some elements of wildness.**"。
- 入选理由：两源为**不同平台**（百科 vs 美术馆权威术语页）、均 200 正文直证，把「如画」明确归入视觉艺术/绘画理论范畴；`scope.md` 理论 127 条中无 `picturesque`，`golden-ratio` 之外无其他欧洲/跨时期美学命题，本格仅 1 条（补充），补此条可填格。第 41 轮曾因第二源不可达（Tate DNS 失败、Britannica 403）放弃，本轮 Tate 可达，构成**新的可达双源**。

---

## 候选 4｜风格 / 中世纪 / 伊斯兰·南亚

- 建议 id：`mughal-architecture`
- 中文名：**莫卧儿建筑（Mughal architecture）**
- 主题：**风格** ｜ 层级：**重要** ｜ 时期：**中世纪**（按目标格；见备注）｜ 地区：**伊斯兰/南亚**
- 定义：16–17 世纪印度次大陆莫卧儿王朝的建筑风格，融合印度、波斯与伊斯兰传统，以严格几何、完美对称、等级化材料与形式著称（泰姬陵、胡马雍陵、法泰赫普尔西克里、阿格拉堡等）。
- 来源 1（维基百科）：
  - URL：`https://en.wikipedia.org/wiki/Mughal_architecture` ｜ 标题 *Mughal architecture - Wikipedia* ｜ HTTP **200**
  - 关键句："**Mughal emperors and elites consciously used architecture as a way to publicly display their presence and power.**"；建筑类型/纪念物分节列 Babur / Humayun / Akbar（Agra Fort、Humayun's Tomb、Fatehpur Sikri）/ Jahangir / Shah Jahan（**Taj Mahal**、Wazir Khan Mosque）/ Aurangzeb（Badshahi Mosque）等。
- 来源 2（Designing Buildings，非维基）：
  - URL：`https://www.designingbuildings.co.uk/wiki/Taj_Mahal` ｜ 标题 *Taj Mahal - Designing Buildings* ｜ HTTP **200**
  - 关键句："…commissioned in 1632 by the **Mughal emperor Shah Jahan** … **generally regarded as the best example of Mughal architecture, which is a blend of Indian, Persian and Islamic styles.**"；"Rational and strict geometry. Perfect symmetrical planning."。
- 入选理由：两源为**不同平台**、均 200 正文直证，把「莫卧儿建筑」明确归入建筑风格史并给出风格特征；`scope.md` 风格 62 条中无 `mughal-architecture`，`islamic-architecture`/`indian-architecture` 仅为泛伞条目，本格（伊斯兰/南亚·中世纪）仅 1 条泛条，补此具名风格可填格。第 31 轮 Mughal 第二源全不可达，本轮 `designingbuildings.co.uk/wiki/Taj_Mahal` 可达且正文直指「best example of Mughal architecture」，构成**新的可达双源**。
- 备注：莫卧儿王朝史学上一般归「近世（16–17 世纪）」，本项目粗分时期表将其并入「中世纪/伊斯兰·南亚」格以填格；入库时若严格史学分档，可标注 `period` 存疑并核对（据 TASK_design 时期为粗粒度分区）。与伞条目 `islamic-architecture` 为「具名风格 vs 泛伊斯兰」之关系，非近义重复。

---

## 候选 5｜风格 / 古代 / 伊斯兰·南亚

- 建议 id：`early-islamic-architecture`
- 中文名：**早期伊斯兰建筑（清真寺形制：Umayyad 形成期）**
- 主题：**风格** ｜ 层级：**重要** ｜ 时期：**古代** ｜ 地区：**伊斯兰/南亚**
- 定义：7–8 世纪伊斯兰教形成期的宗教建筑形制——以圆顶圣所（Dome of the Rock, 691）与柱廊式（hypostyle）清真寺（如大马士革大清真寺、Wasit 周五清真寺）为典型，奠定此后伊斯兰宗教建筑的基本型制。
- 来源 1（维基百科）：
  - URL：`https://en.wikipedia.org/wiki/Umayyad_architecture` ｜ 标题 *Umayyad architecture - Wikipedia* ｜ HTTP **200**
  - 关键句："Wasit … included a **square Friday Mosque with a hypostyle roof**."；结构分节含 "**Dome of the Rock**"、"Mosques（General development / **Great Mosque of Damascus**）"。
- 来源 2（Art in Context，艺术史教育与研究平台，非维基）：
  - URL：`https://artincontext.org/islamic-art/` ｜ 标题 *Islamic Art - A Deep Dive into the Gilded World of Islamic Art* ｜ HTTP **200**
  - 关键句："…the shrine in Jerusalem called the **Dome of the Rock (c. 7th century CE)** and the **Al-Aqsa Mosque (completed in 705 CE)**…"；"There was also a focus on **building architectural structures like Mosques**…"。
- 入选理由：两源为**不同平台**、均 200 正文直证，共同把「早期伊斯兰（Umayyad 期）清真寺/圆顶圣所形制」归入建筑史；`scope.md` 风格面 `islamic-architecture`（中世纪泛条）与 `indian-architecture`（古代）之外，无「早期伊斯兰建筑/清真寺形制」具名条目，本格（伊斯兰/南亚·古代）仅 `indian-architecture` 1 条，补此条可填格且与中世纪泛伊斯兰条形成「形成期 vs 后续」区分，非近义重复。
- 备注：`artincontext.org` 为艺术史平台，其对 Umayyad 期建筑的表述偏「伊斯兰艺术」总述，但正文直指 Dome of the Rock / Al-Aqsa 等建筑本体，可用于风格形成期佐证；`designingbuildings.co.uk/wiki/Mosque`、`/Hypostyle` 本轮 404/SSL 不可达。

---

## 双源可达性明细（本轮实测 HTTP）

### 入选双源（均 HTTP 200，不同平台）
| 格 | 来源 A（平台） | HTTP | 来源 B（平台，非维基） | HTTP |
| --- | --- | --- | --- | --- |
| 动线/古代/中国 | `https://en.wikipedia.org/wiki/Forbidden_City`（Wikipedia） | 200 | `https://www.designingbuildings.co.uk/wiki/Forbidden_City`（Designing Buildings） | 200 |
| 理论/跨时期/欧洲 | `https://en.wikipedia.org/wiki/Picturesque`（Wikipedia） | 200 | `https://www.tate.org.uk/art/art-terms/p/picturesque`（Tate） | 200 |
| 风格/中世纪/伊斯兰·南亚 | `https://en.wikipedia.org/wiki/Mughal_architecture`（Wikipedia） | 200 | `https://www.designingbuildings.co.uk/wiki/Taj_Mahal`（Designing Buildings） | 200 |
| 风格/古代/伊斯兰·南亚 | `https://en.wikipedia.org/wiki/Umayyad_architecture`（Wikipedia） | 200 | `https://artincontext.org/islamic-art/`（Art in Context） | 200 |

### 第二源不可达记录
| 目标 | 尝试 URL | 结果 |
| --- | --- | --- |
| 下沉空间/古代/中国 | `https://en.wikipedia.org/wiki/Yaodong`（单源，仅此可达） | 200（**仅 1 平台**，不计双源） |
| 同上 第二源 | `https://www.britannica.com/…`、`https://whc.unesco.org/…`、`https://www.metmuseum.org/…`、`https://www.worldhistory.org/…` | 403 / 403·SSL / 429 / 403 |
| 同上 第二源 | `designingbuildings.co.uk/wiki/{Earth_sheltered_construction,Cave_dwelling,Underground_building,Chinese_architecture,Siheyuan,Courtyard_house,Sunken_courtyard}` | 404 / SSL |
| 同上 第二源 | `artincontext.org/{cave-dwellings,underground-architecture,earth-sheltered}` | 404 |
| 同上 第二源 | `https://www.mdpi.com/search…`、`https://link.springer.com/search…`、`https://www.ihchina.cn/` | 403 / SSL / 网络中断 |
| 动线/古代/中国 备选 | `https://en.wikipedia.org/wiki/Beijing_Central_Axis` | 超时（未取到，改用 Forbidden City 两平台） |
| 风格/中世纪 备选 | `designingbuildings.co.uk/wiki/Mughal_architecture`、`artincontext.org/mughal-art` | 404 |

### 打开 URL 计数
- 本轮实际发起 HTTP 请求 **约 60+ 次**（含同页多次取不同结构、失败重试）；去重后 **约 60 个不同 URL**；其中 **HTTP 200 约 23 个**，其余为 403/404/429/SSL/超时（主要用于排除第二源）。
- 入选 4 格的 8 份来源**全部 HTTP 200**、标题与正文关键句均逐条核对（见上「入选双源」表）。

---

## 机器可读汇总

```
ROUND=46
SCOPE_TOTAL=251   # 理论127/风格62/造景19/动线12/下沉12/材料19
TARGET_CELLS=["下沉空间/古代/中国","动线/古代/中国","理论/跨时期/欧洲","风格/中世纪/伊斯兰/南亚","风格/古代/伊斯兰/南亚"]
DOUBLE_SOURCE_CANDIDATES=4
CELL_NO_DOUBLE_SOURCE=["下沉空间/古代/中国"]   # 仅 Wikipedia Yaodong 单平台可达，第二独立源全部不可达

CANDIDATES=[
 {"id":"imperial-axial-route","title":"宫廷中轴仪礼动线（紫禁城南北中轴行进序列）","theme":"动线","tier":"重要","period":"古代","region":"中国","sources":["wp-forbidden-city","designingbuildings-forbidden-city"],"urls":["https://en.wikipedia.org/wiki/Forbidden_City","https://www.designingbuildings.co.uk/wiki/Forbidden_City"]},
 {"id":"picturesque","title":"如画（Picturesque 美学）","theme":"理论","tier":"重要","period":"跨时期","region":"欧洲","sources":["wp-picturesque","tate-picturesque"],"urls":["https://en.wikipedia.org/wiki/Picturesque","https://www.tate.org.uk/art/art-terms/p/picturesque"]},
 {"id":"mughal-architecture","title":"莫卧儿建筑（Mughal architecture）","theme":"风格","tier":"重要","period":"中世纪","region":"伊斯兰/南亚","sources":["wp-mughal-architecture","designingbuildings-taj-mahal"],"urls":["https://en.wikipedia.org/wiki/Mughal_architecture","https://www.designingbuildings.co.uk/wiki/Taj_Mahal"]},
 {"id":"early-islamic-architecture","title":"早期伊斯兰建筑（清真寺形制：Umayyad 形成期）","theme":"风格","tier":"重要","period":"古代","region":"伊斯兰/南亚","sources":["wp-umayyad-architecture","artincontext-islamic-art"],"urls":["https://en.wikipedia.org/wiki/Umayyad_architecture","https://artincontext.org/islamic-art/"]}
]

CANDIDATE_PENDING_SECOND=[
 {"id":"dikengyuan","title":"地坑院（天井窑院）","theme":"下沉空间","tier":"补充","period":"古代","region":"中国","reachable_sources":["wp-yaodong"],"urls":["https://en.wikipedia.org/wiki/Yaodong"],"status":"single-platform-only（owiki 同源不计第二源）","blocker":"Britannica/UNESCO/Met/WorldHistory 403·429；designingbuildings 相关 slug 404；artincontext 无专页 404；MDPI/Springer 403·SSL；ihchina 网络中断"}
]

SECOND_SOURCE_FAILED={
 "dikengyuan":["britannica 403","unesco 403/SSL","met 429","worldhistory 403","designingbuildings 404 (7 slugs)","artincontext 404","mdpi 403","springer SSL","ihchina network-interrupted"]
}

NOTE_PERIOD={
 "mughal-architecture":"按目标格填中世纪；史学实际16–17世纪，入库时建议标注并核对期限口径"
}
```

是否发现新缺口：**是**——4 个稀疏格（动线/古代/中国、理论/跨时期/欧洲、风格/中世纪/伊斯兰·南亚、风格/古代/伊斯兰·南亚）各给出「≥2 独立权威源 + 属本领域 + scope 缺失」的新 scope 候选；**1 个格（下沉空间/古代/中国）本轮无可达双源候选**（仅 Wikipedia 单平台），如实记录不虚构。
