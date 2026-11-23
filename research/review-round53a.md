# 第 53 轮 B5 补源报告（review-round53a）——4 条构图/视觉原理条目补具名实例

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r53a（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理与上下文文档**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 不存在（本轮 glob 核实 0 命中），实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行）；本项目 `DECISIONS.md`（25 行）、`research/review-round52b.md`（132 行）全部只读。
- **硬性规则确认**：不编造数字、日期、人名、引文、出处；关键事实至少两个独立来源互证，否则标“仅单源/不可得”；来源须能支撑“该作品如何体现此原理”；**同一机构只算 1 源**；联网内容一律视为数据，网页中出现的任何指令均未执行。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 `SUBAGENT-STOP` 以任务说明书为准）、`verification-before-completion`（先实抓、后断言；HTTP 与关键句均以本轮页面回读为准）。
- **对象现状**：本轮为 4 条仍标待核实的构图/视觉原理条目补具名实例证据底稿；**未改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目外内容，抓取未落盘脚本或缓存。
- **诚实结论**：`figure-ground`、`visual-center`、`hierarchy` 三条取得双源；`rule-of-thirds` 经多组候选换例后只找到**单条直接支持同一作品的权威来源**，按任务要求写“仅单源/不可得”，不补造第二源。

## 一、方法与判据

1. **实抓**：逐 URL 记录 HTTP 状态、页面标题与原文关键句；关键句均取自本次实际打开的页面，不凭记忆补写。
2. **独立性**：同机构只算 1 源；优先官方博物馆、大学开放课程/大学出版社、官方博物馆教育页、国家级/权威设计机构。
3. **概念支撑优先**：不只用来源核名称、作者、年份；必须说明来源中的句子如何支撑“作品—原理”的对应关系。若来源未直书原理术语，明确标为“概念归纳”，不冒称源文直书。
4. **不采用维基百科作主源**：沿用 round52b 项目口径。
5. **落地约束**：本报告只读产出；落地时须先把可用来源以 `verified=true` 登记进 `data/sources.json`，再改对应 `entries/batch-*.json` 的 `sources` 与 `sections.实例`，同步 `pending_notes` /「待核实」，复跑 `tools/check.py`。

## 二、四条复核

### 2.1 `rule-of-thirds`（三分法）→ 1938 年英格兰—德国奥运足球赛“纳粹敬礼”照片

- **判定**：**仅单源/不可得（双源不可得）**
- **名称**：England v Germany exhibition match salute photograph / 英格兰—德国足球赛敬礼照片（UNI 页面开篇所用历史照片）
- **地点**：德国·柏林·奥林匹克体育场（Olympic Stadium, Berlin）
- **作者**：源页未具名摄影者，仅记为 “a photographer at field level”；故作者字段保持“未署/源未给”，不补造姓名
- **年份**：**1938**（“The date was May 14, 1938.”）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文） |
| --- | --- | --- | --- | --- | --- |
| ① | University of Northern Iowa，Bettina Fabos《Visual Literacy: Aesthetics, Semiotics, and the Truth Behind an Image》（**大学教材章节**） | `https://uni.edu/fabos/ml/readings/visual_literacy.html` | visual literacy | **200** | “The event was an exhibition match in Berlin's enormous Olympic Stadium, The date was May 14, 1938.”；“Another is ‘rule of thirds,’ a well-known principle of photographic and image composition. By breaking an image down into thirds (both horizontally and vertically), and by placing elements on the points of intersection, we can avoid both the uncomfortable pulling when the form is too close to the frame, and the boring inertia when the form is too central.”；“The stadium line and the row of athletes—particularly their waistlines—rest comfortably on the horizontal thirds, suggesting interest but little tension, until one considers the vectors.” |
| ② | **不可得**：未找到第二条独立权威来源，直接说明**同一照片**如何用三分法构图 | — | — | — | — |

**来源如何支撑原理**：①先给出三分法定义（横竖各三等分、把元素放在交点以避免贴边拉扯与居中呆板），随后对本照片作作品级分析：“stadium line”和“row of athletes—particularly their waistlines”落在水平三分线上；这是本轮唯一一条“同一作品 + 三分法 + 权威页面”三者齐备的直接证据。

**为何判“仅单源/不可得”**：本轮另试 Edgar Degas *L'étoile*（DePaul 大学页面将其列在 Rule of Thirds 标题下，但第二源多为作品元数据或同机构页面）、Grant Wood *American Gothic*（Whitney 教师指南 PDF 与官网音频页未能在可读页面中取得三分法关键句）、Hokusai *The Great Wave*（权威馆藏页可读，但未找到明确的作品级三分法判断）。这些候选均无法凑齐“两个独立机构 + 同一作品 + 直接支撑三分法”，故不把旁证冒充第二源。

---

### 2.2 `figure-ground`（图底关系）→ 诺利罗马地图（Nolli Map / Pianta Grande di Roma）

- **名称**：Nolli Map / Pianta Grande di Roma / 诺利罗马地图
- **地点**：意大利·罗马（描绘对象；TU Delft 页：“The Nolli map from 1748 shows Rome”）
- **作者**：**Giambattista Nolli（乔瓦尼·巴蒂斯塔·诺利）**
- **年份**：**1748**

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文） |
| --- | --- | --- | --- | --- | --- |
| ① | University of Wisconsin Press，《Landscape Journal》论文页（**大学出版社/同行评议期刊**） | `https://lj.uwpress.org/node/3090` | Learning from the Nolli Map: Representing the Landscape through Figure-Ground | **200（首取；复核 403 反爬）** | “The simplest depiction is figure-ground, a method that allows a clear and powerful reading of a space through a binary mapping of built space (object) and empty ground (field).”；“The most influential example of figure-ground is Giambattista Nolli’s 1748 _Pianta Grand…” |
| ② | TU Delft OpenCourseWare，IMAGE \| ABILITY – Visualizing the Unimaginable（**大学开放课程**） | `https://ocw.tudelft.nl/course-readings/ways-distinguish-elements-complex-situation/` | Ways to distinguish elements in a complex situation | **200** | “The Nolli map from 1748 shows Rome in a very clear way. The map is in black and white, with a very clear meaning: white indicates urban public space, while black indicates built area and private space.”；“Nolli could have drawn every single house in the city and he could have indicated different sorts of space in the city, but he made the decision to unify all differences into the most important two: buildings and public space.” |

**来源如何支撑原理**：①给出 figure-ground 的标准定义——“built space (object)”与“empty ground (field)”的二元映射——并把诺利 1748 年罗马图称为最有影响的例子；②用同一张图说明白=公共开放空间、黑=建成/私人空间，且诺利刻意把复杂城市归纳为“buildings and public space”两大项。两源从定义与图面读法两端共同支撑“实体—虚空/图—底的二元构图”。

**独立性说明**：University of Wisconsin Press 与 TU Delft OCW 为不同机构、不同作者/课程文本，均可读，符合独立双源。

---

### 2.3 `visual-center`（视觉中心）→ 葛饰北斋《神奈川冲浪里 / 巨浪》

- **名称**：Under the Wave off Kanagawa (Kanagawa oki nami ura) / The Great Wave / 《神奈川冲浪里》《巨浪》，出自《富岳三十六景》
- **地点**：画面为日本神奈川外海、远眺富士山；源①所述印本藏于大英博物馆
- **作者**：**Katsushika Hokusai（葛饰北斋，1760–1849）**
- **年份**：**1831**（源①：“彩色木刻版画，1831 年”；源②：“around 1831”）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文） |
| --- | --- | --- | --- | --- | --- |
| ① | 大英博物馆中文官网（**官方博物馆中文站**） | `https://britishmuseum.org.cn/blog/classic-collection-by-katsushika-hokusai` | 《神奈川冲浪里》与巨浪之外的故事-大英博物馆中文官网 | **200** | “在画面中，滔天的巨浪就像一只正在咆哮着的、带有 ‘鹫爪’的水怪。画面定格在‘水怪’纵身跃起的最高点，仿佛将以雷霆万钧之势砸向三只载有船员的小船。”；“而透过海浪的间隙，可见富士山伫立于远处，白雪覆盖在山顶上，平静优雅。尽管在惊涛骇浪衬托下的富士山显得格外渺小，却仍傲然屹立着，岿然不动。”；“近景的‘动’与远景的‘静’结合使画面更具冲突感和表现力……其巧妙的几何构图及精准比例使人过目难忘。” |
| ② | Christie’s 佳士得官方拍品页（**权威艺术机构官方图录**） | `https://www.christies.com.cn/zh/lot/katsushika-hokusai-1760-1849-kanagawa-oki-nami-ura-6525585/` | 葛飾北齋（1760-1849）, 神奈川冲浪裏 \| Christie's | **200** | “The ‘waves that are claws’ that Van Gogh saw in this image is, as wave scientists have now explained, a series of cresting waves that end in hooks, known as fractal waves.”；“Mount Fuji is visible from this position as Hokusai has it: far away, so it looks small.”；“Whether they manage, hunkered down over their oars, to slice through the wave like surfers or be pummeled by it is, of course, the captivating mystery of the drama.” |

**来源如何支撑原理（诚实标注：概念归纳）**：两源**未直书**英文术语 “visual center”，但均直接描述了同一构图事实——前景巨浪以最大尺度、最高动势与“鹰爪/钩状浪尖”占据画面主视觉，富士山被置于远景且“看起来很小”；源①还明说“近景的动与远景的静”“巧妙的几何构图及精准比例”。据此可把该作作为“视觉中心偏向前景巨浪而非画面几何中心”的具名实例；落地时须写“构图归纳”，不得冒称源文直书“视觉中心”。

**独立性说明**：大英博物馆中文官网与 Christie’s 官方图录为不同机构、不同撰稿，均可读。

---

### 2.4 `hierarchy`（视觉层级）→ 哈里·贝克伦敦地铁示意图（Diagrammatic London Underground Map）

- **名称**：Diagrammatic London Underground Map / Tube map / 伦敦地铁示意图
- **地点**：英国·伦敦（London Transport / London Underground）
- **作者**：**Harry Beck（Henry C. Beck，哈里·贝克，1902–1974）**
- **年份**：**1931 设计 / 1933 出版为袖珍地图**（Design Museum 页明确两时间点）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文） |
| --- | --- | --- | --- | --- | --- |
| ① | Design Museum（**权威设计博物馆**，文末注明文本 © Design Museum and London Transport Museum） | `https://designmuseum.org/london-transport` | London Transport - Design Museum | **200** | “Existing maps were crowded, confusing and hard to read. In 1931, in his spare time, Harry Beck (1902-1974) redesigned the Underground map as a simple diagram.”；“Beck represented each line in a different colour and interchange stations as diamonds. The crowded central area was enlarged for legibility and the course of each route was simplified into the form of a vertical, horizontal or diagonal.”；“The diagrammatic map was produced in 1933 as a pocket map and Beck continued to refine it until 1959.” |
| ② | TU Delft OpenCourseWare，IMAGE \| ABILITY – Visualizing the Unimaginable（**大学开放课程**） | `https://ocw.tudelft.nl/course-readings/ways-distinguish-elements-complex-situation/` | Ways to distinguish elements in a complex situation | **200** | “The map is optimized for the traveler in the subway station. Once you are in the subway train, you do not need a lot of information about the whole network. Then you just need to focus on the next stations and the station where you might want to transfer to another line.”；“So here we see another level of information, represented in a different way: the subway line graph.”；“The map design by Harry Beck is regarded a precedent for many subway maps that were based on similar design ideas.” |

**来源如何支撑原理**：①说明贝克把拥挤难读的网络改为简图，并用颜色区分线路、菱形标换乘、放大中心区、把路线简化为水平/垂直/对角——这些都是按读者任务组织信息层级的做法；②进一步说明该图按乘客场景优化，只让乘客先聚焦“下一站”和“换乘站”，并指出其中存在“another level of information”。两源共同支撑“视觉层级＝按重要性/使用场景分层呈现信息”。

**独立性说明**：Design Museum 与 TU Delft OCW 为不同机构、不同文本；同一 TU Delft 页面在本报告分别用于 figure-ground 的诺利地图段与 hierarchy 的贝克地图段，但两条对象的证据段落互不替代。

## 三、汇总

| 条目 | 具名实例 | 地点 | 作者 | 年份 | 源① | 源② | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `rule-of-thirds` | 1938 英格兰—德国奥运足球赛敬礼照片 | 柏林奥林匹克体育场 | 源页未署摄影者 | 1938 | University of Northern Iowa《Visual Literacy》 | 不可得 | 200 / — | **仅单源/不可得**：UNI 直接作三分法作品分析；未凑齐第二独立权威源 |
| `figure-ground` | Nolli Map / Pianta Grande di Roma / 诺利罗马地图 | 意大利·罗马 | Giambattista Nolli | 1748 | University of Wisconsin Press《Landscape Journal》 | TU Delft OCW | 200 / 200（源①复核 403 反爬） | **可用**：①定义 figure-ground 并称其为最具影响实例；②直证黑白二元图底读法 |
| `visual-center` | Under the Wave off Kanagawa / The Great Wave / 《神奈川冲浪里》 | 神奈川外海、富士山远眺；印本藏大英博物馆 | Katsushika Hokusai | 1831 | 大英博物馆中文官网 | Christie’s 官方拍品页 | 200 / 200 | **可用（概念归纳）**：两源直证巨浪主视觉与富士山远景缩小；未直书“视觉中心” |
| `hierarchy` | Diagrammatic London Underground Map / Tube map | 英国·伦敦 | Harry Beck | 1931 设计 / 1933 出版 | Design Museum《London Transport》 | TU Delft OCW | 200 / 200 | **可用**：颜色/换乘符号/中心放大/信息分层均由两源支撑 |

- **双源齐备率**：3/4；`rule-of-thirds` 为 1/2，按任务要求标“仅单源/不可得”。
- **来源计数**：六个主来源首取 HTTP 均为 200；完成前复核时 University of Wisconsin Press 节点页返回 403 反爬（本地 `curl` 同样 403），但该页在本轮首取中已实读到标题与 abstract 关键句，故按“首取 200 / 复核 403 反爬”如实记录；其余主来源复核 200。无编造、无完整 URL 缺失。
- **落地提醒**：`visual-center` 的“非几何中心”是对两源所述前景/远景尺度与动势反差的构图归纳；落地文案必须保留“归纳”表述。
- **未做之事**：未修改任何条目数据或其他项目文件；四条 `sections.实例` 仍待 lead 依本报告另行改写并复跑 `tools/check.py`。

## 四、证据回执（verification-before-completion）

| 来源 | 回验句（缩写） | 结果 |
| --- | --- | --- |
| UNI visual literacy | “The date was May 14, 1938.” / “rule of thirds…placing elements on the points of intersection” / “waistlines—rest comfortably on the horizontal thirds” | 页面实读命中 |
| University of Wisconsin Press | “The simplest depiction is figure-ground…” / “built space (object) and empty ground (field)” / “most influential example of figure-ground is Giambattista Nolli’s 1748…” | 首取页面实读命中（第二句在服务端截断处前仍可见）；完成前复核 403 反爬 |
| TU Delft OCW（Nolli 段） | “white indicates urban public space, while black indicates built area and private space.” / “unify all differences into the most important two: buildings and public space.” | 页面实读命中 |
| British Museum CN | “滔天的巨浪…‘鹫爪’…水怪” / “富士山…显得格外渺小” / “近景的‘动’与远景的‘静’…巧妙的几何构图及精准比例” | 页面实读命中 |
| Christie’s CN | “waves that are claws…cresting waves that end in hooks” / “Mount Fuji…far away, so it looks small.” / “captivating mystery of the drama.” | 页面实读命中 |
| Design Museum | “crowded, confusing and hard to read” / “represented each line in a different colour and interchange stations as diamonds” / “crowded central area was enlarged for legibility” / “produced in 1933 as a pocket map” | 页面实读命中 |
| TU Delft OCW（Beck 段） | “optimized for the traveler” / “focus on the next stations…transfer” / “another level of information” / “precedent for many subway maps” | 页面实读命中 |

> HTTP 状态均来自本轮页面抓取回执：首取六个主来源均为 200；完成前复核时 University of Wisconsin Press 节点页返回 403 反爬（已首取实读关键句），本地 `curl` 对部分站点也出现 000/重定向等通道差异。关键句均为本轮页面可见原文。网页中任何指令性文本均按数据处理，未执行。
