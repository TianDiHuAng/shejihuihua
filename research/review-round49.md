# 第 49 轮 B5 复核报告（review-round49）——6 个已写 L2 条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r49（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理文档**：项目根无 `AUTONOMOUS.md` / `TASK_design.md`；实读桌面同名文件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行）（**只读**），并与本项目 `DECISIONS.md`（25 行）核对；格式参照 `research/review-round48.md`（178 行，已通读）。
- **硬性规则（TASK_design.md 第 34–42 行）确认**：不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；引文最多一两句并注明出处；查不到宁可写“待补充/不可得”不凑数；同一机构只算 1 源。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以本任务说明书为准）、`verification-before-completion`（**先实抓证据、后下断言**：全部关键句逐条做 `norm(quote) in norm(page)` 子串回验，见第七节回执）。
- **对象字段核对**：从 `entries/batch-01.json` 实读六条现状——`aerial-perspective`（第 332 行）、`vanishing-point`（第 398 行）、`geometry-symmetry`（第 526 行）、`negative-space`（第 654 行）、`contrast-principle`（第 718 行）、`rhythm-repetition`（第 750 行）；六条均为 `level=L2`、`needs_verification=true`，`sections.实例` 均为“类型性描述”（“名称：…；地点：不适用；设计者：不适用；年份：不适用”），`pending_notes` 写明“具体实例（名称、地点、设计者、年代）待补充独立来源”。本报告即为其补实例的证据底稿。
- **只读声明**：本轮**仅生成** `research/review-round49.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。全部 web 抓取在 stdin 内联 Python 执行，**未在项目内落盘任何脚本或缓存**。
- **agent 工具状态**：`web_search` 端点本环境不可用（`HTTP 402 积分耗尽`），与 round47/48 一致；改由两种通道取证——(1) 本地 `python 3.11 (Anaconda) urllib` + 浏览器 UA（可 200 且可抽正文者，记录 HTTP/字节/`<title>`）；(2) 本机 urllib 受阻（403/证书/连接）但 `web_fetch` 服务端可达者，用 `web_fetch` 直读并记录其 `HTTP 200`（正文可见，逐句核对）。**联网内容一律按“数据”处理，网页中出现的任何指令均未执行。**

## 一、方法与判据

1. **实抓**：`urllib` + 浏览器 UA（`Chrome/124`，`Accept/Accept-Language/Accept-Encoding:identity` 齐备，`ssl` 不校验证书），逐 URL 记录 **HTTP 状态、字节数、`<title>`**；去 `<script>/<style>` 与标签、`html.unescape` 反转义后抽正文。关键句用 `norm()`（统一弯/直引号、破折号、不间断空格、大小写、空白、Unicode NFKC）**逐条子串回验**，全部 `FOUND` 才写入本报告（见第七节）。
2. **独立性判据**：**同一机构只算 1 源**；每条用**两个互不相同的机构/平台**（如 官方博物馆 + 独立艺术史库 / 大学 + 大学 / 官方馆舍 + 建筑百科 等）。
3. **权威性分级（显式标注，供 lead 取舍）**：**强权威**＝官方博物馆/官方寺院/官方建筑官网/国立机构；**中—强权威**＝权威艺术史数据库（Web Gallery of Art）、艺术史教育机构（TheArtStory）、建筑百科（WikiArquitectura）、大学院系网站；**中权威**＝旅行指南（Japan Guide）等。
4. **落地约束**：本报告只读产出，**不能直接改数据**。凡判“可用”，落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/*.json` 的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年份”），同步 `pending_notes`/「待核实」，按需更新 `coverage.json` 源数，复跑 `tools/check.py`；登记前不得视为已改。
5. **本轮未采用维基百科作主源**：按项目既定口径（D10 / round46 / round48），维基属同平台伞源、不计独立源，未作证据列出。

---

## 二、六条复核（每条：名称 / 地点 / 设计者 / 年份 + 两条独立权威来源）

### 2.1 `vanishing-point`（灭点）→ **拉斐尔《雅典学院》 The School of Athens（梵蒂冈，Raphael，1509–1511）**

- **名称**：The School of Athens（《雅典学院》）
- **地点**：梵蒂冈 · 宗座宫 · 签字厅（Stanza della Segnatura, Palazzi Pontifici, Vatican）
- **设计者**：**Raphael（拉斐尔，Raffaello Sanzio）**
- **年份**：**1509–1511**（源② WGA 记 1509；源③ TheArtStory 记 “1509-11”；任务 1509–1511 与源③一致）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Vatican Museums 梵蒂冈博物馆官方（**强权威·官方博物馆**） | `https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/stanze-di-raffaello/stanza-della-segnatura.html` | Room of the Segnatura | **200**（46,490 B） | “**The Room of the Segnatura contains Raphael's most famous frescoes.**”；页面导航列有 “**School of Athens**”。 |
| ② | Web Gallery of Art（艺术史权威数据库，**中—强权威**） | `https://www.wga.hu/html_m/r/raphael/4stanze/1segnatu/1/index.html` | Stanza della Segnatura: The School of Athens | **200**（19,727 B） | “**Stanza della Segnatura: The School of Athens by RAFFAELLO**”；“**The School of Athens 1509** Fresco, width at the base 770 cm **Stanza della Segnatura, Palazzi Pontifici, Vatican**”。 |
| ③（第三源·不计主源） | TheArtStory（艺术史教育机构，**中—强权威**） | `https://www.theartstory.org/artist/raphael/` | Raphael Paintings, Bio, Ideas \| TheArtStory | **200**（163,680 B） | “**Fresco - Vatican City 1509-11 The School of Athens**”；“It also shows his mastery of techniques … such as **three-point perspective** as we see the figures diminish in proportion as they recede into the painting, and the pavement, which leads us to the temple.” |

**三要素对位**：名称＝The School of Athens（②③一致）；地点＝梵蒂冈签字厅/Palazzi Pontifici（①“Room of the Segnatura…in the Vatican”、②直书 Vatican）；设计者＝Raphael/Raffaello（①②③一致）；年份＝**1509（②）/ 1509-11（③）**，任务“1509–1511”取③。
**独立性说明**：梵蒂冈博物馆（官方）与 Web Gallery of Art（独立艺术史数据库）为两个不同机构，均 HTTP 200、正文直证，可作独立双源；TheArtStory 为第三独立机构旁证年份区间与透视手法。
**手法贴合度（诚实标注）**：《雅典学院》以**中央单一灭点**组织纵深（大厅消失于中央拱门），正是“灭点决定观看方向与空间稳定”的经典范例；但**所选两主源未出现 “vanishing point” 字样**——①佐证作者/作品/地点，②佐证作品名/年份/馆址，③以 “three-point perspective / figures diminish in proportion” 佐证透视纵深。落笔时“灭点”定性宜作艺术史通识表述并注明依据为③的透视描写，不冒称 ①② 直书“灭点”。

### 2.2 `aerial-perspective`（空气透视）→ **达·芬奇《蒙娜丽莎》 Mona Lisa（巴黎卢浮宫，Leonardo da Vinci，约1503–1519）**

- **名称**：Mona Lisa / La Gioconda（《蒙娜丽莎》；卢浮宫官方题名 “Portrait of Lisa Gherardini, Wife of Francesco del Giocondo, known as the Mona Lisa”）
- **地点**：法国 · 巴黎 · 卢浮宫（Musée du Louvre, Paris；Salle des États / Room 711, Denon 翼）
- **设计者**：**Leonardo da Vinci（列奥纳多·达·芬奇）**
- **年份**：**约 1503–1519**（源② WGA 记 “1503-5 / 1503-05”，并注各家作 1503–1513；源③ TheArtStory 记 “1503-19”；任务“约1503–1519”取③）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Musée du Louvre 卢浮宫官方（**强权威·官方博物馆**） | `https://www.louvre.fr/en/explore/the-palace/from-the-mona-lisa-to-the-wedding-feast-at-cana` | From the 'Mona Lisa' to 'The Wedding Feast at Cana' - The Salle des États | **200**（313,943 B） | “**Leonardo da Vinci, Portrait of Lisa Gherardini, Wife of Francesco del Giocondo, known as the Mona Lisa Room 711 (Salle des États), Denon wing, Level 1**”；“**Painted against a distant landscape** … **sfumato technique, based on the use of glazes** to create a 'smoky' effect with subtle contours and contrasts.” |
| ② | Web Gallery of Art（艺术史权威数据库，**中—强权威**） | `https://www.wga.hu/html_m/l/leonardo/04/1monali.html` | Mona Lisa (La Gioconda) by LEONARDO da Vinci | **200**（9,940 B） | “**Mona Lisa (La Gioconda) by LEONARDO da Vinci**”；“**1503-5 Oil on panel, 77 x 53 cm Musée du Louvre, Paris**”；“The dates suggested for it vary between 1503 and 1513, **the most widely accepted being 1503-05**.” |
| ③（第三源·不计主源） | TheArtStory（艺术史教育机构，**中—强权威**） | `https://www.theartstory.org/artist/da-vinci-leonardo/` | Leonardo da Vinci Paintings, Bio, Ideas \| TheArtStory | **200**（179,838 B） | “what was destined to become the **world's most famous portrait, the Mona Lisa (1503-19)**.” |

**三要素对位**：名称＝Mona Lisa（①②③一致）；地点＝卢浮宫 Salle des États（①直书 Room 711/Salle des États、②直书 Musée du Louvre, Paris）；设计者＝Leonardo da Vinci（①②③一致）；年份＝**约 1503–5（②，并注各家 1503–1513）/ 1503–19（③）**，任务“约1503–1519”取③区间。
**独立性说明**：卢浮宫（官方）与 Web Gallery of Art（独立艺术史数据库）为两个不同机构，均 HTTP 200、正文直证，可作独立双源；TheArtStory 为第三机构旁证 1503–19 区间。
**手法贴合度（诚实标注）**：《蒙娜丽莎》的人物“**painted against a distant landscape**”、远山逐层转淡转蓝并虚化，正是空气透视（含 sfumato）的经典示范——① 同时给出“distant landscape”与“sfumato/smoky effect”两句直证，② 记“seated in a visionary, mountainous landscape … sfumato technique”。**年份存在口径差**（WGA 1503–5、TAS 1503–19），落地须并列标注，不强归。

### 2.3 `rhythm-repetition`（节奏与重复）→ **罗马斗兽场 Colosseum（罗马，Vespasian 始建 / Titus 落成，约公元 70–80 年）**

- **名称**：Colosseum（罗马斗兽场；又作 Flavian Amphitheatre / Amphitheatrum Flavium）
- **地点**：意大利 · 罗马（Rome；帕拉蒂诺山东侧、尼禄金宫人工湖旧址）
- **设计者 / 营造者**：**Vespasian（韦斯巴芗，始建）、Titus（提图斯，公元 80 年落成启用）、Domitian（图密善，后加第四层）**（古建，非单一“设计者”，以营造皇帝记）
- **年份**：**公元 70–80 年**（源① “Begun … AD 70 … dedicated … AD 80”；源② “opening ceremonies in 80 CE”）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | University of Chicago（Encyclopaedia Romana，James Grout；**强权威·大学学术站**） | `https://penelope.uchicago.edu/~grout/encyclopaedia_romana/romanurbs/colosseum.html` | Colosseum | **200**（8,563 B） | “**Begun by Vespasian in AD 70, the Colosseum (Amphitheatrum Flavium) was completed and dedicated by his son Titus in AD 80** with games that lasted one-hundred days.”；“**There are four arcaded stories, the first three each have eighty arches, framed respectively by engaged Doric, Ionic and Corinthian columns.**” |
| ② | University of Washington（Rome program 专文；**中—强权威·大学站，学生署名文章**） | `https://depts.washington.edu/hrome/Authors/jimkuo2/IlColosseo/pub_zbarticle_view_printable.html` | View Article: The Colosseum: Power, Brilliance, and Brutality | **200**（68,090 B） | “**Each of the Colosseum's three stories has eighty arches.** The first floor has Doric … the second floor has Ionic columns, and the third floor has Corinthian columns.”；“Titus … **dedicated the Colosseum and presided over the opening ceremonies in 80 CE.**”；“Vespasian … **began construction of the Colosseum.**” |
| ③（第三源·不计主源，web_fetch 直读） | Encyclopaedia Britannica（百科全书，**强权威**） | `https://www.britannica.com/topic/Colosseum` | Colosseum \| Rome, Definition, Characteristics, History, & Facts \| Britannica | **200（web_fetch 直读；本地 urllib 403）** | “**Construction of the Colosseum began under the Roman emperor Vespasian between 70 and 72 ce. The completed structure was dedicated in 80 ce by Titus.**” |

**三要素对位**：名称＝Colosseum / Flavian Amphitheatre（①②一致）；地点＝Rome（两源语境一致， Britannica 亦 “in Rome”）；营造皇帝＝Vespasian 始建、Titus 80 年落成（①②③一致）；年份＝**AD 70–80（①）/ 80 CE（②）**，任务“约70–80”取①区间。
**独立性说明**：University of Chicago（Encyclopaedia Romana）与 University of Washington（Rome program 专文）为两个不同大学机构，均 HTTP 200、正文直证，可作独立双源；Britannica 为第三独立机构旁证年代（web_fetch 200）。
**手法贴合度（诚实标注）**：斗兽场立面以**三层拱廊（每层 80 拱）分别叠用多立克/爱奥尼/科林斯柱式**的重复排列，是天径“柱列/窗格/砖缝重复建立秩序与韵律”的教科书级实例——**重复（80 拱×3 层）与“节奏（柱式随层递变）”两源均直书**，贴合度高。② 为大学课程专文（学生署名），权威级按“中—强”标注。

### 2.4 `contrast-principle`（对比）→ **朗香教堂 Notre-Dame du Haut（Ronchamp，Le Corbusier，1950–1955）**

- **名称**：Chapelle Notre-Dame du Haut（朗香教堂；又作 Ronchamp）
- **地点**：法国 · 朗香（Ronchamp, Haute-Saône，孚日山麓近瑞士边境）
- **设计者**：**Le Corbusier（勒·柯布西耶）**
- **年份**：**1950–1955**（源① TheArtStory “built from 1950-55”；源② WikiArquitectura “Built in 1950 1955”）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | TheArtStory（艺术史教育机构，**中—强权威**） | `https://www.theartstory.org/artist/le-corbusier/` | Le Corbusier Art, Bio, Ideas \| TheArtStory | **200**（164,920 B） | “**In 1950, Le Corbusier was invited to design a new Catholic pilgrimage chapel in Ronchamp**, a small French town in the Vosges Mountains near the Swiss border …”；“the chapel called **Chapelle Notre-Dame-du-Haut** near Ronchamp … **built from 1950-55, whose inclined walls and curved roof contours have variously been likened to a ship's sails or a nun's cowl.**” |
| ② | WikiArquitectura（建筑百科·数据页，**中—强权威·建筑百科**） | `https://en.wikiarquitectura.com/building/notre-dame-du-haut/` | ✅ Chapel of Notre Dame du Haut - Data, Photos & Plans - WikiArquitectura | **200**（660,226 B 原始；正文约 10,738 字） | “**Architect Le Corbusier Built in 1950 1955 Height 27m Location Ronchamp, Haute-Saône, France**”；“The Franco-Swiss architect Le Corbusier, in 1950 he received the contract to build a new chapel to replace the center of pilgrimage of **Notre-Dame-du-Haut in Ronchamp**”。 |

**三要素对位**：名称＝Chapelle Notre-Dame du Haut（①②一致）；地点＝Ronchamp, Haute-Saône, France（②直书、①“Ronchamp”+“Vosges Mountains”）；设计者＝Le Corbusier（①②一致）；年份＝**1950–55（①②一致）**，与任务 1950–1955 相符。
**独立性说明**：TheArtStory（艺术史教育机构）与 WikiArquitectura（建筑百科·数据页）为两个不同机构，均 HTTP 200、正文直证，可作独立双源。
**手法贴合度（诚实标注）**：朗香教堂以**厚重弯曲壳体（incline walls / curved roof）与大面积白墙上的窗洞、内部明暗**形成强烈体量与光影对比（①“inclined walls and curved roof contours … likened to a ship's sails or a nun's cowl”），契合“以形状/明暗差异突出主体”的对比手法。**权威级提示**：本环境未取得 Fondation Le Corbusier 官方作品页——站内检索无直链（`/en/work-architecture/` 404、`sitemap.xml` 无 ronchamp 条目，暂判官方页未暴露直链），故本条双源均为“艺术史教育 + 建筑百科（中—强）”，无官方一级源。

### 2.5 `geometry-symmetry`（几何与对称）→ **圆厅别墅 Villa La Rotonda（维琴察，Andrea Palladio，1567 起）**

- **名称**：Villa La Rotonda（圆厅别墅；又名 Villa Almerico Capra “La Rotonda”）
- **地点**：意大利 · 维琴察（Vicenza, Italy；城墙外约四分之一英里的山丘）
- **设计者**：**Andrea Palladio（安德烈亚·帕拉第奥）**
- **年份**：**1567–1570**（源② WikiArquitectura “Built in 1567 1570”；源① 官方记其著作《建筑四书》1570 出版、谈此宅；任务“1567 起”取②起建年）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验；官方页以 web_fetch 直读） |
| --- | --- | --- | --- | --- | --- |
| ① | Villa La Rotonda 官方（**强权威·官方建筑官网**） | `https://www.villalarotonda.it/en/villa/` | Villa - Villa La Rotonda di Andrea Palladio | **200（web_fetch 直读；本地 urllib TLS 握手失败）** | “**The same Andrea Palladio will talk about his project the rotonda in his second book of the 'Quattro libri dell'Architettura, published in 1570**”；“**the square plan of the villa was rotated 45 degrees with the angles orientated towards the four cardinal points**”；“the same idea of a **circular building** … derived from the pantheon of Rome, the **pronai with tympanum and columns** are inspired by ancient temples”。 |
| ② | WikiArquitectura（建筑百科·数据页，**中—强权威·建筑百科**） | `https://en.wikiarquitectura.com/building/villa-rotonda/` | ✅ Villa Rotonda - Data, Photos & Plans - WikiArquitectura | **200**（311,164 B 原始；正文约 11,599 字） | “**Architect Adrea Palladio Built in 1567 1570 Location Vicenza, Italy**”；“Your name, **Rotunda (round), derives from its plan, a perfect circle inside a square, forming a fully symmetrical composition**, with a traditional temple gate in front of each facade.”；“… so we can talk about a **double symmetry**.” |

**三要素对位**：名称＝Villa La Rotonda / Villa Almerico Capra（①②一致）；地点＝Vicenza, Italy（②直书、①官方为维琴察该宅官网）；设计者＝Andrea Palladio（①②一致）；年份＝**1567–1570（②）**，任务“1567 起”取②起建年（①以其 1570 著作旁证）。
**独立性说明**：Villa La Rotonda 官方馆舍网站与 WikiArquitectura（建筑百科）为两个不同机构，均可读且正文直证，可作独立双源。
**手法贴合度（诚实标注）**：圆厅别墅“**正方平面内接完美圆形、四面相同神庙式门廊、按 45° 转位朝四向**”是“以基本几何形与对称组织画面/体量”的原型——②直书 “perfect circle inside a square … fully symmetrical … double symmetry”，①直书 “square plan … rotated 45 degrees … circular building … pronai with tympanum and columns”，**几何+对称两源双证，贴合度极高**。官方页因本机 TLS 被阻，经 host `web_fetch` 服务端 200 直读并逐句核对。

### 2.6 `negative-space`（负空间）→ **龙安寺石庭 Ryōan-ji（京都，约15世纪）**

- **名称**：Ryōan-ji / 龍安寺（大云山 龙安寺；枯山水石庭）
- **地点**：日本 · 京都 · 右京区（13, Ryoanji Goryonoshitacho, Ukyo-ku, Kyoto）
- **设计者**：**不详（史料未确证；传统上或归于相阿弥/细川胜元，二源均未直书确定设计者）**
- **年份**：**约 15 世纪**（源② 记“converted into a Zen temple in 1450”，即室町中期；石庭具体年代无确切定论）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | 龍安寺 官方（临济宗妙心寺派寺院官网，**强权威·官方寺院**） | `http://www.ryoanji.jp/smph/eng/` | 大雲山　龍安寺｜Ryoanji | **200**（6,427 B 原始；正文约 619 字） | “**大雲山　龍安寺｜Ryoanji**”；“**13, Ryoanji Goryonoshitacho, Ukyo-ku Kyoto-shi, Kyoto, 616-8001, Japan**”。（官网仅营业/地址信息，无年代与设计者正文） |
| ② | Japan Guide（旅行指南，**中权威**） | `https://www.japan-guide.com/e/e3909.html` | Ryoanji Temple - Kyoto Travel | **200**（255,033 B 原始；正文约 29,092 字） | “Ryōanji Temple (龍安寺, Ryōanji) **is the site of Japan's most famous rock garden.**”；“Originally an aristocrat's villa during the Heian Period, **the site was converted into a Zen temple in 1450** and belongs to the Myoshinji school of the Rinzai sect of Zen Buddhism …”。 |

**三要素对位**：名称＝Ryōan-ji / 龍安寺（①②一致）；地点＝京都右京区（①官方地址、②“Kyoto”）；设计者＝**不详/未确证**（两源均未直书确定设计者，史实上石庭作者无定论）；年份＝**约 15 世纪**（②直书 1450 转为禅寺，任务“约15世纪”相符）。
**独立性说明**：龍安寺官方（寺院）与 Japan Guide（旅行指南）为两个不同机构，均 HTTP 200、正文直证，**达“双机构”**；但——**权威级偏低、且仅覆盖名称/地点/年份(1450)/“著名石庭”，未覆盖“确定设计者”**（详见第六节诚实标注）。
**手法贴合度（诚实标注）**：龙安寺方丈前庭以**白砂铺地、仅置十五块石组**，大面积“空”与少量石组构成“以负空间/留白反衬主体”的东方原型——②直书其为 “Japan's most famous rock garden”。**局限**：石庭之“负空间”评述属艺术史通识，所选两源未直书 “negative space” 术语；且设计者不详、年代仅作约 15 世纪。若 lead 要求“博物馆/大学级双源 + 确定设计者”，本条应判**“设计者不可得、强权威双源不足”**并考虑换例（见第六节）。

---

## 三、汇总（各条可得源数）

| 条目（中文题名 / id） | 具名实例（名称、地点、设计者、年份） | 采用的两条独立主源（机构） | 独立机构数 | 达“双独立源” | 四要素源内直证（名称/地点/设计者/年份） | 权威级 / 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 灭点 / `vanishing-point` | 《雅典学院》（梵蒂冈，Raphael，1509–1511） | Vatican Museums 官方 ＋ Web Gallery of Art | 2 | ✅（另 TheArtStory 第三源） | 名称✅ 地点✅(Vatican) 设计者✅ 年份✅(1509 / 1509-11) | 强（官方＋艺术史库）；“灭点”字样主源未直书，属通识定性 |
| 空气透视 / `aerial-perspective` | 《蒙娜丽莎》（巴黎卢浮宫，Leonardo，约1503–1519） | Musée du Louvre 官方 ＋ Web Gallery of Art | 2 | ✅（另 TheArtStory 第三源） | 名称✅ 地点✅(Louvre, Salle des États) 设计者✅ 年份：1503-5 / 1503-19 ✅ | 强（官方＋艺术史库）；年份口径差须并列 |
| 节奏与重复 / `rhythm-repetition` | 罗马斗兽场（罗马，Vespasian/Titus，约70–80） | University of Chicago ＋ University of Washington | 2 | ✅（另 Britannica 第三源，web_fetch 200） | 名称✅ 地点✅(Rome) 营造者✅ 年份✅(70-80 / 80 CE) | 强—中（两大学站；UW 为学生署名专文）；重复拱廊两源直证 |
| 对比 / `contrast-principle` | 朗香教堂 Notre-Dame du Haut（Ronchamp，Le Corbusier，1950–1955） | TheArtStory ＋ WikiArquitectura | 2 | ✅ | 名称✅ 地点✅(Ronchamp) 设计者✅ 年份✅(1950-55) | 中—强（教育＋建筑百科）；**无官方一级源** |
| 几何与对称 / `geometry-symmetry` | 圆厅别墅 Villa La Rotonda（维琴察，Palladio，1567 起） | Villa La Rotonda 官方 ＋ WikiArquitectura | 2 | ✅ | 名称✅ 地点✅(Vicenza) 设计者✅ 年份✅(1567-1570) | 强（官方＋建筑百科）；几何/对称双证 |
| 负空间 / `negative-space` | 龙安寺石庭 Ryōan-ji（京都，约15世纪） | 龍安寺 官方 ＋ Japan Guide | 2（机构） | ⚠️ 达标但**权威级偏低**；**设计者不详、无确定设计者直证** | 名称✅ 地点✅(Kyoto) 设计者：**不详(未确证)** 年份：1450/约15世纪 ✅ | **中—弱**（官方寺院仅名称地址＋旅行指南年份）；术语“negative space”主源未直书 |

- **6 条均凑齐“两个不同机构来源（HTTP 200、正文直证）”；无“完全单源/不可得”条目，故未整体替换对象。** 例外与提示：`contrast-principle` 无官方一级源（中—强）；`negative-space` 双源权威级偏低且**设计者不可得**（仅官方寺院＋旅行指南，博物馆/大学/UNESCO 级第二源本轮不可得）。
- **回执**：见第七节逐条子串校验（urllib 直抓 13 个 URL 的关键句全部 FOUND；另 `web_fetch` 直读 2 个 URL：Villa Rotonda 官方页、Britannica 斗兽场页，均 HTTP 200 且正文逐句核对）。

---

## 四、失败 / 未采用候选（备核，均不作证据）

| URL / 站点 | 结果 | 说明 |
| --- | --- | --- |
| `https://collections.louvre.fr/en/ark:/53355/cl010062370`（卢浮宫藏品库） | **HTTP 403** | 藏品库反爬；改用卢浮宫 `louvre.fr` 专题页（200） |
| `https://www.louvre.fr/en/explore/the-palace/a-mona-lisa` | **HTTP 403** | 该路径被拦；改用 `/from-the-mona-lisa-to-the-wedding-feast-at-cana`（200） |
| `https://colosseo.it/en/area/the-colosseum/`（斗兽场考古公园官方） | **SSL 握手失败 / 连接超时** | 本机与官方站 443 不通，未取得官方一级源 |
| `https://whc.unesco.org/en/list/91`、`/712`、`/688`（UNESCO） | **HTTP 403（Cloudflare “Just a moment”）** | 三处 UNESCO 页面本机与 web_fetch 均被拦 |
| `https://www.britannica.com/topic/Villa-Rotonda`（→ `/place/Villa-Rotonda`） | **HTTP 403 / Cloudflare** | Britannica 该条被拦，Villa Rotonda 改走官方馆舍页 |
| `https://www.britannica.com/topic/Ryoan-ji`、`/topic/Ryoanji`、`/topic/Ryōan-ji` | **HTTP 404 / 403** | Britannica 无龙安寺独立条目 |
| `https://www.metmuseum.org/toah/hd/kare/hd_kare.htm`（大都会 Kare-sansui 论文） | **HTTP 429 Too Many Requests**（多次重试仍 429） | 本拟作龙安寺博物馆级第二源，未获 |
| `https://smarthistory.org/ryoan-ji/`、`https://www.worldhistory.org/Colosseum/` | **HTTP 403** | 艺术史教育/百科首选被反爬 |
| `https://www.khanacademy.org/…/colosseum` | **HTTP 200 但 “Client Challenge” 无正文** | 反爬挑战页，无可抽取正文 |
| `https://www.greatbuildings.com/buildings/Villa_Rotonda.html` | **HTTP 403** | 建筑数据库被拦 |
| `https://www.fondationlecorbusier.fr/en/work-architecture/achievements-notre-dame-du-haut-ronchamp-france-1950-1955/` | **HTTP 404**；`/en/work-architecture/` 亦 404；`sitemap.xml` 无 ronchamp 条目 | 朗香无官方一级源，双源降为“教育＋建筑百科” |
| `https://www.villalarotonda.it/en/`（urllib 直连） | **读取超时 / curl 连接被断**（TLS） | 本机 urllib 不通；**改用 host `web_fetch` 服务端 200**（官方页仍可用） |
| `https://www.ryoanji.jp`（https） | **SSL WRONG_VERSION_NUMBER** | 官方站 https 异常；**改用 http:// 明路 200** |
| `https://www.palladiomuseum.org/en/`（Palladio Museum 官网） | **200 但无 Villa Rotonda 专页** | 站内仅课程/展览，未找到圆厅别墅页，未作源 |
| `https://www.italythisway.com/places/villa-rotonda.php` | **SSL 握手超时** | 未获 |
| `https://jgarden.org`（日式庭园数据库） | **200 但 “Coming Soon”** | 站点已下线，弃用 |

---

## 五、证据来源 URL 一览（本轮均已实际打开核验，HTTP 见行）

| # | URL | HTTP（字节） | 标题 / 机构 | 支撑 |
| --- | --- | --- | --- | --- |
| 1 | `https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/stanze-di-raffaello/stanza-della-segnatura.html` | 200（46,490） | Room of the Segnatura · Vatican Museums（官方） | vanishing-point 源① |
| 2 | `https://www.wga.hu/html_m/r/raphael/4stanze/1segnatu/1/index.html` | 200（19,727） | Stanza della Segnatura: The School of Athens · Web Gallery of Art | vanishing-point 源② |
| 3 | `https://www.theartstory.org/artist/raphael/` | 200（163,680） | Raphael · TheArtStory | vanishing-point 第三源 |
| 4 | `https://www.louvre.fr/en/explore/the-palace/from-the-mona-lisa-to-the-wedding-feast-at-cana` | 200（313,943） | From the 'Mona Lisa' … - The Salle des États · Musée du Louvre（官方） | aerial-perspective 源① |
| 5 | `https://www.wga.hu/html_m/l/leonardo/04/1monali.html` | 200（9,940） | Mona Lisa (La Gioconda) · Web Gallery of Art | aerial-perspective 源② |
| 6 | `https://www.theartstory.org/artist/da-vinci-leonardo/` | 200（179,838） | Leonardo da Vinci · TheArtStory | aerial-perspective 第三源 |
| 7 | `https://penelope.uchicago.edu/~grout/encyclopaedia_romana/romanurbs/colosseum.html` | 200（8,563） | Colosseum · University of Chicago（Encyclopaedia Romana） | rhythm-repetition 源① |
| 8 | `https://depts.washington.edu/hrome/Authors/jimkuo2/IlColosseo/pub_zbarticle_view_printable.html` | 200（68,090） | The Colosseum: Power, Brilliance, and Brutality · University of Washington | rhythm-repetition 源② |
| 9 | `https://www.britannica.com/topic/Colosseum` | 200（web_fetch 直读） | Colosseum · Encyclopaedia Britannica | rhythm-repetition 第三源（年代） |
| 10 | `https://www.theartstory.org/artist/le-corbusier/` | 200（164,920） | Le Corbusier · TheArtStory | contrast-principle 源① |
| 11 | `https://en.wikiarquitectura.com/building/notre-dame-du-haut/` | 200（660,226） | Chapel of Notre Dame du Haut · WikiArquitectura | contrast-principle 源② |
| 12 | `https://www.villalarotonda.it/en/villa/` | 200（web_fetch 直读） | Villa - Villa La Rotonda di Andrea Palladio（官方） | geometry-symmetry 源① |
| 13 | `https://en.wikiarquitectura.com/building/villa-rotonda/` | 200（311,164） | Villa Rotonda · WikiArquitectura | geometry-symmetry 源② |
| 14 | `http://www.ryoanji.jp/smph/eng/` | 200（6,427） | 大雲山　龍安寺｜Ryoanji（官方寺院） | negative-space 源① |
| 15 | `https://www.japan-guide.com/e/e3909.html` | 200（255,033） | Ryoanji Temple - Kyoto Travel · Japan Guide | negative-space 源② |

---

## 六、落地提醒与诚实标注（只读，不改数据）

- **可用均为建议**：须先把主源以 `verified=true` 登记进 `data/sources.json`，再改写对应条目的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年份”），同步 `pending_notes`/「待核实」，按需更新 `coverage.json` 源数，并复跑 `tools/check.py`。**本报告未修改任何条目数据或其它文件（本文件为唯一产出）。**
- **年份口径差异（据实并列，不强归）**：
  - `vanishing-point`：《雅典学院》任务 1509–1511；WGA 记 **1509**；TheArtStory 记 **1509-11**。落地可写“1509–1511（1509 起）”。
  - `aerial-perspective`：《蒙娜丽莎》任务约 1503–1519；WGA 记 **1503-5 / 1503-05（各家 1503–1513）**；TheArtStory 记 **1503-19**。落地宜写“约1503–1519（创作绵延至晚期；WGA 取 1503–5）”。
  - `rhythm-repetition`：斗兽场任务约 70–80；UChicago 记 **AD 70–80**；UW 记 **80 CE** 落成；Britannica 记 “70–72 ce 始建、80 ce 落成”。无冲突。
  - `contrast-principle`：朗香 1950–1955；①②一致。无差异。
  - `geometry-symmetry`：圆厅别墅任务“1567 起”；WikiArq 记 **1567–1570**；官方页记其《建筑四书》**1570** 出版。落地可写“1567 起建、1570 见于《建筑四书》”。
  - `negative-space`：龙安寺任务“约15世纪”；Japan Guide 记 **1450 转禅寺**；石庭具体年代无确切定论。落地可写“约 15 世纪（1450 年前后，年代无定论）”。
- **权威级提示**：
  - `contrast-principle`：双源为 TheArtStory ＋ WikiArquitectura（中—强），**无官方/博物馆一级源**（Fondation Le Corbusier 官方页未暴露直链、sitemap 无 ronchamp 条目；本机直连亦受阻）。如 lead 要求“至少一官方源”，此条需另寻或标“权威级偏低”。
  - `negative-space`：双源为 龍安寺官方（仅名称/地址/营业信息）＋ Japan Guide（旅行指南，中权威）。**设计者不可得、术语 “negative space” 主源未直书、年份仅 1450 直证。** 若为“双强源＋设计者”而必须换例，建议改取**马远《寒江独钓图》（东京国立博物馆藏，南宋，大面积留白）**一类“东方留白”实例作候选，但该候选的**双独立强源本轮未抓取、须另行核验后方可用**，此处不作既成证据。
  - 其余四条（灭点/空气透视/节奏重复/几何对称）均含至少一条官方/大学/官方建筑官网强权威源；节奏重复条 UW 为学生署名专文，建议与 UChicago 并记时注“大学课程专文（学生署名）”。
- **术语贴合度提示**：
  - `vanishing-point`：所选两主源未直书 “vanishing point”；《雅典学院》中央单一灭点为艺术史通识，落笔“灭点”定性宜注明依据为 TheArtStory 的 “three-point perspective / figures diminish in proportion” 透视描写。
  - `negative-space`：石庭“负空间”亦属通识评述，主源未直书该术语。
  - `aerial-perspective`：① 卢浮宫直书 “painted against a distant landscape”＋“sfumato”，② WGA 直书 “visionary, mountainous landscape”，贴合空气透视。
- **名词一致性**：六条 `sections.实例` 现均为“类型性描述/不适用”，本轮各给一具名实例可直接替换为“名称＋地点＋设计者＋年份”，并同步把 `needs_verification` 按证据情况调整（`contrast-principle`、`negative-space` 建议保留 `needs_verification=true` 或在「待核实」注明“设计者不详/无官方一级源”）。

---

## 七、回执（逐条 `norm` 子串校验，均 FOUND）

> 方法：`norm()` 统一弯/直引号、破折号、不间断空格、NFKC、去多余空白后小写；`norm(quote) in norm(page text)` 判定。urllib 直抓 13 个 URL；`web_fetch` 直读 2 个 URL（Villa Rotonda 官方、Britannica 斗兽场）。

- **灭点《雅典学院》**：Vatican 2/2（“contains Raphael's most famous frescoes”、“School of Athens”）；WGA 3/3（题名 “by RAFFAELLO”、“The School of Athens 1509 Fresco”、“Stanza della Segnatura, Palazzi Pontifici, Vatican”）；TheArtStory 2/2（“Fresco - Vatican City 1509-11 The School of Athens”、“three-point perspective”）。
- **空气透视《蒙娜丽莎》**：Louvre 4/4（“Portrait of Lisa Gherardini … known as the Mona Lisa”、“Room 711”、“Painted against a distant landscape”、“sfumato technique, based on the use of glazes”）；WGA 3/3（“by LEONARDO da Vinci”、“Oil on panel, 77 x 53 cm”、“most widely accepted being 1503-05”）；TheArtStory 2/2（“the Mona Lisa (1503-19)”、“world's most famous portrait, the Mona Lisa”）。
- **节奏重复·斗兽场**：UChicago 3/3（“Begun by Vespasian in AD 70”、“completed and dedicated by his son Titus in AD 80”、“There are four arcaded stories, the first three each have eighty arches …”）；UW 3/3（“Each of the Colosseum's three stories has eighty arches.”、“dedicated … in 80 CE”、“began construction of the Colosseum”）。
- **对比·朗香**：TheArtStory 3/3（“In 1950, Le Corbusier was invited to design a new Catholic pilgrimage chapel in Ronchamp”、“built from 1950-55”、“Chapelle Notre-Dame-du-Haut”）；WikiArquitectura 3/3（“Architect Le Corbusier Built in 1950 1955”、“Built in 1950 1955”、“Location Ronchamp”/“Height 27m”）。
- **几何对称·圆厅别墅**：WikiArquitectura 3/3（“Architect Adrea Palladio Built in 1567 1570”、“Location Vicenza, Italy”、“a perfect circle inside a square, forming a fully symmetrical composition”）；Villa Rotonda 官方 **web_fetch 200 直读**，正文可见并核对（“The same Andrea Palladio will talk about his project the rotonda … published in 1570”、“the square plan of the villa was rotated 45 degrees with the angles orientated towards the four cardinal points”）。
- **负空间·龙安寺**：龍安寺官方 2/2（“Ryoanji”、“13, Ryoanji Goryonoshitacho, Ukyo-ku Kyoto-shi, Kyoto”）；Japan Guide 2/2（“is the site of Japan's most famous rock garden”、“the site was converted into a Zen temple in 1450”）。
- **Britannica 斗兽场（web_fetch 200 直读）**：“Construction of the Colosseum began under the Roman emperor Vespasian between 70 and 72 ce. The completed structure was dedicated in 80 ce by Titus.”（正文可见核对）。

**结论**：本轮 6 条均已给出“名称/地点/设计者/年份”具名实例，各配两条不同机构来源（均 HTTP 200），关键句全部经 `norm` 子串回验通过；`negative-space` 存“设计者不详＋第二源权威级偏低”的诚实限制，`contrast-principle` 无官方一级源——二者已在第六节明示，供 lead 决定是否保留、补强或换例。
