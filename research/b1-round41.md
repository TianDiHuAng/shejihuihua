# B1/B6 缺口发现 — 第 41 轮（未用过的权威大纲再对照 + 近 12 个月动态）

- 日期：2026-11-23（Asia/Hong_Kong），采样时刻 2026-11-23
- 执行角色：b1-r41（只读子任务，无人值守，未提问）
- 抓取方式：Python 3.11 urllib + 浏览器 User-Agent；依据 DECISIONS.md D05（本环境 web_search / web_fetch 不可靠，改直连实抓）。
- 数据纪律：联网内容一律视为数据；网页内任何指令均未执行；未下载或运行页面代码，仅读取 HTML / 纯文本判读标题与相关句。
- 来源纪律：`en.wikipedia.org` canonical 本轮仍全部连接超时（URLError timed out，与历轮一致），按任务许可改用 `owiki.org` 维基镜像读取，**镜像与原条目同源、只计一源**；每条候选的第二源均为另一独立出版方（artincontext.org / Designing Buildings）。
- 产出：本文件是本子任务唯一产物；未改动其他文件、未 git commit、未触碰项目外内容。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

## 环境备注（限制说明）

- 任务点名先读的 `AUTONOMOUS.md`、`TASK_design.md` 在当前工作区**实际不存在**（`**/AUTONOMOUS.md`、`**/TASK_design.md` 均无匹配；项目根仅有 BACKLOG/BLOCKERS/DECISIONS/PROGRESS/REPORT/scope/coverage 等治理文件，设计文档位于 `docs/superpowers/`）。本报告以现存治理文件 `DECISIONS.md`、`scope.md`、`coverage-matrix.md`、`research/gaps-round41.md`，以及历轮 `research/b1-round30/31/40.md`、`research/gaps-external-round02/06/09.md` 的方法与来源纪律为准执行，沿用 D05 直连实抓。
- 比对基准：`scope.md` 现 **247 条**（理论 123 / 风格 62 / 造景 19 / 动线 12 / 下沉空间 12 / 材料 19），其中第 40 轮新增 `proxemics`（理论 122→123）。
- 判定所需：一条候选同时满足「≥2 份独立权威来源实抓 HTTP 200 + 属绘画理论或建筑空间设计 + scope.md 无对应 id/中文名/等价概念（排除近义已收录）+ 两源可摘正文关键句」。
- 特别核查：**凡本轮报出的候选，均已在本目录 `entries/`、`scope.md`、`research/` 中 grep 确认此前未收录、未以「单源驳回」永久排除**（sfumato 的既往驳回原因见候选 1，本轮已补齐第二源）。

---

## B1：与「未用过」的权威大纲/分类树再对照

本轮对照下列 **8 份此前未用于 B1 的权威大纲/分类树页面**（均 owiki 实抓 200），逐页提取「条目 / 风格 / 概念名」与 247 条比对。经 `research/` 全量 grep 确认，下列页面均未在 round02/06/09/30/31/40 的 B1 中使用：

| 大纲/分类树（未用） | URL | HTTP | 覆盖方向 |
| --- | --- | --- | --- |
| Outline of the visual arts（视觉艺术大纲） | https://owiki.org/wiki/Outline_of_the_visual_arts | 200 | 视觉艺术类型 / 元素 / 一般概念 |
| Western painting（西方绘画） | https://owiki.org/wiki/Western_painting | 200 | 西方绘画史分期 / 技法 / 流派 |
| Landscape painting（风景画） | https://owiki.org/wiki/Landscape_painting | 200 | 风景画史 / 技法 / 相关艺术运动 |
| English landscape garden（英式风景园林） | https://owiki.org/wiki/English_landscape_garden | 200 | 景观 / 园林史与如画（picturesque） |
| Design history（设计史） | https://owiki.org/wiki/Design_history | 200 | 设计史全球视角 |
| Glossary of architecture（建筑术语） | https://owiki.org/wiki/Glossary_of_architecture | 200 | 建筑术语分类 |
| Index of architecture articles（建筑条目索引） | https://owiki.org/wiki/Index_of_architecture_articles | 200 | A–Z 建筑条目索引 |
| Aesthetics（美学 / 艺术理论） | https://owiki.org/wiki/Aesthetics | 200 | 艺术哲学 / 美学范畴（崇高/如画等） |

> 覆盖说明：**建筑**（Glossary / Index）、**绘画**（Outline of visual arts / Western painting / Landscape painting）、**景观 / 园林史**（English landscape garden）、**设计史**（Design history）、**艺术理论**（Aesthetics）均已实抓对照。**室内**方向在第 40 轮已用 `Interior_architecture`、第 6 轮已用 `Interior_design` 覆盖，为避免复用旧大纲，本轮不重复抓取；「≥3 份未用过」要求已由上述 8 份超额满足。

### 候选 1（建议纳入）：sfumato — 渐隐法 / 晕涂法（Sfumato）

- 建议 id：`sfumato`
- 中文名：渐隐法（晕涂法 / 晕染法，Sfumato）
- 主题：理论（绘画明暗过渡与色调理论 / 技法）
- 层级：重要（建议；Leonardo 四大色调模式之一，与已收录「核心」chiaroscuro 并列）
- 时期：文艺复兴至19世纪（15–16 世纪意大利文艺复兴，Leonardo da Vinci）
- 地区：欧洲
- 目标位置：理论 / 文艺复兴至19世纪 / 欧洲（该格现 12 条 3/8/1，属**新增覆盖**，非填空格）
- 来源一（维基，owiki 镜像）：https://owiki.org/wiki/Sfumato —《Sfumato ::: Open WIKI》— HTTP 200
  - 说明：维基 canonical `https://en.wikipedia.org/wiki/Sfumato` 本轮连接超时（URLError timed out），按任务许可用 owiki 镜像读取，仅计一源。
  - 正文关键句：「Sfumato is a painting technique for softening the transition between colours, mimicking an area beyond what the human eye is focusing on, or the out-of-focus plane.」
  - 正文关键句：「Leonardo da Vinci was the most prominent practitioner of sfumato, based on his research in optics and human vision, and his experimentation with the camera obscura.」
  - 正文关键句：「He described sfumato as "without lines or borders, in the manner of smoke".」
  - 正文关键句：「sfumato is one of four modes of painting colours available to Italian High Renaissance painters, along with cangiante, chiaroscuro, and unione.」
- 来源二（独立出版方，artincontext.org — 艺术教育独立出版，非维基；与本项目第 31 轮已采纳的 aic-academic 同一出版方）：https://artincontext.org/sfumato/ —《Sfumato - The History and Use of the Sfumato Technique》— HTTP 200
  - 正文关键句：「The sfumato technique is a Renaissance art method for easing color transitions and simulating an area other than what the human eye can see, also known as the out-of-focus plane.」
  - 正文关键句：「Leonardo da Vinci was perhaps the most notable developer of sfumato art.」
  - 正文关键句：「He pioneered it and used it in several of his paintings, including the famous sfumato examples: Virgin of the Rocks (1486) and his renowned Mona Lisa (1506) portrait.」
- 入选理由（关键：既往驳回原因已被本轮证据消解）：`research/gaps-external-round02.md` 第 41 行曾明确记录——「sfumato（渐隐法）…**虽属光影理论范围**，但仅 N2 一处明确列出，不列」，即第 02 轮判定其**属本领域（光影理论）但因只有单一来源而驳回**。本轮已实抓到**第二个独立出版方** artincontext.org 的同定义长文（HTTP 200，正文直证「Renaissance art method for easing color transitions…out-of-focus plane」「Leonardo…most notable developer」），**双独立源成立、驳回的技术障碍（单源）已消除**。故这是一条「新的、有权威依据」的缺口：概念本身早已在域内，缺的正是先前不可得的第二独立源，本轮补齐。
- 概念贴合度：高（一源为专门条目给出定义＋命名者＋「四模式之一」定位；另一源为独立艺术教育出版给出同一「缓和色阶过渡、模拟失焦面」定义与 Leonardo 代表作实例，独立互证）。
- 与既有条目区隔（逐一核对，均不等价）：
  - `chiaroscuro`（明暗法，核心）= 强**明暗对比**以塑造体积；维基正文明确把 sfumato 与 chiaroscuro 并列为 High Renaissance **四种色调模式之二**（"one of four modes…along with cangiante, chiaroscuro, and unione"），二者是并列的不同模式，非近义。
  - `light-shadow-modeling`（光影塑形）/ `five-tones`（明暗五调子）= 形体受光的**调子层次**；sfumato 专指**轮廓与色阶的柔化过渡/失焦感**，不是调子分级。
  - `tenebrism`（暗色调主义，补充）= 极端明暗、大面积暗部；与 sfumato 的「无界线、如烟」柔和过渡相反。
  - `aerial-perspective`（空气透视）= 远景因大气在**色彩与清晰度上退后**；sfumato 是**局部形体边缘的柔化技法/色调处理**，二者目的与手段不同（前者是空间纵深，后者是形体过渡）。
- 备注：本条为「新增覆盖」而非填稀疏格；建议层级「重要」。是否采纳及定级由 lead 裁决。

### 候选 2（建议纳入）：trompe-l'œil — 错视画 / 欺骗眼睛（Trompe-l'œil）

- 建议 id：`trompe-loeil`
- 中文名：错视画（欺骗眼睛 / 三维错觉画，Trompe-l'œil）
- 主题：理论（绘画错觉技法 / 空间错觉，横跨绘画与建筑空间）
- 层级：重要（建议；直接作用于「空间错觉」，与建筑空间设计强相关）
- 时期：文艺复兴至19世纪（15 世纪起，术语 1800 年确立）至跨时期
- 地区：欧洲（后及全球）
- 目标位置：理论 / 文艺复兴至19世纪 / 欧洲（现 12 条，属**新增覆盖**）
- 来源一（维基，owiki 镜像）：https://owiki.org/wiki/Trompe-l%27%C5%93il —《Trompe-l'œil ::: Open WIKI》— HTTP 200
  - 说明：维基 canonical 本轮连接超时，用 owiki 镜像读取，仅计一源。
  - 正文关键句：「Trompe-l'œil … is an artistic term for the highly realistic optical illusion of three-dimensional space and objects on a two-dimensional surface.」
  - 正文关键句：「Trompe-l'œil, which is most often associated with painting, tricks the viewer into perceiving painted objects or spaces as real.」
  - 正文关键句：「Forced perspective is a related illusion in architecture, and Op art a modern style mostly dealing with geometric patterns.」
- 来源二（独立出版方，artincontext.org）：https://artincontext.org/trompe-loeil/ —《Trompe l'Oeil - Trompe l'Oeil Painting Techniques With Examples》— HTTP 200
  - 正文关键句：「Trompe l'Oeil paintings use forced perspective to fool the observer into believing that painted objects or environments are real.」
  - 正文关键句：「Trompe l'Oeil art simulates three-dimensional environments and objects on a two-dimensional plane.」
- 来源三（独立出版方，Designing Buildings — 英国建筑行业知识库，与本项目第 40 轮 proxemics 第二源同源机构）：https://www.designingbuildings.co.uk/wiki/Trompe_l%27oeil —《Trompe l'oeil (part 2) - Designing Buildings》— HTTP 200
  - 正文关键句：「In architecture, trompe l'oeil … describes visual effects designed to intentionally create an optical illusion.」
  - 正文关键句：「Such techniques can be used to satisfy aesthetic requirements or address a design's limitations, (such as making a very small space appear less claustrophobic or, in interior decorating, painting a mural or applying wallpaper to give the viewer the impression of a window with a pleasant view.」
- 入选理由：一源（维基）定义为「在二维平面上对**三维空间与物体**的高度写实光学错觉」「使观者把画出的物体或**空间**当成真实」，并指出「forced perspective 是建筑中的相关错觉」；第二源（artincontext）给出同一「用 forced perspective 在二维平面模拟三维环境」的定义；第三源（Designing Buildings，独立建筑知识库）直接把 trompe l'œil 落在**建筑 / 室内空间**语境（「使很小的空间显得不那么局促」「室内装饰画壁画造出窗景」），与「建筑空间设计」直接互证。三源独立、均 200、均可摘正文关键句。该概念是「以写实错觉扩展/伪造感知空间」的专门技法与理论，直接服务空间设计。
- 概念贴合度：高（绘画技法定义由两源互证，建筑空间取向由独立建筑知识库另证）。
- 与既有条目区隔（均不等价）：
  - `spatial-perception`（空间感知）= 人对距离/方向/围合的**知觉判断**机制；trompe-l'œil 是**制造空间错觉的表现技法**，非知觉理论。
  - `space-definition`（建筑空间定义）/ `enclosure`（围合）= 实体界面的空间界定；trompe-l'œil 用**二维假象**伪造/扩展空间感知，属表现层技法。
  - `quadratura`（若论天花错觉画）——本轮 owiki 仅单源、无第二独立源，未纳入；trompe-l'œil 为其上位通名。
- 备注：本条为「新增覆盖」，建议层级「重要」。是否采纳及定级由 lead 裁决。

### 已对照但未纳入（体现筛选，均说明为何不满足「≥2 独立源 + 属本领域 + 非近义」）

- **picturesque（如画）/ sublime（崇高）**：在 `English_landscape_garden`、`Landscape_painting`、`Aesthetics` 三份大纲中均出现（属本领域美学/景观理论），但本轮**第二独立权威源无一可达**——Britannica HTTP 403（/art/picturesque）、Tate DNS 解析失败（getaddrinfo fail）、Encyclopedia.com 连接超时、infoplease HTTP 403、Designing Buildings 无 `Picturesque` / `The_Picturesque` slug（均 404）。按任务「只在有完整双源 URL 证据时才报」的规则，**不列为本轮候选**，留待后续补齐第二源。
- **fresco（湿壁画）**：双独立源可达（owiki `Fresco` HTTP 200 ＋ Designing Buildings `Fresco` HTTP 200），但属**壁画工艺 / 材料技法**，与本项目「绘画理论」核心（明暗/色彩/构图/透视/空间原理）贴合度弱于 sfumato / trompe-l'œil；列作「可议备选」，非本轮主推。
- **cangiante / unione**：Leonardo 另两种色调模式，owiki 各 HTTP 200，但**仅单源、无第二独立源**；且 sfumato 正文已将其列为并列模式，颗粒度更细、可并入 sfumato 正文，不单独立条。
- **impasto（厚涂）、notan（浓淡/明暗设计）、wabi-sabi（侘寂）、ma（间 / 负空间）、quadratura（错觉天花画）**：owiki 均 HTTP 200，但（a）impasto / quadratura 无第二独立源（artincontext `/impasto/` 404、Designing Buildings `Impasto` 404）；（b）ma 与既有 `negative-space` / `liubai`、notan 与既有 `value` / `chiaroscuro` 近义，触犯「排除近义已收录」；（c）wabi-sabi 属日本美学世界观，与 `yijing`（意境）等概念叠加后颗粒度边界不清、且无第二独立源。均不纳入。
- **Western painting / History of painting / List of art movements 中的绘画流派史**（印象派、立体主义、表现主义、野兽派等）：按 TASK_design 口径「风格＝主要建筑风格史」，**绘画流派史不在本项目风格范围**（与 `research/gaps-external-round02.md`、`b1-round40.md` 既有排除口径一致），不产出风格条目。
- **Design history / Glossary of architecture / Index of architecture articles**：为「设计史总述 / 术语表 / A–Z 条目索引」，其列项或已收录、或为近义、或仅单源，除上述两候选外未再产出满足双源的新概念。

### B1 结论

**有。** 本轮对照 8 份未用过的权威大纲/分类树，确认 **2 条**满足全部判据（≥2 独立权威源 HTTP 200 + 属本领域 + scope 缺失 + 非近义）的新候选：

1. **`sfumato`（渐隐法）** —— 第 02 轮已判定「属光影理论范围」、但因**单源**驳回；本轮补齐第二独立源 artincontext.org，**单源障碍消除，双源成立**，为最扎实的「新权威缺口」。
2. **`trompe-l'œil`（错视画）** —— 绘画↔建筑空间错觉技法，三源（owiki ＋ artincontext ＋ Designing Buildings）互证，scope 无对应。

picturesque / sublime 虽属本领域美学理论，但第二独立源本轮不可达（403 / DNS / 超时 / 404），按规则不列为候选。

---

## B6：近 12 个月（2025-11 至 2026-11）与绘画理论/建筑空间设计直接相关的理论性新研究/事件

来源页面（均 owiki 实抓 HTTP 200，标题核对）：
- https://owiki.org/wiki/2025_in_architecture —《2025 in architecture ::: Open WIKI》200
- https://owiki.org/wiki/2026_in_architecture —《2026 in architecture ::: Open WIKI》200
- https://owiki.org/wiki/2025_in_art —《2025 in art ::: Open WIKI》200
- https://owiki.org/wiki/2026_in_art —《2026 in art ::: Open WIKI》200

保守原则：仅保留能核对到日期/来源 URL、且能明确说明对本项目具体条目产生「新增或更新」理论性影响的条目。窗口 [2025-11, 2026-11] 内实际出现的事项性质如下：

- 2025-11-03：罗马中世纪 Torre dei Conti 修缮中局部坍塌（建成遗产维护议题）——建筑事故，与具体理论/原理条目无直接对应（与历轮同口径排除）。
- 2025-11-18：Gustav Klimt《Portrait of Elisabeth Lederer》以 2.384 亿美元成交（现代艺术拍卖纪录）——绘画市场/拍卖事件，非绘画理论进展。
- 2025 Pritzker 奖授予刘家琨（Liu Jiakun）；2025 AIA 金质奖授予 Deborah Berke；2025 Stirling 奖授予 London Southwark 的 Appleby Blue Almshouse——均为**奖项事件**，属实例/语境，不改变任何理论条目定义；Pritzker 2025 已见于更早 B6 记录。
- 2025_in_architecture 其余为建筑开馆（Techo 国际机场 2025-09-09、Kai Tak Sports Park 2025-03-01、Tottori 县立美术馆 2025-03-30、Universal Epic Universe 2025-05-22 等）与讣告；2026_in_architecture 内容稀疏，仅列 4 个建筑（Appleby Blue Almshouse、Las Chumberas 教堂社区中心、520 Fifth Avenue、米兰奥运村）与讣告；2026_in_art 仅讣告、无理论事件（页面尾部「Books/Films/Programming Languages…」排行榜为 owiki 镜像在每页注入的**站点样板**，非词条正文，不计入）。
- 更早已在 `research/gaps-external-round02.md` 记录的 3 条「实例/语境更新」仍是唯一可用候选（Guggenheim Abu Dhabi 预计 2026-12 开馆、Lucas Museum 2026-09-22 开馆、Pritzker 2025 刘家琨），本轮**未出现需要据此新增/更新条目的理论性新动态**。

### B6 结论

**B6 未发现新的可核验动态。** 近 12 个月内检索到的均为奖项、讣告、建筑开馆、拍卖与建筑事故，均不构成对「绘画理论 / 建筑空间设计」条目的理论性新增或更新；已记录的 3 条实例/语境候选维持不变，本轮无需据此改动 scope 或条目。

---

## 本轮实际打开的 URL 与 HTTP 状态

### 对照用大纲/分类树（owiki 镜像，均未在往轮 B1 使用）
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/Outline_of_the_visual_arts | Outline of the visual arts ::: Open WIKI | 200 |
| https://owiki.org/wiki/Western_painting | Western painting ::: Open WIKI | 200 |
| https://owiki.org/wiki/Landscape_painting | Landscape painting ::: Open WIKI | 200 |
| https://owiki.org/wiki/English_landscape_garden | English landscape garden ::: Open WIKI | 200 |
| https://owiki.org/wiki/Design_history | Design history ::: Open WIKI | 200 |
| https://owiki.org/wiki/Glossary_of_architecture | Glossary of architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/Index_of_architecture_articles | Index of architecture articles ::: Open WIKI | 200 |
| https://owiki.org/wiki/Aesthetics | Aesthetics ::: Open WIKI | 200 |

### 候选证据
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/Sfumato | Sfumato ::: Open WIKI | 200 |
| https://artincontext.org/sfumato/ | Sfumato - The History and Use of the Sfumato Technique | 200 |
| https://owiki.org/wiki/Trompe-l%27%C5%93il | Trompe-l'œil ::: Open WIKI | 200 |
| https://artincontext.org/trompe-loeil/ | Trompe l'Oeil - Trompe l'Oeil Painting Techniques With Examples | 200 |
| https://www.designingbuildings.co.uk/wiki/Trompe_l%27oeil | Trompe l'oeil (part 2) - Designing Buildings | 200 |

### B6 来源
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/2025_in_architecture | 2025 in architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/2026_in_architecture | 2026 in architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/2025_in_art | 2025 in art ::: Open WIKI | 200 |
| https://owiki.org/wiki/2026_in_art | 2026 in art ::: Open WIKI | 200 |

### 附加探测（评估「近义 / 双源可达性 / 超域」用，均实际打开）
| URL | 结果 | 用途 |
| --- | --- | --- |
| https://owiki.org/wiki/Impasto | 200 | 单源、无第二源，弃 |
| https://owiki.org/wiki/Notan | 200 | 近义 value/chiaroscuro，弃 |
| https://owiki.org/wiki/Wabi-sabi | 200 | 单源、域边界不清，弃 |
| https://owiki.org/wiki/Ma_(negative_space) | 200 | 近义 negative-space/liubai，弃 |
| https://owiki.org/wiki/Quadratura | 200（重定向 Illusionistic ceiling painting） | 单源，弃 |
| https://owiki.org/wiki/Cangiante | 200 | 单源，并入 sfumato 正文，不单列 |
| https://owiki.org/wiki/Fresco | 200 | 双源可达但技法偏材料，备选 |
| https://www.designingbuildings.co.uk/wiki/Fresco | 200（Fresco - Designing Buildings） | fresco 第二源（备选） |
| https://owiki.org/wiki/Picturesque | 200 | 缺第二源，弃 |
| https://owiki.org/wiki/Sublime_(philosophy) | 200 | 缺第二源，弃 |
| https://owiki.org/wiki/Garden_design | 200 | 景观方向核对（S12 旧源，不计新大纲） |

### 失败/不可用（审计用，第二源探索）
| URL | 结果 | 备注 |
| --- | --- | --- |
| https://en.wikipedia.org/wiki/Sfumato · /Trompe-l%27%C5%93il · /Outline_of_the_visual_arts | URLError timed out | 维基 canonical 超时，改用 owiki 镜像（同源计一源） |
| https://www.britannica.com/art/sfumato · /trompe-loeil · /picturesque | HTTP 403 | Britannica 本轮全部 403 |
| https://www.tate.org.uk/art/art-terms/s/sfumato 等 3 条 | getaddrinfo fail | Tate DNS 不可达 |
| https://www.nationalgallery.org.uk/paintings/glossary/sfumato | getaddrinfo fail | DNS 不可达 |
| https://www.visual-arts-cork.com/painting-techniques.htm | 连接被拒 10061 | 弃用 |
| https://www.encyclopedia.com/…/sfumato · /…/picturesque | URLError timed out | 超时 |
| https://www.metmuseum.org/toah/hd/sfum/hd_sfum.htm | URLError timed out | 超时 |
| https://www.oxfordreference.com/display/… | HTTP 302 | 跳转，未取正文 |
| https://www.designingbuildings.co.uk/wiki/Picturesque · /Sfumato · /Trompe-l%27oeil(初探) · /Picturesque_landscape · /The_picturesque · /Trompe_loeils · /Impasto | HTTP 404 | slug 不存在 |
| https://artincontext.org/picturesque/ · /impasto/ · https://www.theartstory.org/definition/sfumato/ · https://www.infoplease.com/…/picturesque | HTTP 404 / 403 | 无对应专页 |

### 打开 URL 计数
- 本轮实际发起 HTTP 请求 **69 次**；HTTP 200 成功 **43 次**；失败 **26 次**（en.wikipedia 超时 3、Britannica 403 3、Tate/DNS 3、NationalGallery DNS 1、Visual-Arts-Cork 拒连 1、Encyclopedia 超时 2、Met 超时 1、Oxford 302 1、DB/artincontext/theartstory/infoplease 404·403 11）。
- 作为来源实际读取正文的核心证据页面：sfumato 2 个（owiki + artincontext）、trompe-l'œil 3 个（owiki + artincontext + Designing Buildings）；对照大纲 8 个；B6 4 个；附加探测 11 个。

---

## 机器可读汇总

```
CANDIDATES=[
 {"id":"sfumato","title":"渐隐法（晕涂法，Sfumato）","theme":"理论","tier":"重要","period":"文艺复兴至19世纪","region":"欧洲","urls":["https://owiki.org/wiki/Sfumato","https://artincontext.org/sfumato/"],"sources":["w-owiki-sfumato","aic-sfumato"],"note":"round02 曾以单源驳回，本轮补齐第二独立源"},
 {"id":"trompe-loeil","title":"错视画（欺骗眼睛，Trompe-l'œil）","theme":"理论","tier":"重要","period":"文艺复兴至19世纪","region":"欧洲","urls":["https://owiki.org/wiki/Trompe-l%27%C5%93il","https://artincontext.org/trompe-loeil/","https://www.designingbuildings.co.uk/wiki/Trompe_l%27oeil"],"sources":["w-owiki-trompe","aic-trompe","dbb-trompe"],"note":"绘画↔建筑空间错觉，三源互证"}
]
REJECTED=["picturesque(缺第二独立源403/DNS/超时/404)","sublime(缺第二独立源)","fresco(双源可达但技法偏材料/非理论核心)","cangiante/unione(单源,并入sfumato)","impasto/quadratura(单源)","notan(近义value/chiaroscuro)","wabi-sabi(单源/域边界不清)","ma(近义negative-space/liubai)","painting-movements(风格限建筑,超域)"]
B6_NEW=[]
B1_RESULT="有：2 条新双源缺口候选（sfumato、trompe-l'œil）"
B6_RESULT="未发现新的可核验动态"
URLS_REQUESTED=69
URLS_OK_200=43
URLS_FAILED=26
```

是否发现新缺口：是
