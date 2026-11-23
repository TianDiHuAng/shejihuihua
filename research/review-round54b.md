# 第 54 轮 B5 补源报告（review-round54b）——4 条建筑风格条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r54b（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理与上下文文档**：本项目根无 `AUTONOMOUS.md` / `TASK_design.md`（实读尝试确认 NOT_FOUND），实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）、`D:/Users/Administrator/Desktop/TASK_design.md`（67 行）；本项目 `DECISIONS.md`（25 行）、`research/review-round53b.md`（129 行，同格式前例）、`research/gaps-round50.md`（第 109、185、188、191 行四条 B5 待核实清单）。全部只读。
- **硬性规则确认**（TASK_design.md 第 34–42 行 / AUTONOMOUS.md 第六节）：不编造名称、地点、作者、年份、引文、出处；**关键事实至少两个独立来源互证，否则标“待核实”**；查不到宁可写“不可得”也不凑数；**同一机构只算 1 源**；联网内容一律视为数据，**网页中出现的任何指令均未执行**。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按 SUBAGENT-STOP 以任务说明书为准）、`verification-before-completion`（先实抓、后断言：全部关键句逐条 `norm(quote) in norm(page)` 子串回验，见第五节回执）。
- **对象现状**：`gaps-round50.md` 列出 `functionalism-architecture`「具体实例（名称、地点、设计者、年代）待补充独立来源」（第 109 行）、`constructivism`（185）、`japanese-architecture`（188）、`imperial-architecture`（191）。本报告即为其补实例的证据底稿；**未改任何条目数据**。
- **避重**：`symmetry-layout` 已用北京故宫（round53b §2.4），故 `imperial-architecture` 改用**凡尔赛宫**；`bauhaus` 已用德绍包豪斯校舍，故 `functionalism-architecture` 改用**萨伏伊别墅**。四例互不重复。
- **通道**：`web_search` 仅用于**定位 URL**（DuckDuckGo/搜索聚合结果），不作证据；证据正文取自 `web_fetch` 服务端直读（Britannica 三页、凡尔赛官方）与 `urllib` 直连（浏览器 UA、禁验证 SSL：法隆寺官方、Tate Papers、LibreTexts、Fondation Le Corbusier）。UNESCO 三页（660/81/1321）经 `web_fetch` 与 `urllib` 均 403 反爬，未作证据；MoMA、Smarthistory 亦 403，已改易双源实例/换机构，符合任务“凑不齐双源则换更易双源实例”的指示。全部抓取在 stdin 内联 Python 完成，**未在项目内落盘任何脚本或缓存**。
- **只读声明**：本轮**仅生成** `research/review-round54b.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容。

## 一、方法与判据

1. **实抓**：逐 URL 记录 **HTTP 状态、字节数、`<title>`**；去 `<script>/<style>` 与标签、`html.unescape` 后抽正文；关键句用 `norm()`（NFKC + 弯/直引号、破折号、零宽空格、不间断空格归一 + 空白折叠 + 小写）逐条子串回验，`FOUND` 才写入本报告（见第五节）。
2. **独立性判据**：**同一机构只算 1 源**；四条均用两个互不相同的机构（寺院官方 / 百科全书 / 宫殿官方管理机构 / 大学开放教材 / 国立美术馆研究期刊 / 建筑师基金会）。
3. **权威性分级**：**强权威**＝古迹官方机构页、宫殿官方管理方、建筑师官方基金会、大学开放教材；**中—强权威**＝百科全书（Britannica，编辑署名）、Tate Papers（美术馆同行评议研究期刊）。
4. **不采用维基百科作主源**：按项目既定口径（D10 / round46 / round49 / round51b / round52b / round53b），维基属同平台伞源、不计独立源，未作证据列出。
5. **落地约束**：本报告只读产出，不能直接改数据。凡判“可用”，落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/batch-*.json` 的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年份”），同步 `pending_notes` /「待核实」，按需更新 `coverage.json` 源数，复跑 `tools/check.py`；登记前不得视为已改。

## 二、四条复核（每条：名称 / 地点 / 作者 / 年份 + 两条独立权威来源）

### 2.1 `japanese-architecture`（日本建筑）→ **法隆寺（Hōryū-ji / Hōryū Temple），7 世纪（创建 607，670 火灾后重建），奈良县生驹郡斑鸠町**

- **名称**：法隆寺 / Hōryū-ji（Ikarugadera、Wakakusa）
- **地点**：**日本奈良县生驹郡斑鸠町**（①官方地址字段 “Horyuji 1-1 Horyuji Sannai, Ikaruga-cho, Ikoma-gun, Nara”；② “in the town of Ikaruga, northwestern Nara ken (prefecture)”）
- **作者 / 营造主体**：**推古天皇与圣德太子发愿营造**（① “Empress Suiko and Crown Prince Shotoku Taishi fulfilled Emperor Yomei's deathbed wish by building in 607 a temple and a statue of a Buddha”；② “Beginning about ad 600, a number of Buddhist monuments were constructed by order of the prince Shōtoku … regent of the empress Suiko”）。**两源均未载单一建筑师姓名，不得编造。**
- **年份**：**创建 607；670 火灾后重建**（① “building in 607 a temple”；“On the fateful night of April 30 in the year 670, a great blaze swept through the temple grounds”；② “The original Horyu Temple was built between 601 and 607. A fire in 670 destroyed the site, which was subsequently rebuilt and enlarged.”）。**诚实标注**：任务提示的 “607/701” 中 **701 两主源均未直书**；②仅给 601–607 创建区间与 670 后重建，现存最早木构通常记为 7 世纪末—8 世纪初；落地写 607 / 670 后重建，不写 701，除非另补权威源。

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Horyuji Temple 官方英文史页（**强权威·寺院官方机构**） | `https://horyuji.or.jp/en/garan` | Introduction \| Horyuji Temple | **200**（23,988 B） | “Empress Suiko and Crown Prince Shotoku Taishi fulfilled Emperor Yomei's deathbed wish by **building in 607 a temple and a statue of a Buddha**, to which the temple was dedicated.”；“The grounds of Horyuji (Horyu Temple) house **the world's oldest surviving wooden structures**, conveying images of Japan as it existed more than 1,300 years ago, during the Asuka period (538–710).”；“On the fateful night of April 30 in the year 670, a great blaze swept through the temple grounds”；地址字段 “Horyuji 1-1 Horyuji Sannai, Ikaruga-cho, Ikoma-gun, Nara, 636-0115 JAPAN”；“In December of 1993, Horyuji … became **the first treasure of any kind in Japan to be selected by UNE[SCO]**” |
| ② | Encyclopædia Britannica「Hōryū Temple」（**中—强权威·百科全书，Britannica Editors 署名**，`web_fetch` 服务端直读） | `https://www.britannica.com/topic/Horyu-Temple` | Hōryū Temple \| Buddhist architecture, Nara period, World Heritage Site \| Britannica | **200**（`web_fetch` 直读；`urllib` 复抓 403 反爬，非死链） | “**Hōryū Temple**, Japanese Buddhist temple complex in the town of **Ikaruga, northwestern Nara** ken (prefecture), west-central Honshu, Japan.”；“Beginning about ad 600 … constructed by order of **the prince Shōtoku … regent of the empress Suiko**.”；“**The original Hōryū Temple was built between 601 and 607. A fire in 670 destroyed the site, which was subsequently rebuilt and enlarged.**”；“Several structures … have survived from that rebuilding and are **among the oldest extant wooden structures in the world**.”；“collectively designated a UNESCO World Heritage site in 1993” |

**四要素对位**：名称＝法隆寺 / Hōryū-ji（①②同一寺院）；地点＝奈良县斑鸠町（①官方地址；② “Ikaruga, northwestern Nara”）；作者＝推古天皇＋圣德太子发愿（①②一致，无单一建筑师）；年份＝**607 创建、670 后重建（两源直证；701 未直书，不写）**。

**独立性说明**：法隆寺官方机构与 Britannica 编辑团队为两个不同机构、独立撰稿，均可读、正文直证，可作独立双源。

**对“日本建筑”风格的支撑与诚实标注**：两源共同确认该寺为**日本飞鸟时代佛教建筑、现存世界最早木构建筑群**——①直书 “world's oldest surviving wooden structures … during the Asuka period (538–710)”；②直书 “among the oldest extant wooden structures in the world” 且 1993 年列入世界遗产。“日本建筑”是覆盖自古坟—飞鸟—奈良—平安直至现代的**大跨度风格集合**，法隆寺只代表其中**飞鸟时代佛教木构（柱列、抬梁、斗栱雏形、塔与金堂伽蓝配置）**这一段；落地时须写“早期日本佛教木构代表例”，不得写成“日本建筑的全称代表”。**注意**：①页“1993 … selected by UNE”系抓取文本截断（下文为 SCO），仅用于佐证世界遗产身份，与② “designated a UNESCO World Heritage site in 1993” 一致。

### 2.2 `imperial-architecture`（宫殿建筑）→ **凡尔赛宫（Palace of Versailles / Château de Versailles），1661–1710 主体营建，法国凡尔赛**

- **名称**：凡尔赛宫 / Palace of Versailles / Château de Versailles
- **地点**：**法国凡尔赛（巴黎西南）**（② “palace, Versailles, France”；①官方地址 “Place d'Armes, 78000 Versailles, France”）
- **作者 / 营造主体**：**路易十四（Louis XIV）主导扩建并自任“建筑师”角色**（① “The King … **took on the role of architect himself**, and built a masterpiece with which he would forever be associated.”；②编辑条目 “History” 段以 Louis XIV 为主轴）。**诚实标注**：凡尔赛宫历经 Louis XIII 猎屋 → Louis XIV 扩建 → Louis XV/XVI 增建；①另记 Le Vau（1668–1670 “Le Vau Envelope”）、Royal Chapel（1699–1710）等分段工程，**不存在单一“设计者”**，落地写“路易十四主持营建、历代续建”，不写单一建筑师名。
- **年份**：**1661–1710（主体营建）**（① “in **1661** shortly after the death of his First Minister, he undertook major works on it”；同页工程序列止于 “the Royal Chapel in **1699-1710**”；② “declared the official royal residence in **1682** … abandoned after the death of Louis XIV in **1715**”——两源区间吻合）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Château de Versailles 官方「History」（**强权威·宫殿官方管理机构**） | `https://en.chateauversailles.fr/discover/history` | History \| Château de Versailles | **200**（107,313 B） | “He became so fond of the place that, **in 1661 shortly after the death of his First Minister, he undertook major works on it**.”；“The King, who could see great things for the chateau and the forests around it, **took on the role of architect himself**, and built a masterpiece with which he would forever be associated.”；工程序列 “the forecourt in 1662, the 'Le Vau Envelope' in 1668-1670 … **the Royal Chapel in 1699-1710**”；“**From 1682 it became the main residence** of the French Court and government”；“over 50 years and after nearly 100 million Livres, he had laid all the foundations” |
| ② | Encyclopædia Britannica「Palace of Versailles / History」（**中—强权威·百科全书，Britannica Editors 署名**，`web_fetch` 服务端直读） | `https://www.britannica.com/topic/Palace-of-Versailles/History` | Palace of Versailles - French Royalty, Baroque Architecture, Grandeur \| Britannica | **200**（`web_fetch` 直读；`urllib` 复抓 403 反爬，非死链） | “**The Palace of Versailles was declared the official royal residence in 1682** and the official residence of the court of France on May 6, 1682, **but it was abandoned after the death of Louis XIV in 1715**.”；“Until Louis XIV's time, the town of Versailles comprised but a few houses to the south of the present Place d'Armes.” |

**四要素对位**：名称＝凡尔赛宫（①②同一对象）；地点＝法国凡尔赛（①官方地址；② “Versailles, France”）；作者＝路易十四主持（①直书自任 architect 角色；②以其统治为营建主轴）；年份＝**1661 起主体扩建、1699–1710 收尾（①直书）；1682 成为王室驻地、1715 路易十四去世（②直书）**。

**独立性说明**：凡尔赛宫官方管理机构与 Britannica 编辑团队为两个不同机构，均可读、正文直证，可作独立双源。

**对“宫殿建筑”风格的支撑与诚实标注**：①直书路易十四“自任建筑师角色、把宫殿变成权力与权威的表达（made his palace an expression of power and authority）”，并以 1661–1710 的分段工程与 1682 迁都形成**宫廷—政府一体化**的宫殿范式；②独立确认 1682 正式成为王室／宫廷驻地、1715 后一度废弃。两源合起来支撑：**凡尔赛是欧洲绝对主义王权宫殿的典型——以宫殿作为权力中枢与礼仪舞台**。**注意**：②为通史性概述，未复述 1661/1710 精确起讫，精确起讫以①官方工程序列为准；①所记 Louis XIII 猎屋（1623–1634）说明该宫非一人一时之作，落地不得写“1661 始建、1710 全部竣工”。

### 2.3 `constructivism`（构成主义）→ **第三国际纪念碑（塔特林塔 / Tatlin's Tower），弗拉基米尔·塔特林，1919–1920，未建成，莫斯科（彼得格勒展出模型）**

- **名称**：第三国际纪念碑 / Monument to the Third International / Pamiatnik III Internatsionala / 塔特林塔（Tatlin's Tower）
- **地点**：**俄罗斯·莫斯科（设计为纪念第三国际；1920 年模型先在彼得格勒、后移至莫斯科工会大厦展出）**（① “the construction of the first Model of the Monument to the Third International in Pétrograd in 1919–20”；“On 8 November, 1920 … Tatlin exhibited a five-metre high model … he relocated it to the Trade Union House in Moscow”）
- **作者**：**弗拉基米尔·塔特林（Vladimir Tatlin，1885–1953）**（①通篇 “Tatlin's constructivism”；② “**Vladimir Tatlin's proposal for the Monument to the Third International (1919)**”）
- **年份**：**1919–1920（设计/模型）**（① “in Pétrograd in **1919–20**”；“On 8 November, **1920** … exhibited a five-metre high model”；②标 “**(1919)**”）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Tate Papers（Tate 美术馆研究期刊，第 8 期；**中—强权威·美术馆同行评议研究**） | `https://www.tate.org.uk/research/tate-papers/08/model-of-vladimir-tatlins-monument-to-the-third-international-reconstruction-as-instrument-of-research-and-states-of-knowledge` | The Model of Vladimir Tatlin's Monument to the Third International: Reconstruction as an Instrument of Research and States of Knowledge – Tate Papers \| Tate | **200**（114,179 B） | “Andersen undertook mainly through T.M. Shapiro, one of Tatlin's assistants for **the construction of the first Model of the Monument to the Third International in Pétrograd in 1919–20**.”；“**On 8 November, 1920, the anniversary of the Revolution, Tatlin exhibited a five-metre high model** in his 'space, materials and construction workshop'.”；“**Although never built, this 400 metre-high tower of glass and steel** spanning the Neva was to rise in a slope of two latticed spirals …”；“a feature which undoubtedly contributed to legitimise Hultén and Andersen's historical speech on the theory ruling **Tatlin's constructivism** as much as it did the reconstruction process” |
| ② | Humanities LibreTexts / Irvine Valley College「Early 20th Century in Europe」（**强权威·大学开放教材平台**） | `https://human.libretexts.org/Courses/Irvine_Valley_College/Grimm_Art_Appreciation_(IVC_ARTH_20)/15%3A_18th-_and_19th-Century_Art-_Realism_to_Impressionism/15.08%3A_Early_20th_Century_in_Europe` | 15.8: Early 20th Century in Europe - Humanities LibreTexts | **200**（198,825 B；搜索结果给出的 13.8 链接 301 至此） | “**The canonical work of Constructivism was Vladimir Tatlin's proposal for the Monument to the Third International (1919)**, **which combined a machine aesthetic with dynamic components celebrating technology such as searchlights and projection screens**.”；“The First Working Group of Constructivists defined Constructivism as the combination of faktura—the particular material properties of an object—…” |

**四要素对位**：名称＝第三国际纪念碑 / Monument to the Third International（①②同一方案）；地点＝俄罗斯（①彼得格勒/莫斯科展出轨迹；②置苏联构成主义语境）；作者＝Vladimir Tatlin（①②一致）；年份＝**1919–1920（①直书 1919–20、1920 模型；②标 1919）**。

**独立性说明**：Tate Papers（美术馆研究期刊）与 Humanities LibreTexts / Irvine Valley College（大学开放教材）为两个不同机构、独立撰稿，均可读、正文直证，可作独立双源。MoMA、Smarthistory 在本环境 403，已改换机构，符合“换更易双源实例”指示。

**对“构成主义”原理的直接支撑**：②是**术语直证**——“**构成主义的典范之作是塔特林为第三国际纪念碑的提案（1919）**”“**结合机器美学与庆祝技术的动态构件（探照灯、投影屏）**”，直接把该作品定性为构成主义代表并说明其手法；①是**作品专属史料**——直书 1919–20 模型制作、1920 年 11 月 8 日五米模型展出、“**虽未建成**、400 米高玻璃与钢铁塔、双螺旋格架 + 四个几何体”，并把它纳入 “Tatlin's constructivism” 的理论脉络。**两源均直接支撑“该作品如何体现构成主义：以工业材料与结构逻辑取代纪念性雕饰、把艺术—建筑—技术合成一体”**，贴合度高，无需保留性标注。**注意**：①的 “never built / 未建成” 是硬事实，落地须写“方案/模型，未建成”，不得写成“已建成的建筑”；地点写“苏联（俄罗斯）”，勿把“为第三国际设计”误写成“位于第三国际总部”。

### 2.4 `functionalism-architecture`（功能主义建筑）→ **萨伏伊别墅（Villa Savoye），勒·柯布西耶（与皮埃尔·让纳雷），1928–1931，法国普瓦西**

- **名称**：萨伏伊别墅及园丁住宅 / Villa Savoye and Gardener's Lodge
- **地点**：**法国普瓦西（Poissy，塞纳河畔）**（① “**Poissy, France, 1928**”；② “Villa Savoye, located in **Poissy, France**”）
- **作者**：**勒·柯布西耶（Le Corbusier）与皮埃尔·让纳雷（Pierre Jeanneret）**（①页面标题即 “**Le Corbusier and Pierre Jeanneret : the Villa Savoye - 1928-1931**”；② “Designed by the influential architect **Le Corbusier**”）
- **年份**：**1928–1931**（①标题直书 “1928-1931”、内文 “Poissy, France, 1928”；②摘要 “Built between **1929 and 1931**”，同页编辑条目引用 “the Villa Savoye (**1929–31**) in Poissy, France”。诚实标注：①以 1928 为设计/委托起点、②以 1929 为施工起点，**落地写 1928–1931（设计—建成），并注明两源起点口径不同**）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Fondation Le Corbusier 官方作品页（**强权威·建筑师官方基金会**） | `https://www.fondationlecorbusier.fr/en?p=15437` | Le Corbusier and Pierre Jeanneret : the Villa Savoye - 1928-1931 | **200**（84,158 B） | 标题 “**Le Corbusier and Pierre Jeanneret : the Villa Savoye - 1928-1931**”；“**Villa Savoye and Gardener's Lodge Poissy, France, 1928**”；“**Villa Savoye was a veritable manifesto, the last of the Purist houses, and it remains the one that best illustrates the "five points of modern architecture"**.”；“…architecture did away with the load-bearing walls of traditional architecture, thus freeing the horizontal layout and the facades …”；“**As at Maison La Roche, the pilotis freed the ground space**, giving the building an air of weightlessness.” |
| ② | Encyclopædia Britannica「Villa Savoye」（**中—强权威·百科全书，含编辑条目引用；见保留标注**，`web_fetch` 服务端直读） | `https://www.britannica.com/place/Villa-Savoye` | Villa Savoye \| Poissy, France \| Britannica | **200**（`web_fetch` 直读；页面 URL 由 `/topic/` 301 至 `/place/`） | “**Villa Savoye, located in Poissy, France, is a renowned example of Modernist architecture. Designed by the influential architect Le Corbusier**, it embodies his concept of a 'house as a machine for living in.' **Built between 1929 and 1931**, the villa is characterized by its **pilotis … ribbon windows, and open floor plan**, all hallmarks of the International Style.”；“**prioritizing functionality** and a new sense of space through modern materials and design principles”；编辑条目引用 “…the International Style is **the Villa Savoye (1929–31) in Poissy, France**.”；“The building's principal block was **raised one story above the ground on pilotis** … floors were cantilevered to permit long strip windows” |

**四要素对位**：名称＝萨伏伊别墅（①②同一作品）；地点＝法国普瓦西（①②直书）；作者＝Le Corbusier + Pierre Jeanneret（①标题直书两人；②写 Le Corbusier）；年份＝**1928–1931（①标题直书；② 1929–31，起点口径不同，已标注）**。

**独立性说明**：Fondation Le Corbusier（建筑师官方基金会）与 Britannica（百科全书编辑团队）为两个不同机构，均可读、正文直证，可作独立双源。

**对“功能主义建筑”原理的直接支撑**：①直书该别墅是**“名副其实的宣言”“最完满说明现代建筑五点”**，并解释底层架空柱（pilotis）“**取消承重墙、释放水平布局与立面、开出长条窗**”“**架空释放地面、赋予失重感**”——这是“形式追随功能、结构服务使用”的机制证据；②直书“**以功能优先（prioritizing functionality）**”“**住宅是居住的机器**”“底层架空柱／带形窗／开放平面”，从百科层面独立确认其现代主义—功能主义定位。**保留标注**：②的 Quick Summary 段自述 “Summary created from Britannica articles using AI”；虽为 Britannica 官方发布并列出所据编辑条目，若 lead 要求“一手编辑撰稿”，应以同页引用的 Britannica 编辑条目（Western architecture / International Style）为准。落地时引②优先用其**编辑条目引用句**。

## 三、汇总

| 条目 | 具名实例 | 地点 | 作者 / 营造主体 | 年份 | 源① | 源② | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `japanese-architecture` | 法隆寺 Hōryū-ji | 日本奈良县斑鸠町 | 推古天皇＋圣德太子发愿（无单一建筑师） | 创建 607；670 火灾后重建（701 两源未直书，不写） | Horyuji Temple 官方史页 | Britannica「Hōryū Temple」 | 200 / 200 | **可用但须标注**：只代表飞鸟时代佛教木构；701 无源，不写 |
| `imperial-architecture` | 凡尔赛宫 Palace of Versailles | 法国凡尔赛 | 路易十四主持营建，历代续建（无单一建筑师） | 1661 起扩建；1699–1710 收尾；1682 为王室驻地 | Château de Versailles 官方 History | Britannica「Palace of Versailles / History」 | 200 / 200 | **可用（①直书 1661、1699–1710、1682；②独立佐证 1682/1715）** |
| `constructivism` | 第三国际纪念碑（塔特林塔） | 俄罗斯（彼得格勒/莫斯科展出） | Vladimir Tatlin | 1919–1920（未建成方案/模型） | Tate Papers 第 8 期研究论文 | Humanities LibreTexts 大学开放教材 | 200 / 200 | **可用（②术语直证“构成主义典范之作”，①史料直证 1919–20/1920/未建成）** |
| `functionalism-architecture` | 萨伏伊 Villa Savoye | 法国普瓦西 | Le Corbusier + Pierre Jeanneret | 1928–1931（②记 1929–31 施工） | Fondation Le Corbusier 官方作品页 | Britannica「Villa Savoye」 | 200 / 200 | **可用但须标注**：② Quick Summary 为 AI 摘要，优先引其编辑条目句；年份起点口径不同 |

- **双源齐备率：4/4**；8 个主来源全部取证成功（2 个经 `web_fetch` 服务端直读，6 个经 `urllib` 直连），**0 死链、0 编造、0 单源、0 不可得**；无需写“仅单源/不可得”。
- **机构独立性**：每条均为两个不同机构，符合“同一机构只算 1 源”。八机构为：Horyuji Temple、Encyclopædia Britannica、Château de Versailles、Tate、Humanities LibreTexts / Irvine Valley College、Fondation Le Corbusier。
- **需落地时保留的诚实标注（5 处）**：
  1. `japanese-architecture`：701 两主源未直书，落地写“607 创建 / 670 后重建”，不写 701；“日本建筑”须限定为“飞鸟时代佛教木构代表例”。
  2. `imperial-architecture`：无单一建筑师，写“路易十四主持、历代续建”；②未复述 1661/1710 精确起讫，精确起讫以①官方工程序列为准。
  3. `constructivism`：必须写“方案/模型，未建成”；勿把“为第三国际设计”误写成“位于第三国际总部”。
  4. `functionalism-architecture`：② Quick Summary 为 AI 摘要，优先引其编辑条目句；年份写 1928–1931 并注明两源起点口径（1928 设计 / 1929 施工）。
  5. 三个 Britannica 页 `urllib` 复抓 403 系反爬，`web_fetch` 服务端直读 200，非死链；UNESCO 660/81/1321、MoMA、Smarthistory 在本环境 403 未作证据，已换机构取证。
- **未做之事**：本报告未修改任何条目数据或其它文件；四条 `sections.实例` 现状仍须由 lead 按第一节“落地约束”另行改写并复跑 `tools/check.py`。

## 四、被拒用来源记录（供后续参考，不作证据）

| URL | 状态 | 处置 |
| --- | --- | --- |
| `https://whc.unesco.org/en/list/660/`（法隆寺） | `web_fetch` 403 / `urllib` 403 | 弃用，改寺院官方 + Britannica |
| `https://whc.unesco.org/en/list/81/`（凡尔赛；正确为 83） | `web_fetch` 403 / `urllib` 403 | 弃用，改宫殿官方 + Britannica |
| `https://whc.unesco.org/en/list/1321/`（柯布作品） | `web_fetch` 403 / `urllib` 403 | 弃用，改基金会官方 + Britannica |
| `https://www.moma.org/collection/works/82800`、`https://www.moma.org/audio/playlist/175/2326` | 403 | 弃用，改 Tate Papers + LibreTexts |
| `https://smarthistory.org/tatlin-tower/` | 403 | 弃用 |
| `https://www.britannica.com/art/Constructivism` | 404（正确为 `/art/constructivism` 不存在） | 弃用，改 LibreTexts |
| `http://ad.ntust.edu.tw/.../homa.20.1.htm`（台科大学生作业页） | 200 但为 Big5 乱码、学生作业非权威 | 弃用（权威级别不足） |

## 五、证据回执（verification-before-completion）

逐条 `norm(quote) in norm(page)` 子串回验结果（`FOUND` 才写入正文）：

| 来源 | 回验句（缩写） | 结果 |
| --- | --- | --- |
| Horyuji 官方 garan | "empress suiko and crown prince shotoku taishi ... building in 607 a temple" / "the world's oldest surviving wooden structures" / "horyuji 1-1 horyuji sannai, ikaruga-cho, ikoma-gun, nara" / "became the first treasure of any kind in japan to be selected by une" | FOUND |
| Britannica Hōryū Temple | "the original horyu temple was built between 601 and 607" / "a fire in 670 destroyed the site, which was subsequently rebuilt and enlarged" / "among the oldest extant wooden structures in the world" / "in the town of ikaruga, northwestern nara" | FOUND（`web_fetch` 全文可见；`urllib` 复抓 403 反爬） |
| 凡尔赛官方 History | "in 1661 shortly after the death of his first minister, he undertook major works" / "took on the role of architect himself" / "the royal chapel in 1699-1710" / "from 1682 it became the main residence" | FOUND |
| Britannica Versailles History | "the palace of versailles was declared the official royal residence in 1682" / "abandoned after the death of louis xiv in 1715" | FOUND（`web_fetch` 全文可见；`urllib` 复抓 403） |
| Tate Papers 08 | "the construction of the first model of the monument to the third international i" / "on 8 november, 1920 ... tatlin exhibited a five-metre high model" / "although never built, this 400 metre-high tower of glass and steel" / "tatlin's constructivism" | FOUND |
| LibreTexts 15.8 | "the canonical work of constructivism was vladimir tatlin's proposal for the monument to the third international (1919)" / "which combined a machine aesthetic with dynamic components celebrating technology such as searchlights and projection screens" | FOUND |
| Fondation Le Corbusier 15437 | "le corbusier and pierre jeanneret : the villa savoye - 1928-1931" / "villa savoye and gardener's lodge poissy, france, 1928" / "villa savoye was a veritable manifesto, the last of the purist houses" / "best illustrates the" + "five points of modern architecture" / "the pilotis freed the ground space" | FOUND |
| Britannica Villa Savoye | "villa savoye, located in poissy, france, is a renowned example of modernist architecture. designed by the influential architect le corbusier" / "built between 1929 and 1931" / "prioritizing functionality" / "the villa savoye (1929–31) in poissy, france" | FOUND（`web_fetch` 全文可见） |

> 校验方法：UTF-8 解码 → 去 script/style/标签 → `html.unescape` → `norm()`（NFKC + 弯直引号/破折号/零宽空格/不间断空格归一 + 空白折叠 + 小写）→ 子串命中。HTML `<title>` 与 HTTP 状态来自同一轮实抓；字节数为响应体原始字节数。Britannica 三页 `urllib` 复抓 403 但 `web_fetch` 服务端直读 200，正文关键句在工具回传全文中逐字可见，已按回执列出。
