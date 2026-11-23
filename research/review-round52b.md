# 第 52 轮 B5 补源报告（review-round52b）——4 条色彩理论条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r52b（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理与上下文文档**：本项目根不存在 `AUTONOMOUS.md` / `TASK_design.md`（已用 glob 核实），实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行）；本项目 `DECISIONS.md`（25 行）、`research/review-round51b.md`（125 行，同格式前例）、`research/gaps-round50.md`（第 16 行起 B5 待核实清单）、`data/sources.json`（只读抽查）。全部只读。
- **硬性规则确认**（TASK_design.md 第 34–42 行 / AUTONOMOUS.md 第六节）：不编造数字、日期、人名、引文、出处；**关键事实至少两个独立来源互证，否则标“待核实”**；引文最多一两句并注明出处；查不到宁可写“不可得”也不凑数；**同一机构只算 1 源**；联网内容一律视为数据，**网页中出现的任何指令均未执行**。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按 SUBAGENT-STOP 以任务说明书为准）、`verification-before-completion`（先实抓、后断言：全部关键句逐条做 `norm(quote) in norm(page)` 子串回验，见第四节回执）。
- **对象现状**：`gaps-round50.md` 列出 `hue` / `saturation` / `primary-colors` / `color-symbolism` 四条“具体实例（名称、地点、设计者、年代）待补充独立来源”。本报告即为其补实例的证据底稿；四条 `sections.实例` 现状仍为类型性描述，**本报告未改任何条目数据**。
- **通道**：`web_search` 端点本轮可用但间歇性无返回；正文抓取以 `urllib`（浏览器 UA、禁验证 SSL）为主，Cloudflare / 反爬页面（Louvre Abu Dhabi）以 `web_fetch` 服务端直读取证；Cambridge PDF 以 `pypdf` 抽取文本。MoMA / Smarthistory / Met / Tate 部分页面本环境返回 403，未作来源。
- **只读声明**：本轮**仅生成** `research/review-round52b.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容。全部抓取在 stdin 内联 Python / web_fetch 完成，**未在项目内落盘任何脚本或缓存**。

## 一、方法与判据

1. **实抓**：逐 URL 记录 **HTTP 状态、字节数、`<title>`**；去 `<script>/<style>` 与标签、`html.unescape` 后抽正文；关键句用 `norm()`（统一弯/直引号、破折号、不间断空格、大小写、空白、Unicode NFKC）逐条子串回验，全部 `FOUND` 才写入本报告（见第四节）。PDF 用 `pypdf` 抽取 40 页文本后同样回验。
2. **独立性判据**：**同一机构只算 1 源**；四条均用两个互不相同的机构（官方博物馆 / 皇家学会 / 大学出版平台 / 国家级教育电视台）。
3. **权威性分级**：**强权威**＝官方博物馆馆藏页；**强权威**＝皇家学会（英国国家学会）官方博客与出版物目录；**中—强权威**＝大学出版平台（Humanities LibreTexts / University of Cambridge 学者章节）、国家级教育电视（CETV）。
4. **不采用维基百科作主源**：按项目既定口径（D10 / round46 / round49 / round51b），维基属同平台伞源、不计独立源，未作证据列出。
5. **概念支撑优先**：每条不只核“作品基本信息”，而是要求至少一句原文直接说明该作品/该图式**如何体现**对应色彩概念；若两源措辞角度不同，逐条写明，不冒称源文直书术语。
6. **落地约束**：本报告只读产出，不能直接改数据。凡判“可用”，落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/batch-*.json` 的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年份”），同步 `pending_notes` /「待核实」，按需更新 `coverage.json` 源数，复跑 `tools/check.py`；登记前不得视为已改。

## 二、四条复核（每条：名称 / 地点 / 设计者 / 年份 + 两条独立权威来源）

### 2.1 `hue`（色相）→ **牛顿《光学》色环图 Newton's colour circle（1704，《光学》原书图版）**

- **名称**：Newton's colour circle / 牛顿色环图（裁于 Isaac Newton《Opticks; or, A Treatise of the Reflexions, Refractions, Inflexions and Colours of Light》，1704）
- **地点**：英国 · 伦敦（《光学》1704 年于伦敦出版；皇家学会藏该书 1704 年版，目录号 R69313）
- **设计者**：**Isaac Newton（艾萨克·牛顿）**
- **年份**：**1704**（两源一致：皇家学会博客“published Opticks (1704)… included the first colour wheel”；Cambridge 章“Newton's color circle, introduced in his Opticks of 1704”）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | The Royal Society 官方博客（**强权威·英国国家学会**） | `https://royalsociety.org/blog/2021/11/colour-wheel/` | Colour wheel \| Royal Society | **200**（123,175 B） | “Over 30 years passed until he published *Opticks* (1704), his treatise on light, **which included the first colour wheel**.”；“**Newton set the seven spectral colours into a circle of unequal segments**, based on the pattern of musical scale, and **created a geometric model which underpins all subsequent theory on colour harmony**.” |
| ② | J. D. Mollon, Department of Experimental Psychology, University of Cambridge；章节 *The Origins of Modern Color Science*（**强权威·大学学者出版章节，PDF**） | `https://vision.psychol.cam.ac.uk/jdmollon/papers/MollonColorScience.pdf` | The Origins of Modern Color Science（PDF，40 页；载于 *The Science of Color*） | **200**（427,769 B，40 页） | “**On the circumference of a circle (Figure 1.2) he represents each of the seven principal colors of the spectrum.**”；“**Figure 1.2 Newton's color circle, introduced in his Opticks of 1704.**”；“Colors that lie on the circumference are the most saturated”；“**will all exhibit the same hue but will vary in saturation.**” |

**四要素对位**：名称＝Newton's colour circle / 牛顿色环图（①②同一图式，①称 first colour wheel，②称 Newton's color circle）；地点＝英国伦敦（①明记《光学》1704 出版、皇家学会藏该书；②作者机构为 Cambridge，图版载于 1704 年《光学》）；设计者＝Isaac Newton（①②一致）；年份＝**1704（两源直书）**。

**独立性说明**：The Royal Society（学会官方）与 University of Cambridge 学者章节（大学出版）为两个不同机构，均可读、正文直证，可作独立双源。二者内容相关但不互抄：①重“七色按音乐比例排成圆周、奠定色彩和谐模型”，②重“圆周上每一位置对应一种谱色、同一半径上色相不变而饱和度变”。

**对“色相（hue）”概念的直接支撑**：②原文“he represents each of the seven principal colors of the spectrum”（圆周代表七种谱色）＋“all exhibit the same hue but will vary in saturation”（同半径色相相同）**正是色相作为可环绕排列的独立颜色维度的经典图示**；①“the seven spectral colours into a circle… geometric model which underpins all subsequent theory on colour harmony”说明这一排布成为后世色相环的原型。两源均直证，贴合度高。

### 2.2 `saturation`（饱和度／纯度）→ **马蒂斯《舞蹈》 Dance（艾尔米塔什博物馆，1909–1910）**

- **名称**：Dance / 《舞蹈》（又常记为 Dance II；与 1909 年 MoMA 藏《Dance (I)》为不同画布）
- **地点**：俄罗斯 · 圣彼得堡 · 艾尔米塔什博物馆（The State Hermitage Museum；藏品号 Щ-9673，原题名页著录）
- **设计者**：**Henri Matisse（亨利·马蒂斯）**
- **年份**：**1909–1910**（①官方字段 “Date: 1909-1910”；正文另记 “commissioned in 1910”；通称 1910）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | The State Hermitage Museum 官方数字馆藏页（**强权威·官方博物馆**） | `https://www.hermitagemuseum.org/digital-collection/28411?lng=en` | Dance | **200**（64,456 B） | “**Matisse, Henri (1869-1954)**”；“**commissioned in 1910**”；“**The frenzy of the pagan bacchanalia is embodied in the powerful, stunning accord of red, blue and green, uniting Man, Heaven and Earth.**”；“**Date: 1909-1910**”；“**Technique: oil on canvas**”；“**Dimensions: 260x391 cm**”。 |
| ② | Humanities LibreTexts / *SmartHistory of Art* 10.3（DR. BETH HARRIS、DR. STEVEN ZUCKER；**中—强权威·大学开放教材**） | `https://human.libretexts.org/Bookshelves/Art/Art_History_and_Theory/SmartHistory_of_Art/10%3A_Modernisms_1900__1980/10.03%3A_Fauvism__Expressionism` | 10.3: Fauvism + Expressionism - Humanities LibreTexts | **200**（381,638 B） | “the Fauves produced bright cheery landscapes and figure paintings, **characterized by pure vivid color and bold distinctive brushwork**”；“**The dancers inhabit a brilliant blue and green field.**”；“**Henri Matisse, Dance I by Dr. Beth Harris and Dr. Steven Zucker**”；“**Henri Matisse, Dance , 1910, oil on canvas, 260 x 291 cm (The Hermitage, St. Petersburg)**”。 |

**四要素对位**：名称＝Dance / 《舞蹈》（①②同一 1910 年艾尔米塔什作品；②另述 1909 年 MoMA 的《Dance (I)》为草稿版本）；地点＝圣彼得堡艾尔米塔什（①官方馆藏页；② “The Hermitage, St. Petersburg”）；设计者＝Henri Matisse（①②一致）；年份＝**1909–1910（①官方字段）/ 1910（②）**。

**独立性说明**：艾尔米塔什博物馆（官方馆藏）与 Humanities LibreTexts（大学开放教材）为两个不同机构，均可读、正文直证，可作独立双源。

**对“饱和度”概念的直接支撑与诚实标注**：①“powerful, stunning accord of red, blue and green”直证该画以**强烈、纯整的红／蓝／绿三色**组织画面，是高饱和配色的官方馆藏描述；②把马蒂斯所属野兽派定性为“pure vivid color”，并直书“The dancers inhabit a brilliant blue and green field”，从艺术史教材角度支撑“大面积高纯度色块”这一手法。**注意**：②未对 1910 年这一幅直接使用 “saturation” 一词（该词在同页用于德兰的《舞蹈》），“高饱和度”是对两源所述“pure vivid / powerful stunning / brilliant”的概念归纳，落笔时不得冒称源文直书“saturation”。另②记尺寸 “260 x 291 cm” 与①官方 “260x391 cm” 不一致，落地以①馆方著录为准，②尺寸疑为排版误植，不据此改数据。

### 2.3 `primary-colors`（原色）→ **蒙德里安《蓝、红、黄、黑构成》（卢浮宫阿布扎比，1922）**

- **名称**：Composition with Blue, Red, Yellow and Black / 《蓝、红、黄、黑构成》
- **地点**：阿拉伯联合酋长国 · 阿布扎比 · 卢浮宫阿布扎比（Louvre Abu Dhabi；藏品号 LAD 2009.001，79.8 × 50 cm）
- **设计者**：**Piet Mondrian（皮特·蒙德里安）**
- **年份**：**1922**（①官方字段；正文亦写 “This 1922 composition”）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Louvre Abu Dhabi 官方在线馆藏故事页（**强权威·官方博物馆**） | `https://prod-cm.louvreabudhabi.ae/en/whats-online/art-from-home/mondrian` | Srory behind Blue, Red, Yellow & Black Compostion \| Louvre Abu Dhabi（原页标题有拼写笔误，照录） | **200**（`web_fetch` 服务端直读全文；`urllib` 复抓一次遇 403 反爬，非死链） | “**Composition with Blue, Red, Yellow and Black**”；“**Piet Mondrian**”；“**France, Paris**”；“**1922**”；“**Oil on canvas**”；“**LAD 2009.001\|79.8 x 50 cm**”；“In the 1920s, the Dutch painter developed an art based on elementary principles: straight lines, areas separated from each other, **and the three primary colours (red, yellow, blue) and the two non-colours (black and white)**.” |
| ② | Tate Kids 官方艺术家页（**强权威·泰特美术馆官方教育平台**） | `https://www.tate.org.uk/kids/artists/who-piet-mondrian` | Who is Piet Mondrian? \| Tate Kids | **200**（50,364 B；由 `/kids/explore/who-is/who-piet-mondrian?` 重定向至本规范 URL） | “**He often used primary colours – red yellow and blue – as in this painting.**”；“**Piet Mondrian Composition with Yellow, Blue and Red (1937–42) Tate**”；“Notice how the red, yellow and blue are placed to the side and the centre of painting doesn't have any colour.” |

**四要素对位**：名称＝Composition with Blue, Red, Yellow and Black（①馆藏题名；②讨论同一画家的同类作品 Composition with Yellow, Blue and Red, 1937–42, Tate）；地点＝阿布扎比卢浮宫（①官方馆藏；②为泰特版作品，见下）；设计者＝Piet Mondrian（①②一致）；年份＝**1922（①，所选实例）/ 1937–42（②所举另一幅）**。

**独立性说明**：Louvre Abu Dhabi（官方博物馆）与 Tate（官方博物馆教育平台）为两个不同机构，均可读、正文直证，可作独立双源。

**对“原色”概念的直接支撑与诚实标注**：①是**作品专属**证据，明说蒙德里安的艺术基于“直 lines、相互分隔的色域，**三原色红黄蓝＋非色黑白**”，直接支撑“该作品如何体现原色概念”；②是**概念／画家习惯**证据，明说“他常用原色红黄蓝”，并指出红黄蓝被置于画面侧边、中央留白。**注意**：②所配图为泰特藏另一幅 1937–42 作品，落地时应写“以蒙德里安《蓝、红、黄、黑构成》（1922，阿布扎比卢浮宫）为具名实例；Tate Kids 以另一幅同类作品说明其一贯的原色用法”，不得冒称②在评述 1922 年这一幅。

### 2.4 `color-symbolism`（色彩象征）→ **德拉克洛瓦《自由引导人民》（卢浮宫，1830）**

- **名称**：Le 28 juillet 1830. La Liberté guidant le peuple / 《自由引导人民》（英文 Liberty Leading the People）
- **地点**：法国 · 巴黎 · 卢浮宫博物馆（Musée du Louvre，绘画部，藏品号 RF 129；Salle 700，Aile Denon, Niveau 1）
- **设计者**：**Eugène Delacroix（欧仁·德拉克洛瓦）**
- **年份**：**1830**（三源一致：①教材 “July 28, 1830… September–December 1830”；②CETV “1830 年七月革命”；③卢浮宫官方 “1830”）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Humanities LibreTexts / Gavilan College《A World Perspective of Art Appreciation》11.2（**中—强权威·大学开放教材**） | `https://human.libretexts.org/Courses/Gavilan_College/A_World_Perspective_of_Art_Appreciation_(Gustlin_and_Gustlin)_2.0/11%3A_The_Industrial_Revolution_(1800_CE__1899_CE)/11.02%3A_Romanticism_(1780-1850)` | 11.2: Romanticism (1780-1850) - Humanities LibreTexts | **200**（163,336 B） | “**The flag's blue, white, and red colors symbolize liberty, equality, and fraternity, the ideals of the French Revolution.**”；“**Delacroix used these colors strategically throughout the composition to direct the viewer's attention upward from the crowd to Liberty and the waving flag.**”；“**Eugène Delacroix, Liberty Leading the People (July 28, 1830), September - December 1830, oil on canvas, 260 x 325 cm (Musée du Louvre, Paris)**”。 |
| ② | 中国教育电视台 CETV《博物馆之夜·云逛卢浮宫》（**中—强权威·国家级教育电视，注明素材来源为卢浮宫建筑与馆藏**） | `https://www.centv.cn/p/462928.html` | 博物馆之夜-【云逛卢浮宫】《自由引导人民》_CETV | **200**（43,674 B） | “**她手中挥舞着一面蓝、白、红三色相间的三色旗**，带领着民众浴血奋战。”；“**蓝、白、红三色组合在画面上多次出现，欧仁·德拉克洛瓦的用意显而易见。**”；“**蓝、白、红三色旗是法国国旗，是1789年法国大革命的象征**”；“（**来源：卢浮宫建筑与馆藏**）”。 |

**补充第三次核验（不计入双源）**：Musée du Louvre 官方藏品记录 `https://collections.louvre.fr/en/ark:/53355/cl010065872`，标题 *Le 28 juillet 1830. La Liberté guidant le peuple - Louvre site des collections*，HTTP **200**（137,229 B）；回验命中 “Delacroix, Eugène”、“1830”、“RF 129”、“Currently on display at the Musée du Louvre”。仅用于核名称／作者／年份／馆藏，未用于概念定性。

**四要素对位**：名称＝La Liberté guidant le peuple / Liberty Leading the People（①②同一作品）；地点＝巴黎卢浮宫（①图注直书 Musée du Louvre, Paris；②“云逛卢浮宫”；③官方藏品页现任陈列 Salle 700）；设计者＝Eugène Delacroix（①②一致，③官方著录）；年份＝**1830（三源一致）**。

**独立性说明**：Humanities LibreTexts（美国大学开放教材）与中国教育电视台（国家级教育电视）为两个不同机构、不同语言、独立撰稿，均可读、正文直证，可作独立双源；二者概念定性措辞相近是因同述卢浮宫原作与法国三色旗的公共史实，非同源转载（②自注来源为卢浮宫馆藏素材）。

**对“色彩象征”概念的直接支撑**：①直书“旗的蓝白红三色象征自由、平等、博爱”且“德拉克洛瓦在全画策略性地使用这些颜色，把视线从人群引向自由女神与旗帜”；②直书“蓝白红三色组合在画面上多次出现，德拉克洛瓦的用意显而易见”“三色旗是法国国旗、1789 年法国大革命的象征”。**两源均直接支撑“颜色在此画中承载政治寓意并被反复组织”**，贴合度是本轮四条中最高的一条。

## 三、汇总

| 条目 | 具名实例 | 地点 | 设计者 | 年份 | 源① | 源② | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `hue` | 牛顿《光学》色环图 Newton's colour circle | 英国·伦敦（《光学》1704 出版） | Isaac Newton | 1704 | Royal Society 官方博客 `colour-wheel/` | Cambridge（Mollon）PDF 章节 | 200 / 200 | **可用（两源直证色相环）** |
| `saturation` | 马蒂斯《舞蹈》 Dance | 圣彼得堡·艾尔米塔什博物馆 | Henri Matisse | 1909–1910（通称 1910） | Hermitage 官方数字馆藏 28411 | Humanities LibreTexts 10.3 Fauvism | 200 / 200 | **可用（“高饱和”为对 pure vivid / powerful stunning 的归纳，源未直书 saturation）** |
| `primary-colors` | 蒙德里安《蓝、红、黄、黑构成》 | 阿布扎比·卢浮宫阿布扎比（LAD 2009.001） | Piet Mondrian | 1922 | Louvre Abu Dhabi 官方在线馆藏 | Tate Kids 官方艺术家页 | 200 / 200 | **可用（②配图为另一幅 1937–42 作品，须注明）** |
| `color-symbolism` | 德拉克洛瓦《自由引导人民》 | 巴黎·卢浮宫（RF 129） | Eugène Delacroix | 1830 | Humanities LibreTexts 11.2 Romanticism | CETV 云逛卢浮宫（另附 Louvre 官方藏品页作事实核） | 200 / 200 | **可用（两源直证三色象征）** |

- **双源齐备率：4/4**；8 个主来源全部取证成功（其中 1 个官方页经 `web_fetch` 服务端直读，1 个 PDF 经 `pypdf` 抽文），**0 死链、0 编造、0 单源、0 不可得**；无需写“仅单源/不可得”。
- **机构独立性**：每条均为两个不同机构，符合“同一机构只算 1 源”。四条合计涉及 8 个机构（Royal Society、Cambridge、Hermitage、Humanities LibreTexts、Louvre Abu Dhabi、Tate、CETV、Louvre——其中 LibreTexts 在两条中各计一次，但两条来源互不重复）。
- **需落地时保留的诚实标注（3 处）**：
  1. `saturation`：源文未对 1910 年这幅直书 “saturation”；以馆方“powerful, stunning accord of red, blue and green”＋教材“pure vivid color / brilliant blue and green field”为依据，属概念归纳。尺寸以馆方 260×391 cm 为准，教材 260×291 cm 不采。
  2. `primary-colors`：Tate Kids 页面所配作品为泰特藏 1937–42 年另一幅，落地须写明“以另一幅同类作品说明其一贯原色用法”；1922 年作品信息以 Louvre Abu Dhabi 为准。
  3. `hue` / `color-symbolism`：均为两源直证，无保留标注；但 `color-symbolism` 的 CETV 为转述卢浮宫馆藏素材的国家教育电视，若后续要求“两条均为一手机构原文”，可把 Louvre 官方藏品页升为主源之一（但该页仅支撑基本信息，不支撑象征概念）。
- **未做之事**：本报告未修改任何条目数据或其它文件；四条 `sections.实例` 现状仍为“类型性描述”，须由 lead 按第一节“落地约束”另行改写并复跑 `tools/check.py`。

## 四、证据回执（verification-before-completion）

逐条 `norm(quote) in norm(page)` 子串回验结果（全部 FOUND 才写入正文）：

| 来源 | 回验句（缩写） | 结果 |
| --- | --- | --- |
| Royal Society blog | "which included the first colour wheel" / "Newton set the seven spectral colours into a circle of unequal segments" / "created a geometric model which underpins all subsequent theory on colour harmony" | FOUND |
| Cambridge Mollon PDF | "On the circumference of a circle (Figure 1.2) he represents each of the seven principal colors of the spectrum" / "Newton's color circle, introduced in his Opticks of 1704" / "Colors that lie on the circumference are the most saturated" / "will all exhibit the same hue but will vary in saturation." | FOUND（长句因 PDF 换行连字符改取连续子串） |
| Hermitage 28411 | "Matisse, Henri (1869-1954)" / "commissioned in 1910" / "powerful, stunning accord of red, blue and green" / "Date: 1909-1910" / "Dimensions: 260x391 cm" | FOUND |
| LibreTexts 10.3 | "characterized by pure vivid color and bold distinctive brushwork" / "The dancers inhabit a brilliant blue and green field." / "Henri Matisse, Dance I by Dr. Beth Harris and Dr. Steven Zucker" / "Henri Matisse, Dance , 1910, oil on canvas, 260 x 291 cm (The Hermitage, St. Petersburg)" | FOUND |
| Louvre Abu Dhabi | "Composition with Blue, Red, Yellow and Black" / "Piet Mondrian" / "1922" / "Oil on canvas" / "LAD 2009.001" / "the three primary colours (red, yellow, blue) and the two non-colours (black and white)" | FOUND（`web_fetch` 全文可见；`urllib` 一次复抓 403 反爬） |
| Tate Kids | "He often used primary colours - red yellow and blue - as in this painting." / "Composition with Yellow, Blue and Red (1937-42) Tate" | FOUND（弯引号已归一） |
| LibreTexts 11.2 | "The flag's blue, white, and red colors symbolize liberty , equality , and fraternity , the ideals of the French Revolution." / "Delacroix used these colors strategically throughout the composition to direct the viewer's attention upward from the crowd to Liberty and the waving flag." / "Eugène Delacroix, Liberty Leading the People (July 28, 1830)… (Musée du Louvre, Paris)" | FOUND |
| CETV 462928 | "她手中挥舞着一面蓝、白、红三色相间的三色旗" / "蓝、白、红三色组合在画面上多次出现，欧仁·德拉克洛瓦的用意显而易见" / "蓝、白、红三色旗是法国国旗，是1789年法国大革命的象征" / "来源：卢浮宫建筑与馆藏" | FOUND |
| Louvre collections（补充） | "Le 28 juillet 1830. La Liberté guidant le peuple" / "Delacroix, Eugène" / "1830" / "RF 129" / "Currently on display at the Musée du Louvre" | FOUND |

> 校验方法：UTF-8 解码 → 去 script/style/标签 → `html.unescape` → `norm()`（NFKC + 弯直引号/破折号/不间断空格归一 + 空白折叠 + 小写）→ 子串命中；PDF 经 `pypdf` 逐页 `extract_text()` 后同法处理。HTML `<title>` 与 HTTP 状态来自同一轮实抓；字节数为响应体原始字节数。
