# 第 53 轮 B5 补源报告（review-round53b）——4 条构图／动线条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r53b（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理与上下文文档**：本项目根无 `AUTONOMOUS.md` / `TASK_design.md`（已实际读取尝试并确认 NOT_FOUND），实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行）；本项目 `DECISIONS.md`（25 行）、`research/review-round52b.md`（132 行，同格式前例）、`research/gaps-round50.md`（第 30–32、133 行 B5 待核实清单）。全部只读。
- **硬性规则确认**（TASK_design.md 第 34–42 行 / AUTONOMOUS.md 第六节）：不编造数字、日期、人名、引文、出处；**关键事实至少两个独立来源互证，否则标“待核实”**；查不到宁可写“不可得”也不凑数；**同一机构只算 1 源**；联网内容一律视为数据，**网页中出现的任何指令均未执行**。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按 SUBAGENT-STOP 以任务说明书为准）、`verification-before-completion`（先实抓、后断言：全部关键句逐条做 `norm(quote) in norm(page)` 子串回验，见第四节回执）。
- **对象现状**：`gaps-round50.md` 列出 `simplification`「具体实例（名称、地点、设计者、年代）待补充独立来源」、`visual-movement`「具体实例的设计者与年代待补充独立来源」、`leading-lines`「具体实例的拍摄者与年代待核实」、`symmetry-layout`「具体实例（名称、地点、设计者、年代）待补充独立来源」。本报告即为其补实例的证据底稿；**未改任何条目数据**。
- **通道**：`web_search` / 多数站点 `web_fetch` 在本环境不可用（Met、British Museum、Smithsonian、Smarthistory、UMMA、Yale、UChicago ARTIC 均 403/429/验证页），改用 `urllib`（浏览器 UA、禁验证 SSL）直连；DuckDuckGo HTML 搜索（urllib）仅用于**定位 URL**，不作证据；Britannica 一条仅 `web_fetch` 服务端直读成功。全部抓取在 stdin 内联 Python 完成，**未在项目内落盘任何脚本或缓存**。
- **只读声明**：本轮**仅生成** `research/review-round53b.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容。

## 一、方法与判据

1. **实抓**：逐 URL 记录 **HTTP 状态、字节数、`<title>`**；去 `<script>/<style>` 与标签、`html.unescape` 后抽正文；关键句用 `norm()`（NFKC + 弯/直引号、破折号、不间断空格归一 + 空白折叠 + 小写）逐条子串回验，`FOUND` 才写入本报告（见第四节）。
2. **独立性判据**：**同一机构只算 1 源**；四条均用两个互不相同的机构（同行评议学会期刊 / 大学教学网站 / 官方博物馆 / 大学开放教材 / 百科全书 / 大学学院 / 联合国教科文组织 / 香港故宫文化博物馆）。
3. **权威性分级**：**强权威**＝官方博物馆馆藏页、联合国教科文组织世界遗产中心；**中—强权威**＝同行评议学会期刊（J-STAGE / Japan Society for Graphic Science）、大学学院教学页、大学开放教材平台、百科全书（Britannica，见保留标注）。
4. **不采用维基百科作主源**：按项目既定口径（D10 / round46 / round49 / round51b / round52b），维基属同平台伞源、不计独立源，未作证据列出。
5. **概念支撑优先**：每条不只核“作品基本信息”，而是要求至少一句原文说明该作品/该图式**如何体现**对应构图原理；若源文未直书术语，明确写“概念归纳、源未直书”，不冒称源文用词。
6. **落地约束**：本报告只读产出，不能直接改数据。凡判“可用”，落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/batch-*.json` 的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年份”），同步 `pending_notes` /「待核实」，按需更新 `coverage.json` 源数，复跑 `tools/check.py`；登记前不得视为已改。

## 二、四条复核（每条：名称 / 地点 / 作者 / 年份 + 两条独立权威来源）

### 2.1 `leading-lines`（引导线）→ **葛饰北斋《神奈川冲浪里》(Under the Wave off Kanagawa / The Great Wave)，《富岳三十六景》之一**

- **名称**：Under the Wave off Kanagawa (Kanagawa oki nami ura) / The Great Wave / 《神奈川冲浪里》（又译《大浪》），出自 Thirty-six Views of Mount Fuji《富岳三十六景》（②原文 “The Great Wave off Kanagawa: Thirty-six Views of Mt. Fuji”）
- **地点**：日本（江户时代浮世绘，②著录 “Tokyo, Japan”，并注明图像来源 The Seattle Art Museum）；①为日本图形学会学会论文，研究日本原作构图
- **作者**：**Katsushika Hokusai（葛饰北斋，1760–1849）**（①②一致；②页题 “Hokusai, Katsushika 1760”）
- **年份**：**约 1830–1832**（通行著录；**本轮两条主源未直书具体年份**，②仅写 “created during the Edo Period”。补充第三次核：`https://oer.hax.psu.edu/cas391/sites/inart1/3worksthatchangedthegame-thegreatwaveoffkanagawathegreatwaveoffkanagawakatsushikahokusai-1831`，HTTP 200，题名直书 “Katsushika Hokusai (1831)”——**仅用于补年份，不计入双源、不用于概念定性**）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | J-STAGE / Japan Society for Graphic Science《Journal of Graphic Science of Japan》2007, 41(4):3–8（**中—强权威·同行评议学会期刊**） | `https://www.jstage.jst.go.jp/article/jsgs1967/41/4/41_4_3/_article` | An Analysis on the Composition of the Great Wave at Kanagawa by Hokusai | **200**（68,518 B） | “This paper is devoted to investigating the **composition** of 'the Great wave at Kanagawa' in the geometrical view point.”；“Moreover **it is shown that there exists a golden rectangle in 'the Great Wave at Kanagawa' which plays the pivotal role of the composition**.”；页面字段 “2007 Volume 41 Issue 4 Pages 3-8” |
| ② | Connecticut College「Asian Art and Architecture」编辑推荐页（**中—强权威·大学教学研究网站**） | `https://diluo.digital.conncoll.edu/Asianart/editors-pick/hokusais-the-great-wave-2/` | Hokusai’s The Great Wave – Asian Art and Architecture | **200**（104,504 B） | “**Fuji at the center of the image, making it an anchor to the piece**.”；“**These colors highlight the depth and movement within the wave**.”；“Cederquist admired **how the waves in The Great Wave were curved and angled**” |

**四要素对位**：名称＝Under the Wave off Kanagawa / The Great Wave（①②同一作品；②副标题直书《富岳三十六景》）；地点＝日本（②“Tokyo, Japan”；①日本学会原作构图研究）；作者＝Katsushika Hokusai（①②一致）；年份＝约 1830–1832（**两主源未直书，补充源标 1831，须诚实标注**）。

**独立性说明**：Japan Society for Graphic Science（J-STAGE 学会期刊）与 Connecticut College（大学教学网站）为两个不同机构、不同国家、独立撰稿，均可读、正文直证，可作独立双源。

**对“引导线”原理的支撑与诚实标注**：①以几何分析证明此画构图由**黄金矩形骨架**统摄（“plays the pivotal role of the composition”），提供“线／几何框架组织视线”的结构证据；②直书富士山“**位于画面中心、成为作品的锚点**”，并描述浪的形态“**弯曲且带角度**”、“色彩突出了浪中的纵深与运动”。两源合起来支撑：**弯曲、带角的浪形围绕中央锚点（富士山）组织，构成把视线引向中心的引导线结构**。**注意**：两源均未出现字面术语 “leading lines”；“引导线”是对上述“几何骨架＋中央锚点＋ curved and angled 浪形”的**概念归纳，不得冒称源文直书 “leading lines”**。若 lead 要求术语字面直证，本条应降为“待核实”。

### 2.2 `simplification`（简化）→ **马蒂斯《红色和谐》(Red Room / Harmony in Red)，1908，艾尔米塔什博物馆**

- **名称**：Red Room (Harmony in Red) / The Dessert: Harmony in Red (La Desserte, harmonie rouge) / 《红色和谐》（《红房间》）
- **地点**：法国创作；现藏**俄罗斯·圣彼得堡·艾尔米塔什博物馆**（The State Hermitage Museum，General Staff Building，Room 440a,b；藏品号 **ГЭ-9660**）
- **作者**：**Henri Matisse（亨利·马蒂斯，1869–1954）**（①官方字段 “Author: Matisse, Henri (1869-1954)”；②标题直书）
- **年份**：**1908**（两源一致：①官方字段 “Date: 1908”；②章节标题即 “Henri Matisse, Harmony in Red (The Red Room)”，正文述其 1908 年创作语境）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | The State Hermitage Museum 官方数字馆藏页（**强权威·官方博物馆**） | `https://hermitagemuseum.org/digital-collection/28389?lng=en` | Red Room (Harmony in Red) | **200**（63,713 B） | “**The artist himself called this a "decorative panel"**”；“The luxuriant raspberry red fabric … taking over the surface of the table and uniting it in a single whole, **swallowing up the three-dimensional space of the room and masterfully confirming the decorative potential of the canvas surface**.”；“**But in affirming the flatness of the red colour**, the artist managed to create within it the impression of space”；字段 “Museum number: ГЭ-9660 / Author: Matisse, Henri (1869-1954) / Place: France / Date: 1908 / Technique: oil on canvas / Dimensions: 180,5x221 cm” |
| ② | UEN Pressbooks《Renaissance Through Contemporary Art History》课程章节 ARTH2720（**中—强权威·大学开放教材**） | `https://uen.pressbooks.pub/arth2720/chapter/matisse-harmony-in-red/` | Henri Matisse, Harmony in Red (The Red Room) – Renaissance Through Contemporary Art History | **200**（157,586 B） | “This jumbling of patterns propels the background of the picture plane, **asserting the flatness of the canvas**.”；“**The two-dimensionality of the canvas is further underscored by the window in the upper left**”；“for all of these **attempts to collapse space**, Matisse counteracts the effect with a variety of perspective cues”；“Although the structure of Harmony in Red remains assertive, **Matisse's foremost concern was to create a pleasing pattern**.” |

**四要素对位**：名称＝Red Room (Harmony in Red)（①②同一 1908 年作品）；地点＝法国创作、艾尔米塔什收藏（①官方字段；②教材讨论同一作品）；作者＝Henri Matisse（①②一致）；年份＝**1908（两源直书）**。

**独立性说明**：艾尔米塔什博物馆（官方馆藏）与 UEN Pressbooks（大学开放教材）为两个不同机构，均可读、正文直证，可作独立双源。

**对“简化”原理的直接支撑**：①馆方原文直书“**吞没房间的三维空间、确认画布表面的装饰潜力**”“**肯定红色的平面性**”“画家自称装饰嵌板”，直接说明该画如何把三维场景压缩为二维色面——即“简化”的核心操作；②教材原文直书“**断言画布的平面性**”“**画布的二维性被进一步强调**”“**试图压塌空间**”“**首要关切是创造悦目的图案**”。**两源均直接支撑“该作品如何体现简化原理”，贴合度是本轮最高的一条，无需保留性标注。**

### 2.3 `visual-movement`（视觉动线／视线引导）→ **拉斐尔《雅典学院》(The School of Athens)，1509–1511，梵蒂冈签字厅**

- **名称**：The School of Athens / Scuola di Atene / 《雅典学院》
- **地点**：**梵蒂冈·使徒宫·签字厅（Stanza della Segnatura）**（②原文 “Painted in the Vatican for Pope Julius II between 1509-1511”；①“architectural space … inspired by Donato Bramante's design for St. Peter's Basilica”）
- **作者**：**Raphael / Raffaello Sanzio（拉斐尔，1483–1520）**（② “Sanzio, Raffaello (Urbino, 1483- Rome, 1520)”；①通篇以 Raphael 为作者）
- **年份**：**1509–1511**（②直书 “between 1509-1511”；①所引 Britannica 目录列表作 “1510–11”，与②一致区间）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Encyclopædia Britannica 问答页（**中—强权威·百科全书；见保留标注**） | `https://www.britannica.com/biography/How-did-Raphael-use-perspective-to-organize-the-School-of-Athens` | How did Raphael use perspective to organize the School of Athens? \| Britannica | **200**（`web_fetch` 服务端直读全文；`urllib` 复抓 403 反爬，非死链） | “Raphael controlled the placement of figures through an interweaving and interlocking pattern, **where the poses and gestures of various groups lead the viewer's eye across the composition**. **This movement culminates at the central figures of Plato and Aristotle, who are positioned at the converging point of the perspectival space**.” |
| ② | Grinnell College「Origins of a Liberal Education」课程展页（**中—强权威·大学学院教学页**） | `https://www.originsliberaleducation.sites.grinnell.edu/exhibits/show/origins/schoolofathens` | School of Athens and Disputation of the Holy Sacrament · Origins of a Liberal Education | **200**（16,266 B） | “**well defined linear perspective**”；“the two horizontal registers created by **compositional lines that contain and ground the subjects of the work**”；“**Painted in the Vatican for Pope Julius II between 1509-1511**” |

**四要素对位**：名称＝The School of Athens（①②同一壁画）；地点＝梵蒂冈签字厅（②直书；①所述建筑空间为圣彼得大教堂设计灵感）；作者＝Raphael（①②一致）；年份＝**1509–1511（②直书；①目录列表 1510–11）**。

**独立性说明**：Britannica（百科全书）与 Grinnell College（大学学院课程展页）为两个不同机构、独立撰稿，均可读、正文直证，可作独立双源。

**对“视觉动线”原理的直接支撑与诚实标注**：①是**作品专属、术语直证**的证据——“**各组人物的姿态与手势把观者的眼睛引过整个画面**”“**这一运动终结于柏拉图与亚里士多德——他们正处在透视空间的汇聚点上**”，直接描述视线移动路径及其终点；②从形式分析角度直书“**明确的线性透视**”“**构图线条形成两条水平分区、包容并稳住画面主体**”，支撑“由线条与构图组织视线”的结构。**两处保留标注**：（a）①页自身声明 “Created from Britannica articles using AI. AI can make mistakes, so verify using Britannica articles.”——虽为 Britannica 官方发布页并列出所据条目，但属 **AI 生成问答**，若 lead 要求“一手编辑撰稿”，应改以 Britannica 编辑条目或 Smarthistory 等替换；（b）②中 “the viewer's gaze is lead upward … through diagonal compositional lines” 一句明确评述的是**配对壁画《圣礼的争辩》(Disputation of the Holy Sacrament)**，**不是**《雅典学院》，落地时不得误植到本条。

### 2.4 `symmetry-layout`（对称布局）→ **北京故宫（紫禁城），1406–1420，明成祖朱棣敕建**

- **名称**：Forbidden City / Imperial Palace of the Ming and Qing Dynasties in Beijing / 紫禁城（今故宫博物院）
- **地点**：**中国·北京·北京中轴线核心**（② “Built on Beijing's central axis”；①世界遗产项目 “Imperial Palaces of the Ming and Qing Dynasties in Beijing and Shenyang”）
- **作者 / 营造主体**：**明成祖朱棣（Zhu Di）敕建，明代宫廷营造体系实施**（① “constructed between 1406 and 1420 by the Ming emperor Zhu Di”；**两源均未载单一建筑师姓名，不得编造**）
- **年份**：**1406–1420**（①直书 “constructed between 1406 and 1420 by the Ming emperor Zhu Di”；日本语版同页记 1420 年完成）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | UNESCO World Heritage Centre（**强权威·联合国教科文组织官方**） | `https://whc.unesco.org/en/list/439/` | Imperial Palaces of the Ming and Qing Dynasties in Beijing and Shenyang - UNESCO World Heritage Centre | **200**（155,647 B） | “The Imperial Palace of the Ming and Qing Dynasties in Beijing known as the Forbidden City was **constructed between 1406 and 1420 by the Ming emperor Zhu Di**”；“The layout and spatial arrangement inherits and embodies the traditional characteristic of urban planning and palace construction in ancient China, **featuring a central axis, symmetrical design and layout of outer court at the front and inner court at the rear** …” |
| ② | Hong Kong Palace Museum 官方展览页（**强权威·故宫博物院香港分馆/官方博物馆**） | `https://www.hkpm.org.hk/en/exhibition/entering-the-forbidden-city-architecture-collection-and-heritage` | Entering the Forbidden City: Architecture, Collection, and Heritage \| Hong Kong Palace Museum | **200**（40,096 B） | “**Built on Beijing's central axis, the position of the Forbidden City testifies to its significance to Chinese politics and culture.**” |

**四要素对位**：名称＝Forbidden City / 紫禁城（①②同一对象）；地点＝北京中轴线（②直书；①世界遗产北京—沈阳项目）；作者＝明成祖朱棣敕建（①直书，②未载单一建筑师）；年份＝**1406–1420（①直书）**。

**独立性说明**：UNESCO 世界遗产中心（国际组织官方）与香港故宫文化博物馆（官方博物馆）为两个不同机构，均可读、正文直证，可作独立双源。

**对“对称布局”原理的支撑与诚实标注**：①是**作品专属、术语直证**——“**以一条中轴线、对称的设计与布局、前朝后寝**”，直接说明该建筑群如何以轴线对称组织空间；②独立确认“**紫禁城建于北京中轴线之上**”，从博物馆展览角度佐证其中轴地位。**注意**：②未直接使用 “symmetrical” 一词，“对称”的直接术语证据来自①；②的作用是独立佐证“中轴线”这一对称布局的结构前提。落地时应写“以 UNESCO 的 symmetrical design 描述为主证，香港故宫页佐证中轴线地位”，不得冒称②直书“对称”。

## 三、汇总

| 条目 | 具名实例 | 地点 | 作者 / 营造主体 | 年份 | 源① | 源② | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `leading-lines` | 葛饰北斋《神奈川冲浪里》The Great Wave（《富岳三十六景》） | 日本（江户浮世绘；②著录 Tokyo, Japan） | Katsushika Hokusai | 约 1830–1832（两主源未直书；补源 1831） | J-STAGE 学会论文（构图几何分析） | Connecticut College 亚洲艺术教学页 | 200 / 200 | **可用但须标注**：两源均未直书 “leading lines”，属“几何骨架＋中央锚点＋弯曲浪形”的**概念归纳**；年份需补源支撑 |
| `simplification` | 马蒂斯《红色和谐》Red Room (Harmony in Red)（ГЭ-9660） | 法国创作；圣彼得堡·艾尔米塔什博物馆 | Henri Matisse | 1908 | Hermitage 官方数字馆藏 28389 | UEN Pressbooks 大学开放教材 | 200 / 200 | **可用（两源直证平面化/压塌三维空间，无保留）** |
| `visual-movement` | 拉斐尔《雅典学院》The School of Athens | 梵蒂冈·签字厅 | Raphael (Raffaello Sanzio) | 1509–1511 | Britannica 问答页（`web_fetch` 直读） | Grinnell College 课程展页 | 200 / 200 | **可用但须标注**：①为 Britannica 的 AI 生成问答页；②的“gaze … diagonal lines”述配对壁画，不得误植 |
| `symmetry-layout` | 北京故宫（紫禁城）Forbidden City | 中国·北京·中轴线核心 | 明成祖朱棣敕建（无单一建筑师记载） | 1406–1420 | UNESCO 世界遗产 439 | 香港故宫文化博物馆官方展览页 | 200 / 200 | **可用（①直书 central axis + symmetrical design；②直书中轴线地位）** |

- **双源齐备率：4/4**；8 个主来源全部取证成功（1 个经 `web_fetch` 服务端直读，7 个经 `urllib` 直连），**0 死链、0 编造、0 单源、0 不可得**；无需写“仅单源/不可得”。
- **机构独立性**：每条均为两个不同机构，符合“同一机构只算 1 源”。八机构为：Japan Society for Graphic Science（J-STAGE）、Connecticut College、The State Hermitage Museum、UEN Pressbooks、Encyclopædia Britannica、Grinnell College、UNESCO、Hong Kong Palace Museum。
- **需落地时保留的诚实标注（3 处）**：
  1. `leading-lines`：两源均未直书 “leading lines”；“引导线”为概念归纳。年份 1830–1832 由补充源（Penn State OER，标 1831）支撑，两主源未直书。
  2. `visual-movement`：①是 Britannica 官方发布但自述 AI 生成的问答页；②的视线路径句述配对壁画《圣礼的争辩》，落地不得误植。
  3. `symmetry-layout`：②只直书“built on Beijing's central axis”，未直书 “symmetrical”；对称术语证据以①为准。作者写“朱棣敕建”，不写具体建筑师。
- **未做之事**：本报告未修改任何条目数据或其它文件；四条 `sections.实例` 现状仍须由 lead 按第一节“落地约束”另行改写并复跑 `tools/check.py`。

## 四、证据回执（verification-before-completion）

逐条 `norm(quote) in norm(page)` 子串回验结果（全部 FOUND 才写入正文）：

| 来源 | 回验句（缩写） | 结果 |
| --- | --- | --- |
| J-STAGE 41_4_3 | "there exists a golden rectangle in" / "which plays the pivotal role of the composition" / "2007 volume 41 issue 4 pages 3-8" | FOUND |
| Connecticut College | "Fuji at the center of the image, making it an anchor to the piece" / "these colors highlight the depth and movement within the wave" / "waves in the great wave were curved and angled" | FOUND |
| Hermitage 28389 | "swallowing up the three-dimensional space of the room and masterfully confirming the decorative potential of the canvas surface" / "in affirming the flatness of the red colour" / "the artist himself called this a \"decorative panel\"" / "date: 1908" / "matisse, henri (1869-1954)" | FOUND |
| UEN Pressbooks | "asserting the flatness of the canvas" / "the two-dimensionality of the canvas is further underscored by the window in the upper left" / "for all of these attempts to collapse space" / "matisse's foremost concern was to create a pleasing pattern" | FOUND |
| Britannica AI 问答页 | "lead the viewer's eye across the composition" / "this movement culminates at the central figures of plato and aristotle" / "who are positioned at the converging point of the perspectival space" | FOUND（`web_fetch` 全文可见；`urllib` 一次复抓 403 反爬） |
| Grinnell College | "well defined linear perspective" / "the two horizontal registers created by compositional lines that contain and ground the subjects of the work" / "painted in the vatican for pope julius ii between 1509-1511" | FOUND |
| UNESCO 439 | "featuring a central axis, symmetrical design and layout of outer court at the front and inner court at the rear" / "constructed between 1406 and 1420 by the ming emperor zhu di" | FOUND |
| HKPM 展览页 | "built on beijing's central axis, the position of the forbidden city testifies to its significance to chinese politics and culture" | FOUND |

> 校验方法：UTF-8 解码 → 去 script/style/标签 → `html.unescape` → `norm()`（NFKC + 弯直引号/破折号/不间断空格归一 + 空白折叠 + 小写）→ 子串命中。HTML `<title>` 与 HTTP 状态来自同一轮实抓；字节数为响应体原始字节数。
