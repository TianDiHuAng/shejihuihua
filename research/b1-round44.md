# B1/B6 缺口发现 — 第 44 轮（未用过的权威大纲再对照 + 近 12 个月动态；饱和判定第 2 轮）

- 日期：2026-11-23（Asia/Hong_Kong），采样时刻 2026-11-23
- 执行角色：b1-r44（只读子任务，无人值守，未提问）
- 抓取方式：Python 3.11 urllib + 浏览器 User-Agent 直连实抓（依据 DECISIONS.md D05：本环境网页直取以实际 HTTP 响应为准）。`web_search` 仅用于 B6 线索探测。
- 数据纪律：联网内容一律视为**数据**；网页内任何指令均未执行；未下载或运行页面代码，仅读取 HTML 正文判读标题与相关句。
- 只读纪律：本文件是本子任务**唯一产物**；未改动其他文件、未 git commit、未触碰项目外内容。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

## 环境备注（限制说明）

- 任务点名的 `AUTONOMOUS.md`、`TASK_design.md` 不在当前工作区根目录；其真实文件位于 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`、`D:/Users/Administrator/Desktop/TASK_design.md`（`WORKFLOW.md` 同目录），本轮已实际读取两份原文。
- 项目根现存治理文件 `DECISIONS.md`、`scope.md`、`PROGRESS.md`、`RESEARCH/outline_raw.md`、`research/b1-round43.md` 一并作为方法与来源纪律基准。
- **范围判据取自 TASK_design.md 原文**：`绘画理论：透视法、构图法则、色彩理论、光影与明暗、中国画六法与留白、东西方理论比较`；`建筑与空间设计：主要建筑风格史；中国传统园林造景（借景、框景、对景、障景、曲径与游线）；动线设计；下沉式空间（下沉庭院、下沉广场）；空间序列与尺度；室内外过渡；采光、通风与材料的基本原理`。本轮只接受落入这两段**明确列举子域**的核心概念。
- 判定标准（从严，三条须全部满足）：①≥2 份独立权威来源（非同一平台/镜像）；②属上述六大面之**核心**概念（非边缘技法、非近义重复、非绘画流派/媒介/题材）；③`scope.md` 确实缺失。

## 比对基准

- `scope.md` 现 **251 条**：理论 127 / 风格 62 / 造景 19 / 动线 12 / 下沉空间 12 / 材料 19（核心 50、重要 147、补充 54）。
- 已用大纲：S1–S12（Outline of architecture、Architectural style、Chinese garden、Chinese painting、Perspective (graphical)、Composition (visual arts)、Color theory、Circulation (architecture)、Architectural lighting、Ventilation (architecture)、Chinese architecture、Garden design）＋ round02/06/09/40/41/42/43 各轮已用页面（详见 `research/outline_raw.md`、`gaps-external-round*.md`、`b1-round40~43.md`）。
- 第 42 轮已纳入 `hatching`（排线法）、`stippling`（点描法）；第 43 轮从严判定 0 新缺口。本轮**不得重复**上述条目与 round40~43 已用页面。
- 已逐条在 `entries/`、`scope.md`、`coverage.json`、`data/sources.json`、`research/` 中 grep 核对：本轮 9 份大纲页 slug 在 `research/` 命中 **0**（见文末机器可读汇总 `B1_ALL_UNUSED_CONFIRMED=true`），确认「此前从未用于本项目任一轮」。

---

## B1：与「未用过」的权威大纲/分类树再对照

本轮对照下列 **9 份此前从未用于本项目任一轮**的权威百科大纲/分类树/学科总述页面（文件级 grep `research/` 命中 0 次；均 owiki 镜像实抓 HTTP 200）。「≥3 份未用过」要求已远超满足。

| # | 大纲/分类树（未用） | URL | HTTP | 覆盖方向 |
| --- | --- | --- | --- | --- |
| 1 | Mathematics and architecture（建筑与数学，学科总述） | https://owiki.org/wiki/Mathematics_and_architecture | 200 | 空间原理 / 比例 / 几何 |
| 2 | Architectural technology（建筑技术，学科总述） | https://owiki.org/wiki/Architectural_technology | 200 | 材料 / 构造 / 建筑科学 |
| 3 | Walkability（步行适宜性，城市规划概念树） | https://owiki.org/wiki/Walkability | 200 | 动线 / 人行流线 |
| 4 | Public space（公共空间，概念总述） | https://owiki.org/wiki/Public_space | 200 | 空间 / 广场 / 动线 |
| 5 | Natural building（自然建筑，材料分类树） | https://owiki.org/wiki/Natural_building | 200 | 材料 / 通风 / 可持续 |
| 6 | Timeline of architectural styles（建筑风格时间轴） | https://owiki.org/wiki/Timeline_of_architectural_styles | 200 | 风格（越域/细粒度核对） |
| 7 | Underground living（地下/覆土居住，类型总述） | https://owiki.org/wiki/Underground_living | 200 | 下沉空间 |
| 8 | Fine art（美术，艺术门类总述） | https://owiki.org/wiki/Fine_art | 200 | 绘画理论（门类越域核对） |
| 9 | Art criticism（艺术批评，方法论总述） | https://owiki.org/wiki/Art_criticism | 200 | 绘画理论（方法论越域核对） |

> 覆盖说明：绘画理论（Fine art、Art criticism，越域/方法论核对）、风格（Timeline of architectural styles）、材料（Architectural technology、Natural building）、动线（Walkability、Public space）、下沉空间（Underground living）、空间原理（Mathematics and architecture）六大面均有一份或多份未用大纲实抓对照。全部为 owiki 镜像单一平台，故均**不计第二独立源**；本轮无候选，不涉第二源判定。

### 逐份大纲提取与「未纳入」理由

**#1 Mathematics and architecture（200，55.7KB）** — 建筑借数学：用几何定义空间形态；自公元前 6 世纪毕达哥拉斯学派起以比例营造和谐；埃及/希腊/印度/伊斯兰宗教性比例；用数学对象（镶嵌 tessellation）装饰；伊斯兰几何纹样、印度神庙分形结构；文艺复兴强调对称与比例（Alberti、Serlio、Palladio，承 Vitruvius《De architectura》与毕氏算术）；19 世纪双曲面结构（Shukhov、Gaudí：双曲抛物面、悬链拱、螺旋面、直纹面）；20 世纪现代/解构几何；测地线穹顶（Fuller）、极小曲面（丹佛机场）、薄壳。
- 未纳入理由：`proportion`（比例，核心）、`golden-ratio`（黄金分割）、`geometry-symmetry`（几何与对称）、`parametric-architecture`（参数化建筑）**已收录**；`tessellation` 属**建筑装饰**，双曲面/悬链拱/测地穹顶/极小曲面/薄壳属**结构工程与几何装饰的边缘技法**，非「空间原理/构图」核心概念；宗教比例属历史例证。→ **不构成核心缺口**。

**#2 Architectural technology（200，15.2KB）** — 建筑技术（building technology）= 把技术应用于建筑设计；是建筑学与建筑工程的分支，与建筑科学（building science）紧密相关；处理建筑各要素及其相互作用；Vitruvius 对建筑类型/风格/材料/建造方法的分类为其基础；材料史为砖、石、木、钢（结构）、板岩与瓦（屋面）、铅/铜（防水）、1849 钢筋混凝土；现代墙体/楼板/屋面分层含结构、保温、防水；涉及法规与标准。
- 未纳入理由：属**学科/职业层面总述**；材料与构造列举（brick/stone/timber/steel/concrete/insulation/waterproofing）**近义**于 `structural-material`（结构材料）、`material-durability`（材料耐久）、`damp-proofing`（防潮）、`transparent-material`（透明材料）；「建筑技术/建筑科学」为交叉学科，非六大面核心概念。→ **不构成核心缺口**（学科层/近义）。

**#3 Walkability（200，33.2KB）** — 城市规划概念：步行合理距离内可达设施；城市空间应宜居而非仅为机动车通道；新城市主义第一原则；1960s 简·雅各布斯；影响因素：人行道/步道/行人路权、交通与道路状况、土地利用、建筑可达性、安全；五个城市设计品质：imageability（意象性）、enclosure（围合）、human scale（人体尺度）、transparency（透明性）、complexity（复杂性）；urban DMA（密度/混合/可达网络）；permeability、connectivity；walk score。
- 未纳入理由：本质为**城市步行适宜性评价指标**，与已收录 `pedestrian-flow`（人行流线，核心）、`circulation`（动线，核心）**近义**；五个 urban design qualities 属**评价维度**（`human-scale`、`enclosure`、`interface-permeability` 已有对应条目）；属城市规划层面，非「动线设计」新增核心。→ **不构成核心缺口**（近义/边缘）。

**#4 Public space（200，29.4KB）** — 向公众开放可达的场所：道路、人行道、公共广场、公园、海滩；部分政府建筑；shared space（共享街道）；作为民主/集会空间（含法学、社会学维度）；私有化；semi-public spaces；英国/美国定义；design theory / urban design 中的公共空间。
- 未纳入理由：城市公共空间/公共领域概念（含社会学、法学维度），与已收录 `plaza`（广场，造景）、`openness`/`boundary`/`enclosure`（空间原理）、`node-path`（节点与路径）**近义/域外**；「semi-public space」「privatization」属城市社会学，非六大面核心。→ **不构成核心缺口**（近义/域外）。

**#5 Natural building（200，27.6KB）** — 生态建筑，属绿色建筑/可持续建筑/生态设计；用本地天然材料：黏土+砂→cob/adobe；土、木、秸秆、稻壳、竹、石；earthbag、hempcrete、cordwood、timber frame、straw bale、rammed earth；通过设计实现自然通风；朝向/气候/场地；低隐含能耗；避免硅酸盐水泥/钢/VOC。
- 未纳入理由：与已收录 `vernacular-material`（乡土材料，含 adobe/rammed earth）、`sustainable-design`/`green-architecture`/`sustainable-architecture`、`natural-ventilation`（自然通风）**近义/已覆盖**；具体工艺（cob/earthbag/hempcrete/cordwood/straw bale）为**材料工艺品类级边缘细节**。→ **不构成核心缺口**（近义/边缘）。

**#6 Timeline of architectural styles（200，60.1KB）** — 6000 BC–present 建筑风格年代时间轴；条形含 Western Chalukya、Maru-Gurjara、Song、Ottonian、Fatimid、Chimor、Chola、Norse、Angkorian、Muisca、Aghlabid、Shinden-zukuri、Carolingian、Rashtrakuta、Pueblo、Abbasid、Moorish、Asturian、Nara、Umayyad、Tang 等。
- 未纳入理由：为**风格年代时间轴**；核心/主要风格（Romanesque/Gothic/Renaissance/Baroque/Neoclassical/Modern/Bauhaus…）已在 62 条风格面；所列 Western Chalukya/Maru-Gurjara/Chola/Angkorian/Pueblo/Muisca/Aghlabid 等为**地域/王朝细粒度风格**，属边缘，且单一来源（时间轴页）**不满足「≥2 独立权威源」新增门槛**；Mughal 等已由 `indian-architecture`/`islamic-architecture` 伞条目覆盖。→ **不构成核心缺口**（细粒度/边缘/单源）。

**#7 Underground living（200，19.3KB）** — 地下居住；洞穴或人造结构；优点：抗恶劣天气、安静、不显眼、近乎恒温（土壤隔热）、节能环保；缺点：可能积水需泵排；实例 Sassi di Matera、Coober Pedy、Matmata、南极点站；依山而建常一侧外露（改善采光）；历史；建造法（高位烟囱+低位入口形成持续气流）；城市地下空间（UUS）可持续发展。
- 未纳入理由：与已收录 `earth-sheltered`（覆土建筑）、`semi-sunken-space`（半下沉空间）、`sunken-courtyard`/`sunken-plaza`/`sunken-garden`、`damp-proofing`/`drainage`/`safety-guarding` **近义/已覆盖**；积水泵排、烟囱气流为**下沉空间已知常见问题与被动通风细节**；UUS 城市地下空间开发属城市尺度边缘。→ **不构成核心缺口**（近义/边缘）。

**#8 Fine art（200，42.3KB）** — 美术主要为审美/创作表达，区别于流行/装饰/实用艺术；历史上五大美术为绘画、雕塑、建筑、音乐、诗歌；流派/题材等级（history painting 高于 still life）；视觉艺术；版画/素描为绘画相关形式；现代含电影/摄影/录像。
- 未纳入理由：为**综合艺术门类划分**（含 music/poetry/theatre/dance），**越出**本项目「绘画理论 / 建筑」两域；genre 等级（history painting/still life）属**题材门类**（round43 已按「题材门类非六子域」排除）；与已收录 `academic-art-theory` 及 outline `Aesthetics`（round41）无新增核心。→ **不构成核心缺口**（越域/题材门类）。

**#9 Art criticism（200，33.9KB）** — 对视觉艺术的讨论/评价；以美学或美的理论为语境；历史批评 vs 当代批评；方法论/理论：aesthetic、pragmatic、expressive、formalist、relativist、imitation、ritual、cognition、mimetic、postmodern；依设计元素与原则做形式分析。
- 未纳入理由：属**艺术批评方法论/艺术史**（formalism、iconography 已在 round42 判边缘）；与已收录 `academic-art-theory`、outline `Aesthetics`（round41）相关但**非六大面核心概念**；评价方法论属边缘。→ **不构成核心缺口**（边缘/方法论）。

### 候选概念逐条「未纳入」汇总表

| 候选（来自本轮大纲） | 归属面 | 未纳入理由 |
| --- | --- | --- |
| 比例/和谐/对称（毕氏、Alberti、Palladio） | 空间原理 | 已收录 proportion、golden-ratio、geometry-symmetry |
| tessellation / 双曲面 / 悬链拱 / 测地穹顶 / 薄壳 | 空间原理 | 建筑装饰与结构工程**边缘技法/工程细节** |
| 建筑技术/建筑科学（brick/stone/timber/steel/concrete/insulation/waterproofing） | 材料 | **学科层/近义** structural-material、material-durability、damp-proofing、transparent-material |
| walkability（步行适宜性、五个 urban design qualities） | 动线 | **近义** pedestrian-flow、circulation；评价维度（human-scale/enclosure/permeability 已有条目） |
| public space / shared space / semi-public / privatization | 空间/动线 | **近义/域外** plaza、openness、boundary、node-path；城市社会学维度 |
| natural building（cob/adobe/earthbag/hempcrete/cordwood/straw bale） | 材料/通风 | 近义 vernacular-material、sustainable-design、green/sustainable-architecture、natural-ventilation；品类级边缘 |
| Western Chalukya/Chola/Angkorian/Pueblo/Muisca/Aghlabid… | 风格 | **细粒度地域/王朝风格**、边缘且单源（时间轴）；核心风格已在 62 条 |
| underground living（恒温/积水泵排/烟囱气流/UUS） | 下沉空间 | **近义/已覆盖** earth-sheltered、semi-sunken、sunken-*、damp-proofing、drainage |
| fine art（五大美术含 music/poetry；genre 等级） | 绘画理论 | **越域**（综合艺术门类）+ **题材门类**（round43 已排除） |
| art criticism（formalism/iconography/mimetic 等） | 绘画理论 | **方法论/艺术史**，边缘；非六子域核心 |

### B1 结论

**不构成新的核心缺口。** 本轮以 **9 份此前从未使用**的权威大纲/分类树（Mathematics and architecture、Architectural technology、Walkability、Public space、Natural building、Timeline of architectural styles、Underground living、Fine art、Art criticism，均 owiki 实抓 HTTP 200，`research/` grep 命中 0）逐页对照 251 条。所提取的候选概念全部落入以下任一情形：**（a）越出六大面**（fine art 综合艺术门类、art criticism 方法论、public space 城市社会学）；**（b）近义已收录**（walkability↔pedestrian-flow/circulation；natural building↔vernacular-material/sustainable；underground living↔earth-sheltered/sunken-*；建筑技术材料↔structural-material）；或 **（c）边缘技法/细粒度/单源**（tessellation/双曲面/薄壳；地域/王朝细分风格仅时间轴一源；cob/earthbag 等工艺品类）。无一条同时满足「≥2 独立权威源 + 六大面核心概念 + scope 缺失」的严格判据。故 B1 计 **0 条新核心缺口**。

---

## B6：近 12 个月（2025-11 至 2026-11）与绘画理论/建筑空间设计直接相关的理论性新研究/事件

结构化来源页面（均 owiki 实抓 HTTP 200）：
- https://owiki.org/wiki/2025_in_architecture —《2025 in architecture ::: Open WIKI》200
- https://owiki.org/wiki/2026_in_architecture —《2026 in architecture ::: Open WIKI》200
- https://owiki.org/wiki/2025_in_art —《2025 in art ::: Open WIKI》200
- https://owiki.org/wiki/2026_in_art —《2026 in art ::: Open WIKI》200
- 补充线索：`web_search` 3 组查询（2025–2026 建筑/绘画理论新著与进展），返回 10 条结果（见下方清单，仅作线索，未逐一抓取正文）。

保守原则：仅保留能核对到日期/来源、且能明确说明对本项目具体条目产生「新增或更新」**理论性**影响者。窗口内实际事项性质如下（均**非**理论进展）：
- 2025 in architecture：2025-01-07 起南加州山火毁多座建筑、2025-03-16 Valkenburg Wilhelminatoren 坍塌、2025-11-03 罗马 Torre dei Conti 修缮中局部坍塌（1 死）——**建成遗产维护/事故**；2025 奖项（Pritzker 刘家琨、AIA 金质奖 Deborah Berke、Stirling 奖 Appleby Blue Almshouse）；多地建筑开馆；讣告——**奖项/开馆/讣告**，均不改变任何理论条目定义。
- 2026 in architecture：页面极稀疏（约 2KB），仅列 building 名单与讣告（Hiroshi Nakamura、Murad Hasratyan、Liu Thai Ker 等）——**无理论条目**；尾部 Books/Films/… 为 owiki 镜像每页注入的**站点样板**，非词条正文，不计入。
- 2025 in art：艺博会档期（Art Basel / Frieze / TEFAF 等）、2025-09-25 Bristol 博物馆 600+ 文物被盗、2025-10-19 卢浮宫 Galerie d'Apollon 法国王冠珠宝被盗、2025-03「Rembrandt 海景画被盗」经证实为拍片摆拍、Joan Mitchell 捐赠、2026 威尼斯双年展 Koyo Kouoh 遗愿推进——**展览/市场/安防事件**，非理论。
- 2026 in art：仅讣告（Molly Parkin、Hiroshi Nakamura）——**无理论条目**。
- `web_search` 新著/论文线索（2025–2026，均**当代理论思潮/专著/期刊论文**，非六大面核心概念的定义性变更）：In Fourth Nature Concept, Form Follows Spirit（Prochnow, 2026, [REAL CORP](https://repository.corp.at/1356)）、The Stoic Baroque（Brepols, 艺术理论丛书, [链接](https://www.brepols.net/products/IS-9782503602554-1)）、Architecture as Design Cognition（Khōrein 期刊, [链接](https://khorein.ifdt.bg.ac.rs/index.php/ch/article/view/127)）、Palimpsest Temporality design framework（[Scienmag](https://scienmag.com/palimpsest-temporality-offers-new-design-framework-for-regenerating-aging-buildings/)）、Beyond participation: form-based adaptability（Emerald ARCH, 2026, [链接](https://www.emerald.com/arch/article-abstract/doi/10.1108/ARCH-11-2025-0504/1362518/Beyond-participation-architecting-the-unknown)）、From systemic transformation to regenerative futures（T&F, 2026, [链接](https://www.tandfonline.com/doi/abs/10.1080/14606925.2026.2706313)）、Architects and machines creative partners（[Scienmag](https://scienmag.com/architects-and-machines-are-becoming-creative-partners-not-rivals/)）、BIOARCHITECTURE（[Liedtke Museum](https://liedtke-museum.com/index.php?Itemid=2759&id=982&lang=en&option=com_content&view=article)）、《论绘画之非客体》朱利安中译（[澎湃](https://thepaper.cn/newsDetail_forward_34156817)）、福柯论画（[百度百科](https://baike.baidu.com/item/%E7%A6%8F%E6%9F%AF%E8%AE%BA%E7%94%BB/67717778)）。上述为**话语/专著/论文层面**，均为**单一出版方或单篇**，未提出需据以新增或改写本 scope 任一核心条目（透视/构图/色彩/光影/中国画/建筑风格史/园林造景/动线/下沉/材料/空间原理）的**规范性理论变更**。

### B6 结论

**B6 未发现需要更新条目的理论性新研究/事件。** 近 12 个月内可核验事项均为事故、奖项、开馆、讣告、拍卖/盗窃与当代理论专著/期刊思潮；无一构成对「绘画理论 / 建筑空间设计」**核心条目**的理论性新增或更新。已载于 `research/gaps-external-round02.md` 的 3 条实例/语境候选（Guggenheim Abu Dhabi 预计 2026-12 开馆、Lucas Museum 2026-09-22 开馆、Pritzker 2025 刘家琨）维持不变，本轮无需据此改动 scope 或条目。

---

## 本轮实际打开的 URL 与 HTTP 状态

### 对照用大纲/分类树（owiki 镜像，均未在往轮使用；文件级 grep research/ 命中 0）
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/Mathematics_and_architecture | Mathematics and architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/Architectural_technology | Architectural technology ::: Open WIKI | 200 |
| https://owiki.org/wiki/Walkability | Walkability ::: Open WIKI | 200 |
| https://owiki.org/wiki/Public_space | Public space ::: Open WIKI | 200 |
| https://owiki.org/wiki/Natural_building | Natural building ::: Open WIKI | 200 |
| https://owiki.org/wiki/Timeline_of_architectural_styles | Timeline of architectural styles ::: Open WIKI | 200 |
| https://owiki.org/wiki/Underground_living | Underground living ::: Open WIKI | 200 |
| https://owiki.org/wiki/Fine_art | Fine art ::: Open WIKI | 200 |
| https://owiki.org/wiki/Art_criticism | Art criticism ::: Open WIKI | 200 |

### B6 来源
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/2025_in_architecture | 2025 in architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/2026_in_architecture | 2026 in architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/2025_in_art | 2025 in art ::: Open WIKI | 200 |
| https://owiki.org/wiki/2026_in_art | 2026 in art ::: Open WIKI | 200 |

### 失败/不可用
- 无（本轮全部 HTTP 200，无 403/404/超时）。

### web_search 线索（B6；返回摘要，未逐一抓正文，不计入「打开 URL」）
- https://repository.corp.at/1356
- https://www.brepols.net/products/IS-9782503602554-1
- https://khorein.ifdt.bg.ac.rs/index.php/ch/article/view/127
- https://scienmag.com/palimpsest-temporality-offers-new-design-framework-for-regenerating-aging-buildings/
- https://www.emerald.com/arch/article-abstract/doi/10.1108/ARCH-11-2025-0504/1362518/Beyond-participation-architecting-the-unknown
- https://www.tandfonline.com/doi/abs/10.1080/14606925.2026.2706313
- https://scienmag.com/architects-and-machines-are-becoming-creative-partners-not-rivals/
- https://liedtke-museum.com/index.php?Itemid=2759&id=982&lang=en&option=com_content&view=article
- https://thepaper.cn/newsDetail_forward_34156817
- https://baike.baidu.com/item/%E7%A6%8F%E6%9F%AF%E8%AE%BA%E7%94%BB/67717778

### 打开 URL 计数
- 本轮实际发起 HTTP 请求 **31 次**（含同页重复抓取以提取不同结构：标题/段落/列表）；**去重后 14 个不同 URL**；**全部 HTTP 200（0 失败）**。
  - 其中 B1 对照核心大纲页 **9 个**（均 200）；B6 结构化年报页 **4 个**（均 200）；连通性/结构确认另测 `Outline_of_architecture` 1 个（200，往轮已用，仅计数不去重为「新大纲」）。
- `web_search` 另发起查询 **3 组**（返回 10 条线索，非 HTTP 正文抓取）。

---

## 机器可读汇总

```
ROUND=44
SCOPE_TOTAL=251   # 理论127/风格62/造景19/动线12/下沉12/材料19
B1_OUTLINES_UNUSED=9   #[Mathematics_and_architecture,Architectural_technology,Walkability,Public_space,Natural_building,Timeline_of_architectural_styles,Underground_living,Fine_art,Art_criticism]
B1_ALL_UNUSED_CONFIRMED=true   # research/ grep 命中 0（9 slug 全 0）
B1_CANDIDATES=[]   # 无满足「≥2独立源+六大面核心+scope缺失」者
B1_REJECTED=[
 "mathematics-architecture(proportion/golden-ratio/geometry-symmetry 已收录; tessellation/hyperboloid/geodesic/thin-shell 边缘技法)",
 "architectural-technology(学科层; 材料构造近义 structural-material/material-durability/damp-proofing/transparent-material)",
 "walkability(城市规划评价指标; 近义 pedestrian-flow/circulation; 五品质为评价维度)",
 "public-space(城市公共领域/社会学/法学; 近义 plaza/openness/boundary/node-path; 域外)",
 "natural-building(近义 vernacular-material/sustainable-design/green/sustainable-architecture/natural-ventilation; cob/earthbag 品类级)",
 "timeline-architectural-styles(地域/王朝细粒度风格; 边缘且单源; Mughal 等已由 indian/islamic 伞条目覆盖)",
 "underground-living(近义 earth-sheltered/semi-sunken/sunken-*/damp-proofing/drainage; 恒温/积水泵排/烟囱气流 已知细节)",
 "fine-art(综合艺术门类含 music/poetry 越域; genre 等级=题材门类, round43 已排除)",
 "art-criticism(formalism/iconography/mimetic 方法论; 边缘/艺术史, 非六子域核心)"
]
B1_RESULT="不构成新的核心缺口（0 条）"
B6_NEW=[]
B6_RESULT="未发现需要更新条目的理论性新研究/事件（事故/奖项/开馆/讣告/拍卖/盗窃/当代专著与期刊思潮均非核心概念理论变更）"
URLS_REQUESTED=31
URLS_OK_200=31
URLS_FAILED=0
URLS_DISTINCT=14
```

是否发现新缺口：否
