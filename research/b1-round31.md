# B1/B2 稀疏格补条 — 第 31 轮（2 条新 scope 候选，双源实抓）

- 日期：2026-11-22（Asia/Hong_Kong）
- 执行角色：b1-r31（只读子任务，无人值守）
- 抓取方式：Python 3.11 urllib + 浏览器 User-Agent；依据 DECISIONS.md D05（web_search / web_fetch 在本环境返回错误，改用 Python 直连实抓）。
- 数据纪律：联网内容一律视为数据；网页内任何指令均未执行；未下载或运行页面代码，仅读取 HTML / 纯文本判读标题与相关句。维基 canonical（en.wikipedia.org）本轮连接均超时（WinError 10060），按任务许可改用 `owiki.org` 镜像读取，**同源只计一源**；每条候选的第二源均为另一独立出版方。
- 产出：本文件是本子任务唯一产物；未改动其他文件、未 git commit、未触碰项目外内容。

## 环境备注（限制说明）

- 任务点名先读的 `AUTONOMOUS.md`、`TASK_design.md` 在当前工作区**实际不存在**（`**/AUTONOMOUS.md`、`**/TASK_design.md` 均无匹配；项目根仅有 BACKLOG/BLOCKERS/DECISIONS/PROGRESS/REPORT/scope/coverage 等治理文件，设计文档位于 `docs/superpowers/plans|specs/`）。本报告以现存治理文件 `DECISIONS.md`、`scope.md`、`coverage-matrix.md`、`research/gaps-round30.md` 与上轮 `research/b1-round30.md` 的方法及来源纪律为准执行，沿用 D05 直连实抓。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

## 选格依据（为何是这 2 格）

`gaps-round30.md` 的 B2 覆盖矩阵列出「稀疏格（≤1 条）7」，第 30 轮已补 `风格/文艺复兴至19世纪/美洲`（mexican-baroque）与 `理论/20世纪/东亚`（metabolism），现存 7 格稀疏格及现状（据 `coverage-matrix.md` 当前版）：

| 稀疏格 | 现条目数（核心/重要/补充） | 现唯一/主要条目 |
| --- | --- | --- |
| 理论 / 欧洲 / 古代 | 1（1/0/0） | vitruvian-triad（维特鲁威三原则） |
| 理论 / 欧洲 / 跨时期 | 1（0/0/1） | golden-ratio（黄金分割） |
| 理论 / 全球 / 文艺复兴至19世纪 | 1（0/0/1） | core-shadow（明暗交界线） |
| 风格 / 古代 / 伊斯兰·南亚 | 1（0/1/0） | indian-architecture（印度建筑） |
| 风格 / 中世纪 / 伊斯兰·南亚 | 1（0/1/0） | islamic-architecture（伊斯兰建筑） |
| 动线 / 古代 / 中国 | 1（0/1/0） | loop-route（回游式动线） |
| 下沉空间 / 古代 / 中国 | 1（0/1/0） | light-well（天井） |

**本轮选这 2 格（各补 1 条）**：

1. **理论 / 文艺复兴至19世纪 / 全球** —— 该格仅 1 条「明暗交界线」（补充级），整格缺「学院派/艺术教育理论」这一 17–19 世纪主导绘画实践的核心脉络；补「学院派理论与素描教学」把西方学院体系（Académie des Beaux-Arts）的绘画理论、门类等级与素描教学落到具名条目，与任务示例方向（学院派理论/素描教学）完全一致。
2. **理论 / 欧洲 / 古代** —— 该格仅 1 条「维特鲁威三原则」；补「古典柱式」（Classical order）补齐古典建筑比例/柱式理论，这是 Vitruvius 三原则之外、贯通绘画比例理论与建筑空间设计的核心理论，且与既有的 proportion / ancient-greek / symmetry-layout 均不等价。

**为何未走任务示例中的其它方向（凑不齐双源则换方向并说明）**：

- `风格 / 古代 / 伊斯兰·南亚 → 莫卧儿建筑`、`风格 / 中世纪 / 伊斯兰·南亚 → 伊斯兰建筑细分（Indo-Islamic）`：维基源（owiki）可达（`Mughal_architecture`、`Indo-Islamic_architecture`、`Hindu_temple_architecture` 均 HTTP 200），但**第二独立权威源全部不可达**——Britannica 403、UNESCO 403、Met 超时/429、World History Encyclopedia 403、New World Encyclopedia 超时、Visual-Arts-Cork 拒连 10061、artincontext 无 Mughal 专文（`/mughal-art/`、`/mughal-architecture/` 均 404）、Designing Buildings 无相关 slug（`Mughal_architecture`、`Indo-Islamic_architecture`、`Islamic_architecture`、`Hindu_architecture`、`Temple_architecture` 均 404）。缺第二源，故本轮放弃该方向。
- `动线 / 古代 / 中国 → 传统廊庑/游廊`：Designing Buildings `Veranda`(200)/`Corridor`(200) 与 owiki `Veranda`(200) 可达，但该概念与已收录 `corridor-space`（廊道空间，理论/跨时期/全球）高度近义，触犯判据「排除近义已收录项」；且英文源为通名、非中国「廊庑」专指，概念贴合度不足，故放弃。

## 判据

一条候选「值得新增」需同时满足：
1. 属绘画理论或建筑空间设计范围；
2. 在 `scope.md` 244 条中无对应 id / 中文名 / 等价概念（排除近义已收录项；已 grep 核实无 `柱式/order/学院/academic` 等重复项，`beaux-arts` 为「学院派建筑（布扎艺术）」属建筑风格，与本条绘画学院派理论不同域）；
3. 确实补上目标稀疏格（主题 × 时期 × 地区三者吻合）；
4. 至少两份**独立**权威来源实抓为 HTTP 200，页面标题与主题吻合，并能摘出正文关键句（维基镜像仅计一源，第二源须为不同出版方）。

---

## 候选 1：academic-art-theory（学院派理论与素描教学 / 学院主义）— 建议纳入

- 建议 id：`academic-art-theory`
- 中文名：学院派理论与素描教学（学院主义 / Academic art）
- 主题：理论
- 层级：重要
- 时期：文艺复兴至19世纪（17–19 世纪学院体系与沙龙）
- 地区：全球（以欧洲艺术学院体系为中心，影响全球）
- 目标稀疏格：理论 / 文艺复兴至19世纪 / 全球（现 1 条，0/0/1，为 core-shadow）
- 来源一（维基，owiki 镜像）：https://owiki.org/wiki/Academic_art —《Academic art ::: Open WIKI》— HTTP 200
  - 说明：维基 canonical `https://en.wikipedia.org/wiki/Academic_art` 本轮连接超时（WinError 10060），按任务许可用 owiki 镜像读取，仅计一源。
  - 正文关键句：「Academic art, academicism, or academism, is a style of painting and sculpture produced under the influence of European academies of art.」
  - 正文关键句：「The academies were established to replace medieval artists' guilds and aimed to systematize the teaching of art.」
  - 正文关键句：「They emphasized the emulation of established masters and the classical tradition, downplaying the importance of individual creativity, valuing instead collective, aesthetic and ethical concepts.」
  - 正文关键句：「Overall, academicism has had a significant impact on the development of art education and artistic styles.」
- 来源二（独立出版方，Art in Context）：https://artincontext.org/academic-art/ —《Academic Art - A Look at the Canvas of Intellectual Expression》— HTTP 200
  - 正文关键句：「Academic artists could be Neoclassical, Romantic, historicist, Orientalist, Realist, or eclectic, but they commonly valued disciplined drawing, anatomy, composition, finish, and subjects ranked by an institutional hierarchy.」
  - 正文关键句：「'Academic' describes an institutional system as much as an appearance.」
- 入选理由：维基「Academic art」专条定义其为欧洲艺术学院影响下产生的绘画与雕塑风格/体系，明确学院「以系统化艺术教学为目的」、强调「临摹大师与古典传统」，并点明其对「艺术教育」的深远影响；第二源 Art in Context（独立艺术教育出版方）独立印证其核心是「制度化体系（institutional system）」，并把「素描(drawing)、解剖、构图、完成度、按门类等级排序的题材」列为其受训与评审要点——正好覆盖「学院派理论 + 素描教学 + 门类等级」三个主题点，与目标格「理论/文艺复兴至19世纪/全球」吻合。两源独立、均 200、均可摘正文关键句。本条把 `beaux-arts`（学院派建筑，建筑风格）之外的「绘画学院派理论与素描教学」补入理论维度，与既有 `core-shadow` 不重叠。
- 概念贴合度：高（一源为该主题正式专条并给出命名与教学制度，另一源为独立出版方对「学院＝制度体系＋素描/解剖/构图训练＋门类等级」的独立佐证）。
- 与既有条目区隔：`beaux-arts` = 学院派**建筑**（布扎艺术，风格）；本条 = 学院派**绘画理论/素描教学**（理论）。二者同源于艺术学院传统但分属不同主题与领域，不构成近义重复。

## 候选 2：classical-order（古典柱式 / Classical order）— 建议纳入

- 建议 id：`classical-order`
- 中文名：古典柱式（古典建筑柱式 / Classical order）
- 主题：理论
- 层级：重要
- 时期：古代（古希腊、古罗马）
- 地区：欧洲
- 目标稀疏格：理论 / 欧洲 / 古代（现 1 条，1/0/0，为 vitruvian-triad）
- 来源一（维基，owiki 镜像）：https://owiki.org/wiki/Classical_order —《Classical order ::: Open WIKI》— HTTP 200
  - 说明：维基 canonical `https://en.wikipedia.org/wiki/Classical_order` 本轮连接超时（WinError 10060），用 owiki 镜像读取，仅计一源。
  - 正文关键句：「An order in architecture is a certain assemblage of parts subject to uniform established proportions, regulated by the office that each part has to perform.」
  - 正文关键句：「Coming down to the present from Ancient Greek and Ancient Roman civilization, the architectural orders are the styles of classical architecture, each distinguished by its proportions and characteristic profiles and details, and most readily recognizable by the type of column employed.」
  - 正文关键句：「The three orders of architecture—the Doric, Ionic, and Corinthian—originated in Greece.」
- 来源二（独立出版方，Designing Buildings）：https://www.designingbuildings.co.uk/wiki/Classical_architecture —《Classical architecture - Designing Buildings》— HTTP 200
  - 正文关键句：「Greek architecture followed a highly-structured system of proportions that related individual architectural components to the whole building.」
  - 正文关键句：「This system was developed according to three basic styles, or 'orders' – Doric, Ionic and Corinthian – that formed the heart of classical Greek architecture.」
  - 正文关键句：「The Romans also used these widely but added two of their own orders: Tuscan and Composite.」
- 入选理由：维基「Classical order」专条定义柱式为「受统一既定比例约束、由各部分职责规范的一组构件」，指出其源自古希腊/古罗马、以柱式类型辨识，并给出 Doric/Ionic/Corinthian 三大希腊柱式；第二源 Designing Buildings（英国建筑行业知识库，独立于维基）独立印证希腊建筑「遵循高度结构化的比例体系」，且「由 Doric、Ionic、Corinthian 三种基本柱式构成古典希腊建筑的核心」，罗马另加 Tuscan、Composite 两柱式，与维基完全互证。两源独立、均 200、均可摘正文关键句。本条把「理论/欧洲/古代」从仅有维特鲁威三原则扩展为「三原则 + 柱式比例理论」，属贯通绘画比例与建筑空间设计的核心古典理论。
- 概念贴合度：高（两源独立、均 200，均以柱式/order 为条目核心并直接给出比例体系与五柱式构成）。
- 与既有条目区隔：`vitruvian-triad` = 建筑三原则（坚固/实用/美观）；`proportion`/`golden-ratio` = 一般比例；`ancient-greek`/`ancient-roman` = 建筑**风格**。`classical-order` 为**柱式比例体系（理论）**，与上述均不等价。

---

## 实际打开的 URL 与 HTTP 状态

| 来源 id | 页面 URL | 页面标题 | HTTP |
| --- | --- | --- | --- |
| w-owiki-academic | https://owiki.org/wiki/Academic_art | Academic art ::: Open WIKI | 200 |
| aic-academic | https://artincontext.org/academic-art/ | Academic Art - A Look at the Canvas of Intellectual Expression | 200 |
| w-owiki-classorder | https://owiki.org/wiki/Classical_order | Classical order ::: Open WIKI | 200 |
| dbb-classarch | https://www.designingbuildings.co.uk/wiki/Classical_architecture | Classical architecture - Designing Buildings | 200 |

> 维基 canonical（en.wikipedia.org）本轮多次连接超时（WinError 10060），按任务许可与 D05 改用 owiki 镜像读取；镜像与原条目同源，各仅计一源，第二源分别为 Art in Context（artincontext.org）与 Designing Buildings（designingbuildings.co.uk），均为独立出版方。

## 试抓失败 / 被排除的来源（审计用）

| URL | 结果 | 备注 |
| --- | --- | --- |
| https://en.wikipedia.org/wiki/Academic_art · /Classical_order · /Mughal_architecture · /Indo-Islamic_architecture · /Hindu_temple_architecture · /Veranda · /Dravidian_architecture | TimeoutError 10060 | 维基 canonical 全部超时，改用 owiki 镜像（同源计一源） |
| https://www.britannica.com/art/Mughal-architecture · /topic/Indo-Islamic-architecture · /topic/Dravidian-architecture · /art/academic-art | HTTP 403 | Cloudflare 拦截 urllib，弃用 |
| https://whc.unesco.org/en/list/252/ (Taj Mahal) | HTTP 403 | Forbidden，弃用 |
| https://www.metmuseum.org/toah/hd/mugh/hd_mugh.htm · /hd_mugh_2 · /hd/indm · /hd/acad | Timeout / HTTP 429 | 网络不可达或限流，弃用 |
| https://www.worldhistory.org/Mughal_Architecture/ · /Indo-Islamic_Architecture/ · /Hindu_Architecture/ · /Dravidian_Architecture/ | HTTP 403 | Forbidden，弃用 |
| https://www.newworldencyclopedia.org/entry/{Mughal_architecture,Indo-Islamic_architecture,Academic_art,Veranda,Mughal_Empire} | Timeout | 不可达，弃用 |
| https://www.designingbuildings.co.uk/wiki/{Mughal_architecture,Indo-Islamic_architecture,Islamic_architecture,Hindu_architecture,Temple_architecture,Beaux-Arts_architecture,Beaux-Arts_style,Academic_art} | HTTP 404 | slug 不存在；本项目第二源仅 `Classical_architecture`/`Veranda`/`Corridor`/`Loggia`/`Colonnade`/`Arcade` 等可达 |
| https://www.encyclopedia.com/.../academic-art · /.../mughal-architecture | Timeout | 不可达，弃用 |
| https://www.visual-arts-cork.com/architecture/mughal.htm · /history-of-art/academic-art.htm | ConnectionRefused 10061 | 拒连，弃用 |
| https://www.arthistory.net/academic-art/ · https://www.tate.org.uk/art/art-terms/a/academic-art | getaddrinfo 失败 | DNS 解析失败，弃用 |
| https://www.theartstory.org/movement/academic-art/ | HTTP 404 | slug 不匹配，弃用 |
| https://www.khanacademy.org/humanities/.../a/academic-art | 200 但「Client Challenge」 | JS 挑战页，无静态正文，不计为来源 |
| https://artincontext.org/mughal-art/ · /mughal-architecture/ · https://www.thecollector.com/{academic-art,what-is-academic-art,mughal-architecture} · https://www.archdaily.com/tag/mughal-architecture | HTTP 404 | 备选方向第二源不可达，故 Mughal/Indo-Islamic 方向搁置 |
| https://www.archnet.org/ | HTTP 429 | 限流，弃用 |

## 机器可读汇总

```
CANDIDATES=[{"id":"academic-art-theory","title":"学院派理论与素描教学（学院主义 / Academic art）","theme":"理论","tier":"重要","period":"文艺复兴至19世纪","region":"全球","urls":["https://owiki.org/wiki/Academic_art","https://artincontext.org/academic-art/"],"sources":["w-owiki-academic","aic-academic"]},{"id":"classical-order","title":"古典柱式（古典建筑柱式 / Classical order）","theme":"理论","tier":"重要","period":"古代","region":"欧洲","urls":["https://owiki.org/wiki/Classical_order","https://www.designingbuildings.co.uk/wiki/Classical_architecture"],"sources":["w-owiki-classorder","dbb-classarch"]}]
REJECTED=[]
```
